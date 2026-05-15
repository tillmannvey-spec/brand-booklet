#!/usr/bin/env python3
"""
build_asset_index.py — Brand Asset Inventory Builder
Scans ./brand/ subdirectories, reads .meta.json files, prints a Markdown table.
Used by the Haiku subagent in Phase F to populate AGENTS.md.

Usage:
    python build_asset_index.py ./brand/
    python build_asset_index.py --help
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime


FOLDER_LABELS = {
    "01_logos":     "Logos",
    "02_patches":   "Patches",
    "03_stickers":  "Stickers",
    "04_marketing": "Marketing",
    "05_typography": "Typography",
    "06_color":     "Color",
}

LOCKED_PATTERNS = ["primary_v1", "primary_v2"]  # extend as needed

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
DOC_EXTENSIONS = {".md", ".json", ".txt"}


def read_meta(meta_path: Path) -> dict:
    try:
        with open(meta_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def truncate(text: str, max_len: int = 60) -> str:
    if not text:
        return ""
    text = str(text).replace("\n", " ").strip()
    return text[:max_len] + "..." if len(text) > max_len else text


def scan_brand_dir(brand_dir: Path) -> list[dict]:
    assets = []

    for folder_name in sorted(os.listdir(brand_dir)):
        folder_path = brand_dir / folder_name
        if not folder_path.is_dir():
            continue

        label = FOLDER_LABELS.get(folder_name, folder_name)

        for file_name in sorted(os.listdir(folder_path)):
            file_path = folder_path / file_name
            suffix = file_path.suffix.lower()

            # Skip meta files (shown inline), skip hidden files
            if file_name.startswith(".") or suffix == ".json" and file_name.endswith(".meta.json"):
                continue
            # Only index image and doc files
            if suffix not in IMAGE_EXTENSIONS | DOC_EXTENSIONS:
                continue

            meta = {}
            meta_path = folder_path / (file_path.stem + ".meta.json")
            if meta_path.exists():
                meta = read_meta(meta_path)

            # Determine status
            is_locked = any(pat in file_name for pat in LOCKED_PATTERNS)
            status = "Locked" if is_locked else "Approved"
            if suffix in DOC_EXTENSIONS:
                status = "Reference"

            # File size
            try:
                size_kb = file_path.stat().st_size / 1024
                size_str = f"{size_kb:.0f} KB"
            except Exception:
                size_str = "?"

            assets.append({
                "folder":   folder_name,
                "label":    label,
                "file":     file_name,
                "path":     f"./brand/{folder_name}/{file_name}",
                "status":   status,
                "size":     size_str,
                "model":    meta.get("model", ""),
                "prompt":   truncate(meta.get("prompt", ""), 60),
                "date":     meta.get("date", ""),
            })

    return assets


def render_markdown_table(assets: list[dict]) -> str:
    if not assets:
        return "_No assets found._\n"

    lines = [
        "| Folder | File | Status | Size | Model | Notes |",
        "|---|---|---|---|---|---|",
    ]

    current_folder = None
    for a in assets:
        if a["folder"] != current_folder:
            current_folder = a["folder"]

        model_str = a["model"] if a["model"] else ""
        notes = a["prompt"] if a["prompt"] else ""

        lines.append(
            f"| `{a['folder']}` | `{a['file']}` | {a['status']} | {a['size']} "
            f"| {model_str} | {notes} |"
        )

    return "\n".join(lines) + "\n"


def render_locked_list(assets: list[dict]) -> str:
    locked = [a for a in assets if a["status"] == "Locked"]
    if not locked:
        return "_None locked yet._\n"
    return "\n".join(f"- `{a['path']}`" for a in locked) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Scan ./brand/ and print an asset inventory Markdown table."
    )
    parser.add_argument(
        "brand_dir",
        nargs="?",
        default="./brand",
        help="Path to the brand directory (default: ./brand)",
    )
    parser.add_argument(
        "--locked-only",
        action="store_true",
        help="Print only locked assets",
    )
    args = parser.parse_args()

    brand_dir = Path(args.brand_dir)
    if not brand_dir.exists():
        print(f"Error: directory not found: {brand_dir}", file=sys.stderr)
        sys.exit(1)

    assets = scan_brand_dir(brand_dir)

    if args.locked_only:
        print(render_locked_list(assets))
        return

    print(f"<!-- Asset index generated {datetime.now().strftime('%Y-%m-%d %H:%M')} -->")
    print()
    print("## Asset Inventory")
    print()
    print(render_markdown_table(assets))
    print()
    print("## Locked Files (Do Not Modify Without User Approval)")
    print()
    print(render_locked_list(assets))


if __name__ == "__main__":
    main()
