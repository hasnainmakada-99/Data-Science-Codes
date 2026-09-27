#!/usr/bin/env python3
"""Per-slide construction for the MRM Aug-26 deck."""
from deck import *
from pptx.enum.chart import XL_LABEL_POSITION as LP

# ═══════════════════════════════════════════════════ 5 · Executive Dashboard
def s05(sp):
    title_block(sp,"Executive Dashboard","Adani Lucknow Airport City   ·   Monthly Review   ·   August 2026")
    kpi_row(sp,1.62,[("Contract Value","₹1,725 Cr","39-month contract",NAVY,DEEP),
                     ("Duration","39 Months","commenced Feb 2026",NAVY,DEEP),
                     ("Completion","15 May 2029","contractual target",NAVY,DEEP),
                     ("Project Health","WATCHLIST","commercial slippage",AMBER,AMBDK)])
    LX,LW=M,11.30; RX,RW=12.20,7.20
    marker(sp,LX,3.24,"Commercial Progress",TATA,"₹ Cr")
    marker(sp,RX,3.24,"Safety & Quality",GREEN)
    bar_chart(sp,LX,3.70,LW,2.24,["FTM","CUM"],
              [("Actual",(15.50,37.80)),("Revamp Plan",(31.06-15.50,54.00-37.80)),
               ("Baseline",(40.00-31.06,114.00-54.00))],
              (TATA,BLUMID,RGBColor(0xCF,0xE2,0xF1)),"Commercial",maxv=120,fmt='0.0',stacked=True,
              cat_size=19,lbl_size=18,gap=78,label_pos=LP.INSIDE_END,plot=(0.075,0.03,0.915,0.94))
    ly=6.08
    for i,(lab,c) in enumerate((("Actual",TATA),("Revamp Plan",BLUMID),("Baseline",RGBColor(0xCF,0xE2,0xF1)))):
        lx=LX+i*2.35
        box(sp,lx,ly+0.05,0.22,0.13,fill=c,line=RULE,lw=0.5)
        text(tbox(sp,lx+0.32,ly,2.0,0.24),lab,T_CAP,MUTED,caps=True,space=0.8)
    tiles=[("FTM vs Baseline","−61%","₹24.50 Cr short",RED,RED),
           ("CUM vs Baseline","−67%","₹76.20 Cr short",RED,RED),
           ("Gap to Close","₹76.2 Cr","33 months remaining",AMBER,DEEP)]
    tw,ty,th=3.5667,6.60,1.30
    for i,(hd,val,sb,rail,vc) in enumerate(tiles):
        x=LX+i*(tw+GUT)
        rail_card(sp,x,ty,tw,th,hd,rail)
        t=tbox(sp,x+0.26,ty+0.48,tw-0.50,0.44); t.text_frame.word_wrap=False
        text(t,val,T_BIG,vc,bold=True)
        text(tbox(sp,x+0.26,ty+0.98,tw-0.50,0.22),sb,T_CAP,MUTED)
    ring(sp,RX-0.04,3.66,2.16,0.88,GREEN,"Quality","FTRI Score","88%")
    SX,SW=RX+2.42,RW-2.42
    t=tbox(sp,SX,3.70,SW,0.50); t.text_frame.word_wrap=False
    text(t,"3,44,498",T_BIG,DEEP,bold=True)
    text(tbox(sp,SX,4.22,SW,0.24),"Safe Manhours · ITD",T_CAP,MUTED,caps=True,space=0.9)
    box(sp,SX,4.58,SW,0.01,fill=RULE)
    t=tbox(sp,SX,4.72,SW,0.50); t.text_frame.word_wrap=False
    text(t,"0",T_BIG,GREEN,bold=True)
    text(tbox(sp,SX,5.24,SW,0.24),"Lost Time Injuries",T_CAP,MUTED,caps=True,space=0.9)
    text(tbox(sp,SX,5.58,SW,0.26),"WIR 118 / 26        MIR 63 / 1",T_CAP,BODY)
    ry=6.34
    for i,(lab,val,scale,col,fmt) in enumerate([("Near Misses",4,11,AMBER,"0"),
                                                ("Inductions",1691,2400,GREEN,"#,##0"),
                                                ("Open NCR",1,5,GREEN,"0")]):
        rail_chart(sp,RX,ry+i*0.74,RW,lab,val,scale,col,fmt)
    cards=[("Critical Issues",RED,["Alternate batching-plant operation delay",
                                   "Work-front handover incomplete",
                                   "RT-1 handover 24 Aug vs BL 16 Jun 26"]),
           ("Key Decision",GREEN,["Alternate concrete supplier approved","for 5,000 m³ on 31 August 2026."]),
           ("Support Requested",TATA,["Adhoc payment vs RA bills within 15 days",
                                      "100% payment for concrete supply",
                                      "Supply RA bills within 21 days"])]
    cw,cy,chh=6.0667,8.86,1.72
    for i,(hd,rail,lines) in enumerate(cards):
        x=M+i*(cw+GUT)
        box(sp,x,cy,cw,chh,fill=WHITE,line=RULE); box(sp,x,cy,0.10,chh,fill=rail)
        text(tbox(sp,x+0.28,cy+0.18,cw-0.54,0.26),hd,T_CARD,NAVY,bold=True,caps=True,space=1.1)
        bullets(sp,x+0.28,cy+0.58,cw-0.54,1.00,lines)

# ═══════════════════════════════════════════════════ 6 · Design Dashboard
def s06(sp):
    title_block(sp,"Design Dashboard","Drawing deliverables   ·   DD and GFC status as on 31 Aug 2026")
    kpi_row(sp,1.62,[("DD Submitted","1,220","1,014 approved · 83%",NAVY,DEEP),
                     ("GFC Submitted","247","178 approved · 72%",NAVY,DEEP),
                     ("Approval Backlog","239","ICT 170 · Arch 39 · Struct 30",AMBER,AMBDK),
                     ("Façade Package","CRITICAL","awaiting commercials",RED,REDDK)])
    LX,LW=M,11.90; RX,RW=12.80,6.60
    marker(sp,LX,3.24,"Design Deliverable Matrix",TATA)
    hdr=["Discipline","DD Scope","DD Sub","DD Appr","GFC Scope","GFC Sub","GFC Appr"]
    rowsd=[["Architectural","372","372","372","478","114","75"],
           ["Structural","182","182","182","607","133","103"],
           ["MEP","791","371","371","791","—","—"],
           ["Façade","235","—","—","NA","—","—"],
           ["Landscape","103","48","48","103","—","—"],
           ["BOH (Kitchen)","128","36","—","NA","—","—"],
           ["VT","41","41","41","NA","—","—"],
           ["IT-ICT & Security","208","170","—","208","—","—"],
           ["Interior & FOH/BOH","1,012","—","—","1,012","—","—"],
           ["Total","3,313","1,220","1,014","3,284","247","178"]]
    al=[PP_ALIGN.LEFT]+[PP_ALIGN.RIGHT]*6
    table(sp,LX,3.70,LW,hdr,rowsd,[3.0,1.3,1.2,1.3,1.4,1.2,1.3],rh=0.62,hh=0.62,aligns=al)
    marker(sp,RX,3.24,"Approval Progress",GREEN)
    rail_chart(sp,RX,3.72,RW,"DD Approved",1014,1220,GREEN,"#,##0","Design",sub_="83% of 1,220")
    rail_chart(sp,RX,4.62,RW,"GFC Approved",178,247,AMBER,"#,##0","Design",sub_="72% of 247")
    y=panel(sp,RX,5.56,RW,2.10,"Closure Priorities",NAVY)
    bullets(sp,RX+0.26,y+0.22,RW-0.52,1.40,
            ["HVAC and Electrical PDA submission","BIM and approval workshops",
             "Façade design and vendor onboarding"])
    y=panel(sp,RX,7.86,RW,2.72,"Watch Item",RED)
    bullets(sp,RX+0.26,y+0.22,RW-0.52,2.00,
            ["Rework on the Façade package starts only","after commercials are finalised.",
             "","Façade design and vendor onboarding","remains the critical-path activity."])

# ═══════════════════════════════════════════════════ 7 · GFC Drawings Status
def s07(sp):
    title_block(sp,"GFC Drawings Status","Release programme by discipline   ·   August 2026")
    kpi_row(sp,1.62,[("Foundation","R0 ISSUED","optimised revision 20 Aug",GREEN,GRNDK),
                     ("Structural GFC","3 OF 5","released to date",NAVY,DEEP),
                     ("Architectural GFC","22–29 SEP","B3 / B2 / B1 window",NAVY,DEEP),
                     ("MEPF GFC","22 SEP–14 OCT","B3 through GF",AMBER,AMBDK)])
    cw=(RIGHT-M-2*GUT)/3
    y=panel(sp,M,3.24,cw,4.30,"Structural GFC Release",NAVY)
    milestone_rows(sp,M+0.24,y+0.16,cw-0.48,
        [("Foundation","20 Aug","Issued","g"),("Basement 03","20 Aug","Early","g"),
         ("Basement 02","31 Aug","On plan","g"),("Basement 01","18 Sep","Scheduled","n"),
         ("Ground Floor","14 Oct","On plan","n")],rh=0.54)
    x2=M+cw+GUT
    y=panel(sp,x2,3.24,cw,4.30,"Architectural GFC Release",NAVY)
    milestone_rows(sp,x2+0.24,y+0.16,cw-0.48,
        [("Basement 03","22 Sep","Scheduled","n"),("Basement 02","22 Sep","Scheduled","n"),
         ("Basement 01","29 Sep","Scheduled","n")],rh=0.54)
    text(tbox(sp,x2+0.24,y+1.90,cw-0.48,0.80),
         "B3 centre line issued 01 Jun\nB2 centre line issued 20 Jul",T_BODY,MUTED,line=1.25)
    x3=M+2*(cw+GUT)
    y=panel(sp,x3,3.24,cw,4.30,"MEPF GFC Release",NAVY)
    milestone_rows(sp,x3+0.24,y+0.16,cw-0.48,
        [("Basement 03","22 Sep","Scheduled","n"),("Basement 02","22 Sep","Scheduled","n"),
         ("Basement 01","29 Sep","Scheduled","n"),("Ground Floor","14 Oct","On plan","n")],rh=0.54)
    y=panel(sp,M,7.90,RIGHT-M,2.68,"Foundation GFC Release Note",TATA)
    bullets(sp,M+0.30,y+0.26,RIGHT-M-0.60,1.90,
        ["R0 issued 27 May 2026; optimised revision issued 20 August 2026.",
         "Structural GFC for Basement 03 released early against plan; Basement 02 tracking on plan for 31 August.",
         "Peer review approval is the gate for the remaining structural releases."])

# ═══════════════════════════════════════════════════ 8 · BIM Status
def s08(sp):
    title_block(sp,"BIM Status","Model maturity by block and discipline   ·   as on 31 Aug 2026")
    kpi_row(sp,1.62,[("Overall Model","83.4%","completion across all blocks",GREEN,GRNDK),
                     ("Highest","89%","3H Hotel · BOH",GREEN,GRNDK),
                     ("Lowest","75%","Retail 1 · Structure",AMBER,AMBDK),
                     ("Blocks Tracked","6","4 disciplines each",NAVY,DEEP)])
    marker(sp,M,3.24,"Model Completion by Block",TATA,"%")
    bar_chart(sp,M,3.70,13.60,6.00,
              ["Substructure","3H Hotel","4H Hotel","Retail 1","Retail 2","Convention"],
              [("Architecture",(84,83,82,86,86,83)),("Structure",(80,82,81,75,83,85)),
               ("MEPF",(82,86,84,83,86,86)),("BOH",(85,89,87,None,None,76))],
              (TATA,NAVY,TEAL,GREEN),"BIM",maxv=100,fmt='0"%"',cat_size=T_CAP,lbl_size=14,
              gap=48,label_all=True,label_pos=LP.INSIDE_END,plot=(0.11,0.02,0.87,0.96))
    ly=9.90
    for i,(lab,c) in enumerate((("Architecture",TATA),("Structure",NAVY),("MEPF",TEAL),("BOH",GREEN))):
        lx=M+i*2.4
        box(sp,lx,ly+0.05,0.22,0.13,fill=c,line=RULE,lw=0.5)
        text(tbox(sp,lx+0.32,ly,2.0,0.24),lab,T_CAP,MUTED,caps=True,space=0.8)
    RX,RW=14.60,4.80
    y=panel(sp,RX,3.24,RW,2.60,"Read-Out",NAVY)
    bullets(sp,RX+0.26,y+0.24,RW-0.52,1.80,
            ["Maturity is consistently","above 80% across the","estate, with two","exceptions."])
    y=panel(sp,RX,6.10,RW,2.10,"Below Threshold",AMBER)
    rows(sp,RX+0.26,y+0.20,RW-0.52,[("Retail 1 · Structure","75%"),("Convention · BOH","76%")],rh=0.56)
    y=panel(sp,RX,8.44,RW,2.14,"Action",TATA)
    bullets(sp,RX+0.26,y+0.22,RW-0.52,1.50,
            ["Close Retail 1 structural","model gap ahead of the","GFC release window."])

# ═══════════════════════════════════════════════════ 9 · BIM Clash Report
def s09(sp):
    title_block(sp,"BIM Clash Report","Clash inventory and interface hotspots   ·   as on 31 Aug 2026")
    kpi_row(sp,1.62,[("17 Aug","15,297","total clashes",NAVY,DEEP),
                     ("24 Aug","34,845","peak inventory",RED,REDDK),
                     ("27 Aug","17,400","total clashes",GREEN,GRNDK),
                     ("Reduction","−50%","17,445 clashes closed",GREEN,GRNDK)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Clash Trend",TATA)
    bar_chart(sp,LX,3.72,LW,3.00,["17 Aug","24 Aug","27 Aug"],
              [("Total Clashes",(15297,34845,17400))],(TATA,),"Clash",maxv=40000,
              horizontal=False,cat_size=T_CAP,lbl_size=T_CAP,gap=90,
              label_pos=LP.OUTSIDE_END,plot=(0.06,0.12,0.90,0.76))
    y=panel(sp,LX,7.00,LW,3.58,"Trend Read-Out",NAVY)
    bullets(sp,LX+0.28,y+0.26,LW-0.56,2.60,
            ["Clash count peaked at 34,845 on 24 August following the",
             "federated model refresh.",
             "",
             "Peak-to-current reduction of 17,445 clashes — a 50% cut in",
             "three days through targeted MEPF coordination."])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"27 Aug Hotspots",GREEN,"by interface")
    bar_chart(sp,RX,3.72,RW,4.50,
              ["MEPF vs AR","LA vs MEPF","MEPF vs ST","AR vs ST","LA vs ST","LA vs LA"],
              [("Count",(5131,2233,1957,1576,1339,1073))],(TATA,),"Clash",maxv=6200,
              cat_size=T_CAP,lbl_size=T_CAP,gap=60,label_pos=LP.OUTSIDE_END,
              plot=(0.19,0.02,0.79,0.96))
    y=panel(sp,RX,8.48,RW,2.10,"Concentration",AMBER)
    bullets(sp,RX+0.28,y+0.24,RW-0.56,1.40,
            ["The top three interfaces account for 54% of the 27 August clash inventory.",
             "MEPF versus Architecture alone represents 29%."])

# ═══════════════════════════════════════════════════ 10 · MEP NSC Packages
def s10(sp):
    title_block(sp,"MEP NSC Packages","Release status and forward pipeline   ·   September 2026")
    kpi_row(sp,1.62,[("Total Packages","17","in the NSC scope",NAVY,DEEP),
                     ("Initial Submission","6","completed",GREEN,GRNDK),
                     ("Due by 15 Sep","5","immediate window",AMBER,AMBDK),
                     ("Forward Pipeline","6","20 Sep – 20 Oct",TATA,DEEP)])
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
    y=panel(sp,x3,3.24,cw,5.10,"Forward Pipeline",TATA)
    milestone_rows(sp,x3+0.24,y+0.18,cw-0.48,
        [("HVAC Low Side","20 Sep","",'n'),("Electrical Low Side","20 Sep","",'n'),
         ("HT & LT Cables","20 Sep","",'n'),("Bus Ducts","25 Sep","",'n'),
         ("LT Panels","30 Sep","",'n'),("ELV Systems","20 Oct","",'n')],rh=0.62)
    y=panel(sp,M,8.70,RIGHT-M,1.88,"Next Deliveries",NAVY)
    bullets(sp,M+0.30,y+0.26,RIGHT-M-0.60,1.10,
            ["Close PHE, Fire Fighting and UPS by 05 September 2026 to hold the September release window."])

# ═══════════════════════════════════════════════════ 11 · Procurement
def s11(sp):
    title_block(sp,"Procurement Dashboard","Package status, formwork and material milestones   ·   August 2026")
    kpi_row(sp,1.62,[("Civil","ON TRACK","rebar vendor by 15 Sep",GREEN,GRNDK),
                     ("MEP","WATCHLIST","LPS onboarded · NSC open",AMBER,AMBDK),
                     ("Façade & ID","CRITICAL","ID and tender pending",RED,REDDK),
                     ("Formwork at Site","1,500 m²","column, wall and footing",NAVY,DEEP)])
    LX,LW=M,11.60
    marker(sp,LX,3.24,"Formwork Procurement",TATA,"m²")
    y=panel(sp,LX,3.70,LW,3.10,"Column / Shear Wall / Footing",NAVY)
    milestone_rows(sp,LX+0.28,y+0.20,LW-0.56,
        [("1,500 m² at site","03 Sep","Dispatch","g"),
         ("6,200 m² phased supply","15 Oct","Complete","n")],rh=0.62)
    text(tbox(sp,LX+0.28,y+1.60,LW-0.56,0.60),
         "Full column and shear-wall formwork dispatch completes 15 October 2026.",T_BODY,MUTED,line=1.25)
    y=panel(sp,LX,7.06,LW,3.52,"Slab Formwork",TATA)
    yy=y+0.24
    for lab,val,cap,col in (("Received","1,500 m²","at site",GREEN),
                            ("Committed","1,700 m²","by 20 Sep",AMBER),
                            ("Pipeline","10,000 m²","order by 11 Sep",TATA)):
        box(sp,LX+0.28,yy,0.09,0.72,fill=col)
        text(tbox(sp,LX+0.50,yy+0.04,3.2,0.26),lab,T_CAP,MUTED,caps=True,space=0.9)
        text(tbox(sp,LX+0.50,yy+0.32,3.2,0.34),val,T_MID,DEEP,bold=True)
        text(tbox(sp,LX+4.20,yy+0.24,3.0,0.28),cap,T_BODY,BODY)
        yy+=0.92
    RX,RW=12.80,6.60
    marker(sp,RX,3.24,"Material Milestones",GREEN)
    y=panel(sp,RX,3.70,RW,6.88,"September – October",NAVY)
    milestone_rows(sp,RX+0.26,y+0.22,RW-0.52,
        [("30 MT PT strand","05 Sep","",'n'),
         ("3,000 MT reinforcement steel","Sep","",'n'),
         ("Slab-formwork order","11 Sep","",'n'),
         ("1,700 m² slab formwork","20 Sep","",'n'),
         ("Full formwork dispatch","15 Oct","",'n')],rh=0.86)
    text(tbox(sp,RX+0.26,y+4.70,RW-0.52,1.40),
         "ID package not issued and the Façade tender remains pending — both sit on the critical path.",
         T_BODY,REDDK,line=1.28)

# ═══════════════════════════════════════════════════ 12 · Construction
def s12(sp):
    title_block(sp,"Construction Dashboard","Physical progress and constraints   ·   August 2026")
    kpi_row(sp,1.62,[("Month Concrete","3,025 m³","against 5,584 m³ plan",AMBER,AMBDK),
                     ("Workmen","1,032","against 1,000 plan",GREEN,GRNDK),
                     ("Staff","142","deployed on site",NAVY,DEEP),
                     ("Foundations","62 of 147","across three blocks",AMBER,AMBDK)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Area-Wise Foundations",TATA)
    for i,(lab,val,scale,col) in enumerate([("4-H Hotel",39,46,GREEN),("3-H Hotel",15,51,AMBER),
                                            ("Convention Centre",8,50,RED)]):
        rail_chart(sp,LX,3.72+i*0.86,LW,lab,val,scale,col,"#,##0","Constr",
                   sub_=f"of {scale} foundations")
    text(tbox(sp,LX,6.34,LW,0.28),"Retail 1 / 2 — awaiting handover",T_BODY,MUTED)
    y=panel(sp,LX,6.82,LW,3.76,"Milestones Achieved",GREEN)
    bullets(sp,LX+0.28,y+0.26,LW-0.56,2.70,
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
    y=panel(sp,RX,7.08,RW,3.50,"Recovery Actions",GREEN)
    bullets(sp,RX+0.28,y+0.24,RW-0.56,2.60,
            ["Resequence around available handovers",
             "Deploy alternate RMC source for mass concrete pours",
             "Progress on available GFC and sustain manpower",
             "Engineering: PT drawings availability",
             "Construction: commence Retail blocks"])

# ═══════════════════════════════════════════════════ 13 · Mobilization
def s13(sp):
    title_block(sp,"Mobilization Dashboard","Manpower, camp delivery and plant   ·   August 2026")
    kpi_row(sp,1.62,[("Sept Manpower Plan","1,205","+173 net augmentation",TATA,DEEP),
                     ("Currently Available","1,032","workmen on site",GREEN,GRNDK),
                     ("Tower Cranes","03 / 05","1 installed",AMBER,AMBDK),
                     ("Workmen Sheds","5 × G+2","all erected by 31 Oct",NAVY,DEEP)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Workmen Camp Delivery",TATA,"G+2 sheds")
    y=panel(sp,LX,3.72,LW,3.52,"Shed Programme",NAVY)
    milestone_rows(sp,LX+0.28,y+0.20,LW-0.56,
        [("C1","22 Aug","Occupied","g"),("B1","18 Sep","Erection","a"),
         ("A1","04 Oct","Plinth done","a"),("C2","06 Oct","Plinth done","a"),
         ("B2","31 Oct","WO issued","n")],rh=0.54)
    marker(sp,LX,7.50,"Manpower",GREEN)
    bar_chart(sp,LX,7.96,LW,2.60,["Available","Sept Plan"],
              [("Workmen",(1032,1205))],(TATA,),"Manpower",maxv=1500,
              cat_size=T_CAP,lbl_size=T_CAP,gap=70,label_pos=LP.INSIDE_END,
              plot=(0.13,0.04,0.85,0.92))
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Camp Amenities & Services",GREEN)
    y=panel(sp,RX,3.72,RW,4.30,"Delivery Status",NAVY)
    milestone_rows(sp,RX+0.28,y+0.20,RW-0.56,
        [("Kitchen 1","—","Completed","g"),("Cement Store","—","Completed","g"),
         ("Toilets (220)","—","20 done","a"),("Bath Sheds","13 Sep","Scheduled","n"),
         ("Kitchen 2","10 Sep","Scheduled","n"),("Dining 2 / Store","15 Sep","Scheduled","n"),
         ("Drain","26 Sep","Scheduled","n")],rh=0.52)
    y=panel(sp,RX,8.28,RW,2.30,"Plant & Machinery Mobilization",TATA)
    rows(sp,RX+0.28,y+0.22,RW-0.56,
         [("DG Sets","04 / 04"),("Trailer","02 / 02"),("Vibro Roller","01 / 01")],rh=0.46)

# ═══════════════════════════════════════════════════ 14–16 · MOM tracker
MOM_COLW=[0.7,2.4,6.6,2.9,1.9,4.0]
MOM_HDR=["Sr.","Point Discussed","Discussion / Observation","Action By","Target Date","TPL Update"]

def mom_slide(sp, n, rowsd, title="Update on Last MOM"):
    title_block(sp,title,f"Minutes of meeting tracker   ·   page {n} of 3")
    avail=BODY_BOT-BODY_TOP-0.50
    per=avail/max(1,len(rowsd))
    table(sp,M,BODY_TOP,RIGHT-M,MOM_HDR,rowsd,MOM_COLW,rh=per,hh=0.50,
          cell=T_TBLC,hdr=T_TBLH)

# ═══════════════════════════════════════════════════ 17 · September Plan
def s17(sp):
    title_block(sp,"September 2026 Plan","Planned value, quantities and weekly distribution")
    kpi_row(sp,1.62,[("Total Planned Value","₹37.5 Cr","September 2026",NAVY,DEEP),
                     ("Supply","₹24.0 Cr","64% of plan",TATA,DEEP),
                     ("Service","₹12.5 Cr","33% of plan",TEAL,DEEP),
                     ("Design","₹1.0 Cr","3% of plan",NAVY,DEEP)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Major Items",TATA,"₹ Cr")
    y=panel(sp,LX,3.72,LW,4.10,"Value Breakdown",NAVY)
    rows(sp,LX+0.28,y+0.22,LW-0.56,
         [("Reinforcement Supply","₹17.2 Cr"),("Reinforcement Service","₹8.0 Cr"),
          ("M40 Supply","₹6.2 Cr"),("M40 Service","₹3.8 Cr"),
          ("Design Review","₹1.0 Cr"),("Other Activities","₹1.3 Cr")],rh=0.56)
    marker(sp,LX,8.04,"Value Mix",GREEN)
    bar_chart(sp,LX,8.50,LW,2.08,["Supply","Service","Design"],
              [("₹ Cr",(24.0,12.5,1.0))],(TATA,),"SeptPlan",maxv=30,fmt='0.0',
              cat_size=T_CAP,lbl_size=T_CAP,gap=60,label_pos=LP.OUTSIDE_END,
              plot=(0.13,0.02,0.82,0.96))
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Weekly Distribution",TATA)
    y=panel(sp,RX,3.72,RW,3.40,"M40 Concrete and Reinforcement",NAVY)
    hdr=["Week","M40 (m³)","Rebar (MT)"]
    table(sp,RX+0.26,y+0.20,RW-0.52,hdr,
          [["W1","1,943","750"],["W2","2,553","750"],["W3","1,946","500"],["W4","3,584","1,000"]],
          [1.2,2.0,2.0],rh=0.52,hh=0.44,
          aligns=[PP_ALIGN.LEFT,PP_ALIGN.RIGHT,PP_ALIGN.RIGHT])
    y=panel(sp,RX,7.38,RW,3.20,"Critical Quantities",TATA)
    rows(sp,RX+0.28,y+0.22,RW-0.56,
         [("M40 Supply","10,344 m³"),("M40 Service","10,344 m³"),
          ("Reinforcement","3,000 MT"),("M10 Supply + Service","405 m³")],rh=0.58)

# ═══════════════════════════════════════════════════ 19 · Compliance
def s19(sp):
    title_block(sp,"Statutory Compliance","Closure path and open positions   ·   August 2026")
    kpi_row(sp,1.62,[("Open Positions","3","of 4 tracked items",AMBER,AMBDK),
                     ("Closed","1","policy amendment",GREEN,GRNDK),
                     ("Client Input Pending","PENDING","BG amendment · 21 Aug 2026",RED,REDDK),
                     ("Next Milestone","05 SEP","BOCW receipt expected",TATA,DEEP)])
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
        x=M+i*(cw+GUT)
        strip={'g':GREEN,'a':AMBER,'r':RED,'n':NAVY}[kind]
        box(sp,x,3.70,cw,6.88,fill=WHITE,line=RULE)
        box(sp,x,3.70,cw,0.42,fill=strip)
        text(tbox(sp,x+0.20,3.805,cw-0.40,0.24),f"ITEM {num}",T_CARD,WHITE,bold=True,caps=True,space=1.2)
        text(tbox(sp,x+0.24,4.32,cw-0.48,0.96),name,T_MID,DEEP,bold=True,line=1.12)
        chip(sp,x+0.24,5.38,cw-0.48,0.38,status,kind)
        bullets(sp,x+0.24,5.98,cw-0.48,4.20,lines,size=T_BODY)

# ═══════════════════════════════════════════════════ 20 · EHS
def s20(sp):
    title_block(sp,"EHS Performance","Zero Harm   ·   August 2026")
    kpi_row(sp,1.62,[("Safe Man-Hours FTM","1,27,954","August 2026",GREEN,GRNDK),
                     ("Safe Man-Hours ITD","3,44,498","inception to date",GREEN,GRNDK),
                     ("Fatalities & LTI","0","zero lagging incidents",GREEN,GRNDK),
                     ("Near Misses","4","high-potential incidents",AMBER,AMBDK)])
    LX,LW=M,11.60
    marker(sp,LX,3.24,"Leading Indicators",TATA,"activity counts · FTM vs ITD")
    bar_chart(sp,LX,3.70,LW,5.10,
              ["Inductions","Safety Observations","Tool Box Talks","Training Sessions"],
              [("FTM",(585,122,265,35)),("ITD",(1691,781,615,109))],
              (TATA,NAVY),"EHS",maxv=1900,fmt='#,##0',cat_size=T_CAP,lbl_size=15,gap=55,
              label_all=True,label_pos=LP.OUTSIDE_END,plot=(0.17,0.02,0.74,0.96))
    ly=8.94
    for i,(lab,c) in enumerate((("For the Month (FTM)",TATA),("Inception to Date (ITD)",NAVY))):
        lx=LX+i*3.6
        box(sp,lx,ly+0.05,0.22,0.13,fill=c,line=RULE,lw=0.5)
        text(tbox(sp,lx+0.32,ly,3.2,0.24),lab,T_CAP,MUTED,caps=True,space=0.8)
    y=panel(sp,LX,9.38,LW,1.20,"Note",NAVY)
    text(tbox(sp,LX+0.28,y+0.18,LW-0.56,0.50),
         "Safe man-hours are reported in the header cards; this chart shows activity counts.",
         T_CAP,MUTED)
    RX,RW=12.80,6.60
    marker(sp,RX,3.24,"Lagging Indicators",GREEN)
    y=panel(sp,RX,3.70,RW,3.90,"Zero Harm Achieved",GREEN)
    for i,(lab,val) in enumerate([("Fatalities & Lost Time Injuries","0"),
                                  ("Restricted Work & Medical Treatment","0"),
                                  ("High-Potential Incidents & Near Misses","4")]):
        yy=y+0.24+i*1.10
        text(tbox(sp,RX+0.28,yy,RW-1.60,0.60),lab,T_BODY,BODY,line=1.2)
        t=tbox(sp,RX+RW-1.30,yy-0.06,1.00,0.50); t.text_frame.word_wrap=False
        text(t,val,T_BIG,GREEN if val=="0" else AMBER,bold=True,align=PP_ALIGN.RIGHT)
        if i<2: box(sp,RX+0.28,yy+0.90,RW-0.56,0.008,fill=RULE)
    y=panel(sp,RX,7.86,RW,2.72,"Commitment",TATA)
    bullets(sp,RX+0.28,y+0.26,RW-0.56,1.90,
            ["Zero incidents recorded across all","primary lagging parameters,","including fatalities and lost","time injuries."])

# ═══════════════════════════════════════════════════ 27 · Quality Indicators
def s27(sp):
    title_block(sp,"Quality Indicators","Leading and lagging quality performance   ·   August 2026")
    kpi_row(sp,1.62,[("First Time Right Index","88%","project outcome",GREEN,GRNDK),
                     ("Training Imparted","74","effort hours",TATA,DEEP),
                     ("Good / Best Practices","16","recorded this month",GREEN,GRNDK),
                     ("Deviation Closure TAT","19.9","days average",AMBER,AMBDK)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Leading Indicators",TATA,"proactive quality inputs")
    bar_chart(sp,LX,3.72,LW,4.10,
              ["Training Imparted","Good/Best Practices","Material Approvals",
               "Management Walkdown","Mockups"],
              [("Count",(74,16,12,9,5))],(TATA,),"QualityInd",maxv=92,
              cat_size=T_CAP,lbl_size=T_CAP,gap=55,label_pos=LP.OUTSIDE_END,
              plot=(0.30,0.02,0.68,0.96))
    y=panel(sp,LX,8.06,LW,2.52,"Read-Out",NAVY)
    bullets(sp,LX+0.28,y+0.24,LW-0.56,1.70,
            ["Proactive quality investment translates directly into",
             "near-perfect execution and zero-defect outcomes."])
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Lagging Indicators",GREEN,"actual project outcomes")
    bar_chart(sp,RX,3.72,RW,4.10,
              ["Obs. External","Obs. Internal","Rejection","Repetitive Dev.","Snag Issued","Stop Work"],
              [("Count",(32,15,1,0,0,0))],(NAVY,),"QualityInd",maxv=40,
              cat_size=T_CAP,lbl_size=T_CAP,gap=45,label_pos=LP.OUTSIDE_END,
              plot=(0.24,0.02,0.74,0.96))
    ring(sp,RX,8.10,2.20,0.88,GREEN,"Quality","First Time Right","88%")
    SX=RX+2.50
    rows(sp,SX,8.24,RW-2.50,[("Skill Ratio","0.60"),("Flash Report","0"),
                             ("Deviation Closure in TAT","19.9 days")],rh=0.62)

# ═══════════════════════════════════════════════════ 28 · Quality Performance
def s28(sp, images):
    title_block(sp,"Quality Performance","Observation and training closure   ·   August 2026")
    kpi_row(sp,1.62,[("Observations Closed","24","of 32 raised",GREEN,GRNDK),
                     ("Open Observations","8","under action",AMBER,AMBDK),
                     ("NCR Closed","103","of 123 raised",GREEN,GRNDK),
                     ("Trainings","44","450 man-hours",TATA,DEEP)])
    LX,LW=M,9.20
    marker(sp,LX,3.24,"Observation Closure",TATA)
    bar_chart(sp,LX,3.72,LW,2.60,["Closed","Open"],[("Observations",(24,8))],(GREEN,),
              "QualityInd",maxv=32,cat_size=T_CAP,lbl_size=T_CAP,gap=70,
              label_pos=LP.INSIDE_END,plot=(0.16,0.04,0.82,0.92))
    marker(sp,LX,6.60,"NCR Closure",GREEN)
    bar_chart(sp,LX,7.08,LW,2.60,["Closed","Open"],[("NCR",(103,20))],(TATA,),
              "QualityInd",maxv=130,cat_size=T_CAP,lbl_size=T_CAP,gap=70,
              label_pos=LP.INSIDE_END,plot=(0.16,0.04,0.82,0.92))
    RX,RW=10.40,9.00
    marker(sp,RX,3.24,"Training Delivered",TATA)
    y=panel(sp,RX,3.72,RW,3.10,"Cumulative",NAVY)
    rows(sp,RX+0.28,y+0.24,RW-0.56,
         [("Cumulative trainings","44"),("Cumulative man-hours","450.02")],rh=0.72,vsize=T_MID)
    y=panel(sp,RX,7.08,RW,3.50,"Note",TATA)
    bullets(sp,RX+0.28,y+0.26,RW-0.56,2.50,
            ["Source charts on this slide previously linked to an external",
             "SharePoint workbook and would not refresh outside the TPL",
             "tenant. They are now embedded and travel with the deck."])

# ═══════════════════════════════════════════════════ dividers
def divider(sp, title, subtitle=None):
    text(tbox(sp,2.50,4.60,15.00,1.10),title,56,NAVY,bold=True,align=PP_ALIGN.CENTER,wrap=False)
    box(sp,8.20,5.92,3.60,0.05,fill=TATA)
    if subtitle:
        text(tbox(sp,2.50,6.20,15.00,0.40),subtitle,T_SECT,MUTED,caps=True,space=1.4,
             align=PP_ALIGN.CENTER,wrap=False)
