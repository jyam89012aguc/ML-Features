"""Auto-generated D2 wrappers from distribution_signature__base__001_075.py.

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

def f07_dsig_001_up_minus_down_vol_zscore_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return _rolling_zscore(net, MDAYS).diff().diff()

def f07_dsig_002_up_minus_down_vol_zscore_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return _rolling_zscore(net, QDAYS).diff().diff()

def f07_dsig_003_down_vol_fraction_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    dn = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dn, tot).diff().diff()

def f07_dsig_004_down_vol_fraction_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    dn = volume.where(chg < 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    tot = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dn, tot).diff().diff()

def f07_dsig_005_down_vol_slope_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    dn = volume.where(chg < 0, 0)
    return _rolling_slope(dn, QDAYS).diff().diff()

def f07_dsig_006_down_vol_zscore_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    dn = volume.where(chg < 0, 0)
    return _rolling_zscore(dn, MDAYS).diff().diff()

def f07_dsig_007_down_vol_zscore_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    dn = volume.where(chg < 0, 0)
    return _rolling_zscore(dn, QDAYS).diff().diff()

def f07_dsig_008_up_vol_zscore_decline_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up = volume.where(chg > 0, 0)
    return _rolling_zscore(up, QDAYS).diff().diff()

def f07_dsig_009_up_vol_regression_slope_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up = volume.where(chg > 0, 0)
    return _rolling_slope(up, QDAYS).diff().diff()

def f07_dsig_010_up_minus_down_vol_cumulative_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return net.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_011_up_minus_down_vol_slope_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return _rolling_slope(net, QDAYS).diff().diff()

def f07_dsig_012_supply_ratio_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dn, up).diff().diff()

def f07_dsig_013_supply_ratio_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up = volume.where(chg > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    dn = volume.where(chg < 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dn, up).diff().diff()

def f07_dsig_014_supply_ratio_slope_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(dn, up)
    return _rolling_slope(ratio, QDAYS).diff().diff()

def f07_dsig_015_down_vol_days_fraction_21d_d2(close: pd.Series) -> pd.Series:
    flag = (close.diff() < 0).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_016_down_vol_days_fraction_63d_d2(close: pd.Series) -> pd.Series:
    flag = (close.diff() < 0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_017_red_vs_green_vol_mean_21d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    red = volume.where(close < open_)
    green = volume.where(close > open_)
    return _safe_div(red.rolling(MDAYS, min_periods=WDAYS).mean(), green.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff()

def f07_dsig_018_red_vs_green_vol_mean_63d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    red = volume.where(close < open_)
    green = volume.where(close > open_)
    return _safe_div(red.rolling(QDAYS, min_periods=MDAYS).mean(), green.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f07_dsig_019_red_bar_vol_slope_63d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    red = volume.where(close < open_, 0)
    return _rolling_slope(red, QDAYS).diff().diff()

def f07_dsig_020_avg_vol_close_below_open_21d_z_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    red = volume.where(close < open_)
    m = red.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(m, YDAYS).diff().diff()

def f07_dsig_021_avg_vol_close_below_open_63d_z_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    red = volume.where(close < open_)
    m = red.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(m, YDAYS).diff().diff()

def f07_dsig_022_close_below_open_vol_weighted_pct_63d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    red_v = volume.where(close < open_, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    tot_v = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(red_v, tot_v).diff().diff()

def f07_dsig_023_red_bar_dollar_vol_z_63d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    red_dv = dv.where(close < open_)
    m = red_dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(m, YDAYS).diff().diff()

def f07_dsig_024_weighted_directional_vol_index_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    w = volume * chg.abs()
    sw = volume * chg
    num = sw.rolling(MDAYS, min_periods=WDAYS).sum()
    den = w.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(num, den).diff().diff()

def f07_dsig_025_weighted_directional_vol_index_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    w = volume * chg.abs()
    sw = volume * chg
    num = sw.rolling(QDAYS, min_periods=MDAYS).sum()
    den = w.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den).diff().diff()

def f07_dsig_026_churning_bar_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    avg_v = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > 2.0 * avg_v
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.8
    flag = (big_v & narrow).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_027_churning_bar_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    avg_v = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > 2.0 * avg_v
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.8
    flag = (big_v & narrow).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_028_avg_vol_on_small_range_bars_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.5
    v = volume.where(narrow)
    return v.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_029_effort_result_ratio_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    r = close.pct_change().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(v, r).diff().diff()

def f07_dsig_030_effort_result_ratio_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    r = close.pct_change().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(v, r).diff().diff()

def f07_dsig_031_up_effort_result_mismatch_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    up_v = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    up_r = chg.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(up_v, up_r).diff().diff()

def f07_dsig_032_up_effort_result_mismatch_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    up_v = volume.where(chg > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    up_r = chg.where(chg > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up_v, up_r).diff().diff()

def f07_dsig_033_high_vol_low_close_position_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 1.0 / 3.0
    flag = (big & weak).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_034_high_vol_low_close_position_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 1.0 / 3.0
    flag = (big & weak).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_035_vol_per_atr_move_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    v = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    tr = _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(v, tr).diff().diff()

def f07_dsig_036_vol_per_atr_move_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    v = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    tr = _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(v, tr).diff().diff()

def f07_dsig_037_log_vol_log_range_ratio_21d_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    r = (high - low).rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_log(v) - _safe_log(r)).diff().diff()

def f07_dsig_038_churning_intensity_z_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z_v = _rolling_zscore(volume, YDAYS)
    atr252 = _atr(high, low, close, YDAYS)
    rng_norm = (high - low) / atr252.replace(0, np.nan)
    z_r = _rolling_zscore(rng_norm, YDAYS)
    return (z_v - z_r).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_039_churning_intensity_z_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z_v = _rolling_zscore(volume, YDAYS)
    atr252 = _atr(high, low, close, YDAYS)
    rng_norm = (high - low) / atr252.replace(0, np.nan)
    z_r = _rolling_zscore(rng_norm, YDAYS)
    return (z_v - z_r).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_040_high_vol_narrow_range_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = z > 1.5
    atr = _atr(high, low, close, MDAYS)
    narrow = high - low < 0.6 * atr
    flag = (big & narrow).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_041_high_vol_narrow_range_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    big = z > 1.5
    atr = _atr(high, low, close, MDAYS)
    narrow = high - low < 0.6 * atr
    flag = (big & narrow).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_042_wide_vol_low_progress_count_21d_d2(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    wide = high - low > 1.5 * atr
    rel = (close - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    tiny = rel < 0.005
    big_v = _rolling_zscore(volume, YDAYS) > 1.0
    flag = (wide & tiny & big_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_043_vol_expansion_without_price_expansion_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    z_v = _rolling_zscore(volume, YDAYS)
    z_r = _rolling_zscore(close.pct_change().abs(), YDAYS)
    return _rolling_slope(z_v - z_r, MDAYS).diff().diff()

def f07_dsig_044_price_volume_correlation_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return close.rolling(MDAYS, min_periods=WDAYS).corr(volume).diff().diff()

def f07_dsig_045_price_volume_correlation_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    return close.rolling(QDAYS, min_periods=MDAYS).corr(volume).diff().diff()

def f07_dsig_046_price_vol_slope_divergence_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_sl = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    v_sl = _rolling_slope(volume, QDAYS) / volume.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return (p_sl - v_sl).diff().diff()

def f07_dsig_047_cum_vol_vs_cum_price_slope_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    cv = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    cp = close.rolling(QDAYS, min_periods=MDAYS).sum()
    v_sl = _rolling_slope(cv, QDAYS) / cv.replace(0, np.nan)
    p_sl = _rolling_slope(cp, QDAYS) / cp.replace(0, np.nan)
    return (v_sl - p_sl).diff().diff()

def f07_dsig_048_distribution_day_count_1pct_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    big_loss = chg < -0.01
    higher_v = volume > volume.shift(1)
    flag = (big_loss & higher_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_049_distribution_day_count_1pct_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    big_loss = chg < -0.01
    higher_v = volume > volume.shift(1)
    flag = (big_loss & higher_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_050_distribution_day_cluster_max_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    big_loss = chg < -0.01
    higher_v = volume > volume.shift(1)
    flag = (big_loss & higher_v).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max().diff().diff()

def f07_dsig_051_obv_slope_63d_neg_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    return _rolling_slope(obv, QDAYS).diff().diff()

def f07_dsig_052_obv_slope_252d_neg_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    return _rolling_slope(obv, YDAYS).diff().diff()

def f07_dsig_053_obv_price_divergence_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    p_sl = _rolling_slope(close, QDAYS)
    o_sl = _rolling_slope(obv, QDAYS)
    p_n = p_sl / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    o_n = o_sl / obv.rolling(QDAYS, min_periods=MDAYS).mean().abs().replace(0, np.nan)
    return (p_n - o_n).diff().diff()

def f07_dsig_054_obv_price_divergence_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    p_sl = _rolling_slope(close, YDAYS)
    o_sl = _rolling_slope(obv, YDAYS)
    p_n = p_sl / close.rolling(YDAYS, min_periods=QDAYS).mean().replace(0, np.nan)
    o_n = o_sl / obv.rolling(YDAYS, min_periods=QDAYS).mean().abs().replace(0, np.nan)
    return (p_n - o_n).diff().diff()

def f07_dsig_055_obv_zscore_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    return _rolling_zscore(obv, YDAYS).diff().diff()

def f07_dsig_056_obv_plateau_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    flat = (obv.diff().abs() < 0.1 * obv.rolling(MDAYS, min_periods=WDAYS).std()).astype(float)
    return flat.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_057_ad_line_slope_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    return _rolling_slope(ad, QDAYS).diff().diff()

def f07_dsig_058_ad_line_slope_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    return _rolling_slope(ad, YDAYS).diff().diff()

def f07_dsig_059_ad_price_divergence_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    p_sl = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    a_sl = _rolling_slope(ad, QDAYS) / ad.rolling(QDAYS, min_periods=MDAYS).mean().abs().replace(0, np.nan)
    return (p_sl - a_sl).diff().diff()

def f07_dsig_060_ad_line_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    return _rolling_zscore(ad, YDAYS).diff().diff()

def f07_dsig_061_cmf_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    return (mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)).diff().diff()

def f07_dsig_062_cmf_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    return (mfv.rolling(QDAYS, min_periods=MDAYS).sum() / volume.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)).diff().diff()

def f07_dsig_063_cmf_slope_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    cmf = mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    return _rolling_slope(cmf, MDAYS).diff().diff()

def f07_dsig_064_cmf_slope_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    cmf = mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    return _rolling_slope(cmf, QDAYS).diff().diff()

def f07_dsig_065_mfi_14d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    pos_sum = pos.rolling(14, min_periods=5).sum()
    neg_sum = neg.rolling(14, min_periods=5).sum()
    mr = pos_sum / neg_sum.replace(0, np.nan)
    return (100.0 - 100.0 / (1.0 + mr)).diff().diff()

def f07_dsig_066_mfi_28d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    pos_sum = pos.rolling(28, min_periods=10).sum()
    neg_sum = neg.rolling(28, min_periods=10).sum()
    mr = pos_sum / neg_sum.replace(0, np.nan)
    return (100.0 - 100.0 / (1.0 + mr)).diff().diff()

def f07_dsig_067_mfi_divergence_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    mr = pos.rolling(14, min_periods=5).sum() / neg.rolling(14, min_periods=5).sum().replace(0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    p_n = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    m_n = _rolling_slope(mfi, QDAYS) / mfi.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return (p_n - m_n).diff().diff()

def f07_dsig_068_mfi_slope_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    mr = pos.rolling(14, min_periods=5).sum() / neg.rolling(14, min_periods=5).sum().replace(0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return _rolling_slope(mfi, MDAYS).diff().diff()

def f07_dsig_069_mfi_slope_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    mr = pos.rolling(14, min_periods=5).sum() / neg.rolling(14, min_periods=5).sum().replace(0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return _rolling_slope(mfi, QDAYS).diff().diff()

def f07_dsig_070_nvi_slope_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vd = volume < volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vd, chg, 0.0), index=close.index)
    nvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_slope(nvi, MDAYS).diff().diff()

def f07_dsig_071_pvi_slope_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vu = volume > volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vu, chg, 0.0), index=close.index)
    pvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_slope(pvi, MDAYS).diff().diff()

def f07_dsig_072_nvi_to_pvi_ratio_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vd = volume < volume.shift(1)
    vu = volume > volume.shift(1)
    chg = close.pct_change().fillna(0)
    nvi_incr = pd.Series(np.where(vd, chg, 0.0), index=close.index)
    pvi_incr = pd.Series(np.where(vu, chg, 0.0), index=close.index)
    nvi = 100.0 * (1.0 + nvi_incr).cumprod()
    pvi = 100.0 * (1.0 + pvi_incr).cumprod()
    return _safe_div(nvi.rolling(MDAYS, min_periods=WDAYS).mean(), pvi.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff()

def f07_dsig_073_nvi_zscore_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vd = volume < volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vd, chg, 0.0), index=close.index)
    nvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_zscore(nvi, QDAYS).diff().diff()

def f07_dsig_074_pvi_zscore_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    vu = volume > volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vu, chg, 0.0), index=close.index)
    pvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_zscore(pvi, QDAYS).diff().diff()

def f07_dsig_075_composite_moneyflow_distribution_score_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    mfv = clv.fillna(0) * volume
    cmf = mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    z_o = -_rolling_zscore(_rolling_slope(obv, QDAYS), YDAYS)
    z_a = -_rolling_zscore(_rolling_slope(ad, QDAYS), YDAYS)
    z_c = -_rolling_zscore(cmf, YDAYS)
    return (z_o + z_a + z_c).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()
DISTRIBUTION_SIGNATURE_D2_REGISTRY_001_075 = {'f07_dsig_001_up_minus_down_vol_zscore_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_001_up_minus_down_vol_zscore_21d_d2}, 'f07_dsig_002_up_minus_down_vol_zscore_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_002_up_minus_down_vol_zscore_63d_d2}, 'f07_dsig_003_down_vol_fraction_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_003_down_vol_fraction_21d_d2}, 'f07_dsig_004_down_vol_fraction_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_004_down_vol_fraction_63d_d2}, 'f07_dsig_005_down_vol_slope_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_005_down_vol_slope_63d_d2}, 'f07_dsig_006_down_vol_zscore_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_006_down_vol_zscore_21d_d2}, 'f07_dsig_007_down_vol_zscore_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_007_down_vol_zscore_63d_d2}, 'f07_dsig_008_up_vol_zscore_decline_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_008_up_vol_zscore_decline_63d_d2}, 'f07_dsig_009_up_vol_regression_slope_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_009_up_vol_regression_slope_63d_d2}, 'f07_dsig_010_up_minus_down_vol_cumulative_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_010_up_minus_down_vol_cumulative_63d_d2}, 'f07_dsig_011_up_minus_down_vol_slope_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_011_up_minus_down_vol_slope_63d_d2}, 'f07_dsig_012_supply_ratio_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_012_supply_ratio_21d_d2}, 'f07_dsig_013_supply_ratio_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_013_supply_ratio_63d_d2}, 'f07_dsig_014_supply_ratio_slope_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_014_supply_ratio_slope_63d_d2}, 'f07_dsig_015_down_vol_days_fraction_21d_d2': {'inputs': ['close'], 'func': f07_dsig_015_down_vol_days_fraction_21d_d2}, 'f07_dsig_016_down_vol_days_fraction_63d_d2': {'inputs': ['close'], 'func': f07_dsig_016_down_vol_days_fraction_63d_d2}, 'f07_dsig_017_red_vs_green_vol_mean_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_017_red_vs_green_vol_mean_21d_d2}, 'f07_dsig_018_red_vs_green_vol_mean_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_018_red_vs_green_vol_mean_63d_d2}, 'f07_dsig_019_red_bar_vol_slope_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_019_red_bar_vol_slope_63d_d2}, 'f07_dsig_020_avg_vol_close_below_open_21d_z_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_020_avg_vol_close_below_open_21d_z_d2}, 'f07_dsig_021_avg_vol_close_below_open_63d_z_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_021_avg_vol_close_below_open_63d_z_d2}, 'f07_dsig_022_close_below_open_vol_weighted_pct_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_022_close_below_open_vol_weighted_pct_63d_d2}, 'f07_dsig_023_red_bar_dollar_vol_z_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_023_red_bar_dollar_vol_z_63d_d2}, 'f07_dsig_024_weighted_directional_vol_index_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_024_weighted_directional_vol_index_21d_d2}, 'f07_dsig_025_weighted_directional_vol_index_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_025_weighted_directional_vol_index_63d_d2}, 'f07_dsig_026_churning_bar_count_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_026_churning_bar_count_21d_d2}, 'f07_dsig_027_churning_bar_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_027_churning_bar_count_63d_d2}, 'f07_dsig_028_avg_vol_on_small_range_bars_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_028_avg_vol_on_small_range_bars_21d_d2}, 'f07_dsig_029_effort_result_ratio_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_029_effort_result_ratio_21d_d2}, 'f07_dsig_030_effort_result_ratio_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_030_effort_result_ratio_63d_d2}, 'f07_dsig_031_up_effort_result_mismatch_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_031_up_effort_result_mismatch_21d_d2}, 'f07_dsig_032_up_effort_result_mismatch_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_032_up_effort_result_mismatch_63d_d2}, 'f07_dsig_033_high_vol_low_close_position_count_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_033_high_vol_low_close_position_count_21d_d2}, 'f07_dsig_034_high_vol_low_close_position_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_034_high_vol_low_close_position_count_63d_d2}, 'f07_dsig_035_vol_per_atr_move_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_035_vol_per_atr_move_21d_d2}, 'f07_dsig_036_vol_per_atr_move_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_036_vol_per_atr_move_63d_d2}, 'f07_dsig_037_log_vol_log_range_ratio_21d_d2': {'inputs': ['high', 'low', 'volume'], 'func': f07_dsig_037_log_vol_log_range_ratio_21d_d2}, 'f07_dsig_038_churning_intensity_z_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_038_churning_intensity_z_21d_d2}, 'f07_dsig_039_churning_intensity_z_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_039_churning_intensity_z_63d_d2}, 'f07_dsig_040_high_vol_narrow_range_count_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_040_high_vol_narrow_range_count_21d_d2}, 'f07_dsig_041_high_vol_narrow_range_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_041_high_vol_narrow_range_count_63d_d2}, 'f07_dsig_042_wide_vol_low_progress_count_21d_d2': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f07_dsig_042_wide_vol_low_progress_count_21d_d2}, 'f07_dsig_043_vol_expansion_without_price_expansion_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_043_vol_expansion_without_price_expansion_21d_d2}, 'f07_dsig_044_price_volume_correlation_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_044_price_volume_correlation_21d_d2}, 'f07_dsig_045_price_volume_correlation_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_045_price_volume_correlation_63d_d2}, 'f07_dsig_046_price_vol_slope_divergence_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_046_price_vol_slope_divergence_63d_d2}, 'f07_dsig_047_cum_vol_vs_cum_price_slope_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_047_cum_vol_vs_cum_price_slope_63d_d2}, 'f07_dsig_048_distribution_day_count_1pct_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_048_distribution_day_count_1pct_21d_d2}, 'f07_dsig_049_distribution_day_count_1pct_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_049_distribution_day_count_1pct_63d_d2}, 'f07_dsig_050_distribution_day_cluster_max_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_050_distribution_day_cluster_max_63d_d2}, 'f07_dsig_051_obv_slope_63d_neg_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_051_obv_slope_63d_neg_d2}, 'f07_dsig_052_obv_slope_252d_neg_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_052_obv_slope_252d_neg_d2}, 'f07_dsig_053_obv_price_divergence_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_053_obv_price_divergence_63d_d2}, 'f07_dsig_054_obv_price_divergence_252d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_054_obv_price_divergence_252d_d2}, 'f07_dsig_055_obv_zscore_252d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_055_obv_zscore_252d_d2}, 'f07_dsig_056_obv_plateau_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_056_obv_plateau_count_21d_d2}, 'f07_dsig_057_ad_line_slope_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_057_ad_line_slope_63d_d2}, 'f07_dsig_058_ad_line_slope_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_058_ad_line_slope_252d_d2}, 'f07_dsig_059_ad_price_divergence_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_059_ad_price_divergence_63d_d2}, 'f07_dsig_060_ad_line_zscore_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_060_ad_line_zscore_252d_d2}, 'f07_dsig_061_cmf_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_061_cmf_21d_d2}, 'f07_dsig_062_cmf_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_062_cmf_63d_d2}, 'f07_dsig_063_cmf_slope_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_063_cmf_slope_21d_d2}, 'f07_dsig_064_cmf_slope_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_064_cmf_slope_63d_d2}, 'f07_dsig_065_mfi_14d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_065_mfi_14d_d2}, 'f07_dsig_066_mfi_28d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_066_mfi_28d_d2}, 'f07_dsig_067_mfi_divergence_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_067_mfi_divergence_63d_d2}, 'f07_dsig_068_mfi_slope_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_068_mfi_slope_21d_d2}, 'f07_dsig_069_mfi_slope_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_069_mfi_slope_63d_d2}, 'f07_dsig_070_nvi_slope_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_070_nvi_slope_21d_d2}, 'f07_dsig_071_pvi_slope_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_071_pvi_slope_21d_d2}, 'f07_dsig_072_nvi_to_pvi_ratio_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_072_nvi_to_pvi_ratio_21d_d2}, 'f07_dsig_073_nvi_zscore_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_073_nvi_zscore_63d_d2}, 'f07_dsig_074_pvi_zscore_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_074_pvi_zscore_63d_d2}, 'f07_dsig_075_composite_moneyflow_distribution_score_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_075_composite_moneyflow_distribution_score_63d_d2}}
