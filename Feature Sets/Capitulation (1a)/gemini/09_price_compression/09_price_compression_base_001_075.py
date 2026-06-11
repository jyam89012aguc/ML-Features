"""
Price Compression — Base Features 001–075
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

def pcmp_001_hl_range_ratio_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_001_hl_range_ratio_21d feature"""
    # (High - Low) / Close
    r = (high - low)
    return _safe_div(r, (high + low) / 2.0)

def pcmp_002_hl_range_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_002_hl_range_zscore_252d feature"""
    r = (high - low)
    return (r - r.rolling(252).mean()) / r.rolling(252).std()

def pcmp_003_hl_range_pct_rank_ath(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_003_hl_range_pct_rank_ath feature"""
    r = (high - low)
    return r.expanding().rank(pct=True)

def pcmp_004_range_compression_ratio_21d_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_004_range_compression_ratio_21d_63d feature"""
    # Short-term range vs Medium-term range
    r21 = (high - low).rolling(21).mean()
    r63 = (high - low).rolling(63).mean()
    return _safe_div(r21, r63)

def pcmp_005_range_compression_ratio_63d_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_005_range_compression_ratio_63d_252d feature"""
    r63 = (high - low).rolling(63).mean()
    r252 = (high - low).rolling(252).mean()
    return _safe_div(r63, r252)


# 016-030: Volatility-Based Compression (Realized Vol)

def pcmp_016_vol_compression_ratio_21d_252d(close: pd.Series) -> pd.Series:
    """pcmp_016_vol_compression_ratio_21d_252d feature"""
    v21 = close.pct_change().rolling(21).std()
    v252 = close.pct_change().rolling(252).std()
    return _safe_div(v21, v252)

def pcmp_017_vol_zscore_252d(close: pd.Series) -> pd.Series:
    """pcmp_017_vol_zscore_252d feature"""
    v = close.pct_change().rolling(21).std()
    return (v - v.rolling(252).mean()) / v.rolling(252).std()

def pcmp_018_bb_width_20_2(close: pd.Series) -> pd.Series:
    """pcmp_018_bb_width_20_2 feature"""
    # Bollinger Band Width: (Upper - Lower) / Mid
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    return _safe_div(4 * std, ma)


# 031-045: Statistical Tightness (Close Clustering)

def pcmp_031_close_proximity_to_ma_20(close: pd.Series) -> pd.Series:
    """pcmp_031_close_proximity_to_ma_20 feature"""
    # Percent distance from 20-day MA
    ma = close.rolling(20).mean()
    return _safe_div(close - ma, ma).abs()

def pcmp_032_close_clustering_index_21d(close: pd.Series) -> pd.Series:
    """pcmp_032_close_clustering_index_21d feature"""
    # Std dev of Close prices over last 21 days normalized by average Close
    return _safe_div(close.rolling(21).std(), close.rolling(21).mean())

def pcmp_033_high_low_overlap_ratio_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_033_high_low_overlap_ratio_5d feature"""
    # Fraction of 5-day range shared by all days
    h_min = high.rolling(5).min()
    l_max = low.rolling(5).max()
    common_range = (h_min - l_max).clip(lower=0)
    total_range = high.rolling(5).max() - low.rolling(5).min()
    return _safe_div(common_range, total_range)


# 046-060: Candle Morphology Compression

def pcmp_046_avg_body_size_ratio_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_046_avg_body_size_ratio_21d feature"""
    # Average abs(Open - Close) / Average (High - Low)
    body = (close - open).abs()
    return _safe_div(body.rolling(21).mean(), close.rolling(21).std()) # Use std as range proxy

def pcmp_047_consecutive_tight_days_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_047_consecutive_tight_days_63d feature"""
    # Count of days where range < 0.5 * 252d average range
    r = high - low
    avg_r = r.rolling(252).mean()
    is_tight = (r < 0.5 * avg_r).astype(int)
    return is_tight.rolling(63).sum()

def pcmp_048_candle_wick_compression_ratio_21d(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_048_candle_wick_compression_ratio_21d feature"""
    # Ratio of wick size to total candle size
    wick = (high - low) - (close - open).abs()
    return _safe_div(wick.rolling(21).mean(), (high - low).rolling(21).mean())


# 061-075: Multi- Horizon Compression Composites

def pcmp_061_tightness_index_composite_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_061_tightness_index_composite_21d feature"""
    # Average of BB Width, Vol Ratio, and HL Ratio
    bbw = pcmp_018_bb_width_20_2(close)
    vr = pcmp_016_vol_compression_ratio_21d_252d(close)
    hlr = pcmp_001_hl_range_ratio_21d(high, low)
    return (bbw + vr + hlr) / 3.0

def pcmp_062_vol_compression_oscillator_63d(close: pd.Series) -> pd.Series:
    """pcmp_062_vol_compression_oscillator_63d feature"""
    # Percentile of 21d vol in 252d distribution
    v21 = close.pct_change().rolling(21).std()
    return v21.rolling(252).rank(pct=True)

def pcmp_063_range_expansion_to_compression_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_063_range_expansion_to_compression_ratio feature"""
    # Ratio of max range in 63d to current 5d avg range
    r = high - low
    return _safe_div(r.rolling(63).max(), r.rolling(5).mean())

def pcmp_064_mktcap_compression_index_21d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """pcmp_064_mktcap_compression_index_21d feature"""
    mc = close * sharesbas
    v_mc = mc.pct_change().rolling(21).std()
    return _safe_div(v_mc, v_mc.rolling(252).mean())

def pcmp_065_underwater_curve_compression_63d(close: pd.Series) -> pd.Series:
    """pcmp_065_underwater_curve_compression_63d feature"""
    # Std dev of the drawdown depth over last 63 days
    h = close.rolling(252).max()
    uw = (close - h) / h
    return uw.rolling(63).std()

def pcmp_066_terminal_range_stability_score(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_066_terminal_range_stability_score feature"""
    # R-squared of the HL range (is the range narrowing linearly?)
    r = high - low
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    return r.rolling(21).apply(_rsq, raw=True)

def pcmp_067_keltner_channel_width_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_067_keltner_channel_width_ratio feature"""
    # ATR / EMA(20)
    ema = close.ewm(span=20).mean()
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(20).mean()
    return _safe_div(atr, ema)

def pcmp_068_price_sideways_duration_21d(close: pd.Series) -> pd.Series:
    """pcmp_068_price_sideways_duration_21d feature"""
    # Consecutive days within 2% of the price 5 days ago
    near = (close / close.shift(5) - 1).abs() < 0.02
    return near.astype(int).groupby((near != near.shift()).cumsum()).cumsum()

def pcmp_069_proximity_to_apex_score_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_069_proximity_to_apex_score_63d feature"""
    # Slope of Highs vs Slope of Lows (negative = converging)
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sh = high.rolling(21).apply(_slope, raw=True)
    sl = low.rolling(21).apply(_slope, raw=True)
    return sh - sl # Converging when high slope < low slope

def pcmp_070_volume_at_compression_peak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pcmp_070_volume_at_compression_peak_63d feature"""
    # Volume on the day of lowest 21-day realized volatility
    v21 = close.pct_change().rolling(21).std()
    min_v_idx = v21.rolling(63).apply(np.argmin, raw=True)
    return volume.iloc[min_v_idx.astype(int)]

def pcmp_071_range_fractal_dimension_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_071_range_fractal_dimension_21d feature"""
    # Log(Total HL Sum) / Log(Window)
    r = high - low
    return _safe_div(np.log(r.rolling(21).sum()), np.log(21))

def pcmp_072_atr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """pcmp_072_atr_zscore_252d feature"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14).mean()
    return (atr - atr.rolling(252).mean()) / atr.rolling(252).std()

def pcmp_073_price_point_density_63d(close: pd.Series) -> pd.Series:
    """pcmp_073_price_point_density_63d feature"""
    # Number of unique prices / total days (lower = price pinning/stalling)
    return close.rolling(63).apply(lambda x: len(np.unique(x)) / 63.0, raw=True)

def pcmp_074_bollinger_bandwidth_zscore_252d(close: pd.Series) -> pd.Series:
    """pcmp_074_bollinger_bandwidth_zscore_252d feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    bw = _safe_div(4 * std, ma)
    return (bw - bw.rolling(252).mean()) / bw.rolling(252).std()

def pcmp_075_price_compression_final_composite(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """pcmp_075_price_compression_final_composite feature"""
    # (1 - BB Width) * (1 - Vol Ratio) * (Range Stability)
    bbw = pcmp_018_bb_width_20_2(close)
    vr = pcmp_016_vol_compression_ratio_21d_252d(close)
    rs = pcmp_066_terminal_range_stability_score(high, low)
    return (1.0 - bbw.clip(0,1)) * (1.0 - vr.clip(0,1)) * rs

def pcmp_030_stat_depth_var_0(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_001_hl_range_ratio_21d"""
    return _zscore_rolling(pcmp_001_hl_range_ratio_21d(high,low), _TD_MON)

def pcmp_031_stat_depth_var_1(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_002_hl_range_zscore_252d"""
    return _rank_pct(pcmp_002_hl_range_zscore_252d(high,low), _TD_MON)

def pcmp_032_stat_depth_var_2(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_003_hl_range_pct_rank_ath"""
    return _zscore_rolling(pcmp_003_hl_range_pct_rank_ath(high,low), _TD_MON)

def pcmp_033_stat_depth_var_3(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_004_range_compression_ratio_21d_63d"""
    return _rank_pct(pcmp_004_range_compression_ratio_21d_63d(high,low), _TD_MON)

def pcmp_034_stat_depth_var_4(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_005_range_compression_ratio_63d_252d"""
    return _zscore_rolling(pcmp_005_range_compression_ratio_63d_252d(high,low), _TD_MON)

def pcmp_035_stat_depth_var_5(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_016_vol_compression_ratio_21d_252d"""
    return _rank_pct(pcmp_016_vol_compression_ratio_21d_252d(high,low), _TD_MON)

def pcmp_036_stat_depth_var_6(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_017_vol_zscore_252d"""
    return _zscore_rolling(pcmp_017_vol_zscore_252d(high,low), _TD_MON)

def pcmp_037_stat_depth_var_7(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_018_bb_width_20_2"""
    return _rank_pct(pcmp_018_bb_width_20_2(high,low), _TD_MON)

def pcmp_038_stat_depth_var_8(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_031_close_proximity_to_ma_20"""
    return _zscore_rolling(pcmp_031_close_proximity_to_ma_20(high,low), _TD_MON)

def pcmp_039_stat_depth_var_9(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_032_close_clustering_index_21d"""
    return _rank_pct(pcmp_032_close_clustering_index_21d(high,low), _TD_MON)

def pcmp_040_stat_depth_var_10(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_033_high_low_overlap_ratio_5d"""
    return _zscore_rolling(pcmp_033_high_low_overlap_ratio_5d(high,low), _TD_MON)

def pcmp_041_stat_depth_var_11(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_046_avg_body_size_ratio_21d"""
    return _rank_pct(pcmp_046_avg_body_size_ratio_21d(high,low), _TD_MON)

def pcmp_042_stat_depth_var_12(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_047_consecutive_tight_days_63d"""
    return _zscore_rolling(pcmp_047_consecutive_tight_days_63d(high,low), _TD_MON)

def pcmp_043_stat_depth_var_13(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_048_candle_wick_compression_ratio_21d"""
    return _rank_pct(pcmp_048_candle_wick_compression_ratio_21d(high,low), _TD_MON)

def pcmp_044_stat_depth_var_14(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_061_tightness_index_composite_21d"""
    return _zscore_rolling(pcmp_061_tightness_index_composite_21d(high,low), _TD_MON)

def pcmp_045_stat_depth_var_15(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_062_vol_compression_oscillator_63d"""
    return _rank_pct(pcmp_062_vol_compression_oscillator_63d(high,low), _TD_MON)

def pcmp_046_stat_depth_var_16(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_063_range_expansion_to_compression_ratio"""
    return _zscore_rolling(pcmp_063_range_expansion_to_compression_ratio(high,low), _TD_MON)

def pcmp_047_stat_depth_var_17(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_064_mktcap_compression_index_21d"""
    return _rank_pct(pcmp_064_mktcap_compression_index_21d(high,low), _TD_MON)

def pcmp_048_stat_depth_var_18(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_065_underwater_curve_compression_63d"""
    return _zscore_rolling(pcmp_065_underwater_curve_compression_63d(high,low), _TD_MON)

def pcmp_049_stat_depth_var_19(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_066_terminal_range_stability_score"""
    return _rank_pct(pcmp_066_terminal_range_stability_score(high,low), _TD_MON)

def pcmp_050_stat_depth_var_20(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_067_keltner_channel_width_ratio"""
    return _zscore_rolling(pcmp_067_keltner_channel_width_ratio(high,low), _TD_MON)

def pcmp_051_stat_depth_var_21(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_068_price_sideways_duration_21d"""
    return _rank_pct(pcmp_068_price_sideways_duration_21d(high,low), _TD_MON)

def pcmp_052_stat_depth_var_22(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_069_proximity_to_apex_score_63d"""
    return _zscore_rolling(pcmp_069_proximity_to_apex_score_63d(high,low), _TD_MON)

def pcmp_053_stat_depth_var_23(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_070_volume_at_compression_peak_63d"""
    return _rank_pct(pcmp_070_volume_at_compression_peak_63d(high,low), _TD_MON)

def pcmp_054_stat_depth_var_24(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_071_range_fractal_dimension_21d"""
    return _zscore_rolling(pcmp_071_range_fractal_dimension_21d(high,low), _TD_MON)

def pcmp_055_stat_depth_var_25(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_072_atr_zscore_252d"""
    return _rank_pct(pcmp_072_atr_zscore_252d(high,low), _TD_MON)

def pcmp_056_stat_depth_var_26(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_073_price_point_density_63d"""
    return _zscore_rolling(pcmp_073_price_point_density_63d(high,low), _TD_MON)

def pcmp_057_stat_depth_var_27(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_074_bollinger_bandwidth_zscore_252d"""
    return _rank_pct(pcmp_074_bollinger_bandwidth_zscore_252d(high,low), _TD_MON)

def pcmp_058_stat_depth_var_28(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_075_price_compression_final_composite"""
    return _zscore_rolling(pcmp_075_price_compression_final_composite(high,low), _TD_MON)

def pcmp_059_stat_depth_var_29(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_001_hl_range_ratio_21d"""
    return _rank_pct(pcmp_001_hl_range_ratio_21d(high,low), _TD_MON)

def pcmp_060_stat_depth_var_30(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_002_hl_range_zscore_252d"""
    return _zscore_rolling(pcmp_002_hl_range_zscore_252d(high,low), _TD_MON)

def pcmp_061_stat_depth_var_31(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_003_hl_range_pct_rank_ath"""
    return _rank_pct(pcmp_003_hl_range_pct_rank_ath(high,low), _TD_MON)

def pcmp_062_stat_depth_var_32(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_004_range_compression_ratio_21d_63d"""
    return _zscore_rolling(pcmp_004_range_compression_ratio_21d_63d(high,low), _TD_MON)

def pcmp_063_stat_depth_var_33(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_005_range_compression_ratio_63d_252d"""
    return _rank_pct(pcmp_005_range_compression_ratio_63d_252d(high,low), _TD_MON)

def pcmp_064_stat_depth_var_34(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_016_vol_compression_ratio_21d_252d"""
    return _zscore_rolling(pcmp_016_vol_compression_ratio_21d_252d(high,low), _TD_MON)

def pcmp_065_stat_depth_var_35(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_017_vol_zscore_252d"""
    return _rank_pct(pcmp_017_vol_zscore_252d(high,low), _TD_MON)

def pcmp_066_stat_depth_var_36(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_018_bb_width_20_2"""
    return _zscore_rolling(pcmp_018_bb_width_20_2(high,low), _TD_MON)

def pcmp_067_stat_depth_var_37(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_031_close_proximity_to_ma_20"""
    return _rank_pct(pcmp_031_close_proximity_to_ma_20(high,low), _TD_MON)

def pcmp_068_stat_depth_var_38(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_032_close_clustering_index_21d"""
    return _zscore_rolling(pcmp_032_close_clustering_index_21d(high,low), _TD_MON)

def pcmp_069_stat_depth_var_39(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_033_high_low_overlap_ratio_5d"""
    return _rank_pct(pcmp_033_high_low_overlap_ratio_5d(high,low), _TD_MON)

def pcmp_070_stat_depth_var_40(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_046_avg_body_size_ratio_21d"""
    return _zscore_rolling(pcmp_046_avg_body_size_ratio_21d(high,low), _TD_MON)

def pcmp_071_stat_depth_var_41(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_047_consecutive_tight_days_63d"""
    return _rank_pct(pcmp_047_consecutive_tight_days_63d(high,low), _TD_MON)

def pcmp_072_stat_depth_var_42(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_048_candle_wick_compression_ratio_21d"""
    return _zscore_rolling(pcmp_048_candle_wick_compression_ratio_21d(high,low), _TD_MON)

def pcmp_073_stat_depth_var_43(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_061_tightness_index_composite_21d"""
    return _rank_pct(pcmp_061_tightness_index_composite_21d(high,low), _TD_MON)

def pcmp_074_stat_depth_var_44(high: pd.Series, low: pd.Series) -> pd.Series:
    """_zscore_rolling variation of pcmp_062_vol_compression_oscillator_63d"""
    return _zscore_rolling(pcmp_062_vol_compression_oscillator_63d(high,low), _TD_MON)

def pcmp_075_stat_depth_var_45(high: pd.Series, low: pd.Series) -> pd.Series:
    """_rank_pct variation of pcmp_063_range_expansion_to_compression_ratio"""
    return _rank_pct(pcmp_063_range_expansion_to_compression_ratio(high,low), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V09_REGISTRY = {
    "pcmp_001_hl_range_ratio_21d": {"inputs": ["high", "low"], "func": pcmp_001_hl_range_ratio_21d},
    "pcmp_002_hl_range_zscore_252d": {"inputs": ["high", "low"], "func": pcmp_002_hl_range_zscore_252d},
    "pcmp_003_hl_range_pct_rank_ath": {"inputs": ["high", "low"], "func": pcmp_003_hl_range_pct_rank_ath},
    "pcmp_004_range_compression_ratio_21d_63d": {"inputs": ["high", "low"], "func": pcmp_004_range_compression_ratio_21d_63d},
    "pcmp_005_range_compression_ratio_63d_252d": {"inputs": ["high", "low"], "func": pcmp_005_range_compression_ratio_63d_252d},
    "pcmp_016_vol_compression_ratio_21d_252d": {"inputs": ["close"], "func": pcmp_016_vol_compression_ratio_21d_252d},
    "pcmp_017_vol_zscore_252d": {"inputs": ["close"], "func": pcmp_017_vol_zscore_252d},
    "pcmp_018_bb_width_20_2": {"inputs": ["close"], "func": pcmp_018_bb_width_20_2},
    "pcmp_031_close_proximity_to_ma_20": {"inputs": ["close"], "func": pcmp_031_close_proximity_to_ma_20},
    "pcmp_032_close_clustering_index_21d": {"inputs": ["close"], "func": pcmp_032_close_clustering_index_21d},
    "pcmp_033_high_low_overlap_ratio_5d": {"inputs": ["high", "low"], "func": pcmp_033_high_low_overlap_ratio_5d},
    "pcmp_046_avg_body_size_ratio_21d": {"inputs": ["open", "close"], "func": pcmp_046_avg_body_size_ratio_21d},
    "pcmp_047_consecutive_tight_days_63d": {"inputs": ["high", "low"], "func": pcmp_047_consecutive_tight_days_63d},
    "pcmp_048_candle_wick_compression_ratio_21d": {"inputs": ["high", "low", "open", "close"], "func": pcmp_048_candle_wick_compression_ratio_21d},
    "pcmp_061_tightness_index_composite_21d": {"inputs": ["close", "high", "low"], "func": pcmp_061_tightness_index_composite_21d},
    "pcmp_062_vol_compression_oscillator_63d": {"inputs": ["close"], "func": pcmp_062_vol_compression_oscillator_63d},
    "pcmp_063_range_expansion_to_compression_ratio": {"inputs": ["high", "low"], "func": pcmp_063_range_expansion_to_compression_ratio},
    "pcmp_064_mktcap_compression_index_21d": {"inputs": ["close", "sharesbas"], "func": pcmp_064_mktcap_compression_index_21d},
    "pcmp_065_underwater_curve_compression_63d": {"inputs": ["close"], "func": pcmp_065_underwater_curve_compression_63d},
    "pcmp_066_terminal_range_stability_score": {"inputs": ["high", "low"], "func": pcmp_066_terminal_range_stability_score},
    "pcmp_067_keltner_channel_width_ratio": {"inputs": ["high", "low", "close"], "func": pcmp_067_keltner_channel_width_ratio},
    "pcmp_068_price_sideways_duration_21d": {"inputs": ["close"], "func": pcmp_068_price_sideways_duration_21d},
    "pcmp_069_proximity_to_apex_score_63d": {"inputs": ["high", "low"], "func": pcmp_069_proximity_to_apex_score_63d},
    "pcmp_070_volume_at_compression_peak_63d": {"inputs": ["close", "volume"], "func": pcmp_070_volume_at_compression_peak_63d},
    "pcmp_071_range_fractal_dimension_21d": {"inputs": ["high", "low"], "func": pcmp_071_range_fractal_dimension_21d},
    "pcmp_072_atr_zscore_252d": {"inputs": ["high", "low", "close"], "func": pcmp_072_atr_zscore_252d},
    "pcmp_073_price_point_density_63d": {"inputs": ["close"], "func": pcmp_073_price_point_density_63d},
    "pcmp_074_bollinger_bandwidth_zscore_252d": {"inputs": ["close"], "func": pcmp_074_bollinger_bandwidth_zscore_252d},
    "pcmp_075_price_compression_final_composite": {"inputs": ["close", "high", "low"], "func": pcmp_075_price_compression_final_composite},
    "pcmp_030_stat_depth_var_0": {"inputs": ["high", "low"], "func": pcmp_030_stat_depth_var_0},
    "pcmp_031_stat_depth_var_1": {"inputs": ["high", "low"], "func": pcmp_031_stat_depth_var_1},
    "pcmp_032_stat_depth_var_2": {"inputs": ["high", "low"], "func": pcmp_032_stat_depth_var_2},
    "pcmp_033_stat_depth_var_3": {"inputs": ["high", "low"], "func": pcmp_033_stat_depth_var_3},
    "pcmp_034_stat_depth_var_4": {"inputs": ["high", "low"], "func": pcmp_034_stat_depth_var_4},
    "pcmp_035_stat_depth_var_5": {"inputs": ["high", "low"], "func": pcmp_035_stat_depth_var_5},
    "pcmp_036_stat_depth_var_6": {"inputs": ["high", "low"], "func": pcmp_036_stat_depth_var_6},
    "pcmp_037_stat_depth_var_7": {"inputs": ["high", "low"], "func": pcmp_037_stat_depth_var_7},
    "pcmp_038_stat_depth_var_8": {"inputs": ["high", "low"], "func": pcmp_038_stat_depth_var_8},
    "pcmp_039_stat_depth_var_9": {"inputs": ["high", "low"], "func": pcmp_039_stat_depth_var_9},
    "pcmp_040_stat_depth_var_10": {"inputs": ["high", "low"], "func": pcmp_040_stat_depth_var_10},
    "pcmp_041_stat_depth_var_11": {"inputs": ["high", "low"], "func": pcmp_041_stat_depth_var_11},
    "pcmp_042_stat_depth_var_12": {"inputs": ["high", "low"], "func": pcmp_042_stat_depth_var_12},
    "pcmp_043_stat_depth_var_13": {"inputs": ["high", "low"], "func": pcmp_043_stat_depth_var_13},
    "pcmp_044_stat_depth_var_14": {"inputs": ["high", "low"], "func": pcmp_044_stat_depth_var_14},
    "pcmp_045_stat_depth_var_15": {"inputs": ["high", "low"], "func": pcmp_045_stat_depth_var_15},
    "pcmp_046_stat_depth_var_16": {"inputs": ["high", "low"], "func": pcmp_046_stat_depth_var_16},
    "pcmp_047_stat_depth_var_17": {"inputs": ["high", "low"], "func": pcmp_047_stat_depth_var_17},
    "pcmp_048_stat_depth_var_18": {"inputs": ["high", "low"], "func": pcmp_048_stat_depth_var_18},
    "pcmp_049_stat_depth_var_19": {"inputs": ["high", "low"], "func": pcmp_049_stat_depth_var_19},
    "pcmp_050_stat_depth_var_20": {"inputs": ["high", "low"], "func": pcmp_050_stat_depth_var_20},
    "pcmp_051_stat_depth_var_21": {"inputs": ["high", "low"], "func": pcmp_051_stat_depth_var_21},
    "pcmp_052_stat_depth_var_22": {"inputs": ["high", "low"], "func": pcmp_052_stat_depth_var_22},
    "pcmp_053_stat_depth_var_23": {"inputs": ["high", "low"], "func": pcmp_053_stat_depth_var_23},
    "pcmp_054_stat_depth_var_24": {"inputs": ["high", "low"], "func": pcmp_054_stat_depth_var_24},
    "pcmp_055_stat_depth_var_25": {"inputs": ["high", "low"], "func": pcmp_055_stat_depth_var_25},
    "pcmp_056_stat_depth_var_26": {"inputs": ["high", "low"], "func": pcmp_056_stat_depth_var_26},
    "pcmp_057_stat_depth_var_27": {"inputs": ["high", "low"], "func": pcmp_057_stat_depth_var_27},
    "pcmp_058_stat_depth_var_28": {"inputs": ["high", "low"], "func": pcmp_058_stat_depth_var_28},
    "pcmp_059_stat_depth_var_29": {"inputs": ["high", "low"], "func": pcmp_059_stat_depth_var_29},
    "pcmp_060_stat_depth_var_30": {"inputs": ["high", "low"], "func": pcmp_060_stat_depth_var_30},
    "pcmp_061_stat_depth_var_31": {"inputs": ["high", "low"], "func": pcmp_061_stat_depth_var_31},
    "pcmp_062_stat_depth_var_32": {"inputs": ["high", "low"], "func": pcmp_062_stat_depth_var_32},
    "pcmp_063_stat_depth_var_33": {"inputs": ["high", "low"], "func": pcmp_063_stat_depth_var_33},
    "pcmp_064_stat_depth_var_34": {"inputs": ["high", "low"], "func": pcmp_064_stat_depth_var_34},
    "pcmp_065_stat_depth_var_35": {"inputs": ["high", "low"], "func": pcmp_065_stat_depth_var_35},
    "pcmp_066_stat_depth_var_36": {"inputs": ["high", "low"], "func": pcmp_066_stat_depth_var_36},
    "pcmp_067_stat_depth_var_37": {"inputs": ["high", "low"], "func": pcmp_067_stat_depth_var_37},
    "pcmp_068_stat_depth_var_38": {"inputs": ["high", "low"], "func": pcmp_068_stat_depth_var_38},
    "pcmp_069_stat_depth_var_39": {"inputs": ["high", "low"], "func": pcmp_069_stat_depth_var_39},
    "pcmp_070_stat_depth_var_40": {"inputs": ["high", "low"], "func": pcmp_070_stat_depth_var_40},
    "pcmp_071_stat_depth_var_41": {"inputs": ["high", "low"], "func": pcmp_071_stat_depth_var_41},
    "pcmp_072_stat_depth_var_42": {"inputs": ["high", "low"], "func": pcmp_072_stat_depth_var_42},
    "pcmp_073_stat_depth_var_43": {"inputs": ["high", "low"], "func": pcmp_073_stat_depth_var_43},
    "pcmp_074_stat_depth_var_44": {"inputs": ["high", "low"], "func": pcmp_074_stat_depth_var_44},
    "pcmp_075_stat_depth_var_45": {"inputs": ["high", "low"], "func": pcmp_075_stat_depth_var_45},
}
