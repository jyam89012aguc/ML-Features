"""
Peak to Trough — Base Features 076–150
Domain: amplitude of high to low swings
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

def ptt_076_ptt_ratio_pct_rank_ath(close: pd.Series) -> pd.Series:
    """ptt_076_ptt_ratio_pct_rank_ath feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    return r.expanding().rank(pct=True)

def ptt_077_recovery_fraction_zscore_252d(close: pd.Series) -> pd.Series:
    """ptt_077_recovery_fraction_zscore_252d feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    rf = _safe_div(close - l, h - l)
    return (rf - rf.rolling(252).mean()) / rf.rolling(252).std()

def ptt_078_ptt_volatility_ratio_63d(close: pd.Series) -> pd.Series:
    """ptt_078_ptt_volatility_ratio_63d feature"""
    # Std dev of PTT ratio vs mean PTT ratio
    r = _safe_div(_rolling_max(close, 21), _rolling_min(close, 21))
    return _safe_div(r.rolling(63).std(), r.rolling(63).mean())


# 091-105: Trough Re-test and Stability metrics

def ptt_091_count_double_bottom_attempts_252d(close: pd.Series) -> pd.Series:
    """ptt_091_count_double_bottom_attempts_252d feature"""
    # Days within 2% of the previous year's absolute low
    l = _rolling_min(close, 252)
    at_low = (close <= l * 1.02).astype(int)
    return at_low.rolling(252).sum()

def ptt_092_recovery_fraction_mean_reversion_score_21d(close: pd.Series) -> pd.Series:
    """ptt_092_recovery_fraction_mean_reversion_score_21d feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    return (rf - rf.rolling(21).mean()) / rf.rolling(21).std()


# 106-125: Event-Driven Peak-to-Trough Metrics

def ptt_106_ptt_ratio_since_insider_buy_cluster(close: pd.Series, insider_buys: pd.Series) -> pd.Series:
    """ptt_106_ptt_ratio_since_insider_buy_cluster feature"""
    # PTT ratio calculated only since the last significant insider cluster
    indices = pd.Series(np.arange(len(insider_buys)), index=insider_buys.index).where(insider_buys > 1).ffill()
    dist = pd.Series(np.arange(len(close)), index=close.index) - indices
    h = close.expanding().max() # placeholder for since-idx
    l = close.expanding().min()
    return _safe_div(h, l).where(dist < 63)

def ptt_107_ptt_ratio_at_earnings_miss(close: pd.Series, surprise: pd.Series) -> pd.Series:
    """ptt_107_ptt_ratio_at_earnings_miss feature"""
    r = _safe_div(_rolling_max(close, 21), _rolling_min(close, 21))
    return r.where(surprise < 0).ffill()


# 126-140: Multi-Metric Range Comparisons

def ptt_126_mktcap_vs_price_ptt_ratio_spread(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_126_mktcap_vs_price_ptt_ratio_spread feature"""
    mc = close * sharesbas
    r_mc = _safe_div(_rolling_max(mc, 252), _rolling_min(mc, 252))
    r_p = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    return r_mc - r_p

def ptt_127_ev_vs_mktcap_ptt_ratio_spread(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """ptt_127_ev_vs_mktcap_ptt_ratio_spread feature"""
    mc = close * sharesbas
    ev = mc + debt - cashnequiv
    r_ev = _safe_div(_rolling_max(ev, 252), _rolling_min(ev, 252))
    r_mc = _safe_div(_rolling_max(mc, 252), _rolling_min(mc, 252))
    return r_ev - r_mc


# 141-150: Final PTT composites

def ptt_141_recovery_velocity_score_21d(close: pd.Series) -> pd.Series:
    """ptt_141_recovery_velocity_score_21d feature"""
    # Change in recovery fraction / Realized Vol
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    vol = close.pct_change().rolling(21).std()
    return _safe_div(rf.diff(5), vol)

def ptt_142_peak_to_trough_convexity_score_252d(close: pd.Series) -> pd.Series:
    """ptt_142_peak_to_trough_convexity_score_252d feature"""
    # Integral of (Max-Close)/(Max-Min)
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    dist = _safe_div(h - close, h - l)
    return dist.rolling(252).sum()

def ptt_143_days_since_peak_to_days_since_trough_ratio(close: pd.Series) -> pd.Series:
    """ptt_143_days_since_peak_to_days_since_trough_ratio feature"""
    h_idx = close.rolling(252).apply(np.argmax, raw=True)
    l_idx = close.rolling(252).apply(np.argmin, raw=True)
    dsp = 252 - 1 - h_idx
    dst = 252 - 1 - l_idx
    return _safe_div(dsp, dst)

def ptt_144_recovery_fraction_log_drift_63d(close: pd.Series) -> pd.Series:
    """ptt_144_recovery_fraction_log_drift_63d feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    return np.log(rf + _EPS).diff(21)

def ptt_145_mktcap_recovery_efficiency_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_145_mktcap_recovery_efficiency_252d feature"""
    mc = close * sharesbas
    h = _rolling_max(mc, 252)
    l = _rolling_min(mc, 252)
    rf = _safe_div(mc - l, h - l)
    return _safe_div(rf, mc.pct_change().rolling(252).std())

def ptt_146_proximity_to_midpoint_spread_252d(close: pd.Series) -> pd.Series:
    """ptt_146_proximity_to_midpoint_spread_252d feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    mid = (h + l) / 2.0
    return (close - mid) / (h - l)

def ptt_147_recovery_fraction_entropy_63d(close: pd.Series) -> pd.Series:
    """ptt_147_recovery_fraction_entropy_63d feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    def _ent(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, range=(0,1))
        p = hist / np.sum(hist)
        p = p[p > 0]
        return -np.sum(p * np.log(p))
    return rf.rolling(63).apply(_ent, raw=True)

def ptt_148_terminal_recovery_acceleration_score(close: pd.Series) -> pd.Series:
    """ptt_148_terminal_recovery_acceleration_score feature"""
    # 2nd derivative of recovery fraction
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    return rf.diff(5).diff(5)

def ptt_149_ptt_cycle_amplitude_score_252d(close: pd.Series) -> pd.Series:
    """ptt_149_ptt_cycle_amplitude_score_252d feature"""
    # Current PTT ratio relative to multi-year min PTT ratio
    r = ptt_003_peak_to_trough_ratio_252d(close)
    return _safe_div(r, r.rolling(252 * 3).min())

def ptt_150_peak_to_trough_final_pain_score(close: pd.Series) -> pd.Series:
    """ptt_150_peak_to_trough_final_pain_score feature"""
    # Composite: PTT Ratio * (1 - Recovery Fraction)
    r = ptt_003_peak_to_trough_ratio_252d(close)
    rf = ptt_018_recovery_fraction_252d(close)
    return r * (1.0 - rf)

def ptt_095_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_076_ptt_ratio_pct_rank_ath"""
    return _zscore_rolling(ptt_076_ptt_ratio_pct_rank_ath(close), _TD_MON)

def ptt_096_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_077_recovery_fraction_zscore_252d"""
    return _rank_pct(ptt_077_recovery_fraction_zscore_252d(close), _TD_MON)

def ptt_097_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_078_ptt_volatility_ratio_63d"""
    return _zscore_rolling(ptt_078_ptt_volatility_ratio_63d(close), _TD_MON)

def ptt_098_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_091_count_double_bottom_attempts_252d"""
    return _rank_pct(ptt_091_count_double_bottom_attempts_252d(close), _TD_MON)

def ptt_099_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_092_recovery_fraction_mean_reversion_score_21d"""
    return _zscore_rolling(ptt_092_recovery_fraction_mean_reversion_score_21d(close), _TD_MON)

def ptt_100_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_106_ptt_ratio_since_insider_buy_cluster"""
    return _rank_pct(ptt_106_ptt_ratio_since_insider_buy_cluster(close), _TD_MON)

def ptt_101_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_107_ptt_ratio_at_earnings_miss"""
    return _zscore_rolling(ptt_107_ptt_ratio_at_earnings_miss(close), _TD_MON)

def ptt_102_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_126_mktcap_vs_price_ptt_ratio_spread"""
    return _rank_pct(ptt_126_mktcap_vs_price_ptt_ratio_spread(close), _TD_MON)

def ptt_103_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_127_ev_vs_mktcap_ptt_ratio_spread"""
    return _zscore_rolling(ptt_127_ev_vs_mktcap_ptt_ratio_spread(close), _TD_MON)

def ptt_104_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_141_recovery_velocity_score_21d"""
    return _rank_pct(ptt_141_recovery_velocity_score_21d(close), _TD_MON)

def ptt_105_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_142_peak_to_trough_convexity_score_252d"""
    return _zscore_rolling(ptt_142_peak_to_trough_convexity_score_252d(close), _TD_MON)

def ptt_106_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_143_days_since_peak_to_days_since_trough_ratio"""
    return _rank_pct(ptt_143_days_since_peak_to_days_since_trough_ratio(close), _TD_MON)

def ptt_107_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_144_recovery_fraction_log_drift_63d"""
    return _zscore_rolling(ptt_144_recovery_fraction_log_drift_63d(close), _TD_MON)

def ptt_108_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_145_mktcap_recovery_efficiency_252d"""
    return _rank_pct(ptt_145_mktcap_recovery_efficiency_252d(close), _TD_MON)

def ptt_109_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_146_proximity_to_midpoint_spread_252d"""
    return _zscore_rolling(ptt_146_proximity_to_midpoint_spread_252d(close), _TD_MON)

def ptt_110_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_147_recovery_fraction_entropy_63d"""
    return _rank_pct(ptt_147_recovery_fraction_entropy_63d(close), _TD_MON)

def ptt_111_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_148_terminal_recovery_acceleration_score"""
    return _zscore_rolling(ptt_148_terminal_recovery_acceleration_score(close), _TD_MON)

def ptt_112_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_149_ptt_cycle_amplitude_score_252d"""
    return _rank_pct(ptt_149_ptt_cycle_amplitude_score_252d(close), _TD_MON)

def ptt_113_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_150_peak_to_trough_final_pain_score"""
    return _zscore_rolling(ptt_150_peak_to_trough_final_pain_score(close), _TD_MON)

def ptt_114_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_076_ptt_ratio_pct_rank_ath"""
    return _rank_pct(ptt_076_ptt_ratio_pct_rank_ath(close), _TD_MON)

def ptt_115_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_077_recovery_fraction_zscore_252d"""
    return _zscore_rolling(ptt_077_recovery_fraction_zscore_252d(close), _TD_MON)

def ptt_116_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_078_ptt_volatility_ratio_63d"""
    return _rank_pct(ptt_078_ptt_volatility_ratio_63d(close), _TD_MON)

def ptt_117_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_091_count_double_bottom_attempts_252d"""
    return _zscore_rolling(ptt_091_count_double_bottom_attempts_252d(close), _TD_MON)

def ptt_118_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_092_recovery_fraction_mean_reversion_score_21d"""
    return _rank_pct(ptt_092_recovery_fraction_mean_reversion_score_21d(close), _TD_MON)

def ptt_119_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_106_ptt_ratio_since_insider_buy_cluster"""
    return _zscore_rolling(ptt_106_ptt_ratio_since_insider_buy_cluster(close), _TD_MON)

def ptt_120_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_107_ptt_ratio_at_earnings_miss"""
    return _rank_pct(ptt_107_ptt_ratio_at_earnings_miss(close), _TD_MON)

def ptt_121_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_126_mktcap_vs_price_ptt_ratio_spread"""
    return _zscore_rolling(ptt_126_mktcap_vs_price_ptt_ratio_spread(close), _TD_MON)

def ptt_122_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_127_ev_vs_mktcap_ptt_ratio_spread"""
    return _rank_pct(ptt_127_ev_vs_mktcap_ptt_ratio_spread(close), _TD_MON)

def ptt_123_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_141_recovery_velocity_score_21d"""
    return _zscore_rolling(ptt_141_recovery_velocity_score_21d(close), _TD_MON)

def ptt_124_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_142_peak_to_trough_convexity_score_252d"""
    return _rank_pct(ptt_142_peak_to_trough_convexity_score_252d(close), _TD_MON)

def ptt_125_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_143_days_since_peak_to_days_since_trough_ratio"""
    return _zscore_rolling(ptt_143_days_since_peak_to_days_since_trough_ratio(close), _TD_MON)

def ptt_126_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_144_recovery_fraction_log_drift_63d"""
    return _rank_pct(ptt_144_recovery_fraction_log_drift_63d(close), _TD_MON)

def ptt_127_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_145_mktcap_recovery_efficiency_252d"""
    return _zscore_rolling(ptt_145_mktcap_recovery_efficiency_252d(close), _TD_MON)

def ptt_128_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_146_proximity_to_midpoint_spread_252d"""
    return _rank_pct(ptt_146_proximity_to_midpoint_spread_252d(close), _TD_MON)

def ptt_129_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_147_recovery_fraction_entropy_63d"""
    return _zscore_rolling(ptt_147_recovery_fraction_entropy_63d(close), _TD_MON)

def ptt_130_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_148_terminal_recovery_acceleration_score"""
    return _rank_pct(ptt_148_terminal_recovery_acceleration_score(close), _TD_MON)

def ptt_131_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_149_ptt_cycle_amplitude_score_252d"""
    return _zscore_rolling(ptt_149_ptt_cycle_amplitude_score_252d(close), _TD_MON)

def ptt_132_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_150_peak_to_trough_final_pain_score"""
    return _rank_pct(ptt_150_peak_to_trough_final_pain_score(close), _TD_MON)

def ptt_133_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_076_ptt_ratio_pct_rank_ath"""
    return _zscore_rolling(ptt_076_ptt_ratio_pct_rank_ath(close), _TD_MON)

def ptt_134_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_077_recovery_fraction_zscore_252d"""
    return _rank_pct(ptt_077_recovery_fraction_zscore_252d(close), _TD_MON)

def ptt_135_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_078_ptt_volatility_ratio_63d"""
    return _zscore_rolling(ptt_078_ptt_volatility_ratio_63d(close), _TD_MON)

def ptt_136_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_091_count_double_bottom_attempts_252d"""
    return _rank_pct(ptt_091_count_double_bottom_attempts_252d(close), _TD_MON)

def ptt_137_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_092_recovery_fraction_mean_reversion_score_21d"""
    return _zscore_rolling(ptt_092_recovery_fraction_mean_reversion_score_21d(close), _TD_MON)

def ptt_138_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_106_ptt_ratio_since_insider_buy_cluster"""
    return _rank_pct(ptt_106_ptt_ratio_since_insider_buy_cluster(close), _TD_MON)

def ptt_139_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_107_ptt_ratio_at_earnings_miss"""
    return _zscore_rolling(ptt_107_ptt_ratio_at_earnings_miss(close), _TD_MON)

def ptt_140_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_126_mktcap_vs_price_ptt_ratio_spread"""
    return _rank_pct(ptt_126_mktcap_vs_price_ptt_ratio_spread(close), _TD_MON)

def ptt_141_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_127_ev_vs_mktcap_ptt_ratio_spread"""
    return _zscore_rolling(ptt_127_ev_vs_mktcap_ptt_ratio_spread(close), _TD_MON)

def ptt_142_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_141_recovery_velocity_score_21d"""
    return _rank_pct(ptt_141_recovery_velocity_score_21d(close), _TD_MON)

def ptt_143_stat_depth_var_48(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_142_peak_to_trough_convexity_score_252d"""
    return _zscore_rolling(ptt_142_peak_to_trough_convexity_score_252d(close), _TD_MON)

def ptt_144_stat_depth_var_49(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_143_days_since_peak_to_days_since_trough_ratio"""
    return _rank_pct(ptt_143_days_since_peak_to_days_since_trough_ratio(close), _TD_MON)

def ptt_145_stat_depth_var_50(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_144_recovery_fraction_log_drift_63d"""
    return _zscore_rolling(ptt_144_recovery_fraction_log_drift_63d(close), _TD_MON)

def ptt_146_stat_depth_var_51(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_145_mktcap_recovery_efficiency_252d"""
    return _rank_pct(ptt_145_mktcap_recovery_efficiency_252d(close), _TD_MON)

def ptt_147_stat_depth_var_52(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_146_proximity_to_midpoint_spread_252d"""
    return _zscore_rolling(ptt_146_proximity_to_midpoint_spread_252d(close), _TD_MON)

def ptt_148_stat_depth_var_53(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_147_recovery_fraction_entropy_63d"""
    return _rank_pct(ptt_147_recovery_fraction_entropy_63d(close), _TD_MON)

def ptt_149_stat_depth_var_54(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_148_terminal_recovery_acceleration_score"""
    return _zscore_rolling(ptt_148_terminal_recovery_acceleration_score(close), _TD_MON)

def ptt_150_stat_depth_var_55(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_149_ptt_cycle_amplitude_score_252d"""
    return _rank_pct(ptt_149_ptt_cycle_amplitude_score_252d(close), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V07_REGISTRY = {
    "ptt_076_ptt_ratio_pct_rank_ath": {"inputs": ["close"], "func": ptt_076_ptt_ratio_pct_rank_ath},
    "ptt_077_recovery_fraction_zscore_252d": {"inputs": ["close"], "func": ptt_077_recovery_fraction_zscore_252d},
    "ptt_078_ptt_volatility_ratio_63d": {"inputs": ["close"], "func": ptt_078_ptt_volatility_ratio_63d},
    "ptt_091_count_double_bottom_attempts_252d": {"inputs": ["close"], "func": ptt_091_count_double_bottom_attempts_252d},
    "ptt_092_recovery_fraction_mean_reversion_score_21d": {"inputs": ["close"], "func": ptt_092_recovery_fraction_mean_reversion_score_21d},
    "ptt_106_ptt_ratio_since_insider_buy_cluster": {"inputs": ["close", "insider_buys"], "func": ptt_106_ptt_ratio_since_insider_buy_cluster},
    "ptt_107_ptt_ratio_at_earnings_miss": {"inputs": ["close", "surprise"], "func": ptt_107_ptt_ratio_at_earnings_miss},
    "ptt_126_mktcap_vs_price_ptt_ratio_spread": {"inputs": ["close", "sharesbas"], "func": ptt_126_mktcap_vs_price_ptt_ratio_spread},
    "ptt_127_ev_vs_mktcap_ptt_ratio_spread": {"inputs": ["close", "sharesbas", "debt", "cashnequiv"], "func": ptt_127_ev_vs_mktcap_ptt_ratio_spread},
    "ptt_141_recovery_velocity_score_21d": {"inputs": ["close"], "func": ptt_141_recovery_velocity_score_21d},
    "ptt_142_peak_to_trough_convexity_score_252d": {"inputs": ["close"], "func": ptt_142_peak_to_trough_convexity_score_252d},
    "ptt_143_days_since_peak_to_days_since_trough_ratio": {"inputs": ["close"], "func": ptt_143_days_since_peak_to_days_since_trough_ratio},
    "ptt_144_recovery_fraction_log_drift_63d": {"inputs": ["close"], "func": ptt_144_recovery_fraction_log_drift_63d},
    "ptt_145_mktcap_recovery_efficiency_252d": {"inputs": ["close", "sharesbas"], "func": ptt_145_mktcap_recovery_efficiency_252d},
    "ptt_146_proximity_to_midpoint_spread_252d": {"inputs": ["close"], "func": ptt_146_proximity_to_midpoint_spread_252d},
    "ptt_147_recovery_fraction_entropy_63d": {"inputs": ["close"], "func": ptt_147_recovery_fraction_entropy_63d},
    "ptt_148_terminal_recovery_acceleration_score": {"inputs": ["close"], "func": ptt_148_terminal_recovery_acceleration_score},
    "ptt_149_ptt_cycle_amplitude_score_252d": {"inputs": ["close"], "func": ptt_149_ptt_cycle_amplitude_score_252d},
    "ptt_150_peak_to_trough_final_pain_score": {"inputs": ["close"], "func": ptt_150_peak_to_trough_final_pain_score},
    "ptt_095_stat_depth_var_0": {"inputs": ["close"], "func": ptt_095_stat_depth_var_0},
    "ptt_096_stat_depth_var_1": {"inputs": ["close"], "func": ptt_096_stat_depth_var_1},
    "ptt_097_stat_depth_var_2": {"inputs": ["close"], "func": ptt_097_stat_depth_var_2},
    "ptt_098_stat_depth_var_3": {"inputs": ["close"], "func": ptt_098_stat_depth_var_3},
    "ptt_099_stat_depth_var_4": {"inputs": ["close"], "func": ptt_099_stat_depth_var_4},
    "ptt_100_stat_depth_var_5": {"inputs": ["close"], "func": ptt_100_stat_depth_var_5},
    "ptt_101_stat_depth_var_6": {"inputs": ["close"], "func": ptt_101_stat_depth_var_6},
    "ptt_102_stat_depth_var_7": {"inputs": ["close"], "func": ptt_102_stat_depth_var_7},
    "ptt_103_stat_depth_var_8": {"inputs": ["close"], "func": ptt_103_stat_depth_var_8},
    "ptt_104_stat_depth_var_9": {"inputs": ["close"], "func": ptt_104_stat_depth_var_9},
    "ptt_105_stat_depth_var_10": {"inputs": ["close"], "func": ptt_105_stat_depth_var_10},
    "ptt_106_stat_depth_var_11": {"inputs": ["close"], "func": ptt_106_stat_depth_var_11},
    "ptt_107_stat_depth_var_12": {"inputs": ["close"], "func": ptt_107_stat_depth_var_12},
    "ptt_108_stat_depth_var_13": {"inputs": ["close"], "func": ptt_108_stat_depth_var_13},
    "ptt_109_stat_depth_var_14": {"inputs": ["close"], "func": ptt_109_stat_depth_var_14},
    "ptt_110_stat_depth_var_15": {"inputs": ["close"], "func": ptt_110_stat_depth_var_15},
    "ptt_111_stat_depth_var_16": {"inputs": ["close"], "func": ptt_111_stat_depth_var_16},
    "ptt_112_stat_depth_var_17": {"inputs": ["close"], "func": ptt_112_stat_depth_var_17},
    "ptt_113_stat_depth_var_18": {"inputs": ["close"], "func": ptt_113_stat_depth_var_18},
    "ptt_114_stat_depth_var_19": {"inputs": ["close"], "func": ptt_114_stat_depth_var_19},
    "ptt_115_stat_depth_var_20": {"inputs": ["close"], "func": ptt_115_stat_depth_var_20},
    "ptt_116_stat_depth_var_21": {"inputs": ["close"], "func": ptt_116_stat_depth_var_21},
    "ptt_117_stat_depth_var_22": {"inputs": ["close"], "func": ptt_117_stat_depth_var_22},
    "ptt_118_stat_depth_var_23": {"inputs": ["close"], "func": ptt_118_stat_depth_var_23},
    "ptt_119_stat_depth_var_24": {"inputs": ["close"], "func": ptt_119_stat_depth_var_24},
    "ptt_120_stat_depth_var_25": {"inputs": ["close"], "func": ptt_120_stat_depth_var_25},
    "ptt_121_stat_depth_var_26": {"inputs": ["close"], "func": ptt_121_stat_depth_var_26},
    "ptt_122_stat_depth_var_27": {"inputs": ["close"], "func": ptt_122_stat_depth_var_27},
    "ptt_123_stat_depth_var_28": {"inputs": ["close"], "func": ptt_123_stat_depth_var_28},
    "ptt_124_stat_depth_var_29": {"inputs": ["close"], "func": ptt_124_stat_depth_var_29},
    "ptt_125_stat_depth_var_30": {"inputs": ["close"], "func": ptt_125_stat_depth_var_30},
    "ptt_126_stat_depth_var_31": {"inputs": ["close"], "func": ptt_126_stat_depth_var_31},
    "ptt_127_stat_depth_var_32": {"inputs": ["close"], "func": ptt_127_stat_depth_var_32},
    "ptt_128_stat_depth_var_33": {"inputs": ["close"], "func": ptt_128_stat_depth_var_33},
    "ptt_129_stat_depth_var_34": {"inputs": ["close"], "func": ptt_129_stat_depth_var_34},
    "ptt_130_stat_depth_var_35": {"inputs": ["close"], "func": ptt_130_stat_depth_var_35},
    "ptt_131_stat_depth_var_36": {"inputs": ["close"], "func": ptt_131_stat_depth_var_36},
    "ptt_132_stat_depth_var_37": {"inputs": ["close"], "func": ptt_132_stat_depth_var_37},
    "ptt_133_stat_depth_var_38": {"inputs": ["close"], "func": ptt_133_stat_depth_var_38},
    "ptt_134_stat_depth_var_39": {"inputs": ["close"], "func": ptt_134_stat_depth_var_39},
    "ptt_135_stat_depth_var_40": {"inputs": ["close"], "func": ptt_135_stat_depth_var_40},
    "ptt_136_stat_depth_var_41": {"inputs": ["close"], "func": ptt_136_stat_depth_var_41},
    "ptt_137_stat_depth_var_42": {"inputs": ["close"], "func": ptt_137_stat_depth_var_42},
    "ptt_138_stat_depth_var_43": {"inputs": ["close"], "func": ptt_138_stat_depth_var_43},
    "ptt_139_stat_depth_var_44": {"inputs": ["close"], "func": ptt_139_stat_depth_var_44},
    "ptt_140_stat_depth_var_45": {"inputs": ["close"], "func": ptt_140_stat_depth_var_45},
    "ptt_141_stat_depth_var_46": {"inputs": ["close"], "func": ptt_141_stat_depth_var_46},
    "ptt_142_stat_depth_var_47": {"inputs": ["close"], "func": ptt_142_stat_depth_var_47},
    "ptt_143_stat_depth_var_48": {"inputs": ["close"], "func": ptt_143_stat_depth_var_48},
    "ptt_144_stat_depth_var_49": {"inputs": ["close"], "func": ptt_144_stat_depth_var_49},
    "ptt_145_stat_depth_var_50": {"inputs": ["close"], "func": ptt_145_stat_depth_var_50},
    "ptt_146_stat_depth_var_51": {"inputs": ["close"], "func": ptt_146_stat_depth_var_51},
    "ptt_147_stat_depth_var_52": {"inputs": ["close"], "func": ptt_147_stat_depth_var_52},
    "ptt_148_stat_depth_var_53": {"inputs": ["close"], "func": ptt_148_stat_depth_var_53},
    "ptt_149_stat_depth_var_54": {"inputs": ["close"], "func": ptt_149_stat_depth_var_54},
    "ptt_150_stat_depth_var_55": {"inputs": ["close"], "func": ptt_150_stat_depth_var_55},
}
