# MRM Aug-26 Deck — Forensic Analysis & Cross-Check

**Source:** `KAMIL BHAI WORK/MRM Aug-26 _ Presented (1).pptx` (78.6 MB) — the **ORIGINAL** deck, not any redesign.
**Cross-checked against:** `Project_Context_Summary.md` + `Full_Chat_Transcript.md` (same folder).
**Method:** OOXML package unpacked + python-pptx shape/geometry/typography audit. Every claim below was measured, not assumed.

---

## 1. Ground truth: what the file actually is

| Property | Value |
|---|---|
| Slides | 38 |
| Canvas | **20.0 × 11.25 in** (18288000 × 10287000 EMU) — 16:9 but **1.5× the standard 13.33 × 7.5 in** |
| Slide masters / layouts | 1 master, 13 layouts |
| Notes slides | 20 |
| Real chart objects | **7** — all on slide 28 only |
| Embedded OLE objects | 4 — all on slide 18 only |
| Tables | 4 (slides 6, 14, 15, 16) |
| Pictures | 80 (69 MB of `ppt/media`) |
| Embedded fonts | 14 `.fntdata` files (~3.8 MB) |

**Shape census (whole deck): 860 AutoShapes · 314 Freeforms · 272 Groups · 134 TextBoxes · 80 Pictures · 14 Placeholders · 7 Charts · 4 Tables · 4 OLE · 2 Lines**

> 🔎 **The single most important structural fact:** with 1,446 drawn shapes against only **14 placeholders**, this deck is effectively **hand-drawn artwork**, not a layout-driven deck. The master/layouts are barely used. That is the root cause of *both* the alignment complaint *and* why every automated rebuild pass kept breaking things.

---

## 2. ✅ Claims in the context docs — verified against the file

| Claim in the MD docs | Verdict | Evidence found in the file |
|---|---|---|
| 38 slides, Adani Lucknow Airport City MRM | ✅ True | 38 slides; slide 5 carries ₹1,725 Cr / 39 Months / 15 May 2029 / Adani + Edifice + Turner & Townsend |
| Slide 28 already had 7 native charts | ✅ True | `chart1–chart7.xml`, all on slide 28 |
| Slide 28 links to an **external SharePoint** file | ✅ True | `chart1–chart6` rels → `https://tataprojects4-my.sharepoint.com/.../TPL Weekly report-18.xlsx` (TargetMode=External) |
| Slide 18 has **duplicate shape IDs** (pre-existing) | ✅ True | `slide18.xml` — ids **31, 33, 44, 47** each appear twice |
| Slide 18 has embedded OLE/Excel objects | ✅ True | 4 × `EMBEDDED_OLE_OBJECT` → `Microsoft_Excel_Worksheet{,1,2,3}.xlsx` |
| Slide 27's TATA logo is nested inside a background group | ✅ True | Slide 27 is 42 groups / 45 freeforms deep — no standalone logo shape |
| "Fonts are terribly small, nothing visible" | ✅ **True and worse than it looks** — see §3 |
| "Alignment was very bad" | ✅ True — see §4 |
| Slides 1–4 are title / assembly point / pledge | ✅ True |

## 3. ❗ Claims that are WRONG — correct these before any further work

### 3.1 "4 orphaned / unused embedded workbook fragments exist"
**False.** There are 5 embedded workbooks and **all 5 are referenced**:
- `Microsoft_Excel_Worksheet{,1,2,3}.xlsx` → the four slide-18 OLE objects
- `Microsoft_Excel_Worksheet4.xlsx` → `chart7`

Deleting them as "orphans" would **break slide 18 and slide 28's 7th chart.** This was mis-diagnosed in the earlier session.

### 3.2 "Duplicate `<a:effectLst>` was a pre-existing condition"
**False — it was 100% self-inflicted.** Every slide in the original contains **at most one** `a:effectLst`. The schema violation that produced PowerPoint's *"found a problem with content"* repair prompt was introduced by the shadow-adding helper, not inherited. (The docs do mostly say this, but the framing drifts — the original file is clean on this.)

### 3.3 "chart7 also links to SharePoint"
**Partly wrong.** Only **charts 1–6** point at the SharePoint URL. **chart7 is properly embedded.** So slide 28 is a *mixed* state, not uniformly external.

---

## 4. 🔤 Why the fonts really are unreadable — the finding nobody caught

The canvas is **20 in wide, 1.5× the normal 13.33 in**. PowerPoint scales the *view*, not the *point size* — so **every font on this deck renders at 2/3 of its nominal value** relative to a normal deck.

| Nominal size in file | Effective size on a standard 13.33in deck |
|---|---|
| 12 pt | **8 pt** |
| 14 pt | **9.3 pt** |
| 16 pt | **10.7 pt** |
| 17 pt | **11.3 pt** |
| 20 pt | 13.3 pt |
| 24 pt | 16 pt |

**Measured body-text floor per slide:** 7.2 pt (slide 19) · 9.3 pt (slide 9) · 10.5 pt (slide 20) · 12 pt (slides 10, 12, 13, 18, 21–26) · 13–14 pt (slides 6, 7, 17, 27).

➡️ Slide 19's smallest run renders at an **effective 4.8 pt**. Slide 20's dashboard body text is effectively **7 pt**. On a boardroom projector at the back of the room that is genuinely invisible — **the user's complaint is objectively correct, and the earlier "raise to 14pt+" fix was nowhere near enough.**

**Rule for the rebuild: on this 20-in canvas, minimum body = 21 pt, labels = 24 pt, sub-headers = 30 pt, titles = 54–60 pt** (i.e. multiply your intended standard-deck sizes by 1.5). The V3 flagship's "title 40pt / body 14pt" is therefore still *too small* — it reads as 27pt / 9pt.

### Typography chaos
**12+ distinct typefaces across the slides:** Trebuchet MS (507 runs), Calibri (MS) Bold (229), Calibri (MS) (95), Aptos (84), Canva Sans (48), Canva Sans Bold (28), Fredoka (26), Adani Regular (22), Caladea Bold (21), Arial (19), Cinzel Bold, Roboto.
**~40 distinct point sizes**, including non-integer values from scaling accidents: `7.2, 9.3, 10.52, 13.49, 17.25, 18.02, 19.98, 27.98, 28.01, 54.99, 55.98, 58.01, 122.45`.
`Fredoka` and `Canva Sans` are a dead giveaway that parts of this deck were pasted in from Canva. **210 runs have no explicit size at all** (inheriting from the master) — those will shift unpredictably on any machine.

---

## 5. 📐 Alignment audit — quantified

Near-miss edges (shapes whose left edges are *within 0.06 in* of each other but **not equal** — i.e. visually "almost aligned", which reads as sloppy):

| Slide | Distinct X positions | Near-miss pairs |
|---|---|---|
| 7 | 63 | **17** |
| 20 | 47 | **15** |
| 13 | 66 | **15** |
| 19 | 49 | **13** |
| 8 | 44 | 9 |
| 11 | 51 | 9 |
| 10 | 38 | 8 |
| 27 | 40 | 6 |

Slide 5 alone has **65 distinct left-edge positions**; slide 13 has **66**. A disciplined deck would have 4–8. **There is no grid.**

### Shapes hanging off the canvas (measured, `left<0` or `right>20in` or `bottom>11.25in`)
| Slide | Count | Worst offender |
|---|---|---|
| 14 | 1 | `TextBox 1` sits at **x = 23.54 in** — entirely off-slide (invisible junk) |
| 18 | 4 | groups at y = −0.77 in and x → 21.83 in |
| 20 | 2 | `TextBox 126` extends to x = 20.41 in |
| 21 / 22 / 23 / 24 / 25 / 26 | 4/4/3/3/3/5 | slide 24's `Group 16` is at **y = −2.24 to −0.03 in → fully above the slide** |
| 27 | 2 | groups run to x = 21.83 in (clipped) |
| 31 | 1 | `TextBox 9` starts at **x = −1.01 in** |
| 32 / 33 | 1 each | `Group 10` at y = −0.58 in |

**~30 shapes across 13 slides are partly or wholly outside the canvas.** Some are invisible leftovers; some are visibly clipped. This is the concrete, fixable core of "alignment was very bad".

---

## 6. 📊 Chart & data-representation reality

The deck is described as a "dashboard" but contains only **7 real chart objects**, all on slide 28:

| Chart | Type | Data (live values read from cache) |
|---|---|---|
| Chart 15 | Doughnut | Open Obs 8 / Close Obs 24 |
| Chart 16 | Doughnut | Close 103 / Open 20 |
| Chart 17 | Bar clustered | Cum. Trainings 44 / Cum. Man Hours 450.02 |
| Chart 20 | Doughnut | Close 60 / Open 0 |
| chart5 | **3-D Bar** | ⚠️ 3-D chart — unreadable, unprofessional for CEO review |
| chart1–7 | — | **5 of 7 are doughnuts** — poor for comparison, the classic "looks like a dashboard but says nothing" pattern |

**Everything else that looks like data is fake:** progress bars, %, KPI tiles, RAG chips on slides 5–13, 17, 19, 20, 27 are all AutoShapes + static text. Confirmed by the shape census — slides 5–13 contain **0 charts and 35–122 AutoShapes each**.

➡️ This is exactly why the user keeps saying *"all the data, even the small representations, must be Excel-linked"* — **currently 0% of the dashboard numbers are linked to anything.**

### Key data captured from the original (for rebuilding the workbook)
- **Slide 5 Commercial Progress —** FTM: Baseline ₹40.00 Cr / Revamp ₹31.06 Cr / Actual ₹15.50 Cr / Gap vs BL ₹24.50 Cr / Gap vs RV ₹15.36 Cr · CUM: BL ₹114.00 Cr / RV ₹54.00 Cr / Actual ₹37.80 Cr / Gap vs BL ₹76.20 Cr / Gap vs RV ₹16.20 Cr
- **Slide 5 Safety & Quality —** Manhours 344,498 · LTI 0 · Near Misses 4 · Inductions 1,691 · WIR C/O 118/26 · MIR C/O 63/1 · Open NCR 1 · FTRI 88%
- **Slide 6 Design —** DD Submitted 1,220 (1,014 appr = 83%) · GFC Submitted 247 (178 appr = 72%) · backlog ICT 170, Arch GFC 39, Struct GFC 30 · table 19×9
- **Slide 20 EHS (FTM → ITD) —** Safe Man-Hours 1,27,954 → 3,44,498 · Inductions 585 → 1,691 · Training Sessions 35 → 109 · TBT 265 → 615 · Safety Observations 122 → 781 · Fatalities/LTI 0 · RWC/MTC 0 · HiPo/Near Misses 4
- **Slide 27 Quality —** Leading: Training 74, Mat/Equip Approvals 12, Mockups 5, Good Practices 16, Mgmt Walkdown 9, FTRI 88, Deviation Closure in TAT 19.9 · Lagging: Repetitive Deviations 0, Rejection 1, Snag 0, Stop Work 0, Flash Report 0, Obs Internal 15, Obs External 32

---

## 7. 🎨 The actual palette in the file (measured)

| Hex | Role | Usage count |
|---|---|---|
| `#26384E` | dominant text navy | 97 |
| `#17375E` | heading navy | 55 |
| `#62758A` / `#68798C` | muted gray-blue | 63 |
| `#38A856` / `#39A852` / `#00B050` / `#2E8B57` | 🟢 **four different greens** | 94 |
| `#1479B8` | TATA blue accent | 62 |
| `#F2A900` / `#FFC000` | 🟡 **two ambers** | 55 |
| `#E23B3B` | 🔴 red | 10 |
| `#7657C8` | purple (off-brand) | 38 |
| `#E9EFF5`, `#F7FAFD`, `#F7F4FC` | card tints | 54 |

⚠️ **Four greens, two ambers, two navies and a stray purple.** There is no palette — there are accumulated copy-pastes. A RAG system is impossible to read reliably when green means four different hex values.

---

## 8. 💾 File-health issues

- **78.6 MB** is far too heavy to email; the earlier zip-download failure was a direct consequence.
  - `image75.png` = **15.3 MB**, `image71.png` = **11.1 MB** — two images are **34% of the entire file**. 20 images exceed 1 MB. 69 MB of the 78 MB is `ppt/media`.
  - Fix: downsample to 1920px-long-edge JPEG (q85) → realistically **78 MB → 12–18 MB** with zero visible loss at projection size.
- **14 embedded fonts (~3.8 MB)** including `Canva Sans`, `Fredoka`, `Cinzel Bold` — license-questionable and mostly unnecessary. Keep only `Adani Regular` + one system fallback.
- **SharePoint-linked charts** will show *"this chart's data source cannot be reached"* on any machine outside the TPL tenant — **including, very likely, the Adani CEO's laptop.** These must be converted to embedded workbooks before the presentation.
- **Slide 18 duplicate IDs** are a latent corruption risk — patch by renumbering only, never touch the OLE payloads.
- Slide 9 is silently dropped by LibreOffice PDF export (noted in the transcript) — confirmed a LibreOffice quirk, not file damage, but it means **LibreOffice cannot be trusted as the sole QA renderer.**

---

## 9. 🧭 Transcript read: why 3 attempts failed, and what that implies

The transcript shows the same failure loop three times:

1. **Attempt 1** (7 dashboard slides → Excel charts) → *"you did not change anything"*
2. **Attempt 2** (all 34 slides, Premium Dark Executive) → *"not in line with format, fonts terribly small, don't want dark header"*
3. **Attempt 3** (V3 white flagship, slide 5 only) → **awaiting verdict**

**The pattern:** each attempt restyled *containers* (colors, cards, headers) while leaving the **information architecture, the 1.5× font-scale problem, and the no-grid geometry** untouched. That is precisely what "you just changed colours" means.

**What this analysis adds that the previous three attempts didn't have:**
- The **1.5× canvas scale** — explains the font complaint mathematically and means the V3 flagship (40pt title / 14pt body) is *still* too small. Multiply by 1.5.
- The **30 off-canvas shapes** and **17 near-miss alignments on a single slide** — "bad alignment" is now a concrete, checkable list, not a vibe.
- The **palette has 4 greens** — RAG can't work until that's collapsed to one green / one amber / one red.
- **0% of slides 5–27 data is linked** — the Excel-linking task is 10× bigger than "add charts to 7 slides".
- Two claims in the handoff doc are **wrong** (the "orphan" workbooks, the "pre-existing" effectLst) and acting on them would break the file.

---

## 10. ✅ Recommended next moves (in order)

1. **Do not touch anything until the V3 flagship verdict comes in** — that was an explicit instruction and breaking it again is the fastest way to lose trust.
2. **Send a font-scale correction note with the flagship**: "your deck is 20in wide, so my 40pt title reads as 27pt — I'll rescale the whole system by 1.5×." This directly answers the #1 complaint and proves the diagnosis.
3. **Lock the design system as a table before building**: 1 navy, 1 TATA blue, exactly 1 green / 1 amber / 1 red, 2 grays, 2 tints. One typeface family (Adani Regular + fallback). A 12-column grid on 20in with 0.8in margins → column = 1.53in. A 6-step type scale: 60 / 42 / 30 / 24 / 21 / 18 pt.
4. **Fix the file hygiene separately and first** (it's low-risk, high-visibility): downsample the 20 oversized images, delete the ~30 off-canvas orphan shapes, renumber slide-18 IDs, convert the 6 SharePoint charts to embedded workbooks, drop the 3-D chart. This alone takes the deck from 78 MB → ~15 MB and removes the "data source unreachable" risk in front of the CEO.
5. **Then** roll the system out slide-by-slide with the automated QA gate (bounds check + duplicate-element scan + OOXML validation) already built in the previous session.

---

*Files in `KAMIL BHAI WORK/`: `MRM Aug-26 _ Presented (1).pptx` (78.6 MB, original), `Project_Context_Summary.md` (12 KB), `Full_Chat_Transcript.md` (16 KB). The redesign outputs referenced in the docs — `MRM_Aug26_Dashboard_Data.xlsx`, `MRM_Aug26_Redesigned.pptx`, `MRM_Slide5_Preview.pptx` — are **not** in the repo.*
