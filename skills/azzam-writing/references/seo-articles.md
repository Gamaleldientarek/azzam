# SEO articles and pages for azmx.sa

How Azzam picks, briefs, writes and checks an article, a service page or a location page so it ranks in Saudi Arabia, in Arabic and in English.

## 1. Pick and check

- Start from the SEO radar: `next_actions` (brand `azmx`) gives keywords by importance × gap with the target URL. `keyword` and `cluster` show the cluster; `serp` shows page one in Saudi Arabia.
- Use `serp_fetch` only when the stored page one is older than 30 days.
- **One intent, one page.** Keywords that share three or more top-10 URLs belong on the same page. Before writing a new article, check that no live page already serves the intent; if one does, improve that page instead.
- Gap 4 means no page: write it. Gap 3 means the page exists and does not rank: fix indexing, targeting and internal links before rewriting.

## 2. How Saudis search

- **Three scripts of query:** Arabic («شركة تجربة المستخدم»), English ("ux agency riyadh") and mixed («تصميم ui ux»). Latin acronyms (UX, UI, CX) usually stay Latin in Arabic queries. Target each language's own phrasing; never translate a keyword.
- **Spelling variants:** أ/إ/ا، ة/ه، ى/ي, with and without «ال». Put the variant with the most demand in the title and H1; let the others appear only where the sentence wants them. Never stuff.
- **Location words:** الرياض، السعودية، المملكة / Riyadh, Saudi Arabia, KSA. Use them where the intent is local (location and service pages), not in every article.
- **Dialect questions** («وش هي…», «ايش الفرق بين…») are answered in Modern Standard Arabic, with the answer in the first sentence.
- **Slugs:** Latin, lowercase, hyphenated, three to five words, keyword first, no dates, as the site already does.

## 3. The brief

One page, filed at the top of the draft file. Start from the Blog SEO Brief prompt in `azmx-brand/references/content-prompts.md` and add:

| Field | What goes in it |
|---|---|
| Radar | Keyword IDs, primary and secondary, with volume and gap |
| Intent | What the searcher wants to do or know, in one sentence |
| Reader | Motion and persona from `audiences-and-messaging.md` |
| Angle | What this page says that page one does not (the information gain) |
| Page one | Format that wins, common headings, what every result misses |
| Outline | Mapped to the real fields (section 4 or 5 below) |
| Evidence | Each fact needed, with its evidence-bank line or "open, owner: …" |
| Expert | The named AZM X person who adds the first-hand passage and signs |
| Links | Target service page, related articles or case studies, glossary terms |
| Next step | The one real action for a reader who wants one |

## 4. Writing an article to the Blog collection

The Blog collection has fixed fields. The article is written to them, field by field.

| Field | Role | Rule |
|---|---|---|
| Article Title | H1 and page title | Primary keyword in the first half; the promise or the question; about 60 characters at most. The site's pattern «الموضوع: الوعد» works. |
| Description | Meta description and card summary | Under 155 characters; why this is worth the reader's minute. |
| First Paragraph | The answer | 60 to 120 words that answer the query on their own; the keyword in the first sentence. |
| Second, Third, Fourth Paragraph Title | The three H2s | Phrased as the questions people ask (page one, "People also ask", the cluster's terms). |
| Second, Third, Fourth Paragraph | The body | Formatted text: H4 subheadings, short lists, bold lead-ins and links. **Subheadings are H4, never H3**: the site's articles use H4, which the template styles to match; H3 falls back to a different font. Typical shape: why it matters now in Saudi Arabia; how to do it (the method, with `[EXPERT PASSAGE]`); what to do next or how to measure it, with two or three short questions answered as H4s when page one shows them. |
| Pull Quote | The expert's line | The sharpest sentence from the expert's own passage, quoted exactly. Its tinted box hides when the field is empty: leave it empty until the expert's line exists, never a placeholder. |
| Within Article Image, Image Caption, Within Article Image Alt | The one image in the frame | The frame is 569 px tall with a fluid width (square at 1024 px, about 1.27:1 at 1440 px) and crops to fill. Use an image that survives any crop: a centred brand render, or an example composed for the frame with everything important in the middle. Never a diagram with text near its edges. The caption is one takeaway from the section the image sits in, and takes the article's tint. |
| Diagrams | Inside the rich text | Place diagrams as images inside the paragraph fields (`<img src alt>` before the heading they follow): they render at full column width, uncropped, in both languages, each language with its own version. |
| Thumbnail, Thumbnail Alt | The card image | From the AZM X image library unless a real photo exists. |
| Author | Byline | «بقلم <اسم الخبير>» / "By <expert name>". Never «بقلم فريق عزم إكس». |
| Article Category | Filter | An existing category only. |
| Date, Read Time | Meta | Same format as the existing items. There is no "updated" field; record refreshes in `review.md`. |
| Share Text | Social line | The first line earns the click alone; three hashtags at most. |
| Palette | Colour | By meaning: blue business, purple people, orange creativity, green spirit and Saudi, yellow energy. |
| Featured | Home feature | Leave it. Exactly one article is featured site-wide; Jimmy decides. |

**Length:** match the depth of page one for the keyword, never more. Most pieces land between 900 and 1,600 words per language. Cut anything that restates a heading.

**The expert passage:** in the "how" section. Give the expert three prompts in the draft: what they saw in a project that the reader would not expect (no client name), the mistake they see most often, and what they would do first in the reader's place.

## 5. Service and location pages

- The Services collection has fixed slots (title, description, impact paragraph and three stats, value, three numbers, three benefits, four approach steps, tools, FAQ, images with alt). Write to the slots.
- **No client names or project figures** on SEO, service or location pages. Write the method and its impact on people.
- **Stats and numbers slots** take only evidence-bank lines with status *approved* or *public*. 25 of the 30 figures on the service pages today are unsourced samples; never extend them, and flag them when you touch a page.
- **«وكالة»** goes in the title or H1 only when it is the search term; the body says «شركة سعودية رائدة في الاستشارات الرقمية».
- **FAQ:** real questions from page one and from sales. Durations and prices only after their owners confirm them (evidence bank, EB-11 to EB-13).

## 6. Metadata

- Title about 60 characters, description under 155, in both languages; check how the page builds its title (template plus field) before writing it.
- Social text and image per page; alt text inside the image value; descriptive file names when an image is replaced.

## 7. Internal links

Every article links to:
- its cluster's service page (the radar's target URL),
- at least one related article or case study,
- two to four glossary terms at their first mention, only the most relevant,
- the contact page through a natural closing sentence, not a banner.

Anchors say where they go. When a new page goes live, add a link to it from at least two existing pages.

**External links open in a new tab.** Every link that leaves azmx.sa carries `target="_blank"` in the formatted text, in Arabic and English: `<a href="https://…" target="_blank">`. Links inside azmx.sa stay in the same tab. Add no arrow or other mark beside them (Jimmy, 5 Nov 2026).

## 8. Authority

- A named expert with their role (People collection), their first-hand passage, and the date.
- Sources inline, with publisher and year. Prefer official Saudi sources (Digital Government Authority, GASTAT, SDAIA, Vision 2030 programmes) and recognised research. Cite only what you opened and can link.
- Original data from AZM X reports, when the report is published and the figure is in the evidence bank.

## 9. The draft file

`docs/content/drafts/YYYY-MM-DD-<slug>.md`:

```
# <working title>
Status: brief | drafting | expert | english | gate | approved | handed over
Radar: <keyword IDs>   Target URL: <url>   Expert: <name, role>

## Brief
<the table from section 3>

## Arabic
Article Title:
Description:
First Paragraph:
Second Paragraph Title:
Second Paragraph:
Third Paragraph Title:
Third Paragraph:  (includes [EXPERT PASSAGE] and its three prompts)
Fourth Paragraph Title:
Fourth Paragraph:
Pull Quote:
Image Caption / Within Article Image Alt / Thumbnail Alt:
Author / Article Category / Read Time / Share Text / Palette:

## English
<the same fields>

## Links
<anchor → URL, per language>

## Evidence used
<evidence-bank line for each fact>

## Open facts
<fact → owner>

## Gate
<the eleven tests, each yes, with a note where it needed a fix>
```

## 10. After publishing

- Register the URL against its keyword IDs in the radar and record the publish event.
- After 28 days: clicks, impressions, CTR, average position and enquiries. On page one with a low CTR, rewrite the title and description first. A piece that slips for two months gets a refresh: new facts, a stronger answer, better links.

## 11. Editing a colleague's article

Azzam often edits a piece a colleague wrote. Ahlam Al Rouqi left 19 comments on the edit of her article (3 Nov 2026), and most of them undid changes made only from preference. So:

- **Fix what's wrong and keep what's theirs.** Change facts, structure, links and mechanics. Leave the writer's word choices unless a rule in this skill requires the change.
- **Send the edit back before it goes live.** The writer reads it, and their comments are applied on the branch. Record each comment and what happened to it in the draft file.
- **The closing line stays.** Every article ends with a next step that links to a service or another article, even when the writer proposes cutting it. Jimmy, 4 Nov 2026: it's what connects the reader to the rest of the website. Reword it if needed, and keep it.

## 12. Applying a reviewer's comments

Ahlam Al Rouqi reviews AZM X's copy. Her 88 comments on four case studies (5 Nov 2026) set this method: she proposes, Jimmy decides, Azzam applies.

1. **Start from the live text.** Match each comment to the field as it stands today. The review doc can be older than the page.
2. **Apply her words.** Change them only where a rule or a fact requires it, with the smallest edit, and record why. 72 of the 88 went in this way, 17 of them with a fix.
3. **A comment is a patch.** Read the whole sentence with her words in it, and adjust what the grammar needs. «المكتبة» in place of «مكتبة» needed «وتضم المكتبة…».
4. **Her note isn't text.** "(Most Common)", «حذفها», a tag or a stray quotation mark never reaches the page.
5. **Her flag can be right when her fix isn't.** Find what she saw. «تسلّمتها المجموعة كاملة» can read as "the whole group received it", so «بشكل كامل» failed a rule and «سُلّمت كاملةً إلى المجموعة» answered her.
6. **What you would leave out goes to Jimmy.** List it in a numbered table in the chat: where, it was, proposed. Keep any concern to one line. Write his choice as she wrote it, even against a rule here. He took hers on all 15 he saw.
7. **Follow the change through.** The same term across the page, the English saying the same thing, the title and description matching the H1, and every line still fitting its slot.

Record every comment and what happened to it. On azmx.sa the first set is in `docs/content/azzam-training/`.

## 13. Case study pages

- **Third person.** The page talks about the client's users, «المريض»، «المستخدم», and never to them: not «لخدمتك».
- **A redesign stays «إعادة تصميم»** in titles, subtitles and descriptions, not «إعادة ابتكار». It's the fact, and the phrase the page is found by.
- **Claims stay inside the evidence bank**, above all on a proof of concept. «خوارزميات», «التنبيهات المباشرة» and «فوري» go in only if the evidence says so.
- **A comparative stays, a claim of no friction goes.** «أكثر سلاسة» is fine. «سلس» and «بسلاسة» are the banned "seamless".
- **Check each word's sense.** Finance is «المالية»; «النقدية» means cash.
- **Company names stay plain** until the string bank says otherwise. Ahlam writes them in «», and Jimmy took that on one page, not as a site rule.

English on these pages:

| Use | Not |
|---|---|
| "to help patients access the right care" | ", so patients reach the right care" |
| "users" | "people" |
| "previous app" | "old app" |
| "Therefore," to open a conclusion | "So" |
| A second mention in other words: "in one place" | The same noun twice in a sentence |
