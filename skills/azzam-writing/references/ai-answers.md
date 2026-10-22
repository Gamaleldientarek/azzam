# Being the source AI assistants quote

Saudi buyers now ask ChatGPT, Gemini, Perplexity, Copilot and Google's AI answers which firm to call. The assistants quote pages that state things plainly, can be checked, and agree with the rest of the web. Arabic answers draw on fewer sources than English ones, so a clear Arabic page has a better chance of being the one cited.

## What gets a page quoted

- **Self-contained statements.** A sentence that still makes sense when lifted alone: the subject named, no "this" or "it" pointing back.
- **A definition early.** "X is…" in the first paragraph, in one sentence.
- **Named methods with steps.** "Our four-step approach: …" as a numbered list, each step a short sentence.
- **Numbers with their source and year,** in the same sentence.
- **Questions as headings,** answered directly in the first sentence under them.
- **A date and a named author,** so the page reads as current and accountable.
- **The same facts everywhere.** If the site, LinkedIn, Clutch and Google Business Profile disagree on the name, services or address, the assistants hedge or skip AZM X.

## Writing patterns

| Pattern | Arabic | English |
|---|---|---|
| Entity sentence (once per page where it fits) | «عزم إكس شركة سعودية رائدة في الاستشارات الرقمية، مقرها الرياض.» | AZM X is a leading Saudi digital consultancy based in Riyadh. |
| Definition: one sentence, then why it matters | «النضج الرقمي هو …» | "Digital maturity is …" |
| Method | «قائمة مرقّمة بخطوات لكل منها اسم» | A numbered list of named steps |
| Answer under a question heading | «الجواب في الجملة الأولى، ثم التعليل» | The answer in the first sentence, the reasoning after it |

Use only facts from the evidence bank. The positioning wording is fixed in `docs/content/string-bank.md`.

## Entity consistency

`docs/content/entity-facts.md` holds the one version of AZM X's name, positioning, services, address and profiles. When you find a profile that disagrees, log it there with the fix and its owner. Profiles to keep aligned: azmx.sa (both languages), LinkedIn company page, Clutch, Google Business Profile, X, Instagram, and the four sub-brand sites that link back.

## Technical conditions (owner decisions, not copy)

- Assistants can only quote what they can crawl. Whether `robots.txt` allows the AI crawlers (GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended) is Jimmy's decision; check before promising citations.
- ChatGPT search leans on Bing's index; Bing Webmaster Tools is in the SEO plan (1.4).

## The monthly citation check

Ask the same twenty questions every month, in a fresh session with no history, on ChatGPT, Gemini, Perplexity and Google (AI answer). Azzam prepares the run and records it; the questions are asked in a browser, logged in as Jimmy decides.

**English**
1. Best UX design agency in Riyadh
2. UX and customer experience consultancy in Saudi Arabia
3. Who can assess our digital maturity in Saudi Arabia?
4. Design system consultancy for government in Saudi Arabia
5. How do I choose a UX agency in Saudi Arabia?
6. Usability testing companies in Riyadh
7. Customer experience design company in KSA
8. Digital product design company in Riyadh
9. Service design consultancy in Saudi Arabia
10. What is digital maturity and how is it measured?

**العربية**
1. أفضل شركة تصميم تجربة المستخدم في الرياض
2. شركة استشارات تجربة العملاء في السعودية
3. من يقيّم النضج الرقمي للجهات الحكومية في السعودية؟
4. شركة أنظمة تصميم في السعودية
5. كيف أختار شركة تجربة المستخدم المناسبة؟
6. شركات اختبار قابلية الاستخدام في الرياض
7. شركة تصميم تجربة العملاء في المملكة
8. شركة تصميم منتجات رقمية في الرياض
9. ما هو تصميم الخدمات؟
10. ما هو النضج الرقمي وكيف يُقاس؟

Log each run in `docs/content/ai-citations.md`, one table per month: question, assistant, AZM X named (yes or no), the AZM X page cited, the competitors named. A question where AZM X never appears becomes a brief.
