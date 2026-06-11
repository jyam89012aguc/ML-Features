"""Auto-generated D2 wrappers from volume_blowoff_at_peak__base__076_150.py.

Each function inlines the base body and appends .diff() chained 2 time(s)."""
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

def _rolling_vwap(price, volume, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    num = (price * volume).rolling(n, min_periods=min_periods).sum()
    den = volume.rolling(n, min_periods=min_periods).sum().replace(0, np.nan)
    return num / den

def f05_vbpk_076_anchored_252d_vwap_deviation_z_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, YDAYS)
    dev = _safe_div(close, vw) - 1.0
    return _rolling_zscore(dev, YDAYS).diff().diff()

def f05_vbpk_077_anchored_63d_vwap_deviation_z_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    dev = _safe_div(close, vw) - 1.0
    return _rolling_zscore(dev, QDAYS).diff().diff()

def f05_vbpk_078_anchored_21d_vwap_deviation_z_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, MDAYS)
    dev = _safe_div(close, vw) - 1.0
    return _rolling_zscore(dev, QDAYS).diff().diff()

def f05_vbpk_079_vwap_slope_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    return _rolling_slope(vw, QDAYS).diff().diff()

def f05_vbpk_080_vwap_slope_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, MDAYS)
    return _rolling_slope(vw, MDAYS).diff().diff()

def f05_vbpk_081_dist_to_vwap_63d_atr_normalized_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    atr = _atr(high, low, close, MDAYS)
    return ((close - vw) / atr.replace(0, np.nan)).diff().diff()

def f05_vbpk_082_dist_to_vwap_21d_atr_normalized_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, MDAYS)
    atr = _atr(high, low, close, MDAYS)
    return ((close - vw) / atr.replace(0, np.nan)).diff().diff()

def f05_vbpk_083_excess_vwap_252d_dollars_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, YDAYS)
    return (close - vw).diff().diff()

def f05_vbpk_084_cum_vwap_deviation_integral_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    dev = close - vw
    return dev.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f05_vbpk_085_pct_bars_closing_above_vwap63_in_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    flag = (close > vw).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f05_vbpk_086_vwap_21d_cross_up_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, MDAYS)
    above = (close > vw).astype(int)
    cross_up = ((above == 1) & (above.shift(1) == 0)).astype(float)
    return cross_up.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f05_vbpk_087_above_vwap_dollar_vol_share_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    dv = close * volume
    above = (close > vw).astype(float)
    return _safe_div((dv * above).rolling(QDAYS, min_periods=MDAYS).sum(), dv.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()

def f05_vbpk_088_vwap_deviation_peak_z_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, MDAYS)
    dev = close - vw
    peak = dev.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_zscore(peak, YDAYS).diff().diff()

def f05_vbpk_089_typical_price_vwap_deviation_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    vw = _rolling_vwap(tp, volume, QDAYS)
    return (_safe_div(tp, vw) - 1.0).diff().diff()

def f05_vbpk_090_vwap5_to_vwap63_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    v5 = _rolling_vwap(close, volume, WDAYS)
    v63 = _rolling_vwap(close, volume, QDAYS)
    return (_safe_div(v5, v63) - 1.0).diff().diff()

def f05_vbpk_091_vwap21_to_vwap252_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    v21 = _rolling_vwap(close, volume, MDAYS)
    v252 = _rolling_vwap(close, volume, YDAYS)
    return (_safe_div(v21, v252) - 1.0).diff().diff()

def f05_vbpk_092_vwap_slope_acceleration_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    sl = _rolling_slope(vw, QDAYS)
    return sl.diff().diff().diff()

def f05_vbpk_093_hlc_midpoint_vwap_deviation_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mp = (high + low + close) / 3.0
    vw = _rolling_vwap(close, volume, QDAYS)
    return (_safe_div(mp, vw) - 1.0).diff().diff()

def f05_vbpk_094_volume_tilt_above_vs_below_vwap_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    above = (close > vw).astype(float)
    above_v = (volume * above).rolling(MDAYS, min_periods=WDAYS).sum()
    below_v = (volume * (1.0 - above)).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = above_v + below_v
    return _safe_div(above_v - below_v, tot).diff().diff()

def f05_vbpk_095_above_vwap_dollar_vol_ratio_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    dv = close * volume
    above = (close > vw).astype(float)
    return _safe_div((dv * above).rolling(QDAYS, min_periods=MDAYS).sum(), (dv * (1.0 - above)).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()

def f05_vbpk_096_log_vwap_deviation_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, YDAYS)
    return (_safe_log(close) - _safe_log(vw)).diff().diff()

def f05_vbpk_097_vwap_anchored_at_recent_max_vol_dev_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, volume, QDAYS)
    return (_safe_div(close, vw) - 1.0).diff().diff()

def f05_vbpk_098_anchored_vwap_from_252d_max_day_dev_d2(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = high > rmax
    cum_pv = (close * volume).cumsum()
    cum_v = volume.cumsum()
    anchor_pv = cum_pv.where(is_nh).ffill()
    anchor_v = cum_v.where(is_nh).ffill()
    num = cum_pv - anchor_pv
    den = (cum_v - anchor_v).replace(0, np.nan)
    avwap = num / den
    return (_safe_div(close, avwap) - 1.0).diff().diff()

def f05_vbpk_099_anchored_vwap_from_63d_max_day_dev_d2(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = high > rmax
    cum_pv = (close * volume).cumsum()
    cum_v = volume.cumsum()
    anchor_pv = cum_pv.where(is_nh).ffill()
    anchor_v = cum_v.where(is_nh).ffill()
    num = cum_pv - anchor_pv
    den = (cum_v - anchor_v).replace(0, np.nan)
    avwap = num / den
    return (_safe_div(close, avwap) - 1.0).diff().diff()

def f05_vbpk_100_dollar_vwap_deviation_z_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vw = _rolling_vwap(close, close * volume, YDAYS)
    dev = close - vw
    return _rolling_zscore(dev, YDAYS).diff().diff()

def f05_vbpk_101_dollar_volume_mean_5d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (close * volume).rolling(WDAYS, min_periods=2).mean().diff().diff()

def f05_vbpk_102_dollar_volume_mean_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (close * volume).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f05_vbpk_103_dollar_volume_mean_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (close * volume).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f05_vbpk_104_dollar_volume_momentum_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_log(close * volume).diff(MDAYS).diff().diff()

def f05_vbpk_105_dollar_volume_slope_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _rolling_slope(close * volume, QDAYS).diff().diff()

def f05_vbpk_106_dollar_volume_herfindahl_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume

    def _h(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        sh = w / s
        return float(np.sum(sh ** 2))
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_h, raw=True).diff().diff()

def f05_vbpk_107_dollar_volume_gini_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume

    def _g(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)
        n = len(s)
        if s.sum() == 0:
            return np.nan
        cum = np.cumsum(s)
        return float((n + 1 - 2 * cum.sum() / cum[-1]) / n)
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_g, raw=True).diff().diff()

def f05_vbpk_108_peak_dollar_volume_ratio_to_mean_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return _safe_div(dv.rolling(QDAYS, min_periods=MDAYS).max(), dv.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f05_vbpk_109_top5_dollar_volume_share_of_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume

    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        return float(np.sort(w)[-5:].sum() / s)
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_sh, raw=True).diff().diff()

def f05_vbpk_110_top10_dollar_volume_share_of_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume

    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        return float(np.sort(w)[-10:].sum() / s)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_sh, raw=True).diff().diff()

def f05_vbpk_111_log_dollar_volume_range_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return (_safe_log(dv.rolling(QDAYS, min_periods=MDAYS).max()) - _safe_log(dv.rolling(QDAYS, min_periods=MDAYS).min())).diff().diff()

def f05_vbpk_112_dollar_volume_green_vs_red_ratio_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    chg = close.diff()
    up = dv.where(chg > 0).fillna(0)
    dn = dv.where(chg < 0).fillna(0)
    return _safe_div(up.rolling(MDAYS, min_periods=WDAYS).sum(), dn.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff()

def f05_vbpk_113_dollar_volume_on_new_high_bars_ratio_63d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = (high > prior_max).astype(float)
    dv = close * volume
    return _safe_div((dv * is_nh).rolling(QDAYS, min_periods=MDAYS).sum(), (dv * (1.0 - is_nh)).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()

def f05_vbpk_114_dollar_volume_per_pct_gained_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv_sum = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    r = _safe_log(close).diff(MDAYS).abs()
    return _safe_div(dv_sum, r).diff().diff()

def f05_vbpk_115_dollar_volume_per_atr_move_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv_sum = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    tr_sum = _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dv_sum, tr_sum).diff().diff()

def f05_vbpk_116_coefficient_of_variation_volume_63d_d2(volume: pd.Series) -> pd.Series:
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(sd, m).diff().diff()

def f05_vbpk_117_variance_log_volume_63d_d2(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).rolling(QDAYS, min_periods=MDAYS).var().diff().diff()

def f05_vbpk_118_turnover_proxy_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv_sum = (close * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    c_mean = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(dv_sum, c_mean).diff().diff()

def f05_vbpk_119_dollar_volume_zscore_log_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_log(close * volume), YDAYS).diff().diff()

def f05_vbpk_120_dollar_volume_on_biggest_gain_z_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = close.pct_change()
    dv = close * volume

    def _f(w_ret, w_dv):
        if np.isnan(w_ret).any() or np.isnan(w_dv).any():
            return np.nan
        return float(w_dv[int(np.argmax(w_ret))])
    peak_dv = pd.Series([_f(r.iloc[max(0, i - MDAYS + 1):i + 1].values, dv.iloc[max(0, i - MDAYS + 1):i + 1].values) if i >= WDAYS else np.nan for i in range(len(r))], index=r.index)
    m = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = dv.rolling(YDAYS, min_periods=QDAYS).std()
    return ((peak_dv - m) / sd.replace(0, np.nan)).diff().diff()

def f05_vbpk_121_dollar_volume_velocity_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    sl = _rolling_slope(dv, MDAYS)
    m = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(sl, m).diff().diff()

def f05_vbpk_122_dollar_volume_regime_shift_21_vs_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    b = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_log(a) - _safe_log(b)).diff().diff()

def f05_vbpk_123_dollar_volume_runoff_z_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    peak = dv.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_zscore(peak, YDAYS).diff().diff()

def f05_vbpk_124_dollar_volume_single_bar_peak_z_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    peak = dv.rolling(QDAYS, min_periods=MDAYS).max()
    return _rolling_zscore(peak, YDAYS).diff().diff()

def f05_vbpk_125_dollar_volume_skewness_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume

    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / sd ** 3)
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_sk, raw=True).diff().diff()

def f05_vbpk_126_gap_up_high_vol_reversal_count_21d_d2(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_up = open_ > high.shift(1)
    reverse = close < open_
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (gap_up & reverse & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_127_gap_up_close_below_open_high_vol_21d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_up = open_ > close.shift(1)
    reverse = close < open_
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    flag = (gap_up & reverse & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_128_shooting_star_high_vol_count_21d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - close.clip(lower=open_)
    body_small = body / rng < 0.3
    wick_long = upper / rng > 0.6
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (body_small & wick_long & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_129_bearish_engulf_high_vol_count_63d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prev_up = close.shift(1) > open_.shift(1)
    cur_down = close < open_
    engulf = (open_ > close.shift(1)) & (close < open_.shift(1))
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    flag = (prev_up & cur_down & engulf & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f05_vbpk_130_wide_range_high_vol_bar_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    wide = (high - low) / atr.replace(0, np.nan) > 2.0
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (wide & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_131_wide_range_up_bar_count_5d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    wide = high - low > 1.5 * atr
    up = close > open_
    flag = (wide & up).astype(float)
    return flag.rolling(WDAYS, min_periods=2).sum().diff().diff()

def f05_vbpk_132_avg_high_vol_up_bar_range_21d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    up = close > open_
    rng = (high - low).where(big & up)
    return rng.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f05_vbpk_133_avg_high_vol_up_bar_close_position_21d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    up = close > open_
    pos = ((close - low) / (high - low).replace(0, np.nan)).where(big & up)
    return pos.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f05_vbpk_134_doji_on_max_vol_bar_count_21d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    doji = body / rng < 0.1
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (doji & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_135_high_vol_upthrust_count_21d_d2(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    reverse = close < open_
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (nh & reverse & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_136_exhaustion_gap_at_new_high_count_21d_d2(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    gap = open_ > high.shift(1)
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 3.0 * avg
    weak_close = close - open_ < 0
    flag = (nh & gap & big & weak_close).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_137_churning_bar_count_21d_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    avg_v = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > 2.0 * avg_v
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.8
    flag = (big_v & narrow).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_138_low_progress_high_vol_up_bar_count_21d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rel = (close - open_) / open_.replace(0, np.nan)
    weak = (rel > 0) & (rel < 0.005)
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (weak & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_139_cluster_2sigma_vol_bars_in_21d_d2(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    cluster = (big & big.shift(1).fillna(False)).astype(float)
    return cluster.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_140_consecutive_2sigma_vol_max_63d_d2(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = (z > 2.0).astype(int)
    grp = (big == 0).cumsum()
    streak = big.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max().diff().diff()

def f05_vbpk_141_composite_blowoff_cluster_index_21d_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS).clip(lower=0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.97
    score = z * near.astype(float)
    return score.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_142_peak_3sigma_vol_in_5d_d2(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = (z > 3.0).astype(float)
    return big.rolling(WDAYS, min_periods=2).max().diff().diff()

def f05_vbpk_143_peak_3sigma_vol_in_21d_d2(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = (z > 3.0).astype(float)
    return big.rolling(MDAYS, min_periods=WDAYS).max().diff().diff()

def f05_vbpk_144_multi_bar_reversal_post_climax_5d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    climax_5d_ago = z.shift(WDAYS) > 3.0
    ret_5d = _safe_log(close).diff(WDAYS)
    return ret_5d.where(climax_5d_ago).diff().diff()

def f05_vbpk_145_bull_trap_signature_21d_d2(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    weak = close < open_
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (nh & weak & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f05_vbpk_146_pct_21d_bars_vol_2x_sma252_d2(volume: pd.Series) -> pd.Series:
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume > 2.0 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f05_vbpk_147_pct_21d_bars_vol_5x_sma252_d2(volume: pd.Series) -> pd.Series:
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume > 5.0 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f05_vbpk_148_nearby_high_climax_composite_z_21d_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan)
    score = z * near
    m21 = score.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(m21, YDAYS).diff().diff()

def f05_vbpk_149_blowoff_escalation_score_21d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    s5 = _rolling_slope(lv, WDAYS)
    s21 = _rolling_slope(lv, MDAYS)
    return (s5 - s21).diff().diff()

def f05_vbpk_150_multi_criteria_blowoff_score_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    atr = _atr(high, low, close, MDAYS)
    rng = high - low
    rng_norm = rng / atr.replace(0, np.nan)
    pos = (close - low) / rng.replace(0, np.nan)
    score = z + rng_norm + (pos - 1.0)
    return score.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()
VOLUME_BLOWOFF_AT_PEAK_D2_REGISTRY_076_150 = {'f05_vbpk_076_anchored_252d_vwap_deviation_z_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_076_anchored_252d_vwap_deviation_z_d2}, 'f05_vbpk_077_anchored_63d_vwap_deviation_z_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_077_anchored_63d_vwap_deviation_z_d2}, 'f05_vbpk_078_anchored_21d_vwap_deviation_z_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_078_anchored_21d_vwap_deviation_z_d2}, 'f05_vbpk_079_vwap_slope_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_079_vwap_slope_63d_d2}, 'f05_vbpk_080_vwap_slope_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_080_vwap_slope_21d_d2}, 'f05_vbpk_081_dist_to_vwap_63d_atr_normalized_d2': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f05_vbpk_081_dist_to_vwap_63d_atr_normalized_d2}, 'f05_vbpk_082_dist_to_vwap_21d_atr_normalized_d2': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f05_vbpk_082_dist_to_vwap_21d_atr_normalized_d2}, 'f05_vbpk_083_excess_vwap_252d_dollars_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_083_excess_vwap_252d_dollars_d2}, 'f05_vbpk_084_cum_vwap_deviation_integral_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_084_cum_vwap_deviation_integral_63d_d2}, 'f05_vbpk_085_pct_bars_closing_above_vwap63_in_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_085_pct_bars_closing_above_vwap63_in_21d_d2}, 'f05_vbpk_086_vwap_21d_cross_up_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_086_vwap_21d_cross_up_count_63d_d2}, 'f05_vbpk_087_above_vwap_dollar_vol_share_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_087_above_vwap_dollar_vol_share_63d_d2}, 'f05_vbpk_088_vwap_deviation_peak_z_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_088_vwap_deviation_peak_z_21d_d2}, 'f05_vbpk_089_typical_price_vwap_deviation_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f05_vbpk_089_typical_price_vwap_deviation_63d_d2}, 'f05_vbpk_090_vwap5_to_vwap63_ratio_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_090_vwap5_to_vwap63_ratio_d2}, 'f05_vbpk_091_vwap21_to_vwap252_ratio_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_091_vwap21_to_vwap252_ratio_d2}, 'f05_vbpk_092_vwap_slope_acceleration_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_092_vwap_slope_acceleration_63d_d2}, 'f05_vbpk_093_hlc_midpoint_vwap_deviation_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f05_vbpk_093_hlc_midpoint_vwap_deviation_63d_d2}, 'f05_vbpk_094_volume_tilt_above_vs_below_vwap_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_094_volume_tilt_above_vs_below_vwap_21d_d2}, 'f05_vbpk_095_above_vwap_dollar_vol_ratio_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_095_above_vwap_dollar_vol_ratio_63d_d2}, 'f05_vbpk_096_log_vwap_deviation_252d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_096_log_vwap_deviation_252d_d2}, 'f05_vbpk_097_vwap_anchored_at_recent_max_vol_dev_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_097_vwap_anchored_at_recent_max_vol_dev_63d_d2}, 'f05_vbpk_098_anchored_vwap_from_252d_max_day_dev_d2': {'inputs': ['close', 'high', 'volume'], 'func': f05_vbpk_098_anchored_vwap_from_252d_max_day_dev_d2}, 'f05_vbpk_099_anchored_vwap_from_63d_max_day_dev_d2': {'inputs': ['close', 'high', 'volume'], 'func': f05_vbpk_099_anchored_vwap_from_63d_max_day_dev_d2}, 'f05_vbpk_100_dollar_vwap_deviation_z_252d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_100_dollar_vwap_deviation_z_252d_d2}, 'f05_vbpk_101_dollar_volume_mean_5d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_101_dollar_volume_mean_5d_d2}, 'f05_vbpk_102_dollar_volume_mean_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_102_dollar_volume_mean_21d_d2}, 'f05_vbpk_103_dollar_volume_mean_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_103_dollar_volume_mean_63d_d2}, 'f05_vbpk_104_dollar_volume_momentum_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_104_dollar_volume_momentum_21d_d2}, 'f05_vbpk_105_dollar_volume_slope_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_105_dollar_volume_slope_63d_d2}, 'f05_vbpk_106_dollar_volume_herfindahl_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_106_dollar_volume_herfindahl_63d_d2}, 'f05_vbpk_107_dollar_volume_gini_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_107_dollar_volume_gini_63d_d2}, 'f05_vbpk_108_peak_dollar_volume_ratio_to_mean_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_108_peak_dollar_volume_ratio_to_mean_63d_d2}, 'f05_vbpk_109_top5_dollar_volume_share_of_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_109_top5_dollar_volume_share_of_63d_d2}, 'f05_vbpk_110_top10_dollar_volume_share_of_252d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_110_top10_dollar_volume_share_of_252d_d2}, 'f05_vbpk_111_log_dollar_volume_range_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_111_log_dollar_volume_range_63d_d2}, 'f05_vbpk_112_dollar_volume_green_vs_red_ratio_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_112_dollar_volume_green_vs_red_ratio_21d_d2}, 'f05_vbpk_113_dollar_volume_on_new_high_bars_ratio_63d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f05_vbpk_113_dollar_volume_on_new_high_bars_ratio_63d_d2}, 'f05_vbpk_114_dollar_volume_per_pct_gained_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_114_dollar_volume_per_pct_gained_21d_d2}, 'f05_vbpk_115_dollar_volume_per_atr_move_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f05_vbpk_115_dollar_volume_per_atr_move_21d_d2}, 'f05_vbpk_116_coefficient_of_variation_volume_63d_d2': {'inputs': ['volume'], 'func': f05_vbpk_116_coefficient_of_variation_volume_63d_d2}, 'f05_vbpk_117_variance_log_volume_63d_d2': {'inputs': ['volume'], 'func': f05_vbpk_117_variance_log_volume_63d_d2}, 'f05_vbpk_118_turnover_proxy_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_118_turnover_proxy_63d_d2}, 'f05_vbpk_119_dollar_volume_zscore_log_252d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_119_dollar_volume_zscore_log_252d_d2}, 'f05_vbpk_120_dollar_volume_on_biggest_gain_z_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_120_dollar_volume_on_biggest_gain_z_21d_d2}, 'f05_vbpk_121_dollar_volume_velocity_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_121_dollar_volume_velocity_21d_d2}, 'f05_vbpk_122_dollar_volume_regime_shift_21_vs_252_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_122_dollar_volume_regime_shift_21_vs_252_d2}, 'f05_vbpk_123_dollar_volume_runoff_z_21d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_123_dollar_volume_runoff_z_21d_d2}, 'f05_vbpk_124_dollar_volume_single_bar_peak_z_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_124_dollar_volume_single_bar_peak_z_63d_d2}, 'f05_vbpk_125_dollar_volume_skewness_63d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_125_dollar_volume_skewness_63d_d2}, 'f05_vbpk_126_gap_up_high_vol_reversal_count_21d_d2': {'inputs': ['open', 'high', 'close', 'volume'], 'func': f05_vbpk_126_gap_up_high_vol_reversal_count_21d_d2}, 'f05_vbpk_127_gap_up_close_below_open_high_vol_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f05_vbpk_127_gap_up_close_below_open_high_vol_21d_d2}, 'f05_vbpk_128_shooting_star_high_vol_count_21d_d2': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f05_vbpk_128_shooting_star_high_vol_count_21d_d2}, 'f05_vbpk_129_bearish_engulf_high_vol_count_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f05_vbpk_129_bearish_engulf_high_vol_count_63d_d2}, 'f05_vbpk_130_wide_range_high_vol_bar_count_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f05_vbpk_130_wide_range_high_vol_bar_count_21d_d2}, 'f05_vbpk_131_wide_range_up_bar_count_5d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f05_vbpk_131_wide_range_up_bar_count_5d_d2}, 'f05_vbpk_132_avg_high_vol_up_bar_range_21d_d2': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f05_vbpk_132_avg_high_vol_up_bar_range_21d_d2}, 'f05_vbpk_133_avg_high_vol_up_bar_close_position_21d_d2': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f05_vbpk_133_avg_high_vol_up_bar_close_position_21d_d2}, 'f05_vbpk_134_doji_on_max_vol_bar_count_21d_d2': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f05_vbpk_134_doji_on_max_vol_bar_count_21d_d2}, 'f05_vbpk_135_high_vol_upthrust_count_21d_d2': {'inputs': ['open', 'high', 'close', 'volume'], 'func': f05_vbpk_135_high_vol_upthrust_count_21d_d2}, 'f05_vbpk_136_exhaustion_gap_at_new_high_count_21d_d2': {'inputs': ['open', 'high', 'close', 'volume'], 'func': f05_vbpk_136_exhaustion_gap_at_new_high_count_21d_d2}, 'f05_vbpk_137_churning_bar_count_21d_d2': {'inputs': ['open', 'high', 'low', 'close', 'volume'], 'func': f05_vbpk_137_churning_bar_count_21d_d2}, 'f05_vbpk_138_low_progress_high_vol_up_bar_count_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f05_vbpk_138_low_progress_high_vol_up_bar_count_21d_d2}, 'f05_vbpk_139_cluster_2sigma_vol_bars_in_21d_d2': {'inputs': ['volume'], 'func': f05_vbpk_139_cluster_2sigma_vol_bars_in_21d_d2}, 'f05_vbpk_140_consecutive_2sigma_vol_max_63d_d2': {'inputs': ['volume'], 'func': f05_vbpk_140_consecutive_2sigma_vol_max_63d_d2}, 'f05_vbpk_141_composite_blowoff_cluster_index_21d_d2': {'inputs': ['high', 'volume'], 'func': f05_vbpk_141_composite_blowoff_cluster_index_21d_d2}, 'f05_vbpk_142_peak_3sigma_vol_in_5d_d2': {'inputs': ['volume'], 'func': f05_vbpk_142_peak_3sigma_vol_in_5d_d2}, 'f05_vbpk_143_peak_3sigma_vol_in_21d_d2': {'inputs': ['volume'], 'func': f05_vbpk_143_peak_3sigma_vol_in_21d_d2}, 'f05_vbpk_144_multi_bar_reversal_post_climax_5d_d2': {'inputs': ['close', 'volume'], 'func': f05_vbpk_144_multi_bar_reversal_post_climax_5d_d2}, 'f05_vbpk_145_bull_trap_signature_21d_d2': {'inputs': ['open', 'high', 'close', 'volume'], 'func': f05_vbpk_145_bull_trap_signature_21d_d2}, 'f05_vbpk_146_pct_21d_bars_vol_2x_sma252_d2': {'inputs': ['volume'], 'func': f05_vbpk_146_pct_21d_bars_vol_2x_sma252_d2}, 'f05_vbpk_147_pct_21d_bars_vol_5x_sma252_d2': {'inputs': ['volume'], 'func': f05_vbpk_147_pct_21d_bars_vol_5x_sma252_d2}, 'f05_vbpk_148_nearby_high_climax_composite_z_21d_d2': {'inputs': ['high', 'volume'], 'func': f05_vbpk_148_nearby_high_climax_composite_z_21d_d2}, 'f05_vbpk_149_blowoff_escalation_score_21d_d2': {'inputs': ['volume'], 'func': f05_vbpk_149_blowoff_escalation_score_21d_d2}, 'f05_vbpk_150_multi_criteria_blowoff_score_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f05_vbpk_150_multi_criteria_blowoff_score_21d_d2}}
