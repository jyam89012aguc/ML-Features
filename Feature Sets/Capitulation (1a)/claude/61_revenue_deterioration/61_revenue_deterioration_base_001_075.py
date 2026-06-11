"""
61_revenue_deterioration — Base Features 001-075
Domain: revenue contraction, growth reversal, top-line deterioration
Asset class: US equities | Sharadar SF1 fundamentals ONLY (no price/volume)
Target context: capitulation — absolute multi-year low / maximum distress

All inputs are daily-frequency Series, forward-filled from the most recent
quarterly Sharadar SF1 report known as of each date (pipeline contract).
Functions look strictly backward — no future information.

Quarterly cadence on daily index:
    1 quarter  ~  63 trading days   (.diff(63)  = QoQ)
    1 year     ~ 252 trading days   (.diff(252) = YoY)
    2 years    ~ 504 trading days
    3 years    ~ 756 trading days
    5 years    ~ 1260 trading days
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


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
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        denom = ((xi - xi_m) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((xi - xi_m) * (x - x_m)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): QoQ and YoY revenue growth rates ---

def rvd_001_rev_qoq_pct(revenue: pd.Series) -> pd.Series:
    """Quarter-over-quarter revenue % change (63-day diff / prior level)."""
    prior = revenue.shift(_TD_QTR)
    return _safe_div(revenue - prior, prior.abs())


def rvd_002_rev_yoy_pct(revenue: pd.Series) -> pd.Series:
    """Year-over-year revenue % change (252-day diff / prior level)."""
    prior = revenue.shift(_TD_YEAR)
    return _safe_div(revenue - prior, prior.abs())


def rvd_003_rev_2y_pct(revenue: pd.Series) -> pd.Series:
    """2-year revenue % change (504-day diff / prior level)."""
    prior = revenue.shift(_TD_2YEAR)
    return _safe_div(revenue - prior, prior.abs())


def rvd_004_rev_3y_pct(revenue: pd.Series) -> pd.Series:
    """3-year revenue % change (756-day diff / prior level)."""
    prior = revenue.shift(_TD_3YEAR)
    return _safe_div(revenue - prior, prior.abs())


def rvd_005_rev_qoq_log(revenue: pd.Series) -> pd.Series:
    """QoQ log-revenue change (log-scale growth rate, quarter lag)."""
    return _log_safe(revenue) - _log_safe(revenue.shift(_TD_QTR))


def rvd_006_rev_yoy_log(revenue: pd.Series) -> pd.Series:
    """YoY log-revenue change (log-scale growth rate, year lag)."""
    return _log_safe(revenue) - _log_safe(revenue.shift(_TD_YEAR))


def rvd_007_rev_level_vs_4q_min(revenue: pd.Series) -> pd.Series:
    """Revenue level minus its trailing 4-quarter (252-day) minimum.
    Distance from the worst recent trough; zero when at a 1-year low."""
    return revenue - _rolling_min(revenue, _TD_YEAR)


def rvd_008_rev_yoy_abs(revenue: pd.Series) -> pd.Series:
    """YoY absolute revenue change (raw dollar decline)."""
    return revenue - revenue.shift(_TD_YEAR)


def rvd_009_rev_qoq_pct_rank_8q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of QoQ revenue % change within a trailing 8-quarter (504-day) window.
    Low rank signals the most severe recent top-line contraction vs the prior 2 years."""
    g = rvd_001_rev_qoq_pct(revenue)
    return g.rolling(_TD_2YEAR, min_periods=max(2, _TD_2YEAR // 4)).rank(pct=True)


def rvd_010_rev_yoy_pct_rank_8q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of YoY revenue % change within a trailing 8-quarter (504-day) window.
    Low rank signals the most severe recent year-over-year contraction vs the prior 2 years."""
    g = rvd_002_rev_yoy_pct(revenue)
    return g.rolling(_TD_2YEAR, min_periods=max(2, _TD_2YEAR // 4)).rank(pct=True)


def rvd_011_rev_qoq_sign(revenue: pd.Series) -> pd.Series:
    """Sign of QoQ change: +1 growth, -1 decline, 0 flat (direction indicator)."""
    return np.sign(revenue - revenue.shift(_TD_QTR))


def rvd_012_rev_yoy_sign(revenue: pd.Series) -> pd.Series:
    """Sign of YoY change: +1 growth, -1 decline (direction indicator)."""
    return np.sign(rvd_008_rev_yoy_abs(revenue))


# --- Group B (013-024): Drawdown from trailing revenue peak ---

def rvd_013_rev_dd_from_4q_peak(revenue: pd.Series) -> pd.Series:
    """Revenue vs trailing 4-quarter (252-day) peak: (rev - peak) / |peak|."""
    peak = _rolling_max(revenue, _TD_YEAR)
    return _safe_div(revenue - peak, peak.abs())


def rvd_014_rev_dd_from_8q_peak(revenue: pd.Series) -> pd.Series:
    """Revenue vs trailing 8-quarter (504-day) peak."""
    peak = _rolling_max(revenue, _TD_2YEAR)
    return _safe_div(revenue - peak, peak.abs())


def rvd_015_rev_dd_from_12q_peak(revenue: pd.Series) -> pd.Series:
    """Revenue vs trailing 12-quarter (756-day) peak."""
    peak = _rolling_max(revenue, _TD_3YEAR)
    return _safe_div(revenue - peak, peak.abs())


def rvd_016_rev_dd_from_20q_peak(revenue: pd.Series) -> pd.Series:
    """Revenue vs trailing 20-quarter (1260-day) peak (5-year max)."""
    peak = _rolling_max(revenue, _TD_5YEAR)
    return _safe_div(revenue - peak, peak.abs())


def rvd_017_rev_dd_from_all_time_peak(revenue: pd.Series) -> pd.Series:
    """Revenue vs all-time (expanding) peak: maximum top-line deterioration."""
    peak = revenue.expanding(min_periods=1).max()
    return _safe_div(revenue - peak, peak.abs())


def rvd_018_rev_log_dd_from_4q_peak(revenue: pd.Series) -> pd.Series:
    """Log-space revenue drawdown from 4-quarter (1-year) rolling peak."""
    peak = _rolling_max(revenue, _TD_YEAR)
    return _log_safe(revenue) - _log_safe(peak)


def rvd_019_rev_log_dd_from_all_time_peak(revenue: pd.Series) -> pd.Series:
    """Log-space revenue drawdown from all-time peak."""
    peak = revenue.expanding(min_periods=1).max()
    return _log_safe(revenue) - _log_safe(peak)


def rvd_020_rev_dd_intensity_1y(revenue: pd.Series) -> pd.Series:
    """Current 1-year rev dd as fraction of trailing 1-year worst dd."""
    dd  = rvd_013_rev_dd_from_4q_peak(revenue)
    wdd = _rolling_min(dd, _TD_YEAR)
    return _safe_div(dd, wdd.abs())


def rvd_021_rev_dd_intensity_ath(revenue: pd.Series) -> pd.Series:
    """All-time rev dd as fraction of expanding worst dd (how close to record low)."""
    dd  = rvd_017_rev_dd_from_all_time_peak(revenue)
    wdd = dd.expanding(min_periods=1).min()
    return _safe_div(dd, wdd.abs())


def rvd_022_rev_pct_rank_4q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue within trailing 4-quarter (252-day) window."""
    return revenue.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).rank(pct=True)


def rvd_023_rev_pct_rank_8q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue within trailing 8-quarter (504-day) window."""
    return revenue.rolling(_TD_2YEAR, min_periods=max(1, _TD_2YEAR // 4)).rank(pct=True)


def rvd_024_rev_pct_rank_20q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue within trailing 20-quarter (1260-day) window."""
    return revenue.rolling(_TD_5YEAR, min_periods=max(1, _TD_5YEAR // 4)).rank(pct=True)


# --- Group C (025-036): Revenue vs trailing averages ---

def rvd_025_rev_vs_4q_avg(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 4-quarter (1-year) trailing average."""
    avg = _rolling_mean(revenue, _TD_YEAR)
    return _safe_div(revenue - avg, avg.abs())


def rvd_026_rev_vs_8q_avg(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 8-quarter (2-year) trailing average."""
    avg = _rolling_mean(revenue, _TD_2YEAR)
    return _safe_div(revenue - avg, avg.abs())


def rvd_027_rev_vs_12q_avg(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 12-quarter (3-year) trailing average."""
    avg = _rolling_mean(revenue, _TD_3YEAR)
    return _safe_div(revenue - avg, avg.abs())


def rvd_028_rev_vs_2q_avg(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 2-quarter (half-year) trailing average."""
    avg = _rolling_mean(revenue, _TD_HALF)
    return _safe_div(revenue - avg, avg.abs())


def rvd_029_rev_zscore_4q(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue within trailing 4-quarter (1-year) window."""
    return _zscore_rolling(revenue, _TD_YEAR)


def rvd_030_rev_zscore_8q(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue within trailing 8-quarter (2-year) window."""
    return _zscore_rolling(revenue, _TD_2YEAR)


def rvd_031_rev_zscore_20q(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue within trailing 20-quarter (5-year) window."""
    return _zscore_rolling(revenue, _TD_5YEAR)


def rvd_032_rev_expanding_zscore(revenue: pd.Series) -> pd.Series:
    """Expanding z-score of revenue (how extreme vs entire history)."""
    m  = revenue.expanding(min_periods=2).mean()
    sd = revenue.expanding(min_periods=2).std()
    return _safe_div(revenue - m, sd)


def rvd_033_rev_vs_4q_median(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 4-quarter trailing median."""
    med = _rolling_median(revenue, _TD_YEAR)
    return _safe_div(revenue - med, med.abs())


def rvd_034_rev_vs_8q_median(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 8-quarter trailing median."""
    med = _rolling_median(revenue, _TD_2YEAR)
    return _safe_div(revenue - med, med.abs())


def rvd_035_rev_vs_ewm_4q(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 4-quarter EWM (exponentially weighted average)."""
    ewm = _ewm_mean(revenue, _TD_YEAR)
    return _safe_div(revenue - ewm, ewm.abs())


def rvd_036_rev_vs_ewm_8q(revenue: pd.Series) -> pd.Series:
    """Revenue deviation from 8-quarter EWM."""
    ewm = _ewm_mean(revenue, _TD_2YEAR)
    return _safe_div(revenue - ewm, ewm.abs())


# --- Group D (037-048): Consecutive declining quarters and run-lengths ---

def rvd_037_rev_qoq_decline_flag(revenue: pd.Series) -> pd.Series:
    """Binary flag: 1 if QoQ revenue change is negative, else 0."""
    return ((revenue - revenue.shift(_TD_QTR)) < 0).astype(float)


def rvd_038_rev_yoy_decline_flag(revenue: pd.Series) -> pd.Series:
    """Binary flag: 1 if YoY revenue change is negative, else 0."""
    return (rvd_008_rev_yoy_abs(revenue) < 0).astype(float)


def rvd_039_rev_qoq_decline_count_4q(revenue: pd.Series) -> pd.Series:
    """Count of QoQ declining quarters in trailing 4-quarter (1-year) window."""
    flag = rvd_037_rev_qoq_decline_flag(revenue)
    return _rolling_sum(flag, _TD_YEAR)


def rvd_040_rev_qoq_decline_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of QoQ declining quarters in trailing 8-quarter (2-year) window."""
    flag = rvd_037_rev_qoq_decline_flag(revenue)
    return _rolling_sum(flag, _TD_2YEAR)


def rvd_041_rev_yoy_decline_count_4q(revenue: pd.Series) -> pd.Series:
    """Count of YoY declining quarters in trailing 4-quarter (1-year) window."""
    flag = rvd_038_rev_yoy_decline_flag(revenue)
    return _rolling_sum(flag, _TD_YEAR)


def rvd_042_rev_yoy_decline_fraction_8q(revenue: pd.Series) -> pd.Series:
    """Fraction of trailing 8-quarter (2-year) window with YoY revenue decline."""
    flag = rvd_038_rev_yoy_decline_flag(revenue)
    return _rolling_mean(flag, _TD_2YEAR)


def rvd_043_rev_consecutive_qoq_decline(revenue: pd.Series) -> pd.Series:
    """
    Trailing consecutive-quarter QoQ decline count: how many of the last N
    sampled quarters (sampled every 63 days) have been negative.
    Counts backward until a non-negative quarter breaks the streak.
    """
    qoq = revenue - revenue.shift(_TD_QTR)
    def _streak(x):
        count = 0
        for v in reversed(x):
            if np.isnan(v):
                break
            if v < 0:
                count += 1
            else:
                break
        return float(count)
    return qoq.rolling(_TD_5YEAR, min_periods=1).apply(_streak, raw=True)


def rvd_044_rev_below_prior_peak_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if revenue is strictly below its 4-quarter trailing peak."""
    peak = _rolling_max(revenue, _TD_YEAR)
    return (revenue < peak).astype(float)


def rvd_045_rev_below_4q_avg_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if revenue is strictly below its 4-quarter trailing average."""
    avg = _rolling_mean(revenue, _TD_YEAR)
    return (revenue < avg).astype(float)


def rvd_046_rev_below_ath_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if revenue is strictly below its all-time expanding max."""
    peak = revenue.expanding(min_periods=1).max()
    return (revenue < peak).astype(float)


def rvd_047_rev_new_4q_low_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if revenue equals the 4-quarter (1-year) trailing minimum."""
    mn = _rolling_min(revenue, _TD_YEAR)
    return (revenue <= mn).astype(float)


def rvd_048_rev_new_20q_low_flag(revenue: pd.Series) -> pd.Series:
    """Flag: 1 if revenue equals the 20-quarter (5-year) trailing minimum."""
    mn = _rolling_min(revenue, _TD_5YEAR)
    return (revenue <= mn).astype(float)


# --- Group E (049-060): Revenue magnitude and speed measures ---

def rvd_049_rev_qoq_pct_abs(revenue: pd.Series) -> pd.Series:
    """Absolute magnitude of QoQ revenue change (volatility of top-line)."""
    return rvd_001_rev_qoq_pct(revenue).abs()


def rvd_050_rev_yoy_pct_abs(revenue: pd.Series) -> pd.Series:
    """Absolute magnitude of YoY revenue change."""
    return rvd_002_rev_yoy_pct(revenue).abs()


def rvd_051_rev_qoq_rolling_std_4q(revenue: pd.Series) -> pd.Series:
    """Rolling std of QoQ revenue growth rate over trailing 4-quarter window."""
    g = rvd_001_rev_qoq_pct(revenue)
    return _rolling_std(g, _TD_YEAR)


def rvd_052_rev_yoy_rolling_std_4q(revenue: pd.Series) -> pd.Series:
    """Rolling std of YoY revenue growth rate over trailing 4-quarter window."""
    g = rvd_002_rev_yoy_pct(revenue)
    return _rolling_std(g, _TD_YEAR)


def rvd_053_rev_qoq_pct_zscore_8q(revenue: pd.Series) -> pd.Series:
    """Z-score of QoQ revenue % change within trailing 8-quarter (504-day) window.
    Measures how extreme the current quarter's top-line contraction is vs the prior 2 years."""
    g = rvd_001_rev_qoq_pct(revenue)
    return _zscore_rolling(g, _TD_2YEAR)


def rvd_054_rev_yoy_slope_4q(revenue: pd.Series) -> pd.Series:
    """OLS slope of YoY revenue growth over trailing 4-quarter window."""
    g = rvd_002_rev_yoy_pct(revenue)
    return _linslope(g, _TD_YEAR)


def rvd_055_rev_level_pct_rank_12q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue level within a trailing 12-quarter (756-day) window.
    Captures where current revenue stands in its 3-year distribution."""
    return revenue.rolling(_TD_3YEAR, min_periods=max(2, _TD_3YEAR // 4)).rank(pct=True)


def rvd_056_rev_level_slope_8q(revenue: pd.Series) -> pd.Series:
    """OLS slope of revenue level over trailing 8-quarter window."""
    return _linslope(revenue, _TD_2YEAR)


def rvd_057_rev_max_single_qoq_drop_4q(revenue: pd.Series) -> pd.Series:
    """Maximum (worst) QoQ revenue drop in trailing 4-quarter window."""
    g = rvd_001_rev_qoq_pct(revenue)
    return _rolling_min(g, _TD_YEAR)


def rvd_058_rev_max_single_qoq_drop_8q(revenue: pd.Series) -> pd.Series:
    """Maximum (worst) QoQ revenue drop in trailing 8-quarter window."""
    g = rvd_001_rev_qoq_pct(revenue)
    return _rolling_min(g, _TD_2YEAR)


def rvd_059_rev_qoq_avg_growth_4q(revenue: pd.Series) -> pd.Series:
    """Mean QoQ revenue growth rate over trailing 4-quarter window."""
    g = rvd_001_rev_qoq_pct(revenue)
    return _rolling_mean(g, _TD_YEAR)


def rvd_060_rev_yoy_avg_growth_4q(revenue: pd.Series) -> pd.Series:
    """Mean YoY revenue growth rate over trailing 4-quarter window."""
    g = rvd_002_rev_yoy_pct(revenue)
    return _rolling_mean(g, _TD_YEAR)


# --- Group F (061-075): Revenue-quality signals (COGS, receivables, inventory) ---

def rvd_061_rev_vs_cor_ratio(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Revenue-to-COGS ratio: declining ratio signals cost pressure eroding revenue."""
    return _safe_div(revenue, cor)


def rvd_062_rev_vs_cor_ratio_qoq_chg(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """QoQ change in revenue-to-COGS ratio (cost divergence from revenue)."""
    r = _safe_div(revenue, cor)
    return r - r.shift(_TD_QTR)


def rvd_063_gp_pct_of_rev(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Gross profit as % of revenue (gross margin); captures revenue-quality decline."""
    return _safe_div(gp, revenue)


def rvd_064_gp_pct_of_rev_zscore_4q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Z-score of gross margin (gross profit / revenue) within trailing 4-quarter window.
    Low z-score signals gross margin is at a recent trough relative to its own history."""
    m = _safe_div(gp, revenue)
    return _zscore_rolling(m, _TD_YEAR)


def rvd_065_gp_pct_of_rev_yoy_chg(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """YoY change in gross margin."""
    m = _safe_div(gp, revenue)
    return m - m.shift(_TD_YEAR)


def rvd_066_receivables_to_rev(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """Receivables-to-revenue ratio: rising ratio = demand weakness / collection risk."""
    return _safe_div(receivables, revenue)


def rvd_067_receivables_to_rev_pct_rank_4q(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """Percentile rank of receivables-to-revenue ratio within trailing 4-quarter window.
    High rank signals receivables unusually elevated relative to revenue (collection risk)."""
    r = _safe_div(receivables, revenue)
    return r.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def rvd_068_receivables_to_rev_yoy_chg(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """YoY change in receivables-to-revenue."""
    r = _safe_div(receivables, revenue)
    return r - r.shift(_TD_YEAR)


def rvd_069_inventory_to_rev(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Inventory-to-revenue ratio: rising ratio signals demand weakness."""
    return _safe_div(inventory, revenue)


def rvd_070_inventory_to_rev_pct_rank_4q(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Percentile rank of inventory-to-revenue ratio within trailing 4-quarter window.
    High rank signals inventory unusually elevated relative to revenue (demand weakness)."""
    r = _safe_div(inventory, revenue)
    return r.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def rvd_071_inventory_to_rev_yoy_chg(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """YoY change in inventory-to-revenue."""
    r = _safe_div(inventory, revenue)
    return r - r.shift(_TD_YEAR)


def rvd_072_deferredrev_to_rev(revenue: pd.Series, deferredrev: pd.Series) -> pd.Series:
    """Deferred revenue to total revenue: declining ratio signals backlog erosion."""
    return _safe_div(deferredrev, revenue)


def rvd_073_deferredrev_to_rev_zscore_8q(revenue: pd.Series, deferredrev: pd.Series) -> pd.Series:
    """Z-score of deferred-revenue-to-revenue ratio within trailing 8-quarter window.
    Measures whether backlog coverage is at an unusually low level vs the prior 2 years."""
    r = _safe_div(deferredrev, revenue)
    return _zscore_rolling(r, _TD_2YEAR)


def rvd_074_rev_per_share_qoq_pct(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """QoQ % change in revenue per diluted share (controls for dilution)."""
    rps = _safe_div(revenue, shareswa)
    prior = rps.shift(_TD_QTR)
    return _safe_div(rps - prior, prior.abs())


def rvd_075_rev_per_share_yoy_pct(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """YoY % change in revenue per diluted share."""
    rps = _safe_div(revenue, shareswa)
    prior = rps.shift(_TD_YEAR)
    return _safe_div(rps - prior, prior.abs())


# ── Registry ──────────────────────────────────────────────────────────────────

REVENUE_DETERIORATION_REGISTRY_001_075 = {
    "rvd_001_rev_qoq_pct": {"inputs": ["revenue"], "func": rvd_001_rev_qoq_pct},
    "rvd_002_rev_yoy_pct": {"inputs": ["revenue"], "func": rvd_002_rev_yoy_pct},
    "rvd_003_rev_2y_pct": {"inputs": ["revenue"], "func": rvd_003_rev_2y_pct},
    "rvd_004_rev_3y_pct": {"inputs": ["revenue"], "func": rvd_004_rev_3y_pct},
    "rvd_005_rev_qoq_log": {"inputs": ["revenue"], "func": rvd_005_rev_qoq_log},
    "rvd_006_rev_yoy_log": {"inputs": ["revenue"], "func": rvd_006_rev_yoy_log},
    "rvd_007_rev_level_vs_4q_min": {"inputs": ["revenue"], "func": rvd_007_rev_level_vs_4q_min},
    "rvd_008_rev_yoy_abs": {"inputs": ["revenue"], "func": rvd_008_rev_yoy_abs},
    "rvd_009_rev_qoq_pct_rank_8q": {"inputs": ["revenue"], "func": rvd_009_rev_qoq_pct_rank_8q},
    "rvd_010_rev_yoy_pct_rank_8q": {"inputs": ["revenue"], "func": rvd_010_rev_yoy_pct_rank_8q},
    "rvd_011_rev_qoq_sign": {"inputs": ["revenue"], "func": rvd_011_rev_qoq_sign},
    "rvd_012_rev_yoy_sign": {"inputs": ["revenue"], "func": rvd_012_rev_yoy_sign},
    "rvd_013_rev_dd_from_4q_peak": {"inputs": ["revenue"], "func": rvd_013_rev_dd_from_4q_peak},
    "rvd_014_rev_dd_from_8q_peak": {"inputs": ["revenue"], "func": rvd_014_rev_dd_from_8q_peak},
    "rvd_015_rev_dd_from_12q_peak": {"inputs": ["revenue"], "func": rvd_015_rev_dd_from_12q_peak},
    "rvd_016_rev_dd_from_20q_peak": {"inputs": ["revenue"], "func": rvd_016_rev_dd_from_20q_peak},
    "rvd_017_rev_dd_from_all_time_peak": {"inputs": ["revenue"], "func": rvd_017_rev_dd_from_all_time_peak},
    "rvd_018_rev_log_dd_from_4q_peak": {"inputs": ["revenue"], "func": rvd_018_rev_log_dd_from_4q_peak},
    "rvd_019_rev_log_dd_from_all_time_peak": {"inputs": ["revenue"], "func": rvd_019_rev_log_dd_from_all_time_peak},
    "rvd_020_rev_dd_intensity_1y": {"inputs": ["revenue"], "func": rvd_020_rev_dd_intensity_1y},
    "rvd_021_rev_dd_intensity_ath": {"inputs": ["revenue"], "func": rvd_021_rev_dd_intensity_ath},
    "rvd_022_rev_pct_rank_4q": {"inputs": ["revenue"], "func": rvd_022_rev_pct_rank_4q},
    "rvd_023_rev_pct_rank_8q": {"inputs": ["revenue"], "func": rvd_023_rev_pct_rank_8q},
    "rvd_024_rev_pct_rank_20q": {"inputs": ["revenue"], "func": rvd_024_rev_pct_rank_20q},
    "rvd_025_rev_vs_4q_avg": {"inputs": ["revenue"], "func": rvd_025_rev_vs_4q_avg},
    "rvd_026_rev_vs_8q_avg": {"inputs": ["revenue"], "func": rvd_026_rev_vs_8q_avg},
    "rvd_027_rev_vs_12q_avg": {"inputs": ["revenue"], "func": rvd_027_rev_vs_12q_avg},
    "rvd_028_rev_vs_2q_avg": {"inputs": ["revenue"], "func": rvd_028_rev_vs_2q_avg},
    "rvd_029_rev_zscore_4q": {"inputs": ["revenue"], "func": rvd_029_rev_zscore_4q},
    "rvd_030_rev_zscore_8q": {"inputs": ["revenue"], "func": rvd_030_rev_zscore_8q},
    "rvd_031_rev_zscore_20q": {"inputs": ["revenue"], "func": rvd_031_rev_zscore_20q},
    "rvd_032_rev_expanding_zscore": {"inputs": ["revenue"], "func": rvd_032_rev_expanding_zscore},
    "rvd_033_rev_vs_4q_median": {"inputs": ["revenue"], "func": rvd_033_rev_vs_4q_median},
    "rvd_034_rev_vs_8q_median": {"inputs": ["revenue"], "func": rvd_034_rev_vs_8q_median},
    "rvd_035_rev_vs_ewm_4q": {"inputs": ["revenue"], "func": rvd_035_rev_vs_ewm_4q},
    "rvd_036_rev_vs_ewm_8q": {"inputs": ["revenue"], "func": rvd_036_rev_vs_ewm_8q},
    "rvd_037_rev_qoq_decline_flag": {"inputs": ["revenue"], "func": rvd_037_rev_qoq_decline_flag},
    "rvd_038_rev_yoy_decline_flag": {"inputs": ["revenue"], "func": rvd_038_rev_yoy_decline_flag},
    "rvd_039_rev_qoq_decline_count_4q": {"inputs": ["revenue"], "func": rvd_039_rev_qoq_decline_count_4q},
    "rvd_040_rev_qoq_decline_count_8q": {"inputs": ["revenue"], "func": rvd_040_rev_qoq_decline_count_8q},
    "rvd_041_rev_yoy_decline_count_4q": {"inputs": ["revenue"], "func": rvd_041_rev_yoy_decline_count_4q},
    "rvd_042_rev_yoy_decline_fraction_8q": {"inputs": ["revenue"], "func": rvd_042_rev_yoy_decline_fraction_8q},
    "rvd_043_rev_consecutive_qoq_decline": {"inputs": ["revenue"], "func": rvd_043_rev_consecutive_qoq_decline},
    "rvd_044_rev_below_prior_peak_flag": {"inputs": ["revenue"], "func": rvd_044_rev_below_prior_peak_flag},
    "rvd_045_rev_below_4q_avg_flag": {"inputs": ["revenue"], "func": rvd_045_rev_below_4q_avg_flag},
    "rvd_046_rev_below_ath_flag": {"inputs": ["revenue"], "func": rvd_046_rev_below_ath_flag},
    "rvd_047_rev_new_4q_low_flag": {"inputs": ["revenue"], "func": rvd_047_rev_new_4q_low_flag},
    "rvd_048_rev_new_20q_low_flag": {"inputs": ["revenue"], "func": rvd_048_rev_new_20q_low_flag},
    "rvd_049_rev_qoq_pct_abs": {"inputs": ["revenue"], "func": rvd_049_rev_qoq_pct_abs},
    "rvd_050_rev_yoy_pct_abs": {"inputs": ["revenue"], "func": rvd_050_rev_yoy_pct_abs},
    "rvd_051_rev_qoq_rolling_std_4q": {"inputs": ["revenue"], "func": rvd_051_rev_qoq_rolling_std_4q},
    "rvd_052_rev_yoy_rolling_std_4q": {"inputs": ["revenue"], "func": rvd_052_rev_yoy_rolling_std_4q},
    "rvd_053_rev_qoq_pct_zscore_8q": {"inputs": ["revenue"], "func": rvd_053_rev_qoq_pct_zscore_8q},
    "rvd_054_rev_yoy_slope_4q": {"inputs": ["revenue"], "func": rvd_054_rev_yoy_slope_4q},
    "rvd_055_rev_level_pct_rank_12q": {"inputs": ["revenue"], "func": rvd_055_rev_level_pct_rank_12q},
    "rvd_056_rev_level_slope_8q": {"inputs": ["revenue"], "func": rvd_056_rev_level_slope_8q},
    "rvd_057_rev_max_single_qoq_drop_4q": {"inputs": ["revenue"], "func": rvd_057_rev_max_single_qoq_drop_4q},
    "rvd_058_rev_max_single_qoq_drop_8q": {"inputs": ["revenue"], "func": rvd_058_rev_max_single_qoq_drop_8q},
    "rvd_059_rev_qoq_avg_growth_4q": {"inputs": ["revenue"], "func": rvd_059_rev_qoq_avg_growth_4q},
    "rvd_060_rev_yoy_avg_growth_4q": {"inputs": ["revenue"], "func": rvd_060_rev_yoy_avg_growth_4q},
    "rvd_061_rev_vs_cor_ratio": {"inputs": ["revenue", "cor"], "func": rvd_061_rev_vs_cor_ratio},
    "rvd_062_rev_vs_cor_ratio_qoq_chg": {"inputs": ["revenue", "cor"], "func": rvd_062_rev_vs_cor_ratio_qoq_chg},
    "rvd_063_gp_pct_of_rev": {"inputs": ["revenue", "gp"], "func": rvd_063_gp_pct_of_rev},
    "rvd_064_gp_pct_of_rev_zscore_4q": {"inputs": ["revenue", "gp"], "func": rvd_064_gp_pct_of_rev_zscore_4q},
    "rvd_065_gp_pct_of_rev_yoy_chg": {"inputs": ["revenue", "gp"], "func": rvd_065_gp_pct_of_rev_yoy_chg},
    "rvd_066_receivables_to_rev": {"inputs": ["revenue", "receivables"], "func": rvd_066_receivables_to_rev},
    "rvd_067_receivables_to_rev_pct_rank_4q": {"inputs": ["revenue", "receivables"], "func": rvd_067_receivables_to_rev_pct_rank_4q},
    "rvd_068_receivables_to_rev_yoy_chg": {"inputs": ["revenue", "receivables"], "func": rvd_068_receivables_to_rev_yoy_chg},
    "rvd_069_inventory_to_rev": {"inputs": ["revenue", "inventory"], "func": rvd_069_inventory_to_rev},
    "rvd_070_inventory_to_rev_pct_rank_4q": {"inputs": ["revenue", "inventory"], "func": rvd_070_inventory_to_rev_pct_rank_4q},
    "rvd_071_inventory_to_rev_yoy_chg": {"inputs": ["revenue", "inventory"], "func": rvd_071_inventory_to_rev_yoy_chg},
    "rvd_072_deferredrev_to_rev": {"inputs": ["revenue", "deferredrev"], "func": rvd_072_deferredrev_to_rev},
    "rvd_073_deferredrev_to_rev_zscore_8q": {"inputs": ["revenue", "deferredrev"], "func": rvd_073_deferredrev_to_rev_zscore_8q},
    "rvd_074_rev_per_share_qoq_pct": {"inputs": ["revenue", "shareswa"], "func": rvd_074_rev_per_share_qoq_pct},
    "rvd_075_rev_per_share_yoy_pct": {"inputs": ["revenue", "shareswa"], "func": rvd_075_rev_per_share_yoy_pct},
}
