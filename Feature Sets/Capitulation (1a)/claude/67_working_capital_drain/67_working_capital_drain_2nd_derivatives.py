"""
67_working_capital_drain — 2nd-Derivative Features 001-025
Domain: rate of change of base working-capital-drain features
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


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline the relevant base computations so this file needs no cross-import.

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


def _cash_drawdown_4q(cash: pd.Series) -> pd.Series:
    return cash - _rolling_max(cash, _TD_YEAR)


def _noncash_wc(assetsc: pd.Series, cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return (assetsc - cashnequiv) - liabilitiesc


def _wc_drain_speed_4q(wc: pd.Series) -> pd.Series:
    return (wc - wc.shift(_TD_YEAR)) / 4.0


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def wcd_drv2_001_wc_qoq_change_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the QoQ WC change (acceleration of WC drain, 2nd difference)."""
    base = _wc_qoq(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_002_wc_yoy_change_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the YoY WC change (how fast the YoY trend is shifting)."""
    base = _wc_yoy(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_003_wc_qoq_pct_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the QoQ percent-change of WC."""
    base = _wc_qoq_pct(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_004_wc_yoy_pct_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent-change of WC (2nd-order YoY momentum shift)."""
    base = _wc_yoy_pct(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_005_wc_drawdown_4q_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter peak drawdown of WC (drawdown worsening rate)."""
    base = _wc_drawdown_4q(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_006_wc_drawdown_8q_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 8-quarter peak drawdown of WC."""
    base = _wc_drawdown_8q(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_007_wc_drawdown_4q_yoy_diff(workingcapital: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter peak drawdown of WC."""
    base = _wc_drawdown_4q(workingcapital)
    return base - base.shift(_TD_YEAR)


def wcd_drv2_008_wc_zscore_4q_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of WC (z-score deterioration rate)."""
    base = _wc_zscore_4q(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_009_wc_zscore_4q_yoy_diff(workingcapital: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of WC."""
    base = _wc_zscore_4q(workingcapital)
    return base - base.shift(_TD_YEAR)


def wcd_drv2_010_dso_qoq_diff_of_diff(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the QoQ DSO change (DSO deterioration acceleration)."""
    dso = _dso(receivables, revenue)
    d1  = dso - dso.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def wcd_drv2_011_ccc_qoq_diff_of_diff(receivables: pd.Series, inventory: pd.Series,
                                        payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """QoQ change in the QoQ CCC change (CCC deterioration acceleration)."""
    ccc = _ccc(receivables, inventory, payables, revenue, cor)
    d1  = ccc - ccc.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def wcd_drv2_012_ccc_yoy_diff(receivables: pd.Series, inventory: pd.Series,
                                payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY change in the QoQ CCC change (annual perspective on CCC acceleration)."""
    ccc = _ccc(receivables, inventory, payables, revenue, cor)
    d1  = ccc - ccc.shift(_TD_QTR)
    return d1 - d1.shift(_TD_YEAR)


def wcd_drv2_013_wc_to_revenue_qoq_diff_of_diff(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the QoQ WC-to-revenue ratio change (2nd order ratio drain)."""
    base = _wc_to_revenue(workingcapital, revenue)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def wcd_drv2_014_cash_drawdown_4q_qoq_diff(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter cash peak drawdown."""
    base = _cash_drawdown_4q(cashnequiv)
    return base - base.shift(_TD_QTR)


def wcd_drv2_015_noncash_wc_qoq_diff_of_diff(assetsc: pd.Series, cashnequiv: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ non-cash WC change (non-cash WC drain acceleration)."""
    base = _noncash_wc(assetsc, cashnequiv, liabilitiesc)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def wcd_drv2_016_wc_drain_speed_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter average WC drain speed."""
    base = _wc_drain_speed_4q(workingcapital)
    return base - base.shift(_TD_QTR)


def wcd_drv2_017_wc_qoq_slope_of_qoq(workingcapital: pd.Series) -> pd.Series:
    """
    Rolling 4-quarter OLS slope of the QoQ WC-change series.
    Captures the trend in QoQ WC momentum (negative slope = worsening drain).
    """
    base = _wc_qoq(workingcapital)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x   = np.arange(n, dtype=float)
        xm  = x.mean()
        ym  = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def wcd_drv2_018_wc_yoy_pct_yoy_diff(workingcapital: pd.Series) -> pd.Series:
    """YoY change in the YoY percent-change of WC (2nd-order YoY momentum)."""
    base = _wc_yoy_pct(workingcapital)
    return base - base.shift(_TD_YEAR)


def wcd_drv2_019_wc_qoq_pct_chg_of_chg(workingcapital: pd.Series) -> pd.Series:
    """Percent change of the QoQ WC-change series (relative acceleration)."""
    base = _wc_qoq(workingcapital)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def wcd_drv2_020_dso_zscore_4q_qoq_diff(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of DSO."""
    dso  = _dso(receivables, revenue)
    m    = _rolling_mean(dso, _TD_YEAR)
    sd   = _rolling_std(dso, _TD_YEAR)
    base = _safe_div(dso - m, sd)
    return base - base.shift(_TD_QTR)


def wcd_drv2_021_wc_drawdown_pct_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """
    QoQ change in (WC percent drawdown from 4Q peak).
    Captures acceleration of pct-drawdown worsening.
    """
    peak = _rolling_max(workingcapital, _TD_YEAR)
    base = _safe_div_abs(workingcapital - peak, peak)
    return base - base.shift(_TD_QTR)


def wcd_drv2_022_wc_zscore_8q_qoq_diff(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in the 8-quarter z-score of WC."""
    m  = _rolling_mean(workingcapital, _TD_2Y)
    sd = _rolling_std(workingcapital, _TD_2Y)
    base = _safe_div(workingcapital - m, sd)
    return base - base.shift(_TD_QTR)


def wcd_drv2_023_wc_qoq_ewm_diff(workingcapital: pd.Series) -> pd.Series:
    """
    Current QoQ WC change minus its own 4-quarter EWM (span=252).
    Measures whether the current QoQ drain is worse than its recent trend.
    """
    base = _wc_qoq(workingcapital)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def wcd_drv2_024_payables_yoy_diff_of_ratio(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """
    QoQ change in the YoY change in payables-to-COGS ratio.
    Captures whether payables stretching is accelerating on a YoY basis.
    """
    ratio = _safe_div(payables, cor.abs().replace(0, np.nan))
    base  = ratio - ratio.shift(_TD_YEAR)
    return base - base.shift(_TD_QTR)


def wcd_drv2_025_wc_cumulative_drain_accel(workingcapital: pd.Series) -> pd.Series:
    """
    Change in the cumulative 4Q WC drain from its expanding minimum (2nd order):
    QoQ diff of (cumulative_4q_drain - expanding_min(cumulative_4q_drain)).
    Rising = drain is compounding faster.
    """
    dw   = workingcapital - workingcapital.shift(_TD_QTR)
    cum  = dw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    peak = cum.expanding(min_periods=1).min()
    base = cum - peak
    return base - base.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

WORKING_CAPITAL_DRAIN_REGISTRY_2ND_DERIVATIVES = {
    "wcd_drv2_001_wc_qoq_change_qoq_diff":        {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_001_wc_qoq_change_qoq_diff},
    "wcd_drv2_002_wc_yoy_change_qoq_diff":        {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_002_wc_yoy_change_qoq_diff},
    "wcd_drv2_003_wc_qoq_pct_qoq_diff":           {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_003_wc_qoq_pct_qoq_diff},
    "wcd_drv2_004_wc_yoy_pct_qoq_diff":           {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_004_wc_yoy_pct_qoq_diff},
    "wcd_drv2_005_wc_drawdown_4q_qoq_diff":       {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_005_wc_drawdown_4q_qoq_diff},
    "wcd_drv2_006_wc_drawdown_8q_qoq_diff":       {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_006_wc_drawdown_8q_qoq_diff},
    "wcd_drv2_007_wc_drawdown_4q_yoy_diff":       {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_007_wc_drawdown_4q_yoy_diff},
    "wcd_drv2_008_wc_zscore_4q_qoq_diff":         {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_008_wc_zscore_4q_qoq_diff},
    "wcd_drv2_009_wc_zscore_4q_yoy_diff":         {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_009_wc_zscore_4q_yoy_diff},
    "wcd_drv2_010_dso_qoq_diff_of_diff":          {"inputs": ["receivables", "revenue"],                                            "func": wcd_drv2_010_dso_qoq_diff_of_diff},
    "wcd_drv2_011_ccc_qoq_diff_of_diff":          {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],           "func": wcd_drv2_011_ccc_qoq_diff_of_diff},
    "wcd_drv2_012_ccc_yoy_diff":                  {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],           "func": wcd_drv2_012_ccc_yoy_diff},
    "wcd_drv2_013_wc_to_revenue_qoq_diff_of_diff": {"inputs": ["workingcapital", "revenue"],                                       "func": wcd_drv2_013_wc_to_revenue_qoq_diff_of_diff},
    "wcd_drv2_014_cash_drawdown_4q_qoq_diff":     {"inputs": ["cashnequiv"],                                                       "func": wcd_drv2_014_cash_drawdown_4q_qoq_diff},
    "wcd_drv2_015_noncash_wc_qoq_diff_of_diff":   {"inputs": ["assetsc", "cashnequiv", "liabilitiesc"],                            "func": wcd_drv2_015_noncash_wc_qoq_diff_of_diff},
    "wcd_drv2_016_wc_drain_speed_qoq_diff":       {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_016_wc_drain_speed_qoq_diff},
    "wcd_drv2_017_wc_qoq_slope_of_qoq":          {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_017_wc_qoq_slope_of_qoq},
    "wcd_drv2_018_wc_yoy_pct_yoy_diff":           {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_018_wc_yoy_pct_yoy_diff},
    "wcd_drv2_019_wc_qoq_pct_chg_of_chg":        {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_019_wc_qoq_pct_chg_of_chg},
    "wcd_drv2_020_dso_zscore_4q_qoq_diff":        {"inputs": ["receivables", "revenue"],                                            "func": wcd_drv2_020_dso_zscore_4q_qoq_diff},
    "wcd_drv2_021_wc_drawdown_pct_qoq_diff":      {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_021_wc_drawdown_pct_qoq_diff},
    "wcd_drv2_022_wc_zscore_8q_qoq_diff":         {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_022_wc_zscore_8q_qoq_diff},
    "wcd_drv2_023_wc_qoq_ewm_diff":              {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_023_wc_qoq_ewm_diff},
    "wcd_drv2_024_payables_yoy_diff_of_ratio":    {"inputs": ["payables", "cor"],                                                   "func": wcd_drv2_024_payables_yoy_diff_of_ratio},
    "wcd_drv2_025_wc_cumulative_drain_accel":     {"inputs": ["workingcapital"],                                                    "func": wcd_drv2_025_wc_cumulative_drain_accel},
}
