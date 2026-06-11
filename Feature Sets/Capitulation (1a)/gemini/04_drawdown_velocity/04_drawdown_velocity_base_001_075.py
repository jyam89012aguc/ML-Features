"""
Drawdown Velocity — Base Features 001–075
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

def dvel_001_log_velocity_5d(close: pd.Series) -> pd.Series:
    """dvel_001_log_velocity_5d"""
    return np.log(close).diff(5) / 5.0

def dvel_002_log_velocity_21d(close: pd.Series) -> pd.Series:
    """dvel_002_log_velocity_21d"""
    return np.log(close).diff(21) / 21.0

def dvel_003_log_velocity_63d(close: pd.Series) -> pd.Series:
    """dvel_003_log_velocity_63d"""
    return np.log(close).diff(63) / 63.0

def dvel_004_log_velocity_252d(close: pd.Series) -> pd.Series:
    """dvel_004_log_velocity_252d"""
    return np.log(close).diff(252) / 252.0

def dvel_005_max_negative_velocity_21d(close: pd.Series) -> pd.Series:
    """dvel_005_max_negative_velocity_21d"""
    # Most vertical 5-day drop in last month
    v = np.log(close).diff(5) / 5.0
    return v.rolling(21).min()

def dvel_006_max_negative_velocity_252d(close: pd.Series) -> pd.Series:
    """dvel_006_max_negative_velocity_252d"""
    v = np.log(close).diff(21) / 21.0
    return v.rolling(252).min()

def dvel_007_avg_negative_velocity_63d(close: pd.Series) -> pd.Series:
    """dvel_007_avg_negative_velocity_63d"""
    v = np.log(close).diff(1)
    return v[v < 0].rolling(63).mean()

def dvel_008_velocity_zscore_252d(close: pd.Series) -> pd.Series:
    """dvel_008_velocity_zscore_252d"""
    v = np.log(close).diff(21)
    return (v - v.rolling(252).mean()) / v.rolling(252).std()


# 009-025: Drawdown-Specific Velocity (Depth / Time Since High)

def dvel_009_drawdown_velocity_252d(close: pd.Series) -> pd.Series:
    """dvel_009_drawdown_velocity_252d feature"""
    # Current DD Depth / Days Since High
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    dsh = close.rolling(252).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)
    return _safe_div(dd, dsh)

def dvel_010_drawdown_velocity_ath(close: pd.Series) -> pd.Series:
    """dvel_010_drawdown_velocity_ath"""
    h = close.cummax()
    dd = (close - h) / h
    # Days since high calculation proxy
    cummax = close.cummax()
    is_high = (close == cummax)
    high_indices = pd.Series(np.arange(len(close)), index=close.index).where(is_high).ffill()
    dsh = pd.Series(np.arange(len(close)), index=close.index) - high_indices
    return _safe_div(dd, dsh)

def dvel_011_mdd_velocity_252d(close: pd.Series) -> pd.Series:
    """dvel_011_mdd_velocity_252d"""
    # Speed at which the Max Drawdown was reached in the last year
    # MDD / Time to reach MDD
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    mdd_val = dd.rolling(252).min()
    mdd_idx = dd.rolling(252).apply(np.argmin, raw=True)
    time_to_mdd = 252 - 1 - mdd_idx
    return _safe_div(mdd_val, time_to_mdd)

def dvel_012_terminal_velocity_10d(close: pd.Series) -> pd.Series:
    """dvel_012_terminal_velocity_10d"""
    # Slope of log price over last 10 days
    return _rolling_slope(np.log(close), 10)

def dvel_013_terminal_velocity_21d(close: pd.Series) -> pd.Series:
    """dvel_013_terminal_velocity_21d"""
    return _rolling_slope(np.log(close), 21)


# 026-040: Volatility-Adjusted Velocity

def dvel_026_sigma_velocity_21d(close: pd.Series) -> pd.Series:
    """dvel_026_sigma_velocity_21d feature"""
    # 21-day return / 21-day realized volatility
    ret = np.log(close).diff(21)
    vol = close.pct_change().rolling(21).std() * np.sqrt(21)
    return _safe_div(ret, vol)

def dvel_027_sigma_velocity_252d(close: pd.Series) -> pd.Series:
    """dvel_027_sigma_velocity_252d"""
    ret = np.log(close).diff(252)
    vol = close.pct_change().rolling(252).std() * np.sqrt(252)
    return _safe_div(ret, vol)

def dvel_028_atr_normalized_velocity_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dvel_028_atr_normalized_velocity_21d"""
    # (Close - Prev Close) / ATR(21)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21).mean()
    return _safe_div(close - close.shift(21), atr)


# 041-055: Interaction Velocities (Volume and Market Cap)

def dvel_041_volume_weighted_velocity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dvel_041_volume_weighted_velocity_21d feature"""
    v = np.log(close).diff(5)
    v_norm = _safe_div(volume, volume.rolling(21).mean())
    return (v * v_norm).rolling(21).mean()

def dvel_042_mktcap_velocity_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dvel_042_mktcap_velocity_63d"""
    mc = close * sharesbas
    return np.log(mc).diff(63) / 63.0

def dvel_043_ev_revenue_velocity_63d(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """dvel_043_ev_revenue_velocity_63d"""
    ev = (close * sharesbas) + debt - cashnequiv
    ratio = ev / revenue
    return np.log(ratio + _EPS).diff(63) / 63.0


# 056-075: Multi-Horizon Acceleration Proxies (Base)

def dvel_056_velocity_spread_21_to_252(close: pd.Series) -> pd.Series:
    """dvel_056_velocity_spread_21_to_252 feature"""
    v21 = np.log(close).diff(21) / 21.0
    v252 = np.log(close).diff(252) / 252.0
    return v21 - v252

def dvel_057_velocity_ratio_5_to_63(close: pd.Series) -> pd.Series:
    """dvel_057_velocity_ratio_5_to_63"""
    v5 = np.log(close).diff(5) / 5.0
    v63 = np.log(close).diff(63) / 63.0
    return _safe_div(v5, v63)

def dvel_058_velocity_persistence_63d(close: pd.Series) -> pd.Series:
    """dvel_058_velocity_persistence_63d"""
    # Frequency of negative 5-day velocity over last 63 days
    v5 = np.log(close).diff(5)
    return (v5 < 0).rolling(63).mean()

def dvel_059_velocity_autocorr_63d(close: pd.Series) -> pd.Series:
    """dvel_059_velocity_autocorr_63d"""
    v5 = np.log(close).diff(5)
    return v5.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)

def dvel_060_velocity_skewness_63d(close: pd.Series) -> pd.Series:
    """dvel_060_velocity_skewness_63d"""
    v5 = np.log(close).diff(5)
    return v5.rolling(63).skew()

def dvel_061_negative_velocity_intensity_21d(close: pd.Series) -> pd.Series:
    """dvel_061_negative_velocity_intensity_21d"""
    v = np.log(close).diff(1)
    neg_v = v.where(v < 0)
    return neg_v.rolling(21).sum() / 21.0

def dvel_062_positive_velocity_intensity_21d(close: pd.Series) -> pd.Series:
    """dvel_062_positive_velocity_intensity_21d"""
    v = np.log(close).diff(1)
    pos_v = v.where(v > 0)
    return pos_v.rolling(21).sum() / 21.0

def dvel_063_velocity_oscillation_index_63d(close: pd.Series) -> pd.Series:
    """dvel_063_velocity_oscillation_index_63d"""
    # Ratio of std dev of velocity to mean velocity
    v5 = np.log(close).diff(5)
    return _safe_div(v5.rolling(63).std(), v5.rolling(63).mean().abs())

def dvel_064_days_to_halve_velocity_63d(close: pd.Series) -> pd.Series:
    """dvel_064_days_to_halve_velocity_63d"""
    # Theoretical days to halve price at current velocity
    v = np.log(close).diff(21) / 21.0
    return _safe_div(np.log(0.5), v)

def dvel_065_rolling_min_velocity_rank_252d(close: pd.Series) -> pd.Series:
    """dvel_065_rolling_min_velocity_rank_252d"""
    v21 = np.log(close).diff(21)
    return v21.rolling(252).rank(pct=True)

def dvel_066_velocity_entropy_63d(close: pd.Series) -> pd.Series:
    """dvel_066_velocity_entropy_63d"""
    v = close.pct_change()
    def _entropy(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log(hist))
    return v.rolling(63).apply(_entropy, raw=True)

def dvel_067_velocity_drawdown_ratio_63d(close: pd.Series) -> pd.Series:
    """dvel_067_velocity_drawdown_ratio_63d"""
    # Velocity vs Max Depth ratio (is it fast relative to how deep it is?)
    v21 = np.log(close).diff(21).abs()
    h = _rolling_max(close, 63)
    dd = (h - close) / h
    return _safe_div(v21, dd)

def dvel_068_ema_velocity_21d(close: pd.Series) -> pd.Series:
    """dvel_068_ema_velocity_21d"""
    # Velocity of EMA(20)
    ema = close.ewm(span=21).mean()
    return np.log(ema).diff(5) / 5.0

def dvel_069_ema_velocity_50d(close: pd.Series) -> pd.Series:
    """dvel_069_ema_velocity_50d"""
    ema = close.ewm(span=50).mean()
    return np.log(ema).diff(10) / 10.0

def dvel_070_vwap_velocity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dvel_070_vwap_velocity_21d"""
    vwap = (close * volume).rolling(21).sum() / volume.rolling(21).sum()
    return np.log(vwap).diff(5) / 5.0

def dvel_071_rolling_slope_velocity_spread_63d(close: pd.Series) -> pd.Series:
    """dvel_071_rolling_slope_velocity_spread_63d"""
    # Spread between 21-day slope and 63-day slope
    s21 = _rolling_slope(np.log(close), 21)
    s63 = _rolling_slope(np.log(close), 63)
    return s21 - s63

def dvel_072_velocity_to_volatility_spread_63d(close: pd.Series) -> pd.Series:
    """dvel_072_velocity_to_volatility_spread_63d"""
    v = np.log(close).diff(21).abs()
    vol = close.pct_change().rolling(63).std() * np.sqrt(21)
    return v - vol

def dvel_073_harmonic_velocity_63d(close: pd.Series) -> pd.Series:
    """dvel_073_harmonic_velocity_63d"""
    # Harmonic mean of daily returns
    ret = close.pct_change() + 1.0
    def _harm(y):
        return len(y) / np.sum(1.0 / y) - 1.0
    return ret.rolling(63).apply(_harm, raw=True)

def dvel_074_geometric_velocity_63d(close: pd.Series) -> pd.Series:
    """dvel_074_geometric_velocity_63d"""
    ret = close.pct_change() + 1.0
    def _geom(y):
        return np.exp(np.mean(np.log(y))) - 1.0
    return ret.rolling(63).apply(_geom, raw=True)

def dvel_075_velocity_composite_momentum_63d(close: pd.Series) -> pd.Series:
    """dvel_075_velocity_composite_momentum_63d"""
    v5 = np.log(close).diff(5) / 5.0
    v21 = np.log(close).diff(21) / 21.0
    v63 = np.log(close).diff(63) / 63.0
    return (0.5 * v5 + 0.3 * v21 + 0.2 * v63)

def dvel_036_variation_0(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_001_log_velocity_5d"""
    base_feat = dvel_001_log_velocity_5d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_037_variation_1(close: pd.Series) -> pd.Series:
    """rank variation of dvel_002_log_velocity_21d"""
    base_feat = dvel_002_log_velocity_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_038_variation_2(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_003_log_velocity_63d"""
    base_feat = dvel_003_log_velocity_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_039_variation_3(close: pd.Series) -> pd.Series:
    """rank variation of dvel_004_log_velocity_252d"""
    base_feat = dvel_004_log_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_040_variation_4(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_005_max_negative_velocity_21d"""
    base_feat = dvel_005_max_negative_velocity_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_041_variation_5(close: pd.Series) -> pd.Series:
    """rank variation of dvel_006_max_negative_velocity_252d"""
    base_feat = dvel_006_max_negative_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_042_variation_6(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_007_avg_negative_velocity_63d"""
    base_feat = dvel_007_avg_negative_velocity_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_043_variation_7(close: pd.Series) -> pd.Series:
    """rank variation of dvel_008_velocity_zscore_252d"""
    base_feat = dvel_008_velocity_zscore_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_044_variation_8(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_010_drawdown_velocity_ath"""
    base_feat = dvel_010_drawdown_velocity_ath(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_045_variation_9(close: pd.Series) -> pd.Series:
    """rank variation of dvel_011_mdd_velocity_252d"""
    base_feat = dvel_011_mdd_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_046_variation_10(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_001_log_velocity_5d"""
    base_feat = dvel_001_log_velocity_5d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_047_variation_11(close: pd.Series) -> pd.Series:
    """rank variation of dvel_002_log_velocity_21d"""
    base_feat = dvel_002_log_velocity_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_048_variation_12(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_003_log_velocity_63d"""
    base_feat = dvel_003_log_velocity_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_049_variation_13(close: pd.Series) -> pd.Series:
    """rank variation of dvel_004_log_velocity_252d"""
    base_feat = dvel_004_log_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_050_variation_14(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_005_max_negative_velocity_21d"""
    base_feat = dvel_005_max_negative_velocity_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_051_variation_15(close: pd.Series) -> pd.Series:
    """rank variation of dvel_006_max_negative_velocity_252d"""
    base_feat = dvel_006_max_negative_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_052_variation_16(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_007_avg_negative_velocity_63d"""
    base_feat = dvel_007_avg_negative_velocity_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_053_variation_17(close: pd.Series) -> pd.Series:
    """rank variation of dvel_008_velocity_zscore_252d"""
    base_feat = dvel_008_velocity_zscore_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_054_variation_18(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_010_drawdown_velocity_ath"""
    base_feat = dvel_010_drawdown_velocity_ath(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_055_variation_19(close: pd.Series) -> pd.Series:
    """rank variation of dvel_011_mdd_velocity_252d"""
    base_feat = dvel_011_mdd_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_056_variation_20(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_001_log_velocity_5d"""
    base_feat = dvel_001_log_velocity_5d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_057_variation_21(close: pd.Series) -> pd.Series:
    """rank variation of dvel_002_log_velocity_21d"""
    base_feat = dvel_002_log_velocity_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_058_variation_22(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_003_log_velocity_63d"""
    base_feat = dvel_003_log_velocity_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_059_variation_23(close: pd.Series) -> pd.Series:
    """rank variation of dvel_004_log_velocity_252d"""
    base_feat = dvel_004_log_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_060_variation_24(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_005_max_negative_velocity_21d"""
    base_feat = dvel_005_max_negative_velocity_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_061_variation_25(close: pd.Series) -> pd.Series:
    """rank variation of dvel_006_max_negative_velocity_252d"""
    base_feat = dvel_006_max_negative_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_062_variation_26(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_007_avg_negative_velocity_63d"""
    base_feat = dvel_007_avg_negative_velocity_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_063_variation_27(close: pd.Series) -> pd.Series:
    """rank variation of dvel_008_velocity_zscore_252d"""
    base_feat = dvel_008_velocity_zscore_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_064_variation_28(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_010_drawdown_velocity_ath"""
    base_feat = dvel_010_drawdown_velocity_ath(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_065_variation_29(close: pd.Series) -> pd.Series:
    """rank variation of dvel_011_mdd_velocity_252d"""
    base_feat = dvel_011_mdd_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_066_variation_30(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_001_log_velocity_5d"""
    base_feat = dvel_001_log_velocity_5d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_067_variation_31(close: pd.Series) -> pd.Series:
    """rank variation of dvel_002_log_velocity_21d"""
    base_feat = dvel_002_log_velocity_21d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_068_variation_32(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_003_log_velocity_63d"""
    base_feat = dvel_003_log_velocity_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_069_variation_33(close: pd.Series) -> pd.Series:
    """rank variation of dvel_004_log_velocity_252d"""
    base_feat = dvel_004_log_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_070_variation_34(close: pd.Series) -> pd.Series:
    """zscore variation of dvel_005_max_negative_velocity_21d"""
    base_feat = dvel_005_max_negative_velocity_21d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dvel_071_variation_35(close: pd.Series) -> pd.Series:
    """rank variation of dvel_006_max_negative_velocity_252d"""
    base_feat = dvel_006_max_negative_velocity_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V04_REGISTRY = {
    "dvel_001_log_velocity_5d": {"inputs": ["close"], "func": dvel_001_log_velocity_5d},
    "dvel_002_log_velocity_21d": {"inputs": ["close"], "func": dvel_002_log_velocity_21d},
    "dvel_003_log_velocity_63d": {"inputs": ["close"], "func": dvel_003_log_velocity_63d},
    "dvel_004_log_velocity_252d": {"inputs": ["close"], "func": dvel_004_log_velocity_252d},
    "dvel_005_max_negative_velocity_21d": {"inputs": ["close"], "func": dvel_005_max_negative_velocity_21d},
    "dvel_006_max_negative_velocity_252d": {"inputs": ["close"], "func": dvel_006_max_negative_velocity_252d},
    "dvel_007_avg_negative_velocity_63d": {"inputs": ["close"], "func": dvel_007_avg_negative_velocity_63d},
    "dvel_008_velocity_zscore_252d": {"inputs": ["close"], "func": dvel_008_velocity_zscore_252d},
    "dvel_009_drawdown_velocity_252d": {"inputs": ["close"], "func": dvel_009_drawdown_velocity_252d},
    "dvel_010_drawdown_velocity_ath": {"inputs": ["close"], "func": dvel_010_drawdown_velocity_ath},
    "dvel_011_mdd_velocity_252d": {"inputs": ["close"], "func": dvel_011_mdd_velocity_252d},
    "dvel_012_terminal_velocity_10d": {"inputs": ["close"], "func": dvel_012_terminal_velocity_10d},
    "dvel_013_terminal_velocity_21d": {"inputs": ["close"], "func": dvel_013_terminal_velocity_21d},
    "dvel_026_sigma_velocity_21d": {"inputs": ["close"], "func": dvel_026_sigma_velocity_21d},
    "dvel_027_sigma_velocity_252d": {"inputs": ["close"], "func": dvel_027_sigma_velocity_252d},
    "dvel_028_atr_normalized_velocity_21d": {"inputs": ["close", "high", "low"], "func": dvel_028_atr_normalized_velocity_21d},
    "dvel_041_volume_weighted_velocity_21d": {"inputs": ["close", "volume"], "func": dvel_041_volume_weighted_velocity_21d},
    "dvel_042_mktcap_velocity_63d": {"inputs": ["close", "sharesbas"], "func": dvel_042_mktcap_velocity_63d},
    "dvel_043_ev_revenue_velocity_63d": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": dvel_043_ev_revenue_velocity_63d},
    "dvel_056_velocity_spread_21_to_252": {"inputs": ["close"], "func": dvel_056_velocity_spread_21_to_252},
    "dvel_057_velocity_ratio_5_to_63": {"inputs": ["close"], "func": dvel_057_velocity_ratio_5_to_63},
    "dvel_058_velocity_persistence_63d": {"inputs": ["close"], "func": dvel_058_velocity_persistence_63d},
    "dvel_059_velocity_autocorr_63d": {"inputs": ["close"], "func": dvel_059_velocity_autocorr_63d},
    "dvel_060_velocity_skewness_63d": {"inputs": ["close"], "func": dvel_060_velocity_skewness_63d},
    "dvel_061_negative_velocity_intensity_21d": {"inputs": ["close"], "func": dvel_061_negative_velocity_intensity_21d},
    "dvel_062_positive_velocity_intensity_21d": {"inputs": ["close"], "func": dvel_062_positive_velocity_intensity_21d},
    "dvel_063_velocity_oscillation_index_63d": {"inputs": ["close"], "func": dvel_063_velocity_oscillation_index_63d},
    "dvel_064_days_to_halve_velocity_63d": {"inputs": ["close"], "func": dvel_064_days_to_halve_velocity_63d},
    "dvel_065_rolling_min_velocity_rank_252d": {"inputs": ["close"], "func": dvel_065_rolling_min_velocity_rank_252d},
    "dvel_066_velocity_entropy_63d": {"inputs": ["close"], "func": dvel_066_velocity_entropy_63d},
    "dvel_067_velocity_drawdown_ratio_63d": {"inputs": ["close"], "func": dvel_067_velocity_drawdown_ratio_63d},
    "dvel_068_ema_velocity_21d": {"inputs": ["close"], "func": dvel_068_ema_velocity_21d},
    "dvel_069_ema_velocity_50d": {"inputs": ["close"], "func": dvel_069_ema_velocity_50d},
    "dvel_070_vwap_velocity_21d": {"inputs": ["close", "volume"], "func": dvel_070_vwap_velocity_21d},
    "dvel_071_rolling_slope_velocity_spread_63d": {"inputs": ["close"], "func": dvel_071_rolling_slope_velocity_spread_63d},
    "dvel_072_velocity_to_volatility_spread_63d": {"inputs": ["close"], "func": dvel_072_velocity_to_volatility_spread_63d},
    "dvel_073_harmonic_velocity_63d": {"inputs": ["close"], "func": dvel_073_harmonic_velocity_63d},
    "dvel_074_geometric_velocity_63d": {"inputs": ["close"], "func": dvel_074_geometric_velocity_63d},
    "dvel_075_velocity_composite_momentum_63d": {"inputs": ["close"], "func": dvel_075_velocity_composite_momentum_63d},
    "dvel_036_variation_0": {"inputs": ["close"], "func": dvel_036_variation_0},
    "dvel_037_variation_1": {"inputs": ["close"], "func": dvel_037_variation_1},
    "dvel_038_variation_2": {"inputs": ["close"], "func": dvel_038_variation_2},
    "dvel_039_variation_3": {"inputs": ["close"], "func": dvel_039_variation_3},
    "dvel_040_variation_4": {"inputs": ["close"], "func": dvel_040_variation_4},
    "dvel_041_variation_5": {"inputs": ["close"], "func": dvel_041_variation_5},
    "dvel_042_variation_6": {"inputs": ["close"], "func": dvel_042_variation_6},
    "dvel_043_variation_7": {"inputs": ["close"], "func": dvel_043_variation_7},
    "dvel_044_variation_8": {"inputs": ["close"], "func": dvel_044_variation_8},
    "dvel_045_variation_9": {"inputs": ["close"], "func": dvel_045_variation_9},
    "dvel_046_variation_10": {"inputs": ["close"], "func": dvel_046_variation_10},
    "dvel_047_variation_11": {"inputs": ["close"], "func": dvel_047_variation_11},
    "dvel_048_variation_12": {"inputs": ["close"], "func": dvel_048_variation_12},
    "dvel_049_variation_13": {"inputs": ["close"], "func": dvel_049_variation_13},
    "dvel_050_variation_14": {"inputs": ["close"], "func": dvel_050_variation_14},
    "dvel_051_variation_15": {"inputs": ["close"], "func": dvel_051_variation_15},
    "dvel_052_variation_16": {"inputs": ["close"], "func": dvel_052_variation_16},
    "dvel_053_variation_17": {"inputs": ["close"], "func": dvel_053_variation_17},
    "dvel_054_variation_18": {"inputs": ["close"], "func": dvel_054_variation_18},
    "dvel_055_variation_19": {"inputs": ["close"], "func": dvel_055_variation_19},
    "dvel_056_variation_20": {"inputs": ["close"], "func": dvel_056_variation_20},
    "dvel_057_variation_21": {"inputs": ["close"], "func": dvel_057_variation_21},
    "dvel_058_variation_22": {"inputs": ["close"], "func": dvel_058_variation_22},
    "dvel_059_variation_23": {"inputs": ["close"], "func": dvel_059_variation_23},
    "dvel_060_variation_24": {"inputs": ["close"], "func": dvel_060_variation_24},
    "dvel_061_variation_25": {"inputs": ["close"], "func": dvel_061_variation_25},
    "dvel_062_variation_26": {"inputs": ["close"], "func": dvel_062_variation_26},
    "dvel_063_variation_27": {"inputs": ["close"], "func": dvel_063_variation_27},
    "dvel_064_variation_28": {"inputs": ["close"], "func": dvel_064_variation_28},
    "dvel_065_variation_29": {"inputs": ["close"], "func": dvel_065_variation_29},
    "dvel_066_variation_30": {"inputs": ["close"], "func": dvel_066_variation_30},
    "dvel_067_variation_31": {"inputs": ["close"], "func": dvel_067_variation_31},
    "dvel_068_variation_32": {"inputs": ["close"], "func": dvel_068_variation_32},
    "dvel_069_variation_33": {"inputs": ["close"], "func": dvel_069_variation_33},
    "dvel_070_variation_34": {"inputs": ["close"], "func": dvel_070_variation_34},
    "dvel_071_variation_35": {"inputs": ["close"], "func": dvel_071_variation_35},
}
