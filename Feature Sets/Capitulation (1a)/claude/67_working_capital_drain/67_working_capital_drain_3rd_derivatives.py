"""
67_working_capital_drain — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative working-capital-drain features
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


# ── 2nd-derivative helpers (self-contained recomputes) ───────────────────────
# Inline the 2nd-derivative base concepts so no cross-file import is needed.

def _wc_qoq(wc: pd.Series) -> pd.Series:
    return wc - wc.shift(_TD_QTR)


def _wc_yoy(wc: pd.Series) -> pd.Series:
    return wc - wc.shift(_TD_YEAR)


def _wc_qoq_pct(wc: pd.Series) -> pd.Series:
    prior = wc.shift(_TD_QTR)
    return _safe_div_abs(wc - prior, prior)


def _wc_yoy_pct(wc: pd.Series) -> pd.Series:
    prior = wc.shift(_TD_YEAR)
    return _safe_div_abs(wc - prior, prior)


def _wc_drawdown_4q(wc: pd.Series) -> pd.Series:
    return wc - _rolling_max(wc, _TD_YEAR)


def _wc_drawdown_8q(wc: pd.Series) -> pd.Series:
    return wc - _rolling_max(wc, _TD_2Y)


def _wc_zscore_4q(wc: pd.Series) -> pd.Series:
    m  = _rolling_mean(wc, _TD_YEAR)
    sd = _rolling_std(wc, _TD_YEAR)
    return _safe_div(wc - m, sd)


def _dso(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(receivables, (revenue / 91.25).abs().replace(0, np.nan))


def _ccc(receivables: pd.Series, inventory: pd.Series,
         payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    dr = (revenue / 91.25).abs().replace(0, np.nan)
    dc = (cor / 91.25).abs().replace(0, np.nan)
    return _safe_div(receivables, dr) + _safe_div(inventory, dc) - _safe_div(payables, dc)


def _wc_to_revenue(wc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(wc, revenue.abs().replace(0, np.nan))


def _drv2_wc_qoq_accel(wc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in QoQ WC change."""
    d1 = _wc_qoq(wc)
    return d1 - d1.shift(_TD_QTR)


def _drv2_wc_drawdown_4q_qoq(wc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in 4Q peak drawdown."""
    base = _wc_drawdown_4q(wc)
    return base - base.shift(_TD_QTR)


def _drv2_wc_zscore_4q_qoq(wc: pd.Series) -> pd.Series:
    """2nd derivative: QoQ change in 4Q z-score."""
    base = _wc_zscore_4q(wc)
    return base - base.shift(_TD_QTR)


def _drv2_ccc_qoq_accel(receivables, inventory, payables, revenue, cor):
    """2nd derivative: QoQ change in QoQ CCC change."""
    ccc = _ccc(receivables, inventory, payables, revenue, cor)
    d1  = ccc - ccc.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_dso_qoq_accel(receivables, revenue):
    """2nd derivative: QoQ change in QoQ DSO change."""
    dso = _dso(receivables, revenue)
    d1  = dso - dso.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def wcd_drv3_001_wc_qoq_accel_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative WC acceleration (3rd difference of WC, QoQ steps)."""
    base = _drv2_wc_qoq_accel(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv3_002_wc_qoq_accel_yoy_diff(workingcapital: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative WC acceleration."""
    base = _drv2_wc_qoq_accel(workingcapital)
    return base - base.shift(_TD_YEAR)


def wcd_drv3_003_wc_drawdown_4q_accel_qoq(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative 4Q-drawdown acceleration."""
    base = _drv2_wc_drawdown_4q_qoq(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv3_004_wc_zscore_accel_qoq(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative z-score acceleration."""
    base = _drv2_wc_zscore_4q_qoq(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv3_005_wc_zscore_accel_yoy(workingcapital: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative z-score acceleration."""
    base = _drv2_wc_zscore_4q_qoq(workingcapital)
    return base - base.shift(_TD_YEAR)


def wcd_drv3_006_ccc_accel_qoq_diff(receivables: pd.Series, inventory: pd.Series,
                                      payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative CCC acceleration (3rd difference of CCC)."""
    base = _drv2_ccc_qoq_accel(receivables, inventory, payables, revenue, cor)
    return base - base.shift(_TD_QTR)


def wcd_drv3_007_dso_accel_qoq_diff(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative DSO acceleration."""
    base = _drv2_dso_qoq_accel(receivables, revenue)
    return base - base.shift(_TD_QTR)


def wcd_drv3_008_wc_yoy_pct_3rd_diff(workingcapital: pd.Series) -> pd.Series:
    """
    3rd-order change: QoQ diff of (QoQ diff of YoY pct change in WC).
    Captures whether the rate-of-change of the rate-of-change of YoY% is accelerating.
    """
    d1 = _wc_yoy_pct(workingcapital)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def wcd_drv3_009_wc_qoq_pct_3rd_diff(workingcapital: pd.Series) -> pd.Series:
    """
    3rd-order change: QoQ diff of (QoQ diff of QoQ pct change in WC).
    """
    d1 = _wc_qoq_pct(workingcapital)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def wcd_drv3_010_wc_drawdown_8q_accel_qoq(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative 8Q-drawdown acceleration."""
    base = _wc_drawdown_8q(workingcapital)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def wcd_drv3_011_wc_to_revenue_3rd_diff(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """3rd-order: QoQ diff of (QoQ diff of QoQ WC-to-revenue change)."""
    ratio = _wc_to_revenue(workingcapital, revenue)
    d1 = ratio - ratio.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def wcd_drv3_012_wc_zscore_slope_of_accel(workingcapital: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the 2nd-derivative (QoQ z-score acceleration) series.
    Trend in the acceleration — convexity of WC z-score deterioration.
    """
    base = _drv2_wc_zscore_4q_qoq(workingcapital)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x    = np.arange(n, dtype=float)
        xm   = x.mean()
        ym   = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def wcd_drv3_013_wc_qoq_accel_ewm_diff(workingcapital: pd.Series) -> pd.Series:
    """
    2nd-derivative WC acceleration minus its own 4-quarter EWM.
    Whether the current acceleration is worse than recent trend.
    """
    base = _drv2_wc_qoq_accel(workingcapital)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def wcd_drv3_014_wc_accel_zscore_4q(workingcapital: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative WC acceleration series within trailing 4 quarters."""
    base = _drv2_wc_qoq_accel(workingcapital)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def wcd_drv3_015_ccc_accel_zscore_4q(receivables: pd.Series, inventory: pd.Series,
                                       payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative CCC acceleration series within trailing 4 quarters."""
    base = _drv2_ccc_qoq_accel(receivables, inventory, payables, revenue, cor)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def wcd_drv3_016_wc_accel_pct_rank_4q(workingcapital: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-derivative WC acceleration within trailing 4-quarter window."""
    base = _drv2_wc_qoq_accel(workingcapital)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def wcd_drv3_017_wc_drawdown_accel_pct_rank_4q(workingcapital: pd.Series) -> pd.Series:
    """Percentile rank of 2nd-derivative 4Q-drawdown acceleration within trailing 4 quarters."""
    base = _drv2_wc_drawdown_4q_qoq(workingcapital)
    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def wcd_drv3_018_wc_accel_is_negative(workingcapital: pd.Series) -> pd.Series:
    """Binary: 1 when the 2nd-derivative WC acceleration is negative (drain worsening faster)."""
    base = _drv2_wc_qoq_accel(workingcapital)
    return (base < 0).astype(float)


def wcd_drv3_019_wc_accel_negative_count_4q(workingcapital: pd.Series) -> pd.Series:
    """Count of days in trailing 4-quarter window where WC acceleration was negative."""
    base = _drv2_wc_qoq_accel(workingcapital)
    neg  = (base < 0).astype(float)
    return neg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()


def wcd_drv3_020_ccc_accel_yoy_diff(receivables: pd.Series, inventory: pd.Series,
                                      payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative CCC acceleration."""
    base = _drv2_ccc_qoq_accel(receivables, inventory, payables, revenue, cor)
    return base - base.shift(_TD_YEAR)


def wcd_drv3_021_wc_yoy_accel_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """
    QoQ diff of (YoY change in QoQ WC change) — 3rd-order cross-horizon derivative.
    Captures whether the annual perspective on WC acceleration is itself changing.
    """
    d1_qoq = _wc_qoq(workingcapital)
    d2_yoy = d1_qoq - d1_qoq.shift(_TD_YEAR)
    return d2_yoy - d2_yoy.shift(_TD_QTR)


def wcd_drv3_022_wc_drawdown_accel_ewm_diff(workingcapital: pd.Series) -> pd.Series:
    """
    2nd-derivative 4Q-drawdown acceleration minus its own 4-quarter EWM.
    Captures whether the drawdown acceleration is worsening vs recent trend.
    """
    base = _drv2_wc_drawdown_4q_qoq(workingcapital)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def wcd_drv3_023_dso_accel_zscore_4q(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of the 2nd-derivative DSO acceleration within trailing 4-quarter window."""
    base = _drv2_dso_qoq_accel(receivables, revenue)
    m  = _rolling_mean(base, _TD_YEAR)
    sd = _rolling_std(base, _TD_YEAR)
    return _safe_div(base - m, sd)


def wcd_drv3_024_wc_accel_expanding_zscore(workingcapital: pd.Series) -> pd.Series:
    """Expanding z-score of the 2nd-derivative WC acceleration (how extreme vs all history)."""
    base = _drv2_wc_qoq_accel(workingcapital)
    m  = base.expanding(min_periods=2).mean()
    sd = base.expanding(min_periods=2).std()
    return _safe_div(base - m, sd)


def wcd_drv3_025_wc_drain_3rd_order_composite(workingcapital: pd.Series,
                                                receivables: pd.Series,
                                                inventory: pd.Series,
                                                payables: pd.Series,
                                                revenue: pd.Series,
                                                cor: pd.Series) -> pd.Series:
    """
    3rd-derivative composite severity: equally weighted mean of three 4Q z-scores —
    WC acceleration, CCC acceleration, DSO acceleration.
    More negative = faster-worsening drain in all three dimensions simultaneously.
    """
    wc_accel  = _drv2_wc_qoq_accel(workingcapital)
    ccc_accel = _drv2_ccc_qoq_accel(receivables, inventory, payables, revenue, cor)
    dso_accel = _drv2_dso_qoq_accel(receivables, revenue)

    def _z4q(s):
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    return (_z4q(wc_accel) + _z4q(ccc_accel) + _z4q(dso_accel)) / 3.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

WORKING_CAPITAL_DRAIN_REGISTRY_3RD_DERIVATIVES = {
    "wcd_drv3_001_wc_qoq_accel_qoq_diff":       {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_001_wc_qoq_accel_qoq_diff},
    "wcd_drv3_002_wc_qoq_accel_yoy_diff":        {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_002_wc_qoq_accel_yoy_diff},
    "wcd_drv3_003_wc_drawdown_4q_accel_qoq":     {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_003_wc_drawdown_4q_accel_qoq},
    "wcd_drv3_004_wc_zscore_accel_qoq":          {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_004_wc_zscore_accel_qoq},
    "wcd_drv3_005_wc_zscore_accel_yoy":          {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_005_wc_zscore_accel_yoy},
    "wcd_drv3_006_ccc_accel_qoq_diff":           {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],                     "func": wcd_drv3_006_ccc_accel_qoq_diff},
    "wcd_drv3_007_dso_accel_qoq_diff":           {"inputs": ["receivables", "revenue"],                                                      "func": wcd_drv3_007_dso_accel_qoq_diff},
    "wcd_drv3_008_wc_yoy_pct_3rd_diff":          {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_008_wc_yoy_pct_3rd_diff},
    "wcd_drv3_009_wc_qoq_pct_3rd_diff":          {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_009_wc_qoq_pct_3rd_diff},
    "wcd_drv3_010_wc_drawdown_8q_accel_qoq":     {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_010_wc_drawdown_8q_accel_qoq},
    "wcd_drv3_011_wc_to_revenue_3rd_diff":       {"inputs": ["workingcapital", "revenue"],                                                   "func": wcd_drv3_011_wc_to_revenue_3rd_diff},
    "wcd_drv3_012_wc_zscore_slope_of_accel":     {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_012_wc_zscore_slope_of_accel},
    "wcd_drv3_013_wc_qoq_accel_ewm_diff":        {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_013_wc_qoq_accel_ewm_diff},
    "wcd_drv3_014_wc_accel_zscore_4q":           {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_014_wc_accel_zscore_4q},
    "wcd_drv3_015_ccc_accel_zscore_4q":          {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],                     "func": wcd_drv3_015_ccc_accel_zscore_4q},
    "wcd_drv3_016_wc_accel_pct_rank_4q":         {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_016_wc_accel_pct_rank_4q},
    "wcd_drv3_017_wc_drawdown_accel_pct_rank_4q": {"inputs": ["workingcapital"],                                                             "func": wcd_drv3_017_wc_drawdown_accel_pct_rank_4q},
    "wcd_drv3_018_wc_accel_is_negative":          {"inputs": ["workingcapital"],                                                             "func": wcd_drv3_018_wc_accel_is_negative},
    "wcd_drv3_019_wc_accel_negative_count_4q":    {"inputs": ["workingcapital"],                                                             "func": wcd_drv3_019_wc_accel_negative_count_4q},
    "wcd_drv3_020_ccc_accel_yoy_diff":            {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],                     "func": wcd_drv3_020_ccc_accel_yoy_diff},
    "wcd_drv3_021_wc_yoy_accel_qoq_diff":         {"inputs": ["workingcapital"],                                                             "func": wcd_drv3_021_wc_yoy_accel_qoq_diff},
    "wcd_drv3_022_wc_drawdown_accel_ewm_diff":    {"inputs": ["workingcapital"],                                                             "func": wcd_drv3_022_wc_drawdown_accel_ewm_diff},
    "wcd_drv3_023_dso_accel_zscore_4q":           {"inputs": ["receivables", "revenue"],                                                      "func": wcd_drv3_023_dso_accel_zscore_4q},
    "wcd_drv3_024_wc_accel_expanding_zscore":     {"inputs": ["workingcapital"],                                                              "func": wcd_drv3_024_wc_accel_expanding_zscore},
    "wcd_drv3_025_wc_drain_3rd_order_composite":  {"inputs": ["workingcapital", "receivables", "inventory", "payables", "revenue", "cor"],   "func": wcd_drv3_025_wc_drain_3rd_order_composite},
}
