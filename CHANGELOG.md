# Changelog

Newest first. Each section becomes the notes of its GitHub release.

## 0.3.3 (2026-11-05)

Ahlam Al Rouqi's notes from her 88 comments on four case studies, with Jimmy's decisions. A test on 14 new lines shaped what went in: Azzam already handled the process and missed her style.

- **Digits for every count.** In titles, intros and body text, in Arabic and English: `saudi-arabic-ux.md`, section 9.
- **Word choices.** «موحّد» not «واحد» for a shared system, «الأسلوب» not «الصوت» for a brand, «السابق» not «القديم», «تتيح» not «تترك», and ten more: section 2.
- **Sentences.** Open on a verb, not a possessive; no word twice in a sentence; plain words, not an image that only works in English; a comparative before «من»; «لجميع» not «لكافة»; «حاجة إلى»: section 6.
- **Applying a reviewer's comments.** A new section in `seo-articles.md`: start from the live text, apply her words, read the sentence after the patch, and send what you would leave out to Jimmy in a numbered table.
- **Case study pages.** A new section in `seo-articles.md`: third person, «إعادة تصميم», claims inside the evidence bank, company names plain, and her English register.

## 0.3.2 (2026-11-05)

- **External links open in a new tab.** In articles, every link that leaves azmx.sa carries `target="_blank"` in the formatted text, in Arabic and English; links inside the site stay in the same tab, with no arrow or other mark: `seo-articles.md`, section 7.

## 0.3.1 (2026-11-04)

Ahlam Al Rouqi's notes from her 19 comments on the edit of her article, approved by Jimmy.

- **One reader, not a group.** Articles and other long copy address one person, and examples open in the first person: `saudi-arabic-ux.md`, section 5. Interface copy keeps its neutral constructions.
- **No needless shadda.** Common verbs lose the shadda; a word that could be misread keeps one mark: section 7.
- **Word choices.** «الزائر» not «الضيف», «نقاط تواصل» not «طبقة من التواصل», «وإنما» after a negation, «كما هو موضح في» before a link: sections 2 and 6.
- **Editing a colleague's article.** A new section in `seo-articles.md`: fix what's wrong and keep what's theirs, send the edit back before it goes live, and the closing line stays.

## 0.3.0 (2026-10-23)

- **Any website, every email.** Azzam now writes for any website AZM X writes for, not only azmx.sa: the AZM X brands' sites and client sites too. For a site that is not azmx.sa, it asks for that site's facts and fields first and never borrows AZM X's evidence.
- **Newsletters and emails.** A new reference, `references/email-newsletters.md`, built from a study of the newsletter templates and every email AZM X sends to people: campaigns, report teasers, announcements, and the confirmation, welcome and thank-you emails.
- **Government and enterprise accounts.** The README sets out what Azzam applies when it writes for government (B2G) and enterprise (B2B) readers.
- **Three outside skills.** The agent preloads Using Superpowers (`superpowers:using-superpowers`) at the start of every task and AZM X Brand (`azmx-brand`) for any AZM X copy, voice or visual work. Frontend Design (`frontend-design:frontend-design`) loads through the Skill tool when a piece has a layout, HTML or a visual; `azmx-brand` wins where they disagree.
- **Dependencies.** The plugin declares Frontend Design and Superpowers from `claude-plugins-official` as dependencies, so installing Azzam installs them.
- **Tests.** A static check that GitHub runs on every push and pull request, and a live test that proves the three skills preload.
- **Releases.** Pushing a tag `azzam--vX.Y.Z` publishes a GitHub release with this changelog's notes.
- **Meet AZZAM!** A new opening for the README.

## 0.2.1 (2026-10-23)

Article rules learned on the first preview: subheadings are H4, never H3; the Blog image frame crops, so diagrams go inside the rich text; the pull quote stays empty until the expert's line exists; and Saudi copy names the coding activity instead of using the Arabic word that reads as a cipher.

## 0.2.0 (2026-10-22)

Saudi Arabic UX writing. A new reference, `saudi-arabic-ux.md`, covers register by surface, Saudi vocabulary, Egyptian and Levantine words to avoid, the white dialect, gender-neutral address, Arabic-first sentences, spelling, Saudi formats (ID, address, IBAN, the riyal sign, calendars), the six Arabic plural forms, occasions, government services and the wider Middle East. The skill loads it before any Arabic word, and the gate checks it.

## 0.1.0 (2026-10-22)

First release: the Azzam agent and the Azzam Writing skill, with three references (UX writing, SEO articles, AI answers). AZM X's facts stay in the private website repository (`docs/content/`).
