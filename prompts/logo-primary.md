# Primary Logo — Fully Worked Example

Brand: "Sentinel" — B2B cybersecurity SaaS
Verbs: Protect / Detect / Accelerate
Colors: Deep charcoal #1C1C1E + electric teal #00D4AA
Off-limits: No shields, no locks, no circuit boards

---

## 5-Layer Prompt

```
Sentinel logo for a cybersecurity software brand.
SUBJECT: Combination mark — a minimalist abstract "S" letterform that suggests both a forward-motion vector and a protective arc, paired with the wordmark "SENTINEL" in tight uppercase geometric sans-serif.
STYLE: Vector-clean flat 2D. No gradients. No 3D. No texture. Geometric precision with 45-degree angles and crisp terminals. Single-weight stroke.
COMPOSITION: Centered on white background. Abstract S-mark on the left, wordmark to the right in a horizontal lockup. Mark is slightly taller than the cap height of the wordmark. Equal optical spacing between symbol and text.
LIGHT & MATERIAL: Matte digital ink. Flat fill — no shadows, no highlights, no gloss. Symbol in electric teal (#00D4AA). Wordmark in deep charcoal (#1C1C1E). No additional colors.
NEGATIVE: No gradients, no glow effects, no photorealism, no 3D depth, no drop shadows, no circuit board patterns, no shield shape, no padlock shape, no globe, no stock clipart, no lens flares, no generic startup aesthetic.
```

## fal Command

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Sentinel logo for a cybersecurity software brand. SUBJECT: Combination mark — a minimalist abstract S letterform that suggests both forward-motion vector and a protective arc, paired with the wordmark SENTINEL in tight uppercase geometric sans-serif. STYLE: Vector-clean flat 2D. No gradients. No 3D. Geometric precision with 45-degree angles and crisp terminals. Single-weight stroke. COMPOSITION: Centered on white background. Abstract S-mark on the left, wordmark to the right. Mark slightly taller than cap height. Equal optical spacing. LIGHT AND MATERIAL: Matte digital ink, flat fill. Symbol in electric teal. Wordmark in deep charcoal. No additional colors. NEGATIVE: No gradients, no glow, no photorealism, no 3D depth, no drop shadows, no circuit boards, no shields, no padlocks, no globes, no clipart." \
  --image_model gpt-image-2 \
  --aspect_ratio 1:1 \
  --quality high \
  --num_images 3
```

## Notes

- Generate 3 variants → select the one where the S-mark is most distinct and the spacing reads best
- If the wordmark is too thin: add "bold weight wordmark, heavy stroke" to Layer 2
- If the S reads as just an S: add "the S form implies a sweeping protective arc in its upper curve" to Layer 1
