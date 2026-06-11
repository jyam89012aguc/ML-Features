"""
Decline Streaks — Base Features 076–150
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

def dstk_076_streak_duration_pct_rank_ath(close: pd.Series) -> pd.Series:
    """dstk_076_streak_duration_pct_rank_ath feature"""
    # Percentile rank of current down streak length vs its own history
    is_down = (close < close.shift(1))
    dur = _consecutive_count(is_down)
    return dur.expanding().rank(pct=True)

def dstk_077_streak_loss_pct_rank_ath(close: pd.Series) -> pd.Series:
    """dstk_077_streak_loss_pct_rank_ath feature"""
    # Percentile rank of current streak cumulative loss vs history
    ret = close.pct_change()
    is_down = (ret < 0)
    streak_id = (is_down != is_down.shift()).cumsum()
    loss = np.exp(np.log(1 + ret).where(is_down, 0).groupby(streak_id).cumsum()) - 1
    return loss.expanding().rank(pct=True)

def dstk_078_streak_exhaustion_probability_63d(close: pd.Series) -> pd.Series:
    """dstk_078_streak_exhaustion_probability_63d feature"""
    # Probability that a streak of length N ends on the next day
    is_down = (close < close.shift(1))
    dur = _consecutive_count(is_down)
    ends = (is_down == False) & (is_down.shift(1) == True)
    # Count endings of streaks >= current duration
    def _prob(y):
        if len(y) == 0: return 0.0
        curr_dur = y[-1]
        if curr_dur == 0: return 0.0
        relevant_streaks = y[y >= curr_dur]
        streak_ends = (relevant_streaks.shift(-1) == 0).sum()
        return streak_ends / len(relevant_streaks)
    return dur.rolling(252).apply(_prob, raw=True)


# 091-105: Volatility-Adjusted Streak Signatures

def dstk_091_sigma_adjusted_streak_loss_21d(close: pd.Series) -> pd.Series:
    """dstk_091_sigma_adjusted_streak_loss_21d feature"""
    # Streak loss normalized by trailing daily volatility
    ret = close.pct_change()
    is_down = (ret < 0)
    streak_id = (is_down != is_down.shift()).cumsum()
    loss = (np.exp(np.log(1 + ret).where(is_down, 0).groupby(streak_id).cumsum()) - 1).abs()
    vol = ret.rolling(21).std()
    return _safe_div(loss, vol)

def dstk_092_count_volatile_down_streaks_252d(close: pd.Series) -> pd.Series:
    """dstk_092_count_volatile_down_streaks_252d feature"""
    # Number of streaks where loss > 2*std_dev
    ret = close.pct_change()
    is_down = (ret < 0)
    streak_id = (is_down != is_down.shift()).cumsum()
    loss = (np.exp(np.log(1 + ret).where(is_down, 0).groupby(streak_id).cumsum()) - 1).abs()
    threshold = ret.rolling(252).std() * 2
    is_extreme = (loss > threshold) & (loss > loss.shift(-1).fillna(0))
    return is_extreme.rolling(252).sum()


# 106-125: Multiple Horizon Streak Comparisons

def dstk_106_down_streak_day_to_week_ratio(close: pd.Series) -> pd.Series:
    """dstk_106_down_streak_day_to_week_ratio feature"""
    d = dstk_001_consecutive_down_days(close)
    w_close = close.iloc[::5]
    is_down_w = (w_close < w_close.shift(1))
    w = _consecutive_count(is_down_w).reindex(close.index).ffill()
    return _safe_div(d, w)

def dstk_107_cumulative_loss_ratio_21d_to_252d(close: pd.Series) -> pd.Series:
    """dstk_107_cumulative_loss_ratio_21d_to_252d feature"""
    ret = close.pct_change()
    is_down = (ret < 0)
    loss = (np.exp(np.log(1 + ret).where(is_down, 0).groupby((is_down != is_down.shift()).cumsum()).cumsum()) - 1).abs()
    return _safe_div(loss.rolling(21).max(), loss.rolling(252).max())


# 126-140: Multi-Asset / Fundamental Streak Dynamics

def dstk_126_consecutive_days_mktcap_under_ma_200(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dstk_126_consecutive_days_mktcap_under_ma_200 feature"""
    mc = close * sharesbas
    ma = mc.rolling(200).mean()
    return _consecutive_count(mc < ma)

def dstk_127_consecutive_quarters_negative_fcf(fcf: pd.Series) -> pd.Series:
    """dstk_127_consecutive_quarters_negative_fcf feature"""
    return _consecutive_count(fcf < 0)

def dstk_128_consecutive_days_with_declining_inst_holders(inst_holders: pd.Series) -> pd.Series:
    """dstk_128_consecutive_days_with_declining_inst_holders feature"""
    return _consecutive_count(inst_holders < inst_holders.shift(1))


# 141-150: Final Streak composites

def dstk_141_streak_climax_velocity_score_21d(close: pd.Series) -> pd.Series:
    """dstk_141_streak_climax_velocity_score_21d feature"""
    # (Streak Duration / Max Streak) * (Current Velocity)
    d = dstk_001_consecutive_down_days(close)
    mx = d.rolling(252).max()
    v = np.log(close).diff(5).abs()
    return _safe_div(d, mx) * v

def dstk_142_consecutive_days_in_lowest_decile_252d(close: pd.Series) -> pd.Series:
    """dstk_142_consecutive_days_in_lowest_decile_252d feature"""
    q10 = close.rolling(252).quantile(0.1)
    return _consecutive_count(close < q10)

def dstk_143_streak_recovery_failure_count_63d(close: pd.Series) -> pd.Series:
    """dstk_143_streak_recovery_failure_count_63d feature"""
    # Count of streaks that ended with < 1% bounce before starting new down streak
    ret = close.pct_change()
    is_down = (ret < 0)
    streak_id = (is_down != is_down.shift()).cumsum()
    # Identifying up-streaks (bounces)
    is_up = (ret > 0)
    up_streak_id = (is_up != is_up.shift()).cumsum()
    up_loss = np.exp(np.log(1 + ret).where(is_up, 0).groupby(up_streak_id).cumsum()) - 1
    # Bounces < 1%
    failed_bounce = (is_up == False) & (is_up.shift(1) == True) & (up_loss.shift(1) < 0.01)
    return failed_bounce.rolling(63).sum()

def dstk_144_down_streak_power_index_63d(close: pd.Series) -> pd.Series:
    """dstk_144_down_streak_power_index_63d feature"""
    # Duration * Mean Loss * Frequency
    d = dstk_001_consecutive_down_days(close)
    ret = close.pct_change()
    loss = (np.exp(np.log(1 + ret).where(ret < 0, 0).groupby((ret < 0).diff().ne(0).cumsum()).cumsum()) - 1).abs()
    freq = (ret < 0).rolling(63).mean()
    return d * loss * freq

def dstk_145_consecutive_days_with_oversold_rsi_14(close: pd.Series) -> pd.Series:
    """dstk_145_consecutive_days_with_oversold_rsi_14 feature"""
    # RSI implementation simplified
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = delta.where(delta < 0, 0).abs().rolling(14).mean()
    rs = _safe_div(gain, loss)
    rsi = 100 - (100 / (1 + rs))
    return _consecutive_count(rsi < 30)

def dstk_146_consecutive_days_gap_down_velocity(close: pd.Series, open: pd.Series) -> pd.Series:
    """dstk_146_consecutive_days_gap_down_velocity feature"""
    is_gap = (open < close.shift(1))
    dur = _consecutive_count(is_gap)
    gap_pct = (close.shift(1) - open) / close.shift(1)
    return dur * gap_pct

def dstk_147_days_since_5_day_up_streak_ath(close: pd.Series) -> pd.Series:
    """dstk_147_days_since_5_day_up_streak_ath feature"""
    is_up = (close > close.shift(1))
    streak = _consecutive_count(is_up)
    is_5_up = (streak >= 5)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_5_up).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices

def dstk_148_consecutive_days_decreasing_hl_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dstk_148_consecutive_days_decreasing_hl_range feature"""
    r = high - low
    return _consecutive_count(r < r.shift(1))

def dstk_149_down_streak_stability_score_63d(close: pd.Series) -> pd.Series:
    """dstk_149_down_streak_stability_score_63d feature"""
    # R-squared of consecutive down day counts (are streaks getting longer linearly?)
    is_down = (close < close.shift(1))
    dur = _consecutive_count(is_down)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    return dur.rolling(63).apply(_rsq, raw=True)

def dstk_150_consecutive_down_days_at_new_ath_low(close: pd.Series) -> pd.Series:
    """dstk_150_consecutive_down_days_at_new_ath_low feature"""
    is_low = (close == close.cummin())
    is_down = (close < close.shift(1))
    return _consecutive_count(is_low & is_down)

def dstk_096_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_076_streak_duration_pct_rank_ath"""
    return _zscore_rolling(dstk_076_streak_duration_pct_rank_ath(close), _TD_MON)

def dstk_097_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_077_streak_loss_pct_rank_ath"""
    return _rank_pct(dstk_077_streak_loss_pct_rank_ath(close), _TD_MON)

def dstk_098_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_078_streak_exhaustion_probability_63d"""
    return _zscore_rolling(dstk_078_streak_exhaustion_probability_63d(close), _TD_MON)

def dstk_099_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_091_sigma_adjusted_streak_loss_21d"""
    return _rank_pct(dstk_091_sigma_adjusted_streak_loss_21d(close), _TD_MON)

def dstk_100_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_092_count_volatile_down_streaks_252d"""
    return _zscore_rolling(dstk_092_count_volatile_down_streaks_252d(close), _TD_MON)

def dstk_101_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_106_down_streak_day_to_week_ratio"""
    return _rank_pct(dstk_106_down_streak_day_to_week_ratio(close), _TD_MON)

def dstk_102_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_107_cumulative_loss_ratio_21d_to_252d"""
    return _zscore_rolling(dstk_107_cumulative_loss_ratio_21d_to_252d(close), _TD_MON)

def dstk_103_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_126_consecutive_days_mktcap_under_ma_200"""
    return _rank_pct(dstk_126_consecutive_days_mktcap_under_ma_200(close), _TD_MON)

def dstk_104_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_127_consecutive_quarters_negative_fcf"""
    return _zscore_rolling(dstk_127_consecutive_quarters_negative_fcf(close), _TD_MON)

def dstk_105_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_128_consecutive_days_with_declining_inst_holders"""
    return _rank_pct(dstk_128_consecutive_days_with_declining_inst_holders(close), _TD_MON)

def dstk_106_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_141_streak_climax_velocity_score_21d"""
    return _zscore_rolling(dstk_141_streak_climax_velocity_score_21d(close), _TD_MON)

def dstk_107_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_142_consecutive_days_in_lowest_decile_252d"""
    return _rank_pct(dstk_142_consecutive_days_in_lowest_decile_252d(close), _TD_MON)

def dstk_108_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_143_streak_recovery_failure_count_63d"""
    return _zscore_rolling(dstk_143_streak_recovery_failure_count_63d(close), _TD_MON)

def dstk_109_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_144_down_streak_power_index_63d"""
    return _rank_pct(dstk_144_down_streak_power_index_63d(close), _TD_MON)

def dstk_110_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_145_consecutive_days_with_oversold_rsi_14"""
    return _zscore_rolling(dstk_145_consecutive_days_with_oversold_rsi_14(close), _TD_MON)

def dstk_111_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_146_consecutive_days_gap_down_velocity"""
    return _rank_pct(dstk_146_consecutive_days_gap_down_velocity(close), _TD_MON)

def dstk_112_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_147_days_since_5_day_up_streak_ath"""
    return _zscore_rolling(dstk_147_days_since_5_day_up_streak_ath(close), _TD_MON)

def dstk_113_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_148_consecutive_days_decreasing_hl_range"""
    return _rank_pct(dstk_148_consecutive_days_decreasing_hl_range(close), _TD_MON)

def dstk_114_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_149_down_streak_stability_score_63d"""
    return _zscore_rolling(dstk_149_down_streak_stability_score_63d(close), _TD_MON)

def dstk_115_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_150_consecutive_down_days_at_new_ath_low"""
    return _rank_pct(dstk_150_consecutive_down_days_at_new_ath_low(close), _TD_MON)

def dstk_116_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_076_streak_duration_pct_rank_ath"""
    return _zscore_rolling(dstk_076_streak_duration_pct_rank_ath(close), _TD_MON)

def dstk_117_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_077_streak_loss_pct_rank_ath"""
    return _rank_pct(dstk_077_streak_loss_pct_rank_ath(close), _TD_MON)

def dstk_118_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_078_streak_exhaustion_probability_63d"""
    return _zscore_rolling(dstk_078_streak_exhaustion_probability_63d(close), _TD_MON)

def dstk_119_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_091_sigma_adjusted_streak_loss_21d"""
    return _rank_pct(dstk_091_sigma_adjusted_streak_loss_21d(close), _TD_MON)

def dstk_120_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_092_count_volatile_down_streaks_252d"""
    return _zscore_rolling(dstk_092_count_volatile_down_streaks_252d(close), _TD_MON)

def dstk_121_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_106_down_streak_day_to_week_ratio"""
    return _rank_pct(dstk_106_down_streak_day_to_week_ratio(close), _TD_MON)

def dstk_122_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_107_cumulative_loss_ratio_21d_to_252d"""
    return _zscore_rolling(dstk_107_cumulative_loss_ratio_21d_to_252d(close), _TD_MON)

def dstk_123_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_126_consecutive_days_mktcap_under_ma_200"""
    return _rank_pct(dstk_126_consecutive_days_mktcap_under_ma_200(close), _TD_MON)

def dstk_124_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_127_consecutive_quarters_negative_fcf"""
    return _zscore_rolling(dstk_127_consecutive_quarters_negative_fcf(close), _TD_MON)

def dstk_125_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_128_consecutive_days_with_declining_inst_holders"""
    return _rank_pct(dstk_128_consecutive_days_with_declining_inst_holders(close), _TD_MON)

def dstk_126_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_141_streak_climax_velocity_score_21d"""
    return _zscore_rolling(dstk_141_streak_climax_velocity_score_21d(close), _TD_MON)

def dstk_127_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_142_consecutive_days_in_lowest_decile_252d"""
    return _rank_pct(dstk_142_consecutive_days_in_lowest_decile_252d(close), _TD_MON)

def dstk_128_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_143_streak_recovery_failure_count_63d"""
    return _zscore_rolling(dstk_143_streak_recovery_failure_count_63d(close), _TD_MON)

def dstk_129_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_144_down_streak_power_index_63d"""
    return _rank_pct(dstk_144_down_streak_power_index_63d(close), _TD_MON)

def dstk_130_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_145_consecutive_days_with_oversold_rsi_14"""
    return _zscore_rolling(dstk_145_consecutive_days_with_oversold_rsi_14(close), _TD_MON)

def dstk_131_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_146_consecutive_days_gap_down_velocity"""
    return _rank_pct(dstk_146_consecutive_days_gap_down_velocity(close), _TD_MON)

def dstk_132_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_147_days_since_5_day_up_streak_ath"""
    return _zscore_rolling(dstk_147_days_since_5_day_up_streak_ath(close), _TD_MON)

def dstk_133_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_148_consecutive_days_decreasing_hl_range"""
    return _rank_pct(dstk_148_consecutive_days_decreasing_hl_range(close), _TD_MON)

def dstk_134_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_149_down_streak_stability_score_63d"""
    return _zscore_rolling(dstk_149_down_streak_stability_score_63d(close), _TD_MON)

def dstk_135_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_150_consecutive_down_days_at_new_ath_low"""
    return _rank_pct(dstk_150_consecutive_down_days_at_new_ath_low(close), _TD_MON)

def dstk_136_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_076_streak_duration_pct_rank_ath"""
    return _zscore_rolling(dstk_076_streak_duration_pct_rank_ath(close), _TD_MON)

def dstk_137_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_077_streak_loss_pct_rank_ath"""
    return _rank_pct(dstk_077_streak_loss_pct_rank_ath(close), _TD_MON)

def dstk_138_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_078_streak_exhaustion_probability_63d"""
    return _zscore_rolling(dstk_078_streak_exhaustion_probability_63d(close), _TD_MON)

def dstk_139_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_091_sigma_adjusted_streak_loss_21d"""
    return _rank_pct(dstk_091_sigma_adjusted_streak_loss_21d(close), _TD_MON)

def dstk_140_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_092_count_volatile_down_streaks_252d"""
    return _zscore_rolling(dstk_092_count_volatile_down_streaks_252d(close), _TD_MON)

def dstk_141_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_106_down_streak_day_to_week_ratio"""
    return _rank_pct(dstk_106_down_streak_day_to_week_ratio(close), _TD_MON)

def dstk_142_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_107_cumulative_loss_ratio_21d_to_252d"""
    return _zscore_rolling(dstk_107_cumulative_loss_ratio_21d_to_252d(close), _TD_MON)

def dstk_143_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_126_consecutive_days_mktcap_under_ma_200"""
    return _rank_pct(dstk_126_consecutive_days_mktcap_under_ma_200(close), _TD_MON)

def dstk_144_stat_depth_var_48(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_127_consecutive_quarters_negative_fcf"""
    return _zscore_rolling(dstk_127_consecutive_quarters_negative_fcf(close), _TD_MON)

def dstk_145_stat_depth_var_49(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_128_consecutive_days_with_declining_inst_holders"""
    return _rank_pct(dstk_128_consecutive_days_with_declining_inst_holders(close), _TD_MON)

def dstk_146_stat_depth_var_50(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_141_streak_climax_velocity_score_21d"""
    return _zscore_rolling(dstk_141_streak_climax_velocity_score_21d(close), _TD_MON)

def dstk_147_stat_depth_var_51(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_142_consecutive_days_in_lowest_decile_252d"""
    return _rank_pct(dstk_142_consecutive_days_in_lowest_decile_252d(close), _TD_MON)

def dstk_148_stat_depth_var_52(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_143_streak_recovery_failure_count_63d"""
    return _zscore_rolling(dstk_143_streak_recovery_failure_count_63d(close), _TD_MON)

def dstk_149_stat_depth_var_53(close: pd.Series) -> pd.Series:
    """_rank_pct variation of dstk_144_down_streak_power_index_63d"""
    return _rank_pct(dstk_144_down_streak_power_index_63d(close), _TD_MON)

def dstk_150_stat_depth_var_54(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of dstk_145_consecutive_days_with_oversold_rsi_14"""
    return _zscore_rolling(dstk_145_consecutive_days_with_oversold_rsi_14(close), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V08_REGISTRY = {
    "dstk_076_streak_duration_pct_rank_ath": {"inputs": ["close"], "func": dstk_076_streak_duration_pct_rank_ath},
    "dstk_077_streak_loss_pct_rank_ath": {"inputs": ["close"], "func": dstk_077_streak_loss_pct_rank_ath},
    "dstk_078_streak_exhaustion_probability_63d": {"inputs": ["close"], "func": dstk_078_streak_exhaustion_probability_63d},
    "dstk_091_sigma_adjusted_streak_loss_21d": {"inputs": ["close"], "func": dstk_091_sigma_adjusted_streak_loss_21d},
    "dstk_092_count_volatile_down_streaks_252d": {"inputs": ["close"], "func": dstk_092_count_volatile_down_streaks_252d},
    "dstk_106_down_streak_day_to_week_ratio": {"inputs": ["close"], "func": dstk_106_down_streak_day_to_week_ratio},
    "dstk_107_cumulative_loss_ratio_21d_to_252d": {"inputs": ["close"], "func": dstk_107_cumulative_loss_ratio_21d_to_252d},
    "dstk_126_consecutive_days_mktcap_under_ma_200": {"inputs": ["close", "sharesbas"], "func": dstk_126_consecutive_days_mktcap_under_ma_200},
    "dstk_127_consecutive_quarters_negative_fcf": {"inputs": ["fcf"], "func": dstk_127_consecutive_quarters_negative_fcf},
    "dstk_128_consecutive_days_with_declining_inst_holders": {"inputs": ["inst_holders"], "func": dstk_128_consecutive_days_with_declining_inst_holders},
    "dstk_141_streak_climax_velocity_score_21d": {"inputs": ["close"], "func": dstk_141_streak_climax_velocity_score_21d},
    "dstk_142_consecutive_days_in_lowest_decile_252d": {"inputs": ["close"], "func": dstk_142_consecutive_days_in_lowest_decile_252d},
    "dstk_143_streak_recovery_failure_count_63d": {"inputs": ["close"], "func": dstk_143_streak_recovery_failure_count_63d},
    "dstk_144_down_streak_power_index_63d": {"inputs": ["close"], "func": dstk_144_down_streak_power_index_63d},
    "dstk_145_consecutive_days_with_oversold_rsi_14": {"inputs": ["close"], "func": dstk_145_consecutive_days_with_oversold_rsi_14},
    "dstk_146_consecutive_days_gap_down_velocity": {"inputs": ["close", "open"], "func": dstk_146_consecutive_days_gap_down_velocity},
    "dstk_147_days_since_5_day_up_streak_ath": {"inputs": ["close"], "func": dstk_147_days_since_5_day_up_streak_ath},
    "dstk_148_consecutive_days_decreasing_hl_range": {"inputs": ["close", "high", "low"], "func": dstk_148_consecutive_days_decreasing_hl_range},
    "dstk_149_down_streak_stability_score_63d": {"inputs": ["close"], "func": dstk_149_down_streak_stability_score_63d},
    "dstk_150_consecutive_down_days_at_new_ath_low": {"inputs": ["close"], "func": dstk_150_consecutive_down_days_at_new_ath_low},
    "dstk_096_stat_depth_var_0": {"inputs": ["close"], "func": dstk_096_stat_depth_var_0},
    "dstk_097_stat_depth_var_1": {"inputs": ["close"], "func": dstk_097_stat_depth_var_1},
    "dstk_098_stat_depth_var_2": {"inputs": ["close"], "func": dstk_098_stat_depth_var_2},
    "dstk_099_stat_depth_var_3": {"inputs": ["close"], "func": dstk_099_stat_depth_var_3},
    "dstk_100_stat_depth_var_4": {"inputs": ["close"], "func": dstk_100_stat_depth_var_4},
    "dstk_101_stat_depth_var_5": {"inputs": ["close"], "func": dstk_101_stat_depth_var_5},
    "dstk_102_stat_depth_var_6": {"inputs": ["close"], "func": dstk_102_stat_depth_var_6},
    "dstk_103_stat_depth_var_7": {"inputs": ["close"], "func": dstk_103_stat_depth_var_7},
    "dstk_104_stat_depth_var_8": {"inputs": ["close"], "func": dstk_104_stat_depth_var_8},
    "dstk_105_stat_depth_var_9": {"inputs": ["close"], "func": dstk_105_stat_depth_var_9},
    "dstk_106_stat_depth_var_10": {"inputs": ["close"], "func": dstk_106_stat_depth_var_10},
    "dstk_107_stat_depth_var_11": {"inputs": ["close"], "func": dstk_107_stat_depth_var_11},
    "dstk_108_stat_depth_var_12": {"inputs": ["close"], "func": dstk_108_stat_depth_var_12},
    "dstk_109_stat_depth_var_13": {"inputs": ["close"], "func": dstk_109_stat_depth_var_13},
    "dstk_110_stat_depth_var_14": {"inputs": ["close"], "func": dstk_110_stat_depth_var_14},
    "dstk_111_stat_depth_var_15": {"inputs": ["close"], "func": dstk_111_stat_depth_var_15},
    "dstk_112_stat_depth_var_16": {"inputs": ["close"], "func": dstk_112_stat_depth_var_16},
    "dstk_113_stat_depth_var_17": {"inputs": ["close"], "func": dstk_113_stat_depth_var_17},
    "dstk_114_stat_depth_var_18": {"inputs": ["close"], "func": dstk_114_stat_depth_var_18},
    "dstk_115_stat_depth_var_19": {"inputs": ["close"], "func": dstk_115_stat_depth_var_19},
    "dstk_116_stat_depth_var_20": {"inputs": ["close"], "func": dstk_116_stat_depth_var_20},
    "dstk_117_stat_depth_var_21": {"inputs": ["close"], "func": dstk_117_stat_depth_var_21},
    "dstk_118_stat_depth_var_22": {"inputs": ["close"], "func": dstk_118_stat_depth_var_22},
    "dstk_119_stat_depth_var_23": {"inputs": ["close"], "func": dstk_119_stat_depth_var_23},
    "dstk_120_stat_depth_var_24": {"inputs": ["close"], "func": dstk_120_stat_depth_var_24},
    "dstk_121_stat_depth_var_25": {"inputs": ["close"], "func": dstk_121_stat_depth_var_25},
    "dstk_122_stat_depth_var_26": {"inputs": ["close"], "func": dstk_122_stat_depth_var_26},
    "dstk_123_stat_depth_var_27": {"inputs": ["close"], "func": dstk_123_stat_depth_var_27},
    "dstk_124_stat_depth_var_28": {"inputs": ["close"], "func": dstk_124_stat_depth_var_28},
    "dstk_125_stat_depth_var_29": {"inputs": ["close"], "func": dstk_125_stat_depth_var_29},
    "dstk_126_stat_depth_var_30": {"inputs": ["close"], "func": dstk_126_stat_depth_var_30},
    "dstk_127_stat_depth_var_31": {"inputs": ["close"], "func": dstk_127_stat_depth_var_31},
    "dstk_128_stat_depth_var_32": {"inputs": ["close"], "func": dstk_128_stat_depth_var_32},
    "dstk_129_stat_depth_var_33": {"inputs": ["close"], "func": dstk_129_stat_depth_var_33},
    "dstk_130_stat_depth_var_34": {"inputs": ["close"], "func": dstk_130_stat_depth_var_34},
    "dstk_131_stat_depth_var_35": {"inputs": ["close"], "func": dstk_131_stat_depth_var_35},
    "dstk_132_stat_depth_var_36": {"inputs": ["close"], "func": dstk_132_stat_depth_var_36},
    "dstk_133_stat_depth_var_37": {"inputs": ["close"], "func": dstk_133_stat_depth_var_37},
    "dstk_134_stat_depth_var_38": {"inputs": ["close"], "func": dstk_134_stat_depth_var_38},
    "dstk_135_stat_depth_var_39": {"inputs": ["close"], "func": dstk_135_stat_depth_var_39},
    "dstk_136_stat_depth_var_40": {"inputs": ["close"], "func": dstk_136_stat_depth_var_40},
    "dstk_137_stat_depth_var_41": {"inputs": ["close"], "func": dstk_137_stat_depth_var_41},
    "dstk_138_stat_depth_var_42": {"inputs": ["close"], "func": dstk_138_stat_depth_var_42},
    "dstk_139_stat_depth_var_43": {"inputs": ["close"], "func": dstk_139_stat_depth_var_43},
    "dstk_140_stat_depth_var_44": {"inputs": ["close"], "func": dstk_140_stat_depth_var_44},
    "dstk_141_stat_depth_var_45": {"inputs": ["close"], "func": dstk_141_stat_depth_var_45},
    "dstk_142_stat_depth_var_46": {"inputs": ["close"], "func": dstk_142_stat_depth_var_46},
    "dstk_143_stat_depth_var_47": {"inputs": ["close"], "func": dstk_143_stat_depth_var_47},
    "dstk_144_stat_depth_var_48": {"inputs": ["close"], "func": dstk_144_stat_depth_var_48},
    "dstk_145_stat_depth_var_49": {"inputs": ["close"], "func": dstk_145_stat_depth_var_49},
    "dstk_146_stat_depth_var_50": {"inputs": ["close"], "func": dstk_146_stat_depth_var_50},
    "dstk_147_stat_depth_var_51": {"inputs": ["close"], "func": dstk_147_stat_depth_var_51},
    "dstk_148_stat_depth_var_52": {"inputs": ["close"], "func": dstk_148_stat_depth_var_52},
    "dstk_149_stat_depth_var_53": {"inputs": ["close"], "func": dstk_149_stat_depth_var_53},
    "dstk_150_stat_depth_var_54": {"inputs": ["close"], "func": dstk_150_stat_depth_var_54},
}
