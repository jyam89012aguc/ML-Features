"""
Peak to Trough — Base Features 001–075
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

def ptt_001_peak_to_trough_ratio_21d(close: pd.Series) -> pd.Series:
    """ptt_001_peak_to_trough_ratio_21d feature"""
    # Ratio of rolling max to rolling min (high / low)
    h = _rolling_max(close, 21)
    l = _rolling_min(close, 21)
    return _safe_div(h, l)

def ptt_002_peak_to_trough_ratio_63d(close: pd.Series) -> pd.Series:
    """ptt_002_peak_to_trough_ratio_63d feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    return _safe_div(h, l)

def ptt_003_peak_to_trough_ratio_252d(close: pd.Series) -> pd.Series:
    """ptt_003_peak_to_trough_ratio_252d feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    return _safe_div(h, l)

def ptt_004_peak_to_trough_ratio_1260d(close: pd.Series) -> pd.Series:
    """ptt_004_peak_to_trough_ratio_1260d feature"""
    h = _rolling_max(close, 1260)
    l = _rolling_min(close, 1260)
    return _safe_div(h, l)

def ptt_005_peak_to_trough_ratio_ath(close: pd.Series) -> pd.Series:
    """ptt_005_peak_to_trough_ratio_ath feature"""
    h = close.cummax()
    l = close.cummin()
    return _safe_div(h, l)

def ptt_006_drawdown_to_ptt_ratio_252d(close: pd.Series) -> pd.Series:
    """ptt_006_drawdown_to_ptt_ratio_252d feature"""
    # Current drawdown relative to the total peak-trough distance in window
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    dd = (h - close)
    total_range = h - l
    return _safe_div(dd, total_range)

def ptt_007_log_peak_to_trough_spread_252d(close: pd.Series) -> pd.Series:
    """ptt_007_log_peak_to_trough_spread_252d feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    return np.log(h) - np.log(l)


# 016-030: Recovery Fraction So Far (Distance from Trough)

def ptt_016_recovery_fraction_21d(close: pd.Series) -> pd.Series:
    """ptt_016_recovery_fraction_21d feature"""
    # (Close - Min) / (Max - Min)
    h = _rolling_max(close, 21)
    l = _rolling_min(close, 21)
    return _safe_div(close - l, h - l)

def ptt_017_recovery_fraction_63d(close: pd.Series) -> pd.Series:
    """ptt_017_recovery_fraction_63d feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    return _safe_div(close - l, h - l)

def ptt_018_recovery_fraction_252d(close: pd.Series) -> pd.Series:
    """ptt_018_recovery_fraction_252d feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    return _safe_div(close - l, h - l)

def ptt_019_recovery_fraction_ath(close: pd.Series) -> pd.Series:
    """ptt_019_recovery_fraction_ath feature"""
    h = close.cummax()
    l = close.cummin()
    return _safe_div(close - l, h - l)

def ptt_020_recovery_ratio_close_to_prev_peak(close: pd.Series) -> pd.Series:
    """ptt_020_recovery_ratio_close_to_prev_peak feature"""
    # Ratio of current price to the peak that preceded the current trough
    h = close.cummax()
    return _safe_div(close, h)


# 031-045: Trough Timing and Dynamics

def ptt_031_days_since_peak_to_trough_252d(close: pd.Series) -> pd.Series:
    """ptt_031_days_since_peak_to_trough_252d feature"""
    # Days from window high to window low
    def _peak_trough_dist(x):
        return np.argmin(x) - np.argmax(x)
    return close.rolling(252).apply(_peak_trough_dist, raw=True)

def ptt_032_days_since_trough_252d(close: pd.Series) -> pd.Series:
    """ptt_032_days_since_trough_252d feature"""
    l_idx = close.rolling(252).apply(np.argmin, raw=True)
    return 252 - 1 - l_idx

def ptt_033_days_since_trough_ath(close: pd.Series) -> pd.Series:
    """ptt_033_days_since_trough_ath feature"""
    l = close.cummin()
    is_low = (close == l)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_low).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices


# 046-060: Asset / Fundamental Peak-to-Trough Metrics

def ptt_046_mktcap_ptt_ratio_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_046_mktcap_ptt_ratio_252d feature"""
    mc = close * sharesbas
    return _safe_div(_rolling_max(mc, 252), _rolling_min(mc, 252))

def ptt_047_revenue_ps_ptt_ratio_ath(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_047_revenue_ps_ptt_ratio_ath feature"""
    revps = _safe_div(revenue, sharesbas)
    return _safe_div(revps.cummax(), revps.cummin())

def ptt_048_equity_ps_ptt_ratio_ath(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_048_equity_ps_ptt_ratio_ath feature"""
    bvps = _safe_div(equity, sharesbas)
    return _safe_div(bvps.cummax(), bvps.cummin())

def ptt_049_pe_ptt_ratio_252d(close: pd.Series, netinc: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_049_pe_ptt_ratio_252d feature"""
    pe = _safe_div(close * sharesbas, netinc)
    pe = pe.where(pe > 0)
    return _safe_div(_rolling_max(pe, 252), _rolling_min(pe, 252))


# 061-075: Peak-to-Trough Persistence and Volatility

def ptt_061_ptt_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """ptt_061_ptt_ratio_zscore_252d feature"""
    r = ptt_003_peak_to_trough_ratio_252d(close)
    return (r - r.rolling(252).mean()) / r.rolling(252).std()

def ptt_062_recovery_fraction_std_63d(close: pd.Series) -> pd.Series:
    """ptt_062_recovery_fraction_std_63d feature"""
    return ptt_017_recovery_fraction_63d(close).rolling(63).std()

def ptt_063_ptt_volatility_adjusted_252d(close: pd.Series) -> pd.Series:
    """ptt_063_ptt_volatility_adjusted_252d feature"""
    # Ratio / Realized Vol
    r = ptt_003_peak_to_trough_ratio_252d(close)
    v = close.pct_change().rolling(252).std()
    return _safe_div(r, v)

def ptt_064_avg_ptt_ratio_multi_horizon(close: pd.Series) -> pd.Series:
    """ptt_064_avg_ptt_ratio_multi_horizon feature"""
    r21 = ptt_001_peak_to_trough_ratio_21d(close)
    r63 = ptt_002_peak_to_trough_ratio_63d(close)
    r252 = ptt_003_peak_to_trough_ratio_252d(close)
    return (r21 + r63 + r252) / 3.0

def ptt_065_current_close_to_midpoint_252d(close: pd.Series) -> pd.Series:
    """ptt_065_current_close_to_midpoint_252d feature"""
    # Ratio of Close to (Max+Min)/2
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    mid = (h + l) / 2.0
    return _safe_div(close, mid)

def ptt_066_trough_persistence_count_252d(close: pd.Series) -> pd.Series:
    """ptt_066_trough_persistence_count_252d feature"""
    # Number of days where close was within 1% of the 252d trough
    l = _rolling_min(close, 252)
    at_low = (close <= l * 1.01).astype(int)
    return at_low.rolling(252).sum()

def ptt_067_recovery_acceleration_21d(close: pd.Series) -> pd.Series:
    """ptt_067_recovery_acceleration_21d feature"""
    # Change in recovery fraction over last month
    return ptt_017_recovery_fraction_63d(close).diff(21)

def ptt_068_ptt_ratio_expansion_index_63d(close: pd.Series) -> pd.Series:
    """ptt_068_ptt_ratio_expansion_index_63d feature"""
    # Current PTT ratio / Prior year mean PTT ratio
    r = ptt_002_peak_to_trough_ratio_63d(close)
    return _safe_div(r, r.rolling(252).mean())

def ptt_069_integral_of_recovery_fraction_63d(close: pd.Series) -> pd.Series:
    """ptt_069_integral_of_recovery_fraction_63d feature"""
    return ptt_017_recovery_fraction_63d(close).rolling(63).sum()

def ptt_070_peak_to_trough_slope_252d(close: pd.Series) -> pd.Series:
    """ptt_070_peak_to_trough_slope_252d feature"""
    # Annualized slope of the line connecting peak to current trough
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    def _slope(y):
        p_idx = np.argmax(y)
        t_idx = np.argmin(y)
        if p_idx == t_idx: return 0.0
        return (y[t_idx] - y[p_idx]) / (t_idx - p_idx + _EPS)
    return close.rolling(252).apply(_slope, raw=True)

def ptt_071_proximity_to_midpoint_ath(close: pd.Series) -> pd.Series:
    """ptt_071_proximity_to_midpoint_ath feature"""
    h = close.cummax()
    l = close.cummin()
    mid = (h + l) / 2.0
    return _safe_div(close, mid)

def ptt_072_recovery_climax_indicator_21d(close: pd.Series) -> pd.Series:
    """ptt_072_recovery_climax_indicator_21d feature"""
    # (Recovery Fraction) * (Volume / Avg Volume)
    rf = ptt_016_recovery_fraction_21d(close)
    # Note: volume input not passed here, using dummy if not available or just RF
    return rf

def ptt_073_mktcap_recovery_fraction_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_073_mktcap_recovery_fraction_252d feature"""
    mc = close * sharesbas
    h = _rolling_max(mc, 252)
    l = _rolling_min(mc, 252)
    return _safe_div(mc - l, h - l)

def ptt_074_ptt_tail_risk_index_252d(close: pd.Series) -> pd.Series:
    """ptt_074_ptt_tail_risk_index_252d feature"""
    # 90th percentile PTT ratio vs median
    r = ptt_001_peak_to_trough_ratio_21d(close)
    return _safe_div(r.rolling(252).quantile(0.9), r.rolling(252).median())

def ptt_075_peak_to_trough_final_composite(close: pd.Series) -> pd.Series:
    """ptt_075_peak_to_trough_final_composite feature"""
    # Weighted average of recovery fractions
    rf21 = ptt_016_recovery_fraction_21d(close)
    rf63 = ptt_017_recovery_fraction_63d(close)
    rf252 = ptt_018_recovery_fraction_252d(close)
    return (0.5 * rf21 + 0.3 * rf63 + 0.2 * rf252)

def ptt_035_stat_depth_var_0(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_001_peak_to_trough_ratio_21d"""
    return _zscore_rolling(ptt_001_peak_to_trough_ratio_21d(close), _TD_MON)

def ptt_036_stat_depth_var_1(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_002_peak_to_trough_ratio_63d"""
    return _rank_pct(ptt_002_peak_to_trough_ratio_63d(close), _TD_MON)

def ptt_037_stat_depth_var_2(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_003_peak_to_trough_ratio_252d"""
    return _zscore_rolling(ptt_003_peak_to_trough_ratio_252d(close), _TD_MON)

def ptt_038_stat_depth_var_3(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_004_peak_to_trough_ratio_1260d"""
    return _rank_pct(ptt_004_peak_to_trough_ratio_1260d(close), _TD_MON)

def ptt_039_stat_depth_var_4(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_005_peak_to_trough_ratio_ath"""
    return _zscore_rolling(ptt_005_peak_to_trough_ratio_ath(close), _TD_MON)

def ptt_040_stat_depth_var_5(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_006_drawdown_to_ptt_ratio_252d"""
    return _rank_pct(ptt_006_drawdown_to_ptt_ratio_252d(close), _TD_MON)

def ptt_041_stat_depth_var_6(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_007_log_peak_to_trough_spread_252d"""
    return _zscore_rolling(ptt_007_log_peak_to_trough_spread_252d(close), _TD_MON)

def ptt_042_stat_depth_var_7(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_016_recovery_fraction_21d"""
    return _rank_pct(ptt_016_recovery_fraction_21d(close), _TD_MON)

def ptt_043_stat_depth_var_8(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_017_recovery_fraction_63d"""
    return _zscore_rolling(ptt_017_recovery_fraction_63d(close), _TD_MON)

def ptt_044_stat_depth_var_9(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_018_recovery_fraction_252d"""
    return _rank_pct(ptt_018_recovery_fraction_252d(close), _TD_MON)

def ptt_045_stat_depth_var_10(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_019_recovery_fraction_ath"""
    return _zscore_rolling(ptt_019_recovery_fraction_ath(close), _TD_MON)

def ptt_046_stat_depth_var_11(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_020_recovery_ratio_close_to_prev_peak"""
    return _rank_pct(ptt_020_recovery_ratio_close_to_prev_peak(close), _TD_MON)

def ptt_047_stat_depth_var_12(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_031_days_since_peak_to_trough_252d"""
    return _zscore_rolling(ptt_031_days_since_peak_to_trough_252d(close), _TD_MON)

def ptt_048_stat_depth_var_13(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_032_days_since_trough_252d"""
    return _rank_pct(ptt_032_days_since_trough_252d(close), _TD_MON)

def ptt_049_stat_depth_var_14(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_033_days_since_trough_ath"""
    return _zscore_rolling(ptt_033_days_since_trough_ath(close), _TD_MON)

def ptt_050_stat_depth_var_15(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_046_mktcap_ptt_ratio_252d"""
    return _rank_pct(ptt_046_mktcap_ptt_ratio_252d(close), _TD_MON)

def ptt_051_stat_depth_var_16(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_047_revenue_ps_ptt_ratio_ath"""
    return _zscore_rolling(ptt_047_revenue_ps_ptt_ratio_ath(close), _TD_MON)

def ptt_052_stat_depth_var_17(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_048_equity_ps_ptt_ratio_ath"""
    return _rank_pct(ptt_048_equity_ps_ptt_ratio_ath(close), _TD_MON)

def ptt_053_stat_depth_var_18(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_049_pe_ptt_ratio_252d"""
    return _zscore_rolling(ptt_049_pe_ptt_ratio_252d(close), _TD_MON)

def ptt_054_stat_depth_var_19(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_061_ptt_ratio_zscore_252d"""
    return _rank_pct(ptt_061_ptt_ratio_zscore_252d(close), _TD_MON)

def ptt_055_stat_depth_var_20(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_062_recovery_fraction_std_63d"""
    return _zscore_rolling(ptt_062_recovery_fraction_std_63d(close), _TD_MON)

def ptt_056_stat_depth_var_21(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_063_ptt_volatility_adjusted_252d"""
    return _rank_pct(ptt_063_ptt_volatility_adjusted_252d(close), _TD_MON)

def ptt_057_stat_depth_var_22(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_064_avg_ptt_ratio_multi_horizon"""
    return _zscore_rolling(ptt_064_avg_ptt_ratio_multi_horizon(close), _TD_MON)

def ptt_058_stat_depth_var_23(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_065_current_close_to_midpoint_252d"""
    return _rank_pct(ptt_065_current_close_to_midpoint_252d(close), _TD_MON)

def ptt_059_stat_depth_var_24(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_066_trough_persistence_count_252d"""
    return _zscore_rolling(ptt_066_trough_persistence_count_252d(close), _TD_MON)

def ptt_060_stat_depth_var_25(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_067_recovery_acceleration_21d"""
    return _rank_pct(ptt_067_recovery_acceleration_21d(close), _TD_MON)

def ptt_061_stat_depth_var_26(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_068_ptt_ratio_expansion_index_63d"""
    return _zscore_rolling(ptt_068_ptt_ratio_expansion_index_63d(close), _TD_MON)

def ptt_062_stat_depth_var_27(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_069_integral_of_recovery_fraction_63d"""
    return _rank_pct(ptt_069_integral_of_recovery_fraction_63d(close), _TD_MON)

def ptt_063_stat_depth_var_28(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_070_peak_to_trough_slope_252d"""
    return _zscore_rolling(ptt_070_peak_to_trough_slope_252d(close), _TD_MON)

def ptt_064_stat_depth_var_29(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_071_proximity_to_midpoint_ath"""
    return _rank_pct(ptt_071_proximity_to_midpoint_ath(close), _TD_MON)

def ptt_065_stat_depth_var_30(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_072_recovery_climax_indicator_21d"""
    return _zscore_rolling(ptt_072_recovery_climax_indicator_21d(close), _TD_MON)

def ptt_066_stat_depth_var_31(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_073_mktcap_recovery_fraction_252d"""
    return _rank_pct(ptt_073_mktcap_recovery_fraction_252d(close), _TD_MON)

def ptt_067_stat_depth_var_32(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_074_ptt_tail_risk_index_252d"""
    return _zscore_rolling(ptt_074_ptt_tail_risk_index_252d(close), _TD_MON)

def ptt_068_stat_depth_var_33(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_075_peak_to_trough_final_composite"""
    return _rank_pct(ptt_075_peak_to_trough_final_composite(close), _TD_MON)

def ptt_069_stat_depth_var_34(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_001_peak_to_trough_ratio_21d"""
    return _zscore_rolling(ptt_001_peak_to_trough_ratio_21d(close), _TD_MON)

def ptt_070_stat_depth_var_35(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_002_peak_to_trough_ratio_63d"""
    return _rank_pct(ptt_002_peak_to_trough_ratio_63d(close), _TD_MON)

def ptt_071_stat_depth_var_36(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_003_peak_to_trough_ratio_252d"""
    return _zscore_rolling(ptt_003_peak_to_trough_ratio_252d(close), _TD_MON)

def ptt_072_stat_depth_var_37(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_004_peak_to_trough_ratio_1260d"""
    return _rank_pct(ptt_004_peak_to_trough_ratio_1260d(close), _TD_MON)

def ptt_073_stat_depth_var_38(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_005_peak_to_trough_ratio_ath"""
    return _zscore_rolling(ptt_005_peak_to_trough_ratio_ath(close), _TD_MON)

def ptt_074_stat_depth_var_39(close: pd.Series) -> pd.Series:
    """_rank_pct variation of ptt_006_drawdown_to_ptt_ratio_252d"""
    return _rank_pct(ptt_006_drawdown_to_ptt_ratio_252d(close), _TD_MON)

def ptt_075_stat_depth_var_40(close: pd.Series) -> pd.Series:
    """_zscore_rolling variation of ptt_007_log_peak_to_trough_spread_252d"""
    return _zscore_rolling(ptt_007_log_peak_to_trough_spread_252d(close), _TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────

V07_REGISTRY = {
    "ptt_001_peak_to_trough_ratio_21d": {"inputs": ["close"], "func": ptt_001_peak_to_trough_ratio_21d},
    "ptt_002_peak_to_trough_ratio_63d": {"inputs": ["close"], "func": ptt_002_peak_to_trough_ratio_63d},
    "ptt_003_peak_to_trough_ratio_252d": {"inputs": ["close"], "func": ptt_003_peak_to_trough_ratio_252d},
    "ptt_004_peak_to_trough_ratio_1260d": {"inputs": ["close"], "func": ptt_004_peak_to_trough_ratio_1260d},
    "ptt_005_peak_to_trough_ratio_ath": {"inputs": ["close"], "func": ptt_005_peak_to_trough_ratio_ath},
    "ptt_006_drawdown_to_ptt_ratio_252d": {"inputs": ["close"], "func": ptt_006_drawdown_to_ptt_ratio_252d},
    "ptt_007_log_peak_to_trough_spread_252d": {"inputs": ["close"], "func": ptt_007_log_peak_to_trough_spread_252d},
    "ptt_016_recovery_fraction_21d": {"inputs": ["close"], "func": ptt_016_recovery_fraction_21d},
    "ptt_017_recovery_fraction_63d": {"inputs": ["close"], "func": ptt_017_recovery_fraction_63d},
    "ptt_018_recovery_fraction_252d": {"inputs": ["close"], "func": ptt_018_recovery_fraction_252d},
    "ptt_019_recovery_fraction_ath": {"inputs": ["close"], "func": ptt_019_recovery_fraction_ath},
    "ptt_020_recovery_ratio_close_to_prev_peak": {"inputs": ["close"], "func": ptt_020_recovery_ratio_close_to_prev_peak},
    "ptt_031_days_since_peak_to_trough_252d": {"inputs": ["close"], "func": ptt_031_days_since_peak_to_trough_252d},
    "ptt_032_days_since_trough_252d": {"inputs": ["close"], "func": ptt_032_days_since_trough_252d},
    "ptt_033_days_since_trough_ath": {"inputs": ["close"], "func": ptt_033_days_since_trough_ath},
    "ptt_046_mktcap_ptt_ratio_252d": {"inputs": ["close", "sharesbas"], "func": ptt_046_mktcap_ptt_ratio_252d},
    "ptt_047_revenue_ps_ptt_ratio_ath": {"inputs": ["revenue", "sharesbas"], "func": ptt_047_revenue_ps_ptt_ratio_ath},
    "ptt_048_equity_ps_ptt_ratio_ath": {"inputs": ["equity", "sharesbas"], "func": ptt_048_equity_ps_ptt_ratio_ath},
    "ptt_049_pe_ptt_ratio_252d": {"inputs": ["close", "netinc", "sharesbas"], "func": ptt_049_pe_ptt_ratio_252d},
    "ptt_061_ptt_ratio_zscore_252d": {"inputs": ["close"], "func": ptt_061_ptt_ratio_zscore_252d},
    "ptt_062_recovery_fraction_std_63d": {"inputs": ["close"], "func": ptt_062_recovery_fraction_std_63d},
    "ptt_063_ptt_volatility_adjusted_252d": {"inputs": ["close"], "func": ptt_063_ptt_volatility_adjusted_252d},
    "ptt_064_avg_ptt_ratio_multi_horizon": {"inputs": ["close"], "func": ptt_064_avg_ptt_ratio_multi_horizon},
    "ptt_065_current_close_to_midpoint_252d": {"inputs": ["close"], "func": ptt_065_current_close_to_midpoint_252d},
    "ptt_066_trough_persistence_count_252d": {"inputs": ["close"], "func": ptt_066_trough_persistence_count_252d},
    "ptt_067_recovery_acceleration_21d": {"inputs": ["close"], "func": ptt_067_recovery_acceleration_21d},
    "ptt_068_ptt_ratio_expansion_index_63d": {"inputs": ["close"], "func": ptt_068_ptt_ratio_expansion_index_63d},
    "ptt_069_integral_of_recovery_fraction_63d": {"inputs": ["close"], "func": ptt_069_integral_of_recovery_fraction_63d},
    "ptt_070_peak_to_trough_slope_252d": {"inputs": ["close"], "func": ptt_070_peak_to_trough_slope_252d},
    "ptt_071_proximity_to_midpoint_ath": {"inputs": ["close"], "func": ptt_071_proximity_to_midpoint_ath},
    "ptt_072_recovery_climax_indicator_21d": {"inputs": ["close"], "func": ptt_072_recovery_climax_indicator_21d},
    "ptt_073_mktcap_recovery_fraction_252d": {"inputs": ["close", "sharesbas"], "func": ptt_073_mktcap_recovery_fraction_252d},
    "ptt_074_ptt_tail_risk_index_252d": {"inputs": ["close"], "func": ptt_074_ptt_tail_risk_index_252d},
    "ptt_075_peak_to_trough_final_composite": {"inputs": ["close"], "func": ptt_075_peak_to_trough_final_composite},
    "ptt_035_stat_depth_var_0": {"inputs": ["close"], "func": ptt_035_stat_depth_var_0},
    "ptt_036_stat_depth_var_1": {"inputs": ["close"], "func": ptt_036_stat_depth_var_1},
    "ptt_037_stat_depth_var_2": {"inputs": ["close"], "func": ptt_037_stat_depth_var_2},
    "ptt_038_stat_depth_var_3": {"inputs": ["close"], "func": ptt_038_stat_depth_var_3},
    "ptt_039_stat_depth_var_4": {"inputs": ["close"], "func": ptt_039_stat_depth_var_4},
    "ptt_040_stat_depth_var_5": {"inputs": ["close"], "func": ptt_040_stat_depth_var_5},
    "ptt_041_stat_depth_var_6": {"inputs": ["close"], "func": ptt_041_stat_depth_var_6},
    "ptt_042_stat_depth_var_7": {"inputs": ["close"], "func": ptt_042_stat_depth_var_7},
    "ptt_043_stat_depth_var_8": {"inputs": ["close"], "func": ptt_043_stat_depth_var_8},
    "ptt_044_stat_depth_var_9": {"inputs": ["close"], "func": ptt_044_stat_depth_var_9},
    "ptt_045_stat_depth_var_10": {"inputs": ["close"], "func": ptt_045_stat_depth_var_10},
    "ptt_046_stat_depth_var_11": {"inputs": ["close"], "func": ptt_046_stat_depth_var_11},
    "ptt_047_stat_depth_var_12": {"inputs": ["close"], "func": ptt_047_stat_depth_var_12},
    "ptt_048_stat_depth_var_13": {"inputs": ["close"], "func": ptt_048_stat_depth_var_13},
    "ptt_049_stat_depth_var_14": {"inputs": ["close"], "func": ptt_049_stat_depth_var_14},
    "ptt_050_stat_depth_var_15": {"inputs": ["close"], "func": ptt_050_stat_depth_var_15},
    "ptt_051_stat_depth_var_16": {"inputs": ["close"], "func": ptt_051_stat_depth_var_16},
    "ptt_052_stat_depth_var_17": {"inputs": ["close"], "func": ptt_052_stat_depth_var_17},
    "ptt_053_stat_depth_var_18": {"inputs": ["close"], "func": ptt_053_stat_depth_var_18},
    "ptt_054_stat_depth_var_19": {"inputs": ["close"], "func": ptt_054_stat_depth_var_19},
    "ptt_055_stat_depth_var_20": {"inputs": ["close"], "func": ptt_055_stat_depth_var_20},
    "ptt_056_stat_depth_var_21": {"inputs": ["close"], "func": ptt_056_stat_depth_var_21},
    "ptt_057_stat_depth_var_22": {"inputs": ["close"], "func": ptt_057_stat_depth_var_22},
    "ptt_058_stat_depth_var_23": {"inputs": ["close"], "func": ptt_058_stat_depth_var_23},
    "ptt_059_stat_depth_var_24": {"inputs": ["close"], "func": ptt_059_stat_depth_var_24},
    "ptt_060_stat_depth_var_25": {"inputs": ["close"], "func": ptt_060_stat_depth_var_25},
    "ptt_061_stat_depth_var_26": {"inputs": ["close"], "func": ptt_061_stat_depth_var_26},
    "ptt_062_stat_depth_var_27": {"inputs": ["close"], "func": ptt_062_stat_depth_var_27},
    "ptt_063_stat_depth_var_28": {"inputs": ["close"], "func": ptt_063_stat_depth_var_28},
    "ptt_064_stat_depth_var_29": {"inputs": ["close"], "func": ptt_064_stat_depth_var_29},
    "ptt_065_stat_depth_var_30": {"inputs": ["close"], "func": ptt_065_stat_depth_var_30},
    "ptt_066_stat_depth_var_31": {"inputs": ["close"], "func": ptt_066_stat_depth_var_31},
    "ptt_067_stat_depth_var_32": {"inputs": ["close"], "func": ptt_067_stat_depth_var_32},
    "ptt_068_stat_depth_var_33": {"inputs": ["close"], "func": ptt_068_stat_depth_var_33},
    "ptt_069_stat_depth_var_34": {"inputs": ["close"], "func": ptt_069_stat_depth_var_34},
    "ptt_070_stat_depth_var_35": {"inputs": ["close"], "func": ptt_070_stat_depth_var_35},
    "ptt_071_stat_depth_var_36": {"inputs": ["close"], "func": ptt_071_stat_depth_var_36},
    "ptt_072_stat_depth_var_37": {"inputs": ["close"], "func": ptt_072_stat_depth_var_37},
    "ptt_073_stat_depth_var_38": {"inputs": ["close"], "func": ptt_073_stat_depth_var_38},
    "ptt_074_stat_depth_var_39": {"inputs": ["close"], "func": ptt_074_stat_depth_var_39},
    "ptt_075_stat_depth_var_40": {"inputs": ["close"], "func": ptt_075_stat_depth_var_40},
}
