# The AI-writing audit

A reader who senses machine-made text stops trusting it, and so does a reviewer. Every piece gets this audit at the gate, in both languages, after the English is written. The audit finds the habit; the fix is a rewritten sentence, never one swapped word.

## English

Load the `avoid-ai-writing:avoid-ai-writing` skill with the Skill tool and run it on the English text, by its script and by hand.

- Check tier 1 and tier 2 words, em dashes, hedges, intensifiers, "not X, it's Y", groups of three, and repeated "So…" or "That's why…" openers.
- Report sentence length as mean and standard deviation. Varied is good.
- The skill reads English only. Never run it on Arabic.
- If the skill is not installed, say so in one line and audit by hand against the no-AI-tells mechanics in `azmx-brand`'s `references/voice-and-tone.md`.

## Arabic, by hand

- Look for these words: «يُعد»، «يلعب دورًا»، «من خلال»، «في ظل»، «علاوة على ذلك»، «بشكل كبير»، «بل».
- Count groups of three.
- Count the sentences that open with one of these words: «لذلك»، «لهذا».
- Then run the review in `saudi-arabic-ux.md`, section 13.

## Both languages

- **The pull quote** must not repeat a body sentence. It is a common tell, and it has happened twice.

## What to hand over

With the draft, give Jimmy the counts for each language before and after the fixes, and the lines that changed. A piece with open findings does not pass the gate.

## Background

Google doesn't penalise AI-assisted text as such (Search Central, 8 February 2023). It rewards original, sourced, helpful pages with a real byline. AI detectors misfire on edited and non-native text, so a detector's score is not the test; this audit and the gate are.
