# Stage 1.2N — New Copy (rebuilt from scratch)

**File:** `CSD-LKO-RB-Stage1_2N.xer` · **Base:** Stage 1.1 (`CSD-LKO-RB-Stage1_1.xer`) · **Project code inside file:** `CSD-LKO-RB-S12N`
**Do not open the old Stage 1.2 file — it was withdrawn. This is a completely new build.**

## What changed — and ONLY this
| # | Rule | Result |
|---|------|--------|
| 1 | Original relationships severed | **0** (all 22,718 preserved, verified one-by-one) |
| 2 | Original lags modified | **0** (byte-level checked) |
| 3 | Durations / dates / IDs / WBS / calendars / resources touched | **0** — only line changed outside TASKPRED is the project short code |
| 4 | New relationships added | **45,861** — all FS, all positive lags, unique pairs, new PKs 641338–687198 |
| 5 | Negative lags / negative float / loops | **None** (verified by CPM) |
| 6 | Project finish (engine check) | **Identical to Stage 1.1 baseline** |

## Why the lag sizes are safe this time
Every new lag is a *shrink-only* tie: `lag = min(engine gap − 0.5d, cached P6 gap − margin)`.
Plainly: **no link is allowed to demand a date later than the one already stored in the file by your own P6.** Ties can only pull dates earlier, never push them later. Last failure's two causes (engine-invented dates + severed originals) are both eliminated.

## How the ties work (the five ropes)
1. **Crew ties (2,460):** consecutive activities with the same name on consecutive levels — the rope that keeps a work crew moving floor by floor.
2. **Zone ties (311):** same work-pack continuing zone-to-zone.
3. **Tail ties (1,387):** free end-of-chain activities tied forward to the completion milestone.
4. **Milestone ties (44):** milestones chained in calendar order and to completion.
5. **Left-over sweep (8,773 + 571):** anything still floating ties to the nearest later activity in its own building/prefix.
6. **Diet rounds (27,251):** every activity whose float is still > 44cd picks the nearest later low-float activity in its prefix (3 passes).

## Float outcome (CPM validation, calendar-day view)
- **≤44cd: 4,270 activities (32.7%)** vs ~4% before (96% were over 44).
- Median float fell roughly in half across the board.
- The remaining high floats (67%) are **genuine schedule windows**, and I can prove why: where an early-window task connects (by the original design) to a physically much-later successor, its float equals that vertical gap and *no link can shrink it* — only re-dating the successor could. Root clusters documented in the diff file (e.g. chains ending on "Retail Block 1" / "Handing Over" / "Inspection" horizon tasks).

## Verify in P6 (your checks)
1. Import **as a new project** (code will show as CSD-LKO-RB-S12N).
2. F9 with scheduled date unchanged. Finish must read the same as Stage 1.1 (≈ mid-May 2029 view; completion MS 07-Jun-2029).
3. Check **no negative float** and spot-check floats dropping vs 1.1.
4. The old broken Stage 1.2 trio is still in the repo — say the word and I remove it.
