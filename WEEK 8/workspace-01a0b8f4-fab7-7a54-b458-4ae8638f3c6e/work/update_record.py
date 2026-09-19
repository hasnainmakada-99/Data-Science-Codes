"""
Update the lab record PDF:
  A. Week-6 footer page numbers 1..21  ->  80..100 (continuing Weeks 1-5 which end at 79)
  B. Index (page 4): append Week-6 rows (Program 11 -> p.80, Program 12 -> p.88), move legend below
  C. Index: correct two wrong page numbers (Program 4: 19 -> 18, Program 8: 56 -> 54)
  D. Program-12 header date typo "20/082026" -> "20/08/2026" (PDF pages 92-104)
Everything else is left byte-for-byte untouched (redaction is applied only to the exact text spans replaced,
with images and vector graphics explicitly excluded from redaction).
"""
import pymupdf

SRC = "/home/user/uploads/assesstment 6 with cover.pdf"
OUT = "/home/user/Lab Record - Assessment 6 (updated).pdf"
FONT_DIR = "/home/user/work/fonts/"
LIB_R = FONT_DIR + "LiberationSerif-Regular.ttf"
LIB_B = FONT_DIR + "LiberationSerif-Bold.ttf"

BLACK = (0, 0, 0)
GRAY = (0x7F / 255,) * 3

REDACT_KW = dict(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                 graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                 text=pymupdf.PDF_REDACT_TEXT_REMOVE)

doc = pymupdf.open(SRC)
assert len(doc) == 104

fs_r = pymupdf.Font(fontfile=LIB_R)
fs_b = pymupdf.Font(fontfile=LIB_B)
f_nb = pymupdf.Font("notosbo")
f_nr = pymupdf.Font("notos")
f_ni = pymupdf.Font("notosit")

log = []


def spans(page):
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                yield s


def redact(page, rects):
    for r in rects:
        page.add_redact_annot(pymupdf.Rect(r), fill=False)
    page.apply_redactions(**REDACT_KW)


def put(page, x, y, text, font_label, fontfile=None, size=10, color=BLACK):
    """Insert text with baseline origin (x, y)."""
    kw = dict(fontsize=size, color=color)
    if fontfile:
        kw.update(fontname=font_label, fontfile=fontfile)
    else:
        kw.update(fontname=font_label)  # pymupdf-fonts alias
    rc = page.insert_text(pymupdf.Point(x, y), text, **kw)
    assert rc >= 0, (text, rc)


def wrap(text, font, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if font.text_length(cand, size) <= width or not cur:
            cur = cand
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- A. Week-6 footers
PAGE_RIGHT_EDGE = 520.0     # right edge of "P a g e" (matches the two-digit pages of Weeks 1-5)
for pno in range(83, 104):          # PDF pages 84..104
    page = doc[pno]
    old_n = pno - 82
    new_n = old_n + 79
    pg_span = num_span = None
    for s in spans(page):
        if s["text"] == "P a g e" and s["bbox"][1] > 770:
            pg_span = s
    assert pg_span, pno
    for s in spans(page):
        if s["bbox"][1] > 770 and s["text"].strip().endswith("|") and abs(s["bbox"][3] - pg_span["bbox"][3]) < 0.5:
            num_span = s
    assert num_span and num_span["text"].strip(" |") == str(old_n), (pno, num_span and num_span["text"])
    r = pymupdf.Rect(num_span["bbox"]) | pymupdf.Rect(pg_span["bbox"])
    baseline = pg_span["origin"][1]
    redact(page, [r])
    num_txt = f"{new_n} | "
    x_pg = PAGE_RIGHT_EDGE - f_nr.text_length("P a g e", 9)
    x_num = x_pg - f_nb.text_length(num_txt, 9)
    put(page, x_num, baseline, num_txt, "notosbo", size=9, color=BLACK)
    put(page, x_pg, baseline, "P a g e", "notos", size=9, color=GRAY)
    log.append(f"PDF p{pno+1}: footer '{old_n} | Page' -> '{new_n} | Page'")

# ---------------------------------------------------------------- D. Program-12 date typo
for pno in range(91, 104):          # PDF pages 92..104
    page = doc[pno]
    tgt = [s for s in spans(page) if s["text"] == "Date: 20/082026"]
    assert len(tgt) == 1, (pno, [s["text"] for s in spans(page) if s["text"].startswith("Date")])
    s = tgt[0]
    redact(page, [s["bbox"]])
    put(page, s["origin"][0], s["origin"][1], "Date: 20/08/2026", "LibSerifB", LIB_B, size=s["size"], color=BLACK)
    log.append(f"PDF p{pno+1}: header 'Date: 20/082026' -> 'Date: 20/08/2026'")

# ---------------------------------------------------------------- C. wrong page numbers in the index
def replace_cell_number(page, old, new, size, y_range):
    tgt = [s for s in spans(page) if s["text"].strip() == old and y_range[0] < s["bbox"][1] < y_range[1] and s["bbox"][0] > 519]
    assert len(tgt) == 1, (old, [(s["text"], s["bbox"]) for s in tgt])
    s = tgt[0]
    redact(page, [s["bbox"]])
    # keep the same horizontal centre inside the "Page No." column
    cx = (s["bbox"][0] + s["bbox"][2]) / 2
    w = fs_r.text_length(new, size)
    put(page, cx - w / 2, s["origin"][1], new, "LibSerifR", LIB_R, size=size, color=BLACK)
    log.append(f"Index: Program page number {old} -> {new}")

replace_cell_number(doc[1], "19", "18", 11, (600, 640))     # Program 4 (Week 2), index page 2
replace_cell_number(doc[3], "56", "54", 10, (30, 80))       # Program 8 (Week 4), index page 4

# ---------------------------------------------------------------- B. Week-6 rows in the index (page 4)
page = doc[3]
legend = [s for s in spans(page) if s["text"].startswith("PP: Practice Program")]
assert len(legend) == 1
legend = legend[0]
legend_text = legend["text"]
legend_x = legend["origin"][0]
old_bottom = 639.35
legend_gap = legend["origin"][1] - old_bottom          # 22.9pt between table bottom and legend baseline
redact(page, [legend["bbox"]])

COLS = [72.8, 110.5, 155.1, 183.2, 218.4, 272.9, 345.7, 520.5, 555.5]
ROW_H = 62.0
SIZE = 10
PITCH = 10.52           # line pitch used in the existing 10-pt rows
FIRST_BASE = 9.9        # first baseline below the row's top rule

rows = [
    dict(week="6", date=["20/08/", "2026"], sl="11", typ="PP", topic="Plotly",
         title="Interactive Bar Chart with Plotly",
         problem="Create an interactive bar chart showing the population of different cities.",
         pg="80"),
    dict(week="6", date=["20/08/", "2026"], sl="12", typ="PP", topic="Plotly",
         title="Interactive Scatter Plot with Plotly",
         problem="Create an interactive scatter plot showing the relationship between house size and price.",
         pg="88"),
]

# --- rules (same 0.5pt black stroke as the existing table)
shape = page.new_shape()
new_bottom = old_bottom + ROW_H * len(rows)
for k in range(1, len(rows) + 1):
    y = old_bottom + ROW_H * k
    if k == len(rows):
        shape.draw_line((72.55, y), (555.75, y))       # outer bottom rule (extends 0.25 like the original)
    else:
        shape.draw_line((73.05, y), (555.25, y))       # inner rule
for x in COLS:
    if x in (COLS[0], COLS[-1]):
        shape.draw_line((x, 639.6), (x, new_bottom + 0.25))
    else:
        shape.draw_line((x, 639.1), (x, new_bottom - 0.25))
shape.finish(color=BLACK, width=0.5, lineCap=0, lineJoin=0)
shape.commit()

def centred_x(text, font, size, x0, x1):
    return (x0 + x1) / 2 - font.text_length(text, size) / 2

for k, row in enumerate(rows):
    top = old_bottom + ROW_H * k
    base = top + FIRST_BASE
    # Week No (bold, centred)
    put(page, centred_x(row["week"], fs_b, SIZE, COLS[0], COLS[1]), base, row["week"], "LibSerifB", LIB_B, SIZE)
    # Date (two lines, left aligned like the existing rows)
    for j, part in enumerate(row["date"]):
        put(page, 116.3, base + PITCH * j, part, "LibSerifR", LIB_R, SIZE)
    # Sl. No.
    put(page, 161.2, base, row["sl"], "LibSerifR", LIB_R, SIZE)
    # Type (centred)
    put(page, centred_x(row["typ"], fs_r, SIZE, COLS[3], COLS[4]), base, row["typ"], "LibSerifR", LIB_R, SIZE)
    # Topic
    put(page, 224.55, base, row["topic"], "LibSerifR", LIB_R, SIZE)
    # Title (wrapped)
    for j, line in enumerate(wrap(row["title"], fs_r, SIZE, COLS[6] - 279.25 - 4.5)):
        put(page, 279.25, base + PITCH * j, line, "LibSerifR", LIB_R, SIZE)
    # Problem statement (wrapped)
    for j, line in enumerate(wrap(row["problem"], fs_r, SIZE, COLS[7] - 351.3 - 4.5)):
        put(page, 351.3, base + PITCH * j, line, "LibSerifR", LIB_R, SIZE)
    # Page No. (centred)
    put(page, centred_x(row["pg"], fs_r, SIZE, COLS[7], COLS[8]), base, row["pg"], "LibSerifR", LIB_R, SIZE)
    log.append(f"Index: added Week 6 / Program {row['sl']} ({row['title']}) -> page {row['pg']}")

# legend re-placed under the extended table, same font/size/x
put(page, legend_x, new_bottom + legend_gap, legend_text, "notosit", size=9, color=BLACK)
log.append(f"Index: legend moved below the new rows (table bottom {old_bottom} -> {new_bottom})")

doc.save(OUT, garbage=3, deflate=True)
doc.close()
print("\n".join(log))
print("saved:", OUT)
