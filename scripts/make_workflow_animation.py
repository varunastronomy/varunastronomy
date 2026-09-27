"""Build the synthetic research-workflow animation used by the profile README."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "research-workflow.gif"
WIDTH, HEIGHT = 1200, 300
STAGES = [
    ("01", "SPACE DATA", "event lists + telemetry", "🛰"),
    ("02", "CALIBRATE", "screening + GTIs", "⚙"),
    ("03", "ANALYSE", "timing + spectra", "📈"),
    ("04", "INTERPRET", "physics + validation", "🧠"),
    ("05", "COMMUNICATE", "papers + open tools", "🚀"),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def frame(active: int, pulse: int) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), "#030817")
    draw = ImageDraw.Draw(image)
    for y in range(HEIGHT):
        shade = int(8 + 14 * y / HEIGHT)
        draw.line((0, y, WIDTH, y), fill=(3, shade, 29 + shade // 2))

    draw.text((42, 24), "VARUNASTRONOMY  //  RESEARCH SIGNAL PATH", font=font(25, True), fill="#EAF7FF")
    draw.text((42, 58), "SYNTHETIC WORKFLOW VISUALISATION", font=font(13, True), fill="#58D6FF")

    centers = [120 + i * 238 for i in range(len(STAGES))]
    y = 155
    for i in range(len(centers) - 1):
        color = "#6B4EFF" if i < active else "#17375B"
        draw.line((centers[i] + 45, y, centers[i + 1] - 45, y), fill=color, width=5)
        for offset in (0, 12, 24):
            x = centers[i] + 70 + ((pulse * 16 + offset) % 125)
            if i == active - 1:
                draw.ellipse((x, y - 4, x + 8, y + 4), fill="#77F5FF")

    for i, ((number, title, subtitle, _), x) in enumerate(zip(STAGES, centers)):
        reached = i <= active
        ring = "#72F3FF" if i == active else ("#765BFF" if reached else "#24405E")
        fill = "#102B4B" if reached else "#091528"
        radius = 43 + (pulse % 3 if i == active else 0)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill, outline=ring, width=4)
        draw.text((x, y - 1), number, anchor="mm", font=font(22, True), fill="#FFFFFF" if reached else "#64809A")
        draw.text((x, 216), title, anchor="mm", font=font(15, True), fill="#DDF7FF" if reached else "#64809A")
        draw.text((x, 241), subtitle, anchor="mm", font=font(11), fill="#7FB6D4" if reached else "#425970")

    draw.rounded_rectangle((930, 24, 1158, 68), radius=14, fill="#101D38", outline="#6B4EFF", width=2)
    draw.text((1044, 46), "AI // TRACEABLE SCIENCE", anchor="mm", font=font(14, True), fill="#DCCFFF")
    return image


def main() -> None:
    frames = [frame(active, pulse) for active in range(len(STAGES)) for pulse in range(6)]
    frames += list(reversed(frames[6:-6]))
    frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=frames[1:],
        duration=120,
        loop=0,
        optimize=True,
    )
    print(OUTPUT)


if __name__ == "__main__":
    main()
