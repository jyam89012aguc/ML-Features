"""
60_earnings_collapse — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative earnings-collapse features
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 3rd-derivative series are sparse/stepwise on a daily index — this is
correct and expected for quarterly-sourced data.
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


# ── Inline 2nd-derivative base helpers ───────────────────────────────────────
# Each function below recomputes its 2nd-derivative base signal before taking
# the 3rd derivative, keeping this file fully self-contained.

def _d2_netinc_qoq_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ net-income change."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return qoq - qoq.shift(_TD_QTR)


def _d2_netinc_yoy_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in YoY net-income change."""
    yoy = netinc - netinc.shift(_TD_YEAR)
    return yoy - yoy.shift(_TD_QTR)


def _d2_netinc_qoq_pct_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ percent-change of net income."""
    prior = netinc.shift(_TD_QTR)
    pct   = _safe_div_abs(netinc - prior, prior)
    return pct - pct.shift(_TD_QTR)


def _d2_netinc_yoy_pct_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in YoY percent-change of net income."""
    prior = netinc.shift(_TD_YEAR)
    pct   = _safe_div_abs(netinc - prior, prior)
    return pct - pct.shift(_TD_QTR)


def _d2_eps_qoq_qoq(eps: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ EPS change."""
    qoq = eps - eps.shift(_TD_QTR)
    return qoq - qoq.shift(_TD_QTR)


def _d2_netinc_zscore_4q_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in 4Q z-score of net income."""
    m  = _rolling_mean(netinc, _TD_YEAR)
    sd = _rolling_std(netinc, _TD_YEAR)
    z  = _safe_div(netinc - m, sd)
    return z - z.shift(_TD_QTR)


def _d2_netinc_drawdown_4q_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in net-income 4Q peak drawdown."""
    dd = netinc - _rolling_max(netinc, _TD_YEAR)
    return dd - dd.shift(_TD_QTR)


def _d2_netinc_worst_loss_1y_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in rolling worst net income."""
    worst = _rolling_min(netinc, _TD_YEAR)
    return worst - worst.shift(_TD_QTR)


def _d2_netinc_loss_frac_1y_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in rolling 1Y loss fraction."""
    base = _rolling_mean((netinc < 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def _d2_netinc_ttm_qoq(netinc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in TTM net income."""
    ttm = netinc.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return ttm - ttm.shift(_TD_QTR)


def _d2_ebit_drawdown_4q_qoq(ebit: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in EBIT 4Q peak drawdown."""
    dd = ebit - _rolling_max(ebit, _TD_YEAR)
    return dd - dd.shift(_TD_QTR)


def _d2_epsdil_drawdown_4q_qoq(epsdil: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in diluted EPS 4Q peak drawdown."""
    dd = epsdil - _rolling_max(epsdil, _TD_YEAR)
    return dd - dd.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def ecl_drv3_001_netinc_qoq_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order QoQ net-income acceleration."""
    d2 = _d2_netinc_qoq_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_002_netinc_yoy_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order YoY net-income change."""
    d2 = _d2_netinc_yoy_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_003_netinc_qoq_pct_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order QoQ percent-change acceleration."""
    d2 = _d2_netinc_qoq_pct_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_004_netinc_yoy_pct_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order YoY percent-change."""
    d2 = _d2_netinc_yoy_pct_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_005_eps_qoq_3rd_deriv(eps: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order QoQ EPS acceleration."""
    d2 = _d2_eps_qoq_qoq(eps)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_006_netinc_zscore_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order z-score acceleration."""
    d2 = _d2_netinc_zscore_4q_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_007_netinc_drawdown_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order net-income drawdown acceleration."""
    d2 = _d2_netinc_drawdown_4q_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_008_netinc_worst_loss_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order worst-loss change."""
    d2 = _d2_netinc_worst_loss_1y_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_009_netinc_loss_fraction_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order loss-fraction acceleration."""
    d2 = _d2_netinc_loss_frac_1y_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_010_netinc_ttm_3rd_deriv(netinc: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order TTM net-income change."""
    d2 = _d2_netinc_ttm_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_011_ebit_drawdown_3rd_deriv(ebit: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order EBIT drawdown acceleration."""
    d2 = _d2_ebit_drawdown_4q_qoq(ebit)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_012_epsdil_drawdown_3rd_deriv(epsdil: pd.Series) -> pd.Series:
    """3rd derivative: QoQ change in the 2nd-order diluted EPS drawdown acceleration."""
    d2 = _d2_epsdil_drawdown_4q_qoq(epsdil)
    return d2 - d2.shift(_TD_QTR)


def ecl_drv3_013_netinc_qoq_rolling_slope_of_d2(netinc: pd.Series) -> pd.Series:
    """
    OLS slope of the 2nd-derivative (d2 of QoQ netinc) over a 4Q window.
    Summarizes the trend in the acceleration of decline.
    """
    d2 = _d2_netinc_qoq_qoq(netinc)

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

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def ecl_drv3_014_eps_qoq_rolling_slope_of_d2(eps: pd.Series) -> pd.Series:
    """OLS slope of the 2nd-derivative of QoQ EPS over a 4Q window."""
    d2 = _d2_eps_qoq_qoq(eps)

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

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def ecl_drv3_015_netinc_d2_zscore_4q(netinc: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative (d2 of QoQ netinc) within a 4Q window."""
    d2 = _d2_netinc_qoq_qoq(netinc)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def ecl_drv3_016_eps_d2_zscore_4q(eps: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative (d2 of QoQ EPS) within a 4Q window."""
    d2 = _d2_eps_qoq_qoq(eps)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def ecl_drv3_017_netinc_d2_positive_flag(netinc: pd.Series) -> pd.Series:
    """
    1 when the 2nd derivative of QoQ net income is positive (deceleration of decline
    or acceleration of recovery).
    """
    d2 = _d2_netinc_qoq_qoq(netinc)
    return (d2 > 0).astype(float)


def ecl_drv3_018_netinc_d2_negative_flag(netinc: pd.Series) -> pd.Series:
    """1 when the 2nd derivative of QoQ net income is negative (accelerating collapse)."""
    d2 = _d2_netinc_qoq_qoq(netinc)
    return (d2 < 0).astype(float)


def ecl_drv3_019_netinc_d3_rolling_mean_4q(netinc: pd.Series) -> pd.Series:
    """Rolling 4Q mean of the 3rd-derivative of net income QoQ change."""
    d2 = _d2_netinc_qoq_qoq(netinc)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


def ecl_drv3_020_eps_d3_rolling_mean_4q(eps: pd.Series) -> pd.Series:
    """Rolling 4Q mean of the 3rd-derivative of EPS QoQ change."""
    d2 = _d2_eps_qoq_qoq(eps)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


def ecl_drv3_021_netinc_d2_pct_rank_4q(netinc: pd.Series) -> pd.Series:
    """Percentile rank of the 2nd-derivative of QoQ net income in a 4Q window."""
    d2 = _d2_netinc_qoq_qoq(netinc)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def ecl_drv3_022_netinc_d3_cumulative_sum_4q(netinc: pd.Series) -> pd.Series:
    """Rolling 4Q sum of the 3rd-derivative of net income (cumulative jerk)."""
    d2 = _d2_netinc_qoq_qoq(netinc)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()


def ecl_drv3_023_netinc_d2_ewm_deviation(netinc: pd.Series) -> pd.Series:
    """2nd derivative of QoQ netinc minus its own 4Q EWM (span=252)."""
    d2  = _d2_netinc_qoq_qoq(netinc)
    ewm = d2.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return d2 - ewm


def ecl_drv3_024_netinc_d3_expanding_zscore(netinc: pd.Series) -> pd.Series:
    """Expanding z-score of the 3rd-derivative of QoQ net-income change."""
    d2 = _d2_netinc_qoq_qoq(netinc)
    d3 = d2 - d2.shift(_TD_QTR)
    m  = d3.expanding(min_periods=2).mean()
    sd = d3.expanding(min_periods=2).std()
    return _safe_div(d3 - m, sd)


def ecl_drv3_025_ebit_d2_zscore_4q(ebit: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative (d2 of QoQ EBIT drawdown) in a 4Q window."""
    d2 = _d2_ebit_drawdown_4q_qoq(ebit)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

EARNINGS_COLLAPSE_REGISTRY_3RD_DERIVATIVES = {
    "ecl_drv3_001_netinc_qoq_3rd_deriv":            {"inputs": ["netinc"],  "func": ecl_drv3_001_netinc_qoq_3rd_deriv},
    "ecl_drv3_002_netinc_yoy_3rd_deriv":            {"inputs": ["netinc"],  "func": ecl_drv3_002_netinc_yoy_3rd_deriv},
    "ecl_drv3_003_netinc_qoq_pct_3rd_deriv":        {"inputs": ["netinc"],  "func": ecl_drv3_003_netinc_qoq_pct_3rd_deriv},
    "ecl_drv3_004_netinc_yoy_pct_3rd_deriv":        {"inputs": ["netinc"],  "func": ecl_drv3_004_netinc_yoy_pct_3rd_deriv},
    "ecl_drv3_005_eps_qoq_3rd_deriv":               {"inputs": ["eps"],     "func": ecl_drv3_005_eps_qoq_3rd_deriv},
    "ecl_drv3_006_netinc_zscore_3rd_deriv":         {"inputs": ["netinc"],  "func": ecl_drv3_006_netinc_zscore_3rd_deriv},
    "ecl_drv3_007_netinc_drawdown_3rd_deriv":       {"inputs": ["netinc"],  "func": ecl_drv3_007_netinc_drawdown_3rd_deriv},
    "ecl_drv3_008_netinc_worst_loss_3rd_deriv":     {"inputs": ["netinc"],  "func": ecl_drv3_008_netinc_worst_loss_3rd_deriv},
    "ecl_drv3_009_netinc_loss_fraction_3rd_deriv":  {"inputs": ["netinc"],  "func": ecl_drv3_009_netinc_loss_fraction_3rd_deriv},
    "ecl_drv3_010_netinc_ttm_3rd_deriv":            {"inputs": ["netinc"],  "func": ecl_drv3_010_netinc_ttm_3rd_deriv},
    "ecl_drv3_011_ebit_drawdown_3rd_deriv":         {"inputs": ["ebit"],    "func": ecl_drv3_011_ebit_drawdown_3rd_deriv},
    "ecl_drv3_012_epsdil_drawdown_3rd_deriv":       {"inputs": ["epsdil"],  "func": ecl_drv3_012_epsdil_drawdown_3rd_deriv},
    "ecl_drv3_013_netinc_qoq_rolling_slope_of_d2":  {"inputs": ["netinc"],  "func": ecl_drv3_013_netinc_qoq_rolling_slope_of_d2},
    "ecl_drv3_014_eps_qoq_rolling_slope_of_d2":     {"inputs": ["eps"],     "func": ecl_drv3_014_eps_qoq_rolling_slope_of_d2},
    "ecl_drv3_015_netinc_d2_zscore_4q":             {"inputs": ["netinc"],  "func": ecl_drv3_015_netinc_d2_zscore_4q},
    "ecl_drv3_016_eps_d2_zscore_4q":                {"inputs": ["eps"],     "func": ecl_drv3_016_eps_d2_zscore_4q},
    "ecl_drv3_017_netinc_d2_positive_flag":         {"inputs": ["netinc"],  "func": ecl_drv3_017_netinc_d2_positive_flag},
    "ecl_drv3_018_netinc_d2_negative_flag":         {"inputs": ["netinc"],  "func": ecl_drv3_018_netinc_d2_negative_flag},
    "ecl_drv3_019_netinc_d3_rolling_mean_4q":       {"inputs": ["netinc"],  "func": ecl_drv3_019_netinc_d3_rolling_mean_4q},
    "ecl_drv3_020_eps_d3_rolling_mean_4q":          {"inputs": ["eps"],     "func": ecl_drv3_020_eps_d3_rolling_mean_4q},
    "ecl_drv3_021_netinc_d2_pct_rank_4q":           {"inputs": ["netinc"],  "func": ecl_drv3_021_netinc_d2_pct_rank_4q},
    "ecl_drv3_022_netinc_d3_cumulative_sum_4q":     {"inputs": ["netinc"],  "func": ecl_drv3_022_netinc_d3_cumulative_sum_4q},
    "ecl_drv3_023_netinc_d2_ewm_deviation":         {"inputs": ["netinc"],  "func": ecl_drv3_023_netinc_d2_ewm_deviation},
    "ecl_drv3_024_netinc_d3_expanding_zscore":      {"inputs": ["netinc"],  "func": ecl_drv3_024_netinc_d3_expanding_zscore},
    "ecl_drv3_025_ebit_d2_zscore_4q":               {"inputs": ["ebit"],    "func": ecl_drv3_025_ebit_d2_zscore_4q},
}
