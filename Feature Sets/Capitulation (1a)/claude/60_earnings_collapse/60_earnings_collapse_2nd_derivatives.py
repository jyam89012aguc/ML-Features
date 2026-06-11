"""
60_earnings_collapse — 2nd-Derivative Features 001-025
Domain: rate of change of base earnings-collapse features
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
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
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


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline the relevant base computations so this file needs no cross-import.

def _netinc_qoq(netinc: pd.Series) -> pd.Series:
    return netinc - netinc.shift(_TD_QTR)


def _netinc_yoy(netinc: pd.Series) -> pd.Series:
    return netinc - netinc.shift(_TD_YEAR)


def _netinc_qoq_pct(netinc: pd.Series) -> pd.Series:
    prior = netinc.shift(_TD_QTR)
    return _safe_div_abs(netinc - prior, prior)


def _netinc_yoy_pct(netinc: pd.Series) -> pd.Series:
    prior = netinc.shift(_TD_YEAR)
    return _safe_div_abs(netinc - prior, prior)


def _eps_qoq(eps: pd.Series) -> pd.Series:
    return eps - eps.shift(_TD_QTR)


def _eps_yoy(eps: pd.Series) -> pd.Series:
    return eps - eps.shift(_TD_YEAR)


def _netinc_zscore_4q(netinc: pd.Series) -> pd.Series:
    m  = _rolling_mean(netinc, _TD_YEAR)
    sd = _rolling_std(netinc, _TD_YEAR)
    return _safe_div(netinc - m, sd)


def _netinc_drawdown_from_4q_peak(netinc: pd.Series) -> pd.Series:
    return netinc - _rolling_max(netinc, _TD_YEAR)


def _netinc_worst_loss_1y(netinc: pd.Series) -> pd.Series:
    return _rolling_min(netinc, _TD_YEAR)


def _netinc_loss_fraction_1y(netinc: pd.Series) -> pd.Series:
    return _rolling_mean((netinc < 0).astype(float), _TD_YEAR)


def _ebit_drawdown_4q(ebit: pd.Series) -> pd.Series:
    return ebit - _rolling_max(ebit, _TD_YEAR)


def _epsdil_drawdown_4q(epsdil: pd.Series) -> pd.Series:
    return epsdil - _rolling_max(epsdil, _TD_YEAR)


def _netinc_ttm(netinc: pd.Series) -> pd.Series:
    return netinc.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def ecl_drv2_001_netinc_qoq_change_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ net-income change (acceleration of QoQ decline)."""
    base = _netinc_qoq(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_002_netinc_yoy_change_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the YoY net-income change (how fast the YoY trend is shifting)."""
    base = _netinc_yoy(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_003_netinc_qoq_pct_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent change of net income."""
    base = _netinc_qoq_pct(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_004_netinc_yoy_pct_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent change of net income."""
    base = _netinc_yoy_pct(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_005_eps_qoq_change_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in the QoQ EPS change (EPS acceleration)."""
    base = _eps_qoq(eps)
    return base - base.shift(_TD_QTR)


def ecl_drv2_006_eps_yoy_change_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in the YoY EPS change."""
    base = _eps_yoy(eps)
    return base - base.shift(_TD_QTR)


def ecl_drv2_007_netinc_zscore_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of net income."""
    base = _netinc_zscore_4q(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_008_netinc_zscore_4q_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of net income."""
    base = _netinc_zscore_4q(netinc)
    return base - base.shift(_TD_YEAR)


def ecl_drv2_009_netinc_drawdown_from_4q_peak_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter-peak drawdown of net income."""
    base = _netinc_drawdown_from_4q_peak(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_010_netinc_drawdown_from_4q_peak_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter-peak drawdown of net income."""
    base = _netinc_drawdown_from_4q_peak(netinc)
    return base - base.shift(_TD_YEAR)


def ecl_drv2_011_netinc_worst_loss_1y_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the rolling 1-year worst net income loss."""
    base = _netinc_worst_loss_1y(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_012_netinc_loss_fraction_1y_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the rolling 1-year loss-quarter fraction."""
    base = _netinc_loss_fraction_1y(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_013_ebit_drawdown_4q_qoq_diff(ebit: pd.Series) -> pd.Series:
    """QoQ change in the EBIT 4-quarter peak drawdown."""
    base = _ebit_drawdown_4q(ebit)
    return base - base.shift(_TD_QTR)


def ecl_drv2_014_epsdil_drawdown_4q_qoq_diff(epsdil: pd.Series) -> pd.Series:
    """QoQ change in the diluted EPS 4-quarter peak drawdown."""
    base = _epsdil_drawdown_4q(epsdil)
    return base - base.shift(_TD_QTR)


def ecl_drv2_015_netinc_ttm_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the TTM (trailing-12-month) net income sum."""
    base = _netinc_ttm(netinc)
    return base - base.shift(_TD_QTR)


def ecl_drv2_016_netinc_ttm_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the TTM net income sum."""
    base = _netinc_ttm(netinc)
    return base - base.shift(_TD_YEAR)


def ecl_drv2_017_netinc_qoq_slope_of_qoq(netinc: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ net-income change series.
    Captures the trend in QoQ momentum.
    """
    base = _netinc_qoq(netinc)

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


def ecl_drv2_018_netinc_yoy_pct_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the YoY percent-change of net income (2nd-order YoY)."""
    base = _netinc_yoy_pct(netinc)
    return base - base.shift(_TD_YEAR)


def ecl_drv2_019_eps_qoq_pct_chg(eps: pd.Series) -> pd.Series:
    """QoQ percent change in the QoQ EPS change series."""
    base = _eps_qoq(eps)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def ecl_drv2_020_netinc_drawdown_pct_qoq_diff(netinc: pd.Series) -> pd.Series:
    """
    QoQ change in (netinc percent drawdown from 4Q peak).
    = d/dq [(netinc - peak) / |peak|].
    """
    peak = _rolling_max(netinc, _TD_YEAR)
    base = _safe_div_abs(netinc - peak, peak)
    return base - base.shift(_TD_QTR)


def ecl_drv2_021_netinc_zscore_8q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 8-quarter z-score of net income."""
    m  = _rolling_mean(netinc, _TD_2Y)
    sd = _rolling_std(netinc, _TD_2Y)
    base = _safe_div(netinc - m, sd)
    return base - base.shift(_TD_QTR)


def ecl_drv2_022_eps_zscore_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of EPS."""
    m  = _rolling_mean(eps, _TD_YEAR)
    sd = _rolling_std(eps, _TD_YEAR)
    base = _safe_div(eps - m, sd)
    return base - base.shift(_TD_QTR)


def ecl_drv2_023_netinc_loss_fraction_3y_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 3-year loss-quarter fraction."""
    base = _rolling_mean((netinc < 0).astype(float), _TD_3Y)
    return base - base.shift(_TD_QTR)


def ecl_drv2_024_netinc_qoq_ewm_diff(netinc: pd.Series) -> pd.Series:
    """
    Current QoQ net-income change minus its own 4-quarter EWM (span=252).
    Measures whether the current QoQ decline is worse than its recent trend.
    """
    base = _netinc_qoq(netinc)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def ecl_drv2_025_netinc_cumulative_collapse_accel(netinc: pd.Series) -> pd.Series:
    """
    Change in the TTM-net-income drawdown from its expanding peak (2nd order):
    QoQ diff of (TTM_netinc - expanding_max(TTM_netinc)).
    """
    ttm  = _netinc_ttm(netinc)
    peak = ttm.expanding(min_periods=1).max()
    base = ttm - peak
    return base - base.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

EARNINGS_COLLAPSE_REGISTRY_2ND_DERIVATIVES = {
    "ecl_drv2_001_netinc_qoq_change_qoq_diff":          {"inputs": ["netinc"],  "func": ecl_drv2_001_netinc_qoq_change_qoq_diff},
    "ecl_drv2_002_netinc_yoy_change_qoq_diff":          {"inputs": ["netinc"],  "func": ecl_drv2_002_netinc_yoy_change_qoq_diff},
    "ecl_drv2_003_netinc_qoq_pct_qoq_diff":             {"inputs": ["netinc"],  "func": ecl_drv2_003_netinc_qoq_pct_qoq_diff},
    "ecl_drv2_004_netinc_yoy_pct_qoq_diff":             {"inputs": ["netinc"],  "func": ecl_drv2_004_netinc_yoy_pct_qoq_diff},
    "ecl_drv2_005_eps_qoq_change_qoq_diff":             {"inputs": ["eps"],     "func": ecl_drv2_005_eps_qoq_change_qoq_diff},
    "ecl_drv2_006_eps_yoy_change_qoq_diff":             {"inputs": ["eps"],     "func": ecl_drv2_006_eps_yoy_change_qoq_diff},
    "ecl_drv2_007_netinc_zscore_4q_qoq_diff":           {"inputs": ["netinc"],  "func": ecl_drv2_007_netinc_zscore_4q_qoq_diff},
    "ecl_drv2_008_netinc_zscore_4q_yoy_diff":           {"inputs": ["netinc"],  "func": ecl_drv2_008_netinc_zscore_4q_yoy_diff},
    "ecl_drv2_009_netinc_drawdown_from_4q_peak_qoq_diff": {"inputs": ["netinc"], "func": ecl_drv2_009_netinc_drawdown_from_4q_peak_qoq_diff},
    "ecl_drv2_010_netinc_drawdown_from_4q_peak_yoy_diff": {"inputs": ["netinc"], "func": ecl_drv2_010_netinc_drawdown_from_4q_peak_yoy_diff},
    "ecl_drv2_011_netinc_worst_loss_1y_qoq_diff":       {"inputs": ["netinc"],  "func": ecl_drv2_011_netinc_worst_loss_1y_qoq_diff},
    "ecl_drv2_012_netinc_loss_fraction_1y_qoq_diff":    {"inputs": ["netinc"],  "func": ecl_drv2_012_netinc_loss_fraction_1y_qoq_diff},
    "ecl_drv2_013_ebit_drawdown_4q_qoq_diff":           {"inputs": ["ebit"],    "func": ecl_drv2_013_ebit_drawdown_4q_qoq_diff},
    "ecl_drv2_014_epsdil_drawdown_4q_qoq_diff":         {"inputs": ["epsdil"],  "func": ecl_drv2_014_epsdil_drawdown_4q_qoq_diff},
    "ecl_drv2_015_netinc_ttm_qoq_diff":                 {"inputs": ["netinc"],  "func": ecl_drv2_015_netinc_ttm_qoq_diff},
    "ecl_drv2_016_netinc_ttm_yoy_diff":                 {"inputs": ["netinc"],  "func": ecl_drv2_016_netinc_ttm_yoy_diff},
    "ecl_drv2_017_netinc_qoq_slope_of_qoq":             {"inputs": ["netinc"],  "func": ecl_drv2_017_netinc_qoq_slope_of_qoq},
    "ecl_drv2_018_netinc_yoy_pct_yoy_diff":             {"inputs": ["netinc"],  "func": ecl_drv2_018_netinc_yoy_pct_yoy_diff},
    "ecl_drv2_019_eps_qoq_pct_chg":                     {"inputs": ["eps"],     "func": ecl_drv2_019_eps_qoq_pct_chg},
    "ecl_drv2_020_netinc_drawdown_pct_qoq_diff":        {"inputs": ["netinc"],  "func": ecl_drv2_020_netinc_drawdown_pct_qoq_diff},
    "ecl_drv2_021_netinc_zscore_8q_qoq_diff":           {"inputs": ["netinc"],  "func": ecl_drv2_021_netinc_zscore_8q_qoq_diff},
    "ecl_drv2_022_eps_zscore_4q_qoq_diff":              {"inputs": ["eps"],     "func": ecl_drv2_022_eps_zscore_4q_qoq_diff},
    "ecl_drv2_023_netinc_loss_fraction_3y_qoq_diff":    {"inputs": ["netinc"],  "func": ecl_drv2_023_netinc_loss_fraction_3y_qoq_diff},
    "ecl_drv2_024_netinc_qoq_ewm_diff":                 {"inputs": ["netinc"],  "func": ecl_drv2_024_netinc_qoq_ewm_diff},
    "ecl_drv2_025_netinc_cumulative_collapse_accel":     {"inputs": ["netinc"],  "func": ecl_drv2_025_netinc_cumulative_collapse_accel},
}
