"""
72_solvency_scores — 2nd-Derivative Features 001-025
Domain: rate of change of base solvency/distress score features
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
The 2nd-derivative series are sparse/stepwise on a daily index because the
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


# ── Base recompute helpers (self-contained; no cross-file import) ─────────────

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


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def slv_drv2_001_altman_z_qoq_diff_of_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """2nd QoQ difference of Altman Z'': acceleration of score decline/improvement."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    d1 = z - z.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_002_altman_z_yoy_diff_of_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in the YoY Altman Z'' change (cross-horizon 2nd derivative)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    d_yoy = z - z.shift(_TD_YEAR)
    return d_yoy - d_yoy.shift(_TD_QTR)


def slv_drv2_003_piotroski_qoq_diff_of_qoq_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """2nd QoQ difference of Piotroski F-score: acceleration of F-score change."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    d1 = f - f.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_004_piotroski_yoy_diff_qoq(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """QoQ change in the YoY Piotroski F-score change."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    d_yoy = f - f.shift(_TD_YEAR)
    return d_yoy - d_yoy.shift(_TD_QTR)


def slv_drv2_005_zmijewski_qoq_diff_of_qoq(
    netinc: pd.Series, assets: pd.Series, liabilities: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series,
) -> pd.Series:
    """2nd QoQ difference of Zmijewski-style score."""
    z = _zmijewski(netinc, assets, liabilities, assetsc, liabilitiesc)
    d1 = z - z.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_006_springate_qoq_diff_of_qoq(
    workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series,
    ebt: pd.Series, liabilitiesc: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """2nd QoQ difference of Springate-style score."""
    s = _springate(workingcapital, assets, ebit, ebt, liabilitiesc, revenue)
    d1 = s - s.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_007_altman_z_zscore_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in the 4Q z-score of Altman Z'' (how fast normalized rank is shifting)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    zz = _zscore_rolling(z, _TD_YEAR)
    return zz - zz.shift(_TD_QTR)


def slv_drv2_008_piotroski_zscore_qoq_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """QoQ change in the 4Q z-score of Piotroski F-score."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    zf = _zscore_rolling(f, _TD_YEAR)
    return zf - zf.shift(_TD_QTR)


def slv_drv2_009_altman_z_drawdown_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in Altman Z'' drawdown from its 1-year peak (is drawdown worsening?)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    dd = z - _rolling_max(z, _TD_YEAR)
    return dd - dd.shift(_TD_QTR)


def slv_drv2_010_piotroski_drawdown_qoq_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """QoQ change in Piotroski F-score drawdown from its 1-year peak."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    dd = f - _rolling_max(f, _TD_YEAR)
    return dd - dd.shift(_TD_QTR)


def slv_drv2_011_roa_qoq_diff_of_qoq(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """2nd QoQ difference of ROA (netinc/assets): ROA acceleration."""
    roa = _safe_div(netinc, assets)
    d1 = roa - roa.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_012_leverage_qoq_diff_of_qoq(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """2nd QoQ difference of leverage (liabilities/assets): leverage acceleration."""
    lev = _safe_div(liabilities, assets)
    d1 = lev - lev.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_013_current_ratio_qoq_diff_of_qoq(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """2nd QoQ difference of current ratio: liquidity acceleration."""
    cr = _safe_div(assetsc, liabilitiesc)
    d1 = cr - cr.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_014_altman_x1_qoq_diff_of_qoq(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """2nd QoQ difference of Altman X1 (wc/assets): working-capital ratio acceleration."""
    x1 = _safe_div(workingcapital, assets)
    d1 = x1 - x1.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_015_altman_x4_qoq_diff_of_qoq(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """2nd QoQ difference of Altman X4 (equity/liabilities): capital buffer acceleration."""
    x4 = _safe_div(equity, liabilities)
    d1 = x4 - x4.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_016_altman_z_slope_4q(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of Altman Z'' score.
    Scalar helper avoids passing array-returning functions to rolling.apply.
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

    return z.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def slv_drv2_017_piotroski_slope_4q(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Rolling 4-quarter OLS slope of Piotroski F-score."""
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

    return f.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def slv_drv2_018_altman_z_yoy_pct_change_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in the YoY percent change of Altman Z'' (2nd-order YoY)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    prior = z.shift(_TD_YEAR)
    pct = _safe_div_abs(z - prior, prior)
    return pct - pct.shift(_TD_QTR)


def slv_drv2_019_distress_signal_breadth_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, liabilitiesc: pd.Series,
    ebt: pd.Series, revenue: pd.Series, debt: pd.Series,
    assetsc: pd.Series, shareswa: pd.Series, gp: pd.Series,
) -> pd.Series:
    """QoQ change in distress signal breadth (how many more/fewer models flag distress)."""
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
    return breadth - breadth.shift(_TD_QTR)


def slv_drv2_020_composite_distress_yoy_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """YoY change in the custom composite distress index (5-ratio z-score average)."""
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
    composite = (z1 + z2 + z3 + z4 + z5) / 5.0
    return composite - composite.shift(_TD_YEAR)


def slv_drv2_021_altman_z_ewm_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in the EWM (span=252) of Altman Z'' (trend momentum change)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    ewm = z.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return ewm - ewm.shift(_TD_QTR)


def slv_drv2_022_piotroski_ewm_qoq_diff(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """QoQ change in the EWM (span=252) of Piotroski F-score."""
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    ewm = f.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return ewm - ewm.shift(_TD_QTR)


def slv_drv2_023_ncfo_to_debt_qoq_diff_of_qoq(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """2nd QoQ difference of NCFo/debt coverage ratio."""
    cov = _safe_div(ncfo, debt.abs().replace(0, np.nan))
    d1 = cov - cov.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_024_interest_coverage_qoq_diff_of_qoq(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """2nd QoQ difference of interest coverage ratio (ebit/intexp)."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    d1 = cov - cov.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def slv_drv2_025_solvency_grand_composite_qoq_diff(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """QoQ change in the grand solvency composite (5-signal z-score average)."""
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
    return grand - grand.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

SOLVENCY_SCORES_REGISTRY_2ND_DERIVATIVES = {
    "slv_drv2_001_altman_z_qoq_diff_of_qoq_diff":      {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                             "func": slv_drv2_001_altman_z_qoq_diff_of_qoq_diff},
    "slv_drv2_002_altman_z_yoy_diff_of_qoq_diff":      {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                             "func": slv_drv2_002_altman_z_yoy_diff_of_qoq_diff},
    "slv_drv2_003_piotroski_qoq_diff_of_qoq_diff":     {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                         "func": slv_drv2_003_piotroski_qoq_diff_of_qoq_diff},
    "slv_drv2_004_piotroski_yoy_diff_qoq":              {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                         "func": slv_drv2_004_piotroski_yoy_diff_qoq},
    "slv_drv2_005_zmijewski_qoq_diff_of_qoq":           {"inputs": ["netinc", "assets", "liabilities", "assetsc", "liabilitiesc"],                                                                                       "func": slv_drv2_005_zmijewski_qoq_diff_of_qoq},
    "slv_drv2_006_springate_qoq_diff_of_qoq":           {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                                               "func": slv_drv2_006_springate_qoq_diff_of_qoq},
    "slv_drv2_007_altman_z_zscore_qoq_diff":            {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                             "func": slv_drv2_007_altman_z_zscore_qoq_diff},
    "slv_drv2_008_piotroski_zscore_qoq_diff":           {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                         "func": slv_drv2_008_piotroski_zscore_qoq_diff},
    "slv_drv2_009_altman_z_drawdown_qoq_diff":          {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                             "func": slv_drv2_009_altman_z_drawdown_qoq_diff},
    "slv_drv2_010_piotroski_drawdown_qoq_diff":         {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                         "func": slv_drv2_010_piotroski_drawdown_qoq_diff},
    "slv_drv2_011_roa_qoq_diff_of_qoq":                 {"inputs": ["netinc", "assets"],                                                                                                                                 "func": slv_drv2_011_roa_qoq_diff_of_qoq},
    "slv_drv2_012_leverage_qoq_diff_of_qoq":            {"inputs": ["liabilities", "assets"],                                                                                                                            "func": slv_drv2_012_leverage_qoq_diff_of_qoq},
    "slv_drv2_013_current_ratio_qoq_diff_of_qoq":       {"inputs": ["assetsc", "liabilitiesc"],                                                                                                                          "func": slv_drv2_013_current_ratio_qoq_diff_of_qoq},
    "slv_drv2_014_altman_x1_qoq_diff_of_qoq":           {"inputs": ["workingcapital", "assets"],                                                                                                                         "func": slv_drv2_014_altman_x1_qoq_diff_of_qoq},
    "slv_drv2_015_altman_x4_qoq_diff_of_qoq":           {"inputs": ["equity", "liabilities"],                                                                                                                            "func": slv_drv2_015_altman_x4_qoq_diff_of_qoq},
    "slv_drv2_016_altman_z_slope_4q":                   {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                             "func": slv_drv2_016_altman_z_slope_4q},
    "slv_drv2_017_piotroski_slope_4q":                  {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                         "func": slv_drv2_017_piotroski_slope_4q},
    "slv_drv2_018_altman_z_yoy_pct_change_qoq_diff":    {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                             "func": slv_drv2_018_altman_z_yoy_pct_change_qoq_diff},
    "slv_drv2_019_distress_signal_breadth_qoq_diff":    {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "liabilitiesc", "ebt", "revenue", "debt", "assetsc", "shareswa", "gp"], "func": slv_drv2_019_distress_signal_breadth_qoq_diff},
    "slv_drv2_020_composite_distress_yoy_diff":         {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"],                                                           "func": slv_drv2_020_composite_distress_yoy_diff},
    "slv_drv2_021_altman_z_ewm_qoq_diff":               {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                                             "func": slv_drv2_021_altman_z_ewm_qoq_diff},
    "slv_drv2_022_piotroski_ewm_qoq_diff":              {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                                         "func": slv_drv2_022_piotroski_ewm_qoq_diff},
    "slv_drv2_023_ncfo_to_debt_qoq_diff_of_qoq":        {"inputs": ["ncfo", "debt"],                                                                                                                                     "func": slv_drv2_023_ncfo_to_debt_qoq_diff_of_qoq},
    "slv_drv2_024_interest_coverage_qoq_diff_of_qoq":   {"inputs": ["ebit", "intexp"],                                                                                                                                   "func": slv_drv2_024_interest_coverage_qoq_diff_of_qoq},
    "slv_drv2_025_solvency_grand_composite_qoq_diff":   {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"], "func": slv_drv2_025_solvency_grand_composite_qoq_diff},
}
