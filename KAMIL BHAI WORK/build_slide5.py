#!/usr/bin/env python3
"""MRM slide 5 — Design System v5.  Top-centred title, generous spacing, no collisions."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree
import openpyxl

NAVY = RGBColor(0x17,0x37,0x5E); DEEP = RGBColor(0x0F,0x24,0x40)
TATA = RGBColor(0x14,0x79,0xB8); BLUTNT = RGBColor(0xE8,0xF1,0xF8); BLUMID = RGBColor(0xB9,0xD5,0xE9)
GREEN= RGBColor(0x2E,0x9E,0x5B); AMBER = RGBColor(0xE9,0xA2,0x1B); RED = RGBColor(0xD6,0x45,0x3D)
BODY = RGBColor(0x4A,0x5A,0x6E); MUTED = RGBColor(0x8A,0x98,0xA8)
RULE = RGBColor(0xE2,0xE8,0xEF); WHITE = RGBColor(0xFF,0xFF,0xFF); AMBDK = RGBColor(0xB8,0x80,0x0F)
FONT = "Trebuchet MS"

M, RIGHT, GUT = 0.60, 19.40, 0.30
def I(v): return Inches(v)

# ------------------------------------------------------------------ workbook
def build_master(path):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Commercial"
    ws.append([None,"Baseline","Revamp Plan","Actual"])
    ws.append(["FTM",40.00,31.06,15.50]); ws.append(["CUM",114.00,54.00,37.80])
    ws["F1"]="Var vs BL %"; ws["F2"]="=ROUND((D2-B2)/B2*100,0)"; ws["F3"]="=ROUND((D3-B3)/B3*100,0)"
    ws["G1"]="Gap Cr"; ws["G2"]="=B2-D2"; ws["G3"]="=B3-D3"
    q = wb.create_sheet("Quality"); q.append([None,"FTRI"]); q.append(["Achieved",0.88]); q.append(["Gap",0.12])
    s = wb.create_sheet("Safety"); s.append([None,"Value","Scale"])
    for r in (["Near Misses",4,11],["Inductions",1691,2400],["Open NCR",1,5],
              ["LTI",0,5],["Safe Manhours ITD",344498,None]): s.append(r)
    wb.save(path)

# ------------------------------------------------------------------ xml utils
def sub(el, tag, **a):
    e = etree.SubElement(el, qn(tag))
    for k,v in a.items(): e.set(k,str(v))
    return e

def strip_chrome(chart, del_cat=True, del_val=True):
    cx = chart._chartSpace
    for ax in cx.iter(qn('c:catAx'), qn('c:valAx')):
        is_cat = ax.tag == qn('c:catAx')
        for g in ax.findall(qn('c:majorGridlines'))+ax.findall(qn('c:minorGridlines')): ax.remove(g)
        d = ax.find(qn('c:delete'))
        if d is None:
            d = etree.Element(qn('c:delete')); ax.find(qn('c:scaling')).addnext(d)
        d.set('val','1' if ((is_cat and del_cat) or ((not is_cat) and del_val)) else '0')
        for t in ('c:majorTickMark','c:minorTickMark'):
            e = ax.find(qn(t))
            if e is not None: e.set('val','none')
    for lg in cx.findall('.//'+qn('c:legend')): lg.getparent().remove(lg)
    chart.has_title = False

def transparent(chart):
    cx = chart._chartSpace
    for host in (cx, cx.find('.//'+qn('c:plotArea'))):
        sp = host.find(qn('c:spPr'))
        if sp is None: sp = etree.SubElement(host, qn('c:spPr'))
        for c in list(sp): sp.remove(c)
        sub(sp,'a:noFill'); sub(sub(sp,'a:ln'),'a:noFill')

def plot_full(chart, x=0.0, y=0.0, w=1.0, h=1.0):
    """Pin the inner plot area so bars line up with the drawn track."""
    pa = chart._chartSpace.find('.//'+qn('c:plotArea'))
    old = pa.find(qn('c:layout'))
    if old is not None: pa.remove(old)
    lay = etree.Element(qn('c:layout')); pa.insert(0, lay)
    ml = sub(lay,'c:manualLayout')
    sub(ml,'c:layoutTarget',val='inner')
    sub(ml,'c:xMode',val='edge'); sub(ml,'c:yMode',val='edge')
    sub(ml,'c:x',val=x); sub(ml,'c:y',val=y); sub(ml,'c:w',val=w); sub(ml,'c:h',val=h)

def lock_text(chart, pt=18):
    cx = chart._chartSpace
    t = cx.find(qn('c:txPr'))
    if t is not None: cx.remove(t)
    t = etree.SubElement(cx, qn('c:txPr'))
    sub(t,'a:bodyPr'); sub(t,'a:lstStyle')
    p = sub(t,'a:p'); sub(sub(p,'a:pPr'),'a:defRPr', sz=int(pt*100), b=1)
    sub(p,'a:endParaRPr', lang='en-US')

def nowrap(dl):
    tx = dl._element.find(qn('c:txPr'))
    if tx is None: return
    bp = tx.find(qn('a:bodyPr'))
    if bp is not None:
        bp.set('wrap','none'); bp.set('spcFirstLastPara','0')

def repoint(chart, sheet):
    for f in chart._chartSpace.iter(qn('c:f')):
        if f.text and '!' in f.text: f.text = sheet+'!'+f.text.split('!',1)[1]

# ------------------------------------------------------------------ drawing
def text(sh, s, size, color, *, bold=False, caps=False, space=0,
         align=PP_ALIGN.LEFT, line=None, wrap=True):
    tf = sh.text_frame; tf.word_wrap = wrap
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    for i, ln in enumerate(s.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if line: p.line_spacing = line
        r = p.add_run(); r.text = ln.upper() if caps else ln
        r.font.size = Pt(size); r.font.bold = bold; r.font.name = FONT; r.font.color.rgb = color
        if space: r.font._rPr.set('spc', str(int(space*100)))
    return sh

def box(shapes,x,y,w,h,fill=None,line=None,lw=0.75):
    s = shapes.add_shape(MSO_SHAPE.RECTANGLE, I(x),I(y),I(w),I(h))
    s.shadow.inherit = False
    if fill is None: s.fill.background()
    else: s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: s.line.fill.background()
    else: s.line.color.rgb = line; s.line.width = Pt(lw)
    s.text_frame.text = ""
    return s

def tbox(shapes,x,y,w,h):
    t = shapes.add_textbox(I(x),I(y),I(w),I(h)); t.text_frame.word_wrap = True; return t

# ------------------------------------------------------------------ build
def build(src,dst,xlsx):
    build_master(xlsx); blob = open(xlsx,'rb').read()
    prs = Presentation(src); sl = prs.slides[4]
    for sh in list(sl.shapes):
        if sh.shape_id not in {99,101,103,104}:
            sh._element.getparent().remove(sh._element)
    sp = sl.shapes; parts = []

    # ---------------- title : TOP CENTRE, clear of both logo zones
    text(tbox(sp, 4.00, 0.18, 12.00, 0.80), "Executive Dashboard", 44, NAVY,
         bold=True, align=PP_ALIGN.CENTER, wrap=False)
    text(tbox(sp, 4.00, 1.00, 12.00, 0.30),
         "Adani Lucknow Airport City   ·   Monthly Review   ·   August 2026",
         18, MUTED, caps=True, space=1.2, align=PP_ALIGN.CENTER, wrap=False)
    box(sp, M, 1.46, RIGHT-M, 0.026, fill=NAVY)

    # ---------------- KPI strip
    kpis = [("Contract Value","₹1,725 Cr","39-MONTH CONTRACT",NAVY,DEEP),
            ("Duration","39 Months","COMMENCED FEB 2026",NAVY,DEEP),
            ("Completion","15 May 2029","CONTRACTUAL TARGET",NAVY,DEEP),
            ("Project Health","WATCHLIST","COMMERCIAL SLIPPAGE",AMBER,AMBDK)]
    kw, ky, kh = 4.475, 1.64, 1.46
    for i,(hd,val,sb,strip,vc) in enumerate(kpis):
        x = M + i*(kw+GUT)
        box(sp,x,ky,kw,kh,fill=WHITE,line=RULE); box(sp,x,ky,kw,0.46,fill=strip)
        text(tbox(sp,x+0.22,ky+0.115,kw-0.44,0.26),hd,24,WHITE,bold=True,caps=True,space=1.2)
        text(tbox(sp,x+0.22,ky+0.60,kw-0.44,0.50),val,38,vc,bold=True,wrap=False)
        text(tbox(sp,x+0.22,ky+1.12,kw-0.44,0.26),sb,18,MUTED,caps=True,space=0.9)

    # ---------------- section markers
    def marker(x,y,label,color,note=""):
        box(sp,x,y+0.05,0.19,0.19,fill=color)
        t = tbox(sp,x+0.36,y,min(8.0, RIGHT-(x+0.36)),0.32); tf = t.text_frame
        tf.margin_left=tf.margin_top=tf.margin_bottom=0; tf.word_wrap=False
        p = tf.paragraphs[0]
        r = p.add_run(); r.text = label.upper()
        r.font.size=Pt(27); r.font.bold=True; r.font.name=FONT; r.font.color.rgb=NAVY
        r.font._rPr.set('spc','130')
        if note:
            r2 = p.add_run(); r2.text = "    "+note
            r2.font.size=Pt(19); r2.font.bold=False; r2.font.name=FONT; r2.font.color.rgb=MUTED

    LX, LW = M, 11.30
    RX, RW = 12.20, 7.20
    marker(LX, 3.34, "Commercial Progress", TATA, "₹ Cr")
    marker(RX, 3.34, "Safety & Quality", GREEN)

    # ---------------- bullet chart
    cd = CategoryChartData(); cd.categories = ["FTM","CUM"]
    cd.add_series("Actual",(15.50,37.80))
    cd.add_series("Revamp Plan",(31.06-15.50,54.00-37.80))
    cd.add_series("Baseline",(40.00-31.06,114.00-54.00))
    gf = sp.add_chart(XL_CHART_TYPE.BAR_STACKED, I(LX), I(3.82), I(LW), I(2.30), cd)
    ch = gf.chart; parts.append(gf.chart.part)
    strip_chrome(ch, del_cat=False, del_val=True); transparent(ch)
    plot_full(ch, 0.075, 0.03, 0.915, 0.94)
    for s_,c_ in zip(ch.series,(TATA,BLUMID,BLUTNT)):
        s_.format.fill.solid(); s_.format.fill.fore_color.rgb = c_; s_.format.line.fill.background()
    ch.plots[0].gap_width = 78; ch.plots[0].overlap = 100
    ca = ch.category_axis
    ca.tick_labels.font.size = Pt(21); ca.tick_labels.font.bold = True
    ca.tick_labels.font.name = FONT; ca.tick_labels.font.color.rgb = NAVY
    ca.format.line.color.rgb = RULE
    sc = ca._element.find(qn('c:scaling'))
    o = sc.find(qn('c:orientation')) or etree.SubElement(sc, qn('c:orientation'))
    o.set('val','maxMin')
    va = ch.value_axis; va.minimum_scale = 0; va.maximum_scale = 120
    s0 = ch.series[0]
    s0.data_labels.show_value = True
    s0.data_labels.font.size = Pt(20); s0.data_labels.font.bold = True
    s0.data_labels.font.name = FONT; s0.data_labels.font.color.rgb = WHITE
    s0.data_labels.position = XL_LABEL_POSITION.INSIDE_END
    s0.data_labels.number_format = '0.0'; s0.data_labels.number_format_is_linked = False
    nowrap(s0.data_labels)
    lock_text(ch, 20); repoint(ch, "Commercial")

    # legend — one tidy line
    ly = 6.24
    for i,(lab,c_) in enumerate((("Actual",TATA),("Revamp Plan",BLUMID),("Baseline",BLUTNT))):
        lx = LX + i*2.45
        box(sp,lx,ly+0.05,0.24,0.14,fill=c_,line=RULE,lw=0.5)
        text(tbox(sp,lx+0.34,ly,2.0,0.24),lab,18,MUTED,caps=True,space=0.8)

    # ---------------- variance tiles
    tiles = [("FTM vs Baseline","−61%","₹24.50 Cr short",RED,RED),
             ("CUM vs Baseline","−67%","₹76.20 Cr short",RED,RED),
             ("Gap to Close","₹76.2 Cr","33 months remaining",AMBER,DEEP)]
    tw, ty, th = 3.5667, 6.78, 1.36
    for i,(hd,val,sb,rail,vc) in enumerate(tiles):
        x = LX + i*(tw+GUT)
        box(sp,x,ty,tw,th,fill=WHITE,line=RULE); box(sp,x,ty,0.09,th,fill=rail)
        text(tbox(sp,x+0.28,ty+0.18,tw-0.50,0.24),hd,18,MUTED,caps=True,space=0.9)
        text(tbox(sp,x+0.28,ty+0.52,tw-0.50,0.46),val,36,vc,bold=True,wrap=False)
        text(tbox(sp,x+0.28,ty+1.06,tw-0.50,0.22),sb,18,MUTED)

    # ---------------- FTRI ring
    gd = CategoryChartData(); gd.categories = ["Achieved","Gap"]; gd.add_series("FTRI",(0.88,0.12))
    rg = sp.add_chart(XL_CHART_TYPE.DOUGHNUT, I(RX-0.06), I(3.70), I(2.32), I(2.32), gd)
    rc = rg.chart; parts.append(rg.chart.part)
    rc.has_legend = False; rc.has_title = False; transparent(rc)
    rc.plots[0].has_data_labels = False
    plot_full(rc, 0.02, 0.02, 0.96, 0.96)
    for pt_,c_ in zip(rc.plots[0].series[0].points,(GREEN,RULE)):
        pt_.format.fill.solid(); pt_.format.fill.fore_color.rgb = c_; pt_.format.line.fill.background()
    dp = rc._chartSpace.find('.//'+qn('c:doughnutChart'))
    for t in ('c:firstSliceAng','c:holeSize'):
        e = dp.find(qn(t))
        if e is not None: dp.remove(e)
    sub(dp,'c:firstSliceAng',val=0); sub(dp,'c:holeSize',val=76)
    repoint(rc,"Quality")
    text(tbox(sp,RX-0.06,4.60,2.32,0.50),"88%",38,DEEP,bold=True,align=PP_ALIGN.CENTER)
    text(tbox(sp,RX-0.06,6.06,2.32,0.24),"FTRI Score",18,MUTED,caps=True,space=1.0,align=PP_ALIGN.CENTER)

    # ---------------- headline safety stats
    SX, SW = RX+2.50, RW-2.50
    text(tbox(sp,SX,3.74,SW,0.56),"3,44,498",40,DEEP,bold=True,wrap=False)
    text(tbox(sp,SX,4.32,SW,0.24),"Safe Manhours · ITD",18,MUTED,caps=True,space=0.9)
    box(sp,SX,4.70,SW,0.01,fill=RULE)
    text(tbox(sp,SX,4.86,SW,0.56),"0",40,GREEN,bold=True,wrap=False)
    text(tbox(sp,SX,5.44,SW,0.24),"Lost Time Injuries",18,MUTED,caps=True,space=0.9)
    text(tbox(sp,SX,5.82,SW,0.26),"WIR 118 / 26        MIR 63 / 1",18,BODY)

    # ---------------- progress rails  (label → gap → track, never touching)
    rails = [("Near Misses",4,11,AMBER,"0"),("Inductions",1691,2400,GREEN,"#,##0"),
             ("Open NCR",1,5,GREEN,"0")]
    ry, ROW = 6.48, 0.78
    for i,(lab,val,scale,col,fmt) in enumerate(rails):
        y = ry + i*ROW
        text(tbox(sp,RX,y,3.2,0.26),lab,18,NAVY,bold=True,caps=True,space=0.8)
        box(sp,RX,y+0.44,RW,0.20,fill=RULE)                     # track
        d = CategoryChartData(); d.categories=[lab]; d.add_series(lab,(val,))
        g2 = sp.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, I(RX), I(y+0.32), I(RW), I(0.44), d)
        c2 = g2.chart; parts.append(g2.chart.part)
        strip_chrome(c2); transparent(c2); c2.has_legend = False
        plot_full(c2, 0.0, 0.0, 1.0, 1.0)
        v2 = c2.value_axis; v2.minimum_scale = 0; v2.maximum_scale = scale
        s2 = c2.series[0]
        s2.format.fill.solid(); s2.format.fill.fore_color.rgb = col; s2.format.line.fill.background()
        c2.plots[0].gap_width = 120                              # bar ≈ track height
        s2.data_labels.show_value = True
        s2.data_labels.font.size = Pt(18); s2.data_labels.font.bold = True
        s2.data_labels.font.name = FONT; s2.data_labels.font.color.rgb = col
        s2.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
        s2.data_labels.number_format = fmt; s2.data_labels.number_format_is_linked = False
        nowrap(s2.data_labels); lock_text(c2, 18); repoint(c2,"Safety")

    # ---------------- narrative cards
    cards = [("Critical Issues",RED,
              "Alternate batching-plant operation delay\nWork-front handover incomplete\nRT-1 handover 24 Aug vs BL 16 Jun 26"),
             ("Key Decision",GREEN,
              "Alternate concrete supplier approved\nfor 5,000 m³ on 31 August 2026."),
             ("Support Requested",TATA,
              "Adhoc payment vs RA bills within 15 days\n100% payment for concrete supply\nSupply RA bills within 21 days")]
    cw, cy, chh = 6.0667, 8.84, 1.72
    for i,(hd,rail,bt) in enumerate(cards):
        x = M + i*(cw+GUT)
        box(sp,x,cy,cw,chh,fill=WHITE,line=RULE); box(sp,x,cy,0.10,chh,fill=rail)
        text(tbox(sp,x+0.30,cy+0.18,cw-0.56,0.28),hd,24,NAVY,bold=True,caps=True,space=1.1)
        text(tbox(sp,x+0.30,cy+0.60,cw-0.56,1.00),bt,18,BODY,line=1.26)

    for cp in parts: cp.chart_workbook.update_from_xlsx_blob(blob)

    nxt = [5000]
    for s_ in prs.slides:
        seen = set()
        for c in s_.shapes._spTree.iter(qn('p:cNvPr')):
            i = c.get('id')
            if i in seen or i == '0':
                nxt[0] += 1; c.set('id', str(nxt[0]))
            else: seen.add(i)
    prs.save(dst); print("saved", dst)

if __name__ == "__main__":
    build("original.pptx","MRM_Slide5_V5.pptx","MRM_Master_Data.xlsx")
