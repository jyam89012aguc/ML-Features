"""
71_accruals_quality — 3rd-Derivative Features 001-025
Domain: rate-of-change of 2nd-derivative accruals-quality features — convexity
of accrual acceleration, jerk in the Sloan ratio trend, momentum-of-momentum
for CFO/netinc, and cross-horizon slope comparisons.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 3rd-derivative series are sparse/stepwise on a daily index because the
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


# ── 2nd-derivative concept helpers (self-contained) ───────────────────────────

def _sloan_ratio(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(netinc - ncfo, assets)


def _sloan_qoq_diff(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    r = _sloan_ratio(netinc, ncfo, assets)
    return r - r.shift(_TD_QTR)


def _cfo_to_netinc(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    return _safe_div_abs(ncfo, netinc)


def _cfo_to_netinc_qoq_diff(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    r = _cfo_to_netinc(netinc, ncfo)
    return r - r.shift(_TD_QTR)


def _wc_accruals(receivables: pd.Series, inventory: pd.Series, payables: pd.Series) -> pd.Series:
    wc = receivables + inventory - payables
    return wc - wc.shift(_TD_QTR)


def _wc_accruals_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                           payables: pd.Series) -> pd.Series:
    base = _wc_accruals(receivables, inventory, payables)
    return base - base.shift(_TD_QTR)


def _ccc(receivables: pd.Series, inventory: pd.Series, payables: pd.Series,
         revenue: pd.Series) -> pd.Series:
    rev_abs = revenue.abs().replace(0, np.nan)
    return (_safe_div(receivables, rev_abs) + _safe_div(inventory, rev_abs)
            - _safe_div(payables, rev_abs)) * 91


def _ccc_qoq_diff(receivables: pd.Series, inventory: pd.Series, payables: pd.Series,
                  revenue: pd.Series) -> pd.Series:
    base = _ccc(receivables, inventory, payables, revenue)
    return base - base.shift(_TD_QTR)


def _accruals_to_rev(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div_abs(netinc - ncfo, revenue)


def _accruals_to_rev_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                revenue: pd.Series) -> pd.Series:
    base = _accruals_to_rev(netinc, ncfo, revenue)
    return base - base.shift(_TD_QTR)


def _cfo_margin(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ncfo, revenue.abs().replace(0, np.nan))


def _cfo_margin_qoq_diff(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    base = _cfo_margin(ncfo, revenue)
    return base - base.shift(_TD_QTR)


def _ttm_accruals_ratio(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    ttm_ni  = netinc.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    ttm_cfo = ncfo.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return _safe_div(ttm_ni - ttm_cfo, assets)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def acq_drv3_001_sloan_ratio_qoq_diff_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                 assets: pd.Series) -> pd.Series:
    """
    Third derivative of Sloan ratio: QoQ diff of (QoQ diff of QoQ diff).
    Captures the jerk (rate of change of acceleration) in accrual deterioration.
    """
    d1 = _sloan_qoq_diff(netinc, ncfo, assets)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_002_sloan_ratio_qoq_diff_yoy_diff(netinc: pd.Series, ncfo: pd.Series,
                                                 assets: pd.Series) -> pd.Series:
    """YoY change of the QoQ diff in Sloan ratio (cross-horizon 3rd derivative)."""
    d1 = _sloan_qoq_diff(netinc, ncfo, assets)
    return d1 - d1.shift(_TD_YEAR)


def acq_drv3_003_cfo_to_netinc_qoq_diff_qoq_diff(netinc: pd.Series,
                                                    ncfo: pd.Series) -> pd.Series:
    """Third derivative of CFO/netinc: QoQ diff of the QoQ diff of the ratio."""
    d1 = _cfo_to_netinc_qoq_diff(netinc, ncfo)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_004_cfo_to_netinc_qoq_diff_yoy_diff(netinc: pd.Series,
                                                    ncfo: pd.Series) -> pd.Series:
    """YoY change of the QoQ diff of CFO/netinc (cross-horizon 3rd derivative)."""
    d1 = _cfo_to_netinc_qoq_diff(netinc, ncfo)
    return d1 - d1.shift(_TD_YEAR)


def acq_drv3_005_wc_accruals_qoq_diff_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                                                  payables: pd.Series) -> pd.Series:
    """Third derivative of WC accruals: jerk in working-capital accrual build-up."""
    d1 = _wc_accruals_qoq_diff(receivables, inventory, payables)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_006_ccc_qoq_diff_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                                         payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of the cash conversion cycle (acceleration of acceleration)."""
    d1 = _ccc_qoq_diff(receivables, inventory, payables, revenue)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_007_accruals_to_rev_qoq_diff_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                      revenue: pd.Series) -> pd.Series:
    """Third derivative of accruals/revenue: jerk in revenue-scaled accrual ratio."""
    d1 = _accruals_to_rev_qoq_diff(netinc, ncfo, revenue)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_008_cfo_margin_qoq_diff_qoq_diff(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of CFO margin: acceleration of cash margin deterioration."""
    d1 = _cfo_margin_qoq_diff(ncfo, revenue)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_009_sloan_ratio_4q_slope_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                 assets: pd.Series) -> pd.Series:
    """
    QoQ change in the 4-quarter OLS slope of the Sloan ratio.
    = rate of change of the accrual-deterioration slope.
    """
    ratio = _sloan_ratio(netinc, ncfo, assets)

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

    slope = ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def acq_drv3_010_cfo_to_netinc_slope_qoq_diff(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """
    QoQ change in the 4-quarter OLS slope of the CFO/netinc ratio.
    Captures whether cash quality erosion trend is itself accelerating.
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

    slope = base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def acq_drv3_011_ttm_accruals_ratio_qoq_diff_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                         assets: pd.Series) -> pd.Series:
    """Third derivative of TTM accruals ratio: jerk in trailing accrual accumulation."""
    base = _ttm_accruals_ratio(netinc, ncfo, assets)
    d1 = base - base.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_012_sloan_ratio_qoq_diff_ewm_diff(netinc: pd.Series, ncfo: pd.Series,
                                                 assets: pd.Series) -> pd.Series:
    """
    QoQ diff of Sloan ratio minus its 4-quarter EWM.
    Measures whether the current accrual acceleration exceeds its own rolling trend.
    """
    d1  = _sloan_qoq_diff(netinc, ncfo, assets)
    ewm = d1.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d1 - ewm


def acq_drv3_013_ccc_yoy_diff_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                                         payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change of the YoY diff of the CCC (mixed-horizon 3rd derivative)."""
    base = _ccc(receivables, inventory, payables, revenue)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def acq_drv3_014_accruals_to_rev_yoy_diff_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                      revenue: pd.Series) -> pd.Series:
    """QoQ change in the YoY diff of accruals/revenue (mixed 3rd derivative)."""
    base = _accruals_to_rev(netinc, ncfo, revenue)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def acq_drv3_015_sloan_ratio_zscore_qoq_diff_qoq_diff(netinc: pd.Series, ncfo: pd.Series,
                                                         assets: pd.Series) -> pd.Series:
    """Third derivative of the z-scored Sloan ratio: jerk in normalized accrual signal."""
    ratio = _sloan_ratio(netinc, ncfo, assets)
    m  = _rolling_mean(ratio, _TD_YEAR)
    sd = _rolling_std(ratio, _TD_YEAR)
    z  = _safe_div(ratio - m, sd)
    d1 = z - z.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def acq_drv3_016_wc_accruals_slope_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                                               payables: pd.Series) -> pd.Series:
    """
    QoQ change in the 4-quarter OLS slope of working-capital accruals.
    Measures whether WC accrual momentum is itself accelerating.
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

    slope = base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def acq_drv3_017_cfo_margin_yoy_diff_qoq_diff(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the YoY diff of CFO margin."""
    base = _cfo_margin(ncfo, revenue)
    d1 = base - base.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_QTR)


def acq_drv3_018_sloan_ratio_2q_vs_4q_slope_diff(netinc: pd.Series, ncfo: pd.Series,
                                                    assets: pd.Series) -> pd.Series:
    """
    Difference between 2-quarter and 4-quarter OLS slopes of Sloan ratio.
    Positive = recent accrual slope is steeper than longer-term trend (acceleration).
    """
    ratio = _sloan_ratio(netinc, ncfo, assets)

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

    slope_2q = ratio.rolling(_TD_2Q, min_periods=max(2, _TD_2Q // 4)).apply(_slope, raw=True)
    slope_4q = ratio.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope_2q - slope_4q


def acq_drv3_019_ccc_2q_vs_4q_slope_diff(receivables: pd.Series, inventory: pd.Series,
                                           payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Difference between 2-quarter and 4-quarter OLS slopes of CCC.
    Positive = recent CCC expansion is accelerating vs medium-term trend.
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

    slope_2q = base.rolling(_TD_2Q, min_periods=max(2, _TD_2Q // 4)).apply(_slope, raw=True)
    slope_4q = base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope_2q - slope_4q


def acq_drv3_020_accruals_to_rev_ewm_diff_qoq(netinc: pd.Series, ncfo: pd.Series,
                                                revenue: pd.Series) -> pd.Series:
    """
    QoQ change of (accruals/revenue minus its 4-quarter EWM).
    Rate of change of the accrual-revenue deviation from trend.
    """
    base = _accruals_to_rev(netinc, ncfo, revenue)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    dev  = base - ewm
    return dev - dev.shift(_TD_QTR)


def acq_drv3_021_sloan_ratio_qoq_diff_zscore_4q(netinc: pd.Series, ncfo: pd.Series,
                                                   assets: pd.Series) -> pd.Series:
    """
    Z-score (4-quarter window) of the QoQ diff of the Sloan ratio.
    Normalizes accrual acceleration against its own recent distribution.
    """
    d1 = _sloan_qoq_diff(netinc, ncfo, assets)
    m  = _rolling_mean(d1, _TD_YEAR)
    sd = _rolling_std(d1, _TD_YEAR)
    return _safe_div(d1 - m, sd)


def acq_drv3_022_cfo_to_netinc_qoq_diff_zscore_4q(netinc: pd.Series,
                                                     ncfo: pd.Series) -> pd.Series:
    """
    Z-score (4-quarter window) of the QoQ diff of CFO/netinc.
    Normalized cash quality acceleration signal.
    """
    d1 = _cfo_to_netinc_qoq_diff(netinc, ncfo)
    m  = _rolling_mean(d1, _TD_YEAR)
    sd = _rolling_std(d1, _TD_YEAR)
    return _safe_div(d1 - m, sd)


def acq_drv3_023_ccc_qoq_diff_zscore_4q(receivables: pd.Series, inventory: pd.Series,
                                          payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score (4-quarter window) of the QoQ diff of CCC."""
    d1 = _ccc_qoq_diff(receivables, inventory, payables, revenue)
    m  = _rolling_mean(d1, _TD_YEAR)
    sd = _rolling_std(d1, _TD_YEAR)
    return _safe_div(d1 - m, sd)


def acq_drv3_024_sloan_ratio_acceleration_cross_horizon(netinc: pd.Series, ncfo: pd.Series,
                                                          assets: pd.Series) -> pd.Series:
    """
    QoQ acceleration of Sloan ratio vs YoY acceleration of Sloan ratio.
    Positive = short-term accrual acceleration is worse than medium-term.
    """
    ratio = _sloan_ratio(netinc, ncfo, assets)
    d1_qoq = ratio - ratio.shift(_TD_QTR)
    d2_qoq = d1_qoq - d1_qoq.shift(_TD_QTR)
    d1_yoy = ratio - ratio.shift(_TD_YEAR)
    d2_yoy = d1_yoy - d1_yoy.shift(_TD_YEAR)
    return d2_qoq - d2_yoy


def acq_drv3_025_accruals_3d_composite(netinc: pd.Series, ncfo: pd.Series,
                                         assets: pd.Series,
                                         receivables: pd.Series,
                                         inventory: pd.Series,
                                         payables: pd.Series,
                                         revenue: pd.Series) -> pd.Series:
    """
    Composite 3rd-derivative accrual quality signal:
    equally weighted z-score sum of (1) jerk in Sloan ratio, (2) jerk in WC accruals/assets,
    (3) jerk in CCC. Higher values = rapidly worsening accrual quality momentum.
    """
    # Sloan jerk
    sloan = _sloan_ratio(netinc, ncfo, assets)
    ds1   = sloan - sloan.shift(_TD_QTR)
    ds2   = ds1 - ds1.shift(_TD_QTR)
    ds3   = ds2 - ds2.shift(_TD_QTR)

    # WC accruals / assets jerk
    wc     = receivables + inventory - payables
    wc_acc = _safe_div(wc - wc.shift(_TD_QTR), assets)
    dw1    = wc_acc - wc_acc.shift(_TD_QTR)
    dw2    = dw1 - dw1.shift(_TD_QTR)
    dw3    = dw2 - dw2.shift(_TD_QTR)

    # CCC jerk
    ccc    = _ccc(receivables, inventory, payables, revenue)
    dc1    = ccc - ccc.shift(_TD_QTR)
    dc2    = dc1 - dc1.shift(_TD_QTR)
    dc3    = dc2 - dc2.shift(_TD_QTR)

    m_s  = _rolling_mean(ds3, _TD_YEAR);  sd_s  = _rolling_std(ds3, _TD_YEAR)
    m_w  = _rolling_mean(dw3, _TD_YEAR);  sd_w  = _rolling_std(dw3, _TD_YEAR)
    m_c  = _rolling_mean(dc3, _TD_YEAR);  sd_c  = _rolling_std(dc3, _TD_YEAR)

    z_s = _safe_div(ds3 - m_s, sd_s)
    z_w = _safe_div(dw3 - m_w, sd_w)
    z_c = _safe_div(dc3 - m_c, sd_c)

    return (z_s + z_w + z_c) / 3.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

ACCRUALS_QUALITY_REGISTRY_3RD_DERIVATIVES = {
    "acq_drv3_001_sloan_ratio_qoq_diff_qoq_diff":         {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_001_sloan_ratio_qoq_diff_qoq_diff},
    "acq_drv3_002_sloan_ratio_qoq_diff_yoy_diff":         {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_002_sloan_ratio_qoq_diff_yoy_diff},
    "acq_drv3_003_cfo_to_netinc_qoq_diff_qoq_diff":       {"inputs": ["netinc", "ncfo"],                                                                    "func": acq_drv3_003_cfo_to_netinc_qoq_diff_qoq_diff},
    "acq_drv3_004_cfo_to_netinc_qoq_diff_yoy_diff":       {"inputs": ["netinc", "ncfo"],                                                                    "func": acq_drv3_004_cfo_to_netinc_qoq_diff_yoy_diff},
    "acq_drv3_005_wc_accruals_qoq_diff_qoq_diff":         {"inputs": ["receivables", "inventory", "payables"],                                              "func": acq_drv3_005_wc_accruals_qoq_diff_qoq_diff},
    "acq_drv3_006_ccc_qoq_diff_qoq_diff":                 {"inputs": ["receivables", "inventory", "payables", "revenue"],                                   "func": acq_drv3_006_ccc_qoq_diff_qoq_diff},
    "acq_drv3_007_accruals_to_rev_qoq_diff_qoq_diff":     {"inputs": ["netinc", "ncfo", "revenue"],                                                         "func": acq_drv3_007_accruals_to_rev_qoq_diff_qoq_diff},
    "acq_drv3_008_cfo_margin_qoq_diff_qoq_diff":          {"inputs": ["ncfo", "revenue"],                                                                   "func": acq_drv3_008_cfo_margin_qoq_diff_qoq_diff},
    "acq_drv3_009_sloan_ratio_4q_slope_qoq_diff":         {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_009_sloan_ratio_4q_slope_qoq_diff},
    "acq_drv3_010_cfo_to_netinc_slope_qoq_diff":          {"inputs": ["netinc", "ncfo"],                                                                    "func": acq_drv3_010_cfo_to_netinc_slope_qoq_diff},
    "acq_drv3_011_ttm_accruals_ratio_qoq_diff_qoq_diff":  {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_011_ttm_accruals_ratio_qoq_diff_qoq_diff},
    "acq_drv3_012_sloan_ratio_qoq_diff_ewm_diff":         {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_012_sloan_ratio_qoq_diff_ewm_diff},
    "acq_drv3_013_ccc_yoy_diff_qoq_diff":                 {"inputs": ["receivables", "inventory", "payables", "revenue"],                                   "func": acq_drv3_013_ccc_yoy_diff_qoq_diff},
    "acq_drv3_014_accruals_to_rev_yoy_diff_qoq_diff":     {"inputs": ["netinc", "ncfo", "revenue"],                                                         "func": acq_drv3_014_accruals_to_rev_yoy_diff_qoq_diff},
    "acq_drv3_015_sloan_ratio_zscore_qoq_diff_qoq_diff":  {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_015_sloan_ratio_zscore_qoq_diff_qoq_diff},
    "acq_drv3_016_wc_accruals_slope_qoq_diff":            {"inputs": ["receivables", "inventory", "payables"],                                              "func": acq_drv3_016_wc_accruals_slope_qoq_diff},
    "acq_drv3_017_cfo_margin_yoy_diff_qoq_diff":          {"inputs": ["ncfo", "revenue"],                                                                   "func": acq_drv3_017_cfo_margin_yoy_diff_qoq_diff},
    "acq_drv3_018_sloan_ratio_2q_vs_4q_slope_diff":       {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_018_sloan_ratio_2q_vs_4q_slope_diff},
    "acq_drv3_019_ccc_2q_vs_4q_slope_diff":               {"inputs": ["receivables", "inventory", "payables", "revenue"],                                   "func": acq_drv3_019_ccc_2q_vs_4q_slope_diff},
    "acq_drv3_020_accruals_to_rev_ewm_diff_qoq":          {"inputs": ["netinc", "ncfo", "revenue"],                                                         "func": acq_drv3_020_accruals_to_rev_ewm_diff_qoq},
    "acq_drv3_021_sloan_ratio_qoq_diff_zscore_4q":        {"inputs": ["netinc", "ncfo", "assets"],                                                          "func": acq_drv3_021_sloan_ratio_qoq_diff_zscore_4q},
    "acq_drv3_022_cfo_to_netinc_qoq_diff_zscore_4q":      {"inputs": ["netinc", "ncfo"],                                                                    "func": acq_drv3_022_cfo_to_netinc_qoq_diff_zscore_4q},
    "acq_drv3_023_ccc_qoq_diff_zscore_4q":                {"inputs": ["receivables", "inventory", "payables", "revenue"],                                   "func": acq_drv3_023_ccc_qoq_diff_zscore_4q},
    "acq_drv3_024_sloan_ratio_acceleration_cross_horizon": {"inputs": ["netinc", "ncfo", "assets"],                                                         "func": acq_drv3_024_sloan_ratio_acceleration_cross_horizon},
    "acq_drv3_025_accruals_3d_composite":                 {"inputs": ["netinc", "ncfo", "assets", "receivables", "inventory", "payables", "revenue"],       "func": acq_drv3_025_accruals_3d_composite},
}
