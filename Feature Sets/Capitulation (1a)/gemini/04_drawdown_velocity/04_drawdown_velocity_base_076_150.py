"""
Drawdown Velocity — Base Features 076–150
Domain: speed and momentum of decline
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

def dvel_076_velocity_ratio_early_vs_late_63d(close: pd.Series) -> pd.Series:
    """dvel_076_velocity_ratio_early_vs_late_63d"""
    v = np.log(close).diff(1)
    def _v_ratio(y):
        mid = len(y) // 2
        v1 = np.mean(y[:mid])
        v2 = np.mean(y[mid:])
        return _safe_div(pd.Series(v2), pd.Series(v1)).iloc[0]
    return v.rolling(63).apply(_v_ratio, raw=True)

def dvel_077_velocity_gradient_63d(close: pd.Series) -> pd.Series:
    """dvel_077_velocity_gradient_63d"""
    # Change in velocity per day
    v = np.log(close).diff(5) / 5.0
    return _rolling_slope(v, 63)

def dvel_078_velocity_relative_to_5y_min(close: pd.Series) -> pd.Series:
    """dvel_078_velocity_relative_to_5y_min"""
    v = np.log(close).diff(21) / 21.0
    v_min = v.rolling(252 * 5).min()
    return _safe_div(v, v_min)

def dvel_079_velocity_acceleration_ratio_21d(close: pd.Series) -> pd.Series:
    """dvel_079_velocity_acceleration_ratio_21d"""
    # Ratio of current acceleration to past acceleration
    accel = np.log(close).diff(1).diff(1)
    return _safe_div(accel.rolling(5).mean(), accel.rolling(21).mean())


# 091-105: Threshold-Based Velocity Counts

def dvel_091_days_at_extreme_negative_velocity_63d(close: pd.Series) -> pd.Series:
    """dvel_091_days_at_extreme_negative_velocity_63d feature"""
    v = np.log(close).diff(1)
    threshold = v.rolling(252).mean() - 2 * v.rolling(252).std()
    return (v < threshold).rolling(63).sum()

def dvel_092_count_velocity_reversals_63d(close: pd.Series) -> pd.Series:
    """dvel_092_count_velocity_reversals_63d"""
    # Count of times velocity sign changes
    v = np.log(close).diff(5)
    reversal = (np.sign(v) != np.sign(v.shift(1))).astype(int)
    return reversal.rolling(63).sum()

def dvel_093_consecutive_negative_velocity_days(close: pd.Series) -> pd.Series:
    """dvel_093_consecutive_negative_velocity_days"""
    v = np.log(close).diff(1)
    is_neg = (v < 0).astype(int)
    return is_neg.groupby((is_neg == 0).cumsum()).cumsum()


# 106-125: Regression-Based Velocity Components

def dvel_106_log_price_slope_stability_63d(close: pd.Series) -> pd.Series:
    """dvel_106_log_price_slope_stability_63d feature"""
    # R-squared of log price regression
    def _rsq(y):
        if len(y) < 2: return np.nan
        return linregress(np.arange(len(y)), y).rvalue**2
    return np.log(close).rolling(63).apply(_rsq, raw=True)

def dvel_107_velocity_residual_std_63d(close: pd.Series) -> pd.Series:
    """dvel_107_velocity_residual_std_63d"""
    # Std dev of log price from its linear trend
    def _res_std(y):
        x = np.arange(len(y))
        res = linregress(x, y)
        y_fit = res.intercept + res.slope * x
        return np.std(y - y_fit)
    return np.log(close).rolling(63).apply(_res_std, raw=True)

def dvel_108_velocity_jump_ratio_21d(close: pd.Series) -> pd.Series:
    """dvel_108_velocity_jump_ratio_21d"""
    # Current daily drop / Max daily drop in last 21 days
    v = np.log(close).diff(1).abs()
    return _safe_div(v, v.rolling(21).max())


# 126-140: Event-Driven Velocity Proxies

def dvel_126_velocity_at_earnings_surprise(close: pd.Series, surprise: pd.Series) -> pd.Series:
    """dvel_126_velocity_at_earnings_surprise feature"""
    v = np.log(close).diff(5)
    return v.where(surprise.abs() > 0).ffill()

def dvel_127_velocity_since_last_dividend(close: pd.Series, dividend: pd.Series) -> pd.Series:
    """dvel_127_velocity_since_last_dividend"""
    v = np.log(close).diff(21)
    indices = pd.Series(np.arange(len(dividend)), index=dividend.index).where(dividend > 0).ffill()
    dist = pd.Series(np.arange(len(dividend)), index=dividend.index) - indices
    return v.where(dist < 21)


# 141-150: Final velocity composites

def dvel_141_mktcap_velocity_to_price_velocity_ratio(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dvel_141_mktcap_velocity_to_price_velocity_ratio feature"""
    v_p = np.log(close).diff(21)
    v_mc = np.log(close * sharesbas).diff(21)
    return _safe_div(v_mc, v_p)

def dvel_142_velocity_to_atr_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dvel_142_velocity_to_atr_ratio_63d"""
    v = np.log(close).diff(21).abs()
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(63).mean() / close.rolling(63).mean()
    return _safe_div(v, atr)

def dvel_143_terminal_velocity_decay_score(close: pd.Series) -> pd.Series:
    """dvel_143_terminal_velocity_decay_score"""
    # Difference between 5-day slope and 21-day slope
    return _rolling_slope(np.log(close), 5) - _rolling_slope(np.log(close), 21)

def dvel_144_drawdown_velocity_inflection_score(close: pd.Series) -> pd.Series:
    """dvel_144_drawdown_velocity_inflection_score"""
    # 2nd derivative sign of log price
    v = np.log(close).diff(5)
    return np.sign(v.diff(5))

def dvel_145_velocity_at_ath_drawdown_max(close: pd.Series) -> pd.Series:
    """dvel_145_velocity_at_ath_drawdown_max"""
    v = np.log(close).diff(21)
    h = close.cummax()
    dd = (h - close) / h
    return v.where(dd == dd.expanding().max())

def dvel_146_velocity_rank_vs_sector_proxy(close: pd.Series) -> pd.Series:
    """dvel_146_velocity_rank_vs_sector_proxy"""
    # Since we can't see other tickers, we compare current velocity to its 5y distribution
    v = np.log(close).diff(21)
    return v.rolling(252 * 5).rank(pct=True)

def dvel_147_days_spent_in_high_velocity_regime_63d(close: pd.Series) -> pd.Series:
    """dvel_147_days_spent_in_high_velocity_regime_63d"""
    v = np.log(close).diff(5).abs()
    threshold = v.rolling(252).mean() + 1.5 * v.rolling(252).std()
    return (v > threshold).rolling(63).sum()

def dvel_148_velocity_to_volume_divergence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dvel_148_velocity_to_volume_divergence_21d"""
    # Price velocity (negative) vs Volume velocity (positive)
    v_p = np.log(close).diff(5)
    v_v = np.log(volume).diff(5)
    return v_v.where(v_p < 0)

def dvel_149_weighted_velocity_sum_252d(close: pd.Series) -> pd.Series:
    """dvel_149_weighted_velocity_sum_252d"""
    v21 = np.log(close).diff(21)
    v63 = np.log(close).diff(63)
    v252 = np.log(close).diff(252)
    return (v21 + v63 + v252) / 3.0

def dvel_150_velocity_climax_score(close: pd.Series) -> pd.Series:
    """dvel_150_velocity_climax_score"""
    # Normalized velocity * Normalized Range
    v = np.log(close).diff(5).abs()
    v_norm = _safe_div(v - v.rolling(63).mean(), v.rolling(63).std())
    r = (close.expanding().max() - close.expanding().min()) / close.expanding().max()
    return v_norm * r

def dvel_094_variation_0(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_076_velocity_ratio_early_vs_late_63d"""
    base_feat = dvel_076_velocity_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_095_variation_1(close: pd.Series) -> pd.Series:
    """rank variation of dvel_077_velocity_gradient_63d"""
    base_feat = dvel_077_velocity_gradient_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_096_variation_2(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_078_velocity_relative_to_5y_min"""
    base_feat = dvel_078_velocity_relative_to_5y_min(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_097_variation_3(close: pd.Series) -> pd.Series:
    """rank variation of dvel_079_velocity_acceleration_ratio_21d"""
    base_feat = dvel_079_velocity_acceleration_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_098_variation_4(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_092_count_velocity_reversals_63d"""
    base_feat = dvel_092_count_velocity_reversals_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_099_variation_5(close: pd.Series) -> pd.Series:
    """rank variation of dvel_093_consecutive_negative_velocity_days"""
    base_feat = dvel_093_consecutive_negative_velocity_days(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_100_variation_6(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_107_velocity_residual_std_63d"""
    base_feat = dvel_107_velocity_residual_std_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_101_variation_7(close: pd.Series) -> pd.Series:
    """rank variation of dvel_108_velocity_jump_ratio_21d"""
    base_feat = dvel_108_velocity_jump_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_102_variation_8(close: pd.Series, dividend: pd.Series) -> pd.Series:
    """zscore variation of dvel_127_velocity_since_last_dividend"""
    base_feat = dvel_127_velocity_since_last_dividend(close,dividend)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_103_variation_9(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """rank variation of dvel_142_velocity_to_atr_ratio_63d"""
    base_feat = dvel_142_velocity_to_atr_ratio_63d(close,high,low)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_104_variation_10(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_076_velocity_ratio_early_vs_late_63d"""
    base_feat = dvel_076_velocity_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_105_variation_11(close: pd.Series) -> pd.Series:
    """rank variation of dvel_077_velocity_gradient_63d"""
    base_feat = dvel_077_velocity_gradient_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_106_variation_12(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_078_velocity_relative_to_5y_min"""
    base_feat = dvel_078_velocity_relative_to_5y_min(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_107_variation_13(close: pd.Series) -> pd.Series:
    """rank variation of dvel_079_velocity_acceleration_ratio_21d"""
    base_feat = dvel_079_velocity_acceleration_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_108_variation_14(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_092_count_velocity_reversals_63d"""
    base_feat = dvel_092_count_velocity_reversals_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_109_variation_15(close: pd.Series) -> pd.Series:
    """rank variation of dvel_093_consecutive_negative_velocity_days"""
    base_feat = dvel_093_consecutive_negative_velocity_days(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_110_variation_16(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_107_velocity_residual_std_63d"""
    base_feat = dvel_107_velocity_residual_std_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_111_variation_17(close: pd.Series) -> pd.Series:
    """rank variation of dvel_108_velocity_jump_ratio_21d"""
    base_feat = dvel_108_velocity_jump_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_112_variation_18(close: pd.Series, dividend: pd.Series) -> pd.Series:
    """zscore variation of dvel_127_velocity_since_last_dividend"""
    base_feat = dvel_127_velocity_since_last_dividend(close,dividend)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_113_variation_19(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """rank variation of dvel_142_velocity_to_atr_ratio_63d"""
    base_feat = dvel_142_velocity_to_atr_ratio_63d(close,high,low)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_114_variation_20(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_076_velocity_ratio_early_vs_late_63d"""
    base_feat = dvel_076_velocity_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_115_variation_21(close: pd.Series) -> pd.Series:
    """rank variation of dvel_077_velocity_gradient_63d"""
    base_feat = dvel_077_velocity_gradient_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_116_variation_22(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_078_velocity_relative_to_5y_min"""
    base_feat = dvel_078_velocity_relative_to_5y_min(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_117_variation_23(close: pd.Series) -> pd.Series:
    """rank variation of dvel_079_velocity_acceleration_ratio_21d"""
    base_feat = dvel_079_velocity_acceleration_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_118_variation_24(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_092_count_velocity_reversals_63d"""
    base_feat = dvel_092_count_velocity_reversals_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_119_variation_25(close: pd.Series) -> pd.Series:
    """rank variation of dvel_093_consecutive_negative_velocity_days"""
    base_feat = dvel_093_consecutive_negative_velocity_days(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_120_variation_26(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_107_velocity_residual_std_63d"""
    base_feat = dvel_107_velocity_residual_std_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_121_variation_27(close: pd.Series) -> pd.Series:
    """rank variation of dvel_108_velocity_jump_ratio_21d"""
    base_feat = dvel_108_velocity_jump_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_122_variation_28(close: pd.Series, dividend: pd.Series) -> pd.Series:
    """zscore variation of dvel_127_velocity_since_last_dividend"""
    base_feat = dvel_127_velocity_since_last_dividend(close,dividend)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_123_variation_29(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """rank variation of dvel_142_velocity_to_atr_ratio_63d"""
    base_feat = dvel_142_velocity_to_atr_ratio_63d(close,high,low)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_124_variation_30(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_076_velocity_ratio_early_vs_late_63d"""
    base_feat = dvel_076_velocity_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_125_variation_31(close: pd.Series) -> pd.Series:
    """rank variation of dvel_077_velocity_gradient_63d"""
    base_feat = dvel_077_velocity_gradient_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_126_variation_32(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_078_velocity_relative_to_5y_min"""
    base_feat = dvel_078_velocity_relative_to_5y_min(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_127_variation_33(close: pd.Series) -> pd.Series:
    """rank variation of dvel_079_velocity_acceleration_ratio_21d"""
    base_feat = dvel_079_velocity_acceleration_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_128_variation_34(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_092_count_velocity_reversals_63d"""
    base_feat = dvel_092_count_velocity_reversals_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_129_variation_35(close: pd.Series) -> pd.Series:
    """rank variation of dvel_093_consecutive_negative_velocity_days"""
    base_feat = dvel_093_consecutive_negative_velocity_days(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_130_variation_36(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_107_velocity_residual_std_63d"""
    base_feat = dvel_107_velocity_residual_std_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_131_variation_37(close: pd.Series) -> pd.Series:
    """rank variation of dvel_108_velocity_jump_ratio_21d"""
    base_feat = dvel_108_velocity_jump_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_132_variation_38(close: pd.Series, dividend: pd.Series) -> pd.Series:
    """zscore variation of dvel_127_velocity_since_last_dividend"""
    base_feat = dvel_127_velocity_since_last_dividend(close,dividend)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_133_variation_39(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """rank variation of dvel_142_velocity_to_atr_ratio_63d"""
    base_feat = dvel_142_velocity_to_atr_ratio_63d(close,high,low)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_134_variation_40(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_076_velocity_ratio_early_vs_late_63d"""
    base_feat = dvel_076_velocity_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_135_variation_41(close: pd.Series) -> pd.Series:
    """rank variation of dvel_077_velocity_gradient_63d"""
    base_feat = dvel_077_velocity_gradient_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_136_variation_42(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_078_velocity_relative_to_5y_min"""
    base_feat = dvel_078_velocity_relative_to_5y_min(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_137_variation_43(close: pd.Series) -> pd.Series:
    """rank variation of dvel_079_velocity_acceleration_ratio_21d"""
    base_feat = dvel_079_velocity_acceleration_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_138_variation_44(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_092_count_velocity_reversals_63d"""
    base_feat = dvel_092_count_velocity_reversals_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_139_variation_45(close: pd.Series) -> pd.Series:
    """rank variation of dvel_093_consecutive_negative_velocity_days"""
    base_feat = dvel_093_consecutive_negative_velocity_days(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_140_variation_46(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_107_velocity_residual_std_63d"""
    base_feat = dvel_107_velocity_residual_std_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_141_variation_47(close: pd.Series) -> pd.Series:
    """rank variation of dvel_108_velocity_jump_ratio_21d"""
    base_feat = dvel_108_velocity_jump_ratio_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_142_variation_48(close: pd.Series, dividend: pd.Series) -> pd.Series:
    """zscore variation of dvel_127_velocity_since_last_dividend"""
    base_feat = dvel_127_velocity_since_last_dividend(close,dividend)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_143_variation_49(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """rank variation of dvel_142_velocity_to_atr_ratio_63d"""
    base_feat = dvel_142_velocity_to_atr_ratio_63d(close,high,low)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_144_variation_50(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_076_velocity_ratio_early_vs_late_63d"""
    base_feat = dvel_076_velocity_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_145_variation_51(close: pd.Series) -> pd.Series:
    """rank variation of dvel_077_velocity_gradient_63d"""
    base_feat = dvel_077_velocity_gradient_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_146_variation_52(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_078_velocity_relative_to_5y_min"""
    base_feat = dvel_078_velocity_relative_to_5y_min(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V04_REGISTRY = {
    "dvel_076_velocity_ratio_early_vs_late_63d": {"inputs": ["close"], "func": dvel_076_velocity_ratio_early_vs_late_63d},
    "dvel_077_velocity_gradient_63d": {"inputs": ["close"], "func": dvel_077_velocity_gradient_63d},
    "dvel_078_velocity_relative_to_5y_min": {"inputs": ["close"], "func": dvel_078_velocity_relative_to_5y_min},
    "dvel_079_velocity_acceleration_ratio_21d": {"inputs": ["close"], "func": dvel_079_velocity_acceleration_ratio_21d},
    "dvel_091_days_at_extreme_negative_velocity_63d": {"inputs": ["close"], "func": dvel_091_days_at_extreme_negative_velocity_63d},
    "dvel_092_count_velocity_reversals_63d": {"inputs": ["close"], "func": dvel_092_count_velocity_reversals_63d},
    "dvel_093_consecutive_negative_velocity_days": {"inputs": ["close"], "func": dvel_093_consecutive_negative_velocity_days},
    "dvel_106_log_price_slope_stability_63d": {"inputs": ["close"], "func": dvel_106_log_price_slope_stability_63d},
    "dvel_107_velocity_residual_std_63d": {"inputs": ["close"], "func": dvel_107_velocity_residual_std_63d},
    "dvel_108_velocity_jump_ratio_21d": {"inputs": ["close"], "func": dvel_108_velocity_jump_ratio_21d},
    "dvel_126_velocity_at_earnings_surprise": {"inputs": ["close", "surprise"], "func": dvel_126_velocity_at_earnings_surprise},
    "dvel_127_velocity_since_last_dividend": {"inputs": ["close", "dividend"], "func": dvel_127_velocity_since_last_dividend},
    "dvel_141_mktcap_velocity_to_price_velocity_ratio": {"inputs": ["close", "sharesbas"], "func": dvel_141_mktcap_velocity_to_price_velocity_ratio},
    "dvel_142_velocity_to_atr_ratio_63d": {"inputs": ["close", "high", "low"], "func": dvel_142_velocity_to_atr_ratio_63d},
    "dvel_143_terminal_velocity_decay_score": {"inputs": ["close"], "func": dvel_143_terminal_velocity_decay_score},
    "dvel_144_drawdown_velocity_inflection_score": {"inputs": ["close"], "func": dvel_144_drawdown_velocity_inflection_score},
    "dvel_145_velocity_at_ath_drawdown_max": {"inputs": ["close"], "func": dvel_145_velocity_at_ath_drawdown_max},
    "dvel_146_velocity_rank_vs_sector_proxy": {"inputs": ["close"], "func": dvel_146_velocity_rank_vs_sector_proxy},
    "dvel_147_days_spent_in_high_velocity_regime_63d": {"inputs": ["close"], "func": dvel_147_days_spent_in_high_velocity_regime_63d},
    "dvel_148_velocity_to_volume_divergence_21d": {"inputs": ["close", "volume"], "func": dvel_148_velocity_to_volume_divergence_21d},
    "dvel_149_weighted_velocity_sum_252d": {"inputs": ["close"], "func": dvel_149_weighted_velocity_sum_252d},
    "dvel_150_velocity_climax_score": {"inputs": ["close"], "func": dvel_150_velocity_climax_score},
    "dvel_094_variation_0": {"inputs": ["close"], "func": dvel_094_variation_0},
    "dvel_095_variation_1": {"inputs": ["close"], "func": dvel_095_variation_1},
    "dvel_096_variation_2": {"inputs": ["close"], "func": dvel_096_variation_2},
    "dvel_097_variation_3": {"inputs": ["close"], "func": dvel_097_variation_3},
    "dvel_098_variation_4": {"inputs": ["close"], "func": dvel_098_variation_4},
    "dvel_099_variation_5": {"inputs": ["close"], "func": dvel_099_variation_5},
    "dvel_100_variation_6": {"inputs": ["close"], "func": dvel_100_variation_6},
    "dvel_101_variation_7": {"inputs": ["close"], "func": dvel_101_variation_7},
    "dvel_102_variation_8": {"inputs": ["close", "dividend"], "func": dvel_102_variation_8},
    "dvel_103_variation_9": {"inputs": ["close", "high", "low"], "func": dvel_103_variation_9},
    "dvel_104_variation_10": {"inputs": ["close"], "func": dvel_104_variation_10},
    "dvel_105_variation_11": {"inputs": ["close"], "func": dvel_105_variation_11},
    "dvel_106_variation_12": {"inputs": ["close"], "func": dvel_106_variation_12},
    "dvel_107_variation_13": {"inputs": ["close"], "func": dvel_107_variation_13},
    "dvel_108_variation_14": {"inputs": ["close"], "func": dvel_108_variation_14},
    "dvel_109_variation_15": {"inputs": ["close"], "func": dvel_109_variation_15},
    "dvel_110_variation_16": {"inputs": ["close"], "func": dvel_110_variation_16},
    "dvel_111_variation_17": {"inputs": ["close"], "func": dvel_111_variation_17},
    "dvel_112_variation_18": {"inputs": ["close", "dividend"], "func": dvel_112_variation_18},
    "dvel_113_variation_19": {"inputs": ["close", "high", "low"], "func": dvel_113_variation_19},
    "dvel_114_variation_20": {"inputs": ["close"], "func": dvel_114_variation_20},
    "dvel_115_variation_21": {"inputs": ["close"], "func": dvel_115_variation_21},
    "dvel_116_variation_22": {"inputs": ["close"], "func": dvel_116_variation_22},
    "dvel_117_variation_23": {"inputs": ["close"], "func": dvel_117_variation_23},
    "dvel_118_variation_24": {"inputs": ["close"], "func": dvel_118_variation_24},
    "dvel_119_variation_25": {"inputs": ["close"], "func": dvel_119_variation_25},
    "dvel_120_variation_26": {"inputs": ["close"], "func": dvel_120_variation_26},
    "dvel_121_variation_27": {"inputs": ["close"], "func": dvel_121_variation_27},
    "dvel_122_variation_28": {"inputs": ["close", "dividend"], "func": dvel_122_variation_28},
    "dvel_123_variation_29": {"inputs": ["close", "high", "low"], "func": dvel_123_variation_29},
    "dvel_124_variation_30": {"inputs": ["close"], "func": dvel_124_variation_30},
    "dvel_125_variation_31": {"inputs": ["close"], "func": dvel_125_variation_31},
    "dvel_126_variation_32": {"inputs": ["close"], "func": dvel_126_variation_32},
    "dvel_127_variation_33": {"inputs": ["close"], "func": dvel_127_variation_33},
    "dvel_128_variation_34": {"inputs": ["close"], "func": dvel_128_variation_34},
    "dvel_129_variation_35": {"inputs": ["close"], "func": dvel_129_variation_35},
    "dvel_130_variation_36": {"inputs": ["close"], "func": dvel_130_variation_36},
    "dvel_131_variation_37": {"inputs": ["close"], "func": dvel_131_variation_37},
    "dvel_132_variation_38": {"inputs": ["close", "dividend"], "func": dvel_132_variation_38},
    "dvel_133_variation_39": {"inputs": ["close", "high", "low"], "func": dvel_133_variation_39},
    "dvel_134_variation_40": {"inputs": ["close"], "func": dvel_134_variation_40},
    "dvel_135_variation_41": {"inputs": ["close"], "func": dvel_135_variation_41},
    "dvel_136_variation_42": {"inputs": ["close"], "func": dvel_136_variation_42},
    "dvel_137_variation_43": {"inputs": ["close"], "func": dvel_137_variation_43},
    "dvel_138_variation_44": {"inputs": ["close"], "func": dvel_138_variation_44},
    "dvel_139_variation_45": {"inputs": ["close"], "func": dvel_139_variation_45},
    "dvel_140_variation_46": {"inputs": ["close"], "func": dvel_140_variation_46},
    "dvel_141_variation_47": {"inputs": ["close"], "func": dvel_141_variation_47},
    "dvel_142_variation_48": {"inputs": ["close", "dividend"], "func": dvel_142_variation_48},
    "dvel_143_variation_49": {"inputs": ["close", "high", "low"], "func": dvel_143_variation_49},
    "dvel_144_variation_50": {"inputs": ["close"], "func": dvel_144_variation_50},
    "dvel_145_variation_51": {"inputs": ["close"], "func": dvel_145_variation_51},
    "dvel_146_variation_52": {"inputs": ["close"], "func": dvel_146_variation_52},
}
