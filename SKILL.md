---
name: brand-booklet
description: Use when creating, refining, rebranding, or optimizing a visual brand identity — whether from scratch with no references, from inspiration/reference brands, evolving an existing brand, or aligning brand assets to an existing website. Produces strategy (positioning, archetype, tone of voice), visual system (color, typography, shape language), full asset set (logos, patches, stickers, marketing visuals), brand documentation, design-system.md for downstream coding, and a presentation-ready Brand-Booklet HTML + PDF. Trigger on "brand booklet", "brand identity", "create brand", "design a logo", "rebrand", "brand refresh", "redesign brand", "brand for [company]", "brand system", "visual identity", "logo system", "brand assets", "style guide", "corporate design", "neue marke", "rebranding", "markenidentität", "brand kit".
---

# Brand Booklet

> Strategy before pixels. Mode-routed intake. Asset generation driven by output medium. **Checkpoint after every phase** so the workflow is safe to abort and resume. Ends with a presentation-ready HTML booklet + PDF.

## Required dependencies

- `fal-media-generator` skill at `~/.claude/skills/fal-media-generator/` — generation runtime
- `high-end-visual-design` skill at `~/.claude/skills/high-end-visual-design/` — Phase 9 HTML design language
- `claude-taste` skill at `~/.claude/skills/claude-taste/` — Phase 9 independent design review
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

## Folder Structure (PFLICHT)

Jedes Brand-Projekt schreibt **alle** Outputs in diese Struktur unter `./brand/`. Nie ad-hoc-Pfade verwenden. Nie Phasen-Outputs überspringen. Die Struktur ist der Wahrheits-Ort und macht den Workflow **resume-fähig**.

```
./brand/
├── 00_session.md            ← LIVE PROGRESS LOG — nach JEDER Phase updaten
├── 00_plan.md               ← Master-Strategie (Strategy + System + Manifest)
├── 00_review.md             ← Asset-Audit-Scores (Phase 7)
│
├── 01_intake/               ← Phase 1
│   ├── mode.md              ← Gewählter Modus + Begründung
│   ├── answers.md           ← Roh-Antworten User
│   ├── references.md        ← (nur INSPIRED) Reference-Synthese
│   └── audit.md             ← (nur REBRAND/OPTIMIZE) Audit-Befunde
│
├── 02_direction/            ← Phase 2 (skip in OPTIMIZE)
│   ├── territories.md       ← Alle 2–3 vorgestellten Territories
│   └── picked.md            ← Gewähltes Territory + Trade-off
│
├── 03_system/               ← Phase 3
│   ├── lift.md              ← LIFT-Analyse
│   ├── colors.md            ← 6 Hex + Rolle + Rationale
│   ├── typography.md        ← Display/Body + Scale + Rationale
│   ├── shape.md             ← Radien, Stroke, Corner-Logic
│   └── voice.md             ← TOV: IS / IS-NOT + Beispiele
│
├── 04_manifest/             ← Phase 4
│   ├── medium.md            ← Output-Medium-Antwort + Begründung
│   └── manifest.md          ← Gefilterte Asset-Liste
│
├── 05_logo_primary/         ← Phase 5
│   ├── primary_v1.png
│   ├── primary_v1.meta.json
│   └── primary_v1.prompt.md ← Voller 5-Layer-Prompt
│
├── 06_logo_variants/        ← Phase 6 / Subagent A
│   ├── horizontal_v1.png    + .meta.json
│   ├── vertical_v1.png      + .meta.json
│   ├── monogram_v1.png      + .meta.json
│   ├── favicon_v1.png       + .meta.json
│   ├── dark_v1.png          + .meta.json
│   └── (app_icon/1color/signature je nach Medium) + .meta.json
│
├── 07_patches/              ← Phase 6 / Subagent B (nur wenn in Manifest)
├── 08_stickers/             ← Phase 6 / Subagent C (nur wenn in Manifest)
├── 09_marketing/            ← Phase 6 / Subagent D (hero, og, square, story, ...)
│
├── 10_color/
│   ├── palette_v1.png       ← Visualisierung
│   └── tokens.json          ← Voll-JSON aller Hex-Codes + Roles
│
├── 11_typography/
│   └── typography_spec.md   ← Markdown-Spec (optional specimen.png)
│
├── 12_docs/                 ← Phase 8 — finale Markdown-Doku
│   ├── Brand-Booklet.md     ← Long-form (≥200 Zeilen)
│   ├── Brand.md             ← One-Pager (≤80 Zeilen)
│   ├── design-system.md     ← Tokens für Coding-Agents
│   └── AGENTS.md            ← Asset-Inventory + Locked-Assets
│
└── 13_booklet/              ← Phase 9 + 10 — Präsentation
    ├── booklet.html         ← /high-end-visual-design Output
    ├── booklet.pdf          ← Final, präsentier-fertig
    ├── assets/              ← Kopien aller im Booklet referenzierten Assets
    ├── design-notes.md      ← Notes aus /claude-taste Review
    └── build.log            ← Render- und PDF-Export-Log
```

**Resume-Regel:** Bei jedem Skill-Start prüfen ob `./brand/00_session.md` existiert. Wenn ja → letzte abgeschlossene Phase lesen und dort fortsetzen. Sonst: bei Phase 0 starten.

---

## Checkpoint Discipline (PFLICHT)

Nach **jedem** Phasen-Ende — bevor zur nächsten Phase übergegangen wird — diese drei Schritte ausführen:

1. **Phase-Outputs schreiben** in die für die Phase vorgesehenen Files (siehe oben).
2. **`00_session.md` aktualisieren** (Append, nicht überschreiben):
   ```markdown
   ## Phase N — <Name> · <YYYY-MM-DD HH:MM>
   Status: complete | partial | blocked
   Key decisions:
   - <decision 1>
   - <decision 2>
   Files written/updated:
   - <path 1>
   - <path 2>
   Next phase: <N+1 name>
   Resume hint: <one sentence describing where to pick up>
   ```
3. **(Wenn die Phase strategie- oder system-relevant war:)** `00_plan.md` incrementell mit-aktualisieren — Phase 1 schreibt den Strategie-Block, Phase 2 das Picked-Territory, Phase 3 das volle Visual-System, Phase 4 die finale Manifest-Tabelle.

Wenn der User abbricht → kein Datenverlust. Wenn der Skill neu startet → `00_session.md` lesen und fortsetzen.

---

## Phase 0 — Preflight & Mode Router

### Preflight (silent)

```bash
ls ~/.claude/skills/fal-media-generator/scripts/generate.py
ls ~/.claude/skills/high-end-visual-design/SKILL.md
ls ~/.claude/skills/claude-taste/SKILL.md
```
Missing → tell user which skill needs to be installed.

Read `references/prompt-patterns.md` now — it stays in context for the full session.

**Resume-Check:** Wenn `./brand/00_session.md` existiert → lies es. Frage den User: "Resume bei Phase X — oder neu starten?"

### Folder bootstrap (silent)

Wenn `./brand/` nicht existiert: Verzeichnisstruktur anlegen.

```bash
mkdir -p ./brand/01_intake ./brand/02_direction ./brand/03_system ./brand/04_manifest \
         ./brand/05_logo_primary ./brand/06_logo_variants ./brand/07_patches \
         ./brand/08_stickers ./brand/09_marketing ./brand/10_color ./brand/11_typography \
         ./brand/12_docs ./brand/13_booklet/assets
```

Initialize `./brand/00_session.md` with project name + start timestamp.

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

**→ Checkpoint:** Schreibe `./brand/01_intake/mode.md` mit gewähltem Modus + 1-Satz-Begründung. Update `00_session.md`.

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

Don't proceed. Spawn a brainstorm subagent (see original Phase 1 spec for the full prompt; result feeds into Phase 2).

### Mode INSPIRED → Reference deconstruction

User provides references. Read/analyze each, extract shape/color/type/mood/composition, find common DNA. Run short 5-Q intake (Q1, Q2, Q3, Q4, Q7, Q9). Write Reference-Synthesis paragraph.

### Mode REBRAND → Audit + evolution path

Audit existing brand (use `brand-auditor` subagent if installed, else inline via `templates/critique-checklist.md`). Identify equity vs drift. Ask user: Refresh (90%) / Evolution (40%) / Reset (10%). Targeted 5-Q intake.

### Mode OPTIMIZE → Site audit + gap analysis

URL or local path required. Extract current tokens via `firecrawl-scrape` or local read of CSS/Tailwind config. Build focused 3–8 asset gap list. Skip directly to Phase 5 with targeted manifest.

**→ Checkpoint (PFLICHT nach Phase 1):**
- `./brand/01_intake/answers.md` — alle User-Antworten verbatim
- `./brand/01_intake/references.md` — (INSPIRED) Reference-Synthese
- `./brand/01_intake/audit.md` — (REBRAND/OPTIMIZE) Audit-Befunde
- `./brand/00_plan.md` — Section "Strategy Brief" anlegen (one-liner, enemy, audience, feeling, aspiration)
- `./brand/00_session.md` — Phase 1 complete log

---

## Phase 2 — Direction Setting (Skip in OPTIMIZE mode)

Generate **2–3 distinct visual territories** with real aesthetic tension. NOT three variations of "minimalist clean".

For each territory: Name · Archetype primary+secondary · Color logic (intent only) · Typography intent · Shape language · Real references · Trade-off statement.

Read `~/.claude/skills/Branding Skill/references/archetypes.md` and `~/.claude/skills/Branding Skill/references/tone-of-voice.md` before generating territories.

**Gate:** Present territories to user. User picks ONE. If user rejects all → return to Phase 1.

**→ Checkpoint (PFLICHT nach Phase 2):**
- `./brand/02_direction/territories.md` — alle 2–3 Optionen mit kompletter Spec
- `./brand/02_direction/picked.md` — Gewähltes Territory + User-Begründung + Trade-off
- `./brand/00_plan.md` — Section "Direction" mit Picked-Territory ergänzen
- `./brand/00_session.md` — Phase 2 complete log

---

## Phase 3 — Visual System (no images yet)

Now commit picked territory to concrete specs. Read `references/design-knowledge.md` for LIFT framework + 12 grid archetypes.

**LIFT analysis** (Leverage / Internal rhythm / Friction / Transferability).

**Define exactly:**
- 6 hex codes (bg, surface, text, text-muted, accent-1, accent-2) with WCAG contrast
- Typography (display + body, Google Fonts only unless user specifies). **NEVER** Inter/Poppins/Montserrat/Roboto/Open Sans.
- Type scale (clamp values): display, h1, h2, h3, body, small, button
- Shape language: radius scale, stroke weight policy
- Voice: 3 words IS / 3 words IS-NOT + 1 in-brand sentence + 1 off-brand sentence

**Gate:** Show user the system. They approve color + type + voice before any image generation.

**→ Checkpoint (PFLICHT nach Phase 3):**
- `./brand/03_system/lift.md`
- `./brand/03_system/colors.md` — 6 Hex + Rolle + Rationale + WCAG
- `./brand/03_system/typography.md` — Display + Body + Scale + Pairing-Rationale
- `./brand/03_system/shape.md` — Radius/Stroke/Corner-Logic
- `./brand/03_system/voice.md` — IS/IS-NOT + Beispielsätze
- `./brand/10_color/tokens.json` — voll strukturiert (JSON, alle Hex + Rollen)
- `./brand/00_plan.md` — Section "Visual System" mit allen Specs
- `./brand/00_session.md` — Phase 3 complete log

---

## Phase 4 — Output Medium → Asset Manifest

ONE question: Wofür wird die Marke primär eingesetzt? (A1 Landing / A2 SaaS / A3 E-Commerce / A4 Editorial / A5 Portfolio / B Print / C Social / D Alles)

Filter default manifest (siehe Tabelle in der Original-Spec) nach Medium.

**→ Checkpoint (PFLICHT nach Phase 4):**
- `./brand/04_manifest/medium.md` — Gewähltes Medium + 1-Satz-Begründung
- `./brand/04_manifest/manifest.md` — Finale Asset-Liste (Tabelle): File / AR / Quality / Notes
- `./brand/00_plan.md` — Section "Asset Manifest" mit finaler Liste
- `./brand/00_session.md` — Phase 4 complete log

---

## Phase 5 — Primary Logo (BLOCKING GATE)

Spawn ONE subagent. Everything else waits.

Build the 5-layer prompt using `references/prompt-patterns.md` → "Primary Logo Template". Use `gpt-image-2` T2I, `--aspect_ratio 1:1`, `--quality high`, `--num_images 3`.

Output goes to `./fal-outputs/images/`. Pick best variant. Copy to `./brand/05_logo_primary/primary_v1.png`.

**REBRAND adjustment (Refresh/Evolution):** Use old logo as `--image_url` (Edit-Mode).
**OPTIMIZE:** Skip Phase 5 unless primary logo is in the gap list.

**After subagent completes:**
1. Read `./brand/05_logo_primary/primary_v1.png` — Claude shows it inline.
2. **HARD STOP.** Say: "Hier ist dein Primary Logo. Wie weiter?"
   - Approve → Phase 6
   - Iterate → regenerate with adjusted prompt (max 3 attempts, write `primary_v2.png`, `primary_v3.png`)
   - Change direction → return to Phase 2

**→ Checkpoint (PFLICHT nach Phase 5 — auch bei Iteration):**
- `./brand/05_logo_primary/primary_vN.png`
- `./brand/05_logo_primary/primary_vN.meta.json` (prompt, model, variant_selected, fal-job-id)
- `./brand/05_logo_primary/primary_vN.prompt.md` — voller 5-Layer-Prompt für Reproduzierbarkeit
- `./brand/00_session.md` — Status (approved / iterating / rejected)

---

## Phase 6 — Parallel Asset Generation

Only start after primary logo is approved.

**Upload primary logo for I2I reference:**

```python
import fal_client, os
os.environ["FAL_KEY"] = "YOUR_FAL_KEY"
url = fal_client.upload_file("./brand/05_logo_primary/primary_v1.png")
print(url)  # → PRIMARY_LOGO_URL for all subagents
```

Spawn subagents in parallel, **only for categories in the filtered manifest from Phase 4**. All use `gpt-image-2` Edit-Mode with PRIMARY_LOGO_URL.

### Subagent A — Logo Variants → `./brand/06_logo_variants/`
horizontal, vertical, monogram, favicon, dark (+ app_icon/1color/signature je nach Medium). Alle `--quality medium`.

### Subagent B — Patches (nur wenn in Manifest) → `./brand/07_patches/`
round, shield, wordmark. Siehe `references/prompt-patterns.md` → "Patch Template".

### Subagent C — Stickers (nur wenn in Manifest) → `./brand/08_stickers/`
Eine pro Verb im Verb-Trio + optional monogram-Sticker.

### Subagent D — Marketing + Color + Type → `./brand/09_marketing/`, `./brand/10_color/`, `./brand/11_typography/`
hero_16x9 (high), og_card (high, Landing), product_pattern (high, E-Commerce), square_1x1 (medium), story_9x16 (medium), app_screenshot_frame (medium, SaaS), palette_v1.png (medium → `./brand/10_color/`), typography_spec.md → `./brand/11_typography/`.

Each subagent returns JSON: `{assets: [{path, ok}], errors: []}`.

**→ Checkpoint (PFLICHT nach jedem Subagenten — nicht erst am Ende):**
- Pro generiertem Asset: `<asset>.png` + `<asset>.meta.json` in der korrekten Unter-Folder
- `./brand/00_session.md` updaten nach jedem abgeschlossenen Subagenten (A/B/C/D), nicht erst am Ende von Phase 6 — so überlebt ein Crash mitten in Wave 6.

---

## Phase 7 — Audit

If `brand-auditor` skill is installed: spawn as subagent on `./brand/`. Scores each asset 0–20, identifies drift, regenerates failing assets (score <12).

If not installed: run inline using `templates/critique-checklist.md`. ≥6 pass / 3–5 iterate / <3 reject. Max 2 iterations per asset. Persistent 4–5 → invoke `/impeccable:bolder`.

**→ Checkpoint (PFLICHT nach Phase 7):**
- `./brand/00_review.md` — pro Asset: Path / Score / Pass-Fail / Notes / Iteration-Status
- `./brand/00_session.md` — Phase 7 complete log

---

## Phase 8 — Documentation

Write **4 files** under `./brand/12_docs/`.

### 1. `./brand/12_docs/Brand-Booklet.md` (≥200 lines)

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

### 2. `./brand/12_docs/Brand.md` (≤80 lines)

One-pager. Mission · Verb-Trio · Colors · Typography · Canonical logo path · 3 hard rules.

### 3. `./brand/12_docs/design-system.md` (replaces brand-to-code skill)

Production-ready design tokens for downstream coding agents. 9 required sections (Brand Context · CSS Custom Properties · Type Scale · Component Patterns · Animation · Layout · Anti-Patterns ≥10 · Tailwind Config · Google Fonts Import).

### 4. `./brand/12_docs/AGENTS.md`

Delegate to Haiku subagent:
```
Run: python ~/.claude/skills/brand-booklet/scripts/build_asset_index.py ./brand/
Read ~/.claude/skills/brand-booklet/templates/agents-md-template.md.
Fill with: asset index table, canonical logo path, color tokens path,
typography spec path, locked assets list.
Write to ./brand/12_docs/AGENTS.md.
```

**→ Checkpoint (PFLICHT nach Phase 8):**
- Alle 4 Files in `./brand/12_docs/`
- `./brand/00_session.md` — Phase 8 complete log

---

## Phase 9 — Brand-Booklet HTML (high-end-visual-design + claude-taste)

Ziel: Aus den Markdown-Docs + generierten Assets eine **presentation-ready HTML-Datei** bauen, die wie ein $150k-Agency-Booklet aussieht — und dann mit `/claude-taste` unabhängig reviewen lassen.

### Step 9.1 — Assets-Bündelung

Kopiere alle für das Booklet benötigten Assets in `./brand/13_booklet/assets/`. So bleibt das Booklet self-contained und portierbar:

```
./brand/13_booklet/assets/
├── primary.png            ← von 05_logo_primary/primary_v1.png
├── horizontal.png         ← von 06_logo_variants/
├── monogram.png
├── favicon.png
├── dark.png
├── hero.png               ← von 09_marketing/hero_16x9_v1.png
├── palette.png            ← von 10_color/palette_v1.png
└── (weitere je nach Manifest)
```

### Step 9.2 — Booklet via `high-end-visual-design`

Invoke the `high-end-visual-design` skill via the Skill tool. Briefing-Prompt für den Skill:

```
Build a single-file presentation-ready HTML brand booklet at
./brand/13_booklet/booklet.html.

Source content (read these now):
- ./brand/12_docs/Brand-Booklet.md
- ./brand/12_docs/Brand.md
- ./brand/12_docs/design-system.md
- ./brand/10_color/tokens.json
- ./brand/11_typography/typography_spec.md
- ./brand/04_manifest/manifest.md

Available assets (use relative paths from booklet.html):
./assets/primary.png, ./assets/horizontal.png, ./assets/monogram.png,
./assets/favicon.png, ./assets/dark.png, ./assets/hero.png,
./assets/palette.png, (weitere s. assets-Ordner)

Required sections (one full-bleed page each — use CSS page-break-after: always):
1. Cover                — Brand name, tagline, primary logo on hero
2. Brand Strategy       — One-liner, archetype, enemy, audience, feeling
3. Tone of Voice        — IS / IS-NOT + example copy
4. Logo System          — All variants in grid with clear-space + min-size specs
5. Color System         — Swatches with hex + role + WCAG ratios
6. Typography           — Display/body specimens + full type scale
7. Shape & Motion       — Radius scale, easing curves, hover physics
8. Marketing Templates  — Hero, OG, square, story (when in manifest)
9. Do / Don't Gallery   — 5 concrete examples
10. Asset Index         — Full table of all deliverables with paths

Critical rules:
- Use the brand's OWN colors from ./brand/10_color/tokens.json — NOT generic blacks.
- Use the brand's OWN fonts from ./brand/11_typography/typography_spec.md — NOT defaults.
- Follow ALL high-end-visual-design directives:
  Double-Bezel cards, macro-whitespace (py-24+), custom cubic-bezier transitions,
  scroll-entry animations, premium fonts (never Inter/Roboto/etc), button-in-button
  trailing icons, no harsh shadows or generic borders.
- Single HTML file, inline <style>, no external JS frameworks. Tailwind CDN OK.
- @media print: hide nav, force section-per-page (210mm × 297mm A4 portrait by default;
  switch to 297mm × 210mm landscape if user requested landscape in Phase 4),
  preserve all imagery at full quality.
- Print-safe page breaks: `page-break-after: always` on every section wrapper.
- All images via <img src="./assets/..."> with explicit width/height to prevent
  layout shift during PDF render.

Output:
- ./brand/13_booklet/booklet.html
- ./brand/13_booklet/design-notes.md  — Architecture decisions (variance-engine pick,
  layout archetype, type-color rationale)
```

### Step 9.3 — Independent Review via `claude-taste`

After the HTML exists, spawn `claude-taste` for an unabhängige Zweitmeinung:

```
Skill({ skill: "claude-taste",
       args: "consult Reviewe ./brand/13_booklet/booklet.html als $150k Brand-Booklet.
              Check: (1) Markentreue — Colors/Fonts/Voice konsistent mit ./brand/12_docs/Brand.md?
              (2) Anti-Slop — Inter-Font, generische Shadows, 1px-Borders, ease-in-out?
              (3) Print-Tauglichkeit — page-breaks sauber, kein clipped content?
              (4) Hierarchy — Cover liest sich als Cover, Sections klar abgegrenzt?
              Gib P1/P2/P3 Findings mit Datei:Zeile + Fix." })
```

Schreibe Findings nach `./brand/13_booklet/design-notes.md`. Fixe P1-Issues sofort, P2-Issues nach Bestätigung des Users, P3-Issues optional.

**→ Checkpoint (PFLICHT nach Phase 9):**
- `./brand/13_booklet/booklet.html`
- `./brand/13_booklet/assets/*` (alle referenzierten Files vorhanden)
- `./brand/13_booklet/design-notes.md` (mit claude-taste Findings + Fix-Status)
- `./brand/00_session.md` — Phase 9 complete log

---

## Phase 10 — PDF Export (presentation-ready)

Ziel: `./brand/13_booklet/booklet.pdf` — A4 portrait (oder landscape, je nach Phase 4), Print-CSS aktiv, alle Bilder eingebettet, page-breaks sauber, präsentier-fertig.

### Step 10.1 — Headless Chromium via Playwright MCP

Wir nutzen `mcp__plugin_playwright_playwright__*` (bereits verfügbar), nicht den `make-pdf` Skill (der ist für markdown, nicht HTML).

```
# 1. Navigate to file
mcp__plugin_playwright_playwright__browser_navigate
  url: file:///<absolute-path>/brand/13_booklet/booklet.html

# 2. Warte bis Fonts geladen + Bilder gerendert
mcp__plugin_playwright_playwright__browser_wait_for
  time: 2

# 3. PDF via Page.pdf() — Playwright unterstützt das nativ
mcp__plugin_playwright_playwright__browser_run_code_unsafe
  code: |
    await page.pdf({
      path: '<absolute-path>/brand/13_booklet/booklet.pdf',
      format: 'A4',
      landscape: false,           // → true wenn Phase 4 landscape gewählt hat
      printBackground: true,      // PFLICHT für volle Brand-Farben
      preferCSSPageSize: true,    // respektiert @page CSS-Rules
      margin: { top: '0', right: '0', bottom: '0', left: '0' }
    });
```

### Step 10.2 — Verify

```bash
ls -la ./brand/13_booklet/booklet.pdf
# Erwarte: > 100 KB (sonst sind Bilder nicht eingebettet)
```

Wenn `< 100 KB` oder `printBackground` ignoriert wurde → erneut rendern mit längerem `wait_for` (Bilder noch nicht fertig).

### Step 10.3 — Visual sanity-check

Optional: Erste Seite des PDFs als Screenshot rendern und inline anzeigen (Vorschau für User).

**→ Checkpoint (PFLICHT nach Phase 10):**
- `./brand/13_booklet/booklet.pdf` (> 100 KB)
- `./brand/13_booklet/build.log` — Render-Command + Timings + File-Size
- `./brand/00_session.md` — Phase 10 complete log + finalisierter "Workflow complete"-Eintrag

---

## Output Checklist (final)

Before declaring done:
- [ ] Mode router answered (Scratch / Inspired / Rebrand / Optimize) → `01_intake/mode.md`
- [ ] Strategy intake → `01_intake/answers.md` + (je nach Mode) `references.md` / `audit.md`
- [ ] Visual territories presented + ONE picked → `02_direction/picked.md` (außer OPTIMIZE)
- [ ] `00_plan.md` enthält Strategy + System + Manifest
- [ ] `03_system/` enthält 5 Files (lift, colors, typography, shape, voice)
- [ ] `04_manifest/manifest.md` finalisiert
- [ ] Primary logo approved → `05_logo_primary/primary_v*.png` + `.meta.json` + `.prompt.md`
- [ ] Phase-6-Assets generiert mit `.meta.json` pro File
- [ ] `00_review.md` exists with scores
- [ ] `12_docs/Brand-Booklet.md` ≥200 lines
- [ ] `12_docs/Brand.md` ≤80 lines
- [ ] `12_docs/design-system.md` mit allen 9 Sections + Anti-Patterns ≥10
- [ ] `12_docs/AGENTS.md` mit Asset-Inventory-Tabelle
- [ ] `13_booklet/booklet.html` existiert + alle Assets in `13_booklet/assets/`
- [ ] `13_booklet/design-notes.md` mit claude-taste Findings
- [ ] `13_booklet/booklet.pdf` existiert + > 100 KB
- [ ] `00_session.md` markiert "Workflow complete"

Show user: Primary Logo + Booklet PDF + Summary + Next step.

---

## Common Failure Modes

| Symptom | Root Cause | Fix |
|---|---|---|
| User unhappy with logo | Skipped Phase 2 | Re-run from Phase 2 with 2-3 territories |
| Assets look like 3 different brands | Skipped Phase 3 gate | Lock system, regenerate via Edit-Mode |
| Generated stickers for SaaS brand | Skipped Phase 4 | Filter manifest, delete unused categories |
| Rebrand drifts too far | T2I instead of Edit-Mode | Re-run Phase 5 with old logo as `--image_url` |
| design-system.md too generic | Skipped Phase 3 specs | Always finish Phase 3 before Phase 5 |
| Booklet HTML feels template-y | Skipped `high-end-visual-design` directives | Re-invoke skill with stricter brief, run claude-taste again |
| PDF blank / no backgrounds | `printBackground: false` | Set `printBackground: true`, `preferCSSPageSize: true` |
| PDF text mis-aligned / clipped | Race: rendered before fonts loaded | Increase `browser_wait_for` to 3–4s before `page.pdf()` |
| Workflow abort, no resume | Session-file fehlt | Bei jedem Phase-Ende `00_session.md` updaten |

---

## Notes

- Never overwrite approved assets. New iterations → `_v2`, `_v3`, …
- Mode Router ist non-negotiable.
- `brand-to-code` skill is **superseded** by Phase 8 → `12_docs/design-system.md`.
- `Branding Skill` (brand-architect) is **superseded** by Phases 1–3.
- `brand-auditor` bleibt separat — standalone-Audit, in Phase 7 hier invoked.
- HTML-Booklet braucht beide Skills (`high-end-visual-design` + `claude-taste`) — der erste liefert das Design-Language-Layer, der zweite die unabhängige Qualitätskontrolle. Skip nur wenn User explizit `--no-booklet` setzt.
- PDF-Export läuft via Playwright MCP, nicht via `make-pdf` (das ist Markdown→PDF, wir brauchen HTML→PDF).
