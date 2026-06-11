"""
74_fundamental_momentum — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative fundamental-momentum features
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ols_slope(arr):
    """Scalar OLS slope for use with rolling().apply(raw=True)."""
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = ((x - xm) ** 2).sum()
    if denom == 0.0:
        return np.nan
    return ((x - xm) * (arr - ym)).sum() / denom


def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_ols_slope, raw=True)


# ── 2nd-derivative inline helpers (self-contained recomputes) ─────────────────

def _revenue_slope_4q(revenue: pd.Series) -> pd.Series:
    return _rolling_slope(revenue, _TD_YEAR)


def _netinc_slope_4q(netinc: pd.Series) -> pd.Series:
    return _rolling_slope(netinc, _TD_YEAR)


def _eps_slope_4q(eps: pd.Series) -> pd.Series:
    return _rolling_slope(eps, _TD_YEAR)


def _ebitda_slope_4q(ebitda: pd.Series) -> pd.Series:
    return _rolling_slope(ebitda, _TD_YEAR)


def _fcf_slope_4q(fcf: pd.Series) -> pd.Series:
    return _rolling_slope(fcf, _TD_YEAR)


def _revenue_slope_4q_qoq_diff(revenue: pd.Series) -> pd.Series:
    """2nd-derivative: QoQ change in the 4-quarter OLS slope of revenue."""
    base = _revenue_slope_4q(revenue)
    return base - base.shift(_TD_QTR)


def _netinc_slope_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """2nd-derivative: QoQ change in the 4-quarter OLS slope of net income."""
    base = _netinc_slope_4q(netinc)
    return base - base.shift(_TD_QTR)


def _eps_slope_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    """2nd-derivative: QoQ change in the 4-quarter OLS slope of EPS."""
    base = _eps_slope_4q(eps)
    return base - base.shift(_TD_QTR)


def _ebitda_slope_4q_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """2nd-derivative: QoQ change in the 4-quarter OLS slope of EBITDA."""
    base = _ebitda_slope_4q(ebitda)
    return base - base.shift(_TD_QTR)


def _fcf_slope_4q_qoq_diff(fcf: pd.Series) -> pd.Series:
    """2nd-derivative: QoQ change in the 4-quarter OLS slope of FCF."""
    base = _fcf_slope_4q(fcf)
    return base - base.shift(_TD_QTR)


def _revenue_qoq_accel(revenue: pd.Series) -> pd.Series:
    d1 = revenue - revenue.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _netinc_qoq_accel(netinc: pd.Series) -> pd.Series:
    d1 = netinc - netinc.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _eps_qoq_accel(eps: pd.Series) -> pd.Series:
    d1 = eps - eps.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _ebitda_qoq_accel(ebitda: pd.Series) -> pd.Series:
    d1 = ebitda - ebitda.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _breadth_net_improving_qoq(metrics):
    return sum(np.sign(m - m.shift(_TD_QTR)) for m in metrics).astype(float)


def _trend_persistence(m: pd.Series, w: int) -> pd.Series:
    improving = (m > m.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, w)


def _netinc_zscore_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    base = _zscore_rolling(netinc, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def _revenue_zscore_4q_qoq_diff(revenue: pd.Series) -> pd.Series:
    base = _zscore_rolling(revenue, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def _eps_zscore_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    base = _zscore_rolling(eps, _TD_YEAR)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def fmo_drv3_001_revenue_slope_qoq_diff_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative revenue slope-diff (3rd order)."""
    d2 = _revenue_slope_4q_qoq_diff(revenue)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_002_netinc_slope_qoq_diff_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative net income slope-diff (3rd order)."""
    d2 = _netinc_slope_4q_qoq_diff(netinc)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_003_eps_slope_qoq_diff_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative EPS slope-diff (3rd order)."""
    d2 = _eps_slope_4q_qoq_diff(eps)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_004_ebitda_slope_qoq_diff_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative EBITDA slope-diff (3rd order)."""
    d2 = _ebitda_slope_4q_qoq_diff(ebitda)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_005_fcf_slope_qoq_diff_qoq_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative FCF slope-diff (3rd order)."""
    d2 = _fcf_slope_4q_qoq_diff(fcf)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_006_revenue_qoq_accel_qoq_diff_qoq_diff(revenue: pd.Series) -> pd.Series:
    """3rd difference of revenue over 63-day steps (QoQ jerk)."""
    d2 = _revenue_qoq_accel(revenue) - _revenue_qoq_accel(revenue).shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_007_netinc_qoq_accel_qoq_diff_qoq_diff(netinc: pd.Series) -> pd.Series:
    """3rd difference of net income over 63-day steps (net income QoQ jerk)."""
    accel = _netinc_qoq_accel(netinc)
    d2 = accel - accel.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_008_eps_qoq_accel_qoq_diff_qoq_diff(eps: pd.Series) -> pd.Series:
    """3rd difference of EPS over 63-day steps (EPS QoQ jerk)."""
    accel = _eps_qoq_accel(eps)
    d2 = accel - accel.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_009_ebitda_qoq_accel_qoq_diff_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """3rd difference of EBITDA over 63-day steps."""
    accel = _ebitda_qoq_accel(ebitda)
    d2 = accel - accel.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_010_breadth_net_improving_qoq_yoy_diff_qoq_diff(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """QoQ change in the YoY diff of QoQ net-improving breadth (3rd order)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    base = _breadth_net_improving_qoq(metrics)
    d2 = base - base.shift(_TD_YEAR)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_011_revenue_trend_persistence_qoq_diff_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative (QoQ diff) of revenue trend persistence."""
    base = _trend_persistence(revenue, _TD_YEAR)
    d2 = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_012_netinc_trend_persistence_qoq_diff_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative (QoQ diff) of net income trend persistence."""
    base = _trend_persistence(netinc, _TD_YEAR)
    d2 = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_013_netinc_zscore_qoq_diff_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative (QoQ diff) of net income 4Q z-score."""
    d2 = _netinc_zscore_4q_qoq_diff(netinc)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_014_revenue_zscore_qoq_diff_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative (QoQ diff) of revenue 4Q z-score."""
    d2 = _revenue_zscore_4q_qoq_diff(revenue)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_015_eps_zscore_qoq_diff_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change of the 2nd-derivative (QoQ diff) of EPS 4Q z-score."""
    d2 = _eps_zscore_4q_qoq_diff(eps)
    return d2 - d2.shift(_TD_QTR)


def fmo_drv3_016_revenue_slope_4q_rolling_std_qoq_diff(revenue: pd.Series) -> pd.Series:
    """
    QoQ change in the rolling std of the 4-quarter revenue slope
    (volatility of slope momentum, differenced).
    """
    slope = _revenue_slope_4q(revenue)
    vol = _rolling_std(slope, _TD_YEAR)
    return vol - vol.shift(_TD_QTR)


def fmo_drv3_017_netinc_slope_4q_rolling_std_qoq_diff(netinc: pd.Series) -> pd.Series:
    """
    QoQ change in the rolling std of the 4-quarter net income slope.
    """
    slope = _netinc_slope_4q(netinc)
    vol = _rolling_std(slope, _TD_YEAR)
    return vol - vol.shift(_TD_QTR)


def fmo_drv3_018_revenue_qoq_accel_rolling_mean_qoq_diff(revenue: pd.Series) -> pd.Series:
    """
    QoQ change in the rolling 4-quarter mean of revenue QoQ acceleration.
    Smoothed 3rd-order signal for revenue.
    """
    accel = _revenue_qoq_accel(revenue)
    smoothed = _rolling_mean(accel, _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def fmo_drv3_019_netinc_qoq_accel_rolling_mean_qoq_diff(netinc: pd.Series) -> pd.Series:
    """
    QoQ change in the rolling 4-quarter mean of net income QoQ acceleration.
    """
    accel = _netinc_qoq_accel(netinc)
    smoothed = _rolling_mean(accel, _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def fmo_drv3_020_eps_qoq_accel_rolling_mean_qoq_diff(eps: pd.Series) -> pd.Series:
    """
    QoQ change in the rolling 4-quarter mean of EPS QoQ acceleration.
    """
    accel = _eps_qoq_accel(eps)
    smoothed = _rolling_mean(accel, _TD_YEAR)
    return smoothed - smoothed.shift(_TD_QTR)


def fmo_drv3_021_revenue_slope_4q_pct_chg_qoq(revenue: pd.Series) -> pd.Series:
    """
    QoQ percent change in the 4-quarter OLS slope of revenue.
    Captures relative acceleration of slope.
    """
    slope = _revenue_slope_4q(revenue)
    prior = slope.shift(_TD_QTR)
    return _safe_div_abs(slope - prior, prior)


def fmo_drv3_022_netinc_slope_4q_pct_chg_qoq(netinc: pd.Series) -> pd.Series:
    """
    QoQ percent change in the 4-quarter OLS slope of net income.
    """
    slope = _netinc_slope_4q(netinc)
    prior = slope.shift(_TD_QTR)
    return _safe_div_abs(slope - prior, prior)


def fmo_drv3_023_ebitda_slope_4q_pct_chg_qoq(ebitda: pd.Series) -> pd.Series:
    """
    QoQ percent change in the 4-quarter OLS slope of EBITDA.
    """
    slope = _ebitda_slope_4q(ebitda)
    prior = slope.shift(_TD_QTR)
    return _safe_div_abs(slope - prior, prior)


def fmo_drv3_024_breadth_net_improving_qoq_diff_rolling_slope(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ diff of the net-improving breadth count.
    Captures whether breadth momentum is itself trending higher or lower.
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    base = _breadth_net_improving_qoq(metrics)
    d2 = base - base.shift(_TD_QTR)
    return _rolling_slope(d2, _TD_YEAR)


def fmo_drv3_025_composite_3rd_order_momentum_zscore(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series, ebitda: pd.Series
) -> pd.Series:
    """
    Composite 3rd-order momentum z-score:
    equally weighted z-score (4-quarter window) of the QoQ-diff of the
    QoQ-diff of the 4-quarter OLS slope, across revenue, net income,
    EPS, and EBITDA.
    Captures the curvature of slope acceleration.
    """
    d2_rev    = _revenue_slope_4q_qoq_diff(revenue)
    d2_ni     = _netinc_slope_4q_qoq_diff(netinc)
    d2_eps    = _eps_slope_4q_qoq_diff(eps)
    d2_ebitda = _ebitda_slope_4q_qoq_diff(ebitda)

    d3_rev    = d2_rev - d2_rev.shift(_TD_QTR)
    d3_ni     = d2_ni - d2_ni.shift(_TD_QTR)
    d3_eps    = d2_eps - d2_eps.shift(_TD_QTR)
    d3_ebitda = d2_ebitda - d2_ebitda.shift(_TD_QTR)

    z_rev    = _zscore_rolling(d3_rev,    _TD_YEAR)
    z_ni     = _zscore_rolling(d3_ni,     _TD_YEAR)
    z_eps    = _zscore_rolling(d3_eps,    _TD_YEAR)
    z_ebitda = _zscore_rolling(d3_ebitda, _TD_YEAR)

    return (z_rev + z_ni + z_eps + z_ebitda) / 4.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

FUNDAMENTAL_MOMENTUM_REGISTRY_3RD_DERIVATIVES = {
    "fmo_drv3_001_revenue_slope_qoq_diff_qoq_diff":          {"inputs": ["revenue"],                                                                                    "func": fmo_drv3_001_revenue_slope_qoq_diff_qoq_diff},
    "fmo_drv3_002_netinc_slope_qoq_diff_qoq_diff":           {"inputs": ["netinc"],                                                                                     "func": fmo_drv3_002_netinc_slope_qoq_diff_qoq_diff},
    "fmo_drv3_003_eps_slope_qoq_diff_qoq_diff":              {"inputs": ["eps"],                                                                                        "func": fmo_drv3_003_eps_slope_qoq_diff_qoq_diff},
    "fmo_drv3_004_ebitda_slope_qoq_diff_qoq_diff":           {"inputs": ["ebitda"],                                                                                     "func": fmo_drv3_004_ebitda_slope_qoq_diff_qoq_diff},
    "fmo_drv3_005_fcf_slope_qoq_diff_qoq_diff":              {"inputs": ["fcf"],                                                                                        "func": fmo_drv3_005_fcf_slope_qoq_diff_qoq_diff},
    "fmo_drv3_006_revenue_qoq_accel_qoq_diff_qoq_diff":      {"inputs": ["revenue"],                                                                                    "func": fmo_drv3_006_revenue_qoq_accel_qoq_diff_qoq_diff},
    "fmo_drv3_007_netinc_qoq_accel_qoq_diff_qoq_diff":       {"inputs": ["netinc"],                                                                                     "func": fmo_drv3_007_netinc_qoq_accel_qoq_diff_qoq_diff},
    "fmo_drv3_008_eps_qoq_accel_qoq_diff_qoq_diff":          {"inputs": ["eps"],                                                                                        "func": fmo_drv3_008_eps_qoq_accel_qoq_diff_qoq_diff},
    "fmo_drv3_009_ebitda_qoq_accel_qoq_diff_qoq_diff":       {"inputs": ["ebitda"],                                                                                     "func": fmo_drv3_009_ebitda_qoq_accel_qoq_diff_qoq_diff},
    "fmo_drv3_010_breadth_net_improving_qoq_yoy_diff_qoq_diff": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],  "func": fmo_drv3_010_breadth_net_improving_qoq_yoy_diff_qoq_diff},
    "fmo_drv3_011_revenue_trend_persistence_qoq_diff_qoq_diff": {"inputs": ["revenue"],                                                                                 "func": fmo_drv3_011_revenue_trend_persistence_qoq_diff_qoq_diff},
    "fmo_drv3_012_netinc_trend_persistence_qoq_diff_qoq_diff":  {"inputs": ["netinc"],                                                                                  "func": fmo_drv3_012_netinc_trend_persistence_qoq_diff_qoq_diff},
    "fmo_drv3_013_netinc_zscore_qoq_diff_qoq_diff":           {"inputs": ["netinc"],                                                                                    "func": fmo_drv3_013_netinc_zscore_qoq_diff_qoq_diff},
    "fmo_drv3_014_revenue_zscore_qoq_diff_qoq_diff":          {"inputs": ["revenue"],                                                                                   "func": fmo_drv3_014_revenue_zscore_qoq_diff_qoq_diff},
    "fmo_drv3_015_eps_zscore_qoq_diff_qoq_diff":              {"inputs": ["eps"],                                                                                       "func": fmo_drv3_015_eps_zscore_qoq_diff_qoq_diff},
    "fmo_drv3_016_revenue_slope_4q_rolling_std_qoq_diff":     {"inputs": ["revenue"],                                                                                   "func": fmo_drv3_016_revenue_slope_4q_rolling_std_qoq_diff},
    "fmo_drv3_017_netinc_slope_4q_rolling_std_qoq_diff":      {"inputs": ["netinc"],                                                                                    "func": fmo_drv3_017_netinc_slope_4q_rolling_std_qoq_diff},
    "fmo_drv3_018_revenue_qoq_accel_rolling_mean_qoq_diff":   {"inputs": ["revenue"],                                                                                   "func": fmo_drv3_018_revenue_qoq_accel_rolling_mean_qoq_diff},
    "fmo_drv3_019_netinc_qoq_accel_rolling_mean_qoq_diff":    {"inputs": ["netinc"],                                                                                    "func": fmo_drv3_019_netinc_qoq_accel_rolling_mean_qoq_diff},
    "fmo_drv3_020_eps_qoq_accel_rolling_mean_qoq_diff":       {"inputs": ["eps"],                                                                                       "func": fmo_drv3_020_eps_qoq_accel_rolling_mean_qoq_diff},
    "fmo_drv3_021_revenue_slope_4q_pct_chg_qoq":              {"inputs": ["revenue"],                                                                                   "func": fmo_drv3_021_revenue_slope_4q_pct_chg_qoq},
    "fmo_drv3_022_netinc_slope_4q_pct_chg_qoq":               {"inputs": ["netinc"],                                                                                    "func": fmo_drv3_022_netinc_slope_4q_pct_chg_qoq},
    "fmo_drv3_023_ebitda_slope_4q_pct_chg_qoq":               {"inputs": ["ebitda"],                                                                                    "func": fmo_drv3_023_ebitda_slope_4q_pct_chg_qoq},
    "fmo_drv3_024_breadth_net_improving_qoq_diff_rolling_slope": {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"], "func": fmo_drv3_024_breadth_net_improving_qoq_diff_rolling_slope},
    "fmo_drv3_025_composite_3rd_order_momentum_zscore":        {"inputs": ["revenue", "netinc", "eps", "ebitda"],                                                        "func": fmo_drv3_025_composite_3rd_order_momentum_zscore},
}
