"""
73_earnings_volatility — 2nd-Derivative Features 001-025
Domain: rate of change of base earnings-volatility features (QoQ diff / slope /
        pct-change of rolling-std, CV, swing-magnitude, downside-dev, resid-std
        and related base concepts).
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
days, 1 year = 252 trading days.  All feature functions in this file look
strictly backward.
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
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(2, span // 4)).std()


def _qoq_diff(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_QTR)


def _cv(s: pd.Series, w: int) -> pd.Series:
    return _safe_div_abs(_rolling_std(s, w), _rolling_mean(s, w))


def _ols_slope(arr: np.ndarray) -> float:
    """Scalar OLS slope for rolling.apply(raw=True)."""
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = float(((x - xm) ** 2).sum())
    if denom == 0.0:
        return np.nan
    return float(((x - xm) * (arr - ym)).sum() / denom)


def _residual_std(arr: np.ndarray) -> float:
    """Scalar residual std of linear trend fit; for rolling.apply(raw=True)."""
    n = len(arr)
    if n < 3:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = float(((x - xm) ** 2).sum())
    if denom == 0.0:
        s = float(arr.std())
        return s if s > 0 else np.nan
    slope = float(((x - xm) * (arr - ym)).sum() / denom)
    intercept = ym - slope * xm
    resid = arr - (slope * x + intercept)
    return float(resid.std())


# ── Base-concept re-computations (self-contained; no cross-file imports) ──────

def _base_netinc_std_4q(netinc: pd.Series) -> pd.Series:
    return _rolling_std(netinc, _TD_YEAR)


def _base_netinc_cv_4q(netinc: pd.Series) -> pd.Series:
    return _cv(netinc, _TD_YEAR)


def _base_eps_std_4q(eps: pd.Series) -> pd.Series:
    return _rolling_std(eps, _TD_YEAR)


def _base_ebit_std_4q(ebit: pd.Series) -> pd.Series:
    return _rolling_std(ebit, _TD_YEAR)


def _base_netinc_qoq_swing_abs_4q(netinc: pd.Series) -> pd.Series:
    return _rolling_mean(_qoq_diff(netinc).abs(), _TD_YEAR)


def _base_netinc_range_4q(netinc: pd.Series) -> pd.Series:
    return _rolling_max(netinc, _TD_YEAR) - _rolling_min(netinc, _TD_YEAR)


def _base_netinc_downside_dev_4q(netinc: pd.Series) -> pd.Series:
    below = netinc.clip(upper=0)
    return _rolling_mean(below ** 2, _TD_YEAR).apply(np.sqrt)


def _base_netinc_resid_std_4q(netinc: pd.Series) -> pd.Series:
    return netinc.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )


def _base_net_margin_std_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return _rolling_std(margin, _TD_YEAR)


def _base_ncfo_std_4q(ncfo: pd.Series) -> pd.Series:
    return _rolling_std(ncfo, _TD_YEAR)


def _base_netinc_vol_of_vol(netinc: pd.Series) -> pd.Series:
    return _rolling_std(_rolling_std(netinc, _TD_YEAR), _TD_2Y)


def _base_eps_cv_4q(eps: pd.Series) -> pd.Series:
    return _cv(eps, _TD_YEAR)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def evl_drv2_001_netinc_std_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling std of net income (volatility acceleration)."""
    base = _base_netinc_std_4q(netinc)
    return base - base.shift(_TD_QTR)


def evl_drv2_002_netinc_std_4q_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the 4q rolling std of net income."""
    base = _base_netinc_std_4q(netinc)
    return base - base.shift(_TD_YEAR)


def evl_drv2_003_netinc_cv_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4q coefficient of variation of net income."""
    base = _base_netinc_cv_4q(netinc)
    return base - base.shift(_TD_QTR)


def evl_drv2_004_netinc_cv_4q_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the 4q CV of net income."""
    base = _base_netinc_cv_4q(netinc)
    return base - base.shift(_TD_YEAR)


def evl_drv2_005_eps_std_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling std of EPS."""
    base = _base_eps_std_4q(eps)
    return base - base.shift(_TD_QTR)


def evl_drv2_006_ebit_std_4q_qoq_diff(ebit: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling std of EBIT."""
    base = _base_ebit_std_4q(ebit)
    return base - base.shift(_TD_QTR)


def evl_drv2_007_netinc_qoq_swing_abs_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the mean absolute QoQ swing of net income (4q window)."""
    base = _base_netinc_qoq_swing_abs_4q(netinc)
    return base - base.shift(_TD_QTR)


def evl_drv2_008_netinc_range_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4q earnings range of net income."""
    base = _base_netinc_range_4q(netinc)
    return base - base.shift(_TD_QTR)


def evl_drv2_009_netinc_range_4q_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the 4q earnings range of net income."""
    base = _base_netinc_range_4q(netinc)
    return base - base.shift(_TD_YEAR)


def evl_drv2_010_netinc_downside_dev_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4q downside semi-deviation of net income."""
    base = _base_netinc_downside_dev_4q(netinc)
    return base - base.shift(_TD_QTR)


def evl_drv2_011_netinc_resid_std_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the trend-residual std of net income (4q window)."""
    base = _base_netinc_resid_std_4q(netinc)
    return base - base.shift(_TD_QTR)


def evl_drv2_012_net_margin_std_4q_qoq_diff(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling std of net margin."""
    base = _base_net_margin_std_4q(netinc, revenue)
    return base - base.shift(_TD_QTR)


def evl_drv2_013_ncfo_std_4q_qoq_diff(ncfo: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling std of operating cash flow."""
    base = _base_ncfo_std_4q(ncfo)
    return base - base.shift(_TD_QTR)


def evl_drv2_014_netinc_vol_of_vol_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the volatility-of-volatility of net income (4q/8q windows)."""
    base = _base_netinc_vol_of_vol(netinc)
    return base - base.shift(_TD_QTR)


def evl_drv2_015_netinc_std_4q_pct_change_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ percent change in the 4q rolling std of net income."""
    base = _base_netinc_std_4q(netinc)
    prior = base.shift(_TD_QTR)
    return _safe_div_abs(base - prior, prior)


def evl_drv2_016_eps_cv_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in the 4q CV of EPS."""
    base = _base_eps_cv_4q(eps)
    return base - base.shift(_TD_QTR)


def evl_drv2_017_netinc_cv_slope_4q(netinc: pd.Series) -> pd.Series:
    """
    OLS slope of the 4q CV of net income over a trailing 4q (252-day) window.
    Positive slope = CV trending upward (rising instability trend).
    """
    base = _base_netinc_cv_4q(netinc)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True
    )


def evl_drv2_018_netinc_std_slope_4q(netinc: pd.Series) -> pd.Series:
    """
    OLS slope of the 4q rolling std of net income over a trailing 4q window.
    Rising slope = accelerating volatility.
    """
    base = _base_netinc_std_4q(netinc)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True
    )


def evl_drv2_019_netinc_downside_dev_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the 4q downside semi-deviation of net income."""
    base = _base_netinc_downside_dev_4q(netinc)
    return base - base.shift(_TD_YEAR)


def evl_drv2_020_netinc_std_4q_ewm_diff(netinc: pd.Series) -> pd.Series:
    """
    4q rolling std minus its own EWM (span=252) — measures whether current
    volatility level is elevated above its recent trend.
    """
    base = _base_netinc_std_4q(netinc)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def evl_drv2_021_netinc_cv_4q_2q_diff(netinc: pd.Series) -> pd.Series:
    """Half-year (2q = 126-day) change in the 4q CV of net income."""
    base = _base_netinc_cv_4q(netinc)
    return base - base.shift(126)


def evl_drv2_022_netinc_qoq_swing_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the mean-absolute QoQ-swing of net income (4q window)."""
    base = _base_netinc_qoq_swing_abs_4q(netinc)
    return base - base.shift(_TD_YEAR)


def evl_drv2_023_eps_std_4q_yoy_diff(eps: pd.Series) -> pd.Series:
    """YoY change in the 4q rolling std of EPS."""
    base = _base_eps_std_4q(eps)
    return base - base.shift(_TD_YEAR)


def evl_drv2_024_netinc_resid_std_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the trend-residual std of net income (4q window)."""
    base = _base_netinc_resid_std_4q(netinc)
    return base - base.shift(_TD_YEAR)


def evl_drv2_025_earnings_instability_accel_composite(
    netinc: pd.Series,
    eps: pd.Series,
    ebit: pd.Series,
) -> pd.Series:
    """
    Composite instability acceleration: average QoQ change in the 4q std
    of netinc, eps, and ebit — three-field volatility acceleration signal.
    """
    d_ni   = _base_netinc_std_4q(netinc) - _base_netinc_std_4q(netinc).shift(_TD_QTR)
    d_eps  = _base_eps_std_4q(eps)       - _base_eps_std_4q(eps).shift(_TD_QTR)
    d_ebit = _base_ebit_std_4q(ebit)     - _base_ebit_std_4q(ebit).shift(_TD_QTR)
    return (d_ni + d_eps + d_ebit) / 3.0


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

EARNINGS_VOLATILITY_REGISTRY_2ND_DERIVATIVES = {
    "evl_drv2_001_netinc_std_4q_qoq_diff":            {"inputs": ["netinc"],              "func": evl_drv2_001_netinc_std_4q_qoq_diff},
    "evl_drv2_002_netinc_std_4q_yoy_diff":            {"inputs": ["netinc"],              "func": evl_drv2_002_netinc_std_4q_yoy_diff},
    "evl_drv2_003_netinc_cv_4q_qoq_diff":             {"inputs": ["netinc"],              "func": evl_drv2_003_netinc_cv_4q_qoq_diff},
    "evl_drv2_004_netinc_cv_4q_yoy_diff":             {"inputs": ["netinc"],              "func": evl_drv2_004_netinc_cv_4q_yoy_diff},
    "evl_drv2_005_eps_std_4q_qoq_diff":               {"inputs": ["eps"],                 "func": evl_drv2_005_eps_std_4q_qoq_diff},
    "evl_drv2_006_ebit_std_4q_qoq_diff":              {"inputs": ["ebit"],                "func": evl_drv2_006_ebit_std_4q_qoq_diff},
    "evl_drv2_007_netinc_qoq_swing_abs_4q_qoq_diff":  {"inputs": ["netinc"],              "func": evl_drv2_007_netinc_qoq_swing_abs_4q_qoq_diff},
    "evl_drv2_008_netinc_range_4q_qoq_diff":          {"inputs": ["netinc"],              "func": evl_drv2_008_netinc_range_4q_qoq_diff},
    "evl_drv2_009_netinc_range_4q_yoy_diff":          {"inputs": ["netinc"],              "func": evl_drv2_009_netinc_range_4q_yoy_diff},
    "evl_drv2_010_netinc_downside_dev_4q_qoq_diff":   {"inputs": ["netinc"],              "func": evl_drv2_010_netinc_downside_dev_4q_qoq_diff},
    "evl_drv2_011_netinc_resid_std_4q_qoq_diff":      {"inputs": ["netinc"],              "func": evl_drv2_011_netinc_resid_std_4q_qoq_diff},
    "evl_drv2_012_net_margin_std_4q_qoq_diff":        {"inputs": ["netinc", "revenue"],   "func": evl_drv2_012_net_margin_std_4q_qoq_diff},
    "evl_drv2_013_ncfo_std_4q_qoq_diff":              {"inputs": ["ncfo"],                "func": evl_drv2_013_ncfo_std_4q_qoq_diff},
    "evl_drv2_014_netinc_vol_of_vol_qoq_diff":        {"inputs": ["netinc"],              "func": evl_drv2_014_netinc_vol_of_vol_qoq_diff},
    "evl_drv2_015_netinc_std_4q_pct_change_qoq":      {"inputs": ["netinc"],              "func": evl_drv2_015_netinc_std_4q_pct_change_qoq},
    "evl_drv2_016_eps_cv_4q_qoq_diff":                {"inputs": ["eps"],                 "func": evl_drv2_016_eps_cv_4q_qoq_diff},
    "evl_drv2_017_netinc_cv_slope_4q":                {"inputs": ["netinc"],              "func": evl_drv2_017_netinc_cv_slope_4q},
    "evl_drv2_018_netinc_std_slope_4q":               {"inputs": ["netinc"],              "func": evl_drv2_018_netinc_std_slope_4q},
    "evl_drv2_019_netinc_downside_dev_yoy_diff":      {"inputs": ["netinc"],              "func": evl_drv2_019_netinc_downside_dev_yoy_diff},
    "evl_drv2_020_netinc_std_4q_ewm_diff":            {"inputs": ["netinc"],              "func": evl_drv2_020_netinc_std_4q_ewm_diff},
    "evl_drv2_021_netinc_cv_4q_2q_diff":              {"inputs": ["netinc"],              "func": evl_drv2_021_netinc_cv_4q_2q_diff},
    "evl_drv2_022_netinc_qoq_swing_yoy_diff":         {"inputs": ["netinc"],              "func": evl_drv2_022_netinc_qoq_swing_yoy_diff},
    "evl_drv2_023_eps_std_4q_yoy_diff":               {"inputs": ["eps"],                 "func": evl_drv2_023_eps_std_4q_yoy_diff},
    "evl_drv2_024_netinc_resid_std_yoy_diff":         {"inputs": ["netinc"],              "func": evl_drv2_024_netinc_resid_std_yoy_diff},
    "evl_drv2_025_earnings_instability_accel_composite": {"inputs": ["netinc", "eps", "ebit"], "func": evl_drv2_025_earnings_instability_accel_composite},
}
