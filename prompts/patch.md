# Patch — Fully Worked Example

Brand: "Sentinel" (same brand as logo-primary.md)
Uses gpt-image-2 edit mode with primary logo as reference.

---

## Round Patch

```bash
# Step 1: Upload primary logo to get CDN URL
python -c "
import fal_client, os
os.environ['FAL_KEY'] = 'YOUR_FAL_KEY'
url = fal_client.upload_file('./brand/01_logos/primary_v1.png')
print(url)
"

# Step 2: Generate round patch
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Transform this logo into a circular embroidered patch design. SENTINEL text curved along the top arc of the circle. The abstract S-mark centered and enlarged in the middle zone. Bottom arc: founding year or tagline. Border: double-ring outline in deep charcoal. Color fill: electric teal for symbol, charcoal for text. Embroidered thread texture — visible stitch lines, slightly raised feel. White background. Clear circular boundary with no bleed beyond the outer ring." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

## Shield Patch

```bash
python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Transform this logo into a heraldic shield badge. Classic pointed-bottom shield outline in deep charcoal stroke. Upper section: the abstract S-mark, enlarged, in electric teal. Horizontal dividing bar across center. Lower section: SENTINEL in bold block uppercase lettering. Shield corners are sharp, not rounded — precise and authoritative. Flat 2D illustration, no photorealism. White background." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 3:4 \
  --quality high
```

## Notes

- If the uploaded logo loses its color fidelity in edit mode, add hex codes explicitly in the prompt
- gpt-image-2 edit mode will interpolate from the reference — the S-mark may be reinterpreted, which is acceptable for patches
- Minimum patch delivery size: provide PNG at 300dpi for embroidery digitization
