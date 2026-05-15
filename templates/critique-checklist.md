# Visual Critique Checklist

Apply this checklist to every generated PNG in Phase D.
Score 1 point for each YES. 0–8 total.

---

## The 8 Checks

**Check 1 — Thumbnail-Readable (30px test)**
> If this asset were shrunk to 30×30px, would the main element still be recognizable?
- YES (1pt): The core symbol/text reads at tiny sizes
- NO (0pt): The design relies on fine details that disappear at small sizes

**Check 2 — Verb-True**
> Does this asset visually embody at least one of the brand's three verbs?
- YES (1pt): Someone seeing this asset would feel the energy of [verb1] / [verb2] / [verb3]
- NO (0pt): The visual is generic and could belong to any brand

**Check 3 — Negative Space**
> Is there intentional breathing room that gives the design weight?
- YES (1pt): White/empty space is used deliberately, not accidentally
- NO (0pt): Elements are crammed, or the space is uniform and boring

**Check 4 — Color Harmony**
> Do the colors feel intentional and consistent with the brand brief?
- YES (1pt): Colors match the specified palette, feel cohesive
- NO (0pt): Off-palette colors snuck in, or the color combination is muddy/clashing

**Check 5 — No AI Cliché**
> Is this asset free from the most common AI-generated brand design failures?
Check for: gradient orbs, generic globes, circuit boards, upward arrows, trite lightbulbs, lens flares, rainbow gradients on dark backgrounds.
- YES (1pt): Clean of all AI tells
- NO (0pt): One or more AI anti-patterns are visible

**Check 6 — Print-Capable**
> Could this asset be reproduced in print without loss of impact?
- YES (1pt): Solid colors (not gradients), sufficient contrast, no RGB-only neon
- NO (0pt): Design relies on screen-only effects that would print poorly

**Check 7 — Consistent with Primary**
> Does this asset feel like it belongs to the same brand system as the primary logo?
- YES (1pt): Same color language, same visual energy, same style register
- NO (0pt): Looks like it came from a different brand

**Check 8 — Off-Limits Respected**
> Is the asset free of everything listed in the brand's hard off-limits?
- YES (1pt): Nothing prohibited is visible
- NO (0pt): At least one off-limits element appears

---

## Scoring & Action

| Score | Grade | Action |
|---|---|---|
| 7–8 | Pass | Accept. Log as "pass" in 00_review.md |
| 5–6 | Soft Pass | Accept with note. Suggest iteration in next version |
| 3–4 | Iterate | Regenerate. Include critique in the new prompt: "The previous version failed [check X] because [reason]. Avoid this by [instruction]." |
| 0–2 | Reject | Rebuild prompt from scratch. Return to LIFT analysis and rebuild the 5-layer prompt entirely. |

**Maximum 2 iterations per asset.** After 2 failures, escalate to the user with the failed assets shown side-by-side and ask for direction.

---

## Escalation: When to Invoke impeccable:bolder

If multiple assets pass the checklist but feel **visually safe, generic, or forgettable** — technically correct but aesthetically flat — invoke `/impeccable:bolder` with this brief:

```
These brand assets score well on the critique checklist but lack visual boldness.
The brand verbs are: [verb1] / [verb2] / [verb3].
The brand personality is: [mood adjectives].
Looking at [specific asset], what specific changes would make it more distinctive,
memorable, and true to the brand's energy? Focus on: composition, color intensity,
symbol treatment, typographic weight, negative space use.
```

Use impeccable:bolder's output as prompt guidance for the next regeneration round — it's a prompt co-pilot for boldness, not a replacement for the image generation step.

---

## Logging Format

In `./brand/00_review.md`:

```markdown
## [filename]
**Score:** [X]/8
**Checks failed:**
- Check [N]: [reason it failed]
**Action:** [pass / iterate with adjustment / reject and rebuild]
**Notes:** [any relevant observation for the brand booklet's Do/Don't Gallery]
```
