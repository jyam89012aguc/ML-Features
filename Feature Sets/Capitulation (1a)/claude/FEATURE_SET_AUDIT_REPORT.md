# Feature Set Audit Report

Date: 2026-05-25

Scope: feature-family directories in this working directory. The audit used the
local harnesses as the primary checks and the external audit notes in
`C:\Users\jyama\Desktop\active_non audited features per AI\Audit Scripts` as
the defect taxonomy guide. Family count and feature-slot count differences are
not treated as defects.

## Harnesses Run

- `python _audit.py 1 102`
- `python _gapcheck.py`
- `python _verify.py > _vchk_current_audit.txt`
- `python _quality_review_51_75.py > _quality_review_51_75_current_audit.txt`
- `python _verify_96_100.py`

## Inventory

- Numeric feature directories: 110
- Non-empty feature directories: 104
- Empty placeholder directories: 6
- Python files, excluding `__pycache__`: 576
- Full smoke harness registered features: 35,175
- Full smoke harness features run successfully: 35,160
- Full smoke harness failures: 15
- Full smoke harness all-NaN outputs: 137
- Full smoke harness constant outputs: 915

## High-Priority Defects

1. `20_up_down_volume/20_up_down_volume_2nd_derivatives.py`
   - Import fails because registry entries `udv_drv2_026` through
     `udv_drv2_075` reference functions that are not defined.
   - This accounts for 50 undefined registry references structurally, and it
     prevents the file from importing in the full smoke harness.

2. `20_up_down_volume/20_up_down_volume_base_001_075.py`
   - `udv_163_vol_on_consecutive_down_days_3d_21d` errors at runtime:
     `unsupported operand type(s) for &: 'float' and 'bool'`.
   - Root cause: the `down` Series is cast to float before boolean `&`.

3. `22_volume_price_divergence/22_volume_price_divergence_2nd_derivatives.py`
   - 8 runtime errors due to undefined helper `_log_ret`.
   - Affected features: `vpd_drv2_057`, `058`, `065`, `066`, `067`, `068`,
     `071`, `072`.

4. `23_dollar_volume_shock/23_dollar_volume_shock_2nd_derivatives.py`
   - 4 runtime errors due to undefined helper `_rolling_max`.
   - Affected features: `dvs_drv2_040`, `041`, `064`, `074`.

5. `24_volume_distribution/24_volume_distribution_2nd_derivatives.py`
   - 2 runtime errors due to undefined helper `_rolling_max`.
   - Affected features: `vds_drv2_069`, `070`.

## Empty Placeholder Directories

These directories exist but contain no `.py` files:

- `105_fractal_structure`
- `106_support_violation`
- `107_change_point_detection`
- `109_return_autocorrelation`
- `110_tail_risk_evt`
- `111_jump_discontinuity`

This is only a defect if those directories are intended to be active feature
sets in this batch.

## Input Discipline And Look-Ahead

- No `DISALLOWED INPUT` findings from `_verify.py`.
- No feature-code forward-looking patterns were reported by `_verify.py`.
- A raw repository grep found one negative shift in `_verify_96_100.py`, but
  that is test-harness synthetic-data construction, not feature code.
- No `!>75KB` file-size findings were reported by `_verify.py`.

## Concept Coverage Findings

The keyword coverage scan found most folders 01-50 covered their canonical
concepts. Possible content gaps:

- `26_rsi_extremes`: missing `RSI of RSI`
- `35_capitulation_thrust`: missing `wide-range bar`
- `40_close_location`: missing `close position in range`
- `44_atr_normalized_move`: missing `move in ATR units`

These are keyword-based findings and should be confirmed against the actual
function semantics before editing.

## Redundancy / Dead-Feature Review For 51-75

The deeper 51-75 quality review found:

- Features analyzed: 7,025
- All-NaN: 26
- Constant: 225
- Near-constant: 551
- Mostly-NaN: 6
- Within-folder pairs with `|corr| >= 0.95`: 8,839
- Within-folder pairs with `|corr| >= 0.999`: 1,305
- Base-to-derivative collision features: 62

Worst exact/near-exact duplicate families in the 51-75 review:

- `56_zero_volume_days`: 264 pairs
- `51_shadow_wick_analysis`: 108 pairs
- `55_price_level_distress`: 94 pairs
- `63_cash_burn`: 73 pairs
- `69_equity_erosion`: 63 pairs
- `61_revenue_deterioration`: 56 pairs

The 51-75 review also reports broad adjacent-family correlation overlap,
especially among liquidity/price-level/fundamental-distress families. Treat
these as audit leads, not automatic delete instructions; several may be
synthetic-data artifacts or intentional concept proximity.

## Informational Only

Many folders intentionally use larger slot counts than the older guide schema:
for example base files with 100 entries and derivative files with 75 entries.
Per the user instruction, those count differences were not treated as defects.

