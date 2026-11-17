---
name: azzam-writing
description: Azzam Writing, AZM X's writing craft and the best Arabic UX writing for the Middle East, Saudi Arabic first. Use for any words a visitor reads on azmx.sa or on any other website AZM X writes for (the AZM X brands' sites, client sites), for newsletters and every email AZM X sends to people, and for Arabic or Saudi interface copy in any product, including UX copy (buttons, links, form labels, errors, empty and success states, page sections), SEO articles and blog posts, service and location pages, titles, meta descriptions, slugs and alt text, content written to be cited by ChatGPT, Gemini, Perplexity and Google AI answers, newsletters, campaign and report emails, confirmation, welcome and thank-you emails, subject lines and preheaders, briefs built from the SEO radar, reviews of a draft, and turning an article into LinkedIn copy. Triggers include "Azzam", "Arabic UX writing", "Saudi Arabic copy", "Arabic microcopy", "localise for Saudi", "write an article", "blog post", "SEO copy", "UX copy", "microcopy", "error message", "button text", "meta description", "newsletter", "email copy", "subject line", "welcome email", "brief", "review this draft", and "rank for".
---

# Azzam Writing

Every word on a website or in an email does one of four jobs: help a reader act, rank for a search a Saudi buyer makes, be the source an AI assistant quotes, or bring a reader back. Write for the job, in Arabic first, from facts that exist. azmx.sa is home ground; the same craft serves any website AZM X writes for and every email it sends.

## Load first, every time

| What | Where | Why |
|---|---|---|
| AZM X voice | `~/.claude/skills/azmx-brand/references/voice-and-tone.md` | The four dimensions, the no-AI-tells mechanics, the pre-publish checklist. Do not restate it; apply it. |
| Audience and core message | `~/.claude/skills/azmx-brand/references/audiences-and-messaging.md` | Pick the motion (B2G or B2B) and the persona before the first line. |
| Arabic craft | the `jee-arabic` skill | Written Arabic, not translated English; punctuation; the checker. In a cloud session without it, follow the Arabic rules in `docs/content/string-bank.md`. |
| AZM X facts | `docs/content/evidence-bank.md`, `docs/content/string-bank.md`, `docs/content/entity-facts.md` in the website repository | The only source for AZM X's claims, names, figures and fixed wording. For an AZM X brand or a client site, that site's own facts: ask for them before the first line, and never borrow AZM X's. |
| Site rules | `CLAUDE.md` at the root of the site's repository | On azmx.sa: positioning, «المنصة», no mixed-language sentences, Jimmy owns his edits. Another site brings its own rules. |

Then the reference for the job:

| Job | Reference |
|---|---|
| Any Arabic copy for a Saudi or Middle East reader: register, Saudi vocabulary, gender-neutral address, spelling, Saudi formats, plurals, occasions | [references/saudi-arabic-ux.md](references/saudi-arabic-ux.md), always, before the first Arabic word |
| Interface copy: buttons, links, forms, errors, states, sections | [references/ux-writing.md](references/ux-writing.md) |
| The words of a filter or a sort above a list: a blog index, a glossary, case studies, reports, jobs | [references/ux-writing.md](references/ux-writing.md), "Filters and sorting", with the fixed labels in `~/.claude/skills/azmx-brand/references/filters.md` |
| Article, blog post, service, location or case study page, metadata, applying a reviewer's comments | [references/seo-articles.md](references/seo-articles.md) |
| Pages meant to be quoted by AI assistants; entity consistency; the monthly citation check | [references/ai-answers.md](references/ai-answers.md) |
| Any email: the monthly newsletter, an occasion greeting, an announcement, a report email, a confirmation, welcome or thank-you email, a brand newsletter; subject lines and preheaders | [references/email-newsletters.md](references/email-newsletters.md), with AZM X's email facts in `docs/content/email-bank.md` and the look in `azmx-brand`'s `references/email-design-system.md` |
| The AI-writing audit, before any piece passes the gate | [references/ai-writing-audit.md](references/ai-writing-audit.md), with the `avoid-ai-writing:avoid-ai-writing` skill for the English |
| A ready prompt shape (blog brief, article, case study, newsletter, LinkedIn) | `~/.claude/skills/azmx-brand/references/content-prompts.md`, then the house rules here override it |
| Any layout, HTML or visual the piece needs (an article's example image, a diagram, a section mock-up) | the `frontend-design:frontend-design` skill for the craft, with the `azmx-brand` skill for colours, type, the chevron and the image library; `azmx-brand` wins where they disagree |

## The flow for one piece

1. **Pick.** From the SEO radar (`next_actions`, then `cluster` and `serp`) or from Jimmy's request. Check the target URL and that no other page already serves the intent.
2. **Brief.** One page, in the shape in `seo-articles.md`. Name the expert who will sign before drafting.
3. **Evidence.** List every fact the piece needs and its line in the evidence bank. Anything missing becomes an open fact with an owner; never a guess.
4. **Arabic draft.** The full body, written to the page's real fields (on azmx.sa, the Blog CMS shape or the template slots; on another site, its own fields). Leave one marked slot, `[EXPERT PASSAGE]`, where the expert adds what they saw first-hand.
5. **Expert pass.** The expert writes the passage, edits and signs. Their name goes on the byline.
6. **English.** Written as an original for an English reader, with English keywords from the radar. Same section order as the Arabic (Framer gives one page node to both languages).
7. **Gate.** Run the AI-writing audit in `ai-writing-audit.md` on both languages, then the tests below. Fix, then run them again.
8. **Hand-off.** Jimmy approves. On azmx.sa, `site-content` writes it into the CMS as a draft (backup, both languages) and Jimmy publishes. On another site, its owner places and publishes it.
9. **Register and check.** Record the URL against its keyword IDs in the radar. After 28 days, read clicks, CTR, position and enquiries; rewrite the title if CTR is low.

UX copy follows steps 3, 4, 6, 7 and 8 only. An email follows its own flow, gate and draft layout in `email-newsletters.md`; nothing is sent without Jimmy's yes to a test send.

## The gate

A piece ships only when every answer is yes.

1. **Job:** can you say in one sentence what the reader gets and what they can do next?
2. **Truth:** does every number, name, quote and claim have a line in the evidence bank with status *approved* or *public*?
3. **Rules:** on an SEO page, a service page or an article, are there no client names or project figures (unless Jimmy approved them for this piece)?
4. **Arabic:** does it read as written in Arabic for a Saudi reader (the review in `saudi-arabic-ux.md` section 13 passes; the `jee-arabic` checker passes; no mixed-language sentence; RLM before a Latin name)?
5. **Voice:** does it pass the azmx-brand pre-publish checklist (no em-dash habit, no triads, none of the banned intensifiers, no emojis, three hashtags at most)?
6. **Search:** is the primary keyword in the title, the H1 and the first paragraph, written naturally, in each language's own phrasing?
7. **Answer first:** does the first paragraph answer the query on its own?
8. **Fit:** does every string fit its field or slot in both languages?
9. **Links:** at least one service page, one related article or case study, and descriptive anchors?
10. **Authorship:** is a named expert on the byline, with their first-hand passage in the text?
11. **Distinct:** could a competitor paste this over their logo? If yes, sharpen it.
12. **Written by a person:** does it pass the AI-writing audit in `ai-writing-audit.md`, in Arabic and in English, with no open findings?

## Where the work goes

- Drafts: `docs/content/drafts/YYYY-MM-DD-<slug>.md`, one file per piece, in the field-by-field layout in `seo-articles.md`, so `site-content` can deliver it without rewriting. For another site, the same layout in that project's drafts folder; ask where it lives.
- Findings and reasons: `review.md` (newest first). Status: `task.md`.
- A fact you confirmed, or a new approved quote: add it to the evidence bank with its source and date. A new fixed term: add it to the string bank. One source of truth per fact.
