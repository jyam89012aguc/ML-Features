"""
92_ownership_concentration — 3rd-Derivative Features (ocn_drv3_001 to ocn_drv3_075)
=====================================================================================
Domain: Rate-of-change of the 2nd-derivative concentration features.
These are the 3rd derivatives of the raw SF3 signals (raw -> base -> drv2 -> drv3).

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

NOTE: No cross-file imports. All base and drv2 logic is recomputed inline.
Drv3 features are QoQ changes (or slope ROC) applied to the drv2 series.
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
# Inline base recompute helpers (no cross-imports)
# ---------------------------------------------------------------------------

def _base_hhi(hhi: pd.Series) -> pd.Series:
    return _align_quarterly_to_daily(hhi)


def _base_eff_n(hhi: pd.Series) -> pd.Series:
    h = _align_quarterly_to_daily(hhi)
    return _safe_div(pd.Series(np.ones(len(h)), index=h.index), h)


def _base_top1_ratio(top1_shares, inst_shares) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top1_shares),
                     _align_quarterly_to_daily(inst_shares))


def _base_top5_ratio(top5_shares, inst_shares) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top5_shares),
                     _align_quarterly_to_daily(inst_shares))


def _base_top10_ratio(top10_shares, inst_shares) -> pd.Series:
    return _safe_div(_align_quarterly_to_daily(top10_shares),
                     _align_quarterly_to_daily(inst_shares))


def _base_outside_top10(top10_shares, inst_shares) -> pd.Series:
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

# ---------------------------------------------------------------------------
# Inline drv2 recompute helpers
# ---------------------------------------------------------------------------

def _drv2_hhi_qoq(hhi: pd.Series) -> pd.Series:
    """2nd deriv: QoQ acceleration of HHI."""
    b = _base_hhi(hhi)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_hhi_yoy(hhi: pd.Series) -> pd.Series:
    """2nd deriv: YoY acceleration of HHI."""
    b = _base_hhi(hhi)
    d1 = b - b.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _drv2_eff_n_qoq(hhi: pd.Series) -> pd.Series:
    b = _base_eff_n(hhi)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_eff_n_yoy(hhi: pd.Series) -> pd.Series:
    b = _base_eff_n(hhi)
    d1 = b - b.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _drv2_top1_qoq(top1_shares, inst_shares) -> pd.Series:
    b = _base_top1_ratio(top1_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_top5_qoq(top5_shares, inst_shares) -> pd.Series:
    b = _base_top5_ratio(top5_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_top10_qoq(top10_shares, inst_shares) -> pd.Series:
    b = _base_top10_ratio(top10_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_gini_qoq(top1_shares, top5_shares, top10_shares, inst_shares) -> pd.Series:
    b = _base_gini_proxy(top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares) -> pd.Series:
    b = _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_outside_top10_qoq(top10_shares, inst_shares) -> pd.Series:
    b = _base_outside_top10(top10_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_tail_ratio_qoq(top5_shares, top10_shares, inst_shares) -> pd.Series:
    b = _base_tail_ratio(top5_shares, top10_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


# ===========================================================================
# 3rd-Derivative Features (drv3_001 to drv3_025)
# ===========================================================================

def ocn_drv3_001_hhi_qoq_roc2(hhi: pd.Series) -> pd.Series:
    """QoQ change of the HHI QoQ acceleration (drv2)."""
    d2 = _drv2_hhi_qoq(hhi)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_002_hhi_yoy_roc2(hhi: pd.Series) -> pd.Series:
    """YoY change of the HHI YoY acceleration (drv2)."""
    d2 = _drv2_hhi_yoy(hhi)
    return d2 - d2.shift(_TD_YEAR)


def ocn_drv3_003_hhi_qoq_roc2_slope(hhi: pd.Series) -> pd.Series:
    """4Q OLS slope of the HHI QoQ acceleration series."""
    d2 = _drv2_hhi_qoq(hhi)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_004_hhi_qoq_roc2_ewm(hhi: pd.Series) -> pd.Series:
    """EWM (span=252) of the HHI QoQ acceleration series."""
    d2 = _drv2_hhi_qoq(hhi)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_005_eff_n_qoq_roc2(hhi: pd.Series) -> pd.Series:
    """QoQ change of the effective-N QoQ acceleration (drv2)."""
    d2 = _drv2_eff_n_qoq(hhi)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_006_eff_n_yoy_roc2(hhi: pd.Series) -> pd.Series:
    """YoY change of the effective-N YoY acceleration (drv2)."""
    d2 = _drv2_eff_n_yoy(hhi)
    return d2 - d2.shift(_TD_YEAR)


def ocn_drv3_007_eff_n_qoq_roc2_slope(hhi: pd.Series) -> pd.Series:
    """4Q OLS slope of the effective-N QoQ acceleration series."""
    d2 = _drv2_eff_n_qoq(hhi)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_008_top1_ratio_qoq_roc2(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the top-1 ratio QoQ acceleration (drv2)."""
    d2 = _drv2_top1_qoq(top1_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_009_top1_ratio_qoq_roc2_slope(top1_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the top-1 ratio QoQ acceleration."""
    d2 = _drv2_top1_qoq(top1_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_010_top1_ratio_qoq_roc2_ewm(top1_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """EWM (span=252) of the top-1 ratio QoQ acceleration."""
    d2 = _drv2_top1_qoq(top1_shares, inst_shares)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_011_top5_ratio_qoq_roc2(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the top-5 ratio QoQ acceleration (drv2)."""
    d2 = _drv2_top5_qoq(top5_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_012_top5_ratio_qoq_roc2_slope(top5_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the top-5 ratio QoQ acceleration."""
    d2 = _drv2_top5_qoq(top5_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_013_top10_ratio_qoq_roc2(top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the top-10 ratio QoQ acceleration (drv2)."""
    d2 = _drv2_top10_qoq(top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_014_top10_ratio_qoq_roc2_slope(top10_shares: pd.Series,
                                              inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the top-10 ratio QoQ acceleration."""
    d2 = _drv2_top10_qoq(top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_015_gini_proxy_qoq_roc2(top1_shares: pd.Series,
                                       top5_shares: pd.Series,
                                       top10_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the Gini-proxy QoQ acceleration (drv2)."""
    d2 = _drv2_gini_qoq(top1_shares, top5_shares, top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_016_gini_proxy_qoq_roc2_slope(top1_shares: pd.Series,
                                             top5_shares: pd.Series,
                                             top10_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the Gini-proxy QoQ acceleration."""
    d2 = _drv2_gini_qoq(top1_shares, top5_shares, top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_017_composite_qoq_roc2(hhi: pd.Series,
                                      top1_shares: pd.Series,
                                      top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the composite QoQ acceleration (drv2)."""
    d2 = _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_018_composite_qoq_roc2_slope(hhi: pd.Series,
                                            top1_shares: pd.Series,
                                            top5_shares: pd.Series,
                                            top10_shares: pd.Series,
                                            inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the composite QoQ acceleration."""
    d2 = _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_019_composite_qoq_roc2_ewm(hhi: pd.Series,
                                          top1_shares: pd.Series,
                                          top5_shares: pd.Series,
                                          top10_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """EWM (span=252) of the composite QoQ acceleration."""
    d2 = _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_020_outside_top10_qoq_roc2(top10_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the outside-top-10 share QoQ acceleration (drv2)."""
    d2 = _drv2_outside_top10_qoq(top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_021_outside_top10_qoq_roc2_slope(top10_shares: pd.Series,
                                                inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the outside-top-10 QoQ acceleration."""
    d2 = _drv2_outside_top10_qoq(top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_022_tail_ratio_qoq_roc2(top5_shares: pd.Series,
                                       top10_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the 6-10 tranche ratio QoQ acceleration (drv2)."""
    d2 = _drv2_tail_ratio_qoq(top5_shares, top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_023_tail_ratio_qoq_roc2_slope(top5_shares: pd.Series,
                                             top10_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the 6-10 tranche ratio QoQ acceleration."""
    d2 = _drv2_tail_ratio_qoq(top5_shares, top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_024_hhi_qoq_roc2_zscore_1y(hhi: pd.Series) -> pd.Series:
    """Z-score (1y) of the HHI QoQ acceleration series."""
    d2 = _drv2_hhi_qoq(hhi)
    mu  = _rolling_mean(d2, _TD_YEAR)
    sig = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - mu, sig)


def ocn_drv3_025_composite_qoq_roc2_zscore_1y(hhi: pd.Series,
                                                top1_shares: pd.Series,
                                                top5_shares: pd.Series,
                                                top10_shares: pd.Series,
                                                inst_shares: pd.Series) -> pd.Series:
    """Z-score (1y) of the composite QoQ acceleration series."""
    d2 = _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    mu  = _rolling_mean(d2, _TD_YEAR)
    sig = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - mu, sig)


# ---------------------------------------------------------------------------
# Additional drv2 helpers used only in new drv3 features
# ---------------------------------------------------------------------------

def _drv2_top1_yoy(top1_shares, inst_shares) -> pd.Series:
    b = _base_top1_ratio(top1_shares, inst_shares)
    d1 = b - b.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _drv2_top5_yoy(top5_shares, inst_shares) -> pd.Series:
    b = _base_top5_ratio(top5_shares, inst_shares)
    d1 = b - b.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _drv2_top10_yoy(top10_shares, inst_shares) -> pd.Series:
    b = _base_top10_ratio(top10_shares, inst_shares)
    d1 = b - b.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _drv2_hhi_slope(hhi: pd.Series) -> pd.Series:
    slope = _ols_slope(_base_hhi(hhi), _TD_YEAR)
    return slope - slope.shift(_TD_QTR)


def _drv2_composite_yoy(hhi, top1_shares, top5_shares, top10_shares, inst_shares) -> pd.Series:
    b = _base_composite(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    d1 = b - b.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _drv2_outside_top10_yoy(top10_shares, inst_shares) -> pd.Series:
    b = _base_outside_top10(top10_shares, inst_shares)
    d1 = b - b.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _base_outside_top5(top5_shares, inst_shares) -> pd.Series:
    t5  = _align_quarterly_to_daily(top5_shares)
    ins = _align_quarterly_to_daily(inst_shares)
    return _safe_div((ins - t5).clip(lower=0), ins)


def _drv2_outside_top5_qoq(top5_shares, inst_shares) -> pd.Series:
    b = _base_outside_top5(top5_shares, inst_shares)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _base_vph(inst_value, inst_holders) -> pd.Series:
    v = _align_quarterly_to_daily(inst_value)
    n = _align_quarterly_to_daily(inst_holders)
    return _safe_div(v, n)


def _drv2_vph_qoq(inst_value, inst_holders) -> pd.Series:
    b = _base_vph(inst_value, inst_holders)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _base_avg_pos(avg_position) -> pd.Series:
    return _align_quarterly_to_daily(avg_position)


def _drv2_avg_pos_qoq(avg_position) -> pd.Series:
    b = _base_avg_pos(avg_position)
    d1 = b - b.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


# ===========================================================================
# New 3rd-Derivative Features 026-075
# ===========================================================================

def ocn_drv3_026_hhi_yoy_roc2_slope(hhi: pd.Series) -> pd.Series:
    """4Q OLS slope of the HHI YoY acceleration series."""
    d2 = _drv2_hhi_yoy(hhi)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_027_hhi_yoy_roc2_ewm(hhi: pd.Series) -> pd.Series:
    """EWM(252) of the HHI YoY acceleration series."""
    d2 = _drv2_hhi_yoy(hhi)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_028_hhi_slope_roc_qoq(hhi: pd.Series) -> pd.Series:
    """QoQ change of the drv2 HHI OLS slope ROC."""
    d2 = _drv2_hhi_slope(hhi)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_029_hhi_slope_roc_slope(hhi: pd.Series) -> pd.Series:
    """4Q OLS slope of the drv2 HHI slope ROC series."""
    d2 = _drv2_hhi_slope(hhi)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_030_eff_n_yoy_roc2_slope(hhi: pd.Series) -> pd.Series:
    """4Q OLS slope of the effective-N YoY acceleration series."""
    d2 = _drv2_eff_n_yoy(hhi)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_031_eff_n_yoy_roc2_ewm(hhi: pd.Series) -> pd.Series:
    """EWM(252) of the effective-N YoY acceleration series."""
    d2 = _drv2_eff_n_yoy(hhi)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_032_top1_ratio_yoy_roc2(top1_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the top-1 ratio YoY acceleration (drv2)."""
    d2 = _drv2_top1_yoy(top1_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_033_top1_ratio_yoy_roc2_slope(top1_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the top-1 ratio YoY acceleration."""
    d2 = _drv2_top1_yoy(top1_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_034_top1_ratio_yoy_roc2_ewm(top1_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the top-1 ratio YoY acceleration."""
    d2 = _drv2_top1_yoy(top1_shares, inst_shares)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_035_top5_ratio_yoy_roc2(top5_shares: pd.Series,
                                       inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the top-5 ratio YoY acceleration (drv2)."""
    d2 = _drv2_top5_yoy(top5_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_036_top5_ratio_yoy_roc2_slope(top5_shares: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the top-5 ratio YoY acceleration."""
    d2 = _drv2_top5_yoy(top5_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_037_top5_ratio_yoy_roc2_ewm(top5_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the top-5 ratio YoY acceleration."""
    d2 = _drv2_top5_yoy(top5_shares, inst_shares)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_038_top10_ratio_yoy_roc2(top10_shares: pd.Series,
                                        inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the top-10 ratio YoY acceleration (drv2)."""
    d2 = _drv2_top10_yoy(top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_039_top10_ratio_yoy_roc2_slope(top10_shares: pd.Series,
                                              inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the top-10 ratio YoY acceleration."""
    d2 = _drv2_top10_yoy(top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_040_gini_proxy_qoq_roc2_ewm(top1_shares: pd.Series,
                                           top5_shares: pd.Series,
                                           top10_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the Gini-proxy QoQ acceleration."""
    d2 = _drv2_gini_qoq(top1_shares, top5_shares, top10_shares, inst_shares)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_041_composite_yoy_roc2(hhi: pd.Series,
                                      top1_shares: pd.Series,
                                      top5_shares: pd.Series,
                                      top10_shares: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the composite YoY acceleration (drv2)."""
    d2 = _drv2_composite_yoy(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_042_composite_yoy_roc2_slope(hhi: pd.Series,
                                            top1_shares: pd.Series,
                                            top5_shares: pd.Series,
                                            top10_shares: pd.Series,
                                            inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the composite YoY acceleration."""
    d2 = _drv2_composite_yoy(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_043_composite_yoy_roc2_ewm(hhi: pd.Series,
                                          top1_shares: pd.Series,
                                          top5_shares: pd.Series,
                                          top10_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the composite YoY acceleration."""
    d2 = _drv2_composite_yoy(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_044_outside_top10_yoy_roc2(top10_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the outside-top-10 YoY acceleration (drv2)."""
    d2 = _drv2_outside_top10_yoy(top10_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_045_outside_top10_yoy_roc2_slope(top10_shares: pd.Series,
                                                inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the outside-top-10 YoY acceleration."""
    d2 = _drv2_outside_top10_yoy(top10_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_046_outside_top5_qoq_roc2(top5_shares: pd.Series,
                                         inst_shares: pd.Series) -> pd.Series:
    """QoQ change of the outside-top-5 QoQ acceleration (drv2)."""
    d2 = _drv2_outside_top5_qoq(top5_shares, inst_shares)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_047_outside_top5_qoq_roc2_slope(top5_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """4Q OLS slope of the outside-top-5 QoQ acceleration."""
    d2 = _drv2_outside_top5_qoq(top5_shares, inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_048_vph_qoq_roc2(inst_value: pd.Series,
                                inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the value-per-holder QoQ acceleration (drv2)."""
    d2 = _drv2_vph_qoq(inst_value, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_049_vph_qoq_roc2_slope(inst_value: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    """4Q OLS slope of the value-per-holder QoQ acceleration."""
    d2 = _drv2_vph_qoq(inst_value, inst_holders)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_050_avg_pos_qoq_roc2(avg_position: pd.Series) -> pd.Series:
    """QoQ change of the average-position QoQ acceleration (drv2)."""
    d2 = _drv2_avg_pos_qoq(avg_position)
    return d2 - d2.shift(_TD_QTR)


def ocn_drv3_051_avg_pos_qoq_roc2_slope(avg_position: pd.Series) -> pd.Series:
    """4Q OLS slope of the average-position QoQ acceleration."""
    d2 = _drv2_avg_pos_qoq(avg_position)
    return _ols_slope(d2, _TD_YEAR)


def ocn_drv3_052_avg_pos_qoq_roc2_ewm(avg_position: pd.Series) -> pd.Series:
    """EWM(252) of the average-position QoQ acceleration."""
    d2 = _drv2_avg_pos_qoq(avg_position)
    return _ewm_mean(d2, _TD_YEAR)


def ocn_drv3_053_hhi_qoq_roc2_rank_1y(hhi: pd.Series) -> pd.Series:
    """1y percentile rank of the HHI QoQ acceleration series."""
    d2 = _drv2_hhi_qoq(hhi)
    return d2.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def ocn_drv3_054_eff_n_qoq_roc2_rank_1y(hhi: pd.Series) -> pd.Series:
    """1y percentile rank of the effective-N QoQ acceleration series."""
    d2 = _drv2_eff_n_qoq(hhi)
    return d2.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def ocn_drv3_055_top1_ratio_qoq_roc2_rank_1y(top1_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """1y percentile rank of the top-1 ratio QoQ acceleration series."""
    d2 = _drv2_top1_qoq(top1_shares, inst_shares)
    return d2.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def ocn_drv3_056_top5_ratio_qoq_roc2_rank_1y(top5_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """1y percentile rank of the top-5 ratio QoQ acceleration series."""
    d2 = _drv2_top5_qoq(top5_shares, inst_shares)
    return d2.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def ocn_drv3_057_top10_ratio_qoq_roc2_rank_1y(top10_shares: pd.Series,
                                                inst_shares: pd.Series) -> pd.Series:
    """1y percentile rank of the top-10 ratio QoQ acceleration series."""
    d2 = _drv2_top10_qoq(top10_shares, inst_shares)
    return d2.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def ocn_drv3_058_composite_qoq_roc2_rank_1y(hhi: pd.Series,
                                              top1_shares: pd.Series,
                                              top5_shares: pd.Series,
                                              top10_shares: pd.Series,
                                              inst_shares: pd.Series) -> pd.Series:
    """1y percentile rank of the composite QoQ acceleration series."""
    d2 = _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return d2.rolling(_TD_YEAR, min_periods=1).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def ocn_drv3_059_hhi_qoq_roc2_2y_mean(hhi: pd.Series) -> pd.Series:
    """2-year rolling mean of the HHI QoQ acceleration series."""
    d2 = _drv2_hhi_qoq(hhi)
    return _rolling_mean(d2, _TD_2Y)


def ocn_drv3_060_composite_qoq_roc2_2y_mean(hhi: pd.Series,
                                              top1_shares: pd.Series,
                                              top5_shares: pd.Series,
                                              top10_shares: pd.Series,
                                              inst_shares: pd.Series) -> pd.Series:
    """2-year rolling mean of the composite QoQ acceleration series."""
    d2 = _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return _rolling_mean(d2, _TD_2Y)


def ocn_drv3_061_hhi_qoq_roc2_abs(hhi: pd.Series) -> pd.Series:
    """Absolute value of HHI QoQ acceleration (magnitude signal)."""
    return _drv2_hhi_qoq(hhi).abs()


def ocn_drv3_062_composite_qoq_roc2_abs(hhi: pd.Series,
                                          top1_shares: pd.Series,
                                          top5_shares: pd.Series,
                                          top10_shares: pd.Series,
                                          inst_shares: pd.Series) -> pd.Series:
    """Absolute value of composite QoQ acceleration (volatility of acceleration)."""
    return _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares).abs()


def ocn_drv3_063_hhi_slope_roc_zscore_1y(hhi: pd.Series) -> pd.Series:
    """1y z-score of the drv2 HHI slope ROC series."""
    d2 = _drv2_hhi_slope(hhi)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv3_064_top1_ratio_qoq_roc2_zscore_1y(top1_shares: pd.Series,
                                                  inst_shares: pd.Series) -> pd.Series:
    """1y z-score of the top-1 ratio QoQ acceleration."""
    d2 = _drv2_top1_qoq(top1_shares, inst_shares)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv3_065_top5_ratio_qoq_roc2_zscore_1y(top5_shares: pd.Series,
                                                  inst_shares: pd.Series) -> pd.Series:
    """1y z-score of the top-5 ratio QoQ acceleration."""
    d2 = _drv2_top5_qoq(top5_shares, inst_shares)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv3_066_top10_ratio_qoq_roc2_zscore_1y(top10_shares: pd.Series,
                                                   inst_shares: pd.Series) -> pd.Series:
    """1y z-score of the top-10 ratio QoQ acceleration."""
    d2 = _drv2_top10_qoq(top10_shares, inst_shares)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv3_067_gini_proxy_qoq_roc2_zscore_1y(top1_shares: pd.Series,
                                                  top5_shares: pd.Series,
                                                  top10_shares: pd.Series,
                                                  inst_shares: pd.Series) -> pd.Series:
    """1y z-score of the Gini-proxy QoQ acceleration."""
    d2 = _drv2_gini_qoq(top1_shares, top5_shares, top10_shares, inst_shares)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv3_068_outside_top10_qoq_roc2_zscore_1y(top10_shares: pd.Series,
                                                     inst_shares: pd.Series) -> pd.Series:
    """1y z-score of the outside-top-10 QoQ acceleration."""
    d2 = _drv2_outside_top10_qoq(top10_shares, inst_shares)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv3_069_tail_ratio_qoq_roc2_zscore_1y(top5_shares: pd.Series,
                                                  top10_shares: pd.Series,
                                                  inst_shares: pd.Series) -> pd.Series:
    """1y z-score of the 6-10 tranche ratio QoQ acceleration."""
    d2 = _drv2_tail_ratio_qoq(top5_shares, top10_shares, inst_shares)
    return _zscore_rolling(d2, _TD_YEAR)


def ocn_drv3_070_hhi_qoq_roc2_sign(hhi: pd.Series) -> pd.Series:
    """Sign (+1/0/-1) of the HHI QoQ acceleration (direction indicator)."""
    return _drv2_hhi_qoq(hhi).apply(np.sign)


def ocn_drv3_071_composite_qoq_roc2_sign(hhi: pd.Series,
                                           top1_shares: pd.Series,
                                           top5_shares: pd.Series,
                                           top10_shares: pd.Series,
                                           inst_shares: pd.Series) -> pd.Series:
    """Sign of the composite concentration QoQ acceleration."""
    return _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares).apply(np.sign)


def ocn_drv3_072_hhi_qoq_roc2_yoy_chg(hhi: pd.Series) -> pd.Series:
    """YoY change in the HHI QoQ acceleration series."""
    d2 = _drv2_hhi_qoq(hhi)
    return d2 - d2.shift(_TD_YEAR)


def ocn_drv3_073_top1_ratio_qoq_roc2_yoy_chg(top1_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """YoY change in the top-1 ratio QoQ acceleration series."""
    d2 = _drv2_top1_qoq(top1_shares, inst_shares)
    return d2 - d2.shift(_TD_YEAR)


def ocn_drv3_074_composite_qoq_roc2_yoy_chg(hhi: pd.Series,
                                              top1_shares: pd.Series,
                                              top5_shares: pd.Series,
                                              top10_shares: pd.Series,
                                              inst_shares: pd.Series) -> pd.Series:
    """YoY change in the composite QoQ acceleration series."""
    d2 = _drv2_composite_qoq(hhi, top1_shares, top5_shares, top10_shares, inst_shares)
    return d2 - d2.shift(_TD_YEAR)


def ocn_drv3_075_outside_top10_qoq_roc2_ewm(top10_shares: pd.Series,
                                               inst_shares: pd.Series) -> pd.Series:
    """EWM(252) of the outside-top-10 QoQ acceleration series."""
    d2 = _drv2_outside_top10_qoq(top10_shares, inst_shares)
    return _ewm_mean(d2, _TD_YEAR)


# ===========================================================================
# Registry
# ===========================================================================
OWNERSHIP_CONCENTRATION_REGISTRY_3RD_DERIVATIVES = {
    "ocn_drv3_001_hhi_qoq_roc2":                  {"inputs": ["hhi"],                                                                             "func": ocn_drv3_001_hhi_qoq_roc2},
    "ocn_drv3_002_hhi_yoy_roc2":                  {"inputs": ["hhi"],                                                                             "func": ocn_drv3_002_hhi_yoy_roc2},
    "ocn_drv3_003_hhi_qoq_roc2_slope":            {"inputs": ["hhi"],                                                                             "func": ocn_drv3_003_hhi_qoq_roc2_slope},
    "ocn_drv3_004_hhi_qoq_roc2_ewm":              {"inputs": ["hhi"],                                                                             "func": ocn_drv3_004_hhi_qoq_roc2_ewm},
    "ocn_drv3_005_eff_n_qoq_roc2":                {"inputs": ["hhi"],                                                                             "func": ocn_drv3_005_eff_n_qoq_roc2},
    "ocn_drv3_006_eff_n_yoy_roc2":                {"inputs": ["hhi"],                                                                             "func": ocn_drv3_006_eff_n_yoy_roc2},
    "ocn_drv3_007_eff_n_qoq_roc2_slope":          {"inputs": ["hhi"],                                                                             "func": ocn_drv3_007_eff_n_qoq_roc2_slope},
    "ocn_drv3_008_top1_ratio_qoq_roc2":           {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_008_top1_ratio_qoq_roc2},
    "ocn_drv3_009_top1_ratio_qoq_roc2_slope":     {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_009_top1_ratio_qoq_roc2_slope},
    "ocn_drv3_010_top1_ratio_qoq_roc2_ewm":       {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_010_top1_ratio_qoq_roc2_ewm},
    "ocn_drv3_011_top5_ratio_qoq_roc2":           {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_011_top5_ratio_qoq_roc2},
    "ocn_drv3_012_top5_ratio_qoq_roc2_slope":     {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_012_top5_ratio_qoq_roc2_slope},
    "ocn_drv3_013_top10_ratio_qoq_roc2":          {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_013_top10_ratio_qoq_roc2},
    "ocn_drv3_014_top10_ratio_qoq_roc2_slope":    {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_014_top10_ratio_qoq_roc2_slope},
    "ocn_drv3_015_gini_proxy_qoq_roc2":           {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                       "func": ocn_drv3_015_gini_proxy_qoq_roc2},
    "ocn_drv3_016_gini_proxy_qoq_roc2_slope":     {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                       "func": ocn_drv3_016_gini_proxy_qoq_roc2_slope},
    "ocn_drv3_017_composite_qoq_roc2":            {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_017_composite_qoq_roc2},
    "ocn_drv3_018_composite_qoq_roc2_slope":      {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_018_composite_qoq_roc2_slope},
    "ocn_drv3_019_composite_qoq_roc2_ewm":        {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_019_composite_qoq_roc2_ewm},
    "ocn_drv3_020_outside_top10_qoq_roc2":        {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_020_outside_top10_qoq_roc2},
    "ocn_drv3_021_outside_top10_qoq_roc2_slope":  {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_021_outside_top10_qoq_roc2_slope},
    "ocn_drv3_022_tail_ratio_qoq_roc2":           {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_drv3_022_tail_ratio_qoq_roc2},
    "ocn_drv3_023_tail_ratio_qoq_roc2_slope":     {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_drv3_023_tail_ratio_qoq_roc2_slope},
    "ocn_drv3_024_hhi_qoq_roc2_zscore_1y":        {"inputs": ["hhi"],                                                                             "func": ocn_drv3_024_hhi_qoq_roc2_zscore_1y},
    "ocn_drv3_025_composite_qoq_roc2_zscore_1y":       {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_025_composite_qoq_roc2_zscore_1y},
    "ocn_drv3_026_hhi_yoy_roc2_slope":                 {"inputs": ["hhi"],                                                                             "func": ocn_drv3_026_hhi_yoy_roc2_slope},
    "ocn_drv3_027_hhi_yoy_roc2_ewm":                   {"inputs": ["hhi"],                                                                             "func": ocn_drv3_027_hhi_yoy_roc2_ewm},
    "ocn_drv3_028_hhi_slope_roc_qoq":                  {"inputs": ["hhi"],                                                                             "func": ocn_drv3_028_hhi_slope_roc_qoq},
    "ocn_drv3_029_hhi_slope_roc_slope":                {"inputs": ["hhi"],                                                                             "func": ocn_drv3_029_hhi_slope_roc_slope},
    "ocn_drv3_030_eff_n_yoy_roc2_slope":               {"inputs": ["hhi"],                                                                             "func": ocn_drv3_030_eff_n_yoy_roc2_slope},
    "ocn_drv3_031_eff_n_yoy_roc2_ewm":                 {"inputs": ["hhi"],                                                                             "func": ocn_drv3_031_eff_n_yoy_roc2_ewm},
    "ocn_drv3_032_top1_ratio_yoy_roc2":                {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_032_top1_ratio_yoy_roc2},
    "ocn_drv3_033_top1_ratio_yoy_roc2_slope":          {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_033_top1_ratio_yoy_roc2_slope},
    "ocn_drv3_034_top1_ratio_yoy_roc2_ewm":            {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_034_top1_ratio_yoy_roc2_ewm},
    "ocn_drv3_035_top5_ratio_yoy_roc2":                {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_035_top5_ratio_yoy_roc2},
    "ocn_drv3_036_top5_ratio_yoy_roc2_slope":          {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_036_top5_ratio_yoy_roc2_slope},
    "ocn_drv3_037_top5_ratio_yoy_roc2_ewm":            {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_037_top5_ratio_yoy_roc2_ewm},
    "ocn_drv3_038_top10_ratio_yoy_roc2":               {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_038_top10_ratio_yoy_roc2},
    "ocn_drv3_039_top10_ratio_yoy_roc2_slope":         {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_039_top10_ratio_yoy_roc2_slope},
    "ocn_drv3_040_gini_proxy_qoq_roc2_ewm":            {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                       "func": ocn_drv3_040_gini_proxy_qoq_roc2_ewm},
    "ocn_drv3_041_composite_yoy_roc2":                 {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_041_composite_yoy_roc2},
    "ocn_drv3_042_composite_yoy_roc2_slope":           {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_042_composite_yoy_roc2_slope},
    "ocn_drv3_043_composite_yoy_roc2_ewm":             {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_043_composite_yoy_roc2_ewm},
    "ocn_drv3_044_outside_top10_yoy_roc2":             {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_044_outside_top10_yoy_roc2},
    "ocn_drv3_045_outside_top10_yoy_roc2_slope":       {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_045_outside_top10_yoy_roc2_slope},
    "ocn_drv3_046_outside_top5_qoq_roc2":              {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_046_outside_top5_qoq_roc2},
    "ocn_drv3_047_outside_top5_qoq_roc2_slope":        {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_047_outside_top5_qoq_roc2_slope},
    "ocn_drv3_048_vph_qoq_roc2":                       {"inputs": ["inst_value", "inst_holders"],                                                      "func": ocn_drv3_048_vph_qoq_roc2},
    "ocn_drv3_049_vph_qoq_roc2_slope":                 {"inputs": ["inst_value", "inst_holders"],                                                      "func": ocn_drv3_049_vph_qoq_roc2_slope},
    "ocn_drv3_050_avg_pos_qoq_roc2":                   {"inputs": ["avg_position"],                                                                    "func": ocn_drv3_050_avg_pos_qoq_roc2},
    "ocn_drv3_051_avg_pos_qoq_roc2_slope":             {"inputs": ["avg_position"],                                                                    "func": ocn_drv3_051_avg_pos_qoq_roc2_slope},
    "ocn_drv3_052_avg_pos_qoq_roc2_ewm":               {"inputs": ["avg_position"],                                                                    "func": ocn_drv3_052_avg_pos_qoq_roc2_ewm},
    "ocn_drv3_053_hhi_qoq_roc2_rank_1y":               {"inputs": ["hhi"],                                                                             "func": ocn_drv3_053_hhi_qoq_roc2_rank_1y},
    "ocn_drv3_054_eff_n_qoq_roc2_rank_1y":             {"inputs": ["hhi"],                                                                             "func": ocn_drv3_054_eff_n_qoq_roc2_rank_1y},
    "ocn_drv3_055_top1_ratio_qoq_roc2_rank_1y":        {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_055_top1_ratio_qoq_roc2_rank_1y},
    "ocn_drv3_056_top5_ratio_qoq_roc2_rank_1y":        {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_056_top5_ratio_qoq_roc2_rank_1y},
    "ocn_drv3_057_top10_ratio_qoq_roc2_rank_1y":       {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_057_top10_ratio_qoq_roc2_rank_1y},
    "ocn_drv3_058_composite_qoq_roc2_rank_1y":         {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_058_composite_qoq_roc2_rank_1y},
    "ocn_drv3_059_hhi_qoq_roc2_2y_mean":               {"inputs": ["hhi"],                                                                             "func": ocn_drv3_059_hhi_qoq_roc2_2y_mean},
    "ocn_drv3_060_composite_qoq_roc2_2y_mean":         {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_060_composite_qoq_roc2_2y_mean},
    "ocn_drv3_061_hhi_qoq_roc2_abs":                   {"inputs": ["hhi"],                                                                             "func": ocn_drv3_061_hhi_qoq_roc2_abs},
    "ocn_drv3_062_composite_qoq_roc2_abs":             {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_062_composite_qoq_roc2_abs},
    "ocn_drv3_063_hhi_slope_roc_zscore_1y":            {"inputs": ["hhi"],                                                                             "func": ocn_drv3_063_hhi_slope_roc_zscore_1y},
    "ocn_drv3_064_top1_ratio_qoq_roc2_zscore_1y":      {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_064_top1_ratio_qoq_roc2_zscore_1y},
    "ocn_drv3_065_top5_ratio_qoq_roc2_zscore_1y":      {"inputs": ["top5_shares", "inst_shares"],                                                      "func": ocn_drv3_065_top5_ratio_qoq_roc2_zscore_1y},
    "ocn_drv3_066_top10_ratio_qoq_roc2_zscore_1y":     {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_066_top10_ratio_qoq_roc2_zscore_1y},
    "ocn_drv3_067_gini_proxy_qoq_roc2_zscore_1y":      {"inputs": ["top1_shares", "top5_shares", "top10_shares", "inst_shares"],                       "func": ocn_drv3_067_gini_proxy_qoq_roc2_zscore_1y},
    "ocn_drv3_068_outside_top10_qoq_roc2_zscore_1y":   {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_068_outside_top10_qoq_roc2_zscore_1y},
    "ocn_drv3_069_tail_ratio_qoq_roc2_zscore_1y":      {"inputs": ["top5_shares", "top10_shares", "inst_shares"],                                      "func": ocn_drv3_069_tail_ratio_qoq_roc2_zscore_1y},
    "ocn_drv3_070_hhi_qoq_roc2_sign":                  {"inputs": ["hhi"],                                                                             "func": ocn_drv3_070_hhi_qoq_roc2_sign},
    "ocn_drv3_071_composite_qoq_roc2_sign":            {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_071_composite_qoq_roc2_sign},
    "ocn_drv3_072_hhi_qoq_roc2_yoy_chg":               {"inputs": ["hhi"],                                                                             "func": ocn_drv3_072_hhi_qoq_roc2_yoy_chg},
    "ocn_drv3_073_top1_ratio_qoq_roc2_yoy_chg":        {"inputs": ["top1_shares", "inst_shares"],                                                      "func": ocn_drv3_073_top1_ratio_qoq_roc2_yoy_chg},
    "ocn_drv3_074_composite_qoq_roc2_yoy_chg":         {"inputs": ["hhi", "top1_shares", "top5_shares", "top10_shares", "inst_shares"],                "func": ocn_drv3_074_composite_qoq_roc2_yoy_chg},
    "ocn_drv3_075_outside_top10_qoq_roc2_ewm":         {"inputs": ["top10_shares", "inst_shares"],                                                     "func": ocn_drv3_075_outside_top10_qoq_roc2_ewm},
}
