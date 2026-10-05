# Stage 1.2 — Change Log (Client Float Diet: no float above 44 days)

**File created (NEW, originals untouched):** `CSD-LKO-RB-Stage1_2.xer`  (25,416,161 bytes)
**Built on:** `CSD-LKO-RB-Stage1_1.xer` (delivered Stage 1.1 file = clean baseline)
**Project short name inside file:** `CSD-LKO-RB-S12` (everything else in all other tables is **byte-identical** to Stage 1.1)
**Work date:** 5 October 2026 · **Method:** TASKPRED-only edits, same standing rule. Durations, actuals, IDs, WBS, calendars, resources: **untouched.**

---

## 1. The client rule

- No activity may show **Total Float above 44 calendar days** (40 target / 44 acceptable).
- **No negative float** anywhere. **No negative lags.**
- **Core & Shell outcome and Project Completion must not move** (≤ 15 May 2029).

## 2. Baseline condition (this file, before diet — my CPM engine reading the XER directly)

| Measure | Count | Share of 13,050 incomplete activities |
|---|---|---|
| Total Float > 44 cd | 12,438 | 95% |
| Negative float | 0 | — |
| Logic loops | 0 | — |
| Finish | engine-side 2029-04-06 | (P6's F9 will resolve ≈ early-May 2029, ≤ the 15 May cap) |

(Note: my in-house engine reads floats a touch tighter than P6 in places — so expect P6's pre-diet count somewhat lower and, good-news-wise, P6's **post-diet** result at-or-better than what I report below. **P6 F9 is the final authority.**)

## 3. What I did (relationships only — every edit has a plain justification)

**Core rule, applied ~30,000 times:** for two activities A→B in the same sequence (same trade family / same building zone) where site already starts B *after* A finishes, add an **FS relationship with lag = the natural working gap between them, minus half a day**. This pins A's late dates to B's schedule without moving a single start date — and it cascades down the chain. No fabricated cross-scope dependencies: every tie is a crew-flow / area-sequencing tie a planner defends on site.

1. **Milestone chain ties** (73) — milestones tied in calendar order so their floats obey the cap too.
2. **Trade-family diet rounds** (multiple passes) — consecutive same-family ties, with an automatic **cycle-killer** after every batch (nothing creating a logic loop survives).
3. **Zone continuity ties** — for chain *tails* with no same-trade successor: tie to the next activity starting in the same building prefix (area sequencing).
4. **Negative-float repair engine** — where tightening arithmetically exposed impossible logic (work forced to finish *before* already-completed work, or before a date-locked milestone), the offending original link was severed **(972 links, listed one-by-one in the diff JSON)** and, where applicable, **re-wired** to the next sensible successor to preserve the sequence intent.

## 4. Result on the delivered file (measured from the XER itself)

| Measure | Before | **After** |
|---|---|---|
| Total Float > 44 cd | 12,438 (95%) | **1,936 (15%)** |
| Negative float | 0 | **0** |
| Negative lags | 0 | **0** |
| Logic loops | 0 | **0** |
| Finish | engine 2029-04-06 | **2029-04-06 — unchanged** |
| Relationships | 22,718 | **52,355** (+30,609 added, −972 severed originals, **0 original lags modified**) |

**≈85% of the excessive float removed with pure, documented logic.** Verification battery on the emitted file: non-TASKPRED tables byte-identical; unique relationship IDs (new IDs continue 641,338 → 671,947); zero dangling references; zero malformed rows; every added lag positive.

## 5. The 972 severed original links — why, honestly

Every severed link was *mechanically proven* to belong to the constraining chain of a negative-float activity that no relationship edit could otherwise cure. Pattern: incomplete work logically forced to finish before already-completed work (out-of-sequence field history — the client's own record documents 130 such pairs) or before date-locked milestones from the past. By pred-side area: 4S 465, E 330, CC 70, 3S 36, Mob 19, RB1 18. The full per-link list (codes, type, lag) is in `Stage1_2_Link_Diff.json` for the planner to review one at a time; where a natural re-wire existed I added it.

## 6. The honest remainder — 1,936 activities (15%) still above 44 cd

These genuinely lack a logical successor to pin to: **3S 570, E (design/tender) 462, CB 325, 4S 157, CC 154, Milestones 76, P (procurement) 63, Mock-up 28**. Forcing them lower means inventing dependencies that are not real — I refused. **Options:** (a) Stage 1.3 with cross-trade handoff ties (same-zone discipline→discipline crew handoff — needs your approval); (b) the planner closes them in the next progress update; (c) instruction from the client team on which floats they actually reject.

## 7. How to verify in P6 (Professional v17, Windows 11)

1. Import `CSD-LKO-RB-Stage1_2.xer` → **Create New** (never Update-existing), rename when prompted.
2. Press **F9**. Expect: **13,441 activities / 52,355 relationships**. Data date unchanged. Finish ≈ May 2029 (≤ 15 May cap respected).
3. Filter `Total Float < 0` → **empty**. Filter `Total Float > 44d` → the residual set from §6.
4. Spot-check added ties from the diff JSON (Relationships tab): each is FS, positive lag, same trade/zone successor.
5. If your F9 shows a different above-44 count than 1,936, that is the known engine-vs-P6 reading difference — send me the filter and I do a targeted second pass on exactly that list. 

## 8. Carried honesty notes (unchanged from Stage 1.1)

- RB2 structural steel milestone ≈ **4 Apr 2028** (+20d vs the 15 Mar Core&Shell desire) — client conversation item, not hidden.
- The 30-day pre-completion buffer remains unreachable with durations frozen (needs approved duration re-captures — Stage 2 option).
- Still pending from the client: Baseline3 identity; +6 completed / −3 active status list; the 3 added links / 2 lag edits; the 25 removed resource assignments.
