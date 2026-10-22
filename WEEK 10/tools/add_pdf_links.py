import re, sys, os
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (ArrayObject, DictionaryObject, NameObject,
                           NumberObject, RectangleObject, TextStringObject)

PDF = sys.argv[1]
GH = ("https://github.com/hasnainmakada-99/Data-Science-Codes/blob/main/"
      "WEEK%2010/programs/")
PROG_URLS = {
 22: GH + "Program22_CaseClasses.scala",
 23: GH + "Program23_SaddleVegas.scala",
 24: GH + "Program24_Breeze.scala",
 25: GH + "Program25_SpireSaddle.scala",
}

reader = PdfReader(PDF)
writer = PdfWriter()
for p in reader.pages:
    writer.add_page(p)

URL_RE = re.compile(r"https?://[^\s<>\"]+")

def fragments(page):
    out = []
    def visitor(text, cm, tm, font_dict, font_size):
        if text and text.strip():
            out.append((text, tm[4], tm[5], font_size or 10))
    page.extract_text(visitor_text=visitor)
    return out

def add_annot(page, rect, url):
    annot = DictionaryObject()
    annot[NameObject("/Type")] = NameObject("/Annot")
    annot[NameObject("/Subtype")] = NameObject("/Link")
    annot[NameObject("/Rect")] = rect
    annot[NameObject("/Border")] = ArrayObject([NumberObject(0)] * 3)
    annot[NameObject("/F")] = NumberObject(4)
    action = DictionaryObject()
    action[NameObject("/S")] = NameObject("/URI")
    action[NameObject("/URI")] = TextStringObject(url)
    annot[NameObject("/A")] = action
    if "/Annots" not in page:
        page[NameObject("/Annots")] = ArrayObject()
    page["/Annots"].append(writer._add_object(annot))

added = 0
for i, page in enumerate(writer.pages):
    txt = page.extract_text() or ""
    m = re.search(r"Program S\. No\.\s*(\d+)", txt)
    prog = int(m.group(1)) if m else None
    prog_url = PROG_URLS.get(prog)

    items = fragments(page)
    # group into lines by y
    lines = {}
    for t, x, y, fs in items:
        lines.setdefault(round(y, 0), []).append((x, t, fs))

    for y, frags in sorted(lines.items(), reverse=True):
        frags.sort(key=lambda f: f[0])
        line = "".join(f[1] for f in frags)
        x_start = frags[0][0]
        fs = frags[0][2]

        # ---- GitHub reference: merge the wrapped continuation lines
        if prog_url and "Python program" in line and "GitHub" in line:
            # walk downward while the following lines look like URL continuations
            ys = sorted(lines.keys(), reverse=True)
            idx = ys.index(y)
            y_low = y
            for k in range(idx + 1, min(idx + 4, len(ys))):
                ny = ys[k]
                nxt = "".join(f[1] for f in sorted(lines[ny], key=lambda f: f[0]))
                if re.match(r"^\s*\d+\.\s", nxt):
                    break
                if ("github.com" in nxt or "WEEK%2010" in nxt or ".scala" in nxt
                        or nxt.strip().startswith("Science-Codes")
                        or nxt.strip().startswith("Data-")):
                    y_low = ny
                else:
                    break
            rect = RectangleObject([x_start, y_low - 3, x_start + 440, y + fs * 1.0])
            add_annot(page, rect, prog_url)
            added += 1
            continue

        if prog_url and "github.com" in line:
            continue

        # ---- plain URLs on a numbered reference line only
        if not re.match(r"^\s*\d+\.\s", line):
            continue
        # a long URL may wrap onto the next line; merge continuations first
        ys_all = sorted(lines.keys(), reverse=True)
        k = ys_all.index(y)
        merged = line
        if not URL_RE.search(line):
            if k + 1 < len(ys_all):
                nxt = "".join(f[1] for f in sorted(lines[ys_all[k + 1]], key=lambda f: f[0]))
                if "http" in line or "https" in line:
                    merged = line + nxt.strip()
        for mm in URL_RE.finditer(merged):
            url = mm.group(0).rstrip(".,;)")
            pos = 0
            x0 = x1 = None
            for fx, ft, ffs in frags:
                end = pos + len(ft)
                if x0 is None and end > mm.start():
                    x0 = fx
                if pos < mm.start() + len(url):
                    x1 = fx + len(ft) * ffs * 0.5
                pos = end
            if x0 is None:
                continue
            if x1 is None or x1 <= x0:
                x1 = x0 + len(url) * fs * 0.5
            rect = RectangleObject([x0, y - 3, x1 + 2, y + fs * 1.0])
            add_annot(page, rect, url)
            added += 1

out = PDF + ".tmp"
with open(out, "wb") as fh:
    writer.write(fh)
os.replace(out, PDF)
print("link annotations added:", added)
