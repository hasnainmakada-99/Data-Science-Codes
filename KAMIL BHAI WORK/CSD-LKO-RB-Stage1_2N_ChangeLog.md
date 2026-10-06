# Stage 1.2N v2 — Rebuilt (07-Oct-2026)

**File:** `CSD-LKO-RB-Stage1_2N.xer` · **Base:** Stage 1.1 · **Project code inside file:** `CSD-LKO-RB-S12N`

> **The first 1.2N upload was withdrawn and replaced.** Root cause found: a file-format defect — every added relationship row carried **one tab too many** (11 fields against a 10-field table header). My lenient parser hid it; P6's strict importer did not. The check that catches this is now permanently in the battery: every row in every table is verified field-for-field against its header before anything ships.

## What this build does — and cannot do — in plain words

- Added **40,982 new Finish-Start relationships**. **Every added lag is exactly zero** — the question "how does P6 convert lag hours" (different calendars carry different hours/day) is now eliminated by construction: 0 hours is 0 in every calendar.
- Every tie is placed **only where the file's own dates already give it at least 4 working days of natural slack** — checked twice, against the P6-cached dates stored inside the file AND an independent date-only CPM engine. Because of that: **the schedule can keep its dates or pull them earlier; nothing can be pushed later.** Verified in the validator: all 13,050 activity start dates are byte-identical to Stage 1.1; project finish unchanged; 0 negative float; 0 logic loops.
- **Honest ceiling:** zero-lag ropes with slack can only do so much. Float ≤ 44cd rose from 534 to **1,274 activities (~10%)**; the >250-day float tail collapsed from 3,445 to **1,258**. Most remaining floats sit at 50–120 days, held there by genuine scheduling windows between early work and physically-later floors — **no relationship edit can shrink those without re-dating the successor work** (which is the client's planner's decision, not something a links-only file should smuggle in).
- To go further toward the client's 40/44-day target, the right next step is a **two-way loop through your P6**: you F9 and export, I place the next tier of ties against those live dates, you verify again. P6 stays the final authority on every batch.

## Verification battery (run on the shipped bytes)

| Check | Result |
|---|---|
| Original relationships severed | **0** of 22,718 (row-by-row) |
| Original lags modified | **0** (byte-level) |
| Anything outside TASKPRED changed | Nothing (project code renamed CSD-LKO-RB-S12N only) |
| Row field counts vs table headers (all tables) | exact |
| New ties | 40,982, all PR_FS, all lag 0, unique pairs & PKs (641338–682319) |
| Dangling task references | 0 |
| Negative float / loops (CPM validator) | 0 / 0 |
| Every activity's start date vs Stage 1.1 | 13,050/13,050 identical |
| Project finish (validator view) | 2029-04-06, identical to baseline |

## Float distribution (validator, calendar days)

| Band | Stage 1.1 | Stage 1.2N v2 |
|---|---|---|
| ≤ 44d (target) | 534 | **1,274** |
| 44–60d | 168 | 488 |
| 60–120d | 1,242 | 3,604 |
| 120–250d | 7,661 | 6,426 |
| > 250d | 3,445 | **1,258** |

## Your checks in P6
1. Import as a **new project** (shows as CSD-LKO-RB-S12N).
2. F9 — finish must match Stage 1.1 exactly; dates may only sit on or before their 1.1 positions.
3. Confirm no negative float and spot-check the float columns against the table above.
