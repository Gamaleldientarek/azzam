# Newsletters and emails

How Azzam writes every email AZM X sends to people: the monthly internal newsletter, occasion greetings, announcements, report emails, the website's confirmation and thank-you emails, and brand newsletters. Built on 23 Oct 2026 from a study of the newsletter templates, the report and announcement emails, the website's transactional templates, the email design system and every campaign in Brevo.

Three sources sit beside this file:

- **AZM X's email facts** (series name, standing lines, sender names, lists, templates, subjects already sent, links): `docs/content/email-bank.md` in the website repository. Copy names and fixed lines from there; never retype them.
- **The evidence** behind every rule here, with file paths: `docs/content/email-study-2026-10-23.md`.
- **The look** (components, colour, type, RTL mechanics, dark mode): `references/email-design-system.md` in `azmx-brand`. When you produce the HTML yourself, load `frontend-design:frontend-design` too; `azmx-brand` wins where they disagree.

## 1. Two absolutes

1. **Nothing is sent without Jimmy's explicit yes to a test send.** Jimmy schedules or sends AZM X campaigns himself. Azzam never writes into Brevo, never uploads, never sends. A brand that sends from its own account (Anatomi) follows the same rule.
2. **Supplied Arabic is never changed without asking.** Copy the content team's Arabic, a quoted report sentence or a client's paragraph character for character, with its elongations, emoji and dialect spellings. If something looks like a typo, ask. An approved fix is the smallest possible edit, never a retype.

## 2. Pick the email type, then the voice

| Type | Reader | Language | Register | Azzam's job |
|---|---|---|---|---|
| Monthly internal newsletter | The team and the board | Arabic only | Saudi dialect, warm and genuinely funny; jokes, elongations and emoji are the content | Draft the subject and preview options, write approved standing lines, list possible typos as questions. The content team's copy is canonical: do not rewrite it. |
| Internal occasion greeting (National Day, Founding Day, Eid) | The team | Arabic block, then the English translation | Ceremonial Modern Standard Arabic with a short prayer | Write it in full. National Day and Founding Day are different days with different messages. |
| Internal announcement (the annual report) | The team | As briefed (the one sent so far was English) | Celebratory, team first: lead with the people, not the company | Write it in full from the brief's figures. |
| External report email | Decision-makers, B2B and B2G | Arabic | Formal Modern Standard Arabic with light warmth; a research house, not a generator | Write it in full. No filler openers, no hollow superlatives, no em dash, no emoji. |
| Website transactional email (confirm, confirm return, thank-you per form) | Anyone who typed an address, including bots | Full Arabic block, then full English block | Short, warm Saudi dialect, as the content team wrote it and Jimmy approved on 21 Oct 2026 | Keep that register for any new transactional email unless Jimmy says otherwise. It must read safely in a stranger's inbox. |
| Brand newsletter (Anatomi, Colab, Majarah, Clix) | The brand's audience | The brand's language | The brand's own voice, from its site and `azmx-brand`'s `sub-brand-voices.md`; never AZM X's look or chevron | Write to the brand's brief and supplied copy. |
| Newsletter for the website's subscribers | People who confirmed on azmx.sa | Not decided | Not decided | Nothing exists yet. Before a first line, ask Jimmy for the format, tone, sender, cadence and the first issue's content. The welcome email promised them articles, reports and the glossary. |

AZM X is «شركة سعودية رائدة في الاستشارات الرقمية» / "a leading Saudi digital consultancy" in every email. Never studio, agency or boutique.

## 3. Structure by type

**Monthly internal newsletter.** Hero (eyebrow, the series name, the month line), a digest card with one chip per section, 9 to 11 numbered sections, the standing sections when the month has content for them (coffee hour, welcome, spotlight, then the agenda, which always closes the issue), and the compact footer. At most one of each big moment per issue (launch banner, achievement card, spotlight card, flipped header, fun award); drop it rather than fake it. A section title and its digest chip are the same string. No sign-off: the footer's "made with love" line closes it.

**Occasion greeting.** Hidden preheader, logo, a designed banner (its words repeated in the alt text), the Arabic greeting, the English greeting, the prayer and its translation, footer. No button.

**Announcement and report email.** Hero (eyebrow, serif title, subtitle), a greeting, two short intro paragraphs, the proof (stat tiles, findings or a pull-quote quoted word for word), one download block with a headline above one button, footer. One job: open or download the thing announced.

**Website transactional email.** Hidden Arabic preheader, header with the logo, then the Arabic block (form label, headline, greeting, one or two body sentences, the service or report title when present, one primary button, a quieter secondary one, the "not you?" note, a lead line and three link rows), then the English block in the same order, then the shared footer.

## 4. Subject lines and preheaders

- **Draft three or four subjects, each with one line of reasoning, recommend one, and let Jimmy pick.** A subject adapted from a past formula is still a draft.
- **Length:** 45 characters at most; phones show about 35 to 40 Arabic characters, so the hook goes first. Bilingual transactional subjects are one string, «Arabic | English», Arabic first.
- **Newsletter:** a recognisable identity (the series name, or the "month is over" line used June to August) plus exactly one emoji, then curiosity that teases without explaining. Jimmy picked the issue's own question in September.
- **External report:** lead with a finding or a question the reader cares about, stated with dignity, framed as a market finding rather than an accusation.
- **Transactional:** a short statement of what happened, the Arabic part 10 to 35 characters («طلبك وصلنا», «تقريرك جاهز»).
- **The preheader completes the subject and never repeats it.** Newsletter previews carry a second set of two or three teasers. Campaigns set it in Brevo's preview field only; do not add a different hidden preheader in the HTML. Transactional emails carry one hidden Arabic preheader sentence, and it is never empty.

## 5. Arabic and English together

- **A bilingual email is a complete Arabic block, then a complete English block,** with the same meaning line for line. Never two languages in one sentence or one line.
- **Greet each block in its own script, with a fallback:** an Arabic-script first name only in the Arabic greeting, a Latin one only in the English greeting; otherwise «أهلًا بك،» and "Hello,". A title or tag goes in by script too; a title that mixes scripts is left out of both blocks.
- **In an Arabic-only email, a Latin name may close a sentence but should not sit in its middle;** rephrase or transliterate. Keep one form of a partner's name through the email.
- **The brand name is «عزم إكس», with the hamza,** in bodies and sender names alike.
- **Right to left:** every Latin fragment, number, date, year, URL and English title is easy to isolate in an LTR span; write the copy so it can be. A title that starts with a Latin word gets a right-to-left mark before it. Arrows point left in Arabic emails («‹», «◀︎», «↓» for download). No letter-spacing on Arabic.
- **Numbers and dates:** Western digits everywhere. The month line is the Gregorian month in Arabic with the year in an LTR span («سبتمبر 2026»). An event with no date yet says «قريبًا», never an invented date. Ranges take an en dash and never break across lines. Times are Riyadh time.
- **Saudi rules still apply:** `saudi-arabic-ux.md` for register, vocabulary and spelling, and one placement of the tanwin through an email («قريبًا»).

## 6. Personalisation

- **Campaign greetings** use the contact's first and last name; give the greeting a fallback so it never renders as an empty «أهلاً ،».
- **The internal newsletter is not personalised.**
- **Transactional emails** use the relay's params, each inside an `{% if %}` with a fallback. Every sentence must read well with and without the param.
- **Never put text a submitter wrote into an email:** only the first name (if it looks like a name), a mapped service or report title, and a mapped link.

## 7. Calls to action and links

- **One primary action per email.** Secondary actions are small text links, never competing buttons.
- **A CTA is an imperative of two or three words that names what the reader gets** («حمّل التقرير كاملًا», «سجّل وابدأ الكورس»). A button names what it does: «افتح التقرير» when the PDF is linked, «تصفّح تقاريرنا» when it is not. A calendar button reads «📅 أضف للتقويم».
- **A CTA only where a real next step exists.** If a link has no wording or no URL yet, ship the section without the button; never `href="#"`.
- **Use the exact link Jimmy gives, character for character.** Website emails link to azmx.sa (Arabic) and azmx.sa/en (English).

## 8. Images and live text

- **Headings, body and buttons stay live text,** so the email reads with images blocked. Animation is decoration: the email reads as a finished static design.
- **Every image has an alt text in the email's language.** When an image carries words, the alt carries the same words. People: the name, an em dash, then the role as their title is written («{الاسم} — {المسمى الوظيفي}»). Photos: what the photo shows, in a few words. Decorative images take an empty alt.
- **Write for system fonts:** Gmail shows no brand fonts, so a line must work in any Arabic system font.
- **Words on a photo must survive Gmail's dark-mode inversion;** move the words off the photo rather than adding a colour wash.

## 9. Trust and deliverability wording

- **Say why the reader got the email** when they may not have asked for it: a "not you? ignore it" line, and the link's expiry on confirmations.
- **Keep confirmations neutral,** because bots type other people's addresses.
- **Promise only what the flow does:** no "we will reply" where nobody will, no "attached" where the report is only linked. Each "not you?" line must fit its email (an applicant did apply).
- **Keep emphasis scarce:** few exclamation marks, no capitals for urgency.
- **One sender name per email type, kept from issue to issue,** and a sender that fits the type (the newsletter's sender is wrong for a formal report). The current names are in the email bank.

## 10. Footer

Jimmy's compact footer on every AZM X email: logo and social icons on one row, a short meta line that names the email (the issue's month, the report, or the tagline), «صُنعت بحب في الرياض ❤️», and one small link: unsubscribe on campaigns, the privacy policy on transactional emails. The website emails use it on a black card. Never design a long footer. A campaign footer carries the unsubscribe tag exactly once.

## 11. Lengths

| Element | Length |
|---|---|
| Subject | 45 characters at most |
| Preview / preheader | One sentence; the brand target is 80 to 100 characters, transactional ones run 40 to 50 |
| CTA | 2 or 3 words |
| Transactional headline | 2 to 5 words; body one or two sentences |
| Newsletter section body | About 120 to 160 characters; body copy flows as one paragraph per block |
| Newsletter agenda line | 30 to 50 characters, ending with a full stop |
| Newsletter HTML | Under 100 KB (Gmail clips at 102 KB); more sections cost more than longer sentences, and a cut is Jimmy's call |

After every copy edit, check where lines break at phone widths: the last line holds at least two words, a trailing emoji stays with its word, a range never splits. Fix with a non-breaking space, never by changing the words.

## 12. Open rulings

The brand rules and the emails AZM X has sent disagree on these. Until Jimmy rules, follow the email type's own record and name the point in your report:

1. **Emoji.** The brand bans them in subjects and copy; the newsletter requires one in its subject and uses them as content; report subjects have used one or none; every footer carries ❤️.
2. **Em dashes.** The brand bans the em-dash habit and the report brief bans it outright; the newsletter's month line, footer meta and previews use it as fixed furniture.
3. **Exclamation marks.** The brand says none doing the selling; the approved transactional copy carries several.
4. **Sender names.** No written convention yet; the live names drift.
5. **The unsubscribe label** on report emails and greetings still names the newsletter.
6. **Arabic and English say different things** in some live transactional templates; the email bank lists them.
7. **The English philosophy line** for any English footer.

## 13. The email gate

An email ships to Jimmy only when every answer is yes:

1. **Type:** is the register the one in the table in section 2?
2. **Truth:** does every name, figure, date and claim come from the brief, the supplied copy or the evidence bank?
3. **Supplied Arabic:** is it unchanged, with every possible typo raised as a question?
4. **Subject:** three or four options, 45 characters or fewer, with a recommendation?
5. **Preheader:** does it complete the subject without repeating it, and is it never empty?
6. **Languages:** Arabic block first, English block with the same meaning, no mixed sentence, greetings by script with fallbacks?
7. **Action:** one primary CTA of two or three words, every link real and exact?
8. **Alt and live text:** does the email read with images blocked?
9. **Trust:** does it say why the reader got it, and promise only what happens?
10. **Footer:** the compact footer, with the unsubscribe tag once on a campaign?
11. **Voice:** does it pass the `azmx-brand` pre-publish checklist, within the open rulings above?

## 14. The draft file

One file per email: `docs/content/drafts/YYYY-MM-DD-email-<slug>.md`, in this order:

1. Type, reader, list, sender name, send date proposed.
2. Subject options with one line of reasoning each, and the recommendation.
3. Preview text.
4. The blocks in order, Arabic then English, each string on its own line, labelled with its slot.
5. Alt text for every image.
6. Every link, exactly.
7. Open facts with their owners, and the open rulings this email touches.

Jimmy approves. The email's owner builds or uploads it, Jimmy test-sends, and Jimmy sends.
