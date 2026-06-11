"""
Trough Clustering — Base Features 001–075
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

def tcl_001_local_minima_count_63d(close: pd.Series) -> pd.Series:
    """tcl_001_local_minima_count_63d feature"""
    # Count of local minima in the last 3 months
    mins = _find_local_minima(close, order=5)
    return mins.rolling(63).sum()

def tcl_002_local_minima_count_252d(close: pd.Series) -> pd.Series:
    """tcl_002_local_minima_count_252d feature"""
    mins = _find_local_minima(close, order=5)
    return mins.rolling(252).sum()

def tcl_003_days_between_minima_avg_252d(close: pd.Series) -> pd.Series:
    """tcl_003_days_between_minima_avg_252d feature"""
    mins = _find_local_minima(close, order=5)
    is_min = (mins == 1)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_min).ffill()
    diffs = indices.diff()
    return diffs.rolling(252).mean()

def tcl_004_minima_intensity_index_63d(close: pd.Series) -> pd.Series:
    """tcl_004_minima_intensity_index_63d feature"""
    # (Count of Minima) / (Standard Deviation of distances between them)
    mins = _find_local_minima(close, order=5)
    cnt = mins.rolling(63).sum()
    is_min = (mins == 1)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_min).ffill()
    dist_std = idx.diff().rolling(63).std()
    return _safe_div(cnt, dist_std)


# 016-030: Repeated Bottom Proximity (Spatial Clustering)

def tcl_016_proximity_to_prior_local_min(close: pd.Series) -> pd.Series:
    """tcl_016_proximity_to_prior_local_min feature"""
    # Close relative to the price level of the last local minimum
    mins = _find_local_minima(close, order=5)
    min_levels = close.where(mins == 1).ffill()
    return _safe_div(close, min_levels)

def tcl_017_price_spread_between_minima_63d(close: pd.Series) -> pd.Series:
    """tcl_017_price_spread_between_minima_63d feature"""
    # Std dev of the price levels of local minima in the last 63 days
    mins = _find_local_minima(close, order=5)
    min_levels = close.where(mins == 1)
    return min_levels.rolling(63).std() / close.rolling(63).mean()

def tcl_018_support_level_persistence_252d(close: pd.Series) -> pd.Series:
    """tcl_018_support_level_persistence_252d feature"""
    # Count of days where Close is within 2% of any local minimum in last 252d
    mins = _find_local_minima(close, order=5)
    min_levels = close.where(mins == 1).ffill()
    # Check current close vs the 'current' support floor
    near = (close / min_levels - 1).abs() < 0.02
    return near.rolling(252).sum()


# 031-045: Multi- Horizon Trough Overlaps

def tcl_031_minima_overlap_21_63_ratio(close: pd.Series) -> pd.Series:
    """tcl_031_minima_overlap_21_63_ratio feature"""
    m21 = _find_local_minima(close, order=3).rolling(63).sum()
    m63 = _find_local_minima(close, order=10).rolling(63).sum()
    return _safe_div(m21, m63)

def tcl_032_minima_concentration_63d(close: pd.Series) -> pd.Series:
    """tcl_032_minima_concentration_63d feature"""
    # Fraction of window spent within 5% of the average minima price
    mins = _find_local_minima(close, order=5)
    min_levels = close.where(mins == 1)
    avg_min = min_levels.rolling(63).mean()
    near = (close / avg_min - 1).abs() < 0.05
    return near.rolling(63).mean()


# 046-060: Asset / Fundamental Trough Clustering

def tcl_046_mktcap_minima_count_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_046_mktcap_minima_count_252d feature"""
    mc = close * sharesbas
    mins = _find_local_minima(mc, order=5)
    return mins.rolling(252).sum()

def tcl_047_revenue_ps_minima_count_ath(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_047_revenue_ps_minima_count_ath feature"""
    revps = _safe_div(revenue, sharesbas)
    mins = _find_local_minima(revps, order=2) # Sparse data
    return mins.expanding().sum()

def tcl_048_equity_ps_minima_count_ath(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_048_equity_ps_minima_count_ath feature"""
    bvps = _safe_div(equity, sharesbas)
    mins = _find_local_minima(bvps, order=2)
    return mins.expanding().sum()


# 061-075: Clustering Stability and Inflection

def tcl_061_minima_velocity_63d(close: pd.Series) -> pd.Series:
    """tcl_061_minima_velocity_63d feature"""
    # Change in minima count per day
    mins = _find_local_minima(close, order=5)
    cnt = mins.rolling(63).sum()
    return cnt.diff(5)

def tcl_062_trough_alignment_index_252d(close: pd.Series) -> pd.Series:
    """tcl_062_trough_alignment_index_252d feature"""
    # Measures how "flat" the line connecting troughs is (1 / Std Dev of trough prices)
    mins = _find_local_minima(close, order=5)
    min_levels = close.where(mins == 1)
    s = min_levels.rolling(252).std() / close.rolling(252).mean()
    return _safe_div(1.0, s)

def tcl_063_trough_renewal_rate_63d(close: pd.Series) -> pd.Series:
    """tcl_063_trough_renewal_rate_63d feature"""
    # Ratio of new 63d lows to local minima count
    l63 = (close == _rolling_min(close, 63)).astype(int).rolling(63).sum()
    mins = _find_local_minima(close, order=5).rolling(63).sum()
    return _safe_div(l63, mins)

def tcl_064_days_since_trough_cluster_peak_252d(close: pd.Series) -> pd.Series:
    """tcl_064_days_since_trough_cluster_peak_252d feature"""
    # Days since the maximum density of minima was achieved
    mins = _find_local_minima(close, order=5)
    dens = mins.rolling(21).sum()
    mx_dens_idx = dens.rolling(252).apply(np.argmax, raw=True)
    return 252 - 1 - mx_dens_idx

def tcl_065_trough_capitulation_score_63d(close: pd.Series) -> pd.Series:
    """tcl_065_trough_capitulation_score_63d feature"""
    # (Minima Count) * (Proximity to ATH Low)
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    prox = _safe_div(close, close.cummin())
    return cnt * (1.0 / prox)

def tcl_066_volume_at_trough_cluster_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """tcl_066_volume_at_trough_cluster_mean_63d feature"""
    # Average volume on local minima days relative to avg volume
    mins = _find_local_minima(close, order=5)
    v_mins = volume.where(mins == 1).rolling(63).mean()
    v_avg = volume.rolling(63).mean()
    return _safe_div(v_mins, v_avg)

def tcl_067_trough_dispersion_zscore_252d(close: pd.Series) -> pd.Series:
    """tcl_067_trough_dispersion_zscore_252d feature"""
    mins = _find_local_minima(close, order=5)
    is_min = (mins == 1)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_min).ffill()
    dist = idx.diff()
    return (dist - dist.rolling(252).mean()) / dist.rolling(252).std()

def tcl_068_consecutive_trough_tests_21d(close: pd.Series) -> pd.Series:
    """tcl_068_consecutive_trough_tests_21d feature"""
    # Days in a row close to the 21-day trough level
    l = _rolling_min(close, 21)
    near = (close <= l * 1.01).astype(int)
    return near.groupby((near == 0).cumsum()).cumsum()

def tcl_069_trough_reclaim_ratio_63d(close: pd.Series) -> pd.Series:
    """tcl_069_trough_reclaim_ratio_63d feature"""
    # Number of times price broke a local min and reclaimed it within 3 days
    mins = _find_local_minima(close, order=5)
    min_levels = close.where(mins == 1).ffill()
    break_low = (close < min_levels.shift(1))
    reclaim = (close > min_levels.shift(1)) & (break_low.shift(1) | break_low.shift(2))
    return reclaim.rolling(63).sum().astype(int)

def tcl_070_trough_stability_duration_252d(close: pd.Series) -> pd.Series:
    """tcl_070_trough_stability_duration_252d feature"""
    # Longest period without a new local minimum
    mins = _find_local_minima(close, order=5)
    is_not_min = (mins == 0).astype(int)
    return is_not_min.groupby((mins == 1).cumsum()).cumsum().rolling(252).max()

def tcl_071_trough_amplitude_volatility_63d(close: pd.Series) -> pd.Series:
    """tcl_071_trough_amplitude_volatility_63d feature"""
    # Std dev of trough price levels
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    return levels.rolling(63).std()

def tcl_072_ratio_of_troughs_in_lower_quartile_252d(close: pd.Series) -> pd.Series:
    """tcl_072_ratio_of_troughs_in_lower_quartile_252d feature"""
    mins = _find_local_minima(close, order=5)
    q25 = close.rolling(252).quantile(0.25)
    is_low_min = (mins == 1) & (close < q25)
    return _safe_div(is_low_min.rolling(252).sum(), mins.rolling(252).sum())

def tcl_073_trough_clustering_final_composite(close: pd.Series) -> pd.Series:
    """tcl_073_trough_clustering_final_composite feature"""
    # (Minima Count) * (Stability) / (Dispersion)
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    align = tcl_062_trough_alignment_index_252d(close)
    return cnt * align

def tcl_074_mktcap_trough_alignment_index_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_074_mktcap_trough_alignment_index_252d feature"""
    mc = close * sharesbas
    mins = _find_local_minima(mc, order=5)
    levels = mc.where(mins == 1)
    s = levels.rolling(252).std() / mc.rolling(252).mean()
    return _safe_div(1.0, s)

def tcl_075_trough_density_acceleration_21d(close: pd.Series) -> pd.Series:
    """tcl_075_trough_density_acceleration_21d feature"""
    # 2nd derivative of minima count
    cnt = _find_local_minima(close, order=5).rolling(21).sum()
    return cnt.diff(5).diff(5)

def tcl_028_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_001_local_minima_count_63d"""
    return _zscore_rolling(tcl_001_local_minima_count_63d(close), _TD_MON)

def tcl_029_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_002_local_minima_count_252d"""
    return _rank_pct(tcl_002_local_minima_count_252d(close), _TD_MON)

def tcl_030_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_003_days_between_minima_avg_252d"""
    return _zscore_rolling(tcl_003_days_between_minima_avg_252d(close), _TD_MON)

def tcl_031_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_004_minima_intensity_index_63d"""
    return _rank_pct(tcl_004_minima_intensity_index_63d(close), _TD_MON)

def tcl_032_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_016_proximity_to_prior_local_min"""
    return _zscore_rolling(tcl_016_proximity_to_prior_local_min(close), _TD_MON)

def tcl_033_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_017_price_spread_between_minima_63d"""
    return _rank_pct(tcl_017_price_spread_between_minima_63d(close), _TD_MON)

def tcl_034_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_018_support_level_persistence_252d"""
    return _zscore_rolling(tcl_018_support_level_persistence_252d(close), _TD_MON)

def tcl_035_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_031_minima_overlap_21_63_ratio"""
    return _rank_pct(tcl_031_minima_overlap_21_63_ratio(close), _TD_MON)

def tcl_036_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_032_minima_concentration_63d"""
    return _zscore_rolling(tcl_032_minima_concentration_63d(close), _TD_MON)

def tcl_037_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_046_mktcap_minima_count_252d"""
    return _rank_pct(tcl_046_mktcap_minima_count_252d(close), _TD_MON)

def tcl_038_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_047_revenue_ps_minima_count_ath"""
    return _zscore_rolling(tcl_047_revenue_ps_minima_count_ath(close), _TD_MON)

def tcl_039_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_048_equity_ps_minima_count_ath"""
    return _rank_pct(tcl_048_equity_ps_minima_count_ath(close), _TD_MON)

def tcl_040_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_061_minima_velocity_63d"""
    return _zscore_rolling(tcl_061_minima_velocity_63d(close), _TD_MON)

def tcl_041_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_062_trough_alignment_index_252d"""
    return _rank_pct(tcl_062_trough_alignment_index_252d(close), _TD_MON)

def tcl_042_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_063_trough_renewal_rate_63d"""
    return _zscore_rolling(tcl_063_trough_renewal_rate_63d(close), _TD_MON)

def tcl_043_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_064_days_since_trough_cluster_peak_252d"""
    return _rank_pct(tcl_064_days_since_trough_cluster_peak_252d(close), _TD_MON)

def tcl_044_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_065_trough_capitulation_score_63d"""
    return _zscore_rolling(tcl_065_trough_capitulation_score_63d(close), _TD_MON)

def tcl_045_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_066_volume_at_trough_cluster_mean_63d"""
    return _rank_pct(tcl_066_volume_at_trough_cluster_mean_63d(close), _TD_MON)

def tcl_046_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_067_trough_dispersion_zscore_252d"""
    return _zscore_rolling(tcl_067_trough_dispersion_zscore_252d(close), _TD_MON)

def tcl_047_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_068_consecutive_trough_tests_21d"""
    return _rank_pct(tcl_068_consecutive_trough_tests_21d(close), _TD_MON)

def tcl_048_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_069_trough_reclaim_ratio_63d"""
    return _zscore_rolling(tcl_069_trough_reclaim_ratio_63d(close), _TD_MON)

def tcl_049_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_070_trough_stability_duration_252d"""
    return _rank_pct(tcl_070_trough_stability_duration_252d(close), _TD_MON)

def tcl_050_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_071_trough_amplitude_volatility_63d"""
    return _zscore_rolling(tcl_071_trough_amplitude_volatility_63d(close), _TD_MON)

def tcl_051_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_072_ratio_of_troughs_in_lower_quartile_252d"""
    return _rank_pct(tcl_072_ratio_of_troughs_in_lower_quartile_252d(close), _TD_MON)

def tcl_052_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_073_trough_clustering_final_composite"""
    return _zscore_rolling(tcl_073_trough_clustering_final_composite(close), _TD_MON)

def tcl_053_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_074_mktcap_trough_alignment_index_252d"""
    return _rank_pct(tcl_074_mktcap_trough_alignment_index_252d(close), _TD_MON)

def tcl_054_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_075_trough_density_acceleration_21d"""
    return _zscore_rolling(tcl_075_trough_density_acceleration_21d(close), _TD_MON)

def tcl_055_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_001_local_minima_count_63d"""
    return _rank_pct(tcl_001_local_minima_count_63d(close), _TD_MON)

def tcl_056_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_002_local_minima_count_252d"""
    return _zscore_rolling(tcl_002_local_minima_count_252d(close), _TD_MON)

def tcl_057_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_003_days_between_minima_avg_252d"""
    return _rank_pct(tcl_003_days_between_minima_avg_252d(close), _TD_MON)

def tcl_058_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_004_minima_intensity_index_63d"""
    return _zscore_rolling(tcl_004_minima_intensity_index_63d(close), _TD_MON)

def tcl_059_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_016_proximity_to_prior_local_min"""
    return _rank_pct(tcl_016_proximity_to_prior_local_min(close), _TD_MON)

def tcl_060_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_017_price_spread_between_minima_63d"""
    return _zscore_rolling(tcl_017_price_spread_between_minima_63d(close), _TD_MON)

def tcl_061_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_018_support_level_persistence_252d"""
    return _rank_pct(tcl_018_support_level_persistence_252d(close), _TD_MON)

def tcl_062_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_031_minima_overlap_21_63_ratio"""
    return _zscore_rolling(tcl_031_minima_overlap_21_63_ratio(close), _TD_MON)

def tcl_063_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_032_minima_concentration_63d"""
    return _rank_pct(tcl_032_minima_concentration_63d(close), _TD_MON)

def tcl_064_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_046_mktcap_minima_count_252d"""
    return _zscore_rolling(tcl_046_mktcap_minima_count_252d(close), _TD_MON)

def tcl_065_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_047_revenue_ps_minima_count_ath"""
    return _rank_pct(tcl_047_revenue_ps_minima_count_ath(close), _TD_MON)

def tcl_066_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_048_equity_ps_minima_count_ath"""
    return _zscore_rolling(tcl_048_equity_ps_minima_count_ath(close), _TD_MON)

def tcl_067_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_061_minima_velocity_63d"""
    return _rank_pct(tcl_061_minima_velocity_63d(close), _TD_MON)

def tcl_068_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_062_trough_alignment_index_252d"""
    return _zscore_rolling(tcl_062_trough_alignment_index_252d(close), _TD_MON)

def tcl_069_stat_depth_var_41(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_063_trough_renewal_rate_63d"""
    return _rank_pct(tcl_063_trough_renewal_rate_63d(close), _TD_MON)

def tcl_070_stat_depth_var_42(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_064_days_since_trough_cluster_peak_252d"""
    return _zscore_rolling(tcl_064_days_since_trough_cluster_peak_252d(close), _TD_MON)

def tcl_071_stat_depth_var_43(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_065_trough_capitulation_score_63d"""
    return _rank_pct(tcl_065_trough_capitulation_score_63d(close), _TD_MON)

def tcl_072_stat_depth_var_44(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_066_volume_at_trough_cluster_mean_63d"""
    return _zscore_rolling(tcl_066_volume_at_trough_cluster_mean_63d(close), _TD_MON)

def tcl_073_stat_depth_var_45(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_067_trough_dispersion_zscore_252d"""
    return _rank_pct(tcl_067_trough_dispersion_zscore_252d(close), _TD_MON)

def tcl_074_stat_depth_var_46(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of tcl_068_consecutive_trough_tests_21d"""
    return _zscore_rolling(tcl_068_consecutive_trough_tests_21d(close), _TD_MON)

def tcl_075_stat_depth_var_47(close: pd.Series) -> pd.Series:
    """_rank_pct variation of tcl_069_trough_reclaim_ratio_63d"""
    return _rank_pct(tcl_069_trough_reclaim_ratio_63d(close), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V10_REGISTRY = {
    "tcl_001_local_minima_count_63d": {"inputs": ["close"], "func": tcl_001_local_minima_count_63d},
    "tcl_002_local_minima_count_252d": {"inputs": ["close"], "func": tcl_002_local_minima_count_252d},
    "tcl_003_days_between_minima_avg_252d": {"inputs": ["close"], "func": tcl_003_days_between_minima_avg_252d},
    "tcl_004_minima_intensity_index_63d": {"inputs": ["close"], "func": tcl_004_minima_intensity_index_63d},
    "tcl_016_proximity_to_prior_local_min": {"inputs": ["close"], "func": tcl_016_proximity_to_prior_local_min},
    "tcl_017_price_spread_between_minima_63d": {"inputs": ["close"], "func": tcl_017_price_spread_between_minima_63d},
    "tcl_018_support_level_persistence_252d": {"inputs": ["close"], "func": tcl_018_support_level_persistence_252d},
    "tcl_031_minima_overlap_21_63_ratio": {"inputs": ["close"], "func": tcl_031_minima_overlap_21_63_ratio},
    "tcl_032_minima_concentration_63d": {"inputs": ["close"], "func": tcl_032_minima_concentration_63d},
    "tcl_046_mktcap_minima_count_252d": {"inputs": ["close", "sharesbas"], "func": tcl_046_mktcap_minima_count_252d},
    "tcl_047_revenue_ps_minima_count_ath": {"inputs": ["revenue", "sharesbas"], "func": tcl_047_revenue_ps_minima_count_ath},
    "tcl_048_equity_ps_minima_count_ath": {"inputs": ["equity", "sharesbas"], "func": tcl_048_equity_ps_minima_count_ath},
    "tcl_061_minima_velocity_63d": {"inputs": ["close"], "func": tcl_061_minima_velocity_63d},
    "tcl_062_trough_alignment_index_252d": {"inputs": ["close"], "func": tcl_062_trough_alignment_index_252d},
    "tcl_063_trough_renewal_rate_63d": {"inputs": ["close"], "func": tcl_063_trough_renewal_rate_63d},
    "tcl_064_days_since_trough_cluster_peak_252d": {"inputs": ["close"], "func": tcl_064_days_since_trough_cluster_peak_252d},
    "tcl_065_trough_capitulation_score_63d": {"inputs": ["close"], "func": tcl_065_trough_capitulation_score_63d},
    "tcl_066_volume_at_trough_cluster_mean_63d": {"inputs": ["close", "volume"], "func": tcl_066_volume_at_trough_cluster_mean_63d},
    "tcl_067_trough_dispersion_zscore_252d": {"inputs": ["close"], "func": tcl_067_trough_dispersion_zscore_252d},
    "tcl_068_consecutive_trough_tests_21d": {"inputs": ["close"], "func": tcl_068_consecutive_trough_tests_21d},
    "tcl_069_trough_reclaim_ratio_63d": {"inputs": ["close"], "func": tcl_069_trough_reclaim_ratio_63d},
    "tcl_070_trough_stability_duration_252d": {"inputs": ["close"], "func": tcl_070_trough_stability_duration_252d},
    "tcl_071_trough_amplitude_volatility_63d": {"inputs": ["close"], "func": tcl_071_trough_amplitude_volatility_63d},
    "tcl_072_ratio_of_troughs_in_lower_quartile_252d": {"inputs": ["close"], "func": tcl_072_ratio_of_troughs_in_lower_quartile_252d},
    "tcl_073_trough_clustering_final_composite": {"inputs": ["close"], "func": tcl_073_trough_clustering_final_composite},
    "tcl_074_mktcap_trough_alignment_index_252d": {"inputs": ["close", "sharesbas"], "func": tcl_074_mktcap_trough_alignment_index_252d},
    "tcl_075_trough_density_acceleration_21d": {"inputs": ["close"], "func": tcl_075_trough_density_acceleration_21d},
    "tcl_028_stat_depth_var_0": {"inputs": ["close"], "func": tcl_028_stat_depth_var_0},
    "tcl_029_stat_depth_var_1": {"inputs": ["close"], "func": tcl_029_stat_depth_var_1},
    "tcl_030_stat_depth_var_2": {"inputs": ["close"], "func": tcl_030_stat_depth_var_2},
    "tcl_031_stat_depth_var_3": {"inputs": ["close"], "func": tcl_031_stat_depth_var_3},
    "tcl_032_stat_depth_var_4": {"inputs": ["close"], "func": tcl_032_stat_depth_var_4},
    "tcl_033_stat_depth_var_5": {"inputs": ["close"], "func": tcl_033_stat_depth_var_5},
    "tcl_034_stat_depth_var_6": {"inputs": ["close"], "func": tcl_034_stat_depth_var_6},
    "tcl_035_stat_depth_var_7": {"inputs": ["close"], "func": tcl_035_stat_depth_var_7},
    "tcl_036_stat_depth_var_8": {"inputs": ["close"], "func": tcl_036_stat_depth_var_8},
    "tcl_037_stat_depth_var_9": {"inputs": ["close"], "func": tcl_037_stat_depth_var_9},
    "tcl_038_stat_depth_var_10": {"inputs": ["close"], "func": tcl_038_stat_depth_var_10},
    "tcl_039_stat_depth_var_11": {"inputs": ["close"], "func": tcl_039_stat_depth_var_11},
    "tcl_040_stat_depth_var_12": {"inputs": ["close"], "func": tcl_040_stat_depth_var_12},
    "tcl_041_stat_depth_var_13": {"inputs": ["close"], "func": tcl_041_stat_depth_var_13},
    "tcl_042_stat_depth_var_14": {"inputs": ["close"], "func": tcl_042_stat_depth_var_14},
    "tcl_043_stat_depth_var_15": {"inputs": ["close"], "func": tcl_043_stat_depth_var_15},
    "tcl_044_stat_depth_var_16": {"inputs": ["close"], "func": tcl_044_stat_depth_var_16},
    "tcl_045_stat_depth_var_17": {"inputs": ["close"], "func": tcl_045_stat_depth_var_17},
    "tcl_046_stat_depth_var_18": {"inputs": ["close"], "func": tcl_046_stat_depth_var_18},
    "tcl_047_stat_depth_var_19": {"inputs": ["close"], "func": tcl_047_stat_depth_var_19},
    "tcl_048_stat_depth_var_20": {"inputs": ["close"], "func": tcl_048_stat_depth_var_20},
    "tcl_049_stat_depth_var_21": {"inputs": ["close"], "func": tcl_049_stat_depth_var_21},
    "tcl_050_stat_depth_var_22": {"inputs": ["close"], "func": tcl_050_stat_depth_var_22},
    "tcl_051_stat_depth_var_23": {"inputs": ["close"], "func": tcl_051_stat_depth_var_23},
    "tcl_052_stat_depth_var_24": {"inputs": ["close"], "func": tcl_052_stat_depth_var_24},
    "tcl_053_stat_depth_var_25": {"inputs": ["close"], "func": tcl_053_stat_depth_var_25},
    "tcl_054_stat_depth_var_26": {"inputs": ["close"], "func": tcl_054_stat_depth_var_26},
    "tcl_055_stat_depth_var_27": {"inputs": ["close"], "func": tcl_055_stat_depth_var_27},
    "tcl_056_stat_depth_var_28": {"inputs": ["close"], "func": tcl_056_stat_depth_var_28},
    "tcl_057_stat_depth_var_29": {"inputs": ["close"], "func": tcl_057_stat_depth_var_29},
    "tcl_058_stat_depth_var_30": {"inputs": ["close"], "func": tcl_058_stat_depth_var_30},
    "tcl_059_stat_depth_var_31": {"inputs": ["close"], "func": tcl_059_stat_depth_var_31},
    "tcl_060_stat_depth_var_32": {"inputs": ["close"], "func": tcl_060_stat_depth_var_32},
    "tcl_061_stat_depth_var_33": {"inputs": ["close"], "func": tcl_061_stat_depth_var_33},
    "tcl_062_stat_depth_var_34": {"inputs": ["close"], "func": tcl_062_stat_depth_var_34},
    "tcl_063_stat_depth_var_35": {"inputs": ["close"], "func": tcl_063_stat_depth_var_35},
    "tcl_064_stat_depth_var_36": {"inputs": ["close"], "func": tcl_064_stat_depth_var_36},
    "tcl_065_stat_depth_var_37": {"inputs": ["close"], "func": tcl_065_stat_depth_var_37},
    "tcl_066_stat_depth_var_38": {"inputs": ["close"], "func": tcl_066_stat_depth_var_38},
    "tcl_067_stat_depth_var_39": {"inputs": ["close"], "func": tcl_067_stat_depth_var_39},
    "tcl_068_stat_depth_var_40": {"inputs": ["close"], "func": tcl_068_stat_depth_var_40},
    "tcl_069_stat_depth_var_41": {"inputs": ["close"], "func": tcl_069_stat_depth_var_41},
    "tcl_070_stat_depth_var_42": {"inputs": ["close"], "func": tcl_070_stat_depth_var_42},
    "tcl_071_stat_depth_var_43": {"inputs": ["close"], "func": tcl_071_stat_depth_var_43},
    "tcl_072_stat_depth_var_44": {"inputs": ["close"], "func": tcl_072_stat_depth_var_44},
    "tcl_073_stat_depth_var_45": {"inputs": ["close"], "func": tcl_073_stat_depth_var_45},
    "tcl_074_stat_depth_var_46": {"inputs": ["close"], "func": tcl_074_stat_depth_var_46},
    "tcl_075_stat_depth_var_47": {"inputs": ["close"], "func": tcl_075_stat_depth_var_47},
}
