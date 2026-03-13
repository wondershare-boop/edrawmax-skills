#!/usr/bin/env python3
"""
EdrawMax Diagram Downloader
Downloads PNG and SVG files from EdrawMax AI API response URLs to local disk.

Usage:
    python download_diagram.py --png-url <url> --svg-url <url> [--output-dir <dir>]

Output:
    Prints JSON with local file paths:
    {"png_path": "...", "svg_path": "..."}

Author: EdrawMax AI Team（万兴图示 AI 团队）
© 2026 Wondershare EdrawMax（万兴图示）. All rights reserved.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import ssl
from datetime import datetime


def download_file(url: str, output_path: str) -> str:
    """Download a file from URL to output_path. Returns the output_path on success."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, headers={"User-Agent": "EdrawMax-Skill/2.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            data = resp.read()
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(data)
        return output_path
    except urllib.error.URLError as e:
        print(f"[ERROR] Failed to download {url}: {e}", file=sys.stderr)
        return ""
    except OSError as e:
        print(f"[ERROR] Failed to write {output_path}: {e}", file=sys.stderr)
        return ""


def main():
    parser = argparse.ArgumentParser(description="Download EdrawMax diagram files")
    parser.add_argument("--png-url", required=True, help="PNG image URL from API response")
    parser.add_argument("--svg-url", required=True, help="SVG image URL from API response")
    parser.add_argument("--output-dir", default="./edrawmax_output", help="Output directory (default: ./edrawmax_output)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    png_filename = f"diagram_{timestamp}.png"
    svg_filename = f"diagram_{timestamp}.svg"

    png_path = os.path.join(args.output_dir, png_filename)
    svg_path = os.path.join(args.output_dir, svg_filename)

    result = {"png_path": "", "svg_path": ""}

    downloaded_png = download_file(args.png_url, png_path)
    if downloaded_png:
        result["png_path"] = os.path.abspath(downloaded_png)

    downloaded_svg = download_file(args.svg_url, svg_path)
    if downloaded_svg:
        result["svg_path"] = os.path.abspath(downloaded_svg)

    print(json.dumps(result, ensure_ascii=False))

    if not result["png_path"] and not result["svg_path"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
