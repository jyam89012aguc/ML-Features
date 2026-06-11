"""advance_magnitude_duration d2 features 001_075 — 2nd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff() so the output is the second bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__001_075.py."""
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

def f03_amad_001_log_advance_magnitude_252d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_log(close) - _safe_log(rmin)).diff().diff()

def f03_amad_002_log_advance_magnitude_63d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    return (_safe_log(close) - _safe_log(rmin)).diff().diff()

def f03_amad_003_log_advance_magnitude_1260d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return (_safe_log(close) - _safe_log(rmin)).diff().diff()

def f03_amad_004_log_advance_magnitude_2520d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(2520, min_periods=YDAYS * 2).min()
    return (_safe_log(close) - _safe_log(rmin)).diff().diff()

def f03_amad_005_log_advance_close_anchored_1260d_d2(close: pd.Series) -> pd.Series:
    rmin = close.rolling(1260, min_periods=YDAYS).min()
    return (_safe_log(close) - _safe_log(rmin)).diff().diff()

def f03_amad_006_log_high_above_252d_low_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_log(rmax) - _safe_log(rmin)).diff().diff()

def f03_amad_007_log_high_above_1260d_low_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return (_safe_log(rmax) - _safe_log(rmin)).diff().diff()

def f03_amad_008_multiplicative_advance_pct_252d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return ((_safe_div(close, rmin) - 1.0) * 100.0).diff().diff()

def f03_amad_009_log_high_now_minus_log_low_then_252d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_log(high) - _safe_log(rmin)).diff().diff()

def f03_amad_010_log_high_now_minus_log_low_then_1260d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return (_safe_log(high) - _safe_log(rmin)).diff().diff()

def f03_amad_011_cumulative_positive_log_return_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return r.clip(lower=0).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_012_secular_advance_log_zscore_in_2520d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return _rolling_zscore(adv, 2520, min_periods=YDAYS * 2).diff().diff()

def f03_amad_013_anchored_vwap_advance_log_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_log(close) - _safe_log(_safe_div(pv, vv))).diff().diff()

def f03_amad_014_max_running_total_log_return_252d_d2(close: pd.Series) -> pd.Series:
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return r252.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f03_amad_015_net_log_return_252d_d2(close: pd.Series) -> pd.Series:
    return (_safe_log(close) - _safe_log(close.shift(YDAYS))).diff().diff()

def f03_amad_016_days_above_sma252_in_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_017_days_above_50pct_of_252d_range_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    return (pos > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_018_days_in_HH_HL_state_252d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    flag = ((high > high.shift(1)) & (low > low.shift(1))).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_019_days_within_5pct_of_252d_high_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (close >= 0.95 * rmax).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_020_days_within_10pct_of_252d_high_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (close >= 0.9 * rmax).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_021_longest_streak_close_above_sma63_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    flag = (close > sma).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f03_amad_022_longest_streak_close_above_sma252_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (close > sma).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f03_amad_023_days_since_last_close_below_sma63_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    below = close < sma
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(below).ffill()
    return (pos - last).diff().diff()

def f03_amad_024_days_since_last_close_below_sma252_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    below = close < sma
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(below).ffill()
    return (pos - last).diff().diff()

def f03_amad_025_days_since_first_252d_high_in_current_uptrend_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above = close > sma
    streak_id = (~above).cumsum()
    rmax_prior = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (high > rmax_prior) & above
    pos = pd.Series(np.arange(len(close)), index=close.index)
    first_in_streak = pos.where(new_high).groupby(streak_id).cummin()
    return (pos - first_in_streak).where(above, np.nan).diff().diff()

def f03_amad_026_days_above_anchored_252d_vwap_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap = _safe_div(pv, vv)
    return (close > vwap).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_027_uptrend_state_score_252d_d2(close: pd.Series) -> pd.Series:
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((close > s21) & (s21 > s63) & (s63 > s252) & (s252 > s252.shift(MDAYS))).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f03_amad_028_count_higher_highs_252d_d2(high: pd.Series) -> pd.Series:
    return (high > high.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_029_count_higher_lows_252d_d2(low: pd.Series) -> pd.Series:
    return (low > low.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_030_count_close_in_top_decile_of_252d_range_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    return (pos >= 0.9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_031_log_advance_per_bar_252d_window_d2(close: pd.Series) -> pd.Series:
    return ((_safe_log(close) - _safe_log(close.shift(YDAYS))) / float(YDAYS)).diff().diff()

def f03_amad_032_log_advance_per_bar_63d_window_d2(close: pd.Series) -> pd.Series:
    return ((_safe_log(close) - _safe_log(close.shift(QDAYS))) / float(QDAYS)).diff().diff()

def f03_amad_033_atr_units_per_bar_advance_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return ((close - rmin) / atr.replace(0, np.nan) / float(YDAYS)).diff().diff()

def f03_amad_034_position_in_252d_range_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return ((close - rmin) / rng).diff().diff()

def f03_amad_035_log_advance_per_bar_above_sma63_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    above = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    ret = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return _safe_div(ret, above + 1.0).diff().diff()

def f03_amad_036_cumulative_gain_per_bar_above_sma252_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    cum = _safe_log(close).diff().clip(lower=0).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(cum, above + 1.0).diff().diff()

def f03_amad_037_amplitude_normalized_advance_252d_d2(close: pd.Series) -> pd.Series:
    ret = _safe_log(close) - _safe_log(close.shift(YDAYS))
    sd = _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(ret, sd).diff().diff()

def f03_amad_038_normalized_magnitude_per_uptrend_day_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    up = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    return _safe_div(pos, up + 1.0).diff().diff()

def f03_amad_039_advance_efficiency_per_uptrend_bar_252d_d2(close: pd.Series) -> pd.Series:
    up = (close.diff() > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    ret = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return _safe_div(ret, up + 1.0).diff().diff()

def f03_amad_040_secular_per_bar_log_advance_2520d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(2520, min_periods=YDAYS * 2).min()
    return ((_safe_log(close) - _safe_log(rmin)) / 2520.0).diff().diff()

def f03_amad_041_advance_magnitude_per_atr_252d_d2(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return ((close - rmin) / atr.replace(0, np.nan)).diff().diff()

def f03_amad_042_trough_to_peak_log_per_age_score_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    age = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(rmax) - _safe_log(rmin), age + 1.0).diff().diff()

def f03_amad_043_first_third_log_return_per_bar_252d_d2(close: pd.Series) -> pd.Series:
    third = 252 // 3
    lp = _safe_log(close)
    return ((lp.shift(YDAYS - third) - lp.shift(YDAYS)) / float(third)).diff().diff()

def f03_amad_044_last_third_log_return_per_bar_252d_d2(close: pd.Series) -> pd.Series:
    third = 252 // 3
    lp = _safe_log(close)
    return ((lp - lp.shift(YDAYS - 2 * third)) / float(third)).diff().diff()

def f03_amad_045_amplitude_per_pullback_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = _safe_log(rmax) - _safe_log(rmin)
    running_max = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, running_max) - 1.0
    pullbacks = (dd < -0.05).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rng, 1.0 + pullbacks).diff().diff()

def f03_amad_046_quantile_p95_log_close_252d_d2(close: pd.Series) -> pd.Series:
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.95).diff().diff()

def f03_amad_047_quantile_p50_log_close_252d_d2(close: pd.Series) -> pd.Series:
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.5).diff().diff()

def f03_amad_048_quantile_p5_log_close_252d_d2(close: pd.Series) -> pd.Series:
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.05).diff().diff()

def f03_amad_049_close_to_p95_log_distance_252d_d2(close: pd.Series) -> pd.Series:
    return (_safe_log(close) - _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.95)).diff().diff()

def f03_amad_050_close_to_p50_log_distance_252d_d2(close: pd.Series) -> pd.Series:
    return (_safe_log(close) - _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.5)).diff().diff()

def f03_amad_051_quantile_iqr_log_close_252d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)).diff().diff()

def f03_amad_052_distribution_skew_log_close_252d_d2(close: pd.Series) -> pd.Series:
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff()

def f03_amad_053_distribution_kurt_log_close_252d_d2(close: pd.Series) -> pd.Series:
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).kurt().diff().diff()

def f03_amad_054_distance_to_252d_max_normalized_by_std_log_close_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    mx = lp.rolling(YDAYS, min_periods=QDAYS).max()
    sd = lp.rolling(YDAYS, min_periods=QDAYS).std()
    return ((mx - lp) / sd.replace(0, np.nan)).diff().diff()

def f03_amad_055_max_to_min_log_close_252d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp.rolling(YDAYS, min_periods=QDAYS).max() - lp.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff()

def f03_amad_056_max_to_min_log_close_1260d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp.rolling(1260, min_periods=YDAYS).max() - lp.rolling(1260, min_periods=YDAYS).min()).diff().diff()

def f03_amad_057_max_to_min_log_close_2520d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp.rolling(2520, min_periods=YDAYS * 2).max() - lp.rolling(2520, min_periods=YDAYS * 2).min()).diff().diff()

def f03_amad_058_max_to_min_log_close_63d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    return (lp.rolling(QDAYS, min_periods=MDAYS).max() - lp.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff()

def f03_amad_059_log_close_iqr_to_range_ratio_252d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    iqr = lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    rng = lp.rolling(YDAYS, min_periods=QDAYS).max() - lp.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(iqr, rng).diff().diff()

def f03_amad_060_distance_close_to_252d_median_atr_units_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    atr = _atr(high, low, close, MDAYS)
    return ((close - med) / atr.replace(0, np.nan)).diff().diff()

def f03_amad_061_trough_to_peak_atr_units_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    mx = close.rolling(YDAYS, min_periods=QDAYS).max()
    mn = close.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return ((mx - mn) / atr.replace(0, np.nan)).diff().diff()

def f03_amad_062_trough_to_peak_bars_252d_d2(close: pd.Series) -> pd.Series:

    def _span(w):
        if np.isnan(w).any():
            return np.nan
        return float(int(np.argmax(w)) - int(np.argmin(w)))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_span, raw=True).diff().diff()

def f03_amad_063_trough_to_peak_speed_252d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)

    def _spd(w):
        if np.isnan(w).any():
            return np.nan
        a, b = (int(np.argmin(w)), int(np.argmax(w)))
        if a == b:
            return np.nan
        return float((w[b] - w[a]) / (b - a))
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_spd, raw=True).diff().diff()

def f03_amad_064_peak_to_now_bars_252d_d2(close: pd.Series) -> pd.Series:

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True).diff().diff()

def f03_amad_065_peak_to_now_log_decay_252d_d2(close: pd.Series) -> pd.Series:
    return (_safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())).diff().diff()

def f03_amad_066_mid_advance_position_marker_252d_d2(close: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    mid = (rmax + rmin) / 2.0
    rng = (rmax - rmin).replace(0, np.nan)
    return ((close - mid) / rng).diff().diff()

def f03_amad_067_trough_age_252d_d2(low: pd.Series) -> pd.Series:

    def _ta(w):
        return float(len(w) - 1 - int(np.argmin(w)))
    return low.rolling(YDAYS, min_periods=QDAYS).apply(_ta, raw=True).diff().diff()

def f03_amad_068_advance_age_signed_score_252d_d2(close: pd.Series, low: pd.Series) -> pd.Series:

    def _ta(w):
        return float(len(w) - 1 - int(np.argmin(w)))

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    ta = low.rolling(YDAYS, min_periods=QDAYS).apply(_ta, raw=True)
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    return (ta - pa).diff().diff()

def f03_amad_069_mature_advance_indicator_252d_d2(close: pd.Series) -> pd.Series:

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((pa > MDAYS) & (close > sma)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f03_amad_070_days_in_distribution_top_decile_252d_d2(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    p90 = lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    return (lp >= p90).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f03_amad_071_trough_to_peak_log_x_age_252d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    return ((_safe_log(rmax) - _safe_log(rmin)) * pa).diff().diff()

def f03_amad_072_peak_to_prior_peak_log_advance_252d_d2(close: pd.Series) -> pd.Series:
    mx = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_log(mx) - _safe_log(mx.shift(YDAYS))).diff().diff()

def f03_amad_073_secular_trough_to_peak_log_2520d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    mx = close.rolling(2520, min_periods=YDAYS * 2).max()
    mn = low.rolling(2520, min_periods=YDAYS * 2).min()
    return (_safe_log(mx) - _safe_log(mn)).diff().diff()

def f03_amad_074_long_horizon_advance_completeness_2520d_d2(close: pd.Series) -> pd.Series:
    return _safe_div(close, close.rolling(2520, min_periods=YDAYS * 2).max()).diff().diff()

def f03_amad_075_advance_completeness_pct_of_252d_max_d2(close: pd.Series) -> pd.Series:
    return _safe_div(close, close.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff()
ADVANCE_MAGNITUDE_DURATION_D2_REGISTRY_001_075 = {'f03_amad_001_log_advance_magnitude_252d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_001_log_advance_magnitude_252d_d2}, 'f03_amad_002_log_advance_magnitude_63d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_002_log_advance_magnitude_63d_d2}, 'f03_amad_003_log_advance_magnitude_1260d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_003_log_advance_magnitude_1260d_d2}, 'f03_amad_004_log_advance_magnitude_2520d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_004_log_advance_magnitude_2520d_d2}, 'f03_amad_005_log_advance_close_anchored_1260d_d2': {'inputs': ['close'], 'func': f03_amad_005_log_advance_close_anchored_1260d_d2}, 'f03_amad_006_log_high_above_252d_low_d2': {'inputs': ['high', 'low'], 'func': f03_amad_006_log_high_above_252d_low_d2}, 'f03_amad_007_log_high_above_1260d_low_d2': {'inputs': ['high', 'low'], 'func': f03_amad_007_log_high_above_1260d_low_d2}, 'f03_amad_008_multiplicative_advance_pct_252d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_008_multiplicative_advance_pct_252d_d2}, 'f03_amad_009_log_high_now_minus_log_low_then_252d_d2': {'inputs': ['high', 'low'], 'func': f03_amad_009_log_high_now_minus_log_low_then_252d_d2}, 'f03_amad_010_log_high_now_minus_log_low_then_1260d_d2': {'inputs': ['high', 'low'], 'func': f03_amad_010_log_high_now_minus_log_low_then_1260d_d2}, 'f03_amad_011_cumulative_positive_log_return_252d_d2': {'inputs': ['close'], 'func': f03_amad_011_cumulative_positive_log_return_252d_d2}, 'f03_amad_012_secular_advance_log_zscore_in_2520d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_012_secular_advance_log_zscore_in_2520d_d2}, 'f03_amad_013_anchored_vwap_advance_log_252d_d2': {'inputs': ['close', 'volume'], 'func': f03_amad_013_anchored_vwap_advance_log_252d_d2}, 'f03_amad_014_max_running_total_log_return_252d_d2': {'inputs': ['close'], 'func': f03_amad_014_max_running_total_log_return_252d_d2}, 'f03_amad_015_net_log_return_252d_d2': {'inputs': ['close'], 'func': f03_amad_015_net_log_return_252d_d2}, 'f03_amad_016_days_above_sma252_in_252d_d2': {'inputs': ['close'], 'func': f03_amad_016_days_above_sma252_in_252d_d2}, 'f03_amad_017_days_above_50pct_of_252d_range_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_017_days_above_50pct_of_252d_range_d2}, 'f03_amad_018_days_in_HH_HL_state_252d_d2': {'inputs': ['high', 'low'], 'func': f03_amad_018_days_in_HH_HL_state_252d_d2}, 'f03_amad_019_days_within_5pct_of_252d_high_d2': {'inputs': ['close', 'high'], 'func': f03_amad_019_days_within_5pct_of_252d_high_d2}, 'f03_amad_020_days_within_10pct_of_252d_high_d2': {'inputs': ['close', 'high'], 'func': f03_amad_020_days_within_10pct_of_252d_high_d2}, 'f03_amad_021_longest_streak_close_above_sma63_252d_d2': {'inputs': ['close'], 'func': f03_amad_021_longest_streak_close_above_sma63_252d_d2}, 'f03_amad_022_longest_streak_close_above_sma252_252d_d2': {'inputs': ['close'], 'func': f03_amad_022_longest_streak_close_above_sma252_252d_d2}, 'f03_amad_023_days_since_last_close_below_sma63_d2': {'inputs': ['close'], 'func': f03_amad_023_days_since_last_close_below_sma63_d2}, 'f03_amad_024_days_since_last_close_below_sma252_d2': {'inputs': ['close'], 'func': f03_amad_024_days_since_last_close_below_sma252_d2}, 'f03_amad_025_days_since_first_252d_high_in_current_uptrend_d2': {'inputs': ['close', 'high'], 'func': f03_amad_025_days_since_first_252d_high_in_current_uptrend_d2}, 'f03_amad_026_days_above_anchored_252d_vwap_d2': {'inputs': ['close', 'volume'], 'func': f03_amad_026_days_above_anchored_252d_vwap_d2}, 'f03_amad_027_uptrend_state_score_252d_d2': {'inputs': ['close'], 'func': f03_amad_027_uptrend_state_score_252d_d2}, 'f03_amad_028_count_higher_highs_252d_d2': {'inputs': ['high'], 'func': f03_amad_028_count_higher_highs_252d_d2}, 'f03_amad_029_count_higher_lows_252d_d2': {'inputs': ['low'], 'func': f03_amad_029_count_higher_lows_252d_d2}, 'f03_amad_030_count_close_in_top_decile_of_252d_range_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_030_count_close_in_top_decile_of_252d_range_d2}, 'f03_amad_031_log_advance_per_bar_252d_window_d2': {'inputs': ['close'], 'func': f03_amad_031_log_advance_per_bar_252d_window_d2}, 'f03_amad_032_log_advance_per_bar_63d_window_d2': {'inputs': ['close'], 'func': f03_amad_032_log_advance_per_bar_63d_window_d2}, 'f03_amad_033_atr_units_per_bar_advance_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_033_atr_units_per_bar_advance_252d_d2}, 'f03_amad_034_position_in_252d_range_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_034_position_in_252d_range_d2}, 'f03_amad_035_log_advance_per_bar_above_sma63_252d_d2': {'inputs': ['close'], 'func': f03_amad_035_log_advance_per_bar_above_sma63_252d_d2}, 'f03_amad_036_cumulative_gain_per_bar_above_sma252_252d_d2': {'inputs': ['close'], 'func': f03_amad_036_cumulative_gain_per_bar_above_sma252_252d_d2}, 'f03_amad_037_amplitude_normalized_advance_252d_d2': {'inputs': ['close'], 'func': f03_amad_037_amplitude_normalized_advance_252d_d2}, 'f03_amad_038_normalized_magnitude_per_uptrend_day_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_038_normalized_magnitude_per_uptrend_day_252d_d2}, 'f03_amad_039_advance_efficiency_per_uptrend_bar_252d_d2': {'inputs': ['close'], 'func': f03_amad_039_advance_efficiency_per_uptrend_bar_252d_d2}, 'f03_amad_040_secular_per_bar_log_advance_2520d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_040_secular_per_bar_log_advance_2520d_d2}, 'f03_amad_041_advance_magnitude_per_atr_252d_d2': {'inputs': ['close', 'low', 'high'], 'func': f03_amad_041_advance_magnitude_per_atr_252d_d2}, 'f03_amad_042_trough_to_peak_log_per_age_score_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_042_trough_to_peak_log_per_age_score_252d_d2}, 'f03_amad_043_first_third_log_return_per_bar_252d_d2': {'inputs': ['close'], 'func': f03_amad_043_first_third_log_return_per_bar_252d_d2}, 'f03_amad_044_last_third_log_return_per_bar_252d_d2': {'inputs': ['close'], 'func': f03_amad_044_last_third_log_return_per_bar_252d_d2}, 'f03_amad_045_amplitude_per_pullback_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_045_amplitude_per_pullback_252d_d2}, 'f03_amad_046_quantile_p95_log_close_252d_d2': {'inputs': ['close'], 'func': f03_amad_046_quantile_p95_log_close_252d_d2}, 'f03_amad_047_quantile_p50_log_close_252d_d2': {'inputs': ['close'], 'func': f03_amad_047_quantile_p50_log_close_252d_d2}, 'f03_amad_048_quantile_p5_log_close_252d_d2': {'inputs': ['close'], 'func': f03_amad_048_quantile_p5_log_close_252d_d2}, 'f03_amad_049_close_to_p95_log_distance_252d_d2': {'inputs': ['close'], 'func': f03_amad_049_close_to_p95_log_distance_252d_d2}, 'f03_amad_050_close_to_p50_log_distance_252d_d2': {'inputs': ['close'], 'func': f03_amad_050_close_to_p50_log_distance_252d_d2}, 'f03_amad_051_quantile_iqr_log_close_252d_d2': {'inputs': ['close'], 'func': f03_amad_051_quantile_iqr_log_close_252d_d2}, 'f03_amad_052_distribution_skew_log_close_252d_d2': {'inputs': ['close'], 'func': f03_amad_052_distribution_skew_log_close_252d_d2}, 'f03_amad_053_distribution_kurt_log_close_252d_d2': {'inputs': ['close'], 'func': f03_amad_053_distribution_kurt_log_close_252d_d2}, 'f03_amad_054_distance_to_252d_max_normalized_by_std_log_close_d2': {'inputs': ['close'], 'func': f03_amad_054_distance_to_252d_max_normalized_by_std_log_close_d2}, 'f03_amad_055_max_to_min_log_close_252d_d2': {'inputs': ['close'], 'func': f03_amad_055_max_to_min_log_close_252d_d2}, 'f03_amad_056_max_to_min_log_close_1260d_d2': {'inputs': ['close'], 'func': f03_amad_056_max_to_min_log_close_1260d_d2}, 'f03_amad_057_max_to_min_log_close_2520d_d2': {'inputs': ['close'], 'func': f03_amad_057_max_to_min_log_close_2520d_d2}, 'f03_amad_058_max_to_min_log_close_63d_d2': {'inputs': ['close'], 'func': f03_amad_058_max_to_min_log_close_63d_d2}, 'f03_amad_059_log_close_iqr_to_range_ratio_252d_d2': {'inputs': ['close'], 'func': f03_amad_059_log_close_iqr_to_range_ratio_252d_d2}, 'f03_amad_060_distance_close_to_252d_median_atr_units_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_060_distance_close_to_252d_median_atr_units_d2}, 'f03_amad_061_trough_to_peak_atr_units_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f03_amad_061_trough_to_peak_atr_units_252d_d2}, 'f03_amad_062_trough_to_peak_bars_252d_d2': {'inputs': ['close'], 'func': f03_amad_062_trough_to_peak_bars_252d_d2}, 'f03_amad_063_trough_to_peak_speed_252d_d2': {'inputs': ['close'], 'func': f03_amad_063_trough_to_peak_speed_252d_d2}, 'f03_amad_064_peak_to_now_bars_252d_d2': {'inputs': ['close'], 'func': f03_amad_064_peak_to_now_bars_252d_d2}, 'f03_amad_065_peak_to_now_log_decay_252d_d2': {'inputs': ['close'], 'func': f03_amad_065_peak_to_now_log_decay_252d_d2}, 'f03_amad_066_mid_advance_position_marker_252d_d2': {'inputs': ['close'], 'func': f03_amad_066_mid_advance_position_marker_252d_d2}, 'f03_amad_067_trough_age_252d_d2': {'inputs': ['low'], 'func': f03_amad_067_trough_age_252d_d2}, 'f03_amad_068_advance_age_signed_score_252d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_068_advance_age_signed_score_252d_d2}, 'f03_amad_069_mature_advance_indicator_252d_d2': {'inputs': ['close'], 'func': f03_amad_069_mature_advance_indicator_252d_d2}, 'f03_amad_070_days_in_distribution_top_decile_252d_d2': {'inputs': ['close'], 'func': f03_amad_070_days_in_distribution_top_decile_252d_d2}, 'f03_amad_071_trough_to_peak_log_x_age_252d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_071_trough_to_peak_log_x_age_252d_d2}, 'f03_amad_072_peak_to_prior_peak_log_advance_252d_d2': {'inputs': ['close'], 'func': f03_amad_072_peak_to_prior_peak_log_advance_252d_d2}, 'f03_amad_073_secular_trough_to_peak_log_2520d_d2': {'inputs': ['close', 'low'], 'func': f03_amad_073_secular_trough_to_peak_log_2520d_d2}, 'f03_amad_074_long_horizon_advance_completeness_2520d_d2': {'inputs': ['close'], 'func': f03_amad_074_long_horizon_advance_completeness_2520d_d2}, 'f03_amad_075_advance_completeness_pct_of_252d_max_d2': {'inputs': ['close'], 'func': f03_amad_075_advance_completeness_pct_of_252d_max_d2}}
