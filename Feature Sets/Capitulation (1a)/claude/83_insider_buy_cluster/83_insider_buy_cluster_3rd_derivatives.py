"""
83_insider_buy_cluster — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative insider buy-cluster features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction filings to one row per (ticker, date).  These are EVENT-DRIVEN
flow series: most days are ZERO (no insider transaction filed); positive values
appear only on filing days.  Do NOT forward-fill.

3rd-Derivative Note
--------------------
3rd-derivative features are derived from 2nd-derivative concepts (themselves
derived from rolling-window buy-cluster aggregates).  On a daily index with
sparse event data they will be extremely sparse — this is correct and expected.
All derivations look strictly backward.

Canonical SF2 field names used in this file (lowercase):
    insider_buy_count, insider_buyers, officer_buy_count, director_buy_count

Feature numbering: ibc_drv3_001 .. ibc_drv3_075
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WK   = 5
_TD_MO   = 21
_TD_QTR  = 63
_TD_2Q   = 126
_TD_YEAR = 252
_TD_2Y   = 504
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _active_days(s: pd.Series, w: int) -> pd.Series:
    return _rolling_sum((s > 0).astype(float), w)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _ols_slope(arr: np.ndarray) -> float:
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = ((x - xm) ** 2).sum()
    if denom == 0.0:
        return np.nan
    return float(((x - xm) * (arr - ym)).sum() / denom)


# ── Base and 2nd-derivative helpers (self-contained, no cross-file imports) ───

def _buyers_21d(insider_buyers: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buyers, _TD_MO)


def _buyers_63d(insider_buyers: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buyers, _TD_QTR)


def _buy_count_21d(insider_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_count, _TD_MO)


def _buy_count_63d(insider_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_count, _TD_QTR)


def _active_days_21d(insider_buy_count: pd.Series) -> pd.Series:
    return _active_days(insider_buy_count, _TD_MO)


def _active_days_63d(insider_buy_count: pd.Series) -> pd.Series:
    return _active_days(insider_buy_count, _TD_QTR)


def _officer_63d(officer_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_count, _TD_QTR)


def _director_63d(director_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_count, _TD_QTR)


def _buyer_zscore_21d(insider_buyers: pd.Series) -> pd.Series:
    return _zscore_rolling(_buyers_21d(insider_buyers), _TD_YEAR)


def _buyer_zscore_63d(insider_buyers: pd.Series) -> pd.Series:
    return _zscore_rolling(_buyers_63d(insider_buyers), _TD_YEAR)


# 2nd-derivative concepts (recomputed inline)
def _d2_buyers_21d(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of the 21d buyer count."""
    b = _buyers_21d(insider_buyers)
    return b - b.shift(_TD_MO)


def _d2_buyers_63d(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 63d buyer count."""
    b = _buyers_63d(insider_buyers)
    return b - b.shift(_TD_QTR)


def _d2_buy_count_21d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of the 21d buy-transaction count."""
    b = _buy_count_21d(insider_buy_count)
    return b - b.shift(_TD_MO)


def _d2_buy_count_63d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 63d buy-transaction count."""
    b = _buy_count_63d(insider_buy_count)
    return b - b.shift(_TD_QTR)


def _d2_active_days_21d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of the 21d active-buy-day count."""
    a = _active_days_21d(insider_buy_count)
    return a - a.shift(_TD_MO)


def _d2_active_days_63d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 63d active-buy-day count."""
    a = _active_days_63d(insider_buy_count)
    return a - a.shift(_TD_QTR)


def _d2_buyer_zscore_21d(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of the 21d buyer z-score."""
    z = _buyer_zscore_21d(insider_buyers)
    return z - z.shift(_TD_MO)


def _d2_buyer_zscore_63d(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 63d buyer z-score."""
    z = _buyer_zscore_63d(insider_buyers)
    return z - z.shift(_TD_QTR)


def _d2_officer_63d(officer_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 63d officer buy count."""
    b = _officer_63d(officer_buy_count)
    return b - b.shift(_TD_QTR)


def _d2_director_63d(director_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 63d director buy count."""
    b = _director_63d(director_buy_count)
    return b - b.shift(_TD_QTR)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def ibc_drv3_001_buyers_21d_d2_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of 21d buyer count].
    = b21(t) - 2*b21(t-21) + b21(t-42) differenced again by 21d.
    """
    d2 = _d2_buyers_21d(insider_buyers)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_002_buyers_63d_d2_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 63d buyer count]."""
    d2 = _d2_buyers_63d(insider_buyers)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_003_buy_count_21d_d2_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of 21d buy-transaction count]."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_004_buy_count_63d_d2_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 63d buy-transaction count]."""
    d2 = _d2_buy_count_63d(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_005_active_days_21d_d2_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of 21d active-buy-day count]."""
    d2 = _d2_active_days_21d(insider_buy_count)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_006_active_days_63d_d2_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 63d active-buy-day count]."""
    d2 = _d2_active_days_63d(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_007_buyer_zscore_21d_d2_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of the 21d buyer z-score]."""
    d2 = _d2_buyer_zscore_21d(insider_buyers)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_008_buyer_zscore_63d_d2_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of the 63d buyer z-score]."""
    d2 = _d2_buyer_zscore_63d(insider_buyers)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_009_officer_63d_d2_63d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 63d officer buy count]."""
    d2 = _d2_officer_63d(officer_buy_count)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_010_director_63d_d2_63d_diff(director_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 63d director buy count]."""
    d2 = _d2_director_63d(director_buy_count)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_011_buyers_21d_d2_slope_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of the 2nd-derivative [21d diff of 21d buyer count] over trailing 252 days."""
    d2 = _d2_buyers_21d(insider_buyers)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_012_buy_count_21d_d2_slope_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 2nd-deriv [21d diff of 21d buy-count] over trailing 252 days."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_013_buyers_63d_d2_slope_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of the 2nd-deriv [63d diff of 63d buyer count] over trailing 252 days."""
    d2 = _d2_buyers_63d(insider_buyers)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_014_buyers_21d_d2_zscore_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative [21d diff of 21d buyer count] in a 252-day window."""
    d2 = _d2_buyers_21d(insider_buyers)
    return _zscore_rolling(d2, _TD_YEAR)


def ibc_drv3_015_buy_count_21d_d2_zscore_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative [21d diff of 21d buy count] in a 252-day window."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return _zscore_rolling(d2, _TD_YEAR)


def ibc_drv3_016_buyers_21d_d2_rank_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of the 2nd-deriv [21d diff of 21d buyer count] in a 252-day window."""
    d2 = _d2_buyers_21d(insider_buyers)
    return _rolling_rank_pct(d2, _TD_YEAR)


def ibc_drv3_017_buy_count_63d_d2_rank_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of the 2nd-deriv [63d diff of 63d buy count] in a 252-day window."""
    d2 = _d2_buy_count_63d(insider_buy_count)
    return _rolling_rank_pct(d2, _TD_YEAR)


def ibc_drv3_018_buyers_21d_d2_ewm_dev(insider_buyers: pd.Series) -> pd.Series:
    """
    Deviation of the 2nd-deriv [21d diff of 21d buyer count] from its EWM (span=63).
    Measures when the acceleration of buyers diverges from its recent trend.
    """
    d2 = _d2_buyers_21d(insider_buyers)
    return d2 - _ewm_mean(d2, _TD_QTR)


def ibc_drv3_019_buy_count_21d_d2_ewm_dev(insider_buy_count: pd.Series) -> pd.Series:
    """Deviation of 2nd-deriv [21d diff of 21d buy count] from its EWM (span=63)."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return d2 - _ewm_mean(d2, _TD_QTR)


def ibc_drv3_020_buyers_21d_d2_positive_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary: 1 when the 2nd-deriv of 21d buyer count is positive (accelerating burst)."""
    d2 = _d2_buyers_21d(insider_buyers)
    return (d2 > 0).astype(float)


def ibc_drv3_021_buy_count_21d_d2_positive_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 when the 2nd-deriv of 21d buy-transaction count is positive."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return (d2 > 0).astype(float)


def ibc_drv3_022_buyers_63d_d2_positive_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary: 1 when the 2nd-deriv of 63d buyer count is positive."""
    d2 = _d2_buyers_63d(insider_buyers)
    return (d2 > 0).astype(float)


def ibc_drv3_023_buyers_21d_d3_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """True 3rd-order difference: diff of [diff of [diff of 21d buyer count]], 21d steps.
    = b21(t) - 3*b21(t-21) + 3*b21(t-42) - b21(t-63).
    """
    b21 = _buyers_21d(insider_buyers)
    d1  = b21 - b21.shift(_TD_MO)
    d2  = d1  - d1.shift(_TD_MO)
    return d2  - d2.shift(_TD_MO)


def ibc_drv3_024_buy_count_21d_d3_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """True 3rd-order difference of 21d buy-transaction count with 21d steps."""
    b21 = _buy_count_21d(insider_buy_count)
    d1  = b21 - b21.shift(_TD_MO)
    d2  = d1  - d1.shift(_TD_MO)
    return d2  - d2.shift(_TD_MO)


def ibc_drv3_025_buyers_21d_d2_52w_high_flag(insider_buyers: pd.Series) -> pd.Series:
    """
    Binary: 1 when the 2nd-deriv [21d diff of 21d buyer count] is at its
    trailing 252-day high.  Marks extreme positive acceleration.
    """
    d2    = _d2_buyers_21d(insider_buyers)
    hi252 = _rolling_max(d2, _TD_YEAR)
    return (d2 >= hi252).astype(float)


# ── Additional 2nd-deriv helpers for 3rd-deriv features (026-075) ────────────

def _d2_buyers_126d(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 126d buyer count."""
    b = _rolling_sum(insider_buyers, _TD_2Q)
    return b - b.shift(_TD_QTR)


def _d2_buy_count_126d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 126d buy-transaction count."""
    b = _rolling_sum(insider_buy_count, _TD_2Q)
    return b - b.shift(_TD_QTR)


def _d2_active_days_126d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of the 126d active-buy-day count."""
    a = _rolling_sum((insider_buy_count > 0).astype(float), _TD_2Q)
    return a - a.shift(_TD_QTR)


def _d2_officer_21d(officer_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of 21d officer buy count."""
    b = _rolling_sum(officer_buy_count, _TD_MO)
    return b - b.shift(_TD_MO)


def _d2_director_21d(director_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of 21d director buy count."""
    b = _rolling_sum(director_buy_count, _TD_MO)
    return b - b.shift(_TD_MO)


def _d2_buy_day_density_21d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of 21d buy-day density."""
    d = _safe_div(_rolling_sum((insider_buy_count > 0).astype(float), _TD_MO),
                  pd.Series(float(_TD_MO), index=insider_buy_count.index))
    return d - d.shift(_TD_MO)


def _d2_buy_day_density_63d(insider_buy_count: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of 63d buy-day density."""
    d = _safe_div(_rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR),
                  pd.Series(float(_TD_QTR), index=insider_buy_count.index))
    return d - d.shift(_TD_QTR)


def _d2_multi_buyer_days_21d(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of multi-buyer-days count (>=2 buyers) in 21d."""
    m = _rolling_sum((insider_buyers >= 2).astype(float), _TD_MO)
    return m - m.shift(_TD_MO)


def _d2_multi_buyer_days_63d(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 63d diff of multi-buyer-days count (>=2 buyers) in 63d."""
    m = _rolling_sum((insider_buyers >= 2).astype(float), _TD_QTR)
    return m - m.shift(_TD_QTR)


def _d2_buyers_ewm_cross(insider_buyers: pd.Series) -> pd.Series:
    """2nd-deriv: 21d diff of (EWM_21 - EWM_63) buyer cross."""
    cross = _ewm_mean(insider_buyers, _TD_MO) - _ewm_mean(insider_buyers, _TD_QTR)
    return cross - cross.shift(_TD_MO)


# ── 3rd-Derivative Feature Functions (026-075) ────────────────────────────────

def ibc_drv3_026_buyers_126d_d2_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 126d buyer count]."""
    d2 = _d2_buyers_126d(insider_buyers)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_027_buy_count_126d_d2_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 126d buy-transaction count]."""
    d2 = _d2_buy_count_126d(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_028_active_days_126d_d2_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 126d active-buy-day count]."""
    d2 = _d2_active_days_126d(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_029_officer_21d_d2_21d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of 21d officer buy count]."""
    d2 = _d2_officer_21d(officer_buy_count)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_030_director_21d_d2_21d_diff(director_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of 21d director buy count]."""
    d2 = _d2_director_21d(director_buy_count)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_031_buy_day_density_21d_d2_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of 21d buy-day density]."""
    d2 = _d2_buy_day_density_21d(insider_buy_count)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_032_buy_day_density_63d_d2_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 63d buy-day density]."""
    d2 = _d2_buy_day_density_63d(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_033_multi_buyer_days_21d_d2_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of 21d multi-buyer-day count]."""
    d2 = _d2_multi_buyer_days_21d(insider_buyers)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_034_multi_buyer_days_63d_d2_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [63d diff of 63d multi-buyer-day count]."""
    d2 = _d2_multi_buyer_days_63d(insider_buyers)
    return d2 - d2.shift(_TD_QTR)


def ibc_drv3_035_buyers_ewm_cross_d2_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of (EWM_21 - EWM_63) buyer cross]."""
    d2 = _d2_buyers_ewm_cross(insider_buyers)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_036_buyers_21d_d2_slope_in_63d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of 2nd-deriv [21d diff of 21d buyer count] over trailing 63-day window."""
    d2 = _d2_buyers_21d(insider_buyers)
    return d2.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_037_buy_count_21d_d2_slope_in_63d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 2nd-deriv [21d diff of 21d buy count] over trailing 63-day window."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return d2.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_038_buyers_63d_d2_slope_in_63d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of 2nd-deriv [63d diff of 63d buyer count] over trailing 63-day window."""
    d2 = _d2_buyers_63d(insider_buyers)
    return d2.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_039_buyers_21d_d2_zscore_in_63d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score of 2nd-deriv [21d diff of 21d buyer count] in trailing 63-day window."""
    d2 = _d2_buyers_21d(insider_buyers)
    return _zscore_rolling(d2, _TD_QTR)


def ibc_drv3_040_buy_count_21d_d2_zscore_in_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of 2nd-deriv [21d diff of 21d buy count] in trailing 63-day window."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return _zscore_rolling(d2, _TD_QTR)


def ibc_drv3_041_buyers_63d_d2_zscore_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score of 2nd-deriv [63d diff of 63d buyer count] in trailing 252-day window."""
    d2 = _d2_buyers_63d(insider_buyers)
    return _zscore_rolling(d2, _TD_YEAR)


def ibc_drv3_042_buy_count_63d_d2_zscore_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of 2nd-deriv [63d diff of 63d buy count] in trailing 252-day window."""
    d2 = _d2_buy_count_63d(insider_buy_count)
    return _zscore_rolling(d2, _TD_YEAR)


def ibc_drv3_043_buyers_21d_d2_rank_in_63d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-deriv [21d diff of 21d buyer count] in trailing 63-day window."""
    d2 = _d2_buyers_21d(insider_buyers)
    return _rolling_rank_pct(d2, _TD_QTR)


def ibc_drv3_044_buy_count_21d_d2_rank_in_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-deriv [21d diff of 21d buy count] in trailing 63-day window."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return _rolling_rank_pct(d2, _TD_QTR)


def ibc_drv3_045_buyers_63d_d2_rank_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-deriv [63d diff of 63d buyer count] in trailing 252-day window."""
    d2 = _d2_buyers_63d(insider_buyers)
    return _rolling_rank_pct(d2, _TD_YEAR)


def ibc_drv3_046_buyers_21d_d2_ewm_dev_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """21d diff of [d2_buyers_21d minus its EWM(span=63)]; acceleration of EWM-deviation of momentum."""
    d2  = _d2_buyers_21d(insider_buyers)
    dev = d2 - _ewm_mean(d2, _TD_QTR)
    return dev - dev.shift(_TD_MO)


def ibc_drv3_047_buy_count_21d_d2_ewm_dev_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21d diff of [d2_buy_count_21d minus its EWM(span=63)]."""
    d2  = _d2_buy_count_21d(insider_buy_count)
    dev = d2 - _ewm_mean(d2, _TD_QTR)
    return dev - dev.shift(_TD_MO)


def ibc_drv3_048_buyers_21d_d2_positive_streak(insider_buyers: pd.Series) -> pd.Series:
    """Current consecutive-day streak of positive 2nd-deriv [21d diff of 21d buyer count]."""
    d2   = _d2_buyers_21d(insider_buyers)
    flag = (d2 > 0).astype(int)
    arr  = flag.values
    out  = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1) if arr[i] else 0.0
    return pd.Series(out, index=insider_buyers.index)


def ibc_drv3_049_buy_count_21d_d2_positive_streak(insider_buy_count: pd.Series) -> pd.Series:
    """Current consecutive-day streak of positive 2nd-deriv [21d diff of 21d buy count]."""
    d2   = _d2_buy_count_21d(insider_buy_count)
    flag = (d2 > 0).astype(int)
    arr  = flag.values
    out  = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1) if arr[i] else 0.0
    return pd.Series(out, index=insider_buy_count.index)


def ibc_drv3_050_buyers_63d_d2_positive_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary: 1 when 2nd-deriv [63d diff of 63d buyer count] is positive."""
    d2 = _d2_buyers_63d(insider_buyers)
    return (d2 > 0).astype(float)


def ibc_drv3_051_buy_count_63d_d2_positive_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 when 2nd-deriv [63d diff of 63d buy-transaction count] is positive."""
    d2 = _d2_buy_count_63d(insider_buy_count)
    return (d2 > 0).astype(float)


def ibc_drv3_052_active_days_21d_d2_positive_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 when 2nd-deriv [21d diff of 21d active-buy-days] is positive."""
    d2 = _d2_active_days_21d(insider_buy_count)
    return (d2 > 0).astype(float)


def ibc_drv3_053_active_days_63d_d2_positive_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 when 2nd-deriv [63d diff of 63d active-buy-days] is positive."""
    d2 = _d2_active_days_63d(insider_buy_count)
    return (d2 > 0).astype(float)


def ibc_drv3_054_buyers_21d_d2_52w_low_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary: 1 when 2nd-deriv [21d diff of 21d buyer count] is at its 252-day low (extreme deceleration)."""
    d2    = _d2_buyers_21d(insider_buyers)
    lo252 = _rolling_min(d2, _TD_YEAR)
    return (d2 <= lo252).astype(float)


def ibc_drv3_055_buy_count_21d_d2_52w_high_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 when 2nd-deriv [21d diff of 21d buy count] is at its 252-day high."""
    d2    = _d2_buy_count_21d(insider_buy_count)
    hi252 = _rolling_max(d2, _TD_YEAR)
    return (d2 >= hi252).astype(float)


def ibc_drv3_056_buyers_21d_d3_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [21d diff of [21d diff of 21d buyer count]]."""
    b21 = _buyers_21d(insider_buyers)
    d1  = b21 - b21.shift(_TD_MO)
    d2  = d1  - d1.shift(_TD_MO)
    return d2  - d2.shift(_TD_QTR)


def ibc_drv3_057_buy_count_21d_d3_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 63d diff of [21d diff of [21d diff of 21d buy count]]."""
    b21 = _buy_count_21d(insider_buy_count)
    d1  = b21 - b21.shift(_TD_MO)
    d2  = d1  - d1.shift(_TD_MO)
    return d2  - d2.shift(_TD_QTR)


def ibc_drv3_058_buyers_63d_d3_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """True 3rd-order difference of 63d buyer count with 63d steps."""
    b63 = _buyers_63d(insider_buyers)
    d1  = b63 - b63.shift(_TD_QTR)
    d2  = d1  - d1.shift(_TD_QTR)
    return d2  - d2.shift(_TD_QTR)


def ibc_drv3_059_buy_count_63d_d3_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """True 3rd-order difference of 63d buy-transaction count with 63d steps."""
    b63 = _buy_count_63d(insider_buy_count)
    d1  = b63 - b63.shift(_TD_QTR)
    d2  = d1  - d1.shift(_TD_QTR)
    return d2  - d2.shift(_TD_QTR)


def ibc_drv3_060_officer_63d_d2_21d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [63d diff of 63d officer buy count]."""
    d2 = _d2_officer_63d(officer_buy_count)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_061_director_63d_d2_21d_diff(director_buy_count: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [63d diff of 63d director buy count]."""
    d2 = _d2_director_63d(director_buy_count)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_062_buyers_21d_d2_rolling_max_63d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 63-day maximum of 2nd-deriv [21d diff of 21d buyer count]; measures recent peak acceleration."""
    d2 = _d2_buyers_21d(insider_buyers)
    return _rolling_max(d2, _TD_QTR)


def ibc_drv3_063_buy_count_21d_d2_rolling_max_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 63-day maximum of 2nd-deriv [21d diff of 21d buy count]."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return _rolling_max(d2, _TD_QTR)


def ibc_drv3_064_buyers_21d_d2_slope_in_504d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of 2nd-deriv [21d diff of 21d buyer count] over trailing 504-day window."""
    d2 = _d2_buyers_21d(insider_buyers)
    return d2.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_065_buyers_63d_d2_ewm_dev(insider_buyers: pd.Series) -> pd.Series:
    """Deviation of 2nd-deriv [63d diff of 63d buyer count] from its EWM (span=63)."""
    d2 = _d2_buyers_63d(insider_buyers)
    return d2 - _ewm_mean(d2, _TD_QTR)


def ibc_drv3_066_buy_count_63d_d2_ewm_dev(insider_buy_count: pd.Series) -> pd.Series:
    """Deviation of 2nd-deriv [63d diff of 63d buy count] from its EWM (span=63)."""
    d2 = _d2_buy_count_63d(insider_buy_count)
    return d2 - _ewm_mean(d2, _TD_QTR)


def ibc_drv3_067_active_days_21d_d2_slope_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 2nd-deriv [21d diff of 21d active-buy-days] over 252-day window."""
    d2 = _d2_active_days_21d(insider_buy_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_068_active_days_63d_d2_slope_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 2nd-deriv [63d diff of 63d active-buy-days] over 252-day window."""
    d2 = _d2_active_days_63d(insider_buy_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_069_buyers_21d_d2_rank_in_504d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-deriv [21d diff of 21d buyer count] in trailing 504-day window."""
    d2 = _d2_buyers_21d(insider_buyers)
    return _rolling_rank_pct(d2, _TD_2Y)


def ibc_drv3_070_buy_count_21d_d2_rank_in_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-deriv [21d diff of 21d buy count] in trailing 504-day window."""
    d2 = _d2_buy_count_21d(insider_buy_count)
    return _rolling_rank_pct(d2, _TD_2Y)


def ibc_drv3_071_buyers_63d_d2_rank_in_504d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-deriv [63d diff of 63d buyer count] in trailing 504-day window."""
    d2 = _d2_buyers_63d(insider_buyers)
    return _rolling_rank_pct(d2, _TD_2Y)


def ibc_drv3_072_buyer_zscore_21d_d2_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """3rd deriv: 21d diff of [21d diff of (21d buyer z-score)]; jerk of buyer z-score."""
    d2 = _d2_buyer_zscore_21d(insider_buyers)
    return d2 - d2.shift(_TD_MO)


def ibc_drv3_073_buyer_zscore_63d_d2_63d_diff_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score (252d) of the 2nd-deriv [63d diff of 63d buyer z-score]."""
    d2 = _d2_buyer_zscore_63d(insider_buyers)
    return _zscore_rolling(d2, _TD_YEAR)


def ibc_drv3_074_buyers_21d_d3_slope_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of [21d diff of [21d diff of [21d diff of 21d buyer count]]] over 252-day window."""
    b21 = _buyers_21d(insider_buyers)
    d1  = b21 - b21.shift(_TD_MO)
    d2  = d1  - d1.shift(_TD_MO)
    d3  = d2  - d2.shift(_TD_MO)
    return d3.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv3_075_buyers_21d_d2_composite_signal(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Composite 3rd-deriv signal: sum of [d2_buyers_21d > 0] + [d2_buy_count_21d > 0] + [d2_active_days_21d > 0]."""
    d2b = _d2_buyers_21d(insider_buyers)
    d2c = _d2_buy_count_21d(insider_buy_count)
    d2a = _d2_active_days_21d(insider_buy_count)
    return ((d2b > 0).astype(float) + (d2c > 0).astype(float) + (d2a > 0).astype(float))


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

INSIDER_BUY_CLUSTER_REGISTRY_3RD_DERIVATIVES = {
    "ibc_drv3_001_buyers_21d_d2_21d_diff":          {"inputs": ["insider_buyers"],       "func": ibc_drv3_001_buyers_21d_d2_21d_diff},
    "ibc_drv3_002_buyers_63d_d2_63d_diff":          {"inputs": ["insider_buyers"],       "func": ibc_drv3_002_buyers_63d_d2_63d_diff},
    "ibc_drv3_003_buy_count_21d_d2_21d_diff":       {"inputs": ["insider_buy_count"],    "func": ibc_drv3_003_buy_count_21d_d2_21d_diff},
    "ibc_drv3_004_buy_count_63d_d2_63d_diff":       {"inputs": ["insider_buy_count"],    "func": ibc_drv3_004_buy_count_63d_d2_63d_diff},
    "ibc_drv3_005_active_days_21d_d2_21d_diff":     {"inputs": ["insider_buy_count"],    "func": ibc_drv3_005_active_days_21d_d2_21d_diff},
    "ibc_drv3_006_active_days_63d_d2_63d_diff":     {"inputs": ["insider_buy_count"],    "func": ibc_drv3_006_active_days_63d_d2_63d_diff},
    "ibc_drv3_007_buyer_zscore_21d_d2_21d_diff":    {"inputs": ["insider_buyers"],       "func": ibc_drv3_007_buyer_zscore_21d_d2_21d_diff},
    "ibc_drv3_008_buyer_zscore_63d_d2_63d_diff":    {"inputs": ["insider_buyers"],       "func": ibc_drv3_008_buyer_zscore_63d_d2_63d_diff},
    "ibc_drv3_009_officer_63d_d2_63d_diff":         {"inputs": ["officer_buy_count"],    "func": ibc_drv3_009_officer_63d_d2_63d_diff},
    "ibc_drv3_010_director_63d_d2_63d_diff":        {"inputs": ["director_buy_count"],   "func": ibc_drv3_010_director_63d_d2_63d_diff},
    "ibc_drv3_011_buyers_21d_d2_slope_in_252d":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_011_buyers_21d_d2_slope_in_252d},
    "ibc_drv3_012_buy_count_21d_d2_slope_in_252d":  {"inputs": ["insider_buy_count"],    "func": ibc_drv3_012_buy_count_21d_d2_slope_in_252d},
    "ibc_drv3_013_buyers_63d_d2_slope_in_252d":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_013_buyers_63d_d2_slope_in_252d},
    "ibc_drv3_014_buyers_21d_d2_zscore_in_252d":    {"inputs": ["insider_buyers"],       "func": ibc_drv3_014_buyers_21d_d2_zscore_in_252d},
    "ibc_drv3_015_buy_count_21d_d2_zscore_in_252d": {"inputs": ["insider_buy_count"],    "func": ibc_drv3_015_buy_count_21d_d2_zscore_in_252d},
    "ibc_drv3_016_buyers_21d_d2_rank_in_252d":      {"inputs": ["insider_buyers"],       "func": ibc_drv3_016_buyers_21d_d2_rank_in_252d},
    "ibc_drv3_017_buy_count_63d_d2_rank_in_252d":   {"inputs": ["insider_buy_count"],    "func": ibc_drv3_017_buy_count_63d_d2_rank_in_252d},
    "ibc_drv3_018_buyers_21d_d2_ewm_dev":           {"inputs": ["insider_buyers"],       "func": ibc_drv3_018_buyers_21d_d2_ewm_dev},
    "ibc_drv3_019_buy_count_21d_d2_ewm_dev":        {"inputs": ["insider_buy_count"],    "func": ibc_drv3_019_buy_count_21d_d2_ewm_dev},
    "ibc_drv3_020_buyers_21d_d2_positive_flag":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_020_buyers_21d_d2_positive_flag},
    "ibc_drv3_021_buy_count_21d_d2_positive_flag":  {"inputs": ["insider_buy_count"],    "func": ibc_drv3_021_buy_count_21d_d2_positive_flag},
    "ibc_drv3_022_buyers_63d_d2_positive_flag":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_022_buyers_63d_d2_positive_flag},
    "ibc_drv3_023_buyers_21d_d3_21d_diff":          {"inputs": ["insider_buyers"],       "func": ibc_drv3_023_buyers_21d_d3_21d_diff},
    "ibc_drv3_024_buy_count_21d_d3_21d_diff":       {"inputs": ["insider_buy_count"],    "func": ibc_drv3_024_buy_count_21d_d3_21d_diff},
    "ibc_drv3_025_buyers_21d_d2_52w_high_flag":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_025_buyers_21d_d2_52w_high_flag},
    # --- New 3rd-derivative features 026-075 ---
    "ibc_drv3_026_buyers_126d_d2_63d_diff":         {"inputs": ["insider_buyers"],       "func": ibc_drv3_026_buyers_126d_d2_63d_diff},
    "ibc_drv3_027_buy_count_126d_d2_63d_diff":      {"inputs": ["insider_buy_count"],    "func": ibc_drv3_027_buy_count_126d_d2_63d_diff},
    "ibc_drv3_028_active_days_126d_d2_63d_diff":    {"inputs": ["insider_buy_count"],    "func": ibc_drv3_028_active_days_126d_d2_63d_diff},
    "ibc_drv3_029_officer_21d_d2_21d_diff":         {"inputs": ["officer_buy_count"],    "func": ibc_drv3_029_officer_21d_d2_21d_diff},
    "ibc_drv3_030_director_21d_d2_21d_diff":        {"inputs": ["director_buy_count"],   "func": ibc_drv3_030_director_21d_d2_21d_diff},
    "ibc_drv3_031_buy_day_density_21d_d2_21d_diff": {"inputs": ["insider_buy_count"],    "func": ibc_drv3_031_buy_day_density_21d_d2_21d_diff},
    "ibc_drv3_032_buy_day_density_63d_d2_63d_diff": {"inputs": ["insider_buy_count"],    "func": ibc_drv3_032_buy_day_density_63d_d2_63d_diff},
    "ibc_drv3_033_multi_buyer_days_21d_d2_21d_diff": {"inputs": ["insider_buyers"],      "func": ibc_drv3_033_multi_buyer_days_21d_d2_21d_diff},
    "ibc_drv3_034_multi_buyer_days_63d_d2_63d_diff": {"inputs": ["insider_buyers"],      "func": ibc_drv3_034_multi_buyer_days_63d_d2_63d_diff},
    "ibc_drv3_035_buyers_ewm_cross_d2_21d_diff":    {"inputs": ["insider_buyers"],       "func": ibc_drv3_035_buyers_ewm_cross_d2_21d_diff},
    "ibc_drv3_036_buyers_21d_d2_slope_in_63d":      {"inputs": ["insider_buyers"],       "func": ibc_drv3_036_buyers_21d_d2_slope_in_63d},
    "ibc_drv3_037_buy_count_21d_d2_slope_in_63d":   {"inputs": ["insider_buy_count"],    "func": ibc_drv3_037_buy_count_21d_d2_slope_in_63d},
    "ibc_drv3_038_buyers_63d_d2_slope_in_63d":      {"inputs": ["insider_buyers"],       "func": ibc_drv3_038_buyers_63d_d2_slope_in_63d},
    "ibc_drv3_039_buyers_21d_d2_zscore_in_63d":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_039_buyers_21d_d2_zscore_in_63d},
    "ibc_drv3_040_buy_count_21d_d2_zscore_in_63d":  {"inputs": ["insider_buy_count"],    "func": ibc_drv3_040_buy_count_21d_d2_zscore_in_63d},
    "ibc_drv3_041_buyers_63d_d2_zscore_in_252d":    {"inputs": ["insider_buyers"],       "func": ibc_drv3_041_buyers_63d_d2_zscore_in_252d},
    "ibc_drv3_042_buy_count_63d_d2_zscore_in_252d": {"inputs": ["insider_buy_count"],    "func": ibc_drv3_042_buy_count_63d_d2_zscore_in_252d},
    "ibc_drv3_043_buyers_21d_d2_rank_in_63d":       {"inputs": ["insider_buyers"],       "func": ibc_drv3_043_buyers_21d_d2_rank_in_63d},
    "ibc_drv3_044_buy_count_21d_d2_rank_in_63d":    {"inputs": ["insider_buy_count"],    "func": ibc_drv3_044_buy_count_21d_d2_rank_in_63d},
    "ibc_drv3_045_buyers_63d_d2_rank_in_252d":      {"inputs": ["insider_buyers"],       "func": ibc_drv3_045_buyers_63d_d2_rank_in_252d},
    "ibc_drv3_046_buyers_21d_d2_ewm_dev_21d_diff":  {"inputs": ["insider_buyers"],       "func": ibc_drv3_046_buyers_21d_d2_ewm_dev_21d_diff},
    "ibc_drv3_047_buy_count_21d_d2_ewm_dev_21d_diff": {"inputs": ["insider_buy_count"],  "func": ibc_drv3_047_buy_count_21d_d2_ewm_dev_21d_diff},
    "ibc_drv3_048_buyers_21d_d2_positive_streak":   {"inputs": ["insider_buyers"],       "func": ibc_drv3_048_buyers_21d_d2_positive_streak},
    "ibc_drv3_049_buy_count_21d_d2_positive_streak": {"inputs": ["insider_buy_count"],   "func": ibc_drv3_049_buy_count_21d_d2_positive_streak},
    "ibc_drv3_050_buyers_63d_d2_positive_flag":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_050_buyers_63d_d2_positive_flag},
    "ibc_drv3_051_buy_count_63d_d2_positive_flag":  {"inputs": ["insider_buy_count"],    "func": ibc_drv3_051_buy_count_63d_d2_positive_flag},
    "ibc_drv3_052_active_days_21d_d2_positive_flag": {"inputs": ["insider_buy_count"],   "func": ibc_drv3_052_active_days_21d_d2_positive_flag},
    "ibc_drv3_053_active_days_63d_d2_positive_flag": {"inputs": ["insider_buy_count"],   "func": ibc_drv3_053_active_days_63d_d2_positive_flag},
    "ibc_drv3_054_buyers_21d_d2_52w_low_flag":      {"inputs": ["insider_buyers"],       "func": ibc_drv3_054_buyers_21d_d2_52w_low_flag},
    "ibc_drv3_055_buy_count_21d_d2_52w_high_flag":  {"inputs": ["insider_buy_count"],    "func": ibc_drv3_055_buy_count_21d_d2_52w_high_flag},
    "ibc_drv3_056_buyers_21d_d3_63d_diff":          {"inputs": ["insider_buyers"],       "func": ibc_drv3_056_buyers_21d_d3_63d_diff},
    "ibc_drv3_057_buy_count_21d_d3_63d_diff":       {"inputs": ["insider_buy_count"],    "func": ibc_drv3_057_buy_count_21d_d3_63d_diff},
    "ibc_drv3_058_buyers_63d_d3_63d_diff":          {"inputs": ["insider_buyers"],       "func": ibc_drv3_058_buyers_63d_d3_63d_diff},
    "ibc_drv3_059_buy_count_63d_d3_63d_diff":       {"inputs": ["insider_buy_count"],    "func": ibc_drv3_059_buy_count_63d_d3_63d_diff},
    "ibc_drv3_060_officer_63d_d2_21d_diff":         {"inputs": ["officer_buy_count"],    "func": ibc_drv3_060_officer_63d_d2_21d_diff},
    "ibc_drv3_061_director_63d_d2_21d_diff":        {"inputs": ["director_buy_count"],   "func": ibc_drv3_061_director_63d_d2_21d_diff},
    "ibc_drv3_062_buyers_21d_d2_rolling_max_63d":   {"inputs": ["insider_buyers"],       "func": ibc_drv3_062_buyers_21d_d2_rolling_max_63d},
    "ibc_drv3_063_buy_count_21d_d2_rolling_max_63d": {"inputs": ["insider_buy_count"],   "func": ibc_drv3_063_buy_count_21d_d2_rolling_max_63d},
    "ibc_drv3_064_buyers_21d_d2_slope_in_504d":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_064_buyers_21d_d2_slope_in_504d},
    "ibc_drv3_065_buyers_63d_d2_ewm_dev":           {"inputs": ["insider_buyers"],       "func": ibc_drv3_065_buyers_63d_d2_ewm_dev},
    "ibc_drv3_066_buy_count_63d_d2_ewm_dev":        {"inputs": ["insider_buy_count"],    "func": ibc_drv3_066_buy_count_63d_d2_ewm_dev},
    "ibc_drv3_067_active_days_21d_d2_slope_in_252d": {"inputs": ["insider_buy_count"],   "func": ibc_drv3_067_active_days_21d_d2_slope_in_252d},
    "ibc_drv3_068_active_days_63d_d2_slope_in_252d": {"inputs": ["insider_buy_count"],   "func": ibc_drv3_068_active_days_63d_d2_slope_in_252d},
    "ibc_drv3_069_buyers_21d_d2_rank_in_504d":      {"inputs": ["insider_buyers"],       "func": ibc_drv3_069_buyers_21d_d2_rank_in_504d},
    "ibc_drv3_070_buy_count_21d_d2_rank_in_504d":   {"inputs": ["insider_buy_count"],    "func": ibc_drv3_070_buy_count_21d_d2_rank_in_504d},
    "ibc_drv3_071_buyers_63d_d2_rank_in_504d":      {"inputs": ["insider_buyers"],       "func": ibc_drv3_071_buyers_63d_d2_rank_in_504d},
    "ibc_drv3_072_buyer_zscore_21d_d2_21d_diff":    {"inputs": ["insider_buyers"],       "func": ibc_drv3_072_buyer_zscore_21d_d2_21d_diff},
    "ibc_drv3_073_buyer_zscore_63d_d2_63d_diff_in_252d": {"inputs": ["insider_buyers"],  "func": ibc_drv3_073_buyer_zscore_63d_d2_63d_diff_in_252d},
    "ibc_drv3_074_buyers_21d_d3_slope_in_252d":     {"inputs": ["insider_buyers"],       "func": ibc_drv3_074_buyers_21d_d3_slope_in_252d},
    "ibc_drv3_075_buyers_21d_d2_composite_signal":  {"inputs": ["insider_buyers", "insider_buy_count"], "func": ibc_drv3_075_buyers_21d_d2_composite_signal},
}
