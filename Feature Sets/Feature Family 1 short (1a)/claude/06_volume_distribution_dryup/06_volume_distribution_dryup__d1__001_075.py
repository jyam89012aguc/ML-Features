"""Auto-generated D1 wrappers from volume_distribution_dryup__base__001_075.py.

Each function inlines the base body and appends .diff() chained 1 time(s)."""
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

def f06_vddu_001_volume_sma5_to_sma252_d1(volume: pd.Series) -> pd.Series:
    a = volume.rolling(WDAYS, min_periods=2).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(a, b).diff()

def f06_vddu_002_volume_sma21_to_sma252_d1(volume: pd.Series) -> pd.Series:
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(a, b).diff()

def f06_vddu_003_volume_sma21_to_sma63_d1(volume: pd.Series) -> pd.Series:
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(a, b).diff()

def f06_vddu_004_volume_median_5d_to_252d_d1(volume: pd.Series) -> pd.Series:
    a = volume.rolling(WDAYS, min_periods=2).median()
    b = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(a, b).diff()

def f06_vddu_005_log_volume_diff_21_vs_252_means_d1(volume: pd.Series) -> pd.Series:
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_log(a) - _safe_log(b)).diff()

def f06_vddu_006_dollar_volume_sma21_to_sma252_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    b = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(a, b).diff()

def f06_vddu_007_volume_zscore_252d_d1(volume: pd.Series) -> pd.Series:
    return _rolling_zscore(volume, YDAYS).diff()

def f06_vddu_008_volume_zscore_63d_d1(volume: pd.Series) -> pd.Series:
    return _rolling_zscore(volume, QDAYS).diff()

def f06_vddu_009_pct_rank_mean_21d_vol_in_252d_d1(volume: pd.Series) -> pd.Series:
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return m21.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w) if not np.isnan(w).any() else np.nan, raw=True).diff()

def f06_vddu_010_pct_rank_mean_5d_vol_in_63d_d1(volume: pd.Series) -> pd.Series:
    m5 = volume.rolling(WDAYS, min_periods=2).mean()
    return m5.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w) if not np.isnan(w).any() else np.nan, raw=True).diff()

def f06_vddu_011_log_volume_contraction_21d_d1(volume: pd.Series) -> pd.Series:
    return (-_safe_log(volume).diff(MDAYS)).diff()

def f06_vddu_012_log_volume_contraction_63d_d1(volume: pd.Series) -> pd.Series:
    return (-_safe_log(volume).diff(QDAYS)).diff()

def f06_vddu_013_volume_drop_pct_vs_252d_max_d1(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(YDAYS, min_periods=QDAYS).max()
    return (1.0 - _safe_div(volume, mx)).diff()

def f06_vddu_014_volume_drop_pct_vs_63d_max_d1(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(QDAYS, min_periods=MDAYS).max()
    return (1.0 - _safe_div(volume, mx)).diff()

def f06_vddu_015_volume_vs_252d_75pct_d1(volume: pd.Series) -> pd.Series:
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return _safe_div(volume, p).diff()

def f06_vddu_016_volume_vs_63d_75pct_d1(volume: pd.Series) -> pd.Series:
    p = volume.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    return _safe_div(volume, p).diff()

def f06_vddu_017_dollar_volume_drop_pct_vs_252d_max_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    mx = dv.rolling(YDAYS, min_periods=QDAYS).max()
    return (1.0 - _safe_div(dv, mx)).diff()

def f06_vddu_018_dollar_volume_drop_pct_vs_63d_max_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    mx = dv.rolling(QDAYS, min_periods=MDAYS).max()
    return (1.0 - _safe_div(dv, mx)).diff()

def f06_vddu_019_log_max_vol_252d_over_mean_5d_d1(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(YDAYS, min_periods=QDAYS).max()
    a5 = volume.rolling(WDAYS, min_periods=2).mean()
    return (_safe_log(mx) - _safe_log(a5)).diff()

def f06_vddu_020_dollar_volume_current_vs_peak_ratio_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max()).diff()

def f06_vddu_021_avg_dollar_volume_contraction_21_vs_63_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    b = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(a, b).diff()

def f06_vddu_022_volume_sma5_to_ema63_d1(volume: pd.Series) -> pd.Series:
    s5 = volume.rolling(WDAYS, min_periods=2).mean()
    e63 = volume.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()
    return _safe_div(s5, e63).diff()

def f06_vddu_023_ema21_to_ema252_volume_d1(volume: pd.Series) -> pd.Series:
    e21 = volume.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()
    e252 = volume.ewm(span=YDAYS, adjust=False, min_periods=QDAYS).mean()
    return _safe_div(e21, e252).diff()

def f06_vddu_024_volume_proximity_to_252d_min_d1(volume: pd.Series) -> pd.Series:
    mn = volume.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(volume, mn).diff()

def f06_vddu_025_dollar_volume_proximity_to_252d_min_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    mn = dv.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(dv, mn).diff()

def f06_vddu_026_volume_slope_21d_d1(volume: pd.Series) -> pd.Series:
    return _rolling_slope(volume, MDAYS).diff()

def f06_vddu_027_volume_slope_63d_d1(volume: pd.Series) -> pd.Series:
    return _rolling_slope(volume, QDAYS).diff()

def f06_vddu_028_log_volume_slope_21d_d1(volume: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_log(volume), MDAYS).diff()

def f06_vddu_029_log_volume_slope_63d_d1(volume: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_log(volume), QDAYS).diff()

def f06_vddu_030_dollar_volume_slope_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _rolling_slope(close * volume, MDAYS).diff()

def f06_vddu_031_dollar_volume_slope_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _rolling_slope(close * volume, QDAYS).diff()

def f06_vddu_032_volume_ema_slope_21d_d1(volume: pd.Series) -> pd.Series:
    e = volume.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()
    return _rolling_slope(e, MDAYS).diff()

def f06_vddu_033_volume_slope_normalized_by_mean_21d_d1(volume: pd.Series) -> pd.Series:
    sl = _rolling_slope(volume, MDAYS)
    m = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(sl, m).diff()

def f06_vddu_034_consecutive_declining_5d_avg_vol_streak_d1(volume: pd.Series) -> pd.Series:
    avg5 = volume.rolling(WDAYS, min_periods=2).mean()
    dec = (avg5.diff() < 0).astype(int)
    grp = (dec == 0).cumsum()
    return dec.groupby(grp).cumsum().diff()

def f06_vddu_035_days_since_vol_1sigma_d1(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 1.0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff()

def f06_vddu_036_days_since_vol_2sigma_d1(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 2.0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff()

def f06_vddu_037_days_since_252d_vol_max_d1(volume: pd.Series) -> pd.Series:

    def _bsm(w):
        return len(w) - 1 - int(np.argmax(w))
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True).diff()

def f06_vddu_038_days_since_63d_vol_max_d1(volume: pd.Series) -> pd.Series:

    def _bsm(w):
        return len(w) - 1 - int(np.argmax(w))
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True).diff()

def f06_vddu_039_declining_vol_days_count_21d_d1(volume: pd.Series) -> pd.Series:
    dec = (volume.diff() < 0).astype(float)
    return dec.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f06_vddu_040_declining_vol_days_count_63d_d1(volume: pd.Series) -> pd.Series:
    dec = (volume.diff() < 0).astype(float)
    return dec.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f06_vddu_041_log_volume_range_63d_d1(volume: pd.Series) -> pd.Series:
    return (_safe_log(volume.rolling(QDAYS, min_periods=MDAYS).max()) - _safe_log(volume.rolling(QDAYS, min_periods=MDAYS).min())).diff()

def f06_vddu_042_volume_range_compression_21_vs_63_d1(volume: pd.Series) -> pd.Series:
    rng21 = volume.rolling(MDAYS, min_periods=WDAYS).max() - volume.rolling(MDAYS, min_periods=WDAYS).min()
    rng63 = volume.rolling(QDAYS, min_periods=MDAYS).max() - volume.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(rng21, rng63).diff()

def f06_vddu_043_volume_cv_drop_21_vs_63_d1(volume: pd.Series) -> pd.Series:
    cv21 = volume.rolling(MDAYS, min_periods=WDAYS).std() / volume.rolling(MDAYS, min_periods=WDAYS).mean().replace(0, np.nan)
    cv63 = volume.rolling(QDAYS, min_periods=MDAYS).std() / volume.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return (cv21 - cv63).diff()

def f06_vddu_044_log_volume_std_drop_21_vs_63_d1(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    return _safe_div(lv.rolling(MDAYS, min_periods=WDAYS).std(), lv.rolling(QDAYS, min_periods=MDAYS).std()).diff()

def f06_vddu_045_volume_exponential_decay_half_life_63d_d1(volume: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(volume), QDAYS)
    return _safe_div(-np.log(2.0), sl).diff()

def f06_vddu_046_volume_drift_to_vol_of_vol_63d_d1(volume: pd.Series) -> pd.Series:
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(m, sd).diff()

def f06_vddu_047_pct_days_vol_below_half_sma252_in_21d_d1(volume: pd.Series) -> pd.Series:
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume < 0.5 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f06_vddu_048_pct_days_vol_below_quarter_sma252_in_21d_d1(volume: pd.Series) -> pd.Series:
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume < 0.25 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f06_vddu_049_pct_days_vol_below_25pct_252d_in_21d_d1(volume: pd.Series) -> pd.Series:
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = (volume < p).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f06_vddu_050_pct_days_vol_below_25pct_252d_in_63d_d1(volume: pd.Series) -> pd.Series:
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = (volume < p).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f06_vddu_051_low_vol_up_day_count_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close.diff() > 0
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (up & (volume < med)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f06_vddu_052_low_vol_up_day_count_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close.diff() > 0
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (up & (volume < med)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f06_vddu_053_up_to_down_vol_ratio_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0)
    dn_v = volume.where(chg < 0)
    return _safe_div(up_v.rolling(MDAYS, min_periods=WDAYS).mean(), dn_v.rolling(MDAYS, min_periods=WDAYS).mean()).diff()

def f06_vddu_054_up_to_down_vol_ratio_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0)
    dn_v = volume.where(chg < 0)
    return _safe_div(up_v.rolling(QDAYS, min_periods=MDAYS).mean(), dn_v.rolling(QDAYS, min_periods=MDAYS).mean()).diff()

def f06_vddu_055_up_to_down_vol_ratio_drop_21_vs_63_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0)
    dn_v = volume.where(chg < 0)
    r21 = _safe_div(up_v.rolling(MDAYS, min_periods=WDAYS).mean(), dn_v.rolling(MDAYS, min_periods=WDAYS).mean())
    r63 = _safe_div(up_v.rolling(QDAYS, min_periods=MDAYS).mean(), dn_v.rolling(QDAYS, min_periods=MDAYS).mean())
    return (r21 - r63).diff()

def f06_vddu_056_low_vol_new_high_count_21d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_v = volume < med
    flag = (nh & low_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f06_vddu_057_low_vol_new_high_count_63d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = high > prior_max
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_v = volume < med
    flag = (nh & low_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f06_vddu_058_low_vol_new_highs_share_of_all_new_highs_63d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = (high > prior_max).astype(float)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_v = (volume < med).astype(float)
    num = (nh * low_v).rolling(QDAYS, min_periods=MDAYS).sum()
    den = nh.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den).diff()

def f06_vddu_059_avg_vol_on_new_21d_high_bars_to_21d_total_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = (high > prior_max).astype(float)
    nh_mean = _safe_div((volume * nh).rolling(MDAYS, min_periods=WDAYS).sum(), nh.rolling(MDAYS, min_periods=WDAYS).sum())
    all_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(nh_mean, all_mean).diff()

def f06_vddu_060_avg_vol_on_new_63d_high_bars_to_63d_total_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = (high > prior_max).astype(float)
    nh_mean = _safe_div((volume * nh).rolling(QDAYS, min_periods=MDAYS).sum(), nh.rolling(QDAYS, min_periods=MDAYS).sum())
    all_mean = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(nh_mean, all_mean).diff()

def f06_vddu_061_pct_new_high_bars_below_median_vol_63d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = high > prior_max
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    below = volume < med
    nh_total = nh.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    nh_below = (nh & below).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(nh_below, nh_total).diff()

def f06_vddu_062_dryup_at_high_composite_count_21d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    z = _rolling_zscore(volume, YDAYS)
    low = z < -0.5
    flag = (near & low).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f06_vddu_063_up_volume_waning_slope_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0).fillna(0)
    return _rolling_slope(up_v, QDAYS).diff()

def f06_vddu_064_up_minus_down_vol_slope_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    diff_v = volume.where(chg > 0).fillna(0) - volume.where(chg < 0).fillna(0)
    return _rolling_slope(diff_v, MDAYS).diff()

def f06_vddu_065_up_minus_down_vol_slope_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    diff_v = volume.where(chg > 0).fillna(0) - volume.where(chg < 0).fillna(0)
    return _rolling_slope(diff_v, QDAYS).diff()

def f06_vddu_066_avg_up_vol_5d_vs_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0).fillna(0)
    a = up_v.rolling(WDAYS, min_periods=2).mean()
    b = up_v.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(a, b).diff()

def f06_vddu_067_cumulative_net_vol_21_vs_63_ratio_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    net = volume.where(chg > 0).fillna(0) - volume.where(chg < 0).fillna(0)
    a = net.rolling(MDAYS, min_periods=WDAYS).sum()
    b = net.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(a, b).diff()

def f06_vddu_068_accumulated_up_vol_decay_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0).fillna(0)
    cum = up_v.rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_slope(cum, QDAYS).diff()

def f06_vddu_069_dryup_with_price_stagnation_score_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = -_rolling_zscore(volume, YDAYS)
    flat = -_safe_log(close).diff(MDAYS).abs()
    return (z.rolling(MDAYS, min_periods=WDAYS).mean() + flat).diff()

def f06_vddu_070_price_near_high_with_low_vol_count_21d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (near & (volume < med)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f06_vddu_071_near_252d_high_with_low_quartile_vol_count_21d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.97
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = (near & (volume < p)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f06_vddu_072_price_vol_divergence_at_top_z_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (_rolling_zscore(close, QDAYS) - _rolling_zscore(volume, QDAYS)).diff()

def f06_vddu_073_silent_topping_index_21d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    z = -_rolling_zscore(volume, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.95
    score = z * near.astype(float)
    return score.rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f06_vddu_074_low_vol_rally_days_fraction_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up = chg > 0
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_up = (up & (volume < med)).astype(float)
    return _safe_div(low_up.rolling(MDAYS, min_periods=WDAYS).sum(), up.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()).diff()

def f06_vddu_075_low_vol_thrust_count_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg_pct = close.pct_change()
    thrust = chg_pct > 0.01
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    low_v = volume < med
    flag = (thrust & low_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()
VOLUME_DISTRIBUTION_DRYUP_D1_REGISTRY_001_075 = {'f06_vddu_001_volume_sma5_to_sma252_d1': {'inputs': ['volume'], 'func': f06_vddu_001_volume_sma5_to_sma252_d1}, 'f06_vddu_002_volume_sma21_to_sma252_d1': {'inputs': ['volume'], 'func': f06_vddu_002_volume_sma21_to_sma252_d1}, 'f06_vddu_003_volume_sma21_to_sma63_d1': {'inputs': ['volume'], 'func': f06_vddu_003_volume_sma21_to_sma63_d1}, 'f06_vddu_004_volume_median_5d_to_252d_d1': {'inputs': ['volume'], 'func': f06_vddu_004_volume_median_5d_to_252d_d1}, 'f06_vddu_005_log_volume_diff_21_vs_252_means_d1': {'inputs': ['volume'], 'func': f06_vddu_005_log_volume_diff_21_vs_252_means_d1}, 'f06_vddu_006_dollar_volume_sma21_to_sma252_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_006_dollar_volume_sma21_to_sma252_d1}, 'f06_vddu_007_volume_zscore_252d_d1': {'inputs': ['volume'], 'func': f06_vddu_007_volume_zscore_252d_d1}, 'f06_vddu_008_volume_zscore_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_008_volume_zscore_63d_d1}, 'f06_vddu_009_pct_rank_mean_21d_vol_in_252d_d1': {'inputs': ['volume'], 'func': f06_vddu_009_pct_rank_mean_21d_vol_in_252d_d1}, 'f06_vddu_010_pct_rank_mean_5d_vol_in_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_010_pct_rank_mean_5d_vol_in_63d_d1}, 'f06_vddu_011_log_volume_contraction_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_011_log_volume_contraction_21d_d1}, 'f06_vddu_012_log_volume_contraction_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_012_log_volume_contraction_63d_d1}, 'f06_vddu_013_volume_drop_pct_vs_252d_max_d1': {'inputs': ['volume'], 'func': f06_vddu_013_volume_drop_pct_vs_252d_max_d1}, 'f06_vddu_014_volume_drop_pct_vs_63d_max_d1': {'inputs': ['volume'], 'func': f06_vddu_014_volume_drop_pct_vs_63d_max_d1}, 'f06_vddu_015_volume_vs_252d_75pct_d1': {'inputs': ['volume'], 'func': f06_vddu_015_volume_vs_252d_75pct_d1}, 'f06_vddu_016_volume_vs_63d_75pct_d1': {'inputs': ['volume'], 'func': f06_vddu_016_volume_vs_63d_75pct_d1}, 'f06_vddu_017_dollar_volume_drop_pct_vs_252d_max_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_017_dollar_volume_drop_pct_vs_252d_max_d1}, 'f06_vddu_018_dollar_volume_drop_pct_vs_63d_max_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_018_dollar_volume_drop_pct_vs_63d_max_d1}, 'f06_vddu_019_log_max_vol_252d_over_mean_5d_d1': {'inputs': ['volume'], 'func': f06_vddu_019_log_max_vol_252d_over_mean_5d_d1}, 'f06_vddu_020_dollar_volume_current_vs_peak_ratio_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_020_dollar_volume_current_vs_peak_ratio_d1}, 'f06_vddu_021_avg_dollar_volume_contraction_21_vs_63_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_021_avg_dollar_volume_contraction_21_vs_63_d1}, 'f06_vddu_022_volume_sma5_to_ema63_d1': {'inputs': ['volume'], 'func': f06_vddu_022_volume_sma5_to_ema63_d1}, 'f06_vddu_023_ema21_to_ema252_volume_d1': {'inputs': ['volume'], 'func': f06_vddu_023_ema21_to_ema252_volume_d1}, 'f06_vddu_024_volume_proximity_to_252d_min_d1': {'inputs': ['volume'], 'func': f06_vddu_024_volume_proximity_to_252d_min_d1}, 'f06_vddu_025_dollar_volume_proximity_to_252d_min_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_025_dollar_volume_proximity_to_252d_min_d1}, 'f06_vddu_026_volume_slope_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_026_volume_slope_21d_d1}, 'f06_vddu_027_volume_slope_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_027_volume_slope_63d_d1}, 'f06_vddu_028_log_volume_slope_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_028_log_volume_slope_21d_d1}, 'f06_vddu_029_log_volume_slope_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_029_log_volume_slope_63d_d1}, 'f06_vddu_030_dollar_volume_slope_21d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_030_dollar_volume_slope_21d_d1}, 'f06_vddu_031_dollar_volume_slope_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_031_dollar_volume_slope_63d_d1}, 'f06_vddu_032_volume_ema_slope_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_032_volume_ema_slope_21d_d1}, 'f06_vddu_033_volume_slope_normalized_by_mean_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_033_volume_slope_normalized_by_mean_21d_d1}, 'f06_vddu_034_consecutive_declining_5d_avg_vol_streak_d1': {'inputs': ['volume'], 'func': f06_vddu_034_consecutive_declining_5d_avg_vol_streak_d1}, 'f06_vddu_035_days_since_vol_1sigma_d1': {'inputs': ['volume'], 'func': f06_vddu_035_days_since_vol_1sigma_d1}, 'f06_vddu_036_days_since_vol_2sigma_d1': {'inputs': ['volume'], 'func': f06_vddu_036_days_since_vol_2sigma_d1}, 'f06_vddu_037_days_since_252d_vol_max_d1': {'inputs': ['volume'], 'func': f06_vddu_037_days_since_252d_vol_max_d1}, 'f06_vddu_038_days_since_63d_vol_max_d1': {'inputs': ['volume'], 'func': f06_vddu_038_days_since_63d_vol_max_d1}, 'f06_vddu_039_declining_vol_days_count_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_039_declining_vol_days_count_21d_d1}, 'f06_vddu_040_declining_vol_days_count_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_040_declining_vol_days_count_63d_d1}, 'f06_vddu_041_log_volume_range_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_041_log_volume_range_63d_d1}, 'f06_vddu_042_volume_range_compression_21_vs_63_d1': {'inputs': ['volume'], 'func': f06_vddu_042_volume_range_compression_21_vs_63_d1}, 'f06_vddu_043_volume_cv_drop_21_vs_63_d1': {'inputs': ['volume'], 'func': f06_vddu_043_volume_cv_drop_21_vs_63_d1}, 'f06_vddu_044_log_volume_std_drop_21_vs_63_d1': {'inputs': ['volume'], 'func': f06_vddu_044_log_volume_std_drop_21_vs_63_d1}, 'f06_vddu_045_volume_exponential_decay_half_life_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_045_volume_exponential_decay_half_life_63d_d1}, 'f06_vddu_046_volume_drift_to_vol_of_vol_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_046_volume_drift_to_vol_of_vol_63d_d1}, 'f06_vddu_047_pct_days_vol_below_half_sma252_in_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_047_pct_days_vol_below_half_sma252_in_21d_d1}, 'f06_vddu_048_pct_days_vol_below_quarter_sma252_in_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_048_pct_days_vol_below_quarter_sma252_in_21d_d1}, 'f06_vddu_049_pct_days_vol_below_25pct_252d_in_21d_d1': {'inputs': ['volume'], 'func': f06_vddu_049_pct_days_vol_below_25pct_252d_in_21d_d1}, 'f06_vddu_050_pct_days_vol_below_25pct_252d_in_63d_d1': {'inputs': ['volume'], 'func': f06_vddu_050_pct_days_vol_below_25pct_252d_in_63d_d1}, 'f06_vddu_051_low_vol_up_day_count_21d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_051_low_vol_up_day_count_21d_d1}, 'f06_vddu_052_low_vol_up_day_count_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_052_low_vol_up_day_count_63d_d1}, 'f06_vddu_053_up_to_down_vol_ratio_21d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_053_up_to_down_vol_ratio_21d_d1}, 'f06_vddu_054_up_to_down_vol_ratio_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_054_up_to_down_vol_ratio_63d_d1}, 'f06_vddu_055_up_to_down_vol_ratio_drop_21_vs_63_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_055_up_to_down_vol_ratio_drop_21_vs_63_d1}, 'f06_vddu_056_low_vol_new_high_count_21d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_056_low_vol_new_high_count_21d_d1}, 'f06_vddu_057_low_vol_new_high_count_63d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_057_low_vol_new_high_count_63d_d1}, 'f06_vddu_058_low_vol_new_highs_share_of_all_new_highs_63d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_058_low_vol_new_highs_share_of_all_new_highs_63d_d1}, 'f06_vddu_059_avg_vol_on_new_21d_high_bars_to_21d_total_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_059_avg_vol_on_new_21d_high_bars_to_21d_total_d1}, 'f06_vddu_060_avg_vol_on_new_63d_high_bars_to_63d_total_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_060_avg_vol_on_new_63d_high_bars_to_63d_total_d1}, 'f06_vddu_061_pct_new_high_bars_below_median_vol_63d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_061_pct_new_high_bars_below_median_vol_63d_d1}, 'f06_vddu_062_dryup_at_high_composite_count_21d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_062_dryup_at_high_composite_count_21d_d1}, 'f06_vddu_063_up_volume_waning_slope_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_063_up_volume_waning_slope_63d_d1}, 'f06_vddu_064_up_minus_down_vol_slope_21d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_064_up_minus_down_vol_slope_21d_d1}, 'f06_vddu_065_up_minus_down_vol_slope_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_065_up_minus_down_vol_slope_63d_d1}, 'f06_vddu_066_avg_up_vol_5d_vs_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_066_avg_up_vol_5d_vs_63d_d1}, 'f06_vddu_067_cumulative_net_vol_21_vs_63_ratio_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_067_cumulative_net_vol_21_vs_63_ratio_d1}, 'f06_vddu_068_accumulated_up_vol_decay_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_068_accumulated_up_vol_decay_63d_d1}, 'f06_vddu_069_dryup_with_price_stagnation_score_21d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_069_dryup_with_price_stagnation_score_21d_d1}, 'f06_vddu_070_price_near_high_with_low_vol_count_21d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_070_price_near_high_with_low_vol_count_21d_d1}, 'f06_vddu_071_near_252d_high_with_low_quartile_vol_count_21d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_071_near_252d_high_with_low_quartile_vol_count_21d_d1}, 'f06_vddu_072_price_vol_divergence_at_top_z_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_072_price_vol_divergence_at_top_z_63d_d1}, 'f06_vddu_073_silent_topping_index_21d_d1': {'inputs': ['high', 'volume'], 'func': f06_vddu_073_silent_topping_index_21d_d1}, 'f06_vddu_074_low_vol_rally_days_fraction_21d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_074_low_vol_rally_days_fraction_21d_d1}, 'f06_vddu_075_low_vol_thrust_count_63d_d1': {'inputs': ['close', 'volume'], 'func': f06_vddu_075_low_vol_thrust_count_63d_d1}}
