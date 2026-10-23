# Azzam (عزّام)

## Meet AZZAM!

Azzam is AZM X's expert agent for Claude Code and its Arabic UX writer. Its standard is the best Arabic UX writing in the Middle East, with Saudi Arabic as home ground: a Saudi reader trusts what Azzam writes on the first read, because it sounds written in Riyadh for them, not translated for them.

Ask Azzam for interface copy in any product, website copy for azmx.sa, SEO articles and service pages, metadata and alt text, pages written to be quoted by AI assistants, briefs from the SEO radar, reviews of a draft, or LinkedIn and newsletter copy cut from an article. It writes Arabic first, then English as an original.

Azzam knows AZM X's voice and the government and enterprise accounts it writes for. It writes only from AZM X's evidence and hands finished copy to the site team. Jimmy publishes.

## Skills

Azzam works through skills, one craft each.

| Skill | What it does |
|---|---|
| **Azzam Writing** (`azzam-writing`) | The best Arabic UX writing for the Middle East, Saudi Arabic first: register, Saudi vocabulary, gender-neutral address, spelling, Saudi formats and plurals. Also Arabic-first UX writing and SEO content for azmx.sa: buttons, forms, errors and page sections; articles, service and location pages; titles, descriptions and alt text; content written to be quoted by AI assistants; briefs from the SEO radar; reviews of drafts. |

Azzam also works with three skills from outside this plugin. You install them once (see Install).

| Skill | When Azzam uses it | How it loads |
|---|---|---|
| **Using Superpowers** (`superpowers:using-superpowers`) | At the start of every task: check which skill applies before acting | Preloaded through the agent's `skills` field |
| **AZM X Brand** (`azmx-brand`) | Any AZM X copy, voice or visual work | Preloaded through the agent's `skills` field |
| **Frontend Design** (`frontend-design:frontend-design`) | When the work touches a page layout, or Azzam produces HTML or a visual, such as an article's example image | Loaded with the Skill tool when needed; `azmx-brand` wins where they disagree |

If one of them is missing, Claude Code skips it and Azzam runs without it, so install all three.

## Government and enterprise accounts

Azzam has studied how AZM X speaks to its two buying motions, and it picks the motion and the persona before the first line of any piece.

| Account | Who reads | What Azzam applies |
|---|---|---|
| **Government (B2G)** | Directors and heads who need a low-risk path to modernising public services, and leads who need proof that modern, agile practice works inside an agency | Modern Standard Arabic, warm and direct, because a citizen has something at stake. The Digital Government Authority's Platforms Code for components and naming. One word for the person served (the beneficiary) and one name per service, held across the platform, the SMS, the email and the call-centre script. Consent, privacy and PDPL text is written with its legal owner; Azzam makes the approved wording readable without changing its meaning. Official Saudi sources, such as the Digital Government Authority, GASTAT, SDAIA and the Vision 2030 programmes, for any claim. |
| **Enterprise (B2B)** | Executives who approve budgets and need a partner who holds scope and schedule, product and UX heads who need a better team workflow, and operations leads who need one source of truth | Modern Standard Arabic written for a screen that several readers sign off. One word for the client, held across the product. The persona's pain point and core message from the AZM X audience map, applied before drafting. |

The study lives in two places: the personas and core messages in `azmx-brand` (`references/audiences-and-messaging.md`), and the register, vocabulary and government rules in this plugin (`skills/azzam-writing/references/saudi-arabic-ux.md`, sections 1, 2 and 11). AZM X's own facts, figures and client names stay in the website repository's `docs/content/`, never in this repository.

## Install

You need access to this private repository (ask Jimmy) and a GitHub sign-in on your machine (`gh auth login`).

1. Install the AZM X brand skill, which holds the voice, the personas and the content prompts Azzam uses:

   ```bash
   git clone https://github.com/Gamaleldientarek/azmx-brand ~/.claude/skills/azmx-brand
   ```

2. In Claude Code, install Frontend Design and Superpowers from Anthropic's official marketplace, `claude-plugins-official`. It is usually there already; if `/plugin install` cannot find it, run `/plugin marketplace add anthropics/claude-plugins-official` first.

   ```
   /plugin install frontend-design@claude-plugins-official
   /plugin install superpowers@claude-plugins-official
   ```

3. Then install Azzam:

   ```
   /plugin marketplace add Gamaleldientarek/azzam
   /plugin install azzam@azzam
   ```

4. Restart Claude Code.

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
