import subprocess, os, sys, re
from PIL import Image, ImageDraw

PDF = sys.argv[1]
d = os.path.dirname(PDF)
work = "/tmp/coverwork"
os.makedirs(work, exist_ok=True)
for f in os.listdir(work):
    os.remove(os.path.join(work, f))

# 1. render page 1 at high dpi
subprocess.run(["pdftoppm", "-r", "200", "-png", "-f", "1", "-l", "1", PDF,
                os.path.join(work, "pg")], check=True, capture_output=True)
src = os.path.join(work, "pg-1.png")
if not os.path.exists(src):
    src = [os.path.join(work, f) for f in os.listdir(work) if f.endswith(".png")][0]

im = Image.open(src).convert("RGB")
W, H = im.size

# 2. find the banner circle
target = (0xC4, 0x59, 0x11)
rows = {}
for y in range(int(H * 0.25), int(H * 0.75), 1):
    xs = [x for x in range(0, int(W * 0.5))
          if (lambda p: abs(p[0]-target[0]) < 28 and abs(p[1]-target[1]) < 28
              and abs(p[2]-target[2]) < 28)(im.getpixel((x, y)))]
    if xs:
        rows[y] = (min(xs), max(xs))
ys = sorted(rows)
bands = []
start = prev = ys[0]
for y in ys[1:]:
    if y - prev > 20:
        bands.append((start, prev)); start = y
    prev = y
bands.append((start, prev))
b0 = bands[0]
mid = (b0[0] + b0[1]) // 2
r = (b0[1] - b0[0]) / 2.0
cx = rows[mid][0] + r
cy = mid
print("circle: cx=%.0f cy=%.0f r=%.0f (img %dx%d)" % (cx, cy, r, W, H))

# 3. composite the circular student photo
photo = Image.open("/tmp/a8img/i-002.png").convert("RGBA")
size = int(2 * r)
photo = photo.resize((size, size), Image.LANCZOS)
mask = Image.new("L", (size * 4, size * 4), 0)
ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
mask = mask.resize((size, size), Image.LANCZOS)
photo.putalpha(mask)
im.paste(photo, (int(cx - r), int(cy - r)), photo)

out_png = os.path.join(work, "cover.png")
im.save(out_png, dpi=(200, 200))
print("composited cover ->", out_png)

# 4. new single-page PDF from the image
one = os.path.join(work, "cover.pdf")
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
c = canvas.Canvas(one, pagesize=A4)
c.drawImage(out_png, 0, 0, width=A4[0], height=A4[1])
c.showPage(); c.save()

# 5. replace page 1, keep the rest
rest = os.path.join(work, "rest.pdf")
subprocess.run(["mutool", "merge", "-o", rest, PDF, "2-N"], check=True, capture_output=True)
final = os.path.join(work, "final.pdf")
subprocess.run(["mutool", "merge", "-o", final, one, rest], check=True, capture_output=True)
import shutil; shutil.copy(final, PDF)
print("rebuilt PDF with photo on cover")
