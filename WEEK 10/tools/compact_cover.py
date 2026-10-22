import sys
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

path = sys.argv[1]
doc = Document(path)
COVER = {"Laboratory Record","submitted as part of","Programming for Data Science Lab",
         "(MACSE502)","LAB ASSESESMENT-9","LAB ASSESESMENT-10","LAB ASSESSMENT-9","LAB ASSESSMENT-10","by","To","Dr M Rajasekhara Babu",
         "School of Computer Science and Engineering"}
seen = False
for p in doc.paragraphs:
    t = p.text.strip()
    if t in COVER or t.startswith("October"):
        seen = True
    if not seen:
        continue
    pf = p.paragraph_format
    pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 1.0
    if t == "":
        for r in p.runs:
            r.font.size = Pt(2)
    if t.startswith("October"):
        break
doc.save(path)
print("cover compacted")
