# Stage 1.1 — Corrected Logic Rebuild of `CSD-LKO-RB`

**Date:** 5 Oct 2026 · **Supersedes:** `CSD-LKO-RB-Stage1.xer` (**do NOT import that file — see §1**)
**Output:** `CSD-LKO-RB-Stage1_1.xer` (project inside named **CSD-LKO-RB-S11**; your original `CSD-LKO-RB` is untouched)

---

## 1. What went wrong with Stage 1 — root cause, found and fixed

You were right to stop. I ran a byte-level forensic audit. The verdict:

| Check | Stage 1 file |
|---|---|
| All 15 data tables (activities, WBS, calendars, resources…) | ✅ identical to your file |
| Relationship rows added | ✅ the right 103 edits, −46 removals |
| **Primary keys of the relationship table (`task_pred_id`)** | ❌ **BROKEN — key `618223` repeated 104 times** |
| Cached early dates on my added rows | ❌ junk dates copied from a sample row (harmless but ugly) |

**Plain explanation:** every relationship in an XER file carries its own unique ID number (row `618223`, `618224`, …). When my tooling generated the 103 new relationships, it stamped them **all with the same ID (`618223`)** — P6 opened the box and found 104 different parts wearing one serial number. Its importer choked on the relationship table and the tables after it, which is exactly why your import broke and the project looked wrong.

**The fix in this file:** every added relationship now carries its own fresh ID (`640884` → `641337`, continuing from where your file stopped), and junk cached dates were cleared.

## 2. Proof this file is structurally clean (verified after rebuild, on the exact bytes you will import)

| Test | Result |
|---|---|
| All 15 non-relationship tables byte-identical to your original | **PASS** |
| Changed lines outside the relationship table | exactly **1** (project rename) |
| Relationship rows / unique primary keys | 22,718 / **22,718** ✅ |
| Dangling references (points to a missing activity) | **0** |
| Malformed rows (wrong number of columns anywhere) | **0** |
| Re-scheduled from the final bytes: loops / negative float | **0 / 0** |

## 3. What changed in the logic (same rules you approved, +1 more safe round)

- **R1 — Facade-steel zones overlap** (all 5 buildings): serial FS → SS+10d; zone-1 re-anchored to Ground-Floor slab SS+35d; fabrication trigger overlapped. *(site-confirm)*
- **R3 — CC facade boundary** overlap (SS+12d).
- **R4 — Testing & snagging streams** floor-to-floor SS (gap-bounded, delays nothing): 59 links.
- **R6 — Driving-chain surgery**: two clean rounds of 50% overlaps were accepted (+18 days, then +8 days). A third round was **automatically rejected** — it would have bought only 2 days while creating 5 negative-float activities. Detail: `Stage1_1_Link_Diff.json`.

## 4. The dates (my engine — expect P6 F9 a few days later)

| Milestone | 30-Sep file | **Stage 1.1** | Limit | Status |
|---|---|---|---|---|
| 4 Star Steel Completion | ~Mar 2028 | **6 Jan 2028** | 15 Mar 2028 | ✅ |
| 3 Star Steel Completion | ~Apr 2028 | **12 Jan 2028** | 15 Mar 2028 | ✅ |
| Retail 1 Steel Completion | ~May 2028 | **17 Dec 2027** | 15 Mar 2028 | ✅ |
| CC Steel Completion | ~Mar 2028 | **14 Jan 2028** | 15 Mar 2028 | ✅ |
| **Retail 2 Steel Completion** | **2 Jun 2028** | **~4 Apr 2028** | 15 Mar 2028 | ⚠️ ~20 days over |
| **Project Completion** | **7 Jun 2029** | **~9–14 May 2029** | **15 May 2029** | ✅ (tight) |

**On the delayed-project credibility point you raised:** intermediate dates land earlier than the old baseline *because the deadline is fixed and durations are frozen* — overlap is the only lever left. What makes it defensible at the client table is that every overlap is documented here and needs your site team's sign-off, not hidden.

**On your 30-day buffer, honestly:** after the two accepted rounds, honest logic bottoms out at ~9 May (engine). The rejected third round proves there's ~2 more days available, not 30. **A true 30-day pre-completion buffer is not reachable without either** (a) re-capturing durations on specific tasks (breaks your rule #7 — your call), or (b) site-driven scope/sequence decisions for the retail blocks. Say the word and I will prepare the exact duration-recapture shopping list with days-per-task. Retail-2's steel branch is the deepest issue — bound by the ~4-month-late handovers; flagged for the client narrative, per the plan.

## 5. Import instructions (Primavera P6, v17)

1. In P6, **delete the broken attempt** (`CSD-LKO-RB-S1`) if it exists.
2. File → Import → **XER** → choose `CSD-LKO-RB-Stage1_1.xer`.
3. **Import Action = "Create New"** (it will become project **CSD-LKO-RB-S11**). Leave global-data options at defaults.
4. After import, open the project and press **F9**.
5. Expected counts: 13,441 activities, 22,718 relationships, same WBS structure as your original.
6. If the wizard throws *any* error, stop and send me the exact message — do not hand-repair.

## 6. Open items (unchanged from before)
- What did "Revision of Baseline3" do? · +6/−3 status moves vs the 30-Sep file · 25 removed resource assignments
- RB2 Ground-to-4th pour mismatch (drawing 6 vs XER 5) · deliverable expectations ("something else")

*Durations, actual dates, activity IDs, WBS, calendars, resources: untouched. Verifiable in §2.*
