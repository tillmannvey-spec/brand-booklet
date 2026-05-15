---
name: brand-booklet
description: Use when creating, refining, rebranding, or optimizing a visual brand identity — whether from scratch with no references, from inspiration/reference brands, evolving an existing brand, or aligning brand assets to an existing website. Produces strategy (positioning, archetype, tone of voice), visual system (color, typography, shape language), full asset set (logos, patches, stickers, marketing visuals), brand documentation, and design-system.md for downstream coding. Trigger on "brand booklet", "brand identity", "create brand", "design a logo", "rebrand", "brand refresh", "redesign brand", "brand for [company]", "brand system", "visual identity", "logo system", "brand assets", "style guide", "corporate design", "neue marke", "rebranding", "markenidentität", "brand kit".
---

# Brand Booklet

> Strategy before pixels. Mode-routed intake. Asset generation driven by output medium.

## Required dependencies

- `fal-media-generator` skill at `~/.claude/skills/fal-media-generator/` — generation runtime
- Optional `brand-auditor` skill at `~/.claude/skills/brand-auditor/` — Phase 7 quality audit
- Cross-skill reference files (read on demand):
  - `~/.claude/skills/Branding Skill/references/archetypes.md` — 12 Jungian archetypes
  - `~/.claude/skills/Branding Skill/references/tone-of-voice.md` — TOV framework
  - `~/.claude/skills/Branding Skill/references/naming-framework.md` — naming methodology (only if brand needs a name)

## Always-loaded local references

- `references/prompt-patterns.md` — read BEFORE any fal command (5-layer prompt structure, model selection)
- `references/design-knowledge.md` — LIFT system, 12 grid archetypes (read in Phase 3)
- `references/booklet-template.md` — fill in Phase 8

## Model discipline (HARD RULES)

**Model: `gpt-image-2` für ALLES — keine Ausnahmen.**

Kein Wechsel zu `nano-banana-pro`, `ideogram-v3`, `flux-*` oder anderen Modellen. Auch nicht für Marketing-Heros. Auch nicht für Color-Palette-Visualisierungen. Wenn das Modell nicht reicht: Prompt verbessern, nicht Modell wechseln.

**Mode:**
- **T2I** (kein `--image_url`) — **NUR** für das allererste Asset (Primary Logo in Scratch/Inspired wenn keine Referenz existiert)
- **Edit-Mode** (`--image_url` mit Primary Logo CDN-URL) — für **alle anderen Assets**. Kohärenz ist nicht verhandelbar.

**Quality-Regel:**

| Asset-Typ | Quality | Begründung |
|---|---|---|
| Hero (16:9), OG-Card, große Marketing-Visuals, Pattern-Backgrounds, alles was auf >50% Viewport-Width angezeigt wird | `--quality high` | Skaliert auf große Anzeige, jede Pixel-Schwäche sichtbar |
| Primary Logo (allererste T2I-Generation) | `--quality high` | Anchor-Asset, alle Edits hängen davon ab |
| Alle Logo-Varianten (horizontal, vertical, monogram, dark, app-icon, 1-color, signature) | `--quality medium` | Edit-Mode, Anker steht schon, mittel reicht |
| Favicon | `--quality medium` | Wird sowieso auf 16–32px komprimiert |
| Patches, Stickers | `--quality medium` | Kleine Anzeigegrößen, Print-Tauglichkeit reicht bei medium |
| Square 1:1, Story 9:16 Social | `--quality medium` | Werden auf Phone-Screens konsumiert, medium ausreichend |
| Color-Palette-Visualisierung, Type-Specimen | `--quality medium` | Funktionale Visualisierung, kein Hero |
| App-Screenshot-Frame (SaaS) | `--quality medium` | Mockup-Frame, nicht der Star |

**Faustregel:** "Wird das groß angezeigt (>50% Viewport oder >800px Renderbreite)?" → `high`. Sonst → `medium`. Im Zweifel: `medium`.

`--quality low` nie verwenden außer User fordert explizit Throwaway-Drafts.

---

## Phase 0 — Preflight & Mode Router

### Preflight (silent)

```bash
ls ~/.claude/skills/fal-media-generator/scripts/generate.py
```
Missing → tell user: "fal-media-generator skill nicht gefunden. Bitte installieren unter `~/.claude/skills/fal-media-generator/`."

Read `references/prompt-patterns.md` now — it stays in context for the full session.

### Mode Router (ask user)

This is the single most important question of the workflow. Ask it first, do not skip:

```
Welcher Modus passt zu deinem Projekt?

1. SCRATCH    — Neue Marke, keine konkreten Referenzen. Brauchst Richtungsfindung.
2. INSPIRED   — Neue Marke, du hast Referenzen (Brands, Designer, Stil-Wünsche).
3. REBRAND    — Bestehende Marke soll erneuert werden. Equity erhalten, Drift entfernen.
4. OPTIMIZE   — Bestehende Website existiert. Brand-Assets sollen mit ihr alignen oder Lücken schließen.
```

Wait for answer. Branch to the matching Phase 1 variant. Do not run a generic intake.

---

## Phase 1 — Intake (mode-specific)

### Mode SCRATCH → Strategic intake + brainstorm

Ask these 10 questions, **one at a time** (not as a bulk form):

1. **One-liner:** Wie beschreibst du diese Marke einem Fremden in einem Satz?
2. **Enemy:** Wogegen steht diese Marke? (Konkret — nicht "schlechter Service")
3. **Audience:** Beschreib deinen idealen Kunden als echte Person (Alter, Job, Frust, Geschmack)
4. **Feeling:** Was soll jemand 5 Sekunden nach dem ersten Kontakt fühlen?
5. **Competitors:** Nenne 2–3 Konkurrenten. Was machen sie visuell, das du **vermeiden** willst?
6. **Aspiration:** Nenne 1–3 Marken (egal welche Branche), deren Ästhetik du bewunderst. Konkret was?
7. **Constraint:** Was muss bleiben? (Bestehendes Logo, Mutterkonzern, Legal)
8. **Stage:** Startup MVP / etabliertes Unternehmen / Rebrand / Extension?
9. **Outputs:** Was brauchst du wirklich? (Guidelines / Figma / Web-Assets / alles)
10. **Timeline:** Wann muss es fertig sein?

**Brainstorm-Fallback (only if Q6 is empty or vague):**

Don't proceed. Spawn a brainstorm subagent:

```
Read ~/.claude/skills/Branding Skill/references/archetypes.md.
The user has no aesthetic references. Their brand brief so far:
[paste answers Q1-Q5, Q7-Q10]

Generate 5 distinct aesthetic territories, each with:
- Memorable name (e.g., "Brutalist Authority", "Nordic Restraint", "Editorial Warmth")
- Primary archetype + secondary tension
- 3 real-world references (specific designers / brands / movements / eras — never generic)
- One-sentence visual fingerprint
- Why this fits the user's brief

Return as a numbered list. Force genuine tension between options — no three variations of "minimalist".
```

Present options to user, wait for pick. The picked territory feeds Phase 2.

### Mode INSPIRED → Reference deconstruction

User provides references (links, screenshots, brand names, designer names).

1. Read/analyze each reference. If URLs: use `firecrawl-scrape` or `claude-design-clone` skills to extract visual tokens.
2. For each reference, extract: shape language, color logic, type approach, mood, composition rules.
3. Find the **common DNA** across all references — that's the user's actual taste signal.
4. Run shortened 5-question intake (skip Q5, Q6 — user already gave references):
   - Q1 One-liner
   - Q2 Enemy
   - Q3 Audience
   - Q4 Feeling
   - Q7 Constraint
   - Q9 Outputs

Output: Reference Synthesis paragraph + 5-Q answers → feeds Phase 2.

### Mode REBRAND → Audit + evolution path

1. **Audit existing brand:**
   - If `brand-auditor` skill installed: spawn as subagent on existing `./brand/` or pasted assets.
   - Otherwise: Read existing logo, site, materials via Read tool. Score against `templates/critique-checklist.md`.
2. **Identify equity** (what to preserve):
   - Brand name?
   - Color (one anchor color)?
   - Mark/symbol (full keep / silhouette keep / reset)?
   - Type (font family)?
3. **Identify drift** (what to drop):
   - AI clichés
   - Outdated style cues
   - Off-positioning visuals
4. **Define evolution path:** ask user explicitly:
   - **Refresh** — keep mark, modernize execution (90% retention)
   - **Evolution** — keep name + one anchor element, rebuild system (40% retention)
   - **Reset** — keep name only, rebuild everything (10% retention)
5. **Targeted strategy intake** (5 questions focused on new direction):
   - What's wrong with the current brand? (Be specific)
   - What customer perception are you fixing?
   - Aspiration brands for the new direction?
   - Hard constraints (what must NOT change)?
   - Timeline?

### Mode OPTIMIZE → Site audit + gap analysis

1. **Site audit** (need URL or local path):
   - If URL: use `firecrawl-scrape` or browser tools to extract current design tokens.
   - If local code: read CSS variables, `tailwind.config.*`, design tokens, brand assets.
   - Extract: current palette (hex), fonts, logo files, brand voice (from copy).
2. **Gap analysis** — find what's missing or off:
   - Missing logo variants? (favicon, dark mode, social card)
   - Color drift between sections?
   - Off-brand sections (stock photo islands, generic CTAs)?
   - Aspect-ratio gaps for marketing channels?
3. **Targeted asset manifest** — don't regenerate everything. Build a focused list of 3–8 assets to fix specific gaps.
4. **Skip directly to Phase 5** with the targeted manifest. No new strategy work needed if site already has a brand.

---

## Phase 2 — Direction Setting (Skip in OPTIMIZE mode)

This phase exists because users in SCRATCH/INSPIRED/REBRAND modes need to commit to **one** direction before any pixels are generated. Today's failure mode: skill commits to a logo before strategy is locked.

Generate **2–3 distinct visual territories** with real aesthetic tension. NOT three variations of "minimalist clean".

For each territory, define:

| Field | Example |
|---|---|
| **Name** | "Brutalist Authority" / "Nordic Restraint" / "Playful Precision" |
| **Archetype primary + secondary** | Sage + Outlaw (tension creates personality) |
| **Color logic** | Intent only — "high-contrast monochrome + one electric accent" |
| **Typography intent** | "Industrial display sans + monospace body" (no font names yet) |
| **Shape language** | Geometric / organic / mixed — and what specifically |
| **Real references** | Designers, movements, eras, real brands (specific, never generic) |
| **Trade-off statement** | "Wins on X, sacrifices Y" — force a real choice |

Read `~/.claude/skills/Branding Skill/references/archetypes.md` and `~/.claude/skills/Branding Skill/references/tone-of-voice.md` before generating territories.

**Gate:** Present territories to user. User picks ONE. Do not offer 5 more variants. If user rejects all, return to Phase 1 — the strategy is unclear.

---

## Phase 3 — Visual System (no images yet)

Now commit picked territory to concrete specs. Read `references/design-knowledge.md` for LIFT framework + 12 grid archetypes.

**LIFT analysis** (from picked territory):
- **L — Leverage-Asset:** strongest visual element to build the system around
- **I — Internal Rhythm:** visual cadence across all assets
- **F — Friction Sources:** what would make this brand feel generic
- **T — Transferability:** what breaks at 32px / on dark backgrounds

**Define exactly:**

```
Colors (6 hex codes):
  --color-bg          Primary background, sets mood
  --color-surface     Cards, sections
  --color-text        Primary text — must hit 7:1 contrast on bg
  --color-text-muted  Secondary text — 4.5:1 minimum
  --color-accent-1    Signature color
  --color-accent-2    Tension with accent-1

Typography:
  --font-display      Headlines. Personality. NEVER Inter/Poppins/Montserrat/Roboto/Open Sans.
  --font-body         Body. Readable.
  (Google Fonts only unless user specifies)

Type scale (clamp values):
  display, h1, h2, h3, body, small, button

Shape language:
  radius scale, stroke weight policy, corner treatment

Voice:
  3 words IS / 3 words IS-NOT + 1 in-brand sentence + 1 off-brand sentence
```

Write `./brand/00_plan.md` with all of the above + asset manifest (filled in Phase 4).

**Gate:** Show user the system. They approve color + type + voice before any image generation. This gate prevents 90% of regeneration loops.

---

## Phase 4 — Output Medium → Asset Manifest

ONE question:

```
Wofür wird die Marke primär eingesetzt?

A. Website — welcher Typ?
   A1. Landing Page (Marketing, Hero-driven)
   A2. SaaS App / Dashboard
   A3. E-Commerce
   A4. Editorial / Blog / Content-heavy
   A5. Portfolio / Showcase
B. Print only
C. Social Media first
D. Mehrere (alles)
```

The answer **filters the asset manifest**. Don't generate stickers and patches for a SaaS brand that has no use for them.

### Default asset manifest by medium

| Medium | Logos | Patches | Stickers | Marketing | Extras |
|---|---|---|---|---|---|
| A1 Landing | primary, horizontal, vertical, monogram, favicon, dark-variant | — | optional ×2 | hero 16:9, square 1:1, story 9:16 | OG card, web pattern |
| A2 SaaS | primary, monogram, favicon, app-icon (rounded square), dark-variant | — | — | square 1:1 | chart palette, empty-state illustration direction |
| A3 E-Commerce | primary, horizontal, monogram, favicon | round, wordmark | ×3 | hero 16:9, square 1:1, story 9:16 | product BG pattern, packaging mockup direction |
| A4 Editorial | primary, horizontal, monogram, favicon | — | — | hero 16:9, story 9:16 | drop-cap font spec, byline mark, photo direction |
| A5 Portfolio | primary, monogram, signature mark, favicon | — | optional ×2 | square 1:1, story 9:16 | cursor variants, case-study cover template |
| B Print | primary, horizontal, vertical, monogram, 1-color | round, shield, wordmark | ×3 | — | CMYK conversion check, business card mockup |
| C Social | primary, square-locked, monogram, favicon | — | ×4 (full verb-trio) | square 1:1, story 9:16, profile 1:1 | sticker pack, IG highlight covers |
| D Alle | full default set | full | full | full | full |

Filter the manifest into `./brand/00_plan.md`. Show the user the final list. Confirm before generation.

---

## Phase 5 — Primary Logo (BLOCKING GATE)

Spawn ONE subagent. Everything else waits.

Build the 5-layer prompt using `references/prompt-patterns.md` → "Primary Logo Template". Adapt each layer to the locked strategy + visual system from Phase 3.

**Subagent instruction:**

```
Read ~/.claude/skills/brand-booklet/references/prompt-patterns.md.
Build a 5-layer logo prompt from the visual system + picked territory below.
Use gpt-image-2 T2I (no --image_url — primary logo has no reference yet).

Visual system: [paste Phase 3 specs]
Picked territory: [paste Phase 2 winning territory]
LIFT analysis: [paste from 00_plan.md]

Command:
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "[your 5-layer prompt]" \
  --image_model gpt-image-2 \
  --aspect_ratio 1:1 \
  --quality high \
  --num_images 3

Output files are in ./fal-outputs/images/.
Pick the best variant. Copy to ./brand/01_logos/primary_v1.png.
Write ./brand/01_logos/primary_v1.meta.json with prompt, model, variant_selected.
Return: path to primary_v1.png + winning prompt text.
```

**REBRAND mode adjustment:** If user chose "Refresh" or "Evolution" evolution path, generate the primary with Edit-Mode using the **old logo** as `--image_url`. The new logo evolves from the old.

**OPTIMIZE mode:** Skip Phase 5 unless primary logo is in the gap list.

**After subagent completes:**
1. Read `./brand/01_logos/primary_v1.png` — Claude shows it inline.
2. **HARD STOP.** Say: "Hier ist dein Primary Logo. Wie weiter?"
   - Approve → Phase 6
   - Iterate → regenerate with adjusted prompt (max 3 attempts)
   - Change direction → return to Phase 2

---

## Phase 6 — Parallel Asset Generation

Only start after primary logo is approved.

**Upload primary logo for I2I reference:**

```python
import fal_client, os
os.environ["FAL_KEY"] = "YOUR_FAL_KEY"
url = fal_client.upload_file("./brand/01_logos/primary_v1.png")
print(url)  # → PRIMARY_LOGO_URL for all subagents
```

Spawn subagents in parallel, **but only for categories in the filtered asset manifest from Phase 4**. Each subagent receives: filtered manifest slice, brand brief, visual system, PRIMARY_LOGO_URL.

**All subagents use `gpt-image-2` Edit-Mode with PRIMARY_LOGO_URL.** No model switching. Quality per table below.

### Subagent A — Logo Variants

Variants, aspect ratios, quality:

| File | AR | Quality | Notes |
|---|---|---|---|
| `horizontal_v1.png` | 16:9 | `medium` | Text lockup beside symbol |
| `vertical_v1.png` | 1:1 | `medium` | Stacked |
| `monogram_v1.png` | 1:1 | `medium` | Symbol only |
| `favicon_v1.png` | 1:1 | `medium` | Ultra-simplified for 16–32px |
| `dark_v1.png` | 1:1 | `medium` | Inverted for dark BG |
| `app_icon_v1.png` (SaaS) | 1:1 | `medium` | Rounded-square iOS/Android |
| `1color_v1.png` (Print) | 1:1 | `medium` | Single-ink version |
| `signature_v1.png` (Portfolio) | 1:1 | `medium` | Hand-style mark |

For each: build edit prompt, run fal command with `--image_model gpt-image-2 --image_url $PRIMARY_LOGO_URL --quality medium`, copy to `./brand/01_logos/`, write `.meta.json`.

### Subagent B — Patches (only if in manifest)

3 patches: `round_v1.png`, `shield_v1.png`, `wordmark_v1.png`. All `--quality medium`. See `references/prompt-patterns.md` → "Patch Template".

### Subagent C — Stickers (only if in manifest)

One per verb in verb-trio + optional monogram sticker. All `--quality medium`. See `references/prompt-patterns.md` → "Sticker Template".

### Subagent D — Marketing + Color + Typography Visualization

Manifest-driven, all `gpt-image-2` Edit-Mode:

| File | AR | Quality | Notes |
|---|---|---|---|
| `hero_16x9_v1.png` | 16:9 | **`high`** | Hero — wird groß auf Landing-Page angezeigt |
| `og_card_v1.png` (Landing) | 16:9 | **`high`** | Social-Share-Preview, prominent gerendert |
| `product_pattern_v1.png` (E-Commerce) | 1:1 | **`high`** | Repeatable BG, deckt große Flächen |
| `square_1x1_v1.png` | 1:1 | `medium` | Social-Feed-Größe |
| `story_9x16_v1.png` | 9:16 | `medium` | Mobile-Phone-Größe |
| `app_screenshot_frame_v1.png` (SaaS) | 16:9 | `medium` | Mockup-Frame, supporting visual |
| `./brand/06_color/palette_v1.png` | 16:9 | `medium` | Funktionale Swatch-Visualisierung |

Also write (no image):
- `./brand/06_color/tokens.json` — full JSON with all hex codes
- `./brand/05_typography/typography_spec.md` — markdown spec

Each subagent returns JSON: `{assets: [{path, ok}], errors: []}`.

---

## Phase 7 — Audit

If `brand-auditor` skill is installed at `~/.claude/skills/brand-auditor/`:

```
Spawn brand-auditor subagent on ./brand/.
It will:
- Score each asset 0-20 on professional criteria
- Identify color drift, style fragmentation, verb gaps
- Auto-regenerate failing assets (score <12) with revised prompts
- Write ./brand/00_review.md
```

If not installed, run inline using `templates/critique-checklist.md`:
- Score each asset 0–8
- ≥6 pass · 3–5 iterate · <3 reject
- Max 2 iterations per asset
- If consistent 4–5 ("too safe") → invoke `/impeccable:bolder` with failing asset + brief

Log to `./brand/00_review.md`.

---

## Phase 8 — Documentation

Write **4 files**:

### 1. `./brand/Brand-Booklet.md` (≥200 lines)

Read `references/booklet-template.md` and fill completely. Required sections:
1. Brand Strategy (positioning, archetype, LIFT, anti-positioning)
2. Tone of Voice (with example copy)
3. Logo System (variants, usage, clear space, min sizes)
4. Color System (with WCAG contrast)
5. Typography (scale, pairing rationale, print vs. screen)
6. Patch & Sticker System (if in manifest)
7. Marketing Templates (format specs per channel)
8. Do/Don't Gallery (5 concrete examples)
9. Asset Manifest (table of all files)

### 2. `./brand/Brand.md` (≤80 lines)

One-pager. Mission · Verb-Trio · Colors · Typography · Canonical logo path · 3 hard rules.

### 3. `./brand/design-system.md` (replaces brand-to-code skill)

Production-ready design tokens for downstream coding agents. Required sections:

```markdown
## 1. Brand Context (1 paragraph — sets the vibe for the coding AI)

## 2. CSS Custom Properties
:root {
  --color-bg, --color-surface, --color-text, --color-text-muted, --color-accent-1, --color-accent-2
  --font-display, --font-body
  --space-xs through --space-2xl (modular scale)
  --radius-sm, --radius-md, --radius-lg
  --shadow-sm, --shadow-md, --shadow-lg
  --ease-default, --duration-fast/normal/slow
}

## 3. Typography Scale (clamp values, weights, letter-spacing, line-height)

## 4. Component Patterns (buttons, cards, sections, nav, hero, forms — hover/active/focus states)

## 5. Animation & Motion (easing curve + why, hover duration, scroll-trigger style, what NEVER animates)

## 6. Layout Rules (max-width, grid columns/gap, section spacing, breakpoints)

## 7. Anti-Patterns (CRITICAL — 10+ specific prohibitions: no centered-everything, no blue-purple gradient,
   no generic card grids, no Tailwind defaults, etc. + brand-specific)

## 8. Tailwind Config Extension (copy-paste ready)

## 9. Google Fonts Import (link tag with exact weights)
```

This file is what `frontend-design`, `design-html`, `landing-page-design` skills consume downstream.

### 4. `./brand/AGENTS.md`

Delegate to Haiku subagent:

```
Run: python ~/.claude/skills/brand-booklet/scripts/build_asset_index.py ./brand/
Read ~/.claude/skills/brand-booklet/templates/agents-md-template.md.
Fill with: asset index table, canonical logo path, color tokens path,
typography spec path, locked assets list.
Write to ./brand/AGENTS.md.
```

---

## Output Checklist

Before declaring done:
- [ ] Mode router was answered (Scratch / Inspired / Rebrand / Optimize)
- [ ] Strategy intake completed (10 / 5 / targeted questions per mode)
- [ ] Visual territories presented + ONE picked (Scratch/Inspired/Rebrand only)
- [ ] `./brand/00_plan.md` exists with LIFT + colors + type + manifest
- [ ] Output medium question answered → manifest filtered
- [ ] Primary logo approved by user
- [ ] All manifest assets generated + `.meta.json` written
- [ ] `./brand/00_review.md` exists with scores
- [ ] `./brand/Brand-Booklet.md` ≥200 lines
- [ ] `./brand/Brand.md` ≤80 lines
- [ ] `./brand/design-system.md` with all 9 sections, anti-patterns list ≥10 items
- [ ] `./brand/AGENTS.md` with asset inventory table

Show user the primary logo + summary of what was created + concrete next step:
- Landing page? → "Run `/frontend-design` or `/design-html` with `design-system.md` as input"
- Full site? → "Run `/landing-page-design` or `/interactive-portfolio`"
- Audit later? → "Run `/brand-auditor` anytime to re-score and improve"

---

## Common Failure Modes

| Symptom | Root Cause | Fix |
|---|---|---|
| User unhappy with logo after generation | Skipped Phase 2 (direction setting) | Re-run from Phase 2 with 2-3 territories |
| Assets look like 3 different brands | Skipped Phase 3 gate (visual system not locked) | Lock system, regenerate via Edit-Mode |
| Generated stickers for a SaaS brand nobody wanted | Skipped Phase 4 (output medium) | Filter manifest, delete unused categories |
| Rebrand drifts too far from original | Used T2I for primary instead of Edit-Mode on old logo | Re-run Phase 5 with old logo as `--image_url` |
| design-system.md is too generic | Skipped Phase 3 (didn't define colors/type concretely before generation) | Always finish Phase 3 before Phase 5 |

---

## Notes

- Never overwrite approved assets. New iterations use `_v2`, `_v3`, etc.
- The Mode Router is non-negotiable. Don't run a generic intake "to save time" — the modes diverge sharply after question 1.
- `brand-to-code` skill is **superseded** by Phase 8 → `design-system.md`. You can deprecate that skill once this one is verified.
- `Branding Skill` (brand-architect) is **superseded** by Phases 1–3. You can deprecate after verification.
- `brand-auditor` remains separate — it's a standalone audit tool, invoked here in Phase 7 but also runs independently.
