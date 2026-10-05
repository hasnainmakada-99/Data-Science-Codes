# CSD-LKO Schedule Review: Full Record of the Work to Date

**Project:** City side development project at Choudhary Charan Singh International Airport, Lucknow
**Prepared for:** Planning Manager, Tata Projects
**Record date:** 5 Oct 2026
**Purpose:** One document that records everything discussed and produced so far: what you gave me, what I built, every finding, every correction I made to my own earlier statements, the decisions you made, and what is still open.

> **How to read this record.** Sections 1 to 3 list the inputs and outputs. Sections 4 to 11 are the findings, in the order the work happened. Section 12 is the list of corrections to my own earlier statements. Sections 13 to 15 are the requirements you set, the open points, and the plan. The appendix has the activity-by-activity tables for the reference building (Hotel 4 Star).
>
> **Convention.** "wd" means working days in each activity's own calendar (10-hour days unless noted). "Calendar days" means plain calendar days. Dates are dd Mon yyyy.

---

## 1. The situation you described

- You joined Tata Projects as **Planning Manager**. The baseline schedule had been submitted and approved by the previous manager.
- **No backup exists** for how that baseline was prepared: no sequencing logic, no activity-coding logic, no cost-loading backup. The client has no backup either.
- The client approved the initial baseline. Later the client asked for a **revamped (date-adjusted recovery) schedule**, which was submitted and is the schedule now in use.
- The client has asked you to **build a proper revised schedule with backups**. You had already sorted out the activity coding. What you could not understand was the **sequencing logic**: how the main WBS groups flow, and how the activities inside them are ordered.
- Later you updated the revamp schedule to **30 Sep 2026**. The client wants that update used as the data date for a **revised baseline**.

---

## 2. Files you gave me

| # | File | What it is | Key facts I extracted |
|---|---|---|---|
| 1 | `CSD-LKO-Org-BL.xer` (Desktop, 23.3 MB) | **Original approved baseline** | Project `CSD-LKO-WOP`. 13,446 activities, 22,563 relationships, 3,160 WBS nodes. Planned 14 Feb 2026 to 15 May 2029. No progress. No constraints. |
| 2 | `Assumptions for Schedule - For Review.docx` (Downloads, ~7 MB) | Assumptions narrative extracted from the server, titled **"Assumptions and Considerations-R0"** | Key dates, site handover dates, calendars, holidays, monsoon, cost bifurcation, sale values, progress weightages, productivity norms, pour plans (21 embedded images, not viewed) |
| 3 | `Assumptions for Schedule - R2.pdf` (Downloads, 22 pages) | **"Assumptions and Considerations for Baseline Schedule-R2"**, dated 21/05/26, Adani and Tata Projects logos | Same assumptions as R0, plus clearly labelled pour-plan drawings (read in full) |
| 4 | `CSD-LKO-Revamp-BL.xer` (Desktop, 23.1 MB) | **Recovery schedule** as submitted afterwards | Project `CSD-LKO-Adani`. Data date 31 Jul 2026. 13,441 activities, 22,598 relationships. 269 complete, 127 active. Completion still 15 May 2029. |
| 5 | `CSD-LKO-Revamp-30-Sep.xer` (Desktop, 23.1 MB) | **Your update to 30 Sep 2026** | Project `CSD-LKO-26-SEP-26`. Data date 30 Sep 2026. 13,441 activities, 22,658 relationships. 385 complete, 194 active. Forecast completion **7 Jun 2029**. |

I opened all of these read-only. **I have not modified any file you gave me.**

---

## 3. Files I prepared

All of these are in the folder the app made for this session.

| File | What it is |
|---|---|
| `CSD-LKO_Baseline_Logic_Flowchart.html` | First deliverable: three static diagrams (project-level WBS flow, design-to-handover per building, design workflow chain), a link-count table and baseline-health notes. Built from the baseline XER. |
| `CSD-LKO_Construction_Logic_Explorer.html` | Interactive explorer for all 11,801 Construction activities. Tree of WBS on the left; for any node it draws an activity-level flowchart (up to 700 activities) or a group summary (larger nodes). Click an activity for predecessors and successors. Search. **Export logic CSV** per node. Durations corrected to each activity's own calendar. Single file, works offline. |
| `CSD-LKO_Construction_Logic_Narrative.html` | The detailed narrative: 8 sections, 24 reference blocks (A to X) with 28 diagrams and activity-by-activity tables in plain English. Section 8 is the cross-check against the assumptions document. Generated from the XER. |
| `CSD-LKO_Conversation_Record.md` | **This file.** |

I also ran many analysis scripts (Python, standard library only) in a temporary folder. They are not deliverables and are not kept after the session. Section 16 describes the methods so the results can be reproduced.

---

## 4. The original baseline: structure

### 4.1 Size and contents

- One project, `CSD-LKO-WOP`, titled "CSD-LKO_Baseline Original (Does not contain progress)".
- **13,446 activities:** 13,341 tasks, 68 finish milestones, 37 start milestones. All "Not Started".
- **22,563 relationships:** FS 21,992 (97.5%), FF 438 (1.9%), SS 133 (0.6%). **231 have lags** (1.0%). **No negative lags.**
- **No constraints on any activity.** All dates come from logic, durations and calendars.
- 3,160 WBS nodes, 77 resources, 49,232 resource assignments (every task is resourced).
- Planned start 14 Feb 2026. Project Completion milestone 15 May 2029, with **zero float**.
- Calendars: `global calender` (12 h); `6*8 with NGT and holiday` (8 h); `CSD-LKO Calender (6 day + Holiday + Monsoon)` (10 h, 7,193 tasks); `CSD-LKO Calender (6 day + Holiday)` (10 h, 5,077 tasks); `CSD-LKO-Design (5 Day + Holiday)` (10 h, 1,174 tasks); `DFCPL` (10 h); a second monsoon calendar (2 tasks).

### 4.2 The six main WBS groups

| WBS group | Activities | Sub-groups (activities) |
|---|---|---|
| Milestones | 103 | Key Milestones 10; Site Handover By Client 5; Design 15; Construction 68; Handovers of Buildings 5 |
| Mobilization | 54 | Site Office Setup 8; Workforce Camp 9; Plant & Machinary 37 |
| Procurement | 267 | Key Vendor Mobilisation 231; Delivery of Critical Items 36 |
| Design & Drawings | 1,167 | Consultant Onboarding 16; Concept Design 14; Schematic Design 39; Detail Design 120; Tender (Revised BOQ) 13; GFCs 834; Shop Drawings 96; As Built Drawings 35 |
| Mockups | 54 | Civil work 2; MEP Work 10; ID Work 30; Misc 8; Facade 4 |
| Construction | 11,801 (88%) | Hotel 4 Star 2,378; Hotel 3 Star 2,239; Retail Block 2 2,079; Retail Block 1 1,814; Convention Center 1,962; Bridge Between RB1 & RB2 35; Common Basements MEP & Finishes 1,221; Structural Steel Fabrication 3; Infra Works 10; External Development/Landscape 23; Misc 3; Project Closure 34 |

### 4.3 How the six groups connect (relationship counts, predecessor group to successor group)

| From | To | Links | Types |
|---|---|---|---|
| Construction | Construction | 19,050 | FS 18,752, FF 216, SS 82 |
| Design & Drawings | Design & Drawings | 1,251 | FS 1,231, FF 8, SS 12 |
| Design & Drawings | Construction | 770 | FS |
| Construction | Milestones | 378 | FS 235, FF 114, SS 29 |
| Procurement | Procurement | 223 | FS 222, FF 1 |
| Procurement | Construction | 114 | FS 112, FF 1, SS 1 |
| Design & Drawings | Procurement | 114 | FS 113, FF 1 |
| Design & Drawings | Milestones | 104 | FS 33, FF 71 |
| Construction | Design & Drawings | 102 | FS |
| Milestones | Design & Drawings | 84 | FS |
| Milestones | Procurement | 69 | FS |
| Mockups | Mockups | 50 | FS |
| Mobilization | Mobilization | 44 | FS 39, FF 4, SS 1 |
| Milestones | Mobilization | 33 | FS |
| Procurement | Design & Drawings | 28 | FS |
| Design & Drawings | Mockups | 26 | FS |
| Mobilization | Milestones | 26 | FS |
| Milestones | Construction | 23 | FS 7, FF 15, SS 1 |
| Milestones | Milestones | 22 | FS 17, FF 5 |
| Construction | Procurement | 18 | FS |
| Mockups / Procurement | each other | 10 each way | FS |
| Mobilization | Construction | 8 | FS 1, SS 7 |
| Mockups | Design & Drawings | 6 | FS 4, FF 2 |

**Reading:** Design & Drawings releases Construction (770 links) and Procurement (114). Procurement feeds Construction (114). Milestones act as gates that start Mobilization, Design and Procurement activities and collect finishes back from Construction (378), Design (104) and Mobilization (26). Almost all Construction links stay inside a building: each building is its own chain.

### 4.3a Early observations at the design level

- Key Milestones gate the start of consultant onboarding, schematic and detail design.
- The design chain is: Consultant Onboarding, Concept Design, Schematic Design, Detail Design, GFCs, Shop Drawings. Detail Design also drives the Tender (Revised BOQ) block. Link counts between these blocks: Consultant to Concept 14, Concept to Schematic 33, Schematic to Detail 34, Detail to GFCs 139, GFCs to Shop Drawings 37.
- GFCs release each building's construction: GFCs to Hotel 3 Star 190 links, Hotel 4 Star 184, Retail Block 2 146, Convention Center 115, Retail Block 1 108.
- Each building drives its handover milestone: Hotel 3 Star 50, Hotel 4 Star 45, Retail Block 2 22, Convention Center 19, Retail Block 1 16. The handover milestones drive Project Closure by 15 Finish-to-Finish links.

### 4.4 Structure of each building

Every building has the same sections: **Substructure, Superstructure, Wet finishes/MEP/ID, Structural Steel works for Facade, Facade, Terrace Works, Vertical Transport, Testing/Commissioning/HO** (Hotel 4 Star also has a Swimming Pool).

| Building | Activities | Substructure | Structure floors | Pours per floor (bottom to top) | Finishes/MEP | Facade |
|---|---|---|---|---|---|---|
| Hotel 4 Star | 2,378 | 485 | 8 | 5, 4, 3, 3, 3, 3, 3, 3 | 949 | 88 |
| Hotel 3 Star | 2,239 | 347 | 9 | 3, 3, 2, 2, 2, 2, 2, 2, 2 | 1,091 | 100 |
| Retail Block 2 | 2,079 | 663 | 7 | 5, 5, 5, 5, 5, 5, 5 | 553 | 64 |
| Retail Block 1 | 1,814 | 694 | 5 | 3, 3, 3, 3, 4 | 395 | 40 |
| Convention Center | 1,962 | 694 | 6 | 3, 3, 4, 3, 4, 4 | 478 | 40 |

Substructure pour counts: Hotel 4 Star 4 (Foundation, Grade Slab, Basements 03, 02, 01); Hotel 3 Star 3 for Foundation and 2 for the rest; Retail Block 2 has 6; Retail Block 1 and Convention Center have 7.

Convention Center floor names are Ground Floor, First Mezzanine, Second Mezzanine, First Floor, Third Mezzanine, Second Floor.

### 4.5 Hotel 4 Star in detail

- Substructure: Foundation 131 activities (4 pours); Basement 03 Grade Slab 24; Basement 03 104; Basement 02 84; Basement 01 142.
- Superstructure: Ground Floor 156; First Floor 140; Service Floor, Second to Sixth Floor 84 each; Roof Top 7.
- Wet finishes/MEP/ID: Ground Floor 83; First Floor 79; Service Floor 77; Second to Sixth Floor 142 each.
- Facade zones (12 activities each): GF to Service Floor; Second to Third; Third to Fourth; Fourth to Fifth; Fifth to Sixth; Sixth to Terrace; Above Terrace (16).
- Testing, Commissioning, HO: 3 activities per floor.
- Common Basements MEP & Finishes (shared): Basement 03 405, Basement 02 396, Basement 01 417, each with a block for every building plus "High Side MEP"; Testing/Commissioning/HO 3.

---

## 5. The sequencing rules I found in the baseline

I tested each rule by script across all five buildings. I did not read all 13,446 activities by hand.

### 5.1 Foundation and substructure

1. Foundation Pour 1's first activity (Pocket Excavation) waits for **three things**: the Project Commencement milestone, the site office setup (Mobilization), and the foundation GFC drawing release. Termite treatment, waterproofing and approved concrete mix designs also wait for their vendor or approval activities.
2. A footing group follows a fixed order: Pocket Excavation, Surface dressing, ATT (anti-termite treatment), PCC, Shuttering (and Blockwork), Waterproofing, Reinforcement, Concrete.
3. Foundation then feeds Basement 03 (24 links in Hotel 4 Star), Basement 03 feeds Basement 02 (8 links), Basement 02 feeds Basement 01 (11 links), each **pour to the same pour**.
4. Basement 01 slab concrete feeds the **Basement 03 grade slab** deshuttering (4 links). This is an unusual order. It is flagged for confirmation with site.

### 5.2 Superstructure

- **Rule 1, pour by pour.** A pour on a floor starts only after the **slab concrete of the same pour on the structure below**, and after the **GFC "Issue of Hard Copy on Site"** drawing activity for that floor. Slab PT work also waits for the PT work of the pour below.
- **Rule 2.** Because the link is only "slab below is cast", each pour column rises independently of the others. By logic alone, Pour 1 could be several floors up while Pour 3 is still lower. In practice crews and resources would limit this.
- Floor-to-floor links in Hotel 4 Star: Ground to First 12, First to Service 11, Service to Second 10, then 10 per floor up to the Sixth Floor, which feeds the Roof Top with 3.
- Where the first floor starts: Ground Floor Pour 1 (5 pours) starts after Basement 01 Pour 1 slab concrete; Pours 3, 4 and 5 start after Basement 01 Pour 3 slab.
- Verified in all five buildings: every pour of every floor is fed by slab concrete below, with the exceptions in section 10.

### 5.3 The pour cycle (Hotel 4 Star, Ground Floor Pour 2 is the reference)

- **Column and wall:** Reinforcement, Shuttering, LPS (lightning protection), Concrete. A second lift repeats it where the columns have two lifts.
- **Staircase core:** built flight by flight beside the wall: Reinforcement, Shuttering and Casting of the wall up to flight N; Reinforcement, Shuttering and Casting of the stair; MEP coordination up to flight N. Then the next flight.
- **Slab:** Shuttering, Reinforcement Bottom Net with chairs, Laying of PT Tendon, Reinforcement Top Net, MEP Coordination, Concrete of Slab, **Wait for Strength Gain (6 wd)**, PT Work (4 wd).
- Some pours have **no staircase** (for example Ground Floor Pour 4 has columns in two lifts and a slab only).

### 5.4 Finishes, MEP and ID

- **Start trigger.** Floor N finishes start when the **slab above floor N is cast**, which is the last pour of the next structure floor (or the Roof Top slab for the top floor). Examples: Hotel 4 Star Ground Floor finishes wait for First Floor Pours 3 and 4; Second Floor finishes wait for Third Floor Pour 3; Sixth Floor finishes wait for the Roof Top slab. Hotel 3 Star uses Pour 2, Retail Block 2 uses Pour 4, Retail Block 1 uses Pour 3 (with one exception), Convention Center uses Pour 3.
- They also wait for the architectural and MEP GFC drawings (about 20 links per floor).
- **Order inside a floor (Second Floor, 142 activities):** Deshuttering, Brickwork/Blockwork, then the MEP first fix in parallel (slab and wall conduiting, pipe supports, duct supports, drainage and water supply), Waterproofing of toilets, Plaster, then risers, testing, ceilings, flooring, doors and windows, putty and paint, then fixtures.
- **Five MEP trades** each run first fix, second fix, final fix: HVAC, Electrical, Plumbing, Firefighting, ELV.
- Each floor has **three faces** (Front, Back, Side). Interior wall finish ID works wait for the facade of that face and for the step **"Running of Wild Air"**, which also waits for the HVAC second fix.
- **There are zero floor-to-floor links inside the finishes** in any building. The only trigger is the structure above.

### 5.5 Facade

- The facade is built **zone by zone, not floor by floor with the structure.** It starts only after the top structure is nearly done, via a finish-to-finish link with a lag (for example Sixth Floor Pour 3 PT Work to the first facade zone, +8.75 wd).
- Each zone and face runs: Integration of Services Before Facade, Fixing of Facade Support, Fixing of Facade, Integration of Services After Facade. Faces overlap with SS +2.5 wd lags (75 such links in the baseline).
- Zones chain to each other (for example Second-Third to Third-Fourth 6 links, to GF-Service 4 links).
- **Structural Steel works for Facade** is a separate six-activity chain, one zone per activity (35 days each in Hotel 4 Star), run **strictly one after another**, triggered by the structure and by Structural Steel Fabrication.
- Long lags exist on facade steel: SS +112.5 and +75 days from a fabrication activity, FF +37.5 and +18.75 days.

### 5.6 Terrace, pool, lifts, testing, handover

- **Terrace Works:** Waterproofing (after the Roof Top slab), Flooring, Installation of Fans/Solar/MEP equipment.
- **Vertical Transport:** Wait for Strength Gain after the Roof Top slab, Deshuttering, Plaster, Installation of Lift (after the lift vendor), Testing and Commissioning.
- **Swimming Pool (Hotel 4 Star only):** Pump Room (after the basement High Side MEP), Balancing Tank, plumbing connections, Waterproofing, Tiling, Landscape.
- **Testing and handover, per floor, in sequence:** Testing and Commissioning (45 wd, waits for all final-fix MEP of the floor), then Snagging and Desnagging (45 wd, waits for testing and all dry finishes), then Handing Over (1 wd). The building handover milestone collects the floors. In Hotel 4 Star, testing also has a finish-to-finish link from the swimming pool, which looks like a stray link.

### 5.7 Common basements, bridge, and the small WBS

- **Common Basements MEP & Finishes** is finished area by area, one block under each building, after the grade slab concrete (for example `4S-SS-GS125`), and after design and vendor releases. The **High Side MEP** blocks (pumps, STP, ETP, pedestals) feed the other basement blocks.
- **Structural Steel Fabrication** (3 activities) feeds Convention Center steel erection and the facade steel of every building.
- **Infra Works** (sewage, water, fire hydrant network, HT/LT cables) wait for the building facades at ground level, and release landscape and statutory approvals.
- **External Development/Landscape** follows infra and the facades, and feeds as-built drawings and the Project Completion milestone.
- **Project Closure** (statutory approvals, 34 activities) follows building handovers (15 FF links) and infra, and feeds Project Completion.
- **Bridge Between Retail Block 1 and 2:** its steel erection waits for the PT work of the retail-block slabs it connects to and, on the ground floor, for steel fabrication.

### 5.8 Milestones in the baseline (selected)

LOI 14 Feb 2026; Project Commencement 16 Apr 2026; 4 Star substructure start 16 Apr 2026; 3 Star 16 May; Retail Block 1 and Convention Center 16 Jun; Retail Block 2 16 Jul; Completion of Mobilisation 3 Sep 2026; latest Wet Works and Structural Steel completion milestones 15 Mar 2028; Project Completion 15 May 2029.

### 5.9 Baseline quality (DCMA 14-point style checks)

| Check | Result |
|---|---|
| Loops | none |
| Missing predecessor | 1 (Issue of LOI) |
| Missing successor | 79, all milestones |
| Negative lags | 0 |
| Lags | 231 (1.0%) |
| Relationship types | FS 97.5%, FF 1.9%, SS 0.6% |
| Hard constraints | 0 |
| Float over 44 wd (tasks) | 7,393 (55%) |
| Negative float | 0 |
| Zero float | 202 (196 Construction, mostly Convention Center 193; 6 milestones) |
| Duration over 44 wd | 473 (3.5%) |
| Duplicate predecessor-successor pairs | 23 |
| Tasks with no resources | 0 |
| Critical path connected to completion | yes |

### 5.10 Exceptions and unusual items (baseline)

- **Convention Center.** On Second Mezzanine and Third Mezzanine, Pour 4 starts with **structural steel erection** (linked to earlier pours) instead of slab concrete from below. On First Floor and Second Mezzanine, the pours have **no GFC gate**. The critical path runs almost entirely through the Convention Center (193 of the 196 critical construction activities).
- **Retail Block 1.** Third Floor finishes are gated on Fourth Floor **Pour 2**, not the last pour as in the other floors.
- **Basement 03 grade slab** deshuttering waits for the Basement 01 slab (see 5.1).
- **Finishing floors have no links to each other** (zero floor-to-floor links), which creates large float.
- **Long lags** (112.5 d, 75 d, 186.25 d) are undocumented. They probably stand for vendor lead times.
- **Names to confirm with site:** "Running of Wild Air" (the assumptions document shows it is an HVAC item with 0% cost that gates ID finishes), and "Slab Conduiting" after deshuttering.

---

## 6. The assumptions documents (R0 and R2)

### 6.1 Key dates

- Receipt of LOI: 13 Feb 2026. Effective Date/NTP: 14 Feb 2026.
- Project Commencement Date: 16 Apr 2026.
- **Core & Shell Completion: 15 Mar 2028 (as per contract).**
- **Project Completion: 15 May 2029 (as per contract).**

### 6.2 Assumptions 1 to 13 (numbered as in R2)

1. Site handover dates: Hotel 4 Star 16 Apr 2026; Hotel 3 Star 16 May 2026; Retail Block 1 16 Jun 2026; Convention Centre 16 Jun 2026; Retail Block 2 16 Jul 2026.
2. Site is handed over after retaining structure and mass excavation (up to footing top).
3. Site and access shall be free from encumbrances as per the timelines.
4. NSC scope is incorporated considering standard activities and might change; final dates will not change due to changes in detail information.
5. GFC dates for Architecture, Structure and MEPF drawings are based on dates given by the Design team.
6. ID design date will be finalised after consultant onboarding.
7. **Superstructure ID finishes will start after completion of facade and "running of wild air".**
8. Pours may change based on PT vendor drawings, without extending the floor duration.
9. Calendar: 6 days (Monday to Saturday), 10 working hours.
10. Holidays (13 listed, table below).
11. Monsoon considerations: 2026: 2 days/week in July, 3 days/week in August, 2 days/week in September. 2027: 2, 2 and 1. 2028: 1, 1 and 1.
12. Internal works not impacted by monsoon use a 6-day calendar with holidays and no monsoon.
13. Design works use a 5-day calendar with the same holidays.

**Holidays considered:**

| Holiday | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| New Year Day | | 01-Jan-27 | 01-Jan-28 | 01-Jan-29 |
| Republic Day | | 26-Jan-27 | 26-Jan-28 | 26-Jan-29 |
| Holi | 04-Mar-26 | 22-Mar-27 | 11-Mar-28 | 01-Mar-29 |
| Ei-ul-Fitar | 21-Mar-26 | 10-Mar-27 | 26-Feb-28 | 14-Feb-29 |
| Good Friday | 03-Apr-26 | 26-Mar-27 | 14-Apr-28 | 30-Mar-29 |
| Labour Day | 01-May-26 | 01-May-27 | 01-May-28 | 01-May-29 |
| Eid-ul-Adha | 27-May-26 | 16-May-26 | 04-May-28 | 24-Apr-29 |
| Independence Day | 15-Aug-26 | 15-Aug-27 | 15-Aug-28 | |
| Ganesh Chaturthi | 14-Sep-26 | 04-Sep-27 | 23-Aug-28 | |
| Gandhi Jayanti | 02-Oct-26 | 02-Oct-27 | 02-Oct-28 | |
| Dusshera | 20-Oct-26 | 09-Oct-27 | 27-Sep-28 | |
| Diwali | 08-Nov-26 | 29-Oct-27 | 17-Oct-28 | |
| Christmas | 25-Dec-26 | 25-Dec-27 | 25-Dec-28 | |

(The document lists Eid-ul-Adha 2027 as 16-May-26 in the 2027 column. That looks like a typo in the source. I did not correct it.)

### 6.3 Assumptions 14 to 22 (cost and resource loading)

- 14: resource loading is from the **tender BOQ quantities**.
- 15: resources for the pours are distributed in proportion to their areas.
- 16: where rates vary by floor, a weighted average of rates is used.
- 17: **NSC cost distribution:** Interior package, Retail and Office common area ID: Block 3 Retail+Office 75%, Block 4 Retail+Entertainment 25%. Hotel and Convention Center ID: Block 1 4 Star 35%, Block 2 3 Star 35%, Block 5 Convention Hall 30%.
- 18: sale values for items not in the contract (before and after markup, in Rs.): Swimming Pool ID 10,00,000 (reduced from Hotel & CC ID); Basement ID 2,00,00,000 / 2,21,04,660 (reduced 50% from each ID package); Terrace Flooring 1,00,00,000 / 1,10,52,330 (reduced 60% from Hotel & CC ID and 40% from Retail ID); Kitchen 4,50,00,000 / 4,97,35,485 (from Hotel & CC ID); Lift 35,00,00,000 / 38,50,00,000 (from Electrical); Swimming Pool Plumbing 50,00,000 (from Plumbing Low Side); Fans, Solar and other MEP equipment 2,00,00,000 (50% each from Electrical and HVAC Low Side); Swimming Pool Landscape 25,00,000 (from Softscape).
- 19: revenue of security, ICT and audio-visual equipment is considered in ELV activities.
- 20: **MEP High Side / Low Side split:** HVAC 65/35; Electrical 60/40; Plumbing 35/65; Fire Fighting 40/60.
- 21: payment during construction for design is taken separately for cash flow and is not loaded in P6.
- 22: revenue from preliminaries and design-review coordination, shop-drawing and BIM charges is taken separately (fixed payment) and is not loaded in P6.

### 6.4 Assumption 17 detail: % of cost by activity name

**ID work, Hotel & CC:** Wall finish ID Works 10%; False Ceiling Installation 12%; Flooring of toilets/kitchen/Balcony 8%; Doors & Windows/Fire Doors/Shaft Doors 10%; False ceiling final finishes 3%; Wooden Flooring/Flooring 10%; Railing for staircase 3%; Fixed Furniture 9%; Soft Furnishing & Signage 15%; Loose Furniture 20%.

**ID work, Retail & Office:** Wall finish ID Works 15%; False Ceiling Installation 20%; Flooring of toilets 8%; Doors & Windows 10%; False ceiling final finishes 2%; Wooden Flooring 10%; Railing for staircase 3%; Fixed Furniture 5%; Soft Furnishing & Signage 20%; Loose Furniture 7%.

**Low Side MEP:**

- *HVAC.* 1st fix: Duct Support Fabrication 2%; Installing duct hangers and supports 4%; Laying drain piping 6%; Laying refrigerant piping 1%. 2nd fix: Duct installation 15%; Insulation of ducts 9%; Chilled water / VRF piping 20%; Indoor units (AHU, FCU) 18%; Connecting refrigerant and drain piping 5%; **Running of Wild Air 0%**. Final fix: grills, diffusers, dampers 10%; thermostats and control panels 5%; Testing, Commissioning & Balancing 5%.
- *Electrical.* 1st fix: Slab Conduiting 10%; Wall Conduiting 5%; back boxes 3%. 2nd fix: Cable tray laying 4%; Cabling & Wire Pulling 20%; Floor Rising Main 14%; DB fixing 3%; Floor/Distribution Panel 8%; Equipment Earthing 3%. Final fix: Switches & Socket 10%; Light Fixtures 15%; Testing & Commissioning 5%.
- *Plumbing.* 1st fix: pipe supports and clamps 5%; water supply pipes 10%; drainage pipes 10%; fixture base supports 5%; Pressure testing 1%; concealed parts of toilet fixtures 5%. 2nd fix: Insulation of hot water pipes 5%; Testing drainage lines 1%; vertical risers and main distribution 10%; floor traps and gully traps 3%. Final fix: sanitary fixtures 20%; CP fittings 10%; Connection of appliances 5%; Testing & Commissioning 10%.
- *Firefighting.* 1st fix: pipe supports and hangers 7%; branch piping 15%; Hydrostatic pressure testing 2%. 2nd fix: Painting/insulation of exposed fire pipes 1%; Testing risers and branch lines 2%; vertical risers and distribution piping in shafts 20%; sprinkler branch lines 15%. Final fix: portable fire extinguishers 1%; hydrant accessories 10%; Integration with fire alarm 5%; sprinkler heads 15%; Testing & Commissioning 7%.
- *ELV.* 1st fix: Wall Conduiting 3%; Slab Conduiting 7%; back boxes 5%. 2nd fix: Cable tray 5%; ELV cabling 12%; ELV Rack 5%; Termination of cables 5%; device bases 10%. Final fix: data and voice faceplate 5%; Camera and Wifi 5%; fire alarm devices + PA 6%; Active System 10%; Fire Panel 5%; Audio Visual 5%; Access Control 5%; Integration of active components 2%; Testing & Commissioning 5%.
- *Kitchen.* Counters and cabinet 10%; MEP services 15%; Kitchen equipment 70%; Testing 5%.
- *Lift.* Installation 90%; Testing 10%.

**High Side MEP:** Plumbing (B3): Sump pumps 15%, Pump installation 15%, ETP 15%, STP 20%, Hydro-pneumatic 20%, Connection of pumps and tanks 10%, Testing 5%. Plumbing (B2): Pump 30%, Hydro-pneumatic 40%, Connection 20%, Testing 10%. Electrical (B1): DG set 20%, UPS 10%, HT/LT cables 10%, Transformer 15%, Main HT/LT panels and switchgear 20%, Readiness of Electrical Panel Room 3%, Busbar trunking/rising main 10%, Substation earthing 3%, HT/LT termination 4%, Testing 5%. Plumbing (B1): Pump 30%, Hydro-pneumatic 40%, Connection 20%, Testing 10%. Firefighting (B1): Fire pump 35%, Pump room piping and valves 35%, Fire control panels 20%, Testing 10%. HVAC (B1): Chiller 25%, Pump 10%, Cooling tower 10%, AHU 10%, Heat Pump 5%, Ventilation Fan 5%, MS Piping 5%, Valves and fittings 10%, Insulation and cladding 5%, Electrical works 10%, Testing 5%. Plumbing High Side by basement: B3 60%, B2 20%, B1 20%.

**Facade (activity split):** Integration of Services Before Facade 5%; Fixing of Facade Support 25%; Fixing of Facade 60%; Integration of Services After Facade 10%. **Facade type:** FRP 30%, Glass 70%.

**External development / landscape:** Hardscape: GSB 8%, DLC 8%, PQC 10%, Saucer Drain 5%, Kerb Stone 5%, Bituminous Concrete 10%, Hardscape 50%, Water Body 4%. Softscape: Horticulture and drip irrigation 50%, Signage 20%, Lighting 30%.

**ID type:** MEP 30%, Finishes 70%. **MEP ID stream:** HVAC 30%, Electrical 35%, Plumbing 20%, Firefighting 10%, ELV 5%.

**Swimming Pool plumbing:** Pump Room 40%, Balancing Tank 40%, plumbing connections 15%, Testing 5%. **Pool ID:** Tiling inside pool 70%, Tiling on deck 30%. **Basement ID:** Gypsum board 50%, Door & Window 50%; by basement B3 20%, B2 30%, B1 50%. **Water Body:** Pump Room 40%, Balancing Tank 30%, plumbing 15%, Tiling 10%, Testing/Commissioning/HO 5%. **LPS:** Horizontal 70%, Vertical 30%.

### 6.5 Progress measurement weightages (assumption 23)

| WBS | Weight |
|---|---|
| **Procurement** | **17.0%** (Key Vendor Mobilisation 12.0%: Civil 1.20, MEP 3.60, Finishes/ID Retail & Offices 2.40, Finishes/ID Hotels & CC 2.40, Facade 1.20, Misc 1.08, Mix Design of Concrete 0.12; Delivery of Critical Items 5.0%: Structure Steel 1.0, Manufacturing 2.5, Factory Inspection & Approval 1.0, Delivery 0.5) |
| **Design & Drawings** | **10.0%** (Consultant Onboarding 0.5, Concept 1.0, Schematic 1.0, Detail Design 2.0, Tender 0.5, GFCs 3.0, Shop Drawings 1.0, As Built 1.0) |
| **Mockups** | **3.0%** (Civil 0.1, MEP 0.2, ID 2.0, Misc 0.2, Facade 0.5) |
| **Construction** | **70.0%** |

Construction split: Hotel 4 Star 12.0% (Substructure 1.4, Superstructure 2.4, Wet finishes 0.6, MEP 1.4, ID 1.8, Steel for Facade 0.6, Facade 1.8, Terrace 0.2, Pool 0.5, Vertical Transport 0.6, Testing/Commissioning/HO 0.6). Hotel 3 Star 12.0% (Substructure 1.4, Superstructure 2.9, Wet 0.6, MEP 1.4, ID 1.8, Steel 0.6, Facade 1.8, Terrace 0.2, VT 0.6, T&C 0.6). Retail Block 2 14.0% (1.7, 2.8, 0.7, 2.1, 1.4, 0.7, 2.1, 0.4, 1.4, 0.7). Retail Block 1 10.0% (1.2, 2.0, 0.5, 1.5, 1.0, 0.5, 1.5, 0.3, 1.0, 0.5). Convention Center 10.0% (1.2, 2.4, 0.5, 1.2, 1.5, 0.5, 1.5, 0.2, 0.5, 0.5). Common Basements MEP & Finishes 5.0% (B3 1.5, B2 1.0, B1 2.0, T&C 0.5). Structural Steel Fabrication 0.5%. Infra Works 1%. External Development/Landscape 3% (Roads 0.5, External MEP 0.2, Landscape 2.0, Water Body 0.1, Handing Over 0.2). Misc 0.5%. Project Closure 2%.

### 6.6 Productivity norms (assumption 24)

| Activity | Labour | UOM | Productivity (UOM/day) |
|---|---|---|---|
| Reinforcement | Barbender + 0.5 Helper | MT | 0.15 |
| Formwork | Carpenter + 0.5 Helper | Sqm | 6 |
| Masonry | Mason + 0.5 Helper | Cum | 1.5 |
| Plaster | Mason + 0.5 Helper | Sqm | 15 |
| Flooring | Flooring Mason + Helper | INR | 20,000 |
| Painting | Painter | Sqm | 10 |
| Concrete | Mason + Helper | Cum | 30 |
| Waterproofing | Mason + 0.5 Helper | Sqm | 12 |
| Waterproofing | Mason + 0.5 Helper | INR | 10,500 |
| Structural Steel Erection | 1 Fitter + 2 welder + 2 Rigger + 2 Helper | MT | 1.5 |
| Structural Steel Fabrication | 1 Fitter + 2 welder + 2 Rigger + 2 Helper + 1 Gas cutter | MT | 0.8 |

### 6.7 Pour plans (R2 drawings, read in full)

| Building | Substructure | Floors |
|---|---|---|
| Hotel 4 Star | 4 pours | Ground Floor roof 5; First Floor roof 4; Service Floor roof onwards 3 |
| Hotel 3 Star | Pours 1 and 2, plus Pour 3 for footing only | Ground Floor roof 3; First Floor roof 3; Service Floor roof onwards 2 |
| Retail Block 2 | 6 pours | Ground Floor roof to 4th Floor roof: 6 pours (Pour 6 is a small separate area at the top left); 5th to 6th Floor roof: 5 pours (area 8,000 sqm) |
| Convention Centre | 7 pours | Ground Floor, 1st Mezzanine, 1st Floor roof: 3 pours; 2nd Mezzanine, 3rd Mezzanine, Second Floor roof: 4 pours (Pour 4 is a central block between Pours 1, 2 and 3) |
| Retail Block 1 | 7 pours | Ground and 1st Floor roof 3; 2nd Floor roof 3; 3rd Floor roof 3; 4th Floor roof 4 |

### 6.8 R0 versus R2

R2 is dated 21 May 2026 and carries the Adani and Tata Projects logos. The assumptions text in R0 and R2 looked the same where I compared them (key dates, calendars, cost splits, weightages, norms). I compared by eye, not line by line. R2 has clearer pour-plan drawings.

### 6.9 Cross-check against the baseline XER

| Item | Assumptions document | Baseline XER | Result |
|---|---|---|---|
| Project Commencement | 16 Apr 2026 | milestone on 16 Apr 2026 | Matches |
| Project Completion | 15 May 2029 | milestone on 15 May 2029 | Matches |
| Site handover dates | 16 Apr, 16 May, 16 Jun, 16 Jun, 16 Jul 2026 | substructure commencement milestones on the same dates | Matches |
| Core & Shell completion | 15 Mar 2028 | latest wet-works and steel completion milestones are 15 Mar 2028 | Consistent |
| Receipt of LOI | 13 Feb 2026 (NTP 14 Feb) | "Issue of LOI" milestone 14 Feb 2026 | One-day difference, check |
| Calendars | 6 days, 10 hours, holidays, monsoon; 5-day design | calendars with exactly these names and hours | Matches |
| ID finishes start | after facade and Running of Wild Air | Wall finish ID works wait for Running of Wild Air, which waits for facade fixing | Matches my finding |
| Pours | may change with PT vendor drawings; resources by area | pours are the unit of sequencing and PT work | Explains why pours exist |
| LPS | cost item, horizontal 70% / vertical 30% | "LPS" activity in column and wall cycles | Supports my reading |
| Running of Wild Air | HVAC second fix, 0% cost | gate in the ID finishes logic | A zero-cost HVAC gate |

**Pour counts against the R2 drawings.** Substructure counts in all five buildings match. Hotel 4 Star floors match. Hotel 3 Star floors match (Ground and First 3, Service onwards 2). Retail Block 1 floors match (3, with 4 on the 4th floor roof). Convention Center floors match (3, 3, 4, 3, 4, 4). Retail Block 2 5th and 6th floors match (5). **One difference remains: Retail Block 2, Ground Floor to 4th Floor roof.** The drawing shows 6 pours (Pour 6 is a small separate area); the XER has 5 pours on each of those floors.

**The assumptions documents contain no sequencing logic.** They confirm dates, calendars and pour structure, and they give the cost and resource assumptions that partly replace the missing cost-loading backup. I have not yet checked those cost splits against the resource assignments in the XER.

---

## 7. The recovery schedule (`CSD-LKO-Revamp-BL.xer`, data date 31 Jul 2026) compared with the baseline

### 7.1 What the file is

A **progressed update**, not just a re-dated copy. Project `CSD-LKO-Adani`. Same WBS. 13,441 activities (5 fewer than the baseline), 22,598 relationships. Status: 13,045 not started, 269 complete, 127 active. Calendars were renamed with a "-25" suffix. Schedule options: retained logic on, use expected finish dates on, relationship lag calendar = predecessor. **Project completion unchanged at 15 May 2029.**

### 7.2 Why it was needed (evidence in the file)

- **Site handover slipped.** Retail Block 1 start 16 Jun to 24 Aug 2026 and Retail Block 2 16 Jul to 21 Sep 2026, both held with Mandatory Start constraints. "Completion of Site Handover By Client" moved from 16 Jul to 21 Sep 2026.
- **The first work started late.** Hotel 4 Star pocket excavation actually started on 20 May 2026 against 16 Apr in the baseline.
- **Progress behind plan.** Of 1,061 activities planned (baseline early dates) to finish by 31 Jul, 259 were complete (24%). Of 1,189 planned to start, 373 had started (31%).

### 7.3 How the finish date was held

- **Construction durations shortened on about 500 activities** (502 shorter, 7 longer). Examples: chilled-water and VRF piping, cable tray work and cable tray installation about 43% of baseline durations; ducts and insulation about 50 to 57%; flooring 62%; brickwork 55%; Fixing of Facade 81%.
- **63 foundation waterproofing activities set to zero duration.** Zero-duration non-milestone activities rose from 46 to 109.
- **Design:** structural drawing preparation cut (45 to 7 days on 25 activities; 31 to 7 on 22; 37 to 15 on 19; 32 to 15 on 17). "Issue of Hard Copy on Site" lengthened from 1 to 4 days on 137 activities. 114 design activities shorter, 154 longer.
- **Procurement shortened on 18 activities:** Transformer manufacturing 248 to 90 days; Chiller 248 to 120; Vertical transport 261 to 150; AHU 180 to 90; Pumps 180 to 90; STP/ETP 267 to 120.
- **GFC release milestones slipped a lot** (for milestones not yet complete): "GFC Issuance - MEP & FF Sign Off" 3 Sep 2026 to 26 Apr 2027 (+235 days); "GFC Issuance - Civil core & shell" 22 Sep 2026 to 18 Mar 2027 (+177 days); "4 Star Hotel Commencement" 17 Mar 2027 to 11 Aug 2027 (+147 days).
- (Early dates of completed milestones such as Issue of LOI and Project Commencement show the data date, because they are complete with actual dates. I did not treat that as slippage.)

### 7.4 Logic changes

99% of the baseline links survived. **160 removed, 195 added.**

| Category | Removed | Added |
|---|---|---|
| Design to Design (GFC drawing sequence re-chained, for example fan-out to serial) | 111 | 126 |
| Construction to Construction (FS) | 26 | 37 |
| Design to Construction | 12 | 21 |
| Design to Procurement | 8 | 2 |
| Construction to Construction (FF) | 2 | 2 |
| Procurement to Construction | | 4 |
| Other | 1 | 3 |

Notable changes:

- **Retail Block 1 foundation.** Five activities deleted (`RB1-SS-FN410` Blockwork, `FN415` Waterproofing, `FN485` Blockwork, `FN495` and `FN500` Waterproofing) and the links around them redone.
- **Basement PT sequence reworked.** Basement 03 PT now precedes Basement 02 PT (for example `4S-SS-B-03.305` to `4S-SS-B-02.195`).
- **New links:** the common basement finishes' Deshuttering now waits for the PT work of the slab above (for each building).
- **New cross-building link:** Convention Center Basement 03 steel waits for Hotel 3 Star foundation concrete (`3S-SS-FN80` and `FN165` to `CC-SS-B03.10`, `.15`, `.20`, `.25`).
- **One lag changed** (a milestone link from 25 to 3 days).
- **Constraints: 21 added.** 19 Mandatory Finish on foundation pocket excavations (Hotel 3 Star and Convention Center, 23 Jul to 20 Aug 2026) and 2 Mandatory Start on the Retail Block 1 and 2 site handover milestones.

### 7.5 Calendars

Construction calendars are unchanged apart from the "-25" rename. The design calendar lost ten July 2026 working-time exceptions (8-hour entries on specific Wednesdays and Fridays) and gained two Labour Day holidays (1 May 2026 and 1 May 2028). This is from a crude parse of the calendar data.

### 7.6 Quality checks, baseline versus recovery

| Check | Baseline | Recovery (31 Jul) |
|---|---|---|
| Loops | none | none |
| Missing logic (non-milestone) | 0 | 0 |
| Negative lags | 0 | 0 |
| Relationship mix | 97.5% FS | 97.5% FS |
| Hard constraints | 0 | 21 |
| Negative float | 0 | 53 activities |
| Zero float, not complete | 202 | 391 |
| Float over 44 wd | 55% | 46% |
| Started before a Finish-to-Start predecessor finished | 0 | 105 |
| Actual dates after the data date | 0 | 4 |
| Activities with no resources | 0 | 0 |

The four actual-date errors: `P-MEP-UPS-25` (actual start 8 May 2027, finish 28 May 2027), `E-DD-Misc-Lighting-10` (actual start 3 May 2027), `P-MEP-Stack-15` (actual start 30 Apr 2027), `4S-SS-FN625` (actual finish 1 Aug 2026, one day after the data date).

### 7.6a Is the logic correct and workable? (my assessment)

- **Baseline: valid and mostly workable.** No loops, no open ends, all dates logic-driven, rules consistent across buildings and matching the assumptions document, completion on the critical path with zero float. **Weak points:** finishing floors are not linked to each other (55% of activities float over 44 wd); nothing limits crews or areas, so all pours and buildings can run in parallel; the Convention Center exceptions and long undocumented lags; zero float on completion suggests the dates were fitted to the contract date (not provable from the file). It is a correct logic network but not a resource-realistic one.
- **Recovery (31 Jul): not workable as it stands.** It meets the finish date by forcing it: 21 hard constraints, 53 activities with negative float, 105 started out of sequence, 4 actual dates in the future, stale milestones, and many durations that look like date-fitting (MEP finishes cut to roughly 40 to 60%, drawing preparation 45 to 7 days, 63 waterproofing activities at zero days) without any change in logic. I did not check whether crews were increased.
- **Correction recorded in section 12:** I first said critical activities rose from 202 to 713. That included completed activities. The correct figure for incomplete work is **444** (391 at zero float and 53 negative).

---

## 8. The 30 Sep update (`CSD-LKO-Revamp-30-Sep.xer`)

### 8.1 State of the file

- Project `CSD-LKO-26-SEP-26`. **Data date 30 Sep 2026.** Same 13,441 activities as the 31 Jul file, 22,658 relationships.
- Status: 12,862 not started, **385 complete**, **194 active**.
- **Forecast completion 7 Jun 2029**, which is **23 days after the contract date of 15 May 2029.** The 31 Jul version showed 15 May 2029 only because it was held by constraints.
- Schedule options unchanged: retained logic, use expected finish dates (none set), predecessor calendar for lags.

### 8.2 Quality checks (30 Sep)

| Check | Result |
|---|---|
| Loops | none |
| Missing predecessor or successor (non-milestone) | 0 |
| Missing successor | 12 (all finish milestones) |
| Negative lags | 0 |
| Lags | 241 (1.1%) |
| Relationship mix | FS 96.5%, FF 2.1%, SS 1.4% |
| Hard constraints on remaining work | 0 (2 Start On or After on handover milestones; 2 Mandatory Finish on completed activities) |
| Negative float | 0 |
| Zero float | 140 |
| Actual dates after data date | 0 |
| Out-of-sequence in status | 0 |
| Remaining activities with no resources | 0 |
| Active activities with remaining duration 0 | 2; with 0% complete 10 |
| Complete activities lacking actual dates | 0 |

### 8.3 Progress

- By group: Construction 192 complete and 100 active; Design & Drawings 109 and 76; Procurement 37 and 12; Mobilisation 31 and 6; Milestones 16 complete.
- By building (Construction, complete / active / total): Hotel 4 Star 107 / 17 / 2,378; Hotel 3 Star 56 / 26 / 2,239; Convention Center 26 / 45 / 1,962; Retail Block 1 2 / 12 / 1,809; Retail Block 2 1 / 0 / 2,079; Common Basements, Infra, External, Bridge, Project Closure: none.
- Against the original baseline: of 1,916 activities planned to finish by 30 Sep, 379 are complete (20%). Of 1,982 planned to start, 559 have started (28%).
- 130 Finish-to-Start pairs actually started before their predecessor actually finished (mostly foundation activities). This is history, not a calculation problem under retained logic.

### 8.4 What drives the finish

The finish is driven by one chain: the **Retail Block 1 site handover (12 Oct 2026, a Start On or After constraint)**, to the **Retail Block 2 ramp excavation (6 Nov 2026)**, then through Retail Block 2 construction (133 critical activities) to the Retail Block 2 handover and Project Completion on 7 Jun 2029. Critical (incomplete) activities: 140, of which Retail Block 2 133, Milestones 4, Project Closure 3. Retail Block 2's site handover milestone shows a Start On or After constraint of 21 Sep 2026, but logic pushes it to 6 Nov 2026.

### 8.5 Changes since the 31 Jul file

- 59 more durations shortened (none lengthened), for example Testing & Commissioning and Snagging 45 to 30 days in several floors, Fixing of Facade Support on the Convention Center terrace 75 to 60, `4S-SS-GS90` Reinforcement 10 to 5.
- **250 relationships removed, 310 added.** The main change: **117 foundation Finish-to-Start links became Start-to-Start**, so foundation pours overlap (for example `CC-SS-FN445` to `CC-SS-FN465`). 157 Construction FS links were removed, 7 FS added. 68 Milestone to Milestone FS links were added, mostly tying milestones to Project Completion. 32 Construction FF links were added (for example Handing Over now finishes with Snagging, `4S-T&C-6th15` to `4S-T&C-6th20`). 58 Design FS removed and 55 Design SS added. 4 Milestone to Construction SS added.
- Relationship mix moved from FS 97.5% to FS 96.5%.

### 8.6 Remaining durations compared with the original baseline

- Not-complete tasks shorter than in the baseline: **659**; longer: **161**. The sum of remaining task durations is 95% of the baseline's.
- Biggest average cuts: Drawings Preparation & Submission (111 activities, about 37% of baseline); Waterproofing (46 activities, about 2%); Fixing of Facade 78%; Slab Conduiting 71%; Snagging 74%; Testing & Commissioning 75%; Flooring 62%; Brickwork 55%; Equipment Earthing 52%; Cable tray laying 43%.
- Zero-duration tasks remaining (not milestone, not complete): 45 (44 of them Waterproofing).

---

## 9. Float analysis (30 Sep update)

### 9.1 Working days (first measurement)

- Remaining activities: 13,056. Float over 40 wd: 9,299 (**71%**). Zero float 140; 1 to 40: 3,617; 40 to 100: 4,654; 100 to 200: 2,272; 200 to 400: 2,193; over 400: 180.
- Medians: Superstructure 43 wd; Wet finishes, MEP, ID 82; Facade 31; Testing/Commissioning/HO 39; Substructure 50; Design & Drawings 211; Procurement 213; Milestones 355.
- Note: my earlier figure of 66% used a 44-day threshold and excluded milestones.

### 9.2 Calendar days (the unit you set)

You set the rule: **positive float at most 40 calendar days (44 acceptable), negative float 0.**

| Float (calendar days) | Activities |
|---|---|
| below 0 | 1 |
| 0 | 140 |
| 1 to 40 | 2,991 |
| 41 to 44 | 211 |
| 45 to 100 | 4,322 |
| 101 to 200 | 2,124 |
| 201 to 365 | 2,514 |
| over 365 | 753 |

**Over 44 calendar days: 9,713 (74%). Over 40: 9,924.**

Largest groups over 44 days: Hotel 4 Star 2,097 of 2,271; Retail Block 2 1,764 of 2,078; Hotel 3 Star 1,689 of 2,183; all 1,221 Common Basements activities; Design & Drawings 1,014 of 1,058; Convention Center 884 of 1,936; Retail Block 1 668 of 1,807; Procurement 195 of 230; Milestones 73 of 87; Bridge 35 of 35; Mockups 25 of 54; Mobilisation 22 of 23; Project Closure 12 of 34; External Development 10 of 23.

Why: the finish is driven by one chain, and everything else is not tied to it by crews, areas or need dates. Negative float is currently 0 only because Project Completion has no contract-date constraint. Once it is held at 15 May 2029, the 23-day gap appears as negative float on the Retail Block 2 chain.

### 9.3 Core & Shell

Contract Core & Shell date: **15 Mar 2028**. In the original baseline the Core & Shell milestones all landed on or before it. In the 30 Sep schedule they run later:

| Milestone | 30 Sep forecast | Days after 15 Mar 2028 |
|---|---|---|
| Retail Block 2 Structural Steel Completion | 2 Jun 2028 | 79 |
| Retail Block 1 Structural Steel Completion | 29 May 2028 | 75 |
| Convention Centre Wet Works Completion | 28 Apr 2028 | 44 |
| Hotel 3 Star Structural Steel Completion | 18 Apr 2028 | 34 |
| Hotel 4 Star Structural Steel Completion | 5 Apr 2028 | 21 |
| Other milestones (wet works completions of 4 Star 8 Feb, 3 Star 3 Mar, Retail 1 29 Mar, Retail 2 17 Mar 2028) | on or near the date, Retail 1 14 days late | |

These milestones show 370 to 980 days of float because nothing ties them to the contract date. Once held at 15 Mar 2028 they will show large negative float.

### 9.4 What drives the late Core & Shell milestones

The same pattern repeats in every building: substructure, then superstructure, then the **"Structural Steel works for Facade"** zone chain, which ends at the late milestone.

| Building | Steel-for-facade chain starts | Steel completion milestone |
|---|---|---|
| Retail Block 2 | 28 Dec 2027 | 2 Jun 2028 |
| Retail Block 1 | 3 Dec 2027 | 29 May 2028 |
| Hotel 3 Star | 8 Jan 2028 | 18 Apr 2028 |
| Hotel 4 Star | 15 Oct 2027 | 5 Apr 2028 |

Convention Center's late milestone is wet works completion, driven by its second-floor finishes chain starting 10 Mar 2028.

Two **logic** choices cause this:

1. The steel zones run strictly one after another, each 35 days, so one building takes about five months.
2. The steel chain starts only after the top-floor structure is nearly done (a finish-to-finish link with a lag).

Both are choices about links, not durations. Steel zones could overlap or run in parallel, and each zone could start after the structure below it, subject to confirmation by your construction team.

---

## 10. Requirements and constraints you set (in order)

1. **Contract date for completion: 15 May 2029.** (Your answer to my question on the revised baseline's completion date. The alternatives I offered were the 7 Jun 2029 forecast or a client-given date.)
2. **Full rebuild of remaining work** (your answer on edit depth). I had also offered "minimal fixes only" and "restore baseline logic where unsupported".
3. **Deliverables:** you answered "something else" and did not describe it. **This is still open.**
4. **Global changes in the XER first.** You will apply global changes in P6 yourself before the revised baseline is prepared, and will send me that XER. I listed candidates (constraints, zero-duration waterproofing, compressed durations, "-25" calendar names, "Holyday" spelling, WBS spelling "Mobilisation" versus "Mobilization").
5. **Float rule from the client:** positive float not more than 40 calendar days (44 acceptable) and **negative float 0**.
6. **Logic may change** as long as the completion date stays intact. The contract timelines for Core & Shell and other works are in the assumptions PDF.
7. **Original and remaining durations are fixed.** I cannot change any duration. Only relationships (links and lags) can change.

---

## 11. What I told you I can and cannot do

**Can:** edit the XER directly (add and remove relationships, change lags and constraints); test the logic with my own schedule calculation, including checking the Core & Shell and Completion dates and the float; keep all actuals unchanged; document every change in a change log with the activity ID, old and new value, and reason.

**Cannot:**
- **P6 gives the final dates, not me.** My calculation will be close but may differ by a few days (holidays, monsoon calendars). You press F9 in P6 and we may need another tuning pass.
- I cannot prove the compression is achievable on site. With durations fixed, closing the gap depends only on logic. The result is a proposal your construction team must validate.
- It may not close fully for Retail Block 1 and 2, whose handover came about four months late. If overlap alone is not enough, I will show the remaining gap.
- Importing carries some risk. I will keep IDs and structure unchanged, but I cannot test an import. If P6 rejects the file, send me the error.

**Rules I will follow in the rebuild:**
- No change to any original or remaining duration.
- No negative lags unless you tell me otherwise. Overlap goes through Start-to-Start or Finish-to-Finish links with positive lags.
- Every logic change gets a reason in the change log. Rules such as "this zone can start when the zone below is a third done" need a crew or area basis.
- Float is consumed by adding real links (crew and area flow between floors, buildings and design releases), not by padding.

**My cautions:** holding 15 May 2029 and capping float at 44 days leaves very little slack anywhere, so the schedule will look aggressive and a few slipped activities will push the finish.

**My order of preference for consuming float:** (1) real logic, (2) named lead-time activities in place of hidden lags, (3) ALAP or constraints only if the client accepts them in writing, (4) never padding durations or adding artificial lags.

---

## 12. Corrections to my own earlier statements

I made these errors during the work. All are corrected here.

| # | What I said earlier | Correction |
|---|---|---|
| 1 | Durations, floats and lags divided by 8 hours a day (explorer, first explanations). | The project calendars use **10-hour working days**. All durations shown before the fix were overstated by 25%. Example: "Wait for Strength Gain" is **6 working days**, not 7.5. The explorer and the narrative were corrected. |
| 2 | In the first explanation of testing, "Handover follows both testing and snagging". | The sequence per floor is **Testing and Commissioning, then Snagging, then Handing Over.** Handing Over waits for snagging. |
| 3 | I listed several pour-count differences between the assumptions document and the XER (Retail Block 1 4th floor, Convention Center mezzanines, Hotel 3 Star Service Floor, Retail Block 2). | Those were from **reading pour labels in the R0 extracted text, and they were wrong.** With the R2 drawings: everything matches except **Retail Block 2, Ground to 4th Floor roof** (drawing 6 pours, XER 5). |
| 4 | I suggested the unusual Pour 4 logic in the Convention Center might come from a pour-count difference. | It does not. In the drawing, Pour 4 on the 2nd and 3rd mezzanine is a central block surrounded by Pours 1 to 3, so it may be a steel-framed area. To be confirmed. |
| 5 | "Critical activities rose from 202 to 713" in the recovery schedule. | That count included 269 completed activities. For work still to do the figure is **444** (391 at zero float, 53 negative). |
| 6 | "66% of remaining activities have more than 44 working days of float" (30 Sep). | The 66% used a 44-day threshold and excluded milestones. Over 40 wd it is 71%. In **calendar days** (your unit) it is **74% over 44**. |
| 7 | My reading of "Running of Wild Air" as running the AC or ventilation. | The assumptions document lists it as an **HVAC second-fix item with 0% cost** and says ID finishes start only after the facade and this step. It is a zero-cost gate in the logic. The exact site meaning is still to be confirmed. |
| 8 | "Rule 2": pours rise independently. | Softened: by logic alone, in practice crews and resources would limit this. |
| 9 | "Hotel 3 Star Service Floor has a 3-pour vs 2 difference". | Wrong. The drawing shows Service Floor onwards with 2 pours. |
| 10 | Early shorthand for the milestone dates in the recovery file ("100 of 105 moved"). | Completed milestones show the data date in their early dates, so that count was an artifact. I only report milestones that are not yet complete. |

---

## 13. Open points

1. **The deliverables you want** (your "something else" answer). Not yet described.
2. **The globally changed XER** and the list of changes you applied.
3. **Which milestones define "Core & Shell Completion".** My assumption: everything in the Milestones, Construction, Core & Shell Works group, all on or before 15 Mar 2028.
4. **Other contractual dates** ("other works"): building completion dates, facade, landscape, external works. Please send them if the contract lists them.
5. **Whether the Retail Block 1 and 2 site handover dates (12 Oct and 6 Nov 2026) are fixed by the client.**
6. **Site confirmation of the logic proposals**, especially the steel-for-facade zones (overlap or parallel erection, earlier start), the finishing-floor crew flow, the Convention Center Pour 4 (steel) logic and the grade-slab order.
7. **Retail Block 2 Pour 6** (drawing shows 6 pours on Ground to 4th Floor roof; XER has 5).
8. **LOI date** (13 Feb in the assumptions, 14 Feb in the XER milestone).
9. **Cost and resource cross-check** (assumptions splits versus XER assignments) has not been done.
10. **Actuals clean-up in the 31 Jul recovery file** (four future actual dates) is moot if the 30 Sep file replaces it, but those four activities should be checked in the 30 Sep file (they are clean there).

---

## 14. Plan for the revised baseline

1. **You apply global changes in P6** and send the XER with the list of changes.
2. I **verify the global changes took effect** and compare with the 30 Sep file.
3. **Stage 1: logic and float.** I build a calculation from the XER and calendars, then propose logic changes (relationships and lags only):
   - Set the milestone targets (Core & Shell on 15 Mar 2028, Completion on 15 May 2029) and measure the negative float they create.
   - Find the longest chains that cannot be shortened by durations (fixed) and identify overlap opportunities: steel-for-facade zones, structure-to-finishes triggers, finishing floors, common basements, building-to-building crew flow, design flow.
   - Add real links to bring float to 40 to 44 calendar days or less.
   - Produce a **change log** for you and the construction team.
4. **Stage 2: the XER**, after you agree the change log. I will edit relationships and lags only, keep IDs and actuals untouched, and give you a file to import and reschedule (F9) in P6.
5. **Final dates come from P6.** We may need another pass.

---

## 15. Notes on risk for the client conversation

- Holding Core & Shell on 15 Mar 2028 and Completion on 15 May 2029 together with a 44-day float cap leaves almost no slack. Any slipped activity will push the finish.
- The Retail Block 1 and 2 handover delay of roughly four months is the largest single factor. The client should understand it is a cause of the gap.
- The recovery schedule was held to 15 May 2029 by constraints and compressed durations. The 30 Sep update no longer has those constraints and shows 7 Jun 2029.

---

## 16. Method notes

- **XER parsing:** plain text parsing of the tables `PROJECT`, `PROJWBS`, `TASK`, `TASKPRED`, `TASKRSRC`, `CALENDAR`, `SCHEDOPTIONS`. Activities matched between files by activity ID (`task_code`).
- **Durations in working days:** `target_drtn_hr_cnt` divided by the task calendar's hours per day (10 for the construction and design calendars). Lags use the predecessor's calendar, which matches the schedule option in the files.
- **Float:** working-day figures are `total_float_hr_cnt` divided by the task calendar's hours per day. Calendar-day figures are the difference between late finish and early finish dates.
- **Driving chains:** for each activity, the predecessor that implies the latest start (from early dates, relationship type and lag) is followed back. This is an approximation; P6's own driving-path analysis may differ slightly.
- **Quality checks:** based on the DCMA 14-point style tests. Thresholds are guidance, not contract requirements.
- **Plain-English meanings** of activity names are standard construction meanings, not text from the files, except where the assumptions document confirms them (LPS, Running of Wild Air).
- **Not examined:** the images embedded in the R0 docx; cost and resource assignments in the XER; the contract; whether the sequences match real site practice; the P6 import of any edited file.

---

## Appendix A. Reference blocks: activity-by-activity tables (Hotel 4 Star)

These tables are the same as in `CSD-LKO_Construction_Logic_Narrative.html`, section 5. Each block is one real group of activities. "#" is the diagram number inside the block. "Starts after" lists the predecessors: "#n" refers to another activity in the same block; items that are not numbers come from outside the block (design releases, vendors, other floors). Durations are in working days.

### A. Foundation: one footing group (Pour 1, footing CF32)

This is the very first construction work. A footing group follows a fixed order: dig the pocket, level the surface, treat the soil against termites, lay a lean concrete base (PCC), waterproof, fix the steel, and cast. Its first activity waits for the Project Commencement milestone, the site office being set up, and the foundation drawings being issued. Vendors for termite treatment, waterproofing and approved concrete mix designs are also pre-requisites. Every other footing group, pour and building repeats this recipe.

*Where in the schedule: Construction > Hotel 4 Star > Substructure > Foundation > Pour 1*

35 activities, planned (early dates) 2026-04-16 to 2026-06-10. Triggered by: Procurement: Key Vendor Mobilisation › Mix Design of Concre; Procurement: Civil work › Waterproofing; Milestone: Project Commencement Date; Mobilization: Site Office Setup; Design: GFC drawing issued on site; Procurement: Civil work › ATT. Releases: Foundation › Pour 2 › CF41A; Basement 03 › Pour 1 › Column, Core Wall, Shear Wall; Basement 03 › Pour 1 › Staircase; Milestone: 4 Star Sub Structure Commencement.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Pocket Excavation (4wd) → #2 Surface dressing (1wd) → #3 ATT (1wd) → #4 PCC (1wd) → #6 Blockwork/Brickwork (1wd) → #8 Pocket Excavation (3wd) → #10 Surface dressing (1wd) → #12 ATT (1wd) → #13 PCC (1wd) → #14 Shuttering (10wd) → #16 Waterproofing (5wd) → #18 Reinforcement (18wd) → #21 Concrete (1wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SS-FN10` | **Pocket Excavation**. Digging out the pockets (pits) for the footings. | 4 | Milestone: Project Commencement Date, Mobilization: Site Office Setup, Design: GFC drawing issued on site |
| 2 | `4S-SS-FN15` | **Surface dressing**. Levelling and compacting the excavated surface. | 1 | #1 |
| 3 | `4S-SS-FN20` | **ATT**. Anti-termite treatment: chemical treatment of the soil under the foundation or slab to prevent termite attack. | 1 | #2, Procurement: Civil work › ATT |
| 4 | `4S-SS-FN25` | **PCC**. Plain cement concrete: a thin lean concrete layer that gives a clean, level base to build on. | 1 | #3 FF, #2 |
| 5 | `4S-SS-FN30` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the footing CF32. | 10 | #4 |
| 6 | `4S-SS-FN35` | **Blockwork/Brickwork**. Building walls with bricks or blocks (enclosures, partitions, pit walls). | 1 | #1, #4 |
| 7 | `4S-SS-FN45` | **Waterproofing**. Applying waterproofing to stop water getting through. | 5 | #4, #5, Procurement: Civil work › Waterproofing |
| 8 | `4S-SS-FN40` | **Pocket Excavation**. Digging out the pockets (pits) for the footings. | 3 | #6 |
| 9 | `4S-SS-FN65` | **Reinforcement**. Cutting, bending and tying the steel bars for the footing CF32. This is inspected before the formwork is closed. | 20 | #7 |
| 10 | `4S-SS-FN50` | **Surface dressing**. Levelling and compacting the excavated surface. | 1 | #8 |
| 11 | `4S-SS-FN90` | **Concrete**. Pouring and compacting the concrete for the footing CF32. | 1 | #9, Procurement: Key Vendor Mobilisation › Mix Design of Concre x3 |
| 12 | `4S-SS-FN55` | **ATT**. Anti-termite treatment: chemical treatment of the soil under the foundation or slab to prevent termite attack. | 1 | #10, Procurement: Civil work › ATT |
| 13 | `4S-SS-FN60` | **PCC**. Plain cement concrete: a thin lean concrete layer that gives a clean, level base to build on. | 1 | #12 FF, #10 |
| 14 | `4S-SS-FN75` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the footing CF26. | 10 | #13 |
| 15 | `4S-SS-FN70` | **Blockwork/Brickwork**. Building walls with bricks or blocks (enclosures, partitions, pit walls). | 1 | #8, #13 |
| 16 | `4S-SS-FN80` | **Waterproofing**. Applying waterproofing to stop water getting through. | 5 | #13, #14, Procurement: Civil work › Waterproofing |
| 17 | `4S-SS-FN85` | **Pocket Excavation**. Digging out the pockets (pits) for the footings. | 2 | #15 |
| 18 | `4S-SS-FN120` | **Reinforcement**. Cutting, bending and tying the steel bars for the footing CF26. This is inspected before the formwork is closed. | 18 | #16 |
| 19 | `4S-SS-FN100` | **ATT**. Anti-termite treatment: chemical treatment of the soil under the foundation or slab to prevent termite attack. | 1 | #17, Procurement: Civil work › ATT |
| 20 | `4S-SS-FN95` | **Surface dressing**. Levelling and compacting the excavated surface. | 1 | #17 |
| 21 | `4S-SS-FN135` | **Concrete**. Pouring and compacting the concrete for the footing CF26. | 1 | #18 |
| 22 | `4S-SS-FN105` | **PCC**. Plain cement concrete: a thin lean concrete layer that gives a clean, level base to build on. | 1 | #19 FF, #20 |
| 23 | `4S-SS-FN110` | **Blockwork/Brickwork**. Building walls with bricks or blocks (enclosures, partitions, pit walls). | 1 | #17, #22 |
| 24 | `4S-SS-FN115` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the footing CF1D, CF1K, CF32A. | 2 | #22 |
| 25 | `4S-SS-FN130` | **Pocket Excavation**. Digging out the pockets (pits) for the footings. | 1 | #23 |
| 26 | `4S-SS-FN125` | **Waterproofing**. Applying waterproofing to stop water getting through. | 5 | #22, #24, Procurement: Civil work › Waterproofing |
| 27 | `4S-SS-FN140` | **Surface dressing**. Levelling and compacting the excavated surface. | 1 | #25 |
| 28 | `4S-SS-FN190` | **Reinforcement**. Cutting, bending and tying the steel bars for the footing CF1D, CF1K, CF32A. This is inspected before the formwork is closed. | 8 | #26 |
| 29 | `4S-SS-FN150` | **ATT**. Anti-termite treatment: chemical treatment of the soil under the foundation or slab to prevent termite attack. | 1 | #27, Procurement: Civil work › ATT |
| 30 | `4S-SS-FN210` | **Concrete**. Pouring and compacting the concrete for the footing CF1D, CF1K, CF32A. | 1 | #28 |
| 31 | `4S-SS-FN160` | **PCC**. Plain cement concrete: a thin lean concrete layer that gives a clean, level base to build on. | 1 | #29 |
| 32 | `4S-SS-FN175` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the footing CF14A, F6. | 2 | #31 |
| 33 | `4S-SS-FN195` | **Waterproofing**. Applying waterproofing to stop water getting through. | 5 | #31, #32, Procurement: Civil work › Waterproofing |
| 34 | `4S-SS-FN225` | **Reinforcement**. Cutting, bending and tying the steel bars for the footing CF14A, F6. This is inspected before the formwork is closed. | 4 | #33 |
| 35 | `4S-SS-FN260` | **Concrete**. Pouring and compacting the concrete for the footing CF14A, F6. | 1 | #34 |

### B. Basement 03: a standard pour (Pour 1)

A basement is built pour by pour. In each pour the ground is first filled and blinded, then columns and the core and shear walls are cast, the stair core is built flight by flight, and finally the slab is cast. The pour starts after the footing concrete below it, and its slab releases the same pour of the basement above it.

*Where in the schedule: Construction > Hotel 4 Star > Substructure > Basement 03 > Pour 1*

29 activities, planned (early dates) 2026-06-11 to 2026-09-21. Triggered by: Procurement: MEP Work › LPS; Procurement: Civil work › PT Works; Foundation › Pour 1 › CF26; Foundation › Pour 1 › CF14A, F6; Foundation › Pour 1 › CF32; Foundation › Pour 1 › CF1D, CF1K, CF32A and 1 more. Releases: Basement 02 › Pour 1 › Column, Core Wall, Shear Wall; Basement 02 › Pour 1 › Staircase; Basement 03 › Pour 2 › Slab.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Reinforcement (7wd) → #3 LPS (1wd) → #6 Shuttering (7wd) → #8 Concrete (2wd) → #10 Soil Filling/Plum Concrete (10wd) → #12 Surface dressing (8wd) → #14 ATT (4wd) → #16 PCC (4wd) → #18 Shuttering (5wd) → #20 Reinforcement Bottom Net with chai (3wd) → #22 Laying of PT Tendon (4wd) → #24 Reinforcement Top Net (3wd) → #26 MEP Coordination (1wd) → #27 Concrete of Slab (1wd) → #28 Wait for Strength Gain (6wd) → #29 PT Work (6wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SS-B-03.10` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 7 | Foundation › Pour 1 › CF26, Foundation › Pour 1 › CF14A, F6, Foundation › Pour 1 › CF32, Foundation › Pour 1 › CF1D, CF1K, CF32A, Design: GFC drawing issued on site |
| 2 | `4S-SS-B-03.15` | **Reinforcement of wall upto Flight 1**. Fixing the steel bars for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 3 | Foundation › Pour 1 › CF26, Foundation › Pour 1 › CF14A, F6, Foundation › Pour 1 › CF1D, CF1K, CF32A, Foundation › Pour 1 › CF32, Design: GFC drawing issued on site |
| 3 | `4S-SS-B-03.35` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 1 | #1, Procurement: MEP Work › LPS |
| 4 | `4S-SS-B-03.40` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 5 | #1 |
| 5 | `4S-SS-B-03.20` | **Shuttering of wall upto Flight 1**. Erecting formwork for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 3 | #2 |
| 6 | `4S-SS-B-03.45` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 7 | #1, #3 |
| 7 | `4S-SS-B-03.25` | **Casting of wall upto Flight 1**. Pouring concrete for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #5 |
| 8 | `4S-SS-B-03.65` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 2 | #6 |
| 9 | `4S-SS-B-03.30` | **Shuttering of Staircase upto Flight 1**. Erecting formwork for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 3 | #7 |
| 10 | `4S-SS-B-03.75` | **Soil Filling/Plum Concrete**. Filling with soil or plum (mass) concrete under the slab to bring levels up. | 10 | #8, #4 |
| 11 | `4S-SS-B-03.50` | **Reinforcement of Staircase upto Flight 1**. Fixing the steel bars for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 3 | #9 |
| 12 | `4S-SS-B-03.85` | **Surface dressing**. Levelling and compacting the excavated surface. | 8 | #10 FF +1d |
| 13 | `4S-SS-B-03.55` | **MEP coordination upto Flight 1**. Checking that pipes, sleeves and conduits are placed correctly in the stair core up to flight 1 before casting continues. | 1 | #11 |
| 14 | `4S-SS-B-03.115` | **ATT**. Anti-termite treatment: chemical treatment of the soil under the foundation or slab to prevent termite attack. | 4 | #12 FF +1d |
| 15 | `4S-SS-B-03.60` | **Casting of Staircase upto Flight 1**. Pouring concrete for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #13 |
| 16 | `4S-SS-B-03.120` | **PCC**. Plain cement concrete: a thin lean concrete layer that gives a clean, level base to build on. | 4 | #14 FF +1d |
| 17 | `4S-SS-B-03.70` | **Reinforcement of wall upto Flight 2**. Fixing the steel bars for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 3 | #15 |
| 18 | `4S-SS-B-03.130` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the slab. | 5 | #8, #16 |
| 19 | `4S-SS-B-03.80` | **Shuttering of wall upto Flight 2**. Erecting formwork for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 3 | #17 |
| 20 | `4S-SS-B-03.160` | **Reinforcement Bottom Net with chairs**. Fixing the bottom mesh of slab steel, raised on small supports ("chairs") so that concrete covers it. | 3 | #18 |
| 21 | `4S-SS-B-03.90` | **Casting of wall upto Flight 2**. Pouring concrete for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #19 |
| 22 | `4S-SS-B-03.200` | **Laying of PT Tendon**. Laying the post-tensioning steel cables in the slab (they are stressed later). | 4 | #20, Procurement: Civil work › PT Works |
| 23 | `4S-SS-B-03.95` | **Shuttering of Staircase upto Flight 2**. Erecting formwork for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 3 | #21 |
| 24 | `4S-SS-B-03.230` | **Reinforcement Top Net**. Fixing the top mesh of slab steel. | 3 | #22 |
| 25 | `4S-SS-B-03.100` | **Reinforcement of Staircase upto Flight 2**. Fixing the steel bars for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 3 | #23 |
| 26 | `4S-SS-B-03.235` | **MEP Coordination**. A check that all pipes, ducts, sleeves and conduits are placed correctly before concrete is cast, so nothing has to be broken out later. | 1 | #25, #24 |
| 27 | `4S-SS-B-03.255` | **Concrete of Slab**. Pouring and compacting the concrete for the floor slab. | 1 | #26 |
| 28 | `4S-SS-B-03.265` | **Wait for Strength Gain**. No work, only time: the concrete must reach the strength needed before it is stressed, loaded or its formwork is removed. | 6 | #27 |
| 29 | `4S-SS-B-03.305` | **PT Work**. Post-tensioning: stressing the steel cables in the slab with jacks and grouting them. It can only start once the slab concrete has gained strength. | 6 | #28 |

### C. Basement 03 grade slab (Pour 1)

The grade slab is the lowest slab of the basement. In this schedule its first step, deshuttering, waits for the Basement 01 slab concrete of the same pour. This is an unusual order and it should be confirmed with site. It may reflect a top-down or staged method.

*Where in the schedule: Construction > Hotel 4 Star > Substructure > Basement 03(Grade Slab) > Pour 1*

6 activities, planned (early dates) 2026-12-03 to 2027-01-02. Triggered by: Design: GFC drawing issued on site; Basement 01 › Pour 1 › Slab. Releases: Common Basements MEP & Finishes: Basement 03 › Hotel 4 Star › Wet Finishes.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Deshuttering (4wd) → #2 Waterproofing (5wd) → #3 Reinforcement (10wd) → #5 MEP Coordination (2wd) → #6 Concrete (4wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SS-GS10` | **Deshuttering**. Removing the formwork and props once the concrete has gained enough strength. | 4 | Basement 01 › Pour 1 › Slab |
| 2 | `4S-SS-GS15` | **Waterproofing**. Applying waterproofing to stop water getting through. | 5 | #1 |
| 3 | `4S-SS-GS20` | **Reinforcement**. Cutting, bending and tying the steel bars for Pour 1. This is inspected before the formwork is closed. | 10 | #2, Design: GFC drawing issued on site |
| 4 | `4S-SS-GS25` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for Pour 1. | 2 | #3 |
| 5 | `4S-SS-GS30` | **MEP Coordination**. A check that all pipes, ducts, sleeves and conduits are placed correctly before concrete is cast, so nothing has to be broken out later. | 2 | #3 |
| 6 | `4S-SS-GS40` | **Concrete**. Pouring and compacting the concrete for Pour 1. | 4 | #5, #4 |

### D. Basement 01: a pour with two lifts of columns

In Basement 01 the columns and walls are cast in two lifts (first and second), each with its own steel, formwork and concrete. After both lifts and the stairs, the slab is cast. This pour releases the Ground Floor pours above it.

*Where in the schedule: Construction > Hotel 4 Star > Substructure > Basement 01 > Pour 1*

42 activities, planned (early dates) 2026-10-21 to 2026-12-16. Triggered by: Design: GFC drawing issued on site; Design: shop drawing approved; Basement 02 › Pour 1 › Slab; Milestone: Completion of Mobilisation. Releases: Ground Floor › Pour 1 › Staircase - 1; Substructure › Basement 03(Grade Slab) › Pour 1; Ground Floor › Pour 1 › Staircase - 2; Ground Floor › Pour 1 › Column, Core Wall, Shear Wall - First Li; Ground Floor › Pour 1 › Slab; Milestone: 4 Star Sub Structure Completion.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Reinforcement (4wd) → #3 LPS (1wd) → #5 Shuttering (4wd) → #7 Concrete (1wd) → #9 Reinforcement (4wd) → #11 LPS (1wd) → #13 Shuttering (4wd) → #15 Concrete (1wd) → #17 Shuttering (5wd) → #19 Reinforcement Bottom Net with chai (3wd) → #21 Laying of PT Tendon (4wd) → #23 Reinforcement Top Net (3wd) → #39 MEP Coordination (1wd) → #40 Concrete of Slab (1wd) → #41 Wait for Strength Gain (6wd) → #42 PT Work (6wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SS-B-01.10` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 4 | Basement 02 › Pour 1 › Slab, Design: GFC drawing issued on site |
| 2 | `4S-SS-B-01.15` | **Reinforcement of wall upto Flight 1**. Fixing the steel bars for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 2 | Basement 02 › Pour 1 › Slab |
| 3 | `4S-SS-B-01.25` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 1 | #1 |
| 4 | `4S-SS-B-01.20` | **Shuttering of wall upto Flight 1**. Erecting formwork for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 2 | #2 |
| 5 | `4S-SS-B-01.35` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 4 | #1, #3 |
| 6 | `4S-SS-B-01.30` | **Casting of wall upto Flight 1**. Pouring concrete for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #4 |
| 7 | `4S-SS-B-01.60` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 1 | #5 |
| 8 | `4S-SS-B-01.40` | **Shuttering of Staircase upto Flight 1**. Erecting formwork for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #6 |
| 9 | `4S-SS-B-01.70` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 4 | #7 |
| 10 | `4S-SS-B-01.45` | **Reinforcement of Staircase upto Flight 1**. Fixing the steel bars for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #8 |
| 11 | `4S-SS-B-01.90` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 1 | #9 |
| 12 | `4S-SS-B-01.50` | **MEP coordination upto Flight 1**. Checking that pipes, sleeves and conduits are placed correctly in the stair core up to flight 1 before casting continues. | 1 | #10 |
| 13 | `4S-SS-B-01.95` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 4 | #9, #11 |
| 14 | `4S-SS-B-01.55` | **Casting of Staircase upto Flight 1**. Pouring concrete for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #12 |
| 15 | `4S-SS-B-01.120` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 1 | #13 |
| 16 | `4S-SS-B-01.65` | **Reinforcement of wall upto Flight 2**. Fixing the steel bars for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 2 | #14 |
| 17 | `4S-SS-B-01.125` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the slab. | 5 | #15 |
| 18 | `4S-SS-B-01.75` | **Shuttering of wall upto Flight 2**. Erecting formwork for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 2 | #16 |
| 19 | `4S-SS-B-01.175` | **Reinforcement Bottom Net with chairs**. Fixing the bottom mesh of slab steel, raised on small supports ("chairs") so that concrete covers it. | 3 | #17 |
| 20 | `4S-SS-B-01.80` | **Casting of wall upto Flight 2**. Pouring concrete for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #18 |
| 21 | `4S-SS-B-01.215` | **Laying of PT Tendon**. Laying the post-tensioning steel cables in the slab (they are stressed later). | 4 | #19, Design: shop drawing approved |
| 22 | `4S-SS-B-01.85` | **Shuttering of Staircase upto Flight 2**. Erecting formwork for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #20 |
| 23 | `4S-SS-B-01.255` | **Reinforcement Top Net**. Fixing the top mesh of slab steel. | 3 | #21 |
| 24 | `4S-SS-B-01.100` | **Reinforcement of Staircase upto Flight 2**. Fixing the steel bars for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #22 |
| 25 | `4S-SS-B-01.105` | **MEP coordination upto Flight 2**. Checking that pipes, sleeves and conduits are placed correctly in the stair core up to flight 2 before casting continues. | 1 | #24 |
| 26 | `4S-SS-B-01.110` | **Casting of Staircase upto Flight 2**. Pouring concrete for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #25 |
| 27 | `4S-SS-B-01.115` | **Reinforcement of wall upto Flight 3**. Fixing the steel bars for the stair-core wall, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 2 | #26 |
| 28 | `4S-SS-B-01.135` | **Shuttering of wall upto Flight 3**. Erecting formwork for the stair-core wall, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 2 | #27 |
| 29 | `4S-SS-B-01.145` | **Casting of wall upto Flight 3**. Pouring concrete for the stair-core wall, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 1 | #28 |
| 30 | `4S-SS-B-01.155` | **Shuttering of Staircase upto Flight 3**. Erecting formwork for the stair flight, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 1 | #29 |
| 31 | `4S-SS-B-01.165` | **Reinforcement of Staircase upto Flight 3**. Fixing the steel bars for the stair flight, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 1 | #30 |
| 32 | `4S-SS-B-01.185` | **MEP coordination upto Flight 3**. Checking that pipes, sleeves and conduits are placed correctly in the stair core up to flight 3 before casting continues. | 1 | #31 |
| 33 | `4S-SS-B-01.195` | **Casting of Staircase upto Flight 3**. Pouring concrete for the stair flight, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 1 | #32 |
| 34 | `4S-SS-B-01.205` | **Reinforcement of wall upto Flight 4**. Fixing the steel bars for the stair-core wall, up to the level of flight 4. The stair core is built flight by flight, together with the wall around it. | 2 | #33 |
| 35 | `4S-SS-B-01.230` | **Shuttering of wall upto Flight 4**. Erecting formwork for the stair-core wall, up to the level of flight 4. The stair core is built flight by flight, together with the wall around it. | 2 | #34 |
| 36 | `4S-SS-B-01.245` | **Casting of wall upto Flight 4**. Pouring concrete for the stair-core wall, up to the level of flight 4. The stair core is built flight by flight, together with the wall around it. | 1 | #35 |
| 37 | `4S-SS-B-01.260` | **Shuttering of Staircase upto Flight 4**. Erecting formwork for the stair flight, up to the level of flight 4. The stair core is built flight by flight, together with the wall around it. | 1 | #36 |
| 38 | `4S-SS-B-01.265` | **Reinforcement of Staircase upto Flight 4**. Fixing the steel bars for the stair flight, up to the level of flight 4. The stair core is built flight by flight, together with the wall around it. | 1 | #37 |
| 39 | `4S-SS-B-01.285` | **MEP Coordination**. A check that all pipes, ducts, sleeves and conduits are placed correctly before concrete is cast, so nothing has to be broken out later. | 1 | #19, #38, #23 |
| 40 | `4S-SS-B-01.300` | **Concrete of Slab**. Pouring and compacting the concrete for the floor slab. | 1 | #39, Milestone: Completion of Mobilisation |
| 41 | `4S-SS-B-01.310` | **Wait for Strength Gain**. No work, only time: the concrete must reach the strength needed before it is stressed, loaded or its formwork is removed. | 6 | #40 |
| 42 | `4S-SS-B-01.355` | **PT Work**. Post-tensioning: stressing the steel cables in the slab with jacks and grouting them. It can only start once the slab concrete has gained strength. | 6 | #41, Basement 02 › Pour 1 › Slab |

### E. Ground Floor Pour 2: the standard superstructure pour

This is the pattern behind almost every floor in every building. Columns and walls are built first (steel, formwork, lightning protection, concrete). The stair core goes up flight by flight alongside it. Then the slab: formwork, bottom steel, PT cables, MEP coordination, top steel, concrete, a waiting period for strength gain, and finally PT stressing. The same pour on the next floor up starts only after this slab is cast.

*Where in the schedule: Construction > Hotel 4 Star > Superstructure > Ground Floor > Pour 2*

35 activities, planned (early dates) 2026-12-26 to 2027-02-11. Triggered by: Basement 01 › Pour 2 › Slab. Releases: First Floor › Pour 2 › Staircase; First Floor › Pour 2 › Column, Core Wall, Shear Wall - First Lif; First Floor › Pour 2 › Slab.

Driving chain inside the block (the sequence of latest-finishing predecessors): #2 Reinforcement (3wd) → #4 LPS (1wd) → #6 Shuttering (3wd) → #8 Concrete (1wd) → #10 Reinforcement (3wd) → #12 LPS (1wd) → #14 Shuttering (3wd) → #16 Concrete (1wd) → #18 Shuttering (5wd) → #20 Reinforcement Bottom Net with chai (2wd) → #22 Laying of PT Tendon (2wd) → #24 Reinforcement Top Net (2wd) → #32 MEP Coordination (1wd) → #33 Concrete of Slab (1wd) → #34 Wait for Strength Gain (6wd) → #35 PT Work (4wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SS-GF.205` | **Reinforcement of wall upto Flight 1**. Fixing the steel bars for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 2 | Basement 01 › Pour 2 › Slab |
| 2 | `4S-SS-GF.220` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 3 | Basement 01 › Pour 2 › Slab |
| 3 | `4S-SS-GF.230` | **Shuttering of wall upto Flight 1**. Erecting formwork for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 2 | #1 |
| 4 | `4S-SS-GF.255` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 1 | #2 |
| 5 | `4S-SS-GF.265` | **Casting of wall upto Flight 1**. Pouring concrete for the stair-core wall, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #3 |
| 6 | `4S-SS-GF.280` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 3 | #2, #4 |
| 7 | `4S-SS-GF.285` | **Shuttering of Staircase upto Flight 1**. Erecting formwork for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #5 |
| 8 | `4S-SS-GF.300` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 1 | #6 |
| 9 | `4S-SS-GF.290` | **Reinforcement of Staircase upto Flight 1**. Fixing the steel bars for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #7 |
| 10 | `4S-SS-GF.310` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 3 | #8 |
| 11 | `4S-SS-GF.295` | **MEP coordination upto Flight 1**. Checking that pipes, sleeves and conduits are placed correctly in the stair core up to flight 1 before casting continues. | 1 | #9 |
| 12 | `4S-SS-GF.335` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 1 | #10 |
| 13 | `4S-SS-GF.315` | **Casting of Staircase upto Flight 1**. Pouring concrete for the stair flight, up to the level of flight 1. The stair core is built flight by flight, together with the wall around it. | 1 | #11 |
| 14 | `4S-SS-GF.350` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 3 | #10, #12 |
| 15 | `4S-SS-GF.320` | **Reinforcement of wall upto Flight 2**. Fixing the steel bars for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 2 | #13 |
| 16 | `4S-SS-GF.365` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 1 | #14 |
| 17 | `4S-SS-GF.340` | **Shuttering of wall upto Flight 2**. Erecting formwork for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 2 | #15 |
| 18 | `4S-SS-GF.375` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the slab. | 5 | #16 |
| 19 | `4S-SS-GF.355` | **Casting of wall upto Flight 2**. Pouring concrete for the stair-core wall, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #17 |
| 20 | `4S-SS-GF.405` | **Reinforcement Bottom Net with chairs**. Fixing the bottom mesh of slab steel, raised on small supports ("chairs") so that concrete covers it. | 2 | #18 |
| 21 | `4S-SS-GF.360` | **Shuttering of Staircase upto Flight 2**. Erecting formwork for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #19 |
| 22 | `4S-SS-GF.435` | **Laying of PT Tendon**. Laying the post-tensioning steel cables in the slab (they are stressed later). | 2 | #20 |
| 23 | `4S-SS-GF.370` | **Reinforcement of Staircase upto Flight 2**. Fixing the steel bars for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #21 |
| 24 | `4S-SS-GF.475` | **Reinforcement Top Net**. Fixing the top mesh of slab steel. | 2 | #22 |
| 25 | `4S-SS-GF.380` | **MEP coordination upto Flight 2**. Checking that pipes, sleeves and conduits are placed correctly in the stair core up to flight 2 before casting continues. | 1 | #23 |
| 26 | `4S-SS-GF.385` | **Casting of Staircase upto Flight 2**. Pouring concrete for the stair flight, up to the level of flight 2. The stair core is built flight by flight, together with the wall around it. | 1 | #25 |
| 27 | `4S-SS-GF.395` | **Reinforcement of wall upto Flight 3**. Fixing the steel bars for the stair-core wall, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 2 | #26 |
| 28 | `4S-SS-GF.400` | **Shuttering of wall upto Flight 3**. Erecting formwork for the stair-core wall, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 2 | #27 |
| 29 | `4S-SS-GF.420` | **Casting of wall upto Flight 3**. Pouring concrete for the stair-core wall, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 1 | #28 |
| 30 | `4S-SS-GF.430` | **Shuttering of Staircase upto Flight 3**. Erecting formwork for the stair flight, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 1 | #29 |
| 31 | `4S-SS-GF.440` | **Reinforcement of Staircase upto Flight 3**. Fixing the steel bars for the stair flight, up to the level of flight 3. The stair core is built flight by flight, together with the wall around it. | 1 | #30 |
| 32 | `4S-SS-GF.495` | **MEP Coordination**. A check that all pipes, ducts, sleeves and conduits are placed correctly before concrete is cast, so nothing has to be broken out later. | 1 | #20, #24, #31 |
| 33 | `4S-SS-GF.505` | **Concrete of Slab**. Pouring and compacting the concrete for the floor slab. | 1 | #32 |
| 34 | `4S-SS-GF.510` | **Wait for Strength Gain**. No work, only time: the concrete must reach the strength needed before it is stressed, loaded or its formwork is removed. | 6 | #33 |
| 35 | `4S-SS-GF.585` | **PT Work**. Post-tensioning: stressing the steel cables in the slab with jacks and grouting them. It can only start once the slab concrete has gained strength. | 4 | #34, Basement 01 › Pour 2 › Slab |

### F. Ground Floor Pour 4: a pour with columns and slab only

Not every pour has a staircase. A pour without a stair core has just two steps per element: columns (two lifts) and the slab. It is the same cycle with fewer activities.

*Where in the schedule: Construction > Hotel 4 Star > Superstructure > Ground Floor > Pour 4*

16 activities, planned (early dates) 2026-12-29 to 2027-02-06. Triggered by: Basement 01 › Pour 3 › Slab; Basement 01 › Pour 4 › Slab. Releases: First Floor › Pour 4 › Column - First Lift; First Floor › Pour 3 › Slab.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Reinforcement (2wd) → #2 LPS (1wd) → #3 Shuttering (1wd) → #4 Concrete (1wd) → #5 Reinforcement (2wd) → #6 LPS (1wd) → #7 Shuttering (2wd) → #8 Concrete (1wd) → #9 Shuttering (4wd) → #10 Reinforcement Bottom Net with chai (2wd) → #11 Laying of PT Tendon (2wd) → #12 Reinforcement Top Net (2wd) → #13 MEP Coordination (1wd) → #14 Concrete of Slab (1wd) → #15 Wait for Strength Gain (6wd) → #16 PT Work (4wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SS-GF.525` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 2 | Basement 01 › Pour 3 › Slab |
| 2 | `4S-SS-GF.540` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 1 | #1 |
| 3 | `4S-SS-GF.550` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 1 | #1, #2 |
| 4 | `4S-SS-GF.565` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 1 | #3 |
| 5 | `4S-SS-GF.575` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 2 | #4 |
| 6 | `4S-SS-GF.595` | **LPS**. Lightning protection system: the earthing and down-conductor work embedded in the structure before concrete is cast. The assumptions document lists LPS as a cost item split into horizontal and vertical. | 1 | #5 |
| 7 | `4S-SS-GF.610` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 2 | #5, #6 |
| 8 | `4S-SS-GF.630` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 1 | #7 |
| 9 | `4S-SS-GF.640` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the slab. | 4 | #8 |
| 10 | `4S-SS-GF.675` | **Reinforcement Bottom Net with chairs**. Fixing the bottom mesh of slab steel, raised on small supports ("chairs") so that concrete covers it. | 2 | #9 |
| 11 | `4S-SS-GF.700` | **Laying of PT Tendon**. Laying the post-tensioning steel cables in the slab (they are stressed later). | 2 | #10 |
| 12 | `4S-SS-GF.725` | **Reinforcement Top Net**. Fixing the top mesh of slab steel. | 2 | #11 |
| 13 | `4S-SS-GF.735` | **MEP Coordination**. A check that all pipes, ducts, sleeves and conduits are placed correctly before concrete is cast, so nothing has to be broken out later. | 1 | #10, #12 |
| 14 | `4S-SS-GF.740` | **Concrete of Slab**. Pouring and compacting the concrete for the floor slab. | 1 | #13 |
| 15 | `4S-SS-GF.750` | **Wait for Strength Gain**. No work, only time: the concrete must reach the strength needed before it is stressed, loaded or its formwork is removed. | 6 | #14 |
| 16 | `4S-SS-GF.765` | **PT Work**. Post-tensioning: stressing the steel cables in the slab with jacks and grouting them. It can only start once the slab concrete has gained strength. | 4 | #15, Basement 01 › Pour 4 › Slab |

### G. Roof Top

The roof slab closes the structure. It matters beyond the roof: the top floor finishes, the terrace waterproofing, the facade steel and the vertical transport all wait for it.

*Where in the schedule: Construction > Hotel 4 Star > Superstructure > Roof Top*

7 activities, planned (early dates) 2027-09-02 to 2027-09-30. Triggered by: Sixth Floor › Pour 3 › Slab; Design: GFC drawing issued on site; Sixth Floor › Pour 1 › Slab; Sixth Floor › Pour 2 › Slab. Releases: Wet finishes, MEP, ID › Sixth Floor › Wet Finishes; Hotel 4 Star › Terrace Works; Design: As Built Drawings › Structural; Hotel 4 Star › Vertical Transport; Milestone: 4 Star Super Structure Completion; Hotel 4 Star › Structural Steel works for Facade.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Reinforcement (4wd) → #2 Shuttering (4wd) → #3 Concrete (1wd) → #4 Shuttering (5wd) → #5 Reinforcement (5wd) → #6 MEP Coordination (1wd) → #7 Concrete of Slab (1wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SS-Roof10` | **Reinforcement**. Cutting, bending and tying the steel bars for the columns, core wall and shear wall. This is inspected before the formwork is closed. | 4 | Sixth Floor › Pour 3 › Slab, Design: GFC drawing issued on site |
| 2 | `4S-SS-Roof15` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the columns, core wall and shear wall. | 4 | #1 |
| 3 | `4S-SS-Roof20` | **Concrete**. Pouring and compacting the concrete for the columns, core wall and shear wall. | 1 | #2 |
| 4 | `4S-SS-Roof25` | **Shuttering**. Erecting the formwork (moulds) that will hold the wet concrete in shape for the slab. | 5 | #3 |
| 5 | `4S-SS-Roof30` | **Reinforcement**. Cutting, bending and tying the steel bars for the slab. This is inspected before the formwork is closed. | 5 | #4 |
| 6 | `4S-SS-Roof35` | **MEP Coordination**. A check that all pipes, ducts, sleeves and conduits are placed correctly before concrete is cast, so nothing has to be broken out later. | 1 | #5 |
| 7 | `4S-SS-Roof40` | **Concrete of Slab**. Pouring and compacting the concrete for the floor slab. | 1 | #6, Sixth Floor › Pour 1 › Slab, Sixth Floor › Pour 2 › Slab |

### H. Floor finishes: wet finishes (Second Floor)

These are the first activities of a finishing floor: removing slab formwork, building walls, and the two parallel runs of slab conduiting. They start when the slab above is cast and the architectural and MEP drawings have been issued.

*Where in the schedule: Construction > Hotel 4 Star > Wet finishes, MEP, ID > Second Floor > Wet Finishes*

4 activities, planned (early dates) 2027-05-27 to 2027-09-06. Triggered by: Third Floor › Pour 3 › Slab; Design: GFC drawing issued on site; MEP 1st Fix, 2nd Fix › Electrical › 1st Fix; MEP 1st Fix, 2nd Fix › ELV › 1st Fix. Releases: MEP 1st Fix, 2nd Fix › Electrical › 1st Fix; MEP 1st Fix, 2nd Fix › ELV › 1st Fix; MEP 1st Fix, 2nd Fix › Plumbing › 1st Fix; MEP 1st Fix, 2nd Fix › Firefighting › 1st Fix; MEP 1st Fix, 2nd Fix › HVAC › 1st Fix; MEP 1st Fix, 2nd Fix › Electrical › 2nd Fix and 2 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Deshuttering (4wd) → #2 Brickwork/Blockwork (30wd) → #3 Waterproofing of Toilets, Balcony  (18wd) → #4 Plaster (18wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-WMI-2nd10` | **Deshuttering**. Removing the formwork and props once the concrete has gained enough strength. | 4 | Third Floor › Pour 3 › Slab |
| 2 | `4S-WMI-2nd15` | **Brickwork/Blockwork**. Building the internal and external walls of the floor with bricks or blocks. | 30 | #1, Design: GFC drawing issued on site |
| 3 | `4S-WMI-2nd55` | **Waterproofing of Toilets, Balcony & Kitchen**. Applying waterproofing in wet areas so that water does not leak to the floor below. | 18 | #2 |
| 4 | `4S-WMI-2nd95` | **Plaster**. Plastering the walls (and ceilings where specified). | 18 | #3, MEP 1st Fix, 2nd Fix › Electrical › 1st Fix x2, MEP 1st Fix, 2nd Fix › ELV › 1st Fix |

### I. Floor finishes: MEP first fix and second fix (Second Floor)

The five MEP trades (HVAC, electrical, plumbing, fire-fighting, ELV) each run in two stages: first fix (the concealed pipes, conduits and supports, done before plaster) and second fix (the visible equipment, done after ceilings and walls). Their tasks are chained inside each trade, and the trades meet at shared points such as plaster, risers and testing.

*Where in the schedule: Construction > Hotel 4 Star > Wet finishes, MEP, ID > Second Floor > MEP 1st Fix, 2nd Fix*

43 activities, planned (early dates) 2027-06-01 to 2027-12-06. Triggered by: Design: GFC drawing issued on site; Wet finishes, MEP, ID › Second Floor › Wet Finishes. Releases: Wet finishes, MEP, ID › Second Floor › Wet Finishes; Front Face - Toward Airport › MEP Final Fix › Plumbing; +2 more outside groups; Front Face - Toward Airport › MEP Final Fix › HVAC; Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor; Front Face - Toward Airport › MEP Final Fix › Electrical and 2 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #5 Cable tray laying (15wd) → #14 Cabling & Wire Pulling (30wd) → #20 DB fixing and connecting (10wd) → #30 Floor/Distribution Panel Installat (10wd) → #37 Equipment Earthing (10wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-WMI-2nd20` | **Slab Conduiting**. Laying the electrical conduits in or on the slab. | 35 | Wet finishes, MEP, ID › Second Floor › Wet Finishes, Design: GFC drawing issued on site |
| 2 | `4S-WMI-2nd30` | **Wall Conduiting**. Laying electrical conduits inside the walls. | 30 | Wet finishes, MEP, ID › Second Floor › Wet Finishes, Design: GFC drawing issued on site |
| 3 | `4S-WMI-2nd40` | **Fixing pipe supports and hangers**. Fixing hangers and supports that will hold pipes under the slab. | 35 | Wet finishes, MEP, ID › Second Floor › Wet Finishes, Design: GFC drawing issued on site |
| 4 | `4S-WMI-2nd35` | **Fixing pipe supports and clamps**. Fixing the clamps and supports that will hold pipes in place. | 20 | Wet finishes, MEP, ID › Second Floor › Wet Finishes, Design: GFC drawing issued on site |
| 5 | `4S-WMI-2nd115` | **Cable tray laying**. Laying out and fixing the cable trays along their routes before cables are pulled. | 15 | Wet finishes, MEP, ID › Second Floor › Wet Finishes |
| 6 | `4S-WMI-2nd25` | **Slab Conduiting**. Laying the electrical conduits in or on the slab. | 35 | Wet finishes, MEP, ID › Second Floor › Wet Finishes, Design: GFC drawing issued on site |
| 7 | `4S-WMI-2nd45` | **Wall Conduiting**. Laying electrical conduits inside the walls. | 30 | Wet finishes, MEP, ID › Second Floor › Wet Finishes, Design: GFC drawing issued on site |
| 8 | `4S-WMI-2nd50` | **Duct Support Fabrication**. Making the steel hangers and supports that will hold the AC ducts. | 35 | Wet finishes, MEP, ID › Second Floor › Wet Finishes, Design: GFC drawing issued on site |
| 9 | `4S-WMI-2nd125` | **Cable tray installation**. Fixing the metal trays that carry cables along ceilings and shafts. | 15 | Wet finishes, MEP, ID › Second Floor › Wet Finishes |
| 10 | `4S-WMI-2nd75` | **Installing back boxes for switches, sockets**. Fixing the embedded boxes inside walls where switches and sockets will go. | 5 | #2, #1, Design: GFC drawing issued on site |
| 11 | `4S-WMI-2nd105` | **Laying branch piping**. Laying the branch pipes that run from the main lines to each point of use. | 35 | #3, Design: GFC drawing issued on site |
| 12 | `4S-WMI-2nd65` | **Laying drainage pipes (soil, waste, vent)**. Laying drainage pipes: soil, waste and vent. | 25 | #4, Design: GFC drawing issued on site |
| 13 | `4S-WMI-2nd60` | **Laying water supply pipes (hot & cold)**. Laying the hot and cold water supply pipes. | 35 | #4, Design: GFC drawing issued on site |
| 14 | `4S-WMI-2nd155` | **Cabling & Wire Pulling**. Pulling power cables and wires through conduits and trays. | 30 | #5 |
| 15 | `4S-WMI-2nd80` | **Installing back boxes for switches, sockets**. Fixing the embedded boxes inside walls where switches and sockets will go. | 5 | #7, #6, Design: GFC drawing issued on site |
| 16 | `4S-WMI-2nd100` | **Installing duct hangers and supports**. Installing the hangers and supports that hold the ducts. | 30 | #8, Design: GFC drawing issued on site |
| 17 | `4S-WMI-2nd165` | **Cabeling of ELV cable - IT/Fire Alarm/Public Address**. Pulling extra-low-voltage cables (data/IT, fire alarm, public address) through the trays and conduits. | 25 | #9 |
| 18 | `4S-WMI-2nd150` | **Hydrostatic pressure testing of piping**. Testing pipes with water under pressure to check for leaks. | 10 | #11, Design: GFC drawing issued on site |
| 19 | `4S-WMI-2nd70` | **Installation of plumbing fixture base supports (WC frames, sink brackets)**. Installing the supports for toilet and sink fixtures before the walls are closed. | 10 | #12, Design: GFC drawing issued on site |
| 20 | `4S-WMI-2nd240` | **DB fixing and connecting**. Mounting the distribution board (floor electrical panel) and connecting its cables. | 10 | #14 |
| 21 | `4S-WMI-2nd245` | **Floor Rising Main Installation**. Installing the vertical electrical main that feeds this floor. | 10 | #14 |
| 22 | `4S-WMI-2nd140` | **Duct installation**. Fitting the air-conditioning ductwork. | 10 | #16 |
| 23 | `4S-WMI-2nd130` | **Laying concealed/exposed refrigerant piping**. Laying the refrigerant pipes for the AC system. | 20 | #16, Design: GFC drawing issued on site |
| 24 | `4S-WMI-2nd135` | **Laying concealed/exposed drain piping**. Laying the AC condensate drain pipes. | 20 | #16, Design: GFC drawing issued on site |
| 25 | `4S-WMI-2nd210` | **ELV Rack Installation**. Installing the cabinets (racks) for network and security equipment. | 15 | #17 |
| 26 | `4S-WMI-2nd175` | **Installation of vertical risers and distribution piping in shafts**. Installing the vertical pipes in the service shafts and the distribution pipes from them. | 15 | #18, Wet finishes, MEP, ID › Second Floor › Wet Finishes |
| 27 | `4S-WMI-2nd180` | **Painting/insulation of exposed fire pipes**. Painting and insulating the exposed fire-fighting pipes. | 10 | #18 |
| 28 | `4S-WMI-2nd85` | **Pressure testing of water supply lines**. Pressure-testing the water supply pipes for leaks. | 10 | #13, #12, #19, Design: GFC drawing issued on site |
| 29 | `4S-WMI-2nd90` | **Installation of concealed parts of toilet fixtures**. Installing the parts of toilet fixtures that sit inside walls (cisterns and frames). | 20 | #19, Design: GFC drawing issued on site |
| 30 | `4S-WMI-2nd330` | **Floor/Distribution Panel Installation**. Installing the floor distribution panel. | 10 | #20 |
| 31 | `4S-WMI-2nd170` | **Insulation of ducts (thermal/acoustic)**. Wrapping the ducts with thermal or acoustic insulation. | 10 | #22 |
| 32 | `4S-WMI-2nd260` | **Termination of cables at junction boxes, patch panels, and control panels**. Connecting cable ends at junction boxes, patch panels and control panels. | 10 | #25 |
| 33 | `4S-WMI-2nd230` | **Installation of sprinkler branch lines in ceilings**. Installing the sprinkler pipework above the ceiling. | 30 | #26 |
| 34 | `4S-WMI-2nd110` | **Insulation of hot water pipes (if applicable)**. Insulating hot-water pipes. | 20 | #28 |
| 35 | `4S-WMI-2nd205` | **Testing risers and branch lines for leakage**. Testing the vertical risers and branch lines for leaks. | 15 | #27 |
| 36 | `4S-WMI-2nd120` | **Installation of vertical risers and main distribution lines**. Installing vertical risers and the main distribution lines. | 35 | #28, #29, Wet finishes, MEP, ID › Second Floor › Wet Finishes |
| 37 | `4S-WMI-2nd480` | **Equipment Earthing**. Connecting equipment to the earthing (grounding) system for safety. | 10 | #30, #21 |
| 38 | `4S-WMI-2nd200` | **Installation of chilled water piping / VRF piping**. Installing the chilled-water or VRF refrigerant piping for air conditioning. | 10 | #31, #23, #24 |
| 39 | `4S-WMI-2nd415` | **Fixing devices like CCTV camera bases, card reader bases, smoke detector bases, PA Bases, Wifi Bases**. Fixing the mounting bases for security, fire and network devices before the devices themselves are installed. | 10 | #32 |
| 40 | `4S-WMI-2nd145` | **Testing drainage lines for leakage/blockage**. Testing the drainage lines for leaks and blockages. | 35 | #19, #34 |
| 41 | `4S-WMI-2nd160` | **Fixing floor traps and gully traps**. Fixing the drain traps in floors so that water can drain and odours are blocked. | 15 | #36 |
| 42 | `4S-WMI-2nd285` | **Installation of indoor units including AHU, FCU**. Installing the AC indoor units: air handling units and fan coil units. | 20 | #38, #23, #24 |
| 43 | `4S-WMI-2nd530` | **Connecting refrigerant and drain piping to indoor units**. Final connection of the AC indoor units to the refrigerant pipes and the condensate drain pipes. | 10 | #42 |

### J. Floor finishes: dry finishes and ID works, front face (Second Floor)

Each floor is split into three faces (front, back and side). Interior finishes begin once the facade for that face is fixed and the step named "Running of Wild Air" is done. The same pattern repeats for the other two faces.

*Where in the schedule: Construction > Hotel 4 Star > Wet finishes, MEP, ID > Second Floor > Front Face - Toward Airport > Dry Finishes/ID Works*

12 activities, planned (early dates) 2027-12-03 to 2028-08-14. Triggered by: Design: GFC drawing issued on site; Procurement: Finishes/ID Work - Hotels & CC › Furniture; Procurement: Finishes/ID Work - Hotels & CC › Wall Cladding; Procurement: Finishes/ID Work - Hotels & CC › ID Flooring; Procurement: Finishes/ID Work - Hotels & CC › Soft Furnishi; Procurement: Finishes/ID Work - Hotels & CC › False Ceiling and 2 more. Releases: Front Face - Toward Airport › MEP Final Fix › Plumbing; Front Face - Toward Airport › MEP Final Fix › Electrical; Front Face - Toward Airport › MEP Final Fix › HVAC; Front Face - Toward Airport › MEP Final Fix › Firefighting; +2 more outside groups; Milestone: 4 Star Hotel Commencement and 2 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Running of Wild Air (1wd) → #3 Wall finish ID Works (35wd) → #4 False Ceiling Installation (35wd) → #5 Flooring of toilets/kitchen/Balcon (10wd) → #6 Putty & First Coat of Paint (10wd) → #8 Wooden Flooring/Flooring (20wd) → #9 Fixed Furniture (40wd) → #10 Final coat of paint (10wd) → #11 Soft Furnishing & Signage (15wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-WMI-2nd195` | **Running of Wild Air**. A gate in the logic with no cost. The submitted assumptions document lists it as an HVAC second-fix item with 0% cost and says interior (ID) finishes start only after the facade and this step. My reading of the site meaning is running the AC or ventilation to dry and condition the space, which should still be confirmed with site. | 1 | Facade › Second Floor - Third Floor › Front Face - Toward Airpor, MEP 1st Fix, 2nd Fix › HVAC › 2nd Fix x5 |
| 2 | `4S-WMI-2nd695` | **False ceiling final finishes**. Finishing the false ceiling (putty, paint and touch-up). | 10 | Front Face - Toward Airport › MEP Final Fix › HVAC |
| 3 | `4S-WMI-2nd570` | **Wall finish ID Works**. Interior-design wall finishes (panelling, wallpaper, cladding). | 35 | #1, Design: GFC drawing issued on site, Procurement: Finishes/ID Work - Hotels & CC › Furniture, Procurement: Finishes/ID Work - Hotels & CC › Wall Cladding, Procurement: Finishes/ID Work - Hotels & CC › ID Flooring, Procurement: Finishes/ID Work - Hotels & CC › Soft Furnishi, Procurement: Finishes/ID Work - Hotels & CC › False Ceiling, Procurement: Finishes/ID Work - Hotels & CC › Doors, MEP 1st Fix, 2nd Fix › HVAC › 2nd Fix x5, MEP 1st Fix, 2nd Fix › Electrical › 2nd Fix x6, MEP 1st Fix, 2nd Fix › Plumbing › 2nd FIx x4, MEP 1st Fix, 2nd Fix › Firefighting › 2nd Fix x4, MEP 1st Fix, 2nd Fix › ELV › 2nd Fix x5 |
| 4 | `4S-WMI-2nd575` | **False Ceiling Installation**. Installing the false-ceiling frame and boards. | 35 | #3 |
| 5 | `4S-WMI-2nd585` | **Flooring of toilets/kitchen/Balcony**. Laying tiles or floor finish in toilets, kitchen and balcony (after waterproofing). | 10 | #4, Wet finishes, MEP, ID › Second Floor › Wet Finishes |
| 6 | `4S-WMI-2nd595` | **Putty & First Coat of Paint**. Applying wall putty and the first coat of paint. | 10 | #3, #5 |
| 7 | `4S-WMI-2nd590` | **Doors & Windows/Fire Doors/Shaft Doors**. Installing doors, windows, fire-rated doors and shaft doors. | 35 | #3, #5, Procurement: Misc › Fire Doors |
| 8 | `4S-WMI-2nd620` | **Wooden Flooring/Flooring**. Laying wooden or other final flooring. | 20 | #6 |
| 9 | `4S-WMI-2nd660` | **Fixed Furniture**. Installing built-in furniture (wardrobes, counters, fixed units). | 40 | #8 |
| 10 | `4S-WMI-2nd705` | **Final coat of paint**. Applying the last coat of paint. | 10 | #2, #9, #7, Front Face - Toward Airport › MEP Final Fix › Electrical, Front Face - Toward Airport › MEP Final Fix › Plumbing, Front Face - Toward Airport › MEP Final Fix › Firefighting x3, Front Face - Toward Airport › MEP Final Fix › ELV x6, Side Face › MEP Final Fix › Firefighting |
| 11 | `4S-WMI-2nd710` | **Soft Furnishing & Signage**. Curtains, soft furnishings and signage. | 15 | #10, Design: GFC drawing issued on site, Procurement: Misc › Signage |
| 12 | `4S-WMI-2nd715` | **Loose Furniture**. Placing loose furniture. | 15 | #10 |

### K. Floor finishes: MEP final fix, front face (Second Floor)

The final fix is the visible, finished side of MEP: switches, sockets, fixtures, grills, sprinkler heads, fire alarm and access control devices. It comes after the finishes and just before testing.

*Where in the schedule: Construction > Hotel 4 Star > Wet finishes, MEP, ID > Second Floor > Front Face - Toward Airport > MEP Final Fix*

19 activities, planned (early dates) 2028-04-11 to 2028-07-15. Triggered by: MEP 1st Fix, 2nd Fix › HVAC › 2nd Fix; MEP 1st Fix, 2nd Fix › Electrical › 2nd Fix; MEP 1st Fix, 2nd Fix › Plumbing › 2nd FIx; Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor; MEP 1st Fix, 2nd Fix › Firefighting › 2nd Fix; MEP 1st Fix, 2nd Fix › ELV › 2nd Fix and 2 more. Releases: Hotel 4 Star › Testing, Commissioning, HO › Second Floor; Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor.

Driving chain inside the block (the sequence of latest-finishing predecessors): #2 Switches & Socket (30wd) → #11 Light Fixtures (30wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-WMI-2nd580` | **Installing grills, diffusers, dampers**. Fitting the air grills, diffusers and dampers on the ductwork. | 30 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor |
| 2 | `4S-WMI-2nd600` | **Switches & Socket**. Fixing the switch and socket plates. | 30 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor |
| 3 | `4S-WMI-2nd605` | **Installation of sanitary fixtures (WC, washbasins, urinals, sinks)**. Installing the visible sanitary fixtures: toilets, washbasins, urinals and sinks. | 10 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor, MEP 1st Fix, 2nd Fix › Plumbing › 2nd FIx x2 |
| 4 | `4S-WMI-2nd610` | **Installation of hydrant accessories (valves, hose reels, cabinets)**. Installing fire hydrant accessories: valves, hose reels and cabinets. | 25 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor |
| 5 | `4S-WMI-2nd615` | **Installation of portable fire extinguishers**. Placing portable fire extinguishers. | 30 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor |
| 6 | `4S-WMI-2nd640` | **Installation of sprinkler heads, nozzles, and final alignment**. Fitting the sprinkler heads and aligning them with the finished ceiling. | 35 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor x2, MEP 1st Fix, 2nd Fix › Firefighting › 2nd Fix x2 |
| 7 | `4S-WMI-2nd645` | **Installation of data and Voice Faceplate**. Installing data and telephone outlet faceplates. | 25 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor x2, MEP 1st Fix, 2nd Fix › ELV › 2nd Fix, Design: GFC drawing issued on site, Procurement: MEP Work › ICT/Security, Procurement: MEP Work › BMS |
| 8 | `4S-WMI-2nd655` | **Installation of fire alarm devices + Public Address**. Installing fire alarm devices and public address speakers. | 10 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor x2, Design: GFC drawing issued on site, Procurement: MEP Work › ICT/Security, Procurement: MEP Work › BMS |
| 9 | `4S-WMI-2nd650` | **Installation of Camera & Wifi**. Installing CCTV cameras and Wi-Fi access points. | 30 | Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor x2, Design: GFC drawing issued on site, Procurement: MEP Work › ICT/Security, Procurement: MEP Work › BMS |
| 10 | `4S-WMI-2nd625` | **Installation of thermostats and control panels**. Installing room thermostats and AC control panels. | 30 | #1, Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor, MEP 1st Fix, 2nd Fix › HVAC › 2nd Fix |
| 11 | `4S-WMI-2nd665` | **Light Fixtures**. Installing light fittings. | 30 | #2, MEP 1st Fix, 2nd Fix › Electrical › 2nd Fix |
| 12 | `4S-WMI-2nd630` | **Installation of CP fittings (taps, mixers, showers, health faucets)**. Installing chrome-plated fittings: taps, mixers, showers and health faucets. | 10 | #3, Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor |
| 13 | `4S-WMI-2nd670` | **Integration with fire alarm system**. Connecting devices to the fire alarm system. | 20 | #5 |
| 14 | `4S-WMI-2nd680` | **Fire Panel Intallation & Integration**. Installing the fire alarm control panel and connecting it to the detectors. | 25 | #8 |
| 15 | `4S-WMI-2nd675` | **Installation of Active System**. Installing the active network equipment. | 15 | #8, Design: GFC drawing issued on site, Procurement: MEP Work › ICT/Security, Procurement: MEP Work › BMS |
| 16 | `4S-WMI-2nd685` | **Installation & Integration of Audio Visual System**. Installing and connecting the audio-visual system. | 25 | #8 |
| 17 | `4S-WMI-2nd690` | **Installation & Integration of Access Control**. Installing and connecting the door access control system. | 25 | #8 |
| 18 | `4S-WMI-2nd635` | **Connection of appliances**. Connecting appliances and equipment to their power, water or drain services. | 25 | #12 |
| 19 | `4S-WMI-2nd700` | **Integration of Active components**. Connecting the active network components into the system. | 15 | #15 |

### L. Facade zone (Second to Third Floor)

The facade is built zone by zone, not floor by floor with the structure. The schedule starts it only after the top structure is nearly complete (a finish-to-finish link with a lag). Within a zone, each face runs: MEP before facade, fix supports, fix facade, MEP after facade.

*Where in the schedule: Construction > Hotel 4 Star > Facade > Second Floor - Third Floor*

12 activities, planned (early dates) 2027-09-25 to 2028-01-11. Triggered by: Procurement: Facade › Glass Facade; Structural Steel Fabrication: Structural Steel Fabrication; Hotel 4 Star › Structural Steel works for Facade; Sixth Floor › Pour 3 › Slab. Releases: Facade › Third Floor - Fourth Floor › Front Face - Toward Airpor; Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor; Milestone: Project Completion Date; Facade › Third Floor - Fourth Floor › Back Face - Toward CC; Facade › GF to Service Floor › Front Face - Toward Airport; Milestone: 4 Star Hotel Commencement and 2 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Integration of Services Before Fac (5wd) → #3 Integration of Services Before Fac (5wd) → #5 Fixing of Facade Support (25wd) → #8 Fixing of Facade (25wd) → #10 Integration of Services After Faca (30wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-F-2nd10` | **Integration of Services Before Facade**. Completing the services (MEP) work that must be in place before the facade is fixed. | 5 | Sixth Floor › Pour 3 › Slab FS +7d |
| 2 | `4S-F-2nd15` | **Fixing of Facade Support**. Fixing the brackets and frames that will carry the facade. | 25 | #1 SS +2d, Procurement: Facade › Glass Facade, Structural Steel Fabrication: Structural Steel Fabrication, Sixth Floor › Pour 3 › Slab FF, Hotel 4 Star › Structural Steel works for Facade |
| 3 | `4S-F-2nd20` | **Integration of Services Before Facade**. Completing the services (MEP) work that must be in place before the facade is fixed. | 5 | #1 |
| 4 | `4S-F-2nd40` | **Fixing of Facade**. Fixing the facade (the external skin of glass, panels or cladding) on the building. | 25 | #2 |
| 5 | `4S-F-2nd25` | **Fixing of Facade Support**. Fixing the brackets and frames that will carry the facade. | 25 | #3 SS +2d |
| 6 | `4S-F-2nd30` | **Integration of Services Before Facade**. Completing the services (MEP) work that must be in place before the facade is fixed. | 5 | #3 |
| 7 | `4S-F-2nd60` | **Integration of Services After Facade**. Finishing the services (MEP) connections to the facade after the facade is fixed. | 30 | #4 |
| 8 | `4S-F-2nd50` | **Fixing of Facade**. Fixing the facade (the external skin of glass, panels or cladding) on the building. | 25 | #5 |
| 9 | `4S-F-2nd35` | **Fixing of Facade Support**. Fixing the brackets and frames that will carry the facade. | 15 | #6 SS +2d |
| 10 | `4S-F-2nd65` | **Integration of Services After Facade**. Finishing the services (MEP) connections to the facade after the facade is fixed. | 30 | #8 |
| 11 | `4S-F-2nd45` | **Fixing of Facade**. Fixing the facade (the external skin of glass, panels or cladding) on the building. | 20 | #9 |
| 12 | `4S-F-2nd55` | **Integration of Services After Facade**. Finishing the services (MEP) connections to the facade after the facade is fixed. | 30 | #11 |

### M. Structural steel for the facade (whole building)

Steel supports for the facade are done zone by zone from the middle upwards and downwards. They are triggered by the structure and by steel fabrication, and they release the facade support-fixing activities.

*Where in the schedule: Construction > Hotel 4 Star > Structural Steel works for Facade*

6 activities, planned (early dates) 2027-08-18 to 2028-03-15. Triggered by: Structural Steel Fabrication: Structural Steel Fabrication; Sixth Floor › Pour 1 › Slab; Sixth Floor › Pour 2 › Slab; Sixth Floor › Pour 3 › Slab; Superstructure › Roof Top › Slab. Releases: Facade › GF to Service Floor › Front Face - Toward Airport; Facade › Second Floor - Third Floor › Front Face - Toward Airpor; Facade › Third Floor - Fourth Floor › Front Face - Toward Airpor; Facade › Fourth Floor - Fifth Floor › Front Face - Toward Airpor; Facade › Fifth Floor - Sixth Floor › Front Face - Toward Airport; Facade › Sixth Floor - Terrace › Front Face - Toward Airport and 1 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Second Floor to Third Floor (28wd) → #2 GF to Service Floor (28wd) → #3 Third Floor to Fourth Floor (28wd) → #4 Fourth Floor to Fifth Floor (28wd) → #5 Fifth Floor to Sixth Floor (28wd) → #6 Sixth Floor to Terrace (24wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-F-SS10` | **Second Floor to Third Floor**. Structural steel work that supports the facade in this floor range. | 28 | Structural Steel Fabrication: Structural Steel Fabrication SS +90d, Sixth Floor › Pour 1 › Slab, Sixth Floor › Pour 2 › Slab FF +10d, Sixth Floor › Pour 3 › Slab FF +10d |
| 2 | `4S-F-SS15` | **GF to Service Floor**. Structural steel work that supports the facade in this floor range. | 28 | #1 |
| 3 | `4S-F-SS20` | **Third Floor to Fourth Floor**. Structural steel work that supports the facade in this floor range. | 28 | #2 |
| 4 | `4S-F-SS25` | **Fourth Floor to Fifth Floor**. Structural steel work that supports the facade in this floor range. | 28 | #3 |
| 5 | `4S-F-SS30` | **Fifth Floor to Sixth Floor**. Structural steel work that supports the facade in this floor range. | 28 | #4 |
| 6 | `4S-F-SS35` | **Sixth Floor to Terrace**. Structural steel work that supports the facade in this floor range, up to the terrace. | 24 | #5, Superstructure › Roof Top › Slab FF +15d, Structural Steel Fabrication: Structural Steel Fabrication FF +30d |

### N. Terrace works

Waterproofing the roof, flooring and installing rooftop equipment. Waterproofing starts from the roof slab.

*Where in the schedule: Construction > Hotel 4 Star > Terrace Works*

3 activities, planned (early dates) 2027-10-01 to 2028-12-21. Triggered by: Superstructure › Roof Top › Slab; Design: GFC drawing issued on site; Facade › Above Terrace › Rooftop; Procurement: MEP Work › Solar PV System; Facade › Above Terrace › Front Face - Toward Airport; Facade › Above Terrace › Back Face - Toward CC and 1 more. Releases: Facade › Above Terrace › Rooftop; Hotel 4 Star › Testing, Commissioning, HO › Terrace Floor.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Waterproofing (45wd) → #2 Flooring (30wd) → #3 Installation of Fans, Solar and ot (45wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-Terrace10` | **Waterproofing**. Applying waterproofing to stop water getting through. | 45 | Superstructure › Roof Top › Slab |
| 2 | `4S-Terrace15` | **Flooring**. Laying the floor finish. | 30 | #1, Design: GFC drawing issued on site |
| 3 | `4S-Terrace20` | **Installation of Fans, Solar and other MEP Equipments**. Installing rooftop fans, solar equipment and other MEP equipment. | 45 | #2, Facade › Above Terrace › Rooftop, Procurement: MEP Work › Solar PV System, Design: GFC drawing issued on site, Facade › Above Terrace › Front Face - Toward Airport, Facade › Above Terrace › Back Face - Toward CC, Facade › Above Terrace › Side Face |

### O. Swimming pool

Present in Hotel 4 Star only. It depends on the basement pump-room MEP and vendor packages.

*Where in the schedule: Construction > Hotel 4 Star > Swimming Pool*

8 activities, planned (early dates) 2027-08-25 to 2028-09-11. Triggered by: Procurement: Misc › Swiming Pool/Water Body; Common Basements MEP & Finishes: Basement 01 › High Side MEP › Civil Work. Releases: Design: As Built Drawings › Misc; Milestone: Land Scape Completion; Hotel 4 Star › Testing, Commissioning, HO › Second Floor.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Pump Room (60wd) → #2 Balancing Tank (60wd) → #3 Fixing of Plumbing Connenctions (60wd) → #4 Waterproofing (30wd) → #5 Tiling inside Swimming Pool (30wd) → #7 Testing & Commissioning (60wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-SP10` | **Pump Room**. Building the pump room. | 60 | Common Basements MEP & Finishes: Basement 01 › High Side MEP › Civil Work |
| 2 | `4S-SP15` | **Balancing Tank**. Building the swimming pool balancing tank, which holds overflow water and keeps the pool level steady. | 60 | #1 |
| 3 | `4S-SP20` | **Fixing of Plumbing Connenctions**. Fixing the plumbing connections of the swimming pool. | 60 | #2 |
| 4 | `4S-SP25` | **Waterproofing**. Applying waterproofing to stop water getting through. | 30 | #3, Procurement: Misc › Swiming Pool/Water Body |
| 5 | `4S-SP30` | **Tiling inside Swimming Pool**. Tiling the inside of the swimming pool. | 30 | #3, #4 |
| 6 | `4S-SP35` | **Tiling on Deck**. Tiling the pool deck. | 25 | #5 |
| 7 | `4S-SP40` | **Testing & Commissioning**. Testing every system (HVAC, electrical, plumbing, fire, ELV) and bringing it into working order. | 60 | #3, #4, #5 |
| 8 | `4S-SP45` | **Landscape around Swimming Pool**. Landscaping around the swimming pool. | 30 | #5, #6 |

### P. Vertical transport (lifts)

Lift installation follows the roof slab (after a strength-gain wait), the shaft deshuttering and plaster, and lift vendor mobilisation.

*Where in the schedule: Construction > Hotel 4 Star > Vertical Transport*

5 activities, planned (early dates) 2027-10-01 to 2028-07-19. Triggered by: Superstructure › Roof Top › Slab; Procurement: MEP Work › Vertical Transport. Releases: Design: As Built Drawings › Misc; Hotel 4 Star › Testing, Commissioning, HO › Terrace Floor; Project Closure: Project Closure › Statutory Approvals › Lift Licence to operate.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Wait for Strength Gain (6wd) → #2 Deshuttering (5wd) → #3 Plaster (15wd) → #4 Installation of Lift/Escalator (120wd) → #5 Testing & Commissioning (45wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-VT10` | **Wait for Strength Gain**. No work, only time: the concrete must reach the strength needed before it is stressed, loaded or its formwork is removed. | 6 | Superstructure › Roof Top › Slab |
| 2 | `4S-VT15` | **Deshuttering**. Removing the formwork and props once the concrete has gained enough strength. | 5 | #1 |
| 3 | `4S-VT20` | **Plaster**. Plastering the walls (and ceilings where specified). | 15 | #2 |
| 4 | `4S-VT25` | **Installation of Lift/Escalator**. Installing the lifts and escalators. | 120 | #3, Procurement: MEP Work › Vertical Transport |
| 5 | `4S-VT30` | **Testing & Commissioning**. Testing every system (HVAC, electrical, plumbing, fire, ELV) and bringing it into working order. | 45 | #4 |

### Q. Testing, commissioning and handover (one floor)

Each floor gets three activities in sequence. Testing & Commissioning waits for all the final-fix MEP of the floor. Snagging & Desnagging waits for the testing and for all the dry finishes. Handing Over waits for snagging. The building handover milestone then collects the floors. Testing also has a finish-to-finish link from the swimming pool, which looks like a stray link to check.

*Where in the schedule: Construction > Hotel 4 Star > Testing, Commissioning, HO > Second Floor*

3 activities, planned (early dates) 2028-07-19 to 2028-11-07. Triggered by: Front Face - Toward Airport › MEP Final Fix › HVAC; Front Face - Toward Airport › MEP Final Fix › Electrical; Front Face - Toward Airport › MEP Final Fix › Plumbing; Front Face - Toward Airport › MEP Final Fix › Firefighting; Front Face - Toward Airport › MEP Final Fix › ELV; Back Face - Toward CC › MEP Final Fix › HVAC and 2 more. Releases: Milestone: Hotel 4 Star.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Testing & Commissioning (45wd) → #2 Snagging & Desnagging (45wd) → #3 Handing Over (1wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `4S-T&C-2nd10` | **Testing & Commissioning**. Testing every system (HVAC, electrical, plumbing, fire, ELV) and bringing it into working order. | 45 | Front Face - Toward Airport › MEP Final Fix › HVAC x2, Front Face - Toward Airport › MEP Final Fix › Electrical x2, Front Face - Toward Airport › MEP Final Fix › Plumbing x3, Front Face - Toward Airport › MEP Final Fix › Firefighting x4, Front Face - Toward Airport › MEP Final Fix › ELV x8, Back Face - Toward CC › MEP Final Fix › HVAC x2, Back Face - Toward CC › MEP Final Fix › Electrical x2, Back Face - Toward CC › MEP Final Fix › Plumbing x3, Back Face - Toward CC › MEP Final Fix › Firefighting x4, Back Face - Toward CC › MEP Final Fix › ELV x8, Side Face › MEP Final Fix › HVAC x2, Side Face › MEP Final Fix › Electrical x2, Side Face › MEP Final Fix › Plumbing x3, Side Face › MEP Final Fix › Firefighting x4, Side Face › MEP Final Fix › ELV x8, Hotel 4 Star › Swimming Pool FF |
| 2 | `4S-T&C-2nd15` | **Snagging & Desnagging**. Snagging: inspecting for defects and listing them. Desnagging: fixing them. | 45 | #1, Second Floor › Front Face - Toward Airport › Dry Finishes/ID Wor x11, Second Floor › Back Face - Toward CC › Dry Finishes/ID Works x12, Second Floor › Side Face › Dry Finishes/ID Works x12 |
| 3 | `4S-T&C-2nd20` | **Handing Over**. Formal handing over of the completed floor to the client. | 1 | #2 |

### R. Common basements: one block (Basement 03, Hotel 4 Star area)

The common basements are finished area by area, one block under each building. A block runs the same finishes and MEP chain as a floor, after the grade slab concrete and the supporting design and vendor releases.

*Where in the schedule: Construction > Common Basements MEP & Finishes > Basement 03 > Hotel 4 Star*

80 activities, planned (early dates) 2027-01-28 to 2028-10-09. Triggered by: Design: GFC drawing issued on site; Substructure › Basement 03(Grade Slab) › Pour 3; Substructure › Basement 03(Grade Slab) › Pour 1; Substructure › Basement 03(Grade Slab) › Pour 2; Substructure › Basement 03(Grade Slab) › Pour 4; Common Basements MEP & Finishes: Basement 03 › High Side MEP › Civil Work and 2 more. Releases: Common Basements MEP & Finishes: Basement 03 › High Side MEP › Plumbing; Procurement: Civil work › Flooring (PU/Kota Stone); Procurement: MEP Work › ACO Drain; Common Basements MEP & Finishes: Common Basements MEP & Finishes › Testing, Commissioning, HO.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Waiting for curing & Deshuttering (7wd) → #2 Brickwork/Blockwork (45wd) → #12 Wall Conduiting (30wd) → #19 Installing back boxes for switches (5wd) → #26 Plaster (30wd) → #33 Cable tray laying (35wd) → #39 Cabling & Wire Pulling (60wd) → #44 DB fixing and connecting (35wd) → #49 Floor/Distribution Panel Installat (30wd) → #52 Floor Rising Main Installation (30wd) → #53 Equipment Earthing (30wd) → #54 Flooring (50wd) → #56 Installation of Gypsum Board (10wd) → #57 Wall Painting first coat including (10wd) → #66 Switches & Socket (30wd) → #75 Light Fixtures (30wd) → #80 Wall painting final coat (6wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `CB-B03-4S-WMI-25` | **Waiting for curing & Deshuttering**. Waiting for the concrete to cure and then removing formwork. | 7 | Substructure › Basement 03(Grade Slab) › Pour 3, Substructure › Basement 03(Grade Slab) › Pour 1, Substructure › Basement 03(Grade Slab) › Pour 2, Substructure › Basement 03(Grade Slab) › Pour 4 |
| 2 | `CB-B03-4S-WMI-30` | **Brickwork/Blockwork**. Building the internal and external walls of the floor with bricks or blocks. | 45 | #1, Design: GFC drawing issued on site |
| 3 | `CB-B03-4S-WMI-100` | **Structural Misc Works**. Small structural jobs: pits, upstands and similar. | 50 | #1 |
| 4 | `CB-B03-4S-WMI-95` | **Slab Conduiting**. Laying the electrical conduits in or on the slab. | 35 | #1 |
| 5 | `CB-B03-4S-WMI-90` | **Slab Conduiting**. Laying the electrical conduits in or on the slab. | 35 | #1 |
| 6 | `CB-B03-4S-WMI-20` | **Installation of Rungs**. Installing steel ladder rungs in pits and shafts. | 35 | #2 |
| 7 | `CB-B03-4S-WMI-180` | **Fixing pipe supports and clamps**. Fixing the clamps and supports that will hold pipes in place. | 35 | #2 |
| 8 | `CB-B03-4S-WMI-165` | **Duct Support Fabrication**. Making the steel hangers and supports that will hold the AC ducts. | 35 | #2, Design: GFC drawing issued on site |
| 9 | `CB-B03-4S-WMI-235` | **Fixing pipe supports and hangers**. Fixing hangers and supports that will hold pipes under the slab. | 35 | #2 |
| 10 | `CB-B03-4S-WMI-335` | **Painting on Ceiling (Ceiling Finish)**. Painting the ceiling. | 15 | #2 |
| 11 | `CB-B03-4S-WMI-285` | **Wall Conduiting**. Laying electrical conduits inside the walls. | 30 | #2 |
| 12 | `CB-B03-4S-WMI-45` | **Wall Conduiting**. Laying electrical conduits inside the walls. | 30 | #2 |
| 13 | `CB-B03-4S-WMI-10` | **Waterproofing**. Applying waterproofing to stop water getting through. | 30 | #6 |
| 14 | `CB-B03-4S-WMI-175` | **Laying drainage pipes (soil, waste, vent)**. Laying drainage pipes: soil, waste and vent. | 35 | #7 |
| 15 | `CB-B03-4S-WMI-170` | **Laying water supply pipes (hot & cold)**. Laying the hot and cold water supply pipes. | 35 | #7 |
| 16 | `CB-B03-4S-WMI-120` | **Installing duct hangers and supports**. Installing the hangers and supports that hold the ducts. | 30 | #10, #8 |
| 17 | `CB-B03-4S-WMI-230` | **Laying branch piping**. Laying the branch pipes that run from the main lines to each point of use. | 35 | #9 |
| 18 | `CB-B03-4S-WMI-305` | **Installing back boxes for switches, sockets**. Fixing the embedded boxes inside walls where switches and sockets will go. | 5 | #11, #4 |
| 19 | `CB-B03-4S-WMI-115` | **Installing back boxes for switches, sockets**. Fixing the embedded boxes inside walls where switches and sockets will go. | 5 | #12, #5 |
| 20 | `CB-B03-4S-WMI-15` | **Flooring**. Laying the floor finish. | 30 | #13 |
| 21 | `CB-B03-4S-WMI-200` | **Installation of plumbing fixture base supports (WC frames, sink brackets)**. Installing the supports for toilet and sink fixtures before the walls are closed. | 30 | #14 |
| 22 | `CB-B03-4S-WMI-125` | **Laying concealed/exposed refrigerant piping**. Laying the refrigerant pipes for the AC system. | 30 | #16 |
| 23 | `CB-B03-4S-WMI-130` | **Laying concealed/exposed drain piping**. Laying the AC condensate drain pipes. | 30 | #16 |
| 24 | `CB-B03-4S-WMI-135` | **Duct installation**. Fitting the air-conditioning ductwork. | 35 | #16 |
| 25 | `CB-B03-4S-WMI-240` | **Hydrostatic pressure testing of piping**. Testing pipes with water under pressure to check for leaks. | 30 | #17 |
| 26 | `CB-B03-4S-WMI-40` | **Plaster**. Plastering the walls (and ceilings where specified). | 30 | #12, #19, #18, #3 |
| 27 | `CB-B03-4S-WMI-75` | **Installation of concealed parts of toilet fixtures**. Installing the parts of toilet fixtures that sit inside walls (cisterns and frames). | 30 | #21 |
| 28 | `CB-B03-4S-WMI-140` | **Insulation of ducts (thermal/acoustic)**. Wrapping the ducts with thermal or acoustic insulation. | 30 | #24 |
| 29 | `CB-B03-4S-WMI-255` | **Painting/insulation of exposed fire pipes**. Painting and insulating the exposed fire-fighting pipes. | 30 | #25 |
| 30 | `CB-B03-4S-WMI-185` | **Pressure testing of water supply lines**. Pressure-testing the water supply pipes for leaks. | 25 | #15, #14, #21 |
| 31 | `CB-B03-4S-WMI-290` | **Cable tray installation**. Fixing the metal trays that carry cables along ceilings and shafts. | 35 | #26, #10 |
| 32 | `CB-B03-4S-WMI-245` | **Installation of vertical risers and distribution piping in shafts**. Installing the vertical pipes in the service shafts and the distribution pipes from them. | 35 | #26, #25 |
| 33 | `CB-B03-4S-WMI-50` | **Cable tray laying**. Laying out and fixing the cable trays along their routes before cables are pulled. | 35 | #26, #10 |
| 34 | `CB-B03-4S-WMI-210` | **Insulation of hot water pipes (if applicable)**. Insulating hot-water pipes. | 30 | #30 |
| 35 | `CB-B03-4S-WMI-145` | **Installation of chilled water piping / VRF piping**. Installing the chilled-water or VRF refrigerant piping for air conditioning. | 35 | #28 |
| 36 | `CB-B03-4S-WMI-260` | **Testing risers and branch lines for leakage**. Testing the vertical risers and branch lines for leaks. | 30 | #29 |
| 37 | `CB-B03-4S-WMI-295` | **Cabeling of ELV cable - IT/Fire Alarm/Public Address**. Pulling extra-low-voltage cables (data/IT, fire alarm, public address) through the trays and conduits. | 45 | #31 |
| 38 | `CB-B03-4S-WMI-250` | **Installation of sprinkler branch lines in ceilings**. Installing the sprinkler pipework above the ceiling. | 35 | #32, #10 |
| 39 | `CB-B03-4S-WMI-55` | **Cabling & Wire Pulling**. Pulling power cables and wires through conduits and trays. | 60 | #33, Procurement: MEP Work › HT & LT Cables |
| 40 | `CB-B03-4S-WMI-190` | **Installation of vertical risers and main distribution lines**. Installing vertical risers and the main distribution lines. | 35 | #26, #10, #30 |
| 41 | `CB-B03-4S-WMI-205` | **Testing drainage lines for leakage/blockage**. Testing the drainage lines for leaks and blockages. | 30 | #21, #34 |
| 42 | `CB-B03-4S-WMI-360` | **Installation of indoor units including AHU, FCU**. Installing the AC indoor units: air handling units and fan coil units. | 60 | #35, #22, #23 |
| 43 | `CB-B03-4S-WMI-375` | **ELV Rack Installation**. Installing the cabinets (racks) for network and security equipment. | 30 | #37 |
| 44 | `CB-B03-4S-WMI-65` | **DB fixing and connecting**. Mounting the distribution board (floor electrical panel) and connecting its cables. | 35 | #39 |
| 45 | `CB-B03-4S-WMI-195` | **Fixing floor traps and gully traps**. Fixing the drain traps in floors so that water can drain and odours are blocked. | 30 | #40 |
| 46 | `CB-B03-4S-WMI-80` | **Laying of ACO Drains**. Laying channel (ACO) drains. | 20 | #41, #27, Procurement: MEP Work › ACO Drain |
| 47 | `CB-B03-4S-WMI-150` | **Connecting refrigerant and drain piping to indoor units**. Final connection of the AC indoor units to the refrigerant pipes and the condensate drain pipes. | 20 | #42 |
| 48 | `CB-B03-4S-WMI-300` | **Termination of cables at junction boxes, patch panels, and control panels**. Connecting cable ends at junction boxes, patch panels and control panels. | 35 | #43 |
| 49 | `CB-B03-4S-WMI-365` | **Floor/Distribution Panel Installation**. Installing the floor distribution panel. | 30 | #44, Procurement: MEP Work › HT/LT Panel, Procurement: MEP Work › Bus duct and Riser |
| 50 | `CB-B03-4S-WMI-85` | **Installation of ACO Drain Grating**. Installing gratings on the channel drains. | 7 | #46 |
| 51 | `CB-B03-4S-WMI-315` | **Fixing devices like CCTV camera bases, card reader bases, smoke detector bases, PA Bases, Wifi Bases**. Fixing the mounting bases for security, fire and network devices before the devices themselves are installed. | 25 | #48 |
| 52 | `CB-B03-4S-WMI-110` | **Floor Rising Main Installation**. Installing the vertical electrical main that feeds this floor. | 30 | #49 |
| 53 | `CB-B03-4S-WMI-370` | **Equipment Earthing**. Connecting equipment to the earthing (grounding) system for safety. | 30 | #49, #52 |
| 54 | `CB-B03-4S-WMI-35` | **Flooring**. Laying the floor finish. | 50 | #2, #47, #41, #36, #51, #3, #24, #28, #35, #42, #47 FF, #33, #39, #44, #49, #52, #53, #40, #34, #41 FF, #45, #46, #32, #29, #36 FF, #38, #31, #37, #43, #48, #51 FF, Common Basements MEP & Finishes: Basement 03 › High Side MEP › Civil Work, Common Basements MEP & Finishes: Basement 03 › High Side MEP › Civil Work FF |
| 55 | `CB-B03-4S-WMI-105` | **Civil Misc Works**. Small civil jobs not covered elsewhere (minor concrete, curbs, pits and similar). | 30 | #54 |
| 56 | `CB-B03-4S-WMI-330` | **Installation of Gypsum Board**. Installing gypsum boards for ceilings or partitions. | 10 | #54 |
| 57 | `CB-B03-4S-WMI-340` | **Wall Painting first coat including putty**. Putty and the first coat of paint on walls. | 10 | #56 |
| 58 | `CB-B03-4S-WMI-160` | **Installing grills, diffusers, dampers**. Fitting the air grills, diffusers and dampers on the ductwork. | 30 | #57 |
| 59 | `CB-B03-4S-WMI-275` | **Installation of portable fire extinguishers**. Placing portable fire extinguishers. | 30 | #57 |
| 60 | `CB-B03-4S-WMI-325` | **Installation of fire alarm devices + Public Address**. Installing fire alarm devices and public address speakers. | 15 | #57 |
| 61 | `CB-B03-4S-WMI-270` | **Installation of hydrant accessories (valves, hose reels, cabinets)**. Installing fire hydrant accessories: valves, hose reels and cabinets. | 25 | #57 |
| 62 | `CB-B03-4S-WMI-310` | **Installation of data and Voice Faceplate**. Installing data and telephone outlet faceplates. | 25 | #57 |
| 63 | `CB-B03-4S-WMI-320` | **Installation of Camera & Wifi**. Installing CCTV cameras and Wi-Fi access points. | 30 | #57 |
| 64 | `CB-B03-4S-WMI-405` | **Door & Window**. Installing doors and windows. | 10 | #57 |
| 65 | `CB-B03-4S-WMI-265` | **Installation of sprinkler heads, nozzles, and final alignment**. Fitting the sprinkler heads and aligning them with the finished ceiling. | 35 | #57, #38 |
| 66 | `CB-B03-4S-WMI-70` | **Switches & Socket**. Fixing the switch and socket plates. | 30 | #57 |
| 67 | `CB-B03-4S-WMI-355` | **Wheel stoppers**. Fixing the wheel stoppers in parking bays. | 8 | #57 |
| 68 | `CB-B03-4S-WMI-215` | **Installation of sanitary fixtures (WC, washbasins, urinals, sinks)**. Installing the visible sanitary fixtures: toilets, washbasins, urinals and sinks. | 10 | #57, #45 |
| 69 | `CB-B03-4S-WMI-380` | **Installation of Active System**. Installing the active network equipment. | 15 | #60 |
| 70 | `CB-B03-4S-WMI-155` | **Installation of thermostats and control panels**. Installing room thermostats and AC control panels. | 30 | #58 |
| 71 | `CB-B03-4S-WMI-280` | **Integration with fire alarm system**. Connecting devices to the fire alarm system. | 20 | #59 |
| 72 | `CB-B03-4S-WMI-390` | **Fire Panel Intallation & Integration**. Installing the fire alarm control panel and connecting it to the detectors. | 25 | #60 |
| 73 | `CB-B03-4S-WMI-395` | **Installation & Integration of Audio Visual System**. Installing and connecting the audio-visual system. | 25 | #60 |
| 74 | `CB-B03-4S-WMI-400` | **Installation & Integration of Access Control**. Installing and connecting the door access control system. | 25 | #60 |
| 75 | `CB-B03-4S-WMI-60` | **Light Fixtures**. Installing light fittings. | 30 | #66, #53 |
| 76 | `CB-B03-4S-WMI-350` | **Line marking for parking bays, arrows, pedestrian paths**. Painting parking bays, arrows and pedestrian paths on the basement floor. | 8 | #67 |
| 77 | `CB-B03-4S-WMI-220` | **Installation of CP fittings (taps, mixers, showers, health faucets)**. Installing chrome-plated fittings: taps, mixers, showers and health faucets. | 10 | #68, #57 |
| 78 | `CB-B03-4S-WMI-385` | **Integration of Active components**. Connecting the active network components into the system. | 15 | #69 |
| 79 | `CB-B03-4S-WMI-225` | **Connection of appliances**. Connecting appliances and equipment to their power, water or drain services. | 25 | #77 |
| 80 | `CB-B03-4S-WMI-345` | **Wall painting final coat**. The final coat of wall paint. | 6 | #76, #62, #63, #71, #65, #61, #59, #79, #75, #70, #72, #64, #50, #73, #74, #78, #55, Common Basements MEP & Finishes: Basement 03 › High Side MEP › Plumbing x7 |

### S. Common basements: High Side MEP (Basement 03)

The pumps, the sewage and effluent treatment plants and their pedestals. Other basement blocks wait for them, so they are shared hubs.

*Where in the schedule: Construction > Common Basements MEP & Finishes > Basement 03 > High Side MEP*

8 activities, planned (early dates) 2027-08-28 to 2028-09-30. Triggered by: Common Basements MEP & Finishes: Hotel 4 Star › Wet Finishes › ETP; Common Basements MEP & Finishes: Convention Center › Wet Finishes › Water Tanks; Common Basements MEP & Finishes: Basement 03 › Hotel 3 Star › Wet Finishes; Common Basements MEP & Finishes: Hotel 3 Star › Wet Finishes › STP/ETP; Procurement: MEP Work › STP/ETP/WTP; Common Basements MEP & Finishes: Basement 03 › Convention Center › Wet Finishes and 1 more. Releases: Common Basements MEP & Finishes: Basement 03 › Hotel 4 Star › Wet Finishes; Common Basements MEP & Finishes: Basement 03 › Hotel 4 Star › Dry Finishes; Common Basements MEP & Finishes: Basement 03 › Hotel 3 Star › Dry Finishes; Common Basements MEP & Finishes: Basement 03 › Retail Block 2 › Dry Finishes; Common Basements MEP & Finishes: Basement 03 › Retail Block 1 › Dry Finishes; Common Basements MEP & Finishes: Basement 03 › Convention Center › Dry Finishes and 2 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Construction of pedestals for the  (30wd) → #5 Pump installation (7wd) → #7 Connection of Pumps and water tank (45wd) → #8 Testing of Pumps, Connections (7wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `CB-B03-HS-MEP45` | **Construction of pedestals for the Equipments**. Casting concrete plinths on which pumps and plant equipment will stand. | 30 | Common Basements MEP & Finishes: Basement 03 › Convention Center › Wet Finishes |
| 2 | `CB-B03-HS-MEP30` | **Sump pumps installation**. Installing the sump pumps that remove water from basement pits. | 7 | #1, Common Basements MEP & Finishes: Convention Center › Wet Finishes › Water Tanks |
| 3 | `CB-B03-HS-MEP25` | **Effulent Treatment Plant (ETP)**. Installing the effluent treatment plant that treats wastewater. | 60 | #1, Common Basements MEP & Finishes: Basement 03 › Hotel 3 Star › Wet Finishes, Common Basements MEP & Finishes: Hotel 3 Star › Wet Finishes › STP/ETP, Procurement: MEP Work › STP/ETP/WTP, Common Basements MEP & Finishes: Hotel 4 Star › Wet Finishes › ETP |
| 4 | `CB-B03-HS-MEP40` | **Sweage Treatment Plant (STP)**. Installing the sewage treatment plant. | 60 | #1, Common Basements MEP & Finishes: Basement 03 › Hotel 3 Star › Wet Finishes, Common Basements MEP & Finishes: Hotel 3 Star › Wet Finishes › STP/ETP, Procurement: MEP Work › STP/ETP/WTP |
| 5 | `CB-B03-HS-MEP20` | **Pump installation**. Installing the pumps. | 7 | #1, Common Basements MEP & Finishes: Basement 03 › Convention Center › Wet Finishes, Common Basements MEP & Finishes: Convention Center › Wet Finishes › Water Tanks, Common Basements MEP & Finishes: Retail Block 2 › Wet Finishes › Water Tanks |
| 6 | `CB-B03-HS-MEP35` | **Hydro-pneumatic system installation**. Installing the pressurised water supply system. | 20 | #1, #5 |
| 7 | `CB-B03-HS-MEP10` | **Connection of Pumps and water tanks**. Plumbing connections between the pumps and the water tanks. | 45 | #5 |
| 8 | `CB-B03-HS-MEP15` | **Testing of Pumps, Connections**. Testing the pumps and their connections. | 7 | #6, #2, #3, #4, #7 |

### T. Project closure: statutory approvals

Applications, inspections and certificates (fire NOC, electrical inspector, power connection, sewage and water connections). They start when the related building handovers or infra works are done and feed the Project Completion milestone.

*Where in the schedule: Construction > Project Closure*

34 activities, planned (early dates) 2028-07-17 to 2029-05-15. Triggered by: External Development/Landscape › External MEP; Convention Center › Vertical Transport; Convention Center › Facade › Rooftop; Design: Detail Design › Green Building; +10 more outside groups; Infra Works and 2 more. Releases: Milestone: Project Completion Date.

Driving chain inside the block (the sequence of latest-finishing predecessors): #4 OEM Details (0wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `PC20` | **Filling of application and fees payment**. Filling of application and fees payment | 20 | External Development/Landscape › External MEP |
| 2 | `PC35` | **Filling of application and fees payment**. Filling of application and fees payment | 20 | Convention Center › Vertical Transport, Retail Block 1 › Vertical Transport, Retail Block 2 › Vertical Transport, Hotel 3 Star › Vertical Transport, Hotel 4 Star › Vertical Transport |
| 3 | `PC10` | **Filling of application and fees payment**. Filling of application and fees payment | 10 | Infra Works |
| 4 | `PC70` | **OEM Details**. OEM Details | 0 | Milestone: Hotel 4 Star FF, Milestone: Hotel 3 Star FF, Milestone: Retail Block 1 FF, Milestone: Retail Block 2 FF, Milestone: Convention Center FF |
| 5 | `PC50` | **Filling of application and fees payment**. Filling of application and fees payment | 20 | Basement 03 › High Side MEP › Plumbing x2 |
| 6 | `PC85` | **Filling of application and fees payment**. Filling of application and fees payment | 10 | Convention Center › Facade › Rooftop, Design: Detail Design › Green Building |
| 7 | `PC140` | **Filling of application and fees payment**. Filling of application and fees payment | 5 | Infra Works |
| 8 | `PC75` | **List of Equipments**. List of Equipments | 0 | Milestone: Hotel 4 Star FF, Milestone: Hotel 3 Star FF, Milestone: Retail Block 1 FF, Milestone: Retail Block 2 FF, Milestone: Convention Center FF |
| 9 | `PC115` | **Initial Drawing submission for CEIG**. Initial Drawing submission for CEIG | 10 | Infra Works, Basement 01 › High Side MEP › Electrical |
| 10 | `PC155` | **Filling of application and fees payment**. Filling of application and fees payment | 5 | Infra Works, Misc |
| 11 | `PC170` | **Filling of application and fees payment**. Filling of application and fees payment | 10 | Infra Works |
| 12 | `PC80` | **Relevant Warranties, Guarantees**. Relevant Warranties, Guarantees | 0 | Milestone: Hotel 4 Star FF, Milestone: Hotel 3 Star FF, Milestone: Retail Block 1 FF, Milestone: Retail Block 2 FF, Milestone: Convention Center FF |
| 13 | `PC25` | **Inspection from authority**. Inspection from authority | 20 | #1 |
| 14 | `PC40` | **Inspection**. Inspection | 20 | #2 |
| 15 | `PC65` | **Inspection from authority (Fesibility report)**. Inspection from authority (Fesibility report) | 10 | #3 |
| 16 | `PC55` | **Inspection from authority**. Inspection from authority | 20 | #5 |
| 17 | `PC95` | **Inspection from authority**. Inspection from authority | 20 | #6 |
| 18 | `PC145` | **Inspection from authority**. Inspection from authority | 10 | #7 |
| 19 | `PC120` | **Getting Drawing approval**. Getting Drawing approval | 15 | #9 |
| 20 | `PC160` | **Inspection from authority**. Inspection from authority | 10 | #10 |
| 21 | `PC175` | **Inspection**. Inspection | 10 | #11 |
| 22 | `PC30` | **Certification to storage and operation**. Certification to storage and operation | 40 | #13 |
| 23 | `PC45` | **Certification**. Certification | 40 | #14 |
| 24 | `PC100` | **Pole Structure work**. Pole Structure work | 10 | #15 |
| 25 | `PC60` | **Certification**. Certification | 40 | #16 |
| 26 | `PC90` | **Certification**. Certification | 0 | #17 |
| 27 | `PC150` | **Certification & Water supply**. Certification & Water supply | 10 | #18 |
| 28 | `PC125` | **Inspection from authority (CEIG Inspection)**. Inspection from authority (CEIG Inspection) | 10 | #19 |
| 29 | `PC165` | **Certification**. Certification | 10 | #20 |
| 30 | `PC15` | **Connection to drain**. Connection to drain | 8 | #21 |
| 31 | `PC105` | **Submission of Technical document for Load sanction**. Submission of Technical document for Load sanction | 10 | #24 |
| 32 | `PC130` | **Certification from CEIG authority**. Certification from CEIG authority | 10 | #28 |
| 33 | `PC110` | **Avail letter from UPPCL for Load sanction**. Avail letter from UPPCL for Load sanction | 10 | #31 |
| 34 | `PC135` | **Load realese/connection (Minimum charges would start from here)**. Load realese/connection (Minimum charges would start from here) | 7 | #32 |

### U. External development and landscape

Roads, external MEP (DG, STP), landscape and the water body. They follow the infra works and the building facades, and they feed as-built drawings and the Project Completion milestone.

*Where in the schedule: Construction > External Development/Landscape*

23 activities, planned (early dates) 2028-06-29 to 2029-04-11. Triggered by: Basement 03 › High Side MEP › Plumbing; Basement 01 › Hotel 4 Star › Wet Finishes; Procurement: MEP Work › DG; +6 more outside groups; Design: Detail Design › Misc; Facade › GF to Service Floor › Side Face and 2 more. Releases: Project Closure › Statutory Approvals › CCOE, CTO (DG); Design: As Built Drawings › MEPF; Milestone: Land Scape Completion; Milestone: Project Completion Date; Milestone: External Works Completion; Milestone: Land Scape Commencement and 2 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #2 Pump Room (30wd) → #5 Balancing Tank (30wd) → #9 Waterproofing (25wd) → #12 Fixing of Plumbing Connenctions (60wd) → #15 Tiling (24wd) → #18 Testing, Commissioning & HO (10wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `ED-E.MEP-30` | **DG (Diesel Generator) set installation, exhaust, and fuel system connections**. DG (Diesel Generator) set installation, exhaust, and fuel system connections | 15 | Basement 01 › Hotel 4 Star › Wet Finishes, Procurement: MEP Work › DG |
| 2 | `ED-WB25` | **Pump Room**. Building the pump room. | 30 | Basement 01 › High Side MEP › HVAC |
| 3 | `ED-R10` | **GSB**. GSB | 40 | Design: Detail Design › Misc x2, Facade › GF to Service Floor › Side Face x2, Facade › Above Terrace › Side Face FF +10d x2, Facade › Third Mezzanine - Terrace › East & West Elevation FF +10d |
| 4 | `ED-E.MEP-10` | **Fabrication of Structural Steel**. Fabrication of Structural Steel | 35 | #1, Basement 03 › High Side MEP › Plumbing x2, Procurement: MEP Work › DG/STP Stack |
| 5 | `ED-WB30` | **Balancing Tank**. Building the swimming pool balancing tank, which holds overflow water and keeps the pool level steady. | 30 | #2 |
| 6 | `ED-LS10` | **Hardscape**. Hardscape | 25 | #3, Procurement: Misc › Landscape |
| 7 | `ED-R15` | **DLC**. DLC | 40 | #3 FF +10d |
| 8 | `ED-E.MEP-15` | **Erection of Structural Steel**. Erection of Structural Steel | 35 | #4 |
| 9 | `ED-WB10` | **Waterproofing**. Applying waterproofing to stop water getting through. | 25 | #5 |
| 10 | `ED-R25` | **PQC**. PQC | 40 | #7 FF +10d |
| 11 | `ED-E.MEP-20` | **MS Pipe Chimani**. MS Pipe Chimani | 35 | #8 |
| 12 | `ED-WB20` | **Fixing of Plumbing Connenctions**. Fixing the plumbing connections of the swimming pool. | 60 | #9, #5 |
| 13 | `ED-R35` | **Saucer Drain works**. Saucer Drain works | 25 | #10 FF +5d |
| 14 | `ED-E.MEP-25` | **Lightening**. Lightening | 35 | #11 |
| 15 | `ED-WB15` | **Tiling**. Tiling | 24 | #12, #6 |
| 16 | `ED-R20` | **Kerb Stone**. Kerb Stone | 25 | #13 FF +10d |
| 17 | `ED-E.MEP-40` | **Testing & Commissiong**. Testing & Commissiong | 35 | #14 |
| 18 | `ED-WB35` | **Testing, Commissioning & HO**. Testing, Commissioning & HO | 10 | #12, #15 |
| 19 | `ED-R30` | **Bituminous Concrete**. Bituminous Concrete | 25 | #16 FF +5d |
| 20 | `ED-LS15` | **Softscape including Horticulture, Drip Irrigation**. Softscape including Horticulture, Drip Irrigation | 12 | #6, #19, Infra Works x10 |
| 21 | `ED-LS20` | **Signage**. Signage | 12 | #6, #19, Infra Works x10, Design: GFC drawing issued on site |
| 22 | `ED-LS25` | **Lighting**. Lighting | 12 | #6, #19, Infra Works x10, Procurement: Misc › Lighting, Design: GFC drawing issued on site |
| 23 | `ED-HO10` | **Snagging, Desnagging & HO**. Snagging, Desnagging & HO | 10 | #20, #21, #22, #18 FF, #17 |

### V. Infra works

Sewage, domestic water, fire hydrant network, HT/LT cables and similar networks. They wait for the facade ground-floor work on the buildings and release landscape and the statutory approvals.

*Where in the schedule: Construction > Infra Works*

10 activities, planned (early dates) 2028-12-13 to 2029-02-24. Triggered by: Facade › GF to Service Floor › Front Face - Toward Airport; Facade › GF to Service Floor › Back Face - Toward CC; Facade › Above Terrace › Front Face - Toward Airport. Releases: Project Closure › Statutory Approvals › Sewage connection; Project Closure › Statutory Approvals › Water Connection; External Development/Landscape › Landscape; Project Closure › Statutory Approvals › FNOC (Fire NOC); Project Closure › Statutory Approvals › CEIG (Electrical Inspect; Project Closure › Statutory Approvals › Sanction of Power connec.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Swerage System (60wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `IW10` | **Swerage System**. Swerage System | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 2 | `IW15` | **Storm Water System**. Storm Water System | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 3 | `IW20` | **Irrigation System**. Irrigation System | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 4 | `IW25` | **Domestic Water System**. Domestic Water System | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 5 | `IW30` | **Flushing Water System**. Flushing Water System | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 6 | `IW35` | **Fire Hydrants Network**. Fire Hydrants Network | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 7 | `IW40` | **HT/LT Cables**. HT/LT Cables | 40 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 8 | `IW45` | **ELV infra Netwrok**. ELV infra Netwrok | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 9 | `IW50` | **Street Lighting Network**. Street Lighting Network | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |
| 10 | `IW55` | **Solid Waste Management (if applicable)**. Solid Waste Management (if applicable) | 60 | Facade › GF to Service Floor › Front Face - Toward Airport x2, Facade › GF to Service Floor › Back Face - Toward CC x2, Facade › Above Terrace › Front Face - Toward Airport |

### W. Structural steel fabrication (shared)

Three activities that fabricate steel for the Convention Center and bridge structures and for facade steel on every building.

*Where in the schedule: Construction > Structural Steel Fabrication*

3 activities, planned (early dates) 2027-02-25 to 2027-12-10. Triggered by: Procurement: Civil work › Structural Steel; Procurement: Delivery of Critical Items › Structure Steel. Releases: Bridge Between RB1 & RB2 › Ground Floor › Slab; Second Mezanine › Pour 4 › Slab; Second Floor › Pour 4 › Columns; Second Floor › Pour 4 › Slab; Hotel 4 Star › Structural Steel works for Facade; +8 more outside groups and 2 more.

Driving chain inside the block (the sequence of latest-finishing predecessors): #3 Fabrication of Structure steel for (180wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `SSF10` | **Fabrication of structural steel- Truss and Column**. Fabrication of structural steel- Truss and Column | 80 | Procurement: Civil work › Structural Steel, Procurement: Delivery of Critical Items › Structure Steel |
| 2 | `SSF15` | **Fabrication of Structure steel for Glass Facade Support**. Fabrication of Structure steel for Glass Facade Support | 120 | Procurement: Delivery of Critical Items › Structure Steel |
| 3 | `SSF20` | **Fabrication of Structure steel for FRP Facade Support**. Fabrication of Structure steel for FRP Facade Support | 180 | Procurement: Delivery of Critical Items › Structure Steel |

### X. Bridge between Retail Block 1 and 2: Ground Floor

A link bridge built floor by floor between the two retail blocks. Its steel erection waits for the PT work of the retail-block slabs it connects to and, on the ground floor, for steel fabrication.

*Where in the schedule: Construction > Bridge Between RB1 & RB2 > Ground Floor*

6 activities, planned (early dates) 2027-05-03 to 2027-06-25. Triggered by: Basement 01 › Pour 6 › Slab; Structural Steel Fabrication. Releases: Milestone: Bridge Structure Commencement; Bridge Between RB1 & RB2 › First Floor › Slab; Retail Block 2 › Structural Steel works for Facade.

Driving chain inside the block (the sequence of latest-finishing predecessors): #1 Erection of Structural Steel Beams (25wd) → #2 Metal Deck Sheet (10wd) → #3 Shear Studs (6wd) → #4 Reinforcement (4wd) → #5 MEP Coordination (1wd) → #6 Concrete of Slab (1wd).

| # | Activity ID | Activity and what it means | Dur (wd) | Starts after |
|---|---|---|---|---|
| 1 | `Bridge-SS-GF.475` | **Erection of Structural Steel Beams**. Erection of Structural Steel Beams | 25 | Basement 01 › Pour 6 › Slab, Structural Steel Fabrication SS +20d |
| 2 | `Bridge-SS-GF.555` | **Metal Deck Sheet**. Metal Deck Sheet | 10 | #1 |
| 3 | `Bridge-SS-GF.560` | **Shear Studs**. Shear Studs | 6 | #2 |
| 4 | `Bridge-SS-GF.565` | **Reinforcement**. Cutting, bending and tying the steel bars for the slab. This is inspected before the formwork is closed. | 4 | #3 |
| 5 | `Bridge-SS-GF.570` | **MEP Coordination**. A check that all pipes, ducts, sleeves and conduits are placed correctly before concrete is cast, so nothing has to be broken out later. | 1 | #2, #4 |
| 6 | `Bridge-SS-GF.575` | **Concrete of Slab**. Pouring and compacting the concrete for the floor slab. | 1 | #5 |

