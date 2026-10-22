import os, json, sys
sys.path.insert(0, "/tmp")
from content_w9 import S
from docx import Document
from docx.shared import Pt, Inches, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = "/media/bruce-wayne/HASNAIN/VIT WORK/Data-Science-Codes/WEEK 9"
ASSETS = os.path.join(BASE, "assets")
PROG = os.path.join(BASE, "programs")
COVER = os.path.join(BASE, "PDS_lab_CoverPage_Week_9.docx")
INDEX_TPL = os.path.join(BASE, "Index_SlNo_01_21.docx")
OUT = os.path.join(BASE, "Week9_Programs_18_21.docx")
PMAP = "/tmp/w9_pagemap.json"
PAGES = json.load(open(PMAP)) if os.path.exists(PMAP) else {}

TNR, MONO = "Times New Roman", "Consolas"
C_TITLE, C_LABEL, C_BODY = "833C0B", "F7CAAC", "FFFFFF"
C_FNHEAD, C_IDXHEAD, C_IDXBAND = "C45911", "EB782C", "F7DED1"

STUDENT = "Student Reg. No: 26MML0031    Name: Hasnain Makada"
FACULTY = ("Faculty: Dr Rajasekhara Babu M, Professor, School of CSE, "
           "Vellore Institute of Technology (VIT), Vellore")
START_PAGE = 131
GH = "https://github.com/hasnainmakada-99/Data-Science-Codes/blob/main/WEEK%209/programs/"
SRC = {18:"Program18_Arrays.scala", 19:"Program19_ListsSetsTuples.scala",
       20:"Program20_HashMapCollisions.scala", 21:"Program21_FunctionalCombinators.scala"}

def shade(cell, hexfill):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    if hexfill is None:
        return
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexfill)
    tcPr.append(shd)

def vcenter(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    va = OxmlElement("w:vAlign"); va.set(qn("w:val"), "center")
    tcPr.append(va)

def vmerge(cell, val):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:vMerge")):
        tcPr.remove(old)
    vm = OxmlElement("w:vMerge")
    if val:
        vm.set(qn("w:val"), val)
    tcPr.append(vm)

def page_border(section):
    sectPr = section._sectPr
    for old in sectPr.findall(qn("w:pgBorders")):
        sectPr.remove(old)
    b = OxmlElement("w:pgBorders")
    b.set(qn("w:display"), "allPages"); b.set(qn("w:offsetFrom"), "page")
    for edge in ("top", "left", "bottom", "right"):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:val"), "double"); e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "24"); e.set(qn("w:color"), "000000")
        e.set(qn("w:shadow"), "1")
        b.append(e)
    anchor = None
    for tag in ("w:pgNumType", "w:cols", "w:docGrid"):
        el = sectPr.find(qn(tag))
        if el is not None:
            anchor = el; break
    if anchor is not None:
        anchor.addprevious(b)
    else:
        sectPr.append(b)

def tight(table, t=15, b=15, l=60, r=60):
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblCellMar")):
        tblPr.remove(old)
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", t), ("left", l), ("bottom", b), ("right", r)):
        e = OxmlElement("w:" + side); e.set(qn("w:w"), str(val)); e.set(qn("w:type"), "dxa")
        mar.append(e)
    tblPr.append(mar)

def set_widths(table, widths):
    table.autofit = False
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblLayout")):
        tblPr.remove(old)
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    for old in tblPr.findall(qn("w:tblW")):
        tblPr.remove(old)
    tw = OxmlElement("w:tblW")
    tw.set(qn("w:w"), str(int(sum(w.twips for w in widths)))); tw.set(qn("w:type"), "dxa")
    tblPr.append(tw)
    grid = table._tbl.find(qn("w:tblGrid"))
    if grid is not None:
        table._tbl.remove(grid)
    g = OxmlElement("w:tblGrid")
    for w in widths:
        gc = OxmlElement("w:gridCol"); gc.set(qn("w:w"), str(int(w.twips))); g.append(gc)
    table._tbl.insert(list(table._tbl).index(table._tbl.tblPr) + 1, g)
    for row in table.rows:
        for i, c in enumerate(row.cells):
            if i < len(widths):
                c.width = widths[i]

def put(cell, text, size=10, bold=False, color=None, align=None, mono=False, valign="top"):
    cell.text = ""
    p = cell.paragraphs[0]
    if align is not None:
        p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 1.0
    for i, ln in enumerate(str(text).split(chr(10))):
        if i:
            p = cell.add_paragraph()
            pf = p.paragraph_format
            pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 1.0
            if align is not None:
                p.alignment = align
        r = p.add_run(ln)
        r.font.size = Pt(size); r.font.bold = bold
        r.font.name = MONO if mono else TNR
        if color:
            r.font.color.rgb = RGBColor.from_string(color)
        if mono:
            rpr = r._r.get_or_add_rPr()
            rf = OxmlElement("w:rFonts")
            rf.set(qn("w:ascii"), MONO); rf.set(qn("w:hAnsi"), MONO)
            rpr.append(rf)
    if valign == "center":
        vcenter(cell)

def add_field(p, instr, ph):
    r = p.add_run()
    f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin"); r._r.append(f1)
    r2 = p.add_run()
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr
    r2._r.append(it)
    r3 = p.add_run()
    f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "separate"); r3._r.append(f2)
    r4 = p.add_run(ph)
    r5 = p.add_run()
    f3 = OxmlElement("w:fldChar"); f3.set(qn("w:fldCharType"), "end"); r5._r.append(f3)
    r4.font.size = Pt(9); r4.font.name = TNR


import re as _re2
URL_RE = _re2.compile(r"(https?://[^\s]+)")

def add_hyperlink(paragraph, url, text, size=10.5):
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts"); rf.set(qn("w:ascii"), TNR); rf.set(qn("w:hAnsi"), TNR)
    rPr.append(rf)
    col = OxmlElement("w:color"); col.set(qn("w:val"), "0563C1"); rPr.append(col)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rPr.append(sz)
    run.append(rPr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    run.append(t)
    link.append(run)
    paragraph._p.append(link)

def put_linked(cell, text, size=10.5):
    cell.text = ""
    lines = str(text).split(chr(10))
    for i, ln in enumerate(lines):
        p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 1.0
        pos = 0
        for m in URL_RE.finditer(ln):
            if m.start() > pos:
                r = p.add_run(ln[pos:m.start()])
                r.font.size = Pt(size); r.font.name = TNR
            add_hyperlink(p, m.group(1), m.group(1), size=size)
            pos = m.end()
        if pos < len(ln):
            r = p.add_run(ln[pos:])
            r.font.size = Pt(size); r.font.name = TNR

def clear_paras(c):
    for p in list(c.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    c.paragraphs[0].text = ""

def build_header(section, prog):
    section.header.is_linked_to_previous = False
    hdr = section.header
    clear_paras(hdr)
    for i, (txt, b, sz) in enumerate([("2026 FALL SEMESTER", True, 12),
                                      ("Programming for Data Science (MACSE502) Lab Record", True, 12),
                                      (prog["typ"], True, 11)]):
        p = hdr.paragraphs[0] if i == 0 else hdr.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pf = p.paragraph_format; pf.space_before = Pt(0); pf.space_after = Pt(0)
        r = p.add_run(txt); r.font.bold = b; r.font.size = Pt(sz); r.font.name = TNR
    p = hdr.add_paragraph()
    pf = p.paragraph_format; pf.space_before = Pt(0); pf.space_after = Pt(0)
    pPr = p._p.get_or_add_pPr()
    tabs = OxmlElement("w:tabs")
    for pos, al in ((4513, "center"), (9026, "right")):
        t = OxmlElement("w:tab")
        t.set(qn("w:val"), al)
        t.set(qn("w:pos"), str(pos))
        tabs.append(t)
    pPr.append(tabs)
    for txt in ("Date: " + prog["date"], chr(9) + "Week No.: " + str(prog["week"]),
                chr(9) + "Program S. No. " + str(prog["no"])):
        r = p.add_run(txt); r.font.size = Pt(12); r.font.name = TNR; r.font.bold = True

def build_footer(section, ph=None):
    section.footer.is_linked_to_previous = False
    ftr = section.footer
    clear_paras(ftr)
    p1 = ftr.paragraphs[0]; p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p1.add_run(STUDENT); r.font.size = Pt(9); r.font.name = TNR
    p2 = ftr.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p2.add_run(FACULTY); r.font.size = Pt(9); r.font.name = TNR; r.font.italic = True
    p3 = ftr.add_paragraph(); p3.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    add_field(p3, " PAGE ", str(ph or START_PAGE))
    r = p3.add_run(" | P a g e"); r.font.size = Pt(9); r.font.name = TNR

# ---------------------------------------------------------------- build
doc = Document(COVER)

# cover: faculty line + student photo
for i, p in enumerate(doc.paragraphs):
    if p.text.strip() == "School of Computer Science and Engineering":
        fac = p.insert_paragraph_before("Dr M Rajasekhara Babu")
        fac.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in fac.runs:
            r.font.size = Pt(14); r.font.bold = True; r.font.name = TNR
        break

cover = doc.sections[0]
cover.left_margin = cover.right_margin = Emu(914400)
cover.top_margin = cover.bottom_margin = Emu(457200)
cover.header.is_linked_to_previous = False
cover.footer.is_linked_to_previous = False

# ---- INDEX ----
idx = doc.add_section(WD_SECTION.NEW_PAGE)
idx.orientation = WD_ORIENT.PORTRAIT
idx.page_width = Emu(7560310); idx.page_height = Emu(10692130)
idx.left_margin = idx.right_margin = Emu(457200)
idx.top_margin = Emu(457200); idx.bottom_margin = Emu(457200)
page_border(idx)
idx.header.is_linked_to_previous = False; clear_paras(idx.header)
idx.footer.is_linked_to_previous = False; clear_paras(idx.footer)

def heading(text, size=12):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format; pf.space_before = Pt(0); pf.space_after = Pt(0)
    r = p.add_run(text); r.font.bold = True; r.font.size = Pt(size); r.font.name = TNR

heading("2026 FALL SEMESTER")
heading("Programming for Data Science Lab (MACSE502) Record")
heading("INDEX")

TITLES = {
 2: "AI Model Performance Analysis Using Pandas",
 4: "Movie Rating Data Preprocessing Using Pandas",
 6: "Warehouse Shipment and Logistic Analytics Using NumPy",
 8: "Employee Attrition Prediction Using Workforce Indicators",
 9: "Web Scraping and Data Collection",
 10: "Online Job Market Analytics",
}

PREV = {1:"1",2:"6",3:"14",4:"18",5:"30",6:"35",7:"46",8:"54",9:"63",10:"70",
        11:"80",12:"88",13:"101",14:"105",15:"109",16:"113",17:"122"}
EXTRA = {
 2:("An AI company maintains model performance records containing:\n\u2022  ModelID\n"
    "\u2022  Accuracy\n\u2022  Algorithm\nPerform:\n1. Select ModelID and Accuracy.\n"
    "2. Filter models with Accuracy greater than 90%.\n3. Add Status with default value "
    "\"Production Ready\".\n4. Sort models by Accuracy.\n5. Calculate average model accuracy."),
 4:("A streaming platform maintains movie records containing:\n\u2022  MovieID\n"
    "\u2022  Rating\n\u2022  Genre\nPerform:\n1. Create a dataset with missing values.\n"
    "2. Fill missing Rating values using average rating.\n3. Remove rows with missing "
    "MovieID or Genre.\n4. Convert Rating into integer type.\nNormalize rating values."),
 6:("A logistics company tracks shipments from 4 warehouses across 7 weeks. Create a 4 x 7 "
    "shipment matrix. Perform: (1) compute average shipments, (2) compute standard deviation, "
    "(3) slice the first two warehouses and last three weeks, (4) reshape the matrix into a "
    "7 x 4 matrix, and (5) perform element-wise multiplication with a transportation-cost "
    "matrix of the same shape."),
 8:("A company wants to analyze workforce behavior and predict employee attrition. Create a "
    "DataFrame containing: OvertimeHours JobSatisfactionScore SalaryLevel TrainingHours "
    "WorkLifeBalance YearsAtCompany PromotionCount AttritionStatus\nPerform:\n"
    "1. Create Log_OvertimeHours.\n2. Categorize JobSatisfactionScore into: Disengaged, "
    "Satisfied, Highly Engaged.\n3. Generate correlation matrix.\n4. Create a Treemap "
    "Visualization of employee categories.\n5. Analyze workforce trends."),
 10:("A recruitment agency wants to analyze job opportunities posted on a dynamic job portal. "
     "Develop a Python application using Selenium to scrape job listings, extract Job Title, "
     "Company Name, Location and Salary (if available), store the collected data in a Pandas "
     "DataFrame, save the dataset as a CSV file, and visualize job demand by location."),
}

tpl = Document(INDEX_TPL)
rows = [[c.text for c in r.cells] for r in tpl.tables[0].rows]
recs = []
for r in rows[1:]:
    sl = int(r[2].strip())
    prob = r[6].strip() or EXTRA.get(sl, "")
    title = r[5].strip()
    low = title.lower()
    if (not title) or low.startswith("requests") or low.startswith("beautifulsoup"):
        title = TITLES.get(sl, title)
    page = PREV.get(sl, "")
    if sl >= 18:
        page = PAGES.get(str(sl), str(START_PAGE))
    recs.append([r[0].strip(), r[1].strip(), str(sl), r[3].strip(),
                 r[4].strip(), title, prob, page])

IW = [Emu(478790), Emu(566420), Emu(356870), Emu(447040), Emu(692150),
      Emu(780000), Emu(2400000), Emu(444500)]
it = doc.add_table(rows=1 + len(recs), cols=8)
it.style = "Table Grid"; it.alignment = WD_TABLE_ALIGNMENT.CENTER
set_widths(it, IW); tight(it, 6, 6, 35, 35)

for ci, h in enumerate(["Week No","Date","Sl. No.","Type","Topic",
                        "Title with download Link for document","Problem Statement","Page No."]):
    c = it.rows[0].cells[ci]
    put(c, h, size=8.5, bold=True, color="FFFFFF",
        align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
    shade(c, C_IDXHEAD)

for ri, rec in enumerate(recs):
    row = it.rows[ri + 1]
    for ci, val in enumerate(rec):
        c = row.cells[ci]
        put(c, val, size=7.5, bold=(ci == 0),
            align=WD_ALIGN_PARAGRAPH.CENTER if ci in (0,1,2,3,7) else None,
            valign="center" if ci != 6 else "top")
        shade(c, C_IDXBAND if ri % 2 == 0 else None)

lp = doc.add_paragraph(); lp.paragraph_format.space_before = Pt(4)
r = lp.add_run("PP: Practice Program; EP: Exercise Program; CP: Challenging Program")
r.font.size = Pt(9); r.font.name = TNR

# ---- PROGRAMS ----
CW = [Emu(1076960), Emu(449580), Emu(990600), Emu(665480), Emu(2541905), Emu(35560)]

for prog in S:
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    sec.orientation = WD_ORIENT.PORTRAIT
    sec.page_width = Emu(7560310); sec.page_height = Emu(10692130)
    sec.left_margin = sec.right_margin = Emu(914400)
    sec.top_margin = Emu(914400); sec.bottom_margin = Emu(914400)
    page_border(sec)
    build_header(sec, prog)
    build_footer(sec, START_PAGE)

    nf = len(prog["functions"])
    ta = doc.add_table(rows=5 + nf, cols=6)
    ta.style = "Table Grid"
    set_widths(ta, CW); tight(ta, 15, 15, 60, 60)

    tr = ta.rows[0]
    for c in tr.cells:
        shade(c, C_TITLE)
    put(tr.cells[0], "Title", size=12, bold=True, color="FFFFFF",
        align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
    m = tr.cells[1].merge(tr.cells[5])
    put(m, prog["title"], size=11, bold=True, color="FFFFFF",
        align=WD_ALIGN_PARAGRAPH.CENTER, valign="top")

    def label_row(row, label, value):
        shade(row.cells[0], C_LABEL)
        put(row.cells[0], label, size=12, bold=True,
            align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
        mm = row.cells[1].merge(row.cells[5])
        shade(mm, C_BODY)
        put(mm, value, size=10.5, color="000000")

    label_row(ta.rows[1], "Problem Statement", prog["problem"])
    label_row(ta.rows[2], "Objectives", chr(10).join("\u2022 " + o for o in prog["objectives"]))
    label_row(ta.rows[3], "Dataset URL Link / File", prog["dataset"])

    # functions header row - single "Functions Details" label with vMerge over body rows
    hr = ta.rows[4]
    shade(hr.cells[0], C_LABEL)
    put(hr.cells[0], "Functions Details", size=12, bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
    vmerge(hr.cells[0], "restart")
    for ci, txt in enumerate(["Sl. No.", "Function", "Package"], start=1):
        shade(hr.cells[ci], C_FNHEAD)
        put(hr.cells[ci], txt, size=11, bold=True, color="FFFFFF", valign="center")
    dcell = hr.cells[4].merge(hr.cells[5])
    shade(dcell, C_FNHEAD)
    put(dcell, "Description of function", size=11, bold=True, color="FFFFFF", valign="center")

    for k, (fn, pkg, desc) in enumerate(prog["functions"]):
        row = ta.rows[5 + k]
        shade(row.cells[0], C_LABEL)
        put(row.cells[0], "", size=10)
        vmerge(row.cells[0], None)          # continue the vertical merge
        for ci in range(1, 6):
            shade(row.cells[ci], C_BODY)
        put(row.cells[1], str(k + 1), size=10.5, align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
        put(row.cells[2], fn, size=10, mono=True, color="000000")
        put(row.cells[3], pkg, size=10, color="000000")
        dd = row.cells[4].merge(row.cells[5])
        shade(dd, C_BODY)
        put(dd, desc, size=10, color="000000")

    # Steps + Program
    tb = doc.add_table(rows=2, cols=6)
    tb.style = "Table Grid"
    set_widths(tb, CW); tight(tb, 15, 15, 60, 60)
    shade(tb.rows[0].cells[0], C_LABEL)
    put(tb.rows[0].cells[0], "Steps/ Process/ Procedure/ Algorithm/ Flowchart/ Model",
        size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
    m = tb.rows[0].cells[1].merge(tb.rows[0].cells[5])
    shade(m, C_BODY)
    put(m, chr(10).join(prog["steps"]), size=10.5, color="000000")

    shade(tb.rows[1].cells[0], C_LABEL)
    put(tb.rows[1].cells[0], "Program", size=11, bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
    pc = tb.rows[1].cells[1].merge(tb.rows[1].cells[5])
    shade(pc, C_BODY)
    pc.text = ""
    src = open(os.path.join(PROG, SRC[prog["no"]])).read().rstrip(chr(10))
    first = True
    for line in src.split(chr(10)):
        p = pc.paragraphs[0] if first else pc.add_paragraph()
        first = False
        pf = p.paragraph_format
        pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 1.0
        r = p.add_run(line if line else " ")
        r.font.size = Pt(6.8); r.font.name = MONO
        rpr = r._r.get_or_add_rPr()
        rf = OxmlElement("w:rFonts")
        rf.set(qn("w:ascii"), MONO); rf.set(qn("w:hAnsi"), MONO)
        rpr.append(rf)

    # Snapshots + conclusions + references
    tc = doc.add_table(rows=4, cols=6)
    tc.style = "Table Grid"
    set_widths(tc, CW); tight(tc, 15, 15, 60, 60)

    for k, (fname, cap) in enumerate([("Program%d_part1.png" % prog["no"], prog["snap1"]),
                                      ("Program%d_part2.png" % prog["no"], prog["snap2"])]):
        row = tc.rows[k]
        shade(row.cells[0], C_LABEL)
        put(row.cells[0],
            "Output Snapshots With Explanation/ Observations" if k == 0 else "",
            size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
        m = row.cells[1].merge(row.cells[5])
        shade(m, C_BODY)
        m.text = ""
        p = m.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(os.path.join(ASSETS, fname), width=Inches(4.9))
        cp = m.add_paragraph(cap)
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.paragraph_format.space_before = Pt(2); cp.paragraph_format.space_after = Pt(2)
        for r in cp.runs:
            r.font.size = Pt(8.5); r.font.name = TNR; r.font.bold = True; r.font.italic = True
        explain = prog["explain1"] if k == 0 else prog["explain2"]
        ep = m.add_paragraph(explain)
        ep.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        ep.paragraph_format.space_before = Pt(1); ep.paragraph_format.space_after = Pt(3)
        for r in ep.runs:
            r.font.size = Pt(8.5); r.font.name = TNR

    shade(tc.rows[2].cells[0], C_LABEL)
    put(tc.rows[2].cells[0], "Conclusions", size=11, bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
    m = tc.rows[2].cells[1].merge(tc.rows[2].cells[5])
    shade(m, C_BODY)
    put(m, prog["concl"], size=10.5, color="000000")

    shade(tc.rows[3].cells[0], C_LABEL)
    put(tc.rows[3].cells[0], "References", size=11, bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER, valign="center")
    m = tc.rows[3].cells[1].merge(tc.rows[3].cells[5])
    shade(m, C_BODY)
    refs = list(prog["refs"])
    refs.append("%d. Python program (GitHub link): %s%s" % (len(refs) + 1, GH,
                SRC[prog["no"]].replace(" ", "%20")))
    put_linked(m, chr(10).join(refs), size=10.5)

prog_secs = doc.sections[2:]
if prog_secs:
    sp = prog_secs[0]._sectPr
    for old in sp.findall(qn("w:pgNumType")):
        sp.remove(old)
    pg = OxmlElement("w:pgNumType")
    pg.set(qn("w:fmt"), "decimal"); pg.set(qn("w:start"), str(START_PAGE))
    sp.append(pg)

# strip the inherited green page background
import zipfile as _zf, shutil as _sh, re as _re, os as _os
doc.save(OUT)
_tmp = OUT + ".tmp"
_zin = _zf.ZipFile(OUT, "r")
_zout = _zf.ZipFile(_tmp, "w", _zf.ZIP_DEFLATED)
for _it in _zin.infolist():
    _d = _zin.read(_it.filename)
    if _it.filename == "word/document.xml":
        _s = _d.decode("utf-8")
        _s = _re.sub(r'<w:background[^>]*/>', '', _s)
        _d = _s.encode("utf-8")
    elif _it.filename == "word/settings.xml":
        _s = _d.decode("utf-8")
        _s = _re.sub(r'<w:displayBackgroundShape[^>]*/>', '', _s)
        _d = _s.encode("utf-8")
    _zout.writestr(_it, _d)
_zin.close(); _zout.close(); _sh.move(_tmp, OUT)

print("saved:", OUT, os.path.getsize(OUT))
