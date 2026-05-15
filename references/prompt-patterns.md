# Prompt Patterns — Brand-Booklet Quick Reference

Always-loaded. Subagents read this before building any prompt.

---

## The 5-Layer Prompt Structure

Every brand asset prompt uses these 5 layers in order:

```
Layer 1 — SUBJECT:      What exactly is shown (logo for X brand, patch for Y, sticker with Z)
Layer 2 — STYLE:        Visual language (vector-clean, flat 2D, geometric, hand-drawn, etc.)
Layer 3 — COMPOSITION:  Layout and format (centered, left-aligned, circular frame, badge shape)
Layer 4 — LIGHT & MAT:  Material quality (matte ink, metallic foil, embroidered texture, clean digital)
Layer 5 — NEGATIVE:     What must NOT appear (no gradients, no photorealism, no 3D depth, no generic icons)
```

---

## Model Selection Guide

**Default: `gpt-image-2` for EVERYTHING.**  
T2I (no `--image_url`) only for the very first asset when no reference image exists yet.  
Edit-Mode (`--image_url`) for everything else — logo variants, patches, stickers, marketing, all of it.

| Asset type | Mode | Why |
|---|---|---|
| Primary logo — first generation only | `gpt-image-2` T2I | No reference exists yet; generates the visual anchor |
| All subsequent assets | `gpt-image-2` Edit | Locks in brand coherence via primary logo as reference |
| Exception: text-critical marketing text | `ideogram-v3` | If exact readable text must appear in marketing image |

**Upload primary logo before any Edit-Mode calls:**
```python
import fal_client, os
os.environ['FAL_KEY'] = 'YOUR_FAL_KEY'
url = fal_client.upload_file('./brand/01_logos/primary_v1.png')
print(url)  # Save this CDN URL — use as --image_url in all subsequent calls
```

---

## fal Commands — Copy-Paste Ready

### Step 0: Upload Primary Logo (run once before any Edit-Mode call)
```bash
python -c "
import fal_client, os
os.environ['FAL_KEY'] = 'YOUR_FAL_KEY'
url = fal_client.upload_file('./brand/01_logos/primary_v1.png')
print(url)
"
# Save the printed CDN URL — use as PRIMARY_LOGO_CDN_URL in all commands below
```

### Primary Logo — First Generation Only (gpt-image-2, T2I)
```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "[SUBJECT]. [STYLE]. [COMPOSITION]. [LIGHT & MAT]. No [NEGATIVE]." \
  --image_model gpt-image-2 \
  --aspect_ratio 1:1 \
  --quality high \
  --num_images 3
# Output: ./fal-outputs/images/
# Select best → copy to: ./brand/01_logos/primary_v1.png
# Then run Step 0 above to get the CDN URL
```

### Logo Variants (gpt-image-2, Edit-Mode)
```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "[Edit instruction: describe the layout change — vertical/horizontal/monogram. Keep colors and symbol.] White background." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

### Patches + Stickers (gpt-image-2, Edit-Mode)
```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "[Patch/sticker instruction derived from primary logo. Circular frame / die-cut border / badge shape.]" \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

### Marketing Visuals (gpt-image-2, Edit-Mode — using primary logo as style reference)
```bash
# Hero 16:9
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "[SUBJECT scene]. [STYLE consistent with brand]. [COMPOSITION asymmetric]. [LIGHT]. Brand name '[Name]' as text in image. [NEGATIVE]." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 16:9 \
  --quality high

# Square 1:1
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "[Social square scene — tight, bold, brand-colored]. Brand name '[Name]' visible in image." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high

# Story 9:16
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "[Vertical story format. Graphic over text zone split. Brand symbol dominant top, name bottom.]" \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 9:16 \
  --quality high
```

---

## Template Library

### Primary Logo Template
```
[Brand name] logo design for a [industry] brand.
[STYLE]: Vector-clean flat 2D graphic. [Symbol type: lettermark / abstract mark / combination mark].
[COMPOSITION]: Centered on white background. Symbol [above/left of] brand name in [typeface category] typography.
[Light & Mat]: Matte digital ink. No shadows, no 3D effects, no textures.
[Negative]: No gradients, no photorealism, no 3D depth, no drop shadows, no lens flares, no decorative borders, no clipart.
Colors: [primary hex] and [accent hex] only.
```

### Logo Variant Template (for gpt-image-2 edit)
```
Redesign this logo into a [horizontal / vertical / monogram] variant.
Keep identical: brand colors, symbol shape, typographic style.
Change: layout to [landscape / stacked / symbol-only].
White background. Clean edges. No new design elements.
```

### Round Patch Template (for gpt-image-2 edit)
```
Transform this logo into a circular embroidered patch design.
Circular frame with brand name curved along the top border.
Center: the logo symbol, enlarged.
Bottom: brand tagline or founding year curved along bottom.
Embroidered texture, thread-like fills, clean geometric stitching lines.
White background with clear circular boundary.
Colors: [primary], [accent], white thread.
```

### Shield Patch Template (for gpt-image-2 edit)
```
Transform this logo into a shield/crest badge.
Traditional heraldic shield outline. 
Upper field: [brand symbol or abstraction].
Lower field: brand name in block lettering.
Dividing line at center of shield.
Clean flat illustration, not photorealistic.
White background.
```

### Kiss-Cut Sticker Template (for gpt-image-2 edit)
```
Create a die-cut sticker based on this logo representing the concept of [verb].
Bold graphic illustration, energetic and collectible.
Thick white stroke outline around the entire design (die-cut border effect).
Style: [consistent with primary logo style].
White background.
No text unless brand name only.
```

### Marketing Hero Template (gpt-image-2 Edit-Mode, PRIMARY_LOGO_CDN_URL as reference)
```
[Brand name] brand marketing image.
[Scene: specific moment that embodies brand verb-trio — be concrete, not abstract].
[Style: photographic / illustrative / graphic depending on brand personality].
[Composition: rule-of-thirds, brand-colored elements in frame].
[Light: describe quality and direction — "warm golden hour side-light", "cool studio flat-light", etc.].
Brand primary color [hex] dominant in the scene.
Brand name "[name]" as visible text in [position] of the image.
```
Use `--image_url [PRIMARY_LOGO_CDN_URL]` to carry brand colors and mark into the scene.

---

## Stock Modifiers (append to any prompt as needed)

**Print-safe:** `ISO 12647 color standard, CMYK-safe palette, no RGB-only neon`  
**Logo quality:** `vector-clean, crisp edges, scalable, no anti-aliasing artifacts`  
**Transparent intent:** `white background (will be removed for transparency), clean subject edges`  
**No-AI-slop:** `avoid gradient soup, avoid generic globe icons, avoid lens flares, avoid stock-photo aesthetic`

---

## Negative Prompt Library

**Always include for logos:**
`no gradients, no photorealism, no 3D depth, no drop shadows, no lens flares, no clipart, no generic symbols`

**Always include for patches/stickers:**
`no digital gradients, no flat-color boredom, no blurry edges, no transparent background (white is correct)`

**Always include for marketing visuals:**
`no stock photo people, no generic office backgrounds, no abstract geometric shapes without meaning`

---

## Parameter Quick Reference

| Param | Use case | Values |
|---|---|---|
| `--image_model` | Model selection | `ideogram-v3`, `gpt-image-2`, `nano-banana-pro`, `recraft-v4`, `flux-2-max` |
| `--aspect_ratio` | Format | `1:1`, `16:9`, `9:16`, `4:3` |
| `--resolution` | Quality (nano-banana) | `1K`, `2K`, `4K` |
| `--quality` | Quality (gpt-image-2) | `low`, `medium`, `high` |
| `--num_images` | Variants | `1`–`4` (ideogram, nano-banana support native; others loop) |
| `--image_url` | I2I reference | CDN URL only (upload local files first!) |
| `--seed` | Reproducibility | Any integer |
