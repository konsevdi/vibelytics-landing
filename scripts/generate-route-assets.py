#!/usr/bin/env python3
"""Generate first-party route imagery for Vibelytics.

The generated PNGs replace route-used assets with deterministic, repo-owned
visuals. The script uses only the Python standard library so the static site
keeps its no-new-dependencies constraint.
"""

from __future__ import annotations

import math
import os
import struct
import zlib

WIDTH = 1672
HEIGHT = 941

DEEP = (4, 6, 13)
PANEL = (7, 16, 30)
CYAN = (30, 231, 255)
MINT = (60, 242, 181)
VIOLET = (163, 106, 255)
EMBER = (255, 139, 92)
BLUE = (87, 150, 255)
GOLD = (246, 198, 91)
INK = (248, 251, 255)


def clamp(value: float, low: int = 0, high: int = 255) -> int:
    return max(low, min(high, int(round(value))))


def mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    t = max(0.0, min(1.0, t))
    return (
        clamp(a[0] + (b[0] - a[0]) * t),
        clamp(a[1] + (b[1] - a[1]) * t),
        clamp(a[2] + (b[2] - a[2]) * t),
    )


class Canvas:
    def __init__(self, width: int = WIDTH, height: int = HEIGHT) -> None:
        self.width = width
        self.height = height
        self.pixels = bytearray(width * height * 3)

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
        cx, cy = self.width * 0.72, self.height * 0.34
        max_dist = math.hypot(self.width, self.height)
        for y in range(self.height):
            row_t = y / (self.height - 1)
            base = mix(top, bottom, row_t)
            for x in range(self.width):
                dist = math.hypot(x - cx, y - cy) / max_dist
                glow = max(0.0, 1.0 - dist * 3.3)
                grain = (((x * 17 + y * 31 + (x ^ y) * 7) % 23) - 11) * 0.55
                color = mix(base, accent, glow * 0.16)
                idx = (y * self.width + x) * 3
                self.pixels[idx] = clamp(color[0] + grain)
                self.pixels[idx + 1] = clamp(color[1] + grain)
                self.pixels[idx + 2] = clamp(color[2] + grain)

    def rect(self, x: int, y: int, w: int, h: int, color: tuple[int, int, int], alpha: float = 1.0) -> None:
        for yy in range(max(0, y), min(self.height, y + h)):
            for xx in range(max(0, x), min(self.width, x + w)):
                self.set_pixel(xx, yy, color, alpha)

    def circle(self, cx: float, cy: float, r: float, color: tuple[int, int, int], alpha: float = 1.0) -> None:
        x0, x1 = int(cx - r), int(cx + r) + 1
        y0, y1 = int(cy - r), int(cy + r) + 1
        r2 = r * r
        for y in range(y0, y1):
            for x in range(x0, x1):
                d2 = (x - cx) ** 2 + (y - cy) ** 2
                if d2 <= r2:
                    edge = 1.0 - math.sqrt(d2 / r2)
                    self.set_pixel(x, y, color, alpha * min(1.0, edge * 4.0))

    def glow(self, cx: float, cy: float, r: float, color: tuple[int, int, int], alpha: float) -> None:
        x0, x1 = int(cx - r), int(cx + r) + 1
        y0, y1 = int(cy - r), int(cy + r) + 1
        r2 = r * r
        for y in range(y0, y1):
            for x in range(x0, x1):
                d2 = (x - cx) ** 2 + (y - cy) ** 2
                if d2 <= r2:
                    falloff = (1.0 - d2 / r2) ** 2
                    self.set_pixel(x, y, color, alpha * falloff)

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: tuple[int, int, int],
        width: float = 2.0,
        alpha: float = 1.0,
    ) -> None:
        steps = int(max(abs(x2 - x1), abs(y2 - y1), 1))
        for i in range(steps + 1):
            t = i / steps
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            self.circle(x, y, width / 2, color, alpha)

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

    def save(self, path: str) -> None:
        def chunk(kind: bytes, data: bytes) -> bytes:
            return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

        raw = bytearray()
        stride = self.width * 3
        for y in range(self.height):
            raw.append(0)
            start = y * stride
            raw.extend(self.pixels[start : start + stride])

        png = b"\x89PNG\r\n\x1a\n"
        png += chunk(b"IHDR", struct.pack(">IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0))
        png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        png += chunk(b"IEND", b"")
        with open(path, "wb") as handle:
            handle.write(png)


def draw_grid(canvas: Canvas, color: tuple[int, int, int], alpha: float, step: int = 84) -> None:
    for x in range(-step, canvas.width + step, step):
        canvas.line(x, canvas.height, x + 420, 0, color, 1.0, alpha)
    for y in range(90, canvas.height, step):
        canvas.line(0, y, canvas.width, y - 120, color, 1.0, alpha)


def draw_signal_nodes(canvas: Canvas, nodes: list[tuple[int, int]], color: tuple[int, int, int]) -> None:
    for i, (x1, y1) in enumerate(nodes):
        for x2, y2 in nodes[i + 1 :]:
            dist = math.hypot(x2 - x1, y2 - y1)
            if dist < 390:
                canvas.line(x1, y1, x2, y2, color, 1.25, 0.14)
    for i, (x, y) in enumerate(nodes):
        accent = [CYAN, MINT, VIOLET, EMBER][i % 4]
        canvas.glow(x, y, 42, accent, 0.16)
        canvas.circle(x, y, 7 + (i % 3) * 2, INK, 0.9)
        canvas.circle(x, y, 4 + (i % 3), accent, 0.95)


def festival_network() -> Canvas:
    c = Canvas()
    c.background((3, 4, 10), (9, 16, 31), CYAN)
    c.glow(1180, 230, 520, VIOLET, 0.24)
    c.glow(820, 470, 360, CYAN, 0.18)
    c.glow(1320, 690, 320, EMBER, 0.12)
    draw_grid(c, BLUE, 0.08, 96)

    c.rect(0, 700, WIDTH, 241, (3, 5, 11), 0.72)
    for x in range(160, 1560, 120):
        c.line(x, 912, 836, 618, (79, 111, 157), 1.2, 0.16)
    c.polygon([(560, 600), (1120, 602), (1315, 775), (350, 774)], (12, 25, 43), 0.84)
    c.polygon([(625, 622), (1050, 623), (1155, 715), (512, 715)], (18, 37, 58), 0.9)
    c.line(625, 622, 512, 715, CYAN, 2.0, 0.36)
    c.line(1050, 623, 1155, 715, MINT, 2.0, 0.32)
    c.line(512, 715, 1155, 715, INK, 1.0, 0.14)

    for start_x, color in [(540, CYAN), (725, MINT), (925, VIOLET), (1120, EMBER)]:
        c.polygon([(start_x, 620), (start_x + 48, 620), (start_x + 190, 130), (start_x - 140, 130)], color, 0.055)
        c.line(start_x, 620, start_x + 80, 148, color, 1.5, 0.2)

    nodes = [
        (310, 238), (470, 326), (602, 212), (755, 376), (900, 282),
        (1056, 370), (1210, 250), (1352, 418), (1480, 330), (695, 548),
        (850, 500), (1018, 536), (1188, 590), (438, 520), (1420, 610),
    ]
    draw_signal_nodes(c, nodes, CYAN)
    for y in [770, 818, 864]:
        c.line(210, y, 1450, y - 28, (248, 251, 255), 1.1, 0.08)
    return c


def taste_map() -> Canvas:
    c = Canvas()
    c.background((4, 7, 15), (5, 15, 26), MINT)
    c.glow(520, 380, 520, CYAN, 0.18)
    c.glow(1280, 500, 470, VIOLET, 0.16)
    draw_grid(c, CYAN, 0.06, 92)

    c.rect(118, 112, 1436, 714, (8, 18, 32), 0.74)
    c.rect(148, 144, 870, 652, (7, 14, 26), 0.84)
    c.rect(1058, 144, 464, 652, (9, 18, 32), 0.82)

    for x in range(210, 980, 92):
        c.line(x, 176, x - 92, 770, (105, 140, 190), 1.0, 0.12)
    for y in range(210, 756, 76):
        c.line(174, y, 990, y - 58, (105, 140, 190), 1.0, 0.11)

    districts = [
        [(245, 255), (390, 218), (515, 280), (470, 420), (305, 438)],
        [(544, 236), (772, 210), (846, 358), (700, 466), (540, 390)],
        [(332, 508), (490, 458), (642, 565), (566, 708), (360, 690)],
        [(720, 506), (910, 420), (960, 658), (792, 746), (650, 610)],
    ]
    for points, color in zip(districts, [CYAN, VIOLET, MINT, BLUE]):
        c.polygon(points, color, 0.08)
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            c.line(x1, y1, x2, y2, color, 1.2, 0.24)

    route = [(310, 392), (465, 336), (620, 414), (760, 356), (892, 478), (810, 640), (604, 614)]
    for (x1, y1), (x2, y2) in zip(route, route[1:]):
        c.line(x1, y1, x2, y2, MINT, 4.0, 0.42)
        c.line(x1, y1, x2, y2, CYAN, 1.5, 0.7)
    draw_signal_nodes(c, route + [(428, 590), (705, 244), (915, 310)], MINT)

    card_y = [184, 330, 476, 622]
    colors = [MINT, GOLD, CYAN, EMBER]
    widths = [286, 220, 318, 250]
    for i, y in enumerate(card_y):
        c.rect(1100, y, 360, 96, (18, 34, 54), 0.78)
        c.rect(1124, y + 28, widths[i], 12, colors[i], 0.72)
        c.rect(1124, y + 56, 220 - i * 18, 8, INK, 0.18)
        c.circle(1436, y + 48, 18, colors[i], 0.8)

    for x in [1124, 1212, 1300, 1388]:
        c.line(x, 730, x + 55, 704, CYAN, 1.2, 0.18)
        c.circle(x + 55, 704, 8, CYAN, 0.48)
    return c


def backstage() -> Canvas:
    c = Canvas()
    c.background((4, 5, 11), (9, 13, 24), EMBER)
    c.glow(930, 430, 530, GOLD, 0.16)
    c.glow(1260, 330, 400, CYAN, 0.12)

    c.rect(0, 690, WIDTH, 251, (5, 7, 13), 0.86)
    c.polygon([(665, 150), (1115, 150), (1258, 705), (502, 705)], (12, 18, 29), 0.9)
    c.polygon([(756, 220), (1026, 220), (1108, 675), (675, 675)], (246, 198, 91), 0.11)
    c.polygon([(800, 270), (990, 270), (1035, 652), (750, 652)], (30, 231, 255), 0.08)

    for x in [250, 396, 542, 1240, 1386, 1532]:
        c.rect(x, 150, 34, 590, (8, 12, 22), 0.86)
        c.line(x + 17, 150, x + 17, 740, (255, 255, 255), 1.0, 0.08)

    for x, y, w, h, color in [
        (170, 705, 320, 118, CYAN),
        (520, 748, 250, 92, MINT),
        (1118, 714, 360, 126, VIOLET),
        (1290, 602, 190, 86, EMBER),
    ]:
        c.rect(x, y, w, h, (12, 23, 38), 0.92)
        c.rect(x + 18, y + 20, w - 36, 10, color, 0.5)
        c.rect(x + 18, y + 50, w - 78, 8, INK, 0.16)
        c.line(x, y, x + w, y, color, 1.5, 0.26)
        c.circle(x + w - 32, y + 28, 10, color, 0.78)

    for sx, color in [(638, CYAN), (814, MINT), (1010, EMBER)]:
        c.polygon([(sx, 180), (sx + 60, 180), (sx + 210, 760), (sx - 230, 760)], color, 0.045)

    for i, x in enumerate([210, 348, 486, 1188, 1326, 1464]):
        c.line(x, 92, x + 42, 220, (80, 106, 150), 2.0, 0.26)
        c.circle(x + 42, 220, 16, [CYAN, MINT, VIOLET, EMBER][i % 4], 0.55)
        c.glow(x + 42, 220, 80, [CYAN, MINT, VIOLET, EMBER][i % 4], 0.08)

    c.line(170, 875, 1510, 842, INK, 1.0, 0.08)
    c.line(280, 928, 820, 690, BLUE, 1.0, 0.09)
    c.line(1390, 928, 890, 690, BLUE, 1.0, 0.09)
    return c


ASSETS = {
    "festival-network.png": festival_network,
    "taste-map.png": taste_map,
    "backstage.png": backstage,
}


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    asset_dir = os.path.join(root, "assets")
    os.makedirs(asset_dir, exist_ok=True)
    for filename, factory in ASSETS.items():
        path = os.path.join(asset_dir, filename)
        factory().save(path)
        print(f"generated {path}")


if __name__ == "__main__":
    main()
