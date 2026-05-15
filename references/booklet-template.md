# Brand Booklet — [BRAND NAME]
*Version 1.0 — Generated [DATE]*

---

## 1. Brand Strategy

### Mission
[One sentence. What does this brand do and for whom? Concrete, not aspirational fluff.]

### Verb-Trio
**[Verb 1]** / **[Verb 2]** / **[Verb 3]**

These three verbs define what the brand DOES, not what it IS. Every design decision maps back to them.

### LIFT Analysis
| Dimension | Decision |
|---|---|
| Leverage-Asset | [The one visual element the entire system builds around] |
| Internal Rhythm | [The visual cadence that runs through all assets] |
| Friction Sources | [What to avoid: category clichés, AI tells, mismatched energy] |
| Transferability | [How the identity performs at 32px, inverted, 1-color, in print] |

### Positioning
[2–3 sentences. Where does this brand sit in its category? What does it own that others don't?]

### Target Audience
| Dimension | Description |
|---|---|
| Who | [Age, role, sophistication level] |
| Context | [When and where do they encounter this brand?] |
| What they want | [Functional need this brand meets] |
| What they really want | [Emotional need underneath the functional one] |

---

## 2. Tone of Voice

### Voice Adjectives
**[Adjective 1]** — [What this means in practice]
**[Adjective 2]** — [What this means in practice]
**[Adjective 3]** — [What this means in practice]

### Copy Examples

| Context | Write THIS | Not this |
|---|---|---|
| Headline | [Example] | [Anti-example] |
| CTA button | [Example] | [Anti-example] |
| Error message | [Example] | [Anti-example] |
| Product description | [Example] | [Anti-example] |

### Hard Off-Limits
Never use these words or phrases in brand communication:
- [Word/phrase 1 — why it's wrong for this brand]
- [Word/phrase 2]
- [Word/phrase 3]

---

## 3. Logo System

### Primary Mark
`./brand/01_logos/primary_v1.png`

[Describe the symbol, its meaning, why it was chosen. How does it embody the verb-trio?]

### Usage Rules
- **Minimum size:** [X]px digital / [X]mm print
- **Clear space:** [X]px on all sides (= the height of the symbol or cap-height of wordmark)
- **Approved backgrounds:** White, [primary color], [accent color]
- **Never:** Stretched, rotated, recolored, or placed on busy backgrounds without a container

### Logo Variants

| Variant | File | Use Case |
|---|---|---|
| Primary (combination mark) | `01_logos/primary_v1.png` | Default — most contexts |
| Horizontal lockup | `01_logos/horizontal_v1.png` | Headers, navigation bars, letterheads |
| Vertical/stacked | `01_logos/vertical_v1.png` | Profile images, signage, square formats |
| Monogram/mark only | `01_logos/monogram_v1.png` | Favicon, embossing, very small sizes, watermarks |

### Logo Don'ts
- Do not add drop shadows
- Do not use in low-contrast situations without a container
- Do not rearrange or resize individual elements
- Do not apply gradients to any logo element
- Do not use the wordmark without the symbol (except in monogram contexts)

---

## 4. Color System

### Brand Palette

| Role | Name | HEX | Use |
|---|---|---|---|
| Primary | [Name] | `#XXXXXX` | Main brand color, CTAs, primary surfaces |
| Accent | [Name] | `#XXXXXX` | Highlights, hover states, callouts |
| Neutral | [Name] | `#XXXXXX` | Backgrounds, body text, structural elements |
| Dark | [Name] | `#XXXXXX` | Headers, footers, dark UI |
| Light | [Name] | `#XXXXXX` | Light backgrounds, cards |

`./brand/06_color/tokens.json` — machine-readable source of truth
`./brand/06_color/palette_v1.png` — visual reference

### Usage Proportions (60/30/10 Rule)
- **60%** Neutral — backgrounds, large surfaces
- **30%** Primary — main UI, large brand elements
- **10%** Accent — CTAs, highlights, key interactions

### Contrast Ratios
| Combination | Ratio | WCAG |
|---|---|---|
| Primary text on neutral bg | [X]:1 | AA / AAA |
| White text on primary color | [X]:1 | AA / AAA |
| Accent on neutral bg | [X]:1 | AA / AAA |

---

## 5. Typography

### Type System

| Role | Font | Weight | Size |
|---|---|---|---|
| Display / Hero | [Font name] | 700–900 | 48–96px |
| Headline | [Font name] | 600–700 | 32–48px |
| Subheading | [Font name] | 500–600 | 24–32px |
| Body | [Font name] | 400 | 16–18px |
| Caption | [Font name] | 400 | 12–14px |
| Code / Mono | [Font name] | 400 | 14px |

`./brand/05_typography/typography_spec.md` — full specification

### Pairing Rationale
[Why these two fonts work together. What each one does. How they relate to the verb-trio.]

### Print vs. Screen
| Context | Recommendation |
|---|---|
| Screen (digital) | [Font + rendering notes] |
| Print (coated stock) | [Font + size minimum for print] |
| Large format / outdoor | [Font + weight recommendation] |
| Small / body text | [Font + minimum size] |

---

## 6. Patch & Sticker System

### Patches

| Name | File | Application Context |
|---|---|---|
| Round emblem | `02_patches/round_v1.png` | Apparel, bags, merchandise |
| Shield/crest | `02_patches/shield_v1.png` | Formal merchandise, corporate gifting |
| Wordmark badge | `02_patches/wordmark_v1.png` | Minimal contexts, professional use |

**Patch production notes:**
- Provide to embroidery vendor as PNG with white background (they will digitize)
- Minimum patch size: 5cm diameter for round, 4cm width for wordmark
- Thread count recommendation: [X] colors maximum for cost efficiency

### Stickers

| Name | File | Verb it represents |
|---|---|---|
| [Name] | `03_stickers/sticker_[verb1]_v1.png` | [Verb 1] |
| [Name] | `03_stickers/sticker_[verb2]_v1.png` | [Verb 2] |
| [Name] | `03_stickers/sticker_[verb3]_v1.png` | [Verb 3] |
| Monogram | `03_stickers/sticker_monogram_v1.png` | Brand icon |

**Sticker production notes:**
- Kiss-cut on white label stock (the white stroke border in the design = the cut line)
- Print as: PNG at 300dpi, CMYK conversion recommended for offset printing
- Size: minimum 5×5cm, recommended 8×8cm for readability

---

## 7. Marketing Templates

### Hero (16:9)
`./brand/04_marketing/hero_16x9_v1.png`

| Spec | Value |
|---|---|
| Format | 1920×1080px |
| Primary use | Website hero, presentations, YouTube thumbnails, digital banners |
| Composition | [Rule-of-thirds / Split / etc.] — [describe what's in the frame] |
| Brand placement | [Where the logo/brand name sits] |

### Square (1:1)
`./brand/04_marketing/square_1x1_v1.png`

| Spec | Value |
|---|---|
| Format | 1080×1080px |
| Primary use | Instagram feed, Facebook posts, profile images |
| Composition | [Describe key visual element placement] |

### Story (9:16)
`./brand/04_marketing/story_9x16_v1.png`

| Spec | Value |
|---|---|
| Format | 1080×1920px |
| Primary use | Instagram/TikTok stories, Reels covers, Pinterest |
| Composition | [Top zone: visual / Bottom zone: text + CTA] |

### Adaptation Rules
When creating new marketing assets based on these templates:
1. [Rule 1 about color use]
2. [Rule 2 about logo placement]
3. [Rule 3 about typography in marketing materials]

---

## 8. Do/Don't Gallery

### 1. Logo Usage
✅ **DO:** Place primary logo on white or brand-primary background with clear space
❌ **DON'T:** Place logo on busy photography without a container or overlay

### 2. Color Application
✅ **DO:** Use primary color for the dominant 30% of any composition
❌ **DON'T:** Mix warm and cool versions of the brand color in the same layout

### 3. Typography
✅ **DO:** Use display font for all headlines, body font for all reading text
❌ **DON'T:** Use display font at body size or body font at hero scale

### 4. Photography/Imagery Style
✅ **DO:** [Describe the correct image aesthetic for this brand]
❌ **DON'T:** [Describe the wrong image aesthetic — stock photos, wrong lighting, etc.]

### 5. Brand Voice
✅ **DO:** [Example of on-brand copy]
❌ **DON'T:** [Example of off-brand copy — typically generic, filler words, AI slop]

---

## 9. Asset Manifest

[This section is filled by the Haiku subagent via build_asset_index.py]

| Folder | File | Description | Status |
|---|---|---|---|
| 01_logos | primary_v1.png | Combination mark, primary | Locked |
| 01_logos | horizontal_v1.png | Horizontal lockup | Locked |
| 01_logos | vertical_v1.png | Vertical/stacked lockup | Locked |
| 01_logos | monogram_v1.png | Symbol/lettermark only | Locked |
| 02_patches | round_v1.png | Round emblem patch | Approved |
| 02_patches | shield_v1.png | Shield/crest patch | Approved |
| 02_patches | wordmark_v1.png | Wordmark badge | Approved |
| 03_stickers | sticker_[verb1]_v1.png | Verb 1 sticker | Approved |
| 03_stickers | sticker_[verb2]_v1.png | Verb 2 sticker | Approved |
| 03_stickers | sticker_[verb3]_v1.png | Verb 3 sticker | Approved |
| 03_stickers | sticker_monogram_v1.png | Monogram sticker | Approved |
| 04_marketing | hero_16x9_v1.png | Hero 16:9 | Approved |
| 04_marketing | square_1x1_v1.png | Square 1:1 | Approved |
| 04_marketing | story_9x16_v1.png | Story 9:16 | Approved |
| 05_typography | typography_spec.md | Type system specification | Reference |
| 06_color | tokens.json | Color tokens (machine-readable) | Reference |
| 06_color | palette_v1.png | Color palette visualization | Reference |

### Version Policy
- `_v1` files are approved and locked — do not overwrite
- New versions use `_v2`, `_v3` suffix
- Regeneration always produces a new version, never overwrites

---

*Brand-Booklet generated by brand-booklet skill. AI-generated assets are visual starting points — final production logos should be vectorized in Figma or Illustrator before print use.*
