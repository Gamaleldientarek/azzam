#!/usr/bin/env python3
"""Static checks for the Azzam plugin. Standard library only.

Usage:
  python3 tests/check.py                       # check this repository
  python3 tests/check.py --tag azzam--v0.3.0   # also check a release tag matches the version
  python3 tests/check.py --website <path>      # also check the website repository's copy is in sync

Exit code 0 when every check passes, 1 otherwise.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Skills the agent must preload through its `skills` frontmatter field.
PRELOADED = ["superpowers:using-superpowers", "azmx-brand", "azzam-writing"]
# Skills the agent body must tell Azzam to load on demand with the Skill tool.
ON_DEMAND = ["frontend-design:frontend-design"]
# The one line the website copy of the agent may differ by.
PLUGIN_SKILLS_LINE = "Jimmy adds new skills as `azzam-<craft>` in this plugin's `skills/` folder."
WEBSITE_SKILLS_LINE = "Jimmy adds new skills as `azzam-<craft>` in `.claude/skills/`."

SECRET_PATTERNS = [
    (r"GTM-[A-Z0-9]{5,}", "Tag Manager ID"),
    (r"\bG-[A-Z0-9]{8,}\b", "Analytics ID"),
    (r"sk-ant-[A-Za-z0-9_-]{10,}", "Anthropic key"),
    (r"\bghp_[A-Za-z0-9]{20,}", "GitHub token"),
    (r"\bxkeysib-[A-Za-z0-9-]{20,}", "Brevo key"),
    (r"\bAKIA[0-9A-Z]{16}\b", "AWS key"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key"),
]
# AZM X's facts live in the website repository's docs/content/, never here.
FACT_FILES = ["evidence-bank.md", "string-bank.md", "entity-facts.md"]

failures = []


def check(ok, message):
    print(("PASS  " if ok else "FAIL  ") + message)
    if not ok:
        failures.append(message)


def frontmatter(path):
    """Parse simple YAML frontmatter: `key: value`, `key: [a, b]` and block lists."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    data, key = {}, None
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        item = re.match(r"^\s+-\s+(.*)$", line)
        if item and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(item.group(1).strip().strip("'\""))
            continue
        pair = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if pair:
            key, value = pair.group(1), pair.group(2).strip()
            if value.startswith("[") and value.endswith("]"):
                data[key] = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
            else:
                data[key] = value.strip("'\"") if value else []
    return data, text[end + 4:]


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        check(False, f"{path.relative_to(ROOT)} is valid JSON ({error})")
        return None


def check_manifests():
    plugin = read_json(ROOT / ".claude-plugin/plugin.json")
    market = read_json(ROOT / ".claude-plugin/marketplace.json")
    if plugin is None or market is None:
        return None
    version = plugin.get("version", "")
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), f"plugin.json version is semver ({version})")
    check(plugin.get("name") == "azzam", "plugin.json name is azzam")
    entries = [p for p in market.get("plugins", []) if p.get("name") == "azzam"]
    check(len(entries) == 1, "marketplace.json lists the azzam plugin once")
    if entries:
        check(entries[0].get("version") == version, "marketplace.json plugin version matches plugin.json")
        check(entries[0].get("source") == "./", "marketplace.json source is ./")
    check(market.get("metadata", {}).get("version") == version, "marketplace.json metadata version matches plugin.json")
    return version


def check_changelog(version):
    path = ROOT / "CHANGELOG.md"
    check(path.exists(), "CHANGELOG.md exists")
    if path.exists() and version:
        text = path.read_text(encoding="utf-8")
        check(re.search(rf"^## {re.escape(version)}\b", text, re.M) is not None, f"CHANGELOG.md has a section for {version}")


def check_agent():
    path = ROOT / "agents/azzam.md"
    check(path.exists(), "agents/azzam.md exists")
    if not path.exists():
        return
    meta, body = frontmatter(path)
    for field in ["name", "description", "model", "color"]:
        check(bool(meta.get(field)), f"agent frontmatter has {field}")
    check(meta.get("name") == "azzam", "agent name is azzam")
    skills = meta.get("skills") if isinstance(meta.get("skills"), list) else []
    for skill in PRELOADED:
        check(skill in skills, f"agent preloads {skill}")
    for skill in skills:
        if ":" not in skill and skill.startswith("azzam-"):
            check((ROOT / "skills" / skill / "SKILL.md").exists(), f"preloaded skill {skill} exists in skills/")
    for skill in ON_DEMAND:
        check(f"`{skill}`" in body, f"agent body names {skill} for on-demand loading")
    if "tools" in meta:
        tools = meta["tools"] if isinstance(meta["tools"], list) else [meta["tools"]]
        check("Skill" in tools or "*" in tools, "agent tools allow the Skill tool")
    check(PLUGIN_SKILLS_LINE in body, "agent points new skills at this plugin's skills/ folder")
    check(len(body) < 10000, f"agent body is under 10,000 characters ({len(body)})")


def check_skills():
    folders = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    check(len(folders) > 0, "skills/ holds at least one skill")
    for folder in folders:
        skill_md = folder / "SKILL.md"
        check(skill_md.exists(), f"{folder.name}/SKILL.md exists")
        if not skill_md.exists():
            continue
        meta, body = frontmatter(skill_md)
        check(meta.get("name") == folder.name, f"{folder.name}: frontmatter name matches its folder")
        check(bool(meta.get("description")), f"{folder.name}: has a description")
        linked = set(re.findall(r"\]\((references/[^)#\s]+)\)", body))
        for link in sorted(linked):
            check((folder / link).exists(), f"{folder.name}: link {link} resolves")
        for ref in sorted((folder / "references").glob("*.md")):
            rel = f"references/{ref.name}"
            check(rel in linked, f"{folder.name}: {rel} is linked from SKILL.md")


def check_readme():
    path = ROOT / "README.md"
    check(path.exists(), "README.md exists")
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for skill in PRELOADED + ON_DEMAND:
        check(f"`{skill}`" in text, f"README names {skill}")
    check("frontend-design@claude-plugins-official" in text, "README says how to install Frontend Design")
    check("superpowers@claude-plugins-official" in text, "README says how to install Superpowers")
    check("Meet AZZAM!" in text, "README opens with Meet AZZAM!")


def tracked_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".json", ".py", ".sh", ".yml", ".yaml", ".html"}:
            yield path


def check_privacy():
    for path in tracked_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT)
        for pattern, label in SECRET_PATTERNS:
            if re.search(pattern, text):
                check(False, f"{rel}: contains what looks like a {label}")
    for name in FACT_FILES:
        found = list(ROOT.rglob(name))
        check(not found, f"no copy of {name} in this repository (facts stay in the website repository)")


def check_tag(tag, version):
    # Claude Code's own convention (`claude plugin tag`): <plugin-name>--v<version>.
    check(tag == f"azzam--v{version}", f"release tag {tag} matches azzam--v{version}")


def check_dependencies():
    plugin = read_json(ROOT / ".claude-plugin/plugin.json") or {}
    market = read_json(ROOT / ".claude-plugin/marketplace.json") or {}
    deps = plugin.get("dependencies", [])
    names = [d if isinstance(d, str) else f"{d.get('name')}@{d.get('marketplace', 'azzam')}" for d in deps]
    allowed = market.get("allowCrossMarketplaceDependenciesOn", [])
    for skill in PRELOADED + ON_DEMAND:
        if ":" in skill:
            plugin_name = skill.split(":")[0]
            wanted = f"{plugin_name}@claude-plugins-official"
            check(wanted in names, f"plugin.json depends on {wanted}")
    for name in names:
        market_name = name.split("@")[1] if "@" in name else "azzam"
        if market_name != "azzam":
            check(market_name in allowed, f"marketplace.json allows dependencies from {market_name}")


def check_website(website):
    site = Path(website).expanduser()
    agent = site / ".claude/agents/azzam.md"
    check(agent.exists(), "website copy of the agent exists")
    if agent.exists():
        expected = (ROOT / "agents/azzam.md").read_text(encoding="utf-8").replace(PLUGIN_SKILLS_LINE, WEBSITE_SKILLS_LINE)
        check(agent.read_text(encoding="utf-8") == expected, "website agent matches the plugin agent except the skills-folder line")
    for src in sorted((ROOT / "skills").rglob("*")):
        if src.is_file():
            rel = src.relative_to(ROOT / "skills")
            dst = site / ".claude/skills" / rel
            check(dst.exists() and dst.read_bytes() == src.read_bytes(), f"website copy of skills/{rel} is identical")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tag", help="release tag to check against the plugin version, e.g. azzam--v0.3.0")
    parser.add_argument("--website", help="path to the website repository, to check its Azzam copy is in sync")
    args = parser.parse_args()

    version = check_manifests()
    check_dependencies()
    check_changelog(version)
    check_agent()
    check_skills()
    check_readme()
    check_privacy()
    if args.tag:
        check_tag(args.tag, version)
    if args.website:
        check_website(args.website)

    print()
    if failures:
        print(f"{len(failures)} check(s) failed.")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
