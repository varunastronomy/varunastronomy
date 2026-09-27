#!/usr/bin/env python3
"""Create subtle looping GIFs from synthetic profile artwork."""
from pathlib import Path
from PIL import Image, ImageEnhance
import math

ROOT = Path(__file__).resolve().parents[1] / "assets" / "dynamic-universe"
SPECS = {
    "neutron-star-burst": (0.055, 0.34, 0.0),
    "spinning-black-hole": (0.035, 0.10, 1.2),
    "neutron-star-jets": (0.030, 0.20, 0.0),
    "stellar-flare": (0.045, 0.28, 0.0),
    "accreting-binary": (0.040, 0.16, 0.0),
}

for name, (zoom_amp, light_amp, rotation_amp) in SPECS.items():
    source = Image.open(ROOT / f"{name}.png").convert("RGB")
    source.thumbnail((540, 304), Image.Resampling.LANCZOS)
    width, height = source.size
    frames = []
    for index in range(24):
        phase = 2 * math.pi * index / 24
        zoom = 1 + zoom_amp * (1 + math.sin(phase)) / 2
        size = (round(width * zoom), round(height * zoom))
        frame = source.resize(size, Image.Resampling.LANCZOS)
        left = (frame.width - width) // 2
        top = (frame.height - height) // 2
        frame = frame.crop((left, top, left + width, top + height))
        if rotation_amp:
            frame = frame.rotate(rotation_amp * math.sin(phase), Image.Resampling.BICUBIC)
        brightness = 1 + light_amp * max(0, math.sin(phase))
        frame = ImageEnhance.Brightness(frame).enhance(brightness)
        frames.append(frame.quantize(colors=192, method=Image.Quantize.MEDIANCUT))
    frames[0].save(
        ROOT / f"{name}.gif",
        save_all=True,
        append_images=frames[1:],
        duration=75,
        loop=0,
        optimize=True,
        disposal=2,
    )
