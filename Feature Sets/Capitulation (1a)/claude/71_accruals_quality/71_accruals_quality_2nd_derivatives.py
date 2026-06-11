"""
71_accruals_quality — 2nd-Derivative Features 001-025
Domain: rate-of-change of base accruals-quality features — acceleration of
accrual deterioration, momentum of the CFO/netinc gap, velocity of working-
capital accruals, and slope signals for Sloan ratio and CCC trends.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 2nd-derivative series are sparse/stepwise on a daily index because the
underlying data is quarterly — this is correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file receive Series already prepared this way;
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


# ── Base concept helpers (self-contained; no cross-file imports) ──────────────

def _sloan_ratio(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(netinc - ncfo, assets)


def _cfo_to_netinc(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    return _safe_div_abs(ncfo, netinc)


def _wc_accruals(receivables: pd.Series, inventory: pd.Series, payables: pd.Series) -> pd.Series:
    wc = receivables + inventory - payables
    return wc - wc.shift(_TD_QTR)


def _ccc(receivables: pd.Series, inventory: pd.Series, payables: pd.Series,
         revenue: pd.Series) -> pd.Series:
    rev_abs = revenue.abs().replace(0, np.nan)
    return (_safe_div(receivables, rev_abs) + _safe_div(inventory, rev_abs)
            - _safe_div(payables, rev_abs)) * 91


def _ttm_accruals_ratio(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    ttm_ni  = netinc.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    ttm_cfo = ncfo.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return _safe_div(ttm_ni - ttm_cfo, assets)


def _accruals_to_revenue(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div_abs(netinc - ncfo, revenue)


def _cfo_margin(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ncfo, revenue.abs().replace(0, np.nan))


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def acq_drv2_001_sloan_ratio_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                       assets: pd.Series) -> pd.Series:
    """QoQ change in the Sloan accruals ratio (first derivative = acceleration of accruals)."""
    base = _sloan_ratio(netinc, ncfo, assets)
    return base - base.shift(_TD_QTR)


def acq_drv2_002_sloan_ratio_yoy_diff(netinc: pd.Series, ncfo: pd.Series,
                                       assets: pd.Series) -> pd.Series:
    """YoY change in the Sloan accruals ratio."""
    base = _sloan_ratio(netinc, ncfo, assets)
    return base - base.shift(_TD_YEAR)


def acq_drv2_003_sloan_ratio_qoq_pct_chg(netinc: pd.Series, ncfo: pd.Series,
                                           assets: pd.Series) -> pd.Series:
    """QoQ percent change in the Sloan accruals ratio."""
    base = _sloan_ratio(netinc, ncfo, assets)
    prior = base.shift(_TD_QTR)
    return _safe_div_abs(base - prior, prior)


def acq_drv2_004_cfo_to_netinc_qoq_diff(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ change in the CFO/netinc cash backing ratio."""
    base = _cfo_to_netinc(netinc, ncfo)
    return base - base.shift(_TD_QTR)


def acq_drv2_005_cfo_to_netinc_yoy_diff(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """YoY change in the CFO/netinc cash backing ratio."""
    base = _cfo_to_netinc(netinc, ncfo)
    return base - base.shift(_TD_YEAR)


def acq_drv2_006_wc_accruals_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                                        payables: pd.Series) -> pd.Series:
    """QoQ change in working-capital accruals (second difference of WC)."""
    base = _wc_accruals(receivables, inventory, payables)
    return base - base.shift(_TD_QTR)


def acq_drv2_007_wc_accruals_yoy_diff(receivables: pd.Series, inventory: pd.Series,
                                        payables: pd.Series) -> pd.Series:
    """YoY change in working-capital accruals."""
    base = _wc_accruals(receivables, inventory, payables)
    return base - base.shift(_TD_YEAR)


def acq_drv2_008_ccc_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                                payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the cash conversion cycle (rate of CCC expansion)."""
    base = _ccc(receivables, inventory, payables, revenue)
    return base - base.shift(_TD_QTR)


def acq_drv2_009_ccc_yoy_diff(receivables: pd.Series, inventory: pd.Series,
                                payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in the cash conversion cycle."""
    base = _ccc(receivables, inventory, payables, revenue)
    return base - base.shift(_TD_YEAR)


def acq_drv2_010_ttm_accruals_ratio_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                               assets: pd.Series) -> pd.Series:
    """QoQ change in the TTM accruals ratio (acceleration of trailing accruals)."""
    base = _ttm_accruals_ratio(netinc, ncfo, assets)
    return base - base.shift(_TD_QTR)


def acq_drv2_011_accruals_to_revenue_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                revenue: pd.Series) -> pd.Series:
    """QoQ change in the accruals/revenue ratio."""
    base = _accruals_to_revenue(netinc, ncfo, revenue)
    return base - base.shift(_TD_QTR)


def acq_drv2_012_accruals_to_revenue_yoy_diff(netinc: pd.Series, ncfo: pd.Series,
                                                revenue: pd.Series) -> pd.Series:
    """YoY change in the accruals/revenue ratio."""
    base = _accruals_to_revenue(netinc, ncfo, revenue)
    return base - base.shift(_TD_YEAR)


def acq_drv2_013_cfo_margin_qoq_diff(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in CFO margin (rate of cash margin erosion)."""
    base = _cfo_margin(ncfo, revenue)
    return base - base.shift(_TD_QTR)


def acq_drv2_014_sloan_ratio_4q_slope(netinc: pd.Series, ncfo: pd.Series,
                                       assets: pd.Series) -> pd.Series:
    """
    OLS slope of the Sloan accruals ratio over trailing 4-quarter window.
    Directly captures the trend direction of accrual deterioration.
    """
    base = _sloan_ratio(netinc, ncfo, assets)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def acq_drv2_015_cfo_to_netinc_4q_slope(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """
    OLS slope of CFO/netinc ratio over trailing 4-quarter window.
    Negative slope = cash quality eroding over time.
    """
    base = _cfo_to_netinc(netinc, ncfo)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def acq_drv2_016_sloan_ratio_qoq_diff_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                 assets: pd.Series) -> pd.Series:
    """
    Second derivative of Sloan ratio: QoQ diff of (QoQ diff of Sloan ratio).
    Captures convexity/acceleration in accrual deterioration.
    """
    base = _sloan_ratio(netinc, ncfo, assets)
    d1 = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def acq_drv2_017_cfo_to_netinc_ewm_diff(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """
    CFO/netinc ratio minus its 4-quarter EWM.
    Negative = current cash quality is below its own recent trend.
    """
    base = _cfo_to_netinc(netinc, ncfo)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def acq_drv2_018_wc_accruals_4q_slope(receivables: pd.Series, inventory: pd.Series,
                                        payables: pd.Series) -> pd.Series:
    """
    OLS slope of working-capital accruals over trailing 4-quarter window.
    Captures momentum in WC accrual build-up.
    """
    base = _wc_accruals(receivables, inventory, payables)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def acq_drv2_019_sloan_ratio_zscore_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                               assets: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter rolling z-score of the Sloan accruals ratio."""
    ratio = _sloan_ratio(netinc, ncfo, assets)
    m  = _rolling_mean(ratio, _TD_YEAR)
    sd = _rolling_std(ratio, _TD_YEAR)
    zscore = _safe_div(ratio - m, sd)
    return zscore - zscore.shift(_TD_QTR)


def acq_drv2_020_ccc_4q_slope(receivables: pd.Series, inventory: pd.Series,
                                payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    OLS slope of the cash conversion cycle over trailing 4-quarter window.
    Rising slope = worsening working-capital efficiency trend.
    """
    base = _ccc(receivables, inventory, payables, revenue)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def acq_drv2_021_accruals_to_revenue_4q_slope(netinc: pd.Series, ncfo: pd.Series,
                                                revenue: pd.Series) -> pd.Series:
    """OLS slope of accruals/revenue ratio over trailing 4-quarter window."""
    base = _accruals_to_revenue(netinc, ncfo, revenue)

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

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def acq_drv2_022_total_accruals_qoq_pct_chg(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ percent change in total accruals (netinc - ncfo)."""
    base  = netinc - ncfo
    prior = base.shift(_TD_QTR)
    return _safe_div_abs(base - prior, prior)


def acq_drv2_023_sloan_ratio_yoy_zscore_diff(netinc: pd.Series, ncfo: pd.Series,
                                               assets: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of the Sloan accruals ratio."""
    ratio = _sloan_ratio(netinc, ncfo, assets)
    m  = _rolling_mean(ratio, _TD_YEAR)
    sd = _rolling_std(ratio, _TD_YEAR)
    zscore = _safe_div(ratio - m, sd)
    return zscore - zscore.shift(_TD_YEAR)


def acq_drv2_024_cfo_margin_yoy_diff(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in CFO margin."""
    base = _cfo_margin(ncfo, revenue)
    return base - base.shift(_TD_YEAR)


def acq_drv2_025_accruals_composite_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                               assets: pd.Series,
                                               receivables: pd.Series,
                                               inventory: pd.Series,
                                               payables: pd.Series) -> pd.Series:
    """
    QoQ change in the composite accrual quality z-score
    (z(Sloan ratio) + z(WC accruals/assets)) / 2 — acceleration of composite deterioration.
    """
    sloan = _sloan_ratio(netinc, ncfo, assets)
    wc = receivables + inventory - payables
    wc_acc = _safe_div(wc - wc.shift(_TD_QTR), assets)

    m1  = _rolling_mean(sloan, _TD_YEAR)
    sd1 = _rolling_std(sloan, _TD_YEAR)
    z1  = _safe_div(sloan - m1, sd1)

    m2  = _rolling_mean(wc_acc, _TD_YEAR)
    sd2 = _rolling_std(wc_acc, _TD_YEAR)
    z2  = _safe_div(wc_acc - m2, sd2)

    composite = (z1 + z2) / 2.0
    return composite - composite.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

ACCRUALS_QUALITY_REGISTRY_2ND_DERIVATIVES = {
    "acq_drv2_001_sloan_ratio_qoq_diff":             {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_001_sloan_ratio_qoq_diff},
    "acq_drv2_002_sloan_ratio_yoy_diff":             {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_002_sloan_ratio_yoy_diff},
    "acq_drv2_003_sloan_ratio_qoq_pct_chg":          {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_003_sloan_ratio_qoq_pct_chg},
    "acq_drv2_004_cfo_to_netinc_qoq_diff":           {"inputs": ["netinc", "ncfo"],                                                    "func": acq_drv2_004_cfo_to_netinc_qoq_diff},
    "acq_drv2_005_cfo_to_netinc_yoy_diff":           {"inputs": ["netinc", "ncfo"],                                                    "func": acq_drv2_005_cfo_to_netinc_yoy_diff},
    "acq_drv2_006_wc_accruals_qoq_diff":             {"inputs": ["receivables", "inventory", "payables"],                              "func": acq_drv2_006_wc_accruals_qoq_diff},
    "acq_drv2_007_wc_accruals_yoy_diff":             {"inputs": ["receivables", "inventory", "payables"],                              "func": acq_drv2_007_wc_accruals_yoy_diff},
    "acq_drv2_008_ccc_qoq_diff":                     {"inputs": ["receivables", "inventory", "payables", "revenue"],                   "func": acq_drv2_008_ccc_qoq_diff},
    "acq_drv2_009_ccc_yoy_diff":                     {"inputs": ["receivables", "inventory", "payables", "revenue"],                   "func": acq_drv2_009_ccc_yoy_diff},
    "acq_drv2_010_ttm_accruals_ratio_qoq_diff":      {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_010_ttm_accruals_ratio_qoq_diff},
    "acq_drv2_011_accruals_to_revenue_qoq_diff":     {"inputs": ["netinc", "ncfo", "revenue"],                                         "func": acq_drv2_011_accruals_to_revenue_qoq_diff},
    "acq_drv2_012_accruals_to_revenue_yoy_diff":     {"inputs": ["netinc", "ncfo", "revenue"],                                         "func": acq_drv2_012_accruals_to_revenue_yoy_diff},
    "acq_drv2_013_cfo_margin_qoq_diff":              {"inputs": ["ncfo", "revenue"],                                                    "func": acq_drv2_013_cfo_margin_qoq_diff},
    "acq_drv2_014_sloan_ratio_4q_slope":             {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_014_sloan_ratio_4q_slope},
    "acq_drv2_015_cfo_to_netinc_4q_slope":           {"inputs": ["netinc", "ncfo"],                                                    "func": acq_drv2_015_cfo_to_netinc_4q_slope},
    "acq_drv2_016_sloan_ratio_qoq_diff_qoq_diff":    {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_016_sloan_ratio_qoq_diff_qoq_diff},
    "acq_drv2_017_cfo_to_netinc_ewm_diff":           {"inputs": ["netinc", "ncfo"],                                                    "func": acq_drv2_017_cfo_to_netinc_ewm_diff},
    "acq_drv2_018_wc_accruals_4q_slope":             {"inputs": ["receivables", "inventory", "payables"],                              "func": acq_drv2_018_wc_accruals_4q_slope},
    "acq_drv2_019_sloan_ratio_zscore_qoq_diff":      {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_019_sloan_ratio_zscore_qoq_diff},
    "acq_drv2_020_ccc_4q_slope":                     {"inputs": ["receivables", "inventory", "payables", "revenue"],                   "func": acq_drv2_020_ccc_4q_slope},
    "acq_drv2_021_accruals_to_revenue_4q_slope":     {"inputs": ["netinc", "ncfo", "revenue"],                                         "func": acq_drv2_021_accruals_to_revenue_4q_slope},
    "acq_drv2_022_total_accruals_qoq_pct_chg":       {"inputs": ["netinc", "ncfo"],                                                    "func": acq_drv2_022_total_accruals_qoq_pct_chg},
    "acq_drv2_023_sloan_ratio_yoy_zscore_diff":      {"inputs": ["netinc", "ncfo", "assets"],                                          "func": acq_drv2_023_sloan_ratio_yoy_zscore_diff},
    "acq_drv2_024_cfo_margin_yoy_diff":              {"inputs": ["ncfo", "revenue"],                                                    "func": acq_drv2_024_cfo_margin_yoy_diff},
    "acq_drv2_025_accruals_composite_qoq_diff":      {"inputs": ["netinc", "ncfo", "assets", "receivables", "inventory", "payables"],  "func": acq_drv2_025_accruals_composite_qoq_diff},
}
