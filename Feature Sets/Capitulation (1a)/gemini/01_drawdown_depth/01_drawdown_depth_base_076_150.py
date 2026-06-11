"""
Drawdown Depth — Base Features 076–150
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

def dd_076_drawdown_atr_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dd_076_drawdown_atr_ratio_21d"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _rolling_mean(tr, 21)
    h = _rolling_max(close, 21)
    return _safe_div(close - h, atr)

def dd_077_drawdown_atr_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dd_077_drawdown_atr_ratio_63d"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _rolling_mean(tr, 63)
    h = _rolling_max(close, 63)
    return _safe_div(close - h, atr)

def dd_078_drawdown_atr_ratio_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dd_078_drawdown_atr_ratio_252d"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _rolling_mean(tr, 252)
    h = _rolling_max(close, 252)
    return _safe_div(close - h, atr)

def dd_079_drawdown_to_range_ratio_252d(close: pd.Series) -> pd.Series:
    """dd_079_drawdown_to_range_ratio_252d"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    r = h - l
    return _safe_div(close - h, r)

def dd_080_drawdown_to_range_ratio_ath(close: pd.Series) -> pd.Series:
    """dd_080_drawdown_to_range_ratio_ath"""
    h = close.expanding().max()
    l = close.expanding().min()
    r = h - l
    return _safe_div(close - h, r)

def dd_081_close_position_in_252d_range(close: pd.Series) -> pd.Series:
    """dd_081_close_position_in_252d_range"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    return _safe_div(close - l, h - l)

def dd_082_close_position_in_ath_range(close: pd.Series) -> pd.Series:
    """dd_082_close_position_in_ath_range"""
    h = close.expanding().max()
    l = close.expanding().min()
    return _safe_div(close - l, h - l)

def dd_083_drawdown_vs_historical_std_252d(close: pd.Series) -> pd.Series:
    """dd_083_drawdown_vs_historical_std_252d"""
    dd = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    return _safe_div(dd, _rolling_std(dd, 252 * 3))

def dd_084_drawdown_to_volatility_adjusted_ath(close: pd.Series) -> pd.Series:
    """dd_084_drawdown_to_volatility_adjusted_ath"""
    dd = _safe_div(close - close.expanding().max(), close.expanding().max())
    vol = _pct_change(close, 1).expanding().std()
    return _safe_div(dd, vol * np.sqrt(252))

def dd_085_drawdown_log_zscore_ath(close: pd.Series) -> pd.Series:
    """dd_085_drawdown_log_zscore_ath"""
    log_dd = np.log(close) - np.log(close.expanding().max())
    return _zscore_rolling(log_dd, 252 * 5)


# 086-095: Drawdown relative to various smoothed highs

def dd_086_drawdown_from_ema_high_21d(close: pd.Series) -> pd.Series:
    """dd_086_drawdown_from_ema_high_21d feature"""
    h = _ewm_mean(close, 21).expanding().max()
    return _safe_div(close - h, h)

def dd_087_drawdown_from_ema_high_63d(close: pd.Series) -> pd.Series:
    """dd_087_drawdown_from_ema_high_63d"""
    h = _ewm_mean(close, 63).expanding().max()
    return _safe_div(close - h, h)

def dd_088_drawdown_from_ema_high_252d(close: pd.Series) -> pd.Series:
    """dd_088_drawdown_from_ema_high_252d"""
    h = _ewm_mean(close, 252).expanding().max()
    return _safe_div(close - h, h)

def dd_089_drawdown_from_rolling_median_high_252d(close: pd.Series) -> pd.Series:
    """dd_089_drawdown_from_rolling_median_high_252d"""
    h = _rolling_median(close, 252).expanding().max()
    return _safe_div(close - h, h)

def dd_090_drawdown_from_rolling_mean_high_252d(close: pd.Series) -> pd.Series:
    """dd_090_drawdown_from_rolling_mean_high_252d"""
    h = _rolling_mean(close, 252).expanding().max()
    return _safe_div(close - h, h)

def dd_091_drawdown_from_90th_percentile_252d(close: pd.Series) -> pd.Series:
    """dd_091_drawdown_from_90th_percentile_252d"""
    h = close.rolling(252).quantile(0.9)
    return _safe_div(close - h, h)

def dd_092_drawdown_from_95th_percentile_252d(close: pd.Series) -> pd.Series:
    """dd_092_drawdown_from_95th_percentile_252d"""
    h = close.rolling(252).quantile(0.95)
    return _safe_div(close - h, h)

def dd_093_drawdown_from_99th_percentile_ath(close: pd.Series) -> pd.Series:
    """dd_093_drawdown_from_99th_percentile_ath"""
    h = close.expanding().quantile(0.99)
    return _safe_div(close - h, h)

def dd_094_drawdown_to_historical_min_ratio_252d(close: pd.Series) -> pd.Series:
    """dd_094_drawdown_to_historical_min_ratio_252d"""
    l = _rolling_min(close, 252 * 5)
    return _safe_div(close, l)

def dd_095_drawdown_to_historical_min_ratio_ath(close: pd.Series) -> pd.Series:
    """dd_095_drawdown_to_historical_min_ratio_ath"""
    l = close.expanding().min()
    return _safe_div(close, l)


# 096-105: Relative drawdown depth (vs own history)

def dd_096_drawdown_depth_zscore_63d(close: pd.Series) -> pd.Series:
    """dd_096_drawdown_depth_zscore_63d feature"""
    dd = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    return _zscore_rolling(dd, 252)

def dd_097_drawdown_depth_zscore_252d(close: pd.Series) -> pd.Series:
    """dd_097_drawdown_depth_zscore_252d"""
    dd = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    return _zscore_rolling(dd, 252 * 3)

def dd_098_drawdown_depth_pct_rank_ath(close: pd.Series) -> pd.Series:
    """dd_098_drawdown_depth_pct_rank_ath"""
    dd = _safe_div(close - close.expanding().max(), close.expanding().max())
    return dd.expanding().rank(pct=True)

def dd_099_drawdown_depth_vs_last_major_drawdown(close: pd.Series) -> pd.Series:
    """dd_099_drawdown_depth_vs_last_major_drawdown"""
    # Current drawdown relative to the max drawdown of the previous year
    dd_curr = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    dd_prev = _rolling_min(_safe_div(close.shift(252) - _rolling_max(close.shift(252), 252), _rolling_max(close.shift(252), 252)), 252)
    return _safe_div(dd_curr, dd_prev)

def dd_100_drawdown_intensity_index_63d(close: pd.Series) -> pd.Series:
    """dd_100_drawdown_intensity_index_63d"""
    # Average of drawdown vs 21, 42, 63 day highs
    dd21 = _safe_div(close - _rolling_max(close, 21), _rolling_max(close, 21))
    dd42 = _safe_div(close - _rolling_max(close, 42), _rolling_max(close, 42))
    dd63 = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    return (dd21 + dd42 + dd63) / 3.0


# 101-115: Interaction between price and volume-weighted highs

def dd_101_drawdown_from_vwap_high_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dd_101_drawdown_from_vwap_high_21d feature"""
    vwap = _safe_div(_rolling_sum(close * volume, 21), _rolling_sum(volume, 21))
    h = vwap.expanding().max()
    return _safe_div(close - h, h)

def dd_102_drawdown_from_vwap_high_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dd_102_drawdown_from_vwap_high_63d"""
    vwap = _safe_div(_rolling_sum(close * volume, 63), _rolling_sum(volume, 63))
    h = vwap.expanding().max()
    return _safe_div(close - h, h)

def dd_103_drawdown_from_vwap_high_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dd_103_drawdown_from_vwap_high_252d"""
    vwap = _safe_div(_rolling_sum(close * volume, 252), _rolling_sum(volume, 252))
    h = vwap.expanding().max()
    return _safe_div(close - h, h)

def dd_104_drawdown_weighted_by_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dd_104_drawdown_weighted_by_volume_63d"""
    dd = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    v_norm = _safe_div(volume, _rolling_mean(volume, 63))
    return dd * v_norm

def dd_105_drawdown_weighted_by_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dd_105_drawdown_weighted_by_volume_252d"""
    dd = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    v_norm = _safe_div(volume, _rolling_mean(volume, 252))
    return dd * v_norm


# 106-120: Drawdown relative to market capitalization / shares

def dd_106_mktcap_drawdown_log_spread_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_106_mktcap_drawdown_log_spread_252d feature"""
    mc = close * sharesbas
    h = _rolling_max(mc, 252)
    return np.log(h) - np.log(mc)

def dd_107_mktcap_drawdown_log_spread_ath(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_107_mktcap_drawdown_log_spread_ath"""
    mc = close * sharesbas
    h = mc.expanding().max()
    return np.log(h) - np.log(mc)

def dd_108_equity_drawdown_log_spread_ath(equity: pd.Series) -> pd.Series:
    """dd_108_equity_drawdown_log_spread_ath"""
    h = equity.expanding().max()
    return np.log(h) - np.log(equity)

def dd_109_revenue_drawdown_log_spread_ath(revenue: pd.Series) -> pd.Series:
    """dd_109_revenue_drawdown_log_spread_ath"""
    h = revenue.expanding().max()
    return np.log(h) - np.log(revenue)

def dd_110_fcf_drawdown_log_spread_ath(fcf: pd.Series) -> pd.Series:
    """dd_110_fcf_drawdown_log_spread_ath"""
    h = fcf.expanding().max()
    return np.log(h) - np.log(fcf)

def dd_111_asset_drawdown_log_spread_ath(assets: pd.Series) -> pd.Series:
    """dd_111_asset_drawdown_log_spread_ath"""
    h = assets.expanding().max()
    return np.log(h) - np.log(assets)

def dd_112_drawdown_from_intrinsic_value_proxy_ath(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_112_drawdown_from_intrinsic_value_proxy_ath"""
    bvps = _safe_div(equity, sharesbas)
    h = bvps.expanding().max()
    return _safe_div(close - h, h)

def dd_113_drawdown_from_revenue_ps_high_ath(close: pd.Series, revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_113_drawdown_from_revenue_ps_high_ath"""
    revps = _safe_div(revenue, sharesbas)
    h = revps.expanding().max()
    return _safe_div(close - h, h)

def dd_114_drawdown_from_fcf_ps_high_ath(close: pd.Series, fcf: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_114_drawdown_from_fcf_ps_high_ath"""
    fcfps = _safe_div(fcf, sharesbas)
    h = fcfps.expanding().max()
    return _safe_div(close - h, h)

def dd_115_drawdown_from_ebit_ps_high_ath(close: pd.Series, ebit: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_115_drawdown_from_ebit_ps_high_ath"""
    ebitps = _safe_div(ebit, sharesbas)
    h = ebitps.expanding().max()
    return _safe_div(close - h, h)


# 121-135: Drawdown relative to trailing high-low volatility

def dd_121_drawdown_to_hl_vol_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dd_121_drawdown_to_hl_vol_ratio_63d feature"""
    dd = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    hl_vol = _rolling_std(high - low, 63) / _rolling_mean(close, 63)
    return _safe_div(dd, hl_vol)

def dd_122_drawdown_to_hl_vol_ratio_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dd_122_drawdown_to_hl_vol_ratio_252d"""
    dd = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    hl_vol = _rolling_std(high - low, 252) / _rolling_mean(close, 252)
    return _safe_div(dd, hl_vol)

def dd_123_drawdown_to_body_vol_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """dd_123_drawdown_to_body_vol_ratio_63d"""
    dd = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    body_vol = _rolling_std((close - open).abs(), 63) / _rolling_mean(close, 63)
    return _safe_div(dd, body_vol)

def dd_124_drawdown_to_body_vol_ratio_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """dd_124_drawdown_to_body_vol_ratio_252d"""
    dd = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    body_vol = _rolling_std((close - open).abs(), 252) / _rolling_mean(close, 252)
    return _safe_div(dd, body_vol)

def dd_125_drawdown_to_gap_vol_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """dd_125_drawdown_to_gap_vol_ratio_63d"""
    dd = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    gap_vol = _rolling_std((open - close.shift(1)).abs(), 63) / _rolling_mean(close, 63)
    return _safe_div(dd, gap_vol)


# 126-140: Multi-window drawdown averages

def dd_126_avg_drawdown_21_63_252(close: pd.Series) -> pd.Series:
    """dd_126_avg_drawdown_21_63_252 feature"""
    dd21 = _safe_div(close - _rolling_max(close, 21), _rolling_max(close, 21))
    dd63 = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    dd252 = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    return (dd21 + dd63 + dd252) / 3.0

def dd_127_max_drawdown_21_63_252(close: pd.Series) -> pd.Series:
    """dd_127_max_drawdown_21_63_252"""
    dd21 = _safe_div(close - _rolling_max(close, 21), _rolling_max(close, 21))
    dd63 = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    dd252 = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    return pd.concat([dd21, dd63, dd252], axis=1).min(axis=1)

def dd_128_min_drawdown_21_63_252(close: pd.Series) -> pd.Series:
    """dd_128_min_drawdown_21_63_252"""
    dd21 = _safe_div(close - _rolling_max(close, 21), _rolling_max(close, 21))
    dd63 = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    dd252 = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    return pd.concat([dd21, dd63, dd252], axis=1).max(axis=1)

def dd_129_drawdown_dispersion_252d(close: pd.Series) -> pd.Series:
    """dd_129_drawdown_dispersion_252d"""
    # Std dev of drawdowns across windows 21..252
    windows = [21, 42, 63, 126, 252]
    dds = [ _safe_div(close - _rolling_max(close, w), _rolling_max(close, w)) for w in windows ]
    return pd.concat(dds, axis=1).std(axis=1)

def dd_130_drawdown_step_ratio_252d(close: pd.Series) -> pd.Series:
    """dd_130_drawdown_step_ratio_252d"""
    # Ratio of 252d drawdown to 126d drawdown
    dd252 = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    dd126 = _safe_div(close - _rolling_max(close, 126), _rolling_max(close, 126))
    return _safe_div(dd252, dd126)


# 141-150: Final set of depth features

def dd_141_drawdown_from_ath_minus_drawdown_from_252d(close: pd.Series) -> pd.Series:
    """dd_141_drawdown_from_ath_minus_drawdown_from_252d feature"""
    return dd_008_drawdown_ath(close) - _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))

def dd_142_drawdown_from_5y_high_minus_drawdown_from_1y_high(close: pd.Series) -> pd.Series:
    """dd_142_drawdown_from_5y_high_minus_drawdown_from_1y_high"""
    dd5y = _safe_div(close - _rolling_max(close, 1260), _rolling_max(close, 1260))
    dd1y = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    return dd5y - dd1y

def dd_143_drawdown_area_normalized_63d(close: pd.Series) -> pd.Series:
    """dd_143_drawdown_area_normalized_63d"""
    # Area under curve normalized by window length
    return dd_072_drawdown_area_under_curve_63d(close) / 63.0

def dd_144_drawdown_area_normalized_252d(close: pd.Series) -> pd.Series:
    """dd_144_drawdown_area_normalized_252d"""
    return dd_073_drawdown_area_under_curve_252d(close) / 252.0

def dd_145_drawdown_convexity_proxy_63d(close: pd.Series) -> pd.Series:
    """dd_145_drawdown_convexity_proxy_63d"""
    # Area vs max depth ratio (lower = more convex/sharp decline)
    area = dd_072_drawdown_area_under_curve_63d(close)
    max_dd = _rolling_min(_safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63)), 63)
    return _safe_div(area, max_dd * 63.0)

def dd_146_drawdown_convexity_proxy_252d(close: pd.Series) -> pd.Series:
    """dd_146_drawdown_convexity_proxy_252d"""
    area = dd_073_drawdown_area_under_curve_252d(close)
    max_dd = _rolling_min(_safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252)), 252)
    return _safe_div(area, max_dd * 252.0)

def dd_147_drawdown_entropy_proxy_252d(close: pd.Series) -> pd.Series:
    """dd_147_drawdown_entropy_proxy_252d"""
    # Variance of daily changes in drawdown (measure of jaggedness)
    dd = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    return _rolling_std(_pct_change(dd, 1), 252)

def dd_148_drawdown_recovery_ratio_252d(close: pd.Series) -> pd.Series:
    """dd_148_drawdown_recovery_ratio_252d"""
    # Current close relative to the low within the current drawdown
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    return _safe_div(close - l, h - l)

def dd_149_drawdown_recovery_ratio_ath(close: pd.Series) -> pd.Series:
    """dd_149_drawdown_recovery_ratio_ath"""
    h = close.expanding().max()
    l = close.expanding().min()
    return _safe_div(close - l, h - l)

def dd_150_drawdown_final_depth_metric(close: pd.Series) -> pd.Series:
    """dd_150_drawdown_final_depth_metric"""
    # Composite: weighted average of drawdowns across horizons
    dd21 = _safe_div(close - _rolling_max(close, 21), _rolling_max(close, 21))
    dd63 = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    dd252 = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    dd504 = _safe_div(close - _rolling_max(close, 504), _rolling_max(close, 504))
    return (0.4 * dd21 + 0.3 * dd63 + 0.2 * dd252 + 0.1 * dd504)

def dd_129_variation_0(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """zscore variation of dd_076_drawdown_atr_ratio_21d"""
    base_feat = dd_076_drawdown_atr_ratio_21d(close,high,low)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_130_variation_1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """rank variation of dd_077_drawdown_atr_ratio_63d"""
    base_feat = dd_077_drawdown_atr_ratio_63d(close,high,low)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_131_variation_2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """zscore variation of dd_078_drawdown_atr_ratio_252d"""
    base_feat = dd_078_drawdown_atr_ratio_252d(close,high,low)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_132_variation_3(close: pd.Series) -> pd.Series:
    """rank variation of dd_079_drawdown_to_range_ratio_252d"""
    base_feat = dd_079_drawdown_to_range_ratio_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_133_variation_4(close: pd.Series) -> pd.Series:
    """zscore variation of dd_080_drawdown_to_range_ratio_ath"""
    base_feat = dd_080_drawdown_to_range_ratio_ath(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_134_variation_5(close: pd.Series) -> pd.Series:
    """rank variation of dd_081_close_position_in_252d_range"""
    base_feat = dd_081_close_position_in_252d_range(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_135_variation_6(close: pd.Series) -> pd.Series:
    """zscore variation of dd_082_close_position_in_ath_range"""
    base_feat = dd_082_close_position_in_ath_range(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_136_variation_7(close: pd.Series) -> pd.Series:
    """rank variation of dd_083_drawdown_vs_historical_std_252d"""
    base_feat = dd_083_drawdown_vs_historical_std_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_137_variation_8(close: pd.Series) -> pd.Series:
    """zscore variation of dd_084_drawdown_to_volatility_adjusted_ath"""
    base_feat = dd_084_drawdown_to_volatility_adjusted_ath(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_138_variation_9(close: pd.Series) -> pd.Series:
    """rank variation of dd_085_drawdown_log_zscore_ath"""
    base_feat = dd_085_drawdown_log_zscore_ath(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_139_variation_10(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """zscore variation of dd_076_drawdown_atr_ratio_21d"""
    base_feat = dd_076_drawdown_atr_ratio_21d(close,high,low)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_140_variation_11(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """rank variation of dd_077_drawdown_atr_ratio_63d"""
    base_feat = dd_077_drawdown_atr_ratio_63d(close,high,low)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_141_variation_12(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """zscore variation of dd_078_drawdown_atr_ratio_252d"""
    base_feat = dd_078_drawdown_atr_ratio_252d(close,high,low)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_142_variation_13(close: pd.Series) -> pd.Series:
    """rank variation of dd_079_drawdown_to_range_ratio_252d"""
    base_feat = dd_079_drawdown_to_range_ratio_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dd_143_variation_14(close: pd.Series) -> pd.Series:
    """zscore variation of dd_080_drawdown_to_range_ratio_ath"""
    base_feat = dd_080_drawdown_to_range_ratio_ath(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V01_REGISTRY = {
    "dd_076_drawdown_atr_ratio_21d": {"inputs": ["close", "high", "low"], "func": dd_076_drawdown_atr_ratio_21d},
    "dd_077_drawdown_atr_ratio_63d": {"inputs": ["close", "high", "low"], "func": dd_077_drawdown_atr_ratio_63d},
    "dd_078_drawdown_atr_ratio_252d": {"inputs": ["close", "high", "low"], "func": dd_078_drawdown_atr_ratio_252d},
    "dd_079_drawdown_to_range_ratio_252d": {"inputs": ["close"], "func": dd_079_drawdown_to_range_ratio_252d},
    "dd_080_drawdown_to_range_ratio_ath": {"inputs": ["close"], "func": dd_080_drawdown_to_range_ratio_ath},
    "dd_081_close_position_in_252d_range": {"inputs": ["close"], "func": dd_081_close_position_in_252d_range},
    "dd_082_close_position_in_ath_range": {"inputs": ["close"], "func": dd_082_close_position_in_ath_range},
    "dd_083_drawdown_vs_historical_std_252d": {"inputs": ["close"], "func": dd_083_drawdown_vs_historical_std_252d},
    "dd_084_drawdown_to_volatility_adjusted_ath": {"inputs": ["close"], "func": dd_084_drawdown_to_volatility_adjusted_ath},
    "dd_085_drawdown_log_zscore_ath": {"inputs": ["close"], "func": dd_085_drawdown_log_zscore_ath},
    "dd_086_drawdown_from_ema_high_21d": {"inputs": ["close"], "func": dd_086_drawdown_from_ema_high_21d},
    "dd_087_drawdown_from_ema_high_63d": {"inputs": ["close"], "func": dd_087_drawdown_from_ema_high_63d},
    "dd_088_drawdown_from_ema_high_252d": {"inputs": ["close"], "func": dd_088_drawdown_from_ema_high_252d},
    "dd_089_drawdown_from_rolling_median_high_252d": {"inputs": ["close"], "func": dd_089_drawdown_from_rolling_median_high_252d},
    "dd_090_drawdown_from_rolling_mean_high_252d": {"inputs": ["close"], "func": dd_090_drawdown_from_rolling_mean_high_252d},
    "dd_091_drawdown_from_90th_percentile_252d": {"inputs": ["close"], "func": dd_091_drawdown_from_90th_percentile_252d},
    "dd_092_drawdown_from_95th_percentile_252d": {"inputs": ["close"], "func": dd_092_drawdown_from_95th_percentile_252d},
    "dd_093_drawdown_from_99th_percentile_ath": {"inputs": ["close"], "func": dd_093_drawdown_from_99th_percentile_ath},
    "dd_094_drawdown_to_historical_min_ratio_252d": {"inputs": ["close"], "func": dd_094_drawdown_to_historical_min_ratio_252d},
    "dd_095_drawdown_to_historical_min_ratio_ath": {"inputs": ["close"], "func": dd_095_drawdown_to_historical_min_ratio_ath},
    "dd_096_drawdown_depth_zscore_63d": {"inputs": ["close"], "func": dd_096_drawdown_depth_zscore_63d},
    "dd_097_drawdown_depth_zscore_252d": {"inputs": ["close"], "func": dd_097_drawdown_depth_zscore_252d},
    "dd_098_drawdown_depth_pct_rank_ath": {"inputs": ["close"], "func": dd_098_drawdown_depth_pct_rank_ath},
    "dd_099_drawdown_depth_vs_last_major_drawdown": {"inputs": ["close"], "func": dd_099_drawdown_depth_vs_last_major_drawdown},
    "dd_100_drawdown_intensity_index_63d": {"inputs": ["close"], "func": dd_100_drawdown_intensity_index_63d},
    "dd_101_drawdown_from_vwap_high_21d": {"inputs": ["close", "volume"], "func": dd_101_drawdown_from_vwap_high_21d},
    "dd_102_drawdown_from_vwap_high_63d": {"inputs": ["close", "volume"], "func": dd_102_drawdown_from_vwap_high_63d},
    "dd_103_drawdown_from_vwap_high_252d": {"inputs": ["close", "volume"], "func": dd_103_drawdown_from_vwap_high_252d},
    "dd_104_drawdown_weighted_by_volume_63d": {"inputs": ["close", "volume"], "func": dd_104_drawdown_weighted_by_volume_63d},
    "dd_105_drawdown_weighted_by_volume_252d": {"inputs": ["close", "volume"], "func": dd_105_drawdown_weighted_by_volume_252d},
    "dd_106_mktcap_drawdown_log_spread_252d": {"inputs": ["close", "sharesbas"], "func": dd_106_mktcap_drawdown_log_spread_252d},
    "dd_107_mktcap_drawdown_log_spread_ath": {"inputs": ["close", "sharesbas"], "func": dd_107_mktcap_drawdown_log_spread_ath},
    "dd_108_equity_drawdown_log_spread_ath": {"inputs": ["equity"], "func": dd_108_equity_drawdown_log_spread_ath},
    "dd_109_revenue_drawdown_log_spread_ath": {"inputs": ["revenue"], "func": dd_109_revenue_drawdown_log_spread_ath},
    "dd_110_fcf_drawdown_log_spread_ath": {"inputs": ["fcf"], "func": dd_110_fcf_drawdown_log_spread_ath},
    "dd_111_asset_drawdown_log_spread_ath": {"inputs": ["assets"], "func": dd_111_asset_drawdown_log_spread_ath},
    "dd_112_drawdown_from_intrinsic_value_proxy_ath": {"inputs": ["close", "equity", "sharesbas"], "func": dd_112_drawdown_from_intrinsic_value_proxy_ath},
    "dd_113_drawdown_from_revenue_ps_high_ath": {"inputs": ["close", "revenue", "sharesbas"], "func": dd_113_drawdown_from_revenue_ps_high_ath},
    "dd_114_drawdown_from_fcf_ps_high_ath": {"inputs": ["close", "fcf", "sharesbas"], "func": dd_114_drawdown_from_fcf_ps_high_ath},
    "dd_115_drawdown_from_ebit_ps_high_ath": {"inputs": ["close", "ebit", "sharesbas"], "func": dd_115_drawdown_from_ebit_ps_high_ath},
    "dd_121_drawdown_to_hl_vol_ratio_63d": {"inputs": ["close", "high", "low"], "func": dd_121_drawdown_to_hl_vol_ratio_63d},
    "dd_122_drawdown_to_hl_vol_ratio_252d": {"inputs": ["close", "high", "low"], "func": dd_122_drawdown_to_hl_vol_ratio_252d},
    "dd_123_drawdown_to_body_vol_ratio_63d": {"inputs": ["close", "open"], "func": dd_123_drawdown_to_body_vol_ratio_63d},
    "dd_124_drawdown_to_body_vol_ratio_252d": {"inputs": ["close", "open"], "func": dd_124_drawdown_to_body_vol_ratio_252d},
    "dd_125_drawdown_to_gap_vol_ratio_63d": {"inputs": ["close", "open"], "func": dd_125_drawdown_to_gap_vol_ratio_63d},
    "dd_126_avg_drawdown_21_63_252": {"inputs": ["close"], "func": dd_126_avg_drawdown_21_63_252},
    "dd_127_max_drawdown_21_63_252": {"inputs": ["close"], "func": dd_127_max_drawdown_21_63_252},
    "dd_128_min_drawdown_21_63_252": {"inputs": ["close"], "func": dd_128_min_drawdown_21_63_252},
    "dd_129_drawdown_dispersion_252d": {"inputs": ["close"], "func": dd_129_drawdown_dispersion_252d},
    "dd_130_drawdown_step_ratio_252d": {"inputs": ["close"], "func": dd_130_drawdown_step_ratio_252d},
    "dd_141_drawdown_from_ath_minus_drawdown_from_252d": {"inputs": ["close"], "func": dd_141_drawdown_from_ath_minus_drawdown_from_252d},
    "dd_142_drawdown_from_5y_high_minus_drawdown_from_1y_high": {"inputs": ["close"], "func": dd_142_drawdown_from_5y_high_minus_drawdown_from_1y_high},
    "dd_143_drawdown_area_normalized_63d": {"inputs": ["close"], "func": dd_143_drawdown_area_normalized_63d},
    "dd_144_drawdown_area_normalized_252d": {"inputs": ["close"], "func": dd_144_drawdown_area_normalized_252d},
    "dd_145_drawdown_convexity_proxy_63d": {"inputs": ["close"], "func": dd_145_drawdown_convexity_proxy_63d},
    "dd_146_drawdown_convexity_proxy_252d": {"inputs": ["close"], "func": dd_146_drawdown_convexity_proxy_252d},
    "dd_147_drawdown_entropy_proxy_252d": {"inputs": ["close"], "func": dd_147_drawdown_entropy_proxy_252d},
    "dd_148_drawdown_recovery_ratio_252d": {"inputs": ["close"], "func": dd_148_drawdown_recovery_ratio_252d},
    "dd_149_drawdown_recovery_ratio_ath": {"inputs": ["close"], "func": dd_149_drawdown_recovery_ratio_ath},
    "dd_150_drawdown_final_depth_metric": {"inputs": ["close"], "func": dd_150_drawdown_final_depth_metric},
    "dd_129_variation_0": {"inputs": ["close", "high", "low"], "func": dd_129_variation_0},
    "dd_130_variation_1": {"inputs": ["close", "high", "low"], "func": dd_130_variation_1},
    "dd_131_variation_2": {"inputs": ["close", "high", "low"], "func": dd_131_variation_2},
    "dd_132_variation_3": {"inputs": ["close"], "func": dd_132_variation_3},
    "dd_133_variation_4": {"inputs": ["close"], "func": dd_133_variation_4},
    "dd_134_variation_5": {"inputs": ["close"], "func": dd_134_variation_5},
    "dd_135_variation_6": {"inputs": ["close"], "func": dd_135_variation_6},
    "dd_136_variation_7": {"inputs": ["close"], "func": dd_136_variation_7},
    "dd_137_variation_8": {"inputs": ["close"], "func": dd_137_variation_8},
    "dd_138_variation_9": {"inputs": ["close"], "func": dd_138_variation_9},
    "dd_139_variation_10": {"inputs": ["close", "high", "low"], "func": dd_139_variation_10},
    "dd_140_variation_11": {"inputs": ["close", "high", "low"], "func": dd_140_variation_11},
    "dd_141_variation_12": {"inputs": ["close", "high", "low"], "func": dd_141_variation_12},
    "dd_142_variation_13": {"inputs": ["close"], "func": dd_142_variation_13},
    "dd_143_variation_14": {"inputs": ["close"], "func": dd_143_variation_14},
}
