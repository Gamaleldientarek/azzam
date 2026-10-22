# Azzam (عزّام)

AZM X's expert agent for Claude Code. Azzam works through skills, one craft each.

| Skill | What it does |
|---|---|
| **Azzam Writing** (`azzam-writing`) | The best Arabic UX writing for the Middle East, Saudi Arabic first: register, Saudi vocabulary, gender-neutral address, spelling, Saudi formats and plurals. Also Arabic-first UX writing and SEO content for azmx.sa: buttons, forms, errors and page sections; articles, service and location pages; titles, descriptions and alt text; content written to be quoted by AI assistants; briefs from the SEO radar; reviews of drafts. |

## Install

You need access to this private repository (ask Jimmy) and a GitHub sign-in on your machine (`gh auth login`).

1. Install the AZM X brand skill, which holds the voice, the personas and the content prompts Azzam uses:

   ```bash
   git clone https://github.com/Gamaleldientarek/azmx-brand ~/.claude/skills/azmx-brand
   ```

2. In Claude Code:

   ```
   /plugin marketplace add Gamaleldientarek/azzam
   /plugin install azzam@azzam
   ```

3. Restart Claude Code.

## Use

Open the `azmx-framer-website` repository as your working folder. It holds AZM X's facts (`docs/content/`: string bank, evidence bank, entity facts) and the drafts folder Azzam writes to.

Then ask in plain words, for example "Azzam, write the Arabic for the contact form errors" or "Azzam, draft an article on Arabic UI design", or run `/azzam:azzam-writing`.

## How Azzam works

- **Arabic first.** Native Modern Standard Arabic for a Saudi reader, then English written as an original.
- **Facts only from the evidence bank.** Anything missing goes to its owner as an open fact.
- **A named expert signs.** Azzam drafts the full text; an AZM X expert adds a first-hand passage, edits and signs.
- **Never touches Framer, never publishes.** Approved copy goes to the site through the `azmx-site` plugin; Jimmy publishes.

## Changes

Edit through a pull request; Jimmy approves. A new craft is a new skill folder named `azzam-<craft>`, added to the table in `agents/azzam.md`.

Private to AZM X. Not for redistribution.
