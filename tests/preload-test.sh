#!/usr/bin/env bash
# Live test: load this checkout as a plugin in a fresh, headless Claude Code run,
# dispatch the Azzam agent once, and confirm from the debug log that every skill
# in its `skills` field was preloaded.
#
# Needs: the `claude` CLI signed in, and azmx-brand, frontend-design and
# superpowers installed (see README). Costs one short Haiku run.
#
# Usage: tests/preload-test.sh [model]      # default model: haiku
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
model="${1:-haiku}"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

expected=(superpowers:using-superpowers azmx-brand azzam-writing)

if ! command -v claude >/dev/null 2>&1; then
  echo "FAIL  the claude CLI is not on PATH"; exit 1
fi

# Run from an empty folder so only the plugin's agent (azzam:azzam) exists.
(cd "$work" && claude -p --model "$model" --plugin-dir "$repo" --debug-file "$work/debug.txt" \
  "Use the Agent tool once with subagent_type azzam:azzam and this exact prompt: 'Wiring test. Call no tools. Reply with only the name of every skill whose full SKILL.md text you can see in your context, one per line.' Then print the subagent's reply verbatim and stop." \
  </dev/null >"$work/out.txt" 2>&1) || { echo "FAIL  claude exited with an error:"; cat "$work/out.txt"; exit 1; }

status=0
for skill in "${expected[@]}"; do
  if grep -qF "[Agent: azzam:azzam] Preloaded skill '$skill'" "$work/debug.txt"; then
    echo "PASS  preloaded $skill"
  else
    echo "FAIL  did not preload $skill"; status=1
  fi
done
if grep -F "[Agent: azzam:azzam] Warning: Skill" "$work/debug.txt"; then
  echo "FAIL  Claude Code warned about a skill (above)"; status=1
fi

echo
echo "Agent reply:"
cat "$work/out.txt"
exit "$status"
