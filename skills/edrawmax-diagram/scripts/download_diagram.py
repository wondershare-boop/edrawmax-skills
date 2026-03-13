#!/usr/bin/env python3
"""
EdrawMax Diagram Downloader
Downloads PNG and SVG files from EdrawMax AI API response URLs to local disk.

Usage:
    python download_diagram.py --png-url <url> --svg-url <url> [--output-dir <dir>]

Output:
    Prints JSON with local file paths:
    {"png_path": "...", "svg_path": "..."}

Security:
    - Only HTTPS URLs from trusted EdrawMax OSS domains are accepted.
    - TLS certificates are fully verified (system trust store).

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
from urllib.parse import urlparse

# Trusted hostname suffixes for EdrawMax OSS URLs.
# Only URLs whose hostname ends with one of these suffixes are allowed.
TRUSTED_HOSTS = (
    ".aliyuncs.com",
    ".wondershare.com",
    ".edrawsoft.com",
    ".edrawmax.com",
)


def validate_url(url: str) -> None:
    """
    Raise ValueError if the URL is not a safe, trusted HTTPS URL.
    Checks:
      - Scheme must be https
      - Hostname must match a trusted EdrawMax OSS domain suffix
    """
    parsed = urlparse(url)
    if parsed.scheme != "https":
        raise ValueError(f"Rejected non-HTTPS URL: {url!r}")
    host = parsed.hostname or ""
    if not any(host.endswith(suffix) for suffix in TRUSTED_HOSTS):
        raise ValueError(
            f"Rejected URL from untrusted host '{host}'. "
            f"Allowed domains: {', '.join(TRUSTED_HOSTS)}"
        )


def download_file(url: str, output_path: str) -> str:
    """
    Download a file from a trusted HTTPS URL to output_path.
    Returns output_path on success, empty string on failure.
    TLS certificate verification uses the system default trust store.
    """
    try:
        validate_url(url)
    except ValueError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return ""

    # Use system default SSL context — certificate verification is enabled.
    ctx = ssl.create_default_context()

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
    png_path = os.path.join(args.output_dir, f"diagram_{timestamp}.png")
    svg_path = os.path.join(args.output_dir, f"diagram_{timestamp}.svg")

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

