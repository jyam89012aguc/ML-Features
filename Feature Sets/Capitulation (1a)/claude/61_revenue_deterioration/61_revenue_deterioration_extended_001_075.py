"""
61_revenue_deterioration — Extended Features 001-075
Domain: revenue contraction, growth reversal, top-line deterioration —
        additional variants: new horizons, acceleration, TTM aggregates,
        recovery distance, growth-streak depth, dispersion, quality ratios
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
_TD_4YEAR = 1008
_TD_5YEAR = 1260
_TD_QTR   = 63
_TD_HALF  = 126
_TD_3Q    = 189
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _range_position(s: pd.Series, w: int) -> pd.Series:
    """Position of s within its trailing w-window range: 0=at low, 1=at high."""
    mn = _rolling_min(s, w)
    mx = _rolling_max(s, w)
    return _safe_div(s - mn, mx - mn)


def _qoq_pct(revenue: pd.Series, lag: int) -> pd.Series:
    """Generic lag-period percent change with abs(prior) denominator."""
    prior = revenue.shift(lag)
    return _safe_div(revenue - prior, prior.abs())


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Additional change horizons (half-year, 3Q, 4-year) ---

def rvd_ext_001_rev_2q_pct(revenue: pd.Series) -> pd.Series:
    """2-quarter (126-day) revenue % change."""
    return _qoq_pct(revenue, _TD_HALF)


def rvd_ext_002_rev_3q_pct(revenue: pd.Series) -> pd.Series:
    """3-quarter (189-day) revenue % change."""
    return _qoq_pct(revenue, _TD_3Q)


def rvd_ext_003_rev_4y_pct(revenue: pd.Series) -> pd.Series:
    """4-year (1008-day) revenue % change."""
    return _qoq_pct(revenue, _TD_4YEAR)


def rvd_ext_004_rev_5y_pct(revenue: pd.Series) -> pd.Series:
    """5-year (1260-day) revenue % change."""
    return _qoq_pct(revenue, _TD_5YEAR)


def rvd_ext_005_rev_2q_abs(revenue: pd.Series) -> pd.Series:
    """2-quarter absolute revenue change (raw dollar move)."""
    return revenue - revenue.shift(_TD_HALF)


def rvd_ext_006_rev_2y_abs(revenue: pd.Series) -> pd.Series:
    """2-year absolute revenue change (raw dollar move)."""
    return revenue - revenue.shift(_TD_2YEAR)


def rvd_ext_007_rev_3q_log(revenue: pd.Series) -> pd.Series:
    """3-quarter log-revenue change (log-scale growth rate)."""
    return _log_safe(revenue) - _log_safe(revenue.shift(_TD_3Q))


def rvd_ext_008_rev_2y_log(revenue: pd.Series) -> pd.Series:
    """2-year log-revenue change."""
    return _log_safe(revenue) - _log_safe(revenue.shift(_TD_2YEAR))


def rvd_ext_009_rev_qoq_pct_half_lag(revenue: pd.Series) -> pd.Series:
    """QoQ revenue % change measured one quarter ago (lagged growth memory)."""
    return _qoq_pct(revenue, _TD_QTR).shift(_TD_QTR)


def rvd_ext_010_rev_2q_pct_rank_12q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of 2-quarter revenue % change within trailing 12-quarter window."""
    return _rolling_rank_pct(_qoq_pct(revenue, _TD_HALF), _TD_3YEAR)


def rvd_ext_011_rev_yoy_pct_rank_12q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of YoY revenue % change within trailing 12-quarter window."""
    return _rolling_rank_pct(_qoq_pct(revenue, _TD_YEAR), _TD_3YEAR)


def rvd_ext_012_rev_2q_sign(revenue: pd.Series) -> pd.Series:
    """Sign of 2-quarter revenue change: +1 growth, -1 decline, 0 flat."""
    return np.sign(revenue - revenue.shift(_TD_HALF))


# --- Group B (013-024): Revenue acceleration (change of growth rate) ---

def rvd_ext_013_rev_qoq_growth_accel(revenue: pd.Series) -> pd.Series:
    """Acceleration of QoQ revenue growth: current QoQ % minus prior-quarter QoQ %."""
    g = _qoq_pct(revenue, _TD_QTR)
    return g - g.shift(_TD_QTR)


def rvd_ext_014_rev_yoy_growth_accel(revenue: pd.Series) -> pd.Series:
    """Acceleration of YoY revenue growth: current YoY % minus prior-year YoY %."""
    g = _qoq_pct(revenue, _TD_YEAR)
    return g - g.shift(_TD_YEAR)


def rvd_ext_015_rev_yoy_growth_accel_qoq(revenue: pd.Series) -> pd.Series:
    """Quarter-on-quarter acceleration of YoY revenue growth rate."""
    g = _qoq_pct(revenue, _TD_YEAR)
    return g - g.shift(_TD_QTR)


def rvd_ext_016_rev_level_second_diff(revenue: pd.Series) -> pd.Series:
    """Second difference of revenue level at quarterly cadence (curvature)."""
    d1 = revenue - revenue.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def rvd_ext_017_rev_growth_decel_flag(revenue: pd.Series) -> pd.Series:
    """Flag: QoQ revenue growth slowed vs the prior quarter (deceleration)."""
    g = _qoq_pct(revenue, _TD_QTR)
    return (g < g.shift(_TD_QTR)).astype(float)


def rvd_ext_018_rev_decline_worsening_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue declining QoQ and decline deeper than the prior quarter."""
    qoq = revenue - revenue.shift(_TD_QTR)
    return ((qoq < 0) & (qoq < qoq.shift(_TD_QTR))).astype(float)


def rvd_ext_019_rev_qoq_chg_mean_4q(revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of absolute QoQ revenue change (smoothed drift)."""
    return _rolling_mean(revenue - revenue.shift(_TD_QTR), _TD_YEAR)


def rvd_ext_020_rev_qoq_chg_mean_8q(revenue: pd.Series) -> pd.Series:
    """Trailing 8-quarter mean of absolute QoQ revenue change."""
    return _rolling_mean(revenue - revenue.shift(_TD_QTR), _TD_2YEAR)


def rvd_ext_021_rev_yoy_growth_slope_8q(revenue: pd.Series) -> pd.Series:
    """8-quarter mean of QoQ change in YoY revenue growth (sustained growth trend)."""
    g = _qoq_pct(revenue, _TD_YEAR)
    return _rolling_mean(g - g.shift(_TD_QTR), _TD_2YEAR)


def rvd_ext_022_rev_worst_qoq_drop_12q(revenue: pd.Series) -> pd.Series:
    """Worst (most negative) QoQ revenue % change in trailing 12-quarter window."""
    return _rolling_min(_qoq_pct(revenue, _TD_QTR), _TD_3YEAR)


def rvd_ext_023_rev_qoq_growth_minus_yoy_growth(revenue: pd.Series) -> pd.Series:
    """QoQ revenue growth minus YoY revenue growth (short-vs-long momentum gap)."""
    return _qoq_pct(revenue, _TD_QTR) - _qoq_pct(revenue, _TD_YEAR)


def rvd_ext_024_rev_yoy_growth_below_zero_flag(revenue: pd.Series) -> pd.Series:
    """Flag: YoY revenue growth rate is negative (top-line contraction)."""
    return (_qoq_pct(revenue, _TD_YEAR) < 0).astype(float)


# --- Group C (025-036): Range position and new-low / new-high flags ---

def rvd_ext_025_rev_range_pos_4q(revenue: pd.Series) -> pd.Series:
    """Revenue position within its trailing 4-quarter range (0=low, 1=high)."""
    return _range_position(revenue, _TD_YEAR)


def rvd_ext_026_rev_range_pos_8q(revenue: pd.Series) -> pd.Series:
    """Revenue position within its trailing 8-quarter range."""
    return _range_position(revenue, _TD_2YEAR)


def rvd_ext_027_rev_range_pos_12q(revenue: pd.Series) -> pd.Series:
    """Revenue position within its trailing 12-quarter range."""
    return _range_position(revenue, _TD_3YEAR)


def rvd_ext_028_rev_range_pos_20q(revenue: pd.Series) -> pd.Series:
    """Revenue position within its trailing 20-quarter (5-year) range."""
    return _range_position(revenue, _TD_5YEAR)


def rvd_ext_029_rev_new_8q_low_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue at or below its trailing 8-quarter minimum."""
    return (revenue <= _rolling_min(revenue, _TD_2YEAR)).astype(float)


def rvd_ext_030_rev_new_12q_low_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue at or below its trailing 12-quarter minimum."""
    return (revenue <= _rolling_min(revenue, _TD_3YEAR)).astype(float)


def rvd_ext_031_rev_new_ath_low_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue at or below its all-history expanding minimum."""
    return (revenue <= revenue.expanding(min_periods=1).min()).astype(float)


def rvd_ext_032_rev_below_8q_avg_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue strictly below its trailing 8-quarter average."""
    return (revenue < _rolling_mean(revenue, _TD_2YEAR)).astype(float)


def rvd_ext_033_rev_below_12q_avg_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue strictly below its trailing 12-quarter average."""
    return (revenue < _rolling_mean(revenue, _TD_3YEAR)).astype(float)


def rvd_ext_034_rev_below_8q_median_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue strictly below its trailing 8-quarter median."""
    return (revenue < _rolling_median(revenue, _TD_2YEAR)).astype(float)


def rvd_ext_035_rev_at_2q_low_flag(revenue: pd.Series) -> pd.Series:
    """Flag: revenue at or below its trailing 2-quarter (126-day) minimum."""
    return (revenue <= _rolling_min(revenue, _TD_HALF)).astype(float)


def rvd_ext_036_rev_count_new_4q_lows_8q(revenue: pd.Series) -> pd.Series:
    """Count of days in the trailing 8 quarters that printed a 4-quarter revenue low."""
    flag = (revenue <= _rolling_min(revenue, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_2YEAR)


# --- Group D (037-048): Recovery distance and drawdown-depth variants ---

def rvd_ext_037_rev_recovery_from_8q_low(revenue: pd.Series) -> pd.Series:
    """Revenue minus its trailing 8-quarter minimum (rebound off the trough)."""
    return revenue - _rolling_min(revenue, _TD_2YEAR)


def rvd_ext_038_rev_recovery_from_12q_low(revenue: pd.Series) -> pd.Series:
    """Revenue minus its trailing 12-quarter minimum."""
    return revenue - _rolling_min(revenue, _TD_3YEAR)


def rvd_ext_039_rev_pct_recovery_from_8q_low(revenue: pd.Series) -> pd.Series:
    """Revenue rebound off 8-quarter trough as fraction of abs(trough)."""
    mn = _rolling_min(revenue, _TD_2YEAR)
    return _safe_div(revenue - mn, mn.abs())


def rvd_ext_040_rev_pct_recovery_from_ath_low(revenue: pd.Series) -> pd.Series:
    """Revenue rebound off all-time trough as fraction of abs(trough)."""
    mn = revenue.expanding(min_periods=1).min()
    return _safe_div(revenue - mn, mn.abs())


def rvd_ext_041_rev_dd_from_2q_peak(revenue: pd.Series) -> pd.Series:
    """Revenue drawdown from trailing 2-quarter (126-day) peak."""
    peak = _rolling_max(revenue, _TD_HALF)
    return _safe_div(revenue - peak, peak.abs())


def rvd_ext_042_rev_dd_from_16q_peak(revenue: pd.Series) -> pd.Series:
    """Revenue drawdown from trailing 16-quarter (4-year) peak."""
    peak = _rolling_max(revenue, _TD_4YEAR)
    return _safe_div(revenue - peak, peak.abs())


def rvd_ext_043_rev_log_dd_from_8q_peak(revenue: pd.Series) -> pd.Series:
    """Log-space revenue drawdown from trailing 8-quarter peak."""
    return _log_safe(revenue) - _log_safe(_rolling_max(revenue, _TD_2YEAR))


def rvd_ext_044_rev_log_dd_from_12q_peak(revenue: pd.Series) -> pd.Series:
    """Log-space revenue drawdown from trailing 12-quarter peak."""
    return _log_safe(revenue) - _log_safe(_rolling_max(revenue, _TD_3YEAR))


def rvd_ext_045_rev_dd_depth_below_8q_peak_abs(revenue: pd.Series) -> pd.Series:
    """Absolute dollar gap between revenue and its trailing 8-quarter peak (>=0)."""
    return (_rolling_max(revenue, _TD_2YEAR) - revenue).clip(lower=0.0)


def rvd_ext_046_rev_dd_intensity_8q(revenue: pd.Series) -> pd.Series:
    """Current 8q drawdown as fraction of worst 8q drawdown over trailing 5 years."""
    peak = _rolling_max(revenue, _TD_2YEAR)
    dd = _safe_div(revenue - peak, peak.abs())
    return _safe_div(dd, _rolling_min(dd, _TD_5YEAR).abs())


def rvd_ext_047_rev_time_below_8q_peak_frac(revenue: pd.Series) -> pd.Series:
    """Fraction of trailing 8 quarters revenue spent strictly below its 8q peak."""
    flag = (revenue < _rolling_max(revenue, _TD_2YEAR)).astype(float)
    return _rolling_mean(flag, _TD_2YEAR)


def rvd_ext_048_rev_dd_4q_minus_dd_12q(revenue: pd.Series) -> pd.Series:
    """Difference between 4-quarter drawdown and 12-quarter drawdown (recent vs deep)."""
    dd4 = _safe_div(revenue - _rolling_max(revenue, _TD_YEAR), _rolling_max(revenue, _TD_YEAR).abs())
    dd12 = _safe_div(revenue - _rolling_max(revenue, _TD_3YEAR), _rolling_max(revenue, _TD_3YEAR).abs())
    return dd4 - dd12


# --- Group E (049-060): TTM aggregates and growth-streak depth ---

def rvd_ext_049_rev_ttm_sum(revenue: pd.Series) -> pd.Series:
    """Trailing-twelve-month revenue (4-quarter rolling sum)."""
    return _rolling_sum(revenue, _TD_YEAR)


def rvd_ext_050_rev_ttm_qoq_change(revenue: pd.Series) -> pd.Series:
    """QoQ change in trailing-twelve-month revenue."""
    ttm = _rolling_sum(revenue, _TD_YEAR)
    return ttm - ttm.shift(_TD_QTR)


def rvd_ext_051_rev_ttm_yoy_pct(revenue: pd.Series) -> pd.Series:
    """YoY percent change in trailing-twelve-month revenue."""
    ttm = _rolling_sum(revenue, _TD_YEAR)
    return _safe_div(ttm - ttm.shift(_TD_YEAR), ttm.shift(_TD_YEAR).abs())


def rvd_ext_052_rev_ttm_dd_from_peak(revenue: pd.Series) -> pd.Series:
    """TTM revenue drawdown from its trailing 5-year peak."""
    ttm = _rolling_sum(revenue, _TD_YEAR)
    peak = ttm.rolling(_TD_5YEAR, min_periods=_TD_YEAR).max()
    return _safe_div(ttm - peak, peak.abs())


def rvd_ext_053_rev_ttm_decline_flag(revenue: pd.Series) -> pd.Series:
    """Flag: TTM revenue lower than one quarter ago (annualized contraction)."""
    ttm = _rolling_sum(revenue, _TD_YEAR)
    return ((ttm - ttm.shift(_TD_QTR)) < 0).astype(float)


def rvd_ext_054_rev_consecutive_yoy_decline(revenue: pd.Series) -> pd.Series:
    """Trailing consecutive-quarter YoY decline count, sampled every 63 days."""
    yoy = revenue - revenue.shift(_TD_YEAR)
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
    return yoy.rolling(_TD_5YEAR, min_periods=1).apply(_streak, raw=True)


def rvd_ext_055_rev_yoy_decline_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of YoY declining quarters in the trailing 8-quarter window."""
    flag = ((revenue - revenue.shift(_TD_YEAR)) < 0).astype(float)
    return _rolling_sum(flag, _TD_2YEAR)


def rvd_ext_056_rev_qoq_decline_count_12q(revenue: pd.Series) -> pd.Series:
    """Count of QoQ declining quarters in the trailing 12-quarter window."""
    flag = ((revenue - revenue.shift(_TD_QTR)) < 0).astype(float)
    return _rolling_sum(flag, _TD_3YEAR)


def rvd_ext_057_rev_qoq_decline_fraction_12q(revenue: pd.Series) -> pd.Series:
    """Fraction of the trailing 12-quarter window with QoQ revenue decline."""
    flag = ((revenue - revenue.shift(_TD_QTR)) < 0).astype(float)
    return _rolling_mean(flag, _TD_3YEAR)


def rvd_ext_058_rev_max_consec_decline_12q(revenue: pd.Series) -> pd.Series:
    """Maximum QoQ-decline streak observed within the trailing 12-quarter window."""
    qoq = revenue - revenue.shift(_TD_QTR)
    contracting = (qoq < 0).astype(float)
    def _maxstreak(x):
        best = 0.0
        cur = 0.0
        for v in x:
            if v == 1.0:
                cur += 1.0
                if cur > best:
                    best = cur
            else:
                cur = 0.0
        return best
    return contracting.rolling(_TD_3YEAR, min_periods=1).apply(_maxstreak, raw=True)


def rvd_ext_059_rev_ttm_4y_to_1y_avg_ratio(revenue: pd.Series) -> pd.Series:
    """Trailing 4-year mean revenue divided by trailing 1-year mean revenue."""
    return _safe_div(_rolling_mean(revenue, _TD_4YEAR), _rolling_mean(revenue, _TD_YEAR).abs())


def rvd_ext_060_rev_ttm_pct_of_5y_peak(revenue: pd.Series) -> pd.Series:
    """TTM revenue as fraction of its trailing-5-year peak TTM (<=1; low = collapse)."""
    ttm = _rolling_sum(revenue, _TD_YEAR)
    peak = ttm.rolling(_TD_5YEAR, min_periods=_TD_YEAR).max()
    return _safe_div(ttm, peak.replace(0, np.nan))


# --- Group F (061-068): Dispersion and stability of revenue ---

def rvd_ext_061_rev_zscore_12q(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue within a trailing 12-quarter (756-day) window."""
    return _zscore_rolling(revenue, _TD_3YEAR)


def rvd_ext_062_rev_qoq_pct_zscore_12q(revenue: pd.Series) -> pd.Series:
    """Z-score of QoQ revenue growth within a trailing 12-quarter window."""
    return _zscore_rolling(_qoq_pct(revenue, _TD_QTR), _TD_3YEAR)


def rvd_ext_063_rev_yoy_pct_zscore_8q(revenue: pd.Series) -> pd.Series:
    """Z-score of YoY revenue growth within a trailing 8-quarter window."""
    return _zscore_rolling(_qoq_pct(revenue, _TD_YEAR), _TD_2YEAR)


def rvd_ext_064_rev_qoq_pct_std_8q(revenue: pd.Series) -> pd.Series:
    """Rolling std of QoQ revenue growth over the trailing 8-quarter window."""
    return _rolling_std(_qoq_pct(revenue, _TD_QTR), _TD_2YEAR)


def rvd_ext_065_rev_coef_variation_8q(revenue: pd.Series) -> pd.Series:
    """Coefficient of variation of revenue over the trailing 8-quarter window."""
    return _safe_div(_rolling_std(revenue, _TD_2YEAR), _rolling_mean(revenue, _TD_2YEAR).abs())


def rvd_ext_066_rev_drop_vs_volatility(revenue: pd.Series) -> pd.Series:
    """Current QoQ revenue change normalized by trailing 8q std of QoQ changes."""
    qoq = revenue - revenue.shift(_TD_QTR)
    return _safe_div(qoq, _rolling_std(qoq, _TD_2YEAR))


def rvd_ext_067_rev_vs_8q_median_pct(revenue: pd.Series) -> pd.Series:
    """Revenue percent deviation from trailing 8-quarter median."""
    med = _rolling_median(revenue, _TD_2YEAR)
    return _safe_div(revenue - med, med.abs())


def rvd_ext_068_rev_vs_ewm_12q(revenue: pd.Series) -> pd.Series:
    """Revenue percent deviation from trailing 12-quarter exponentially-weighted mean."""
    ewm = _ewm_mean(revenue, _TD_3YEAR)
    return _safe_div(revenue - ewm, ewm.abs())


# --- Group G (069-075): Revenue-quality ratios and composites ---

def rvd_ext_069_assetturnover_proxy(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Revenue-to-total-assets ratio (asset-turnover proxy; declining = deterioration)."""
    return _safe_div(revenue, assets)


def rvd_ext_070_assetturnover_yoy_chg(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in revenue-to-assets ratio."""
    r = _safe_div(revenue, assets)
    return r - r.shift(_TD_YEAR)


def rvd_ext_071_rev_to_workingcapital(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Revenue divided by working capital (top-line efficiency of working capital)."""
    return _safe_div(revenue, workingcapital)


def rvd_ext_072_opex_to_rev_ratio(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    """Operating expense as fraction of revenue (rising = top-line not covering costs)."""
    return _safe_div(opex, revenue)


def rvd_ext_073_cor_to_rev_yoy_chg(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY change in COGS-to-revenue ratio (cost rising relative to top line)."""
    r = _safe_div(cor, revenue)
    return r - r.shift(_TD_YEAR)


def rvd_ext_074_rev_per_share_dd_from_8q_peak(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Revenue-per-share drawdown from its trailing 8-quarter peak."""
    rps = _safe_div(revenue, shareswa)
    peak = _rolling_max(rps, _TD_2YEAR)
    return _safe_div(rps - peak, peak.abs())


def rvd_ext_075_revenue_deterioration_composite(revenue: pd.Series) -> pd.Series:
    """Composite deterioration score: depth-from-12q-peak (%), inverse 12q pct-rank,
    abs 12q z-score (clipped), and YoY-decline indicator. Higher = more severe."""
    peak = _rolling_max(revenue, _TD_3YEAR)
    depth = _safe_div(peak - revenue, peak.abs()).clip(lower=0.0, upper=1.0)
    rank = _rolling_rank_pct(revenue, _TD_3YEAR).fillna(0.5)
    z = _zscore_rolling(revenue, _TD_3YEAR).abs().clip(upper=3.0) / 3.0
    decl = (_qoq_pct(revenue, _TD_YEAR) < 0).astype(float)
    return depth + (1.0 - rank) + z + decl


# ── Registry ──────────────────────────────────────────────────────────────────

REVENUE_DETERIORATION_EXTENDED_REGISTRY_001_075 = {
    "rvd_ext_001_rev_2q_pct": {"inputs": ["revenue"], "func": rvd_ext_001_rev_2q_pct},
    "rvd_ext_002_rev_3q_pct": {"inputs": ["revenue"], "func": rvd_ext_002_rev_3q_pct},
    "rvd_ext_003_rev_4y_pct": {"inputs": ["revenue"], "func": rvd_ext_003_rev_4y_pct},
    "rvd_ext_004_rev_5y_pct": {"inputs": ["revenue"], "func": rvd_ext_004_rev_5y_pct},
    "rvd_ext_005_rev_2q_abs": {"inputs": ["revenue"], "func": rvd_ext_005_rev_2q_abs},
    "rvd_ext_006_rev_2y_abs": {"inputs": ["revenue"], "func": rvd_ext_006_rev_2y_abs},
    "rvd_ext_007_rev_3q_log": {"inputs": ["revenue"], "func": rvd_ext_007_rev_3q_log},
    "rvd_ext_008_rev_2y_log": {"inputs": ["revenue"], "func": rvd_ext_008_rev_2y_log},
    "rvd_ext_009_rev_qoq_pct_half_lag": {"inputs": ["revenue"], "func": rvd_ext_009_rev_qoq_pct_half_lag},
    "rvd_ext_010_rev_2q_pct_rank_12q": {"inputs": ["revenue"], "func": rvd_ext_010_rev_2q_pct_rank_12q},
    "rvd_ext_011_rev_yoy_pct_rank_12q": {"inputs": ["revenue"], "func": rvd_ext_011_rev_yoy_pct_rank_12q},
    "rvd_ext_012_rev_2q_sign": {"inputs": ["revenue"], "func": rvd_ext_012_rev_2q_sign},
    "rvd_ext_013_rev_qoq_growth_accel": {"inputs": ["revenue"], "func": rvd_ext_013_rev_qoq_growth_accel},
    "rvd_ext_014_rev_yoy_growth_accel": {"inputs": ["revenue"], "func": rvd_ext_014_rev_yoy_growth_accel},
    "rvd_ext_015_rev_yoy_growth_accel_qoq": {"inputs": ["revenue"], "func": rvd_ext_015_rev_yoy_growth_accel_qoq},
    "rvd_ext_016_rev_level_second_diff": {"inputs": ["revenue"], "func": rvd_ext_016_rev_level_second_diff},
    "rvd_ext_017_rev_growth_decel_flag": {"inputs": ["revenue"], "func": rvd_ext_017_rev_growth_decel_flag},
    "rvd_ext_018_rev_decline_worsening_flag": {"inputs": ["revenue"], "func": rvd_ext_018_rev_decline_worsening_flag},
    "rvd_ext_019_rev_qoq_chg_mean_4q": {"inputs": ["revenue"], "func": rvd_ext_019_rev_qoq_chg_mean_4q},
    "rvd_ext_020_rev_qoq_chg_mean_8q": {"inputs": ["revenue"], "func": rvd_ext_020_rev_qoq_chg_mean_8q},
    "rvd_ext_021_rev_yoy_growth_slope_8q": {"inputs": ["revenue"], "func": rvd_ext_021_rev_yoy_growth_slope_8q},
    "rvd_ext_022_rev_worst_qoq_drop_12q": {"inputs": ["revenue"], "func": rvd_ext_022_rev_worst_qoq_drop_12q},
    "rvd_ext_023_rev_qoq_growth_minus_yoy_growth": {"inputs": ["revenue"], "func": rvd_ext_023_rev_qoq_growth_minus_yoy_growth},
    "rvd_ext_024_rev_yoy_growth_below_zero_flag": {"inputs": ["revenue"], "func": rvd_ext_024_rev_yoy_growth_below_zero_flag},
    "rvd_ext_025_rev_range_pos_4q": {"inputs": ["revenue"], "func": rvd_ext_025_rev_range_pos_4q},
    "rvd_ext_026_rev_range_pos_8q": {"inputs": ["revenue"], "func": rvd_ext_026_rev_range_pos_8q},
    "rvd_ext_027_rev_range_pos_12q": {"inputs": ["revenue"], "func": rvd_ext_027_rev_range_pos_12q},
    "rvd_ext_028_rev_range_pos_20q": {"inputs": ["revenue"], "func": rvd_ext_028_rev_range_pos_20q},
    "rvd_ext_029_rev_new_8q_low_flag": {"inputs": ["revenue"], "func": rvd_ext_029_rev_new_8q_low_flag},
    "rvd_ext_030_rev_new_12q_low_flag": {"inputs": ["revenue"], "func": rvd_ext_030_rev_new_12q_low_flag},
    "rvd_ext_031_rev_new_ath_low_flag": {"inputs": ["revenue"], "func": rvd_ext_031_rev_new_ath_low_flag},
    "rvd_ext_032_rev_below_8q_avg_flag": {"inputs": ["revenue"], "func": rvd_ext_032_rev_below_8q_avg_flag},
    "rvd_ext_033_rev_below_12q_avg_flag": {"inputs": ["revenue"], "func": rvd_ext_033_rev_below_12q_avg_flag},
    "rvd_ext_034_rev_below_8q_median_flag": {"inputs": ["revenue"], "func": rvd_ext_034_rev_below_8q_median_flag},
    "rvd_ext_035_rev_at_2q_low_flag": {"inputs": ["revenue"], "func": rvd_ext_035_rev_at_2q_low_flag},
    "rvd_ext_036_rev_count_new_4q_lows_8q": {"inputs": ["revenue"], "func": rvd_ext_036_rev_count_new_4q_lows_8q},
    "rvd_ext_037_rev_recovery_from_8q_low": {"inputs": ["revenue"], "func": rvd_ext_037_rev_recovery_from_8q_low},
    "rvd_ext_038_rev_recovery_from_12q_low": {"inputs": ["revenue"], "func": rvd_ext_038_rev_recovery_from_12q_low},
    "rvd_ext_039_rev_pct_recovery_from_8q_low": {"inputs": ["revenue"], "func": rvd_ext_039_rev_pct_recovery_from_8q_low},
    "rvd_ext_040_rev_pct_recovery_from_ath_low": {"inputs": ["revenue"], "func": rvd_ext_040_rev_pct_recovery_from_ath_low},
    "rvd_ext_041_rev_dd_from_2q_peak": {"inputs": ["revenue"], "func": rvd_ext_041_rev_dd_from_2q_peak},
    "rvd_ext_042_rev_dd_from_16q_peak": {"inputs": ["revenue"], "func": rvd_ext_042_rev_dd_from_16q_peak},
    "rvd_ext_043_rev_log_dd_from_8q_peak": {"inputs": ["revenue"], "func": rvd_ext_043_rev_log_dd_from_8q_peak},
    "rvd_ext_044_rev_log_dd_from_12q_peak": {"inputs": ["revenue"], "func": rvd_ext_044_rev_log_dd_from_12q_peak},
    "rvd_ext_045_rev_dd_depth_below_8q_peak_abs": {"inputs": ["revenue"], "func": rvd_ext_045_rev_dd_depth_below_8q_peak_abs},
    "rvd_ext_046_rev_dd_intensity_8q": {"inputs": ["revenue"], "func": rvd_ext_046_rev_dd_intensity_8q},
    "rvd_ext_047_rev_time_below_8q_peak_frac": {"inputs": ["revenue"], "func": rvd_ext_047_rev_time_below_8q_peak_frac},
    "rvd_ext_048_rev_dd_4q_minus_dd_12q": {"inputs": ["revenue"], "func": rvd_ext_048_rev_dd_4q_minus_dd_12q},
    "rvd_ext_049_rev_ttm_sum": {"inputs": ["revenue"], "func": rvd_ext_049_rev_ttm_sum},
    "rvd_ext_050_rev_ttm_qoq_change": {"inputs": ["revenue"], "func": rvd_ext_050_rev_ttm_qoq_change},
    "rvd_ext_051_rev_ttm_yoy_pct": {"inputs": ["revenue"], "func": rvd_ext_051_rev_ttm_yoy_pct},
    "rvd_ext_052_rev_ttm_dd_from_peak": {"inputs": ["revenue"], "func": rvd_ext_052_rev_ttm_dd_from_peak},
    "rvd_ext_053_rev_ttm_decline_flag": {"inputs": ["revenue"], "func": rvd_ext_053_rev_ttm_decline_flag},
    "rvd_ext_054_rev_consecutive_yoy_decline": {"inputs": ["revenue"], "func": rvd_ext_054_rev_consecutive_yoy_decline},
    "rvd_ext_055_rev_yoy_decline_count_8q": {"inputs": ["revenue"], "func": rvd_ext_055_rev_yoy_decline_count_8q},
    "rvd_ext_056_rev_qoq_decline_count_12q": {"inputs": ["revenue"], "func": rvd_ext_056_rev_qoq_decline_count_12q},
    "rvd_ext_057_rev_qoq_decline_fraction_12q": {"inputs": ["revenue"], "func": rvd_ext_057_rev_qoq_decline_fraction_12q},
    "rvd_ext_058_rev_max_consec_decline_12q": {"inputs": ["revenue"], "func": rvd_ext_058_rev_max_consec_decline_12q},
    "rvd_ext_059_rev_ttm_4y_to_1y_avg_ratio": {"inputs": ["revenue"], "func": rvd_ext_059_rev_ttm_4y_to_1y_avg_ratio},
    "rvd_ext_060_rev_ttm_pct_of_5y_peak": {"inputs": ["revenue"], "func": rvd_ext_060_rev_ttm_pct_of_5y_peak},
    "rvd_ext_061_rev_zscore_12q": {"inputs": ["revenue"], "func": rvd_ext_061_rev_zscore_12q},
    "rvd_ext_062_rev_qoq_pct_zscore_12q": {"inputs": ["revenue"], "func": rvd_ext_062_rev_qoq_pct_zscore_12q},
    "rvd_ext_063_rev_yoy_pct_zscore_8q": {"inputs": ["revenue"], "func": rvd_ext_063_rev_yoy_pct_zscore_8q},
    "rvd_ext_064_rev_qoq_pct_std_8q": {"inputs": ["revenue"], "func": rvd_ext_064_rev_qoq_pct_std_8q},
    "rvd_ext_065_rev_coef_variation_8q": {"inputs": ["revenue"], "func": rvd_ext_065_rev_coef_variation_8q},
    "rvd_ext_066_rev_drop_vs_volatility": {"inputs": ["revenue"], "func": rvd_ext_066_rev_drop_vs_volatility},
    "rvd_ext_067_rev_vs_8q_median_pct": {"inputs": ["revenue"], "func": rvd_ext_067_rev_vs_8q_median_pct},
    "rvd_ext_068_rev_vs_ewm_12q": {"inputs": ["revenue"], "func": rvd_ext_068_rev_vs_ewm_12q},
    "rvd_ext_069_assetturnover_proxy": {"inputs": ["revenue", "assets"], "func": rvd_ext_069_assetturnover_proxy},
    "rvd_ext_070_assetturnover_yoy_chg": {"inputs": ["revenue", "assets"], "func": rvd_ext_070_assetturnover_yoy_chg},
    "rvd_ext_071_rev_to_workingcapital": {"inputs": ["revenue", "workingcapital"], "func": rvd_ext_071_rev_to_workingcapital},
    "rvd_ext_072_opex_to_rev_ratio": {"inputs": ["revenue", "opex"], "func": rvd_ext_072_opex_to_rev_ratio},
    "rvd_ext_073_cor_to_rev_yoy_chg": {"inputs": ["revenue", "cor"], "func": rvd_ext_073_cor_to_rev_yoy_chg},
    "rvd_ext_074_rev_per_share_dd_from_8q_peak": {"inputs": ["revenue", "shareswa"], "func": rvd_ext_074_rev_per_share_dd_from_8q_peak},
    "rvd_ext_075_revenue_deterioration_composite": {"inputs": ["revenue"], "func": rvd_ext_075_revenue_deterioration_composite},
}
