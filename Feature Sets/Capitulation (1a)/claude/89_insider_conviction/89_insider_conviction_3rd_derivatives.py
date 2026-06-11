"""
89_insider_conviction — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative insider-conviction features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
--------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records to one row per (ticker, date).

FLOW series: EVENT-DRIVEN — most days are ZERO. Not forward-filled.
STOCK series (insider_shares_held): CUMULATIVE level; persists/steps.

3rd-derivative series are very sparse on the daily index because underlying
insider data is event-driven and conviction ratios change only on transaction
days — this is CORRECT AND EXPECTED. Non-zero values mark higher-order
inflection points in conviction dynamics.

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


# ── 2nd-derivative helpers (self-contained recomputes) ────────────────────────

def _buy_conviction_ratio_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_MO), insider_shares_held)


def _buy_conviction_ratio_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held)


def _drv2_conviction_ratio_mo_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def _drv2_conviction_ratio_mo_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def _drv2_conviction_ratio_qtr_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _buy_conviction_ratio_qtr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def _held_growth_qtr(insider_shares_held: pd.Series) -> pd.Series:
    return insider_shares_held - insider_shares_held.shift(_TD_QTR)


def _drv2_held_growth_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    base = _held_growth_qtr(insider_shares_held)
    return base - base.shift(_TD_QTR)


def _net_conviction_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    net = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    return _safe_div(net, insider_shares_held)


def _drv2_net_conviction_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _drv2_conviction_zscore_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_YEAR)
    return base - base.shift(_TD_MO)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def icn_drv3_001_conviction_mo_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-derivative conviction MoM diff.
    Captures the jerk (rate of change of acceleration) of monthly conviction."""
    d2 = _drv2_conviction_ratio_mo_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_002_conviction_mo_diff_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in the 2nd-derivative conviction MoM diff."""
    d2 = _drv2_conviction_ratio_mo_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_003_conviction_qtr_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-derivative conviction QoQ diff."""
    d2 = _drv2_conviction_ratio_mo_qtr_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_004_conviction_qtr_diff_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in the 2nd-derivative conviction QoQ diff."""
    d2 = _drv2_conviction_ratio_mo_qtr_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_005_qtr_conviction_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv QoQ conviction ratio diff."""
    d2 = _drv2_conviction_ratio_qtr_qtr_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_006_held_growth_diff_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv held_shares QoQ growth diff."""
    d2 = _drv2_held_growth_qtr_diff(insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_007_held_growth_diff_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in the 2nd-deriv held_shares QoQ growth diff."""
    d2 = _drv2_held_growth_qtr_diff(insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_008_net_conviction_diff_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv net conviction MoM diff."""
    d2 = _drv2_net_conviction_mo_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_009_net_conviction_diff_qtr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in the 2nd-deriv net conviction MoM diff."""
    d2 = _drv2_net_conviction_mo_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_010_conviction_zscore_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv conviction z-score MoM diff."""
    d2 = _drv2_conviction_zscore_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_011_conviction_zscore_diff_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in the 2nd-deriv conviction z-score MoM diff."""
    d2 = _drv2_conviction_zscore_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_012_conviction_pct_change_acceleration(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: change in the 2nd-deriv month-over-month percent change of conviction ratio.
    (pct_change of the MoM diff), then differenced again."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    d1_pct = _safe_div(ratio - ratio.shift(_TD_MO), ratio.shift(_TD_MO).abs().replace(0, np.nan))
    d2 = d1_pct - d1_pct.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_013_held_pct_growth_jerk(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: third difference of quarterly held_shares percent growth."""
    pct = _safe_div(insider_shares_held - insider_shares_held.shift(_TD_QTR), insider_shares_held.shift(_TD_QTR))
    d1 = pct - pct.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_014_conviction_ewm_mo_jerk(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv EWM(span=21) conviction diff."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm   = ratio.ewm(span=_TD_MO, min_periods=max(1, _TD_MO // 4)).mean()
    d2    = (ewm - ewm.shift(_TD_MO)) - (ewm - ewm.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_015_conviction_slope_diff_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the OLS slope of monthly conviction ratio.
    (Slope is a 2nd-derivative concept; its change is 3rd-order.)"""
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
    slope = ratio.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_MO)


def icn_drv3_016_conviction_slope_diff_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in the OLS slope of monthly conviction ratio."""
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
    slope = ratio.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def icn_drv3_017_held_trend_slope_diff_mo(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the OLS slope of insider_shares_held (1-year)."""
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
    slope = insider_shares_held.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_MO)


def icn_drv3_018_net_conviction_diff_1y_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: year-over-year change in the 2nd-deriv MoM net conviction diff."""
    d2 = _drv2_net_conviction_mo_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_YEAR)


def icn_drv3_019_conviction_ratio_1y_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv YoY conviction ratio diff."""
    d2 = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    yoy_diff = d2 - d2.shift(_TD_YEAR)
    return yoy_diff - yoy_diff.shift(_TD_MO)


def icn_drv3_020_held_zscore_acceleration(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: change in the MoM diff of the 1-year held_shares z-score (jerk of zscore)."""
    zs = _zscore_rolling(insider_shares_held, _TD_YEAR)
    d1 = zs - zs.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_021_conviction_zscore_1y_diff_acceleration(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: QoQ change in the 2nd-deriv QoQ conviction z-score diff."""
    zs   = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_YEAR)
    d2   = (zs - zs.shift(_TD_QTR)) - (zs - zs.shift(_TD_QTR)).shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_022_officer_conviction_diff_mo_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv officer MoM conviction diff."""
    base  = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    d2    = (base - base.shift(_TD_MO)) - (base - base.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_023_conviction_ewm_crossover_jerk(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv EWM crossover (short-long) diff.
    Measures the jerk of the conviction EWM acceleration signal."""
    ratio     = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    short_ewm = ratio.ewm(span=_TD_MO,  min_periods=max(1, _TD_MO  // 4)).mean()
    long_ewm  = ratio.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    cross     = short_ewm - long_ewm
    d2        = (cross - cross.shift(_TD_QTR)) - (cross - cross.shift(_TD_QTR)).shift(_TD_QTR)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_024_net_conviction_zscore_diff_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv z-score of net conviction MoM diff."""
    base = _net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held)
    zs   = _zscore_rolling(base, _TD_YEAR)
    d2   = (zs - zs.shift(_TD_MO)) - (zs - zs.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_025_grand_conviction_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series, insider_buy_count: pd.Series, officer_buy_value: pd.Series, insider_sell_shares: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in the 2nd-deriv of the grand conviction composite.
    Grand composite = z-score average of 5 signals; here we take its 3rd time-derivative."""
    z1 = _zscore_rolling(_safe_div(_rolling_sum(insider_buy_shares, _TD_QTR), insider_shares_held), _TD_YEAR)
    z2 = _zscore_rolling(insider_shares_held - insider_shares_held.shift(_TD_QTR), _TD_YEAR)
    z3 = _zscore_rolling(_rolling_sum(insider_buy_count, _TD_QTR), _TD_YEAR)
    z4 = _zscore_rolling(_safe_div(_rolling_sum(officer_buy_value, _TD_QTR), insider_shares_held), _TD_YEAR)
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    z5 = _zscore_rolling(_safe_div(net, insider_shares_held), _TD_YEAR)
    n_valid = (z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float)
               + z4.notna().astype(float) + z5.notna().astype(float))
    total   = z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0)
    composite = _safe_div(total, n_valid)
    d1 = composite - composite.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


# ── Additional 2nd-derivative helpers for 3rd-derivative functions 026-075 ────

def _buy_conviction_ratio_halfyr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(insider_buy_shares, _TD_HALF), insider_shares_held)


def _net_conviction_qtr(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    net = _rolling_sum(insider_buy_shares, _TD_QTR) - _rolling_sum(insider_sell_shares, _TD_QTR)
    return _safe_div(net, insider_shares_held)


def _officer_conviction_qtr(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR), insider_shares_held)


def _drv2_buy_conviction_halfyr_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def _drv2_buy_conviction_halfyr_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def _drv2_net_conviction_qtr_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _net_conviction_qtr(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def _drv2_net_conviction_qtr_qtr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _net_conviction_qtr(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return base - base.shift(_TD_QTR)


def _drv2_officer_conviction_qtr_mo_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _officer_conviction_qtr(officer_buy_value, insider_shares_held)
    return base - base.shift(_TD_MO)


def _drv2_conviction_ratio_qtr_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    base = _buy_conviction_ratio_qtr(insider_buy_shares, insider_shares_held)
    return base - base.shift(_TD_MO)


def _drv2_held_growth_mo_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    base = insider_shares_held - insider_shares_held.shift(_TD_MO)
    return base - base.shift(_TD_MO)


def _drv2_held_zscore_1y_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    base = _zscore_rolling(insider_shares_held, _TD_YEAR)
    return base - base.shift(_TD_MO)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def icn_drv3_026_conviction_halfyr_diff_mo_diff_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv half-year conviction MoM diff."""
    d2 = _drv2_buy_conviction_halfyr_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_027_conviction_halfyr_diff_qtr_diff_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv half-year conviction QoQ diff."""
    d2 = _drv2_buy_conviction_halfyr_qtr_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_028_conviction_halfyr_diff_mo_diff_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv half-year conviction MoM diff."""
    d2 = _drv2_buy_conviction_halfyr_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_029_conviction_halfyr_diff_qtr_diff_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv half-year conviction QoQ diff."""
    d2 = _drv2_buy_conviction_halfyr_qtr_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_030_net_conviction_qtr_diff_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv quarterly net conviction MoM diff."""
    d2 = _drv2_net_conviction_qtr_mo_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_031_net_conviction_qtr_diff_qtr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv quarterly net conviction MoM diff."""
    d2 = _drv2_net_conviction_qtr_mo_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_032_net_conviction_qtr_qqdiff_mo_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv quarterly net conviction QoQ diff."""
    d2 = _drv2_net_conviction_qtr_qtr_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_033_officer_conviction_qtr_diff_mo_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv officer quarterly conviction MoM diff."""
    d2 = _drv2_officer_conviction_qtr_mo_diff(officer_buy_value, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_034_officer_conviction_qtr_diff_qtr_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv officer quarterly conviction MoM diff."""
    d2 = _drv2_officer_conviction_qtr_mo_diff(officer_buy_value, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_035_conviction_qtr_diff_mo_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv quarterly conviction MoM diff."""
    d2 = _drv2_conviction_ratio_qtr_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_036_conviction_qtr_diff_mo_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv quarterly conviction MoM diff."""
    d2 = _drv2_conviction_ratio_qtr_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_037_held_growth_mo_diff_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv monthly held growth MoM diff."""
    d2 = _drv2_held_growth_mo_mo_diff(insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_038_held_growth_mo_diff_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv monthly held growth MoM diff."""
    d2 = _drv2_held_growth_mo_mo_diff(insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_039_held_zscore_mo_diff_qtr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv held z-score MoM diff."""
    d2 = _drv2_held_zscore_1y_mo_diff(insider_shares_held)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_040_held_zscore_mo_diff_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv held z-score MoM diff."""
    d2 = _drv2_held_zscore_1y_mo_diff(insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_041_conviction_ewm_diff_mo_qtr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv EWM(21) conviction MoM diff."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm = ratio.ewm(span=_TD_MO, min_periods=max(1, _TD_MO // 4)).mean()
    d2 = (ewm - ewm.shift(_TD_MO)) - (ewm - ewm.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_042_conviction_mo_diff_1y_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: year-over-year change in the 2nd-deriv conviction MoM diff."""
    d2 = _drv2_conviction_ratio_mo_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_YEAR)


def icn_drv3_043_net_conviction_mo_diff_1y_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: year-over-year change in the 2nd-deriv net conviction MoM diff."""
    d2 = _drv2_net_conviction_mo_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_YEAR)


def icn_drv3_044_held_growth_qtr_diff_mo_diff_mo(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv held QoQ growth QoQ diff."""
    d2 = _drv2_held_growth_qtr_diff(insider_shares_held)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_045_held_growth_qtr_diff_1y_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: year-over-year change in the 2nd-deriv held QoQ growth QoQ diff."""
    d2 = _drv2_held_growth_qtr_diff(insider_shares_held)
    return d2 - d2.shift(_TD_YEAR)


def icn_drv3_046_conviction_zscore_diff_1y_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: year-over-year change in the 2nd-deriv conviction z-score MoM diff."""
    d2 = _drv2_conviction_zscore_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_YEAR)


def icn_drv3_047_conviction_qtr_mo_diff_1y_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: year-over-year change in the 2nd-deriv quarterly conviction MoM diff."""
    d2 = _drv2_conviction_ratio_qtr_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_YEAR)


def icn_drv3_048_net_conviction_diff_halfyr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: half-year change in the 2nd-deriv net conviction MoM diff."""
    d2 = _drv2_net_conviction_mo_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_HALF)


def icn_drv3_049_conviction_mo_diff_halfyr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: half-year change in the 2nd-deriv conviction MoM diff."""
    d2 = _drv2_conviction_ratio_mo_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_HALF)


def icn_drv3_050_held_growth_diff_halfyr_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: half-year change in the 2nd-deriv held QoQ growth QoQ diff."""
    d2 = _drv2_held_growth_qtr_diff(insider_shares_held)
    return d2 - d2.shift(_TD_HALF)


def icn_drv3_051_conviction_qtr_diff_halfyr_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: half-year change in 2nd-deriv quarterly conviction QoQ diff."""
    d2 = _drv2_conviction_ratio_qtr_qtr_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_HALF)


def icn_drv3_052_officer_conviction_mo_diff_qtr_diff(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in 2nd-deriv officer MoM conviction diff."""
    base = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    d2   = (base - base.shift(_TD_MO)) - (base - base.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_053_officer_conviction_ewm_jerk(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv EWM(21) officer conviction diff."""
    base = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    ewm  = base.ewm(span=_TD_MO, min_periods=max(1, _TD_MO // 4)).mean()
    d2   = (ewm - ewm.shift(_TD_MO)) - (ewm - ewm.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_054_net_conviction_ewm_jerk(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv EWM(21) net conviction diff."""
    net  = _rolling_sum(insider_buy_shares, _TD_MO) - _rolling_sum(insider_sell_shares, _TD_MO)
    base = _safe_div(net, insider_shares_held)
    ewm  = base.ewm(span=_TD_MO, min_periods=max(1, _TD_MO // 4)).mean()
    d2   = (ewm - ewm.shift(_TD_MO)) - (ewm - ewm.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_055_held_pct_growth_jerk_mo(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv monthly held_shares % growth MoM diff."""
    prior = insider_shares_held.shift(_TD_MO)
    pct = _safe_div(insider_shares_held - prior, prior)
    d1 = pct - pct.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_056_conviction_pct_change_qtr_jerk(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv QoQ pct-change of conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    d1_pct = _safe_div(ratio - ratio.shift(_TD_QTR), ratio.shift(_TD_QTR).abs().replace(0, np.nan))
    d2 = d1_pct - d1_pct.shift(_TD_QTR)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_057_conviction_halfyr_diff_1y_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: year-over-year change in 2nd-deriv half-year conviction MoM diff."""
    d2 = _drv2_buy_conviction_halfyr_mo_diff(insider_buy_shares, insider_shares_held)
    return d2 - d2.shift(_TD_YEAR)


def icn_drv3_058_net_qtr_diff_halfyr_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: half-year change in 2nd-deriv quarterly net conviction QoQ diff."""
    d2 = _drv2_net_conviction_qtr_qtr_diff(insider_buy_shares, insider_sell_shares, insider_shares_held)
    return d2 - d2.shift(_TD_HALF)


def icn_drv3_059_held_growth_qtr_mo_diff_mo_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv quarterly held growth MoM diff."""
    growth = insider_shares_held - insider_shares_held.shift(_TD_QTR)
    d2 = (growth - growth.shift(_TD_MO)) - (growth - growth.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_060_conviction_zscore_qtr_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv conviction z-score QoQ diff."""
    zs = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_YEAR)
    d2 = (zs - zs.shift(_TD_QTR)) - (zs - zs.shift(_TD_QTR)).shift(_TD_QTR)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_061_held_trend_slope_diff_qtr(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: quarter-over-quarter change in OLS slope of insider_shares_held (1-year)."""
    def _slope(arr):
        n = len(arr)
        if n < 2: return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    slope = insider_shares_held.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def icn_drv3_062_conviction_slope_qtr_diff_mo_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: month-over-month change in 2nd-deriv 63d OLS slope of conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    def _slope(arr):
        n = len(arr)
        if n < 2: return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    slope = ratio.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)
    d2 = (slope - slope.shift(_TD_MO)) - (slope - slope.shift(_TD_MO)).shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_063_conviction_ratio_mo_triple_diff(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly difference of buy conviction ratio (d3 at 1-month lag)."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    d1 = ratio - ratio.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_064_net_conviction_mo_triple_diff(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly difference of net conviction ratio."""
    base = _net_conviction_mo(insider_buy_shares, insider_sell_shares, insider_shares_held)
    d1 = base - base.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_065_held_shares_triple_diff_qtr(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple quarterly difference of insider_shares_held."""
    d1 = insider_shares_held - insider_shares_held.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_066_conviction_zscore_triple_diff_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly difference of 1-year conviction z-score."""
    zs = _zscore_rolling(_buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held), _TD_YEAR)
    d1 = zs - zs.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_067_officer_conviction_triple_diff_mo(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly difference of monthly officer conviction ratio."""
    base = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    d1 = base - base.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_068_held_pct_growth_qtr_triple_diff(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple quarterly difference of quarterly held_shares percent growth."""
    prior = insider_shares_held.shift(_TD_QTR)
    pct = _safe_div(insider_shares_held - prior, prior)
    d1 = pct - pct.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_069_buy_value_conviction_jerk_mo(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly diff of monthly buy_value conviction ratio."""
    base = _safe_div(_rolling_sum(insider_buy_value, _TD_MO), insider_shares_held)
    d1 = base - base.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_070_conviction_halfyr_triple_diff_mo(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly difference of half-year buy conviction ratio."""
    base = _buy_conviction_ratio_halfyr(insider_buy_shares, insider_shares_held)
    d1 = base - base.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_071_net_conviction_halfyr_triple_diff_mo(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly difference of half-year net conviction ratio."""
    net = _rolling_sum(insider_buy_shares, _TD_HALF) - _rolling_sum(insider_sell_shares, _TD_HALF)
    base = _safe_div(net, insider_shares_held)
    d1 = base - base.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_072_conviction_qtr_triple_diff_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple quarterly difference of quarterly buy conviction ratio."""
    base = _buy_conviction_ratio_qtr(insider_buy_shares, insider_shares_held)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_073_officer_conviction_jerk_qtr(officer_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple quarterly difference of monthly officer conviction ratio."""
    base = _safe_div(_rolling_sum(officer_buy_value, _TD_MO), insider_shares_held)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icn_drv3_074_held_zscore_2y_triple_diff_mo(insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple monthly difference of 2-year z-score of insider_shares_held."""
    zs = _zscore_rolling(insider_shares_held, _TD_2Y)
    d1 = zs - zs.shift(_TD_MO)
    d2 = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def icn_drv3_075_conviction_ewm_qtr_jerk_qtr(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """3rd-order: triple quarterly difference of EWM(span=63) of monthly conviction ratio."""
    ratio = _buy_conviction_ratio_mo(insider_buy_shares, insider_shares_held)
    ewm = ratio.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 4)).mean()
    d1 = ewm - ewm.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

INSIDER_CONVICTION_REGISTRY_3RD_DERIVATIVES = {
    "icn_drv3_001_conviction_mo_diff_mo_diff":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_001_conviction_mo_diff_mo_diff},
    "icn_drv3_002_conviction_mo_diff_qtr_diff":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_002_conviction_mo_diff_qtr_diff},
    "icn_drv3_003_conviction_qtr_diff_mo_diff":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_003_conviction_qtr_diff_mo_diff},
    "icn_drv3_004_conviction_qtr_diff_qtr_diff":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_004_conviction_qtr_diff_qtr_diff},
    "icn_drv3_005_qtr_conviction_diff_mo_diff":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_005_qtr_conviction_diff_mo_diff},
    "icn_drv3_006_held_growth_diff_mo_diff":            {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_006_held_growth_diff_mo_diff},
    "icn_drv3_007_held_growth_diff_qtr_diff":           {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_007_held_growth_diff_qtr_diff},
    "icn_drv3_008_net_conviction_diff_mo_diff":         {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_008_net_conviction_diff_mo_diff},
    "icn_drv3_009_net_conviction_diff_qtr_diff":        {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_009_net_conviction_diff_qtr_diff},
    "icn_drv3_010_conviction_zscore_diff_mo_diff":      {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_010_conviction_zscore_diff_mo_diff},
    "icn_drv3_011_conviction_zscore_diff_qtr_diff":     {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_011_conviction_zscore_diff_qtr_diff},
    "icn_drv3_012_conviction_pct_change_acceleration":  {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_012_conviction_pct_change_acceleration},
    "icn_drv3_013_held_pct_growth_jerk":                {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_013_held_pct_growth_jerk},
    "icn_drv3_014_conviction_ewm_mo_jerk":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_014_conviction_ewm_mo_jerk},
    "icn_drv3_015_conviction_slope_diff_mo":            {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_015_conviction_slope_diff_mo},
    "icn_drv3_016_conviction_slope_diff_qtr":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_016_conviction_slope_diff_qtr},
    "icn_drv3_017_held_trend_slope_diff_mo":            {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_017_held_trend_slope_diff_mo},
    "icn_drv3_018_net_conviction_diff_1y_diff":         {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_018_net_conviction_diff_1y_diff},
    "icn_drv3_019_conviction_ratio_1y_diff_mo_diff":    {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_019_conviction_ratio_1y_diff_mo_diff},
    "icn_drv3_020_held_zscore_acceleration":            {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_020_held_zscore_acceleration},
    "icn_drv3_021_conviction_zscore_1y_diff_acceleration": {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                           "func": icn_drv3_021_conviction_zscore_1y_diff_acceleration},
    "icn_drv3_022_officer_conviction_diff_mo_diff":     {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_022_officer_conviction_diff_mo_diff},
    "icn_drv3_023_conviction_ewm_crossover_jerk":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_023_conviction_ewm_crossover_jerk},
    "icn_drv3_024_net_conviction_zscore_diff_mo_diff":  {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_024_net_conviction_zscore_diff_mo_diff},
    "icn_drv3_025_grand_conviction_diff_mo_diff":            {"inputs": ["insider_buy_shares", "insider_shares_held", "insider_buy_count", "officer_buy_value", "insider_sell_shares"], "func": icn_drv3_025_grand_conviction_diff_mo_diff},
    "icn_drv3_026_conviction_halfyr_diff_mo_diff_mo":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_026_conviction_halfyr_diff_mo_diff_mo},
    "icn_drv3_027_conviction_halfyr_diff_qtr_diff_mo":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_027_conviction_halfyr_diff_qtr_diff_mo},
    "icn_drv3_028_conviction_halfyr_diff_mo_diff_qtr":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_028_conviction_halfyr_diff_mo_diff_qtr},
    "icn_drv3_029_conviction_halfyr_diff_qtr_diff_qtr":      {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_029_conviction_halfyr_diff_qtr_diff_qtr},
    "icn_drv3_030_net_conviction_qtr_diff_mo_diff":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_030_net_conviction_qtr_diff_mo_diff},
    "icn_drv3_031_net_conviction_qtr_diff_qtr_diff":         {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_031_net_conviction_qtr_diff_qtr_diff},
    "icn_drv3_032_net_conviction_qtr_qqdiff_mo_diff":        {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_032_net_conviction_qtr_qqdiff_mo_diff},
    "icn_drv3_033_officer_conviction_qtr_diff_mo_diff":      {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_033_officer_conviction_qtr_diff_mo_diff},
    "icn_drv3_034_officer_conviction_qtr_diff_qtr_diff":     {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_034_officer_conviction_qtr_diff_qtr_diff},
    "icn_drv3_035_conviction_qtr_diff_mo_mo_diff":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_035_conviction_qtr_diff_mo_mo_diff},
    "icn_drv3_036_conviction_qtr_diff_mo_qtr_diff":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_036_conviction_qtr_diff_mo_qtr_diff},
    "icn_drv3_037_held_growth_mo_diff_mo_diff":              {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_037_held_growth_mo_diff_mo_diff},
    "icn_drv3_038_held_growth_mo_diff_qtr_diff":             {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_038_held_growth_mo_diff_qtr_diff},
    "icn_drv3_039_held_zscore_mo_diff_qtr_diff":             {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_039_held_zscore_mo_diff_qtr_diff},
    "icn_drv3_040_held_zscore_mo_diff_mo_diff":              {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_040_held_zscore_mo_diff_mo_diff},
    "icn_drv3_041_conviction_ewm_diff_mo_qtr_diff":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_041_conviction_ewm_diff_mo_qtr_diff},
    "icn_drv3_042_conviction_mo_diff_1y_diff":               {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_042_conviction_mo_diff_1y_diff},
    "icn_drv3_043_net_conviction_mo_diff_1y_diff":           {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_043_net_conviction_mo_diff_1y_diff},
    "icn_drv3_044_held_growth_qtr_diff_mo_diff_mo":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_044_held_growth_qtr_diff_mo_diff_mo},
    "icn_drv3_045_held_growth_qtr_diff_1y_diff":             {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_045_held_growth_qtr_diff_1y_diff},
    "icn_drv3_046_conviction_zscore_diff_1y_diff":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_046_conviction_zscore_diff_1y_diff},
    "icn_drv3_047_conviction_qtr_mo_diff_1y_diff":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_047_conviction_qtr_mo_diff_1y_diff},
    "icn_drv3_048_net_conviction_diff_halfyr_diff":          {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_048_net_conviction_diff_halfyr_diff},
    "icn_drv3_049_conviction_mo_diff_halfyr_diff":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_049_conviction_mo_diff_halfyr_diff},
    "icn_drv3_050_held_growth_diff_halfyr_diff":             {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_050_held_growth_diff_halfyr_diff},
    "icn_drv3_051_conviction_qtr_diff_halfyr_diff":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_051_conviction_qtr_diff_halfyr_diff},
    "icn_drv3_052_officer_conviction_mo_diff_qtr_diff":      {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_052_officer_conviction_mo_diff_qtr_diff},
    "icn_drv3_053_officer_conviction_ewm_jerk":              {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_053_officer_conviction_ewm_jerk},
    "icn_drv3_054_net_conviction_ewm_jerk":                  {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_054_net_conviction_ewm_jerk},
    "icn_drv3_055_held_pct_growth_jerk_mo":                  {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_055_held_pct_growth_jerk_mo},
    "icn_drv3_056_conviction_pct_change_qtr_jerk":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_056_conviction_pct_change_qtr_jerk},
    "icn_drv3_057_conviction_halfyr_diff_1y_diff":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_057_conviction_halfyr_diff_1y_diff},
    "icn_drv3_058_net_qtr_diff_halfyr_diff":                 {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_058_net_qtr_diff_halfyr_diff},
    "icn_drv3_059_held_growth_qtr_mo_diff_mo_diff":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_059_held_growth_qtr_mo_diff_mo_diff},
    "icn_drv3_060_conviction_zscore_qtr_diff_mo_diff":       {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_060_conviction_zscore_qtr_diff_mo_diff},
    "icn_drv3_061_held_trend_slope_diff_qtr":                {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_061_held_trend_slope_diff_qtr},
    "icn_drv3_062_conviction_slope_qtr_diff_mo_diff":        {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_062_conviction_slope_qtr_diff_mo_diff},
    "icn_drv3_063_conviction_ratio_mo_triple_diff":          {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_063_conviction_ratio_mo_triple_diff},
    "icn_drv3_064_net_conviction_mo_triple_diff":            {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_064_net_conviction_mo_triple_diff},
    "icn_drv3_065_held_shares_triple_diff_qtr":              {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_065_held_shares_triple_diff_qtr},
    "icn_drv3_066_conviction_zscore_triple_diff_mo":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_066_conviction_zscore_triple_diff_mo},
    "icn_drv3_067_officer_conviction_triple_diff_mo":        {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_067_officer_conviction_triple_diff_mo},
    "icn_drv3_068_held_pct_growth_qtr_triple_diff":          {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_068_held_pct_growth_qtr_triple_diff},
    "icn_drv3_069_buy_value_conviction_jerk_mo":             {"inputs": ["insider_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_069_buy_value_conviction_jerk_mo},
    "icn_drv3_070_conviction_halfyr_triple_diff_mo":         {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_070_conviction_halfyr_triple_diff_mo},
    "icn_drv3_071_net_conviction_halfyr_triple_diff_mo":     {"inputs": ["insider_buy_shares", "insider_sell_shares", "insider_shares_held"],                                       "func": icn_drv3_071_net_conviction_halfyr_triple_diff_mo},
    "icn_drv3_072_conviction_qtr_triple_diff_qtr":           {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_072_conviction_qtr_triple_diff_qtr},
    "icn_drv3_073_officer_conviction_jerk_qtr":              {"inputs": ["officer_buy_value", "insider_shares_held"],                                                               "func": icn_drv3_073_officer_conviction_jerk_qtr},
    "icn_drv3_074_held_zscore_2y_triple_diff_mo":            {"inputs": ["insider_shares_held"],                                                                                    "func": icn_drv3_074_held_zscore_2y_triple_diff_mo},
    "icn_drv3_075_conviction_ewm_qtr_jerk_qtr":              {"inputs": ["insider_buy_shares", "insider_shares_held"],                                                              "func": icn_drv3_075_conviction_ewm_qtr_jerk_qtr},
}
