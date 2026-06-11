"""
92_ownership_concentration — 2nd-Derivative Features (ocn_drv2_001 to ocn_drv2_075)
=====================================================================================
Domain: Rate-of-change (first derivative) of selected base concentration features.
These are the 2nd derivatives of the raw SF3 signals (raw -> base -> drv2).

Quarterly -> Daily Alignment Contract
--------------------------------------
All inputs are daily Series forward-filled from quarterly Sharadar SF3 13-F data.
Because underlying data is quarterly, derivative series are sparse/stepwise on a
daily index — this is expected behaviour and does not indicate a bug.
QoQ diff is implemented via .shift(63); slope via OLS over rolling windows.

Input fields (same as base files):
    hhi          — Herfindahl-Hirschman index of institutional holdings (0..1)
    top1_shares  — shares held by the single largest institutional holder
    top5_shares  — shares held by top-5 institutional holders combined
    top10_shares — shares held by top-10 institutional holders combined
    inst_shares  — aggregate shares held by ALL institutions
    inst_holders — count of institutional holders
    inst_value   — aggregate USD value held by all institutions
    avg_position — mean shares per institutional holder

Trading-day constants:
    1 quarter  = 63 td   (_TD_QTR)
    2 quarters = 126 td  (_TD_2Q)
    1 year     = 252 td  (_TD_YEAR)
    2 years    = 504 td  (_TD_2Y)
    3 years    = 756 td  (_TD_3Y)

NOTE: No cross-file imports. All base-feature logic is recomputed inline.
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
_TD_QTR  = 63
_TD_2Q   = 126
_EPS     = 1e-9

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _align_quarterly_to_daily(s: pd.Series) -> pd.Series:
    """Return s as-is (already forward-filled to daily by the pipeline)."""
    return s


def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    b_safe = b.replace(0, np.nan)
    return a / b_safe


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=2).std()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=1).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _ols_slope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over window w."""
    def _slope(arr):
        if len(arr) < 4:
            return np.nan
        xw = np.arange(len(arr), dtype=float)
        xw -= xw.mean()
        yw = arr - arr.mean()
        denom = (xw * xw).sum()
        return (xw * yw).sum() / denom if denom > _EPS else np.nan
    return s.rolling(w, min_periods=4).apply(_slope, raw=True)


# ---------------------------------------------------------------------------
# Inline base-feature recompute helpers (no cross-imports)
# ---------------------------------------------------------------------------

def _base_hhi(hhi: pd.Series) -> pd.Series:
    return _align_quarterly_to_daily(hhi)


def _base_eff_n(hhi: pd.Series) -> pd.Series:
    h = _align_quarterly_to_daily(hhi)
    return _safe_div(pd.Series(np.ones(len(h)), index=h.index), h)


def _base_top1_ratio(top1_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(inst_shares))


def _base_top5_ratio(top5_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top5_shares),
                     _align_quarterly_to_daily(inst_shares))


def _base_top10_ratio(top10_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top10_shares),
                     _align_quarterly_to_daily(inst_shares))


def _base_outside_top10(top10_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((ins - t10).clip(lower=0), ins)


def _base_gini_proxy(top1_shares, top5_shares, top10_shares, inst_shares) -> pd.Series:
    ins = _align_quarterly_to_daily(inst_shares)
    s1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    s5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    s10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    return 0.5 * (0.1 * s1 + (0.5 - 0.1) * (s1 + s5) + (1.0 - 0.5) * (s5 + s10))


def _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares) -> pd.Series:
    ins = _align_quarterly_to_daily(inst_shares)
    h   = _align_quarterly_to_daily(hhi)
    r1  = _safe_div(_align_quarterly_to_daily(top1_shares),  ins)
    r5  = _safe_div(_align_quarterly_to_daily(top5_shares),  ins)
    r10 = _safe_div(_align_quarterly_to_daily(top10_shares), ins)
    return (h + r1 + r5 + r10) / 4.0


def _base_tail_ratio(top5_shares, top10_shares, inst_shares) -> pd.Series:
    t5  = _align_quarterly_to_daily(top5_shares)
    t10 = _align_quarterly_to_daily(top10_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((t10 - t5).clip(lower=0), ins)


def _base_avg_pos(avg_position: pd.Series) -> pd.Series:
    return _align_quarterly_to_daily(avg_position)


# ===========================================================================
# 2nd-Derivative Features (drv2_001 to drv2_025)
# ===========================================================================

def ocn_drv2_001_hhi_qoq_roc(hhi: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the HHI QoQ change (acceleration)."""
    base = _base_hhi(hhi)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_002_hhi_yoy_roc(hhi: pd.Series) -> pd.Series:
    """YoY rate-of-change of the HHI YoY change."""
    base = _base_hhi(hhi)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_003_hhi_slope_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of HHI."""
    slope = _ols_slope(_base_hhi(hhi), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_004_eff_n_qoq_roc(hhi: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the effective-N QoQ change."""
    base = _base_eff_n(hhi)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_005_eff_n_yoy_roc(hhi: pd.Series) -> pd.Series:
    """YoY rate-of-change of the effective-N YoY change."""
    base = _base_eff_n(hhi)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_006_eff_n_slope_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of effective-N."""
    slope = _ols_slope(_base_eff_n(hhi), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_007_top1_ratio_qoq_roc(top1_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the top-1 ratio QoQ change."""
    base = _base_top1_ratio(top1_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_008_top1_ratio_yoy_roc(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the top-1 ratio YoY change."""
    base = _base_top1_ratio(top1_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_009_top1_ratio_slope_roc(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of top-1 concentration ratio."""
    slope = _ols_slope(_base_top1_ratio(top1_shares, inst_shares), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_010_top5_ratio_qoq_roc(top5_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the top-5 ratio QoQ change."""
    base = _base_top5_ratio(top5_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_011_top5_ratio_yoy_roc(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the top-5 ratio YoY change."""
    base = _base_top5_ratio(top5_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_012_top5_ratio_slope_roc(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of top-5 concentration ratio."""
    slope = _ols_slope(_base_top5_ratio(top5_shares, inst_shares), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_013_top10_ratio_qoq_roc(top10_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the top-10 ratio QoQ change."""
    base = _base_top10_ratio(top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_014_top10_ratio_yoy_roc(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the top-10 ratio YoY change."""
    base = _base_top10_ratio(top10_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_015_top10_ratio_slope_roc(top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of top-10 concentration ratio."""
    slope = _ols_slope(_base_top10_ratio(top10_shares, inst_shares), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_016_gini_proxy_qoq_roc(top1_shares: pd.Series,
                                      top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the Gini-proxy QoQ change."""
    base = _base_gini_proxy(top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_017_gini_proxy_yoy_roc(top1_shares: pd.Series,
                                     top5_shares: pd.Series,
                                     top10_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the Gini-proxy YoY change."""
    base = _base_gini_proxy(top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_018_composite_qoq_roc(hhi: pd.Series,
                                    top1_shares: pd.Series,
                                    top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the composite concentration QoQ change."""
    base = _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_019_composite_yoy_roc(hhi: pd.Series,
                                    top1_shares: pd.Series,
                                    top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the composite concentration YoY change."""
    base = _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_020_composite_slope_roc(hhi: pd.Series,
                                      top1_shares: pd.Series,
                                      top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of the composite concentration."""
    slope = _ols_slope(
        _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares),
        _TD_YEAR
    )
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_021_outside_top10_qoq_roc(top10_shares: pd.Series,
                                         inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the outside-top-10 share QoQ change."""
    base = _base_outside_top10(top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_022_outside_top10_yoy_roc(top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the outside-top-10 share YoY change."""
    base = _base_outside_top10(top10_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_023_tail_ratio_qoq_roc(top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the 6-10 tranche ratio QoQ change."""
    base = _base_tail_ratio(top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_024_avg_pos_qoq_roc(avg_position: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the average position QoQ change."""
    base = _base_avg_pos(avg_position)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_025_hhi_ewm_roc(hhi: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the EWM-smoothed HHI (deviation from trend accel)."""
    base = _ewm_mean(_base_hhi(hhi), _TD_YEAR)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


# --- New 2nd-Derivative Features 026-075 ------------------------------------

# Additional base helpers used only in new features
def _base_vph(inst_value: pd.Series, inst_holders: pd.Series) -> pd.Series:
    v = _align_quarterly_to_daily(inst_value)
    n = _align_quarterly_to_daily(inst_holders)
    return _safe_div(v, n)


def _base_avg_pos_ratio(top1_shares: pd.Series, avg_position: pd.Series) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(avg_position))


def _base_outside_top5(top5_shares: pd.Series, inst_shares: pd.Series) -> pd.Series:
    t5  = _align_quarterly_to_daily(top5_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((ins - t5).clip(lower=0), ins)


def ocn_drv2_026_hhi_2q_roc(hhi: pd.Series) -> pd.Series:
    """2Q rate-of-change of the HHI 2Q change (2-step acceleration)."""
    base = _base_hhi(hhi)
    d1 = base - base.shift(2 * _TD_QTR)
    return d1 - d1.shift(2 * _TD_QTR)


def ocn_drv2_027_hhi_slope_8q_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in the 8Q OLS slope of HHI."""
    slope = _ols_slope(_base_hhi(hhi), _TD_2Y)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_028_hhi_ewm_slope_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in the OLS slope of the EWM-smoothed HHI."""
    smoothed = _ewm_mean(_base_hhi(hhi), _TD_YEAR)
    slope = _ols_slope(smoothed, _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_029_eff_n_2q_roc(hhi: pd.Series) -> pd.Series:
    """2Q rate-of-change of the effective-N 2Q change."""
    base = _base_eff_n(hhi)
    d1 = base - base.shift(2 * _TD_QTR)
    return d1 - d1.shift(2 * _TD_QTR)


def ocn_drv2_030_eff_n_slope_8q_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in the 8Q OLS slope of effective-N."""
    slope = _ols_slope(_base_eff_n(hhi), _TD_2Y)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_031_top1_ratio_2q_roc(top1_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """2Q rate-of-change of the top-1 ratio 2Q change."""
    base = _base_top1_ratio(top1_shares, inst_shares)
    d1 = base - base.shift(2 * _TD_QTR)
    return d1 - d1.shift(2 * _TD_QTR)


def ocn_drv2_032_top1_ratio_yoy_zscore_roc(top1_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 1y z-score of top-1 ratio."""
    zs = _zscore_rolling(_base_top1_ratio(top1_shares, inst_shares), _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def ocn_drv2_033_top5_ratio_2q_roc(top5_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """2Q rate-of-change of the top-5 ratio 2Q change."""
    base = _base_top5_ratio(top5_shares, inst_shares)
    d1 = base - base.shift(2 * _TD_QTR)
    return d1 - d1.shift(2 * _TD_QTR)


def ocn_drv2_034_top5_ratio_yoy_zscore_roc(top5_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 1y z-score of top-5 ratio."""
    zs = _zscore_rolling(_base_top5_ratio(top5_shares, inst_shares), _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def ocn_drv2_035_top10_ratio_2q_roc(top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """2Q rate-of-change of the top-10 ratio 2Q change."""
    base = _base_top10_ratio(top10_shares, inst_shares)
    d1 = base - base.shift(2 * _TD_QTR)
    return d1 - d1.shift(2 * _TD_QTR)


def ocn_drv2_036_top10_ratio_slope_8q_roc(top10_shares: pd.Series,
                                            inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 8Q OLS slope of top-10 concentration ratio."""
    slope = _ols_slope(_base_top10_ratio(top10_shares, inst_shares), _TD_2Y)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_037_gini_proxy_slope_roc(top1_shares: pd.Series,
                                        top5_shares: pd.Series,
                                        top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of the Gini-proxy."""
    slope = _ols_slope(
        _base_gini_proxy(top1_shares, top5_shares, top10_shares, inst_shares),
        _TD_YEAR
    )
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_038_gini_proxy_2q_roc(top1_shares: pd.Series,
                                     top5_shares: pd.Series,
                                     top10_shares: pd.Series,
                                     inst_shares: pd.Series) -> pd.Series:
    """2Q rate-of-change of the Gini-proxy 2Q change."""
    base = _base_gini_proxy(top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(2 * _TD_QTR)
    return d1 - d1.shift(2 * _TD_QTR)


def ocn_drv2_039_outside_top10_slope_roc(top10_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of the outside-top-10 share."""
    slope = _ols_slope(_base_outside_top10(top10_shares, inst_shares), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_040_tail_ratio_yoy_roc(top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the 6-10 tranche ratio YoY change."""
    base = _base_tail_ratio(top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_041_avg_pos_yoy_roc(avg_position: pd.Series) -> pd.Series:
    """YoY rate-of-change of the average position YoY change."""
    base = _base_avg_pos(avg_position)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_042_avg_pos_slope_roc(avg_position: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of average institutional position."""
    slope = _ols_slope(_base_avg_pos(avg_position), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_043_vph_qoq_roc(inst_value: pd.Series,
                               inst_holders: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the value-per-holder QoQ change."""
    base = _base_vph(inst_value, inst_holders)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_044_vph_yoy_roc(inst_value: pd.Series,
                               inst_holders: pd.Series) -> pd.Series:
    """YoY rate-of-change of the value-per-holder YoY change."""
    base = _base_vph(inst_value, inst_holders)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_045_vph_slope_roc(inst_value: pd.Series,
                                 inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of value per holder."""
    slope = _ols_slope(_base_vph(inst_value, inst_holders), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_046_outside_top5_qoq_roc(top5_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """QoQ rate-of-change of the outside-top-5 fraction QoQ change."""
    base = _base_outside_top5(top5_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ocn_drv2_047_outside_top5_yoy_roc(top5_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """YoY rate-of-change of the outside-top-5 fraction YoY change."""
    base = _base_outside_top5(top5_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def ocn_drv2_048_hhi_qoq_zscore_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in the 1y z-score of HHI."""
    zs = _zscore_rolling(_base_hhi(hhi), _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def ocn_drv2_049_composite_2q_roc(hhi: pd.Series,
                                    top1_shares: pd.Series,
                                    top5_shares: pd.Series,
                                    top10_shares: pd.Series,
                                    inst_shares: pd.Series) -> pd.Series:
    """2Q rate-of-change of the composite concentration 2Q change."""
    base = _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(2 * _TD_QTR)
    return d1 - d1.shift(2 * _TD_QTR)


def ocn_drv2_050_composite_slope_8q_roc(hhi: pd.Series,
                                          top1_shares: pd.Series,
                                          top5_shares: pd.Series,
                                          top10_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 8Q OLS slope of composite concentration."""
    slope = _ols_slope(
        _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares),
        _TD_2Y
    )
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_051_hhi_yoy_ewm_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in EWM(252) of the HHI YoY change."""
    d1 = _base_hhi(hhi)
    d1 = d1 - d1.shift(_TD_YEAR)
    smoothed = _ewm_mean(d1, _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def ocn_drv2_052_top1_ratio_ewm_roc(top1_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change in EWM(252) of top-1 ratio."""
    smoothed = _ewm_mean(_base_top1_ratio(top1_shares, inst_shares), _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def ocn_drv2_053_top5_ratio_ewm_roc(top5_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change in EWM(252) of top-5 ratio."""
    smoothed = _ewm_mean(_base_top5_ratio(top5_shares, inst_shares), _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def ocn_drv2_054_top10_ratio_ewm_roc(top10_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change in EWM(252) of top-10 ratio."""
    smoothed = _ewm_mean(_base_top10_ratio(top10_shares, inst_shares), _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def ocn_drv2_055_eff_n_ewm_roc(hhi: pd.Series) -> pd.Series:
    """QoQ change in EWM(252) of effective-N."""
    smoothed = _ewm_mean(_base_eff_n(hhi), _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def ocn_drv2_056_hhi_slope_roc_zscore_1y(hhi: pd.Series) -> pd.Series:
    """1y rolling z-score of the QoQ change in 4Q HHI OLS slope."""
    slope_roc = _ols_slope(_base_hhi(hhi), _TD_YEAR)
    d1 = slope_roc - slope_roc.shift(_TD_QTR)
    return _zscore_rolling(d1, _TD_YEAR)


def ocn_drv2_057_top1_ratio_qoq_roc_zscore_1y(top1_shares: pd.Series,
                                                 inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the QoQ change in top-1 QoQ ROC."""
    base = _base_top1_ratio(top1_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_058_top5_ratio_qoq_roc_zscore_1y(top5_shares: pd.Series,
                                                 inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the QoQ change in top-5 QoQ ROC."""
    base = _base_top5_ratio(top5_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_059_gini_proxy_qoq_roc_zscore_1y(top1_shares: pd.Series,
                                                 top5_shares: pd.Series,
                                                 top10_shares: pd.Series,
                                                 inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the Gini-proxy QoQ ROC."""
    base = _base_gini_proxy(top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_060_composite_qoq_roc_zscore_1y(hhi: pd.Series,
                                               top1_shares: pd.Series,
                                               top5_shares: pd.Series,
                                               top10_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the composite concentration QoQ ROC."""
    base = _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_061_hhi_qoq_roc_ewm(hhi: pd.Series) -> pd.Series:
    """EWM(252) applied to the HHI QoQ acceleration series."""
    base = _base_hhi(hhi)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv2_062_top1_ratio_qoq_roc_ewm(top1_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the top-1 ratio QoQ acceleration."""
    base = _base_top1_ratio(top1_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv2_063_top5_ratio_qoq_roc_ewm(top5_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the top-5 ratio QoQ acceleration."""
    base = _base_top5_ratio(top5_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv2_064_top10_ratio_qoq_roc_ewm(top10_shares: pd.Series,
                                            inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the top-10 ratio QoQ acceleration."""
    base = _base_top10_ratio(top10_shares, inst_shares)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv2_065_eff_n_qoq_roc_ewm(hhi: pd.Series) -> pd.Series:
    """EWM(252) of the effective-N QoQ acceleration."""
    base = _base_eff_n(hhi)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv2_066_outside_top10_slope_8q_roc(top10_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 8Q OLS slope of the outside-top-10 fraction."""
    slope = _ols_slope(_base_outside_top10(top10_shares, inst_shares), _TD_2Y)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_067_tail_ratio_slope_roc(top5_shares: pd.Series,
                                        top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4Q OLS slope of the 6-10 tranche ratio."""
    slope = _ols_slope(_base_tail_ratio(top5_shares, top10_shares, inst_shares), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def ocn_drv2_068_hhi_qoq_roc_slope_8q(hhi: pd.Series) -> pd.Series:
    """8Q OLS slope of the HHI QoQ acceleration series."""
    base = _base_hhi(hhi)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ols_slope(d2, _TD_2Y)


def ocn_drv2_069_composite_yoy_roc_zscore_1y(hhi: pd.Series,
                                               top1_shares: pd.Series,
                                               top5_shares: pd.Series,
                                               top10_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the composite YoY ROC series."""
    base = _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_YEAR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_070_avg_pos_qoq_roc_ewm(avg_position: pd.Series) -> pd.Series:
    """EWM(252) of the average position QoQ acceleration."""
    base = _base_avg_pos(avg_position)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv2_071_hhi_yoy_roc_zscore_1y(hhi: pd.Series) -> pd.Series:
    """1y rolling z-score of the HHI YoY ROC series."""
    base = _base_hhi(hhi)
    d1 = base - base.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_YEAR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_072_eff_n_yoy_roc_zscore_1y(hhi: pd.Series) -> pd.Series:
    """1y rolling z-score of the effective-N YoY ROC series."""
    base = _base_eff_n(hhi)
    d1 = base - base.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_YEAR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_073_top1_ratio_yoy_roc_zscore_1y(top1_shares: pd.Series,
                                                 inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the top-1 ratio YoY ROC series."""
    base = _base_top1_ratio(top1_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_YEAR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_074_top5_ratio_yoy_roc_zscore_1y(top5_shares: pd.Series,
                                                 inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the top-5 ratio YoY ROC series."""
    base = _base_top5_ratio(top5_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_YEAR)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv2_075_top10_ratio_yoy_roc_zscore_1y(top10_shares: pd.Series,
                                                  inst_shares: pd.Series) -> pd.Series:
    """1y rolling z-score of the top-10 ratio YoY ROC series."""
    base = _base_top10_ratio(top10_shares, inst_shares)
    d1 = base - base.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_YEAR)
    return _zscore_rolling(d2, _TD_YEAR)


# ===========================================================================
# Registry
# ===========================================================================
OWNERSHIP_CONCENTRATION_REGISTRY_2ND_DERIVATIVES = {
    "ocn_drv2_001_hhi_qoq_roc":          {"inputs": ["hhi"],                                                             "func": ocn_drv2_001_hhi_qoq_roc},
    "ocn_drv2_002_hhi_yoy_roc":          {"inputs": ["hhi"],                                                             "func": ocn_drv2_002_hhi_yoy_roc},
    "ocn_drv2_003_hhi_slope_roc":        {"inputs": ["hhi"],                                                             "func": ocn_drv2_003_hhi_slope_roc},
    "ocn_drv2_004_eff_n_qoq_roc":        {"inputs": ["hhi"],                                                             "func": ocn_drv2_004_eff_n_qoq_roc},
    "ocn_drv2_005_eff_n_yoy_roc":        {"inputs": ["hhi"],                                                             "func": ocn_drv2_005_eff_n_yoy_roc},
    "ocn_drv2_006_eff_n_slope_roc":      {"inputs": ["hhi"],                                                             "func": ocn_drv2_006_eff_n_slope_roc},
    "ocn_drv2_007_top1_ratio_qoq_roc":   {"inputs": ["top1_shares", "inst_shares"],                                      "func": ocn_drv2_007_top1_ratio_qoq_roc},
    "ocn_drv2_008_top1_ratio_yoy_roc":   {"inputs": ["top1_shares", "inst_shares"],                                      "func": ocn_drv2_008_top1_ratio_yoy_roc},
    "ocn_drv2_009_top1_ratio_slope_roc": {"inputs": ["top1_shares", "inst_shares"],                                      "func": ocn_drv2_009_top1_ratio_slope_roc},
    "ocn_drv2_010_top5_ratio_qoq_roc":   {"inputs": ["top5_shares", "inst_shares"],                                      "func": ocn_drv2_010_top5_ratio_qoq_roc},
    "ocn_drv2_011_top5_ratio_yoy_roc":   {"inputs": ["top5_shares", "inst_shares"],                                      "func": ocn_drv2_011_top5_ratio_yoy_roc},
    "ocn_drv2_012_top5_ratio_slope_roc": {"inputs": ["top5_shares", "inst_shares"],                                      "func": ocn_drv2_012_top5_ratio_slope_roc},
    "ocn_drv2_013_top10_ratio_qoq_roc":  {"inputs": ["top10_shares", "inst_shares"],                                     "func": ocn_drv2_013_top10_ratio_qoq_roc},
    "ocn_drv2_014_top10_ratio_yoy_roc":  {"inputs": ["top10_shares", "inst_shares"],                                     "func": ocn_drv2_014_top10_ratio_yoy_roc},
    "ocn_drv2_015_top10_ratio_slope_roc":{"inputs": ["top10_shares", "inst_shares"],                                     "func": ocn_drv2_015_top10_ratio_slope_roc},
    "ocn_drv2_016_gini_proxy_qoq_roc":   {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],       "func": ocn_drv2_016_gini_proxy_qoq_roc},
    "ocn_drv2_017_gini_proxy_yoy_roc":   {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],       "func": ocn_drv2_017_gini_proxy_yoy_roc},
    "ocn_drv2_018_composite_qoq_roc":    {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],"func": ocn_drv2_018_composite_qoq_roc},
    "ocn_drv2_019_composite_yoy_roc":    {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],"func": ocn_drv2_019_composite_yoy_roc},
    "ocn_drv2_020_composite_slope_roc":  {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],"func": ocn_drv2_020_composite_slope_roc},
    "ocn_drv2_021_outside_top10_qoq_roc":{"inputs": ["top10_shares", "inst_shares"],                                     "func": ocn_drv2_021_outside_top10_qoq_roc},
    "ocn_drv2_022_outside_top10_yoy_roc":{"inputs": ["top10_shares", "inst_shares"],                                     "func": ocn_drv2_022_outside_top10_yoy_roc},
    "ocn_drv2_023_tail_ratio_qoq_roc":   {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                      "func": ocn_drv2_023_tail_ratio_qoq_roc},
    "ocn_drv2_024_avg_pos_qoq_roc":      {"inputs": ["avg_position"],                                                    "func": ocn_drv2_024_avg_pos_qoq_roc},
    "ocn_drv2_025_hhi_ewm_roc":                     {"inputs": ["hhi"],                                                                          "func": ocn_drv2_025_hhi_ewm_roc},
    "ocn_drv2_026_hhi_2q_roc":                      {"inputs": ["hhi"],                                                                          "func": ocn_drv2_026_hhi_2q_roc},
    "ocn_drv2_027_hhi_slope_8q_roc":                {"inputs": ["hhi"],                                                                          "func": ocn_drv2_027_hhi_slope_8q_roc},
    "ocn_drv2_028_hhi_ewm_slope_roc":               {"inputs": ["hhi"],                                                                          "func": ocn_drv2_028_hhi_ewm_slope_roc},
    "ocn_drv2_029_eff_n_2q_roc":                    {"inputs": ["hhi"],                                                                          "func": ocn_drv2_029_eff_n_2q_roc},
    "ocn_drv2_030_eff_n_slope_8q_roc":              {"inputs": ["hhi"],                                                                          "func": ocn_drv2_030_eff_n_slope_8q_roc},
    "ocn_drv2_031_top1_ratio_2q_roc":               {"inputs": ["top1_shares", "inst_shares"],                                                   "func": ocn_drv2_031_top1_ratio_2q_roc},
    "ocn_drv2_032_top1_ratio_yoy_zscore_roc":       {"inputs": ["top1_shares", "inst_shares"],                                                   "func": ocn_drv2_032_top1_ratio_yoy_zscore_roc},
    "ocn_drv2_033_top5_ratio_2q_roc":               {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_033_top5_ratio_2q_roc},
    "ocn_drv2_034_top5_ratio_yoy_zscore_roc":       {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_034_top5_ratio_yoy_zscore_roc},
    "ocn_drv2_035_top10_ratio_2q_roc":              {"inputs": ["top10_shares", "inst_shares"],                                                  "func": ocn_drv2_035_top10_ratio_2q_roc},
    "ocn_drv2_036_top10_ratio_slope_8q_roc":        {"inputs": ["top10_shares", "inst_shares"],                                                  "func": ocn_drv2_036_top10_ratio_slope_8q_roc},
    "ocn_drv2_037_gini_proxy_slope_roc":            {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                    "func": ocn_drv2_037_gini_proxy_slope_roc},
    "ocn_drv2_038_gini_proxy_2q_roc":               {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                    "func": ocn_drv2_038_gini_proxy_2q_roc},
    "ocn_drv2_039_outside_top10_slope_roc":         {"inputs": ["top10_shares", "inst_shares"],                                                  "func": ocn_drv2_039_outside_top10_slope_roc},
    "ocn_drv2_040_tail_ratio_yoy_roc":              {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                   "func": ocn_drv2_040_tail_ratio_yoy_roc},
    "ocn_drv2_041_avg_pos_yoy_roc":                 {"inputs": ["avg_position"],                                                                 "func": ocn_drv2_041_avg_pos_yoy_roc},
    "ocn_drv2_042_avg_pos_slope_roc":               {"inputs": ["avg_position"],                                                                 "func": ocn_drv2_042_avg_pos_slope_roc},
    "ocn_drv2_043_vph_qoq_roc":                     {"inputs": ["inst_value", "inst_holders"],                                                   "func": ocn_drv2_043_vph_qoq_roc},
    "ocn_drv2_044_vph_yoy_roc":                     {"inputs": ["inst_value", "inst_holders"],                                                   "func": ocn_drv2_044_vph_yoy_roc},
    "ocn_drv2_045_vph_slope_roc":                   {"inputs": ["inst_value", "inst_holders"],                                                   "func": ocn_drv2_045_vph_slope_roc},
    "ocn_drv2_046_outside_top5_qoq_roc":            {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_046_outside_top5_qoq_roc},
    "ocn_drv2_047_outside_top5_yoy_roc":            {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_047_outside_top5_yoy_roc},
    "ocn_drv2_048_hhi_qoq_zscore_roc":              {"inputs": ["hhi"],                                                                          "func": ocn_drv2_048_hhi_qoq_zscore_roc},
    "ocn_drv2_049_composite_2q_roc":                {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],             "func": ocn_drv2_049_composite_2q_roc},
    "ocn_drv2_050_composite_slope_8q_roc":          {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],             "func": ocn_drv2_050_composite_slope_8q_roc},
    "ocn_drv2_051_hhi_yoy_ewm_roc":                 {"inputs": ["hhi"],                                                                          "func": ocn_drv2_051_hhi_yoy_ewm_roc},
    "ocn_drv2_052_top1_ratio_ewm_roc":              {"inputs": ["top1_shares", "inst_shares"],                                                   "func": ocn_drv2_052_top1_ratio_ewm_roc},
    "ocn_drv2_053_top5_ratio_ewm_roc":              {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_053_top5_ratio_ewm_roc},
    "ocn_drv2_054_top10_ratio_ewm_roc":             {"inputs": ["top10_shares", "inst_shares"],                                                  "func": ocn_drv2_054_top10_ratio_ewm_roc},
    "ocn_drv2_055_eff_n_ewm_roc":                   {"inputs": ["hhi"],                                                                          "func": ocn_drv2_055_eff_n_ewm_roc},
    "ocn_drv2_056_hhi_slope_roc_zscore_1y":         {"inputs": ["hhi"],                                                                          "func": ocn_drv2_056_hhi_slope_roc_zscore_1y},
    "ocn_drv2_057_top1_ratio_qoq_roc_zscore_1y":    {"inputs": ["top1_shares", "inst_shares"],                                                   "func": ocn_drv2_057_top1_ratio_qoq_roc_zscore_1y},
    "ocn_drv2_058_top5_ratio_qoq_roc_zscore_1y":    {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_058_top5_ratio_qoq_roc_zscore_1y},
    "ocn_drv2_059_gini_proxy_qoq_roc_zscore_1y":    {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                    "func": ocn_drv2_059_gini_proxy_qoq_roc_zscore_1y},
    "ocn_drv2_060_composite_qoq_roc_zscore_1y":     {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],             "func": ocn_drv2_060_composite_qoq_roc_zscore_1y},
    "ocn_drv2_061_hhi_qoq_roc_ewm":                 {"inputs": ["hhi"],                                                                          "func": ocn_drv2_061_hhi_qoq_roc_ewm},
    "ocn_drv2_062_top1_ratio_qoq_roc_ewm":          {"inputs": ["top1_shares", "inst_shares"],                                                   "func": ocn_drv2_062_top1_ratio_qoq_roc_ewm},
    "ocn_drv2_063_top5_ratio_qoq_roc_ewm":          {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_063_top5_ratio_qoq_roc_ewm},
    "ocn_drv2_064_top10_ratio_qoq_roc_ewm":         {"inputs": ["top10_shares", "inst_shares"],                                                  "func": ocn_drv2_064_top10_ratio_qoq_roc_ewm},
    "ocn_drv2_065_eff_n_qoq_roc_ewm":               {"inputs": ["hhi"],                                                                          "func": ocn_drv2_065_eff_n_qoq_roc_ewm},
    "ocn_drv2_066_outside_top10_slope_8q_roc":      {"inputs": ["top10_shares", "inst_shares"],                                                  "func": ocn_drv2_066_outside_top10_slope_8q_roc},
    "ocn_drv2_067_tail_ratio_slope_roc":             {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                   "func": ocn_drv2_067_tail_ratio_slope_roc},
    "ocn_drv2_068_hhi_qoq_roc_slope_8q":            {"inputs": ["hhi"],                                                                          "func": ocn_drv2_068_hhi_qoq_roc_slope_8q},
    "ocn_drv2_069_composite_yoy_roc_zscore_1y":     {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],             "func": ocn_drv2_069_composite_yoy_roc_zscore_1y},
    "ocn_drv2_070_avg_pos_qoq_roc_ewm":             {"inputs": ["avg_position"],                                                                 "func": ocn_drv2_070_avg_pos_qoq_roc_ewm},
    "ocn_drv2_071_hhi_yoy_roc_zscore_1y":           {"inputs": ["hhi"],                                                                          "func": ocn_drv2_071_hhi_yoy_roc_zscore_1y},
    "ocn_drv2_072_eff_n_yoy_roc_zscore_1y":         {"inputs": ["hhi"],                                                                          "func": ocn_drv2_072_eff_n_yoy_roc_zscore_1y},
    "ocn_drv2_073_top1_ratio_yoy_roc_zscore_1y":    {"inputs": ["top1_shares", "inst_shares"],                                                   "func": ocn_drv2_073_top1_ratio_yoy_roc_zscore_1y},
    "ocn_drv2_074_top5_ratio_yoy_roc_zscore_1y":    {"inputs": ["top5_shares", "inst_shares"],                                                   "func": ocn_drv2_074_top5_ratio_yoy_roc_zscore_1y},
    "ocn_drv2_075_top10_ratio_yoy_roc_zscore_1y":   {"inputs": ["top10_shares", "inst_shares"],                                                  "func": ocn_drv2_075_top10_ratio_yoy_roc_zscore_1y},
}
