#!/usr/bin/env python3
"""Render render.html to entry.png with headless Chromium (build-time only)."""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
HTML = HERE / "render.html"
OUT = HERE / "entry.png"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/home/hatch/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome",
            args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
        )
        page = browser.new_page(viewport={"width": 1024, "height": 1024})
        page.goto(HTML.as_uri())
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT), clip={"x": 0, "y": 0, "width": 1024, "height": 1024})
        browser.close()
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
