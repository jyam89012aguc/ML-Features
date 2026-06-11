"""Auto-generated D3 wrappers from volume_blowoff_at_peak__base__001_075.py.

Each function inlines the base body and appends .diff() chained 3 time(s)."""
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

def f05_vbpk_001_volume_zscore_252d_d3(volume: pd.Series) -> pd.Series:
    return _rolling_zscore(volume, YDAYS).diff().diff().diff()

def f05_vbpk_002_volume_zscore_63d_d3(volume: pd.Series) -> pd.Series:
    return _rolling_zscore(volume, QDAYS).diff().diff().diff()

def f05_vbpk_003_volume_ratio_to_252d_median_d3(volume: pd.Series) -> pd.Series:
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(volume, med).diff().diff().diff()

def f05_vbpk_004_volume_ratio_to_63d_median_d3(volume: pd.Series) -> pd.Series:
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    return _safe_div(volume, med).diff().diff().diff()

def f05_vbpk_005_dollar_volume_zscore_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return _rolling_zscore(dv, YDAYS).diff().diff().diff()

def f05_vbpk_006_dollar_volume_zscore_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return _rolling_zscore(dv, QDAYS).diff().diff().diff()

def f05_vbpk_007_log_volume_max_21d_d3(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).rolling(MDAYS, min_periods=WDAYS).max().diff().diff().diff()

def f05_vbpk_008_single_day_peak_volume_zscore_21d_d3(volume: pd.Series) -> pd.Series:
    peak = volume.rolling(MDAYS, min_periods=WDAYS).max()
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(peak, m).diff().diff().diff()

def f05_vbpk_009_max_volume_5d_vs_252d_median_d3(volume: pd.Series) -> pd.Series:
    peak = volume.rolling(WDAYS, min_periods=2).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(peak, med).diff().diff().diff()

def f05_vbpk_010_max_volume_21d_vs_252d_median_d3(volume: pd.Series) -> pd.Series:
    peak = volume.rolling(MDAYS, min_periods=WDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(peak, med).diff().diff().diff()

def f05_vbpk_011_max_volume_63d_vs_252d_median_d3(volume: pd.Series) -> pd.Series:
    peak = volume.rolling(QDAYS, min_periods=MDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(peak, med).diff().diff().diff()

def f05_vbpk_012_volume_top_decile_count_21d_d3(volume: pd.Series) -> pd.Series:
    thr = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (volume >= thr).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f05_vbpk_013_volume_top_percentile_count_63d_d3(volume: pd.Series) -> pd.Series:
    thr = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (volume >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f05_vbpk_014_dollar_volume_top_decile_count_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    thr = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (dv >= thr).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f05_vbpk_015_count_3sigma_vol_days_63d_d3(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 3.0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f05_vbpk_016_count_5sigma_vol_days_252d_d3(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 5.0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f05_vbpk_017_days_since_max_252d_volume_d3(volume: pd.Series) -> pd.Series:

    def _bsm(w):
        return len(w) - 1 - int(np.argmax(w))
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True).diff().diff().diff()

def f05_vbpk_018_days_since_max_63d_volume_d3(volume: pd.Series) -> pd.Series:

    def _bsm(w):
        return len(w) - 1 - int(np.argmax(w))
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True).diff().diff().diff()

def f05_vbpk_019_max_to_mean_volume_ratio_63d_d3(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(QDAYS, min_periods=MDAYS).max()
    mn = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(mx, mn).diff().diff().diff()

def f05_vbpk_020_max_to_mean_dollar_volume_ratio_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    mx = dv.rolling(QDAYS, min_periods=MDAYS).max()
    mn = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(mx, mn).diff().diff().diff()

def f05_vbpk_021_volume_rank_pct_252d_d3(volume: pd.Series) -> pd.Series:
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w) if not np.isnan(w).any() else np.nan, raw=True).diff().diff().diff()

def f05_vbpk_022_volume_rank_pct_63d_d3(volume: pd.Series) -> pd.Series:
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w) if not np.isnan(w).any() else np.nan, raw=True).diff().diff().diff()

def f05_vbpk_023_log_volume_zscore_252d_d3(volume: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_log(volume), YDAYS).diff().diff().diff()

def f05_vbpk_024_extreme_volume_tail_mass_63d_d3(volume: pd.Series) -> pd.Series:

    def _tm(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)[-5:].sum()
        tot = w.sum()
        return s / tot if tot > 0 else np.nan
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_tm, raw=True).diff().diff().diff()

def f05_vbpk_025_volume_kurtosis_63d_d3(volume: pd.Series) -> pd.Series:

    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / sd ** 4 - 3.0)
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_k, raw=True).diff().diff().diff()

def f05_vbpk_026_volume_sma5_to_sma63_d3(volume: pd.Series) -> pd.Series:
    s5 = volume.rolling(WDAYS, min_periods=2).mean()
    s63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s5, s63).diff().diff().diff()

def f05_vbpk_027_volume_sma5_to_sma252_d3(volume: pd.Series) -> pd.Series:
    s5 = volume.rolling(WDAYS, min_periods=2).mean()
    s252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s5, s252).diff().diff().diff()

def f05_vbpk_028_volume_sma21_to_sma252_d3(volume: pd.Series) -> pd.Series:
    s21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    s252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s21, s252).diff().diff().diff()

def f05_vbpk_029_volume_sma21_to_sma63_d3(volume: pd.Series) -> pd.Series:
    s21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s21, s63).diff().diff().diff()

def f05_vbpk_030_dollar_volume_sma21_to_sma252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    s21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    s252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s21, s252).diff().diff().diff()

def f05_vbpk_031_log_volume_diff_5d_d3(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).diff(WDAYS).diff().diff().diff()

def f05_vbpk_032_log_volume_diff_21d_d3(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).diff(MDAYS).diff().diff().diff()

def f05_vbpk_033_log_volume_diff_63d_d3(volume: pd.Series) -> pd.Series:
    return _safe_log(volume).diff(QDAYS).diff().diff().diff()

def f05_vbpk_034_avg_volume_5d_to_median_252d_d3(volume: pd.Series) -> pd.Series:
    a = volume.rolling(WDAYS, min_periods=2).mean()
    m = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(a, m).diff().diff().diff()

def f05_vbpk_035_ema_volume_ratio_short_vs_long_d3(volume: pd.Series) -> pd.Series:
    e5 = volume.ewm(span=5, adjust=False, min_periods=2).mean()
    e63 = volume.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()
    return _safe_div(e5, e63).diff().diff().diff()

def f05_vbpk_036_volume_slope_21d_d3(volume: pd.Series) -> pd.Series:
    return _rolling_slope(volume, MDAYS).diff().diff().diff()

def f05_vbpk_037_volume_slope_63d_d3(volume: pd.Series) -> pd.Series:
    return _rolling_slope(volume, QDAYS).diff().diff().diff()

def f05_vbpk_038_volume_accel_vs_63d_baseline_z_d3(volume: pd.Series) -> pd.Series:
    slope = _rolling_slope(volume, MDAYS)
    return _rolling_zscore(slope, QDAYS).diff().diff().diff()

def f05_vbpk_039_volume_regime_shift_21_vs_252_d3(volume: pd.Series) -> pd.Series:
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_log(a) - _safe_log(b)).diff().diff().diff()

def f05_vbpk_040_volume_rising_streak_max_21d_d3(volume: pd.Series) -> pd.Series:
    up = (volume.diff() > 0).astype(int)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max().diff().diff().diff()

def f05_vbpk_041_volume_up_day_count_21d_d3(volume: pd.Series) -> pd.Series:
    up = (volume.diff() > 0).astype(float)
    return up.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f05_vbpk_042_volume_expansion_at_new_high_days_63d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    new_high = (high > prior_max).astype(float)
    nh_vol = (volume * new_high).rolling(QDAYS, min_periods=MDAYS).sum()
    nh_cnt = new_high.rolling(QDAYS, min_periods=MDAYS).sum()
    nh_mean = _safe_div(nh_vol, nh_cnt)
    all_mean = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(nh_mean, all_mean).diff().diff().diff()

def f05_vbpk_043_volume_expanding_pct_days_21d_d3(volume: pd.Series) -> pd.Series:
    up = (volume.diff() > 0).astype(float)
    return up.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f05_vbpk_044_log_volume_regression_intercept_21d_d3(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)

    def _ic(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        return float(c0)
    return lv.rolling(MDAYS, min_periods=WDAYS).apply(_ic, raw=True).diff().diff().diff()

def f05_vbpk_045_volume_mean_reverter_score_63d_d3(volume: pd.Series) -> pd.Series:
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return ((volume - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_046_top5_volume_share_of_63d_d3(volume: pd.Series) -> pd.Series:

    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        tot = w.sum()
        if tot == 0:
            return np.nan
        return float(np.sort(w)[-5:].sum() / tot)
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_sh, raw=True).diff().diff().diff()

def f05_vbpk_047_top1_volume_share_of_21d_d3(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(MDAYS, min_periods=WDAYS).max()
    sm = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(mx, sm).diff().diff().diff()

def f05_vbpk_048_top5_volume_share_of_252d_d3(volume: pd.Series) -> pd.Series:

    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        tot = w.sum()
        if tot == 0:
            return np.nan
        return float(np.sort(w)[-5:].sum() / tot)
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_sh, raw=True).diff().diff().diff()

def f05_vbpk_049_volume_sum_21d_vs_63d_d3(volume: pd.Series) -> pd.Series:
    a = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    b = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(a, b).diff().diff().diff()

def f05_vbpk_050_volume_sum_21d_vs_252d_d3(volume: pd.Series) -> pd.Series:
    a = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    b = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(a, b).diff().diff().diff()

def f05_vbpk_051_volume_on_new_252d_high_zscore_recent_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = high > prior_max
    nh_vol = volume.where(is_nh).ffill()
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return ((nh_vol - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_052_volume_on_new_63d_high_zscore_recent_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = high > prior_max
    nh_vol = volume.where(is_nh).ffill()
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return ((nh_vol - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_053_avg_volume_at_new_ath_63d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high > prior_max).astype(float)
    s = (volume * is_nh).rolling(QDAYS, min_periods=MDAYS).sum()
    c = is_nh.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(s, c).diff().diff().diff()

def f05_vbpk_054_newhigh_vs_nonnewhigh_volume_ratio_63d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high > prior_max).astype(float)
    is_nn = 1.0 - is_nh
    nh = _safe_div((volume * is_nh).rolling(QDAYS, min_periods=MDAYS).sum(), is_nh.rolling(QDAYS, min_periods=MDAYS).sum())
    nn = _safe_div((volume * is_nn).rolling(QDAYS, min_periods=MDAYS).sum(), is_nn.rolling(QDAYS, min_periods=MDAYS).sum())
    return _safe_div(nh, nn).diff().diff().diff()

def f05_vbpk_055_up_volume_zscore_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = (close.diff() > 0).astype(float)
    up_vol = volume * up
    return _rolling_zscore(up_vol, MDAYS).diff().diff().diff()

def f05_vbpk_056_up_volume_share_at_peak_63d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = high > prior_max
    is_up = close.diff() > 0
    nh_up = (is_nh & is_up).astype(float) * volume
    up_all = is_up.astype(float) * volume
    return _safe_div(nh_up.rolling(QDAYS, min_periods=MDAYS).sum(), up_all.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f05_vbpk_057_volume_on_top5pct_high_bars_z_252d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = high.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    top_flag = (high - rmin) / rng >= 0.95
    masked = volume.where(top_flag)
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return ((masked.ffill() - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_058_dollar_volume_at_new_highs_vs_other_63d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = (high > prior_max).astype(float)
    is_nn = 1.0 - is_nh
    dv = close * volume
    nh = _safe_div((dv * is_nh).rolling(QDAYS, min_periods=MDAYS).sum(), is_nh.rolling(QDAYS, min_periods=MDAYS).sum())
    nn = _safe_div((dv * is_nn).rolling(QDAYS, min_periods=MDAYS).sum(), is_nn.rolling(QDAYS, min_periods=MDAYS).sum())
    return _safe_div(nh, nn).diff().diff().diff()

def f05_vbpk_059_volume_times_return_top_quintile_share_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    vr = volume * r

    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w)
        k = max(1, n // 5)
        tot = w.sum()
        if tot == 0:
            return np.nan
        return float(np.sort(w)[-k:].sum() / tot)
    return vr.rolling(QDAYS, min_periods=MDAYS).apply(_sh, raw=True).diff().diff().diff()

def f05_vbpk_060_price_volume_product_anomaly_z_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    vr = volume * r
    return _rolling_zscore(vr, MDAYS).diff().diff().diff()

def f05_vbpk_061_vol_rallies_vs_pullbacks_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0).fillna(0)
    dn_v = volume.where(chg < 0).fillna(0)
    return _safe_div(up_v.rolling(QDAYS, min_periods=MDAYS).sum(), dn_v.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f05_vbpk_062_cumulative_up_volume_zscore_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0).fillna(0)
    cum = up_v.rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_zscore(cum, YDAYS).diff().diff().diff()

def f05_vbpk_063_peak_bar_volume_z_63d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:

    def _peakv(idx_window, vol_window):
        if np.isnan(idx_window).any():
            return np.nan
        return float(vol_window[int(np.argmax(idx_window))])

    def _f(w_high, w_vol):
        if np.isnan(w_high).any() or np.isnan(w_vol).any():
            return np.nan
        i = int(np.argmax(w_high))
        return float(w_vol[i])
    peak_v = pd.Series([_f(high.iloc[max(0, i - QDAYS + 1):i + 1].values, volume.iloc[max(0, i - QDAYS + 1):i + 1].values) if i >= MDAYS else np.nan for i in range(len(high))], index=high.index)
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return ((peak_v - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_064_volume_on_new_252d_high_mean_z_252d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high > prior_max).astype(float)
    nh_mean = _safe_div((volume * is_nh).rolling(YDAYS, min_periods=QDAYS).sum(), is_nh.rolling(YDAYS, min_periods=QDAYS).sum())
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return ((nh_mean - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_065_newhigh_with_2x_vol_count_21d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (nh & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f05_vbpk_066_up_volume_blowoff_index_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().clip(lower=0)
    v_r = volume * r
    m21 = v_r.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(m21, YDAYS).diff().diff().diff()

def f05_vbpk_067_volume_of_largest_gain_day_z_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = close.pct_change()

    def _vol_on_max(w_ret, w_vol):
        if np.isnan(w_ret).any() or np.isnan(w_vol).any():
            return np.nan
        i = int(np.argmax(w_ret))
        return float(w_vol[i])
    peak_v = pd.Series([_vol_on_max(r.iloc[max(0, i - MDAYS + 1):i + 1].values, volume.iloc[max(0, i - MDAYS + 1):i + 1].values) if i >= WDAYS else np.nan for i in range(len(r))], index=r.index)
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return ((peak_v - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_068_top5_gain_days_vol_share_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = close.pct_change()

    def _topv(w_ret, w_vol):
        if np.isnan(w_ret).any() or np.isnan(w_vol).any():
            return np.nan
        idx = np.argsort(w_ret)[-5:]
        return float(np.sum(w_vol[idx]))
    s = pd.Series([_topv(r.iloc[max(0, i - QDAYS + 1):i + 1].values, volume.iloc[max(0, i - QDAYS + 1):i + 1].values) if i >= MDAYS else np.nan for i in range(len(r))], index=r.index)
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s, m * 5.0).diff().diff().diff()

def f05_vbpk_069_vol_range_product_top_21d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    vr = volume * rng
    mx = vr.rolling(MDAYS, min_periods=WDAYS).max()
    med = vr.rolling(QDAYS, min_periods=MDAYS).median()
    return _safe_div(mx, med).diff().diff().diff()

def f05_vbpk_070_avg_top5_vol_range_to_median_63d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    vr = volume * (high - low)

    def _r(w):
        if np.isnan(w).any():
            return np.nan
        med = np.median(w)
        if med == 0:
            return np.nan
        return float(np.sort(w)[-5:].mean() / med)
    return vr.rolling(QDAYS, min_periods=MDAYS).apply(_r, raw=True).diff().diff().diff()

def f05_vbpk_071_peak_bar_dollar_vol_z_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    peak = dv.rolling(MDAYS, min_periods=WDAYS).max()
    m = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = dv.rolling(YDAYS, min_periods=QDAYS).std()
    return ((peak - m) / sd.replace(0, np.nan)).diff().diff().diff()

def f05_vbpk_072_price_vs_volume_z_divergence_at_top_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    zp = _rolling_zscore(close, QDAYS)
    zv = _rolling_zscore(volume, QDAYS)
    return (zp - zv).diff().diff().diff()

def f05_vbpk_073_closer_to_high_high_vol_count_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = (close - low) / (high - low).replace(0, np.nan)
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = ((pos >= 0.75) & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f05_vbpk_074_pct_near_max_high_with_2sigma_vol_21d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (near & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f05_vbpk_075_composite_blowoff_score_near_max_21d_d3(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan)
    z = _rolling_zscore(volume, YDAYS)
    score = z.clip(lower=0) * near
    return score.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()
VOLUME_BLOWOFF_AT_PEAK_D3_REGISTRY_001_075 = {'f05_vbpk_001_volume_zscore_252d_d3': {'inputs': ['volume'], 'func': f05_vbpk_001_volume_zscore_252d_d3}, 'f05_vbpk_002_volume_zscore_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_002_volume_zscore_63d_d3}, 'f05_vbpk_003_volume_ratio_to_252d_median_d3': {'inputs': ['volume'], 'func': f05_vbpk_003_volume_ratio_to_252d_median_d3}, 'f05_vbpk_004_volume_ratio_to_63d_median_d3': {'inputs': ['volume'], 'func': f05_vbpk_004_volume_ratio_to_63d_median_d3}, 'f05_vbpk_005_dollar_volume_zscore_252d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_005_dollar_volume_zscore_252d_d3}, 'f05_vbpk_006_dollar_volume_zscore_63d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_006_dollar_volume_zscore_63d_d3}, 'f05_vbpk_007_log_volume_max_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_007_log_volume_max_21d_d3}, 'f05_vbpk_008_single_day_peak_volume_zscore_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_008_single_day_peak_volume_zscore_21d_d3}, 'f05_vbpk_009_max_volume_5d_vs_252d_median_d3': {'inputs': ['volume'], 'func': f05_vbpk_009_max_volume_5d_vs_252d_median_d3}, 'f05_vbpk_010_max_volume_21d_vs_252d_median_d3': {'inputs': ['volume'], 'func': f05_vbpk_010_max_volume_21d_vs_252d_median_d3}, 'f05_vbpk_011_max_volume_63d_vs_252d_median_d3': {'inputs': ['volume'], 'func': f05_vbpk_011_max_volume_63d_vs_252d_median_d3}, 'f05_vbpk_012_volume_top_decile_count_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_012_volume_top_decile_count_21d_d3}, 'f05_vbpk_013_volume_top_percentile_count_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_013_volume_top_percentile_count_63d_d3}, 'f05_vbpk_014_dollar_volume_top_decile_count_21d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_014_dollar_volume_top_decile_count_21d_d3}, 'f05_vbpk_015_count_3sigma_vol_days_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_015_count_3sigma_vol_days_63d_d3}, 'f05_vbpk_016_count_5sigma_vol_days_252d_d3': {'inputs': ['volume'], 'func': f05_vbpk_016_count_5sigma_vol_days_252d_d3}, 'f05_vbpk_017_days_since_max_252d_volume_d3': {'inputs': ['volume'], 'func': f05_vbpk_017_days_since_max_252d_volume_d3}, 'f05_vbpk_018_days_since_max_63d_volume_d3': {'inputs': ['volume'], 'func': f05_vbpk_018_days_since_max_63d_volume_d3}, 'f05_vbpk_019_max_to_mean_volume_ratio_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_019_max_to_mean_volume_ratio_63d_d3}, 'f05_vbpk_020_max_to_mean_dollar_volume_ratio_63d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_020_max_to_mean_dollar_volume_ratio_63d_d3}, 'f05_vbpk_021_volume_rank_pct_252d_d3': {'inputs': ['volume'], 'func': f05_vbpk_021_volume_rank_pct_252d_d3}, 'f05_vbpk_022_volume_rank_pct_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_022_volume_rank_pct_63d_d3}, 'f05_vbpk_023_log_volume_zscore_252d_d3': {'inputs': ['volume'], 'func': f05_vbpk_023_log_volume_zscore_252d_d3}, 'f05_vbpk_024_extreme_volume_tail_mass_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_024_extreme_volume_tail_mass_63d_d3}, 'f05_vbpk_025_volume_kurtosis_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_025_volume_kurtosis_63d_d3}, 'f05_vbpk_026_volume_sma5_to_sma63_d3': {'inputs': ['volume'], 'func': f05_vbpk_026_volume_sma5_to_sma63_d3}, 'f05_vbpk_027_volume_sma5_to_sma252_d3': {'inputs': ['volume'], 'func': f05_vbpk_027_volume_sma5_to_sma252_d3}, 'f05_vbpk_028_volume_sma21_to_sma252_d3': {'inputs': ['volume'], 'func': f05_vbpk_028_volume_sma21_to_sma252_d3}, 'f05_vbpk_029_volume_sma21_to_sma63_d3': {'inputs': ['volume'], 'func': f05_vbpk_029_volume_sma21_to_sma63_d3}, 'f05_vbpk_030_dollar_volume_sma21_to_sma252_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_030_dollar_volume_sma21_to_sma252_d3}, 'f05_vbpk_031_log_volume_diff_5d_d3': {'inputs': ['volume'], 'func': f05_vbpk_031_log_volume_diff_5d_d3}, 'f05_vbpk_032_log_volume_diff_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_032_log_volume_diff_21d_d3}, 'f05_vbpk_033_log_volume_diff_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_033_log_volume_diff_63d_d3}, 'f05_vbpk_034_avg_volume_5d_to_median_252d_d3': {'inputs': ['volume'], 'func': f05_vbpk_034_avg_volume_5d_to_median_252d_d3}, 'f05_vbpk_035_ema_volume_ratio_short_vs_long_d3': {'inputs': ['volume'], 'func': f05_vbpk_035_ema_volume_ratio_short_vs_long_d3}, 'f05_vbpk_036_volume_slope_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_036_volume_slope_21d_d3}, 'f05_vbpk_037_volume_slope_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_037_volume_slope_63d_d3}, 'f05_vbpk_038_volume_accel_vs_63d_baseline_z_d3': {'inputs': ['volume'], 'func': f05_vbpk_038_volume_accel_vs_63d_baseline_z_d3}, 'f05_vbpk_039_volume_regime_shift_21_vs_252_d3': {'inputs': ['volume'], 'func': f05_vbpk_039_volume_regime_shift_21_vs_252_d3}, 'f05_vbpk_040_volume_rising_streak_max_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_040_volume_rising_streak_max_21d_d3}, 'f05_vbpk_041_volume_up_day_count_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_041_volume_up_day_count_21d_d3}, 'f05_vbpk_042_volume_expansion_at_new_high_days_63d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_042_volume_expansion_at_new_high_days_63d_d3}, 'f05_vbpk_043_volume_expanding_pct_days_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_043_volume_expanding_pct_days_21d_d3}, 'f05_vbpk_044_log_volume_regression_intercept_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_044_log_volume_regression_intercept_21d_d3}, 'f05_vbpk_045_volume_mean_reverter_score_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_045_volume_mean_reverter_score_63d_d3}, 'f05_vbpk_046_top5_volume_share_of_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_046_top5_volume_share_of_63d_d3}, 'f05_vbpk_047_top1_volume_share_of_21d_d3': {'inputs': ['volume'], 'func': f05_vbpk_047_top1_volume_share_of_21d_d3}, 'f05_vbpk_048_top5_volume_share_of_252d_d3': {'inputs': ['volume'], 'func': f05_vbpk_048_top5_volume_share_of_252d_d3}, 'f05_vbpk_049_volume_sum_21d_vs_63d_d3': {'inputs': ['volume'], 'func': f05_vbpk_049_volume_sum_21d_vs_63d_d3}, 'f05_vbpk_050_volume_sum_21d_vs_252d_d3': {'inputs': ['volume'], 'func': f05_vbpk_050_volume_sum_21d_vs_252d_d3}, 'f05_vbpk_051_volume_on_new_252d_high_zscore_recent_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_051_volume_on_new_252d_high_zscore_recent_d3}, 'f05_vbpk_052_volume_on_new_63d_high_zscore_recent_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_052_volume_on_new_63d_high_zscore_recent_d3}, 'f05_vbpk_053_avg_volume_at_new_ath_63d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_053_avg_volume_at_new_ath_63d_d3}, 'f05_vbpk_054_newhigh_vs_nonnewhigh_volume_ratio_63d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_054_newhigh_vs_nonnewhigh_volume_ratio_63d_d3}, 'f05_vbpk_055_up_volume_zscore_21d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_055_up_volume_zscore_21d_d3}, 'f05_vbpk_056_up_volume_share_at_peak_63d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f05_vbpk_056_up_volume_share_at_peak_63d_d3}, 'f05_vbpk_057_volume_on_top5pct_high_bars_z_252d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_057_volume_on_top5pct_high_bars_z_252d_d3}, 'f05_vbpk_058_dollar_volume_at_new_highs_vs_other_63d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f05_vbpk_058_dollar_volume_at_new_highs_vs_other_63d_d3}, 'f05_vbpk_059_volume_times_return_top_quintile_share_63d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_059_volume_times_return_top_quintile_share_63d_d3}, 'f05_vbpk_060_price_volume_product_anomaly_z_21d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_060_price_volume_product_anomaly_z_21d_d3}, 'f05_vbpk_061_vol_rallies_vs_pullbacks_63d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_061_vol_rallies_vs_pullbacks_63d_d3}, 'f05_vbpk_062_cumulative_up_volume_zscore_63d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_062_cumulative_up_volume_zscore_63d_d3}, 'f05_vbpk_063_peak_bar_volume_z_63d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_063_peak_bar_volume_z_63d_d3}, 'f05_vbpk_064_volume_on_new_252d_high_mean_z_252d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_064_volume_on_new_252d_high_mean_z_252d_d3}, 'f05_vbpk_065_newhigh_with_2x_vol_count_21d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_065_newhigh_with_2x_vol_count_21d_d3}, 'f05_vbpk_066_up_volume_blowoff_index_21d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_066_up_volume_blowoff_index_21d_d3}, 'f05_vbpk_067_volume_of_largest_gain_day_z_252d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_067_volume_of_largest_gain_day_z_252d_d3}, 'f05_vbpk_068_top5_gain_days_vol_share_63d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_068_top5_gain_days_vol_share_63d_d3}, 'f05_vbpk_069_vol_range_product_top_21d_d3': {'inputs': ['high', 'low', 'volume'], 'func': f05_vbpk_069_vol_range_product_top_21d_d3}, 'f05_vbpk_070_avg_top5_vol_range_to_median_63d_d3': {'inputs': ['high', 'low', 'volume'], 'func': f05_vbpk_070_avg_top5_vol_range_to_median_63d_d3}, 'f05_vbpk_071_peak_bar_dollar_vol_z_21d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_071_peak_bar_dollar_vol_z_21d_d3}, 'f05_vbpk_072_price_vs_volume_z_divergence_at_top_63d_d3': {'inputs': ['close', 'volume'], 'func': f05_vbpk_072_price_vs_volume_z_divergence_at_top_63d_d3}, 'f05_vbpk_073_closer_to_high_high_vol_count_21d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f05_vbpk_073_closer_to_high_high_vol_count_21d_d3}, 'f05_vbpk_074_pct_near_max_high_with_2sigma_vol_21d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_074_pct_near_max_high_with_2sigma_vol_21d_d3}, 'f05_vbpk_075_composite_blowoff_score_near_max_21d_d3': {'inputs': ['high', 'volume'], 'func': f05_vbpk_075_composite_blowoff_score_near_max_21d_d3}}
