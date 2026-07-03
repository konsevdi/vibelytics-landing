#!/usr/bin/env python3
"""Generate Vibelytics brand raster derivatives.

Source relationship:
- brand/vibelytics-mark.svg is the canonical editable mark.
- This no-dependency exporter uses the same geometry and colors to produce
  PNG derivatives for the static site and social surfaces.
"""

from __future__ import annotations

import math
import os
import shutil
import struct
import zlib

DEEP = (4, 6, 13)
PANEL = (7, 16, 30)
CYAN = (30, 231, 255)
MINT = (60, 242, 181)
VIOLET = (163, 106, 255)
EMBER = (255, 139, 92)
BLUE = (87, 150, 255)
GOLD = (246, 198, 91)
CORAL = (255, 109, 95)
INK = (248, 251, 255)
MUTED = (196, 206, 220)


FONT = {
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10011", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "01010", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "11011", "10001"],
    "X": ["10001", "01010", "00100", "00100", "00100", "01010", "10001"],
    "Y": ["10001", "01010", "00100", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
}


def clamp(value: float) -> int:
    return max(0, min(255, int(round(value))))


def mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    t = max(0.0, min(1.0, t))
    return (
        clamp(a[0] + (b[0] - a[0]) * t),
        clamp(a[1] + (b[1] - a[1]) * t),
        clamp(a[2] + (b[2] - a[2]) * t),
    )


class Canvas:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.pixels = bytearray(width * height * 3)
        self.fill(DEEP)

    def fill(self, color: tuple[int, int, int]) -> None:
        self.pixels[:] = bytes(color) * (self.width * self.height)

    def set_pixel(self, x: int, y: int, color: tuple[int, int, int], alpha: float = 1.0) -> None:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return
        idx = (y * self.width + x) * 3
        if alpha >= 1:
            self.pixels[idx : idx + 3] = bytes(color)
            return
        inv = 1.0 - alpha
        self.pixels[idx] = clamp(self.pixels[idx] * inv + color[0] * alpha)
        self.pixels[idx + 1] = clamp(self.pixels[idx + 1] * inv + color[1] * alpha)
        self.pixels[idx + 2] = clamp(self.pixels[idx + 2] * inv + color[2] * alpha)

    def background(self, top: tuple[int, int, int], bottom: tuple[int, int, int], accent: tuple[int, int, int]) -> None:
        cx, cy = self.width * 0.78, self.height * 0.28
        max_dist = math.hypot(self.width, self.height)
        for y in range(self.height):
            base = mix(top, bottom, y / max(1, self.height - 1))
            for x in range(self.width):
                dist = math.hypot(x - cx, y - cy) / max_dist
                glow = max(0.0, 1.0 - dist * 2.7)
                grain = (((x * 13 + y * 29 + (x ^ y) * 5) % 19) - 9) * 0.45
                color = mix(base, accent, glow * 0.18)
                idx = (y * self.width + x) * 3
                self.pixels[idx] = clamp(color[0] + grain)
                self.pixels[idx + 1] = clamp(color[1] + grain)
                self.pixels[idx + 2] = clamp(color[2] + grain)

    def rect(self, x: int, y: int, w: int, h: int, color: tuple[int, int, int], alpha: float = 1.0) -> None:
        for yy in range(max(0, y), min(self.height, y + h)):
            for xx in range(max(0, x), min(self.width, x + w)):
                self.set_pixel(xx, yy, color, alpha)

    def rounded_rect(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        r: int,
        color: tuple[int, int, int],
        alpha: float = 1.0,
        gradient: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]] | None = None,
    ) -> None:
        for yy in range(max(0, y), min(self.height, y + h)):
            for xx in range(max(0, x), min(self.width, x + w)):
                dx = max(x - xx, 0, xx - (x + w - 1))
                dy = max(y - yy, 0, yy - (y + h - 1))
                if dx == 0 and dy == 0:
                    corner_x = x + r if xx < x + r else x + w - r - 1 if xx > x + w - r - 1 else xx
                    corner_y = y + r if yy < y + r else y + h - r - 1 if yy > y + h - r - 1 else yy
                    if (xx - corner_x) ** 2 + (yy - corner_y) ** 2 > r * r:
                        continue
                    if gradient:
                        t = ((xx - x) / max(1, w) + (h - (yy - y)) / max(1, h)) / 2
                        base = mix(gradient[0], gradient[1], min(1, t * 1.35))
                        use = mix(base, gradient[2], max(0, t - 0.55) * 1.6)
                    else:
                        use = color
                    self.set_pixel(xx, yy, use, alpha)

    def circle(self, cx: float, cy: float, r: float, color: tuple[int, int, int], alpha: float = 1.0) -> None:
        r2 = r * r
        for y in range(int(cy - r), int(cy + r) + 1):
            for x in range(int(cx - r), int(cx + r) + 1):
                d2 = (x - cx) ** 2 + (y - cy) ** 2
                if d2 <= r2:
                    edge = 1.0 - math.sqrt(d2 / r2)
                    self.set_pixel(x, y, color, alpha * min(1.0, edge * 4.0))

    def glow(self, cx: float, cy: float, r: float, color: tuple[int, int, int], alpha: float) -> None:
        r2 = r * r
        for y in range(int(cy - r), int(cy + r) + 1):
            for x in range(int(cx - r), int(cx + r) + 1):
                d2 = (x - cx) ** 2 + (y - cy) ** 2
                if d2 <= r2:
                    self.set_pixel(x, y, color, alpha * ((1.0 - d2 / r2) ** 2))

    def line(self, x1: float, y1: float, x2: float, y2: float, color: tuple[int, int, int], width: float, alpha: float) -> None:
        steps = int(max(abs(x2 - x1), abs(y2 - y1), 1))
        for i in range(steps + 1):
            t = i / steps
            self.circle(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t, width / 2, color, alpha)

    def polygon(self, points: list[tuple[float, float]], color: tuple[int, int, int], alpha: float) -> None:
        min_x = int(max(0, min(p[0] for p in points)))
        max_x = int(min(self.width - 1, max(p[0] for p in points)))
        min_y = int(max(0, min(p[1] for p in points)))
        max_y = int(min(self.height - 1, max(p[1] for p in points)))
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                inside = False
                j = len(points) - 1
                for i in range(len(points)):
                    xi, yi = points[i]
                    xj, yj = points[j]
                    if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-9) + xi:
                        inside = not inside
                    j = i
                if inside:
                    self.set_pixel(x, y, color, alpha)

    def text(self, text: str, x: int, y: int, scale: int, color: tuple[int, int, int], alpha: float = 1.0) -> None:
        cursor = x
        for char in text.upper():
            glyph = FONT.get(char, FONT[" "])
            for gy, row in enumerate(glyph):
                for gx, bit in enumerate(row):
                    if bit == "1":
                        self.rect(cursor + gx * scale, y + gy * scale, scale, scale, color, alpha)
            cursor += 6 * scale

    def save(self, path: str) -> None:
        def chunk(kind: bytes, data: bytes) -> bytes:
            return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

        raw = bytearray()
        stride = self.width * 3
        for y in range(self.height):
            raw.append(0)
            raw.extend(self.pixels[y * stride : (y + 1) * stride])
        png = b"\x89PNG\r\n\x1a\n"
        png += chunk(b"IHDR", struct.pack(">IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0))
        png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        png += chunk(b"IEND", b"")
        with open(path, "wb") as handle:
            handle.write(png)


def draw_mark(canvas: Canvas, x: int, y: int, size: int, with_shadow: bool = True) -> None:
    if with_shadow:
        canvas.glow(x + size * 0.58, y + size * 0.62, size * 0.55, CYAN, 0.18)
        canvas.glow(x + size * 0.72, y + size * 0.76, size * 0.48, EMBER, 0.12)
    canvas.rounded_rect(
        x,
        y,
        size,
        size,
        int(size * 0.23),
        CYAN,
        1,
        gradient=(MINT, CYAN, VIOLET),
    )
    canvas.glow(x + size * 0.74, y + size * 0.74, size * 0.55, EMBER, 0.16)
    inset = int(size * 0.135)
    canvas.rounded_rect(x + inset, y + inset, size - inset * 2, size - inset * 2, int(size * 0.115), PANEL, 0.94)

    def sx(px: float) -> float:
        return x + size * px / 400.0

    def sy(py: float) -> float:
        return y + size * py / 400.0

    points = [(110, 250), (151, 210), (190, 250), (279, 126), (315, 163), (194, 306)]
    canvas.polygon([(sx(px), sy(py)) for px, py in points], INK, 1)
    canvas.polygon([(sx(151), sy(210)), (sx(190), sy(250)), (sx(169), sy(274)), (sx(128), sy(234))], (221, 248, 255), 0.72)
    canvas.polygon([(sx(194), sy(306)), (sx(315), sy(163)), (sx(297), sy(144)), (sx(184), sy(274))], (255, 255, 255), 0.9)
    canvas.circle(sx(302), sy(154), max(2, size * 0.022), MINT, 1)


def draw_signal_panel(canvas: Canvas, x: int, y: int, w: int, h: int) -> None:
    canvas.rounded_rect(x, y, w, h, 18, (8, 18, 33), 0.86)
    nodes = [
        (x + int(w * 0.14), y + int(h * 0.34)),
        (x + int(w * 0.31), y + int(h * 0.52)),
        (x + int(w * 0.49), y + int(h * 0.30)),
        (x + int(w * 0.64), y + int(h * 0.60)),
        (x + int(w * 0.82), y + int(h * 0.42)),
    ]
    for (x1, y1), (x2, y2) in zip(nodes, nodes[1:]):
        canvas.line(x1, y1, x2, y2, CYAN, 3, 0.52)
    for i, (nx, ny) in enumerate(nodes):
        color = [MINT, CYAN, VIOLET, EMBER, BLUE][i]
        canvas.glow(nx, ny, 54, color, 0.14)
        canvas.circle(nx, ny, 10, color, 0.92)
    bars = [(MINT, 0.74), (GOLD, 0.55), (CORAL, 0.36)]
    for i, (color, pct) in enumerate(bars):
        yy = y + h - 118 + i * 34
        canvas.rect(x + 46, yy, int((w - 92) * pct), 10, color, 0.76)
        canvas.rect(x + 46, yy + 16, int((w - 92) * 0.45), 7, INK, 0.18)


def mark_only(size: int) -> Canvas:
    c = Canvas(size, size)
    c.fill(DEEP)
    pad = max(2, int(size * 0.07))
    draw_mark(c, pad, pad, size - pad * 2, with_shadow=False)
    return c


def avatar() -> Canvas:
    c = Canvas(400, 400)
    c.background((5, 8, 16), (9, 17, 30), CYAN)
    for i in range(-80, 520, 48):
        c.line(i, 400, i + 220, 0, CYAN, 1, 0.08)
        c.line(0, i, 400, i - 80, MINT, 1, 0.06)
    draw_mark(c, 54, 54, 292, True)
    return c


def social(width: int, height: int, header: bool = False) -> Canvas:
    c = Canvas(width, height)
    c.background((3, 5, 12), (8, 15, 28), CYAN)
    c.glow(width * 0.78, height * 0.30, width * 0.34, VIOLET, 0.18)
    c.glow(width * 0.64, height * 0.72, width * 0.25, EMBER, 0.11)
    for x in range(-120, width + 120, 92):
        c.line(x, height, x + 360, 0, BLUE, 1, 0.08)
    for y in range(64, height, 78):
        c.line(0, y, width, y - 120, CYAN, 1, 0.05)

    if header:
        mark_size = 186
        draw_mark(c, 92, 150, mark_size, True)
        c.text("VIBELYTICS", 330, 132, 9, INK, 0.96)
        c.text("AI LAUNCH COPILOT", 334, 252, 4, MUTED, 0.78)
        c.text("GO / ADJUST / HOLD BEFORE SPEND", 334, 318, 3, MINT, 0.84)
        draw_signal_panel(c, width - 455, 92, 350, 318)
    else:
        draw_mark(c, 82, 156, 190, True)
        c.text("VIBELYTICS", 318, 132, 9, INK, 0.96)
        c.text("AI LAUNCH COPILOT", 322, 236, 5, MINT, 0.86)
        c.text("FOR LIVE CULTURE", 322, 294, 5, MUTED, 0.76)
        c.text("GO / ADJUST / HOLD BEFORE SPEND", 322, 420, 3, INK, 0.68)
        draw_signal_panel(c, 900, 156, 220, 318)
    return c


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    brand_dir = os.path.join(root, "brand")

    outputs = {
        os.path.join(root, "favicon.png"): mark_only(64),
        os.path.join(root, "apple-touch-icon.png"): mark_only(180),
        os.path.join(brand_dir, "vibelytics-mark.png"): mark_only(400),
        os.path.join(brand_dir, "vibelytics-x-avatar.png"): avatar(),
        os.path.join(brand_dir, "vibelytics-og-image.png"): social(1200, 630),
        os.path.join(brand_dir, "vibelytics-x-header.png"): social(1500, 500, header=True),
    }
    for path, canvas in outputs.items():
        canvas.save(path)
        print(f"generated {path}")

    shutil.copyfile(os.path.join(brand_dir, "vibelytics-og-image.png"), os.path.join(root, "og-image.png"))
    shutil.copyfile(os.path.join(brand_dir, "vibelytics-og-image.png"), os.path.join(root, "twitter-image.png"))
    print("generated deployed social images")


if __name__ == "__main__":
    main()
