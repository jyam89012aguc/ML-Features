"""
61_revenue_deterioration — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative revenue-deterioration features —
captures the jerk/curvature of top-line contraction momentum.
Asset class: US equities | Sharadar SF1 fundamentals ONLY (no price/volume)
Target context: capitulation — absolute multi-year low / maximum distress

All inputs are daily-frequency Series, forward-filled from the most recent
quarterly Sharadar SF1 report known as of each date (pipeline contract).
Functions look strictly backward — no future information.

Because SF1 data steps only ~4x/year on the daily index, these 3rd-derivative
outputs will be very sparse/stepwise — this is expected and correct.  They
capture whether the acceleration of deterioration is itself accelerating.

Quarterly cadence on daily index:
    1 quarter  ~  63 trading days
    1 year     ~ 252 trading days
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2YEAR = 504
_TD_3YEAR = 756
_TD_5YEAR = 1260
_TD_QTR   = 63
_TD_HALF  = 126
_EPS      = 1e-9

# ── Alignment helper ──────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Re-index a quarterly SF1 Series onto a daily trading-day index and
    forward-fill gaps.  Contract: all feature-function inputs in this file
    have already been aligned this way by the upstream pipeline; this helper
    is provided for documentation and optional manual use only.
    """
    return q_series.reindex(daily_index).ffill()

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/NaN denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        n = len(x)
        if n < 2:
            return np.nan
        xi   = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        denom = ((xi - xi_m) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((xi - xi_m) * (x - x_m)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=True)


# ── Helper: compute 2nd-derivative base values (inline, self-contained) ───────

def _d2_rev_qoq_pct_63d_diff(revenue: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of QoQ revenue % change."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return g.diff(_TD_QTR)


def _d2_rev_yoy_pct_63d_diff(revenue: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of YoY revenue % change."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return g.diff(_TD_QTR)


def _d2_rev_dd_4q_peak_63d_diff(revenue: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of 4-quarter revenue drawdown."""
    peak = _rolling_max(revenue, _TD_YEAR)
    dd   = _safe_div(revenue - peak, peak.abs())
    return dd.diff(_TD_QTR)


def _d2_rev_dd_ath_63d_diff(revenue: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of all-time revenue drawdown."""
    peak = revenue.expanding(min_periods=1).max()
    dd   = _safe_div(revenue - peak, peak.abs())
    return dd.diff(_TD_QTR)


def _d2_rev_vs_4q_avg_63d_diff(revenue: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of revenue vs 4-quarter average."""
    avg = _rolling_mean(revenue, _TD_YEAR)
    dev = _safe_div(revenue - avg, avg.abs())
    return dev.diff(_TD_QTR)


def _d2_rev_zscore_4q_63d_diff(revenue: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of revenue z-score."""
    z = _zscore_rolling(revenue, _TD_YEAR)
    return z.diff(_TD_QTR)


def _d2_rev_qoq_pct_252d_slope(revenue: pd.Series) -> pd.Series:
    """2nd derivative: OLS slope of QoQ revenue growth over 252-day window."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return _linslope(g, _TD_YEAR)


def _d2_rev_yoy_pct_504d_slope(revenue: pd.Series) -> pd.Series:
    """2nd derivative: OLS slope of YoY revenue growth over 504-day window."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return _linslope(g, _TD_2YEAR)


def _d2_gp_pct_of_rev_63d_diff(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of gross margin."""
    m = _safe_div(gp, revenue)
    return m.diff(_TD_QTR)


def _d2_receivables_to_rev_63d_diff(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of receivables/revenue."""
    ratio = _safe_div(receivables, revenue)
    return ratio.diff(_TD_QTR)


def _d2_composite_det_63d_diff(revenue: pd.Series) -> pd.Series:
    """2nd derivative: 63-day diff of composite deterioration index."""
    g_yoy = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    g_qoq = _safe_div(revenue - revenue.shift(_TD_QTR),  revenue.shift(_TD_QTR).abs())
    peak  = _rolling_max(revenue, _TD_YEAR)
    dd    = _safe_div(revenue - peak, peak.abs())
    z_yoy = _zscore_rolling(g_yoy, _TD_2YEAR)
    z_qoq = _zscore_rolling(g_qoq, _TD_2YEAR)
    z_dd  = _zscore_rolling(dd,    _TD_2YEAR)
    composite = (z_yoy + z_qoq + z_dd) / 3.0
    return composite.diff(_TD_QTR)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def rvd_drv3_001_rev_qoq_pct_63d_diff2(revenue: pd.Series) -> pd.Series:
    """2nd diff (jerk) of QoQ revenue % change (further acceleration of QoQ velocity)."""
    d2 = _d2_rev_qoq_pct_63d_diff(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_002_rev_yoy_pct_63d_diff2(revenue: pd.Series) -> pd.Series:
    """2nd diff of YoY revenue % change (jerk of YoY growth acceleration)."""
    d2 = _d2_rev_yoy_pct_63d_diff(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_003_rev_dd_4q_peak_63d_diff2(revenue: pd.Series) -> pd.Series:
    """2nd diff of 4-quarter revenue drawdown (jerk of peak-distance widening)."""
    d2 = _d2_rev_dd_4q_peak_63d_diff(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_004_rev_dd_ath_63d_diff2(revenue: pd.Series) -> pd.Series:
    """2nd diff of all-time revenue drawdown (jerk of ATH distance worsening)."""
    d2 = _d2_rev_dd_ath_63d_diff(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_005_rev_vs_4q_avg_63d_diff2(revenue: pd.Series) -> pd.Series:
    """2nd diff of revenue vs 4-quarter average (jerk of average breakdown)."""
    d2 = _d2_rev_vs_4q_avg_63d_diff(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_006_rev_zscore_4q_63d_diff2(revenue: pd.Series) -> pd.Series:
    """2nd diff of revenue z-score within 4-quarter window (jerk of statistical extremity)."""
    d2 = _d2_rev_zscore_4q_63d_diff(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_007_rev_qoq_pct_252d_slope_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of the OLS slope of QoQ revenue growth (slope-of-slope)."""
    d2 = _d2_rev_qoq_pct_252d_slope(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_008_rev_yoy_pct_504d_slope_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of the OLS slope of YoY revenue growth (slope-of-slope)."""
    d2 = _d2_rev_yoy_pct_504d_slope(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_009_rev_qoq_pct_63d_diff_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope over 252 days of the 2nd-derivative QoQ series (trend of acceleration)."""
    d2 = _d2_rev_qoq_pct_63d_diff(revenue)
    return _linslope(d2, _TD_YEAR)


def rvd_drv3_010_rev_yoy_pct_63d_diff_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope over 252 days of the 2nd-derivative YoY series (trend of acceleration)."""
    d2 = _d2_rev_yoy_pct_63d_diff(revenue)
    return _linslope(d2, _TD_YEAR)


def rvd_drv3_011_rev_dd_4q_63d_diff_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope over 252 days of the 4q-drawdown 2nd derivative (trend of drawdown accel)."""
    d2 = _d2_rev_dd_4q_peak_63d_diff(revenue)
    return _linslope(d2, _TD_YEAR)


def rvd_drv3_012_rev_composite_det_63d_diff2(revenue: pd.Series) -> pd.Series:
    """2nd diff of composite deterioration index (jerk of composite signal)."""
    d2 = _d2_composite_det_63d_diff(revenue)
    return d2.diff(_TD_QTR)


def rvd_drv3_013_rev_qoq_pct_63d_diff_ewm(revenue: pd.Series) -> pd.Series:
    """EWM-smoothed 2nd-derivative QoQ revenue % change (de-noised acceleration)."""
    d2 = _d2_rev_qoq_pct_63d_diff(revenue)
    return _ewm_mean(d2, _TD_YEAR)


def rvd_drv3_014_rev_yoy_pct_63d_diff_ewm(revenue: pd.Series) -> pd.Series:
    """EWM-smoothed 2nd-derivative YoY revenue % change."""
    d2 = _d2_rev_yoy_pct_63d_diff(revenue)
    return _ewm_mean(d2, _TD_YEAR)


def rvd_drv3_015_rev_dd_ath_63d_diff_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope over 252 days of ATH-drawdown 2nd derivative."""
    d2 = _d2_rev_dd_ath_63d_diff(revenue)
    return _linslope(d2, _TD_YEAR)


def rvd_drv3_016_rev_qoq_pct_63d_diff_zscore(revenue: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative QoQ revenue % change within 4-quarter window."""
    d2 = _d2_rev_qoq_pct_63d_diff(revenue)
    return _zscore_rolling(d2, _TD_YEAR)


def rvd_drv3_017_rev_yoy_pct_63d_diff_zscore(revenue: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative YoY revenue % change within 4-quarter window."""
    d2 = _d2_rev_yoy_pct_63d_diff(revenue)
    return _zscore_rolling(d2, _TD_YEAR)


def rvd_drv3_018_rev_dd_4q_63d_diff_zscore(revenue: pd.Series) -> pd.Series:
    """Z-score of 2nd-derivative 4q-drawdown within 4-quarter window."""
    d2 = _d2_rev_dd_4q_peak_63d_diff(revenue)
    return _zscore_rolling(d2, _TD_YEAR)


def rvd_drv3_019_gp_pct_of_rev_63d_diff2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """2nd diff of gross margin (jerk of margin compression)."""
    d2 = _d2_gp_pct_of_rev_63d_diff(revenue, gp)
    return d2.diff(_TD_QTR)


def rvd_drv3_020_receivables_to_rev_63d_diff2(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """2nd diff of receivables/revenue ratio (jerk of demand-quality signal)."""
    d2 = _d2_receivables_to_rev_63d_diff(revenue, receivables)
    return d2.diff(_TD_QTR)


def rvd_drv3_021_rev_qoq_pct_63d_diff_pct_chg(revenue: pd.Series) -> pd.Series:
    """Percent change in 2nd-derivative QoQ over a 63-day lag (relative jerk)."""
    d2    = _d2_rev_qoq_pct_63d_diff(revenue)
    prior = d2.shift(_TD_QTR).abs()
    return _safe_div(d2 - d2.shift(_TD_QTR), prior)


def rvd_drv3_022_rev_yoy_pct_63d_diff_pct_chg(revenue: pd.Series) -> pd.Series:
    """Percent change in 2nd-derivative YoY over a 63-day lag (relative jerk)."""
    d2    = _d2_rev_yoy_pct_63d_diff(revenue)
    prior = d2.shift(_TD_QTR).abs()
    return _safe_div(d2 - d2.shift(_TD_QTR), prior)


def rvd_drv3_023_rev_qoq_pct_63d_diff_4q_avg(revenue: pd.Series) -> pd.Series:
    """4-quarter rolling average of 2nd-derivative QoQ (smoothed acceleration level)."""
    d2 = _d2_rev_qoq_pct_63d_diff(revenue)
    return _rolling_mean(d2, _TD_YEAR)


def rvd_drv3_024_rev_yoy_pct_63d_diff_4q_avg(revenue: pd.Series) -> pd.Series:
    """4-quarter rolling average of 2nd-derivative YoY (smoothed acceleration level)."""
    d2 = _d2_rev_yoy_pct_63d_diff(revenue)
    return _rolling_mean(d2, _TD_YEAR)


def rvd_drv3_025_rev_3d_composite_jerk(revenue: pd.Series) -> pd.Series:
    """
    3rd-derivative composite jerk: equal-weight average of jerk signals from
    QoQ, YoY, and 4q-drawdown 2nd derivatives.  Most negative = sharpest
    acceleration of revenue deterioration.
    """
    d2_qoq = _d2_rev_qoq_pct_63d_diff(revenue)
    d2_yoy = _d2_rev_yoy_pct_63d_diff(revenue)
    d2_dd  = _d2_rev_dd_4q_peak_63d_diff(revenue)
    j_qoq  = d2_qoq.diff(_TD_QTR)
    j_yoy  = d2_yoy.diff(_TD_QTR)
    j_dd   = d2_dd.diff(_TD_QTR)
    return (j_qoq + j_yoy + j_dd) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

REVENUE_DETERIORATION_REGISTRY_3RD_DERIVATIVES = {
    "rvd_drv3_001_rev_qoq_pct_63d_diff2": {"inputs": ["revenue"], "func": rvd_drv3_001_rev_qoq_pct_63d_diff2},
    "rvd_drv3_002_rev_yoy_pct_63d_diff2": {"inputs": ["revenue"], "func": rvd_drv3_002_rev_yoy_pct_63d_diff2},
    "rvd_drv3_003_rev_dd_4q_peak_63d_diff2": {"inputs": ["revenue"], "func": rvd_drv3_003_rev_dd_4q_peak_63d_diff2},
    "rvd_drv3_004_rev_dd_ath_63d_diff2": {"inputs": ["revenue"], "func": rvd_drv3_004_rev_dd_ath_63d_diff2},
    "rvd_drv3_005_rev_vs_4q_avg_63d_diff2": {"inputs": ["revenue"], "func": rvd_drv3_005_rev_vs_4q_avg_63d_diff2},
    "rvd_drv3_006_rev_zscore_4q_63d_diff2": {"inputs": ["revenue"], "func": rvd_drv3_006_rev_zscore_4q_63d_diff2},
    "rvd_drv3_007_rev_qoq_pct_252d_slope_63d_diff": {"inputs": ["revenue"], "func": rvd_drv3_007_rev_qoq_pct_252d_slope_63d_diff},
    "rvd_drv3_008_rev_yoy_pct_504d_slope_63d_diff": {"inputs": ["revenue"], "func": rvd_drv3_008_rev_yoy_pct_504d_slope_63d_diff},
    "rvd_drv3_009_rev_qoq_pct_63d_diff_252d_slope": {"inputs": ["revenue"], "func": rvd_drv3_009_rev_qoq_pct_63d_diff_252d_slope},
    "rvd_drv3_010_rev_yoy_pct_63d_diff_252d_slope": {"inputs": ["revenue"], "func": rvd_drv3_010_rev_yoy_pct_63d_diff_252d_slope},
    "rvd_drv3_011_rev_dd_4q_63d_diff_252d_slope": {"inputs": ["revenue"], "func": rvd_drv3_011_rev_dd_4q_63d_diff_252d_slope},
    "rvd_drv3_012_rev_composite_det_63d_diff2": {"inputs": ["revenue"], "func": rvd_drv3_012_rev_composite_det_63d_diff2},
    "rvd_drv3_013_rev_qoq_pct_63d_diff_ewm": {"inputs": ["revenue"], "func": rvd_drv3_013_rev_qoq_pct_63d_diff_ewm},
    "rvd_drv3_014_rev_yoy_pct_63d_diff_ewm": {"inputs": ["revenue"], "func": rvd_drv3_014_rev_yoy_pct_63d_diff_ewm},
    "rvd_drv3_015_rev_dd_ath_63d_diff_252d_slope": {"inputs": ["revenue"], "func": rvd_drv3_015_rev_dd_ath_63d_diff_252d_slope},
    "rvd_drv3_016_rev_qoq_pct_63d_diff_zscore": {"inputs": ["revenue"], "func": rvd_drv3_016_rev_qoq_pct_63d_diff_zscore},
    "rvd_drv3_017_rev_yoy_pct_63d_diff_zscore": {"inputs": ["revenue"], "func": rvd_drv3_017_rev_yoy_pct_63d_diff_zscore},
    "rvd_drv3_018_rev_dd_4q_63d_diff_zscore": {"inputs": ["revenue"], "func": rvd_drv3_018_rev_dd_4q_63d_diff_zscore},
    "rvd_drv3_019_gp_pct_of_rev_63d_diff2": {"inputs": ["revenue", "gp"], "func": rvd_drv3_019_gp_pct_of_rev_63d_diff2},
    "rvd_drv3_020_receivables_to_rev_63d_diff2": {"inputs": ["revenue", "receivables"], "func": rvd_drv3_020_receivables_to_rev_63d_diff2},
    "rvd_drv3_021_rev_qoq_pct_63d_diff_pct_chg": {"inputs": ["revenue"], "func": rvd_drv3_021_rev_qoq_pct_63d_diff_pct_chg},
    "rvd_drv3_022_rev_yoy_pct_63d_diff_pct_chg": {"inputs": ["revenue"], "func": rvd_drv3_022_rev_yoy_pct_63d_diff_pct_chg},
    "rvd_drv3_023_rev_qoq_pct_63d_diff_4q_avg": {"inputs": ["revenue"], "func": rvd_drv3_023_rev_qoq_pct_63d_diff_4q_avg},
    "rvd_drv3_024_rev_yoy_pct_63d_diff_4q_avg": {"inputs": ["revenue"], "func": rvd_drv3_024_rev_yoy_pct_63d_diff_4q_avg},
    "rvd_drv3_025_rev_3d_composite_jerk": {"inputs": ["revenue"], "func": rvd_drv3_025_rev_3d_composite_jerk},
}
