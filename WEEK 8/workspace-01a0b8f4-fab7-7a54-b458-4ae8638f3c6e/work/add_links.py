import pymupdf
IN  = "/home/user/Lab Record - Assessment 6 (updated).pdf"
OUT = "/home/user/work/tmp_links.pdf"
LIB_R = "/home/user/work/fonts/LiberationSerif-Regular.ttf"
BLUE = (0x05/255, 0x63/255, 0xC1/255)
UL_COLOR = (0.019607843831181526, 0.38823530077934265, 0.7568627595901489)
UL_WIDTH = 0.6519500017166138
doc = pymupdf.open(IN)

def spans(page):
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0: continue
        for l in b["lines"]:
            for s in l["spans"]:
                yield s

def add_uri(page, rect, uri):
    page.insert_link({"kind": pymupdf.LINK_URI, "from": pymupdf.Rect(rect), "uri": uri})

# ---- p91 (Program 11): URL text is complete and exists on GitHub -> just attach the link to both wrapped lines
p = doc[90]
url11 = "https://github.com/hasnainmakada-99/Data-Science-Codes/blob/main/WEEK%206/Week-6-PP.ipynb"
parts = [s for s in spans(p) if s["text"] in ("https://github.com/hasnainmakada-", "99/Data-Science-Codes/blob/main/WEEK%206/Week-6-PP.ipynb")]
assert len(parts) == 2, [s["text"] for s in parts]
assert "".join(s["text"] for s in sorted(parts, key=lambda s: s["bbox"][1])) == url11
for s in parts: add_uri(p, s["bbox"], url11)
print("p91: GitHub link attached (2 line-rects) ->", url11)

# ---- p104 (Program 12): printed target '...Week-6-PP2.pdf' does not exist; repo file is 'Week-6-PP2.ipynb'
p = doc[103]
url12 = "https://github.com/hasnainmakada-99/Data-Science-Codes/blob/main/WEEK%206/Week-6-PP2.ipynb"
first = [s for s in spans(p) if s["text"] == "https://github.com/hasnainmakada-"]
second = [s for s in spans(p) if s["text"] == "99/Data-Science-Codes/blob/main/WEEK%206/Week-6-PP2.pdf"]
assert len(first) == 1 and len(second) == 1
s2 = second[0]
new_txt = "99/Data-Science-Codes/blob/main/WEEK%206/Week-6-PP2.ipynb"
# replace the text of line 2 (same font, size, colour, baseline)
p.add_redact_annot(pymupdf.Rect(s2["bbox"]), fill=False)
p.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE, text=pymupdf.PDF_REDACT_TEXT_REMOVE)
p.insert_text(pymupdf.Point(*s2["origin"]), new_txt, fontname="LibSerifR", fontfile=LIB_R, fontsize=s2["size"], color=BLUE)
new_end = s2["origin"][0] + pymupdf.Font(fontfile=LIB_R).text_length(new_txt, s2["size"])
# extend the blue underline (old one ends at 476.5, y=185.7) to the new text end
sh = p.new_shape(); sh.draw_line((476.3, 185.7), (new_end + 0.5, 185.7)); sh.finish(color=UL_COLOR, width=UL_WIDTH); sh.commit()
add_uri(p, first[0]["bbox"], url12)
add_uri(p, (s2["bbox"][0], s2["bbox"][1], new_end + 0.5, s2["bbox"][3]), url12)
print(f"p104: text 'Week-6-PP2.pdf' -> 'Week-6-PP2.ipynb' (line now ends at x={new_end:.1f}), underline extended, link attached ->", url12)

doc.save(OUT, garbage=3, deflate=True)
