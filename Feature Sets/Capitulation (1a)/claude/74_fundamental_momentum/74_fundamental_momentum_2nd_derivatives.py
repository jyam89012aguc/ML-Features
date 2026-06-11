"""
74_fundamental_momentum — 2nd-Derivative Features 001-025
Domain: rate of change of base fundamental-momentum features
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


# ── Base feature inline helpers ───────────────────────────────────────────────
# Self-contained recomputes so this file needs no cross-file imports.

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


def _breadth_net_improving_qoq(metrics):
    return sum(np.sign(m - m.shift(_TD_QTR)) for m in metrics).astype(float)


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


def _trend_persistence(m: pd.Series, w: int) -> pd.Series:
    improving = (m > m.shift(_TD_QTR)).astype(float)
    return _rolling_mean(improving, w)


def _gp_margin(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue.abs().replace(0, np.nan))


def _netinc_margin(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(netinc, revenue.abs().replace(0, np.nan))


def _ebitda_margin(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ebitda, revenue.abs().replace(0, np.nan))


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def fmo_drv2_001_revenue_slope_4q_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter OLS slope of revenue (slope acceleration)."""
    base = _revenue_slope_4q(revenue)
    return base - base.shift(_TD_QTR)


def fmo_drv2_002_netinc_slope_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter OLS slope of net income."""
    base = _netinc_slope_4q(netinc)
    return base - base.shift(_TD_QTR)


def fmo_drv2_003_eps_slope_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter OLS slope of EPS."""
    base = _eps_slope_4q(eps)
    return base - base.shift(_TD_QTR)


def fmo_drv2_004_ebitda_slope_4q_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter OLS slope of EBITDA."""
    base = _ebitda_slope_4q(ebitda)
    return base - base.shift(_TD_QTR)


def fmo_drv2_005_fcf_slope_4q_qoq_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter OLS slope of FCF."""
    base = _fcf_slope_4q(fcf)
    return base - base.shift(_TD_QTR)


def fmo_drv2_006_revenue_qoq_accel_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in revenue QoQ acceleration (3rd-order on raw; 2nd on base accel)."""
    base = _revenue_qoq_accel(revenue)
    return base - base.shift(_TD_QTR)


def fmo_drv2_007_netinc_qoq_accel_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income QoQ acceleration."""
    base = _netinc_qoq_accel(netinc)
    return base - base.shift(_TD_QTR)


def fmo_drv2_008_eps_qoq_accel_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in EPS QoQ acceleration."""
    base = _eps_qoq_accel(eps)
    return base - base.shift(_TD_QTR)


def fmo_drv2_009_ebitda_qoq_accel_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """QoQ change in EBITDA QoQ acceleration."""
    base = _ebitda_qoq_accel(ebitda)
    return base - base.shift(_TD_QTR)


def fmo_drv2_010_revenue_trend_persistence_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in revenue 4-quarter trend persistence fraction."""
    base = _trend_persistence(revenue, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_011_netinc_trend_persistence_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income 4-quarter trend persistence fraction."""
    base = _trend_persistence(netinc, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_012_eps_trend_persistence_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in EPS 4-quarter trend persistence fraction."""
    base = _trend_persistence(eps, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_013_breadth_net_improving_qoq_yoy_diff(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """YoY change in the net-improving QoQ breadth count."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    base = _breadth_net_improving_qoq(metrics)
    return base - base.shift(_TD_YEAR)


def fmo_drv2_014_breadth_net_improving_qoq_qoq_diff(
    revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    fcf: pd.Series, ncfo: pd.Series, equity: pd.Series, assets: pd.Series
) -> pd.Series:
    """QoQ change in the net-improving QoQ breadth count (breadth momentum)."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, equity, assets]
    base = _breadth_net_improving_qoq(metrics)
    return base - base.shift(_TD_QTR)


def fmo_drv2_015_gp_margin_qoq_accel(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in gross-margin QoQ momentum (2nd derivative of margin)."""
    margin = _gp_margin(gp, revenue)
    d1 = margin - margin.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_drv2_016_netinc_margin_qoq_accel(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in net-income-margin QoQ momentum (2nd derivative)."""
    margin = _netinc_margin(netinc, revenue)
    d1 = margin - margin.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_drv2_017_ebitda_margin_qoq_accel(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in EBITDA-margin QoQ momentum (2nd derivative)."""
    margin = _ebitda_margin(ebitda, revenue)
    d1 = margin - margin.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def fmo_drv2_018_revenue_zscore_4q_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of revenue."""
    base = _zscore_rolling(revenue, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_019_netinc_zscore_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of net income."""
    base = _zscore_rolling(netinc, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_020_eps_zscore_4q_yoy_diff(eps: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of EPS."""
    base = _zscore_rolling(eps, _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def fmo_drv2_021_revenue_pct_rank_4q_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter percentile rank of revenue."""
    base = _rolling_rank_pct(revenue, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_022_netinc_pct_rank_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter percentile rank of net income."""
    base = _rolling_rank_pct(netinc, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_023_eps_pct_rank_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter percentile rank of EPS."""
    base = _rolling_rank_pct(eps, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def fmo_drv2_024_revenue_slope_4q_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter OLS slope of revenue."""
    base = _revenue_slope_4q(revenue)
    return base - base.shift(_TD_YEAR)


def fmo_drv2_025_netinc_slope_4q_ewm_diff(netinc: pd.Series) -> pd.Series:
    """
    Net income 4-quarter OLS slope minus its own 4-quarter EWM (span=252).
    Measures whether current slope is above or below its recent trend.
    """
    base = _netinc_slope_4q(netinc)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

FUNDAMENTAL_MOMENTUM_REGISTRY_2ND_DERIVATIVES = {
    "fmo_drv2_001_revenue_slope_4q_qoq_diff":         {"inputs": ["revenue"],                                                                                           "func": fmo_drv2_001_revenue_slope_4q_qoq_diff},
    "fmo_drv2_002_netinc_slope_4q_qoq_diff":          {"inputs": ["netinc"],                                                                                            "func": fmo_drv2_002_netinc_slope_4q_qoq_diff},
    "fmo_drv2_003_eps_slope_4q_qoq_diff":             {"inputs": ["eps"],                                                                                               "func": fmo_drv2_003_eps_slope_4q_qoq_diff},
    "fmo_drv2_004_ebitda_slope_4q_qoq_diff":          {"inputs": ["ebitda"],                                                                                            "func": fmo_drv2_004_ebitda_slope_4q_qoq_diff},
    "fmo_drv2_005_fcf_slope_4q_qoq_diff":             {"inputs": ["fcf"],                                                                                               "func": fmo_drv2_005_fcf_slope_4q_qoq_diff},
    "fmo_drv2_006_revenue_qoq_accel_qoq_diff":        {"inputs": ["revenue"],                                                                                           "func": fmo_drv2_006_revenue_qoq_accel_qoq_diff},
    "fmo_drv2_007_netinc_qoq_accel_qoq_diff":         {"inputs": ["netinc"],                                                                                            "func": fmo_drv2_007_netinc_qoq_accel_qoq_diff},
    "fmo_drv2_008_eps_qoq_accel_qoq_diff":            {"inputs": ["eps"],                                                                                               "func": fmo_drv2_008_eps_qoq_accel_qoq_diff},
    "fmo_drv2_009_ebitda_qoq_accel_qoq_diff":         {"inputs": ["ebitda"],                                                                                            "func": fmo_drv2_009_ebitda_qoq_accel_qoq_diff},
    "fmo_drv2_010_revenue_trend_persistence_qoq_diff":{"inputs": ["revenue"],                                                                                           "func": fmo_drv2_010_revenue_trend_persistence_qoq_diff},
    "fmo_drv2_011_netinc_trend_persistence_qoq_diff": {"inputs": ["netinc"],                                                                                            "func": fmo_drv2_011_netinc_trend_persistence_qoq_diff},
    "fmo_drv2_012_eps_trend_persistence_qoq_diff":    {"inputs": ["eps"],                                                                                               "func": fmo_drv2_012_eps_trend_persistence_qoq_diff},
    "fmo_drv2_013_breadth_net_improving_qoq_yoy_diff":{"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_drv2_013_breadth_net_improving_qoq_yoy_diff},
    "fmo_drv2_014_breadth_net_improving_qoq_qoq_diff":{"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "equity", "assets"],             "func": fmo_drv2_014_breadth_net_improving_qoq_qoq_diff},
    "fmo_drv2_015_gp_margin_qoq_accel":               {"inputs": ["gp", "revenue"],                                                                                     "func": fmo_drv2_015_gp_margin_qoq_accel},
    "fmo_drv2_016_netinc_margin_qoq_accel":           {"inputs": ["netinc", "revenue"],                                                                                  "func": fmo_drv2_016_netinc_margin_qoq_accel},
    "fmo_drv2_017_ebitda_margin_qoq_accel":           {"inputs": ["ebitda", "revenue"],                                                                                  "func": fmo_drv2_017_ebitda_margin_qoq_accel},
    "fmo_drv2_018_revenue_zscore_4q_qoq_diff":        {"inputs": ["revenue"],                                                                                           "func": fmo_drv2_018_revenue_zscore_4q_qoq_diff},
    "fmo_drv2_019_netinc_zscore_4q_qoq_diff":         {"inputs": ["netinc"],                                                                                            "func": fmo_drv2_019_netinc_zscore_4q_qoq_diff},
    "fmo_drv2_020_eps_zscore_4q_yoy_diff":            {"inputs": ["eps"],                                                                                               "func": fmo_drv2_020_eps_zscore_4q_yoy_diff},
    "fmo_drv2_021_revenue_pct_rank_4q_qoq_diff":      {"inputs": ["revenue"],                                                                                           "func": fmo_drv2_021_revenue_pct_rank_4q_qoq_diff},
    "fmo_drv2_022_netinc_pct_rank_4q_qoq_diff":       {"inputs": ["netinc"],                                                                                            "func": fmo_drv2_022_netinc_pct_rank_4q_qoq_diff},
    "fmo_drv2_023_eps_pct_rank_4q_qoq_diff":          {"inputs": ["eps"],                                                                                               "func": fmo_drv2_023_eps_pct_rank_4q_qoq_diff},
    "fmo_drv2_024_revenue_slope_4q_yoy_diff":         {"inputs": ["revenue"],                                                                                           "func": fmo_drv2_024_revenue_slope_4q_yoy_diff},
    "fmo_drv2_025_netinc_slope_4q_ewm_diff":          {"inputs": ["netinc"],                                                                                            "func": fmo_drv2_025_netinc_slope_4q_ewm_diff},
}
