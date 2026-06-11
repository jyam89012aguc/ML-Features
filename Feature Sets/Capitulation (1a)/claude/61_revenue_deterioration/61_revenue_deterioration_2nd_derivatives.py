"""
61_revenue_deterioration — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base revenue-deterioration features — captures
acceleration of top-line contraction and momentum of growth reversal.
Asset class: US equities | Sharadar SF1 fundamentals ONLY (no price/volume)
Target context: capitulation — absolute multi-year low / maximum distress

All inputs are daily-frequency Series, forward-filled from the most recent
quarterly Sharadar SF1 report known as of each date (pipeline contract).
Functions look strictly backward — no future information.

Because SF1 data steps only ~4x/year on the daily index, diff() and slope
outputs will be stepwise/sparse — this is expected and correct.

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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rvd_drv2_001_rev_qoq_pct_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of QoQ revenue % change (acceleration of QoQ growth deterioration)."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return g.diff(_TD_QTR)


def rvd_drv2_002_rev_yoy_pct_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of YoY revenue % change (acceleration of YoY growth deterioration)."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return g.diff(_TD_QTR)


def rvd_drv2_003_rev_yoy_pct_252d_diff(revenue: pd.Series) -> pd.Series:
    """252-day diff of YoY revenue % change (year-over-year acceleration of annual growth)."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return g.diff(_TD_YEAR)


def rvd_drv2_004_rev_dd_4q_peak_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of 4-quarter revenue drawdown (acceleration of peak-distance widening)."""
    peak = _rolling_max(revenue, _TD_YEAR)
    dd   = _safe_div(revenue - peak, peak.abs())
    return dd.diff(_TD_QTR)


def rvd_drv2_005_rev_dd_ath_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of all-time revenue drawdown (acceleration of ATH distance worsening)."""
    peak = revenue.expanding(min_periods=1).max()
    dd   = _safe_div(revenue - peak, peak.abs())
    return dd.diff(_TD_QTR)


def rvd_drv2_006_rev_yoy_log_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of YoY log-revenue change (log-velocity acceleration)."""
    log_g = _log_safe(revenue) - _log_safe(revenue.shift(_TD_YEAR))
    return log_g.diff(_TD_QTR)


def rvd_drv2_007_rev_qoq_pct_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope of QoQ revenue growth rate over trailing 252-day (4-quarter) window."""
    g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    return _linslope(g, _TD_YEAR)


def rvd_drv2_008_rev_yoy_pct_504d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope of YoY revenue growth rate over trailing 504-day (8-quarter) window."""
    g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    return _linslope(g, _TD_2YEAR)


def rvd_drv2_009_rev_qoq_decline_count_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of QoQ-decline count over 4-quarter window (pace of worsening count)."""
    flag  = ((revenue - revenue.shift(_TD_QTR)) < 0).astype(float)
    count = flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).sum()
    return count.diff(_TD_QTR)


def rvd_drv2_010_rev_vs_4q_avg_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of (revenue vs 4-quarter avg) ratio (pace of average breakdown)."""
    avg = _rolling_mean(revenue, _TD_YEAR)
    dev = _safe_div(revenue - avg, avg.abs())
    return dev.diff(_TD_QTR)


def rvd_drv2_011_rev_zscore_4q_63d_diff(revenue: pd.Series) -> pd.Series:
    """63-day diff of revenue z-score within 4-quarter window (statistical acceleration)."""
    z = _zscore_rolling(revenue, _TD_YEAR)
    return z.diff(_TD_QTR)


def rvd_drv2_012_receivables_to_rev_63d_diff(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """63-day diff of receivables/revenue ratio (acceleration of demand-quality decay)."""
    ratio = _safe_div(receivables, revenue)
    return ratio.diff(_TD_QTR)


def rvd_drv2_013_inventory_to_rev_63d_diff(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """63-day diff of inventory/revenue ratio (acceleration of inventory build-up signal)."""
    ratio = _safe_div(inventory, revenue)
    return ratio.diff(_TD_QTR)


def rvd_drv2_014_gp_pct_of_rev_63d_diff(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """63-day diff of gross margin (acceleration of margin compression)."""
    m = _safe_div(gp, revenue)
    return m.diff(_TD_QTR)


def rvd_drv2_015_rev_to_assets_63d_diff(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """63-day diff of revenue/assets ratio (acceleration of asset-efficiency loss)."""
    ratio = _safe_div(revenue, assets)
    return ratio.diff(_TD_QTR)


def rvd_drv2_016_rev_qoq_pct_ewm_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope of EWM-smoothed QoQ revenue growth over trailing 252-day window."""
    g   = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    ewg = _ewm_mean(g, _TD_YEAR)
    return _linslope(ewg, _TD_YEAR)


def rvd_drv2_017_rev_dd_4q_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope of 4-quarter revenue drawdown over trailing 252-day window."""
    peak = _rolling_max(revenue, _TD_YEAR)
    dd   = _safe_div(revenue - peak, peak.abs())
    return _linslope(dd, _TD_YEAR)


def rvd_drv2_018_rev_yoy_pct_pct_chg_63d(revenue: pd.Series) -> pd.Series:
    """Percent change in YoY revenue growth rate over 63-day lag."""
    g     = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    prior = g.shift(_TD_QTR).abs()
    return _safe_div(g - g.shift(_TD_QTR), prior)


def rvd_drv2_019_rev_dd_ath_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope of all-time revenue drawdown over trailing 252-day window."""
    peak = revenue.expanding(min_periods=1).max()
    dd   = _safe_div(revenue - peak, peak.abs())
    return _linslope(dd, _TD_YEAR)


def rvd_drv2_020_gp_yoy_pct_63d_diff(gp: pd.Series) -> pd.Series:
    """63-day diff of YoY gross profit % change (acceleration of GP deterioration)."""
    g = _safe_div(gp - gp.shift(_TD_YEAR), gp.shift(_TD_YEAR).abs())
    return g.diff(_TD_QTR)


def rvd_drv2_021_rev_cor_spread_qoq_63d_diff(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """63-day diff of (revenue growth - COR growth) spread (acceleration of cost squeeze)."""
    rev_g = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    cor_g = _safe_div(cor - cor.shift(_TD_QTR), cor.shift(_TD_QTR).abs())
    spread = rev_g - cor_g
    return spread.diff(_TD_QTR)


def rvd_drv2_022_rev_per_share_qoq_63d_diff(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """63-day diff of QoQ revenue-per-share % change (per-share deterioration acceleration)."""
    rps  = _safe_div(revenue, shareswa)
    g    = _safe_div(rps - rps.shift(_TD_QTR), rps.shift(_TD_QTR).abs())
    return g.diff(_TD_QTR)


def rvd_drv2_023_rev_qoq_avg_4q_252d_slope(revenue: pd.Series) -> pd.Series:
    """OLS slope of 4-quarter average QoQ growth rate (trend of average deterioration)."""
    g   = _safe_div(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR).abs())
    avg = _rolling_mean(g, _TD_YEAR)
    return _linslope(avg, _TD_YEAR)


def rvd_drv2_024_deferredrev_to_rev_63d_diff(revenue: pd.Series, deferredrev: pd.Series) -> pd.Series:
    """63-day diff of deferred-revenue/revenue ratio (acceleration of backlog erosion)."""
    ratio = _safe_div(deferredrev, revenue)
    return ratio.diff(_TD_QTR)


def rvd_drv2_025_rev_composite_det_63d_diff(revenue: pd.Series) -> pd.Series:
    """
    63-day diff of composite deterioration index (acceleration of composite signal).
    Composite = equal-weight avg of YoY growth z-score, QoQ growth z-score, 4q dd z-score.
    """
    g_yoy = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).abs())
    g_qoq = _safe_div(revenue - revenue.shift(_TD_QTR),  revenue.shift(_TD_QTR).abs())
    peak  = _rolling_max(revenue, _TD_YEAR)
    dd    = _safe_div(revenue - peak, peak.abs())
    z_yoy = _zscore_rolling(g_yoy, _TD_2YEAR)
    z_qoq = _zscore_rolling(g_qoq, _TD_2YEAR)
    z_dd  = _zscore_rolling(dd,    _TD_2YEAR)
    composite = (z_yoy + z_qoq + z_dd) / 3.0
    return composite.diff(_TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

REVENUE_DETERIORATION_REGISTRY_2ND_DERIVATIVES = {
    "rvd_drv2_001_rev_qoq_pct_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_001_rev_qoq_pct_63d_diff},
    "rvd_drv2_002_rev_yoy_pct_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_002_rev_yoy_pct_63d_diff},
    "rvd_drv2_003_rev_yoy_pct_252d_diff": {"inputs": ["revenue"], "func": rvd_drv2_003_rev_yoy_pct_252d_diff},
    "rvd_drv2_004_rev_dd_4q_peak_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_004_rev_dd_4q_peak_63d_diff},
    "rvd_drv2_005_rev_dd_ath_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_005_rev_dd_ath_63d_diff},
    "rvd_drv2_006_rev_yoy_log_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_006_rev_yoy_log_63d_diff},
    "rvd_drv2_007_rev_qoq_pct_252d_slope": {"inputs": ["revenue"], "func": rvd_drv2_007_rev_qoq_pct_252d_slope},
    "rvd_drv2_008_rev_yoy_pct_504d_slope": {"inputs": ["revenue"], "func": rvd_drv2_008_rev_yoy_pct_504d_slope},
    "rvd_drv2_009_rev_qoq_decline_count_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_009_rev_qoq_decline_count_63d_diff},
    "rvd_drv2_010_rev_vs_4q_avg_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_010_rev_vs_4q_avg_63d_diff},
    "rvd_drv2_011_rev_zscore_4q_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_011_rev_zscore_4q_63d_diff},
    "rvd_drv2_012_receivables_to_rev_63d_diff": {"inputs": ["revenue", "receivables"], "func": rvd_drv2_012_receivables_to_rev_63d_diff},
    "rvd_drv2_013_inventory_to_rev_63d_diff": {"inputs": ["revenue", "inventory"], "func": rvd_drv2_013_inventory_to_rev_63d_diff},
    "rvd_drv2_014_gp_pct_of_rev_63d_diff": {"inputs": ["revenue", "gp"], "func": rvd_drv2_014_gp_pct_of_rev_63d_diff},
    "rvd_drv2_015_rev_to_assets_63d_diff": {"inputs": ["revenue", "assets"], "func": rvd_drv2_015_rev_to_assets_63d_diff},
    "rvd_drv2_016_rev_qoq_pct_ewm_slope": {"inputs": ["revenue"], "func": rvd_drv2_016_rev_qoq_pct_ewm_slope},
    "rvd_drv2_017_rev_dd_4q_252d_slope": {"inputs": ["revenue"], "func": rvd_drv2_017_rev_dd_4q_252d_slope},
    "rvd_drv2_018_rev_yoy_pct_pct_chg_63d": {"inputs": ["revenue"], "func": rvd_drv2_018_rev_yoy_pct_pct_chg_63d},
    "rvd_drv2_019_rev_dd_ath_252d_slope": {"inputs": ["revenue"], "func": rvd_drv2_019_rev_dd_ath_252d_slope},
    "rvd_drv2_020_gp_yoy_pct_63d_diff": {"inputs": ["gp"], "func": rvd_drv2_020_gp_yoy_pct_63d_diff},
    "rvd_drv2_021_rev_cor_spread_qoq_63d_diff": {"inputs": ["revenue", "cor"], "func": rvd_drv2_021_rev_cor_spread_qoq_63d_diff},
    "rvd_drv2_022_rev_per_share_qoq_63d_diff": {"inputs": ["revenue", "shareswa"], "func": rvd_drv2_022_rev_per_share_qoq_63d_diff},
    "rvd_drv2_023_rev_qoq_avg_4q_252d_slope": {"inputs": ["revenue"], "func": rvd_drv2_023_rev_qoq_avg_4q_252d_slope},
    "rvd_drv2_024_deferredrev_to_rev_63d_diff": {"inputs": ["revenue", "deferredrev"], "func": rvd_drv2_024_deferredrev_to_rev_63d_diff},
    "rvd_drv2_025_rev_composite_det_63d_diff": {"inputs": ["revenue"], "func": rvd_drv2_025_rev_composite_det_63d_diff},
}
