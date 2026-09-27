# MRM Aug-26 — V8: deck-wide RAG coding + Excel link audit

**Deliverable:** `MRM_Aug-26_Redesigned_V8_RAG.pptx` (38 slides, 64.1 MB)
**Workbook:** `MRM_Master_Data_V8.xlsx` (embedded in the deck; V7's `MRM_Master_Data.xlsx` left untouched) (23 sheets — 21 chart sheets + `Index` + `RAG_Rules`)
**Build date:** 28 September 2026

Nothing else was touched. Verified by checksum after the build:

| File | md5 | State |
|---|---|---|
| `MRM Aug-26 _ Presented (1).pptx` (master) | `65ade7a954fd6e28410c2de83f857b9a` | unchanged |
| `MRM_Aug-26_Redesigned_V7.pptx` | `5d442404ec479b4b9b0be233fbabd2b3` | unchanged (read-only input to the audit) |

---

## 1. RAG colour coding — applied to every indicator

### 1.1 The rule set

Every rule is published on the **`RAG_Rules`** sheet of the embedded workbook —
124 indicators, each with its basis, its three thresholds, its current value and
its resulting status. Nothing is coloured by eye.

| Family | Basis | Green | Amber | Red |
|---|---|---|---|---|
| `progress` | % of a target achieved | ≥ 90% | 70 – 89.9% | < 70% |
| `approval` | % approved of what was submitted | ≥ 90% | 75 – 89.9% | < 75% |
| `quality_ftri` | First Time Right index | ≥ 95% | 85 – 94.9% | < 85% |
| `tat_days` | closure turnaround, lower is better | ≤ 14 d | 14 – 21 d | > 21 d |
| `backlog` | open item count | ≤ 50 | 51 – 200 | > 200 |
| `clash` | open clash inventory | ≤ 5,000 | 5,001 – 20,000 | > 20,000 |
| `hotspot` | clashes on one interface | < 2,000 | 2,000 – 5,000 | > 5,000 |
| `zero_harm` | lagging safety count | 0 | 1 – 4 | ≥ 5 |
| `variance` | actual vs baseline | ≥ −5% | −5 to −20% | < −20% |
| `schedule` | milestone state | issued / complete | scheduled / in progress | overdue / not started |
| `plan` | a forward-looking planned figure | — | always Amber (committed, not yet earned) | — |

### 1.2 What now carries a RAG colour

* **KPI cards** — header strip and the headline number, on all 13 dashboard slides.
* **Charts** — series *and* individual data points. Every bar on the BIM maturity
  chart, the clash trend, the clash hotspots, the quality lagging chart, the
  manpower chart and the observation/NCR charts is coloured by its own value.
* **Progress rails** — the eight bullet rails on slides 5, 6 and 12.
* **Doughnuts** — the FTRI rings on slides 5 and 27 (88% against a 95% target → Amber).
* **Tables** — the design deliverable matrix has a new RAG column and RAG-coloured
  approval figures; the MOM trackers have a RAG column per action; the September
  weekly-pour table is coloured against the August run-rate.
* **Panels, cards and chips** — panel header strips, status chips, milestone rows
  and the statutory-compliance cards.
* **A RAG key** appears bottom-right on every slide that carries RAG items
  (slides 5–17, 19, 20, 27, 28) so the coding is self-describing.

### 1.3 Status changes worth flagging to the CEO

These are the places where a correct RAG reading differs from the way V7 (and the
original deck) presented the number:

| Slide | Indicator | Was | Now | Why |
|---|---|---|---|---|
| 5, 27 | First Time Right 88% | Green | **Amber** | target is 95%; 88% is below it |
| 5 | Inductions 1,691 of 2,400 | Green | **Amber** | 70% of plan |
| 5 | Support Requested card | TATA blue | **Amber** | it is an open ask on the client |
| 6 | GFC approval 72% | Amber | **Red** | below the 75% approval floor |
| 6 | Approval backlog 239 | Amber | **Red** | above the 200 backlog ceiling |
| 7 | Structural GFC 3 of 5 | Navy | **Red** | 60% of the release programme |
| 10 | NSC packages 6 of 17 | Navy | **Red** | 35% released |
| 11 | Formwork at site 1,500 m² | Navy | **Red** | 19% of the 7,700 m² requirement |
| 12 | Month concrete 3,025 m³ | Amber | **Red** | 54% of the 5,584 m³ plan |
| 12 | 4-H foundations 39 of 46 | Green | **Amber** | 85%, below the 90% green line |
| 13 | Tower cranes 03 / 05 | Amber | **Red** | 60% mobilised, one installed |
| 13 | Toilets 20 of 220 | Amber | **Red** | 9% delivered |
| 17 | September plan values | Navy | **Amber** | forward plan, not yet earned |
| 17 | W4 pour 3,584 m³ | Navy | **Red** | more in one week than all of August |
| 27 | Deviation closure 19.9 d | Amber | **Amber** | confirmed against a 14-day target |

---

## 2. Excel link audit — every chart, every reference

### 2.1 Method

`src_v8/verify_links.py` opens the pptx, and for each chart part:

1. reads that chart's own relationships to find the workbook it actually points at,
2. extracts every `c:f` formula (series name, category range, value range),
3. resolves each range **inside the embedded workbook** with openpyxl,
4. compares the resolved cells against the values cached in the chart XML,
5. flags external links, missing workbooks, unknown sheet names, wrong ranges and
   stale caches.

Run it yourself: `python3 verify_links.py <file.pptx>` — exit code 0 means clean.

### 2.2 Result on V7 — **17 of 21 charts were mis-linked**

Full output in `LINK_AUDIT_V7_before.txt`. Summary: **42 problems across 81 references.**

The cause: V7's workbook was hand-authored with thematic sheets (`Commercial`,
`Safety`, `Design`, …) while the chart references were left as the default layout
python-pptx emits (`$B$1` for the first series name, `$A$2:$A$n` for categories,
`$B$2:$B$n` for the first series). Only the *sheet name* was rewritten, not the
ranges — so the columns did not line up. Examples:

```
chart8  (slide 5)  Commercial!$B$1      workbook = 'Baseline'         chart = 'Actual'
chart8  (slide 5)  Commercial!$B$2:$B$3 workbook = 40.0               chart = 15.5
chart17 (slide 9)  Clash!$A$2:$A$7      workbook = '17 Aug'           chart = 'MEPF vs AR'
chart19 (slide 12) Constr!$B$2:$B$2     workbook = 39.0               chart = 15.0
chart23 (slide 20) EHS!$A$2:$A$5        workbook = 'Safe Manhours'    chart = 'Inductions'
chart27 (slide 28) QualityInd!$B$2:$B$3 workbook = 74.0               chart = 24.0
```

The charts *displayed* correctly because PowerPoint renders the cached values, but
the moment anyone clicked **Edit Data** the wrong cells would have come up, and a
refresh would have silently rewritten the chart with the wrong numbers.

### 2.3 Fix

The workbook is no longer hand-authored. It is now **generated from the charts
themselves**: each chart is given its own worksheet whose layout is exactly the
layout the reference formulas expect — header row 1, categories in column A from
row 2, series in columns B, C, D … The link is therefore correct by construction
and cannot drift.

Sheet names are self-documenting and map one-to-one to a chart:

```
Index             S05_Commercial  S05_FTRI      S05_NearMisses  S05_Inductions
S05_OpenNCR       S06_DD          S06_GFC       S08_BIM         S09_Trend
S09_Hotspots      S12_4H          S12_3H        S12_Convention  S13_Manpower
S17_ValueMix      S20_EHS         S27_Leading   S27_Lagging     S27_FTRI
S28_Observations  S28_NCR         RAG_Rules
```

The embedded workbook parts were also renamed from PowerPoint's default
`Microsoft_Excel_Sheet1.xlsx` to `MRM_Master_Data1.xlsx …21.xlsx`, so **Edit Data**
shows the real file name.

### 2.4 Result on V8 — clean

```
charts checked: 21   c:f references resolved: 81   problems: 0
```

Full output in `LINK_AUDIT_V8.txt`. Every chart: embedded workbook present, no
external link, sheet exists, range resolves, workbook contents identical to the
chart cache.

---

## 3. QA gate

| Check | Result |
|---|---|
| OOXML child-sequence validation (`validate.py`) | **PASS** — 73 parts |
| Excel link audit (`verify_links.py`) | **PASS** — 21 charts, 81 refs, 0 problems |
| Layout and package QA (`qa.py`) | **PASS** |
| Slides | 38 |
| Off-canvas shapes (5–38) | 0 |
| Overlapping text boxes | 0 |
| Duplicate `cNvPr` ids | 0 |
| Charts with external links | 0 |
| Charts still pointing at `Sheet1!` | 0 |
| Unresolved `r:id` | 0 |
| Master pptx / V7 pptx | untouched, md5 verified |
| LibreOffice render | 38 / 38 pages, reviewed slide by slide |

---

## 4. Also changed in V8

* MOM tracker text on slides 14–16 condensed further so all three tables hold a
  **15 pt** cell font with no clipping (V7 needed to squeeze rows to fit).
* Slide 27 and 28 KPI captions shortened so nothing overflows its card.
* Slide 28's note now records the SharePoint-link history and the new linkage model.

## 5. Repo contents added by this pass

```
MRM_Aug-26_Redesigned_V8_RAG.pptx   the deliverable
MRM_Master_Data_V8.xlsx             regenerated — 21 chart sheets + Index + RAG_Rules
V8_RAG_AND_LINK_AUDIT.md            this file
LINK_AUDIT_V8.txt                   clean audit of the new deck
LINK_AUDIT_V7_before.txt            the 42 defects found in V7
V8_Renders/slide_NN.jpg             full-page render of every slide
V8_Renders/sheet_N.jpg              six-up contact sheets
src_v8/                             deck.py, slides.py, build.py, mom_data.py,
                                    rag.py, validate.py, qa.py, verify_links.py
```

`src/` and `MRM_Aug-26_Redesigned_V7.pptx` are left exactly as they were.

## 6. Open items

* The pptx is 64.1 MB, above GitHub's 50 MB recommendation. `image75.png` (15.3 MB)
  and `image71.png` (11.1 MB) in `ppt/media` are the main offenders.
* Slide 18's retained drawing and RCC quantity tables are OLE objects; LibreOffice
  ignores their frame sizes when rendering, PowerPoint honours them — check that
  slide in PowerPoint.
* The RAG thresholds in §1.1 are my proposal. They are all in one place
  (`src_v8/rag.py` and the `RAG_Rules` sheet); change a number there and the whole
  deck re-colours on the next build.
* Please revoke the personal access token at <https://github.com/settings/tokens>.
