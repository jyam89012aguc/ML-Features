"""
89_insider_conviction — 2nd-Derivative Features 001-075
Domain: rate of change of base insider-conviction features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records to one row per (ticker, date).

FLOW series: EVENT-DRIVEN — most days are ZERO. Not forward-filled.
STOCK series (insider_shares_held): CUMULATIVE level; persists/steps.

2nd-derivative series are sparse on the daily index because the underlying
insider data is event-driven — this is CORRECT AND EXPECTED. Most days the
derivative will be zero or NaN; non-zero values mark meaningful transitions.

All feature functions look strictly backward.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_HALF  = 126
_TD_QTR   = 63
_TD_2Y    = 504
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; returns NaN wherever denominator is zero or NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


# ── Base feature helpers (self-contained, no cross-file imports) ──────────────

def _buy_conviction_ratio_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)


def _buy_conviction_ratio_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)


def _held_growth_qtr(insider_shares_held: pd.Series) -> pd.Series:
    return insider_shares_held - insider_shares_held.shift(_TD_QTR)


def _held_pct_growth_qtr(insider_shares_held: pd.Series) -> pd.Series:
    prior = insider_shares_held.shift(_TD_QTR)
    return _safe_div(insider_shares_held - prior, prior)


def _net_conviction_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    return _safe_div(net, insider_shares_held)


def _officer_conviction_mo(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)


def _buy_value_conviction_mo(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_value, _TD_MO), insider_shares_held)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def icn_drv2_001_buy_conviction_ratio_mo_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the monthly buy conviction ratio.
    Captures the first time-derivative of conviction intensity."""
    base = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_002_buy_conviction_ratio_mo_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the monthly buy conviction ratio."""
    base = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_003_buy_conviction_ratio_qtr_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the quarterly buy conviction ratio."""
    base = _buy_conviction_ratio_qtr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_004_buy_conviction_ratio_qtr_1y_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Year-over-year change in the quarterly buy conviction ratio."""
    base = _buy_conviction_ratio_qtr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_YEAR)


def icn_drv2_005_held_growth_qtr_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in quarterly held_shares growth (acceleration of accumulation)."""
    base = _held_growth_qtr(insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_006_held_pct_growth_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in quarterly held_shares percent growth."""
    base = _held_pct_growth_qtr(insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_007_net_conviction_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the monthly net conviction ratio."""
    base = _net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_008_net_conviction_qtr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the monthly net conviction ratio."""
    base = _net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_009_officer_conviction_mo_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the monthly officer conviction ratio."""
    base = _officer_conviction_mo(officer_buy_value, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_010_buy_value_conviction_mo_diff(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the monthly buy value conviction ratio."""
    base = _buy_value_conviction_mo(insider_buy_value, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_011_conviction_ratio_zscore_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the 1-year z-score of monthly conviction ratio."""
    base = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_YEAR)
    return base - base.shift(_TD_MO)


def icn_drv2_012_conviction_ratio_zscore_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the 1-year z-score of monthly conviction ratio."""
    base = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def icn_drv2_013_held_zscore_1y_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the 1-year z-score of insider_shares_held."""
    base = _zscore_rolling(insider_shares_held, _TD_YEAR)
    return base - base.shift(_TD_MO)


def icn_drv2_014_held_zscore_1y_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the 1-year z-score of insider_shares_held."""
    base = _zscore_rolling(insider_shares_held, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def icn_drv2_015_buy_conviction_pct_change_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month percent change in monthly conviction ratio."""
    base = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    prior = base.shift(_TD_MO)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def icn_drv2_016_buy_conviction_pct_change_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter percent change in quarterly conviction ratio."""
    base = _buy_conviction_ratio_qtr(insider_buy_shares, insider_shares_held)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def icn_drv2_017_conviction_slope_of_ratio_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Rolling 63-day OLS slope of the monthly conviction ratio series.
    Measures the linear trend in conviction intensity over the quarter."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return ratio.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def icn_drv2_018_held_growth_trend_slope_1y(insider_shares_held: pd.Series) -> pd.Series:
    """Rolling 252-day OLS slope of the quarterly held_shares growth series."""
    growth = _held_growth_qtr(insider_shares_held)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return growth.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def icn_drv2_019_conviction_ewm_diff_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in EWM(span=21) of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm = ratio.ewm(span=_TD_MO, min_periods=max(1, _TD_MO // 4)).mean()
    return ewm - ewm.shift(_TD_MO)


def icn_drv2_020_net_conviction_1y_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Year-over-year change in the monthly net conviction ratio."""
    base = _net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_YEAR)


def icn_drv2_021_buy_conviction_ratio_mo_1y_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Year-over-year change in the monthly buy conviction ratio."""
    base = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_YEAR)


def icn_drv2_022_conviction_zscore_acceleration(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Second difference of 1-year conviction z-score at monthly lag (z-score acceleration)."""
    zs = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_YEAR)
    d1 = zs - zs.shift(_TD_MO)
    return d1 - d1.shift(_TD_MO)


def icn_drv2_023_held_shares_pct_growth_acceleration(insider_shares_held: pd.Series) -> pd.Series:
    """Second difference of quarterly held_shares percent growth (acceleration of % growth)."""
    base = _held_pct_growth_qtr(insider_shares_held)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icn_drv2_024_officer_conviction_qtr_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in monthly officer conviction ratio."""
    base = _officer_conviction_mo(officer_buy_value, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_025_conviction_ratio_ewm_acceleration(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Change in (EWM_short - EWM_long) conviction crossover vs. its value one quarter ago.
    Measures whether the conviction EWM crossover is itself strengthening."""
    ratio      = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    short_ewm  = ratio.ewm(span=_TD_MO,  min_periods=max(1, _TD_MO  // 4)).mean()
    long_ewm   = ratio.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    crossover  = short_ewm - long_ewm
    return crossover - crossover.shift(_TD_QTR)


# ── 2nd-derivative helpers (additional) ──────────────────────────────────────

def _buy_conviction_ratio_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_HALF), insider_shares_held)


def _net_conviction_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    return _safe_div(net, insider_shares_held)


def _officer_conviction_qtr(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR), insider_shares_held)


def _buy_value_conviction_qtr(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_value, _TD_QTR), insider_shares_held)


def _held_growth_mo(insider_shares_held: pd.Series) -> pd.Series:
    return insider_shares_held - insider_shares_held.shift(_TD_MO)


def _held_growth_1y(insider_shares_held: pd.Series) -> pd.Series:
    return insider_shares_held - insider_shares_held.shift(_TD_YEAR)


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def icn_drv2_026_buy_conviction_halfyr_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the half-year buy conviction ratio."""
    base = _buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_027_buy_conviction_halfyr_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the half-year buy conviction ratio."""
    base = _buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_028_buy_conviction_halfyr_1y_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Year-over-year change in the half-year buy conviction ratio."""
    base = _buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_YEAR)


def icn_drv2_029_net_conviction_qtr_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the quarterly net conviction ratio."""
    base = _net_conviction_qtr(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_030_net_conviction_qtr_qtr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the quarterly net conviction ratio."""
    base = _net_conviction_qtr(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_031_net_conviction_qtr_1y_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Year-over-year change in the quarterly net conviction ratio."""
    base = _net_conviction_qtr(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_YEAR)


def icn_drv2_032_officer_conviction_qtr_mo_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the quarterly officer conviction ratio."""
    base = _officer_conviction_qtr(officer_buy_value, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_033_officer_conviction_qtr_1y_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Year-over-year change in the quarterly officer conviction ratio."""
    base = _officer_conviction_qtr(officer_buy_value, insider_shares_held)
    return base - base.shift(_TD_YEAR)


def icn_drv2_034_buy_value_conviction_qtr_mo_diff(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the quarterly buy value conviction ratio."""
    base = _buy_value_conviction_qtr(insider_buy_value, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_035_buy_value_conviction_qtr_qtr_diff(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the quarterly buy value conviction ratio."""
    base = _buy_value_conviction_qtr(insider_buy_value, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_036_held_growth_mo_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the monthly held_shares growth."""
    base = _held_growth_mo(insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_037_held_growth_mo_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the monthly held_shares growth."""
    base = _held_growth_mo(insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_038_held_growth_1y_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the annual held_shares growth."""
    base = _held_growth_1y(insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_039_held_growth_1y_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the annual held_shares growth."""
    base = _held_growth_1y(insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_040_held_pct_growth_mo_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in monthly held_shares percent growth."""
    prior = insider_shares_held.shift(_TD_MO)
    base = _safe_div(insider_shares_held - prior, prior)
    return base - base.shift(_TD_MO)


def icn_drv2_041_conviction_zscore_2y_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in 2-year z-score of monthly conviction ratio."""
    base = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_2Y)
    return base - base.shift(_TD_MO)


def icn_drv2_042_conviction_zscore_2y_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in 2-year z-score of monthly conviction ratio."""
    base = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_2Y)
    return base - base.shift(_TD_QTR)


def icn_drv2_043_held_zscore_2y_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in 2-year z-score of insider_shares_held."""
    base = _zscore_rolling(insider_shares_held, _TD_2Y)
    return base - base.shift(_TD_MO)


def icn_drv2_044_held_zscore_2y_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in 2-year z-score of insider_shares_held."""
    base = _zscore_rolling(insider_shares_held, _TD_2Y)
    return base - base.shift(_TD_QTR)


def icn_drv2_045_buy_value_conviction_mo_qtr_diff(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in monthly buy value conviction ratio."""
    base = _buy_value_conviction_mo(insider_buy_value, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_046_officer_conviction_halfyr_mo_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the half-year officer conviction ratio."""
    base = _safe_div(_rolling_sum(officer_buy_value, _TD_HALF), insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_047_net_conviction_halfyr_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the half-year net conviction ratio."""
    net = _rolling_sum(insider_buy_shares, _TD_HALF) - _rolling_sum(insider_sell_shares, _TD_HALF)
    base = _safe_div(net, insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_048_net_conviction_halfyr_qtr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the half-year net conviction ratio."""
    net = _rolling_sum(insider_buy_shares, _TD_HALF) - _rolling_sum(insider_sell_shares, _TD_HALF)
    base = _safe_div(net, insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_049_buy_conviction_ratio_wk_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the weekly buy conviction ratio (5-day)."""
    base = _safe_div(_rolling_sum(insider_buy_shares, _TD_WK), insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_050_buy_conviction_ratio_wk_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the weekly buy conviction ratio (5-day)."""
    base = _safe_div(_rolling_sum(insider_buy_shares, _TD_WK), insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_051_conviction_slope_1y_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the 1-year OLS slope of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    def _slope(arr):
        n = len(arr)
        if n < 2: return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    slope = ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_MO)


def icn_drv2_052_conviction_slope_1y_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the 1-year OLS slope of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    def _slope(arr):
        n = len(arr)
        if n < 2: return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    slope = ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def icn_drv2_053_held_trend_slope_qtr_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the 63-day OLS slope of insider_shares_held."""
    def _slope(arr):
        n = len(arr)
        if n < 2: return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    slope = insider_shares_held.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_MO)


def icn_drv2_054_held_trend_slope_qtr_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in the 63-day OLS slope of insider_shares_held."""
    def _slope(arr):
        n = len(arr)
        if n < 2: return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    slope = insider_shares_held.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def icn_drv2_055_net_conviction_zscore_1y_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in 1-year z-score of monthly net conviction ratio."""
    base = _zscore_rolling(_net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held), _TD_YEAR)
    return base - base.shift(_TD_MO)


def icn_drv2_056_net_conviction_zscore_1y_qtr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in 1-year z-score of monthly net conviction ratio."""
    base = _zscore_rolling(_net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def icn_drv2_057_buy_conviction_ewm63_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in EWM(span=63) of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm = ratio.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return ewm - ewm.shift(_TD_MO)


def icn_drv2_058_buy_conviction_ewm63_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in EWM(span=63) of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm = ratio.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    return ewm - ewm.shift(_TD_QTR)


def icn_drv2_059_buy_value_conviction_1y_mo_diff(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in annual buy value conviction ratio."""
    base = _safe_div(_rolling_sum(insider_buy_value, _TD_YEAR), insider_shares_held)
    return base - base.shift(_TD_MO)


def icn_drv2_060_buy_value_conviction_1y_qtr_diff(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in annual buy value conviction ratio."""
    base = _safe_div(_rolling_sum(insider_buy_value, _TD_YEAR), insider_shares_held)
    return base - base.shift(_TD_QTR)


def icn_drv2_061_held_pct_growth_1y_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in annual held_shares percent growth."""
    prior = insider_shares_held.shift(_TD_YEAR)
    base = _safe_div(insider_shares_held - prior, prior)
    return base - base.shift(_TD_MO)


def icn_drv2_062_held_pct_growth_1y_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in annual held_shares percent growth."""
    prior = insider_shares_held.shift(_TD_YEAR)
    base = _safe_div(insider_shares_held - prior, prior)
    return base - base.shift(_TD_QTR)


def icn_drv2_063_buy_conviction_pct_change_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Half-year percent change in the monthly conviction ratio."""
    base = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    prior = base.shift(_TD_HALF)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def icn_drv2_064_net_conviction_pct_change_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter percent change in monthly net conviction ratio."""
    base = _net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def icn_drv2_065_officer_conviction_pct_change_qtr(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter percent change in monthly officer conviction ratio."""
    base = _officer_conviction_mo(officer_buy_value, insider_shares_held)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs().replace(0, np.nan))


def icn_drv2_066_buy_conviction_zscore_halfyr_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in 2-year z-score of half-year conviction ratio."""
    base = _zscore_rolling(_buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held), _TD_2Y)
    return base - base.shift(_TD_MO)


def icn_drv2_067_held_expanding_zscore_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in the expanding z-score of insider_shares_held."""
    m  = insider_shares_held.expanding(min_periods=2).mean()
    sd = insider_shares_held.expanding(min_periods=2).std()
    base = _safe_div(insider_shares_held - m, sd)
    return base - base.shift(_TD_MO)


def icn_drv2_068_buy_conviction_qtr_vs_halfyr_diff_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in (quarterly - half-year) conviction ratio spread."""
    spread = _buy_conviction_ratio_qtr(insider_buy_shares, insider_shares_held) - _buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held)
    return spread - spread.shift(_TD_MO)


def icn_drv2_069_buy_conviction_mo_vs_1y_diff_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in (monthly - annual) conviction ratio spread."""
    spread = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held) - _safe_div(_rolling_sum(insider_buy_shares, _TD_YEAR), insider_shares_held)
    return spread - spread.shift(_TD_QTR)


def icn_drv2_070_net_conviction_halfyr_1y_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Year-over-year change in the half-year net conviction ratio."""
    net = _rolling_sum(insider_buy_shares, _TD_HALF) - _rolling_sum(insider_sell_shares, _TD_HALF)
    base = _safe_div(net, insider_shares_held)
    return base - base.shift(_TD_YEAR)


def icn_drv2_071_held_pct_growth_halfyr_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in half-year held_shares percent growth."""
    prior = insider_shares_held.shift(_TD_HALF)
    base = _safe_div(insider_shares_held - prior, prior)
    return base - base.shift(_TD_MO)


def icn_drv2_072_held_pct_growth_halfyr_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in half-year held_shares percent growth."""
    prior = insider_shares_held.shift(_TD_HALF)
    base = _safe_div(insider_shares_held - prior, prior)
    return base - base.shift(_TD_QTR)


def icn_drv2_073_buy_conviction_ewm_halfyr_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in EWM(span=126) of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm = ratio.ewm(span=_TD_HALF, min_periods=max(1, _TD_HALF // 4)).mean()
    return ewm - ewm.shift(_TD_MO)


def icn_drv2_074_buy_conviction_ewm_halfyr_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in EWM(span=126) of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm = ratio.ewm(span=_TD_HALF, min_periods=max(1, _TD_HALF // 4)).mean()
    return ewm - ewm.shift(_TD_QTR)


def icn_drv2_075_buy_conviction_rolling_std_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """Month-over-month change in 1-year rolling std of monthly conviction ratio.
    Captures whether conviction volatility itself is rising — elevated uncertainty."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    std = ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()
    return std - std.shift(_TD_MO)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

INSIDER_CONVICTION_REGISTRY_2ND_DERIVATIVES = {
    "icn_drv2_001_buy_conviction_ratio_mo_mo_diff":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_001_buy_conviction_ratio_mo_mo_diff},
    "icn_drv2_002_buy_conviction_ratio_mo_qtr_diff":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_002_buy_conviction_ratio_mo_qtr_diff},
    "icn_drv2_003_buy_conviction_ratio_qtr_qtr_diff":   {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_003_buy_conviction_ratio_qtr_qtr_diff},
    "icn_drv2_004_buy_conviction_ratio_qtr_1y_diff":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_004_buy_conviction_ratio_qtr_1y_diff},
    "icn_drv2_005_held_growth_qtr_qtr_diff":            {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_005_held_growth_qtr_qtr_diff},
    "icn_drv2_006_held_pct_growth_qtr_diff":            {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_006_held_pct_growth_qtr_diff},
    "icn_drv2_007_net_conviction_mo_diff":              {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_007_net_conviction_mo_diff},
    "icn_drv2_008_net_conviction_qtr_diff":             {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_008_net_conviction_qtr_diff},
    "icn_drv2_009_officer_conviction_mo_diff":          {"inputs": ["officer_buy_value", "insider_shares_held"],                                      "func": icn_drv2_009_officer_conviction_mo_diff},
    "icn_drv2_010_buy_value_conviction_mo_diff":        {"inputs": ["insider_buy_value", "insider_shares_held"],                                      "func": icn_drv2_010_buy_value_conviction_mo_diff},
    "icn_drv2_011_conviction_ratio_zscore_mo_diff":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_011_conviction_ratio_zscore_mo_diff},
    "icn_drv2_012_conviction_ratio_zscore_qtr_diff":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_012_conviction_ratio_zscore_qtr_diff},
    "icn_drv2_013_held_zscore_1y_mo_diff":              {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_013_held_zscore_1y_mo_diff},
    "icn_drv2_014_held_zscore_1y_qtr_diff":             {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_014_held_zscore_1y_qtr_diff},
    "icn_drv2_015_buy_conviction_pct_change_mo":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_015_buy_conviction_pct_change_mo},
    "icn_drv2_016_buy_conviction_pct_change_qtr":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_016_buy_conviction_pct_change_qtr},
    "icn_drv2_017_conviction_slope_of_ratio_qtr":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_017_conviction_slope_of_ratio_qtr},
    "icn_drv2_018_held_growth_trend_slope_1y":          {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_018_held_growth_trend_slope_1y},
    "icn_drv2_019_conviction_ewm_diff_mo":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_019_conviction_ewm_diff_mo},
    "icn_drv2_020_net_conviction_1y_diff":              {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_020_net_conviction_1y_diff},
    "icn_drv2_021_buy_conviction_ratio_mo_1y_diff":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_021_buy_conviction_ratio_mo_1y_diff},
    "icn_drv2_022_conviction_zscore_acceleration":      {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_022_conviction_zscore_acceleration},
    "icn_drv2_023_held_shares_pct_growth_acceleration": {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_023_held_shares_pct_growth_acceleration},
    "icn_drv2_024_officer_conviction_qtr_diff":         {"inputs": ["officer_buy_value", "insider_shares_held"],                                      "func": icn_drv2_024_officer_conviction_qtr_diff},
    "icn_drv2_025_conviction_ratio_ewm_acceleration":   {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_025_conviction_ratio_ewm_acceleration},
    "icn_drv2_026_buy_conviction_halfyr_mo_diff":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_026_buy_conviction_halfyr_mo_diff},
    "icn_drv2_027_buy_conviction_halfyr_qtr_diff":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_027_buy_conviction_halfyr_qtr_diff},
    "icn_drv2_028_buy_conviction_halfyr_1y_diff":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_028_buy_conviction_halfyr_1y_diff},
    "icn_drv2_029_net_conviction_qtr_mo_diff":           {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_029_net_conviction_qtr_mo_diff},
    "icn_drv2_030_net_conviction_qtr_qtr_diff":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_030_net_conviction_qtr_qtr_diff},
    "icn_drv2_031_net_conviction_qtr_1y_diff":           {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_031_net_conviction_qtr_1y_diff},
    "icn_drv2_032_officer_conviction_qtr_mo_diff":       {"inputs": ["officer_buy_value", "insider_shares_held"],                                      "func": icn_drv2_032_officer_conviction_qtr_mo_diff},
    "icn_drv2_033_officer_conviction_qtr_1y_diff":       {"inputs": ["officer_buy_value", "insider_shares_held"],                                      "func": icn_drv2_033_officer_conviction_qtr_1y_diff},
    "icn_drv2_034_buy_value_conviction_qtr_mo_diff":     {"inputs": ["insider_buy_value", "insider_shares_held"],                                      "func": icn_drv2_034_buy_value_conviction_qtr_mo_diff},
    "icn_drv2_035_buy_value_conviction_qtr_qtr_diff":    {"inputs": ["insider_buy_value", "insider_shares_held"],                                      "func": icn_drv2_035_buy_value_conviction_qtr_qtr_diff},
    "icn_drv2_036_held_growth_mo_mo_diff":               {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_036_held_growth_mo_mo_diff},
    "icn_drv2_037_held_growth_mo_qtr_diff":              {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_037_held_growth_mo_qtr_diff},
    "icn_drv2_038_held_growth_1y_mo_diff":               {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_038_held_growth_1y_mo_diff},
    "icn_drv2_039_held_growth_1y_qtr_diff":              {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_039_held_growth_1y_qtr_diff},
    "icn_drv2_040_held_pct_growth_mo_mo_diff":           {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_040_held_pct_growth_mo_mo_diff},
    "icn_drv2_041_conviction_zscore_2y_mo_diff":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_041_conviction_zscore_2y_mo_diff},
    "icn_drv2_042_conviction_zscore_2y_qtr_diff":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_042_conviction_zscore_2y_qtr_diff},
    "icn_drv2_043_held_zscore_2y_mo_diff":               {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_043_held_zscore_2y_mo_diff},
    "icn_drv2_044_held_zscore_2y_qtr_diff":              {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_044_held_zscore_2y_qtr_diff},
    "icn_drv2_045_buy_value_conviction_mo_qtr_diff":     {"inputs": ["insider_buy_value", "insider_shares_held"],                                      "func": icn_drv2_045_buy_value_conviction_mo_qtr_diff},
    "icn_drv2_046_officer_conviction_halfyr_mo_diff":    {"inputs": ["officer_buy_value", "insider_shares_held"],                                      "func": icn_drv2_046_officer_conviction_halfyr_mo_diff},
    "icn_drv2_047_net_conviction_halfyr_mo_diff":        {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_047_net_conviction_halfyr_mo_diff},
    "icn_drv2_048_net_conviction_halfyr_qtr_diff":       {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_048_net_conviction_halfyr_qtr_diff},
    "icn_drv2_049_buy_conviction_ratio_wk_mo_diff":      {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_049_buy_conviction_ratio_wk_mo_diff},
    "icn_drv2_050_buy_conviction_ratio_wk_qtr_diff":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_050_buy_conviction_ratio_wk_qtr_diff},
    "icn_drv2_051_conviction_slope_1y_mo_diff":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_051_conviction_slope_1y_mo_diff},
    "icn_drv2_052_conviction_slope_1y_qtr_diff":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_052_conviction_slope_1y_qtr_diff},
    "icn_drv2_053_held_trend_slope_qtr_mo_diff":         {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_053_held_trend_slope_qtr_mo_diff},
    "icn_drv2_054_held_trend_slope_qtr_qtr_diff":        {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_054_held_trend_slope_qtr_qtr_diff},
    "icn_drv2_055_net_conviction_zscore_1y_mo_diff":     {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_055_net_conviction_zscore_1y_mo_diff},
    "icn_drv2_056_net_conviction_zscore_1y_qtr_diff":    {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_056_net_conviction_zscore_1y_qtr_diff},
    "icn_drv2_057_buy_conviction_ewm63_mo_diff":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_057_buy_conviction_ewm63_mo_diff},
    "icn_drv2_058_buy_conviction_ewm63_qtr_diff":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_058_buy_conviction_ewm63_qtr_diff},
    "icn_drv2_059_buy_value_conviction_1y_mo_diff":      {"inputs": ["insider_buy_value", "insider_shares_held"],                                      "func": icn_drv2_059_buy_value_conviction_1y_mo_diff},
    "icn_drv2_060_buy_value_conviction_1y_qtr_diff":     {"inputs": ["insider_buy_value", "insider_shares_held"],                                      "func": icn_drv2_060_buy_value_conviction_1y_qtr_diff},
    "icn_drv2_061_held_pct_growth_1y_mo_diff":           {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_061_held_pct_growth_1y_mo_diff},
    "icn_drv2_062_held_pct_growth_1y_qtr_diff":          {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_062_held_pct_growth_1y_qtr_diff},
    "icn_drv2_063_buy_conviction_pct_change_halfyr":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_063_buy_conviction_pct_change_halfyr},
    "icn_drv2_064_net_conviction_pct_change_qtr":        {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_064_net_conviction_pct_change_qtr},
    "icn_drv2_065_officer_conviction_pct_change_qtr":    {"inputs": ["officer_buy_value", "insider_shares_held"],                                      "func": icn_drv2_065_officer_conviction_pct_change_qtr},
    "icn_drv2_066_buy_conviction_zscore_halfyr_mo_diff": {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_066_buy_conviction_zscore_halfyr_mo_diff},
    "icn_drv2_067_held_expanding_zscore_mo_diff":        {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_067_held_expanding_zscore_mo_diff},
    "icn_drv2_068_buy_conviction_qtr_vs_halfyr_diff_mo": {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_068_buy_conviction_qtr_vs_halfyr_diff_mo},
    "icn_drv2_069_buy_conviction_mo_vs_1y_diff_qtr":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_069_buy_conviction_mo_vs_1y_diff_qtr},
    "icn_drv2_070_net_conviction_halfyr_1y_diff":        {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],               "func": icn_drv2_070_net_conviction_halfyr_1y_diff},
    "icn_drv2_071_held_pct_growth_halfyr_mo_diff":       {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_071_held_pct_growth_halfyr_mo_diff},
    "icn_drv2_072_held_pct_growth_halfyr_qtr_diff":      {"inputs": ["insider_shares_held"],                                                           "func": icn_drv2_072_held_pct_growth_halfyr_qtr_diff},
    "icn_drv2_073_buy_conviction_ewm_halfyr_mo_diff":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_073_buy_conviction_ewm_halfyr_mo_diff},
    "icn_drv2_074_buy_conviction_ewm_halfyr_qtr_diff":   {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_074_buy_conviction_ewm_halfyr_qtr_diff},
    "icn_drv2_075_buy_conviction_rolling_std_mo_diff":   {"inputs": ["insider_buy_shares", "insider_shares_held"],                                     "func": icn_drv2_075_buy_conviction_rolling_std_mo_diff},
}
