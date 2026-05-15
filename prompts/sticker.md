# Sticker — Fully Worked Example

Brand: "Sentinel" — Verbs: Protect / Detect / Accelerate

---

## Sticker: PROTECT

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Die-cut sticker: PROTECT concept. A bold geometric abstraction of a watchful eye within a minimal shield form — but not a literal shield, more like two angled planes that frame space. Electric teal fill. Thick white stroke outline 6px (die-cut border). Style consistent with the Sentinel logo: geometric, flat, 45-degree angles. Small SENTINEL wordmark at the bottom in deep charcoal. White background. Collectible, premium sticker aesthetic. No gradients, no photorealism, no clip art." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

## Sticker: DETECT

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Die-cut sticker: DETECT concept. A minimalist radar sweep illustration — a single arc radiating from a central point, with two concentric partial arcs. Graphic, not literal. Deep charcoal lines on electric teal ground. Thick white stroke outline (die-cut border). Style: geometric, clean, Sentinel brand aesthetic. No gradients, no photorealism." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

## Sticker: ACCELERATE

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Die-cut sticker: ACCELERATE concept. Bold abstract vector of a forward-motion arrow that also reads as a speed indicator — the Sentinel S-mark implied in the negative space of the motion path. Electric teal primary. Deep charcoal accent. Thick white stroke outline (die-cut border). Geometric, flat, high contrast. No gradients, no photorealism." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

## Notes

- The thick white stroke border in the output represents the die-cut line for production
- If the white border doesn't appear: add "8px white stroke outline around all design edges, visible on white background" to the prompt
- Sticker size recommendation: output at 1080×1080px, deliver at minimum 5cm × 5cm for print
