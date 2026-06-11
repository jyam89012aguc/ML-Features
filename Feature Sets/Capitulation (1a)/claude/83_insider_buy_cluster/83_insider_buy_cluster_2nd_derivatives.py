"""
83_insider_buy_cluster — 2nd-Derivative Features 001-075
Domain: rate of change of base insider buy-cluster features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction filings to one row per (ticker, date).  These are EVENT-DRIVEN
flow series: most days are ZERO (no insider transaction filed); positive values
appear only on filing days.  Do NOT forward-fill.

2nd-Derivative Note
--------------------
The underlying SF2 series are sparse (mostly zero); the 2nd-derivative features
computed by differencing rolling-window aggregates will therefore be very sparse
on a daily index.  This is correct and expected.  All derivations look strictly
backward using .shift(positive), .rolling(), or .expanding().

Canonical SF2 field names used in this file (lowercase):
    insider_buy_count, insider_buyers, officer_buy_count,
    director_buy_count, tenpct_buy_count

Feature numbering: ibc_drv2_001 .. ibc_drv2_075
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


# ── Base concept helpers (self-contained recomputes, no cross-file imports) ───

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


def _buy_day_density_63d(insider_buy_count: pd.Series) -> pd.Series:
    return _safe_div(_active_days(insider_buy_count, _TD_QTR),
                     pd.Series(float(_TD_QTR), index=insider_buy_count.index))


def _buyer_zscore_63d(insider_buyers: pd.Series) -> pd.Series:
    return _zscore_rolling(_buyers_63d(insider_buyers), _TD_YEAR)


def _buyer_zscore_21d(insider_buyers: pd.Series) -> pd.Series:
    return _zscore_rolling(_buyers_21d(insider_buyers), _TD_YEAR)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def ibc_drv2_001_buyers_21d_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """21-day difference of the 21-day distinct-buyer count (QoM change in buyers)."""
    base = _buyers_21d(insider_buyers)
    return base - base.shift(_TD_MO)


def ibc_drv2_002_buyers_63d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the 63-day distinct-buyer count (QoQ change in buyers)."""
    base = _buyers_63d(insider_buyers)
    return base - base.shift(_TD_QTR)


def ibc_drv2_003_buyers_21d_252d_diff(insider_buyers: pd.Series) -> pd.Series:
    """252-day (annual) difference of the 21-day buyer count."""
    base = _buyers_21d(insider_buyers)
    return base - base.shift(_TD_YEAR)


def ibc_drv2_004_buy_count_21d_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 21-day buy-transaction count."""
    base = _buy_count_21d(insider_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_005_buy_count_63d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 63-day buy-transaction count."""
    base = _buy_count_63d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_006_active_days_21d_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 21-day active-buy-day count."""
    base = _active_days_21d(insider_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_007_active_days_63d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 63-day active-buy-day count."""
    base = _active_days_63d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_008_buy_day_density_63d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 63-day buy-day density (fraction of active days)."""
    base = _buy_day_density_63d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_009_buyer_zscore_21d_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """21-day change in the 21-day buyer z-score (acceleration of buyer-burst signal)."""
    base = _buyer_zscore_21d(insider_buyers)
    return base - base.shift(_TD_MO)


def ibc_drv2_010_buyer_zscore_63d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day change in the 63-day buyer z-score."""
    base = _buyer_zscore_63d(insider_buyers)
    return base - base.shift(_TD_QTR)


def ibc_drv2_011_officer_63d_63d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """63-day change in the 63-day officer buy count."""
    base = _officer_63d(officer_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_012_director_63d_63d_diff(director_buy_count: pd.Series) -> pd.Series:
    """63-day change in the 63-day director buy count."""
    base = _director_63d(director_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_013_buyers_21d_pct_chg_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """
    Change in the 21-day buyer count's period-over-period percent change:
    diff_of[(b21 - b21_prior) / b21_prior].
    """
    b21   = _buyers_21d(insider_buyers)
    prior = b21.shift(_TD_MO).replace(0, np.nan)
    pct   = (b21 - prior) / prior
    return pct - pct.shift(_TD_MO)


def ibc_drv2_014_buyers_63d_pct_chg_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """Change in the 63-day buyer count's period-over-period percent change."""
    b63   = _buyers_63d(insider_buyers)
    prior = b63.shift(_TD_QTR).replace(0, np.nan)
    pct   = (b63 - prior) / prior
    return pct - pct.shift(_TD_QTR)


def ibc_drv2_015_buy_count_63d_pct_chg_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """Change in the 63-day buy-transaction count's period percent change."""
    b63   = _buy_count_63d(insider_buy_count)
    prior = b63.shift(_TD_QTR).replace(0, np.nan)
    pct   = (b63 - prior) / prior
    return pct - pct.shift(_TD_QTR)


def ibc_drv2_016_buyers_21d_slope_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """
    OLS slope of the 21-day rolling buyer count over a trailing 252-day window.
    Captures the trend in short-window buying breadth over the past year.
    """
    b21 = _buyers_21d(insider_buyers)
    return b21.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_017_buy_count_21d_slope_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 21-day rolling buy-transaction count over a 252-day window."""
    b21 = _buy_count_21d(insider_buy_count)
    return b21.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_018_active_days_63d_slope_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 63-day active-buy-day count over a 252-day window."""
    a63 = _active_days_63d(insider_buy_count)
    return a63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_019_buyers_21d_ewm_vs_diff(insider_buyers: pd.Series) -> pd.Series:
    """
    21-day buyer count minus its EWM (span=63) — then 21d diff of that deviation.
    Captures acceleration of the deviation from the medium-term EWM trend.
    """
    b21  = _buyers_21d(insider_buyers)
    dev  = b21 - _ewm_mean(b21, _TD_QTR)
    return dev - dev.shift(_TD_MO)


def ibc_drv2_020_buy_count_ewm_cross_21_63_diff(insider_buy_count: pd.Series) -> pd.Series:
    """
    21-day difference of (EWM_21 - EWM_63) for buy-transaction counts.
    Captures acceleration of the fast-vs-slow EWM crossover.
    """
    cross = _ewm_mean(insider_buy_count, _TD_MO) - _ewm_mean(insider_buy_count, _TD_QTR)
    return cross - cross.shift(_TD_MO)


def ibc_drv2_021_buyers_63d_252d_diff(insider_buyers: pd.Series) -> pd.Series:
    """252-day (annual) difference of the 63-day distinct-buyer count."""
    base = _buyers_63d(insider_buyers)
    return base - base.shift(_TD_YEAR)


def ibc_drv2_022_officers_63d_252d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """252-day difference of the 63-day officer buy count."""
    base = _officer_63d(officer_buy_count)
    return base - base.shift(_TD_YEAR)


def ibc_drv2_023_buyer_zscore_63d_252d_diff(insider_buyers: pd.Series) -> pd.Series:
    """252-day difference of the 63-day buyer z-score."""
    base = _buyer_zscore_63d(insider_buyers)
    return base - base.shift(_TD_YEAR)


def ibc_drv2_024_buyers_21d_second_diff(insider_buyers: pd.Series) -> pd.Series:
    """
    Second difference of the 21-day buyer count (21-day step):
    [b21(t) - b21(t-21)] - [b21(t-21) - b21(t-42)] = b21(t) - 2*b21(t-21) + b21(t-42).
    Captures acceleration (convexity) of buying breadth momentum.
    """
    b21 = _buyers_21d(insider_buyers)
    d1  = b21 - b21.shift(_TD_MO)
    return d1 - d1.shift(_TD_MO)


def ibc_drv2_025_buy_count_21d_second_diff(insider_buy_count: pd.Series) -> pd.Series:
    """
    Second difference of the 21-day buy-transaction count (21-day step).
    Captures acceleration of buy-transaction momentum.
    """
    b21 = _buy_count_21d(insider_buy_count)
    d1  = b21 - b21.shift(_TD_MO)
    return d1 - d1.shift(_TD_MO)


# ── Additional base helpers for new 2nd-derivative features ──────────────────

def _buyers_126d(insider_buyers: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buyers, _TD_2Q)


def _buyers_252d(insider_buyers: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buyers, _TD_YEAR)


def _buy_count_126d(insider_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_count, _TD_2Q)


def _buy_count_252d(insider_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(insider_buy_count, _TD_YEAR)


def _active_days_126d(insider_buy_count: pd.Series) -> pd.Series:
    return _active_days(insider_buy_count, _TD_2Q)


def _active_days_252d(insider_buy_count: pd.Series) -> pd.Series:
    return _active_days(insider_buy_count, _TD_YEAR)


def _officer_21d(officer_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_count, _TD_MO)


def _officer_126d(officer_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_count, _TD_2Q)


def _director_21d(director_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_count, _TD_MO)


def _director_126d(director_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_count, _TD_2Q)


def _tenpct_63d(tenpct_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(tenpct_buy_count, _TD_QTR)


def _buy_day_density_21d(insider_buy_count: pd.Series) -> pd.Series:
    return _safe_div(_active_days(insider_buy_count, _TD_MO),
                     pd.Series(float(_TD_MO), index=insider_buy_count.index))


def _buy_day_density_252d(insider_buy_count: pd.Series) -> pd.Series:
    return _safe_div(_active_days(insider_buy_count, _TD_YEAR),
                     pd.Series(float(_TD_YEAR), index=insider_buy_count.index))


def _buyer_zscore_126d(insider_buyers: pd.Series) -> pd.Series:
    return _zscore_rolling(_buyers_126d(insider_buyers), _TD_2Y)


def _multi_buyer_days_21d(insider_buyers: pd.Series) -> pd.Series:
    return _rolling_sum((insider_buyers >= 2).astype(float), _TD_MO)


def _multi_buyer_days_63d(insider_buyers: pd.Series) -> pd.Series:
    return _rolling_sum((insider_buyers >= 2).astype(float), _TD_QTR)


def _ewm_buyers_21(insider_buyers: pd.Series) -> pd.Series:
    return _ewm_mean(insider_buyers, _TD_MO)


def _ewm_buyers_63(insider_buyers: pd.Series) -> pd.Series:
    return _ewm_mean(insider_buyers, _TD_QTR)


def _buyers_ewm_cross(insider_buyers: pd.Series) -> pd.Series:
    return _ewm_buyers_21(insider_buyers) - _ewm_buyers_63(insider_buyers)


# ── 2nd-Derivative Feature Functions (026-075) ────────────────────────────────

def ibc_drv2_026_buyers_126d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the 126-day distinct-buyer count."""
    base = _buyers_126d(insider_buyers)
    return base - base.shift(_TD_QTR)


def ibc_drv2_027_buy_count_126d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 126-day buy-transaction count."""
    base = _buy_count_126d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_028_buyers_252d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the 252-day distinct-buyer count."""
    base = _buyers_252d(insider_buyers)
    return base - base.shift(_TD_QTR)


def ibc_drv2_029_buy_count_252d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 252-day buy-transaction count."""
    base = _buy_count_252d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_030_active_days_126d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 126-day active-buy-day count."""
    base = _active_days_126d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_031_active_days_252d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 252-day active-buy-day count."""
    base = _active_days_252d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_032_officer_21d_21d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 21-day officer buy count."""
    base = _officer_21d(officer_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_033_director_21d_21d_diff(director_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 21-day director buy count."""
    base = _director_21d(director_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_034_tenpct_63d_63d_diff(tenpct_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 63-day 10%-holder buy count."""
    base = _tenpct_63d(tenpct_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_035_officer_126d_63d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 126-day officer buy count."""
    base = _officer_126d(officer_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_036_director_126d_63d_diff(director_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 126-day director buy count."""
    base = _director_126d(director_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_037_buy_day_density_21d_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 21-day buy-day density."""
    base = _buy_day_density_21d(insider_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_038_buy_day_density_252d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 252-day buy-day density."""
    base = _buy_day_density_252d(insider_buy_count)
    return base - base.shift(_TD_QTR)


def ibc_drv2_039_buyer_zscore_126d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the 126-day buyer z-score (vs 504-day distribution)."""
    base = _buyer_zscore_126d(insider_buyers)
    return base - base.shift(_TD_QTR)


def ibc_drv2_040_buyers_21d_5d_diff(insider_buyers: pd.Series) -> pd.Series:
    """5-day difference of the 21-day distinct-buyer count (weekly change in monthly buyers)."""
    base = _buyers_21d(insider_buyers)
    return base - base.shift(_TD_WK)


def ibc_drv2_041_buy_count_21d_5d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """5-day difference of the 21-day buy-transaction count."""
    base = _buy_count_21d(insider_buy_count)
    return base - base.shift(_TD_WK)


def ibc_drv2_042_buyers_63d_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """21-day difference of the 63-day distinct-buyer count."""
    base = _buyers_63d(insider_buyers)
    return base - base.shift(_TD_MO)


def ibc_drv2_043_buy_count_63d_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 63-day buy-transaction count."""
    base = _buy_count_63d(insider_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_044_multi_buyer_days_21d_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """21-day difference of the count of multi-buyer days (>=2 buyers) in 21d."""
    base = _multi_buyer_days_21d(insider_buyers)
    return base - base.shift(_TD_MO)


def ibc_drv2_045_multi_buyer_days_63d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the count of multi-buyer days (>=2 buyers) in 63d."""
    base = _multi_buyer_days_63d(insider_buyers)
    return base - base.shift(_TD_QTR)


def ibc_drv2_046_buyers_ewm_cross_21_63_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of (EWM_21 - EWM_63) distinct-buyer cross signal."""
    cross = _buyers_ewm_cross(insider_buyers)
    return cross - cross.shift(_TD_QTR)


def ibc_drv2_047_buyers_21d_slope_in_63d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of the 21-day rolling buyer count over a trailing 63-day window."""
    b21 = _buyers_21d(insider_buyers)
    return b21.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_048_buy_count_63d_slope_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 63-day rolling buy-transaction count over a 252-day window."""
    b63 = _buy_count_63d(insider_buy_count)
    return b63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_049_active_days_21d_slope_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 21-day active-buy-day count over a 252-day window."""
    a21 = _active_days_21d(insider_buy_count)
    return a21.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_050_officer_63d_slope_in_252d(officer_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 63-day officer buy count over a 252-day window."""
    o63 = _officer_63d(officer_buy_count)
    return o63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_051_director_63d_slope_in_252d(director_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 63-day director buy count over a 252-day window."""
    d63 = _director_63d(director_buy_count)
    return d63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_052_buyers_21d_zscore_in_252d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the z-score of the 21-day buyer count (in 252d window)."""
    z = _zscore_rolling(_buyers_21d(insider_buyers), _TD_YEAR)
    return z - z.shift(_TD_QTR)


def ibc_drv2_053_buy_count_21d_zscore_in_252d_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the z-score of the 21-day buy-transaction count (in 252d window)."""
    z = _zscore_rolling(_buy_count_21d(insider_buy_count), _TD_YEAR)
    return z - z.shift(_TD_MO)


def ibc_drv2_054_buyers_63d_rank_in_252d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the 252-day percentile rank of the 63-day buyer count."""
    r = _rolling_rank_pct(_buyers_63d(insider_buyers), _TD_YEAR)
    return r - r.shift(_TD_QTR)


def ibc_drv2_055_buy_count_63d_rank_in_504d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the 504-day percentile rank of the 63-day buy count."""
    r = _rolling_rank_pct(_buy_count_63d(insider_buy_count), _TD_2Y)
    return r - r.shift(_TD_QTR)


def ibc_drv2_056_buyers_21d_ewm_dev_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of (21d buyer count minus its EWM span=63) deviation."""
    b21 = _buyers_21d(insider_buyers)
    dev = b21 - _ewm_mean(b21, _TD_QTR)
    return dev - dev.shift(_TD_QTR)


def ibc_drv2_057_buy_count_ewm21_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of EWM (span=21) of daily buy-transaction counts."""
    ewm = _ewm_mean(insider_buy_count, _TD_MO)
    return ewm - ewm.shift(_TD_MO)


def ibc_drv2_058_buyers_ewm63_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of EWM (span=63) of daily distinct-buyer counts."""
    ewm = _ewm_mean(insider_buyers, _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def ibc_drv2_059_buyers_252d_252d_diff(insider_buyers: pd.Series) -> pd.Series:
    """252-day difference of the 252-day distinct-buyer count."""
    base = _buyers_252d(insider_buyers)
    return base - base.shift(_TD_YEAR)


def ibc_drv2_060_buy_count_252d_252d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """252-day difference of the 252-day buy-transaction count."""
    base = _buy_count_252d(insider_buy_count)
    return base - base.shift(_TD_YEAR)


def ibc_drv2_061_officer_63d_21d_diff(officer_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 63-day officer buy count."""
    base = _officer_63d(officer_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_062_director_63d_21d_diff(director_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 63-day director buy count."""
    base = _director_63d(director_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_063_buyers_63d_second_diff(insider_buyers: pd.Series) -> pd.Series:
    """Second difference (63d step) of the 63-day buyer count: b63(t) - 2*b63(t-63) + b63(t-126)."""
    b63 = _buyers_63d(insider_buyers)
    d1  = b63 - b63.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ibc_drv2_064_buy_count_63d_second_diff(insider_buy_count: pd.Series) -> pd.Series:
    """Second difference (63d step) of the 63-day buy-transaction count."""
    b63 = _buy_count_63d(insider_buy_count)
    d1  = b63 - b63.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ibc_drv2_065_active_days_21d_5d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """5-day difference of the 21-day active-buy-day count."""
    base = _active_days_21d(insider_buy_count)
    return base - base.shift(_TD_WK)


def ibc_drv2_066_active_days_63d_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 63-day active-buy-day count."""
    base = _active_days_63d(insider_buy_count)
    return base - base.shift(_TD_MO)


def ibc_drv2_067_buyers_21d_slope_in_504d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of the 21-day rolling buyer count over a trailing 504-day window."""
    b21 = _buyers_21d(insider_buyers)
    return b21.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).apply(
        _ols_slope, raw=True)


def ibc_drv2_068_buy_count_21d_rank_in_252d_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 252-day percentile rank of the 21-day buy count."""
    r = _rolling_rank_pct(_buy_count_21d(insider_buy_count), _TD_YEAR)
    return r - r.shift(_TD_MO)


def ibc_drv2_069_buyers_21d_pct_chg_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day difference of the 21-day buyer count's period-over-period percent change."""
    b21   = _buyers_21d(insider_buyers)
    prior = b21.shift(_TD_MO).replace(0, np.nan)
    pct   = (b21 - prior) / prior
    return pct - pct.shift(_TD_QTR)


def ibc_drv2_070_buy_count_63d_pct_chg_21d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """21-day difference of the 63-day buy count's period-over-period percent change."""
    b63   = _buy_count_63d(insider_buy_count)
    prior = b63.shift(_TD_QTR).replace(0, np.nan)
    pct   = (b63 - prior) / prior
    return pct - pct.shift(_TD_MO)


def ibc_drv2_071_buyers_21d_ewm_vs_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day diff of (21d buyer count minus EWM span=63): captures change in momentum deviation."""
    b21 = _buyers_21d(insider_buyers)
    dev = b21 - _ewm_mean(b21, _TD_QTR)
    return dev - dev.shift(_TD_QTR)


def ibc_drv2_072_buyers_ewm_cross_21_63_21d_diff(insider_buyers: pd.Series) -> pd.Series:
    """21-day difference of (EWM_21 - EWM_63) distinct-buyer cross signal."""
    cross = _buyers_ewm_cross(insider_buyers)
    return cross - cross.shift(_TD_MO)


def ibc_drv2_073_buyer_zscore_21d_63d_diff(insider_buyers: pd.Series) -> pd.Series:
    """63-day change in the 21-day buyer z-score (longer horizon acceleration)."""
    base = _buyer_zscore_21d(insider_buyers)
    return base - base.shift(_TD_QTR)


def ibc_drv2_074_buy_count_63d_zscore_in_252d_63d_diff(insider_buy_count: pd.Series) -> pd.Series:
    """63-day difference of the z-score of the 63-day buy count (in 252d window)."""
    z = _zscore_rolling(_buy_count_63d(insider_buy_count), _TD_YEAR)
    return z - z.shift(_TD_QTR)


def ibc_drv2_075_buyers_21d_second_diff_63d_window(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of [21d diff of 21d buyer count] over trailing 63-day window; rate-of-change of momentum slope."""
    b21 = _buyers_21d(insider_buyers)
    d1  = b21 - b21.shift(_TD_MO)
    return d1.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

INSIDER_BUY_CLUSTER_REGISTRY_2ND_DERIVATIVES = {
    "ibc_drv2_001_buyers_21d_21d_diff":              {"inputs": ["insider_buyers"],       "func": ibc_drv2_001_buyers_21d_21d_diff},
    "ibc_drv2_002_buyers_63d_63d_diff":              {"inputs": ["insider_buyers"],       "func": ibc_drv2_002_buyers_63d_63d_diff},
    "ibc_drv2_003_buyers_21d_252d_diff":             {"inputs": ["insider_buyers"],       "func": ibc_drv2_003_buyers_21d_252d_diff},
    "ibc_drv2_004_buy_count_21d_21d_diff":           {"inputs": ["insider_buy_count"],    "func": ibc_drv2_004_buy_count_21d_21d_diff},
    "ibc_drv2_005_buy_count_63d_63d_diff":           {"inputs": ["insider_buy_count"],    "func": ibc_drv2_005_buy_count_63d_63d_diff},
    "ibc_drv2_006_active_days_21d_21d_diff":         {"inputs": ["insider_buy_count"],    "func": ibc_drv2_006_active_days_21d_21d_diff},
    "ibc_drv2_007_active_days_63d_63d_diff":         {"inputs": ["insider_buy_count"],    "func": ibc_drv2_007_active_days_63d_63d_diff},
    "ibc_drv2_008_buy_day_density_63d_63d_diff":     {"inputs": ["insider_buy_count"],    "func": ibc_drv2_008_buy_day_density_63d_63d_diff},
    "ibc_drv2_009_buyer_zscore_21d_21d_diff":        {"inputs": ["insider_buyers"],       "func": ibc_drv2_009_buyer_zscore_21d_21d_diff},
    "ibc_drv2_010_buyer_zscore_63d_63d_diff":        {"inputs": ["insider_buyers"],       "func": ibc_drv2_010_buyer_zscore_63d_63d_diff},
    "ibc_drv2_011_officer_63d_63d_diff":             {"inputs": ["officer_buy_count"],    "func": ibc_drv2_011_officer_63d_63d_diff},
    "ibc_drv2_012_director_63d_63d_diff":            {"inputs": ["director_buy_count"],   "func": ibc_drv2_012_director_63d_63d_diff},
    "ibc_drv2_013_buyers_21d_pct_chg_21d_diff":      {"inputs": ["insider_buyers"],       "func": ibc_drv2_013_buyers_21d_pct_chg_21d_diff},
    "ibc_drv2_014_buyers_63d_pct_chg_63d_diff":      {"inputs": ["insider_buyers"],       "func": ibc_drv2_014_buyers_63d_pct_chg_63d_diff},
    "ibc_drv2_015_buy_count_63d_pct_chg_63d_diff":   {"inputs": ["insider_buy_count"],    "func": ibc_drv2_015_buy_count_63d_pct_chg_63d_diff},
    "ibc_drv2_016_buyers_21d_slope_in_252d":         {"inputs": ["insider_buyers"],       "func": ibc_drv2_016_buyers_21d_slope_in_252d},
    "ibc_drv2_017_buy_count_21d_slope_in_252d":      {"inputs": ["insider_buy_count"],    "func": ibc_drv2_017_buy_count_21d_slope_in_252d},
    "ibc_drv2_018_active_days_63d_slope_in_252d":    {"inputs": ["insider_buy_count"],    "func": ibc_drv2_018_active_days_63d_slope_in_252d},
    "ibc_drv2_019_buyers_21d_ewm_vs_diff":           {"inputs": ["insider_buyers"],       "func": ibc_drv2_019_buyers_21d_ewm_vs_diff},
    "ibc_drv2_020_buy_count_ewm_cross_21_63_diff":   {"inputs": ["insider_buy_count"],    "func": ibc_drv2_020_buy_count_ewm_cross_21_63_diff},
    "ibc_drv2_021_buyers_63d_252d_diff":             {"inputs": ["insider_buyers"],       "func": ibc_drv2_021_buyers_63d_252d_diff},
    "ibc_drv2_022_officers_63d_252d_diff":           {"inputs": ["officer_buy_count"],    "func": ibc_drv2_022_officers_63d_252d_diff},
    "ibc_drv2_023_buyer_zscore_63d_252d_diff":       {"inputs": ["insider_buyers"],       "func": ibc_drv2_023_buyer_zscore_63d_252d_diff},
    "ibc_drv2_024_buyers_21d_second_diff":           {"inputs": ["insider_buyers"],       "func": ibc_drv2_024_buyers_21d_second_diff},
    "ibc_drv2_025_buy_count_21d_second_diff":        {"inputs": ["insider_buy_count"],    "func": ibc_drv2_025_buy_count_21d_second_diff},
    # --- New 2nd-derivative features 026-075 ---
    "ibc_drv2_026_buyers_126d_63d_diff":             {"inputs": ["insider_buyers"],       "func": ibc_drv2_026_buyers_126d_63d_diff},
    "ibc_drv2_027_buy_count_126d_63d_diff":          {"inputs": ["insider_buy_count"],    "func": ibc_drv2_027_buy_count_126d_63d_diff},
    "ibc_drv2_028_buyers_252d_63d_diff":             {"inputs": ["insider_buyers"],       "func": ibc_drv2_028_buyers_252d_63d_diff},
    "ibc_drv2_029_buy_count_252d_63d_diff":          {"inputs": ["insider_buy_count"],    "func": ibc_drv2_029_buy_count_252d_63d_diff},
    "ibc_drv2_030_active_days_126d_63d_diff":        {"inputs": ["insider_buy_count"],    "func": ibc_drv2_030_active_days_126d_63d_diff},
    "ibc_drv2_031_active_days_252d_63d_diff":        {"inputs": ["insider_buy_count"],    "func": ibc_drv2_031_active_days_252d_63d_diff},
    "ibc_drv2_032_officer_21d_21d_diff":             {"inputs": ["officer_buy_count"],    "func": ibc_drv2_032_officer_21d_21d_diff},
    "ibc_drv2_033_director_21d_21d_diff":            {"inputs": ["director_buy_count"],   "func": ibc_drv2_033_director_21d_21d_diff},
    "ibc_drv2_034_tenpct_63d_63d_diff":              {"inputs": ["tenpct_buy_count"],     "func": ibc_drv2_034_tenpct_63d_63d_diff},
    "ibc_drv2_035_officer_126d_63d_diff":            {"inputs": ["officer_buy_count"],    "func": ibc_drv2_035_officer_126d_63d_diff},
    "ibc_drv2_036_director_126d_63d_diff":           {"inputs": ["director_buy_count"],   "func": ibc_drv2_036_director_126d_63d_diff},
    "ibc_drv2_037_buy_day_density_21d_21d_diff":     {"inputs": ["insider_buy_count"],    "func": ibc_drv2_037_buy_day_density_21d_21d_diff},
    "ibc_drv2_038_buy_day_density_252d_63d_diff":    {"inputs": ["insider_buy_count"],    "func": ibc_drv2_038_buy_day_density_252d_63d_diff},
    "ibc_drv2_039_buyer_zscore_126d_63d_diff":       {"inputs": ["insider_buyers"],       "func": ibc_drv2_039_buyer_zscore_126d_63d_diff},
    "ibc_drv2_040_buyers_21d_5d_diff":               {"inputs": ["insider_buyers"],       "func": ibc_drv2_040_buyers_21d_5d_diff},
    "ibc_drv2_041_buy_count_21d_5d_diff":            {"inputs": ["insider_buy_count"],    "func": ibc_drv2_041_buy_count_21d_5d_diff},
    "ibc_drv2_042_buyers_63d_21d_diff":              {"inputs": ["insider_buyers"],       "func": ibc_drv2_042_buyers_63d_21d_diff},
    "ibc_drv2_043_buy_count_63d_21d_diff":           {"inputs": ["insider_buy_count"],    "func": ibc_drv2_043_buy_count_63d_21d_diff},
    "ibc_drv2_044_multi_buyer_days_21d_21d_diff":    {"inputs": ["insider_buyers"],       "func": ibc_drv2_044_multi_buyer_days_21d_21d_diff},
    "ibc_drv2_045_multi_buyer_days_63d_63d_diff":    {"inputs": ["insider_buyers"],       "func": ibc_drv2_045_multi_buyer_days_63d_63d_diff},
    "ibc_drv2_046_buyers_ewm_cross_21_63_63d_diff":  {"inputs": ["insider_buyers"],       "func": ibc_drv2_046_buyers_ewm_cross_21_63_63d_diff},
    "ibc_drv2_047_buyers_21d_slope_in_63d":          {"inputs": ["insider_buyers"],       "func": ibc_drv2_047_buyers_21d_slope_in_63d},
    "ibc_drv2_048_buy_count_63d_slope_in_252d":      {"inputs": ["insider_buy_count"],    "func": ibc_drv2_048_buy_count_63d_slope_in_252d},
    "ibc_drv2_049_active_days_21d_slope_in_252d":    {"inputs": ["insider_buy_count"],    "func": ibc_drv2_049_active_days_21d_slope_in_252d},
    "ibc_drv2_050_officer_63d_slope_in_252d":        {"inputs": ["officer_buy_count"],    "func": ibc_drv2_050_officer_63d_slope_in_252d},
    "ibc_drv2_051_director_63d_slope_in_252d":       {"inputs": ["director_buy_count"],   "func": ibc_drv2_051_director_63d_slope_in_252d},
    "ibc_drv2_052_buyers_21d_zscore_in_252d_63d_diff": {"inputs": ["insider_buyers"],     "func": ibc_drv2_052_buyers_21d_zscore_in_252d_63d_diff},
    "ibc_drv2_053_buy_count_21d_zscore_in_252d_21d_diff": {"inputs": ["insider_buy_count"], "func": ibc_drv2_053_buy_count_21d_zscore_in_252d_21d_diff},
    "ibc_drv2_054_buyers_63d_rank_in_252d_63d_diff": {"inputs": ["insider_buyers"],       "func": ibc_drv2_054_buyers_63d_rank_in_252d_63d_diff},
    "ibc_drv2_055_buy_count_63d_rank_in_504d_63d_diff": {"inputs": ["insider_buy_count"], "func": ibc_drv2_055_buy_count_63d_rank_in_504d_63d_diff},
    "ibc_drv2_056_buyers_21d_ewm_dev_63d_diff":      {"inputs": ["insider_buyers"],       "func": ibc_drv2_056_buyers_21d_ewm_dev_63d_diff},
    "ibc_drv2_057_buy_count_ewm21_21d_diff":         {"inputs": ["insider_buy_count"],    "func": ibc_drv2_057_buy_count_ewm21_21d_diff},
    "ibc_drv2_058_buyers_ewm63_63d_diff":            {"inputs": ["insider_buyers"],       "func": ibc_drv2_058_buyers_ewm63_63d_diff},
    "ibc_drv2_059_buyers_252d_252d_diff":            {"inputs": ["insider_buyers"],       "func": ibc_drv2_059_buyers_252d_252d_diff},
    "ibc_drv2_060_buy_count_252d_252d_diff":         {"inputs": ["insider_buy_count"],    "func": ibc_drv2_060_buy_count_252d_252d_diff},
    "ibc_drv2_061_officer_63d_21d_diff":             {"inputs": ["officer_buy_count"],    "func": ibc_drv2_061_officer_63d_21d_diff},
    "ibc_drv2_062_director_63d_21d_diff":            {"inputs": ["director_buy_count"],   "func": ibc_drv2_062_director_63d_21d_diff},
    "ibc_drv2_063_buyers_63d_second_diff":           {"inputs": ["insider_buyers"],       "func": ibc_drv2_063_buyers_63d_second_diff},
    "ibc_drv2_064_buy_count_63d_second_diff":        {"inputs": ["insider_buy_count"],    "func": ibc_drv2_064_buy_count_63d_second_diff},
    "ibc_drv2_065_active_days_21d_5d_diff":          {"inputs": ["insider_buy_count"],    "func": ibc_drv2_065_active_days_21d_5d_diff},
    "ibc_drv2_066_active_days_63d_21d_diff":         {"inputs": ["insider_buy_count"],    "func": ibc_drv2_066_active_days_63d_21d_diff},
    "ibc_drv2_067_buyers_21d_slope_in_504d":         {"inputs": ["insider_buyers"],       "func": ibc_drv2_067_buyers_21d_slope_in_504d},
    "ibc_drv2_068_buy_count_21d_rank_in_252d_21d_diff": {"inputs": ["insider_buy_count"], "func": ibc_drv2_068_buy_count_21d_rank_in_252d_21d_diff},
    "ibc_drv2_069_buyers_21d_pct_chg_63d_diff":      {"inputs": ["insider_buyers"],       "func": ibc_drv2_069_buyers_21d_pct_chg_63d_diff},
    "ibc_drv2_070_buy_count_63d_pct_chg_21d_diff":   {"inputs": ["insider_buy_count"],    "func": ibc_drv2_070_buy_count_63d_pct_chg_21d_diff},
    "ibc_drv2_071_buyers_21d_ewm_vs_63d_diff":       {"inputs": ["insider_buyers"],       "func": ibc_drv2_071_buyers_21d_ewm_vs_63d_diff},
    "ibc_drv2_072_buyers_ewm_cross_21_63_21d_diff":  {"inputs": ["insider_buyers"],       "func": ibc_drv2_072_buyers_ewm_cross_21_63_21d_diff},
    "ibc_drv2_073_buyer_zscore_21d_63d_diff":        {"inputs": ["insider_buyers"],       "func": ibc_drv2_073_buyer_zscore_21d_63d_diff},
    "ibc_drv2_074_buy_count_63d_zscore_in_252d_63d_diff": {"inputs": ["insider_buy_count"], "func": ibc_drv2_074_buy_count_63d_zscore_in_252d_63d_diff},
    "ibc_drv2_075_buyers_21d_second_diff_63d_window": {"inputs": ["insider_buyers"],      "func": ibc_drv2_075_buyers_21d_second_diff_63d_window},
}
