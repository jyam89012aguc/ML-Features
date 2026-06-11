"""
100_listing_status_risk — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative listing-status-risk features (exhaustion/inflection)
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to a shared trading-day
index.  Status fields (exchange_tier, delist_notice) are forward-filled.
The 3rd-derivative series are highly sparse on a daily index because they
derive from infrequently-changing tier and notice data — this is correct and
expected.  Functions look strictly backward using .shift(positive), .rolling(),
or .expanding().  Trading-day constants: 1 year = 252 td, 1 quarter = 63 td,
1 month = 21 td, 1 week = 5 td.

Inputs
------
exchange_tier : daily ordinal — 1=NYSE/NASDAQ Global Select, 2=NASDAQ Global/
                Capital Market, 3=NYSE American/regional, 4=OTCQX/OTCQB,
                5=Pink/Expert Market.  Higher = lower-tier / more distressed.
delist_notice : binary (1.0/0.0) — 1 when a delisting or listing-deficiency
                notice is in effect.
closeunadj    : raw unadjusted daily close price (USD).
close         : split/dividend-adjusted daily close price (USD).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_2Q    = 126
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _streak_length(binary: pd.Series) -> pd.Series:
    """Current consecutive run length of 1s; resets to 0 on any 0."""
    arr    = binary.fillna(0).values.astype(int)
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=binary.index)


# ── Base and 2nd-derivative helpers (self-contained) ─────────────────────────

def _tier_mean_63(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_mean(exchange_tier.astype(float), _TD_QTR)


def _tier_mean_252(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_mean(exchange_tier.astype(float), _TD_YEAR)


def _tier_max_252(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_max(exchange_tier.astype(float), _TD_YEAR)


def _tier_zscore_252(exchange_tier: pd.Series) -> pd.Series:
    s  = exchange_tier.astype(float)
    m  = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def _tier_cumday_252(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_sum(exchange_tier.astype(float), _TD_YEAR)


def _tier_ewm63(exchange_tier: pd.Series) -> pd.Series:
    return _ewm_mean(exchange_tier.astype(float), _TD_QTR)


def _notice_fraction_63(delist_notice: pd.Series) -> pd.Series:
    return _rolling_mean(delist_notice.astype(float), _TD_QTR)


def _notice_fraction_252(delist_notice: pd.Series) -> pd.Series:
    return _rolling_mean(delist_notice.astype(float), _TD_YEAR)


def _notice_days_252(delist_notice: pd.Series) -> pd.Series:
    return _rolling_sum(delist_notice.astype(float), _TD_YEAR)


def _notice_streak(delist_notice: pd.Series) -> pd.Series:
    return _streak_length(delist_notice.astype(float))


def _sub1_fraction_63(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_QTR)


def _sub1_fraction_252(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_YEAR)


def _sub1_days_252(closeunadj: pd.Series) -> pd.Series:
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_YEAR)


def _close_drawdown_252(close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def _distress_score(exchange_tier: pd.Series, delist_notice: pd.Series, closeunadj: pd.Series) -> pd.Series:
    return (
        exchange_tier.astype(float)
        + 2.0 * delist_notice.astype(float)
        + 3.0 * (closeunadj < 1.0).astype(float)
    )


# ── 2nd-derivative helpers (inlined for 3rd-derivative computation) ───────────

def _drv2_tier_mean_63d_21d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_mean_63(exchange_tier)
    return base - base.shift(_TD_MO)


def _drv2_tier_mean_63d_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_mean_63(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_tier_mean_252d_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_mean_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_tier_max_252d_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_max_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_tier_zscore_252d_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_zscore_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_tier_cumday_252d_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_cumday_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_tier_ewm63_21d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_ewm63(exchange_tier)
    return base - base.shift(_TD_MO)


def _drv2_notice_fraction_63d_21d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_fraction_63(delist_notice)
    return base - base.shift(_TD_MO)


def _drv2_notice_fraction_63d_63d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_fraction_63(delist_notice)
    return base - base.shift(_TD_QTR)


def _drv2_notice_fraction_252d_63d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_fraction_252(delist_notice)
    return base - base.shift(_TD_QTR)


def _drv2_notice_days_252d_63d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_days_252(delist_notice)
    return base - base.shift(_TD_QTR)


def _drv2_notice_streak_21d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_streak(delist_notice)
    return base - base.shift(_TD_MO)


def _drv2_sub1_fraction_63d_21d(closeunadj: pd.Series) -> pd.Series:
    base = _sub1_fraction_63(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_sub1_fraction_252d_63d(closeunadj: pd.Series) -> pd.Series:
    base = _sub1_fraction_252(closeunadj)
    return base - base.shift(_TD_QTR)


def _drv2_close_drawdown_252d_21d(close: pd.Series) -> pd.Series:
    base = _close_drawdown_252(close)
    return base - base.shift(_TD_MO)


def _drv2_distress_ewm63_21d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    base = _ewm_mean(_distress_score(exchange_tier, delist_notice, closeunadj), _TD_QTR)
    return base - base.shift(_TD_MO)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def lsr_drv3_001_tier_mean_63d_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 63d tier mean (inflection in tier acceleration)."""
    d2 = _drv2_tier_mean_63d_21d(exchange_tier)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_002_tier_mean_63d_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 63d tier mean (quarterly inflection)."""
    d2 = _drv2_tier_mean_63d_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_003_tier_mean_252d_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d tier mean."""
    d2 = _drv2_tier_mean_252d_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_004_tier_max_252d_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d max tier (tier-max inflection)."""
    d2 = _drv2_tier_max_252d_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_005_tier_zscore_252d_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d tier z-score."""
    d2 = _drv2_tier_zscore_252d_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_006_tier_cumday_252d_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d cumulative tier-day score."""
    d2 = _drv2_tier_cumday_252d_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_007_tier_ewm63_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of EWM(63) tier."""
    d2 = _drv2_tier_ewm63_21d(exchange_tier)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_008_notice_fraction_63d_21d_diff2(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 63d notice fraction."""
    d2 = _drv2_notice_fraction_63d_21d(delist_notice)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_009_notice_fraction_63d_63d_diff2(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 63d notice fraction."""
    d2 = _drv2_notice_fraction_63d_63d(delist_notice)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_010_notice_fraction_252d_63d_diff2(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d notice fraction."""
    d2 = _drv2_notice_fraction_252d_63d(delist_notice)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_011_notice_days_252d_63d_diff2(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d notice day count."""
    d2 = _drv2_notice_days_252d_63d(delist_notice)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_012_notice_streak_21d_diff2(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of notice streak length."""
    d2 = _drv2_notice_streak_21d(delist_notice)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_013_sub1_fraction_63d_21d_diff2(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 63d sub-$1 fraction."""
    d2 = _drv2_sub1_fraction_63d_21d(closeunadj)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_014_sub1_fraction_252d_63d_diff2(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d sub-$1 fraction."""
    d2 = _drv2_sub1_fraction_252d_63d(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_015_close_drawdown_252d_21d_diff2(close: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 252d price drawdown."""
    d2 = _drv2_close_drawdown_252d_21d(close)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_016_distress_ewm63_21d_diff2(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """21-day change in the 2nd-deriv of EWM(63) combined distress score."""
    d2 = _drv2_distress_ewm63_21d(exchange_tier, delist_notice, closeunadj)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_017_tier_mean_63_accel_ewm21(exchange_tier: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 63d tier mean (smoothed tier acceleration)."""
    d2 = _drv2_tier_mean_63d_21d(exchange_tier)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_018_notice_fraction_accel_ewm21(delist_notice: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 63d notice fraction (smoothed notice acceleration)."""
    d2 = _drv2_notice_fraction_63d_21d(delist_notice)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_019_sub1_fraction_accel_ewm21(closeunadj: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 63d sub-$1 fraction (smoothed sub-$1 acceleration)."""
    d2 = _drv2_sub1_fraction_63d_21d(closeunadj)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_020_drawdown_accel_ewm21(close: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d price drawdown (smoothed drawdown acceleration)."""
    d2 = _drv2_close_drawdown_252d_21d(close)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_021_tier_mean_252d_252d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """252-day change in the YoY 2nd-deriv of 252d tier mean (multi-year exhaustion)."""
    base = _tier_mean_252(exchange_tier)
    d2   = base - base.shift(_TD_YEAR)
    return d2 - d2.shift(_TD_YEAR)


def lsr_drv3_022_notice_fraction_252d_252d_diff2(delist_notice: pd.Series) -> pd.Series:
    """252-day change in the YoY 2nd-deriv of 252d notice fraction."""
    base = _notice_fraction_252(delist_notice)
    d2   = base - base.shift(_TD_YEAR)
    return d2 - d2.shift(_TD_YEAR)


def lsr_drv3_023_tier_zscore_accel_ewm63(exchange_tier: pd.Series) -> pd.Series:
    """EWM(63) of the 2nd-deriv of 252d tier z-score (smoothed quarterly zscore accel)."""
    d2 = _drv2_tier_zscore_252d_63d(exchange_tier)
    return _ewm_mean(d2, _TD_QTR)


def lsr_drv3_024_sub1_fraction_252d_252d_diff2(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the YoY 2nd-deriv of 252d sub-$1 fraction."""
    base = _sub1_fraction_252(closeunadj)
    d2   = base - base.shift(_TD_YEAR)
    return d2 - d2.shift(_TD_YEAR)


def lsr_drv3_025_distress_composite_inflection(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """
    3rd-order inflection of combined distress: 21d diff of the 2nd-deriv of
    EWM(63) distress score, then smoothed with EWM(21).
    Captures the moment distress acceleration itself starts to turn.
    """
    d2   = _drv2_distress_ewm63_21d(exchange_tier, delist_notice, closeunadj)
    d3   = d2 - d2.shift(_TD_MO)
    return _ewm_mean(d3, _TD_MO)


# ── Additional 2nd-derivative helpers for new 3rd-derivative features ─────────

def _tier_mean_126(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_mean(exchange_tier.astype(float), _TD_2Q)


def _tier_ewm21(exchange_tier: pd.Series) -> pd.Series:
    return _ewm_mean(exchange_tier.astype(float), _TD_MO)


def _tier_std_63(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_std(exchange_tier.astype(float), _TD_QTR)


def _tier_pct_rank_252(exchange_tier: pd.Series) -> pd.Series:
    return exchange_tier.astype(float).rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def _notice_fraction_21(delist_notice: pd.Series) -> pd.Series:
    return _rolling_mean(delist_notice.astype(float), _TD_MO)


def _notice_fraction_126(delist_notice: pd.Series) -> pd.Series:
    return _rolling_mean(delist_notice.astype(float), _TD_2Q)


def _notice_ewm63(delist_notice: pd.Series) -> pd.Series:
    return _ewm_mean(delist_notice.astype(float), _TD_QTR)


def _sub1_fraction_126(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_2Q)


def _sub2_fraction_63(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_QTR)


def _close_drawdown_504(close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_2Y)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def _close_drawdown_126(close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_2Q)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def _distress_score_v2(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    return exchange_tier.astype(float) + 2.0 * delist_notice.astype(float)


# 2nd-deriv helpers used by new 3rd-deriv features
def _drv2_tier_mean_126d_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_mean_126(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_tier_mean_126d_21d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_mean_126(exchange_tier)
    return base - base.shift(_TD_MO)


def _drv2_tier_ewm21_21d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_ewm21(exchange_tier)
    return base - base.shift(_TD_MO)


def _drv2_tier_ewm21_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_ewm21(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_tier_std_63d_21d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_std_63(exchange_tier)
    return base - base.shift(_TD_MO)


def _drv2_tier_pct_rank_252d_21d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_pct_rank_252(exchange_tier)
    return base - base.shift(_TD_MO)


def _drv2_tier_pct_rank_252d_63d(exchange_tier: pd.Series) -> pd.Series:
    base = _tier_pct_rank_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def _drv2_notice_fraction_21d_21d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_fraction_21(delist_notice)
    return base - base.shift(_TD_MO)


def _drv2_notice_fraction_126d_63d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_fraction_126(delist_notice)
    return base - base.shift(_TD_QTR)


def _drv2_notice_ewm63_21d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_ewm63(delist_notice)
    return base - base.shift(_TD_MO)


def _drv2_notice_ewm63_63d(delist_notice: pd.Series) -> pd.Series:
    base = _notice_ewm63(delist_notice)
    return base - base.shift(_TD_QTR)


def _drv2_sub1_fraction_126d_63d(closeunadj: pd.Series) -> pd.Series:
    base = _sub1_fraction_126(closeunadj)
    return base - base.shift(_TD_QTR)


def _drv2_sub2_fraction_63d_21d(closeunadj: pd.Series) -> pd.Series:
    base = _sub2_fraction_63(closeunadj)
    return base - base.shift(_TD_MO)


def _drv2_close_drawdown_504d_63d(close: pd.Series) -> pd.Series:
    base = _close_drawdown_504(close)
    return base - base.shift(_TD_QTR)


def _drv2_close_drawdown_126d_21d(close: pd.Series) -> pd.Series:
    base = _close_drawdown_126(close)
    return base - base.shift(_TD_MO)


def _drv2_distress_v2_ewm63_21d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    base = _ewm_mean(_distress_score_v2(exchange_tier, delist_notice), _TD_QTR)
    return base - base.shift(_TD_MO)


def _drv2_distress_ewm252_21d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    base = _ewm_mean(_distress_score(exchange_tier, delist_notice, closeunadj), _TD_YEAR)
    return base - base.shift(_TD_MO)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def lsr_drv3_026_tier_mean_126d_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 126d tier mean (half-year tier inflection)."""
    d2 = _drv2_tier_mean_126d_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_027_tier_mean_126d_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 126d tier mean."""
    d2 = _drv2_tier_mean_126d_21d(exchange_tier)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_028_tier_ewm21_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of EWM(21) tier."""
    d2 = _drv2_tier_ewm21_21d(exchange_tier)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_029_tier_ewm21_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of EWM(21) tier."""
    d2 = _drv2_tier_ewm21_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_030_tier_std_63d_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 63d tier std (tier volatility inflection)."""
    d2 = _drv2_tier_std_63d_21d(exchange_tier)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_031_tier_pct_rank_252d_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 252d tier pct rank."""
    d2 = _drv2_tier_pct_rank_252d_21d(exchange_tier)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_032_tier_pct_rank_252d_63d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 252d tier pct rank."""
    d2 = _drv2_tier_pct_rank_252d_63d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_033_tier_mean_63d_21d_accel_ewm63(exchange_tier: pd.Series) -> pd.Series:
    """EWM(63) of the 2nd-deriv of 63d tier mean (medium-term smoothed acceleration)."""
    d2 = _drv2_tier_mean_63d_21d(exchange_tier)
    return _ewm_mean(d2, _TD_QTR)


def lsr_drv3_034_tier_mean_252d_63d_accel_ewm21(exchange_tier: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d tier mean."""
    d2 = _drv2_tier_mean_252d_63d(exchange_tier)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_035_tier_zscore_252d_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 252d tier z-score."""
    base = _tier_zscore_252(exchange_tier)
    d2   = base - base.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_036_notice_fraction_21d_21d_diff2(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 21d notice fraction."""
    d2 = _drv2_notice_fraction_21d_21d(delist_notice)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_037_notice_fraction_126d_63d_diff2(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 126d notice fraction."""
    d2 = _drv2_notice_fraction_126d_63d(delist_notice)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_038_notice_ewm63_21d_diff2(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of EWM(63) notice flag."""
    d2 = _drv2_notice_ewm63_21d(delist_notice)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_039_notice_ewm63_63d_diff2(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of EWM(63) notice flag."""
    d2 = _drv2_notice_ewm63_63d(delist_notice)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_040_notice_fraction_63d_21d_accel_ewm63(delist_notice: pd.Series) -> pd.Series:
    """EWM(63) of the 2nd-deriv of 63d notice fraction (smoothed notice inflection)."""
    d2 = _drv2_notice_fraction_63d_21d(delist_notice)
    return _ewm_mean(d2, _TD_QTR)


def lsr_drv3_041_sub1_fraction_126d_63d_diff2(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 126d sub-$1 fraction."""
    d2 = _drv2_sub1_fraction_126d_63d(closeunadj)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_042_sub2_fraction_63d_21d_diff2(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 63d sub-$2 fraction."""
    d2 = _drv2_sub2_fraction_63d_21d(closeunadj)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_043_sub1_fraction_63d_21d_accel_ewm63(closeunadj: pd.Series) -> pd.Series:
    """EWM(63) of the 2nd-deriv of 63d sub-$1 fraction."""
    d2 = _drv2_sub1_fraction_63d_21d(closeunadj)
    return _ewm_mean(d2, _TD_QTR)


def lsr_drv3_044_close_drawdown_504d_63d_diff2(close: pd.Series) -> pd.Series:
    """63-day change in the 2nd-deriv of 504d price drawdown."""
    d2 = _drv2_close_drawdown_504d_63d(close)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_045_close_drawdown_126d_21d_diff2(close: pd.Series) -> pd.Series:
    """21-day change in the 2nd-deriv of 126d price drawdown."""
    d2 = _drv2_close_drawdown_126d_21d(close)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_046_distress_v2_ewm63_21d_diff2(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """21-day change in the 2nd-deriv of EWM(63) (tier+2*notice) score."""
    d2 = _drv2_distress_v2_ewm63_21d(exchange_tier, delist_notice)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_047_distress_ewm252_21d_diff2(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """21-day change in the 2nd-deriv of EWM(252) full distress score."""
    d2 = _drv2_distress_ewm252_21d(exchange_tier, delist_notice, closeunadj)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_048_tier_mean_63_accel_ewm63(exchange_tier: pd.Series) -> pd.Series:
    """EWM(63) of the 2nd-deriv of 63d-21d tier mean (longer-smoothed acceleration)."""
    d2 = _drv2_tier_mean_63d_21d(exchange_tier)
    return _ewm_mean(d2, _TD_QTR)


def lsr_drv3_049_notice_streak_21d_accel_ewm21(delist_notice: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of notice streak length."""
    d2 = _drv2_notice_streak_21d(delist_notice)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_050_sub1_fraction_252d_63d_accel_ewm21(closeunadj: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d-63d sub-$1 fraction."""
    d2 = _drv2_sub1_fraction_252d_63d(closeunadj)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_051_tier_mean_63d_21d_diff2_63d(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 21d-diff 2nd-deriv of 63d tier mean."""
    d2 = _drv2_tier_mean_63d_21d(exchange_tier)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_052_tier_mean_252d_63d_diff2_21d(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 63d-diff 2nd-deriv of 252d tier mean."""
    d2 = _drv2_tier_mean_252d_63d(exchange_tier)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_053_tier_zscore_252d_63d_accel_ewm21(exchange_tier: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d tier z-score (quick-smoothed zscore accel)."""
    d2 = _drv2_tier_zscore_252d_63d(exchange_tier)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_054_notice_fraction_252d_63d_accel_ewm21(delist_notice: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d notice fraction."""
    d2 = _drv2_notice_fraction_252d_63d(delist_notice)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_055_notice_days_252d_63d_accel_ewm21(delist_notice: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d notice day count."""
    d2 = _drv2_notice_days_252d_63d(delist_notice)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_056_sub1_fraction_63d_63d_diff2(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 63d-diff 2nd-deriv of 63d sub-$1 fraction."""
    base = _sub1_fraction_63(closeunadj)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def lsr_drv3_057_close_drawdown_252d_63d_accel_ewm21(close: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d-63d price drawdown."""
    base = _close_drawdown_252(close)
    d2   = base - base.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_058_distress_ewm63_21d_accel_ewm63(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """EWM(63) of the 2nd-deriv of EWM(63) distress score."""
    d2 = _drv2_distress_ewm63_21d(exchange_tier, delist_notice, closeunadj)
    return _ewm_mean(d2, _TD_QTR)


def lsr_drv3_059_tier_max_252d_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 21d 2nd-deriv of 252d max tier."""
    base = _tier_max_252(exchange_tier)
    d2   = base - base.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_060_tier_cumday_252d_21d_diff2(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 21d 2nd-deriv of 252d cumulative tier score."""
    base = _tier_cumday_252(exchange_tier)
    d2   = base - base.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_061_tier_mean_63d_63d_accel_ewm21(exchange_tier: pd.Series) -> pd.Series:
    """EWM(21) of the 63d-diff 2nd-deriv of 63d tier mean."""
    d2 = _drv2_tier_mean_63d_63d(exchange_tier)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_062_notice_fraction_63d_63d_accel_ewm21(delist_notice: pd.Series) -> pd.Series:
    """EWM(21) of the 63d-diff 2nd-deriv of 63d notice fraction."""
    d2 = _drv2_notice_fraction_63d_63d(delist_notice)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_063_sub1_fraction_252d_252d_accel_ewm21(closeunadj: pd.Series) -> pd.Series:
    """EWM(21) of the YoY 2nd-deriv of 252d sub-$1 fraction."""
    base = _sub1_fraction_252(closeunadj)
    d2   = base - base.shift(_TD_YEAR)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_064_tier_mean_252d_252d_accel_ewm21(exchange_tier: pd.Series) -> pd.Series:
    """EWM(21) of the YoY 2nd-deriv of 252d tier mean."""
    base = _tier_mean_252(exchange_tier)
    d2   = base - base.shift(_TD_YEAR)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_065_notice_fraction_252d_252d_accel_ewm21(delist_notice: pd.Series) -> pd.Series:
    """EWM(21) of the YoY 2nd-deriv of 252d notice fraction."""
    base = _notice_fraction_252(delist_notice)
    d2   = base - base.shift(_TD_YEAR)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_066_tier_ewm63_21d_accel_ewm63(exchange_tier: pd.Series) -> pd.Series:
    """EWM(63) of the 2nd-deriv of EWM(63) tier (medium-run smoothed impulse)."""
    d2 = _drv2_tier_ewm63_21d(exchange_tier)
    return _ewm_mean(d2, _TD_QTR)


def lsr_drv3_067_distress_ewm63_21d_diff2_ewm63(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """EWM(63) of the 21d change in the 2nd-deriv of EWM(63) distress score."""
    d2  = _drv2_distress_ewm63_21d(exchange_tier, delist_notice, closeunadj)
    d3  = d2 - d2.shift(_TD_MO)
    return _ewm_mean(d3, _TD_QTR)


def lsr_drv3_068_tier_mean_63d_slope_diff_21d(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the rolling 63d OLS slope of the 63d mean tier (slope acceleration)."""
    base = _tier_mean_63(exchange_tier)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    slope = base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_MO)


def lsr_drv3_069_notice_fraction_63_ewm_diff_21d(delist_notice: pd.Series) -> pd.Series:
    """21-day change in (63d notice fraction minus its EWM(252)) — 3rd-order notice signal."""
    base = _notice_fraction_63(delist_notice)
    ewm  = _ewm_mean(base, _TD_YEAR)
    d2   = base - ewm
    return d2 - d2.shift(_TD_MO)


def lsr_drv3_070_sub1_ewm_accel_diff_21d(closeunadj: pd.Series) -> pd.Series:
    """21-day change in EWM(63) of the 2nd-deriv of 63d sub-$1 fraction."""
    d2  = _drv2_sub1_fraction_63d_21d(closeunadj)
    ewm = _ewm_mean(d2, _TD_QTR)
    return ewm - ewm.shift(_TD_MO)


def lsr_drv3_071_drawdown_accel_diff_21d(close: pd.Series) -> pd.Series:
    """21-day change in EWM(21) of the 2nd-deriv of 252d drawdown (jerk signal)."""
    d2  = _drv2_close_drawdown_252d_21d(close)
    ewm = _ewm_mean(d2, _TD_MO)
    return ewm - ewm.shift(_TD_MO)


def lsr_drv3_072_tier_zscore_accel_ewm21(exchange_tier: pd.Series) -> pd.Series:
    """EWM(21) of the 2nd-deriv of 252d tier z-score (quick-smoothed z-score accel)."""
    d2 = _drv2_tier_zscore_252d_63d(exchange_tier)
    return _ewm_mean(d2, _TD_MO)


def lsr_drv3_073_distress_composite_v2_inflection(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """
    3rd-order inflection of tier+2*notice score: 21d diff of the 2nd-deriv of
    EWM(63), then smoothed with EWM(21).
    """
    d2  = _drv2_distress_v2_ewm63_21d(exchange_tier, delist_notice)
    d3  = d2 - d2.shift(_TD_MO)
    return _ewm_mean(d3, _TD_MO)


def lsr_drv3_074_sub1_fraction_252d_slope_diff_21d(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the rolling 63d OLS slope of the 252d sub-$1 fraction series."""
    base = _sub1_fraction_252(closeunadj)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    slope = base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_MO)


def lsr_drv3_075_full_distress_inflection(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """
    Full 3rd-order distress inflection: EWM(63) of (21d diff of the 2nd-deriv of
    EWM(252) distress score).  Captures the turning point in long-run distress trend.
    """
    d2  = _drv2_distress_ewm252_21d(exchange_tier, delist_notice, closeunadj)
    d3  = d2 - d2.shift(_TD_MO)
    return _ewm_mean(d3, _TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

LISTING_STATUS_RISK_REGISTRY_3RD_DERIVATIVES = {
    "lsr_drv3_001_tier_mean_63d_21d_diff2":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_001_tier_mean_63d_21d_diff2},
    "lsr_drv3_002_tier_mean_63d_63d_diff2":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_002_tier_mean_63d_63d_diff2},
    "lsr_drv3_003_tier_mean_252d_63d_diff2":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_003_tier_mean_252d_63d_diff2},
    "lsr_drv3_004_tier_max_252d_63d_diff2":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_004_tier_max_252d_63d_diff2},
    "lsr_drv3_005_tier_zscore_252d_63d_diff2":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_005_tier_zscore_252d_63d_diff2},
    "lsr_drv3_006_tier_cumday_252d_63d_diff2":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_006_tier_cumday_252d_63d_diff2},
    "lsr_drv3_007_tier_ewm63_21d_diff2":             {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_007_tier_ewm63_21d_diff2},
    "lsr_drv3_008_notice_fraction_63d_21d_diff2":    {"inputs": ["delist_notice"],                                 "func": lsr_drv3_008_notice_fraction_63d_21d_diff2},
    "lsr_drv3_009_notice_fraction_63d_63d_diff2":    {"inputs": ["delist_notice"],                                 "func": lsr_drv3_009_notice_fraction_63d_63d_diff2},
    "lsr_drv3_010_notice_fraction_252d_63d_diff2":   {"inputs": ["delist_notice"],                                 "func": lsr_drv3_010_notice_fraction_252d_63d_diff2},
    "lsr_drv3_011_notice_days_252d_63d_diff2":       {"inputs": ["delist_notice"],                                 "func": lsr_drv3_011_notice_days_252d_63d_diff2},
    "lsr_drv3_012_notice_streak_21d_diff2":          {"inputs": ["delist_notice"],                                 "func": lsr_drv3_012_notice_streak_21d_diff2},
    "lsr_drv3_013_sub1_fraction_63d_21d_diff2":      {"inputs": ["closeunadj"],                                    "func": lsr_drv3_013_sub1_fraction_63d_21d_diff2},
    "lsr_drv3_014_sub1_fraction_252d_63d_diff2":     {"inputs": ["closeunadj"],                                    "func": lsr_drv3_014_sub1_fraction_252d_63d_diff2},
    "lsr_drv3_015_close_drawdown_252d_21d_diff2":    {"inputs": ["close"],                                         "func": lsr_drv3_015_close_drawdown_252d_21d_diff2},
    "lsr_drv3_016_distress_ewm63_21d_diff2":         {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv3_016_distress_ewm63_21d_diff2},
    "lsr_drv3_017_tier_mean_63_accel_ewm21":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_017_tier_mean_63_accel_ewm21},
    "lsr_drv3_018_notice_fraction_accel_ewm21":      {"inputs": ["delist_notice"],                                 "func": lsr_drv3_018_notice_fraction_accel_ewm21},
    "lsr_drv3_019_sub1_fraction_accel_ewm21":        {"inputs": ["closeunadj"],                                    "func": lsr_drv3_019_sub1_fraction_accel_ewm21},
    "lsr_drv3_020_drawdown_accel_ewm21":             {"inputs": ["close"],                                         "func": lsr_drv3_020_drawdown_accel_ewm21},
    "lsr_drv3_021_tier_mean_252d_252d_diff2":        {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_021_tier_mean_252d_252d_diff2},
    "lsr_drv3_022_notice_fraction_252d_252d_diff2":  {"inputs": ["delist_notice"],                                 "func": lsr_drv3_022_notice_fraction_252d_252d_diff2},
    "lsr_drv3_023_tier_zscore_accel_ewm63":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_023_tier_zscore_accel_ewm63},
    "lsr_drv3_024_sub1_fraction_252d_252d_diff2":    {"inputs": ["closeunadj"],                                    "func": lsr_drv3_024_sub1_fraction_252d_252d_diff2},
    "lsr_drv3_025_distress_composite_inflection":    {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv3_025_distress_composite_inflection},
    "lsr_drv3_026_tier_mean_126d_63d_diff2":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_026_tier_mean_126d_63d_diff2},
    "lsr_drv3_027_tier_mean_126d_21d_diff2":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_027_tier_mean_126d_21d_diff2},
    "lsr_drv3_028_tier_ewm21_21d_diff2":             {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_028_tier_ewm21_21d_diff2},
    "lsr_drv3_029_tier_ewm21_63d_diff2":             {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_029_tier_ewm21_63d_diff2},
    "lsr_drv3_030_tier_std_63d_21d_diff2":           {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_030_tier_std_63d_21d_diff2},
    "lsr_drv3_031_tier_pct_rank_252d_21d_diff2":     {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_031_tier_pct_rank_252d_21d_diff2},
    "lsr_drv3_032_tier_pct_rank_252d_63d_diff2":     {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_032_tier_pct_rank_252d_63d_diff2},
    "lsr_drv3_033_tier_mean_63d_21d_accel_ewm63":    {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_033_tier_mean_63d_21d_accel_ewm63},
    "lsr_drv3_034_tier_mean_252d_63d_accel_ewm21":   {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_034_tier_mean_252d_63d_accel_ewm21},
    "lsr_drv3_035_tier_zscore_252d_21d_diff2":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_035_tier_zscore_252d_21d_diff2},
    "lsr_drv3_036_notice_fraction_21d_21d_diff2":    {"inputs": ["delist_notice"],                                 "func": lsr_drv3_036_notice_fraction_21d_21d_diff2},
    "lsr_drv3_037_notice_fraction_126d_63d_diff2":   {"inputs": ["delist_notice"],                                 "func": lsr_drv3_037_notice_fraction_126d_63d_diff2},
    "lsr_drv3_038_notice_ewm63_21d_diff2":           {"inputs": ["delist_notice"],                                 "func": lsr_drv3_038_notice_ewm63_21d_diff2},
    "lsr_drv3_039_notice_ewm63_63d_diff2":           {"inputs": ["delist_notice"],                                 "func": lsr_drv3_039_notice_ewm63_63d_diff2},
    "lsr_drv3_040_notice_fraction_63d_21d_accel_ewm63": {"inputs": ["delist_notice"],                             "func": lsr_drv3_040_notice_fraction_63d_21d_accel_ewm63},
    "lsr_drv3_041_sub1_fraction_126d_63d_diff2":     {"inputs": ["closeunadj"],                                    "func": lsr_drv3_041_sub1_fraction_126d_63d_diff2},
    "lsr_drv3_042_sub2_fraction_63d_21d_diff2":      {"inputs": ["closeunadj"],                                    "func": lsr_drv3_042_sub2_fraction_63d_21d_diff2},
    "lsr_drv3_043_sub1_fraction_63d_21d_accel_ewm63": {"inputs": ["closeunadj"],                                   "func": lsr_drv3_043_sub1_fraction_63d_21d_accel_ewm63},
    "lsr_drv3_044_close_drawdown_504d_63d_diff2":    {"inputs": ["close"],                                         "func": lsr_drv3_044_close_drawdown_504d_63d_diff2},
    "lsr_drv3_045_close_drawdown_126d_21d_diff2":    {"inputs": ["close"],                                         "func": lsr_drv3_045_close_drawdown_126d_21d_diff2},
    "lsr_drv3_046_distress_v2_ewm63_21d_diff2":      {"inputs": ["exchange_tier", "delist_notice"],               "func": lsr_drv3_046_distress_v2_ewm63_21d_diff2},
    "lsr_drv3_047_distress_ewm252_21d_diff2":        {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv3_047_distress_ewm252_21d_diff2},
    "lsr_drv3_048_tier_mean_63_accel_ewm63":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_048_tier_mean_63_accel_ewm63},
    "lsr_drv3_049_notice_streak_21d_accel_ewm21":    {"inputs": ["delist_notice"],                                 "func": lsr_drv3_049_notice_streak_21d_accel_ewm21},
    "lsr_drv3_050_sub1_fraction_252d_63d_accel_ewm21": {"inputs": ["closeunadj"],                                  "func": lsr_drv3_050_sub1_fraction_252d_63d_accel_ewm21},
    "lsr_drv3_051_tier_mean_63d_21d_diff2_63d":      {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_051_tier_mean_63d_21d_diff2_63d},
    "lsr_drv3_052_tier_mean_252d_63d_diff2_21d":     {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_052_tier_mean_252d_63d_diff2_21d},
    "lsr_drv3_053_tier_zscore_252d_63d_accel_ewm21": {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_053_tier_zscore_252d_63d_accel_ewm21},
    "lsr_drv3_054_notice_fraction_252d_63d_accel_ewm21": {"inputs": ["delist_notice"],                            "func": lsr_drv3_054_notice_fraction_252d_63d_accel_ewm21},
    "lsr_drv3_055_notice_days_252d_63d_accel_ewm21": {"inputs": ["delist_notice"],                                 "func": lsr_drv3_055_notice_days_252d_63d_accel_ewm21},
    "lsr_drv3_056_sub1_fraction_63d_63d_diff2":      {"inputs": ["closeunadj"],                                    "func": lsr_drv3_056_sub1_fraction_63d_63d_diff2},
    "lsr_drv3_057_close_drawdown_252d_63d_accel_ewm21": {"inputs": ["close"],                                      "func": lsr_drv3_057_close_drawdown_252d_63d_accel_ewm21},
    "lsr_drv3_058_distress_ewm63_21d_accel_ewm63":   {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv3_058_distress_ewm63_21d_accel_ewm63},
    "lsr_drv3_059_tier_max_252d_21d_diff2":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_059_tier_max_252d_21d_diff2},
    "lsr_drv3_060_tier_cumday_252d_21d_diff2":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_060_tier_cumday_252d_21d_diff2},
    "lsr_drv3_061_tier_mean_63d_63d_accel_ewm21":    {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_061_tier_mean_63d_63d_accel_ewm21},
    "lsr_drv3_062_notice_fraction_63d_63d_accel_ewm21": {"inputs": ["delist_notice"],                             "func": lsr_drv3_062_notice_fraction_63d_63d_accel_ewm21},
    "lsr_drv3_063_sub1_fraction_252d_252d_accel_ewm21": {"inputs": ["closeunadj"],                                 "func": lsr_drv3_063_sub1_fraction_252d_252d_accel_ewm21},
    "lsr_drv3_064_tier_mean_252d_252d_accel_ewm21":  {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_064_tier_mean_252d_252d_accel_ewm21},
    "lsr_drv3_065_notice_fraction_252d_252d_accel_ewm21": {"inputs": ["delist_notice"],                           "func": lsr_drv3_065_notice_fraction_252d_252d_accel_ewm21},
    "lsr_drv3_066_tier_ewm63_21d_accel_ewm63":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_066_tier_ewm63_21d_accel_ewm63},
    "lsr_drv3_067_distress_ewm63_21d_diff2_ewm63":   {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv3_067_distress_ewm63_21d_diff2_ewm63},
    "lsr_drv3_068_tier_mean_63d_slope_diff_21d":     {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_068_tier_mean_63d_slope_diff_21d},
    "lsr_drv3_069_notice_fraction_63_ewm_diff_21d":  {"inputs": ["delist_notice"],                                 "func": lsr_drv3_069_notice_fraction_63_ewm_diff_21d},
    "lsr_drv3_070_sub1_ewm_accel_diff_21d":          {"inputs": ["closeunadj"],                                    "func": lsr_drv3_070_sub1_ewm_accel_diff_21d},
    "lsr_drv3_071_drawdown_accel_diff_21d":          {"inputs": ["close"],                                         "func": lsr_drv3_071_drawdown_accel_diff_21d},
    "lsr_drv3_072_tier_zscore_accel_ewm21":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv3_072_tier_zscore_accel_ewm21},
    "lsr_drv3_073_distress_composite_v2_inflection": {"inputs": ["exchange_tier", "delist_notice"],               "func": lsr_drv3_073_distress_composite_v2_inflection},
    "lsr_drv3_074_sub1_fraction_252d_slope_diff_21d": {"inputs": ["closeunadj"],                                   "func": lsr_drv3_074_sub1_fraction_252d_slope_diff_21d},
    "lsr_drv3_075_full_distress_inflection":         {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv3_075_full_distress_inflection},
}
