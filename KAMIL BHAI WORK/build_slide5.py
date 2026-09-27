#!/usr/bin/env python3
"""Rebuild MRM slide 5 to Design System v4.  One master workbook drives every chart."""
import copy, io, os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree
import openpyxl

# ---------------------------------------------------------------- palette
NAVY   = RGBColor(0x17, 0x37, 0x5E)
DEEP   = RGBColor(0x0F, 0x24, 0x40)
TATA   = RGBColor(0x14, 0x79, 0xB8)
BLUTNT = RGBColor(0xE8, 0xF1, 0xF8)
BLUMID = RGBColor(0xC3, 0xDA, 0xEA)
GREEN  = RGBColor(0x2E, 0x9E, 0x5B)
AMBER  = RGBColor(0xE9, 0xA2, 0x1B)
RED    = RGBColor(0xD6, 0x45, 0x3D)
INK    = RGBColor(0x1C, 0x24, 0x30)
BODY   = RGBColor(0x4A, 0x5A, 0x6E)
MUTED  = RGBColor(0x8A, 0x98, 0xA8)
RULE   = RGBColor(0xE2, 0xE8, 0xEF)
WASH   = RGBColor(0xF5, 0xF8, 0xFB)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
AMBDK  = RGBColor(0xB8, 0x80, 0x0F)
FONT   = "Trebuchet MS"

# ---------------------------------------------------------------- grid
M      = 0.60
RIGHT  = 19.40
GUT    = 0.30

def I(v): return Inches(v)

# ---------------------------------------------------------------- master workbook
def build_master(path):
    wb = openpyxl.Workbook()
    ws = wb.active; ws.title = "Commercial"
    ws.append([None, "Baseline", "Revamp Plan", "Actual"])
    ws.append(["FTM (This Month)", 40.00, 31.06, 15.50])
    ws.append(["CUM (Inception to Date)", 114.00, 54.00, 37.80])
    ws["F1"] = "Variance vs Baseline"
    ws["F2"] = "=ROUND((D2-B2)/B2*100,0)"
    ws["F3"] = "=ROUND((D3-B3)/B3*100,0)"
    ws["G1"] = "Gap (Cr)"; ws["G2"] = "=B2-D2"; ws["G3"] = "=B3-D3"

    q = wb.create_sheet("Quality")
    q.append([None, "FTRI"]); q.append(["Achieved", 0.88]); q.append(["Gap", 0.12])

    s = wb.create_sheet("Safety")
    s.append([None, "Value", "Scale"])
    s.append(["Near Misses", 4, 10])
    s.append(["Inductions", 1691, 2000])
    s.append(["Open NCR", 1, 5])
    s.append(["LTI", 0, 5])
    s.append(["Safe Manhours ITD", 344498, None])
    s.append(["WIR C/O", "118 / 26", None])
    s.append(["MIR C/O", "63 / 1", None])
    wb.save(path)

# ---------------------------------------------------------------- xml helpers
def sub(el, tag, **attrs):
    e = etree.SubElement(el, qn(tag))
    for k, v in attrs.items(): e.set(k, str(v))
    return e

def strip_chart_chrome(chart, *, del_cat=True, del_val=True, gridlines=False):
    """Remove every PowerPoint default: gridlines, legend, axis lines, tick marks."""
    cx = chart._chartSpace
    for ax in cx.iter(qn('c:catAx'), qn('c:valAx')):
        is_cat = ax.tag == qn('c:catAx')
        for gl in ax.findall(qn('c:majorGridlines')) + ax.findall(qn('c:minorGridlines')):
            ax.remove(gl)
        d = ax.find(qn('c:delete'))
        if d is None:
            d = etree.Element(qn('c:delete'))
            scaling = ax.find(qn('c:scaling'))
            scaling.addnext(d)
        d.set('val', '1' if ((is_cat and del_cat) or ((not is_cat) and del_val)) else '0')
        for t in ('c:majorTickMark', 'c:minorTickMark'):
            e = ax.find(qn(t))
            if e is not None: e.set('val', 'none')
    for lg in cx.findall('.//' + qn('c:legend')):
        lg.getparent().remove(lg)
    pv = cx.find('.//' + qn('c:plotVisOnly'))
    if pv is not None: pv.set('val', '1')
    chart.has_title = False

def no_fill_chart(chart):
    cx = chart._chartSpace
    spPr = cx.find(qn('c:spPr'))
    if spPr is None:
        spPr = etree.SubElement(cx, qn('c:spPr'))
    for ch in list(spPr): spPr.remove(ch)
    sub(spPr, 'a:noFill'); ln = sub(spPr, 'a:ln'); sub(ln, 'a:noFill')
    pa = cx.find('.//' + qn('c:plotArea'))
    psp = pa.find(qn('c:spPr'))
    if psp is None:
        psp = etree.SubElement(pa, qn('c:spPr'))
    for ch in list(psp): psp.remove(ch)
    sub(psp, 'a:noFill'); ln2 = sub(psp, 'a:ln'); sub(ln2, 'a:noFill')

def lock_chart_text(chart, pt=18):
    cx = chart._chartSpace
    tx = cx.find(qn('c:txPr'))
    if tx is not None: cx.remove(tx)
    tx = etree.SubElement(cx, qn('c:txPr'))
    bd = sub(tx, 'a:bodyPr'); sub(tx, 'a:lstStyle')
    p = sub(tx, 'a:p'); pp = sub(p, 'a:pPr')
    d = sub(pp, 'a:defRPr', sz=str(int(pt * 100)), b='1')
    d.set('spc', '0')
    sub(p, 'a:endParaRPr', lang='en-US')


def nowrap_labels(dlbls):
    tx = dlbls._element.find(qn('c:txPr'))
    if tx is None: return
    bp = tx.find(qn('a:bodyPr'))
    if bp is not None:
        bp.set('wrap', 'none'); bp.set('rot', '0'); bp.set('spcFirstLastPara', '0')


def repoint(chart, sheet):
    """Repoint every c:f formula from python-pptx's Sheet1 to the master sheet."""
    for f in chart._chartSpace.iter(qn('c:f')):
        if f.text and '!' in f.text:
            f.text = sheet + '!' + f.text.split('!', 1)[1]

def share_workbook(chart_parts, blob):
    for cp in chart_parts:
        cp.chart_workbook.update_from_xlsx_blob(blob)

def label_font(chart, size, color, bold=True):
    chart.plots[0].has_data_labels = True
    dl = chart.plots[0].data_labels
    dl.font.size = Pt(size); dl.font.bold = bold; dl.font.name = FONT
    dl.font.color.rgb = color
    dl.number_format_is_linked = False
    return dl

# ---------------------------------------------------------------- primitives
def text(sh, s, size, color, *, bold=False, caps=False, space=0, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, line=None):
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    lines = s.split("\n")
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if line: p.line_spacing = line
        r = p.add_run(); r.text = ln.upper() if caps else ln
        r.font.size = Pt(size); r.font.bold = bold; r.font.name = FONT
        r.font.color.rgb = color
        if space:
            r.font._rPr.set('spc', str(int(space * 100)))
    return sh

def box(shapes, x, y, w, h, fill=None, line=None, lw=0.75):
    from pptx.enum.shapes import MSO_SHAPE
    s = shapes.add_shape(MSO_SHAPE.RECTANGLE, I(x), I(y), I(w), I(h))
    s.shadow.inherit = False
    if fill is None: s.fill.background()
    else: s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: s.line.fill.background()
    else: s.line.color.rgb = line; s.line.width = Pt(lw)
    s.text_frame.text = ""
    return s

def tbox(shapes, x, y, w, h):
    t = shapes.add_textbox(I(x), I(y), I(w), I(h))
    t.text_frame.word_wrap = True
    return t

# ---------------------------------------------------------------- build
def build(src, dst, xlsx):
    build_master(xlsx)
    blob = open(xlsx, 'rb').read()

    prs = Presentation(src)
    sl = prs.slides[4]
    KEEP = {99, 101, 103, 104}                 # logos + footer bar
    for sh in list(sl.shapes):
        if sh.shape_id not in KEEP:
            sh._element.getparent().remove(sh._element)

    sp = sl.shapes
    chart_parts = []

    # ---------- title block
    text(tbox(sp, M, 1.12, 12.0, 0.90), "Executive Dashboard", 60, NAVY, bold=True)
    text(tbox(sp, M, 2.02, 12.0, 0.34),
         "Adani Lucknow Airport City   ·   Monthly Review   ·   August 2026",
         18, MUTED, caps=True, space=1.1)
    box(sp, M, 2.46, RIGHT - M, 0.028, fill=NAVY)

    # ---------- KPI row
    kpis = [("Contract Value", "\u20b91,725 Cr", "39-MONTH CONTRACT", NAVY, DEEP),
            ("Duration",       "39 Months",      "COMMENCED FEB 2026", NAVY, DEEP),
            ("Completion",     "15 May 2029",    "CONTRACTUAL TARGET", NAVY, DEEP),
            ("Project Health", "WATCHLIST",      "COMMERCIAL SLIPPAGE", AMBER, AMBDK)]
    kw, ky, kh = 4.475, 2.62, 1.42
    for i, (hd, val, sub_, strip, vc) in enumerate(kpis):
        x = M + i * (kw + GUT)
        box(sp, x, ky, kw, kh, fill=WHITE, line=RULE)
        box(sp, x, ky, kw, 0.48, fill=strip)
        text(tbox(sp, x + 0.20, ky + 0.125, kw - 0.40, 0.26), hd, 24, WHITE,
             bold=True, caps=True, space=1.2)
        vsz = 38 if len(val) <= 11 else 32
        vb = tbox(sp, x + 0.20, ky + 0.62, kw - 0.40, 0.52)
        vb.text_frame.word_wrap = False
        text(vb, val, vsz, vc, bold=True)
        text(tbox(sp, x + 0.20, ky + 1.16, kw - 0.40, 0.22), sub_, 18, MUTED,
             caps=True, space=0.9)

    # ---------- section markers
    def marker(x, y, w, label, color, note=""):
        box(sp, x, y + 0.045, 0.19, 0.19, fill=color)
        t = tbox(sp, x + 0.34, y, w, 0.34)
        tf = t.text_frame; tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        r = p.add_run(); r.text = label.upper()
        r.font.size = Pt(27); r.font.bold = True; r.font.name = FONT; r.font.color.rgb = NAVY
        r.font._rPr.set('spc', '130')
        if note:
            r2 = p.add_run(); r2.text = "   " + note.upper()
            r2.font.size = Pt(21); r2.font.bold = False; r2.font.name = FONT
            r2.font.color.rgb = MUTED; r2.font._rPr.set('spc', '130')

    LX, LW = M, 11.30
    RX, RW = 12.20, 7.20
    marker(LX, 4.20, 9.0, "Commercial Progress", TATA, "\u20b9 Cr")
    marker(RX, 4.20, 6.0, "Safety & Quality", GREEN)

    # ---------- commercial bullet chart  (stacked bar: actual / revamp-gap / baseline-gap)
    cd = CategoryChartData()
    cd.categories = ["FTM (This Month)", "CUM (Inception to Date)"]
    cd.add_series("Actual",   (15.50, 37.80))
    cd.add_series("Revamp Plan", (31.06 - 15.50, 54.00 - 37.80))
    cd.add_series("Baseline", (40.00 - 31.06, 114.00 - 54.00))
    gf = sp.add_chart(XL_CHART_TYPE.BAR_STACKED, I(LX), I(4.62), I(LW), I(2.30), cd)
    ch = gf.chart
    chart_parts.append(gf.chart.part)
    strip_chart_chrome(ch, del_cat=False, del_val=True)
    no_fill_chart(ch)
    for s_, col in zip(ch.series, (TATA, BLUMID, BLUTNT)):
        s_.format.fill.solid(); s_.format.fill.fore_color.rgb = col
        s_.format.line.fill.background()
    ch.plots[0].gap_width = 58
    ch.plots[0].overlap = 100
    cat_ax = ch.category_axis
    cat_ax.tick_labels.font.size = Pt(18)
    cat_ax.tick_labels.font.name = FONT
    cat_ax.tick_labels.font.color.rgb = BODY
    cat_ax.format.line.color.rgb = RULE
    # data labels only on the Actual series, inside end
    p0 = ch.plots[0]
    ser0 = ch.series[0]
    ser0.data_labels.show_value = True
    ser0.data_labels.font.size = Pt(18)
    ser0.data_labels.font.bold = True
    ser0.data_labels.font.name = FONT
    ser0.data_labels.font.color.rgb = WHITE
    ser0.data_labels.position = XL_LABEL_POSITION.INSIDE_END
    ser0.data_labels.number_format = '0.0'
    ser0.data_labels.number_format_is_linked = False
    nowrap_labels(ser0.data_labels)
    va0 = ch.value_axis
    va0.minimum_scale = 0; va0.maximum_scale = 120
    sc = cat_ax._element.find(qn('c:scaling'))
    o = sc.find(qn('c:orientation'))
    if o is None:
        o = etree.SubElement(sc, qn('c:orientation'))
    o.set('val', 'maxMin')
    lock_chart_text(ch, 18)
    repoint(ch, "Commercial")

    # baseline target ticks + legend (drawn, so they never drift)
    lg = 7.00
    for i, (lab, col) in enumerate((("Actual", TATA), ("Revamp Plan", BLUMID), ("Baseline", BLUTNT))):
        lx = LX + i * 2.05
        box(sp, lx, lg + 0.06, 0.22, 0.13, fill=col, line=RULE, lw=0.5)
        text(tbox(sp, lx + 0.32, lg, 1.7, 0.24), lab, 18, MUTED, caps=True, space=0.8)

    # ---------- variance tiles
    tiles = [("FTM vs Baseline", "\u221261%", "\u20b924.50 Cr short", RED, RED),
             ("CUM vs Baseline", "\u221267%", "\u20b976.20 Cr short", RED, RED),
             ("Gap to Close",    "\u20b976.2 Cr", "33 months remaining", AMBER, DEEP)]
    tw, ty, th = 3.5667, 7.36, 1.32
    for i, (hd, val, sub_, rail, vc) in enumerate(tiles):
        x = LX + i * (tw + GUT)
        box(sp, x, ty, tw, th, fill=WHITE, line=RULE)
        box(sp, x, ty, 0.085, th, fill=rail)
        text(tbox(sp, x + 0.26, ty + 0.18, tw - 0.45, 0.24), hd, 18, MUTED, caps=True, space=0.9)
        vb2 = tbox(sp, x + 0.26, ty + 0.50, tw - 0.52, 0.46)
        vb2.text_frame.word_wrap = False
        text(vb2, val, 36, vc, bold=True)
        text(tbox(sp, x + 0.26, ty + 1.02, tw - 0.45, 0.22), sub_, 18, MUTED)

    # ---------- FTRI ring gauge
    gd = CategoryChartData()
    gd.categories = ["Achieved", "Gap"]
    gd.add_series("FTRI", (0.88, 0.12))
    rg = sp.add_chart(XL_CHART_TYPE.DOUGHNUT, I(RX - 0.02), I(4.54), I(2.20), I(2.20), gd)
    rc = rg.chart
    chart_parts.append(rg.chart.part)
    rc.has_legend = False
    rc.has_title = False
    no_fill_chart(rc)
    rc.plots[0].has_data_labels = False
    pts = rc.plots[0].series[0].points
    for pt, col in zip(pts, (GREEN, RULE)):
        pt.format.fill.solid(); pt.format.fill.fore_color.rgb = col
        pt.format.line.fill.background()
    dp = rc._chartSpace.find('.//' + qn('c:doughnutChart'))
    for t in ('c:firstSliceAng', 'c:holeSize'):
        e = dp.find(qn(t))
        if e is not None: dp.remove(e)
    fr = etree.SubElement(dp, qn('c:firstSliceAng')); fr.set('val', '0')
    hs = etree.SubElement(dp, qn('c:holeSize')); hs.set('val', '78')
    repoint(rc, "Quality")
    # centred value (sits over the ring hole)
    text(tbox(sp, RX - 0.02, 5.40, 2.20, 0.46), "88%", 38, DEEP, bold=True, align=PP_ALIGN.CENTER)
    text(tbox(sp, RX - 0.02, 6.78, 2.20, 0.24), "FTRI Score", 18, MUTED, caps=True,
         space=1.0, align=PP_ALIGN.CENTER)

    # ---------- headline safety stats
    SX = RX + 2.50
    SW = RW - 2.50
    b1 = tbox(sp, SX, 4.58, SW, 0.56); b1.text_frame.word_wrap = False
    text(b1, "3,44,498", 40, DEEP, bold=True)
    text(tbox(sp, SX, 5.16, SW, 0.24), "Safe Manhours \u00b7 ITD", 18, MUTED, caps=True, space=0.9)
    box(sp, SX, 5.52, SW, 0.01, fill=RULE)
    b2 = tbox(sp, SX, 5.66, SW, 0.56); b2.text_frame.word_wrap = False
    text(b2, "0", 40, GREEN, bold=True)
    text(tbox(sp, SX, 6.24, SW, 0.24), "Lost Time Injuries", 18, MUTED, caps=True, space=0.9)
    text(tbox(sp, SX, 6.58, SW, 0.24), "WIR 118 / 26      MIR 63 / 1", 18, BODY)

    # ---------- progress rails (real linked charts)
    rails = [("Near Misses", 4, 11, AMBER, "0"),
             ("Inductions", 1691, 2400, GREEN, "#,##0"),
             ("Open NCR", 1, 5, GREEN, "0")]
    ry = 7.16
    for i, (lab, val, scale, col, fmt) in enumerate(rails):
        y = ry + i * 0.56
        text(tbox(sp, RX, y, 3.0, 0.22), lab, 18, NAVY, bold=True, caps=True, space=0.8)
        box(sp, RX, y + 0.28, RW, 0.19, fill=RULE)          # rail track
        d = CategoryChartData(); d.categories = [lab]; d.add_series(lab, (val,))
        gfx = sp.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, I(RX), I(y + 0.24), I(RW), I(0.38), d)
        c2 = gfx.chart
        chart_parts.append(gfx.chart.part)
        strip_chart_chrome(c2, del_cat=True, del_val=True)
        no_fill_chart(c2)
        c2.has_legend = False
        va = c2.value_axis
        va.minimum_scale = 0; va.maximum_scale = scale
        s2 = c2.series[0]
        s2.format.fill.solid(); s2.format.fill.fore_color.rgb = col
        s2.format.line.fill.background()
        c2.plots[0].gap_width = 12
        s2.data_labels.show_value = True
        s2.data_labels.font.size = Pt(18)
        s2.data_labels.font.bold = True
        s2.data_labels.font.name = FONT
        s2.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
        s2.data_labels.font.color.rgb = col
        s2.data_labels.number_format = fmt
        s2.data_labels.number_format_is_linked = False
        nowrap_labels(s2.data_labels)
        lock_chart_text(c2, 18)
        repoint(c2, "Safety")

    # ---------- bottom narrative cards
    cards = [("Critical Issues", RED,
              "Alternate batching-plant operation delay\n"
              "Work-front handover incomplete\n"
              "RT-1 handover 24 Aug vs BL 16 Jun 26"),
             ("Key Decision", GREEN,
              "Alternate concrete supplier approved\nfor 5,000 m\u00b3 on 31 August 2026."),
             ("Support Requested", TATA,
              "Adhoc payment vs RA bills within 15 days\n"
              "100% payment for concrete supply\n"
              "Supply RA bills within 21 days")]
    cw, cy, chh = 6.0667, 8.92, 1.73
    for i, (hd, rail, bodytxt) in enumerate(cards):
        x = M + i * (cw + GUT)
        box(sp, x, cy, cw, chh, fill=WHITE, line=RULE)
        box(sp, x, cy, 0.10, chh, fill=rail)
        text(tbox(sp, x + 0.28, cy + 0.18, cw - 0.52, 0.28), hd, 24, NAVY,
             bold=True, caps=True, space=1.1)
        text(tbox(sp, x + 0.28, cy + 0.60, cw - 0.52, 1.00), bodytxt, 18, BODY, line=1.22)

    # ---------- one shared master workbook for every chart
    share_workbook(chart_parts, blob)

    # ---------- deck-wide unique shape ids (also clears the inherited slide-18 dupes)
    nxt = [5000]
    for s_ in prs.slides:
        seen = set()
        for c in s_.shapes._spTree.iter(qn('p:cNvPr')):
            i = c.get('id')
            if i in seen or i == '0':
                nxt[0] += 1; c.set('id', str(nxt[0]))
            else:
                seen.add(i)

    prs.save(dst)
    print("saved", dst)

if __name__ == "__main__":
    build("original.pptx", "MRM_Slide5_V4.pptx", "MRM_Master_Data.xlsx")
