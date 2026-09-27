# MRM Aug-26 — Full Deck Redesign (V7)

**Deliverable:** `MRM_Aug-26_Redesigned_V7.pptx` (38 slides, 63.8 MB)
**Source (never modified):** `MRM Aug-26 _ Presented (1).pptx` — md5 `65ade7a954fd6e28410c2de83f857b9a`, verified unchanged after the build.
**Build date:** 28 September 2026

---

## 1. What changed from V6

V6 was a single-slide proof (slide 5). V7 is the **whole deck**.

| | V6 | V7 |
|---|---|---|
| Slides redesigned | 5 only | **5 – 38** (1–4 untouched, as instructed) |
| Type scale | v6 | **v7 — every size reduced ~10%** |
| Charts | 3 | **21**, all workbook-embedded |
| SharePoint-linked charts | 7 still present | **0** — all removed, including the 3-D chart |
| External chart links | 6 | **0** |

### v7 type scale (headings and body both stepped down)

```
Title 40   Subtitle 16   Section 24   Card head 21
Big stat 34   Mid stat 28   Body 17   Caption 16
Table header 16   Table cell 15
```

Titles now auto-shrink (down to 24 pt) when a heading would otherwise run into the
Turner & Townsend or adani logo, so no heading collides with the logo band on any slide.

---

## 2. Slide-by-slide

| Slide | Treatment |
|---|---|
| 1–4 | **Untouched** (cover, emergency assembly, safety pledge, quality pledge) |
| 5 | Executive dashboard — KPI strip, stacked commercial bullet bars, FTRI ring, three safety rails, issue/decision/support cards |
| 6 | Design dashboard — KPI strip, 10-row deliverable matrix, DD/GFC approval rails, closure priorities, façade watch item |
| 7 | GFC drawings — three discipline release panels of milestone rows + status chips |
| 8 | BIM status — grouped model-completion bars for six blocks × four disciplines (Retail 1/2 BOH shown as no-model rather than 0%) |
| 9 | BIM clash report — trend column chart + six-interface hotspot bars. **This slide was flagged hidden in the original; it is now visible.** |
| 10 | MEP NSC packages — submissions / immediate dates / forward pipeline |
| 11 | Procurement — RAG status cards, formwork programme, material milestones |
| 12 | Construction — foundation rails per block, constraints and recovery |
| 13 | Mobilization — shed programme, camp amenities, manpower bars, plant |
| 14–16 | MOM action tracker — six-column styled tables with content-proportional row heights; source text condensed for legibility, nothing dropped |
| 17 | September plan — value breakdown, value mix, weekly distribution, critical quantities |
| 18 | September pour plan — original drawing and RCC quantity objects retained and re-laid out inside the body grid; only the chrome is restyled |
| 19 | Statutory compliance — four numbered closure cards with RAG chips |
| 20 | EHS — activity-count bars (safe man-hours moved to the header cards so they no longer flatten the other series) + zero-harm panel |
| 21–26 | EHS photo grids, re-cropped to a regular grid with captions |
| 27 | Quality indicators — leading/lagging bars + FTRI ring |
| 28 | Quality performance — observation and NCR closure, training delivered |
| 29–33 | Quality practice, training and block-progress photo grids |
| 34 | Section divider |
| 35–37 | Progress, infrastructure and camp photo grids |
| 38 | Closing |

---

## 3. Data linkage

All 21 charts are backed by `MRM_Master_Data.xlsx`, embedded in the deck across
11 sheets: Commercial, Quality, Safety, Design, BIM, Clash, Constr, Manpower,
SeptPlan, EHS, QualityInd. Every plotted value, every data label and every
progress rail reads from that workbook — nothing is typed into a text box.
No chart points at `Sheet1!` and no chart carries an external link.

---

## 4. QA gate — all green

| Check | Result |
|---|---|
| OOXML child-sequence validation (`validate.py`) | **PASS** — 94 parts |
| Slide count | 38 |
| Off-canvas shapes (slides 5–38) | 0 |
| Overlapping text boxes | 0 |
| Duplicate `cNvPr` ids | 0 (deck-wide renumber from 5000) |
| Chart content types declared | 21 / 21 |
| Charts still pointing at `Sheet1!` | 0 |
| Unresolved `r:id` references | 0 |
| Stale relationships from cleared slides | pruned |
| Master file md5 | unchanged |
| LibreOffice render | 38 / 38 pages, reviewed slide by slide |

---

## 5. Repo contents

```
MRM_Aug-26_Redesigned_V7.pptx   the deliverable
MRM_Master_Data.xlsx            the linked workbook
V7_BUILD_NOTES.md               this file
V7_Renders/slide_NN.jpg         full-page render of every slide
V7_Renders/sheet_N.jpg          six-up contact sheets
src/deck.py                     design system + component library
src/slides.py                   per-slide composition
src/build.py                    build driver
src/mom_data.py                 MOM tracker content
src/validate.py                 OOXML schema gate
src/qa.py                       layout and package QA gate
```

Rebuild with `python3 build.py` from a directory containing `master.pptx`.

---

## 6. Open items

* The pptx is 63.8 MB — above GitHub's 50 MB recommendation. `image75.png` (15.3 MB)
  and `image71.png` (11.1 MB) inside `ppt/media` are the main offenders and could be
  down-sampled for a further ~20 MB saving.
* Slide 18's retained drawing and quantity tables are OLE objects; LibreOffice ignores
  their frame sizes when rendering, PowerPoint honours them. Check that slide in
  PowerPoint specifically.
* The personal access token pasted in chat should be revoked at
  <https://github.com/settings/tokens>.
