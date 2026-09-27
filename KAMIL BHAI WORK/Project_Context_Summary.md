# MRM Aug'26 Presentation Redesign — Project Context

## Background

- **Source file:** `MRM Aug-26 _ Presented (1).pptx` — a 38-slide Monthly Review Meeting deck for the **Adani Lucknow Airport City** construction project.
- **Parties:** Client — Adani Lucknow Airport City Ltd. Contractor — Tata Projects Limited (TPL). Executive Consultant — Edifice. PMC — Turner & Townsend.
- **Project facts:** Contract value ₹1,725 Cr, 39-month duration, completion target 15 May 2029. Scope includes a 3-Star Hotel, 4-Star Hotel, Convention Centre, and Retail blocks.
- **Purpose of the ask:** The user needs this deck rebuilt for presentation to the **Adani CEO** — high-stakes, needs to look premium and professional.

## Deck structure (as originally analyzed)

- Slides 1–4: title, safety assembly point, quality pledge — **explicitly off-limits, never to be changed**.
- Slides 5–13: dense numeric dashboards (Executive, Design, GFC Drawings, BIM Status, BIM Clash Report, MEP Packages, Procurement, Construction, Mobilization).
- Slides 14–16: Minutes-of-Meeting (MOM) tracker tables.
- Slide 17: September 2026 Plan.
- Slide 18: divider slide with embedded OLE/Excel objects (pre-existing, left untouched).
- Slide 19: Post-Novation Statutory Compliance Status.
- Slide 20: EHS Performance Dashboard.
- Slides 21–26: Safety/HSE good-practice photo slides.
- Slides 27–28: Quality Indicators / Quality Performance Dashboard (28 already had 7 native charts, well-designed, left untouched).
- Slides 29–37: Quality training photos, progress-comparison slides, site infrastructure photos.
- Slide 38: closing/logo-only slide.

## Standing constraints (given early, never revoked)

1. **Slides 1–4 must never be changed.**
2. **Logo placements** (TATA, Turner & Townsend, Adani) must stay in their exact original positions on every slide — confirmed explicitly and re-confirmed multiple times.

## Chronological request history

### 1. Initial ask
"I am already having a presentation and I want to make it new and beautify it with excel linked sheet." No existing Excel file — one needed to be created from scratch, with slide charts linked to it.

### 2. Analysis phase
Full read-through of the deck's structure and data content was done and explained back to the user before any changes.

### 3. First build — chart-linked dashboards
Built a master Excel workbook (`MRM_Aug26_Dashboard_Data.xlsx`, 9 tabs, formula-driven) and replaced static tables/text on 7 dashboard slides (5, 6, 9, 12, 13, 17, 27) with native, Excel-embedded PowerPoint charts. Environment had no Node/Python/Office tooling installed — Node.js, Python, LibreOffice, and Poppler were installed via winget (with user approval) to enable this work.

### 4. RAG color-coding request
User: client specifically wants a **Red/Amber/Green (RAG)** status template, but **TATA's blue** must also remain present.
- Clarified scope via question: RAG applied to status indicators **and** single-series/status-type charts; multi-series comparison charts keep TATA blue (`#1479B8`) as the brand accent.
- Applied RAG thresholds (green ≥70%, amber 40–69%, red <40% for progress-type metrics; similar tiering for defect counts and clash severity) across both the deck and the Excel workbook.
- Corrected a data-mapping bug found in the process: the deck's "Leading Indicators" and "Lagging Indicators" on slide 27 had been swapped in the initial build; fixed by checking the actual header-chip text in the original file.

### 5. "Do the Excel links break?" question
User asked whether the Excel links were intact. Verified at the byte/XML level (not assumed): confirmed all 14 newly-added charts have valid embedded workbooks; found and disclosed two **pre-existing** conditions in the original file (unrelated to the rebuild): slide 28's charts link to an **external SharePoint file** rather than an embedded one, and 4 orphaned/unused embedded workbook fragments exist in the package.

### 6. Zip file request and PowerPoint repair-prompt bug
User asked for a zip of both files. Initial zip download reportedly failed (~75MB, likely a size/client limit). While diagnosing, the user reported **PowerPoint showing a "found a problem with content" repair prompt** on the pptx.

**Root cause found and fixed (verified independently, not assumed):**
- A duplicate `<a:effectLst>` (shadow effect) element on several shadow-card shapes — schema-invalid (OOXML allows at most one). Caused by shadow-adding code appending a new effect list without removing an existing one. Fixed by always clearing existing effect lists first.
- A **pre-existing** duplicate shape-ID issue on slide 18 (confirmed present in the user's original file too, not introduced by the rebuild) — fixed by renumbering only, without touching slide 18's embedded OLE content.
- A full-file XML scan was added to the workflow from this point on to catch this class of bug before delivery, not just spot-check individual slides.

### 7. "I want everything new" pivot
User: existing redesign still "looked too similar" to the original template — same layout bones, just recolored.
- Clarified and locked scope via questions: **all ~34 non-title slides** get a full rebuild (not just the 7 dashboards), logos stay exactly as before.
- Picked a visual direction via question: **"Premium Dark Executive"** — dark navy header band, borderless shadow-cards, minimal chart gridlines.
- Built and delivered a full-deck pass: navy title bands (dynamically sized to avoid logo zones), borderless shadow-cards replacing the original colored-outline-box + solid-chip-label pattern, RAG-colored status badges, styled MOM tracker tables (navy header row, banded rows), minimal-gridline charts.
- **Additional real bugs found and fixed during this pass** (each independently verified via automated full-deck XML scans, not just visual spot-checks):
  - Same duplicate-`effectLst` bug reintroduced by a new shadow-adding helper function — fixed at the source and reverified deck-wide.
  - A float-vs-integer EMU bug: dividing `Inches()` values for column math produced floats, which python-pptx wrote as invalid non-integer XML attributes — fixed by coercing all computed shape coordinates to integers before use.
  - Logo-detection was initially too permissive and briefly deleted slide 27's TATA logo (uniquely, on that slide, the logo is nested inside a full-slide decorative background group rather than being a standalone shape) — caught, fixed the detector, and slide 27 was excluded from the aggressive rebuild pass to protect its original artwork.
  - A title-detection bug: a large "83.4%" stat number (appearing earlier in shape order than the real title) was mistakenly picked as the slide title on slide 8, given a navy band that covered the actual content — caught, fixed, and the whole deck was re-swept since the same bug could have hit other slides.

### 8. "You didn't really change anything" — second major pivot
User feedback, delivered forcefully and specifically:
1. The presentation is **not consistent** — the rebuilt dashboard slides look different from the untouched "in between" slides (MOM tracker, compliance, EHS, photo slides).
2. **Fonts are terribly small**, "nothing visible."
3. **Reject the dark header** entirely.
4. Go back to a **white background** format like the original, but upgraded.
5. **Alignment was very bad** throughout — elements not lining up, not just a color/font issue but actual positioning/geometry.
6. Wants **graphs/charts, the internal data-representation style, the box/card shapes, and the color palette** all genuinely reinvented — not just recolored.
7. **Every piece of data**, including small elements like progress bars and mini-stats, must be Excel-linked — not just the headline charts.
8. Explicit instruction: **talk it through and get confirmation before building anything else.**

### 9. Agreed approach (current status)
Proposed and the user approved, in this order:
1. Lock a single design system first (palette, type scale, grid, card style) — apply identically everywhere, not improvised per slide.
2. Every meaningful number becomes a real linked chart object, including small stats — using axis-less mini bar/doughnut charts so they read as compact indicators rather than full "standard" charts.
3. Build **one flagship slide only** (Executive Dashboard) fully in the new system and send it for review — **before** touching any other slide, given three prior misses.
4. Only after that slide is approved, apply the same system to the rest of the deck, then run full automated QA (overlap/overflow bounds-checking, schema/duplicate-ID scans, official OOXML validation) before final delivery.

### 10. Flagship slide (V3) — built and under review
Rebuilt the Executive Dashboard from scratch in a new system:
- White background throughout, no dark band — large bold navy title directly on white.
- New **third distinct card style**: flat white cards with a solid-color **header strip** (not the original colored-outline box, not the previous dark-hero shadow-card).
- Font sizes raised significantly (title 40pt, chart/data labels 14pt+, body 14pt).
- KPI facts (Contract Value, Duration, Completion, Health) as header-strip cards.
- Commercial Progress as a larger, cleaner bar chart with **new computed insight tiles** (variance vs baseline, RAG-colored) that didn't exist in the original.
- Safety & Quality metrics — including small stats like LTI, Near Misses, Inductions, Open NCR — rebuilt as individual tiny **linked bar charts** (axis-less, value labeled) rather than static numbers, directly addressing the "all data Excel-linked" requirement.
- FTRI shown as a doughnut gauge.

**Bugs hit and fixed during this build** (again, verified, not assumed):
- A vertical-layout math error caused the bottom row of cards to run off the bottom of the slide — fixed by switching from hand-guessed offsets to a proper accumulating cursor, with a programmatic bounds-check added to catch this class of error going forward.
- A mini-bar chart's data label wrapped to 3 lines ("1,691" → "1,\n69\n1") — traced to the bar sitting too close to its max axis scale, leaving no room for an outside-end label; fixed more robustly by moving the value label out of the chart into an adjacent textbox (chart still holds the real linked data).
- A doughnut gauge's center/sub-label text visually overlapped ("FTRI SCORE" read as "ETRI SCORE") — initially misdiagnosed as a text-positioning issue (repositioning had zero visual effect, which was itself the clue); actual cause was LibreOffice auto-rendering a default data label on the chart itself, which was never explicitly disabled. Fixed by explicitly setting `has_data_labels = False` on the chart.
- The preview file inherited the same pre-existing slide-18 duplicate-ID issue described above; patched the same way.

**Current state:** One file — `MRM_Slide5_Preview.pptx` — containing only the rebuilt Executive Dashboard slide (all other slides unchanged from the original source) — was sent to the user for review. Waiting on their reaction before applying the same system to the rest of the deck.

## Deliverables produced so far

- `MRM_Aug26_Dashboard_Data.xlsx` — master Excel workbook, 9 tabs, formula-driven, RAG + TATA-blue styled charts.
- `MRM_Aug26_Redesigned.pptx` — full 38-slide deck, most recent full-deck pass (Premium Dark Executive direction — since superseded by the white-background pivot, not yet rebuilt deck-wide in the new system).
- `MRM_Aug26_Redesigned_Package.zip` — zip of the two files above.
- `MRM_Slide5_Preview.pptx` — single-slide preview of the new white-background design system, currently awaiting user feedback.

## Open items / not yet done

- Full-deck rebuild in the new white-background system (pending approval of the flagship slide).
- Slide 27 still carries an older treatment (its original TATA logo is uniquely embedded in background art, so it was deliberately excluded from the aggressive rebuild).
- MOM tracker, compliance, EHS, and photo slides have not yet received the new white-background system — only the earlier dark-header-era shell treatment.
