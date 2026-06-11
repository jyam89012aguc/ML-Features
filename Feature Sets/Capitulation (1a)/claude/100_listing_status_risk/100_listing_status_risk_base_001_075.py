"""
100_listing_status_risk — Base Features 001-100
Domain: exchange-tier risk and delisting proximity for distressed US equities
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to a shared trading-day
index.  Status fields (exchange_tier, delist_notice) are forward-filled.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Trading-day constants: 1 year = 252 td, 1 quarter = 63 td,
1 month = 21 td, 1 week = 5 td.

Inputs
------
exchange_tier : daily ordinal — 1=NYSE/NASDAQ Global Select, 2=NASDAQ Global/
                Capital Market, 3=NYSE American/regional, 4=OTCQX/OTCQB,
                5=Pink/Expert Market.  Higher = lower-tier / more distressed.
delist_notice : binary (1.0/0.0) — 1 when a delisting or listing-deficiency
                notice is in effect.
closeunadj    : raw unadjusted daily close price (USD); sub-$1 is delisting-
                relevant under exchange minimum-bid rules.
close         : split/dividend-adjusted daily close price (USD).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _streak_length(binary: pd.Series) -> pd.Series:
    """Current consecutive run length of 1s; resets to 0 on any 0."""
    arr    = binary.fillna(0).values.astype(int)
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=binary.index)


def _days_since_last_one(binary: pd.Series) -> pd.Series:
    """Days elapsed since the most recent 1; NaN if never seen."""
    arr    = binary.fillna(0).values.astype(float)
    result = np.full(len(arr), np.nan)
    last   = np.nan
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = 0.0
        elif not np.isnan(last):
            last += 1.0
        result[i] = last
    return pd.Series(result, index=binary.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Exchange tier level, transitions, and tier averages ---

def lsr_001_exchange_tier_current(exchange_tier: pd.Series) -> pd.Series:
    """Current exchange tier ordinal (1-5); higher = more distressed."""
    return exchange_tier.astype(float)


def lsr_002_tier_is_otc(exchange_tier: pd.Series) -> pd.Series:
    """Binary: 1 if currently on OTC tier (tier >= 4), else 0."""
    return (exchange_tier >= 4).astype(float)


def lsr_003_tier_is_pink(exchange_tier: pd.Series) -> pd.Series:
    """Binary: 1 if currently on Pink/Expert Market (tier == 5), else 0."""
    return (exchange_tier == 5).astype(float)


def lsr_004_tier_downgrade_flag(exchange_tier: pd.Series) -> pd.Series:
    """Binary: 1 on any day where tier increased (moved to lower-tier exchange)."""
    return (exchange_tier > exchange_tier.shift(1)).astype(float)


def lsr_005_tier_upgrade_flag(exchange_tier: pd.Series) -> pd.Series:
    """Binary: 1 on any day where tier decreased (moved to higher-tier exchange)."""
    return (exchange_tier < exchange_tier.shift(1)).astype(float)


def lsr_006_tier_change_magnitude(exchange_tier: pd.Series) -> pd.Series:
    """Signed daily tier change (positive = downgrade, negative = upgrade)."""
    return (exchange_tier - exchange_tier.shift(1)).astype(float)


def lsr_007_tier_downgrades_21d(exchange_tier: pd.Series) -> pd.Series:
    """Count of tier downgrade events in trailing 21 trading days."""
    flag = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_MO)


def lsr_008_tier_downgrades_63d(exchange_tier: pd.Series) -> pd.Series:
    """Count of tier downgrade events in trailing 63 trading days."""
    flag = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def lsr_009_tier_downgrades_252d(exchange_tier: pd.Series) -> pd.Series:
    """Count of tier downgrade events in trailing 252 trading days."""
    flag = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def lsr_010_tier_downgrades_504d(exchange_tier: pd.Series) -> pd.Series:
    """Count of tier downgrade events in trailing 504 trading days."""
    flag = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def lsr_011_rolling_mean_tier_63d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 63-day mean exchange tier."""
    return _rolling_mean(exchange_tier.astype(float), _TD_QTR)


def lsr_012_rolling_mean_tier_252d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 252-day mean exchange tier."""
    return _rolling_mean(exchange_tier.astype(float), _TD_YEAR)


def lsr_013_rolling_max_tier_252d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 252-day maximum tier (worst tier visited)."""
    return _rolling_max(exchange_tier.astype(float), _TD_YEAR)


def lsr_014_rolling_max_tier_504d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 504-day maximum tier (worst tier visited over 2 years)."""
    return _rolling_max(exchange_tier.astype(float), _TD_2Y)


def lsr_015_tier_above_prior_year_avg(exchange_tier: pd.Series) -> pd.Series:
    """Current tier minus trailing-year mean tier (positive = deterioration)."""
    return exchange_tier.astype(float) - _rolling_mean(exchange_tier.astype(float), _TD_YEAR)


# --- Group B (016-030): Delist-notice presence, duration, count, fraction ---

def lsr_016_delist_notice_current(delist_notice: pd.Series) -> pd.Series:
    """Current delist-notice flag (1 if active, 0 otherwise)."""
    return delist_notice.astype(float)


def lsr_017_delist_notice_streak(delist_notice: pd.Series) -> pd.Series:
    """Consecutive days under an active delist notice (current spell length)."""
    return _streak_length(delist_notice)


def lsr_018_days_since_last_notice(delist_notice: pd.Series) -> pd.Series:
    """Days elapsed since the most recent delist-notice day; NaN if never."""
    return _days_since_last_one(delist_notice)


def lsr_019_notice_days_21d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 21 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_MO)


def lsr_020_notice_days_63d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 63 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_QTR)


def lsr_021_notice_days_126d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 126 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_2Q)


def lsr_022_notice_days_252d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 252 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_YEAR)


def lsr_023_notice_fraction_63d(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 63 days."""
    return _rolling_mean(delist_notice.astype(float), _TD_QTR)


def lsr_024_notice_fraction_252d(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 252 days."""
    return _rolling_mean(delist_notice.astype(float), _TD_YEAR)


def lsr_025_notice_fraction_504d(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 504 days."""
    return _rolling_mean(delist_notice.astype(float), _TD_2Y)


def lsr_026_notice_spell_count_252d(delist_notice: pd.Series) -> pd.Series:
    """Number of distinct delist-notice spells (onset events) in trailing 252 days."""
    onset = ((delist_notice == 1) & (delist_notice.shift(1).fillna(0) == 0)).astype(float)
    return _rolling_sum(onset, _TD_YEAR)


def lsr_027_notice_spell_count_504d(delist_notice: pd.Series) -> pd.Series:
    """Number of distinct delist-notice spells in trailing 504 days."""
    onset = ((delist_notice == 1) & (delist_notice.shift(1).fillna(0) == 0)).astype(float)
    return _rolling_sum(onset, _TD_2Y)


def lsr_028_notice_ewm_intensity(delist_notice: pd.Series) -> pd.Series:
    """EWM-smoothed delist-notice presence (span=63)."""
    return _ewm_mean(delist_notice.astype(float), _TD_QTR)


def lsr_029_notice_ewm_intensity_252(delist_notice: pd.Series) -> pd.Series:
    """EWM-smoothed delist-notice presence (span=252)."""
    return _ewm_mean(delist_notice.astype(float), _TD_YEAR)


def lsr_030_notice_expanding_fraction(delist_notice: pd.Series) -> pd.Series:
    """All-history expanding fraction of days under delist notice."""
    return delist_notice.astype(float).expanding(min_periods=1).mean()


# --- Group C (031-050): Sub-$1, sub-$2, sub-$5 nominal-price flags ---

def lsr_031_sub1_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $1.00 (below exchange minimum bid)."""
    return (closeunadj < 1.0).astype(float)


def lsr_032_sub2_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $2.00."""
    return (closeunadj < 2.0).astype(float)


def lsr_033_sub5_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $5.00 (penny-stock threshold)."""
    return (closeunadj < 5.0).astype(float)


def lsr_034_sub1_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days with unadjusted close below $1.00."""
    return _streak_length((closeunadj < 1.0).astype(float))


def lsr_035_sub2_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days with unadjusted close below $2.00."""
    return _streak_length((closeunadj < 2.0).astype(float))


def lsr_036_sub5_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days with unadjusted close below $5.00."""
    return _streak_length((closeunadj < 5.0).astype(float))


def lsr_037_sub1_days_21d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$1 days in trailing 21 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_MO)


def lsr_038_sub1_days_63d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$1 days in trailing 63 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_QTR)


def lsr_039_sub1_days_252d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$1 days in trailing 252 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_YEAR)


def lsr_040_sub1_fraction_63d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $1.00 in trailing 63 days."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_QTR)


def lsr_041_sub1_fraction_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $1.00 in trailing 252 days."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_YEAR)


def lsr_042_sub2_fraction_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $2.00 in trailing 252 days."""
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_YEAR)


def lsr_043_sub5_fraction_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $5.00 in trailing 252 days."""
    return _rolling_mean((closeunadj < 5.0).astype(float), _TD_YEAR)


def lsr_044_dist_to_1_dollar(closeunadj: pd.Series) -> pd.Series:
    """Distance (USD) from unadjusted close to $1.00 threshold (negative = below)."""
    return closeunadj - 1.0


def lsr_045_dist_to_1_dollar_pct(closeunadj: pd.Series) -> pd.Series:
    """Percentage distance from unadjusted close to $1.00 (negative = below threshold)."""
    return _safe_div(closeunadj - 1.0, closeunadj.replace(0, np.nan))


def lsr_046_sub1_longest_spell_252d(closeunadj: pd.Series) -> pd.Series:
    """Longest consecutive sub-$1 spell (in days) within the trailing 252-day window."""
    flag    = (closeunadj < 1.0).astype(float)
    streak  = _streak_length(flag)
    return _rolling_max(streak, _TD_YEAR)


def lsr_047_sub1_longest_spell_504d(closeunadj: pd.Series) -> pd.Series:
    """Longest consecutive sub-$1 spell within the trailing 504-day window."""
    flag   = (closeunadj < 1.0).astype(float)
    streak = _streak_length(flag)
    return _rolling_max(streak, _TD_2Y)


def lsr_048_days_since_last_sub1(closeunadj: pd.Series) -> pd.Series:
    """Days since the most recent sub-$1 close; NaN if never observed."""
    return _days_since_last_one((closeunadj < 1.0).astype(float))


def lsr_049_sub1_expanding_fraction(closeunadj: pd.Series) -> pd.Series:
    """All-history expanding fraction of sub-$1 days."""
    return (closeunadj < 1.0).astype(float).expanding(min_periods=1).mean()


def lsr_050_sub5_days_504d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$5 days in trailing 504 trading days."""
    return _rolling_sum((closeunadj < 5.0).astype(float), _TD_2Y)


# --- Group D (051-065): Combined distress, tier-notice interactions ---

def lsr_051_combined_distress_flag(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    """Binary: 1 when delist notice is active AND tier >= 3."""
    return ((delist_notice == 1) & (exchange_tier >= 3)).astype(float)


def lsr_052_combined_distress_severe(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    """Binary: 1 when delist notice active AND tier >= 4 (OTC or Pink)."""
    return ((delist_notice == 1) & (exchange_tier >= 4)).astype(float)


def lsr_053_notice_sub1_joint(delist_notice: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 when delist notice active AND unadjusted close < $1.00."""
    return ((delist_notice == 1) & (closeunadj < 1.0)).astype(float)


def lsr_054_tier_times_notice(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    """Interaction: tier ordinal multiplied by delist-notice flag."""
    return exchange_tier.astype(float) * delist_notice.astype(float)


def lsr_055_tier_plus_notice_score(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    """Additive distress score: exchange_tier + 2 * delist_notice."""
    return exchange_tier.astype(float) + 2.0 * delist_notice.astype(float)


def lsr_056_tier_x_sub1_flag(exchange_tier: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Interaction: tier ordinal multiplied by sub-$1 flag."""
    return exchange_tier.astype(float) * (closeunadj < 1.0).astype(float)


def lsr_057_notice_days_tier4plus_252d(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    """Days with active notice AND tier >= 4 in trailing 252 days."""
    joint = ((delist_notice == 1) & (exchange_tier >= 4)).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def lsr_058_tier4plus_days_252d(exchange_tier: pd.Series) -> pd.Series:
    """Count of days at OTC/Pink tier (>= 4) in trailing 252 days."""
    return _rolling_sum((exchange_tier >= 4).astype(float), _TD_YEAR)


def lsr_059_tier4plus_days_504d(exchange_tier: pd.Series) -> pd.Series:
    """Count of days at OTC/Pink tier (>= 4) in trailing 504 days."""
    return _rolling_sum((exchange_tier >= 4).astype(float), _TD_2Y)


def lsr_060_tier5_days_252d(exchange_tier: pd.Series) -> pd.Series:
    """Count of days at Pink/Expert Market (tier == 5) in trailing 252 days."""
    return _rolling_sum((exchange_tier == 5).astype(float), _TD_YEAR)


def lsr_061_tier5_expanding_fraction(exchange_tier: pd.Series) -> pd.Series:
    """All-history expanding fraction of days at Pink/Expert Market."""
    return (exchange_tier == 5).astype(float).expanding(min_periods=1).mean()


def lsr_062_tier_cumday_score_252d(exchange_tier: pd.Series) -> pd.Series:
    """Cumulative tier-day product over trailing 252 days (sum of daily tier values)."""
    return _rolling_sum(exchange_tier.astype(float), _TD_YEAR)


def lsr_063_tier_cumday_score_504d(exchange_tier: pd.Series) -> pd.Series:
    """Cumulative tier-day product over trailing 504 days."""
    return _rolling_sum(exchange_tier.astype(float), _TD_2Y)


def lsr_064_tier5_streak(exchange_tier: pd.Series) -> pd.Series:
    """Consecutive days at the lowest tier (tier == 5)."""
    return _streak_length((exchange_tier == 5).astype(float))


def lsr_065_days_since_tier_downgrade(exchange_tier: pd.Series) -> pd.Series:
    """Days elapsed since the last tier downgrade event; NaN if never."""
    downgrade = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _days_since_last_one(downgrade)


# --- Group E (066-075): Price drawdown interacted with tier/notice ---

def lsr_066_close_drawdown_1y(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 252-day rolling peak."""
    peak = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def lsr_067_close_drawdown_2y(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 504-day rolling peak."""
    peak = _rolling_max(close, _TD_2Y)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def lsr_068_close_drawdown_expanding(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from all-history expanding peak."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak.replace(0, np.nan))


def lsr_069_drawdown_x_tier(exchange_tier: pd.Series, close: pd.Series) -> pd.Series:
    """Interaction: 252-day price drawdown magnitude times current tier ordinal."""
    peak = _rolling_max(close, _TD_YEAR)
    dd   = _safe_div(close - peak, peak.replace(0, np.nan)).abs()
    return dd * exchange_tier.astype(float)


def lsr_070_drawdown_x_notice(delist_notice: pd.Series, close: pd.Series) -> pd.Series:
    """Interaction: 252-day price drawdown magnitude times delist-notice flag."""
    peak = _rolling_max(close, _TD_YEAR)
    dd   = _safe_div(close - peak, peak.replace(0, np.nan)).abs()
    return dd * delist_notice.astype(float)


def lsr_071_unadj_close_zscore_252d(closeunadj: pd.Series) -> pd.Series:
    """Z-score of unadjusted close within trailing 252-day window."""
    return _zscore_rolling(closeunadj, _TD_YEAR)


def lsr_072_unadj_close_pct_rank_252d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 252-day window."""
    return _rolling_rank_pct(closeunadj, _TD_YEAR)


def lsr_073_tier_ewm_span63(exchange_tier: pd.Series) -> pd.Series:
    """EWM-smoothed exchange tier (span=63); captures trend in tier trajectory."""
    return _ewm_mean(exchange_tier.astype(float), _TD_QTR)


def lsr_074_tier_ewm_span252(exchange_tier: pd.Series) -> pd.Series:
    """EWM-smoothed exchange tier (span=252)."""
    return _ewm_mean(exchange_tier.astype(float), _TD_YEAR)


def lsr_075_listing_distress_composite(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """
    Composite listing-distress score: z-scored tier (252d) + 2*notice_fraction_63d
    + sub-$1 fraction (63d).  Higher = more distressed.
    """
    z_tier    = _zscore_rolling(exchange_tier.astype(float), _TD_YEAR)
    nf        = _rolling_mean(delist_notice.astype(float), _TD_QTR)
    sub1_frac = _rolling_mean((closeunadj < 1.0).astype(float), _TD_QTR)
    return z_tier + 2.0 * nf + sub1_frac


# --- Group K (151-175): Additional tier/notice/price constructions ---

def lsr_151_tier_rolling_min_63d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 63-day minimum tier (best tier visited in the quarter)."""
    return _rolling_min(exchange_tier.astype(float), _TD_QTR)


def lsr_152_tier_range_252d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 252-day range of exchange tier (max minus min; volatility proxy)."""
    s = exchange_tier.astype(float)
    return _rolling_max(s, _TD_YEAR) - _rolling_min(s, _TD_YEAR)


def lsr_153_tier_range_63d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 63-day range of exchange tier."""
    s = exchange_tier.astype(float)
    return _rolling_max(s, _TD_QTR) - _rolling_min(s, _TD_QTR)


def lsr_154_tier_above_prior_qtr_avg(exchange_tier: pd.Series) -> pd.Series:
    """Current tier minus trailing 63-day mean tier (deviation from quarterly mean)."""
    return exchange_tier.astype(float) - _rolling_mean(exchange_tier.astype(float), _TD_QTR)


def lsr_155_tier_downgrade_rate_63d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of days with a tier downgrade event in trailing 63 days."""
    flag = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _rolling_mean(flag, _TD_QTR)


def lsr_156_tier_downgrade_rate_252d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of days with a tier downgrade event in trailing 252 days."""
    flag = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def lsr_157_tier3plus_days_252d(exchange_tier: pd.Series) -> pd.Series:
    """Count of days at tier >= 3 (mid/lower-tier) in trailing 252 days."""
    return _rolling_sum((exchange_tier >= 3).astype(float), _TD_YEAR)


def lsr_158_tier3plus_fraction_252d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of days at tier >= 3 in trailing 252 days."""
    return _rolling_mean((exchange_tier >= 3).astype(float), _TD_YEAR)


def lsr_159_tier4plus_fraction_63d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of days at OTC/Pink (tier >= 4) in trailing 63 days."""
    return _rolling_mean((exchange_tier >= 4).astype(float), _TD_QTR)


def lsr_160_tier5_fraction_252d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of days at Pink/Expert Market (tier == 5) in trailing 252 days."""
    return _rolling_mean((exchange_tier == 5).astype(float), _TD_YEAR)


def lsr_161_notice_days_504d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 504 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_2Y)


def lsr_162_notice_fraction_5y(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 1260 trading days (5 years)."""
    return _rolling_mean(delist_notice.astype(float), 1260)


def lsr_163_notice_vs_ewm21(delist_notice: pd.Series) -> pd.Series:
    """Delist-notice flag minus its EWM (span=21) — very short-term deviation."""
    n = delist_notice.astype(float)
    return n - _ewm_mean(n, _TD_MO)


def lsr_164_notice_streak_ewm21(delist_notice: pd.Series) -> pd.Series:
    """EWM(21)-smoothed delist-notice streak length."""
    return _ewm_mean(_streak_length(delist_notice), _TD_MO)


def lsr_165_closeunadj_pct_rank_504d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 504-day window."""
    return _rolling_rank_pct(closeunadj, _TD_2Y)


def lsr_166_closeunadj_ewm_span63(closeunadj: pd.Series) -> pd.Series:
    """EWM(63)-smoothed unadjusted close price."""
    return _ewm_mean(closeunadj, _TD_QTR)


def lsr_167_closeunadj_vs_ewm63(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its EWM(63) — short-term price deviation."""
    return closeunadj - _ewm_mean(closeunadj, _TD_QTR)


def lsr_168_sub1_ewm_intensity(closeunadj: pd.Series) -> pd.Series:
    """EWM(63)-smoothed sub-$1 flag (continuous measure of sub-dollar exposure)."""
    return _ewm_mean((closeunadj < 1.0).astype(float), _TD_QTR)


def lsr_169_sub2_ewm_intensity(closeunadj: pd.Series) -> pd.Series:
    """EWM(63)-smoothed sub-$2 flag."""
    return _ewm_mean((closeunadj < 2.0).astype(float), _TD_QTR)


def lsr_170_close_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of adjusted close within trailing 504-day window."""
    return _zscore_rolling(close, _TD_2Y)


def lsr_171_close_pct_rank_756d(close: pd.Series) -> pd.Series:
    """Percentile rank of adjusted close within trailing 756-day window."""
    return _rolling_rank_pct(close, _TD_3Y)


def lsr_172_close_drawdown_5y(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 1260-day (5-year) rolling peak."""
    peak = _rolling_max(close, 1260)
    return _safe_div(close - peak, peak.replace(0, np.nan))


def lsr_173_notice_sub2_joint(delist_notice: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 when delist notice active AND unadjusted close < $2.00."""
    return ((delist_notice == 1) & (closeunadj < 2.0)).astype(float)


def lsr_174_tier4plus_notice_fraction_252d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
) -> pd.Series:
    """Fraction of days with notice AND tier >= 4 in trailing 252 days."""
    joint = ((delist_notice == 1) & (exchange_tier >= 4)).astype(float)
    return _rolling_mean(joint, _TD_YEAR)


def lsr_175_distress_composite_v2(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Distress composite v2: EWM(63) tier zscore(252d) + 3*notice_fraction(63d)
    + 2*sub-$1 fraction(63d) + abs(drawdown_1y).  Higher = more distressed.
    """
    z_tier    = _zscore_rolling(exchange_tier.astype(float), _TD_YEAR)
    nf        = _rolling_mean(delist_notice.astype(float), _TD_QTR)
    sub1      = _rolling_mean((closeunadj < 1.0).astype(float), _TD_QTR)
    peak      = _rolling_max(close, _TD_YEAR)
    dd        = _safe_div(close - peak, peak.replace(0, np.nan)).abs()
    return _ewm_mean(z_tier, _TD_QTR) + 3.0 * nf + 2.0 * sub1 + dd


# ── Registry 001-075 ──────────────────────────────────────────────────────────

LISTING_STATUS_RISK_REGISTRY_001_075 = {
    "lsr_001_exchange_tier_current":       {"inputs": ["exchange_tier"],                              "func": lsr_001_exchange_tier_current},
    "lsr_002_tier_is_otc":                 {"inputs": ["exchange_tier"],                              "func": lsr_002_tier_is_otc},
    "lsr_003_tier_is_pink":                {"inputs": ["exchange_tier"],                              "func": lsr_003_tier_is_pink},
    "lsr_004_tier_downgrade_flag":         {"inputs": ["exchange_tier"],                              "func": lsr_004_tier_downgrade_flag},
    "lsr_005_tier_upgrade_flag":           {"inputs": ["exchange_tier"],                              "func": lsr_005_tier_upgrade_flag},
    "lsr_006_tier_change_magnitude":       {"inputs": ["exchange_tier"],                              "func": lsr_006_tier_change_magnitude},
    "lsr_007_tier_downgrades_21d":         {"inputs": ["exchange_tier"],                              "func": lsr_007_tier_downgrades_21d},
    "lsr_008_tier_downgrades_63d":         {"inputs": ["exchange_tier"],                              "func": lsr_008_tier_downgrades_63d},
    "lsr_009_tier_downgrades_252d":        {"inputs": ["exchange_tier"],                              "func": lsr_009_tier_downgrades_252d},
    "lsr_010_tier_downgrades_504d":        {"inputs": ["exchange_tier"],                              "func": lsr_010_tier_downgrades_504d},
    "lsr_011_rolling_mean_tier_63d":       {"inputs": ["exchange_tier"],                              "func": lsr_011_rolling_mean_tier_63d},
    "lsr_012_rolling_mean_tier_252d":      {"inputs": ["exchange_tier"],                              "func": lsr_012_rolling_mean_tier_252d},
    "lsr_013_rolling_max_tier_252d":       {"inputs": ["exchange_tier"],                              "func": lsr_013_rolling_max_tier_252d},
    "lsr_014_rolling_max_tier_504d":       {"inputs": ["exchange_tier"],                              "func": lsr_014_rolling_max_tier_504d},
    "lsr_015_tier_above_prior_year_avg":   {"inputs": ["exchange_tier"],                              "func": lsr_015_tier_above_prior_year_avg},
    "lsr_016_delist_notice_current":       {"inputs": ["delist_notice"],                              "func": lsr_016_delist_notice_current},
    "lsr_017_delist_notice_streak":        {"inputs": ["delist_notice"],                              "func": lsr_017_delist_notice_streak},
    "lsr_018_days_since_last_notice":      {"inputs": ["delist_notice"],                              "func": lsr_018_days_since_last_notice},
    "lsr_019_notice_days_21d":             {"inputs": ["delist_notice"],                              "func": lsr_019_notice_days_21d},
    "lsr_020_notice_days_63d":             {"inputs": ["delist_notice"],                              "func": lsr_020_notice_days_63d},
    "lsr_021_notice_days_126d":            {"inputs": ["delist_notice"],                              "func": lsr_021_notice_days_126d},
    "lsr_022_notice_days_252d":            {"inputs": ["delist_notice"],                              "func": lsr_022_notice_days_252d},
    "lsr_023_notice_fraction_63d":         {"inputs": ["delist_notice"],                              "func": lsr_023_notice_fraction_63d},
    "lsr_024_notice_fraction_252d":        {"inputs": ["delist_notice"],                              "func": lsr_024_notice_fraction_252d},
    "lsr_025_notice_fraction_504d":        {"inputs": ["delist_notice"],                              "func": lsr_025_notice_fraction_504d},
    "lsr_026_notice_spell_count_252d":     {"inputs": ["delist_notice"],                              "func": lsr_026_notice_spell_count_252d},
    "lsr_027_notice_spell_count_504d":     {"inputs": ["delist_notice"],                              "func": lsr_027_notice_spell_count_504d},
    "lsr_028_notice_ewm_intensity":        {"inputs": ["delist_notice"],                              "func": lsr_028_notice_ewm_intensity},
    "lsr_029_notice_ewm_intensity_252":    {"inputs": ["delist_notice"],                              "func": lsr_029_notice_ewm_intensity_252},
    "lsr_030_notice_expanding_fraction":   {"inputs": ["delist_notice"],                              "func": lsr_030_notice_expanding_fraction},
    "lsr_031_sub1_flag":                   {"inputs": ["closeunadj"],                                 "func": lsr_031_sub1_flag},
    "lsr_032_sub2_flag":                   {"inputs": ["closeunadj"],                                 "func": lsr_032_sub2_flag},
    "lsr_033_sub5_flag":                   {"inputs": ["closeunadj"],                                 "func": lsr_033_sub5_flag},
    "lsr_034_sub1_streak":                 {"inputs": ["closeunadj"],                                 "func": lsr_034_sub1_streak},
    "lsr_035_sub2_streak":                 {"inputs": ["closeunadj"],                                 "func": lsr_035_sub2_streak},
    "lsr_036_sub5_streak":                 {"inputs": ["closeunadj"],                                 "func": lsr_036_sub5_streak},
    "lsr_037_sub1_days_21d":               {"inputs": ["closeunadj"],                                 "func": lsr_037_sub1_days_21d},
    "lsr_038_sub1_days_63d":               {"inputs": ["closeunadj"],                                 "func": lsr_038_sub1_days_63d},
    "lsr_039_sub1_days_252d":              {"inputs": ["closeunadj"],                                 "func": lsr_039_sub1_days_252d},
    "lsr_040_sub1_fraction_63d":           {"inputs": ["closeunadj"],                                 "func": lsr_040_sub1_fraction_63d},
    "lsr_041_sub1_fraction_252d":          {"inputs": ["closeunadj"],                                 "func": lsr_041_sub1_fraction_252d},
    "lsr_042_sub2_fraction_252d":          {"inputs": ["closeunadj"],                                 "func": lsr_042_sub2_fraction_252d},
    "lsr_043_sub5_fraction_252d":          {"inputs": ["closeunadj"],                                 "func": lsr_043_sub5_fraction_252d},
    "lsr_044_dist_to_1_dollar":            {"inputs": ["closeunadj"],                                 "func": lsr_044_dist_to_1_dollar},
    "lsr_045_dist_to_1_dollar_pct":        {"inputs": ["closeunadj"],                                 "func": lsr_045_dist_to_1_dollar_pct},
    "lsr_046_sub1_longest_spell_252d":     {"inputs": ["closeunadj"],                                 "func": lsr_046_sub1_longest_spell_252d},
    "lsr_047_sub1_longest_spell_504d":     {"inputs": ["closeunadj"],                                 "func": lsr_047_sub1_longest_spell_504d},
    "lsr_048_days_since_last_sub1":        {"inputs": ["closeunadj"],                                 "func": lsr_048_days_since_last_sub1},
    "lsr_049_sub1_expanding_fraction":     {"inputs": ["closeunadj"],                                 "func": lsr_049_sub1_expanding_fraction},
    "lsr_050_sub5_days_504d":              {"inputs": ["closeunadj"],                                 "func": lsr_050_sub5_days_504d},
    "lsr_051_combined_distress_flag":      {"inputs": ["exchange_tier", "delist_notice"],             "func": lsr_051_combined_distress_flag},
    "lsr_052_combined_distress_severe":    {"inputs": ["exchange_tier", "delist_notice"],             "func": lsr_052_combined_distress_severe},
    "lsr_053_notice_sub1_joint":           {"inputs": ["delist_notice", "closeunadj"],                "func": lsr_053_notice_sub1_joint},
    "lsr_054_tier_times_notice":           {"inputs": ["exchange_tier", "delist_notice"],             "func": lsr_054_tier_times_notice},
    "lsr_055_tier_plus_notice_score":      {"inputs": ["exchange_tier", "delist_notice"],             "func": lsr_055_tier_plus_notice_score},
    "lsr_056_tier_x_sub1_flag":            {"inputs": ["exchange_tier", "closeunadj"],                "func": lsr_056_tier_x_sub1_flag},
    "lsr_057_notice_days_tier4plus_252d":  {"inputs": ["exchange_tier", "delist_notice"],             "func": lsr_057_notice_days_tier4plus_252d},
    "lsr_058_tier4plus_days_252d":         {"inputs": ["exchange_tier"],                              "func": lsr_058_tier4plus_days_252d},
    "lsr_059_tier4plus_days_504d":         {"inputs": ["exchange_tier"],                              "func": lsr_059_tier4plus_days_504d},
    "lsr_060_tier5_days_252d":             {"inputs": ["exchange_tier"],                              "func": lsr_060_tier5_days_252d},
    "lsr_061_tier5_expanding_fraction":    {"inputs": ["exchange_tier"],                              "func": lsr_061_tier5_expanding_fraction},
    "lsr_062_tier_cumday_score_252d":      {"inputs": ["exchange_tier"],                              "func": lsr_062_tier_cumday_score_252d},
    "lsr_063_tier_cumday_score_504d":      {"inputs": ["exchange_tier"],                              "func": lsr_063_tier_cumday_score_504d},
    "lsr_064_tier5_streak":                {"inputs": ["exchange_tier"],                              "func": lsr_064_tier5_streak},
    "lsr_065_days_since_tier_downgrade":   {"inputs": ["exchange_tier"],                              "func": lsr_065_days_since_tier_downgrade},
    "lsr_066_close_drawdown_1y":           {"inputs": ["close"],                                      "func": lsr_066_close_drawdown_1y},
    "lsr_067_close_drawdown_2y":           {"inputs": ["close"],                                      "func": lsr_067_close_drawdown_2y},
    "lsr_068_close_drawdown_expanding":    {"inputs": ["close"],                                      "func": lsr_068_close_drawdown_expanding},
    "lsr_069_drawdown_x_tier":             {"inputs": ["exchange_tier", "close"],                     "func": lsr_069_drawdown_x_tier},
    "lsr_070_drawdown_x_notice":           {"inputs": ["delist_notice", "close"],                     "func": lsr_070_drawdown_x_notice},
    "lsr_071_unadj_close_zscore_252d":     {"inputs": ["closeunadj"],                                 "func": lsr_071_unadj_close_zscore_252d},
    "lsr_072_unadj_close_pct_rank_252d":   {"inputs": ["closeunadj"],                                 "func": lsr_072_unadj_close_pct_rank_252d},
    "lsr_073_tier_ewm_span63":             {"inputs": ["exchange_tier"],                              "func": lsr_073_tier_ewm_span63},
    "lsr_074_tier_ewm_span252":            {"inputs": ["exchange_tier"],                              "func": lsr_074_tier_ewm_span252},
    "lsr_075_listing_distress_composite":  {"inputs": ["exchange_tier", "delist_notice", "closeunadj"], "func": lsr_075_listing_distress_composite},
    "lsr_151_tier_rolling_min_63d":        {"inputs": ["exchange_tier"],                                 "func": lsr_151_tier_rolling_min_63d},
    "lsr_152_tier_range_252d":             {"inputs": ["exchange_tier"],                                 "func": lsr_152_tier_range_252d},
    "lsr_153_tier_range_63d":              {"inputs": ["exchange_tier"],                                 "func": lsr_153_tier_range_63d},
    "lsr_154_tier_above_prior_qtr_avg":    {"inputs": ["exchange_tier"],                                 "func": lsr_154_tier_above_prior_qtr_avg},
    "lsr_155_tier_downgrade_rate_63d":     {"inputs": ["exchange_tier"],                                 "func": lsr_155_tier_downgrade_rate_63d},
    "lsr_156_tier_downgrade_rate_252d":    {"inputs": ["exchange_tier"],                                 "func": lsr_156_tier_downgrade_rate_252d},
    "lsr_157_tier3plus_days_252d":         {"inputs": ["exchange_tier"],                                 "func": lsr_157_tier3plus_days_252d},
    "lsr_158_tier3plus_fraction_252d":     {"inputs": ["exchange_tier"],                                 "func": lsr_158_tier3plus_fraction_252d},
    "lsr_159_tier4plus_fraction_63d":      {"inputs": ["exchange_tier"],                                 "func": lsr_159_tier4plus_fraction_63d},
    "lsr_160_tier5_fraction_252d":         {"inputs": ["exchange_tier"],                                 "func": lsr_160_tier5_fraction_252d},
    "lsr_161_notice_days_504d":            {"inputs": ["delist_notice"],                                 "func": lsr_161_notice_days_504d},
    "lsr_162_notice_fraction_5y":          {"inputs": ["delist_notice"],                                 "func": lsr_162_notice_fraction_5y},
    "lsr_163_notice_vs_ewm21":             {"inputs": ["delist_notice"],                                 "func": lsr_163_notice_vs_ewm21},
    "lsr_164_notice_streak_ewm21":         {"inputs": ["delist_notice"],                                 "func": lsr_164_notice_streak_ewm21},
    "lsr_165_closeunadj_pct_rank_504d":    {"inputs": ["closeunadj"],                                    "func": lsr_165_closeunadj_pct_rank_504d},
    "lsr_166_closeunadj_ewm_span63":       {"inputs": ["closeunadj"],                                    "func": lsr_166_closeunadj_ewm_span63},
    "lsr_167_closeunadj_vs_ewm63":         {"inputs": ["closeunadj"],                                    "func": lsr_167_closeunadj_vs_ewm63},
    "lsr_168_sub1_ewm_intensity":          {"inputs": ["closeunadj"],                                    "func": lsr_168_sub1_ewm_intensity},
    "lsr_169_sub2_ewm_intensity":          {"inputs": ["closeunadj"],                                    "func": lsr_169_sub2_ewm_intensity},
    "lsr_170_close_zscore_504d":           {"inputs": ["close"],                                         "func": lsr_170_close_zscore_504d},
    "lsr_171_close_pct_rank_756d":         {"inputs": ["close"],                                         "func": lsr_171_close_pct_rank_756d},
    "lsr_172_close_drawdown_5y":           {"inputs": ["close"],                                         "func": lsr_172_close_drawdown_5y},
    "lsr_173_notice_sub2_joint":           {"inputs": ["delist_notice", "closeunadj"],                   "func": lsr_173_notice_sub2_joint},
    "lsr_174_tier4plus_notice_fraction_252d": {"inputs": ["exchange_tier", "delist_notice"],             "func": lsr_174_tier4plus_notice_fraction_252d},
    "lsr_175_distress_composite_v2":       {"inputs": ["exchange_tier", "delist_notice", "closeunadj", "close"], "func": lsr_175_distress_composite_v2},
}
