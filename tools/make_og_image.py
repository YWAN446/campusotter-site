"""Draws og_image.png, the picture shown when the site's link is shared.

Run from the site folder:  python tools/make_og_image.py
Needs Playwright for Python with Chromium installed.
"""
import base64
import pathlib

from playwright.sync_api import sync_playwright

SITE = pathlib.Path(__file__).resolve().parent.parent
# The page has no address of its own, so it cannot load a file. Carry the logo inside it.
LOGO = "data:image/png;base64," + base64.b64encode((SITE / "logo.png").read_bytes()).decode("ascii")

PAGE = f"""<!doctype html>
<html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Instrument+Serif&display=swap" rel="stylesheet">
<style>
  body {{ margin: 0; width: 1200px; height: 630px; background: #f4f7f6; color: #0e1f21;
         display: flex; align-items: center; gap: 64px; padding: 0 84px; box-sizing: border-box; }}
  .mark img {{ width: 300px; height: 300px; display: block; border-radius: 64px; }}
  .name {{ font: 400 44px/1 "Instrument Serif", Georgia, serif; color: #0a5f5e; }}
  h1 {{ font: 400 84px/1 "Instrument Serif", Georgia, serif; margin: 18px 0 0; }}
  p {{ font: 400 27px/1.4 Inter, sans-serif; color: #4a5c5e; margin: 26px 0 0; }}
</style></head>
<body>
  <div class="mark"><img src="{LOGO}" alt=""></div>
  <div>
    <div class="name">CampusOtter</div>
    <h1>Find your faculty mentor. Know what to say.</h1>
    <p>A chat assistant for public health students.</p>
  </div>
</body></html>"""

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630})
    page.set_content(PAGE)
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")
    page.screenshot(path=str(SITE / "og_image.png"))
    browser.close()
print("wrote og_image.png")
