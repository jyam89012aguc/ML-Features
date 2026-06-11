import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


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
    idx = num.index if hasattr(num, "index") else None
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


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def f20_vdah_376_spring_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmin63 = low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    pierced = low < rmin63
    closed_back = close > rmin63
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (pierced & closed_back & (z > 1.0)).astype(float)


def f20_vdah_377_secondary_test_lower_vol_indicator(low: pd.Series, volume: pd.Series) -> pd.Series:
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    first_test = (low <= 1.005 * rmin21)
    recent_first = first_test.shift(1).rolling(WDAYS - 1, min_periods=1).max().fillna(0.0)
    return (first_test & (recent_first > 0) & (volume < volume.rolling(WDAYS, min_periods=1).mean().shift(1))).astype(float)


def f20_vdah_378_probe_above_252d_high_close_below_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    pierced = high > rmax
    closed_below = close < rmax
    return (pierced & closed_below).astype(float)


def f20_vdah_379_rejection_wick_depth_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    upper_wick = high - pd.concat([close, close.shift(1)], axis=1).max(axis=1)
    atr = _atr(high, low, close, n=MDAYS)
    depth = _safe_div(upper_wick, atr)
    z = _rolling_zscore(depth, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return z.where(high >= rmax, np.nan)


def f20_vdah_380_tag_count_at_252d_high_252d(high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (high >= rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_381_cluster_of_rejections_5d_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((pos <= 0.33) & (high >= rmax)).astype(float)
    return (flag.rolling(WDAYS, min_periods=2).sum() >= 3).astype(float)


def f20_vdah_382_low_pierce_with_low_vol_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pierced = low < low.shift(1)
    closed_back = close > low.shift(1)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (pierced & closed_back & (volume < med)).astype(float)


def f20_vdah_383_failed_retake_of_resistance_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recently_above = (close > rmax).shift(1).rolling(3, min_periods=1).max().fillna(False).astype(bool)
    return (recently_above & (close < rmax)).astype(float)


def f20_vdah_384_cluster_inside_days_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return inside.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f20_vdah_385_rejection_at_round_number_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    near_round = pd.Series((high / 5.0 - (high / 5.0).round()).abs() <= 0.20, index=high.index)
    pos = _safe_div(close - low, high - low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (near_round & (pos <= 0.33) & (high >= rmax)).astype(float)


def f20_vdah_386_time_since_first_3sigma_vol_in_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size == 0:
            return float(v.size)
        return float(v.size - 1 - pos[0])
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f20_vdah_387_time_between_first_and_last_3sigma_vol_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 2:
            return 0.0
        return float(pos[-1] - pos[0])
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f20_vdah_388_bars_since_vol_above_252d_avg_indicator(volume: pd.Series) -> pd.Series:
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume > avg).astype(int)
    grp = flag.cumsum()
    return ((~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)).clip(upper=float(YDAYS))


def f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    burst = (z > 3.0)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = (volume < med)
    silent3 = silent & silent.shift(1) & silent.shift(2)
    return (burst.shift(3) & silent3).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    burst = (z > 3.0)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = (volume < med).astype(float)
    silent5 = silent.rolling(WDAYS, min_periods=1).sum() >= 5
    return (burst.shift(5) & silent5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    burst = (z > 3.0)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = (volume < med).astype(float)
    silent21 = silent.rolling(MDAYS, min_periods=WDAYS).sum() >= 18
    return (burst.shift(MDAYS) & silent21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_392_avg_bars_to_normalize_after_burst_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    def _f(w_z, w_v, w_m):
        vz = w_z; vv = w_v; vm = w_m
        if vz.size < 30:
            return np.nan
        bursts = np.where(vz > 3.0)[0]
        if bursts.size == 0:
            return np.nan
        normalization_lags = []
        for b in bursts:
            for j in range(b + 1, vv.size):
                if vv[j] >= vm[j]:
                    normalization_lags.append(j - b)
                    break
        return float(np.mean(normalization_lags)) if normalization_lags else np.nan
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    z_vals = z.values; v_vals = volume.values; m_vals = med.values
    n = volume.size
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(z_vals[i - YDAYS + 1: i + 1], v_vals[i - YDAYS + 1: i + 1], m_vals[i - YDAYS + 1: i + 1])
    return out


def f20_vdah_393_median_silence_length_after_burst_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    def _f(w_z, w_v, w_m):
        if w_z.size < 30:
            return np.nan
        bursts = np.where(w_z > 3.0)[0]
        if bursts.size == 0:
            return np.nan
        silences = []
        for b in bursts:
            cnt = 0
            for j in range(b + 1, w_v.size):
                if w_v[j] < w_m[j]:
                    cnt += 1
                else:
                    break
            silences.append(cnt)
        return float(np.median(silences)) if silences else np.nan
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    z_vals = z.values; v_vals = volume.values; m_vals = med.values
    n = volume.size
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(z_vals[i - YDAYS + 1: i + 1], v_vals[i - YDAYS + 1: i + 1], m_vals[i - YDAYS + 1: i + 1])
    return out


def f20_vdah_394_long_silence_period_count_252d(volume: pd.Series) -> pd.Series:
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = volume < med
    streak = _consecutive_true_streak(silent).astype(float)
    starts_10 = (streak == 10).astype(float)
    return starts_10.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_395_median_burst_to_burst_interval_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _f(w):
        if w.size < 30:
            return np.nan
        pos = np.where(w > 3.0)[0]
        if pos.size < 2:
            return np.nan
        return float(np.median(np.diff(pos)))
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    m3 = volume.rolling(3, min_periods=2).mean()
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (m3 < 0.30 * m21)).astype(float)


def f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    m5 = volume.rolling(WDAYS, min_periods=2).mean()
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (m5 < 0.50 * m21)).astype(float)


def f20_vdah_398_dryup_at_5atr_extension_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ema21 = close.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    atr = _atr(high, low, close, n=MDAYS)
    extended = close >= (ema21 + 5.0 * atr)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (extended & (volume < med)).astype(float)


def f20_vdah_399_parabolic_acceleration_no_vol_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    r5 = close / close.shift(WDAYS) - 1.0
    r21 = close / close.shift(MDAYS) - 1.0
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((r5 > 0.10) & (r21 > 0.25) & (volume < med21)).astype(float)


def f20_vdah_400_vol_per_atr_pct_rank_252d_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, n=MDAYS)
    r = _safe_div(volume, atr)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    pr = r.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return pr.where(high >= rmax, np.nan)


def f20_vdah_401_low_vol_post_2x_atr_breakout_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    up_wide = (tr > 2.0 * atr) & (close > close.shift(1))
    had = up_wide.shift(1).rolling(3, min_periods=1).max().fillna(False).astype(bool)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (had & (volume < med)).astype(float)


def f20_vdah_402_low_vol_close_above_3sigma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    cz = _rolling_zscore(close, YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((cz > 3.0) & (volume < med)).astype(float)


def f20_vdah_403_low_vol_close_above_2sigma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    cz = _rolling_zscore(close, YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((cz > 2.0) & (volume < med)).astype(float)


def f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    q95 = close.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.95)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((close > q95) & (volume < med)).astype(float)


def f20_vdah_405_low_vol_after_5_consec_up_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close > close.shift(1)
    five_up = up & up.shift(1) & up.shift(2) & up.shift(3) & up.shift(4)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (five_up & (volume < med)).astype(float)


def f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = close.expanding(min_periods=YDAYS).max()
    avg5y = volume.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg5y)
    return r.where(close >= rmax, np.nan)


def f20_vdah_407_vol_at_alltime_high_dwell_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = close.expanding(min_periods=YDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((close >= rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    avg5y = volume.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg5y)
    return r.where(close >= rmax5y, np.nan)


def f20_vdah_409_cluster_of_5y_high_low_vol_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((close >= rmax5y) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_410_bars_since_last_5y_high_vol_burst(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    cond = (z > 3.0) & (close >= rmax5y)
    flag = cond.astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_411_vol_at_3y_high_normalized(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax3y = close.rolling(DDAYS_3Y, min_periods=YDAYS).max()
    avg3y = volume.rolling(DDAYS_3Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg3y)
    return r.where(close >= rmax3y, np.nan)


def f20_vdah_412_vol_at_2y_high_normalized(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax2y = close.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    avg2y = volume.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg2y)
    return r.where(close >= rmax2y, np.nan)


def f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(close - rmin5y, rmax5y - rmin5y)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((pos >= 0.90) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    pr = volume.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return pr.where(close >= rmax5y, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_415_extreme_dryup_at_5y_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return ((close >= rmax5y) & (z < -2.0)).astype(float)


def f20_vdah_416_dd_after_3_up_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    up = close > close.shift(1)
    three_up = up.shift(1) & up.shift(2) & up.shift(3)
    dd = (pc < -0.002) & (volume > volume.shift(1))
    return (dd & three_up).astype(float)


def f20_vdah_417_dd_after_5_up_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    up = close > close.shift(1)
    five_up = up.shift(1) & up.shift(2) & up.shift(3) & up.shift(4) & up.shift(5)
    dd = (pc < -0.002) & (volume > volume.shift(1))
    return (dd & five_up).astype(float)


def f20_vdah_418_dd_immediately_after_252d_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_high = (high >= rmax).shift(1).rolling(WDAYS, min_periods=1).max().fillna(False).astype(bool)
    return (dd & recent_high).astype(float)


def f20_vdah_419_dd_immediately_after_252d_high_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_high = (high >= rmax).shift(1).rolling(WDAYS, min_periods=1).max().fillna(False).astype(bool)
    return (dd & recent_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_420_count_dds_in_first_5d_after_252d_high(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    dd = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (high >= rmax).astype(int)
    grp = is_peak.cumsum()
    bars_since_peak = (~is_peak.astype(bool)).astype(int).groupby(grp).cumsum()
    in_post_peak_window = bars_since_peak <= 5
    return dd.where(in_post_peak_window, 0.0).groupby(grp).cumsum().clip(upper=5.0)


def f20_vdah_421_dd_with_no_recovery_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    dd_3ago = dd.shift(3)
    no_up_since = (close.shift(2) <= close.shift(3)) & (close.shift(1) <= close.shift(2)) & (close <= close.shift(1))
    return (dd_3ago & no_up_since).astype(float)


def f20_vdah_422_dd_count_last_21d_after_252d_high_signal(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    dd = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    dd_count_21 = dd.rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_high = (high >= rmax).astype(float).rolling(MDAYS, min_periods=WDAYS).max() > 0
    return ((dd_count_21 >= 4) & recent_high).astype(float)


def f20_vdah_423_heavy_dd_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.02) & (volume > 1.5 * med21)).astype(float)


def f20_vdah_424_heavy_dd_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.02) & (volume > 1.5 * med21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_425_dd_with_widest_range_in_21d_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    tr = _true_range(high, low, close)
    is_widest = tr >= tr.rolling(MDAYS, min_periods=WDAYS).max()
    return (dd & is_widest).astype(float)


def f20_vdah_426_lower_high_after_252d_max_count_63d(high: pd.Series) -> pd.Series:
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    past_peak = (high >= rmax).astype(float).rolling(QDAYS, min_periods=MDAYS).max() > 0
    flag = (h21 < h21.shift(MDAYS)) & past_peak
    return flag.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_427_lower_high_with_low_vol_count_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (h21 < h21.shift(MDAYS)) & (volume < med)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_428_rolling_top_pattern_indicator(high: pd.Series, volume: pd.Series) -> pd.Series:
    h = high.rolling(MDAYS, min_periods=WDAYS).max()
    h_lag1 = h.shift(MDAYS); h_lag2 = h.shift(2 * MDAYS)
    same = ((h - h_lag1).abs() / h_lag1 < 0.01) & ((h_lag1 - h_lag2).abs() / h_lag2 < 0.01)
    v = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v_lag1 = v.shift(MDAYS); v_lag2 = v.shift(2 * MDAYS)
    vol_dec = (v < v_lag1) & (v_lag1 < v_lag2)
    return (same & vol_dec).astype(float)


def f20_vdah_429_triple_top_failure_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    h = high.rolling(MDAYS, min_periods=WDAYS).max()
    h_lag1 = h.shift(MDAYS); h_lag2 = h.shift(2 * MDAYS)
    same = ((h - h_lag1).abs() / h_lag1 < 0.01) & ((h_lag1 - h_lag2).abs() / h_lag2 < 0.01)
    lowest = pd.concat([h, h_lag1, h_lag2], axis=1).min(axis=1)
    return (same & (close < lowest * 0.98)).astype(float)


def f20_vdah_430_neckline_break_with_high_vol_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmin63 = low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = (high >= rmax).astype(float).rolling(QDAYS, min_periods=MDAYS).max() > 0
    return ((close < rmin63) & (z > 1.0) & recent_peak).astype(float)


def f20_vdah_431_rising_wedge_breakdown_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h_slope = (high.rolling(MDAYS, min_periods=WDAYS).max() - high.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS))
    l_slope = (low.rolling(MDAYS, min_periods=WDAYS).min() - low.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS))
    wedge = (h_slope > 0) & (l_slope > 0) & (h_slope < l_slope)
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    return (wedge & (close < rmin21)).astype(float)


def f20_vdah_432_rising_wedge_breakdown_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h_slope = (high.rolling(MDAYS, min_periods=WDAYS).max() - high.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS))
    l_slope = (low.rolling(MDAYS, min_periods=WDAYS).min() - low.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS))
    wedge = (h_slope > 0) & (l_slope > 0) & (h_slope < l_slope)
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    return (wedge & (close < rmin21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_433_descending_triangle_apex_close_above_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    l21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    desc = (h21 < h21.shift(MDAYS)) & ((l21 - l21.shift(MDAYS)).abs() / l21.shift(MDAYS) < 0.01)
    sitting = close > l21
    return (desc & sitting).astype(float)


def f20_vdah_434_failed_attempt_to_break_resistance_count_252d(high: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    cross = high > rmax
    next_below = high.shift(1) < rmax  # peek — flip frame: use PIT-safe shift
    cross_yest = cross.shift(1)
    return (cross_yest & (high < rmax)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_435_gap_below_uptrend_line_low_vol_indicator(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    c21 = close.rolling(MDAYS, min_periods=WDAYS).min()
    c63 = close.rolling(QDAYS, min_periods=MDAYS).min()
    trend_low = pd.concat([c21, c63], axis=1).min(axis=1)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((open < trend_low) & (volume < med)).astype(float)


def f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (high >= rmax) & (volume < med)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_437_cumulative_vol_deficit_below_median_252d(volume: pd.Series) -> pd.Series:
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    deficit = (med - volume).clip(lower=0.0)
    return deficit.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    q20 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.20)
    return ((pos >= 0.90) & (volume <= q20)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_439_avg_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_440_median_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).median()


def f20_vdah_441_max_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_442_min_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).min()


def f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v = volume.where(high >= rmax, np.nan)
    return v.rolling(YDAYS, min_periods=QDAYS).max() - v.rolling(YDAYS, min_periods=QDAYS).min()


def f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    pr = volume.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    q = (pr * 5.0).clip(upper=4.999)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return q.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_high_avg = volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    overall_avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(at_high_avg, overall_avg)


def f20_vdah_446_low_vol_close_top_decile_max_streak_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    cond = (pos >= 0.90) & (volume < med)
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_447_min_vol_age_at_252d_high(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    vmin = volume.rolling(YDAYS, min_periods=QDAYS).min()
    cond = (high >= rmax) & (volume <= vmin)
    flag = cond.astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_448_low_vol_within_5pct_of_252d_high_count(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((high >= 0.95 * rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_449_low_vol_within_2pct_of_252d_high_count(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((high >= 0.98 * rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_450_low_vol_at_exact_252d_high_count(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((high >= rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_376_spring_failure_indicator_d3(high, low, close, volume):
    return f20_vdah_376_spring_failure_indicator(high, low, close, volume).diff().diff().diff()


def f20_vdah_377_secondary_test_lower_vol_indicator_d3(low, volume):
    return f20_vdah_377_secondary_test_lower_vol_indicator(low, volume).diff().diff().diff()


def f20_vdah_378_probe_above_252d_high_close_below_indicator_d3(high, close):
    return f20_vdah_378_probe_above_252d_high_close_below_indicator(high, close).diff().diff().diff()


def f20_vdah_379_rejection_wick_depth_zscore_252d_d3(high, low, close):
    return f20_vdah_379_rejection_wick_depth_zscore_252d(high, low, close).diff().diff().diff()


def f20_vdah_380_tag_count_at_252d_high_252d_d3(high):
    return f20_vdah_380_tag_count_at_252d_high_252d(high).diff().diff().diff()


def f20_vdah_381_cluster_of_rejections_5d_indicator_d3(high, low, close):
    return f20_vdah_381_cluster_of_rejections_5d_indicator(high, low, close).diff().diff().diff()


def f20_vdah_382_low_pierce_with_low_vol_indicator_d3(low, close, volume):
    return f20_vdah_382_low_pierce_with_low_vol_indicator(low, close, volume).diff().diff().diff()


def f20_vdah_383_failed_retake_of_resistance_indicator_d3(high, close):
    return f20_vdah_383_failed_retake_of_resistance_indicator(high, close).diff().diff().diff()


def f20_vdah_384_cluster_inside_days_count_21d_d3(high, low):
    return f20_vdah_384_cluster_inside_days_count_21d(high, low).diff().diff().diff()


def f20_vdah_385_rejection_at_round_number_indicator_d3(high, low, close):
    return f20_vdah_385_rejection_at_round_number_indicator(high, low, close).diff().diff().diff()


def f20_vdah_386_time_since_first_3sigma_vol_in_252d_d3(volume):
    return f20_vdah_386_time_since_first_3sigma_vol_in_252d(volume).diff().diff().diff()


def f20_vdah_387_time_between_first_and_last_3sigma_vol_252d_d3(volume):
    return f20_vdah_387_time_between_first_and_last_3sigma_vol_252d(volume).diff().diff().diff()


def f20_vdah_388_bars_since_vol_above_252d_avg_indicator_d3(volume):
    return f20_vdah_388_bars_since_vol_above_252d_avg_indicator(volume).diff().diff().diff()


def f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d_d3(volume):
    return f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d(volume).diff().diff().diff()


def f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d_d3(volume):
    return f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d(volume).diff().diff().diff()


def f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d_d3(volume):
    return f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d(volume).diff().diff().diff()


def f20_vdah_392_avg_bars_to_normalize_after_burst_252d_d3(volume):
    return f20_vdah_392_avg_bars_to_normalize_after_burst_252d(volume).diff().diff().diff()


def f20_vdah_393_median_silence_length_after_burst_252d_d3(volume):
    return f20_vdah_393_median_silence_length_after_burst_252d(volume).diff().diff().diff()


def f20_vdah_394_long_silence_period_count_252d_d3(volume):
    return f20_vdah_394_long_silence_period_count_252d(volume).diff().diff().diff()


def f20_vdah_395_median_burst_to_burst_interval_252d_d3(volume):
    return f20_vdah_395_median_burst_to_burst_interval_252d(volume).diff().diff().diff()


def f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg_d3(high, volume):
    return f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg(high, volume).diff().diff().diff()


def f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg_d3(high, volume):
    return f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg(high, volume).diff().diff().diff()


def f20_vdah_398_dryup_at_5atr_extension_indicator_d3(high, low, close, volume):
    return f20_vdah_398_dryup_at_5atr_extension_indicator(high, low, close, volume).diff().diff().diff()


def f20_vdah_399_parabolic_acceleration_no_vol_indicator_d3(close, volume):
    return f20_vdah_399_parabolic_acceleration_no_vol_indicator(close, volume).diff().diff().diff()


def f20_vdah_400_vol_per_atr_pct_rank_252d_at_high_d3(high, low, close, volume):
    return f20_vdah_400_vol_per_atr_pct_rank_252d_at_high(high, low, close, volume).diff().diff().diff()


def f20_vdah_401_low_vol_post_2x_atr_breakout_indicator_d3(high, low, close, volume):
    return f20_vdah_401_low_vol_post_2x_atr_breakout_indicator(high, low, close, volume).diff().diff().diff()


def f20_vdah_402_low_vol_close_above_3sigma_252d_d3(close, volume):
    return f20_vdah_402_low_vol_close_above_3sigma_252d(close, volume).diff().diff().diff()


def f20_vdah_403_low_vol_close_above_2sigma_252d_d3(close, volume):
    return f20_vdah_403_low_vol_close_above_2sigma_252d(close, volume).diff().diff().diff()


def f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator_d3(close, volume):
    return f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator(close, volume).diff().diff().diff()


def f20_vdah_405_low_vol_after_5_consec_up_days_indicator_d3(close, volume):
    return f20_vdah_405_low_vol_after_5_consec_up_days_indicator(close, volume).diff().diff().diff()


def f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg_d3(close, volume):
    return f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg(close, volume).diff().diff().diff()


def f20_vdah_407_vol_at_alltime_high_dwell_count_252d_d3(close, volume):
    return f20_vdah_407_vol_at_alltime_high_dwell_count_252d(close, volume).diff().diff().diff()


def f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg_d3(close, volume):
    return f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg(close, volume).diff().diff().diff()


def f20_vdah_409_cluster_of_5y_high_low_vol_count_252d_d3(close, volume):
    return f20_vdah_409_cluster_of_5y_high_low_vol_count_252d(close, volume).diff().diff().diff()


def f20_vdah_410_bars_since_last_5y_high_vol_burst_d3(close, volume):
    return f20_vdah_410_bars_since_last_5y_high_vol_burst(close, volume).diff().diff().diff()


def f20_vdah_411_vol_at_3y_high_normalized_d3(close, volume):
    return f20_vdah_411_vol_at_3y_high_normalized(close, volume).diff().diff().diff()


def f20_vdah_412_vol_at_2y_high_normalized_d3(close, volume):
    return f20_vdah_412_vol_at_2y_high_normalized(close, volume).diff().diff().diff()


def f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d_d3(close, volume):
    return f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d(close, volume).diff().diff().diff()


def f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d_d3(close, volume):
    return f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d(close, volume).diff().diff().diff()


def f20_vdah_415_extreme_dryup_at_5y_high_indicator_d3(close, volume):
    return f20_vdah_415_extreme_dryup_at_5y_high_indicator(close, volume).diff().diff().diff()


def f20_vdah_416_dd_after_3_up_days_indicator_d3(close, volume):
    return f20_vdah_416_dd_after_3_up_days_indicator(close, volume).diff().diff().diff()


def f20_vdah_417_dd_after_5_up_days_indicator_d3(close, volume):
    return f20_vdah_417_dd_after_5_up_days_indicator(close, volume).diff().diff().diff()


def f20_vdah_418_dd_immediately_after_252d_high_indicator_d3(high, close, volume):
    return f20_vdah_418_dd_immediately_after_252d_high_indicator(high, close, volume).diff().diff().diff()


def f20_vdah_419_dd_immediately_after_252d_high_count_252d_d3(high, close, volume):
    return f20_vdah_419_dd_immediately_after_252d_high_count_252d(high, close, volume).diff().diff().diff()


def f20_vdah_420_count_dds_in_first_5d_after_252d_high_d3(high, close, volume):
    return f20_vdah_420_count_dds_in_first_5d_after_252d_high(high, close, volume).diff().diff().diff()


def f20_vdah_421_dd_with_no_recovery_indicator_d3(close, volume):
    return f20_vdah_421_dd_with_no_recovery_indicator(close, volume).diff().diff().diff()


def f20_vdah_422_dd_count_last_21d_after_252d_high_signal_d3(high, close, volume):
    return f20_vdah_422_dd_count_last_21d_after_252d_high_signal(high, close, volume).diff().diff().diff()


def f20_vdah_423_heavy_dd_indicator_d3(close, volume):
    return f20_vdah_423_heavy_dd_indicator(close, volume).diff().diff().diff()


def f20_vdah_424_heavy_dd_count_252d_d3(close, volume):
    return f20_vdah_424_heavy_dd_count_252d(close, volume).diff().diff().diff()


def f20_vdah_425_dd_with_widest_range_in_21d_indicator_d3(high, low, close, volume):
    return f20_vdah_425_dd_with_widest_range_in_21d_indicator(high, low, close, volume).diff().diff().diff()


def f20_vdah_426_lower_high_after_252d_max_count_63d_d3(high):
    return f20_vdah_426_lower_high_after_252d_max_count_63d(high).diff().diff().diff()


def f20_vdah_427_lower_high_with_low_vol_count_252d_d3(high, volume):
    return f20_vdah_427_lower_high_with_low_vol_count_252d(high, volume).diff().diff().diff()


def f20_vdah_428_rolling_top_pattern_indicator_d3(high, volume):
    return f20_vdah_428_rolling_top_pattern_indicator(high, volume).diff().diff().diff()


def f20_vdah_429_triple_top_failure_indicator_d3(high, close):
    return f20_vdah_429_triple_top_failure_indicator(high, close).diff().diff().diff()


def f20_vdah_430_neckline_break_with_high_vol_indicator_d3(high, low, close, volume):
    return f20_vdah_430_neckline_break_with_high_vol_indicator(high, low, close, volume).diff().diff().diff()


def f20_vdah_431_rising_wedge_breakdown_indicator_d3(high, low, close):
    return f20_vdah_431_rising_wedge_breakdown_indicator(high, low, close).diff().diff().diff()


def f20_vdah_432_rising_wedge_breakdown_count_252d_d3(high, low, close):
    return f20_vdah_432_rising_wedge_breakdown_count_252d(high, low, close).diff().diff().diff()


def f20_vdah_433_descending_triangle_apex_close_above_indicator_d3(high, low, close):
    return f20_vdah_433_descending_triangle_apex_close_above_indicator(high, low, close).diff().diff().diff()


def f20_vdah_434_failed_attempt_to_break_resistance_count_252d_d3(high):
    return f20_vdah_434_failed_attempt_to_break_resistance_count_252d(high).diff().diff().diff()


def f20_vdah_435_gap_below_uptrend_line_low_vol_indicator_d3(open, close, volume):
    return f20_vdah_435_gap_below_uptrend_line_low_vol_indicator(open, close, volume).diff().diff().diff()


def f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high_d3(high, volume):
    return f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high(high, volume).diff().diff().diff()


def f20_vdah_437_cumulative_vol_deficit_below_median_252d_d3(volume):
    return f20_vdah_437_cumulative_vol_deficit_below_median_252d(volume).diff().diff().diff()


def f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d_d3(high, low, close, volume):
    return f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_439_avg_vol_on_at_252d_high_bars_252d_d3(high, volume):
    return f20_vdah_439_avg_vol_on_at_252d_high_bars_252d(high, volume).diff().diff().diff()


def f20_vdah_440_median_vol_on_at_252d_high_bars_252d_d3(high, volume):
    return f20_vdah_440_median_vol_on_at_252d_high_bars_252d(high, volume).diff().diff().diff()


def f20_vdah_441_max_vol_on_at_252d_high_bars_252d_d3(high, volume):
    return f20_vdah_441_max_vol_on_at_252d_high_bars_252d(high, volume).diff().diff().diff()


def f20_vdah_442_min_vol_on_at_252d_high_bars_252d_d3(high, volume):
    return f20_vdah_442_min_vol_on_at_252d_high_bars_252d(high, volume).diff().diff().diff()


def f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d_d3(high, volume):
    return f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d(high, volume).diff().diff().diff()


def f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d_d3(high, volume):
    return f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d(high, volume).diff().diff().diff()


def f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d_d3(high, volume):
    return f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d(high, volume).diff().diff().diff()


def f20_vdah_446_low_vol_close_top_decile_max_streak_252d_d3(high, low, close, volume):
    return f20_vdah_446_low_vol_close_top_decile_max_streak_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_447_min_vol_age_at_252d_high_d3(high, volume):
    return f20_vdah_447_min_vol_age_at_252d_high(high, volume).diff().diff().diff()


def f20_vdah_448_low_vol_within_5pct_of_252d_high_count_d3(high, volume):
    return f20_vdah_448_low_vol_within_5pct_of_252d_high_count(high, volume).diff().diff().diff()


def f20_vdah_449_low_vol_within_2pct_of_252d_high_count_d3(high, volume):
    return f20_vdah_449_low_vol_within_2pct_of_252d_high_count(high, volume).diff().diff().diff()


def f20_vdah_450_low_vol_at_exact_252d_high_count_d3(high, volume):
    return f20_vdah_450_low_vol_at_exact_252d_high_count(high, volume).diff().diff().diff()


VOLUME_DRYUP_AT_HIGH_D3_REGISTRY_376_450 = {
    "f20_vdah_376_spring_failure_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_376_spring_failure_indicator_d3},
    "f20_vdah_377_secondary_test_lower_vol_indicator_d3": {"inputs": ["low", "volume"], "func": f20_vdah_377_secondary_test_lower_vol_indicator_d3},
    "f20_vdah_378_probe_above_252d_high_close_below_indicator_d3": {"inputs": ["high", "close"], "func": f20_vdah_378_probe_above_252d_high_close_below_indicator_d3},
    "f20_vdah_379_rejection_wick_depth_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f20_vdah_379_rejection_wick_depth_zscore_252d_d3},
    "f20_vdah_380_tag_count_at_252d_high_252d_d3": {"inputs": ["high"], "func": f20_vdah_380_tag_count_at_252d_high_252d_d3},
    "f20_vdah_381_cluster_of_rejections_5d_indicator_d3": {"inputs": ["high", "low", "close"], "func": f20_vdah_381_cluster_of_rejections_5d_indicator_d3},
    "f20_vdah_382_low_pierce_with_low_vol_indicator_d3": {"inputs": ["low", "close", "volume"], "func": f20_vdah_382_low_pierce_with_low_vol_indicator_d3},
    "f20_vdah_383_failed_retake_of_resistance_indicator_d3": {"inputs": ["high", "close"], "func": f20_vdah_383_failed_retake_of_resistance_indicator_d3},
    "f20_vdah_384_cluster_inside_days_count_21d_d3": {"inputs": ["high", "low"], "func": f20_vdah_384_cluster_inside_days_count_21d_d3},
    "f20_vdah_385_rejection_at_round_number_indicator_d3": {"inputs": ["high", "low", "close"], "func": f20_vdah_385_rejection_at_round_number_indicator_d3},
    "f20_vdah_386_time_since_first_3sigma_vol_in_252d_d3": {"inputs": ["volume"], "func": f20_vdah_386_time_since_first_3sigma_vol_in_252d_d3},
    "f20_vdah_387_time_between_first_and_last_3sigma_vol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_387_time_between_first_and_last_3sigma_vol_252d_d3},
    "f20_vdah_388_bars_since_vol_above_252d_avg_indicator_d3": {"inputs": ["volume"], "func": f20_vdah_388_bars_since_vol_above_252d_avg_indicator_d3},
    "f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d_d3": {"inputs": ["volume"], "func": f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d_d3},
    "f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d_d3": {"inputs": ["volume"], "func": f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d_d3},
    "f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d_d3": {"inputs": ["volume"], "func": f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d_d3},
    "f20_vdah_392_avg_bars_to_normalize_after_burst_252d_d3": {"inputs": ["volume"], "func": f20_vdah_392_avg_bars_to_normalize_after_burst_252d_d3},
    "f20_vdah_393_median_silence_length_after_burst_252d_d3": {"inputs": ["volume"], "func": f20_vdah_393_median_silence_length_after_burst_252d_d3},
    "f20_vdah_394_long_silence_period_count_252d_d3": {"inputs": ["volume"], "func": f20_vdah_394_long_silence_period_count_252d_d3},
    "f20_vdah_395_median_burst_to_burst_interval_252d_d3": {"inputs": ["volume"], "func": f20_vdah_395_median_burst_to_burst_interval_252d_d3},
    "f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg_d3": {"inputs": ["high", "volume"], "func": f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg_d3},
    "f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg_d3": {"inputs": ["high", "volume"], "func": f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg_d3},
    "f20_vdah_398_dryup_at_5atr_extension_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_398_dryup_at_5atr_extension_indicator_d3},
    "f20_vdah_399_parabolic_acceleration_no_vol_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_399_parabolic_acceleration_no_vol_indicator_d3},
    "f20_vdah_400_vol_per_atr_pct_rank_252d_at_high_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_400_vol_per_atr_pct_rank_252d_at_high_d3},
    "f20_vdah_401_low_vol_post_2x_atr_breakout_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_401_low_vol_post_2x_atr_breakout_indicator_d3},
    "f20_vdah_402_low_vol_close_above_3sigma_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_402_low_vol_close_above_3sigma_252d_d3},
    "f20_vdah_403_low_vol_close_above_2sigma_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_403_low_vol_close_above_2sigma_252d_d3},
    "f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator_d3},
    "f20_vdah_405_low_vol_after_5_consec_up_days_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_405_low_vol_after_5_consec_up_days_indicator_d3},
    "f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg_d3": {"inputs": ["close", "volume"], "func": f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg_d3},
    "f20_vdah_407_vol_at_alltime_high_dwell_count_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_407_vol_at_alltime_high_dwell_count_252d_d3},
    "f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg_d3": {"inputs": ["close", "volume"], "func": f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg_d3},
    "f20_vdah_409_cluster_of_5y_high_low_vol_count_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_409_cluster_of_5y_high_low_vol_count_252d_d3},
    "f20_vdah_410_bars_since_last_5y_high_vol_burst_d3": {"inputs": ["close", "volume"], "func": f20_vdah_410_bars_since_last_5y_high_vol_burst_d3},
    "f20_vdah_411_vol_at_3y_high_normalized_d3": {"inputs": ["close", "volume"], "func": f20_vdah_411_vol_at_3y_high_normalized_d3},
    "f20_vdah_412_vol_at_2y_high_normalized_d3": {"inputs": ["close", "volume"], "func": f20_vdah_412_vol_at_2y_high_normalized_d3},
    "f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d_d3},
    "f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d_d3},
    "f20_vdah_415_extreme_dryup_at_5y_high_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_415_extreme_dryup_at_5y_high_indicator_d3},
    "f20_vdah_416_dd_after_3_up_days_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_416_dd_after_3_up_days_indicator_d3},
    "f20_vdah_417_dd_after_5_up_days_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_417_dd_after_5_up_days_indicator_d3},
    "f20_vdah_418_dd_immediately_after_252d_high_indicator_d3": {"inputs": ["high", "close", "volume"], "func": f20_vdah_418_dd_immediately_after_252d_high_indicator_d3},
    "f20_vdah_419_dd_immediately_after_252d_high_count_252d_d3": {"inputs": ["high", "close", "volume"], "func": f20_vdah_419_dd_immediately_after_252d_high_count_252d_d3},
    "f20_vdah_420_count_dds_in_first_5d_after_252d_high_d3": {"inputs": ["high", "close", "volume"], "func": f20_vdah_420_count_dds_in_first_5d_after_252d_high_d3},
    "f20_vdah_421_dd_with_no_recovery_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_421_dd_with_no_recovery_indicator_d3},
    "f20_vdah_422_dd_count_last_21d_after_252d_high_signal_d3": {"inputs": ["high", "close", "volume"], "func": f20_vdah_422_dd_count_last_21d_after_252d_high_signal_d3},
    "f20_vdah_423_heavy_dd_indicator_d3": {"inputs": ["close", "volume"], "func": f20_vdah_423_heavy_dd_indicator_d3},
    "f20_vdah_424_heavy_dd_count_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_424_heavy_dd_count_252d_d3},
    "f20_vdah_425_dd_with_widest_range_in_21d_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_425_dd_with_widest_range_in_21d_indicator_d3},
    "f20_vdah_426_lower_high_after_252d_max_count_63d_d3": {"inputs": ["high"], "func": f20_vdah_426_lower_high_after_252d_max_count_63d_d3},
    "f20_vdah_427_lower_high_with_low_vol_count_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_427_lower_high_with_low_vol_count_252d_d3},
    "f20_vdah_428_rolling_top_pattern_indicator_d3": {"inputs": ["high", "volume"], "func": f20_vdah_428_rolling_top_pattern_indicator_d3},
    "f20_vdah_429_triple_top_failure_indicator_d3": {"inputs": ["high", "close"], "func": f20_vdah_429_triple_top_failure_indicator_d3},
    "f20_vdah_430_neckline_break_with_high_vol_indicator_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_430_neckline_break_with_high_vol_indicator_d3},
    "f20_vdah_431_rising_wedge_breakdown_indicator_d3": {"inputs": ["high", "low", "close"], "func": f20_vdah_431_rising_wedge_breakdown_indicator_d3},
    "f20_vdah_432_rising_wedge_breakdown_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f20_vdah_432_rising_wedge_breakdown_count_252d_d3},
    "f20_vdah_433_descending_triangle_apex_close_above_indicator_d3": {"inputs": ["high", "low", "close"], "func": f20_vdah_433_descending_triangle_apex_close_above_indicator_d3},
    "f20_vdah_434_failed_attempt_to_break_resistance_count_252d_d3": {"inputs": ["high"], "func": f20_vdah_434_failed_attempt_to_break_resistance_count_252d_d3},
    "f20_vdah_435_gap_below_uptrend_line_low_vol_indicator_d3": {"inputs": ["open", "close", "volume"], "func": f20_vdah_435_gap_below_uptrend_line_low_vol_indicator_d3},
    "f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high_d3": {"inputs": ["high", "volume"], "func": f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high_d3},
    "f20_vdah_437_cumulative_vol_deficit_below_median_252d_d3": {"inputs": ["volume"], "func": f20_vdah_437_cumulative_vol_deficit_below_median_252d_d3},
    "f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d_d3},
    "f20_vdah_439_avg_vol_on_at_252d_high_bars_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_439_avg_vol_on_at_252d_high_bars_252d_d3},
    "f20_vdah_440_median_vol_on_at_252d_high_bars_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_440_median_vol_on_at_252d_high_bars_252d_d3},
    "f20_vdah_441_max_vol_on_at_252d_high_bars_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_441_max_vol_on_at_252d_high_bars_252d_d3},
    "f20_vdah_442_min_vol_on_at_252d_high_bars_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_442_min_vol_on_at_252d_high_bars_252d_d3},
    "f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d_d3},
    "f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d_d3},
    "f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d_d3": {"inputs": ["high", "volume"], "func": f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d_d3},
    "f20_vdah_446_low_vol_close_top_decile_max_streak_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_446_low_vol_close_top_decile_max_streak_252d_d3},
    "f20_vdah_447_min_vol_age_at_252d_high_d3": {"inputs": ["high", "volume"], "func": f20_vdah_447_min_vol_age_at_252d_high_d3},
    "f20_vdah_448_low_vol_within_5pct_of_252d_high_count_d3": {"inputs": ["high", "volume"], "func": f20_vdah_448_low_vol_within_5pct_of_252d_high_count_d3},
    "f20_vdah_449_low_vol_within_2pct_of_252d_high_count_d3": {"inputs": ["high", "volume"], "func": f20_vdah_449_low_vol_within_2pct_of_252d_high_count_d3},
    "f20_vdah_450_low_vol_at_exact_252d_high_count_d3": {"inputs": ["high", "volume"], "func": f20_vdah_450_low_vol_at_exact_252d_high_count_d3},
}
