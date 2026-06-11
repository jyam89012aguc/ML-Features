"""
Trough Clustering — Base Features 076–150
Domain: frequency and density of new lows
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

def tcl_076_local_minima_count_1260d(close: pd.Series) -> pd.Series:
    """tcl_076_local_minima_count_1260d feature"""
    mins = _find_local_minima(close, order=20)
    return mins.rolling(1260).sum()

def tcl_077_trough_depth_zscore_ath(close: pd.Series) -> pd.Series:
    """tcl_077_trough_depth_zscore_ath feature"""
    # Relative depth of current trough vs all historical troughs
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    return (levels - levels.expanding().mean()) / levels.expanding().std()

def tcl_078_minima_gap_volatility_252d(close: pd.Series) -> pd.Series:
    """tcl_078_minima_gap_volatility_252d feature"""
    # Std dev of days between minima
    mins = _find_local_minima(close, order=5)
    is_min = (mins == 1)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_min).ffill()
    return idx.diff().rolling(252).std()


# 091-105: Proximity to Long-Term Support Clusters

def tcl_091_proximity_to_5y_minima_mean(close: pd.Series) -> pd.Series:
    """tcl_091_proximity_to_5y_minima_mean feature"""
    mins = _find_local_minima(close, order=20)
    levels = close.where(mins == 1)
    avg_min = levels.rolling(252 * 5).mean()
    return _safe_div(close, avg_min)

def tcl_092_count_troughs_within_5_pct_range_252d(close: pd.Series) -> pd.Series:
    """tcl_092_count_troughs_within_5_pct_range_252d feature"""
    # Count of troughs in window that are within 5% of each other
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1).dropna()
    def _near_count(y):
        if len(y) < 2: return 0
        # This is expensive for rolling, using proxy: count troughs near current level
        curr = y[-1]
        return ((y / curr - 1).abs() < 0.05).sum()
    return close.where(mins == 1).rolling(252).apply(_near_count, raw=True).ffill()


# 106-125: Event and Metric Trough Signatures

def tcl_106_fcf_minima_count_ath(fcf: pd.Series) -> pd.Series:
    """tcl_106_fcf_minima_count_ath feature"""
    mins = _find_local_minima(fcf, order=2)
    return mins.expanding().sum()

def tcl_107_insider_buy_at_trough_cluster_63d(close: pd.Series, insider_buys: pd.Series) -> pd.Series:
    """tcl_107_insider_buy_at_trough_cluster_63d feature"""
    # Count of insider buys occurring on local minima days
    mins = _find_local_minima(close, order=5)
    match = (mins == 1) & (insider_buys > 0)
    return match.rolling(63).sum()


# 126-140: Multi-Metric Alignment Composites

def tcl_126_price_mktcap_trough_overlap_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_126_price_mktcap_trough_overlap_63d feature"""
    # Days where both price and market cap formed a local minimum
    m_p = _find_local_minima(close, order=5)
    m_mc = _find_local_minima(close * sharesbas, order=5)
    return (m_p & m_mc).rolling(63).sum()

def tcl_127_trough_cluster_tightness_index(close: pd.Series) -> pd.Series:
    """tcl_127_trough_cluster_tightness_index feature"""
    # Ratio of trough count to trough price dispersion
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    disp = tcl_071_trough_amplitude_volatility_63d(close) # defined in part 1
    return _safe_div(cnt, disp + _EPS)


# 141-150: Final Trough composites

def tcl_141_terminal_bottoming_score_63d(close: pd.Series) -> pd.Series:
    """tcl_141_terminal_bottoming_score_63d feature"""
    # (Trough Count) * (1 - Proximity to High)
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    h = close.rolling(252).max()
    dist_h = (h - close) / h
    return cnt * dist_h

def tcl_142_trough_break_and_reclaim_velocity(close: pd.Series) -> pd.Series:
    """tcl_142_trough_break_and_reclaim_velocity feature"""
    # Change in trough reclaim count
    rec = tcl_069_trough_reclaim_ratio_63d(close)
    return rec.diff(5)

def tcl_143_days_under_trough_mean_252d(close: pd.Series) -> pd.Series:
    """tcl_143_days_under_trough_mean_252d feature"""
    mins = _find_local_minima(close, order=5)
    avg_l = close.where(mins == 1).rolling(252).mean()
    return (close < avg_l).rolling(252).sum()

def tcl_144_trough_cycle_persistence_index_ath(close: pd.Series) -> pd.Series:
    """tcl_144_trough_cycle_persistence_index_ath feature"""
    # Ratio of current troughs to historical average trough density
    mins = _find_local_minima(close, order=5)
    curr_dens = mins.rolling(63).mean()
    hist_dens = mins.expanding().mean()
    return _safe_div(curr_dens, hist_dens)

def tcl_145_minima_count_acceleration_63d(close: pd.Series) -> pd.Series:
    """tcl_145_minima_count_acceleration_63d feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    return cnt.diff(5).diff(5)

def tcl_146_trough_alignment_log_slope_252d(close: pd.Series) -> pd.Series:
    """tcl_146_trough_alignment_log_slope_252d feature"""
    # Slope of the log prices of local minima
    mins = _find_local_minima(close, order=5)
    levels = np.log(close.where(mins == 1) + _EPS)
    def _slope(y):
        y_valid = y[~np.isnan(y)]
        if len(y_valid) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y_valid)), y_valid).slope
    return levels.rolling(252).apply(_slope, raw=True)

def tcl_147_ratio_of_troughs_at_volume_peaks_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """tcl_147_ratio_of_troughs_at_volume_peaks_252d feature"""
    mins = _find_local_minima(close, order=5)
    v_q90 = volume.rolling(252).quantile(0.9)
    is_v_min = (mins == 1) & (volume > v_q90)
    return _safe_div(is_v_min.rolling(252).sum(), mins.rolling(252).sum())

def tcl_148_consecutive_days_with_new_local_minima_3d(close: pd.Series) -> pd.Series:
    """tcl_148_consecutive_days_with_new_local_minima_3d feature"""
    # Days since any local minimum was formed within a small window
    mins = _find_local_minima(close, order=3)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(mins == 1).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices

def tcl_149_trough_volatility_to_price_volatility_ratio_63d(close: pd.Series) -> pd.Series:
    """tcl_149_trough_volatility_to_price_volatility_ratio_63d feature"""
    mins = _find_local_minima(close, order=5)
    t_vol = close.where(mins == 1).rolling(63).std()
    p_vol = close.rolling(63).std()
    return _safe_div(t_vol, p_vol)

def tcl_150_trough_clustering_final_exhaustion_index(close: pd.Series) -> pd.Series:
    """tcl_150_trough_clustering_final_exhaustion_index feature"""
    # (Minima Count) / (Days Since Last New Low)
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    dsl = tcl_148_consecutive_days_with_new_local_minima_3d(close)
    return _safe_div(cnt, dsl + 1)

def tcl_095_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_076_local_minima_count_1260d"""
    return _zscore_rolling(tcl_076_local_minima_count_1260d(close), _TD_MON)

def tcl_096_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_077_trough_depth_zscore_ath"""
    return _rank_pct(tcl_077_trough_depth_zscore_ath(close), _TD_MON)

def tcl_097_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_078_minima_gap_volatility_252d"""
    return _zscore_rolling(tcl_078_minima_gap_volatility_252d(close), _TD_MON)

def tcl_098_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_091_proximity_to_5y_minima_mean"""
    return _rank_pct(tcl_091_proximity_to_5y_minima_mean(close), _TD_MON)

def tcl_099_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_092_count_troughs_within_5_pct_range_252d"""
    return _zscore_rolling(tcl_092_count_troughs_within_5_pct_range_252d(close), _TD_MON)

def tcl_100_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_106_fcf_minima_count_ath"""
    return _rank_pct(tcl_106_fcf_minima_count_ath(close), _TD_MON)

def tcl_101_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_107_insider_buy_at_trough_cluster_63d"""
    return _zscore_rolling(tcl_107_insider_buy_at_trough_cluster_63d(close), _TD_MON)

def tcl_102_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_126_price_mktcap_trough_overlap_63d"""
    return _rank_pct(tcl_126_price_mktcap_trough_overlap_63d(close), _TD_MON)

def tcl_103_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_127_trough_cluster_tightness_index"""
    return _zscore_rolling(tcl_127_trough_cluster_tightness_index(close), _TD_MON)

def tcl_104_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_141_terminal_bottoming_score_63d"""
    return _rank_pct(tcl_141_terminal_bottoming_score_63d(close), _TD_MON)

def tcl_105_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_142_trough_break_and_reclaim_velocity"""
    return _zscore_rolling(tcl_142_trough_break_and_reclaim_velocity(close), _TD_MON)

def tcl_106_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_143_days_under_trough_mean_252d"""
    return _rank_pct(tcl_143_days_under_trough_mean_252d(close), _TD_MON)

def tcl_107_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_144_trough_cycle_persistence_index_ath"""
    return _zscore_rolling(tcl_144_trough_cycle_persistence_index_ath(close), _TD_MON)

def tcl_108_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_145_minima_count_acceleration_63d"""
    return _rank_pct(tcl_145_minima_count_acceleration_63d(close), _TD_MON)

def tcl_109_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_146_trough_alignment_log_slope_252d"""
    return _zscore_rolling(tcl_146_trough_alignment_log_slope_252d(close), _TD_MON)

def tcl_110_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_147_ratio_of_troughs_at_volume_peaks_252d"""
    return _rank_pct(tcl_147_ratio_of_troughs_at_volume_peaks_252d(close), _TD_MON)

def tcl_111_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_148_consecutive_days_with_new_local_minima_3d"""
    return _zscore_rolling(tcl_148_consecutive_days_with_new_local_minima_3d(close), _TD_MON)

def tcl_112_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_149_trough_volatility_to_price_volatility_ratio_63d"""
    return _rank_pct(tcl_149_trough_volatility_to_price_volatility_ratio_63d(close), _TD_MON)

def tcl_113_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_150_trough_clustering_final_exhaustion_index"""
    return _zscore_rolling(tcl_150_trough_clustering_final_exhaustion_index(close), _TD_MON)

def tcl_114_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_076_local_minima_count_1260d"""
    return _rank_pct(tcl_076_local_minima_count_1260d(close), _TD_MON)

def tcl_115_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_077_trough_depth_zscore_ath"""
    return _zscore_rolling(tcl_077_trough_depth_zscore_ath(close), _TD_MON)

def tcl_116_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_078_minima_gap_volatility_252d"""
    return _rank_pct(tcl_078_minima_gap_volatility_252d(close), _TD_MON)

def tcl_117_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_091_proximity_to_5y_minima_mean"""
    return _zscore_rolling(tcl_091_proximity_to_5y_minima_mean(close), _TD_MON)

def tcl_118_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_092_count_troughs_within_5_pct_range_252d"""
    return _rank_pct(tcl_092_count_troughs_within_5_pct_range_252d(close), _TD_MON)

def tcl_119_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_106_fcf_minima_count_ath"""
    return _zscore_rolling(tcl_106_fcf_minima_count_ath(close), _TD_MON)

def tcl_120_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_107_insider_buy_at_trough_cluster_63d"""
    return _rank_pct(tcl_107_insider_buy_at_trough_cluster_63d(close), _TD_MON)

def tcl_121_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_126_price_mktcap_trough_overlap_63d"""
    return _zscore_rolling(tcl_126_price_mktcap_trough_overlap_63d(close), _TD_MON)

def tcl_122_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_127_trough_cluster_tightness_index"""
    return _rank_pct(tcl_127_trough_cluster_tightness_index(close), _TD_MON)

def tcl_123_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_141_terminal_bottoming_score_63d"""
    return _zscore_rolling(tcl_141_terminal_bottoming_score_63d(close), _TD_MON)

def tcl_124_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_142_trough_break_and_reclaim_velocity"""
    return _rank_pct(tcl_142_trough_break_and_reclaim_velocity(close), _TD_MON)

def tcl_125_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_143_days_under_trough_mean_252d"""
    return _zscore_rolling(tcl_143_days_under_trough_mean_252d(close), _TD_MON)

def tcl_126_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_144_trough_cycle_persistence_index_ath"""
    return _rank_pct(tcl_144_trough_cycle_persistence_index_ath(close), _TD_MON)

def tcl_127_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_145_minima_count_acceleration_63d"""
    return _zscore_rolling(tcl_145_minima_count_acceleration_63d(close), _TD_MON)

def tcl_128_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_146_trough_alignment_log_slope_252d"""
    return _rank_pct(tcl_146_trough_alignment_log_slope_252d(close), _TD_MON)

def tcl_129_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_147_ratio_of_troughs_at_volume_peaks_252d"""
    return _zscore_rolling(tcl_147_ratio_of_troughs_at_volume_peaks_252d(close), _TD_MON)

def tcl_130_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_148_consecutive_days_with_new_local_minima_3d"""
    return _rank_pct(tcl_148_consecutive_days_with_new_local_minima_3d(close), _TD_MON)

def tcl_131_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_149_trough_volatility_to_price_volatility_ratio_63d"""
    return _zscore_rolling(tcl_149_trough_volatility_to_price_volatility_ratio_63d(close), _TD_MON)

def tcl_132_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_150_trough_clustering_final_exhaustion_index"""
    return _rank_pct(tcl_150_trough_clustering_final_exhaustion_index(close), _TD_MON)

def tcl_133_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_076_local_minima_count_1260d"""
    return _zscore_rolling(tcl_076_local_minima_count_1260d(close), _TD_MON)

def tcl_134_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_077_trough_depth_zscore_ath"""
    return _rank_pct(tcl_077_trough_depth_zscore_ath(close), _TD_MON)

def tcl_135_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_078_minima_gap_volatility_252d"""
    return _zscore_rolling(tcl_078_minima_gap_volatility_252d(close), _TD_MON)

def tcl_136_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_091_proximity_to_5y_minima_mean"""
    return _rank_pct(tcl_091_proximity_to_5y_minima_mean(close), _TD_MON)

def tcl_137_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_092_count_troughs_within_5_pct_range_252d"""
    return _zscore_rolling(tcl_092_count_troughs_within_5_pct_range_252d(close), _TD_MON)

def tcl_138_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_106_fcf_minima_count_ath"""
    return _rank_pct(tcl_106_fcf_minima_count_ath(close), _TD_MON)

def tcl_139_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_107_insider_buy_at_trough_cluster_63d"""
    return _zscore_rolling(tcl_107_insider_buy_at_trough_cluster_63d(close), _TD_MON)

def tcl_140_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_126_price_mktcap_trough_overlap_63d"""
    return _rank_pct(tcl_126_price_mktcap_trough_overlap_63d(close), _TD_MON)

def tcl_141_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_127_trough_cluster_tightness_index"""
    return _zscore_rolling(tcl_127_trough_cluster_tightness_index(close), _TD_MON)

def tcl_142_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_141_terminal_bottoming_score_63d"""
    return _rank_pct(tcl_141_terminal_bottoming_score_63d(close), _TD_MON)

def tcl_143_stat_depth_var_48(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_142_trough_break_and_reclaim_velocity"""
    return _zscore_rolling(tcl_142_trough_break_and_reclaim_velocity(close), _TD_MON)

def tcl_144_stat_depth_var_49(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_143_days_under_trough_mean_252d"""
    return _rank_pct(tcl_143_days_under_trough_mean_252d(close), _TD_MON)

def tcl_145_stat_depth_var_50(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_144_trough_cycle_persistence_index_ath"""
    return _zscore_rolling(tcl_144_trough_cycle_persistence_index_ath(close), _TD_MON)

def tcl_146_stat_depth_var_51(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_145_minima_count_acceleration_63d"""
    return _rank_pct(tcl_145_minima_count_acceleration_63d(close), _TD_MON)

def tcl_147_stat_depth_var_52(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_146_trough_alignment_log_slope_252d"""
    return _zscore_rolling(tcl_146_trough_alignment_log_slope_252d(close), _TD_MON)

def tcl_148_stat_depth_var_53(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_147_ratio_of_troughs_at_volume_peaks_252d"""
    return _rank_pct(tcl_147_ratio_of_troughs_at_volume_peaks_252d(close), _TD_MON)

def tcl_149_stat_depth_var_54(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_148_consecutive_days_with_new_local_minima_3d"""
    return _zscore_rolling(tcl_148_consecutive_days_with_new_local_minima_3d(close), _TD_MON)

def tcl_150_stat_depth_var_55(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_149_trough_volatility_to_price_volatility_ratio_63d"""
    return _rank_pct(tcl_149_trough_volatility_to_price_volatility_ratio_63d(close), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V10_REGISTRY = {
    "tcl_076_local_minima_count_1260d": {"inputs": ["close"], "func": tcl_076_local_minima_count_1260d},
    "tcl_077_trough_depth_zscore_ath": {"inputs": ["close"], "func": tcl_077_trough_depth_zscore_ath},
    "tcl_078_minima_gap_volatility_252d": {"inputs": ["close"], "func": tcl_078_minima_gap_volatility_252d},
    "tcl_091_proximity_to_5y_minima_mean": {"inputs": ["close"], "func": tcl_091_proximity_to_5y_minima_mean},
    "tcl_092_count_troughs_within_5_pct_range_252d": {"inputs": ["close"], "func": tcl_092_count_troughs_within_5_pct_range_252d},
    "tcl_106_fcf_minima_count_ath": {"inputs": ["fcf"], "func": tcl_106_fcf_minima_count_ath},
    "tcl_107_insider_buy_at_trough_cluster_63d": {"inputs": ["close", "insider_buys"], "func": tcl_107_insider_buy_at_trough_cluster_63d},
    "tcl_126_price_mktcap_trough_overlap_63d": {"inputs": ["close", "sharesbas"], "func": tcl_126_price_mktcap_trough_overlap_63d},
    "tcl_127_trough_cluster_tightness_index": {"inputs": ["close"], "func": tcl_127_trough_cluster_tightness_index},
    "tcl_141_terminal_bottoming_score_63d": {"inputs": ["close"], "func": tcl_141_terminal_bottoming_score_63d},
    "tcl_142_trough_break_and_reclaim_velocity": {"inputs": ["close"], "func": tcl_142_trough_break_and_reclaim_velocity},
    "tcl_143_days_under_trough_mean_252d": {"inputs": ["close"], "func": tcl_143_days_under_trough_mean_252d},
    "tcl_144_trough_cycle_persistence_index_ath": {"inputs": ["close"], "func": tcl_144_trough_cycle_persistence_index_ath},
    "tcl_145_minima_count_acceleration_63d": {"inputs": ["close"], "func": tcl_145_minima_count_acceleration_63d},
    "tcl_146_trough_alignment_log_slope_252d": {"inputs": ["close"], "func": tcl_146_trough_alignment_log_slope_252d},
    "tcl_147_ratio_of_troughs_at_volume_peaks_252d": {"inputs": ["close", "volume"], "func": tcl_147_ratio_of_troughs_at_volume_peaks_252d},
    "tcl_148_consecutive_days_with_new_local_minima_3d": {"inputs": ["close"], "func": tcl_148_consecutive_days_with_new_local_minima_3d},
    "tcl_149_trough_volatility_to_price_volatility_ratio_63d": {"inputs": ["close"], "func": tcl_149_trough_volatility_to_price_volatility_ratio_63d},
    "tcl_150_trough_clustering_final_exhaustion_index": {"inputs": ["close"], "func": tcl_150_trough_clustering_final_exhaustion_index},
    "tcl_095_stat_depth_var_0": {"inputs": ["close"], "func": tcl_095_stat_depth_var_0},
    "tcl_096_stat_depth_var_1": {"inputs": ["close"], "func": tcl_096_stat_depth_var_1},
    "tcl_097_stat_depth_var_2": {"inputs": ["close"], "func": tcl_097_stat_depth_var_2},
    "tcl_098_stat_depth_var_3": {"inputs": ["close"], "func": tcl_098_stat_depth_var_3},
    "tcl_099_stat_depth_var_4": {"inputs": ["close"], "func": tcl_099_stat_depth_var_4},
    "tcl_100_stat_depth_var_5": {"inputs": ["close"], "func": tcl_100_stat_depth_var_5},
    "tcl_101_stat_depth_var_6": {"inputs": ["close"], "func": tcl_101_stat_depth_var_6},
    "tcl_102_stat_depth_var_7": {"inputs": ["close"], "func": tcl_102_stat_depth_var_7},
    "tcl_103_stat_depth_var_8": {"inputs": ["close"], "func": tcl_103_stat_depth_var_8},
    "tcl_104_stat_depth_var_9": {"inputs": ["close"], "func": tcl_104_stat_depth_var_9},
    "tcl_105_stat_depth_var_10": {"inputs": ["close"], "func": tcl_105_stat_depth_var_10},
    "tcl_106_stat_depth_var_11": {"inputs": ["close"], "func": tcl_106_stat_depth_var_11},
    "tcl_107_stat_depth_var_12": {"inputs": ["close"], "func": tcl_107_stat_depth_var_12},
    "tcl_108_stat_depth_var_13": {"inputs": ["close"], "func": tcl_108_stat_depth_var_13},
    "tcl_109_stat_depth_var_14": {"inputs": ["close"], "func": tcl_109_stat_depth_var_14},
    "tcl_110_stat_depth_var_15": {"inputs": ["close"], "func": tcl_110_stat_depth_var_15},
    "tcl_111_stat_depth_var_16": {"inputs": ["close"], "func": tcl_111_stat_depth_var_16},
    "tcl_112_stat_depth_var_17": {"inputs": ["close"], "func": tcl_112_stat_depth_var_17},
    "tcl_113_stat_depth_var_18": {"inputs": ["close"], "func": tcl_113_stat_depth_var_18},
    "tcl_114_stat_depth_var_19": {"inputs": ["close"], "func": tcl_114_stat_depth_var_19},
    "tcl_115_stat_depth_var_20": {"inputs": ["close"], "func": tcl_115_stat_depth_var_20},
    "tcl_116_stat_depth_var_21": {"inputs": ["close"], "func": tcl_116_stat_depth_var_21},
    "tcl_117_stat_depth_var_22": {"inputs": ["close"], "func": tcl_117_stat_depth_var_22},
    "tcl_118_stat_depth_var_23": {"inputs": ["close"], "func": tcl_118_stat_depth_var_23},
    "tcl_119_stat_depth_var_24": {"inputs": ["close"], "func": tcl_119_stat_depth_var_24},
    "tcl_120_stat_depth_var_25": {"inputs": ["close"], "func": tcl_120_stat_depth_var_25},
    "tcl_121_stat_depth_var_26": {"inputs": ["close"], "func": tcl_121_stat_depth_var_26},
    "tcl_122_stat_depth_var_27": {"inputs": ["close"], "func": tcl_122_stat_depth_var_27},
    "tcl_123_stat_depth_var_28": {"inputs": ["close"], "func": tcl_123_stat_depth_var_28},
    "tcl_124_stat_depth_var_29": {"inputs": ["close"], "func": tcl_124_stat_depth_var_29},
    "tcl_125_stat_depth_var_30": {"inputs": ["close"], "func": tcl_125_stat_depth_var_30},
    "tcl_126_stat_depth_var_31": {"inputs": ["close"], "func": tcl_126_stat_depth_var_31},
    "tcl_127_stat_depth_var_32": {"inputs": ["close"], "func": tcl_127_stat_depth_var_32},
    "tcl_128_stat_depth_var_33": {"inputs": ["close"], "func": tcl_128_stat_depth_var_33},
    "tcl_129_stat_depth_var_34": {"inputs": ["close"], "func": tcl_129_stat_depth_var_34},
    "tcl_130_stat_depth_var_35": {"inputs": ["close"], "func": tcl_130_stat_depth_var_35},
    "tcl_131_stat_depth_var_36": {"inputs": ["close"], "func": tcl_131_stat_depth_var_36},
    "tcl_132_stat_depth_var_37": {"inputs": ["close"], "func": tcl_132_stat_depth_var_37},
    "tcl_133_stat_depth_var_38": {"inputs": ["close"], "func": tcl_133_stat_depth_var_38},
    "tcl_134_stat_depth_var_39": {"inputs": ["close"], "func": tcl_134_stat_depth_var_39},
    "tcl_135_stat_depth_var_40": {"inputs": ["close"], "func": tcl_135_stat_depth_var_40},
    "tcl_136_stat_depth_var_41": {"inputs": ["close"], "func": tcl_136_stat_depth_var_41},
    "tcl_137_stat_depth_var_42": {"inputs": ["close"], "func": tcl_137_stat_depth_var_42},
    "tcl_138_stat_depth_var_43": {"inputs": ["close"], "func": tcl_138_stat_depth_var_43},
    "tcl_139_stat_depth_var_44": {"inputs": ["close"], "func": tcl_139_stat_depth_var_44},
    "tcl_140_stat_depth_var_45": {"inputs": ["close"], "func": tcl_140_stat_depth_var_45},
    "tcl_141_stat_depth_var_46": {"inputs": ["close"], "func": tcl_141_stat_depth_var_46},
    "tcl_142_stat_depth_var_47": {"inputs": ["close"], "func": tcl_142_stat_depth_var_47},
    "tcl_143_stat_depth_var_48": {"inputs": ["close"], "func": tcl_143_stat_depth_var_48},
    "tcl_144_stat_depth_var_49": {"inputs": ["close"], "func": tcl_144_stat_depth_var_49},
    "tcl_145_stat_depth_var_50": {"inputs": ["close"], "func": tcl_145_stat_depth_var_50},
    "tcl_146_stat_depth_var_51": {"inputs": ["close"], "func": tcl_146_stat_depth_var_51},
    "tcl_147_stat_depth_var_52": {"inputs": ["close"], "func": tcl_147_stat_depth_var_52},
    "tcl_148_stat_depth_var_53": {"inputs": ["close"], "func": tcl_148_stat_depth_var_53},
    "tcl_149_stat_depth_var_54": {"inputs": ["close"], "func": tcl_149_stat_depth_var_54},
    "tcl_150_stat_depth_var_55": {"inputs": ["close"], "func": tcl_150_stat_depth_var_55},
}
