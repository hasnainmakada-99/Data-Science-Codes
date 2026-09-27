#!/usr/bin/env python3
"""Per-slide construction for the MRM Aug-26 deck — V8, RAG-coded throughout."""
from deck import *
from pptx.enum.chart import XL_LABEL_POSITION as LP
import rag as R
from rag import FILL, DARK, TINT

GREY=RGBColor(0xCF,0xD8,0xE2)      # neutral reference series (baseline / scale)

def K(hd, val, cap, st):
    """A RAG-coded KPI card tuple."""
    return (hd, val, cap, FILL[st], DARK[st])

# ═══════════════════════════════════════════════════ 5 · Executive Dashboard
def s05(sp):
    title_block(sp,"Executive Dashboard","Adani Lucknow Airport City   ·   Monthly Review   ·   August 2026")
    st_cv=R.note("Contract value","commercial fact","₹1,725 Cr","g")
    st_du=R.note("Contract duration","commercial fact","39 months","g")
    st_co=R.note("Completion date","schedule exposure from commercial slippage","15 May 2029","a")
    st_ph=R.note("Project health","composite of commercial, design and construction","Watchlist","a")
    kpi_row(sp,1.62,[K("Contract Value","₹1,725 Cr","39-month contract",st_cv),
                     K("Duration","39 Months","commenced Feb 2026",st_du),
                     K("Completion","15 May 2029","contractual target",st_co),
                     K("Project Health","WATCHLIST","commercial slippage",st_ph)])
    LX,LW=M,11.30; RX,RW=12.20,7.20
    st_ftm=R.reg("Commercial FTM vs baseline","variance",-61,"-61%")
    st_cum=R.reg("Commercial CUM vs baseline","variance",-67,"-67%")
    st_gap=R.note("Gap to close","₹76.2 Cr over 33 months","₹76.2 Cr","r")
    marker(sp,LX,3.24,"Commercial Progress",FILL[st_cum],"₹ Cr")
    marker(sp,RX,3.24,"Safety & Quality",GREEN)
    bar_chart(sp,LX,3.70,LW,2.24,["FTM","CUM"],
              [("Actual",(15.50,37.80)),("Revamp Plan",(31.06-15.50,54.00-37.80)),
               ("Baseline",(40.00-31.06,114.00-54.00))],
              (RED,AMBER,GREY),"S05_Commercial",maxv=120,fmt='0.0',stacked=True,
              cat_size=19,lbl_size=18,gap=78,label_pos=LP.INSIDE_END,plot=(0.075,0.03,0.915,0.94))
    ly=6.08
    for i,(lab,c) in enumerate((("Actual",RED),("Revamp Plan",AMBER),("Baseline",GREY))):
        lx=LX+i*2.35
        box(sp,lx,ly+0.05,0.22,0.13,fill=c,line=RULE,lw=0.5)
        text(tbox(sp,lx+0.32,ly,2.0,0.24),lab,T_CAP,MUTED,caps=True,space=0.8)
    tiles=[("FTM vs Baseline","−61%","₹24.50 Cr short",st_ftm),
           ("CUM vs Baseline","−67%","₹76.20 Cr short",st_cum),
           ("Gap to Close","₹76.2 Cr","33 months remaining",st_gap)]
    tw,ty,th=3.5667,6.60,1.30
    for i,(hd,val,sb,st) in enumerate(tiles):
        x=LX+i*(tw+GUT)
        rail_card(sp,x,ty,tw,th,hd,FILL[st])
        t=tbox(sp,x+0.26,ty+0.48,tw-0.50,0.44); t.text_frame.word_wrap=False
        text(t,val,T_BIG,DARK[st],bold=True)
        text(tbox(sp,x+0.26,ty+0.98,tw-0.50,0.22),sb,T_CAP,MUTED)
    st_ftri=R.reg("First Time Right index","quality_ftri",88,"88%")
    ring(sp,RX-0.04,3.66,2.16,0.88,FILL[st_ftri],"S05_FTRI","FTRI Score","88%")
    SX,SW=RX+2.42,RW-2.42
    st_smh=R.note("Safe man-hours ITD","3,44,498 with zero LTI","3,44,498","g")
    st_lti=R.reg("Lost time injuries","zero_harm",0,"0")
    t=tbox(sp,SX,3.70,SW,0.50); t.text_frame.word_wrap=False
    text(t,"3,44,498",T_BIG,DARK[st_smh],bold=True)
    text(tbox(sp,SX,4.22,SW,0.24),"Safe Manhours · ITD",T_CAP,MUTED,caps=True,space=0.9)
    box(sp,SX,4.58,SW,0.01,fill=RULE)
    t=tbox(sp,SX,4.72,SW,0.50); t.text_frame.word_wrap=False
    text(t,"0",T_BIG,DARK[st_lti],bold=True)
    text(tbox(sp,SX,5.24,SW,0.24),"Lost Time Injuries",T_CAP,MUTED,caps=True,space=0.9)
    text(tbox(sp,SX,5.58,SW,0.26),"WIR 118 / 26        MIR 63 / 1",T_CAP,BODY)
    st_nm =R.reg("Near misses / HPI","zero_harm",4,"4")
    st_ind=R.reg("Safety inductions vs plan","progress",R.pct(1691,2400),"1,691 of 2,400")
    st_ncr=R.reg("Open NCR","backlog",1,"1")
    ry=6.34
    for i,(lab,val,scale,st,fmt) in enumerate([("Near Misses",4,11,st_nm,"0"),
                                               ("Inductions",1691,2400,st_ind,"#,##0"),
                                               ("Open NCR",1,5,st_ncr,"0")]):
        rail_chart(sp,RX,ry+i*0.74,RW,lab,val,scale,FILL[st],fmt,"S05_"+lab.replace(" ",""))
    cards=[("Critical Issues",'r',["Alternate batching-plant operation delay",
                                   "Work-front handover incomplete",
                                   "RT-1 handover 24 Aug vs BL 16 Jun 26"]),
           ("Key Decision",'g',["Alternate concrete supplier approved","for 5,000 m³ on 31 August 2026."]),
           ("Support Requested",'a',["Adhoc payment vs RA bills within 15 days",
                                     "100% payment for concrete supply",
                                     "Supply RA bills within 21 days"])]
    cw,cy,chh=6.0667,8.60,1.72
    for i,(hd,st,lines) in enumerate(cards):
        x=M+i*(cw+GUT)
        box(sp,x,cy,cw,chh,fill=WHITE,line=RULE); box(sp,x,cy,0.10,chh,fill=FILL[st])
        text(tbox(sp,x+0.28,cy+0.18,cw-0.54,0.26),hd,T_CARD,DARK[st],bold=True,caps=True,space=1.1)
        bullets(sp,x+0.28,cy+0.58,cw-0.54,1.00,lines)
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 6 · Design Dashboard
def s06(sp):
    title_block(sp,"Design Dashboard","Drawing deliverables   ·   DD and GFC status as on 31 Aug 2026")
    st_dd =R.reg("DD approval rate","approval",R.pct(1014,1220),"1,014 of 1,220 · 83%")
    st_gfc=R.reg("GFC approval rate","approval",R.pct(178,247),"178 of 247 · 72%")
    st_bl =R.reg("Design approval backlog","backlog",239,"239 drawings")
    st_fac=R.note("Façade package","design cannot start until commercials close","Critical","r")
    kpi_row(sp,1.62,[K("DD Submitted","1,220","1,014 approved · 83%",st_dd),
                     K("GFC Submitted","247","178 approved · 72%",st_gfc),
                     K("Approval Backlog","239","ICT 170 · Arch 39 · Struct 30",st_bl),
                     K("Façade Package","CRITICAL","awaiting commercials",st_fac)])
    LX,LW=M,11.90; RX,RW=12.80,6.60
    marker(sp,LX,3.24,"Design Deliverable Matrix",TATA)
    hdr=["Discipline","DD Scope","DD Sub","DD Appr","GFC Scope","GFC Sub","GFC Appr","RAG"]
    disc=[("Architectural","372","372","372","478","114","75",372,372),
          ("Structural","182","182","182","607","133","103",182,182),
          ("MEP","791","371","371","791","—","—",371,791),
          ("Façade","235","—","—","NA","—","—",0,235),
          ("Landscape","103","48","48","103","—","—",48,103),
          ("BOH (Kitchen)","128","36","—","NA","—","—",0,128),
          ("VT","41","41","41","NA","—","—",41,41),
          ("IT-ICT & Security","208","170","—","208","—","—",0,208),
          ("Interior & FOH/BOH","1,012","—","—","1,012","—","—",0,1012),
          ("Total","3,313","1,220","1,014","3,284","247","178",1014,3313)]
    rowsd=[];chips={};cellc={}
    for r,(nm,a1,a2,a3,a4,a5,a6,done,scope) in enumerate(disc):
        st=R.rag('progress',R.pct(done,scope))
        R.reg(f"DD approved · {nm}","progress",R.pct(done,scope),f"{done} of {scope}")
        lab={'g':"On track",'a':"Watch",'r':"Critical"}[st]
        rowsd.append([nm,a1,a2,a3,a4,a5,a6,lab]); chips[(r,7)]=st
        cellc[(r,3)]=DARK[st]
    al=[PP_ALIGN.LEFT]+[PP_ALIGN.RIGHT]*6+[PP_ALIGN.CENTER]
    table(sp,LX,3.70,LW,hdr,rowsd,[2.6,1.15,1.05,1.15,1.25,1.05,1.15,1.5],rh=0.62,hh=0.62,
          aligns=al,chips=chips,cell_colors=cellc)
    marker(sp,RX,3.24,"Approval Progress",FILL[st_gfc])
    rail_chart(sp,RX,3.72,RW,"DD Approved",1014,1220,FILL[st_dd],"#,##0","S06_DD",sub_="83% of 1,220")
    rail_chart(sp,RX,4.62,RW,"GFC Approved",178,247,FILL[st_gfc],"#,##0","S06_GFC",sub_="72% of 247")
    y=panel(sp,RX,5.56,RW,2.10,"Closure Priorities",AMBER)
    bullets(sp,RX+0.26,y+0.22,RW-0.52,1.40,
            ["HVAC and Electrical PDA submission","BIM and approval workshops",
             "Façade design and vendor onboarding"])
    y=panel(sp,RX,7.86,RW,2.44,"Watch Item",RED)
    bullets(sp,RX+0.26,y+0.22,RW-0.52,1.80,
            ["Rework on the Façade package starts only","after commercials are finalised.",
             "","Façade design and vendor onboarding","remains the critical-path activity."])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 7 · GFC Drawings Status
def s07(sp):
    title_block(sp,"GFC Drawings Status","Release programme by discipline   ·   August 2026")
    st_f=R.note("Foundation GFC","R0 issued, optimised revision released","Issued","g")
    st_s=R.reg("Structural GFC released","progress",R.pct(3,5),"3 of 5")
    st_a=R.note("Architectural GFC","scheduled 22 - 29 Sep, not yet issued","Scheduled","a")
    st_m=R.note("MEPF GFC","scheduled 22 Sep - 14 Oct, not yet issued","Scheduled","a")
    kpi_row(sp,1.62,[K("Foundation","R0 ISSUED","optimised revision 20 Aug",st_f),
                     K("Structural GFC","3 OF 5","released to date",st_s),
                     K("Architectural GFC","22–29 SEP","B3 / B2 / B1 window",st_a),
                     K("MEPF GFC","22 SEP–14 OCT","B3 through GF",st_m)])
    cw=(RIGHT-M-2*GUT)/3
    y=panel(sp,M,3.24,cw,4.30,"Structural GFC Release",FILL[st_s])
    milestone_rows(sp,M+0.24,y+0.16,cw-0.48,
        [("Foundation","20 Aug","Issued","g"),("Basement 03","20 Aug","Early","g"),
         ("Basement 02","31 Aug","On plan","g"),("Basement 01","18 Sep","Scheduled","a"),
         ("Ground Floor","14 Oct","Scheduled","a")],rh=0.54)
    x2=M+cw+GUT
    y=panel(sp,x2,3.24,cw,4.30,"Architectural GFC Release",FILL[st_a])
    milestone_rows(sp,x2+0.24,y+0.16,cw-0.48,
        [("Basement 03","22 Sep","Scheduled","a"),("Basement 02","22 Sep","Scheduled","a"),
         ("Basement 01","29 Sep","Scheduled","a")],rh=0.54)
    text(tbox(sp,x2+0.24,y+1.90,cw-0.48,0.80),
         "B3 centre line issued 01 Jun\nB2 centre line issued 20 Jul",T_BODY,MUTED,line=1.25)
    x3=M+2*(cw+GUT)
    y=panel(sp,x3,3.24,cw,4.30,"MEPF GFC Release",FILL[st_m])
    milestone_rows(sp,x3+0.24,y+0.16,cw-0.48,
        [("Basement 03","22 Sep","Scheduled","a"),("Basement 02","22 Sep","Scheduled","a"),
         ("Basement 01","29 Sep","Scheduled","a"),("Ground Floor","14 Oct","Scheduled","a")],rh=0.54)
    y=panel(sp,M,7.90,RIGHT-M,2.40,"Foundation GFC Release Note",GREEN)
    bullets(sp,M+0.30,y+0.26,RIGHT-M-0.60,1.70,
        ["R0 issued 27 May 2026; optimised revision issued 20 August 2026.",
         "Structural GFC for Basement 03 released early against plan; Basement 02 tracking on plan for 31 August.",
         "Peer review approval is the gate for the remaining structural releases."])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 8 · BIM Status
def s08(sp):
    title_block(sp,"BIM Status","Model maturity by block and discipline   ·   as on 31 Aug 2026")
    st_ov=R.reg("BIM overall model maturity","progress",83.4,"83.4%")
    st_hi=R.reg("BIM highest block · 3H BOH","progress",89,"89%")
    st_lo=R.reg("BIM lowest block · Retail 1 Structure","progress",75,"75%")
    st_bk=R.note("Blocks under model control","6 blocks × 4 disciplines","6","g")
    kpi_row(sp,1.62,[K("Overall Model","83.4%","completion across all blocks",st_ov),
                     K("Highest","89%","3H Hotel · BOH",st_hi),
                     K("Lowest","75%","Retail 1 · Structure",st_lo),
                     K("Blocks Tracked","6","4 disciplines each",st_bk)])
    marker(sp,M,3.24,"Model Completion by Block",FILL[st_ov],"%   ·   每 bar RAG-coded".replace("每","each"))
    vals=[("Architecture",(84,83,82,86,86,83)),("Structure",(80,82,81,75,83,85)),
          ("MEPF",(82,86,84,83,86,86)),("BOH",(85,89,87,None,None,76))]
    pcs=[[None if v is None else FILL[R.rag('progress',v)] for v in s] for _,s in vals]
    bar_chart(sp,M,3.70,13.60,6.00,
              ["Substructure","3H Hotel","4H Hotel","Retail 1","Retail 2","Convention"],
              vals,(TATA,NAVY,TEAL,GREEN),"S08_BIM",maxv=100,fmt='0"%"',cat_size=T_CAP,lbl_size=14,
              gap=48,label_all=True,label_pos=LP.INSIDE_END,plot=(0.135,0.02,0.845,0.96),
              point_colors=pcs)
    ly=9.86
    for i,(lab,c) in enumerate((("On track ≥ 90%",GREEN),("Watch 70 – 89%",AMBER),("Critical < 70%",RED))):
        lx=M+i*3.1
        box(sp,lx,ly+0.05,0.22,0.13,fill=c,line=RULE,lw=0.5)
        text(tbox(sp,lx+0.32,ly,2.8,0.24),lab,T_CAP,MUTED,caps=True,space=0.8)
    RX,RW=14.60,4.80
    y=panel(sp,RX,3.24,RW,2.60,"Read-Out",AMBER)
    bullets(sp,RX+0.26,y+0.24,RW-0.52,1.80,
            ["Maturity is consistently","above 80% across the","estate, with two","exceptions."])
    y=panel(sp,RX,6.10,RW,2.10,"Below Threshold",RED)
    rows(sp,RX+0.26,y+0.20,RW-0.52,[("Retail 1 · Structure","75%"),("Convention · BOH","76%")],
         rh=0.56,val_color=AMBDK)
    y=panel(sp,RX,8.44,RW,1.86,"Action",AMBER)
    bullets(sp,RX+0.26,y+0.22,RW-0.52,1.20,
            ["Close Retail 1 structural","model gap ahead of the","GFC release window."])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 9 · BIM Clash Report
def s09(sp):
    title_block(sp,"BIM Clash Report","Clash inventory and interface hotspots   ·   as on 31 Aug 2026")
    st_a=R.reg("Clash inventory 17 Aug","clash",15297,"15,297")
    st_b=R.reg("Clash inventory 24 Aug","clash",34845,"34,845")
    st_c=R.reg("Clash inventory 27 Aug","clash",17400,"17,400")
    st_d=R.note("Clash reduction peak to date","17,445 clashes closed in three days","-50%","g")
    kpi_row(sp,1.62,[K("17 Aug","15,297","total clashes",st_a),
                     K("24 Aug","34,845","peak inventory",st_b),
                     K("27 Aug","17,400","total clashes",st_c),
                     K("Reduction","−50%","17,445 clashes closed",st_d)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Clash Trend",FILL[st_c])
    trend=(15297,34845,17400)
    bar_chart(sp,LX,3.72,LW,3.00,["17 Aug","24 Aug","27 Aug"],
              [("Total Clashes",trend)],(TATA,),"S09_Trend",maxv=40000,
              horizontal=False,cat_size=T_CAP,lbl_size=T_CAP,gap=90,
              label_pos=LP.OUTSIDE_END,plot=(0.06,0.12,0.90,0.76),
              point_colors=[[FILL[R.rag('clash',v)] for v in trend]])
    y=panel(sp,LX,7.00,LW,3.30,"Trend Read-Out",AMBER)
    bullets(sp,LX+0.28,y+0.26,LW-0.56,2.40,
            ["Clash count peaked at 34,845 on 24 August following the",
             "federated model refresh.",
             "",
             "Peak-to-current reduction of 17,445 clashes — a 50% cut in",
             "three days through targeted MEPF coordination."])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"27 Aug Hotspots",AMBER,"by interface")
    hs=(5131,2233,1957,1576,1339,1073)
    for nm,v in zip(("MEPF vs AR","LA vs MEPF","MEPF vs ST","AR vs ST","LA vs ST","LA vs LA"),hs):
        R.reg(f"Clash hotspot · {nm}","hotspot",v,f"{v:,}")
    bar_chart(sp,RX,3.72,RW,4.50,
              ["MEPF vs AR","LA vs MEPF","MEPF vs ST","AR vs ST","LA vs ST","LA vs LA"],
              [("Count",hs)],(TATA,),"S09_Hotspots",maxv=6200,
              cat_size=T_CAP,lbl_size=T_CAP,gap=60,label_pos=LP.OUTSIDE_END,
              plot=(0.19,0.02,0.79,0.96),
              point_colors=[[FILL[R.rag('hotspot',v)] for v in hs]])
    y=panel(sp,RX,8.48,RW,1.82,"Concentration",AMBER)
    bullets(sp,RX+0.28,y+0.24,RW-0.56,1.20,
            ["The top three interfaces account for 54% of the 27 August clash inventory.",
             "MEPF versus Architecture alone represents 29%."])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 10 · MEP NSC Packages
def s10(sp):
    title_block(sp,"MEP NSC Packages","Release status and forward pipeline   ·   September 2026")
    st_t=R.reg("NSC packages released","progress",R.pct(6,17),"6 of 17")
    st_i=R.note("Initial submissions complete","6 packages submitted","6","g")
    st_d=R.note("Packages due by 15 Sep","immediate action window","5","a")
    st_p=R.note("Forward pipeline","planned 20 Sep - 20 Oct","6","a")
    kpi_row(sp,1.62,[K("Total Packages","17","6 released · 35%",st_t),
                     K("Initial Submission","6","completed",st_i),
                     K("Due by 15 Sep","5","immediate window",st_d),
                     K("Forward Pipeline","6","20 Sep – 20 Oct",st_p)])
    cw=(RIGHT-M-2*GUT)/3
    y=panel(sp,M,3.24,cw,5.10,"Initial Submissions",GREEN)
    milestone_rows(sp,M+0.24,y+0.18,cw-0.48,
        [("Chillers & Pumps","07 Aug","Done","g"),("Cooling Tower & Pumps","07 Aug","Done","g"),
         ("STP & ETP","28 Apr","Done","g"),("DG Set","29 Jul","Done","g"),
         ("Transformer","14 Aug","Done","g"),("Lifts & Escalators","25 Aug","Done","g")],rh=0.62)
    x2=M+cw+GUT
    y=panel(sp,x2,3.24,cw,5.10,"Immediate Dates",AMBER)
    milestone_rows(sp,x2+0.24,y+0.18,cw-0.48,
        [("PHE Complete","05 Sep","Due","a"),("Fire Fighting","05 Sep","Due","a"),
         ("UPS","05 Sep","Due","a"),("HT Panels","10 Sep","Due","a"),
         ("FAPA","15 Sep","Due","a")],rh=0.62)
    x3=M+2*(cw+GUT)
    y=panel(sp,x3,3.24,cw,5.10,"Forward Pipeline",AMBER)
    milestone_rows(sp,x3+0.24,y+0.18,cw-0.48,
        [("HVAC Low Side","20 Sep","Planned",'a'),("Electrical Low Side","20 Sep","Planned",'a'),
         ("HT & LT Cables","20 Sep","Planned",'a'),("Bus Ducts","25 Sep","Planned",'a'),
         ("LT Panels","30 Sep","Planned",'a'),("ELV Systems","20 Oct","Planned",'a')],rh=0.62)
    y=panel(sp,M,8.70,RIGHT-M,1.60,"Next Deliveries",AMBER)
    bullets(sp,M+0.30,y+0.26,RIGHT-M-0.60,0.90,
            ["Close PHE, Fire Fighting and UPS by 05 September 2026 to hold the September release window."])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 11 · Procurement
def s11(sp):
    title_block(sp,"Procurement Dashboard","Package status, formwork and material milestones   ·   August 2026")
    st_c=R.note("Civil package","rebar vendor award by 15 Sep","On track","g")
    st_m=R.note("MEP package","LPS onboarded, NSC vendors open","Watchlist","a")
    st_f=R.note("Façade and ID packages","ID not issued, façade tender pending","Critical","r")
    st_w=R.reg("Formwork delivered to site","progress",R.pct(1500,7700),"1,500 of 7,700 m²")
    kpi_row(sp,1.62,[K("Civil","ON TRACK","rebar vendor by 15 Sep",st_c),
                     K("MEP","WATCHLIST","LPS onboarded · NSC open",st_m),
                     K("Façade & ID","CRITICAL","ID and tender pending",st_f),
                     K("Formwork at Site","1,500 m²","of 7,700 m² · 19%",st_w)])
    LX,LW=M,11.60
    marker(sp,LX,3.24,"Formwork Procurement",FILL[st_w],"m²")
    y=panel(sp,LX,3.70,LW,3.10,"Column / Shear Wall / Footing",AMBER)
    milestone_rows(sp,LX+0.28,y+0.20,LW-0.56,
        [("1,500 m² at site","03 Sep","Dispatched","g"),
         ("6,200 m² phased supply","15 Oct","Planned","a")],rh=0.62)
    text(tbox(sp,LX+0.28,y+1.60,LW-0.56,0.60),
         "Full column and shear-wall formwork dispatch completes 15 October 2026.",T_BODY,MUTED,line=1.25)
    y=panel(sp,LX,7.06,LW,3.24,"Slab Formwork",AMBER)
    yy=y+0.24
    for lab,val,cap,st in (("Received","1,500 m²","at site",'g'),
                           ("Committed","1,700 m²","by 20 Sep",'a'),
                           ("Pipeline","10,000 m²","order by 11 Sep",'r')):
        R.note(f"Slab formwork · {lab}",cap,val,st)
        box(sp,LX+0.28,yy,0.09,0.72,fill=FILL[st])
        text(tbox(sp,LX+0.50,yy+0.04,3.2,0.26),lab,T_CAP,MUTED,caps=True,space=0.9)
        text(tbox(sp,LX+0.50,yy+0.32,3.2,0.34),val,T_MID,DARK[st],bold=True)
        text(tbox(sp,LX+4.20,yy+0.24,3.0,0.28),cap,T_BODY,BODY)
        yy+=0.92
    RX,RW=12.80,6.60
    marker(sp,RX,3.24,"Material Milestones",AMBER)
    y=panel(sp,RX,3.70,RW,6.60,"September – October",AMBER)
    milestone_rows(sp,RX+0.26,y+0.22,RW-0.52,
        [("30 MT PT strand","05 Sep","Planned",'a'),
         ("3,000 MT reinforcement steel","Sep","Planned",'a'),
         ("Slab-formwork order","11 Sep","Not placed",'r'),
         ("1,700 m² slab formwork","20 Sep","Planned",'a'),
         ("Full formwork dispatch","15 Oct","Planned",'a')],rh=0.86)
    text(tbox(sp,RX+0.26,y+4.70,RW-0.52,1.30),
         "ID package not issued and the Façade tender remains pending — both sit on the critical path.",
         T_BODY,REDDK,line=1.28)
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 12 · Construction
def s12(sp):
    title_block(sp,"Construction Dashboard","Physical progress and constraints   ·   August 2026")
    st_cn=R.reg("Monthly concrete vs plan","progress",R.pct(3025,5584),"3,025 of 5,584 m³")
    st_wm=R.reg("Workmen vs plan","progress",R.pct(1032,1000),"1,032 of 1,000")
    st_sf=R.note("Staff deployed","142 against requirement","142","g")
    st_fd=R.reg("Foundations complete","progress",R.pct(62,147),"62 of 147")
    kpi_row(sp,1.62,[K("Month Concrete","3,025 m³","against 5,584 m³ plan · 54%",st_cn),
                     K("Workmen","1,032","against 1,000 plan · 103%",st_wm),
                     K("Staff","142","deployed on site",st_sf),
                     K("Foundations","62 of 147","across three blocks · 42%",st_fd)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Area-Wise Foundations",FILL[st_fd])
    for i,(lab,val,scale) in enumerate([("4-H Hotel",39,46),("3-H Hotel",15,51),
                                        ("Convention Centre",8,50)]):
        st=R.reg(f"Foundations · {lab}","progress",R.pct(val,scale),f"{val} of {scale}")
        rail_chart(sp,LX,3.72+i*0.86,LW,lab,val,scale,FILL[st],"#,##0",
                   "S12_"+lab.split()[0].replace("-",""),sub_=f"of {scale} foundations")
    text(tbox(sp,LX,6.34,LW,0.28),"Retail 1 / 2 — awaiting handover",T_BODY,REDDK)
    y=panel(sp,LX,6.82,LW,3.48,"Milestones Achieved",GREEN)
    bullets(sp,LX+0.28,y+0.26,LW-0.56,2.50,
            ["4-H: 24 of 77 columns cast",
             "Convention Centre footing concreting commenced",
             "Alternative RMC source approved",
             "Reinforcement steel base rate approved 25 Aug 2026"])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Constraints & Recovery",RED)
    y=panel(sp,RX,3.72,RW,3.10,"Key Constraints",RED)
    bullets(sp,RX+0.28,y+0.24,RW-0.56,2.20,
            ["Retail areas not released",
             "Slow concrete supply and batching readiness",
             "Monsoon disruption and delayed TMT rate approval"])
    y=panel(sp,RX,7.08,RW,3.22,"Recovery Actions",AMBER)
    bullets(sp,RX+0.28,y+0.24,RW-0.56,2.40,
            ["Resequence around available handovers",
             "Deploy alternate RMC source for mass concrete pours",
             "Progress on available GFC and sustain manpower",
             "Engineering: PT drawings availability",
             "Construction: commence Retail blocks"])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 13 · Mobilization
def s13(sp):
    title_block(sp,"Mobilization Dashboard","Manpower, camp delivery and plant   ·   August 2026")
    st_pl=R.note("September manpower plan","+173 net augmentation required","1,205","a")
    st_av=R.reg("Workmen available vs plan","progress",R.pct(1032,1000),"1,032 of 1,000")
    st_tc=R.reg("Tower cranes installed","progress",R.pct(3,5),"3 of 5")
    st_sh=R.reg("Workmen sheds erected","progress",R.pct(1,5),"1 of 5 occupied")
    kpi_row(sp,1.62,[K("Sept Manpower Plan","1,205","+173 net augmentation",st_pl),
                     K("Currently Available","1,032","103% of August plan",st_av),
                     K("Tower Cranes","03 / 05","1 installed · 60%",st_tc),
                     K("Workmen Sheds","5 × G+2","1 occupied · all by 31 Oct",st_sh)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Workmen Camp Delivery",FILL[st_sh],"G+2 sheds")
    y=panel(sp,LX,3.72,LW,3.52,"Shed Programme",AMBER)
    milestone_rows(sp,LX+0.28,y+0.20,LW-0.56,
        [("C1","22 Aug","Occupied","g"),("B1","18 Sep","Erection","a"),
         ("A1","04 Oct","Plinth done","a"),("C2","06 Oct","Plinth done","a"),
         ("B2","31 Oct","WO issued","r")],rh=0.54)
    marker(sp,LX,7.50,"Manpower",FILL[st_av])
    bar_chart(sp,LX,7.96,LW,2.34,["Available","Sept Plan"],
              [("Workmen",(1032,1205))],(TATA,),"S13_Manpower",maxv=1500,
              cat_size=T_CAP,lbl_size=T_CAP,gap=70,label_pos=LP.INSIDE_END,
              plot=(0.13,0.04,0.85,0.92),point_colors=[[GREEN,AMBER]])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Camp Amenities & Services",AMBER)
    y=panel(sp,RX,3.72,RW,4.30,"Delivery Status",AMBER)
    milestone_rows(sp,RX+0.28,y+0.20,RW-0.56,
        [("Kitchen 1","—","Completed","g"),("Cement Store","—","Completed","g"),
         ("Toilets (220)","—","20 of 220","r"),("Bath Sheds","13 Sep","Scheduled","a"),
         ("Kitchen 2","10 Sep","Scheduled","a"),("Dining 2 / Store","15 Sep","Scheduled","a"),
         ("Drain","26 Sep","Scheduled","a")],rh=0.52)
    y=panel(sp,RX,8.28,RW,2.02,"Plant & Machinery Mobilization",GREEN)
    rows(sp,RX+0.28,y+0.22,RW-0.56,
         [("DG Sets","04 / 04"),("Trailer","02 / 02"),("Vibro Roller","01 / 01")],
         rh=0.46,val_color=GRNDK)
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 14–16 · MOM tracker
MOM_COLW=[0.6,2.2,6.6,2.3,1.3,4.1,1.4]
MOM_HDR=["Sr.","Point Discussed","Discussion / Observation","Action By","Target Date",
         "TPL Update","RAG"]

# ═══════════════════════════════════════════════════ 17 · September Plan
def s17(sp):
    title_block(sp,"September 2026 Plan","Planned value, quantities and weekly distribution")
    st=R.note("September planned value","forward plan, not yet earned","₹37.5 Cr","a")
    R.note("September supply plan","forward plan","₹24.0 Cr","a")
    R.note("September service plan","forward plan","₹12.5 Cr","a")
    R.note("September design plan","forward plan, low exposure","₹1.0 Cr","g")
    kpi_row(sp,1.62,[K("Total Planned Value","₹37.5 Cr","September 2026",'a'),
                     K("Supply","₹24.0 Cr","64% of plan",'a'),
                     K("Service","₹12.5 Cr","33% of plan",'a'),
                     K("Design","₹1.0 Cr","3% of plan",'g')])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Major Items",AMBER,"₹ Cr")
    y=panel(sp,LX,3.72,LW,4.10,"Value Breakdown",AMBER)
    rows(sp,LX+0.28,y+0.22,LW-0.56,
         [("Reinforcement Supply","₹17.2 Cr"),("Reinforcement Service","₹8.0 Cr"),
          ("M40 Supply","₹6.2 Cr"),("M40 Service","₹3.8 Cr"),
          ("Design Review","₹1.0 Cr"),("Other Activities","₹1.3 Cr")],rh=0.56,val_color=AMBDK)
    marker(sp,LX,8.04,"Value Mix",AMBER)
    bar_chart(sp,LX,8.50,LW,1.80,["Supply","Service","Design"],
              [("₹ Cr",(24.0,12.5,1.0))],(AMBER,),"S17_ValueMix",maxv=30,fmt='0.0',
              cat_size=T_CAP,lbl_size=T_CAP,gap=60,label_pos=LP.OUTSIDE_END,
              plot=(0.13,0.02,0.82,0.96),point_colors=[[AMBER,AMBER,GREEN]])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Weekly Distribution",AMBER,"benchmark: 3,025 m³ achieved in August")
    y=panel(sp,RX,3.72,RW,3.40,"M40 Concrete and Reinforcement",AMBER)
    wk=[("W1",1943,750),("W2",2553,750),("W3",1946,500),("W4",3584,1000)]
    data=[];cc={}
    for r,(w,m40,rb) in enumerate(wk):
        st_w='r' if m40>3000 else 'a'
        R.note(f"September {w} M40 pour","vs 3,025 m³ achieved in August",f"{m40:,} m³",st_w)
        data.append([w,f"{m40:,}",f"{rb:,}"]); cc[(r,1)]=DARK[st_w]
    table(sp,RX+0.26,y+0.20,RW-0.52,["Week","M40 (m³)","Rebar (MT)"],data,[1.2,2.0,2.0],
          rh=0.52,hh=0.44,aligns=[PP_ALIGN.LEFT,PP_ALIGN.RIGHT,PP_ALIGN.RIGHT],cell_colors=cc)
    y=panel(sp,RX,7.38,RW,2.92,"Critical Quantities",RED)
    crit=[("M40 Supply","10,344 m³",'r'),("M40 Service","10,344 m³",'r'),
          ("Reinforcement","3,000 MT",'r'),("M10 Supply + Service","405 m³",'a')]
    for i,(lab,val,st) in enumerate(crit):
        R.note(f"September quantity · {lab}","against 3,025 m³ August run-rate",val,st)
        yy=y+0.22+i*0.58
        text(tbox(sp,RX+0.28,yy+0.04,RW*0.55,0.28),lab,T_BODY,BODY)
        t=tbox(sp,RX+0.28+RW*0.58,yy+0.04,RW*0.36,0.28); t.text_frame.word_wrap=False
        text(t,val,T_BODY,DARK[st],bold=True,align=PP_ALIGN.RIGHT)
        if i<3: box(sp,RX+0.28,yy+0.565,RW-0.56,0.008,fill=RULE)
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 19 · Compliance
def s19(sp):
    title_block(sp,"Statutory Compliance","Post-novation closure path and open positions   ·   August 2026")
    st_o=R.reg("Statutory items closed","progress",R.pct(1,4),"1 of 4")
    kpi_row(sp,1.62,[K("Open Positions","3","of 4 tracked items",'r'),
                     K("Closed","1","policy amendment",'g'),
                     K("Client Input","PENDING","BG amendment · 21 Aug 2026",'r'),
                     K("Next Milestone","05 SEP","BOCW receipt expected",'a')])
    marker(sp,M,3.24,"Compliance Closure Path",TATA)
    items=[("01","BG Amendment","ALACL input pending","r",
            ["Details requested from client on 21 Aug 2026.",
             "Follow up for ROC, NCLT, MCA, board resolution",
             "and supporting novation documents."]),
           ("02","Policy Amendment","Updated","g",
            ["CAR and Marine policies amended following","novation. No further action required."]),
           ("03","Labour Licence","Closure required","a",
            ["Compliance closure up to July 2026 pending.",
             "Complete formalities and record statutory","acknowledgement."]),
           ("04","BOCW","Expected 05 Sep","a",
            ["Receipt awaited. Track receipt and close","supporting documentation immediately."])]
    cw=(RIGHT-M-3*GUT)/4
    for i,(num,name,status,kind,lines) in enumerate(items):
        R.note(f"Statutory · {name}",status,status,kind)
        x=M+i*(cw+GUT)
        box(sp,x,3.70,cw,6.60,fill=WHITE,line=RULE)
        box(sp,x,3.70,cw,0.42,fill=FILL[kind])
        text(tbox(sp,x+0.20,3.805,cw-0.40,0.24),f"ITEM {num}",T_CARD,WHITE,bold=True,caps=True,space=1.2)
        text(tbox(sp,x+0.24,4.32,cw-0.48,0.96),name,T_MID,DARK[kind],bold=True,line=1.12)
        chip(sp,x+0.24,5.38,cw-0.48,0.38,status,kind)
        bullets(sp,x+0.24,5.98,cw-0.48,4.00,lines,size=T_BODY)
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 20 · EHS
def s20(sp):
    title_block(sp,"EHS Performance","Zero Harm   ·   August 2026")
    R.note("Safe man-hours FTM","zero lagging incidents in the month","1,27,954","g")
    R.note("Safe man-hours ITD","zero lagging incidents to date","3,44,498","g")
    st_l=R.reg("Fatalities and lost time injuries","zero_harm",0,"0")
    st_n=R.reg("High-potential incidents and near misses","zero_harm",4,"4")
    kpi_row(sp,1.62,[K("Safe Man-Hours FTM","1,27,954","August 2026",'g'),
                     K("Safe Man-Hours ITD","3,44,498","inception to date",'g'),
                     K("Fatalities & LTI","0","zero lagging incidents",st_l),
                     K("Near Misses","4","high-potential incidents",st_n)])
    LX,LW=M,11.60
    marker(sp,LX,3.24,"Leading Indicators",GREEN,"activity counts · FTM vs ITD")
    bar_chart(sp,LX,3.70,LW,5.10,
              ["Inductions","Safety Observations","Tool Box Talks","Training Sessions"],
              [("FTM",(585,122,265,35)),("ITD",(1691,781,615,109))],
              (GREEN,GRNDK),"S20_EHS",maxv=1900,fmt='#,##0',cat_size=T_CAP,lbl_size=15,gap=55,
              label_all=True,label_pos=LP.OUTSIDE_END,plot=(0.17,0.02,0.74,0.96))
    ly=8.94
    for i,(lab,c) in enumerate((("For the Month (FTM)",GREEN),("Inception to Date (ITD)",GRNDK))):
        lx=LX+i*3.6
        box(sp,lx,ly+0.05,0.22,0.13,fill=c,line=RULE,lw=0.5)
        text(tbox(sp,lx+0.32,ly,3.2,0.24),lab,T_CAP,MUTED,caps=True,space=0.8)
    y=panel(sp,LX,9.38,LW,0.92,"Note",GREEN)
    text(tbox(sp,LX+0.28,y+0.14,LW-0.56,0.34),
         "Leading indicators are proactive activity — all green. Safe man-hours sit in the header cards.",
         T_CAP,MUTED)
    RX,RW=12.80,6.60
    marker(sp,RX,3.24,"Lagging Indicators",GREEN)
    y=panel(sp,RX,3.70,RW,3.90,"Zero Harm Achieved",GREEN)
    for i,(lab,val,st) in enumerate([("Fatalities & Lost Time Injuries","0",'g'),
                                     ("Restricted Work & Medical Treatment","0",'g'),
                                     ("High-Potential Incidents & Near Misses","4",'a')]):
        yy=y+0.24+i*1.10
        text(tbox(sp,RX+0.28,yy,RW-1.60,0.60),lab,T_BODY,BODY,line=1.2)
        t=tbox(sp,RX+RW-1.30,yy-0.06,1.00,0.50); t.text_frame.word_wrap=False
        text(t,val,T_BIG,DARK[st],bold=True,align=PP_ALIGN.RIGHT)
        if i<2: box(sp,RX+0.28,yy+0.90,RW-0.56,0.008,fill=RULE)
    y=panel(sp,RX,7.86,RW,2.44,"Commitment",GREEN)
    bullets(sp,RX+0.28,y+0.26,RW-0.56,1.70,
            ["Zero incidents recorded across all","primary lagging parameters,","including fatalities and lost","time injuries."])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 27 · Quality Indicators
def s27(sp):
    title_block(sp,"Quality Indicators","Leading and lagging quality performance   ·   August 2026")
    st_f=R.reg("First Time Right index","quality_ftri",88,"88%")
    st_t=R.note("Training effort imparted","74 hours delivered","74","g")
    st_g=R.note("Good and best practices","16 recorded in the month","16","g")
    st_d=R.reg("Deviation closure turnaround","tat_days",19.9,"19.9 days")
    kpi_row(sp,1.62,[K("First Time Right","88%","target 95%",st_f),
                     K("Training Imparted","74","effort hours",st_t),
                     K("Good / Best Practices","16","recorded this month",st_g),
                     K("Deviation Closure","19.9 d","average · target 14",st_d)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Leading Indicators",GREEN,"proactive quality inputs")
    bar_chart(sp,LX,3.72,LW,4.10,
              ["Training Imparted","Good/Best Practices","Material Approvals",
               "Management Walkdown","Mockups"],
              [("Count",(74,16,12,9,5))],(GREEN,),"S27_Leading",maxv=92,
              cat_size=T_CAP,lbl_size=T_CAP,gap=55,label_pos=LP.OUTSIDE_END,
              plot=(0.30,0.02,0.68,0.96))
    y=panel(sp,LX,8.06,LW,2.24,"Read-Out",GREEN)
    bullets(sp,LX+0.28,y+0.24,LW-0.56,1.50,
            ["Proactive quality investment translates directly into",
             "near-perfect execution and zero-defect outcomes."])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Lagging Indicators",AMBER,"actual project outcomes")
    lag=[("Obs. External",32,'r'),("Obs. Internal",15,'a'),("Rejection",1,'a'),
         ("Repetitive Dev.",0,'g'),("Snag Issued",0,'g'),("Stop Work",0,'g')]
    for nm,v,st in lag: R.note(f"Quality lagging · {nm}","open defect count",v,st)
    bar_chart(sp,RX,3.72,RW,4.10,[n for n,_,_ in lag],
              [("Count",tuple(v for _,v,_ in lag))],(NAVY,),"S27_Lagging",maxv=40,
              cat_size=T_CAP,lbl_size=T_CAP,gap=45,label_pos=LP.OUTSIDE_END,
              plot=(0.24,0.02,0.74,0.96),
              point_colors=[[FILL[st] for _,_,st in lag]])
    ring(sp,RX,8.10,2.20,0.88,FILL[st_f],"S27_FTRI","FTRI Score","88%")
    SX=RX+2.50
    for i,(lab,val,st) in enumerate([("Skill Ratio","0.60",'a'),("Flash Report","0",'g'),
                                     ("Deviation Closure in TAT","19.9 days",st_d)]):
        R.note(f"Quality · {lab}","monthly outcome",val,st)
        yy=8.24+i*0.62
        text(tbox(sp,SX,yy+0.04,(RW-2.50)*0.55,0.28),lab,T_BODY,BODY)
        t=tbox(sp,SX+(RW-2.50)*0.58,yy+0.04,(RW-2.50)*0.40,0.28); t.text_frame.word_wrap=False
        text(t,val,T_BODY,DARK[st],bold=True,align=PP_ALIGN.RIGHT)
        if i<2: box(sp,SX,yy+0.605,RW-2.50,0.008,fill=RULE)
    rag_legend(sp)

# ═══════════════════════════════════════════════════ 28 · Quality Performance
def s28(sp, images=None):
    title_block(sp,"Quality Performance","Observation and training closure   ·   August 2026")
    st_o=R.reg("Observation closure rate","approval",R.pct(24,32),"24 of 32 · 75%")
    st_op=R.reg("Open observations","backlog",8,"8 open")
    st_n=R.reg("NCR closure rate","approval",R.pct(103,123),"103 of 123 · 84%")
    st_t=R.note("Trainings delivered","44 sessions, 450 man-hours","44","g")
    kpi_row(sp,1.62,[K("Observations Closed","24","of 32 raised · 75%",st_o),
                     K("Open Observations","8","under action",st_op),
                     K("NCR Closed","103","of 123 raised · 84%",st_n),
                     K("Trainings","44","450 man-hours",st_t)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Observation Closure",FILL[st_o])
    bar_chart(sp,LX,3.72,LW,2.60,["Closed","Open"],[("Observations",(24,8))],(GREEN,),
              "S28_Observations",maxv=32,cat_size=T_CAP,lbl_size=T_CAP,gap=70,
              label_pos=LP.INSIDE_END,plot=(0.16,0.04,0.82,0.92),
              point_colors=[[GREEN,AMBER]])
    marker(sp,LX,6.60,"NCR Closure",FILL[st_n])
    bar_chart(sp,LX,7.08,LW,2.60,["Closed","Open"],[("NCR",(103,20))],(GREEN,),
              "S28_NCR",maxv=130,cat_size=T_CAP,lbl_size=T_CAP,gap=70,
              label_pos=LP.INSIDE_END,plot=(0.16,0.04,0.82,0.92),
              point_colors=[[GREEN,AMBER]])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Training Delivered",GREEN)
    y=panel(sp,RX,3.72,RW,3.10,"Cumulative",GREEN)
    rows(sp,RX+0.28,y+0.24,RW-0.56,
         [("Cumulative trainings","44"),("Cumulative man-hours","450.02")],
         rh=0.72,vsize=T_MID,val_color=GRNDK)
    y=panel(sp,RX,7.08,RW,3.22,"Excel Linkage Note",GREEN)
    bullets(sp,RX+0.28,y+0.26,RW-0.56,2.30,
            ["The seven source charts on this slide linked to an external",
             "SharePoint workbook and would not refresh outside the TPL",
             "tenant. Every chart in this deck now reads from the embedded",
             "MRM_Master_Data.xlsx — one dedicated worksheet per chart."])
    rag_legend(sp)

# ═══════════════════════════════════════════════════ dividers
def divider(sp, title, subtitle=None):
    text(tbox(sp,2.50,4.60,15.00,1.10),title,56,NAVY,bold=True,align=PP_ALIGN.CENTER,wrap=False)
    box(sp,8.20,5.92,3.60,0.05,fill=TATA)
    if subtitle:
        text(tbox(sp,2.50,6.20,15.00,0.40),subtitle,T_SECT,MUTED,caps=True,space=1.4,
             align=PP_ALIGN.CENTER,wrap=False)
