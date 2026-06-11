"""advance_speed d3 features 076_150 — 3rd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff().diff() so the output is the third bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))

def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, 'index') else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)

def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f02_advs_076_consecutive_days_close_above_sma21_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    above = (close > sma).astype(int)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f02_advs_077_consecutive_days_close_above_sma63_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    above = (close > sma).astype(int)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f02_advs_078_consecutive_days_close_above_sma252_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above = (close > sma).astype(int)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float).diff().diff().diff()

def f02_advs_079_fraction_of_252d_above_sma21_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = (close > sma).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_080_fraction_of_252d_above_sma63_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    flag = (close > sma).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_081_fraction_of_252d_above_sma252_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (close > sma).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_082_uptrend_continuity_score_252d_d3(close: pd.Series) -> pd.Series:
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    score = ((close > s21) & (s21 > s63) & (s63 > s252)).astype(float)
    return score.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_083_first_cross_above_sma252_thrust_21d_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    cross = (close > sma) & (close.shift(1) <= sma.shift(1))
    ext = _safe_div(close, sma) - 1.0
    cross_val = ext.where(cross, np.nan)
    return cross_val.rolling(MDAYS, min_periods=WDAYS).max().diff().diff().diff()

def f02_advs_084_ma_extension_acceleration_21d_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    ext = _safe_div(close, sma) - 1.0
    return _rolling_slope(ext, MDAYS).diff().diff().diff()

def f02_advs_085_ma_extension_acceleration_63d_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    ext = _safe_div(close, sma) - 1.0
    return _rolling_slope(ext, QDAYS).diff().diff().diff()

def f02_advs_086_ma_extension_acceleration_252d_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    ext = _safe_div(close, sma) - 1.0
    return _rolling_slope(ext, YDAYS).diff().diff().diff()

def f02_advs_087_days_since_sma21_last_cross_below_d3(close: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    cross_dn = (close < sma) & (close.shift(1) >= sma.shift(1))
    cum = cross_dn.cumsum()
    idx_last = pd.Series(np.arange(len(close)), index=close.index).where(cross_dn).ffill()
    pos = pd.Series(np.arange(len(close)), index=close.index)
    return (pos - idx_last).where(cum > 0, np.nan).diff().diff().diff()

def f02_advs_088_count_log_gap_up_gt_1pct_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return (g > 0.01).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f02_advs_089_count_log_gap_down_lt_neg1pct_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return (g < -0.01).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f02_advs_090_mean_log_gap_up_magnitude_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.where(g > 0).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f02_advs_091_mean_log_gap_down_magnitude_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.where(g < 0).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f02_advs_092_cumulative_log_gap_up_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.clip(lower=0).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f02_advs_093_cumulative_log_gap_down_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.clip(upper=0).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f02_advs_094_share_of_63d_advance_from_gaps_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    cum_gap = g.rolling(QDAYS, min_periods=MDAYS).sum()
    tot = _safe_log(close).diff(QDAYS)
    return _safe_div(cum_gap, tot).diff().diff().diff()

def f02_advs_095_count_runaway_gap_up_252d_d3(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    gap_up = open_ > close.shift(1)
    above = close > high.shift(1)
    return (gap_up & above).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f02_advs_096_count_exhaustion_gap_up_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    gap_up = open_ > close.shift(1)
    bear_body = close < open_
    return (gap_up & bear_body).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f02_advs_097_max_log_gap_up_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f02_advs_098_overnight_log_return_mean_21d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f02_advs_099_overnight_log_return_zscore_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return _rolling_zscore(g, YDAYS).diff().diff().diff()

def f02_advs_100_overnight_vs_intraday_log_corr_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    overnight = _safe_log(open_) - _safe_log(close.shift(1))
    intraday = _safe_log(close) - _safe_log(open_)
    return overnight.rolling(QDAYS, min_periods=MDAYS).corr(intraday).diff().diff().diff()

def f02_advs_101_fraction_positive_overnight_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return (g > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_102_overnight_return_kurt_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.rolling(YDAYS, min_periods=QDAYS).kurt().diff().diff().diff()

def f02_advs_103_log_return_5d_pct_rank_in_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff(WDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff().diff().diff()

def f02_advs_104_log_return_10d_pct_rank_in_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff(10)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff().diff().diff()

def f02_advs_105_log_return_21d_pct_rank_in_1260d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff(MDAYS)
    return r.rolling(1260, min_periods=YDAYS).rank(pct=True).diff().diff().diff()

def f02_advs_106_vertical_move_zscore_5d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    r5 = _safe_log(close).diff(WDAYS)
    return _safe_div(r5, sd * np.sqrt(WDAYS)).diff().diff().diff()

def f02_advs_107_vertical_move_zscore_10d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    r10 = _safe_log(close).diff(10)
    return _safe_div(r10, sd * np.sqrt(10)).diff().diff().diff()

def f02_advs_108_vertical_move_zscore_21d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    r21 = _safe_log(close).diff(MDAYS)
    return _safe_div(r21, sd * np.sqrt(MDAYS)).diff().diff().diff()

def f02_advs_109_vertical_move_atr_units_5d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    return ((close - close.shift(WDAYS)) / atr.replace(0, np.nan)).diff().diff().diff()

def f02_advs_110_vertical_move_atr_units_21d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    return ((close - close.shift(MDAYS)) / atr.replace(0, np.nan)).diff().diff().diff()

def f02_advs_111_count_5d_vertical_z_gt_2_252d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z5 = _safe_div(_safe_log(close).diff(WDAYS), sd * np.sqrt(WDAYS))
    return (z5 > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f02_advs_112_count_21d_vertical_z_gt_2_252d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z21 = _safe_div(_safe_log(close).diff(MDAYS), sd * np.sqrt(MDAYS))
    return (z21 > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f02_advs_113_max_5d_vertical_z_252d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z5 = _safe_div(_safe_log(close).diff(WDAYS), sd * np.sqrt(WDAYS))
    return z5.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f02_advs_114_max_21d_vertical_z_252d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z21 = _safe_div(_safe_log(close).diff(MDAYS), sd * np.sqrt(MDAYS))
    return z21.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f02_advs_115_proximity_to_max_5d_z_252d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z5 = _safe_div(_safe_log(close).diff(WDAYS), sd * np.sqrt(WDAYS))
    mx = z5.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(z5, mx).diff().diff().diff()

def f02_advs_116_proximity_to_max_21d_z_252d_d3(close: pd.Series) -> pd.Series:
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z21 = _safe_div(_safe_log(close).diff(MDAYS), sd * np.sqrt(MDAYS))
    mx = z21.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(z21, mx).diff().diff().diff()

def f02_advs_117_pct_of_252d_within_top_decile_5d_returns_d3(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(WDAYS)
    rk = r5.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (rk >= 0.9).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_118_price_to_252d_low_ratio_minus_1_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close, rmin) - 1.0).diff().diff().diff()

def f02_advs_119_price_to_63d_low_ratio_minus_1_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    return (_safe_div(close, rmin) - 1.0).diff().diff().diff()

def f02_advs_120_price_to_1260d_low_ratio_minus_1_d3(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return (_safe_div(close, rmin) - 1.0).diff().diff().diff()

def f02_advs_121_log_return_first_third_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp.shift(YDAYS - 252 // 3) - lp.shift(YDAYS)).diff().diff().diff()

def f02_advs_122_log_return_middle_third_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp.shift(YDAYS - 2 * (252 // 3)) - lp.shift(YDAYS - 252 // 3)).diff().diff().diff()

def f02_advs_123_log_return_last_third_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp - lp.shift(YDAYS - 2 * (252 // 3))).diff().diff().diff()

def f02_advs_124_ratio_last_third_to_first_third_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    third = 252 // 3
    last = lp - lp.shift(YDAYS - 2 * third)
    first = lp.shift(YDAYS - third) - lp.shift(YDAYS)
    return _safe_div(last, first).diff().diff().diff()

def f02_advs_125_ratio_last_third_to_middle_third_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    third = 252 // 3
    last = lp - lp.shift(YDAYS - 2 * third)
    mid = lp.shift(YDAYS - 2 * third) - lp.shift(YDAYS - third)
    return _safe_div(last, mid).diff().diff().diff()

def f02_advs_126_days_to_traverse_50pct_252d_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng

    def _days(w):
        if np.isnan(w).any():
            return np.nan
        idx = np.where(w >= 0.5)[0]
        if len(idx) == 0:
            return float(len(w))
        return float(len(w) - 1 - idx[0])
    return pos.rolling(YDAYS, min_periods=QDAYS).apply(_days, raw=True).diff().diff().diff()

def f02_advs_127_days_to_traverse_75pct_252d_range_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng

    def _days(w):
        if np.isnan(w).any():
            return np.nan
        idx = np.where(w >= 0.75)[0]
        if len(idx) == 0:
            return float(len(w))
        return float(len(w) - 1 - idx[0])
    return pos.rolling(YDAYS, min_periods=QDAYS).apply(_days, raw=True).diff().diff().diff()

def f02_advs_128_fraction_252d_log_gain_in_last_5d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r5 = lp - lp.shift(WDAYS)
    r252 = lp - lp.shift(YDAYS)
    return _safe_div(r5, r252).diff().diff().diff()

def f02_advs_129_fraction_252d_log_gain_in_last_21d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r21 = lp - lp.shift(MDAYS)
    r252 = lp - lp.shift(YDAYS)
    return _safe_div(r21, r252).diff().diff().diff()

def f02_advs_130_fraction_252d_log_gain_in_last_63d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    r63 = lp - lp.shift(QDAYS)
    r252 = lp - lp.shift(YDAYS)
    return _safe_div(r63, r252).diff().diff().diff()

def f02_advs_131_last_quintile_speed_zscore_in_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    last_q = r.rolling(50, min_periods=10).mean()
    return _rolling_zscore(last_q, YDAYS).diff().diff().diff()

def f02_advs_132_first_quintile_speed_zscore_in_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    first_q_mean = r.rolling(50, min_periods=10).mean().shift(YDAYS - 50)
    return _rolling_zscore(first_q_mean, YDAYS).diff().diff().diff()

def f02_advs_133_non_decreasing_close_run_max_252d_d3(close: pd.Series) -> pd.Series:
    nd = (close >= close.shift(1)).astype(int)
    grp = (nd == 0).cumsum()
    streak = nd.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f02_advs_134_fraction_higher_highs_252d_d3(high: pd.Series) -> pd.Series:
    hh = (high > high.shift(1)).astype(float)
    return hh.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_135_fraction_higher_lows_252d_d3(low: pd.Series) -> pd.Series:
    hl = (low > low.shift(1)).astype(float)
    return hl.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_136_higher_hi_hi_lo_lo_streak_max_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    flag = ((high > high.shift(1)) & (low > low.shift(1))).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f02_advs_137_count_distinct_uptrend_legs_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    new_max = (close >= rmax).astype(float)
    return new_max.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f02_advs_138_mean_uptrend_leg_log_size_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    rmax_lp = lp.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (lp >= rmax_lp).astype(int)

    def _mean_leg(w):
        if np.isnan(w).any() or len(w) < 2:
            return np.nan
        peaks = np.where(w > 0.5)[0]
        if len(peaks) < 2:
            return np.nan
        return float(np.diff(peaks).mean())
    return is_peak.rolling(YDAYS, min_periods=QDAYS).apply(_mean_leg, raw=True).diff().diff().diff()

def f02_advs_139_max_uptrend_leg_log_size_252d_d3(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    rmax_lp = lp.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (lp >= rmax_lp).astype(int)

    def _max_gap(w):
        if np.isnan(w).any():
            return np.nan
        peaks = np.where(w > 0.5)[0]
        if len(peaks) < 2:
            return np.nan
        return float(np.diff(peaks).max())
    return is_peak.rolling(YDAYS, min_periods=QDAYS).apply(_max_gap, raw=True).diff().diff().diff()

def f02_advs_140_mean_pullback_depth_during_advance_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return dd.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_141_max_pullback_depth_during_advance_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return dd.rolling(YDAYS, min_periods=QDAYS).min().diff().diff().diff()

def f02_advs_142_count_pullbacks_gt_5pct_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return (dd < -0.05).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f02_advs_143_mean_pullback_duration_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    flag = (dd < 0).astype(int)

    def _mean_run(w):
        if np.isnan(w).any():
            return np.nan
        runs = []
        c = 0
        for v in w:
            if v > 0.5:
                c += 1
            else:
                if c > 0:
                    runs.append(c)
                c = 0
        if c > 0:
            runs.append(c)
        return float(np.mean(runs)) if runs else 0.0
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_mean_run, raw=True).diff().diff().diff()

def f02_advs_144_straight_line_advance_r2_252d_d3(close: pd.Series) -> pd.Series:

    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss_tot
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True).diff().diff().diff()

def f02_advs_145_cumulative_drawdown_share_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    return dd.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f02_advs_146_clean_advance_index_252d_d3(close: pd.Series) -> pd.Series:

    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss_tot
    r2 = close.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_share = (_safe_div(close, rmax) - 1.0).abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(r2, 1.0 + dd_share).diff().diff().diff()

def f02_advs_147_max_uninterrupted_advance_streak_252d_d3(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    touch = (close >= rmax).astype(int)
    grp = (touch == 0).cumsum()
    streak = touch.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f02_advs_148_count_lower_lows_during_252d_uptrend_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    ll = low < low.shift(1)
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    in_uptrend = close > sma
    return (ll & in_uptrend).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f02_advs_149_velocity_consistency_score_252d_d3(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(m, sd).diff().diff().diff()

def f02_advs_150_terminal_advance_completeness_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    r21 = _safe_log(close).diff(MDAYS)
    z = _rolling_zscore(r21, YDAYS)
    return (pos * z).diff().diff().diff()
ADVANCE_SPEED_D3_REGISTRY_076_150 = {'f02_advs_076_consecutive_days_close_above_sma21_d3': {'inputs': ['close'], 'func': f02_advs_076_consecutive_days_close_above_sma21_d3}, 'f02_advs_077_consecutive_days_close_above_sma63_d3': {'inputs': ['close'], 'func': f02_advs_077_consecutive_days_close_above_sma63_d3}, 'f02_advs_078_consecutive_days_close_above_sma252_d3': {'inputs': ['close'], 'func': f02_advs_078_consecutive_days_close_above_sma252_d3}, 'f02_advs_079_fraction_of_252d_above_sma21_d3': {'inputs': ['close'], 'func': f02_advs_079_fraction_of_252d_above_sma21_d3}, 'f02_advs_080_fraction_of_252d_above_sma63_d3': {'inputs': ['close'], 'func': f02_advs_080_fraction_of_252d_above_sma63_d3}, 'f02_advs_081_fraction_of_252d_above_sma252_d3': {'inputs': ['close'], 'func': f02_advs_081_fraction_of_252d_above_sma252_d3}, 'f02_advs_082_uptrend_continuity_score_252d_d3': {'inputs': ['close'], 'func': f02_advs_082_uptrend_continuity_score_252d_d3}, 'f02_advs_083_first_cross_above_sma252_thrust_21d_d3': {'inputs': ['close'], 'func': f02_advs_083_first_cross_above_sma252_thrust_21d_d3}, 'f02_advs_084_ma_extension_acceleration_21d_d3': {'inputs': ['close'], 'func': f02_advs_084_ma_extension_acceleration_21d_d3}, 'f02_advs_085_ma_extension_acceleration_63d_d3': {'inputs': ['close'], 'func': f02_advs_085_ma_extension_acceleration_63d_d3}, 'f02_advs_086_ma_extension_acceleration_252d_d3': {'inputs': ['close'], 'func': f02_advs_086_ma_extension_acceleration_252d_d3}, 'f02_advs_087_days_since_sma21_last_cross_below_d3': {'inputs': ['close'], 'func': f02_advs_087_days_since_sma21_last_cross_below_d3}, 'f02_advs_088_count_log_gap_up_gt_1pct_63d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_088_count_log_gap_up_gt_1pct_63d_d3}, 'f02_advs_089_count_log_gap_down_lt_neg1pct_63d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_089_count_log_gap_down_lt_neg1pct_63d_d3}, 'f02_advs_090_mean_log_gap_up_magnitude_63d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_090_mean_log_gap_up_magnitude_63d_d3}, 'f02_advs_091_mean_log_gap_down_magnitude_63d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_091_mean_log_gap_down_magnitude_63d_d3}, 'f02_advs_092_cumulative_log_gap_up_63d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_092_cumulative_log_gap_up_63d_d3}, 'f02_advs_093_cumulative_log_gap_down_63d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_093_cumulative_log_gap_down_63d_d3}, 'f02_advs_094_share_of_63d_advance_from_gaps_d3': {'inputs': ['open', 'close'], 'func': f02_advs_094_share_of_63d_advance_from_gaps_d3}, 'f02_advs_095_count_runaway_gap_up_252d_d3': {'inputs': ['open', 'close', 'high'], 'func': f02_advs_095_count_runaway_gap_up_252d_d3}, 'f02_advs_096_count_exhaustion_gap_up_252d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_096_count_exhaustion_gap_up_252d_d3}, 'f02_advs_097_max_log_gap_up_252d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_097_max_log_gap_up_252d_d3}, 'f02_advs_098_overnight_log_return_mean_21d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_098_overnight_log_return_mean_21d_d3}, 'f02_advs_099_overnight_log_return_zscore_252d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_099_overnight_log_return_zscore_252d_d3}, 'f02_advs_100_overnight_vs_intraday_log_corr_63d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_100_overnight_vs_intraday_log_corr_63d_d3}, 'f02_advs_101_fraction_positive_overnight_252d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_101_fraction_positive_overnight_252d_d3}, 'f02_advs_102_overnight_return_kurt_252d_d3': {'inputs': ['open', 'close'], 'func': f02_advs_102_overnight_return_kurt_252d_d3}, 'f02_advs_103_log_return_5d_pct_rank_in_252d_d3': {'inputs': ['close'], 'func': f02_advs_103_log_return_5d_pct_rank_in_252d_d3}, 'f02_advs_104_log_return_10d_pct_rank_in_252d_d3': {'inputs': ['close'], 'func': f02_advs_104_log_return_10d_pct_rank_in_252d_d3}, 'f02_advs_105_log_return_21d_pct_rank_in_1260d_d3': {'inputs': ['close'], 'func': f02_advs_105_log_return_21d_pct_rank_in_1260d_d3}, 'f02_advs_106_vertical_move_zscore_5d_d3': {'inputs': ['close'], 'func': f02_advs_106_vertical_move_zscore_5d_d3}, 'f02_advs_107_vertical_move_zscore_10d_d3': {'inputs': ['close'], 'func': f02_advs_107_vertical_move_zscore_10d_d3}, 'f02_advs_108_vertical_move_zscore_21d_d3': {'inputs': ['close'], 'func': f02_advs_108_vertical_move_zscore_21d_d3}, 'f02_advs_109_vertical_move_atr_units_5d_d3': {'inputs': ['close', 'high', 'low'], 'func': f02_advs_109_vertical_move_atr_units_5d_d3}, 'f02_advs_110_vertical_move_atr_units_21d_d3': {'inputs': ['close', 'high', 'low'], 'func': f02_advs_110_vertical_move_atr_units_21d_d3}, 'f02_advs_111_count_5d_vertical_z_gt_2_252d_d3': {'inputs': ['close'], 'func': f02_advs_111_count_5d_vertical_z_gt_2_252d_d3}, 'f02_advs_112_count_21d_vertical_z_gt_2_252d_d3': {'inputs': ['close'], 'func': f02_advs_112_count_21d_vertical_z_gt_2_252d_d3}, 'f02_advs_113_max_5d_vertical_z_252d_d3': {'inputs': ['close'], 'func': f02_advs_113_max_5d_vertical_z_252d_d3}, 'f02_advs_114_max_21d_vertical_z_252d_d3': {'inputs': ['close'], 'func': f02_advs_114_max_21d_vertical_z_252d_d3}, 'f02_advs_115_proximity_to_max_5d_z_252d_d3': {'inputs': ['close'], 'func': f02_advs_115_proximity_to_max_5d_z_252d_d3}, 'f02_advs_116_proximity_to_max_21d_z_252d_d3': {'inputs': ['close'], 'func': f02_advs_116_proximity_to_max_21d_z_252d_d3}, 'f02_advs_117_pct_of_252d_within_top_decile_5d_returns_d3': {'inputs': ['close'], 'func': f02_advs_117_pct_of_252d_within_top_decile_5d_returns_d3}, 'f02_advs_118_price_to_252d_low_ratio_minus_1_d3': {'inputs': ['close', 'low'], 'func': f02_advs_118_price_to_252d_low_ratio_minus_1_d3}, 'f02_advs_119_price_to_63d_low_ratio_minus_1_d3': {'inputs': ['close', 'low'], 'func': f02_advs_119_price_to_63d_low_ratio_minus_1_d3}, 'f02_advs_120_price_to_1260d_low_ratio_minus_1_d3': {'inputs': ['close', 'low'], 'func': f02_advs_120_price_to_1260d_low_ratio_minus_1_d3}, 'f02_advs_121_log_return_first_third_252d_d3': {'inputs': ['close'], 'func': f02_advs_121_log_return_first_third_252d_d3}, 'f02_advs_122_log_return_middle_third_252d_d3': {'inputs': ['close'], 'func': f02_advs_122_log_return_middle_third_252d_d3}, 'f02_advs_123_log_return_last_third_252d_d3': {'inputs': ['close'], 'func': f02_advs_123_log_return_last_third_252d_d3}, 'f02_advs_124_ratio_last_third_to_first_third_252d_d3': {'inputs': ['close'], 'func': f02_advs_124_ratio_last_third_to_first_third_252d_d3}, 'f02_advs_125_ratio_last_third_to_middle_third_252d_d3': {'inputs': ['close'], 'func': f02_advs_125_ratio_last_third_to_middle_third_252d_d3}, 'f02_advs_126_days_to_traverse_50pct_252d_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f02_advs_126_days_to_traverse_50pct_252d_range_d3}, 'f02_advs_127_days_to_traverse_75pct_252d_range_d3': {'inputs': ['close', 'high', 'low'], 'func': f02_advs_127_days_to_traverse_75pct_252d_range_d3}, 'f02_advs_128_fraction_252d_log_gain_in_last_5d_d3': {'inputs': ['close'], 'func': f02_advs_128_fraction_252d_log_gain_in_last_5d_d3}, 'f02_advs_129_fraction_252d_log_gain_in_last_21d_d3': {'inputs': ['close'], 'func': f02_advs_129_fraction_252d_log_gain_in_last_21d_d3}, 'f02_advs_130_fraction_252d_log_gain_in_last_63d_d3': {'inputs': ['close'], 'func': f02_advs_130_fraction_252d_log_gain_in_last_63d_d3}, 'f02_advs_131_last_quintile_speed_zscore_in_252d_d3': {'inputs': ['close'], 'func': f02_advs_131_last_quintile_speed_zscore_in_252d_d3}, 'f02_advs_132_first_quintile_speed_zscore_in_252d_d3': {'inputs': ['close'], 'func': f02_advs_132_first_quintile_speed_zscore_in_252d_d3}, 'f02_advs_133_non_decreasing_close_run_max_252d_d3': {'inputs': ['close'], 'func': f02_advs_133_non_decreasing_close_run_max_252d_d3}, 'f02_advs_134_fraction_higher_highs_252d_d3': {'inputs': ['high'], 'func': f02_advs_134_fraction_higher_highs_252d_d3}, 'f02_advs_135_fraction_higher_lows_252d_d3': {'inputs': ['low'], 'func': f02_advs_135_fraction_higher_lows_252d_d3}, 'f02_advs_136_higher_hi_hi_lo_lo_streak_max_252d_d3': {'inputs': ['high', 'low'], 'func': f02_advs_136_higher_hi_hi_lo_lo_streak_max_252d_d3}, 'f02_advs_137_count_distinct_uptrend_legs_252d_d3': {'inputs': ['close'], 'func': f02_advs_137_count_distinct_uptrend_legs_252d_d3}, 'f02_advs_138_mean_uptrend_leg_log_size_252d_d3': {'inputs': ['close'], 'func': f02_advs_138_mean_uptrend_leg_log_size_252d_d3}, 'f02_advs_139_max_uptrend_leg_log_size_252d_d3': {'inputs': ['close'], 'func': f02_advs_139_max_uptrend_leg_log_size_252d_d3}, 'f02_advs_140_mean_pullback_depth_during_advance_252d_d3': {'inputs': ['close'], 'func': f02_advs_140_mean_pullback_depth_during_advance_252d_d3}, 'f02_advs_141_max_pullback_depth_during_advance_252d_d3': {'inputs': ['close'], 'func': f02_advs_141_max_pullback_depth_during_advance_252d_d3}, 'f02_advs_142_count_pullbacks_gt_5pct_252d_d3': {'inputs': ['close'], 'func': f02_advs_142_count_pullbacks_gt_5pct_252d_d3}, 'f02_advs_143_mean_pullback_duration_252d_d3': {'inputs': ['close'], 'func': f02_advs_143_mean_pullback_duration_252d_d3}, 'f02_advs_144_straight_line_advance_r2_252d_d3': {'inputs': ['close'], 'func': f02_advs_144_straight_line_advance_r2_252d_d3}, 'f02_advs_145_cumulative_drawdown_share_252d_d3': {'inputs': ['close'], 'func': f02_advs_145_cumulative_drawdown_share_252d_d3}, 'f02_advs_146_clean_advance_index_252d_d3': {'inputs': ['close'], 'func': f02_advs_146_clean_advance_index_252d_d3}, 'f02_advs_147_max_uninterrupted_advance_streak_252d_d3': {'inputs': ['close'], 'func': f02_advs_147_max_uninterrupted_advance_streak_252d_d3}, 'f02_advs_148_count_lower_lows_during_252d_uptrend_d3': {'inputs': ['low', 'close'], 'func': f02_advs_148_count_lower_lows_during_252d_uptrend_d3}, 'f02_advs_149_velocity_consistency_score_252d_d3': {'inputs': ['close'], 'func': f02_advs_149_velocity_consistency_score_252d_d3}, 'f02_advs_150_terminal_advance_completeness_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f02_advs_150_terminal_advance_completeness_252d_d3}}
