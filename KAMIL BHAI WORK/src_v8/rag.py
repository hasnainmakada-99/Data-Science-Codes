"""RAG rule set for the MRM deck.

Every rule is explicit, published on the `RAG_Rules` sheet of the embedded
workbook and rendered on the slide in the matching colour.

Families
--------
progress      % of a target achieved            G >= 90   A 70-89.9   R < 70
approval      % approved of what was submitted  G >= 90   A 75-89.9   R < 75
quality_ftri  First Time Right index            G >= 95   A 85-94.9   R < 85
tat_days      turnaround, lower is better       G <= 14   A 14.1-21   R > 21
backlog       open count, lower is better       G <= 50   A 51-200    R > 200
clash         open clash count                  G <= 5k   A 5-20k     R > 20k
hotspot       clashes on one interface          G < 2000  A 2-5k      R > 5000
zero_harm     lagging safety count              G = 0     A 1-4       R >= 5
schedule      milestone state                   G issued/done   A scheduled/in progress   R overdue/not started
plan          a forward-looking planned figure  always A (committed, not yet earned)
"""
from pptx.dml.color import RGBColor

GREEN=RGBColor(0x2E,0x9E,0x5B); AMBER=RGBColor(0xE9,0xA2,0x1B); RED=RGBColor(0xD6,0x45,0x3D)
GRNDK=RGBColor(0x1E,0x6E,0x3E); AMBDK=RGBColor(0xB8,0x80,0x0F); REDDK=RGBColor(0x96,0x30,0x2A)
GRNT=RGBColor(0xE6,0xF4,0xEB); AMBT=RGBColor(0xFC,0xF2,0xDD); REDT=RGBColor(0xFB,0xEA,0xE9)

FILL={'g':GREEN,'a':AMBER,'r':RED}
DARK={'g':GRNDK,'a':AMBDK,'r':REDDK}
TINT={'g':GRNT,'a':AMBT,'r':REDT}

# ── rule engine ───────────────────────────────────────────────────────────
RULES={
 'progress':     (lambda v: 'g' if v>=90 else 'a' if v>=70 else 'r',  '>= 90%', '70 - 89.9%', '< 70%'),
 'approval':     (lambda v: 'g' if v>=90 else 'a' if v>=75 else 'r',  '>= 90%', '75 - 89.9%', '< 75%'),
 'quality_ftri': (lambda v: 'g' if v>=95 else 'a' if v>=85 else 'r',  '>= 95%', '85 - 94.9%', '< 85%'),
 'tat_days':     (lambda v: 'g' if v<=14 else 'a' if v<=21 else 'r',  '<= 14 d', '14 - 21 d', '> 21 d'),
 'backlog':      (lambda v: 'g' if v<=50 else 'a' if v<=200 else 'r', '<= 50', '51 - 200', '> 200'),
 'clash':        (lambda v: 'g' if v<=5000 else 'a' if v<=20000 else 'r','<= 5,000','5,001 - 20,000','> 20,000'),
 'hotspot':      (lambda v: 'g' if v<2000 else 'a' if v<=5000 else 'r','< 2,000','2,000 - 5,000','> 5,000'),
 'zero_harm':    (lambda v: 'g' if v==0 else 'a' if v<5 else 'r',     '0', '1 - 4', '>= 5'),
 'variance':     (lambda v: 'g' if v>=-5 else 'a' if v>=-20 else 'r', '>= -5%', '-5 to -20%', '< -20%'),
}

def rag(kind, value):
    return RULES[kind][0](value)

def pct(actual, target):
    return 0.0 if not target else actual/target*100.0

# ── the published rule table (written to the workbook) ────────────────────
ROWS=[]
def reg(indicator, kind, value, shown=None, status=None):
    """Record an indicator on the RAG_Rules sheet and return its status letter."""
    st = status or rag(kind, value)
    g,a,r = (RULES[kind][1],RULES[kind][2],RULES[kind][3]) if kind in RULES else ('','','')
    ROWS.append((indicator, kind, g, a, r, shown if shown is not None else value, st.upper()))
    return st

def note(indicator, basis, shown, status):
    """Record a judgement-based indicator (schedule state, plan figure, fact)."""
    ROWS.append((indicator, basis, 'issued / complete', 'scheduled / in progress',
                 'overdue / not started', shown, status.upper()))
    return status
