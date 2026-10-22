# UX writing for azmx.sa

Interface words decide whether a visitor acts. Each one should say what happens next, in the fewest words that stay clear, and use the same name for the same thing everywhere.

## Five principles

1. **Say what happens.** A button names the result, not the mechanism: "Download the report", not "Submit".
2. **One name per thing.** A service, a form or a section has one name across the menu, the page, the form and the emails. Names live in `docs/content/string-bank.md`.
3. **The point first.** Headings carry the message; the body adds what the heading cannot.
4. **Help, never blame.** An error says what went wrong and how to fix it, in plain words.
5. **Both languages are originals.** Write the Arabic, then the English. Measure both against the slot.

## Arabic interface defaults

These are Azzam's defaults until the first UX audit lists what the site already uses; the audit result goes into the string bank and wins.

- **Action buttons in forms and controls:** verbal noun and object, which reads the same for every visitor: «إرسال الطلب»، «تحميل التقرير»، «حجز موعد».
- **Invitations in page sections:** a short imperative is natural: «تواصل معنا»، «تعرّف على خدماتنا».
- **Addressing the reader in body text:** the plural, which suits an organisation and avoids a gendered singular: «فريقكم»، «جهتكم»، «نساعدكم».
- **Polite requests in errors:** «يُرجى» and a clear instruction.
- **Punctuation, digits, Latin names inside Arabic:** the Arabic mechanics in `docs/content/string-bank.md`.

## Patterns

| Pattern | Rule | Arabic | English |
|---|---|---|---|
| Primary button | Verb and object; two to four words | «حجز استشارة» | Book a consultation |
| Link in text | Says where it goes; never «اقرأ المزيد» or "Read more" alone | «تعرّف على طريقتنا في بناء أنظمة التصميم» | See how we build design systems |
| Form label | Above the field, short, no colon; the placeholder never replaces it | «الاسم الكامل» | Full name |
| Helper text | Only when the format is not obvious | «سنرسل نسخة التقرير إلى هذا البريد» | We'll send the report to this address |
| Error, empty field | What is needed and why | «يُرجى كتابة الاسم الكامل لنعرف بمن نتواصل» | Enter your full name so we know who to reply to |
| Error, wrong format | What is wrong and how to fix it | «يُرجى كتابة البريد الإلكتروني كاملًا، مع علامة @ واسم النطاق» | Enter the full email address, with the @ and the domain |
| Success | Confirms, then says what happens next and when | «وصلنا طلبكم، وسنتواصل معكم خلال [مدة الرد]» | We've got your request. We'll reply within [reply time] |
| Empty state | Why it is empty, then the next useful step, and only a step that really exists on the site | «لا توجد وظائف شاغرة الآن» | No open roles right now |
| 404 | Admits the miss, offers two real routes | «لم نجد هذه الصفحة، فربما تغيّر رابطها. ابدأ من خدماتنا أو من أحدث المقالات» | We couldn't find this page; its link may have changed. Start from our services or the latest articles |

The reply time in the success message is an open fact (evidence bank, EB-11). Never fill it with a guess.

## Page sections

- **Hero:** who it is for and what changes for them, in one line; one primary action. The template's heading, subheading and button are the whole message.
- **Value and benefits:** one claim per block, each backed by a method or a public fact, never by an unsourced statistic.
- **Proof:** approved testimonials and logos only (evidence bank). Place proof where the reader doubts, usually after the claim it supports.
- **Close:** one action. If the page has no real next step, it ends without a manufactured one.

## Fit to the slot

- Before writing, read the slot's current text in both languages and on every breakpoint (Framer keeps a copy per breakpoint).
- Write within the length the design holds. If the right words do not fit, say so and propose a shorter line; never let the layout cut a sentence.
- Copy is the same on every breakpoint unless Jimmy decides otherwise.
- Record a slot's length budget in the string bank the first time you measure it.

## UX audit of a page

1. List every visible string on the page in both languages: navigation, headings, buttons, links, labels, helper and error texts, states, alt texts.
2. Check each against the string bank (names, fixed wording) and the patterns above.
3. Return one table: location, current Arabic, proposed Arabic, current English, proposed English, reason. Only lines that need a change.
4. Add the live wording that is right, and any new fixed term, to the string bank.
5. Hand the approved table to `site-content` or `site-builder`; Jimmy publishes.

## Accessible writing

- Alt text carries the image's meaning in the page, in under about 125 characters, without "image of". Decorative images take empty alt.
- Headings in order, one H1 per page.
- Buttons and links make sense read out of context by a screen reader.
- Plain language: one idea per sentence, the common word over the clever one.
