"""topping_pattern d2 features 076_150 — 2nd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff() so the output is the second bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
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

def _rsi14(close):
    delta = close.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = (-delta).where(delta < 0, 0.0)
    avg_gain = gain.rolling(14, min_periods=WDAYS).mean()
    avg_loss = loss.rolling(14, min_periods=WDAYS).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)

def _stoch_k14(close, high, low):
    rmax = high.rolling(14, min_periods=WDAYS).max()
    rmin = low.rolling(14, min_periods=WDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return 100.0 * (close - rmin) / rng

def _macd(close, fast=12, slow=26, sig=9):
    ema_f = close.ewm(span=fast, adjust=False, min_periods=fast).mean()
    ema_s = close.ewm(span=slow, adjust=False, min_periods=slow).mean()
    macd = ema_f - ema_s
    signal = macd.ewm(span=sig, adjust=False, min_periods=sig).mean()
    return (macd, signal, macd - signal)

def f04_topp_076_distribution_day_count_252d_d2(close: pd.Series, open_: pd.Series, volume: pd.Series) -> pd.Series:
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((close < open_) & (volume > med_v)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_077_stalling_day_count_at_top_252d_d2(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    atr = _atr(high, low, close, MDAYS)
    small = rng < 0.7 * atr
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    hi_v = volume > med_v
    flag = (near & small & hi_v & (pos < 0.5)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_078_churning_day_count_at_top_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    quiet = _safe_log(close).diff().abs() < 0.01
    med_v = volume.rolling(MDAYS, min_periods=WDAYS).median()
    hi_v = volume > 2.0 * med_v
    flag = (near & quiet & hi_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_079_percent_distribution_days_after_high_21d_d2(close: pd.Series, open_: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    dist = ((close < open_) & (volume > med_v)).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    after = (pa < MDAYS).astype(float)
    return (dist * after).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f04_topp_080_distribution_clustering_score_21d_d2(close: pd.Series, open_: pd.Series, volume: pd.Series) -> pd.Series:
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    dist = ((close < open_) & (volume > med_v)).astype(int)
    grp = (dist == 0).cumsum()
    streak = dist.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max().diff().diff()

def f04_topp_081_high_volume_red_days_at_high_count_21d_d2(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    red = close < close.shift(1)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    hi_v = volume > 1.5 * v21
    flag = (near & red & hi_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_082_institutional_distribution_signal_252d_d2(close: pd.Series, open_: pd.Series, volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    weight = volume / v21.replace(0, np.nan)
    flag = (close < open_).astype(float) * weight
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_083_churn_zone_density_at_top_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.95 * rmax
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (near & (volume > med_v)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f04_topp_084_volume_at_high_vs_advance_avg_volume_ratio_252d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.95 * rmax
    vol_near = volume.where(near).rolling(YDAYS, min_periods=QDAYS).mean()
    vol_below = volume.where(~near).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(vol_near, vol_below).diff().diff()

def f04_topp_085_narrow_range_at_top_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    rng = high - low
    nr4 = rng < rng.rolling(4, min_periods=4).max().shift(1).combine_first(rng)
    flag = (near & nr4).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_086_inside_day_count_at_high_21d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return (near & inside).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_087_outside_day_count_at_high_21d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    outside = (high > high.shift(1)) & (low < low.shift(1))
    return (near & outside).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_088_mid_range_close_count_at_high_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    mid = (pos > 1.0 / 3.0) & (pos < 2.0 / 3.0)
    return (near & mid).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_089_weak_close_count_at_high_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    return (near & (pos < 1.0 / 3.0)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_090_strong_close_count_at_high_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    return (near & (pos > 2.0 / 3.0)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_091_rsi_bearish_divergence_score_63d_d2(close: pd.Series) -> pd.Series:
    rsi = _rsi14(close)

    def _argmaxpos(w):
        if np.isnan(w).any():
            return np.nan
        return float(int(np.argmax(w)) / max(len(w) - 1, 1))
    p_pos = close.rolling(QDAYS, min_periods=MDAYS).apply(_argmaxpos, raw=True)
    r_pos = rsi.rolling(QDAYS, min_periods=MDAYS).apply(_argmaxpos, raw=True)
    return (p_pos - r_pos).diff().diff()

def f04_topp_092_rsi_negative_divergence_strength_252d_d2(close: pd.Series) -> pd.Series:
    rsi = _rsi14(close)
    p_slope = _rolling_slope(_safe_log(close), YDAYS)
    r_slope = _rolling_slope(rsi, YDAYS)
    return (p_slope - r_slope / 100.0).diff().diff()

def f04_topp_093_rsi_overbought_persistence_count_63d_d2(close: pd.Series) -> pd.Series:
    rsi = _rsi14(close)
    return (rsi > 70.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_094_rsi_failure_swing_count_63d_d2(close: pd.Series) -> pd.Series:
    rsi = _rsi14(close)
    rsi_max_21 = rsi.rolling(MDAYS, min_periods=WDAYS).max()
    rsi_was_overbought = (rsi_max_21.shift(MDAYS) > 70).astype(bool)
    rsi_lower_max = rsi_max_21 < rsi_max_21.shift(MDAYS)
    price_higher_max = close.rolling(MDAYS, min_periods=WDAYS).max() > close.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    flag = (rsi_was_overbought & rsi_lower_max & price_higher_max).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_095_rsi_bear_divergence_count_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    rsi = _rsi14(close)
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    new_pivot = high == rmax_21
    rsi_lower = rsi < rsi.shift(MDAYS)
    return (new_pivot & rsi_lower).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_096_macd_bearish_divergence_score_63d_d2(close: pd.Series) -> pd.Series:
    macd, _, _ = _macd(close)
    p_slope = _rolling_slope(_safe_log(close), QDAYS)
    m_slope = _rolling_slope(macd, QDAYS)
    return (p_slope - m_slope).diff().diff()

def f04_topp_097_macd_hist_lower_high_count_63d_d2(close: pd.Series) -> pd.Series:
    _, _, hist = _macd(close)
    h_max = hist.rolling(MDAYS, min_periods=WDAYS).max()
    return (h_max < h_max.shift(MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_098_macd_signal_cross_below_count_63d_d2(close: pd.Series) -> pd.Series:
    macd, signal, _ = _macd(close)
    cross_dn = (macd < signal) & (macd.shift(1) >= signal.shift(1))
    return cross_dn.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_099_momentum_peak_before_price_peak_lag_63d_d2(close: pd.Series) -> pd.Series:
    mom = close.pct_change(MDAYS)

    def _idx(w):
        if np.isnan(w).any():
            return np.nan
        return float(int(np.argmax(w)))
    p = close.rolling(QDAYS, min_periods=MDAYS).apply(_idx, raw=True)
    m = mom.rolling(QDAYS, min_periods=MDAYS).apply(_idx, raw=True)
    return (m - p).diff().diff()

def f04_topp_100_stochastic_overbought_persistence_count_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    k = _stoch_k14(close, high, low)
    return (k > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_101_stochastic_bear_divergence_score_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    k = _stoch_k14(close, high, low)
    p_slope = _rolling_slope(_safe_log(close), QDAYS)
    k_slope = _rolling_slope(k, QDAYS) / 100.0
    return (p_slope - k_slope).diff().diff()

def f04_topp_102_cci_overextension_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    sma = tp.rolling(20, min_periods=WDAYS).mean()
    md = (tp - sma).abs().rolling(20, min_periods=WDAYS).mean()
    cci = (tp - sma) / (0.015 * md.replace(0, np.nan))
    return (cci > 200.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_103_williams_r_overbought_persistence_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(14, min_periods=WDAYS).max()
    rmin = low.rolling(14, min_periods=WDAYS).min()
    wr = -100.0 * (rmax - close) / (rmax - rmin).replace(0, np.nan)
    return (wr > -20.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_104_roc_bearish_divergence_count_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    roc = close.pct_change(MDAYS)
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    new_pivot = high == rmax_21
    roc_lower = roc < roc.shift(MDAYS)
    return (new_pivot & roc_lower).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_105_momentum_lower_high_count_at_price_higher_high_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    mom = close.pct_change(MDAYS)
    p_max = high.rolling(MDAYS, min_periods=WDAYS).max()
    m_max = mom.rolling(MDAYS, min_periods=WDAYS).max()
    flag = ((p_max > p_max.shift(MDAYS)) & (m_max < m_max.shift(MDAYS))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_106_sma21_break_below_after_high_count_21d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    below = close < sma
    rmax_252 = high.rolling(YDAYS, min_periods=QDAYS).max()

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    after_high = pa < MDAYS
    return (below & after_high).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_107_sma63_break_below_after_high_count_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    below = close < sma

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    after_high = pa < QDAYS
    return (below & after_high).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_108_sma252_break_below_after_high_count_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    below = close < sma

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    after_high = pa < YDAYS
    return (below & after_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_109_days_since_close_first_crossed_below_sma21_after_252d_high_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    cross = (close < sma) & (close.shift(1) >= sma.shift(1))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(cross).ffill()
    return (pos - last).diff().diff()

def f04_topp_110_days_since_close_first_crossed_below_sma63_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    cross = (close < sma) & (close.shift(1) >= sma.shift(1))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(cross).ffill()
    return (pos - last).diff().diff()

def f04_topp_111_trend_line_break_count_252d_d2(low: pd.Series) -> pd.Series:

    def _eval(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            c1, c0 = np.polyfit(x, w, 1)
        except Exception:
            return np.nan
        return float(c1 * (len(w) - 1) + c0)
    line = low.rolling(QDAYS, min_periods=MDAYS).apply(_eval, raw=True)
    below = low < line
    return below.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_112_lower_low_first_appearance_days_since_252d_d2(low: pd.Series) -> pd.Series:
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    new_low = low < prior_min
    pos = pd.Series(np.arange(len(low)), index=low.index)
    last = pos.where(new_low).ffill()
    return (pos - last).diff().diff()

def f04_topp_113_lower_high_first_appearance_days_since_252d_d2(high: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    lower_high = (high < prior_max) & (high.shift(1) >= prior_max.shift(1))
    pos = pd.Series(np.arange(len(high)), index=high.index)
    last = pos.where(lower_high).ffill()
    return (pos - last).diff().diff()

def f04_topp_114_swing_low_break_count_at_top_252d_d2(low: pd.Series, high: pd.Series) -> pd.Series:
    rmin_63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    break_low = low < rmin_63

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    after_high = pa < YDAYS
    return (break_low & after_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_115_first_lower_low_after_252d_high_days_since_d2(low: pd.Series, high: pd.Series) -> pd.Series:
    prior_min = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    new_low = low < prior_min

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    after_high = pa < YDAYS
    first_after = new_low & after_high
    pos = pd.Series(np.arange(len(low)), index=low.index)
    last = pos.where(first_after).ffill()
    return (pos - last).diff().diff()

def f04_topp_116_first_lower_high_after_252d_high_days_since_d2(high: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    lower_high = (high < prior_max) & (high.shift(1) >= prior_max.shift(1))

    def _pa(w):
        return float(len(w) - 1 - int(np.argmax(w)))
    pa = high.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    after_high = pa < YDAYS
    flag = lower_high & after_high
    pos = pd.Series(np.arange(len(high)), index=high.index)
    last = pos.where(flag).ffill()
    return (pos - last).diff().diff()

def f04_topp_117_channel_break_below_score_63d_d2(close: pd.Series, low: pd.Series) -> pd.Series:

    def _eval(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            c1, c0 = np.polyfit(x, w, 1)
        except Exception:
            return np.nan
        return float(c1 * (len(w) - 1) + c0)
    line = low.rolling(QDAYS, min_periods=MDAYS).apply(_eval, raw=True)
    return _safe_div(line - close, close).diff().diff()

def f04_topp_118_trendline_violation_distance_252d_d2(close: pd.Series) -> pd.Series:

    def _resid_max(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            c1, c0 = np.polyfit(x, w, 1)
        except Exception:
            return np.nan
        pred = c1 * x + c0
        return float((w - pred).min())
    return _safe_div(close.rolling(YDAYS, min_periods=QDAYS).apply(_resid_max, raw=True), close).diff().diff()

def f04_topp_119_trend_break_volume_confirmation_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    cross_dn = (close < sma) & (close.shift(1) >= sma.shift(1))
    vol_z = _rolling_zscore(volume, YDAYS)
    return (cross_dn.astype(float) * vol_z).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_120_break_below_anchored_vwap_count_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap = _safe_div(pv, vv)
    return (close < vwap).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_121_climax_top_volume_score_63d_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (close >= 0.97 * rmax).astype(float)
    vol_z = _rolling_zscore(volume, YDAYS)
    return (near * vol_z).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_122_climax_top_one_day_reversal_count_21d_d2(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    rmax_prior = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > rmax_prior
    bear = close < open_
    return (new_high & bear).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_123_exhaustion_gap_at_top_count_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.95 * rmax
    gap_up = open_ > close.shift(1)
    bear = close < open_
    return (near & gap_up & bear).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_124_island_reversal_count_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    gap_up_prev = low.shift(1) > high.shift(2)
    gap_dn_now = high < low.shift(1)
    flag = (gap_up_prev & gap_dn_now).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_125_key_reversal_day_count_at_high_63d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    flag = ((high > high.shift(1)) & (close < low.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_126_outside_engulfing_bearish_at_high_count_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.95 * rmax
    prev_up = close.shift(1) > open_.shift(1)
    cur_down = close < open_
    engulf = (open_ > close.shift(1)) & (close < open_.shift(1))
    flag = (near & prev_up & cur_down & engulf).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_127_dark_cloud_cover_count_at_high_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.95 * rmax
    prev_up = close.shift(1) > open_.shift(1)
    open_above = open_ > high.shift(1)
    close_into = (close < open_) & (close < (open_.shift(1) + close.shift(1)) / 2.0) & (close > open_.shift(1))
    flag = (near & prev_up & open_above & close_into).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_128_evening_star_count_at_high_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.95 * rmax
    body = (close - open_).abs()
    sma_body = body.rolling(MDAYS, min_periods=WDAYS).mean()
    bull_2_ago = close.shift(2) > open_.shift(2)
    small_mid = body.shift(1) < 0.3 * sma_body.shift(1)
    bear_now = close < open_
    flag = (near & bull_2_ago & small_mid & bear_now).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_129_hanging_man_count_at_high_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    lower_wick = close.where(close < open_, open_) - low
    pattern = (body / rng < 0.3) & (lower_wick / rng > 0.5)
    flag = (near & pattern).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_130_long_upper_wick_at_high_count_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    rng = (high - low).replace(0, np.nan)
    upper = high - close.where(close > open_, open_)
    long_wick = upper / rng > 0.5
    return (near & long_wick).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_131_doji_at_high_count_21d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    doji = body / rng < 0.1
    return (near & doji).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_132_spinning_top_at_high_count_21d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - close.where(close > open_, open_)
    lower = close.where(close < open_, open_) - low
    pattern = (body / rng < 0.3) & (upper / rng > 0.2) & (lower / rng > 0.2)
    return (near & pattern).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f04_topp_133_bearish_star_pattern_count_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high.shift(1) >= 0.95 * rmax.shift(1)
    bull = close.shift(2) > open_.shift(2)
    gap_up = open_.shift(1) > close.shift(2)
    body_mid = (close.shift(1) - open_.shift(1)).abs() < 0.3 * (close.shift(2) - open_.shift(2)).abs()
    gap_dn = open_ < close.shift(1)
    bear = close < open_
    flag = (near & bull & gap_up & body_mid & gap_dn & bear).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_134_three_black_crows_count_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_recent = high.shift(2) >= 0.95 * rmax.shift(2)
    bear_3 = (close.shift(2) < open_.shift(2)) & (close.shift(1) < open_.shift(1)) & (close < open_)
    lower_chain = (close < close.shift(1)) & (close.shift(1) < close.shift(2))
    flag = (near_recent & bear_3 & lower_chain).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_135_abandoned_baby_top_count_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_doji = high.shift(1) >= 0.97 * rmax.shift(1)
    body_doji = (close.shift(1) - open_.shift(1)).abs() < 0.1 * (high.shift(1) - low.shift(1))
    gap_up_to_doji = low.shift(1) > high.shift(2)
    gap_dn_from_doji = high < low.shift(1)
    flag = (near_doji & body_doji & gap_up_to_doji & gap_dn_from_doji).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_136_multi_signal_top_score_252d_d2(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    outside = (high > high.shift(1)) & (low < low.shift(1))
    rng = (high - low).replace(0, np.nan)
    body = (close - open_).abs()
    pos = (close - low) / rng
    upper = high - close.where(close > open_, open_)
    doji = body / rng < 0.1
    weak = pos < 0.33
    big_wick = upper / rng > 0.5
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    dist = (close < open_) & (volume > med_v)
    flag_sum = (near & (outside | doji | weak | big_wick | dist)).astype(float)
    return flag_sum.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_137_topping_pattern_density_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((high > prior_max) & (close < close.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f04_topp_138_bullish_to_bearish_pattern_ratio_63d_d2(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    bull_eng = (close > open_) & (close.shift(1) < open_.shift(1)) & (open_ < close.shift(1)) & (close > open_.shift(1))
    bear_eng = (close < open_) & (close.shift(1) > open_.shift(1)) & (open_ > close.shift(1)) & (close < open_.shift(1))
    bull_c = bull_eng.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    bear_c = bear_eng.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (bull_c - bear_c).diff().diff()

def f04_topp_139_weakening_momentum_composite_63d_d2(close: pd.Series) -> pd.Series:
    rsi = _rsi14(close)
    return (-_rolling_slope(rsi, QDAYS)).diff().diff()

def f04_topp_140_distribution_climax_combined_score_63d_d2(close: pd.Series, open_: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    med_v = volume.rolling(YDAYS, min_periods=QDAYS).median()
    dist_c = ((close < open_) & (volume > med_v)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.97 * rmax).astype(float)
    vol_z = _rolling_zscore(volume, YDAYS)
    climax = (near * vol_z).rolling(QDAYS, min_periods=MDAYS).sum()
    return (dist_c * climax).diff().diff()

def f04_topp_141_sentiment_extreme_proxy_score_252d_d2(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    rsi = _rsi14(close)
    rsi_norm = (rsi - 50.0) / 50.0
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (adv * rsi_norm * above).diff().diff()

def f04_topp_142_churning_with_lower_highs_score_63d_d2(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    lower_hh = rmax_21 < rmax_21.shift(MDAYS)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    hi_v = volume > v21
    return (lower_hh & hi_v).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_143_topping_pattern_age_score_252d_d2(high: pd.Series) -> pd.Series:
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    lower_hh = (rmax_21 < rmax_21.shift(MDAYS)) & (rmax_21.shift(MDAYS) >= rmax_21.shift(MDAYS * 2))
    pos = pd.Series(np.arange(len(high)), index=high.index)
    last = pos.where(lower_hh).ffill()
    return (pos - last).diff().diff()

def f04_topp_144_pre_breakdown_setup_score_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin_21 = close.rolling(MDAYS, min_periods=WDAYS).min()
    lower_hh = (rmax_21 < rmax_21.shift(MDAYS)).astype(float)
    at_low = (close <= 1.02 * rmin_21).astype(float)
    return (lower_hh * at_low).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_145_topping_pattern_volume_confirmation_252d_d2(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    below = close < sma
    vz = _rolling_zscore(volume, YDAYS)
    flag = (below & (vz > 1.0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_146_topping_pattern_divergence_count_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax_21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    at_peak = high == rmax_21
    rsi = _rsi14(close)
    div = rsi < rsi.shift(MDAYS)
    return (at_peak & div).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f04_topp_147_topping_failure_resolution_rate_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high_lagged = high.shift(MDAYS) > prior_max.shift(MDAYS)
    failed_now = close < high.shift(MDAYS)
    fail_count = (new_high_lagged & failed_now).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    event_count = new_high_lagged.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(fail_count, event_count + 1.0).diff().diff()

def f04_topp_148_final_high_proximity_score_252d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (1.0 - (_safe_div(close, rmax) - 1.0).abs()).clip(lower=0.0, upper=1.0).diff().diff()

def f04_topp_149_topping_pattern_severity_index_252d_d2(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    upper = high - close.where(close > open_, open_)
    big_wick = upper / rng > 0.5
    bear = close < open_
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high >= 0.97 * rmax
    flag = (near & big_wick & bear).astype(float)
    vol_z = _rolling_zscore(volume, YDAYS).clip(lower=0)
    return (flag * (1.0 + vol_z)).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f04_topp_150_topping_pattern_completeness_index_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:

    def _c2(w):
        if np.isnan(w).any():
            return np.nan
        try:
            return float(np.polyfit(np.arange(len(w)), w, 2)[0])
        except Exception:
            return np.nan
    c2 = close.rolling(YDAYS, min_periods=QDAYS).apply(_c2, raw=True)
    dome = (-c2).clip(lower=0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    prox = _safe_div(close, rmax).clip(upper=1.0)
    vol_div = -_rolling_slope(volume, YDAYS)
    return (dome * prox * vol_div.clip(lower=0)).diff().diff()
TOPPING_PATTERN_D2_REGISTRY_076_150 = {'f04_topp_076_distribution_day_count_252d_d2': {'inputs': ['close', 'open', 'volume'], 'func': f04_topp_076_distribution_day_count_252d_d2}, 'f04_topp_077_stalling_day_count_at_top_252d_d2': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': f04_topp_077_stalling_day_count_at_top_252d_d2}, 'f04_topp_078_churning_day_count_at_top_21d_d2': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f04_topp_078_churning_day_count_at_top_21d_d2}, 'f04_topp_079_percent_distribution_days_after_high_21d_d2': {'inputs': ['close', 'open', 'volume', 'high'], 'func': f04_topp_079_percent_distribution_days_after_high_21d_d2}, 'f04_topp_080_distribution_clustering_score_21d_d2': {'inputs': ['close', 'open', 'volume'], 'func': f04_topp_080_distribution_clustering_score_21d_d2}, 'f04_topp_081_high_volume_red_days_at_high_count_21d_d2': {'inputs': ['close', 'high', 'volume'], 'func': f04_topp_081_high_volume_red_days_at_high_count_21d_d2}, 'f04_topp_082_institutional_distribution_signal_252d_d2': {'inputs': ['close', 'open', 'volume'], 'func': f04_topp_082_institutional_distribution_signal_252d_d2}, 'f04_topp_083_churn_zone_density_at_top_252d_d2': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f04_topp_083_churn_zone_density_at_top_252d_d2}, 'f04_topp_084_volume_at_high_vs_advance_avg_volume_ratio_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f04_topp_084_volume_at_high_vs_advance_avg_volume_ratio_252d_d2}, 'f04_topp_085_narrow_range_at_top_count_21d_d2': {'inputs': ['high', 'low', 'close'], 'func': f04_topp_085_narrow_range_at_top_count_21d_d2}, 'f04_topp_086_inside_day_count_at_high_21d_d2': {'inputs': ['high', 'low'], 'func': f04_topp_086_inside_day_count_at_high_21d_d2}, 'f04_topp_087_outside_day_count_at_high_21d_d2': {'inputs': ['high', 'low'], 'func': f04_topp_087_outside_day_count_at_high_21d_d2}, 'f04_topp_088_mid_range_close_count_at_high_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_088_mid_range_close_count_at_high_21d_d2}, 'f04_topp_089_weak_close_count_at_high_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_089_weak_close_count_at_high_21d_d2}, 'f04_topp_090_strong_close_count_at_high_21d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_090_strong_close_count_at_high_21d_d2}, 'f04_topp_091_rsi_bearish_divergence_score_63d_d2': {'inputs': ['close'], 'func': f04_topp_091_rsi_bearish_divergence_score_63d_d2}, 'f04_topp_092_rsi_negative_divergence_strength_252d_d2': {'inputs': ['close'], 'func': f04_topp_092_rsi_negative_divergence_strength_252d_d2}, 'f04_topp_093_rsi_overbought_persistence_count_63d_d2': {'inputs': ['close'], 'func': f04_topp_093_rsi_overbought_persistence_count_63d_d2}, 'f04_topp_094_rsi_failure_swing_count_63d_d2': {'inputs': ['close'], 'func': f04_topp_094_rsi_failure_swing_count_63d_d2}, 'f04_topp_095_rsi_bear_divergence_count_63d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_095_rsi_bear_divergence_count_63d_d2}, 'f04_topp_096_macd_bearish_divergence_score_63d_d2': {'inputs': ['close'], 'func': f04_topp_096_macd_bearish_divergence_score_63d_d2}, 'f04_topp_097_macd_hist_lower_high_count_63d_d2': {'inputs': ['close'], 'func': f04_topp_097_macd_hist_lower_high_count_63d_d2}, 'f04_topp_098_macd_signal_cross_below_count_63d_d2': {'inputs': ['close'], 'func': f04_topp_098_macd_signal_cross_below_count_63d_d2}, 'f04_topp_099_momentum_peak_before_price_peak_lag_63d_d2': {'inputs': ['close'], 'func': f04_topp_099_momentum_peak_before_price_peak_lag_63d_d2}, 'f04_topp_100_stochastic_overbought_persistence_count_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_100_stochastic_overbought_persistence_count_63d_d2}, 'f04_topp_101_stochastic_bear_divergence_score_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_101_stochastic_bear_divergence_score_63d_d2}, 'f04_topp_102_cci_overextension_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_102_cci_overextension_count_252d_d2}, 'f04_topp_103_williams_r_overbought_persistence_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_103_williams_r_overbought_persistence_63d_d2}, 'f04_topp_104_roc_bearish_divergence_count_63d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_104_roc_bearish_divergence_count_63d_d2}, 'f04_topp_105_momentum_lower_high_count_at_price_higher_high_63d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_105_momentum_lower_high_count_at_price_higher_high_63d_d2}, 'f04_topp_106_sma21_break_below_after_high_count_21d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_106_sma21_break_below_after_high_count_21d_d2}, 'f04_topp_107_sma63_break_below_after_high_count_63d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_107_sma63_break_below_after_high_count_63d_d2}, 'f04_topp_108_sma252_break_below_after_high_count_252d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_108_sma252_break_below_after_high_count_252d_d2}, 'f04_topp_109_days_since_close_first_crossed_below_sma21_after_252d_high_d2': {'inputs': ['close', 'high'], 'func': f04_topp_109_days_since_close_first_crossed_below_sma21_after_252d_high_d2}, 'f04_topp_110_days_since_close_first_crossed_below_sma63_d2': {'inputs': ['close'], 'func': f04_topp_110_days_since_close_first_crossed_below_sma63_d2}, 'f04_topp_111_trend_line_break_count_252d_d2': {'inputs': ['low'], 'func': f04_topp_111_trend_line_break_count_252d_d2}, 'f04_topp_112_lower_low_first_appearance_days_since_252d_d2': {'inputs': ['low'], 'func': f04_topp_112_lower_low_first_appearance_days_since_252d_d2}, 'f04_topp_113_lower_high_first_appearance_days_since_252d_d2': {'inputs': ['high'], 'func': f04_topp_113_lower_high_first_appearance_days_since_252d_d2}, 'f04_topp_114_swing_low_break_count_at_top_252d_d2': {'inputs': ['low', 'high'], 'func': f04_topp_114_swing_low_break_count_at_top_252d_d2}, 'f04_topp_115_first_lower_low_after_252d_high_days_since_d2': {'inputs': ['low', 'high'], 'func': f04_topp_115_first_lower_low_after_252d_high_days_since_d2}, 'f04_topp_116_first_lower_high_after_252d_high_days_since_d2': {'inputs': ['high'], 'func': f04_topp_116_first_lower_high_after_252d_high_days_since_d2}, 'f04_topp_117_channel_break_below_score_63d_d2': {'inputs': ['close', 'low'], 'func': f04_topp_117_channel_break_below_score_63d_d2}, 'f04_topp_118_trendline_violation_distance_252d_d2': {'inputs': ['close'], 'func': f04_topp_118_trendline_violation_distance_252d_d2}, 'f04_topp_119_trend_break_volume_confirmation_252d_d2': {'inputs': ['close', 'volume'], 'func': f04_topp_119_trend_break_volume_confirmation_252d_d2}, 'f04_topp_120_break_below_anchored_vwap_count_252d_d2': {'inputs': ['close', 'volume'], 'func': f04_topp_120_break_below_anchored_vwap_count_252d_d2}, 'f04_topp_121_climax_top_volume_score_63d_d2': {'inputs': ['close', 'volume', 'high'], 'func': f04_topp_121_climax_top_volume_score_63d_d2}, 'f04_topp_122_climax_top_one_day_reversal_count_21d_d2': {'inputs': ['open', 'close', 'high'], 'func': f04_topp_122_climax_top_one_day_reversal_count_21d_d2}, 'f04_topp_123_exhaustion_gap_at_top_count_63d_d2': {'inputs': ['open', 'close', 'high'], 'func': f04_topp_123_exhaustion_gap_at_top_count_63d_d2}, 'f04_topp_124_island_reversal_count_63d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_124_island_reversal_count_63d_d2}, 'f04_topp_125_key_reversal_day_count_at_high_63d_d2': {'inputs': ['close', 'high', 'low'], 'func': f04_topp_125_key_reversal_day_count_at_high_63d_d2}, 'f04_topp_126_outside_engulfing_bearish_at_high_count_63d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_126_outside_engulfing_bearish_at_high_count_63d_d2}, 'f04_topp_127_dark_cloud_cover_count_at_high_63d_d2': {'inputs': ['open', 'close', 'high'], 'func': f04_topp_127_dark_cloud_cover_count_at_high_63d_d2}, 'f04_topp_128_evening_star_count_at_high_63d_d2': {'inputs': ['open', 'close', 'high'], 'func': f04_topp_128_evening_star_count_at_high_63d_d2}, 'f04_topp_129_hanging_man_count_at_high_63d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_129_hanging_man_count_at_high_63d_d2}, 'f04_topp_130_long_upper_wick_at_high_count_63d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_130_long_upper_wick_at_high_count_63d_d2}, 'f04_topp_131_doji_at_high_count_21d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_131_doji_at_high_count_21d_d2}, 'f04_topp_132_spinning_top_at_high_count_21d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_132_spinning_top_at_high_count_21d_d2}, 'f04_topp_133_bearish_star_pattern_count_63d_d2': {'inputs': ['open', 'close', 'high'], 'func': f04_topp_133_bearish_star_pattern_count_63d_d2}, 'f04_topp_134_three_black_crows_count_63d_d2': {'inputs': ['open', 'close', 'high'], 'func': f04_topp_134_three_black_crows_count_63d_d2}, 'f04_topp_135_abandoned_baby_top_count_63d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_135_abandoned_baby_top_count_63d_d2}, 'f04_topp_136_multi_signal_top_score_252d_d2': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': f04_topp_136_multi_signal_top_score_252d_d2}, 'f04_topp_137_topping_pattern_density_63d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_137_topping_pattern_density_63d_d2}, 'f04_topp_138_bullish_to_bearish_pattern_ratio_63d_d2': {'inputs': ['open', 'close', 'high', 'low'], 'func': f04_topp_138_bullish_to_bearish_pattern_ratio_63d_d2}, 'f04_topp_139_weakening_momentum_composite_63d_d2': {'inputs': ['close'], 'func': f04_topp_139_weakening_momentum_composite_63d_d2}, 'f04_topp_140_distribution_climax_combined_score_63d_d2': {'inputs': ['close', 'open', 'high', 'volume'], 'func': f04_topp_140_distribution_climax_combined_score_63d_d2}, 'f04_topp_141_sentiment_extreme_proxy_score_252d_d2': {'inputs': ['close', 'low'], 'func': f04_topp_141_sentiment_extreme_proxy_score_252d_d2}, 'f04_topp_142_churning_with_lower_highs_score_63d_d2': {'inputs': ['close', 'high', 'volume'], 'func': f04_topp_142_churning_with_lower_highs_score_63d_d2}, 'f04_topp_143_topping_pattern_age_score_252d_d2': {'inputs': ['high'], 'func': f04_topp_143_topping_pattern_age_score_252d_d2}, 'f04_topp_144_pre_breakdown_setup_score_63d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_144_pre_breakdown_setup_score_63d_d2}, 'f04_topp_145_topping_pattern_volume_confirmation_252d_d2': {'inputs': ['close', 'high', 'volume'], 'func': f04_topp_145_topping_pattern_volume_confirmation_252d_d2}, 'f04_topp_146_topping_pattern_divergence_count_63d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_146_topping_pattern_divergence_count_63d_d2}, 'f04_topp_147_topping_failure_resolution_rate_252d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_147_topping_failure_resolution_rate_252d_d2}, 'f04_topp_148_final_high_proximity_score_252d_d2': {'inputs': ['close', 'high'], 'func': f04_topp_148_final_high_proximity_score_252d_d2}, 'f04_topp_149_topping_pattern_severity_index_252d_d2': {'inputs': ['close', 'open', 'high', 'low', 'volume'], 'func': f04_topp_149_topping_pattern_severity_index_252d_d2}, 'f04_topp_150_topping_pattern_completeness_index_252d_d2': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f04_topp_150_topping_pattern_completeness_index_252d_d2}}
