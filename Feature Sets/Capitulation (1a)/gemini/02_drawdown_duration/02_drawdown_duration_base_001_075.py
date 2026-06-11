"""
Drawdown Duration — Base Features 001–075
Domain: time spent in drawdown, days since high
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

def ddur_001_days_since_21d_high(close: pd.Series) -> pd.Series:
    """ddur_001_days_since_21d_high"""
    return _days_since_high(close, _TD_MON)

def ddur_002_days_since_63d_high(close: pd.Series) -> pd.Series:
    """ddur_002_days_since_63d_high"""
    return _days_since_high(close, _TD_QTR)

def ddur_003_days_since_126d_high(close: pd.Series) -> pd.Series:
    """ddur_003_days_since_126d_high"""
    return _days_since_high(close, 126)

def ddur_004_days_since_252d_high(close: pd.Series) -> pd.Series:
    """ddur_004_days_since_252d_high"""
    return _days_since_high(close, _TD_YEAR)

def ddur_005_days_since_504d_high(close: pd.Series) -> pd.Series:
    """ddur_005_days_since_504d_high"""
    return _days_since_high(close, 504)

def ddur_006_days_since_756d_high(close: pd.Series) -> pd.Series:
    """ddur_006_days_since_756d_high"""
    return _days_since_high(close, 756)

def ddur_007_days_since_1260d_high(close: pd.Series) -> pd.Series:
    """ddur_007_days_since_1260d_high"""
    return _days_since_high(close, 1260)

def ddur_008_days_since_ath(close: pd.Series) -> pd.Series:
    """ddur_008_days_since_ath"""
    return _days_since_expanding_high(close)

def ddur_009_days_since_high_normalized_252d(close: pd.Series) -> pd.Series:
    """ddur_009_days_since_high_normalized_252d"""
    # Days since high as fraction of lookback
    return _days_since_high(close, 252) / 252.0

def ddur_010_days_since_high_normalized_1260d(close: pd.Series) -> pd.Series:
    """ddur_010_days_since_high_normalized_1260d"""
    return _days_since_high(close, 1260) / 1260.0

def ddur_011_days_since_sma_200_high_252d(close: pd.Series) -> pd.Series:
    """ddur_011_days_since_sma_200_high_252d"""
    ma = _rolling_mean(close, 200)
    return _days_since_high(ma, 252)

def ddur_012_days_since_mktcap_ath(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_012_days_since_mktcap_ath"""
    mc = close * sharesbas
    return _days_since_expanding_high(mc)

def ddur_013_days_since_vwap_high_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ddur_013_days_since_vwap_high_252d"""
    vwap = (close * volume).rolling(252).sum() / volume.rolling(252).sum()
    return _days_since_high(vwap, 252)

def ddur_014_days_since_revenue_ps_ath(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_014_days_since_revenue_ps_ath"""
    revps = revenue / sharesbas
    return _days_since_expanding_high(revps)

def ddur_015_days_since_equity_ps_ath(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_015_days_since_equity_ps_ath"""
    bvps = equity / sharesbas
    return _days_since_expanding_high(bvps)


# 016-030: Consecutive days in drawdown (sub-horizons)

def ddur_016_consecutive_days_under_ath(close: pd.Series) -> pd.Series:
    """ddur_016_consecutive_days_under_ath feature"""
    h = close.cummax()
    under = (close < h).astype(int)
    return under.groupby((under == 0).cumsum()).cumsum()

def ddur_017_consecutive_days_under_252d_high(close: pd.Series) -> pd.Series:
    """ddur_017_consecutive_days_under_252d_high"""
    h = _rolling_max(close, 252)
    under = (close < h).astype(int)
    return under.groupby((under == 0).cumsum()).cumsum()

def ddur_018_consecutive_days_under_sma_200(close: pd.Series) -> pd.Series:
    """ddur_018_consecutive_days_under_sma_200"""
    ma = _rolling_mean(close, 200)
    under = (close < ma).astype(int)
    return under.groupby((under == 0).cumsum()).cumsum()

def ddur_019_consecutive_days_under_expanding_median(close: pd.Series) -> pd.Series:
    """ddur_019_consecutive_days_under_expanding_median"""
    m = close.expanding().median()
    under = (close < m).astype(int)
    return under.groupby((under == 0).cumsum()).cumsum()

def ddur_020_consecutive_days_at_504d_low(close: pd.Series) -> pd.Series:
    """ddur_020_consecutive_days_at_504d_low"""
    l = _rolling_min(close, 504)
    at_low = (close <= l * 1.01).astype(int)  # within 1% of low
    return at_low.groupby((at_low == 0).cumsum()).cumsum()


# 021-040: Ratios and statistical duration properties

def ddur_021_days_since_high_to_mdd_duration_ratio_252d(close: pd.Series) -> pd.Series:
    """ddur_021_days_since_high_to_mdd_duration_ratio_252d feature"""
    # Days since high vs time to reach the current max drawdown depth in window
    dsh = _days_since_high(close, 252)
    dd = (close - _rolling_max(close, 252)) / _rolling_max(close, 252)
    mdd_idx = dd.rolling(252).apply(np.argmin, raw=True)
    time_to_mdd = 252 - 1 - mdd_idx
    return _safe_div(dsh, time_to_mdd)

def ddur_022_days_since_high_zscore_1260d(close: pd.Series) -> pd.Series:
    """ddur_022_days_since_high_zscore_1260d"""
    dsh = _days_since_high(close, 252)
    return (dsh - _rolling_mean(dsh, 1260)) / _rolling_std(dsh, 1260)

def ddur_023_days_since_high_pct_rank_ath(close: pd.Series) -> pd.Series:
    """ddur_023_days_since_high_pct_rank_ath"""
    dsh = _days_since_expanding_high(close)
    return dsh.expanding().rank(pct=True)

def ddur_024_avg_days_since_high_63d(close: pd.Series) -> pd.Series:
    """ddur_024_avg_days_since_high_63d"""
    return _rolling_mean(_days_since_high(close, 63), 63)

def ddur_025_max_days_since_high_252d(close: pd.Series) -> pd.Series:
    """ddur_025_max_days_since_high_252d"""
    return _rolling_max(_days_since_high(close, 252), 252)

def ddur_026_drawdown_age_index_252d(close: pd.Series) -> pd.Series:
    """ddur_026_drawdown_age_index_252d"""
    # Multi-window average of days since high
    d21 = _days_since_high(close, 21)
    d63 = _days_since_high(close, 63)
    d252 = _days_since_high(close, 252)
    return (d21 + d63 + d252) / 3.0

def ddur_027_drawdown_duration_persistence_index_252d(close: pd.Series) -> pd.Series:
    """ddur_027_drawdown_duration_persistence_index_252d"""
    # Frequency of being > 21 days since a 21-day high over last year
    dsh = _days_since_high(close, 21)
    return (dsh > 20).rolling(252).mean()

def ddur_028_days_since_high_vol_adjusted_252d(close: pd.Series) -> pd.Series:
    """ddur_028_days_since_high_vol_adjusted_252d"""
    dsh = _days_since_high(close, 252)
    vol = close.pct_change().rolling(21).std() * np.sqrt(252)
    return dsh * vol

def ddur_029_days_since_expanding_high_normalized_by_vol(close: pd.Series) -> pd.Series:
    """ddur_029_days_since_expanding_high_normalized_by_vol"""
    dsh = _days_since_expanding_high(close)
    vol = close.pct_change().expanding().std() * np.sqrt(252)
    return dsh * vol

def ddur_030_days_since_ath_to_days_since_252d_high_ratio(close: pd.Series) -> pd.Series:
    """ddur_030_days_since_ath_to_days_since_252d_high_ratio"""
    return _safe_div(_days_since_expanding_high(close), _days_since_high(close, 252))


# 041-060: Time spent in specific depth buckets

def ddur_041_days_under_minus_10_pct_from_252d_high(close: pd.Series) -> pd.Series:
    """ddur_041_days_under_minus_10_pct_from_252d_high feature"""
    h = _rolling_max(close, 252)
    under = (close < h * 0.9).rolling(252).sum()
    return under

def ddur_042_days_under_minus_20_pct_from_252d_high(close: pd.Series) -> pd.Series:
    """ddur_042_days_under_minus_20_pct_from_252d_high"""
    h = _rolling_max(close, 252)
    under = (close < h * 0.8).rolling(252).sum()
    return under

def ddur_043_days_under_minus_30_pct_from_504d_high(close: pd.Series) -> pd.Series:
    """ddur_043_days_under_minus_30_pct_from_504d_high"""
    h = _rolling_max(close, 504)
    under = (close < h * 0.7).rolling(504).sum()
    return under

def ddur_044_days_under_minus_50_pct_from_ath(close: pd.Series) -> pd.Series:
    """ddur_044_days_under_minus_50_pct_from_ath"""
    h = close.cummax()
    under = (close < h * 0.5).expanding().sum()
    return under

def ddur_045_pct_time_under_252d_high_last_252d(close: pd.Series) -> pd.Series:
    """ddur_045_pct_time_under_252d_high_last_252d"""
    h = _rolling_max(close, 252)
    return (close < h).rolling(252).mean()

def ddur_046_pct_time_making_new_lows_252d(close: pd.Series) -> pd.Series:
    """ddur_046_pct_time_making_new_lows_252d"""
    l = _rolling_min(close, 252)
    return (close == l).rolling(252).mean()

def ddur_047_days_since_last_new_low_252d(close: pd.Series) -> pd.Series:
    """ddur_047_days_since_last_new_low_252d"""
    l = _rolling_min(close, 252)
    is_low = (close == l)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_low).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices

def ddur_048_days_since_last_new_low_ath(close: pd.Series) -> pd.Series:
    """ddur_048_days_since_last_new_low_ath"""
    l = close.cummin()
    is_low = (close == l)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_low).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices

def ddur_049_avg_days_between_new_lows_252d(close: pd.Series) -> pd.Series:
    """ddur_049_avg_days_between_new_lows_252d"""
    l = _rolling_min(close, 252)
    is_low = (close == l).astype(int)
    return _safe_div(is_low.rolling(252).sum(), 252.0) # Frequency proxy

def ddur_050_duration_of_current_low_cluster_63d(close: pd.Series) -> pd.Series:
    """ddur_050_duration_of_current_low_cluster_63d"""
    # Days spent within 5% of the 63d low
    l = _rolling_min(close, 63)
    in_cluster = (close <= l * 1.05).astype(int)
    return in_cluster.groupby((in_cluster == 0).cumsum()).cumsum()


# 061-075: Multi-asset / Sector context proxies (if peer data was available, using internal anchors instead)

def ddur_061_days_since_ma_cross_death_ath(close: pd.Series) -> pd.Series:
    """ddur_061_days_since_ma_cross_death_ath feature"""
    ma50 = _rolling_mean(close, 50)
    ma200 = _rolling_mean(close, 200)
    death_cross = (ma50 < ma200) & (ma50.shift(1) >= ma200.shift(1))
    indices = pd.Series(np.arange(len(close)), index=close.index).where(death_cross).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices

def ddur_062_days_since_last_revenue_growth_positive(revenue: pd.Series) -> pd.Series:
    """ddur_062_days_since_last_revenue_growth_positive"""
    g = revenue.pct_change(4) # quarterly growth
    pos = (g > 0)
    indices = pd.Series(np.arange(len(revenue)), index=revenue.index).where(pos).ffill()
    return pd.Series(np.arange(len(revenue)), index=revenue.index) - indices

def ddur_063_days_since_last_fcf_growth_positive(fcf: pd.Series) -> pd.Series:
    """ddur_063_days_since_last_fcf_growth_positive"""
    g = fcf.pct_change(4)
    pos = (g > 0)
    indices = pd.Series(np.arange(len(fcf)), index=fcf.index).where(pos).ffill()
    return pd.Series(np.arange(len(fcf)), index=fcf.index) - indices

def ddur_064_days_under_book_value_ath(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_064_days_under_book_value_ath"""
    bvps = equity / sharesbas
    under = (close < bvps).astype(int)
    return under.groupby((under == 0).cumsum()).cumsum()

def ddur_065_days_under_net_cash_ath(close: pd.Series, sharesbas: pd.Series, cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """ddur_065_days_under_net_cash_ath"""
    net_cash_ps = (cashnequiv - debt) / sharesbas
    under = (close < net_cash_ps).astype(int)
    return under.groupby((under == 0).cumsum()).cumsum()

def ddur_066_days_since_insider_buy_cluster_ath(insider_buys: pd.Series) -> pd.Series:
    """ddur_066_days_since_insider_buy_cluster_ath"""
    # Assuming insider_buys is a series of buy counts
    indices = pd.Series(np.arange(len(insider_buys)), index=insider_buys.index).where(insider_buys > 0).ffill()
    return pd.Series(np.arange(len(insider_buys)), index=insider_buys.index) - indices

def ddur_067_days_since_last_dividend_ath(dividend: pd.Series) -> pd.Series:
    """ddur_067_days_since_last_dividend_ath"""
    indices = pd.Series(np.arange(len(dividend)), index=dividend.index).where(dividend > 0).ffill()
    return pd.Series(np.arange(len(dividend)), index=dividend.index) - indices

def ddur_068_days_since_ath_to_days_since_last_low_ratio(close: pd.Series) -> pd.Series:
    """ddur_068_days_since_ath_to_days_since_last_low_ratio"""
    dsh = _days_since_expanding_high(close)
    dsl = ddur_048_days_since_last_new_low_ath(close)
    return _safe_div(dsh, dsl)

def ddur_069_days_since_high_normalized_by_rolling_median_252d(close: pd.Series) -> pd.Series:
    """ddur_069_days_since_high_normalized_by_rolling_median_252d"""
    dsh = _days_since_high(close, 252)
    return _safe_div(dsh, _rolling_median(dsh, 1260))

def ddur_070_days_since_expanding_high_minus_days_since_252d_high(close: pd.Series) -> pd.Series:
    """ddur_070_days_since_expanding_high_minus_days_since_252d_high"""
    return _days_since_expanding_high(close) - _days_since_high(close, 252)

def ddur_071_days_since_ath_acceleration_21d(close: pd.Series) -> pd.Series:
    """ddur_071_days_since_ath_acceleration_21d"""
    dsh = _days_since_expanding_high(close)
    return dsh.diff(21)

def ddur_072_days_since_expanding_low_ath(close: pd.Series) -> pd.Series:
    """ddur_072_days_since_expanding_low_ath"""
    l = close.cummin()
    indices = pd.Series(np.arange(len(close)), index=close.index).where(close == l).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices

def ddur_073_days_spent_in_capitulation_zone_252d(close: pd.Series) -> pd.Series:
    """ddur_073_days_spent_in_capitulation_zone_252d"""
    # Days within 10% of 252d low
    l = _rolling_min(close, 252)
    return (close <= l * 1.1).rolling(252).sum()

def ddur_074_days_spent_in_capitulation_zone_ath(close: pd.Series) -> pd.Series:
    """ddur_074_days_spent_in_capitulation_zone_ath"""
    l = close.cummin()
    return (close <= l * 1.1).expanding().sum()

def ddur_075_days_since_major_drawdown_onset_252d(close: pd.Series) -> pd.Series:
    """ddur_075_days_since_major_drawdown_onset_252d"""
    # Days since the high that led to the current drawdown
    return _days_since_high(close, 252)

def ddur_052_variation_0(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_001_days_since_21d_high"""
    base_feat = ddur_001_days_since_21d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_053_variation_1(close: pd.Series) -> pd.Series:
    """rank variation of ddur_002_days_since_63d_high"""
    base_feat = ddur_002_days_since_63d_high(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_054_variation_2(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_003_days_since_126d_high"""
    base_feat = ddur_003_days_since_126d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_055_variation_3(close: pd.Series) -> pd.Series:
    """rank variation of ddur_004_days_since_252d_high"""
    base_feat = ddur_004_days_since_252d_high(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_056_variation_4(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_005_days_since_504d_high"""
    base_feat = ddur_005_days_since_504d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_057_variation_5(close: pd.Series) -> pd.Series:
    """rank variation of ddur_006_days_since_756d_high"""
    base_feat = ddur_006_days_since_756d_high(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_058_variation_6(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_007_days_since_1260d_high"""
    base_feat = ddur_007_days_since_1260d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_059_variation_7(close: pd.Series) -> pd.Series:
    """rank variation of ddur_008_days_since_ath"""
    base_feat = ddur_008_days_since_ath(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_060_variation_8(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_009_days_since_high_normalized_252d"""
    base_feat = ddur_009_days_since_high_normalized_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_061_variation_9(close: pd.Series) -> pd.Series:
    """rank variation of ddur_010_days_since_high_normalized_1260d"""
    base_feat = ddur_010_days_since_high_normalized_1260d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_062_variation_10(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_001_days_since_21d_high"""
    base_feat = ddur_001_days_since_21d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_063_variation_11(close: pd.Series) -> pd.Series:
    """rank variation of ddur_002_days_since_63d_high"""
    base_feat = ddur_002_days_since_63d_high(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_064_variation_12(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_003_days_since_126d_high"""
    base_feat = ddur_003_days_since_126d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_065_variation_13(close: pd.Series) -> pd.Series:
    """rank variation of ddur_004_days_since_252d_high"""
    base_feat = ddur_004_days_since_252d_high(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_066_variation_14(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_005_days_since_504d_high"""
    base_feat = ddur_005_days_since_504d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_067_variation_15(close: pd.Series) -> pd.Series:
    """rank variation of ddur_006_days_since_756d_high"""
    base_feat = ddur_006_days_since_756d_high(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_068_variation_16(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_007_days_since_1260d_high"""
    base_feat = ddur_007_days_since_1260d_high(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_069_variation_17(close: pd.Series) -> pd.Series:
    """rank variation of ddur_008_days_since_ath"""
    base_feat = ddur_008_days_since_ath(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_070_variation_18(close: pd.Series) -> pd.Series:
    """zscore variation of ddur_009_days_since_high_normalized_252d"""
    base_feat = ddur_009_days_since_high_normalized_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_071_variation_19(close: pd.Series) -> pd.Series:
    """rank variation of ddur_010_days_since_high_normalized_1260d"""
    base_feat = ddur_010_days_since_high_normalized_1260d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V02_REGISTRY = {
    "ddur_001_days_since_21d_high": {"inputs": ["close"], "func": ddur_001_days_since_21d_high},
    "ddur_002_days_since_63d_high": {"inputs": ["close"], "func": ddur_002_days_since_63d_high},
    "ddur_003_days_since_126d_high": {"inputs": ["close"], "func": ddur_003_days_since_126d_high},
    "ddur_004_days_since_252d_high": {"inputs": ["close"], "func": ddur_004_days_since_252d_high},
    "ddur_005_days_since_504d_high": {"inputs": ["close"], "func": ddur_005_days_since_504d_high},
    "ddur_006_days_since_756d_high": {"inputs": ["close"], "func": ddur_006_days_since_756d_high},
    "ddur_007_days_since_1260d_high": {"inputs": ["close"], "func": ddur_007_days_since_1260d_high},
    "ddur_008_days_since_ath": {"inputs": ["close"], "func": ddur_008_days_since_ath},
    "ddur_009_days_since_high_normalized_252d": {"inputs": ["close"], "func": ddur_009_days_since_high_normalized_252d},
    "ddur_010_days_since_high_normalized_1260d": {"inputs": ["close"], "func": ddur_010_days_since_high_normalized_1260d},
    "ddur_011_days_since_sma_200_high_252d": {"inputs": ["close"], "func": ddur_011_days_since_sma_200_high_252d},
    "ddur_012_days_since_mktcap_ath": {"inputs": ["close", "sharesbas"], "func": ddur_012_days_since_mktcap_ath},
    "ddur_013_days_since_vwap_high_252d": {"inputs": ["close", "volume"], "func": ddur_013_days_since_vwap_high_252d},
    "ddur_014_days_since_revenue_ps_ath": {"inputs": ["revenue", "sharesbas"], "func": ddur_014_days_since_revenue_ps_ath},
    "ddur_015_days_since_equity_ps_ath": {"inputs": ["equity", "sharesbas"], "func": ddur_015_days_since_equity_ps_ath},
    "ddur_016_consecutive_days_under_ath": {"inputs": ["close"], "func": ddur_016_consecutive_days_under_ath},
    "ddur_017_consecutive_days_under_252d_high": {"inputs": ["close"], "func": ddur_017_consecutive_days_under_252d_high},
    "ddur_018_consecutive_days_under_sma_200": {"inputs": ["close"], "func": ddur_018_consecutive_days_under_sma_200},
    "ddur_019_consecutive_days_under_expanding_median": {"inputs": ["close"], "func": ddur_019_consecutive_days_under_expanding_median},
    "ddur_020_consecutive_days_at_504d_low": {"inputs": ["close"], "func": ddur_020_consecutive_days_at_504d_low},
    "ddur_021_days_since_high_to_mdd_duration_ratio_252d": {"inputs": ["close"], "func": ddur_021_days_since_high_to_mdd_duration_ratio_252d},
    "ddur_022_days_since_high_zscore_1260d": {"inputs": ["close"], "func": ddur_022_days_since_high_zscore_1260d},
    "ddur_023_days_since_high_pct_rank_ath": {"inputs": ["close"], "func": ddur_023_days_since_high_pct_rank_ath},
    "ddur_024_avg_days_since_high_63d": {"inputs": ["close"], "func": ddur_024_avg_days_since_high_63d},
    "ddur_025_max_days_since_high_252d": {"inputs": ["close"], "func": ddur_025_max_days_since_high_252d},
    "ddur_026_drawdown_age_index_252d": {"inputs": ["close"], "func": ddur_026_drawdown_age_index_252d},
    "ddur_027_drawdown_duration_persistence_index_252d": {"inputs": ["close"], "func": ddur_027_drawdown_duration_persistence_index_252d},
    "ddur_028_days_since_high_vol_adjusted_252d": {"inputs": ["close"], "func": ddur_028_days_since_high_vol_adjusted_252d},
    "ddur_029_days_since_expanding_high_normalized_by_vol": {"inputs": ["close"], "func": ddur_029_days_since_expanding_high_normalized_by_vol},
    "ddur_030_days_since_ath_to_days_since_252d_high_ratio": {"inputs": ["close"], "func": ddur_030_days_since_ath_to_days_since_252d_high_ratio},
    "ddur_041_days_under_minus_10_pct_from_252d_high": {"inputs": ["close"], "func": ddur_041_days_under_minus_10_pct_from_252d_high},
    "ddur_042_days_under_minus_20_pct_from_252d_high": {"inputs": ["close"], "func": ddur_042_days_under_minus_20_pct_from_252d_high},
    "ddur_043_days_under_minus_30_pct_from_504d_high": {"inputs": ["close"], "func": ddur_043_days_under_minus_30_pct_from_504d_high},
    "ddur_044_days_under_minus_50_pct_from_ath": {"inputs": ["close"], "func": ddur_044_days_under_minus_50_pct_from_ath},
    "ddur_045_pct_time_under_252d_high_last_252d": {"inputs": ["close"], "func": ddur_045_pct_time_under_252d_high_last_252d},
    "ddur_046_pct_time_making_new_lows_252d": {"inputs": ["close"], "func": ddur_046_pct_time_making_new_lows_252d},
    "ddur_047_days_since_last_new_low_252d": {"inputs": ["close"], "func": ddur_047_days_since_last_new_low_252d},
    "ddur_048_days_since_last_new_low_ath": {"inputs": ["close"], "func": ddur_048_days_since_last_new_low_ath},
    "ddur_049_avg_days_between_new_lows_252d": {"inputs": ["close"], "func": ddur_049_avg_days_between_new_lows_252d},
    "ddur_050_duration_of_current_low_cluster_63d": {"inputs": ["close"], "func": ddur_050_duration_of_current_low_cluster_63d},
    "ddur_061_days_since_ma_cross_death_ath": {"inputs": ["close"], "func": ddur_061_days_since_ma_cross_death_ath},
    "ddur_062_days_since_last_revenue_growth_positive": {"inputs": ["revenue"], "func": ddur_062_days_since_last_revenue_growth_positive},
    "ddur_063_days_since_last_fcf_growth_positive": {"inputs": ["fcf"], "func": ddur_063_days_since_last_fcf_growth_positive},
    "ddur_064_days_under_book_value_ath": {"inputs": ["close", "equity", "sharesbas"], "func": ddur_064_days_under_book_value_ath},
    "ddur_065_days_under_net_cash_ath": {"inputs": ["close", "sharesbas", "cashnequiv", "debt"], "func": ddur_065_days_under_net_cash_ath},
    "ddur_066_days_since_insider_buy_cluster_ath": {"inputs": ["insider_buys"], "func": ddur_066_days_since_insider_buy_cluster_ath},
    "ddur_067_days_since_last_dividend_ath": {"inputs": ["dividend"], "func": ddur_067_days_since_last_dividend_ath},
    "ddur_068_days_since_ath_to_days_since_last_low_ratio": {"inputs": ["close"], "func": ddur_068_days_since_ath_to_days_since_last_low_ratio},
    "ddur_069_days_since_high_normalized_by_rolling_median_252d": {"inputs": ["close"], "func": ddur_069_days_since_high_normalized_by_rolling_median_252d},
    "ddur_070_days_since_expanding_high_minus_days_since_252d_high": {"inputs": ["close"], "func": ddur_070_days_since_expanding_high_minus_days_since_252d_high},
    "ddur_071_days_since_ath_acceleration_21d": {"inputs": ["close"], "func": ddur_071_days_since_ath_acceleration_21d},
    "ddur_072_days_since_expanding_low_ath": {"inputs": ["close"], "func": ddur_072_days_since_expanding_low_ath},
    "ddur_073_days_spent_in_capitulation_zone_252d": {"inputs": ["close"], "func": ddur_073_days_spent_in_capitulation_zone_252d},
    "ddur_074_days_spent_in_capitulation_zone_ath": {"inputs": ["close"], "func": ddur_074_days_spent_in_capitulation_zone_ath},
    "ddur_075_days_since_major_drawdown_onset_252d": {"inputs": ["close"], "func": ddur_075_days_since_major_drawdown_onset_252d},
    "ddur_052_variation_0": {"inputs": ["close"], "func": ddur_052_variation_0},
    "ddur_053_variation_1": {"inputs": ["close"], "func": ddur_053_variation_1},
    "ddur_054_variation_2": {"inputs": ["close"], "func": ddur_054_variation_2},
    "ddur_055_variation_3": {"inputs": ["close"], "func": ddur_055_variation_3},
    "ddur_056_variation_4": {"inputs": ["close"], "func": ddur_056_variation_4},
    "ddur_057_variation_5": {"inputs": ["close"], "func": ddur_057_variation_5},
    "ddur_058_variation_6": {"inputs": ["close"], "func": ddur_058_variation_6},
    "ddur_059_variation_7": {"inputs": ["close"], "func": ddur_059_variation_7},
    "ddur_060_variation_8": {"inputs": ["close"], "func": ddur_060_variation_8},
    "ddur_061_variation_9": {"inputs": ["close"], "func": ddur_061_variation_9},
    "ddur_062_variation_10": {"inputs": ["close"], "func": ddur_062_variation_10},
    "ddur_063_variation_11": {"inputs": ["close"], "func": ddur_063_variation_11},
    "ddur_064_variation_12": {"inputs": ["close"], "func": ddur_064_variation_12},
    "ddur_065_variation_13": {"inputs": ["close"], "func": ddur_065_variation_13},
    "ddur_066_variation_14": {"inputs": ["close"], "func": ddur_066_variation_14},
    "ddur_067_variation_15": {"inputs": ["close"], "func": ddur_067_variation_15},
    "ddur_068_variation_16": {"inputs": ["close"], "func": ddur_068_variation_16},
    "ddur_069_variation_17": {"inputs": ["close"], "func": ddur_069_variation_17},
    "ddur_070_variation_18": {"inputs": ["close"], "func": ddur_070_variation_18},
    "ddur_071_variation_19": {"inputs": ["close"], "func": ddur_071_variation_19},
}
