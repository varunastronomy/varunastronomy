"""Create original publication preview cards without contact information."""

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "publications"
PAPERS = {
    "xte-j1810-189.png": ("459 Hz Burst Oscillation", "XTE J1810−189", "ApJ · 2025", "#43D9FF"),
    "m15-x2.png": ("Spectral + Burst Studies", "M15 X-2", "JHEAp · 2026", "#9A7BFF"),
    "4u-1702-429.png": ("Spectral + Burst Studies", "4U 1702−429", "MNRAS · 2024", "#FF8A5B"),
    "gx-349-2.png": ("First Polarimetric View", "GX 349+2", "ApJ · 2025", "#53E0B4"),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def make_card(title: str, source: str, journal: str, accent: str) -> Image.Image:
    width, height = 765, 990
    image = Image.new("RGB", (width, height), "#030817")
    draw = ImageDraw.Draw(image)
    for y in range(height):
        draw.line((0, y, width, y), fill=(3, 8 + y // 85, 23 + y // 35))

    draw.ellipse((100, 80, 665, 645), outline=accent, width=8)
    draw.ellipse((215, 195, 550, 530), fill="#0D2340", outline="#EAFBFF", width=5)
    draw.arc((80, 250, 685, 465), 8, 172, fill=accent, width=18)
    draw.arc((80, 250, 685, 465), 188, 352, fill="#704CFF", width=9)
    for x, y, r in ((120, 150, 5), (650, 115, 7), (90, 610, 4), (690, 560, 5), (620, 720, 4)):
        draw.ellipse((x-r, y-r, x+r, y+r), fill="#DDF8FF")

    draw.text((55, 38), "VARUNASTRONOMY // PUBLICATION", font=font(21, True), fill="#8DB8D3")
    draw.text((width // 2, 690), source, anchor="mm", font=font(48, True), fill="#FFFFFF")
    lines = wrap(title, width=27)
    for i, line in enumerate(lines):
        draw.text((width // 2, 765 + i * 45), line, anchor="mm", font=font(30, True), fill=accent)
    draw.rounded_rectangle((220, 890, 545, 950), radius=20, fill="#101D38", outline=accent, width=3)
    draw.text((width // 2, 920), journal, anchor="mm", font=font(23, True), fill="#EAFBFF")
    return image


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for filename, details in PAPERS.items():
        make_card(*details).save(OUT / filename, optimize=True)
        print(OUT / filename)


if __name__ == "__main__":
    main()
