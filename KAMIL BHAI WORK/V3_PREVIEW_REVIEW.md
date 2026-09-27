# `MRM_Slide5_Preview.pptx` — V3 Flagship Review

**Analysed:** 28 Sep 2026 · file pulled directly from `KAMIL BHAI WORK/` on `main` (blob `e1f6fe60`), 75,761,843 bytes.
**Method:** OOXML package + python-pptx / lxml / openpyxl audit, diffed shape-by-shape against `MRM Aug-26 _ Presented (1).pptx`.

---

## 0. Verdict in one line

> **Structurally the cleanest file produced so far — every engineering bug is genuinely fixed — but it still fails 3 of the 4 headline complaints: fonts are effectively 7–9 pt, the "Excel-linked" numbers are static textboxes, and the grid still has 5 different right margins.** Don't ship it as-is; it needs a ×1.5 type pass and a linking fix first.

---

## 1. Diff vs original — scope claim verified

Shape-signature comparison across all 38 slides returns **exactly one difference**:

| Slide 5 | Original | V3 Preview |
|---|---|---|
| AutoShapes | 89 | 23 |
| TextBoxes | 0 | 36 |
| **Charts** | **0** | **6** |
| Group / Freeform / Picture | 3 / 3 / 1 | 3 / 3 / 1 (untouched) |

All other 37 slides are structurally identical. The claim *"only the Executive Dashboard was rebuilt"* is **true**. Logos (`Group 99`, `Group 101`, `Picture 103`) sit at their original coordinates. Slides 1–4 untouched. ✅

---

## 2. Engineering QA — all previously reported bugs are genuinely fixed ✅

| Check | Result |
|---|---|
| Duplicate shape IDs (slide 18 had 31/33/44/47) | ✅ **0 duplicates anywhere** — properly renumbered |
| Duplicate sibling `a:effectLst` (the repair-prompt bug) | ✅ **0 violations**, verified by parsed-tree sibling scan, not grep |
| Non-integer EMU coordinates | ✅ **none** — all x/y/cx/cy are integers |
| Shapes off-canvas on slide 5 | ✅ **0** — the bottom-row overflow is fixed |
| Doughnut auto data-label ("ETRI SCORE" bug) | ✅ fixed — `chart9` has 0 `dLbls` blocks, `autoTitleDeleted=1` |
| Chart cache integrity | ✅ all 6 charts have valid embedded workbooks |

**This part of the work is solid.** The file will open in PowerPoint without a repair prompt.

---

## 3. ❌ Failure 1 — the font complaint is NOT fixed

Canvas is **20 in wide = 1.5× standard**, so nominal pt ÷ 1.5 = what the eye actually sees.

| Nominal on slide 5 | Runs | **Effective size** |
|---|---|---|
| 10.5 pt | 1 | **7.0 pt** |
| 11 pt | 1 | **7.3 pt** |
| 12 pt | 11 | **8.0 pt** |
| 14 pt | 15 | **9.3 pt** |
| 15 pt | 2 | 10.0 pt |
| 18 pt | 5 | 12.0 pt |
| 20 pt | 4 | 13.3 pt |
| 24 pt | 2 | 16.0 pt |
| 40 pt (title) | 1 | **26.7 pt** |

**28 of 41 text runs render below 10 pt effective.** `chart8`'s legend and axis text are hardcoded `sz="1400"` → **9.3 pt effective**.

➡️ The complaint was *"fonts are terribly small, nothing visible."* The V3 title lands at an effective **26.7 pt** and body at **8–9.3 pt** — still smaller than a normal deck's default body text. **Multiply the entire scale by 1.5:** title 60 pt, section heads 30 pt, body 21 pt, hard floor 18 pt.

---

## 4. ❌ Failure 2 — "all data Excel-linked" is not actually true

### 4a. Every visible number is a static textbox, not a chart label

| Shape | Displayed value | Type |
|---|---|---|
| id 143 | `88%` | **static TextBox** floating over the doughnut |
| id 149 | `0` (LTI) | **static TextBox** beside the chart |
| id 152 | `4` (Near Misses) | **static TextBox** |
| id 155 | `1,691` (Inductions) | **static TextBox** |
| id 158 | `1` (Open NCR) | **static TextBox** |
| ids 112/116/120/124 | ₹1,725 Cr · 39 Months · 15 May 2029 · WATCHLIST | **static TextBox** |
| ids 131/135/139 | ₹15.5 Cr −61 % · ₹37.8 Cr −67 % · ₹76.2 Cr | **static TextBox** |

The earlier fix for the *"1,691 wrapping to 1 / 69 / 1"* bug — *"moved the value label out of the chart into an adjacent textbox"* — **directly defeated the linking requirement.** Change the workbook and the bar moves; the printed number does not. That is worse than not linking, because the two can silently disagree in front of the CEO.

**Correct fix:** keep the label inside the chart and give it room — widen the value-axis `max` to ~1.25× the value so an `outEnd` label fits, or use `inEnd` with white text.

### 4b. Six separate 5 KB stub workbooks, not one master

```
Microsoft_Excel_Sheet1.xlsx  5439 B  A1:D3   Baseline / Revamp / Actual × FTM / CUM
Microsoft_Excel_Sheet2.xlsx  5347 B  A1:B3   v 0.88 / r 0.12   (FTRI doughnut)
Microsoft_Excel_Sheet3.xlsx  5314 B  A1:B2   LTI 0
Microsoft_Excel_Sheet4.xlsx  5320 B  A1:B2   Near Misses 4
Microsoft_Excel_Sheet5.xlsx  5322 B  A1:B2   Inductions 1691
Microsoft_Excel_Sheet6.xlsx  5320 B  A1:B2   Open NCR 1
```

Each chart owns a **private, disconnected 2-cell workbook**. There is **no reference to `MRM_Aug26_Dashboard_Data.xlsx` anywhere in the package** — updating that master updates nothing. Right-clicking *Edit Data* on six charts opens six unrelated spreadsheets.

➡️ For a real single source of truth: either (a) one embedded workbook shared by all charts, each chart pointing at a different range, or (b) externally-linked charts against one shipped `.xlsx` — with the caveat that (b) is exactly the failure mode slide 28 already suffers from.

### 4c. The mini bar charts will not render as intended

`chart10–13` (LTI / Near Misses / Inductions / Open NCR) each contain **`c:catAx` and `c:valAx` with no `c:delete val="1"` element at all** — so **both axes will render**. Inside a **0.50 in tall** frame that means axis ticks and numbers fighting a hairline bar. The description *"axis-less mini bar charts"* is not what is in the file.

`dLbls` count is also 0 on all four — so there is literally nothing readable inside the chart; the whole visual is one bar plus two axes.

---

## 5. ❌ Failure 3 — alignment is better, but still not a grid

Slide 5 is down to **29 distinct left edges** (original: 65) — real improvement. But:

**Five different right margins on one slide:**

```
19.20   19.25   19.40   19.45   19.50      (page width 20.00 in)
```

and four different left edges in the margin zone: `0.60 · 0.80 · 0.85 · 0.94`.

Concretely:
- KPI card row ends at **19.395** → margin 0.605
- Mini-stat value textboxes end at **19.45** → margin 0.55
- Critical / Decision / Support cards end at **19.50** → margin 0.50
- Title block starts at **x = 2.50** while all content starts at **x = 0.60** — the title floats off-grid

Remaining near-miss pairs: `(0.80, 0.85)` on X plus 4 on Y. Sub-0.06 in offsets read as *sloppy*, not as *different*.

➡️ Pick **one** margin (0.60 in) and **one** gutter (0.30 in) and snap everything. On a 20 in page: 12 columns × 1.525 in + 0.30 gutters = 19.40 in content width. Nothing should ever end at 19.45.

---

## 6. ⚠️ Inherited problems the preview did NOT address

| Issue | Status in V3 |
|---|---|
| 6 charts on slide 28 still point at `tataprojects4-my.sharepoint.com/.../TPL Weekly report-18.xlsx` | ❌ unchanged — will fail on the CEO's machine |
| 3-D bar chart (`chart5`) | ❌ unchanged |
| File size | ❌ **75.8 MB**; `ppt/media` still **69 MB**, 20 images > 1 MB |
| ~30 off-canvas orphan shapes on slides 14, 18, 20–27, 31–33 | ❌ unchanged |
| 12 typefaces / 14 embedded fonts | ❌ unchanged |
| Slides 6–38 still on the superseded dark-header or original styling | ❌ by design (flagship-only scope) |

---

## 7. ✅ What V3 genuinely gets right

- **New content that did not exist in the original:** the variance tiles (−61 % FTM, −67 % CUM, ₹76.2 Cr gap to close) are computed *insight*, not restyling. This is the strongest idea in the deck and should be extended everywhere.
- **Commercial Progress** is now a real grouped bar (Baseline / Revamp / Actual × FTM / CUM) instead of a static 5 × 3 text grid.
- **The palette is finally disciplined:** `17375E` navy · `1479B8` TATA blue · `2EA85B` green · `F2A900` amber · `E23B3B` red · `62758A` / `1C2430` text greys · `DEE3EA` rule. **One green, one amber, one red** — against four greens in the original. Freeze this as the system.
- Card geometry is internally consistent per row (4.47 in × 4 @ 0.305 gutter; 6.10 in × 3 @ 0.30).
- Zero off-canvas shapes, zero schema violations.

---

## 8. Priority fix list before this goes anywhere near the CEO

1. **×1.5 the whole type scale.** Title 60 pt, section 30 pt, body 21 pt, floor 18 pt. Raise `chart8`'s hardcoded `sz="1400"` to `2100`.
2. **Move value labels back inside the charts** and fix the wrap properly (axis-max headroom), so the visible number *is* the linked number.
3. **Add `c:delete val="1"` to both axes** on `chart10–13`, or replace the four mini bars with one 4-category bar chart.
4. **Consolidate to a single embedded workbook** driving every chart on the slide.
5. **Snap to one 0.60 in margin / 0.30 in gutter grid** — kill the 19.20 / 19.25 / 19.40 / 19.45 / 19.50 spread and align the title to x = 0.60.
6. Only then roll the system out to slides 6–38, and run the SharePoint-link + image-weight hygiene pass separately.

---

## 9. 🔴 Separate and urgent: confidential data in a PUBLIC repo

`hasnainmakada-99/Data-Science-Codes` is **public**. `KAMIL BHAI WORK/` currently exposes to anyone on the internet:

- Adani Lucknow Airport City **contract value (₹1,725 Cr)**, programme dates, commercial variance vs baseline, critical issues, key decisions and payment requests
- Tata Projects **EHS and quality performance data** (LTI, near misses, NCR, FTRI, man-hours)
- Client MOM tracker content with named action owners and target dates
- A **live internal SharePoint URL** embedded in the deck: `tataprojects4-my.sharepoint.com/personal/sanjayt_tataprojects_com/...`

This is client-confidential commercial and safety data belonging to third parties. **Recommend making the repo private or removing this folder immediately.** Note that deleting the files is not sufficient — the blobs remain in git history and would require a history rewrite or repo deletion.

---

*Companion document: `DECK_FORENSIC_ANALYSIS.md` (audit of the original deck) in the same folder.*
