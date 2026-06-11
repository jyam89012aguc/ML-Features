"""
Drawdown Shape — Base Features 076–150
Domain: shape and convexity of decline
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

def dsh_076_drawdown_return_skewness_252d(close: pd.Series) -> pd.Series:
    """dsh_076_drawdown_return_skewness_252d"""
    ret = close.pct_change()
    h = _rolling_max(close, 252)
    in_dd = close < h
    return ret[in_dd].rolling(252).skew()

def dsh_077_drawdown_return_kurtosis_252d(close: pd.Series) -> pd.Series:
    """dsh_077_drawdown_return_kurtosis_252d"""
    ret = close.pct_change()
    h = _rolling_max(close, 252)
    in_dd = close < h
    return ret[in_dd].rolling(252).kurt()

def dsh_078_drawdown_vol_ratio_early_vs_late_63d(close: pd.Series) -> pd.Series:
    """dsh_078_drawdown_vol_ratio_early_vs_late_63d"""
    # Volatility of first half of drawdown vs second half
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _vol_ratio(y):
        mid = len(y) // 2
        v1 = np.std(y[:mid])
        v2 = np.std(y[mid:])
        return _safe_div(pd.Series(v2), pd.Series(v1)).iloc[0]
    return dd.rolling(63).apply(_vol_ratio, raw=True)

def dsh_079_drawdown_velocity_inflection_63d(close: pd.Series) -> pd.Series:
    """dsh_079_drawdown_velocity_inflection_63d"""
    # Sign of 2nd derivative of the path (acceleration sign)
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _inflection(y):
        x = np.arange(len(y))
        coeffs = np.polyfit(x, y, 2)
        return np.sign(coeffs[0])
    return dd.rolling(63).apply(_inflection, raw=True)

def dsh_080_drawdown_tail_to_body_ratio_63d(close: pd.Series) -> pd.Series:
    """dsh_080_drawdown_tail_to_body_ratio_63d"""
    # (Max DD - Mean DD) / Std DD
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    m = dd.rolling(63).mean()
    s = dd.rolling(63).std()
    mx = dd.rolling(63).min()
    return _safe_div(mx - m, s)


# 091-105: Pattern-based Shape metrics

def dsh_091_drawdown_rounded_top_score_63d(close: pd.Series) -> pd.Series:
    """dsh_091_drawdown_rounded_top_score_63d feature"""
    # Fit to negative parabola (-x^2)
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _top_score(y):
        x = np.arange(len(y))
        coeffs = np.polyfit(x, y, 2)
        return -coeffs[0] if coeffs[0] < 0 else 0
    return dd.rolling(63).apply(_top_score, raw=True)

def dsh_092_drawdown_vertical_drop_score_63d(close: pd.Series) -> pd.Series:
    """dsh_092_drawdown_vertical_drop_score_63d"""
    # Sum of drops > 3 std devs
    ret = close.pct_change()
    m = ret.rolling(63).mean()
    s = ret.rolling(63).std()
    outlier = (ret < m - 3 * s).astype(int)
    return outlier.rolling(63).sum()

def dsh_093_drawdown_bounce_fading_score_63d(close: pd.Series) -> pd.Series:
    """dsh_093_drawdown_bounce_fading_score_63d"""
    # Correlation between rally magnitude and rally duration (lower = weaker bounces)
    h = _rolling_max(close, 63)
    ret = close.pct_change()
    is_up = (ret > 0).astype(int)
    # This is complex for a simple series, using proxy: avg rally return
    rally_ret = ret.where(ret > 0).rolling(63).mean()
    return rally_ret

def dsh_094_drawdown_log_linear_residual_std_63d(close: pd.Series) -> pd.Series:
    """dsh_094_drawdown_log_linear_residual_std_63d"""
    h = _rolling_max(close, 63)
    dd = (h - close) / h + 0.01
    def _res_std(y):
        x = np.arange(len(y))
        res = linregress(x, np.log(y))
        y_fit = res.intercept + res.slope * x
        return np.std(np.log(y) - y_fit)
    return dd.rolling(63).apply(_res_std, raw=True)

def dsh_095_drawdown_path_fractal_dimension_63d(close: pd.Series) -> pd.Series:
    """dsh_095_drawdown_path_fractal_dimension_63d"""
    # Simplified Hall-Wood estimator proxy
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    diff = dd.diff().abs()
    return _safe_div(np.log(diff.rolling(63).sum()), np.log(63))


# 106-125: Regression residuals and erraticism

def dsh_106_drawdown_max_residual_252d(close: pd.Series) -> pd.Series:
    """dsh_106_drawdown_max_residual_252d feature"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    def _max_res(y):
        x = np.arange(len(y))
        res = linregress(x, y)
        y_fit = res.intercept + res.slope * x
        return np.max(np.abs(y - y_fit))
    return dd.rolling(252).apply(_max_res, raw=True)

def dsh_107_drawdown_residual_skew_252d(close: pd.Series) -> pd.Series:
    """dsh_107_drawdown_residual_skew_252d"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    def _res_skew(y):
        x = np.arange(len(y))
        res = linregress(x, y)
        y_fit = res.intercept + res.slope * x
        err = y - y_fit
        return pd.Series(err).skew()
    return dd.rolling(252).apply(_res_skew, raw=True)

def dsh_108_drawdown_slope_stability_63d(close: pd.Series) -> pd.Series:
    """dsh_108_drawdown_slope_stability_63d"""
    # R-squared of the slope itself (is the decline accelerating steadily?)
    slopes = _rolling_slope((close - _rolling_max(close, 21)) / _rolling_max(close, 21), 21)
    return _rolling_rsq(slopes, 42)

def dsh_109_drawdown_break_of_slope_score_63d(close: pd.Series) -> pd.Series:
    """dsh_109_drawdown_break_of_slope_score_63d"""
    # Difference in slope between last 10 days and prior 50 days
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _break(y):
        s1 = linregress(np.arange(50), y[:50]).slope
        s2 = linregress(np.arange(13), y[53:]).slope
        return s2 - s1
    return dd.rolling(63).apply(_break, raw=True)

def dsh_110_drawdown_autocorrelation_lag_1_63d(close: pd.Series) -> pd.Series:
    """dsh_110_drawdown_autocorrelation_lag_1_63d"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return dd.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)


# 126-140: Multi-Horizon Slope Composites

def dsh_126_drawdown_slope_avg_21_63_252(close: pd.Series) -> pd.Series:
    """dsh_126_drawdown_slope_avg_21_63_252 feature"""
    s21 = _rolling_slope((close - _rolling_max(close, 21)) / _rolling_max(close, 21), 21)
    s63 = _rolling_slope((close - _rolling_max(close, 63)) / _rolling_max(close, 63), 63)
    s252 = _rolling_slope((close - _rolling_max(close, 252)) / _rolling_max(close, 252), 252)
    return (s21 + s63 + s252) / 3.0

def dsh_127_drawdown_slope_ratio_21_to_252(close: pd.Series) -> pd.Series:
    """dsh_127_drawdown_slope_ratio_21_to_252"""
    s21 = _rolling_slope((close - _rolling_max(close, 21)) / _rolling_max(close, 21), 21)
    s252 = _rolling_slope((close - _rolling_max(close, 252)) / _rolling_max(close, 252), 252)
    return _safe_div(s21, s252)

def dsh_128_drawdown_acceleration_index_63d(close: pd.Series) -> pd.Series:
    """dsh_128_drawdown_acceleration_index_63d"""
    # Ratio of current slope to 63-day average slope
    s = _rolling_slope((close - _rolling_max(close, 21)) / _rolling_max(close, 21), 21)
    return _safe_div(s, s.rolling(63).mean())


# 141-150: Volume/Fundamental Interaction Shapes

def dsh_141_drawdown_volume_weighted_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dsh_141_drawdown_volume_weighted_slope_63d feature"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    v_norm = _safe_div(volume, volume.rolling(63).mean())
    return _rolling_slope(dd * v_norm, 63)

def dsh_142_mktcap_drawdown_slope_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dsh_142_mktcap_drawdown_slope_63d"""
    mc = close * sharesbas
    h = _rolling_max(mc, 63)
    dd = (mc - h) / h
    return _rolling_slope(dd, 63)

def dsh_143_ev_revenue_drawdown_slope_63d(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """dsh_143_ev_revenue_drawdown_slope_63d"""
    ev = (close * sharesbas) + debt - cashnequiv
    ratio = ev / revenue
    h = ratio.expanding().max()
    dd = (ratio - h) / h
    return _rolling_slope(dd, 63)

def dsh_144_drawdown_convexity_multi_window_sum(close: pd.Series) -> pd.Series:
    """dsh_144_drawdown_convexity_multi_window_sum"""
    # Sum of convexity scores across 21, 63, 126, 252 windows
    def _conv(w):
        h = _rolling_max(close, w)
        dd = (close - h) / h
        area = dd.rolling(w).sum().abs()
        max_dd = dd.rolling(w).min().abs()
        return _safe_div(area, 0.5 * max_dd * w)
    return _conv(21) + _conv(63) + _conv(126) + _conv(252)

def dsh_145_drawdown_linear_drift_63d(close: pd.Series) -> pd.Series:
    """dsh_145_drawdown_linear_drift_63d"""
    # Intercept of drawdown path regression
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _int(y):
        x = np.arange(len(y))
        return linregress(x, y).intercept
    return dd.rolling(63).apply(_int, raw=True)

def dsh_146_drawdown_terminal_slope_10d(close: pd.Series) -> pd.Series:
    """dsh_146_drawdown_terminal_slope_10d"""
    # Slope of only the last 10 days of the drawdown
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return _rolling_slope(dd, 10)

def dsh_147_drawdown_hump_score_63d(close: pd.Series) -> pd.Series:
    """dsh_147_drawdown_hump_score_63d"""
    # Measure of how much the middle of the path is above/below the linear line
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _hump(y):
        lin = np.linspace(y[0], y[-1], len(y))
        return np.mean(y - lin)
    return dd.rolling(63).apply(_hump, raw=True)

def dsh_148_drawdown_step_verticality_63d(close: pd.Series) -> pd.Series:
    """dsh_148_drawdown_step_verticality_63d"""
    # Average slope of 'vertical' legs in a step-down pattern
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    diff = dd.diff()
    vertical = diff.where(diff < diff.rolling(63).mean() - 1*diff.rolling(63).std())
    return vertical.rolling(63).mean()

def dsh_149_drawdown_parabolic_acceleration_63d(close: pd.Series) -> pd.Series:
    """dsh_149_drawdown_parabolic_acceleration_63d"""
    # Coeff of x^2 in polyfit (same as curvature but renamed for volume)
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _para(y):
        x = np.arange(len(y))
        return np.polyfit(x, y, 2)[0]
    return dd.rolling(63).apply(_para, raw=True)

def dsh_150_drawdown_shape_complexity_index(close: pd.Series) -> pd.Series:
    """dsh_150_drawdown_shape_complexity_index"""
    # Composite: Std Err * (1 - Rsq) * Jaggedness
    se = dsh_013_drawdown_std_err_63d(close)
    r2 = dsh_011_drawdown_rsq_63d(close)
    jag = dsh_071_drawdown_jaggedness_21d(close)
    return se * (1.0 - r2) * jag

def dsh_100_variation_0(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_076_drawdown_return_skewness_252d"""
    base_feat = dsh_076_drawdown_return_skewness_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_101_variation_1(close: pd.Series) -> pd.Series:
    """rank variation of dsh_077_drawdown_return_kurtosis_252d"""
    base_feat = dsh_077_drawdown_return_kurtosis_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_102_variation_2(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_078_drawdown_vol_ratio_early_vs_late_63d"""
    base_feat = dsh_078_drawdown_vol_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_103_variation_3(close: pd.Series) -> pd.Series:
    """rank variation of dsh_079_drawdown_velocity_inflection_63d"""
    base_feat = dsh_079_drawdown_velocity_inflection_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_104_variation_4(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_080_drawdown_tail_to_body_ratio_63d"""
    base_feat = dsh_080_drawdown_tail_to_body_ratio_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_105_variation_5(close: pd.Series) -> pd.Series:
    """rank variation of dsh_092_drawdown_vertical_drop_score_63d"""
    base_feat = dsh_092_drawdown_vertical_drop_score_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_106_variation_6(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_093_drawdown_bounce_fading_score_63d"""
    base_feat = dsh_093_drawdown_bounce_fading_score_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_107_variation_7(close: pd.Series) -> pd.Series:
    """rank variation of dsh_094_drawdown_log_linear_residual_std_63d"""
    base_feat = dsh_094_drawdown_log_linear_residual_std_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_108_variation_8(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_095_drawdown_path_fractal_dimension_63d"""
    base_feat = dsh_095_drawdown_path_fractal_dimension_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_109_variation_9(close: pd.Series) -> pd.Series:
    """rank variation of dsh_107_drawdown_residual_skew_252d"""
    base_feat = dsh_107_drawdown_residual_skew_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_110_variation_10(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_076_drawdown_return_skewness_252d"""
    base_feat = dsh_076_drawdown_return_skewness_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_111_variation_11(close: pd.Series) -> pd.Series:
    """rank variation of dsh_077_drawdown_return_kurtosis_252d"""
    base_feat = dsh_077_drawdown_return_kurtosis_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_112_variation_12(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_078_drawdown_vol_ratio_early_vs_late_63d"""
    base_feat = dsh_078_drawdown_vol_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_113_variation_13(close: pd.Series) -> pd.Series:
    """rank variation of dsh_079_drawdown_velocity_inflection_63d"""
    base_feat = dsh_079_drawdown_velocity_inflection_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_114_variation_14(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_080_drawdown_tail_to_body_ratio_63d"""
    base_feat = dsh_080_drawdown_tail_to_body_ratio_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_115_variation_15(close: pd.Series) -> pd.Series:
    """rank variation of dsh_092_drawdown_vertical_drop_score_63d"""
    base_feat = dsh_092_drawdown_vertical_drop_score_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_116_variation_16(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_093_drawdown_bounce_fading_score_63d"""
    base_feat = dsh_093_drawdown_bounce_fading_score_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_117_variation_17(close: pd.Series) -> pd.Series:
    """rank variation of dsh_094_drawdown_log_linear_residual_std_63d"""
    base_feat = dsh_094_drawdown_log_linear_residual_std_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_118_variation_18(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_095_drawdown_path_fractal_dimension_63d"""
    base_feat = dsh_095_drawdown_path_fractal_dimension_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_119_variation_19(close: pd.Series) -> pd.Series:
    """rank variation of dsh_107_drawdown_residual_skew_252d"""
    base_feat = dsh_107_drawdown_residual_skew_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_120_variation_20(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_076_drawdown_return_skewness_252d"""
    base_feat = dsh_076_drawdown_return_skewness_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_121_variation_21(close: pd.Series) -> pd.Series:
    """rank variation of dsh_077_drawdown_return_kurtosis_252d"""
    base_feat = dsh_077_drawdown_return_kurtosis_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_122_variation_22(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_078_drawdown_vol_ratio_early_vs_late_63d"""
    base_feat = dsh_078_drawdown_vol_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_123_variation_23(close: pd.Series) -> pd.Series:
    """rank variation of dsh_079_drawdown_velocity_inflection_63d"""
    base_feat = dsh_079_drawdown_velocity_inflection_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_124_variation_24(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_080_drawdown_tail_to_body_ratio_63d"""
    base_feat = dsh_080_drawdown_tail_to_body_ratio_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_125_variation_25(close: pd.Series) -> pd.Series:
    """rank variation of dsh_092_drawdown_vertical_drop_score_63d"""
    base_feat = dsh_092_drawdown_vertical_drop_score_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_126_variation_26(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_093_drawdown_bounce_fading_score_63d"""
    base_feat = dsh_093_drawdown_bounce_fading_score_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_127_variation_27(close: pd.Series) -> pd.Series:
    """rank variation of dsh_094_drawdown_log_linear_residual_std_63d"""
    base_feat = dsh_094_drawdown_log_linear_residual_std_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_128_variation_28(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_095_drawdown_path_fractal_dimension_63d"""
    base_feat = dsh_095_drawdown_path_fractal_dimension_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_129_variation_29(close: pd.Series) -> pd.Series:
    """rank variation of dsh_107_drawdown_residual_skew_252d"""
    base_feat = dsh_107_drawdown_residual_skew_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_130_variation_30(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_076_drawdown_return_skewness_252d"""
    base_feat = dsh_076_drawdown_return_skewness_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_131_variation_31(close: pd.Series) -> pd.Series:
    """rank variation of dsh_077_drawdown_return_kurtosis_252d"""
    base_feat = dsh_077_drawdown_return_kurtosis_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_132_variation_32(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_078_drawdown_vol_ratio_early_vs_late_63d"""
    base_feat = dsh_078_drawdown_vol_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_133_variation_33(close: pd.Series) -> pd.Series:
    """rank variation of dsh_079_drawdown_velocity_inflection_63d"""
    base_feat = dsh_079_drawdown_velocity_inflection_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_134_variation_34(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_080_drawdown_tail_to_body_ratio_63d"""
    base_feat = dsh_080_drawdown_tail_to_body_ratio_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_135_variation_35(close: pd.Series) -> pd.Series:
    """rank variation of dsh_092_drawdown_vertical_drop_score_63d"""
    base_feat = dsh_092_drawdown_vertical_drop_score_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_136_variation_36(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_093_drawdown_bounce_fading_score_63d"""
    base_feat = dsh_093_drawdown_bounce_fading_score_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_137_variation_37(close: pd.Series) -> pd.Series:
    """rank variation of dsh_094_drawdown_log_linear_residual_std_63d"""
    base_feat = dsh_094_drawdown_log_linear_residual_std_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_138_variation_38(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_095_drawdown_path_fractal_dimension_63d"""
    base_feat = dsh_095_drawdown_path_fractal_dimension_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_139_variation_39(close: pd.Series) -> pd.Series:
    """rank variation of dsh_107_drawdown_residual_skew_252d"""
    base_feat = dsh_107_drawdown_residual_skew_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_140_variation_40(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_076_drawdown_return_skewness_252d"""
    base_feat = dsh_076_drawdown_return_skewness_252d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_141_variation_41(close: pd.Series) -> pd.Series:
    """rank variation of dsh_077_drawdown_return_kurtosis_252d"""
    base_feat = dsh_077_drawdown_return_kurtosis_252d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_142_variation_42(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_078_drawdown_vol_ratio_early_vs_late_63d"""
    base_feat = dsh_078_drawdown_vol_ratio_early_vs_late_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_143_variation_43(close: pd.Series) -> pd.Series:
    """rank variation of dsh_079_drawdown_velocity_inflection_63d"""
    base_feat = dsh_079_drawdown_velocity_inflection_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_144_variation_44(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_080_drawdown_tail_to_body_ratio_63d"""
    base_feat = dsh_080_drawdown_tail_to_body_ratio_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_145_variation_45(close: pd.Series) -> pd.Series:
    """rank variation of dsh_092_drawdown_vertical_drop_score_63d"""
    base_feat = dsh_092_drawdown_vertical_drop_score_63d(close)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def dsh_146_variation_46(close: pd.Series) -> pd.Series:
    """zscore variation of dsh_093_drawdown_bounce_fading_score_63d"""
    base_feat = dsh_093_drawdown_bounce_fading_score_63d(close)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V03_REGISTRY = {
    "dsh_076_drawdown_return_skewness_252d": {"inputs": ["close"], "func": dsh_076_drawdown_return_skewness_252d},
    "dsh_077_drawdown_return_kurtosis_252d": {"inputs": ["close"], "func": dsh_077_drawdown_return_kurtosis_252d},
    "dsh_078_drawdown_vol_ratio_early_vs_late_63d": {"inputs": ["close"], "func": dsh_078_drawdown_vol_ratio_early_vs_late_63d},
    "dsh_079_drawdown_velocity_inflection_63d": {"inputs": ["close"], "func": dsh_079_drawdown_velocity_inflection_63d},
    "dsh_080_drawdown_tail_to_body_ratio_63d": {"inputs": ["close"], "func": dsh_080_drawdown_tail_to_body_ratio_63d},
    "dsh_091_drawdown_rounded_top_score_63d": {"inputs": ["close"], "func": dsh_091_drawdown_rounded_top_score_63d},
    "dsh_092_drawdown_vertical_drop_score_63d": {"inputs": ["close"], "func": dsh_092_drawdown_vertical_drop_score_63d},
    "dsh_093_drawdown_bounce_fading_score_63d": {"inputs": ["close"], "func": dsh_093_drawdown_bounce_fading_score_63d},
    "dsh_094_drawdown_log_linear_residual_std_63d": {"inputs": ["close"], "func": dsh_094_drawdown_log_linear_residual_std_63d},
    "dsh_095_drawdown_path_fractal_dimension_63d": {"inputs": ["close"], "func": dsh_095_drawdown_path_fractal_dimension_63d},
    "dsh_106_drawdown_max_residual_252d": {"inputs": ["close"], "func": dsh_106_drawdown_max_residual_252d},
    "dsh_107_drawdown_residual_skew_252d": {"inputs": ["close"], "func": dsh_107_drawdown_residual_skew_252d},
    "dsh_108_drawdown_slope_stability_63d": {"inputs": ["close"], "func": dsh_108_drawdown_slope_stability_63d},
    "dsh_109_drawdown_break_of_slope_score_63d": {"inputs": ["close"], "func": dsh_109_drawdown_break_of_slope_score_63d},
    "dsh_110_drawdown_autocorrelation_lag_1_63d": {"inputs": ["close"], "func": dsh_110_drawdown_autocorrelation_lag_1_63d},
    "dsh_126_drawdown_slope_avg_21_63_252": {"inputs": ["close"], "func": dsh_126_drawdown_slope_avg_21_63_252},
    "dsh_127_drawdown_slope_ratio_21_to_252": {"inputs": ["close"], "func": dsh_127_drawdown_slope_ratio_21_to_252},
    "dsh_128_drawdown_acceleration_index_63d": {"inputs": ["close"], "func": dsh_128_drawdown_acceleration_index_63d},
    "dsh_141_drawdown_volume_weighted_slope_63d": {"inputs": ["close", "volume"], "func": dsh_141_drawdown_volume_weighted_slope_63d},
    "dsh_142_mktcap_drawdown_slope_63d": {"inputs": ["close", "sharesbas"], "func": dsh_142_mktcap_drawdown_slope_63d},
    "dsh_143_ev_revenue_drawdown_slope_63d": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": dsh_143_ev_revenue_drawdown_slope_63d},
    "dsh_144_drawdown_convexity_multi_window_sum": {"inputs": ["close"], "func": dsh_144_drawdown_convexity_multi_window_sum},
    "dsh_145_drawdown_linear_drift_63d": {"inputs": ["close"], "func": dsh_145_drawdown_linear_drift_63d},
    "dsh_146_drawdown_terminal_slope_10d": {"inputs": ["close"], "func": dsh_146_drawdown_terminal_slope_10d},
    "dsh_147_drawdown_hump_score_63d": {"inputs": ["close"], "func": dsh_147_drawdown_hump_score_63d},
    "dsh_148_drawdown_step_verticality_63d": {"inputs": ["close"], "func": dsh_148_drawdown_step_verticality_63d},
    "dsh_149_drawdown_parabolic_acceleration_63d": {"inputs": ["close"], "func": dsh_149_drawdown_parabolic_acceleration_63d},
    "dsh_150_drawdown_shape_complexity_index": {"inputs": ["close"], "func": dsh_150_drawdown_shape_complexity_index},
    "dsh_100_variation_0": {"inputs": ["close"], "func": dsh_100_variation_0},
    "dsh_101_variation_1": {"inputs": ["close"], "func": dsh_101_variation_1},
    "dsh_102_variation_2": {"inputs": ["close"], "func": dsh_102_variation_2},
    "dsh_103_variation_3": {"inputs": ["close"], "func": dsh_103_variation_3},
    "dsh_104_variation_4": {"inputs": ["close"], "func": dsh_104_variation_4},
    "dsh_105_variation_5": {"inputs": ["close"], "func": dsh_105_variation_5},
    "dsh_106_variation_6": {"inputs": ["close"], "func": dsh_106_variation_6},
    "dsh_107_variation_7": {"inputs": ["close"], "func": dsh_107_variation_7},
    "dsh_108_variation_8": {"inputs": ["close"], "func": dsh_108_variation_8},
    "dsh_109_variation_9": {"inputs": ["close"], "func": dsh_109_variation_9},
    "dsh_110_variation_10": {"inputs": ["close"], "func": dsh_110_variation_10},
    "dsh_111_variation_11": {"inputs": ["close"], "func": dsh_111_variation_11},
    "dsh_112_variation_12": {"inputs": ["close"], "func": dsh_112_variation_12},
    "dsh_113_variation_13": {"inputs": ["close"], "func": dsh_113_variation_13},
    "dsh_114_variation_14": {"inputs": ["close"], "func": dsh_114_variation_14},
    "dsh_115_variation_15": {"inputs": ["close"], "func": dsh_115_variation_15},
    "dsh_116_variation_16": {"inputs": ["close"], "func": dsh_116_variation_16},
    "dsh_117_variation_17": {"inputs": ["close"], "func": dsh_117_variation_17},
    "dsh_118_variation_18": {"inputs": ["close"], "func": dsh_118_variation_18},
    "dsh_119_variation_19": {"inputs": ["close"], "func": dsh_119_variation_19},
    "dsh_120_variation_20": {"inputs": ["close"], "func": dsh_120_variation_20},
    "dsh_121_variation_21": {"inputs": ["close"], "func": dsh_121_variation_21},
    "dsh_122_variation_22": {"inputs": ["close"], "func": dsh_122_variation_22},
    "dsh_123_variation_23": {"inputs": ["close"], "func": dsh_123_variation_23},
    "dsh_124_variation_24": {"inputs": ["close"], "func": dsh_124_variation_24},
    "dsh_125_variation_25": {"inputs": ["close"], "func": dsh_125_variation_25},
    "dsh_126_variation_26": {"inputs": ["close"], "func": dsh_126_variation_26},
    "dsh_127_variation_27": {"inputs": ["close"], "func": dsh_127_variation_27},
    "dsh_128_variation_28": {"inputs": ["close"], "func": dsh_128_variation_28},
    "dsh_129_variation_29": {"inputs": ["close"], "func": dsh_129_variation_29},
    "dsh_130_variation_30": {"inputs": ["close"], "func": dsh_130_variation_30},
    "dsh_131_variation_31": {"inputs": ["close"], "func": dsh_131_variation_31},
    "dsh_132_variation_32": {"inputs": ["close"], "func": dsh_132_variation_32},
    "dsh_133_variation_33": {"inputs": ["close"], "func": dsh_133_variation_33},
    "dsh_134_variation_34": {"inputs": ["close"], "func": dsh_134_variation_34},
    "dsh_135_variation_35": {"inputs": ["close"], "func": dsh_135_variation_35},
    "dsh_136_variation_36": {"inputs": ["close"], "func": dsh_136_variation_36},
    "dsh_137_variation_37": {"inputs": ["close"], "func": dsh_137_variation_37},
    "dsh_138_variation_38": {"inputs": ["close"], "func": dsh_138_variation_38},
    "dsh_139_variation_39": {"inputs": ["close"], "func": dsh_139_variation_39},
    "dsh_140_variation_40": {"inputs": ["close"], "func": dsh_140_variation_40},
    "dsh_141_variation_41": {"inputs": ["close"], "func": dsh_141_variation_41},
    "dsh_142_variation_42": {"inputs": ["close"], "func": dsh_142_variation_42},
    "dsh_143_variation_43": {"inputs": ["close"], "func": dsh_143_variation_43},
    "dsh_144_variation_44": {"inputs": ["close"], "func": dsh_144_variation_44},
    "dsh_145_variation_45": {"inputs": ["close"], "func": dsh_145_variation_45},
    "dsh_146_variation_46": {"inputs": ["close"], "func": dsh_146_variation_46},
}
