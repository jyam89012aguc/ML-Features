"""
Decline Streaks — Base Features 001–075
Domain: consecutive down days and negative persistence
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def dstk_001_consecutive_down_days(close: pd.Series) -> pd.Series:
    """dstk_001_consecutive_down_days feature"""
    is_down = (close < close.shift(1))
    return _consecutive_count(is_down)

def dstk_002_cumulative_loss_current_streak(close: pd.Series) -> pd.Series:
    """dstk_002_cumulative_loss_current_streak feature"""
    # Cumulative return of the current consecutive down day streak
    ret = close.pct_change()
    is_down = (ret < 0)
    streak_id = (is_down != is_down.shift()).cumsum()
    def _streak_ret(x): return (1 + x).prod() - 1
    # This is complex for a simple apply, using a cumulative approach instead
    log_ret = np.log(1 + ret)
    cum_log_ret = log_ret.where(is_down, 0).groupby(streak_id).cumsum()
    return np.exp(cum_log_ret) - 1

def dstk_003_max_consecutive_down_days_63d(close: pd.Series) -> pd.Series:
    """dstk_003_max_consecutive_down_days_63d feature"""
    is_down = (close < close.shift(1))
    counts = _consecutive_count(is_down)
    return counts.rolling(63).max()

def dstk_004_avg_consecutive_down_days_252d(close: pd.Series) -> pd.Series:
    """dstk_004_avg_consecutive_down_days_252d feature"""
    is_down = (close < close.shift(1))
    counts = _consecutive_count(is_down)
    # Filter only the ends of streaks to average them
    streak_ends = counts.where(counts > counts.shift(-1).fillna(0))
    return streak_ends.rolling(252).mean()

def dstk_005_down_day_frequency_21d(close: pd.Series) -> pd.Series:
    """dstk_005_down_day_frequency_21d feature"""
    return (close < close.shift(1)).rolling(21).mean()

def dstk_006_down_day_frequency_252d(close: pd.Series) -> pd.Series:
    """dstk_006_down_day_frequency_252d feature"""
    return (close < close.shift(1)).rolling(252).mean()


# 016-030: Multi-Day Down Streaks (Weekly/Monthly equivalents)

def dstk_016_consecutive_down_weeks(close: pd.Series) -> pd.Series:
    """dstk_016_consecutive_down_weeks feature"""
    # Based on 5-day non-overlapping or rolling weekly closes
    w_close = close.iloc[::5]
    is_down = (w_close < w_close.shift(1))
    counts = _consecutive_count(is_down)
    return counts.reindex(close.index).ffill()

def dstk_017_consecutive_down_months(close: pd.Series) -> pd.Series:
    """dstk_017_consecutive_down_months feature"""
    m_close = close.iloc[::21]
    is_down = (m_close < m_close.shift(1))
    counts = _consecutive_count(is_down)
    return counts.reindex(close.index).ffill()


# 031-045: Extreme Streak Signatures

def dstk_031_streak_loss_magnitude_zscore_252d(close: pd.Series) -> pd.Series:
    """dstk_031_streak_loss_magnitude_zscore_252d feature"""
    # Magnitude of current streak loss relative to prior streaks
    loss = dstk_002_cumulative_loss_current_streak(close).abs()
    return (loss - loss.rolling(252).mean()) / loss.rolling(252).std()

def dstk_032_probability_of_down_day_after_3_down(close: pd.Series) -> pd.Series:
    """dstk_032_probability_of_down_day_after_3_down feature"""
    # Historical probability of down day given at least 3 prior down days
    is_down = (close < close.shift(1))
    streak = _consecutive_count(is_down)
    prior_3 = (streak.shift(1) >= 3)
    success = prior_3 & is_down
    return success.rolling(252).sum() / prior_3.rolling(252).sum()

def dstk_033_streak_capitulation_ratio_63d(close: pd.Series) -> pd.Series:
    """dstk_033_streak_capitulation_ratio_63d feature"""
    # Ratio of current streak duration to 63-day max
    curr = dstk_001_consecutive_down_days(close)
    mx = curr.rolling(63).max()
    return _safe_div(curr, mx)


# 046-060: Asset / Fundamental Decline Streaks

def dstk_046_consecutive_down_mktcap_days(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dstk_046_consecutive_down_mktcap_days feature"""
    mc = close * sharesbas
    is_down = (mc < mc.shift(1))
    return _consecutive_count(is_down)

def dstk_047_consecutive_negative_earnings_surprises(surprise: pd.Series) -> pd.Series:
    """dstk_047_consecutive_negative_earnings_surprises feature"""
    is_neg = (surprise < 0)
    return _consecutive_count(is_neg)

def dstk_048_consecutive_declining_revenue_quarters(revenue: pd.Series) -> pd.Series:
    """dstk_048_consecutive_declining_revenue_quarters feature"""
    # Assumes quarterly data
    is_down = (revenue < revenue.shift(1))
    return _consecutive_count(is_down)


# 061-075: Streak Dynamics and Composites

def dstk_061_streak_acceleration_index_21d(close: pd.Series) -> pd.Series:
    """dstk_061_streak_acceleration_index_21d feature"""
    # Ratio of down-day frequency in last 5 days to last 21 days
    f5 = (close < close.shift(1)).rolling(5).mean()
    f21 = (close < close.shift(1)).rolling(21).mean()
    return _safe_div(f5, f21)

def dstk_062_consecutive_days_without_2_pct_rally(close: pd.Series) -> pd.Series:
    """dstk_062_consecutive_days_without_2_pct_rally feature"""
    # Days since a single-day gain >= 2%
    ret = close.pct_change()
    no_rally = (ret < 0.02)
    return _consecutive_count(no_rally)

def dstk_063_consecutive_days_below_ma_20(close: pd.Series) -> pd.Series:
    """dstk_063_consecutive_days_below_ma_20 feature"""
    ma = close.rolling(20).mean()
    under = (close < ma)
    return _consecutive_count(under)

def dstk_064_consecutive_days_making_new_21d_lows(close: pd.Series) -> pd.Series:
    """dstk_064_consecutive_days_making_new_21d_lows feature"""
    is_low = (close == _rolling_min(close, 21))
    return _consecutive_count(is_low)

def dstk_065_down_streak_intensity_index_63d(close: pd.Series) -> pd.Series:
    """dstk_065_down_streak_intensity_index_63d feature"""
    # (Consecutive Down Days) * (Cumulative Streak Loss)
    dur = dstk_001_consecutive_down_days(close)
    loss = dstk_002_cumulative_loss_current_streak(close).abs()
    return dur * loss

def dstk_066_days_since_last_up_day(close: pd.Series) -> pd.Series:
    """dstk_066_days_since_last_up_day feature"""
    is_up = (close > close.shift(1))
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_up).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices

def dstk_067_consecutive_red_candles(close: pd.Series, open: pd.Series) -> pd.Series:
    """dstk_067_consecutive_red_candles feature"""
    is_red = (close < open)
    return _consecutive_count(is_red)

def dstk_068_consecutive_gap_downs(close: pd.Series, open: pd.Series) -> pd.Series:
    """dstk_068_consecutive_gap_downs feature"""
    is_gap_down = (open < close.shift(1))
    return _consecutive_count(is_gap_down)

def dstk_069_streak_relative_to_historical_max_252d(close: pd.Series) -> pd.Series:
    """dstk_069_streak_relative_to_historical_max_252d feature"""
    curr = dstk_001_consecutive_down_days(close)
    mx = curr.rolling(252 * 5).max()
    return _safe_div(curr, mx)

def dstk_070_consecutive_days_with_volume_expansion_and_price_decline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dstk_070_consecutive_days_with_volume_expansion_and_price_decline feature"""
    cond = (close < close.shift(1)) & (volume > volume.shift(1))
    return _consecutive_count(cond)

def dstk_071_avg_loss_per_down_day_in_streak(close: pd.Series) -> pd.Series:
    """dstk_071_avg_loss_per_down_day_in_streak feature"""
    loss = dstk_002_cumulative_loss_current_streak(close).abs()
    dur = dstk_001_consecutive_down_days(close)
    return _safe_div(loss, dur)

def dstk_072_consecutive_days_under_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dstk_072_consecutive_days_under_vwap_21d feature"""
    vwap = (close * volume).rolling(21).sum() / volume.rolling(21).sum()
    under = (close < vwap)
    return _consecutive_count(under)

def dstk_073_consecutive_days_outside_lower_bollinger_20_2(close: pd.Series) -> pd.Series:
    """dstk_073_consecutive_days_outside_lower_bollinger_20_2 feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    lower = ma - 2 * std
    outside = (close < lower)
    return _consecutive_count(outside)

def dstk_074_down_streak_entropy_63d(close: pd.Series) -> pd.Series:
    """dstk_074_down_streak_entropy_63d feature"""
    # Entropy of streak lengths in last 63 days
    is_down = (close < close.shift(1))
    counts = _consecutive_count(is_down)
    streak_ends = counts.where(counts > counts.shift(-1).fillna(0)).dropna()
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y, bins=5, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    return counts.rolling(63).apply(_ent, raw=True)

def dstk_075_decline_streak_final_composite(close: pd.Series) -> pd.Series:
    """dstk_075_decline_streak_final_composite feature"""
    # Weighted sum of day/week/month streak normalized by historical max
    d = dstk_001_consecutive_down_days(close)
    w = dstk_016_consecutive_down_weeks(close)
    m = dstk_017_consecutive_down_months(close)
    return (0.6 * d + 0.3 * w + 0.1 * m)

def dstk_030_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_001_consecutive_down_days"""
    return _zscore_rolling(dstk_001_consecutive_down_days(close), _TD_MON)

def dstk_031_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_002_cumulative_loss_current_streak"""
    return _rank_pct(dstk_002_cumulative_loss_current_streak(close), _TD_MON)

def dstk_032_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_003_max_consecutive_down_days_63d"""
    return _zscore_rolling(dstk_003_max_consecutive_down_days_63d(close), _TD_MON)

def dstk_033_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_004_avg_consecutive_down_days_252d"""
    return _rank_pct(dstk_004_avg_consecutive_down_days_252d(close), _TD_MON)

def dstk_034_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_005_down_day_frequency_21d"""
    return _zscore_rolling(dstk_005_down_day_frequency_21d(close), _TD_MON)

def dstk_035_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_006_down_day_frequency_252d"""
    return _rank_pct(dstk_006_down_day_frequency_252d(close), _TD_MON)

def dstk_036_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_016_consecutive_down_weeks"""
    return _zscore_rolling(dstk_016_consecutive_down_weeks(close), _TD_MON)

def dstk_037_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_017_consecutive_down_months"""
    return _rank_pct(dstk_017_consecutive_down_months(close), _TD_MON)

def dstk_038_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_031_streak_loss_magnitude_zscore_252d"""
    return _zscore_rolling(dstk_031_streak_loss_magnitude_zscore_252d(close), _TD_MON)

def dstk_039_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_032_probability_of_down_day_after_3_down"""
    return _rank_pct(dstk_032_probability_of_down_day_after_3_down(close), _TD_MON)

def dstk_040_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_033_streak_capitulation_ratio_63d"""
    return _zscore_rolling(dstk_033_streak_capitulation_ratio_63d(close), _TD_MON)

def dstk_041_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_046_consecutive_down_mktcap_days"""
    return _rank_pct(dstk_046_consecutive_down_mktcap_days(close), _TD_MON)

def dstk_042_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_047_consecutive_negative_earnings_surprises"""
    return _zscore_rolling(dstk_047_consecutive_negative_earnings_surprises(close), _TD_MON)

def dstk_043_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_048_consecutive_declining_revenue_quarters"""
    return _rank_pct(dstk_048_consecutive_declining_revenue_quarters(close), _TD_MON)

def dstk_044_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_061_streak_acceleration_index_21d"""
    return _zscore_rolling(dstk_061_streak_acceleration_index_21d(close), _TD_MON)

def dstk_045_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_062_consecutive_days_without_2_pct_rally"""
    return _rank_pct(dstk_062_consecutive_days_without_2_pct_rally(close), _TD_MON)

def dstk_046_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_063_consecutive_days_below_ma_20"""
    return _zscore_rolling(dstk_063_consecutive_days_below_ma_20(close), _TD_MON)

def dstk_047_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_064_consecutive_days_making_new_21d_lows"""
    return _rank_pct(dstk_064_consecutive_days_making_new_21d_lows(close), _TD_MON)

def dstk_048_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_065_down_streak_intensity_index_63d"""
    return _zscore_rolling(dstk_065_down_streak_intensity_index_63d(close), _TD_MON)

def dstk_049_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_066_days_since_last_up_day"""
    return _rank_pct(dstk_066_days_since_last_up_day(close), _TD_MON)

def dstk_050_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_067_consecutive_red_candles"""
    return _zscore_rolling(dstk_067_consecutive_red_candles(close), _TD_MON)

def dstk_051_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_068_consecutive_gap_downs"""
    return _rank_pct(dstk_068_consecutive_gap_downs(close), _TD_MON)

def dstk_052_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_069_streak_relative_to_historical_max_252d"""
    return _zscore_rolling(dstk_069_streak_relative_to_historical_max_252d(close), _TD_MON)

def dstk_053_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_070_consecutive_days_with_volume_expansion_and_price_decline"""
    return _rank_pct(dstk_070_consecutive_days_with_volume_expansion_and_price_decline(close), _TD_MON)

def dstk_054_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_071_avg_loss_per_down_day_in_streak"""
    return _zscore_rolling(dstk_071_avg_loss_per_down_day_in_streak(close), _TD_MON)

def dstk_055_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_072_consecutive_days_under_vwap_21d"""
    return _rank_pct(dstk_072_consecutive_days_under_vwap_21d(close), _TD_MON)

def dstk_056_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_073_consecutive_days_outside_lower_bollinger_20_2"""
    return _zscore_rolling(dstk_073_consecutive_days_outside_lower_bollinger_20_2(close), _TD_MON)

def dstk_057_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_074_down_streak_entropy_63d"""
    return _rank_pct(dstk_074_down_streak_entropy_63d(close), _TD_MON)

def dstk_058_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_075_decline_streak_final_composite"""
    return _zscore_rolling(dstk_075_decline_streak_final_composite(close), _TD_MON)

def dstk_059_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_001_consecutive_down_days"""
    return _rank_pct(dstk_001_consecutive_down_days(close), _TD_MON)

def dstk_060_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_002_cumulative_loss_current_streak"""
    return _zscore_rolling(dstk_002_cumulative_loss_current_streak(close), _TD_MON)

def dstk_061_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_003_max_consecutive_down_days_63d"""
    return _rank_pct(dstk_003_max_consecutive_down_days_63d(close), _TD_MON)

def dstk_062_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_004_avg_consecutive_down_days_252d"""
    return _zscore_rolling(dstk_004_avg_consecutive_down_days_252d(close), _TD_MON)

def dstk_063_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_005_down_day_frequency_21d"""
    return _rank_pct(dstk_005_down_day_frequency_21d(close), _TD_MON)

def dstk_064_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_006_down_day_frequency_252d"""
    return _zscore_rolling(dstk_006_down_day_frequency_252d(close), _TD_MON)

def dstk_065_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_016_consecutive_down_weeks"""
    return _rank_pct(dstk_016_consecutive_down_weeks(close), _TD_MON)

def dstk_066_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_017_consecutive_down_months"""
    return _zscore_rolling(dstk_017_consecutive_down_months(close), _TD_MON)

def dstk_067_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_031_streak_loss_magnitude_zscore_252d"""
    return _rank_pct(dstk_031_streak_loss_magnitude_zscore_252d(close), _TD_MON)

def dstk_068_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_032_probability_of_down_day_after_3_down"""
    return _zscore_rolling(dstk_032_probability_of_down_day_after_3_down(close), _TD_MON)

def dstk_069_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_033_streak_capitulation_ratio_63d"""
    return _rank_pct(dstk_033_streak_capitulation_ratio_63d(close), _TD_MON)

def dstk_070_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_046_consecutive_down_mktcap_days"""
    return _zscore_rolling(dstk_046_consecutive_down_mktcap_days(close), _TD_MON)

def dstk_071_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_047_consecutive_negative_earnings_surprises"""
    return _rank_pct(dstk_047_consecutive_negative_earnings_surprises(close), _TD_MON)

def dstk_072_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_048_consecutive_declining_revenue_quarters"""
    return _zscore_rolling(dstk_048_consecutive_declining_revenue_quarters(close), _TD_MON)

def dstk_073_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_061_streak_acceleration_index_21d"""
    return _rank_pct(dstk_061_streak_acceleration_index_21d(close), _TD_MON)

def dstk_074_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_062_consecutive_days_without_2_pct_rally"""
    return _zscore_rolling(dstk_062_consecutive_days_without_2_pct_rally(close), _TD_MON)

def dstk_075_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_063_consecutive_days_below_ma_20"""
    return _rank_pct(dstk_063_consecutive_days_below_ma_20(close), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V08_REGISTRY = {
    "dstk_001_consecutive_down_days": {"inputs": ["close"], "func": dstk_001_consecutive_down_days},
    "dstk_002_cumulative_loss_current_streak": {"inputs": ["close"], "func": dstk_002_cumulative_loss_current_streak},
    "dstk_003_max_consecutive_down_days_63d": {"inputs": ["close"], "func": dstk_003_max_consecutive_down_days_63d},
    "dstk_004_avg_consecutive_down_days_252d": {"inputs": ["close"], "func": dstk_004_avg_consecutive_down_days_252d},
    "dstk_005_down_day_frequency_21d": {"inputs": ["close"], "func": dstk_005_down_day_frequency_21d},
    "dstk_006_down_day_frequency_252d": {"inputs": ["close"], "func": dstk_006_down_day_frequency_252d},
    "dstk_016_consecutive_down_weeks": {"inputs": ["close"], "func": dstk_016_consecutive_down_weeks},
    "dstk_017_consecutive_down_months": {"inputs": ["close"], "func": dstk_017_consecutive_down_months},
    "dstk_031_streak_loss_magnitude_zscore_252d": {"inputs": ["close"], "func": dstk_031_streak_loss_magnitude_zscore_252d},
    "dstk_032_probability_of_down_day_after_3_down": {"inputs": ["close"], "func": dstk_032_probability_of_down_day_after_3_down},
    "dstk_033_streak_capitulation_ratio_63d": {"inputs": ["close"], "func": dstk_033_streak_capitulation_ratio_63d},
    "dstk_046_consecutive_down_mktcap_days": {"inputs": ["close", "sharesbas"], "func": dstk_046_consecutive_down_mktcap_days},
    "dstk_047_consecutive_negative_earnings_surprises": {"inputs": ["surprise"], "func": dstk_047_consecutive_negative_earnings_surprises},
    "dstk_048_consecutive_declining_revenue_quarters": {"inputs": ["revenue"], "func": dstk_048_consecutive_declining_revenue_quarters},
    "dstk_061_streak_acceleration_index_21d": {"inputs": ["close"], "func": dstk_061_streak_acceleration_index_21d},
    "dstk_062_consecutive_days_without_2_pct_rally": {"inputs": ["close"], "func": dstk_062_consecutive_days_without_2_pct_rally},
    "dstk_063_consecutive_days_below_ma_20": {"inputs": ["close"], "func": dstk_063_consecutive_days_below_ma_20},
    "dstk_064_consecutive_days_making_new_21d_lows": {"inputs": ["close"], "func": dstk_064_consecutive_days_making_new_21d_lows},
    "dstk_065_down_streak_intensity_index_63d": {"inputs": ["close"], "func": dstk_065_down_streak_intensity_index_63d},
    "dstk_066_days_since_last_up_day": {"inputs": ["close"], "func": dstk_066_days_since_last_up_day},
    "dstk_067_consecutive_red_candles": {"inputs": ["close", "open"], "func": dstk_067_consecutive_red_candles},
    "dstk_068_consecutive_gap_downs": {"inputs": ["close", "open"], "func": dstk_068_consecutive_gap_downs},
    "dstk_069_streak_relative_to_historical_max_252d": {"inputs": ["close"], "func": dstk_069_streak_relative_to_historical_max_252d},
    "dstk_070_consecutive_days_with_volume_expansion_and_price_decline": {"inputs": ["close", "volume"], "func": dstk_070_consecutive_days_with_volume_expansion_and_price_decline},
    "dstk_071_avg_loss_per_down_day_in_streak": {"inputs": ["close"], "func": dstk_071_avg_loss_per_down_day_in_streak},
    "dstk_072_consecutive_days_under_vwap_21d": {"inputs": ["close", "volume"], "func": dstk_072_consecutive_days_under_vwap_21d},
    "dstk_073_consecutive_days_outside_lower_bollinger_20_2": {"inputs": ["close"], "func": dstk_073_consecutive_days_outside_lower_bollinger_20_2},
    "dstk_074_down_streak_entropy_63d": {"inputs": ["close"], "func": dstk_074_down_streak_entropy_63d},
    "dstk_075_decline_streak_final_composite": {"inputs": ["close"], "func": dstk_075_decline_streak_final_composite},
    "dstk_030_stat_depth_var_0": {"inputs": ["close"], "func": dstk_030_stat_depth_var_0},
    "dstk_031_stat_depth_var_1": {"inputs": ["close"], "func": dstk_031_stat_depth_var_1},
    "dstk_032_stat_depth_var_2": {"inputs": ["close"], "func": dstk_032_stat_depth_var_2},
    "dstk_033_stat_depth_var_3": {"inputs": ["close"], "func": dstk_033_stat_depth_var_3},
    "dstk_034_stat_depth_var_4": {"inputs": ["close"], "func": dstk_034_stat_depth_var_4},
    "dstk_035_stat_depth_var_5": {"inputs": ["close"], "func": dstk_035_stat_depth_var_5},
    "dstk_036_stat_depth_var_6": {"inputs": ["close"], "func": dstk_036_stat_depth_var_6},
    "dstk_037_stat_depth_var_7": {"inputs": ["close"], "func": dstk_037_stat_depth_var_7},
    "dstk_038_stat_depth_var_8": {"inputs": ["close"], "func": dstk_038_stat_depth_var_8},
    "dstk_039_stat_depth_var_9": {"inputs": ["close"], "func": dstk_039_stat_depth_var_9},
    "dstk_040_stat_depth_var_10": {"inputs": ["close"], "func": dstk_040_stat_depth_var_10},
    "dstk_041_stat_depth_var_11": {"inputs": ["close"], "func": dstk_041_stat_depth_var_11},
    "dstk_042_stat_depth_var_12": {"inputs": ["close"], "func": dstk_042_stat_depth_var_12},
    "dstk_043_stat_depth_var_13": {"inputs": ["close"], "func": dstk_043_stat_depth_var_13},
    "dstk_044_stat_depth_var_14": {"inputs": ["close"], "func": dstk_044_stat_depth_var_14},
    "dstk_045_stat_depth_var_15": {"inputs": ["close"], "func": dstk_045_stat_depth_var_15},
    "dstk_046_stat_depth_var_16": {"inputs": ["close"], "func": dstk_046_stat_depth_var_16},
    "dstk_047_stat_depth_var_17": {"inputs": ["close"], "func": dstk_047_stat_depth_var_17},
    "dstk_048_stat_depth_var_18": {"inputs": ["close"], "func": dstk_048_stat_depth_var_18},
    "dstk_049_stat_depth_var_19": {"inputs": ["close"], "func": dstk_049_stat_depth_var_19},
    "dstk_050_stat_depth_var_20": {"inputs": ["close"], "func": dstk_050_stat_depth_var_20},
    "dstk_051_stat_depth_var_21": {"inputs": ["close"], "func": dstk_051_stat_depth_var_21},
    "dstk_052_stat_depth_var_22": {"inputs": ["close"], "func": dstk_052_stat_depth_var_22},
    "dstk_053_stat_depth_var_23": {"inputs": ["close"], "func": dstk_053_stat_depth_var_23},
    "dstk_054_stat_depth_var_24": {"inputs": ["close"], "func": dstk_054_stat_depth_var_24},
    "dstk_055_stat_depth_var_25": {"inputs": ["close"], "func": dstk_055_stat_depth_var_25},
    "dstk_056_stat_depth_var_26": {"inputs": ["close"], "func": dstk_056_stat_depth_var_26},
    "dstk_057_stat_depth_var_27": {"inputs": ["close"], "func": dstk_057_stat_depth_var_27},
    "dstk_058_stat_depth_var_28": {"inputs": ["close"], "func": dstk_058_stat_depth_var_28},
    "dstk_059_stat_depth_var_29": {"inputs": ["close"], "func": dstk_059_stat_depth_var_29},
    "dstk_060_stat_depth_var_30": {"inputs": ["close"], "func": dstk_060_stat_depth_var_30},
    "dstk_061_stat_depth_var_31": {"inputs": ["close"], "func": dstk_061_stat_depth_var_31},
    "dstk_062_stat_depth_var_32": {"inputs": ["close"], "func": dstk_062_stat_depth_var_32},
    "dstk_063_stat_depth_var_33": {"inputs": ["close"], "func": dstk_063_stat_depth_var_33},
    "dstk_064_stat_depth_var_34": {"inputs": ["close"], "func": dstk_064_stat_depth_var_34},
    "dstk_065_stat_depth_var_35": {"inputs": ["close"], "func": dstk_065_stat_depth_var_35},
    "dstk_066_stat_depth_var_36": {"inputs": ["close"], "func": dstk_066_stat_depth_var_36},
    "dstk_067_stat_depth_var_37": {"inputs": ["close"], "func": dstk_067_stat_depth_var_37},
    "dstk_068_stat_depth_var_38": {"inputs": ["close"], "func": dstk_068_stat_depth_var_38},
    "dstk_069_stat_depth_var_39": {"inputs": ["close"], "func": dstk_069_stat_depth_var_39},
    "dstk_070_stat_depth_var_40": {"inputs": ["close"], "func": dstk_070_stat_depth_var_40},
    "dstk_071_stat_depth_var_41": {"inputs": ["close"], "func": dstk_071_stat_depth_var_41},
    "dstk_072_stat_depth_var_42": {"inputs": ["close"], "func": dstk_072_stat_depth_var_42},
    "dstk_073_stat_depth_var_43": {"inputs": ["close"], "func": dstk_073_stat_depth_var_43},
    "dstk_074_stat_depth_var_44": {"inputs": ["close"], "func": dstk_074_stat_depth_var_44},
    "dstk_075_stat_depth_var_45": {"inputs": ["close"], "func": dstk_075_stat_depth_var_45},
}
