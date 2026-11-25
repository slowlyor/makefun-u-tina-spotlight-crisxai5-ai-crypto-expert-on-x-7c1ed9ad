#!/usr/bin/env python3
"""Generate the spotlight graphic for @crisxai5 (1080x1350, phone-readable).

Drawn from scratch with Pillow: vertical gradient, glow orbs, glass chips,
big bold type. No external images used. Translucent shapes are drawn on a
separate overlay layer and alpha-composited (ImageDraw does not blend alpha
on its own).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

# --- background: deep navy -> violet gradient ---
top = (8, 12, 38)
bottom = (38, 16, 84)
img = Image.new("RGB", (W, H))
px = img.load()
for y in range(H):
    t = y / (H - 1)
    row = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    for x in range(W):
        px[x, y] = row

# --- glow orbs on a separate layer, blurred ---
glow = Image.new("RGB", (W, H), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([-220, -140, 420, 420], fill=(34, 120, 220))
gd.ellipse([700, 180, 1280, 760], fill=(150, 60, 220))
gd.ellipse([120, 980, 700, 1520], fill=(20, 160, 190))
glow = glow.filter(ImageFilter.GaussianBlur(140))
img = Image.blend(img, glow, 0.55)

# work in RGBA from here; overlay holds every translucent shape
img = img.convert("RGBA")
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
d = ImageDraw.Draw(img, "RGBA")

def center(y, text, fnt, fill):
    w = d.textlength(text, font=fnt)
    d.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size

def pill(y, text, fnt, pad_x=34, pad_y=14):
    tw = od.textlength(text, font=fnt)
    x0 = (W - tw) / 2 - pad_x
    x1 = (W + tw) / 2 + pad_x
    od.rounded_rectangle([x0, y, x1, y + fnt.size + pad_y * 2], radius=40,
                         fill=(255, 255, 255, 28),
                         outline=(255, 255, 255, 110), width=2)
    od.text(((W - tw) / 2, y + pad_y), text, font=fnt,
            fill=(255, 255, 255, 255))
    return y + fnt.size + pad_y * 2

# --- top eyebrow ---
y = 72
y = center(y, "SPOTLIGHT  •  MUST-FOLLOW ON X", font(BOLD, 32),
           (120, 200, 255))
d.line([(W / 2 - 130, y + 22), (W / 2 + 130, y + 22)],
       fill=(255, 200, 60), width=5)
y += 56

# --- avatar medallion: gold ring + big "C" ---
cx, cy, r = W // 2, y + 108, 108
od.ellipse([cx - r - 12, cy - r - 12, cx + r + 12, cy + r + 12],
           outline=(255, 200, 60, 255), width=9)
od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(20, 40, 90, 255),
           outline=(120, 200, 255, 255), width=4)
img = Image.alpha_composite(img, overlay)
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
d = ImageDraw.Draw(img, "RGBA")
f_c = font(BLACK, 140)
cw = d.textlength("C", font=f_c)
d.text((cx - cw / 2, cy - 88), "C", font=f_c, fill=(255, 255, 255))
y = cy + r + 36

# --- handle + title ---
y = center(y, "@crisxai5", font(BLACK, 100), (255, 255, 255))
y += 14
y = center(y, "AI & Crypto Expert", font(BOLD, 56), (255, 200, 60))
y += 24

# --- tagline (two lines) ---
y = center(y, "AI agents. Crypto insights.", font(REG, 42),
           (225, 235, 255))
y = center(y + 52, "Web3 innovation — all in one feed.", font(REG, 42),
           (225, 235, 255))
y += 56

# --- topic chips (plain text: Noto has no color-emoji glyphs) ---
for label in ["AI Agents", "Crypto Insights", "Web3 Innovation"]:
    y = pill(y, label, font(BOLD, 38))
    y += 16
y += 18

# composite the chips, then draw the opaque CTA card on top
img = Image.alpha_composite(img, overlay)
d = ImageDraw.Draw(img, "RGBA")

card_y0 = y
card_y1 = y + 168
d.rounded_rectangle([70, card_y0, W - 70, card_y1], radius=34,
                    fill=(255, 200, 60, 255))
d.text((140, card_y0 + 22), "FOLLOW", font=font(BLACK, 62),
       fill=(10, 16, 40))
d.text((140, card_y0 + 100), "x.com/crisxai5", font=font(BOLD, 36),
       fill=(10, 16, 40))
ax, ay = W - 190, card_y0 + 84
d.ellipse([ax - 48, ay - 48, ax + 48, ay + 48], fill=(10, 16, 40, 255))
# arrow drawn with lines (no glyph dependency)
d.line([(ax - 22, ay), (ax + 16, ay)], fill=(255, 200, 60), width=7)
d.line([(ax + 16, ay), (ax - 2, ay - 16)], fill=(255, 200, 60), width=7)
d.line([(ax + 16, ay), (ax - 2, ay + 16)], fill=(255, 200, 60), width=7)

# --- footer ---
fy = H - 64
f_foot = font(REG, 30)
fw = d.textlength("Made for the make.fun spotlight bounty", font=f_foot)
d.text(((W - fw) / 2, fy), "Made for the make.fun spotlight bounty",
       font=f_foot, fill=(160, 175, 210))

img.convert("RGB").save("crisxai5-spotlight.png", optimize=True)
print("saved crisxai5-spotlight.png", img.size)
