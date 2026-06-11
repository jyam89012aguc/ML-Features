"""
Price Compression — Base Features 076–150
Domain: range contraction and expansion
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

def pcmp_076_atr_to_price_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_076_atr_to_price_ratio_21d feature"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21).mean()
    return _safe_div(atr, close)

def pcmp_077_parkinson_vol_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_077_parkinson_vol_21d feature"""
    # High-Low estimator
    def _park(h, l):
        return np.sqrt((1 / (4 * np.log(2))) * (np.log(h / l)**2))
    r = _park(high, low)
    return r.rolling(21).mean()

def pcmp_078_garman_klass_vol_21d(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_078_garman_klass_vol_21d feature"""
    # OHLC estimator
    def _gk(o, h, l, c):
        return np.sqrt(0.5 * (np.log(h / l)**2) - (2 * np.log(2) - 1) * (np.log(c / o)**2))
    r = _gk(open, high, low, close)
    return r.rolling(21).mean()


# 091-105: Tightness Persistence and Probability

def pcmp_091_tightness_oscillator_252d(close: pd.Series) -> pd.Series:
    """pcmp_091_tightness_oscillator_252d feature"""
    # 21-day realized vol relative to its 252-day range
    v = close.pct_change().rolling(21).std()
    l = v.rolling(252).min()
    h = v.rolling(252).max()
    return _safe_div(v - l, h - l)

def pcmp_092_count_extreme_tight_days_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_092_count_extreme_tight_days_252d feature"""
    # Days in bottom decile of 252-day HL ranges
    r = high - low
    q10 = r.rolling(252).quantile(0.1)
    return (r < q10).rolling(252).sum()


# 106-125: Regression-Based Compression Slopes

def pcmp_106_vol_compression_slope_63d(close: pd.Series) -> pd.Series:
    """pcmp_106_vol_compression_slope_63d feature"""
    v = close.pct_change().rolling(21).std()
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    return v.rolling(63).apply(_slope, raw=True)

def pcmp_107_range_compression_slope_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_107_range_compression_slope_63d feature"""
    r = high - low
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    return r.rolling(63).apply(_slope, raw=True)


# 126-140: Multi-Metric Range Comparisons

def pcmp_126_body_to_range_ratio_spread_63d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_126_body_to_range_ratio_spread_63d feature"""
    # (Body / Range) - rolling average of (Body / Range)
    ratio = _safe_div((close - open).abs(), high - low)
    return ratio - ratio.rolling(63).mean()

def pcmp_127_gap_to_range_ratio_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_127_gap_to_range_ratio_21d feature"""
    gap = (open - close.shift(1)).abs()
    r = high - low
    return _safe_div(gap.rolling(21).mean(), r.rolling(21).mean())


# 141-150: Final Compression composites

def pcmp_141_volatility_crash_score_21d(close: pd.Series) -> pd.Series:
    """pcmp_141_volatility_crash_score_21d feature"""
    # Ratio of current 5-day vol to 252-day average vol
    v5 = close.pct_change().rolling(5).std()
    v252 = close.pct_change().rolling(252).std()
    return _safe_div(v5, v252)

def pcmp_142_low_compression_persistence_index_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_142_low_compression_persistence_index_63d feature"""
    # Days within 10% of the minimum HL range of the last year
    r = high - low
    l252 = r.rolling(252).min()
    return (r <= l252 * 1.1).rolling(63).sum()

def pcmp_143_compression_momentum_21d(close: pd.Series) -> pd.Series:
    """pcmp_143_compression_momentum_21d feature"""
    # Change in BB Width over last 21 days
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bw = _safe_div(4 * std, ma)
    return bw.diff(21)

def pcmp_144_price_clustering_acceleration_21d(close: pd.Series) -> pd.Series:
    """pcmp_144_price_clustering_acceleration_21d feature"""
    # 2nd derivative of close clustering index
    ci = _safe_div(close.rolling(21).std(), close.rolling(21).mean())
    return ci.diff(5).diff(5)

def pcmp_145_mktcap_tightness_ratio_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_145_mktcap_tightness_ratio_63d feature"""
    mc = close * sharesbas
    v = mc.pct_change().rolling(21).std()
    return _safe_div(v, v.rolling(63).mean())

def pcmp_146_revenue_ps_compression_ath(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_146_revenue_ps_compression_ath feature"""
    revps = _safe_div(revenue, sharesbas)
    v = revps.pct_change().rolling(4).std() # Quarterly std
    return _safe_div(v, v.expanding().mean())

def pcmp_147_equity_ps_compression_ath(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_147_equity_ps_compression_ath feature"""
    bvps = _safe_div(equity, sharesbas)
    v = bvps.pct_change().rolling(4).std()
    return _safe_div(v, v.expanding().mean())

def pcmp_148_candle_overlap_persistence_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_148_candle_overlap_persistence_21d feature"""
    h_min = high.rolling(2).min()
    l_max = low.rolling(2).max()
    overlap = (h_min - l_max).clip(lower=0) > 0
    return overlap.rolling(21).mean()

def pcmp_149_range_oscillation_decay_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_149_range_oscillation_decay_63d feature"""
    r = high - low
    return r.rolling(63).std() / r.rolling(63).mean()

def pcmp_150_terminal_tightness_climax_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_150_terminal_tightness_climax_score feature"""
    # (1 / BB Width) * (1 / Vol) * (Proximity to Low)
    bbw = pcmp_018_bb_width_20_2(close)
    v = close.pct_change().rolling(21).std()
    l = close.rolling(252).min()
    prox = _safe_div(close, l)
    return _safe_div(1.0, bbw * v * prox)

def pcmp_095_stat_depth_var_0(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_076_atr_to_price_ratio_21d"""
    return _zscore_rolling(pcmp_076_atr_to_price_ratio_21d(high,low,close), _TD_MON)

def pcmp_096_stat_depth_var_1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_077_parkinson_vol_21d"""
    return _rank_pct(pcmp_077_parkinson_vol_21d(high,low,close), _TD_MON)

def pcmp_097_stat_depth_var_2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_078_garman_klass_vol_21d"""
    return _zscore_rolling(pcmp_078_garman_klass_vol_21d(high,low,close), _TD_MON)

def pcmp_098_stat_depth_var_3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_091_tightness_oscillator_252d"""
    return _rank_pct(pcmp_091_tightness_oscillator_252d(high,low,close), _TD_MON)

def pcmp_099_stat_depth_var_4(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_092_count_extreme_tight_days_252d"""
    return _zscore_rolling(pcmp_092_count_extreme_tight_days_252d(high,low,close), _TD_MON)

def pcmp_100_stat_depth_var_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_106_vol_compression_slope_63d"""
    return _rank_pct(pcmp_106_vol_compression_slope_63d(high,low,close), _TD_MON)

def pcmp_101_stat_depth_var_6(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_107_range_compression_slope_63d"""
    return _zscore_rolling(pcmp_107_range_compression_slope_63d(high,low,close), _TD_MON)

def pcmp_102_stat_depth_var_7(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_126_body_to_range_ratio_spread_63d"""
    return _rank_pct(pcmp_126_body_to_range_ratio_spread_63d(high,low,close), _TD_MON)

def pcmp_103_stat_depth_var_8(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_127_gap_to_range_ratio_21d"""
    return _zscore_rolling(pcmp_127_gap_to_range_ratio_21d(high,low,close), _TD_MON)

def pcmp_104_stat_depth_var_9(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_141_volatility_crash_score_21d"""
    return _rank_pct(pcmp_141_volatility_crash_score_21d(high,low,close), _TD_MON)

def pcmp_105_stat_depth_var_10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_142_low_compression_persistence_index_63d"""
    return _zscore_rolling(pcmp_142_low_compression_persistence_index_63d(high,low,close), _TD_MON)

def pcmp_106_stat_depth_var_11(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_143_compression_momentum_21d"""
    return _rank_pct(pcmp_143_compression_momentum_21d(high,low,close), _TD_MON)

def pcmp_107_stat_depth_var_12(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_144_price_clustering_acceleration_21d"""
    return _zscore_rolling(pcmp_144_price_clustering_acceleration_21d(high,low,close), _TD_MON)

def pcmp_108_stat_depth_var_13(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_145_mktcap_tightness_ratio_63d"""
    return _rank_pct(pcmp_145_mktcap_tightness_ratio_63d(high,low,close), _TD_MON)

def pcmp_109_stat_depth_var_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_146_revenue_ps_compression_ath"""
    return _zscore_rolling(pcmp_146_revenue_ps_compression_ath(high,low,close), _TD_MON)

def pcmp_110_stat_depth_var_15(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_147_equity_ps_compression_ath"""
    return _rank_pct(pcmp_147_equity_ps_compression_ath(high,low,close), _TD_MON)

def pcmp_111_stat_depth_var_16(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_148_candle_overlap_persistence_21d"""
    return _zscore_rolling(pcmp_148_candle_overlap_persistence_21d(high,low,close), _TD_MON)

def pcmp_112_stat_depth_var_17(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_149_range_oscillation_decay_63d"""
    return _rank_pct(pcmp_149_range_oscillation_decay_63d(high,low,close), _TD_MON)

def pcmp_113_stat_depth_var_18(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_150_terminal_tightness_climax_score"""
    return _zscore_rolling(pcmp_150_terminal_tightness_climax_score(high,low,close), _TD_MON)

def pcmp_114_stat_depth_var_19(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_076_atr_to_price_ratio_21d"""
    return _rank_pct(pcmp_076_atr_to_price_ratio_21d(high,low,close), _TD_MON)

def pcmp_115_stat_depth_var_20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_077_parkinson_vol_21d"""
    return _zscore_rolling(pcmp_077_parkinson_vol_21d(high,low,close), _TD_MON)

def pcmp_116_stat_depth_var_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_078_garman_klass_vol_21d"""
    return _rank_pct(pcmp_078_garman_klass_vol_21d(high,low,close), _TD_MON)

def pcmp_117_stat_depth_var_22(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_091_tightness_oscillator_252d"""
    return _zscore_rolling(pcmp_091_tightness_oscillator_252d(high,low,close), _TD_MON)

def pcmp_118_stat_depth_var_23(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_092_count_extreme_tight_days_252d"""
    return _rank_pct(pcmp_092_count_extreme_tight_days_252d(high,low,close), _TD_MON)

def pcmp_119_stat_depth_var_24(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_106_vol_compression_slope_63d"""
    return _zscore_rolling(pcmp_106_vol_compression_slope_63d(high,low,close), _TD_MON)

def pcmp_120_stat_depth_var_25(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_107_range_compression_slope_63d"""
    return _rank_pct(pcmp_107_range_compression_slope_63d(high,low,close), _TD_MON)

def pcmp_121_stat_depth_var_26(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_126_body_to_range_ratio_spread_63d"""
    return _zscore_rolling(pcmp_126_body_to_range_ratio_spread_63d(high,low,close), _TD_MON)

def pcmp_122_stat_depth_var_27(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_127_gap_to_range_ratio_21d"""
    return _rank_pct(pcmp_127_gap_to_range_ratio_21d(high,low,close), _TD_MON)

def pcmp_123_stat_depth_var_28(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_141_volatility_crash_score_21d"""
    return _zscore_rolling(pcmp_141_volatility_crash_score_21d(high,low,close), _TD_MON)

def pcmp_124_stat_depth_var_29(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_142_low_compression_persistence_index_63d"""
    return _rank_pct(pcmp_142_low_compression_persistence_index_63d(high,low,close), _TD_MON)

def pcmp_125_stat_depth_var_30(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_143_compression_momentum_21d"""
    return _zscore_rolling(pcmp_143_compression_momentum_21d(high,low,close), _TD_MON)

def pcmp_126_stat_depth_var_31(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_144_price_clustering_acceleration_21d"""
    return _rank_pct(pcmp_144_price_clustering_acceleration_21d(high,low,close), _TD_MON)

def pcmp_127_stat_depth_var_32(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_145_mktcap_tightness_ratio_63d"""
    return _zscore_rolling(pcmp_145_mktcap_tightness_ratio_63d(high,low,close), _TD_MON)

def pcmp_128_stat_depth_var_33(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_146_revenue_ps_compression_ath"""
    return _rank_pct(pcmp_146_revenue_ps_compression_ath(high,low,close), _TD_MON)

def pcmp_129_stat_depth_var_34(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_147_equity_ps_compression_ath"""
    return _zscore_rolling(pcmp_147_equity_ps_compression_ath(high,low,close), _TD_MON)

def pcmp_130_stat_depth_var_35(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_148_candle_overlap_persistence_21d"""
    return _rank_pct(pcmp_148_candle_overlap_persistence_21d(high,low,close), _TD_MON)

def pcmp_131_stat_depth_var_36(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_149_range_oscillation_decay_63d"""
    return _zscore_rolling(pcmp_149_range_oscillation_decay_63d(high,low,close), _TD_MON)

def pcmp_132_stat_depth_var_37(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_150_terminal_tightness_climax_score"""
    return _rank_pct(pcmp_150_terminal_tightness_climax_score(high,low,close), _TD_MON)

def pcmp_133_stat_depth_var_38(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_076_atr_to_price_ratio_21d"""
    return _zscore_rolling(pcmp_076_atr_to_price_ratio_21d(high,low,close), _TD_MON)

def pcmp_134_stat_depth_var_39(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_077_parkinson_vol_21d"""
    return _rank_pct(pcmp_077_parkinson_vol_21d(high,low,close), _TD_MON)

def pcmp_135_stat_depth_var_40(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_078_garman_klass_vol_21d"""
    return _zscore_rolling(pcmp_078_garman_klass_vol_21d(high,low,close), _TD_MON)

def pcmp_136_stat_depth_var_41(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_091_tightness_oscillator_252d"""
    return _rank_pct(pcmp_091_tightness_oscillator_252d(high,low,close), _TD_MON)

def pcmp_137_stat_depth_var_42(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_092_count_extreme_tight_days_252d"""
    return _zscore_rolling(pcmp_092_count_extreme_tight_days_252d(high,low,close), _TD_MON)

def pcmp_138_stat_depth_var_43(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_106_vol_compression_slope_63d"""
    return _rank_pct(pcmp_106_vol_compression_slope_63d(high,low,close), _TD_MON)

def pcmp_139_stat_depth_var_44(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_107_range_compression_slope_63d"""
    return _zscore_rolling(pcmp_107_range_compression_slope_63d(high,low,close), _TD_MON)

def pcmp_140_stat_depth_var_45(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_126_body_to_range_ratio_spread_63d"""
    return _rank_pct(pcmp_126_body_to_range_ratio_spread_63d(high,low,close), _TD_MON)

def pcmp_141_stat_depth_var_46(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_127_gap_to_range_ratio_21d"""
    return _zscore_rolling(pcmp_127_gap_to_range_ratio_21d(high,low,close), _TD_MON)

def pcmp_142_stat_depth_var_47(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_141_volatility_crash_score_21d"""
    return _rank_pct(pcmp_141_volatility_crash_score_21d(high,low,close), _TD_MON)

def pcmp_143_stat_depth_var_48(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_142_low_compression_persistence_index_63d"""
    return _zscore_rolling(pcmp_142_low_compression_persistence_index_63d(high,low,close), _TD_MON)

def pcmp_144_stat_depth_var_49(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_143_compression_momentum_21d"""
    return _rank_pct(pcmp_143_compression_momentum_21d(high,low,close), _TD_MON)

def pcmp_145_stat_depth_var_50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_144_price_clustering_acceleration_21d"""
    return _zscore_rolling(pcmp_144_price_clustering_acceleration_21d(high,low,close), _TD_MON)

def pcmp_146_stat_depth_var_51(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_145_mktcap_tightness_ratio_63d"""
    return _rank_pct(pcmp_145_mktcap_tightness_ratio_63d(high,low,close), _TD_MON)

def pcmp_147_stat_depth_var_52(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_146_revenue_ps_compression_ath"""
    return _zscore_rolling(pcmp_146_revenue_ps_compression_ath(high,low,close), _TD_MON)

def pcmp_148_stat_depth_var_53(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_147_equity_ps_compression_ath"""
    return _rank_pct(pcmp_147_equity_ps_compression_ath(high,low,close), _TD_MON)

def pcmp_149_stat_depth_var_54(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_148_candle_overlap_persistence_21d"""
    return _zscore_rolling(pcmp_148_candle_overlap_persistence_21d(high,low,close), _TD_MON)

def pcmp_150_stat_depth_var_55(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_149_range_oscillation_decay_63d"""
    return _rank_pct(pcmp_149_range_oscillation_decay_63d(high,low,close), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V09_REGISTRY = {
    "pcmp_076_atr_to_price_ratio_21d": {"inputs": ["high", "low", "close"], "func": pcmp_076_atr_to_price_ratio_21d},
    "pcmp_077_parkinson_vol_21d": {"inputs": ["high", "low"], "func": pcmp_077_parkinson_vol_21d},
    "pcmp_078_garman_klass_vol_21d": {"inputs": ["high", "low", "open", "close"], "func": pcmp_078_garman_klass_vol_21d},
    "pcmp_091_tightness_oscillator_252d": {"inputs": ["close"], "func": pcmp_091_tightness_oscillator_252d},
    "pcmp_092_count_extreme_tight_days_252d": {"inputs": ["high", "low"], "func": pcmp_092_count_extreme_tight_days_252d},
    "pcmp_106_vol_compression_slope_63d": {"inputs": ["close"], "func": pcmp_106_vol_compression_slope_63d},
    "pcmp_107_range_compression_slope_63d": {"inputs": ["high", "low"], "func": pcmp_107_range_compression_slope_63d},
    "pcmp_126_body_to_range_ratio_spread_63d": {"inputs": ["open", "close", "high", "low"], "func": pcmp_126_body_to_range_ratio_spread_63d},
    "pcmp_127_gap_to_range_ratio_21d": {"inputs": ["close", "open", "high", "low"], "func": pcmp_127_gap_to_range_ratio_21d},
    "pcmp_141_volatility_crash_score_21d": {"inputs": ["close"], "func": pcmp_141_volatility_crash_score_21d},
    "pcmp_142_low_compression_persistence_index_63d": {"inputs": ["high", "low"], "func": pcmp_142_low_compression_persistence_index_63d},
    "pcmp_143_compression_momentum_21d": {"inputs": ["close"], "func": pcmp_143_compression_momentum_21d},
    "pcmp_144_price_clustering_acceleration_21d": {"inputs": ["close"], "func": pcmp_144_price_clustering_acceleration_21d},
    "pcmp_145_mktcap_tightness_ratio_63d": {"inputs": ["close", "sharesbas"], "func": pcmp_145_mktcap_tightness_ratio_63d},
    "pcmp_146_revenue_ps_compression_ath": {"inputs": ["revenue", "sharesbas"], "func": pcmp_146_revenue_ps_compression_ath},
    "pcmp_147_equity_ps_compression_ath": {"inputs": ["equity", "sharesbas"], "func": pcmp_147_equity_ps_compression_ath},
    "pcmp_148_candle_overlap_persistence_21d": {"inputs": ["high", "low"], "func": pcmp_148_candle_overlap_persistence_21d},
    "pcmp_149_range_oscillation_decay_63d": {"inputs": ["high", "low"], "func": pcmp_149_range_oscillation_decay_63d},
    "pcmp_150_terminal_tightness_climax_score": {"inputs": ["close", "high", "low"], "func": pcmp_150_terminal_tightness_climax_score},
    "pcmp_095_stat_depth_var_0": {"inputs": ["high", "low", "close"], "func": pcmp_095_stat_depth_var_0},
    "pcmp_096_stat_depth_var_1": {"inputs": ["high", "low", "close"], "func": pcmp_096_stat_depth_var_1},
    "pcmp_097_stat_depth_var_2": {"inputs": ["high", "low", "close"], "func": pcmp_097_stat_depth_var_2},
    "pcmp_098_stat_depth_var_3": {"inputs": ["high", "low", "close"], "func": pcmp_098_stat_depth_var_3},
    "pcmp_099_stat_depth_var_4": {"inputs": ["high", "low", "close"], "func": pcmp_099_stat_depth_var_4},
    "pcmp_100_stat_depth_var_5": {"inputs": ["high", "low", "close"], "func": pcmp_100_stat_depth_var_5},
    "pcmp_101_stat_depth_var_6": {"inputs": ["high", "low", "close"], "func": pcmp_101_stat_depth_var_6},
    "pcmp_102_stat_depth_var_7": {"inputs": ["high", "low", "close"], "func": pcmp_102_stat_depth_var_7},
    "pcmp_103_stat_depth_var_8": {"inputs": ["high", "low", "close"], "func": pcmp_103_stat_depth_var_8},
    "pcmp_104_stat_depth_var_9": {"inputs": ["high", "low", "close"], "func": pcmp_104_stat_depth_var_9},
    "pcmp_105_stat_depth_var_10": {"inputs": ["high", "low", "close"], "func": pcmp_105_stat_depth_var_10},
    "pcmp_106_stat_depth_var_11": {"inputs": ["high", "low", "close"], "func": pcmp_106_stat_depth_var_11},
    "pcmp_107_stat_depth_var_12": {"inputs": ["high", "low", "close"], "func": pcmp_107_stat_depth_var_12},
    "pcmp_108_stat_depth_var_13": {"inputs": ["high", "low", "close"], "func": pcmp_108_stat_depth_var_13},
    "pcmp_109_stat_depth_var_14": {"inputs": ["high", "low", "close"], "func": pcmp_109_stat_depth_var_14},
    "pcmp_110_stat_depth_var_15": {"inputs": ["high", "low", "close"], "func": pcmp_110_stat_depth_var_15},
    "pcmp_111_stat_depth_var_16": {"inputs": ["high", "low", "close"], "func": pcmp_111_stat_depth_var_16},
    "pcmp_112_stat_depth_var_17": {"inputs": ["high", "low", "close"], "func": pcmp_112_stat_depth_var_17},
    "pcmp_113_stat_depth_var_18": {"inputs": ["high", "low", "close"], "func": pcmp_113_stat_depth_var_18},
    "pcmp_114_stat_depth_var_19": {"inputs": ["high", "low", "close"], "func": pcmp_114_stat_depth_var_19},
    "pcmp_115_stat_depth_var_20": {"inputs": ["high", "low", "close"], "func": pcmp_115_stat_depth_var_20},
    "pcmp_116_stat_depth_var_21": {"inputs": ["high", "low", "close"], "func": pcmp_116_stat_depth_var_21},
    "pcmp_117_stat_depth_var_22": {"inputs": ["high", "low", "close"], "func": pcmp_117_stat_depth_var_22},
    "pcmp_118_stat_depth_var_23": {"inputs": ["high", "low", "close"], "func": pcmp_118_stat_depth_var_23},
    "pcmp_119_stat_depth_var_24": {"inputs": ["high", "low", "close"], "func": pcmp_119_stat_depth_var_24},
    "pcmp_120_stat_depth_var_25": {"inputs": ["high", "low", "close"], "func": pcmp_120_stat_depth_var_25},
    "pcmp_121_stat_depth_var_26": {"inputs": ["high", "low", "close"], "func": pcmp_121_stat_depth_var_26},
    "pcmp_122_stat_depth_var_27": {"inputs": ["high", "low", "close"], "func": pcmp_122_stat_depth_var_27},
    "pcmp_123_stat_depth_var_28": {"inputs": ["high", "low", "close"], "func": pcmp_123_stat_depth_var_28},
    "pcmp_124_stat_depth_var_29": {"inputs": ["high", "low", "close"], "func": pcmp_124_stat_depth_var_29},
    "pcmp_125_stat_depth_var_30": {"inputs": ["high", "low", "close"], "func": pcmp_125_stat_depth_var_30},
    "pcmp_126_stat_depth_var_31": {"inputs": ["high", "low", "close"], "func": pcmp_126_stat_depth_var_31},
    "pcmp_127_stat_depth_var_32": {"inputs": ["high", "low", "close"], "func": pcmp_127_stat_depth_var_32},
    "pcmp_128_stat_depth_var_33": {"inputs": ["high", "low", "close"], "func": pcmp_128_stat_depth_var_33},
    "pcmp_129_stat_depth_var_34": {"inputs": ["high", "low", "close"], "func": pcmp_129_stat_depth_var_34},
    "pcmp_130_stat_depth_var_35": {"inputs": ["high", "low", "close"], "func": pcmp_130_stat_depth_var_35},
    "pcmp_131_stat_depth_var_36": {"inputs": ["high", "low", "close"], "func": pcmp_131_stat_depth_var_36},
    "pcmp_132_stat_depth_var_37": {"inputs": ["high", "low", "close"], "func": pcmp_132_stat_depth_var_37},
    "pcmp_133_stat_depth_var_38": {"inputs": ["high", "low", "close"], "func": pcmp_133_stat_depth_var_38},
    "pcmp_134_stat_depth_var_39": {"inputs": ["high", "low", "close"], "func": pcmp_134_stat_depth_var_39},
    "pcmp_135_stat_depth_var_40": {"inputs": ["high", "low", "close"], "func": pcmp_135_stat_depth_var_40},
    "pcmp_136_stat_depth_var_41": {"inputs": ["high", "low", "close"], "func": pcmp_136_stat_depth_var_41},
    "pcmp_137_stat_depth_var_42": {"inputs": ["high", "low", "close"], "func": pcmp_137_stat_depth_var_42},
    "pcmp_138_stat_depth_var_43": {"inputs": ["high", "low", "close"], "func": pcmp_138_stat_depth_var_43},
    "pcmp_139_stat_depth_var_44": {"inputs": ["high", "low", "close"], "func": pcmp_139_stat_depth_var_44},
    "pcmp_140_stat_depth_var_45": {"inputs": ["high", "low", "close"], "func": pcmp_140_stat_depth_var_45},
    "pcmp_141_stat_depth_var_46": {"inputs": ["high", "low", "close"], "func": pcmp_141_stat_depth_var_46},
    "pcmp_142_stat_depth_var_47": {"inputs": ["high", "low", "close"], "func": pcmp_142_stat_depth_var_47},
    "pcmp_143_stat_depth_var_48": {"inputs": ["high", "low", "close"], "func": pcmp_143_stat_depth_var_48},
    "pcmp_144_stat_depth_var_49": {"inputs": ["high", "low", "close"], "func": pcmp_144_stat_depth_var_49},
    "pcmp_145_stat_depth_var_50": {"inputs": ["high", "low", "close"], "func": pcmp_145_stat_depth_var_50},
    "pcmp_146_stat_depth_var_51": {"inputs": ["high", "low", "close"], "func": pcmp_146_stat_depth_var_51},
    "pcmp_147_stat_depth_var_52": {"inputs": ["high", "low", "close"], "func": pcmp_147_stat_depth_var_52},
    "pcmp_148_stat_depth_var_53": {"inputs": ["high", "low", "close"], "func": pcmp_148_stat_depth_var_53},
    "pcmp_149_stat_depth_var_54": {"inputs": ["high", "low", "close"], "func": pcmp_149_stat_depth_var_54},
    "pcmp_150_stat_depth_var_55": {"inputs": ["high", "low", "close"], "func": pcmp_150_stat_depth_var_55},
}
