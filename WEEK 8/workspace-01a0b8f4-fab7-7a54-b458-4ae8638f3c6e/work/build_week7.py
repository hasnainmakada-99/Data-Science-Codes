"""
Build the Assessment-7 record:
  base  = uploads/WEEK 6 FINAL.pdf        (104 pages: cover, 3 index pages, weeks 1-6 numbered 1-100)
  week7 = uploads/Week7_Bokeh_Programs_13_14_15_FIXED.pdf (12 pages, footers 1-12)
Steps
  1. Cover:  'LAB ASSESESMENT-6'  ->  'LAB ASSESSMENT-7'   (highlight box resized to the new text)
  2. Index:  legend removed from index page 4; NEW index page 5 with the three Week-7 rows + legend
  3. Append Week-7 pages; renumber their footers 1-12 -> 101-112 in the record's footer style
"""
import re
import pymupdf

BASE = "/home/user/uploads/WEEK 6 FINAL.pdf"
W7 = "/home/user/uploads/Week7_Bokeh_Programs_13_14_15_FIXED.pdf"
OUT = "/home/user/Lab Record - Assessment 7 (updated).pdf"
FONT_DIR = "/home/user/work/fonts/"
LIB_R, LIB_B = FONT_DIR + "LiberationSerif-Regular.ttf", FONT_DIR + "LiberationSerif-Bold.ttf"

BLACK = (0, 0, 0)
GRAY = (0x7F / 255,) * 3
COVER_ORANGE = (0xC4 / 255, 0x59 / 255, 0x11 / 255)
REDACT_KW = dict(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                 text=pymupdf.PDF_REDACT_TEXT_REMOVE)

fs_r, fs_b = pymupdf.Font(fontfile=LIB_R), pymupdf.Font(fontfile=LIB_B)
f_nb, f_nr, f_ni = pymupdf.Font("notosbo"), pymupdf.Font("notos"), pymupdf.Font("notosit")
log = []


def spans(page):
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                yield s


def redact(page, rects, expect_removed):
    """Redact only `rects`; assert that exactly the spans whose text is in `expect_removed` disappear."""
    before = [(s["text"], round(s["bbox"][0], 1), round(s["bbox"][1], 1)) for s in spans(page)]
    for r in rects:
        page.add_redact_annot(pymupdf.Rect(r), fill=False)
    page.apply_redactions(**REDACT_KW)
    after = set((s["text"], round(s["bbox"][0], 1), round(s["bbox"][1], 1)) for s in spans(page))
    lost = [b for b in before if b not in after]
    unexpected = [b for b in lost if b[0] not in expect_removed]
    assert not unexpected, f"redaction removed unintended text: {unexpected}"
    assert lost, "redaction removed nothing"


def put(page, x, y, text, font_label, fontfile=None, size=10, color=BLACK):
    kw = dict(fontsize=size, color=color, fontname=font_label)
    if fontfile:
        kw["fontfile"] = fontfile
    assert page.insert_text(pymupdf.Point(x, y), text, **kw) >= 0


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


doc = pymupdf.open(BASE)
assert len(doc) == 104

# =============================================================== 1. COVER
cover = doc[0]
old = [s for s in spans(cover) if s["text"] == "LAB ASSESESMENT-6"]
assert len(old) == 1
old = old[0]
new_txt = "LAB ASSESSMENT-7"
size = round(old["size"], 2)                       # 21.0
new_w = fs_b.text_length(new_txt, size)
centre = (old["bbox"][0] + old["bbox"][2]) / 2
# 1a. resize the grey highlight box behind the title (edit the 're' operator in the content stream)
old_re = "188.28 647.22 218.76 24.18 re"
hl_centre = 188.28 + 218.76 / 2
new_re = f"{hl_centre - new_w / 2:.2f} 647.22 {new_w:.2f} 24.18 re"
done = False
for xref in cover.get_contents():
    data = doc.xref_stream(xref)
    if old_re.encode() in data:
        doc.update_stream(xref, data.replace(old_re.encode(), new_re.encode()))
        done = True
assert done, "highlight rect not found"
# 1b. replace the text
tight = pymupdf.Rect(old["bbox"][0] + 0.5, 175.0, old["bbox"][2] - 0.5, old["bbox"][3] - 0.5)
redact(cover, [tight], {"LAB ASSESESMENT-6"})
put(cover, centre - new_w / 2, old["origin"][1], new_txt, "LibSerifB", LIB_B, size=size, color=COVER_ORANGE)
log.append(f"Cover: 'LAB ASSESESMENT-6' -> '{new_txt}' (highlight box resized {old_re!r} -> {new_re!r})")

# =============================================================== 2. INDEX
COLS = [72.8, 110.5, 155.1, 183.2, 218.4, 272.9, 345.7, 520.5, 555.5]
ROW_H, SIZE, PITCH, FIRST_BASE, LEGEND_GAP = 62.0, 10, 10.52, 9.9, 22.9

# 2a. remove the legend from index page 4 (it must sit under the last row of the table)
p4 = doc[3]
legend = [s for s in spans(p4) if s["text"].startswith("PP: Practice Program")]
assert len(legend) == 1
legend_text, legend_x = legend[0]["text"], legend[0]["origin"][0]
redact(p4, [legend[0]["bbox"]], {legend_text})

# 2b. new index page 5 (same size as the other index pages), continuing the table exactly like page 3/4 do
ref = doc[2].rect
p5 = doc.new_page(pno=4, width=ref.width, height=ref.height)
rows = [
    dict(week="7", date=["27/08/", "2026"], sl="13", typ="PP", topic="Bokeh",
         title="Interactive Scatter Plot with Bokeh",
         problem="Create an interactive scatter plot showing the relationship between petal length and petal width "
                 "from the Iris dataset using Bokeh.", pg="101"),
    dict(week="7", date=["27/08/", "2026"], sl="14", typ="EP", topic="Bokeh",
         title="Interactive Line Plot with Bokeh",
         problem="Create an interactive line plot showing the daily temperatures over a week using Bokeh.", pg="105"),
    dict(week="7", date=["27/08/", "2026"], sl="15", typ="EP", topic="Bokeh",
         title="Interactive Bar Chart with Bokeh",
         problem="Create an interactive bar chart showing the sales figures of different products using Bokeh.", pg="109"),
]
top0 = 28.25                                   # continuation pages (3, 4) start their table here
bottom = top0 + ROW_H * len(rows)
sh = p5.new_shape()
sh.draw_line((72.55, top0), (555.75, top0))
for k in range(1, len(rows) + 1):
    y = top0 + ROW_H * k
    if k == len(rows):
        sh.draw_line((72.55, y), (555.75, y))
    else:
        sh.draw_line((73.05, y), (555.25, y))
for x in COLS:
    if x in (COLS[0], COLS[-1]):
        sh.draw_line((x, top0 - 0.25), (x, bottom + 0.25))
    else:
        sh.draw_line((x, top0 + 0.25), (x, bottom - 0.25))
sh.finish(color=BLACK, width=0.5, lineCap=0, lineJoin=0)
sh.commit()


def cx(text, font, size, x0, x1):
    return (x0 + x1) / 2 - font.text_length(text, size) / 2


for k, row in enumerate(rows):
    base = top0 + ROW_H * k + FIRST_BASE
    put(p5, cx(row["week"], fs_b, SIZE, COLS[0], COLS[1]), base, row["week"], "LibSerifB", LIB_B, SIZE)
    for j, part in enumerate(row["date"]):
        put(p5, 116.3, base + PITCH * j, part, "LibSerifR", LIB_R, SIZE)
    put(p5, 161.2, base, row["sl"], "LibSerifR", LIB_R, SIZE)
    put(p5, cx(row["typ"], fs_r, SIZE, COLS[3], COLS[4]), base, row["typ"], "LibSerifR", LIB_R, SIZE)
    put(p5, 224.55, base, row["topic"], "LibSerifR", LIB_R, SIZE)
    for j, line in enumerate(wrap(row["title"], fs_r, SIZE, COLS[6] - 279.25 - 4.5)):
        put(p5, 279.25, base + PITCH * j, line, "LibSerifR", LIB_R, SIZE)
    for j, line in enumerate(wrap(row["problem"], fs_r, SIZE, COLS[7] - 351.3 - 4.5)):
        put(p5, 351.3, base + PITCH * j, line, "LibSerifR", LIB_R, SIZE)
    put(p5, cx(row["pg"], fs_r, SIZE, COLS[7], COLS[8]), base, row["pg"], "LibSerifR", LIB_R, SIZE)
    log.append(f"Index p5: Week 7 / Program {row['sl']} ({row['typ']}) {row['title']} -> page {row['pg']}")
put(p5, legend_x, bottom + LEGEND_GAP, legend_text, "notosit", size=9, color=BLACK)
log.append("Index: legend moved from page 4 to the end of the table on page 5")

# =============================================================== 3. WEEK 7 PAGES
w7 = pymupdf.open(W7)
assert len(w7) == 12
start = len(doc)                     # 105
doc.insert_pdf(w7)
assert len(doc) == start + 12
PAGE_RIGHT_EDGE = 520.0
for k in range(12):
    page = doc[start + k]
    old_n, new_n = k + 1, k + 101
    foot = [s for s in spans(page) if s["bbox"][1] > 775 and s["bbox"][0] > 440]
    txt = "".join(s["text"] for s in sorted(foot, key=lambda s: s["bbox"][0]))
    assert txt == f"{old_n} | P a g e", (start + k + 1, txt)
    r = pymupdf.Rect(foot[0]["bbox"])
    for s in foot[1:]:
        r |= pymupdf.Rect(s["bbox"])
    baseline = foot[0]["origin"][1]
    redact(page, [r], set(s["text"] for s in foot))
    num_txt = f"{new_n} | "
    x_pg = PAGE_RIGHT_EDGE - f_nr.text_length("P a g e", 9)
    put(page, x_pg - f_nb.text_length(num_txt, 9), baseline, num_txt, "notosbo", size=9, color=BLACK)
    put(page, x_pg, baseline, "P a g e", "notos", size=9, color=GRAY)
log.append(f"Week 7: 12 pages appended as PDF p{start+1}-{start+12}; footers 1-12 -> 101-112")

doc.save(OUT, garbage=3, deflate=True)
print("\n".join(log))
print("saved:", OUT, "| pages:", len(doc))
