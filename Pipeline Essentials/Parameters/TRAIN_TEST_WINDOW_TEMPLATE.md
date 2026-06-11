# TRAIN/TEST WINDOW SELECTION — template for ALL long-bias (10-bagger) ML runs
*2026-06-04. Derived from the Technology Features run; apply to every long pipeline.*

## THE STRUCTURAL PROBLEM (true for every long-bias run)
The label is **forward-looking** (becomes a 10× over the next 5 years), so the winner/control mix is
**temporally skewed**, ALWAYS in the same direction:
- **Early pits → CONTROL-heavy** (a stock that capitulated in 2010 has had time to *fail* to 10×).
- **Late pits → WINNER-heavy** (a stock that capitulated in 2018 and is a 10× by 2024 is over-represented).
This is not a bug — it's intrinsic to forward-return labeling. Plan for it.

### TF evidence (per-year strict >=10x W vs C)
2010: 95C/38W · 2011: 28C/18W · 2012: 21C/23W · 2013: 29C/9W · 2014: 9C/9W · 2015: 6C/7W ·
2016: 9C/35W · 2017: 3C/10W · 2018: 5C/21W · 2019: 15C/50W.  Crossover (W≈C) ≈ 2012–2015.

## THE METHOD — MATCHED-PAIR SPLIT (gives BOTH windows exactly 1:1)
The clean solution: **split by matched PAIR, not by individual pit date.** Each winner has one matched control
(same `match_id`). Keep the pair together and assign it to train/test by the **winner's pit date**. Every window
is then **1 winner : 1 control by construction** — perfectly even, nothing dropped, no synthetic, still chronological.
1. Build strict-winner + matched-control labels with pit dates + `match_id` (`q0_labels`).
2. Sort the match_ids by their winner's pit date.
3. Split the sorted pairs (e.g. 50/50, 60/40, 70/30). Each side has equal winners and controls automatically.
4. Train on the earlier pairs, test on the later pairs. Both are 1:1.
- Minor caveat: a control's own pit can differ from its winner's, so a few controls sit by their winner's date —
  a small chronological compromise for perfect balance. For STRICT per-sample chronology, use the date-cut method
  below and accept imbalance instead.

## ALTERNATIVE — date-cut method (if you want strict per-sample chronology, accept imbalance)
1. Search train=[start,cut), test=[cut,end]; pick the train window naturally ~1:1 by DROPPING the earliest
   control-heavy year(s) and cutting before the winner-heavy tail.
2. Balance the train by removing surplus CONTROLS only (never winners, never synthetic).
3. The test tail stays winner-heavy — judge it with ROC-AUC (base-rate-invariant) and/or the continuous-return
   model. Never report PR-AUC/precision on a winner-heavy test (inflated by base rate).

## TF RESULT (the worked example)
**Matched-pair split (both windows exactly 1:1) — RECOMMENDED:**
- 50/50: TRAIN **110W/110C** (winner-pits 2010-01→2016-02) | TEST **110W/110C** (2016-02→2019-12).
- 60/40: TRAIN 132W/132C | TEST 88W/88C.   70/30: TRAIN 154W/154C | TEST 66W/66C.
- Nothing dropped, chronological by winner pit date.

Date-cut alternative (strict per-sample chronology, imbalanced test):
- TRAIN 2011-01→2017-01 = 101W/102C (0.99:1); TEST 2017-01→2020-01 = 81W/23C (score with ROC-AUC).

## REUSABLE SEARCH SNIPPET
```python
import pandas as pd, numpy as np
lab = pd.read_parquet(r'<WORK_DIR>\q0_labels.parquet'); lab['date']=pd.to_datetime(lab['date'])
sw = set(lab[(lab.role=='winner') & (lab.return_multiple>=WIN_THRESH)].match_id)
st = lab[((lab.role=='winner') & (lab.return_multiple>=WIN_THRESH)) |
         ((lab.role=='control') & (lab.match_id.isin(sw)))].copy()
def wc(s): return int((s.role=='winner').sum()), int((s.role=='control').sum())
for start in ['<y0>-01-01','<y0+1>-01-01']:
    for cut in ['<yc1>-01-01','<yc2>-01-01']:
        tr = st[(st.date>=start)&(st.date<cut)]; te = st[st.date>=cut]
        tw,tc = wc(tr); ew,ec = wc(te)
        print(start, cut, f'train {tw}/{tc} ({tw/max(1,tc):.2f}:1)  test {ew}/{ec} ({ew/max(1,ec):.2f}:1)')
# choose the (start,cut) whose TRAIN ratio is closest to 1:1 with the most samples.
```

## RULES OF THUMB (bake into every long run)
- **Drop the earliest 1–2 control-heavy years** from training — they're mostly unmatched controls and skew it.
- **Train window = the balanced middle**; **test window = the winner-heavy tail** (latest).
- **Balance by removing controls only** (never winners, never synthetic).
- **Test metric = ROC-AUC and/or continuous-return ranking** — never PR-AUC/precision on a winner-heavy test.
- Prefer the **continuous return_multiple target** (regression/ranking) — it has no class ratio to balance and
  uses every ticker's outcome (4–5× more information from the same names).
- Validate **chronologically** (train earlier pits, test later). Never random CV (leaks ~+0.14 ROC-AUC).
- Per pipeline the exact years differ — RE-RUN the search; don't hard-code TF's 2011/2017.
