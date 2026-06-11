"""
Drawdown Depth — Base Features 001–075
Domain: magnitude of decline vs trailing highs
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

def dd_001_drawdown_21d(close: pd.Series) -> pd.Series:
    """dd_001_drawdown_21d"""
    h = _rolling_max(close, _TD_MON)
    return _safe_div(close - h, h)

def dd_002_drawdown_63d(close: pd.Series) -> pd.Series:
    """dd_002_drawdown_63d"""
    h = _rolling_max(close, _TD_QTR)
    return _safe_div(close - h, h)

def dd_003_drawdown_126d(close: pd.Series) -> pd.Series:
    """dd_003_drawdown_126d"""
    h = _rolling_max(close, 126)
    return _safe_div(close - h, h)

def dd_004_drawdown_252d(close: pd.Series) -> pd.Series:
    """dd_004_drawdown_252d"""
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - h, h)

def dd_005_drawdown_504d(close: pd.Series) -> pd.Series:
    """dd_005_drawdown_504d"""
    h = _rolling_max(close, 504)
    return _safe_div(close - h, h)

def dd_006_drawdown_756d(close: pd.Series) -> pd.Series:
    """dd_006_drawdown_756d"""
    h = _rolling_max(close, 756)
    return _safe_div(close - h, h)

def dd_007_drawdown_1260d(close: pd.Series) -> pd.Series:
    """dd_007_drawdown_1260d"""
    h = _rolling_max(close, 1260)
    return _safe_div(close - h, h)

def dd_008_drawdown_ath(close: pd.Series) -> pd.Series:
    """dd_008_drawdown_ath"""
    h = close.expanding().max()
    return _safe_div(close - h, h)

def dd_009_drawdown_log_252d(close: pd.Series) -> pd.Series:
    """dd_009_drawdown_log_252d"""
    h = _rolling_max(close, _TD_YEAR)
    return np.log(close) - np.log(h)

def dd_010_drawdown_log_ath(close: pd.Series) -> pd.Series:
    """dd_010_drawdown_log_ath"""
    h = close.expanding().max()
    return np.log(close) - np.log(h)


# 011-020: Drawdown relative to trailing standard deviation (risk-adjusted)

def dd_011_drawdown_sigma_63d(close: pd.Series) -> pd.Series:
    """dd_011_drawdown_sigma_63d feature"""
    dd = dd_002_drawdown_63d(close)
    std = _rolling_std(close, _TD_QTR) / _rolling_mean(close, _TD_QTR)
    return _safe_div(dd, std)

def dd_012_drawdown_sigma_252d(close: pd.Series) -> pd.Series:
    """dd_012_drawdown_sigma_252d"""
    dd = dd_004_drawdown_252d(close)
    std = _rolling_std(close, _TD_YEAR) / _rolling_mean(close, _TD_YEAR)
    return _safe_div(dd, std)

def dd_013_drawdown_sigma_504d(close: pd.Series) -> pd.Series:
    """dd_013_drawdown_sigma_504d"""
    dd = dd_005_drawdown_504d(close)
    std = _rolling_std(close, 504) / _rolling_mean(close, 504)
    return _safe_div(dd, std)

def dd_014_drawdown_sigma_ath(close: pd.Series) -> pd.Series:
    """dd_014_drawdown_sigma_ath"""
    dd = dd_008_drawdown_ath(close)
    std = close.expanding().std() / close.expanding().mean()
    return _safe_div(dd, std)

def dd_015_drawdown_vol_normalized_21d(close: pd.Series) -> pd.Series:
    """dd_015_drawdown_vol_normalized_21d"""
    dd = dd_001_drawdown_21d(close)
    vol = _rolling_std(_pct_change(close, 1), 21)
    return _safe_div(dd, vol)

def dd_016_drawdown_vol_normalized_63d(close: pd.Series) -> pd.Series:
    """dd_016_drawdown_vol_normalized_63d"""
    dd = dd_002_drawdown_63d(close)
    vol = _rolling_std(_pct_change(close, 1), 63)
    return _safe_div(dd, vol)

def dd_017_drawdown_vol_normalized_252d(close: pd.Series) -> pd.Series:
    """dd_017_drawdown_vol_normalized_252d"""
    dd = dd_004_drawdown_252d(close)
    vol = _rolling_std(_pct_change(close, 1), 252)
    return _safe_div(dd, vol)

def dd_018_drawdown_vol_normalized_ath(close: pd.Series) -> pd.Series:
    """dd_018_drawdown_vol_normalized_ath"""
    dd = dd_008_drawdown_ath(close)
    vol = _pct_change(close, 1).expanding().std()
    return _safe_div(dd, vol)

def dd_019_drawdown_zscore_252d(close: pd.Series) -> pd.Series:
    """dd_019_drawdown_zscore_252d"""
    return _zscore_rolling(dd_004_drawdown_252d(close), _TD_YEAR)

def dd_020_drawdown_zscore_1260d(close: pd.Series) -> pd.Series:
    """dd_020_drawdown_zscore_1260d"""
    return _zscore_rolling(dd_007_drawdown_1260d(close), 1260)


# 021-030: Expanding vs rolling drawdown ratios

def dd_021_drawdown_ratio_252d_ath(close: pd.Series) -> pd.Series:
    """dd_021_drawdown_ratio_252d_ath feature"""
    return _safe_div(dd_004_drawdown_252d(close), dd_008_drawdown_ath(close))

def dd_022_drawdown_ratio_63d_252d(close: pd.Series) -> pd.Series:
    """dd_022_drawdown_ratio_63d_252d"""
    return _safe_div(dd_002_drawdown_63d(close), dd_004_drawdown_252d(close))

def dd_023_drawdown_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """dd_023_drawdown_ratio_21d_63d"""
    return _safe_div(dd_001_drawdown_21d(close), dd_002_drawdown_63d(close))

def dd_024_drawdown_intensity_252d(close: pd.Series) -> pd.Series:
    """dd_024_drawdown_intensity_252d"""
    # Ratio of current drawdown to maximum drawdown in last year
    dd = dd_004_drawdown_252d(close)
    mdd = _rolling_min(dd, _TD_YEAR)
    return _safe_div(dd, mdd)

def dd_025_drawdown_intensity_ath(close: pd.Series) -> pd.Series:
    """dd_025_drawdown_intensity_ath"""
    dd = dd_008_drawdown_ath(close)
    mdd = dd.expanding().min()
    return _safe_div(dd, mdd)

def dd_026_drawdown_vs_historical_max_252d(close: pd.Series) -> pd.Series:
    """dd_026_drawdown_vs_historical_max_252d"""
    dd = dd_004_drawdown_252d(close)
    mdd = _rolling_min(dd, 252 * 5)  # vs 5yr max drawdown
    return _safe_div(dd, mdd)

def dd_027_drawdown_vs_median_252d(close: pd.Series) -> pd.Series:
    """dd_027_drawdown_vs_median_252d"""
    dd = dd_004_drawdown_252d(close)
    return _safe_div(dd, _rolling_median(dd, _TD_YEAR))

def dd_028_drawdown_vs_mean_252d(close: pd.Series) -> pd.Series:
    """dd_028_drawdown_vs_mean_252d"""
    dd = dd_004_drawdown_252d(close)
    return _safe_div(dd, _rolling_mean(dd, _TD_YEAR))

def dd_029_drawdown_pct_rank_252d(close: pd.Series) -> pd.Series:
    """dd_029_drawdown_pct_rank_252d"""
    return _rank_pct(dd_004_drawdown_252d(close), _TD_YEAR)

def dd_030_drawdown_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """dd_030_drawdown_pct_rank_1260d"""
    return _rank_pct(dd_007_drawdown_1260d(close), 1260)


# 031-040: High-low range relative to trailing highs

def dd_031_low_to_high_ratio_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """dd_031_low_to_high_ratio_252d feature"""
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(low, h)

def dd_032_low_to_high_ratio_ath(close: pd.Series, low: pd.Series) -> pd.Series:
    """dd_032_low_to_high_ratio_ath"""
    h = close.expanding().max()
    return _safe_div(low, h)

def dd_033_high_minus_low_over_high_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """dd_033_high_minus_low_over_high_252d"""
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(h - low, h)

def dd_034_high_minus_close_over_high_252d(close: pd.Series) -> pd.Series:
    """dd_034_high_minus_close_over_high_252d"""
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(h - close, h)

def dd_035_ath_minus_low_over_ath(close: pd.Series, low: pd.Series) -> pd.Series:
    """dd_035_ath_minus_low_over_ath"""
    h = close.expanding().max()
    return _safe_div(h - low, h)

def dd_036_ath_minus_close_over_ath(close: pd.Series) -> pd.Series:
    """dd_036_ath_minus_close_over_ath"""
    h = close.expanding().max()
    return _safe_div(h - close, h)

def dd_037_drawdown_from_prev_quarter_high(close: pd.Series) -> pd.Series:
    """dd_037_drawdown_from_prev_quarter_high"""
    h = _rolling_max(close.shift(63), 63)
    return _safe_div(close - h, h)

def dd_038_drawdown_from_prev_year_high(close: pd.Series) -> pd.Series:
    """dd_038_drawdown_from_prev_year_high"""
    h = _rolling_max(close.shift(252), 252)
    return _safe_div(close - h, h)

def dd_039_drawdown_from_2y_ago_high(close: pd.Series) -> pd.Series:
    """dd_039_drawdown_from_2y_ago_high"""
    h = _rolling_max(close.shift(504), 252)
    return _safe_div(close - h, h)

def dd_040_drawdown_from_3y_ago_high(close: pd.Series) -> pd.Series:
    """dd_040_drawdown_from_3y_ago_high"""
    h = _rolling_max(close.shift(756), 252)
    return _safe_div(close - h, h)


# 041-050: Drawdown relative to typical recovery levels

def dd_041_drawdown_vs_63d_avg_drawdown(close: pd.Series) -> pd.Series:
    """dd_041_drawdown_vs_63d_avg_drawdown feature"""
    dd = dd_002_drawdown_63d(close)
    return _safe_div(dd, _rolling_mean(dd, 252))

def dd_042_drawdown_vs_252d_max_drawdown(close: pd.Series) -> pd.Series:
    """dd_042_drawdown_vs_252d_max_drawdown"""
    dd = dd_004_drawdown_252d(close)
    mdd = _rolling_min(dd, 252)
    return _safe_div(dd, mdd)

def dd_043_drawdown_vs_1260d_max_drawdown(close: pd.Series) -> pd.Series:
    """dd_043_drawdown_vs_1260d_max_drawdown"""
    dd = dd_007_drawdown_1260d(close)
    mdd = _rolling_min(dd, 1260)
    return _safe_div(dd, mdd)

def dd_044_drawdown_persistence_63d(close: pd.Series) -> pd.Series:
    """dd_044_drawdown_persistence_63d"""
    # Average drawdown over last 3 months
    dd = dd_002_drawdown_63d(close)
    return _rolling_mean(dd, 63)

def dd_045_drawdown_persistence_252d(close: pd.Series) -> pd.Series:
    """dd_045_drawdown_persistence_252d"""
    # Average drawdown over last year
    dd = dd_004_drawdown_252d(close)
    return _rolling_mean(dd, 252)

def dd_046_drawdown_volatility_63d(close: pd.Series) -> pd.Series:
    """dd_046_drawdown_volatility_63d"""
    dd = dd_002_drawdown_63d(close)
    return _rolling_std(dd, 63)

def dd_047_drawdown_volatility_252d(close: pd.Series) -> pd.Series:
    """dd_047_drawdown_volatility_252d"""
    dd = dd_004_drawdown_252d(close)
    return _rolling_std(dd, 252)

def dd_048_drawdown_skew_252d(close: pd.Series) -> pd.Series:
    """dd_048_drawdown_skew_252d"""
    dd = dd_004_drawdown_252d(close)
    return dd.rolling(252).skew()

def dd_049_drawdown_kurtosis_252d(close: pd.Series) -> pd.Series:
    """dd_049_drawdown_kurtosis_252d"""
    dd = dd_004_drawdown_252d(close)
    return dd.rolling(252).kurt()

def dd_050_drawdown_max_rolling_21d(close: pd.Series) -> pd.Series:
    """dd_050_drawdown_max_rolling_21d"""
    dd = dd_004_drawdown_252d(close)
    return _rolling_min(dd, 21)


# 051-060: Drawdowns relative to moving averages

def dd_051_drawdown_from_sma_20(close: pd.Series) -> pd.Series:
    """dd_051_drawdown_from_sma_20 feature"""
    ma = _rolling_mean(close, 20)
    return _safe_div(close - ma, ma)

def dd_052_drawdown_from_sma_50(close: pd.Series) -> pd.Series:
    """dd_052_drawdown_from_sma_50"""
    ma = _rolling_mean(close, 50)
    return _safe_div(close - ma, ma)

def dd_053_drawdown_from_sma_200(close: pd.Series) -> pd.Series:
    """dd_053_drawdown_from_sma_200"""
    ma = _rolling_mean(close, 200)
    return _safe_div(close - ma, ma)

def dd_054_sma_50_from_sma_200(close: pd.Series) -> pd.Series:
    """dd_054_sma_50_from_sma_200"""
    ma50 = _rolling_mean(close, 50)
    ma200 = _rolling_mean(close, 200)
    return _safe_div(ma50 - ma200, ma200)

def dd_055_drawdown_from_max_sma_200_252d(close: pd.Series) -> pd.Series:
    """dd_055_drawdown_from_max_sma_200_252d"""
    ma200 = _rolling_mean(close, 200)
    h = _rolling_max(ma200, 252)
    return _safe_div(ma200 - h, h)

def dd_056_drawdown_from_ema_20(close: pd.Series) -> pd.Series:
    """dd_056_drawdown_from_ema_20"""
    ma = _ewm_mean(close, 20)
    return _safe_div(close - ma, ma)

def dd_057_drawdown_from_ema_50(close: pd.Series) -> pd.Series:
    """dd_057_drawdown_from_ema_50"""
    ma = _ewm_mean(close, 50)
    return _safe_div(close - ma, ma)

def dd_058_drawdown_from_ema_200(close: pd.Series) -> pd.Series:
    """dd_058_drawdown_from_ema_200"""
    ma = _ewm_mean(close, 200)
    return _safe_div(close - ma, ma)

def dd_059_ema_50_from_ema_200(close: pd.Series) -> pd.Series:
    """dd_059_ema_50_from_ema_200"""
    ma50 = _ewm_mean(close, 50)
    ma200 = _ewm_mean(close, 200)
    return _safe_div(ma50 - ma200, ma200)

def dd_060_drawdown_sma_cross_20_50(close: pd.Series) -> pd.Series:
    """dd_060_drawdown_sma_cross_20_50"""
    ma20 = _rolling_mean(close, 20)
    ma50 = _rolling_mean(close, 50)
    return _safe_div(ma20, ma50) - 1.0


# 061-075: Drawdown depth vs fundamental anchors (if available)

def dd_061_price_to_equity_drawdown_ath(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_061_price_to_equity_drawdown_ath feature"""
    bvps = _safe_div(equity, sharesbas)
    p_bv = _safe_div(close, bvps)
    h = p_bv.expanding().max()
    return _safe_div(p_bv - h, h)

def dd_062_price_to_revenue_drawdown_ath(close: pd.Series, revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_062_price_to_revenue_drawdown_ath"""
    revps = _safe_div(revenue, sharesbas)
    p_rev = _safe_div(close, revps)
    h = p_rev.expanding().max()
    return _safe_div(p_rev - h, h)

def dd_063_price_to_fcf_drawdown_ath(close: pd.Series, fcf: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_063_price_to_fcf_drawdown_ath"""
    fcfps = _safe_div(fcf, sharesbas)
    p_fcf = _safe_div(close, fcfps)
    h = p_fcf.expanding().max()
    return _safe_div(p_fcf - h, h)

def dd_064_mktcap_drawdown_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_064_mktcap_drawdown_252d"""
    mc = close * sharesbas
    h = _rolling_max(mc, 252)
    return _safe_div(mc - h, h)

def dd_065_mktcap_drawdown_ath(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_065_mktcap_drawdown_ath"""
    mc = close * sharesbas
    h = mc.expanding().max()
    return _safe_div(mc - h, h)

def dd_066_ev_drawdown_252d(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """dd_066_ev_drawdown_252d"""
    ev = (close * sharesbas) + debt - cashnequiv
    h = _rolling_max(ev, 252)
    return _safe_div(ev - h, h)

def dd_067_drawdown_log_spread_252d(close: pd.Series) -> pd.Series:
    """dd_067_drawdown_log_spread_252d"""
    # Spread between 252d high and current close in log space
    h = _rolling_max(close, 252)
    return np.log(h) - np.log(close)

def dd_068_drawdown_log_spread_ath(close: pd.Series) -> pd.Series:
    """dd_068_drawdown_log_spread_ath"""
    h = close.expanding().max()
    return np.log(h) - np.log(close)

def dd_069_drawdown_harmonic_mean_ratio_252d(close: pd.Series) -> pd.Series:
    """dd_069_drawdown_harmonic_mean_ratio_252d"""
    # Ratio of close to harmonic mean of highs over 252d
    h = _rolling_max(close, 252)
    harmonic_h = _safe_div(1.0, _rolling_mean(_safe_div(1.0, h), 252))
    return _safe_div(close, harmonic_h)

def dd_070_drawdown_geometric_mean_ratio_252d(close: pd.Series) -> pd.Series:
    """dd_070_drawdown_geometric_mean_ratio_252d"""
    # Ratio of close to geometric mean of highs over 252d
    h = _rolling_max(close, 252)
    geom_h = np.exp(_rolling_mean(np.log(h), 252))
    return _safe_div(close, geom_h)

def dd_071_drawdown_quadratic_mean_ratio_252d(close: pd.Series) -> pd.Series:
    """dd_071_drawdown_quadratic_mean_ratio_252d"""
    # Ratio of close to quadratic mean of highs over 252d
    h = _rolling_max(close, 252)
    quad_h = np.sqrt(_rolling_mean(h**2, 252))
    return _safe_div(close, quad_h)

def dd_072_drawdown_area_under_curve_63d(close: pd.Series) -> pd.Series:
    """dd_072_drawdown_area_under_curve_63d"""
    # Sum of drawdowns over 63 days
    dd = dd_002_drawdown_63d(close)
    return _rolling_sum(dd, 63)

def dd_073_drawdown_area_under_curve_252d(close: pd.Series) -> pd.Series:
    """dd_073_drawdown_area_under_curve_252d"""
    # Sum of drawdowns over 252 days
    dd = dd_004_drawdown_252d(close)
    return _rolling_sum(dd, 252)

def dd_074_drawdown_tail_risk_252d(close: pd.Series) -> pd.Series:
    """dd_074_drawdown_tail_risk_252d"""
    # Ratio of 5th percentile drawdown to mean drawdown
    dd = dd_004_drawdown_252d(close)
    p5 = dd.rolling(252).quantile(0.05)
    m = _rolling_mean(dd, 252)
    return _safe_div(p5, m)

def dd_075_drawdown_var_95_252d(close: pd.Series) -> pd.Series:
    """dd_075_drawdown_var_95_252d"""
    # 95% VaR proxy based on drawdowns
    dd = dd_004_drawdown_252d(close)
    return dd.rolling(252).quantile(0.05)

# ── Registry ──────────────────────────────────────────────────────────────────

V01_REGISTRY = {
    "dd_001_drawdown_21d": {"inputs": ["close"], "func": dd_001_drawdown_21d},
    "dd_002_drawdown_63d": {"inputs": ["close"], "func": dd_002_drawdown_63d},
    "dd_003_drawdown_126d": {"inputs": ["close"], "func": dd_003_drawdown_126d},
    "dd_004_drawdown_252d": {"inputs": ["close"], "func": dd_004_drawdown_252d},
    "dd_005_drawdown_504d": {"inputs": ["close"], "func": dd_005_drawdown_504d},
    "dd_006_drawdown_756d": {"inputs": ["close"], "func": dd_006_drawdown_756d},
    "dd_007_drawdown_1260d": {"inputs": ["close"], "func": dd_007_drawdown_1260d},
    "dd_008_drawdown_ath": {"inputs": ["close"], "func": dd_008_drawdown_ath},
    "dd_009_drawdown_log_252d": {"inputs": ["close"], "func": dd_009_drawdown_log_252d},
    "dd_010_drawdown_log_ath": {"inputs": ["close"], "func": dd_010_drawdown_log_ath},
    "dd_011_drawdown_sigma_63d": {"inputs": ["close"], "func": dd_011_drawdown_sigma_63d},
    "dd_012_drawdown_sigma_252d": {"inputs": ["close"], "func": dd_012_drawdown_sigma_252d},
    "dd_013_drawdown_sigma_504d": {"inputs": ["close"], "func": dd_013_drawdown_sigma_504d},
    "dd_014_drawdown_sigma_ath": {"inputs": ["close"], "func": dd_014_drawdown_sigma_ath},
    "dd_015_drawdown_vol_normalized_21d": {"inputs": ["close"], "func": dd_015_drawdown_vol_normalized_21d},
    "dd_016_drawdown_vol_normalized_63d": {"inputs": ["close"], "func": dd_016_drawdown_vol_normalized_63d},
    "dd_017_drawdown_vol_normalized_252d": {"inputs": ["close"], "func": dd_017_drawdown_vol_normalized_252d},
    "dd_018_drawdown_vol_normalized_ath": {"inputs": ["close"], "func": dd_018_drawdown_vol_normalized_ath},
    "dd_019_drawdown_zscore_252d": {"inputs": ["close"], "func": dd_019_drawdown_zscore_252d},
    "dd_020_drawdown_zscore_1260d": {"inputs": ["close"], "func": dd_020_drawdown_zscore_1260d},
    "dd_021_drawdown_ratio_252d_ath": {"inputs": ["close"], "func": dd_021_drawdown_ratio_252d_ath},
    "dd_022_drawdown_ratio_63d_252d": {"inputs": ["close"], "func": dd_022_drawdown_ratio_63d_252d},
    "dd_023_drawdown_ratio_21d_63d": {"inputs": ["close"], "func": dd_023_drawdown_ratio_21d_63d},
    "dd_024_drawdown_intensity_252d": {"inputs": ["close"], "func": dd_024_drawdown_intensity_252d},
    "dd_025_drawdown_intensity_ath": {"inputs": ["close"], "func": dd_025_drawdown_intensity_ath},
    "dd_026_drawdown_vs_historical_max_252d": {"inputs": ["close"], "func": dd_026_drawdown_vs_historical_max_252d},
    "dd_027_drawdown_vs_median_252d": {"inputs": ["close"], "func": dd_027_drawdown_vs_median_252d},
    "dd_028_drawdown_vs_mean_252d": {"inputs": ["close"], "func": dd_028_drawdown_vs_mean_252d},
    "dd_029_drawdown_pct_rank_252d": {"inputs": ["close"], "func": dd_029_drawdown_pct_rank_252d},
    "dd_030_drawdown_pct_rank_1260d": {"inputs": ["close"], "func": dd_030_drawdown_pct_rank_1260d},
    "dd_031_low_to_high_ratio_252d": {"inputs": ["close", "low"], "func": dd_031_low_to_high_ratio_252d},
    "dd_032_low_to_high_ratio_ath": {"inputs": ["close", "low"], "func": dd_032_low_to_high_ratio_ath},
    "dd_033_high_minus_low_over_high_252d": {"inputs": ["close", "low"], "func": dd_033_high_minus_low_over_high_252d},
    "dd_034_high_minus_close_over_high_252d": {"inputs": ["close"], "func": dd_034_high_minus_close_over_high_252d},
    "dd_035_ath_minus_low_over_ath": {"inputs": ["close", "low"], "func": dd_035_ath_minus_low_over_ath},
    "dd_036_ath_minus_close_over_ath": {"inputs": ["close"], "func": dd_036_ath_minus_close_over_ath},
    "dd_037_drawdown_from_prev_quarter_high": {"inputs": ["close"], "func": dd_037_drawdown_from_prev_quarter_high},
    "dd_038_drawdown_from_prev_year_high": {"inputs": ["close"], "func": dd_038_drawdown_from_prev_year_high},
    "dd_039_drawdown_from_2y_ago_high": {"inputs": ["close"], "func": dd_039_drawdown_from_2y_ago_high},
    "dd_040_drawdown_from_3y_ago_high": {"inputs": ["close"], "func": dd_040_drawdown_from_3y_ago_high},
    "dd_041_drawdown_vs_63d_avg_drawdown": {"inputs": ["close"], "func": dd_041_drawdown_vs_63d_avg_drawdown},
    "dd_042_drawdown_vs_252d_max_drawdown": {"inputs": ["close"], "func": dd_042_drawdown_vs_252d_max_drawdown},
    "dd_043_drawdown_vs_1260d_max_drawdown": {"inputs": ["close"], "func": dd_043_drawdown_vs_1260d_max_drawdown},
    "dd_044_drawdown_persistence_63d": {"inputs": ["close"], "func": dd_044_drawdown_persistence_63d},
    "dd_045_drawdown_persistence_252d": {"inputs": ["close"], "func": dd_045_drawdown_persistence_252d},
    "dd_046_drawdown_volatility_63d": {"inputs": ["close"], "func": dd_046_drawdown_volatility_63d},
    "dd_047_drawdown_volatility_252d": {"inputs": ["close"], "func": dd_047_drawdown_volatility_252d},
    "dd_048_drawdown_skew_252d": {"inputs": ["close"], "func": dd_048_drawdown_skew_252d},
    "dd_049_drawdown_kurtosis_252d": {"inputs": ["close"], "func": dd_049_drawdown_kurtosis_252d},
    "dd_050_drawdown_max_rolling_21d": {"inputs": ["close"], "func": dd_050_drawdown_max_rolling_21d},
    "dd_051_drawdown_from_sma_20": {"inputs": ["close"], "func": dd_051_drawdown_from_sma_20},
    "dd_052_drawdown_from_sma_50": {"inputs": ["close"], "func": dd_052_drawdown_from_sma_50},
    "dd_053_drawdown_from_sma_200": {"inputs": ["close"], "func": dd_053_drawdown_from_sma_200},
    "dd_054_sma_50_from_sma_200": {"inputs": ["close"], "func": dd_054_sma_50_from_sma_200},
    "dd_055_drawdown_from_max_sma_200_252d": {"inputs": ["close"], "func": dd_055_drawdown_from_max_sma_200_252d},
    "dd_056_drawdown_from_ema_20": {"inputs": ["close"], "func": dd_056_drawdown_from_ema_20},
    "dd_057_drawdown_from_ema_50": {"inputs": ["close"], "func": dd_057_drawdown_from_ema_50},
    "dd_058_drawdown_from_ema_200": {"inputs": ["close"], "func": dd_058_drawdown_from_ema_200},
    "dd_059_ema_50_from_ema_200": {"inputs": ["close"], "func": dd_059_ema_50_from_ema_200},
    "dd_060_drawdown_sma_cross_20_50": {"inputs": ["close"], "func": dd_060_drawdown_sma_cross_20_50},
    "dd_061_price_to_equity_drawdown_ath": {"inputs": ["close", "equity", "sharesbas"], "func": dd_061_price_to_equity_drawdown_ath},
    "dd_062_price_to_revenue_drawdown_ath": {"inputs": ["close", "revenue", "sharesbas"], "func": dd_062_price_to_revenue_drawdown_ath},
    "dd_063_price_to_fcf_drawdown_ath": {"inputs": ["close", "fcf", "sharesbas"], "func": dd_063_price_to_fcf_drawdown_ath},
    "dd_064_mktcap_drawdown_252d": {"inputs": ["close", "sharesbas"], "func": dd_064_mktcap_drawdown_252d},
    "dd_065_mktcap_drawdown_ath": {"inputs": ["close", "sharesbas"], "func": dd_065_mktcap_drawdown_ath},
    "dd_066_ev_drawdown_252d": {"inputs": ["close", "sharesbas", "debt", "cashnequiv"], "func": dd_066_ev_drawdown_252d},
    "dd_067_drawdown_log_spread_252d": {"inputs": ["close"], "func": dd_067_drawdown_log_spread_252d},
    "dd_068_drawdown_log_spread_ath": {"inputs": ["close"], "func": dd_068_drawdown_log_spread_ath},
    "dd_069_drawdown_harmonic_mean_ratio_252d": {"inputs": ["close"], "func": dd_069_drawdown_harmonic_mean_ratio_252d},
    "dd_070_drawdown_geometric_mean_ratio_252d": {"inputs": ["close"], "func": dd_070_drawdown_geometric_mean_ratio_252d},
    "dd_071_drawdown_quadratic_mean_ratio_252d": {"inputs": ["close"], "func": dd_071_drawdown_quadratic_mean_ratio_252d},
    "dd_072_drawdown_area_under_curve_63d": {"inputs": ["close"], "func": dd_072_drawdown_area_under_curve_63d},
    "dd_073_drawdown_area_under_curve_252d": {"inputs": ["close"], "func": dd_073_drawdown_area_under_curve_252d},
    "dd_074_drawdown_tail_risk_252d": {"inputs": ["close"], "func": dd_074_drawdown_tail_risk_252d},
    "dd_075_drawdown_var_95_252d": {"inputs": ["close"], "func": dd_075_drawdown_var_95_252d},
}
