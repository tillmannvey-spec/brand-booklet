# Marketing Visual — Fully Worked Example

Brand: "Sentinel" — Verbs: Protect / Detect / Accelerate
Model: gpt-image-2 Edit-Mode (primary logo as style + color reference)

**Upload primary logo first (if not already done):**
```bash
python -c "
import fal_client, os
os.environ['FAL_KEY'] = 'YOUR_FAL_KEY'
url = fal_client.upload_file('./brand/01_logos/primary_v1.png')
print(url)
"
# Use the printed URL as PRIMARY_LOGO_CDN_URL below
```

---

## Hero 16:9

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Sentinel cybersecurity brand hero image. SUBJECT: A solo engineer in a modern dark server room, face illuminated by monitor glow, confidently reviewing a clean dashboard on a large screen. The dashboard shows green status indicators — everything protected. STYLE: High-end editorial photography aesthetic, tight color grade, cinematic quality. Match the electric teal and deep charcoal from the logo reference. COMPOSITION: Left-thirds: engineer at workstation. Right-third: large dark zone with SENTINEL brand name in electric teal type. Asymmetric, not centered. LIGHT: Cool blue-teal monitor fill light from the left, subtle warm backlight from the server racks. NEGATIVE: No stock photo clichés, no lock icons on screens, no explosion/breach imagery, no generic office, no smiling person looking at camera." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 16:9 \
  --quality high
```

## Square 1:1

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Sentinel brand square social post. SUBJECT: Ultra-close crop of a single glowing terminal line: '> ALL SYSTEMS PROTECTED' in monospace font, bright electric teal on deep charcoal screen background. SENTINEL wordmark in small caps at the bottom right. COMPOSITION: Terminal text fills 60% of the frame, centered slightly high. Grain texture on the background. STYLE: Clean, confident, tech-editorial. Match the teal and charcoal palette from the logo reference. No stock photography." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

## Story 9:16

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Sentinel brand story format. SUBJECT: Vertical split composition. Top 65%: The abstract Sentinel S-mark as a monumental graphic element on deep charcoal — large, centered, electric teal — derived from the logo reference. Bottom 35%: Clean white zone with SENTINEL in bold charcoal and a one-line CTA in smaller text. STYLE: Graphic, print-poster quality. No photographic elements. COMPOSITION: Strong vertical motion from symbol to text. TYPE in bottom zone: large SENTINEL + tagline below." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 9:16 \
  --quality high
```

## Notes

- Always use the primary logo as `--image_url` — it locks in brand colors (electric teal, deep charcoal) and overall visual style
- gpt-image-2 Edit-Mode will carry the logo's palette and mark into the scene naturally
- If text rendering is critical (exact wordmark must appear accurately): switch this specific asset to `ideogram-v3` without `--image_url`, but add explicit hex values and style description to the prompt
- For print-ready marketing (≥300dpi at print size): upscale the output via a separate tool after generation
