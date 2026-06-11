"""
72_solvency_scores — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative solvency/distress features
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

NOTE — Altman Z'' (book-value variant)
---------------------------------------
All Altman Z''-related computations below use book equity in place of market
equity (the Z'' double-prime model).  See base file 001-075 for full rationale.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 3rd-derivative series are very sparse/stepwise on a daily index because the
underlying data is quarterly — this is correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  All feature functions in this file look strictly backward.
Quarterly cadence on the daily index: 1 quarter = 63 trading days,
1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Base / 2nd-derivative recompute helpers ───────────────────────────────────

def _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities):
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue):
    f1 = (netinc > 0).astype(float)
    f2 = (ncfo > 0).astype(float)
    roa = _safe_div(netinc, assets)
    f3 = (roa > roa.shift(_TD_QTR)).astype(float)
    f4 = (_safe_div(ncfo, assets) > roa).astype(float)
    lev = _safe_div(debt, assets)
    f5 = (lev < lev.shift(_TD_QTR)).astype(float)
    cr = _safe_div(assetsc, liabilitiesc)
    f6 = (cr > cr.shift(_TD_QTR)).astype(float)
    f7 = (shareswa <= shareswa.shift(_TD_QTR)).astype(float)
    gm = _safe_div(gp, revenue)
    f8 = (gm > gm.shift(_TD_QTR)).astype(float)
    at_ = _safe_div(revenue, assets)
    f9 = (at_ > at_.shift(_TD_QTR)).astype(float)
    return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9


def _zmijewski(netinc, assets, liabilities, assetsc, liabilitiesc):
    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    return -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq


def _springate(workingcapital, assets, ebit, ebt, liabilitiesc, revenue):
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    return 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d


# ─────────────────────────────────────────────────────────────────────────────
# 3rd-derivative helper: take the 2nd-derivative concept and differentiate once
# more (QoQ diff of the 2nd-diff concept = 3rd diff).
# ─────────────────────────────────────────────────────────────────────────────

def _drv2_altman_qoq_accel(workingcapital, assets, retearn, ebit, equity, liabilities):
    """2nd derivative of Altman Z'' (QoQ diff of QoQ diff)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    d1 = z - z.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_piotroski_qoq_accel(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue):
    """2nd derivative of Piotroski F-score."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    d1 = f - f.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_roa_accel(netinc, assets):
    roa = _safe_div(netinc, assets)
    d1 = roa - roa.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_leverage_accel(liabilities, assets):
    lev = _safe_div(liabilities, assets)
    d1 = lev - lev.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_current_ratio_accel(assetsc, liabilitiesc):
    cr = _safe_div(assetsc, liabilitiesc)
    d1 = cr - cr.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_zmijewski_accel(netinc, assets, liabilities, assetsc, liabilitiesc):
    z = _zmijewski(netinc, assets, liabilities, assetsc, liabilitiesc)
    d1 = z - z.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_springate_accel(workingcapital, assets, ebit, ebt, liabilitiesc, revenue):
    s = _springate(workingcapital, assets, ebit, ebt, liabilitiesc, revenue)
    d1 = s - s.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def slv_drv3_001_altman_z_3rd_diff_qoq(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """3rd QoQ difference of Altman Z'' score: jerk / rate of acceleration change."""
    d2 = _drv2_altman_qoq_accel(workingcapital, assets, retearn, ebit, equity, liabilities)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_002_piotroski_3rd_diff_qoq(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """3rd QoQ difference of Piotroski F-score: rate of F-score acceleration change."""
    d2 = _drv2_piotroski_qoq_accel(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_003_zmijewski_3rd_diff_qoq(
    netinc: pd.Series, assets: pd.Series, liabilities: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series,
) -> pd.Series:
    """3rd QoQ difference of Zmijewski-style score."""
    d2 = _drv2_zmijewski_accel(netinc, assets, liabilities, assetsc, liabilitiesc)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_004_springate_3rd_diff_qoq(
    workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series,
    ebt: pd.Series, liabilitiesc: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """3rd QoQ difference of Springate-style score."""
    d2 = _drv2_springate_accel(workingcapital, assets, ebit, ebt, liabilitiesc, revenue)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_005_roa_3rd_diff_qoq(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """3rd QoQ difference of ROA: jerk in profitability trajectory."""
    d2 = _drv2_roa_accel(netinc, assets)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_006_leverage_3rd_diff_qoq(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """3rd QoQ difference of leverage ratio: jerk in leverage trajectory."""
    d2 = _drv2_leverage_accel(liabilities, assets)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_007_current_ratio_3rd_diff_qoq(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """3rd QoQ difference of current ratio: jerk in liquidity trajectory."""
    d2 = _drv2_current_ratio_accel(assetsc, liabilitiesc)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_008_altman_z_zscore_2nd_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """2nd diff of the 4Q z-score of Altman Z'' (diff of drv2_007)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    zz = _zscore_rolling(z, _TD_YEAR)
    d1 = zz - zz.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_009_piotroski_zscore_2nd_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """2nd diff of the 4Q z-score of Piotroski F-score (diff of drv2_008)."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    zf = _zscore_rolling(f, _TD_YEAR)
    d1 = zf - zf.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_010_altman_z_drawdown_2nd_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """2nd QoQ diff of Altman Z'' drawdown from 1-year peak (diff of drv2_009)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    dd = z - _rolling_max(z, _TD_YEAR)
    d1 = dd - dd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_011_piotroski_drawdown_2nd_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """2nd QoQ diff of Piotroski F-score drawdown from 1-year peak."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    dd = f - _rolling_max(f, _TD_YEAR)
    d1 = dd - dd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_012_altman_z_yoy_accel(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in the YoY change of Altman Z'' (2nd order, cross-horizon)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    d_yoy = z - z.shift(_TD_YEAR)
    d1 = d_yoy - d_yoy.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_013_composite_distress_3rd_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """3rd QoQ diff of the 5-ratio custom composite distress index."""
    r1 = _safe_div(workingcapital, assets)
    r2 = _safe_div(retearn, assets)
    r3 = _safe_div(ebit, assets)
    r4 = _safe_div(equity, liabilities)
    r5 = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(r1, _TD_YEAR)
    z2 = _zscore_rolling(r2, _TD_YEAR)
    z3 = _zscore_rolling(r3, _TD_YEAR)
    z4 = _zscore_rolling(r4, _TD_YEAR)
    z5 = _zscore_rolling(r5, _TD_YEAR)
    c = (z1 + z2 + z3 + z4 + z5) / 5.0
    d1 = c - c.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_014_altman_z_ewm_2nd_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """2nd QoQ diff of EWM (span=252) of Altman Z'' (diff of drv2_021)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    ewm = z.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    d1 = ewm - ewm.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_015_piotroski_ewm_2nd_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """2nd QoQ diff of EWM (span=252) of Piotroski F-score."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    ewm = f.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    d1 = ewm - ewm.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_016_altman_z_3rd_diff_yoy(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """YoY diff of the 2nd QoQ derivative of Altman Z'' (long-horizon jerk)."""
    d2 = _drv2_altman_qoq_accel(workingcapital, assets, retearn, ebit, equity, liabilities)
    return d2 - d2.shift(_TD_YEAR)


def slv_drv3_017_piotroski_3rd_diff_yoy(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """YoY diff of the 2nd QoQ derivative of Piotroski F-score."""
    d2 = _drv2_piotroski_qoq_accel(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    return d2 - d2.shift(_TD_YEAR)


def slv_drv3_018_roa_3rd_diff_yoy(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY diff of the 2nd QoQ derivative of ROA."""
    d2 = _drv2_roa_accel(netinc, assets)
    return d2 - d2.shift(_TD_YEAR)


def slv_drv3_019_altman_z_slope_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in the 4Q rolling OLS slope of Altman Z'' (slope acceleration)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)

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

    slope = z.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def slv_drv3_020_piotroski_slope_qoq_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """QoQ change in the 4Q rolling OLS slope of Piotroski F-score."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)

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

    slope = f.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def slv_drv3_021_grand_composite_2nd_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """2nd QoQ diff of the grand solvency composite (5-signal z-avg): jerk in grand score."""
    z_alt = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f_pio = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    roa   = _safe_div(netinc, assets)
    cr    = _safe_div(assetsc, liabilitiesc)
    cfo_r = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(z_alt, _TD_YEAR)
    z2 = _zscore_rolling(f_pio, _TD_YEAR)
    z3 = _zscore_rolling(roa, _TD_YEAR)
    z4 = _zscore_rolling(cr, _TD_YEAR)
    z5 = _zscore_rolling(cfo_r, _TD_YEAR)
    grand = (z1 + z2 + z3 + z4 + z5) / 5.0
    d1 = grand - grand.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_022_distress_breadth_2nd_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, liabilitiesc: pd.Series,
    ebt: pd.Series, revenue: pd.Series, debt: pd.Series,
    assetsc: pd.Series, shareswa: pd.Series, gp: pd.Series,
) -> pd.Series:
    """2nd QoQ diff of distress signal breadth (jerk in number of concurrent distress flags)."""
    z_alt = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f_pio = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    s1 = (z_alt < 1.1).astype(float)
    s2 = (f_pio <= 2).astype(float)
    s3 = (equity < 0).astype(float)
    cr = _safe_div(assetsc, liabilitiesc)
    s4 = (cr < 1.0).astype(float)
    roa_r = _safe_div(ebit, assets)
    s5 = (roa_r < 0).astype(float)
    breadth = s1 + s2 + s3 + s4 + s5
    d1 = breadth - breadth.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv3_023_interest_coverage_3rd_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """3rd QoQ difference of interest coverage ratio: jerk in debt-servicing capacity."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    d1 = cov - cov.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_024_ncfo_to_debt_3rd_diff(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """3rd QoQ difference of NCFo/debt ratio: jerk in cash-flow debt coverage."""
    cov = _safe_div(ncfo, debt.abs().replace(0, np.nan))
    d1 = cov - cov.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def slv_drv3_025_altman_z_rolling_slope_2nd_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """
    2nd QoQ diff of the 4Q OLS slope of Altman Z'' (jerk in slope trend).
    Captures whether the trajectory of the trajectory is stabilizing or accelerating.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)

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

    slope = z.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    d1 = slope - slope.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

SOLVENCY_SCORES_REGISTRY_3RD_DERIVATIVES = {
    "slv_drv3_001_altman_z_3rd_diff_qoq":          {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_001_altman_z_3rd_diff_qoq},
    "slv_drv3_002_piotroski_3rd_diff_qoq":          {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                                  "func": slv_drv3_002_piotroski_3rd_diff_qoq},
    "slv_drv3_003_zmijewski_3rd_diff_qoq":          {"inputs": ["netinc", "assets", "liabilities", "assetsc", "liabilitiesc"],                                                                                                "func": slv_drv3_003_zmijewski_3rd_diff_qoq},
    "slv_drv3_004_springate_3rd_diff_qoq":          {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                                                        "func": slv_drv3_004_springate_3rd_diff_qoq},
    "slv_drv3_005_roa_3rd_diff_qoq":                {"inputs": ["netinc", "assets"],                                                                                                                                          "func": slv_drv3_005_roa_3rd_diff_qoq},
    "slv_drv3_006_leverage_3rd_diff_qoq":           {"inputs": ["liabilities", "assets"],                                                                                                                                     "func": slv_drv3_006_leverage_3rd_diff_qoq},
    "slv_drv3_007_current_ratio_3rd_diff_qoq":      {"inputs": ["assetsc", "liabilitiesc"],                                                                                                                                   "func": slv_drv3_007_current_ratio_3rd_diff_qoq},
    "slv_drv3_008_altman_z_zscore_2nd_diff":        {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_008_altman_z_zscore_2nd_diff},
    "slv_drv3_009_piotroski_zscore_2nd_diff":       {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                                  "func": slv_drv3_009_piotroski_zscore_2nd_diff},
    "slv_drv3_010_altman_z_drawdown_2nd_diff":      {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_010_altman_z_drawdown_2nd_diff},
    "slv_drv3_011_piotroski_drawdown_2nd_diff":     {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                                  "func": slv_drv3_011_piotroski_drawdown_2nd_diff},
    "slv_drv3_012_altman_z_yoy_accel":              {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_012_altman_z_yoy_accel},
    "slv_drv3_013_composite_distress_3rd_diff":     {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"],                                                                    "func": slv_drv3_013_composite_distress_3rd_diff},
    "slv_drv3_014_altman_z_ewm_2nd_diff":           {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_014_altman_z_ewm_2nd_diff},
    "slv_drv3_015_piotroski_ewm_2nd_diff":          {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                                  "func": slv_drv3_015_piotroski_ewm_2nd_diff},
    "slv_drv3_016_altman_z_3rd_diff_yoy":           {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_016_altman_z_3rd_diff_yoy},
    "slv_drv3_017_piotroski_3rd_diff_yoy":          {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                                  "func": slv_drv3_017_piotroski_3rd_diff_yoy},
    "slv_drv3_018_roa_3rd_diff_yoy":                {"inputs": ["netinc", "assets"],                                                                                                                                          "func": slv_drv3_018_roa_3rd_diff_yoy},
    "slv_drv3_019_altman_z_slope_qoq_diff":         {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_019_altman_z_slope_qoq_diff},
    "slv_drv3_020_piotroski_slope_qoq_diff":        {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                                  "func": slv_drv3_020_piotroski_slope_qoq_diff},
    "slv_drv3_021_grand_composite_2nd_diff":        {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],   "func": slv_drv3_021_grand_composite_2nd_diff},
    "slv_drv3_022_distress_breadth_2nd_diff":       {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "liabilitiesc", "ebt", "revenue", "debt", "assetsc", "shareswa", "gp"], "func": slv_drv3_022_distress_breadth_2nd_diff},
    "slv_drv3_023_interest_coverage_3rd_diff":      {"inputs": ["ebit", "intexp"],                                                                                                                                            "func": slv_drv3_023_interest_coverage_3rd_diff},
    "slv_drv3_024_ncfo_to_debt_3rd_diff":           {"inputs": ["ncfo", "debt"],                                                                                                                                              "func": slv_drv3_024_ncfo_to_debt_3rd_diff},
    "slv_drv3_025_altman_z_rolling_slope_2nd_diff": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                                      "func": slv_drv3_025_altman_z_rolling_slope_2nd_diff},
}
