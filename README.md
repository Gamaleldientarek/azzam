# Azzam (عزّام)

[![Tests](https://github.com/Gamaleldientarek/azzam/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/Gamaleldientarek/azzam/actions/workflows/check.yml)
[![Release](https://github.com/Gamaleldientarek/azzam/actions/workflows/release.yml/badge.svg)](https://github.com/Gamaleldientarek/azzam/releases)

## Meet AZZAM!

Azzam is AZM X's expert agent for Claude Code and its Arabic UX writer. Its standard is the best Arabic UX writing in the Middle East, with Saudi Arabic as home ground: a Saudi reader trusts what Azzam writes on the first read, because it sounds written in Riyadh for them, not translated for them.

Azzam writes for any website AZM X writes for, not only azmx.sa: the AZM X brands' sites and client sites too. Ask it for interface copy in any product, website copy, SEO articles and service pages, metadata and alt text, pages written to be quoted by AI assistants, newsletters and every email AZM X sends to people, briefs from the SEO radar, reviews of a draft, or LinkedIn copy cut from an article. It writes Arabic first, then English as an original.

Azzam knows AZM X's voice, the government and enterprise accounts it writes for, and the newsletters and emails AZM X already sends. It writes only from the facts of the site it writes for, and hands finished copy to that site's owner. Jimmy publishes and sends for AZM X.

## Skills

Azzam works through skills, one craft each.

| Skill | What it does |
|---|---|
| **Azzam Writing** (`azzam-writing`) | The best Arabic UX writing for the Middle East, Saudi Arabic first: register, Saudi vocabulary, gender-neutral address, spelling, Saudi formats and plurals. Also Arabic-first UX writing and SEO content for azmx.sa and any other website AZM X writes for: buttons, forms, errors and page sections; articles, service and location pages; titles, descriptions and alt text; content written to be quoted by AI assistants; newsletters, campaign and report emails, and confirmation, welcome and thank-you emails; briefs from the SEO radar; reviews of drafts. |

Azzam also works with four skills from outside this plugin. You install them once (see Install).

| Skill | When Azzam uses it | How it loads |
|---|---|---|
| **Using Superpowers** (`superpowers:using-superpowers`) | At the start of every task: check which skill applies before acting | Preloaded through the agent's `skills` field |
| **AZM X Brand** (`azmx-brand`) | Any AZM X copy, voice or visual work | Preloaded through the agent's `skills` field |
| **Frontend Design** (`frontend-design:frontend-design`) | When the work touches a page layout, or Azzam produces HTML or a visual, such as an article's example image | Loaded with the Skill tool when needed; `azmx-brand` wins where they disagree |
| **Avoid AI Writing** (`avoid-ai-writing:avoid-ai-writing`) | Before any piece passes the gate: the AI-writing audit on its English text. The Arabic audit is by hand, from `references/ai-writing-audit.md` | Loaded with the Skill tool at the audit |

If one of them is missing, Claude Code skips it and Azzam runs without it, so install all four.

## Government and enterprise accounts

Azzam has studied how AZM X speaks to its two buying motions, and it picks the motion and the persona before the first line of any piece.

| Account | Who reads | What Azzam applies |
|---|---|---|
| **Government (B2G)** | Directors and heads who need a low-risk path to modernising public services, and leads who need proof that modern, agile practice works inside an agency | Modern Standard Arabic, warm and direct, because a citizen has something at stake. The Digital Government Authority's Platforms Code for components and naming. One word for the person served (the beneficiary) and one name per service, held across the platform, the SMS, the email and the call-centre script. Consent, privacy and PDPL text is written with its legal owner; Azzam makes the approved wording readable without changing its meaning. Official Saudi sources, such as the Digital Government Authority, GASTAT, SDAIA and the Vision 2030 programmes, for any claim. |
| **Enterprise (B2B)** | Executives who approve budgets and need a partner who holds scope and schedule, product and UX heads who need a better team workflow, and operations leads who need one source of truth | Modern Standard Arabic written for a screen that several readers sign off. One word for the client, held across the product. The persona's pain point and core message from the AZM X audience map, applied before drafting. |

The study lives in two places: the personas and core messages in `azmx-brand` (`references/audiences-and-messaging.md`), and the register, vocabulary and government rules in this plugin (`skills/azzam-writing/references/saudi-arabic-ux.md`, sections 1, 2 and 11). AZM X's own facts, figures and client names stay in the website repository's `docs/content/`, never in this repository.

## Newsletters and emails

Azzam has studied every newsletter template and every email AZM X sends to people: the monthly internal newsletter, occasion greetings, the annual report announcement, the report emails, the website's confirmation and thank-you emails, and the Anatomi newsletter, as built in their projects and as sent through Brevo.

What it learned is in `skills/azzam-writing/references/email-newsletters.md`: the voice for each email type, the block order, subject lines and preheaders, Arabic and English in one email, right-to-left details, personalisation, calls to action, alt text, trust wording, the compact footer, lengths, an email gate and the draft layout. Two rules come first: nothing is sent without Jimmy's yes to a test send, and Arabic the content team supplies is never changed without asking. Where the brand rules and the emails already sent disagree (emoji, em dashes, exclamation marks, sender names), the reference lists the open ruling for Jimmy.

AZM X's own email facts (the series name, standing lines, senders, lists, templates and the subjects already sent) stay in the website repository, in `docs/content/email-bank.md`, with the full evidence in `docs/content/email-study-2026-10-23.md`.

## Install

You need access to this private repository (ask Jimmy) and a GitHub sign-in on your machine (`gh auth login`).

1. Install the AZM X brand skill, which holds the voice, the personas and the content prompts Azzam uses:

   ```bash
   git clone https://github.com/Gamaleldientarek/azmx-brand ~/.claude/skills/azmx-brand
   ```

2. In Claude Code, install Frontend Design and Superpowers from Anthropic's official marketplace, `claude-plugins-official`. Azzam declares both as dependencies, so step 3 installs them too when that marketplace is on your machine; installing them first is the sure way. If `/plugin install` cannot find the marketplace, run `/plugin marketplace add anthropics/claude-plugins-official` first.

   ```
   /plugin install frontend-design@claude-plugins-official
   /plugin install superpowers@claude-plugins-official
   ```

   Then add the marketplace that holds Avoid AI Writing, and install it. Azzam uses it for the AI-writing audit on English text:

   ```
   /plugin marketplace add conorbronsdon/avoid-ai-writing
   /plugin install avoid-ai-writing@conorbronsdon-skills
   ```

3. Then install Azzam:

   ```
   /plugin marketplace add Gamaleldientarek/azzam
   /plugin install azzam@azzam
   ```

4. Restart Claude Code.

## Use

For AZM X work, open the `azmx-framer-website` repository as your working folder. It holds AZM X's facts (`docs/content/`: string bank, evidence bank, entity facts) and the drafts folder Azzam writes to. For another website, open that site's project and give Azzam its facts and fields; it asks for them before the first line.

Then ask in plain words, for example "Azzam, write the Arabic for the contact form errors", "Azzam, draft an article on Arabic UI design" or "Azzam, write this month's newsletter", or run `/azzam:azzam-writing`.

## How Azzam works

- **Arabic first.** Native Modern Standard Arabic for a Saudi reader, then English written as an original.
- **Facts only from the site's evidence.** AZM X's evidence bank for AZM X; a brand's or a client's own facts for their site. Anything missing goes to its owner as an open fact.
- **A named expert signs.** Azzam drafts the full text; an AZM X expert adds a first-hand passage, edits and signs.
- **Never writes into a live site, a CMS or Brevo, and never sends or publishes.** On azmx.sa, approved copy goes in through the `azmx-site` plugin; Jimmy publishes and sends.

## Tests and releases

Two tests guard Azzam:

- **Static check**, run by GitHub on every push and pull request (`.github/workflows/check.yml`), and by you before any commit: the version matches in both manifests and the changelog, the agent preloads its three skills and names Frontend Design, every reference is linked, the README covers install, and no key, tracking ID or AZM X fact file has slipped in.

  ```bash
  python3 tests/check.py
  python3 tests/check.py --website "<path to azmx-framer-website>"   # also checks the website copy is in sync
  ```

- **Live preload test**, run by hand on a Mac with Claude Code signed in: it loads this checkout as a plugin, dispatches Azzam once on Haiku, and reads Claude Code's debug log to prove the three skills were preloaded.

  ```bash
  tests/preload-test.sh
  ```

To release: bump the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, add its section to `CHANGELOG.md`, commit, then run `claude plugin tag --push`. It validates the plugin and pushes a tag in Claude Code's format, `azzam--vX.Y.Z`; GitHub checks the tag against the version and publishes the release with that changelog section as its notes (`.github/workflows/release.yml`). Teammates update with `claude plugin update azzam@azzam`, then restart Claude Code.

## Changes

Edit through a pull request; Jimmy approves. A new craft is a new skill folder named `azzam-<craft>`, added to the table in `agents/azzam.md`. Run both tests before you ask for a release.

Private to AZM X. Not for redistribution.
