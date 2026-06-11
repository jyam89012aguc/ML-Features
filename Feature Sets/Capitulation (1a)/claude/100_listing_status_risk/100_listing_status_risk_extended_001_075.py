"""
100_listing_status_risk — Extended Features 001-075
Domain: exchange-tier risk and delisting proximity — additional variants:
        finer sub-price thresholds, tier-dwell depth, notice/tier sequencing,
        gap windows, recovery-margin angles, and distress composites not
        covered by the base or derivative files.
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


def _onset(binary: pd.Series) -> pd.Series:
    """1 on day binary transitions 0 -> 1."""
    return ((binary == 1) & (binary.shift(1).fillna(0) == 0)).astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-014): Finer nominal-price thresholds and proximity ---

def lsr_ext_001_sub050_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $0.50 (deep penny-stock zone)."""
    return (closeunadj < 0.50).astype(float)


def lsr_ext_002_sub010_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $0.10 (sub-dime distress)."""
    return (closeunadj < 0.10).astype(float)


def lsr_ext_003_sub3_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $3.00."""
    return (closeunadj < 3.0).astype(float)


def lsr_ext_004_sub050_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days with unadjusted close below $0.50."""
    return _streak_length((closeunadj < 0.50).astype(float))


def lsr_ext_005_sub3_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days with unadjusted close below $3.00."""
    return _streak_length((closeunadj < 3.0).astype(float))


def lsr_ext_006_sub050_days_252d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$0.50 days in trailing 252 trading days."""
    return _rolling_sum((closeunadj < 0.50).astype(float), _TD_YEAR)


def lsr_ext_007_sub050_fraction_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $0.50 in trailing 252 days."""
    return _rolling_mean((closeunadj < 0.50).astype(float), _TD_YEAR)


def lsr_ext_008_sub3_fraction_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $3.00 in trailing 252 days."""
    return _rolling_mean((closeunadj < 3.0).astype(float), _TD_YEAR)


def lsr_ext_009_dist_to_1_dollar_log(closeunadj: pd.Series) -> pd.Series:
    """Log ratio of unadjusted close to the $1.00 minimum-bid threshold."""
    return np.log(closeunadj.clip(lower=_EPS) / 1.0)


def lsr_ext_010_dist_to_5_dollar_pct(closeunadj: pd.Series) -> pd.Series:
    """Percentage distance from unadjusted close to the $5.00 penny-stock threshold."""
    return _safe_div(closeunadj - 5.0, closeunadj.replace(0, np.nan))


def lsr_ext_011_sub1_days_756d(closeunadj: pd.Series) -> pd.Series:
    """Count of sub-$1 days in trailing 756 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_3Y)


def lsr_ext_012_sub1_fraction_756d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $1.00 in trailing 756 days."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_3Y)


def lsr_ext_013_sub1_fraction_21d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $1.00 in trailing 21 days (recent bid distress)."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_MO)


def lsr_ext_014_above_1_dollar_streak(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days unadjusted close held at or above $1.00 (compliance run)."""
    return _streak_length((closeunadj >= 1.0).astype(float))


# --- Group B (015-026): Sub-$1 compliance-window features ---

def lsr_ext_015_sub1_consec_30d_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 when sub-$1 streak has reached 30 trading days (deficiency-trigger zone)."""
    return (_streak_length((closeunadj < 1.0).astype(float)) >= 30).astype(float)


def lsr_ext_016_sub1_consec_180d_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 when sub-$1 streak has reached 180 trading days (cure-period exhaustion)."""
    return (_streak_length((closeunadj < 1.0).astype(float)) >= 180).astype(float)


def lsr_ext_017_sub1_streak_pct_rank_504d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of current sub-$1 streak within trailing 504-day window."""
    return _rolling_rank_pct(_streak_length((closeunadj < 1.0).astype(float)), _TD_2Y)


def lsr_ext_018_sub1_longest_spell_756d(closeunadj: pd.Series) -> pd.Series:
    """Longest consecutive sub-$1 spell within the trailing 756-day window."""
    return _rolling_max(_streak_length((closeunadj < 1.0).astype(float)), _TD_3Y)


def lsr_ext_019_sub1_spell_count_252d(closeunadj: pd.Series) -> pd.Series:
    """Number of distinct sub-$1 spells (onset events) in trailing 252 days."""
    return _rolling_sum(_onset((closeunadj < 1.0).astype(float)), _TD_YEAR)


def lsr_ext_020_sub1_spell_count_756d(closeunadj: pd.Series) -> pd.Series:
    """Number of distinct sub-$1 spells in trailing 756 days."""
    return _rolling_sum(_onset((closeunadj < 1.0).astype(float)), _TD_3Y)


def lsr_ext_021_sub1_ewm_intensity_63(closeunadj: pd.Series) -> pd.Series:
    """EWM (span=63) smoothed sub-$1 presence — recency-weighted bid distress."""
    return _ewm_mean((closeunadj < 1.0).astype(float), _TD_QTR)


def lsr_ext_022_sub1_ewm_intensity_252(closeunadj: pd.Series) -> pd.Series:
    """EWM (span=252) smoothed sub-$1 presence."""
    return _ewm_mean((closeunadj < 1.0).astype(float), _TD_YEAR)


def lsr_ext_023_sub1_fraction_63d_zscore_252d(closeunadj: pd.Series) -> pd.Series:
    """Z-score of the 63-day sub-$1 fraction within a 252-day rolling window."""
    frac = _rolling_mean((closeunadj < 1.0).astype(float), _TD_QTR)
    return _zscore_rolling(frac, _TD_YEAR)


def lsr_ext_024_days_since_above_1_dollar(closeunadj: pd.Series) -> pd.Series:
    """Days since the most recent close at or above $1.00; NaN if never above."""
    return _days_since_last_one((closeunadj >= 1.0).astype(float))


def lsr_ext_025_sub1_onset_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 on the exact day unadjusted close first drops below $1.00."""
    return _onset((closeunadj < 1.0).astype(float))


def lsr_ext_026_sub1_recovery_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 on the exact day unadjusted close reclaims $1.00 from below."""
    above = (closeunadj >= 1.0).astype(float)
    return _onset(above)


# --- Group C (027-040): Tier-dwell depth and tier-state variants ---

def lsr_ext_027_tier_ge3_flag(exchange_tier: pd.Series) -> pd.Series:
    """Binary: 1 if currently on tier 3 or worse (regional/OTC/Pink)."""
    return (exchange_tier >= 3).astype(float)


def lsr_ext_028_tier_ge3_streak(exchange_tier: pd.Series) -> pd.Series:
    """Consecutive trading days at tier 3 or worse."""
    return _streak_length((exchange_tier >= 3).astype(float))


def lsr_ext_029_tier_ge4_streak(exchange_tier: pd.Series) -> pd.Series:
    """Consecutive trading days at OTC/Pink tier (>= 4)."""
    return _streak_length((exchange_tier >= 4).astype(float))


def lsr_ext_030_tier_ge3_days_252d(exchange_tier: pd.Series) -> pd.Series:
    """Count of days at tier 3 or worse in trailing 252 days."""
    return _rolling_sum((exchange_tier >= 3).astype(float), _TD_YEAR)


def lsr_ext_031_tier_ge3_fraction_252d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days spent at tier 3 or worse."""
    return _rolling_mean((exchange_tier >= 3).astype(float), _TD_YEAR)


def lsr_ext_032_tier4plus_fraction_252d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days spent at OTC/Pink tier (>= 4)."""
    return _rolling_mean((exchange_tier >= 4).astype(float), _TD_YEAR)


def lsr_ext_033_tier5_fraction_252d(exchange_tier: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days spent at Pink/Expert Market (tier 5)."""
    return _rolling_mean((exchange_tier == 5).astype(float), _TD_YEAR)


def lsr_ext_034_tier_minus_min_252d(exchange_tier: pd.Series) -> pd.Series:
    """Current tier minus best (lowest) tier visited in trailing 252 days."""
    return exchange_tier.astype(float) - _rolling_min(exchange_tier.astype(float), _TD_YEAR)


def lsr_ext_035_tier_minus_min_504d(exchange_tier: pd.Series) -> pd.Series:
    """Current tier minus best (lowest) tier visited in trailing 504 days."""
    return exchange_tier.astype(float) - _rolling_min(exchange_tier.astype(float), _TD_2Y)


def lsr_ext_036_tier_at_504d_max_flag(exchange_tier: pd.Series) -> pd.Series:
    """Binary: 1 when current tier equals the worst tier visited in trailing 504 days."""
    return (exchange_tier.astype(float) >= _rolling_max(exchange_tier.astype(float), _TD_2Y) - _EPS).astype(float)


def lsr_ext_037_tier_rolling_max_756d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 756-day maximum tier (worst tier visited over 3 years)."""
    return _rolling_max(exchange_tier.astype(float), _TD_3Y)


def lsr_ext_038_tier_cumday_score_756d(exchange_tier: pd.Series) -> pd.Series:
    """Cumulative tier-day score over trailing 756 days (sum of daily tier values)."""
    return _rolling_sum(exchange_tier.astype(float), _TD_3Y)


def lsr_ext_039_tier_above_2_excess_252d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 252-day sum of tier-minus-2 excess (cumulative below-mid-tier depth)."""
    excess = (exchange_tier.astype(float) - 2.0).clip(lower=0.0)
    return _rolling_sum(excess, _TD_YEAR)


def lsr_ext_040_tier_ewm_span21(exchange_tier: pd.Series) -> pd.Series:
    """EWM-smoothed exchange tier (span=21) — short-run tier trajectory."""
    return _ewm_mean(exchange_tier.astype(float), _TD_MO)


# --- Group D (041-052): Tier transitions and tier-momentum variants ---

def lsr_ext_041_tier_downgrades_756d(exchange_tier: pd.Series) -> pd.Series:
    """Count of tier downgrade events in trailing 756 trading days."""
    flag = (exchange_tier > exchange_tier.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_3Y)


def lsr_ext_042_tier_change_5d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over the trailing 5 trading days (weekly tier drift)."""
    return (exchange_tier - exchange_tier.shift(_TD_WK)).astype(float)


def lsr_ext_043_tier_change_126d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over the trailing 126 trading days (half-year tier drift)."""
    return (exchange_tier - exchange_tier.shift(_TD_2Q)).astype(float)


def lsr_ext_044_tier_change_504d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over the trailing 504 trading days (two-year tier drift)."""
    return (exchange_tier - exchange_tier.shift(_TD_2Y)).astype(float)


def lsr_ext_045_tier_net_downgrades_252d(exchange_tier: pd.Series) -> pd.Series:
    """Net downgrades minus upgrades within trailing 252 days."""
    diff = (exchange_tier - exchange_tier.shift(1)).astype(float)
    down = diff.clip(lower=0.0)
    up = (-diff).clip(lower=0.0)
    return _rolling_sum(down, _TD_YEAR) - _rolling_sum(up, _TD_YEAR)


def lsr_ext_046_tier_downgrade_magnitude_sum_252d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 252-day sum of downgrade magnitudes (cumulative tier deterioration)."""
    diff = (exchange_tier - exchange_tier.shift(1)).astype(float).clip(lower=0.0)
    return _rolling_sum(diff, _TD_YEAR)


def lsr_ext_047_tier_zscore_756d(exchange_tier: pd.Series) -> pd.Series:
    """Z-score of exchange tier within trailing 756-day window."""
    return _zscore_rolling(exchange_tier.astype(float), _TD_3Y)


def lsr_ext_048_tier_pct_rank_756d(exchange_tier: pd.Series) -> pd.Series:
    """Percentile rank of exchange tier within trailing 756-day window."""
    return _rolling_rank_pct(exchange_tier.astype(float), _TD_3Y)


def lsr_ext_049_tier_ewm_5_minus_252(exchange_tier: pd.Series) -> pd.Series:
    """Tier EWM span-5 minus EWM span-252 (short vs long tier-momentum cross)."""
    return _ewm_mean(exchange_tier.astype(float), _TD_WK) - _ewm_mean(exchange_tier.astype(float), _TD_YEAR)


def lsr_ext_050_days_since_tier_upgrade(exchange_tier: pd.Series) -> pd.Series:
    """Days elapsed since the last tier upgrade event; NaN if never."""
    upgrade = (exchange_tier < exchange_tier.shift(1)).astype(float)
    return _days_since_last_one(upgrade)


def lsr_ext_051_tier_change_velocity_21d(exchange_tier: pd.Series) -> pd.Series:
    """Tier change over 21 days divided by 21 (per-day downgrade velocity)."""
    return (exchange_tier - exchange_tier.shift(_TD_MO)).astype(float) / float(_TD_MO)


def lsr_ext_052_tier_rolling_std_504d(exchange_tier: pd.Series) -> pd.Series:
    """Rolling 504-day standard deviation of exchange tier (tier instability)."""
    return _rolling_std(exchange_tier.astype(float), _TD_2Y)


# --- Group E (053-064): Delist-notice timing and notice-price coupling ---

def lsr_ext_053_notice_days_5d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 5 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_WK)


def lsr_ext_054_notice_days_504d(delist_notice: pd.Series) -> pd.Series:
    """Count of delist-notice days in trailing 504 trading days."""
    return _rolling_sum(delist_notice.astype(float), _TD_2Y)


def lsr_ext_055_notice_off_streak(delist_notice: pd.Series) -> pd.Series:
    """Consecutive trading days with no delist notice in effect (clean run length)."""
    return _streak_length((delist_notice == 0).astype(float))


def lsr_ext_056_notice_streak_log(delist_notice: pd.Series) -> pd.Series:
    """Natural log of (1 + current delist-notice streak length)."""
    return np.log1p(_streak_length(delist_notice))


def lsr_ext_057_notice_streak_vs_504d_max(delist_notice: pd.Series) -> pd.Series:
    """Current notice streak divided by the longest notice streak in trailing 504 days."""
    streak = _streak_length(delist_notice)
    return _safe_div(streak, _rolling_max(streak, _TD_2Y))


def lsr_ext_058_notice_fraction_756d(delist_notice: pd.Series) -> pd.Series:
    """Fraction of days under delist notice in trailing 756 days."""
    return _rolling_mean(delist_notice.astype(float), _TD_3Y)


def lsr_ext_059_notice_fraction_63d_zscore_252d(delist_notice: pd.Series) -> pd.Series:
    """Z-score of the 63-day notice fraction within a 252-day rolling window."""
    frac = _rolling_mean(delist_notice.astype(float), _TD_QTR)
    return _zscore_rolling(frac, _TD_YEAR)


def lsr_ext_060_notice_fraction_pct_rank_504d(delist_notice: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day notice fraction within a 504-day window."""
    frac = _rolling_mean(delist_notice.astype(float), _TD_QTR)
    return _rolling_rank_pct(frac, _TD_2Y)


def lsr_ext_061_notice_spell_count_756d(delist_notice: pd.Series) -> pd.Series:
    """Number of distinct delist-notice spells in trailing 756 days."""
    return _rolling_sum(_onset(delist_notice), _TD_3Y)


def lsr_ext_062_notice_sub050_joint(delist_notice: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 when delist notice active AND unadjusted close < $0.50."""
    return ((delist_notice == 1) & (closeunadj < 0.50)).astype(float)


def lsr_ext_063_notice_sub1_days_252d(delist_notice: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Count of days with notice active AND sub-$1 close in trailing 252 days."""
    joint = ((delist_notice == 1) & (closeunadj < 1.0)).astype(float)
    return _rolling_sum(joint, _TD_YEAR)


def lsr_ext_064_notice_at_price_low_252d(delist_notice: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 when delist notice active AND adjusted close at its 252-day rolling low."""
    low = _rolling_min(close, _TD_YEAR)
    return ((delist_notice == 1) & (close <= low + _EPS)).astype(float)


# --- Group F (065-075): Combined distress interactions and composites ---

def lsr_ext_065_tier_x_sub1_x_notice(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """Triple interaction: tier ordinal times sub-$1 flag times delist-notice flag."""
    sub1 = (closeunadj < 1.0).astype(float)
    return exchange_tier.astype(float) * sub1 * delist_notice.astype(float)


def lsr_ext_066_tier4plus_sub1_flag(exchange_tier: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 when at OTC/Pink tier (>= 4) AND unadjusted close < $1.00."""
    return ((exchange_tier >= 4) & (closeunadj < 1.0)).astype(float)


def lsr_ext_067_tier4plus_sub1_streak(exchange_tier: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Consecutive days at tier >= 4 AND sub-$1 close (severe joint distress run)."""
    joint = ((exchange_tier >= 4) & (closeunadj < 1.0)).astype(float)
    return _streak_length(joint)


def lsr_ext_068_combined_distress_fraction_252d(exchange_tier: pd.Series, delist_notice: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with notice active AND tier >= 3."""
    joint = ((delist_notice == 1) & (exchange_tier >= 3)).astype(float)
    return _rolling_mean(joint, _TD_YEAR)


def lsr_ext_069_distress_score_tier_notice_sub1(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """Additive distress score: exchange_tier + 2*delist_notice + 2*sub-$1 flag."""
    sub1 = (closeunadj < 1.0).astype(float)
    return exchange_tier.astype(float) + 2.0 * delist_notice.astype(float) + 2.0 * sub1


def lsr_ext_070_drawdown_x_tier_x_notice(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """252-day drawdown magnitude times tier ordinal times delist-notice flag."""
    peak = _rolling_max(close, _TD_YEAR)
    dd = _safe_div(close - peak, peak).abs()
    return dd * exchange_tier.astype(float) * delist_notice.astype(float)


def lsr_ext_071_distress_score_ewm63(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """EWM (span=63) smoothed additive distress score (tier + 2*notice + 2*sub1)."""
    sub1 = (closeunadj < 1.0).astype(float)
    score = exchange_tier.astype(float) + 2.0 * delist_notice.astype(float) + 2.0 * sub1
    return _ewm_mean(score, _TD_QTR)


def lsr_ext_072_distress_score_zscore_252d(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
) -> pd.Series:
    """Z-score of the additive distress score within a 252-day rolling window."""
    sub1 = (closeunadj < 1.0).astype(float)
    score = exchange_tier.astype(float) + 2.0 * delist_notice.astype(float) + 2.0 * sub1
    return _zscore_rolling(score, _TD_YEAR)


def lsr_ext_073_unadj_close_drawdown_252d(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted-close drawdown from its 252-day rolling peak (nominal-price decline)."""
    peak = _rolling_max(closeunadj, _TD_YEAR)
    return _safe_div(closeunadj - peak, peak.replace(0, np.nan))


def lsr_ext_074_closeunadj_pct_rank_756d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 756-day window."""
    return _rolling_rank_pct(closeunadj, _TD_3Y)


def lsr_ext_075_listing_capitulation_composite(
    exchange_tier: pd.Series,
    delist_notice: pd.Series,
    closeunadj: pd.Series,
    close: pd.Series,
) -> pd.Series:
    """
    Listing-capitulation composite: z-scored tier (252d) + 2*notice fraction (63d)
    + sub-$1 fraction (63d), all scaled by (1 + absolute 252-day price drawdown).
    Higher = listing distress coincident with price capitulation.
    """
    z_tier   = _zscore_rolling(exchange_tier.astype(float), _TD_YEAR)
    nf       = _rolling_mean(delist_notice.astype(float), _TD_QTR)
    sub1     = _rolling_mean((closeunadj < 1.0).astype(float), _TD_QTR)
    peak     = _rolling_max(close, _TD_YEAR)
    dd       = _safe_div(close - peak, peak).clip(lower=-1.0, upper=0.0).abs()
    base     = z_tier + 2.0 * nf + sub1
    return base * (1.0 + dd)


# ── Registry ──────────────────────────────────────────────────────────────────

LISTING_STATUS_RISK_EXTENDED_REGISTRY_001_075 = {
    "lsr_ext_001_sub050_flag":                    {"inputs": ["closeunadj"],                                           "func": lsr_ext_001_sub050_flag},
    "lsr_ext_002_sub010_flag":                    {"inputs": ["closeunadj"],                                           "func": lsr_ext_002_sub010_flag},
    "lsr_ext_003_sub3_flag":                      {"inputs": ["closeunadj"],                                           "func": lsr_ext_003_sub3_flag},
    "lsr_ext_004_sub050_streak":                  {"inputs": ["closeunadj"],                                           "func": lsr_ext_004_sub050_streak},
    "lsr_ext_005_sub3_streak":                    {"inputs": ["closeunadj"],                                           "func": lsr_ext_005_sub3_streak},
    "lsr_ext_006_sub050_days_252d":               {"inputs": ["closeunadj"],                                           "func": lsr_ext_006_sub050_days_252d},
    "lsr_ext_007_sub050_fraction_252d":           {"inputs": ["closeunadj"],                                           "func": lsr_ext_007_sub050_fraction_252d},
    "lsr_ext_008_sub3_fraction_252d":             {"inputs": ["closeunadj"],                                           "func": lsr_ext_008_sub3_fraction_252d},
    "lsr_ext_009_dist_to_1_dollar_log":           {"inputs": ["closeunadj"],                                           "func": lsr_ext_009_dist_to_1_dollar_log},
    "lsr_ext_010_dist_to_5_dollar_pct":           {"inputs": ["closeunadj"],                                           "func": lsr_ext_010_dist_to_5_dollar_pct},
    "lsr_ext_011_sub1_days_756d":                 {"inputs": ["closeunadj"],                                           "func": lsr_ext_011_sub1_days_756d},
    "lsr_ext_012_sub1_fraction_756d":             {"inputs": ["closeunadj"],                                           "func": lsr_ext_012_sub1_fraction_756d},
    "lsr_ext_013_sub1_fraction_21d":              {"inputs": ["closeunadj"],                                           "func": lsr_ext_013_sub1_fraction_21d},
    "lsr_ext_014_above_1_dollar_streak":          {"inputs": ["closeunadj"],                                           "func": lsr_ext_014_above_1_dollar_streak},
    "lsr_ext_015_sub1_consec_30d_flag":           {"inputs": ["closeunadj"],                                           "func": lsr_ext_015_sub1_consec_30d_flag},
    "lsr_ext_016_sub1_consec_180d_flag":          {"inputs": ["closeunadj"],                                           "func": lsr_ext_016_sub1_consec_180d_flag},
    "lsr_ext_017_sub1_streak_pct_rank_504d":      {"inputs": ["closeunadj"],                                           "func": lsr_ext_017_sub1_streak_pct_rank_504d},
    "lsr_ext_018_sub1_longest_spell_756d":        {"inputs": ["closeunadj"],                                           "func": lsr_ext_018_sub1_longest_spell_756d},
    "lsr_ext_019_sub1_spell_count_252d":          {"inputs": ["closeunadj"],                                           "func": lsr_ext_019_sub1_spell_count_252d},
    "lsr_ext_020_sub1_spell_count_756d":          {"inputs": ["closeunadj"],                                           "func": lsr_ext_020_sub1_spell_count_756d},
    "lsr_ext_021_sub1_ewm_intensity_63":          {"inputs": ["closeunadj"],                                           "func": lsr_ext_021_sub1_ewm_intensity_63},
    "lsr_ext_022_sub1_ewm_intensity_252":         {"inputs": ["closeunadj"],                                           "func": lsr_ext_022_sub1_ewm_intensity_252},
    "lsr_ext_023_sub1_fraction_63d_zscore_252d":  {"inputs": ["closeunadj"],                                           "func": lsr_ext_023_sub1_fraction_63d_zscore_252d},
    "lsr_ext_024_days_since_above_1_dollar":      {"inputs": ["closeunadj"],                                           "func": lsr_ext_024_days_since_above_1_dollar},
    "lsr_ext_025_sub1_onset_flag":                {"inputs": ["closeunadj"],                                           "func": lsr_ext_025_sub1_onset_flag},
    "lsr_ext_026_sub1_recovery_flag":             {"inputs": ["closeunadj"],                                           "func": lsr_ext_026_sub1_recovery_flag},
    "lsr_ext_027_tier_ge3_flag":                  {"inputs": ["exchange_tier"],                                        "func": lsr_ext_027_tier_ge3_flag},
    "lsr_ext_028_tier_ge3_streak":                {"inputs": ["exchange_tier"],                                        "func": lsr_ext_028_tier_ge3_streak},
    "lsr_ext_029_tier_ge4_streak":                {"inputs": ["exchange_tier"],                                        "func": lsr_ext_029_tier_ge4_streak},
    "lsr_ext_030_tier_ge3_days_252d":             {"inputs": ["exchange_tier"],                                        "func": lsr_ext_030_tier_ge3_days_252d},
    "lsr_ext_031_tier_ge3_fraction_252d":         {"inputs": ["exchange_tier"],                                        "func": lsr_ext_031_tier_ge3_fraction_252d},
    "lsr_ext_032_tier4plus_fraction_252d":        {"inputs": ["exchange_tier"],                                        "func": lsr_ext_032_tier4plus_fraction_252d},
    "lsr_ext_033_tier5_fraction_252d":            {"inputs": ["exchange_tier"],                                        "func": lsr_ext_033_tier5_fraction_252d},
    "lsr_ext_034_tier_minus_min_252d":            {"inputs": ["exchange_tier"],                                        "func": lsr_ext_034_tier_minus_min_252d},
    "lsr_ext_035_tier_minus_min_504d":            {"inputs": ["exchange_tier"],                                        "func": lsr_ext_035_tier_minus_min_504d},
    "lsr_ext_036_tier_at_504d_max_flag":          {"inputs": ["exchange_tier"],                                        "func": lsr_ext_036_tier_at_504d_max_flag},
    "lsr_ext_037_tier_rolling_max_756d":          {"inputs": ["exchange_tier"],                                        "func": lsr_ext_037_tier_rolling_max_756d},
    "lsr_ext_038_tier_cumday_score_756d":         {"inputs": ["exchange_tier"],                                        "func": lsr_ext_038_tier_cumday_score_756d},
    "lsr_ext_039_tier_above_2_excess_252d":       {"inputs": ["exchange_tier"],                                        "func": lsr_ext_039_tier_above_2_excess_252d},
    "lsr_ext_040_tier_ewm_span21":                {"inputs": ["exchange_tier"],                                        "func": lsr_ext_040_tier_ewm_span21},
    "lsr_ext_041_tier_downgrades_756d":           {"inputs": ["exchange_tier"],                                        "func": lsr_ext_041_tier_downgrades_756d},
    "lsr_ext_042_tier_change_5d":                 {"inputs": ["exchange_tier"],                                        "func": lsr_ext_042_tier_change_5d},
    "lsr_ext_043_tier_change_126d":               {"inputs": ["exchange_tier"],                                        "func": lsr_ext_043_tier_change_126d},
    "lsr_ext_044_tier_change_504d":               {"inputs": ["exchange_tier"],                                        "func": lsr_ext_044_tier_change_504d},
    "lsr_ext_045_tier_net_downgrades_252d":       {"inputs": ["exchange_tier"],                                        "func": lsr_ext_045_tier_net_downgrades_252d},
    "lsr_ext_046_tier_downgrade_magnitude_sum_252d": {"inputs": ["exchange_tier"],                                     "func": lsr_ext_046_tier_downgrade_magnitude_sum_252d},
    "lsr_ext_047_tier_zscore_756d":               {"inputs": ["exchange_tier"],                                        "func": lsr_ext_047_tier_zscore_756d},
    "lsr_ext_048_tier_pct_rank_756d":             {"inputs": ["exchange_tier"],                                        "func": lsr_ext_048_tier_pct_rank_756d},
    "lsr_ext_049_tier_ewm_5_minus_252":           {"inputs": ["exchange_tier"],                                        "func": lsr_ext_049_tier_ewm_5_minus_252},
    "lsr_ext_050_days_since_tier_upgrade":        {"inputs": ["exchange_tier"],                                        "func": lsr_ext_050_days_since_tier_upgrade},
    "lsr_ext_051_tier_change_velocity_21d":       {"inputs": ["exchange_tier"],                                        "func": lsr_ext_051_tier_change_velocity_21d},
    "lsr_ext_052_tier_rolling_std_504d":          {"inputs": ["exchange_tier"],                                        "func": lsr_ext_052_tier_rolling_std_504d},
    "lsr_ext_053_notice_days_5d":                 {"inputs": ["delist_notice"],                                        "func": lsr_ext_053_notice_days_5d},
    "lsr_ext_054_notice_days_504d":               {"inputs": ["delist_notice"],                                        "func": lsr_ext_054_notice_days_504d},
    "lsr_ext_055_notice_off_streak":              {"inputs": ["delist_notice"],                                        "func": lsr_ext_055_notice_off_streak},
    "lsr_ext_056_notice_streak_log":              {"inputs": ["delist_notice"],                                        "func": lsr_ext_056_notice_streak_log},
    "lsr_ext_057_notice_streak_vs_504d_max":      {"inputs": ["delist_notice"],                                        "func": lsr_ext_057_notice_streak_vs_504d_max},
    "lsr_ext_058_notice_fraction_756d":           {"inputs": ["delist_notice"],                                        "func": lsr_ext_058_notice_fraction_756d},
    "lsr_ext_059_notice_fraction_63d_zscore_252d":{"inputs": ["delist_notice"],                                        "func": lsr_ext_059_notice_fraction_63d_zscore_252d},
    "lsr_ext_060_notice_fraction_pct_rank_504d":  {"inputs": ["delist_notice"],                                        "func": lsr_ext_060_notice_fraction_pct_rank_504d},
    "lsr_ext_061_notice_spell_count_756d":        {"inputs": ["delist_notice"],                                        "func": lsr_ext_061_notice_spell_count_756d},
    "lsr_ext_062_notice_sub050_joint":            {"inputs": ["delist_notice", "closeunadj"],                          "func": lsr_ext_062_notice_sub050_joint},
    "lsr_ext_063_notice_sub1_days_252d":          {"inputs": ["delist_notice", "closeunadj"],                          "func": lsr_ext_063_notice_sub1_days_252d},
    "lsr_ext_064_notice_at_price_low_252d":       {"inputs": ["delist_notice", "close"],                               "func": lsr_ext_064_notice_at_price_low_252d},
    "lsr_ext_065_tier_x_sub1_x_notice":           {"inputs": ["exchange_tier", "delist_notice", "closeunadj"],         "func": lsr_ext_065_tier_x_sub1_x_notice},
    "lsr_ext_066_tier4plus_sub1_flag":            {"inputs": ["exchange_tier", "closeunadj"],                          "func": lsr_ext_066_tier4plus_sub1_flag},
    "lsr_ext_067_tier4plus_sub1_streak":          {"inputs": ["exchange_tier", "closeunadj"],                          "func": lsr_ext_067_tier4plus_sub1_streak},
    "lsr_ext_068_combined_distress_fraction_252d":{"inputs": ["exchange_tier", "delist_notice"],                       "func": lsr_ext_068_combined_distress_fraction_252d},
    "lsr_ext_069_distress_score_tier_notice_sub1":{"inputs": ["exchange_tier", "delist_notice", "closeunadj"],         "func": lsr_ext_069_distress_score_tier_notice_sub1},
    "lsr_ext_070_drawdown_x_tier_x_notice":       {"inputs": ["exchange_tier", "delist_notice", "close"],              "func": lsr_ext_070_drawdown_x_tier_x_notice},
    "lsr_ext_071_distress_score_ewm63":           {"inputs": ["exchange_tier", "delist_notice", "closeunadj"],         "func": lsr_ext_071_distress_score_ewm63},
    "lsr_ext_072_distress_score_zscore_252d":     {"inputs": ["exchange_tier", "delist_notice", "closeunadj"],         "func": lsr_ext_072_distress_score_zscore_252d},
    "lsr_ext_073_unadj_close_drawdown_252d":      {"inputs": ["closeunadj"],                                           "func": lsr_ext_073_unadj_close_drawdown_252d},
    "lsr_ext_074_closeunadj_pct_rank_756d":       {"inputs": ["closeunadj"],                                           "func": lsr_ext_074_closeunadj_pct_rank_756d},
    "lsr_ext_075_listing_capitulation_composite": {"inputs": ["exchange_tier", "delist_notice", "closeunadj", "close"],"func": lsr_ext_075_listing_capitulation_composite},
}
