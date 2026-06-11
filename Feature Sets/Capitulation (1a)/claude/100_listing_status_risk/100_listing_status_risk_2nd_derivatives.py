"""
100_listing_status_risk — 2nd-Derivative Features 001-075
Domain: rate of change of base listing-status-risk features (acceleration)
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to a shared trading-day
index.  Status fields (exchange_tier, delist_notice) are forward-filled.
The 2nd-derivative series are sparse/stepwise on a daily index because the
underlying tier and notice data change infrequently — this is correct and
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


# ── Base feature helpers (self-contained recomputes) ─────────────────────────

def _tier_mean_252(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_mean(exchange_tier.astype(float), _TD_YEAR)


def _tier_mean_63(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_mean(exchange_tier.astype(float), _TD_QTR)


def _tier_max_252(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_max(exchange_tier.astype(float), _TD_YEAR)


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


def _tier_zscore_252(exchange_tier: pd.Series) -> pd.Series:
    s  = exchange_tier.astype(float)
    m  = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def _tier_cumday_252(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_sum(exchange_tier.astype(float), _TD_YEAR)


def _tier_ewm63(exchange_tier: pd.Series) -> pd.Series:
    return _ewm_mean(exchange_tier.astype(float), _TD_QTR)


def _distress_score(exchange_tier: pd.Series, delist_notice: pd.Series, closeunadj: pd.Series) -> pd.Series:
    return (
        exchange_tier.astype(float)
        + 2.0 * delist_notice.astype(float)
        + 3.0 * (closeunadj < 1.0).astype(float)
    )


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def lsr_drv2_001_tier_mean_63d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 63-day rolling mean tier (short-term tier acceleration)."""
    base = _tier_mean_63(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_002_tier_mean_63d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 63-day rolling mean tier (quarterly tier acceleration)."""
    base = _tier_mean_63(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_003_tier_mean_252d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 252-day rolling mean tier."""
    base = _tier_mean_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_004_tier_mean_252d_252d_diff(exchange_tier: pd.Series) -> pd.Series:
    """252-day change in the 252-day rolling mean tier (YoY tier trend shift)."""
    base = _tier_mean_252(exchange_tier)
    return base - base.shift(_TD_YEAR)


def lsr_drv2_005_tier_max_252d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 252-day rolling maximum tier."""
    base = _tier_max_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_006_tier_zscore_252d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 252-day z-scored tier."""
    base = _tier_zscore_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_007_tier_cumday_252d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 252-day cumulative tier-day score."""
    base = _tier_cumday_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_008_tier_ewm63_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the EWM(63) smoothed tier."""
    base = _tier_ewm63(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_009_notice_fraction_63d_21d_diff(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the 63-day rolling notice fraction (notice onset acceleration)."""
    base = _notice_fraction_63(delist_notice)
    return base - base.shift(_TD_MO)


def lsr_drv2_010_notice_fraction_63d_63d_diff(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 63-day rolling notice fraction."""
    base = _notice_fraction_63(delist_notice)
    return base - base.shift(_TD_QTR)


def lsr_drv2_011_notice_fraction_252d_63d_diff(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 252-day rolling notice fraction."""
    base = _notice_fraction_252(delist_notice)
    return base - base.shift(_TD_QTR)


def lsr_drv2_012_notice_fraction_252d_252d_diff(delist_notice: pd.Series) -> pd.Series:
    """252-day change in the 252-day rolling notice fraction (YoY notice acceleration)."""
    base = _notice_fraction_252(delist_notice)
    return base - base.shift(_TD_YEAR)


def lsr_drv2_013_notice_days_252d_63d_diff(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the rolling 252-day notice day count."""
    base = _notice_days_252(delist_notice)
    return base - base.shift(_TD_QTR)


def lsr_drv2_014_notice_streak_21d_diff(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the current delist-notice streak length."""
    base = _notice_streak(delist_notice)
    return base - base.shift(_TD_MO)


def lsr_drv2_015_sub1_fraction_63d_21d_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 63-day sub-$1 fraction (short-term sub-$1 acceleration)."""
    base = _sub1_fraction_63(closeunadj)
    return base - base.shift(_TD_MO)


def lsr_drv2_016_sub1_fraction_63d_63d_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 63-day sub-$1 fraction."""
    base = _sub1_fraction_63(closeunadj)
    return base - base.shift(_TD_QTR)


def lsr_drv2_017_sub1_fraction_252d_63d_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 252-day sub-$1 fraction."""
    base = _sub1_fraction_252(closeunadj)
    return base - base.shift(_TD_QTR)


def lsr_drv2_018_sub1_fraction_252d_252d_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the 252-day sub-$1 fraction (YoY sub-$1 acceleration)."""
    base = _sub1_fraction_252(closeunadj)
    return base - base.shift(_TD_YEAR)


def lsr_drv2_019_sub1_days_252d_63d_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the rolling 252-day count of sub-$1 days."""
    base = _sub1_days_252(closeunadj)
    return base - base.shift(_TD_QTR)


def lsr_drv2_020_close_drawdown_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day change in the 252-day price drawdown (drawdown acceleration)."""
    base = _close_drawdown_252(close)
    return base - base.shift(_TD_MO)


def lsr_drv2_021_close_drawdown_252d_63d_diff(close: pd.Series) -> pd.Series:
    """63-day change in the 252-day price drawdown."""
    base = _close_drawdown_252(close)
    return base - base.shift(_TD_QTR)


def lsr_drv2_022_distress_score_ewm63_21d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """21-day change in the EWM(63) combined distress score."""
    base = _ewm_mean(_distress_score(exchange_tier, delist_notice, closeunadj), _TD_QTR)
    return base - base.shift(_TD_MO)


def lsr_drv2_023_distress_score_ewm252_63d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """63-day change in the EWM(252) combined distress score."""
    base = _ewm_mean(_distress_score(exchange_tier, delist_notice, closeunadj), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def lsr_drv2_024_tier_mean_63_slope(exchange_tier: pd.Series) -> pd.Series:
    """
    Rolling 63-day OLS slope of the 63-day mean tier series.
    Captures the rate at which tier trend is worsening.
    """
    base = _tier_mean_63(exchange_tier)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def lsr_drv2_025_notice_fraction_63_ewm_diff(delist_notice: pd.Series) -> pd.Series:
    """
    63-day notice fraction minus its own EWM(252).
    Measures whether recent notice intensity is accelerating beyond long-run trend.
    """
    base = _notice_fraction_63(delist_notice)
    ewm  = _ewm_mean(base, _TD_YEAR)
    return base - ewm


# ── Additional base helpers for new 2nd-derivative features ──────────────────

def _tier_mean_126(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_mean(exchange_tier.astype(float), _TD_2Q)


def _tier_ewm21(exchange_tier: pd.Series) -> pd.Series:
    return _ewm_mean(exchange_tier.astype(float), _TD_MO)


def _tier_std_63(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_std(exchange_tier.astype(float), _TD_QTR)


def _tier_std_252(exchange_tier: pd.Series) -> pd.Series:
    return _rolling_std(exchange_tier.astype(float), _TD_YEAR)


def _notice_fraction_21(delist_notice: pd.Series) -> pd.Series:
    return _rolling_mean(delist_notice.astype(float), _TD_MO)


def _notice_fraction_126(delist_notice: pd.Series) -> pd.Series:
    return _rolling_mean(delist_notice.astype(float), _TD_2Q)


def _notice_days_63(delist_notice: pd.Series) -> pd.Series:
    return _rolling_sum(delist_notice.astype(float), _TD_QTR)


def _notice_ewm63(delist_notice: pd.Series) -> pd.Series:
    return _ewm_mean(delist_notice.astype(float), _TD_QTR)


def _sub1_fraction_126(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_2Q)


def _sub2_fraction_63(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_QTR)


def _sub2_fraction_252(closeunadj: pd.Series) -> pd.Series:
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_YEAR)


def _close_drawdown_504(close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_2Y)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def _close_drawdown_126(close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_2Q)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def _tier_pct_rank_252(exchange_tier: pd.Series) -> pd.Series:
    return exchange_tier.astype(float).rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def _distress_score_v2(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    return exchange_tier.astype(float) + 2.0 * delist_notice.astype(float)


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def lsr_drv2_026_tier_mean_126d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 126-day rolling mean tier (half-year tier acceleration)."""
    base = _tier_mean_126(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_027_tier_mean_126d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 126-day rolling mean tier."""
    base = _tier_mean_126(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_028_tier_ewm21_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in EWM(21) smoothed tier (short-term tier impulse)."""
    base = _tier_ewm21(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_029_tier_ewm21_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in EWM(21) smoothed tier."""
    base = _tier_ewm21(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_030_tier_std_63d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in 63-day tier standard deviation (volatility acceleration)."""
    base = _tier_std_63(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_031_tier_std_252d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in 252-day tier standard deviation."""
    base = _tier_std_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_032_tier_pct_rank_252d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 252-day tier percentile rank."""
    base = _tier_pct_rank_252(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_033_tier_pct_rank_252d_63d_diff(exchange_tier: pd.Series) -> pd.Series:
    """63-day change in the 252-day tier percentile rank."""
    base = _tier_pct_rank_252(exchange_tier)
    return base - base.shift(_TD_QTR)


def lsr_drv2_034_tier_mean_63d_5d_diff(exchange_tier: pd.Series) -> pd.Series:
    """5-day change in the 63-day rolling mean tier (weekly tier impulse)."""
    base = _tier_mean_63(exchange_tier)
    return base - base.shift(_TD_WK)


def lsr_drv2_035_tier_cumday_252d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 252-day cumulative tier-day score."""
    base = _tier_cumday_252(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_036_notice_fraction_21d_5d_diff(delist_notice: pd.Series) -> pd.Series:
    """5-day change in the 21-day rolling notice fraction (weekly notice impulse)."""
    base = _notice_fraction_21(delist_notice)
    return base - base.shift(_TD_WK)


def lsr_drv2_037_notice_fraction_21d_21d_diff(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the 21-day rolling notice fraction."""
    base = _notice_fraction_21(delist_notice)
    return base - base.shift(_TD_MO)


def lsr_drv2_038_notice_fraction_126d_63d_diff(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the 126-day rolling notice fraction."""
    base = _notice_fraction_126(delist_notice)
    return base - base.shift(_TD_QTR)


def lsr_drv2_039_notice_fraction_126d_21d_diff(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the 126-day rolling notice fraction."""
    base = _notice_fraction_126(delist_notice)
    return base - base.shift(_TD_MO)


def lsr_drv2_040_notice_days_63d_21d_diff(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the rolling 63-day notice day count."""
    base = _notice_days_63(delist_notice)
    return base - base.shift(_TD_MO)


def lsr_drv2_041_notice_ewm63_21d_diff(delist_notice: pd.Series) -> pd.Series:
    """21-day change in the EWM(63)-smoothed notice flag."""
    base = _notice_ewm63(delist_notice)
    return base - base.shift(_TD_MO)


def lsr_drv2_042_notice_ewm63_63d_diff(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the EWM(63)-smoothed notice flag."""
    base = _notice_ewm63(delist_notice)
    return base - base.shift(_TD_QTR)


def lsr_drv2_043_notice_streak_63d_diff(delist_notice: pd.Series) -> pd.Series:
    """63-day change in the current delist-notice streak length."""
    base = _notice_streak(delist_notice)
    return base - base.shift(_TD_QTR)


def lsr_drv2_044_sub1_fraction_21d_5d_diff(closeunadj: pd.Series) -> pd.Series:
    """5-day change in the 21-day sub-$1 fraction (weekly sub-$1 impulse)."""
    base = _rolling_mean((closeunadj < 1.0).astype(float), _TD_MO)
    return base - base.shift(_TD_WK)


def lsr_drv2_045_sub1_fraction_126d_63d_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 126-day sub-$1 fraction."""
    base = _sub1_fraction_126(closeunadj)
    return base - base.shift(_TD_QTR)


def lsr_drv2_046_sub1_fraction_126d_21d_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 126-day sub-$1 fraction."""
    base = _sub1_fraction_126(closeunadj)
    return base - base.shift(_TD_MO)


def lsr_drv2_047_sub2_fraction_63d_21d_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the 63-day sub-$2 fraction."""
    base = _sub2_fraction_63(closeunadj)
    return base - base.shift(_TD_MO)


def lsr_drv2_048_sub2_fraction_252d_63d_diff(closeunadj: pd.Series) -> pd.Series:
    """63-day change in the 252-day sub-$2 fraction."""
    base = _sub2_fraction_252(closeunadj)
    return base - base.shift(_TD_QTR)


def lsr_drv2_049_sub1_days_252d_21d_diff(closeunadj: pd.Series) -> pd.Series:
    """21-day change in the rolling 252-day count of sub-$1 days."""
    base = _sub1_days_252(closeunadj)
    return base - base.shift(_TD_MO)


def lsr_drv2_050_close_drawdown_504d_63d_diff(close: pd.Series) -> pd.Series:
    """63-day change in the 504-day price drawdown."""
    base = _close_drawdown_504(close)
    return base - base.shift(_TD_QTR)


def lsr_drv2_051_close_drawdown_504d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day change in the 504-day price drawdown."""
    base = _close_drawdown_504(close)
    return base - base.shift(_TD_MO)


def lsr_drv2_052_close_drawdown_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day change in the 126-day price drawdown."""
    base = _close_drawdown_126(close)
    return base - base.shift(_TD_MO)


def lsr_drv2_053_close_drawdown_126d_63d_diff(close: pd.Series) -> pd.Series:
    """63-day change in the 126-day price drawdown."""
    base = _close_drawdown_126(close)
    return base - base.shift(_TD_QTR)


def lsr_drv2_054_close_drawdown_252d_252d_diff(close: pd.Series) -> pd.Series:
    """252-day change in the 252-day price drawdown (YoY drawdown shift)."""
    base = _close_drawdown_252(close)
    return base - base.shift(_TD_YEAR)


def lsr_drv2_055_distress_score_v2_ewm63_21d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """21-day change in EWM(63) of (tier + 2*notice) score."""
    base = _ewm_mean(_distress_score_v2(exchange_tier, delist_notice), _TD_QTR)
    return base - base.shift(_TD_MO)


def lsr_drv2_056_distress_score_v2_ewm63_63d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """63-day change in EWM(63) of (tier + 2*notice) score."""
    base = _ewm_mean(_distress_score_v2(exchange_tier, delist_notice), _TD_QTR)
    return base - base.shift(_TD_QTR)


def lsr_drv2_057_distress_score_ewm63_63d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """63-day change in the EWM(63) combined distress score."""
    base = _ewm_mean(_distress_score(exchange_tier, delist_notice, closeunadj), _TD_QTR)
    return base - base.shift(_TD_QTR)


def lsr_drv2_058_distress_score_ewm252_21d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """21-day change in the EWM(252) combined distress score."""
    base = _ewm_mean(_distress_score(exchange_tier, delist_notice, closeunadj), _TD_YEAR)
    return base - base.shift(_TD_MO)


def lsr_drv2_059_tier_mean_63d_slope_21(exchange_tier: pd.Series) -> pd.Series:
    """
    Rolling 21-day OLS slope of the 63-day mean tier series (short-window slope).
    """
    base = _tier_mean_63(exchange_tier)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return base.rolling(_TD_MO, min_periods=max(2, _TD_MO // 4)).apply(_slope, raw=True)


def lsr_drv2_060_notice_fraction_252d_slope(delist_notice: pd.Series) -> pd.Series:
    """
    Rolling 63-day OLS slope of the 252-day notice fraction series.
    """
    base = _notice_fraction_252(delist_notice)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def lsr_drv2_061_sub1_fraction_252d_slope(closeunadj: pd.Series) -> pd.Series:
    """
    Rolling 63-day OLS slope of the 252-day sub-$1 fraction series.
    """
    base = _sub1_fraction_252(closeunadj)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def lsr_drv2_062_close_drawdown_252d_slope(close: pd.Series) -> pd.Series:
    """
    Rolling 63-day OLS slope of the 252-day price drawdown series.
    """
    base = _close_drawdown_252(close)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def lsr_drv2_063_tier_mean_252d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 252-day rolling mean tier."""
    base = _tier_mean_252(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_064_tier_max_252d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 252-day rolling maximum tier."""
    base = _tier_max_252(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_065_tier_zscore_252d_21d_diff(exchange_tier: pd.Series) -> pd.Series:
    """21-day change in the 252-day z-scored tier."""
    base = _tier_zscore_252(exchange_tier)
    return base - base.shift(_TD_MO)


def lsr_drv2_066_tier_zscore_252d_252d_diff(exchange_tier: pd.Series) -> pd.Series:
    """252-day change in the 252-day z-scored tier (YoY zscore shift)."""
    base = _tier_zscore_252(exchange_tier)
    return base - base.shift(_TD_YEAR)


def lsr_drv2_067_notice_fraction_63d_252d_diff(delist_notice: pd.Series) -> pd.Series:
    """252-day change in the 63-day rolling notice fraction (YoY short-frac shift)."""
    base = _notice_fraction_63(delist_notice)
    return base - base.shift(_TD_YEAR)


def lsr_drv2_068_sub1_fraction_63d_252d_diff(closeunadj: pd.Series) -> pd.Series:
    """252-day change in the 63-day sub-$1 fraction (YoY short sub-$1 shift)."""
    base = _sub1_fraction_63(closeunadj)
    return base - base.shift(_TD_YEAR)


def lsr_drv2_069_tier_mean_63_ewm_diff(exchange_tier: pd.Series) -> pd.Series:
    """63d mean tier minus its own EWM(252) — long-term tier trend deviation."""
    base = _tier_mean_63(exchange_tier)
    ewm  = _ewm_mean(base, _TD_YEAR)
    return base - ewm


def lsr_drv2_070_notice_fraction_21_ewm_diff(delist_notice: pd.Series) -> pd.Series:
    """21d notice fraction minus its own EWM(63) — short-term notice deviation."""
    base = _notice_fraction_21(delist_notice)
    ewm  = _ewm_mean(base, _TD_QTR)
    return base - ewm


def lsr_drv2_071_sub1_fraction_63_ewm252_diff(closeunadj: pd.Series) -> pd.Series:
    """63d sub-$1 fraction minus its EWM(252) — long-term sub-$1 trend deviation."""
    base = _sub1_fraction_63(closeunadj)
    ewm  = _ewm_mean(base, _TD_YEAR)
    return base - ewm


def lsr_drv2_072_close_drawdown_252_ewm_diff(close: pd.Series) -> pd.Series:
    """252d drawdown minus its EWM(63) — drawdown deviation from medium-term trend."""
    base = _close_drawdown_252(close)
    ewm  = _ewm_mean(base, _TD_QTR)
    return base - ewm


def lsr_drv2_073_distress_score_v2_21d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """21-day change in raw (tier + 2*notice) distress score."""
    base = _distress_score_v2(exchange_tier, delist_notice)
    return base - base.shift(_TD_MO)


def lsr_drv2_074_distress_score_v2_63d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """63-day change in raw (tier + 2*notice) distress score."""
    base = _distress_score_v2(exchange_tier, delist_notice)
    return base - base.shift(_TD_QTR)


def lsr_drv2_075_distress_score_full_63d_diff(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """63-day change in raw full distress score (tier + 2*notice + 3*sub1)."""
    base = _distress_score(exchange_tier, delist_notice, closeunadj)
    return base - base.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

LISTING_STATUS_RISK_REGISTRY_2ND_DERIVATIVES = {
    "lsr_drv2_001_tier_mean_63d_21d_diff":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_001_tier_mean_63d_21d_diff},
    "lsr_drv2_002_tier_mean_63d_63d_diff":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_002_tier_mean_63d_63d_diff},
    "lsr_drv2_003_tier_mean_252d_63d_diff":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_003_tier_mean_252d_63d_diff},
    "lsr_drv2_004_tier_mean_252d_252d_diff":        {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_004_tier_mean_252d_252d_diff},
    "lsr_drv2_005_tier_max_252d_63d_diff":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_005_tier_max_252d_63d_diff},
    "lsr_drv2_006_tier_zscore_252d_63d_diff":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_006_tier_zscore_252d_63d_diff},
    "lsr_drv2_007_tier_cumday_252d_63d_diff":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_007_tier_cumday_252d_63d_diff},
    "lsr_drv2_008_tier_ewm63_21d_diff":             {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_008_tier_ewm63_21d_diff},
    "lsr_drv2_009_notice_fraction_63d_21d_diff":    {"inputs": ["delist_notice"],                                 "func": lsr_drv2_009_notice_fraction_63d_21d_diff},
    "lsr_drv2_010_notice_fraction_63d_63d_diff":    {"inputs": ["delist_notice"],                                 "func": lsr_drv2_010_notice_fraction_63d_63d_diff},
    "lsr_drv2_011_notice_fraction_252d_63d_diff":   {"inputs": ["delist_notice"],                                 "func": lsr_drv2_011_notice_fraction_252d_63d_diff},
    "lsr_drv2_012_notice_fraction_252d_252d_diff":  {"inputs": ["delist_notice"],                                 "func": lsr_drv2_012_notice_fraction_252d_252d_diff},
    "lsr_drv2_013_notice_days_252d_63d_diff":       {"inputs": ["delist_notice"],                                 "func": lsr_drv2_013_notice_days_252d_63d_diff},
    "lsr_drv2_014_notice_streak_21d_diff":          {"inputs": ["delist_notice"],                                 "func": lsr_drv2_014_notice_streak_21d_diff},
    "lsr_drv2_015_sub1_fraction_63d_21d_diff":      {"inputs": ["closeunadj"],                                    "func": lsr_drv2_015_sub1_fraction_63d_21d_diff},
    "lsr_drv2_016_sub1_fraction_63d_63d_diff":      {"inputs": ["closeunadj"],                                    "func": lsr_drv2_016_sub1_fraction_63d_63d_diff},
    "lsr_drv2_017_sub1_fraction_252d_63d_diff":     {"inputs": ["closeunadj"],                                    "func": lsr_drv2_017_sub1_fraction_252d_63d_diff},
    "lsr_drv2_018_sub1_fraction_252d_252d_diff":    {"inputs": ["closeunadj"],                                    "func": lsr_drv2_018_sub1_fraction_252d_252d_diff},
    "lsr_drv2_019_sub1_days_252d_63d_diff":         {"inputs": ["closeunadj"],                                    "func": lsr_drv2_019_sub1_days_252d_63d_diff},
    "lsr_drv2_020_close_drawdown_252d_21d_diff":    {"inputs": ["close"],                                         "func": lsr_drv2_020_close_drawdown_252d_21d_diff},
    "lsr_drv2_021_close_drawdown_252d_63d_diff":    {"inputs": ["close"],                                         "func": lsr_drv2_021_close_drawdown_252d_63d_diff},
    "lsr_drv2_022_distress_score_ewm63_21d_diff":   {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv2_022_distress_score_ewm63_21d_diff},
    "lsr_drv2_023_distress_score_ewm252_63d_diff":  {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv2_023_distress_score_ewm252_63d_diff},
    "lsr_drv2_024_tier_mean_63_slope":              {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_024_tier_mean_63_slope},
    "lsr_drv2_025_notice_fraction_63_ewm_diff":     {"inputs": ["delist_notice"],                                 "func": lsr_drv2_025_notice_fraction_63_ewm_diff},
    "lsr_drv2_026_tier_mean_126d_63d_diff":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_026_tier_mean_126d_63d_diff},
    "lsr_drv2_027_tier_mean_126d_21d_diff":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_027_tier_mean_126d_21d_diff},
    "lsr_drv2_028_tier_ewm21_21d_diff":             {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_028_tier_ewm21_21d_diff},
    "lsr_drv2_029_tier_ewm21_63d_diff":             {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_029_tier_ewm21_63d_diff},
    "lsr_drv2_030_tier_std_63d_21d_diff":           {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_030_tier_std_63d_21d_diff},
    "lsr_drv2_031_tier_std_252d_63d_diff":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_031_tier_std_252d_63d_diff},
    "lsr_drv2_032_tier_pct_rank_252d_21d_diff":     {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_032_tier_pct_rank_252d_21d_diff},
    "lsr_drv2_033_tier_pct_rank_252d_63d_diff":     {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_033_tier_pct_rank_252d_63d_diff},
    "lsr_drv2_034_tier_mean_63d_5d_diff":           {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_034_tier_mean_63d_5d_diff},
    "lsr_drv2_035_tier_cumday_252d_21d_diff":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_035_tier_cumday_252d_21d_diff},
    "lsr_drv2_036_notice_fraction_21d_5d_diff":     {"inputs": ["delist_notice"],                                 "func": lsr_drv2_036_notice_fraction_21d_5d_diff},
    "lsr_drv2_037_notice_fraction_21d_21d_diff":    {"inputs": ["delist_notice"],                                 "func": lsr_drv2_037_notice_fraction_21d_21d_diff},
    "lsr_drv2_038_notice_fraction_126d_63d_diff":   {"inputs": ["delist_notice"],                                 "func": lsr_drv2_038_notice_fraction_126d_63d_diff},
    "lsr_drv2_039_notice_fraction_126d_21d_diff":   {"inputs": ["delist_notice"],                                 "func": lsr_drv2_039_notice_fraction_126d_21d_diff},
    "lsr_drv2_040_notice_days_63d_21d_diff":        {"inputs": ["delist_notice"],                                 "func": lsr_drv2_040_notice_days_63d_21d_diff},
    "lsr_drv2_041_notice_ewm63_21d_diff":           {"inputs": ["delist_notice"],                                 "func": lsr_drv2_041_notice_ewm63_21d_diff},
    "lsr_drv2_042_notice_ewm63_63d_diff":           {"inputs": ["delist_notice"],                                 "func": lsr_drv2_042_notice_ewm63_63d_diff},
    "lsr_drv2_043_notice_streak_63d_diff":          {"inputs": ["delist_notice"],                                 "func": lsr_drv2_043_notice_streak_63d_diff},
    "lsr_drv2_044_sub1_fraction_21d_5d_diff":       {"inputs": ["closeunadj"],                                    "func": lsr_drv2_044_sub1_fraction_21d_5d_diff},
    "lsr_drv2_045_sub1_fraction_126d_63d_diff":     {"inputs": ["closeunadj"],                                    "func": lsr_drv2_045_sub1_fraction_126d_63d_diff},
    "lsr_drv2_046_sub1_fraction_126d_21d_diff":     {"inputs": ["closeunadj"],                                    "func": lsr_drv2_046_sub1_fraction_126d_21d_diff},
    "lsr_drv2_047_sub2_fraction_63d_21d_diff":      {"inputs": ["closeunadj"],                                    "func": lsr_drv2_047_sub2_fraction_63d_21d_diff},
    "lsr_drv2_048_sub2_fraction_252d_63d_diff":     {"inputs": ["closeunadj"],                                    "func": lsr_drv2_048_sub2_fraction_252d_63d_diff},
    "lsr_drv2_049_sub1_days_252d_21d_diff":         {"inputs": ["closeunadj"],                                    "func": lsr_drv2_049_sub1_days_252d_21d_diff},
    "lsr_drv2_050_close_drawdown_504d_63d_diff":    {"inputs": ["close"],                                         "func": lsr_drv2_050_close_drawdown_504d_63d_diff},
    "lsr_drv2_051_close_drawdown_504d_21d_diff":    {"inputs": ["close"],                                         "func": lsr_drv2_051_close_drawdown_504d_21d_diff},
    "lsr_drv2_052_close_drawdown_126d_21d_diff":    {"inputs": ["close"],                                         "func": lsr_drv2_052_close_drawdown_126d_21d_diff},
    "lsr_drv2_053_close_drawdown_126d_63d_diff":    {"inputs": ["close"],                                         "func": lsr_drv2_053_close_drawdown_126d_63d_diff},
    "lsr_drv2_054_close_drawdown_252d_252d_diff":   {"inputs": ["close"],                                         "func": lsr_drv2_054_close_drawdown_252d_252d_diff},
    "lsr_drv2_055_distress_score_v2_ewm63_21d_diff": {"inputs": ["exchange_tier", "delist_notice"],              "func": lsr_drv2_055_distress_score_v2_ewm63_21d_diff},
    "lsr_drv2_056_distress_score_v2_ewm63_63d_diff": {"inputs": ["exchange_tier", "delist_notice"],              "func": lsr_drv2_056_distress_score_v2_ewm63_63d_diff},
    "lsr_drv2_057_distress_score_ewm63_63d_diff":   {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv2_057_distress_score_ewm63_63d_diff},
    "lsr_drv2_058_distress_score_ewm252_21d_diff":  {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv2_058_distress_score_ewm252_21d_diff},
    "lsr_drv2_059_tier_mean_63d_slope_21":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_059_tier_mean_63d_slope_21},
    "lsr_drv2_060_notice_fraction_252d_slope":      {"inputs": ["delist_notice"],                                 "func": lsr_drv2_060_notice_fraction_252d_slope},
    "lsr_drv2_061_sub1_fraction_252d_slope":        {"inputs": ["closeunadj"],                                    "func": lsr_drv2_061_sub1_fraction_252d_slope},
    "lsr_drv2_062_close_drawdown_252d_slope":       {"inputs": ["close"],                                         "func": lsr_drv2_062_close_drawdown_252d_slope},
    "lsr_drv2_063_tier_mean_252d_21d_diff":         {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_063_tier_mean_252d_21d_diff},
    "lsr_drv2_064_tier_max_252d_21d_diff":          {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_064_tier_max_252d_21d_diff},
    "lsr_drv2_065_tier_zscore_252d_21d_diff":       {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_065_tier_zscore_252d_21d_diff},
    "lsr_drv2_066_tier_zscore_252d_252d_diff":      {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_066_tier_zscore_252d_252d_diff},
    "lsr_drv2_067_notice_fraction_63d_252d_diff":   {"inputs": ["delist_notice"],                                 "func": lsr_drv2_067_notice_fraction_63d_252d_diff},
    "lsr_drv2_068_sub1_fraction_63d_252d_diff":     {"inputs": ["closeunadj"],                                    "func": lsr_drv2_068_sub1_fraction_63d_252d_diff},
    "lsr_drv2_069_tier_mean_63_ewm_diff":           {"inputs": ["exchange_tier"],                                 "func": lsr_drv2_069_tier_mean_63_ewm_diff},
    "lsr_drv2_070_notice_fraction_21_ewm_diff":     {"inputs": ["delist_notice"],                                 "func": lsr_drv2_070_notice_fraction_21_ewm_diff},
    "lsr_drv2_071_sub1_fraction_63_ewm252_diff":    {"inputs": ["closeunadj"],                                    "func": lsr_drv2_071_sub1_fraction_63_ewm252_diff},
    "lsr_drv2_072_close_drawdown_252_ewm_diff":     {"inputs": ["close"],                                         "func": lsr_drv2_072_close_drawdown_252_ewm_diff},
    "lsr_drv2_073_distress_score_v2_21d_diff":      {"inputs": ["exchange_tier", "delist_notice"],               "func": lsr_drv2_073_distress_score_v2_21d_diff},
    "lsr_drv2_074_distress_score_v2_63d_diff":      {"inputs": ["exchange_tier", "delist_notice"],               "func": lsr_drv2_074_distress_score_v2_63d_diff},
    "lsr_drv2_075_distress_score_full_63d_diff":    {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_drv2_075_distress_score_full_63d_diff},
}
