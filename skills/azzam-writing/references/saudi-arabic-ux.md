# Saudi Arabic UX writing

Azzam's home ground. The standard: a Saudi reader trusts the interface on the first read, because every word sounds like it was written in Riyadh for them, not translated for them. This file holds the decisions that make that happen. Apply it with `jee-arabic` (craft and checker) and `ux-writing.md` (patterns).

## 1. Pick the register before the first word

| Surface | Register | Why |
|---|---|---|
| Government services, banks, insurance, health | Modern Standard Arabic, warm and direct | Trust and legal clarity. The reader is a citizen or a customer with something at stake. |
| B2B and enterprise products | Modern Standard Arabic | Several readers sign off the same screen. |
| Consumer apps (food, retail, travel, wallets) | Modern Standard Arabic as the base; Saudi "white dialect" only for greetings, empty states and light notifications, and only when the brand's voice guide allows it | Warmth where nothing is at stake. |
| Errors about money, payments, consent, privacy, legal text | Modern Standard Arabic, always | No playfulness where a mistake costs the reader. |
| Pan-Arab products | Modern Standard Arabic with neutral vocabulary | One voice that no market reads as foreign. |

Never mix registers inside one sentence, and never change register between two screens of the same task.

## 2. Saudi vocabulary

| Use | Not | Note |
|---|---|---|
| «الجوال»، «رقم الجوال» | «الموبايل»، «المحمول» | The Saudi word for a mobile phone. |
| «رمز التحقق» | «كود التفعيل»، «الكود» | The one-time code sent by SMS. |
| «كلمة المرور» | «كلمة السر»، «الباسورد» | |
| «تسجيل الدخول»، «إنشاء حساب» | «لوج إن»، «ساين أب» | |
| «الهوية الوطنية»، «رقم الهوية» | «البطاقة الشخصية»، «الرقم القومي» | The second pair is Egyptian. |
| «رقم الإقامة» | «رقم الهوية» for residents | Residents hold an Iqama; say so. |
| «العنوان الوطني» | «العنوان البريدي» on its own | The official address system. |
| «المستفيد» (government), «العميل» (commercial) | Both in one product | Pick one per product and hold it. |
| «الطلب»، «المعاملة» | «الأوردر» | «المعاملة» for government procedures. |
| «السلة»، «إتمام الطلب»، «التوصيل»، «استرداد المبلغ» | «الكارت»، «الشيك أوت»، «الدليفري»، «الريفند» | Arabic words exist and are understood; use them. |
| «ريال»، «ر.س» | «SAR» inside an Arabic sentence | See the riyal sign in section 8. |
| «برمجيًا»، «في البرمجة»، «عند التطوير» | «الشيفرة»، «الشيفرة البرمجية» | «الشيفرة» reads as a cipher, not as code. Name the activity instead: «ضبط الاتجاه برمجيًا». «الكود» only in developer-facing copy. |
| «الزائر» | «الضيف» | In articles on hospitality and service (Jimmy, 4 Nov 2026). «الزوار» for the plural; «الضيافة» stays the name of the sector. |
| «نقاط تواصل» | «طبقة من التواصل» | The moments where a product speaks to the user (Ahlam Al Rouqi). |

## 3. Words that sound Egyptian or Levantine in a Saudi product

These read as foreign in Riyadh even when the reader understands them. Egyptian leaks most often, because it is the register many Arabic writers grew up with.

| Avoid | Egyptian or Levantine | Write instead |
|---|---|---|
| «عايز»، «عاوز» | Egyptian | «تريد» (MSA), «تبغى» or «تبي» (Saudi, consumer only) |
| «دلوقتي» | Egyptian | «الآن» (MSA), «الحين» (Saudi, consumer only) |
| «كده»، «إزاي»، «لسه» | Egyptian | «هكذا»، «كيف»، «لم … بعد» |
| «حضرتك» | Egyptian | Address the reader directly, or use a neutral construction |
| «بدّك»، «شو»، «هلّق»، «منيح» | Levantine | «تريد»، «ماذا»، «الآن»، «جيد» |
| «أوكي» | Borrowed | «حسنًا»، «تمام» |

## 4. The Saudi white dialect, when the brand allows it

A light, nationally understood Saudi register, closer to Najd and Hejaz than to any village speech. Use it as seasoning, not as the meal.

| Moment | Examples |
|---|---|
| Greeting | «هلا»، «يا هلا»، «حيّاك» |
| Acknowledging a request | «أبشر»، «تم» |
| Thanks | «يعطيك العافية»، «مشكور» |
| Light connectors | «الحين»، «زين»، «مرة» (very), «ترى» |

Rules: never in an error about money or data; never in consent or legal text; never half a sentence in dialect and half in MSA; written the same way every time (the brand's voice guide holds the list).

## 5. Address and gender

Arabic verbs and adjectives carry gender. A masculine default leaves out half the readers.

1. **Name the action, not the actor.** Buttons and labels as verbal nouns: «إرسال الطلب»، «تحديث البيانات».
2. **Use neutral constructions in instructions.** «يُرجى إدخال رقم الجوال» reads the same for everyone; «أدخل رقم الجوال» does not.
3. **Leave pronoun endings unvoweled.** «حسابك»، «لك»، «بك» are read correctly by both men and women as long as no vowel mark fixes them.
4. **Greet by name, not by «عزيزي».** «مرحبًا محمد» or «أهلًا بك» instead of «عزيزي العميل».
5. **When the product knows the reader's gender** (from the profile), address them correctly; never guess from a name.
6. **In articles and other long copy, write to one person, not to a group.** Ahlam Al Rouqi, Communication Lead: «دائمًا نخاطب المتلقي كشخص وليس كجمع». Write «تذكر»، «استخدمت»، «فاكتب»، «ابدأْ», and make every linked word follow, the closing line included: «بك» not «بكم», «منتجك» not «منتجكم». Open an example in the first person, which is also neutral: «لنفترض أن عميلًا…», not «تخيّلوا عميلًا…». Rules 1 and 2 still govern interface copy.

## 6. Arabic-first sentences

Translated Arabic has tells. Remove them.

| Tell | Instead |
|---|---|
| Subject first, English order: «طلبك تم إرساله» | Verb first: «أُرسل طلبك» |
| «قم بـ» + verbal noun: «قم بالضغط على زر الإرسال» | The verb itself: «اضغط إرسال» |
| «تم» + verbal noun on every confirmation | Use it sparingly; vary with the passive or a direct sentence: «حُفظت التغييرات»، «وصلنا طلبك» |
| «من خلال»، «بشكل سريع»، «سوف»، «حيث أن» | «عبر»، «بسرعة»، «سـ»، and cut «حيث أن» |
| Filler nouns: «عملية الدفع»، «خاصية البحث» | «الدفع»، «البحث» |
| Calques: «لا تتردد في التواصل معنا»، «اضغط هنا» | «تواصلوا معنا متى احتجتم»، a link that names its destination |
| «بل» after a negation: «لا تعتمد على السهولة وحدها، بل على…» | «وإنما»: «لا تعتمد على السهولة وحدها، وإنما على…» (Ahlam Al Rouqi) |
| «كما شرحنا في» before a link to another page | «كما هو موضح في» (Ahlam Al Rouqi) |
| An institution as the subject when the sentence works without it: «ما تريد المؤسسة قوله» | Cut it: «ما تريد قوله» (Ahlam Al Rouqi) |

## 7. Spelling that signals care

A Saudi reader judges an interface by its hamzas before its design.

- **Hamzat al-qat':** «إنشاء»، «إلى»، «أن»، «إدخال»، «إرسال». The bare alef in these words is the most common quality error in Arabic interfaces.
- **Alef maqsura and yeh:** «على»، «إلى»، «مستشفى»، «حتى».
- **Taa marbuta, not heh:** «الخدمة»، «الصفحة».
- **Tanween before the alef:** «شكرًا»، «حاليًا»، «مثلًا», the same way across the product.
- **Punctuation:** «،» «؛» «؟», no space before them, and «» for quotation.
- **Vowel marks only where they prevent a misreading:** «يُرجى»، «عُدّل». No shadda on a common verb the sentence already settles: «تدل»، «تمت»، «ترحب»، «توجه»، «تعثر» (Ahlam Al Rouqi). A word that could be read as another word keeps one mark: «تُعد» ("is considered"), so it isn't read as «تَعِد» ("promises").

## 8. Saudi formats

| Item | Format | Copy note | Source |
|---|---|---|---|
| Mobile number | `+966 5X XXX XXXX`; written locally as `05XXXXXXXX` | The field runs left to right. Accept Arabic-Indic and Western digits and convert them. | |
| National ID and Iqama | 10 digits; the first is 1 for citizens and 2 for residents | Label it «رقم الهوية الوطنية أو الإقامة» when both may apply. | SAMA rulebook |
| National Address | Short address: 4 letters and 4 digits; building number 4 digits; postal code 5 digits; additional number 4 digits | Ask for the short address first; offer the full form as a fallback. | Saudi Post (SPL) |
| IBAN | `SA` followed by 22 characters (24 in all) | Show it in groups of four, left to right. | |
| Currency | «ريال» or «ر.س» | The new riyal sign (U+20C1, approved February 2025, encoded in Unicode 17.0) appears only where the font supports it; SAMA asks for it to sit left of the number with a space. Otherwise write «ر.س». | SAMA; Unicode |
| Dates | Gregorian «م» and Hijri «هـ», Hijri on the Umm al-Qura calendar | Say which calendar a field expects. | |
| Week | Weekend Friday and Saturday; working days Sunday to Thursday | «أيام العمل من الأحد إلى الخميس» | |
| Time | «ص» and «م» for the 12-hour clock | | |

## 9. Numbers and plurals in dynamic text

Arabic has six plural forms (CLDR: zero, one, two, few, many, other). A string that concatenates a number and a noun is wrong in Arabic most of the time. Write every form in the localisation file.

| Form | Rule (last two digits) | «طلب» |
|---|---|---|
| zero | 0 | «لا توجد طلبات» |
| one | 1 | «طلب واحد» |
| two | 2 | «طلبان» |
| few | 3 to 10 | «3 طلبات» |
| many | 11 to 99 | «11 طلبًا» |
| other | 100 to 102, and the rest | «100 طلب» |

Use digits in interface text; spelled-out numbers from 3 to 10 reverse their gender and invite mistakes.

## 10. Occasions

- **Ramadan:** changed working hours and delivery times need their own copy, written before the month starts. Greetings: «رمضان مبارك»، «رمضان كريم».
- **Eid al-Fitr and Eid al-Adha:** «عيدكم مبارك»؛ say plainly what closes and when it reopens.
- **Saudi National Day (23 September) and Founding Day (22 February)** are two different days with two different meanings; never swap their names or their messages.
- **Commitments:** in transactional copy, give a concrete time or date. Keep phrases of faith for greetings, where they carry their meaning, not as a hedge on a delivery promise.

## 11. Government and regulated services

- The Digital Government Authority's Platforms Code is the national design reference for government platforms; follow its components and naming before inventing new ones.
- One name per service across the platform, the SMS, the email and the call centre script.
- Consent, privacy and PDPL wording is written with the legal owner, never by Azzam alone. Azzam makes the approved text readable; it does not change its meaning.

## 12. Across the Middle East

Saudi Arabia first. When a product reaches other markets:

- **Gulf (UAE, Kuwait, Qatar, Bahrain, Oman):** close to Saudi choices; swap local nouns (the national ID's name, the currency).
- **Egypt:** consumer apps commonly speak Egyptian Arabic; government and finance stay in MSA.
- **Levant:** MSA for anything formal; Levantine only for a local consumer brand.
- **Maghreb:** MSA with French loanwords in some markets; check the local convention for digits.

One product, one market voice. A pan-Arab product writes MSA with neutral vocabulary and localises only nouns and formats.

## 13. Review before it ships

1. Register right for the surface (section 1), and the same across the task?
2. No Egyptian or Levantine words (section 3)?
3. Gender-neutral where the reader is unknown, and one reader, not a group, in articles (section 5)?
4. Verb-first, no «قم بـ», no stacked «تم» (section 6)?
5. Hamzas, alef maqsura and taa marbuta correct, with no needless shadda (section 7)?
6. Saudi formats right, with left-to-right fields set (section 8)?
7. All six plural forms written for every dynamic count (section 9)?
8. One name per service, matching the string bank?
9. The `jee-arabic` checker passes, or the Arabic rules in the string bank where it is not installed?
10. Read aloud by someone who grew up in Saudi Arabia: does it sound like home?
