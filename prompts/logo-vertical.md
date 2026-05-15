# Logo Vertical Variant — Fully Worked Example

Generates a stacked/vertical version from the approved primary logo via gpt-image-2 edit mode.

---

## Command

```bash
# Upload primary first (if not already done):
python -c "
import fal_client, os
os.environ['FAL_KEY'] = 'YOUR_FAL_KEY'
url = fal_client.upload_file('./brand/01_logos/primary_v1.png')
print(url)
"

python ~/.claude/skills/fal-media-generator/scripts/generate.py image \
  "Redesign this logo into a vertical stacked variant. The abstract symbol should be centered and enlarged at the top. The wordmark SENTINEL sits centered below the symbol with a gap of approximately one symbol-height between them. Both elements are horizontally centered on the vertical axis. White background. Identical colors to the original: electric teal symbol, deep charcoal wordmark. No additional design elements. Clean, minimal, centered stacked lockup." \
  --image_model gpt-image-2 \
  --image_url "[PRIMARY_LOGO_CDN_URL]" \
  --aspect_ratio 1:1 \
  --quality high
```

## Notes

- The vertical variant often needs 2–3 attempts because gpt-image-2 may center the layout slightly off
- If the symbol is too small relative to the wordmark: add "symbol is 3x the visual weight of the wordmark text" to the prompt
- If the colors drift: add exact hex codes "electric teal #00D4AA, deep charcoal #1C1C1E" explicitly
