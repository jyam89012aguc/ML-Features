"""advance_speed d1 features 001_075 — 1st-derivative wrappers.

Each function inlines the corresponding base body and appends .diff() so the output is the first bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__001_075.py."""
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

def f02_advs_001_compound_log_speed_from_252d_low_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0).diff()

def f02_advs_002_compound_log_speed_from_63d_low_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(QDAYS, min_periods=MDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0).diff()

def f02_advs_003_compound_log_speed_from_1260d_low_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(1260, min_periods=YDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(1260, min_periods=YDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0).diff()

def f02_advs_004_ratio_compound_speed_252d_vs_1260d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    r252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    r1260 = low.rolling(1260, min_periods=YDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    d252 = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    d1260 = low.rolling(1260, min_periods=YDAYS).apply(_dsm, raw=True)
    sp_y = _safe_div(_safe_log(close) - _safe_log(r252), d252 + 1.0)
    sp_5y = _safe_div(_safe_log(close) - _safe_log(r1260), d1260 + 1.0)
    return _safe_div(sp_y, sp_5y).diff()

def f02_advs_005_compound_log_speed_zscore_in_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    sp = _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0)
    return _rolling_zscore(sp, YDAYS).diff()

def f02_advs_006_compound_speed_excess_vs_baseline_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    sp = _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0)
    return (sp - sp.rolling(YDAYS, min_periods=QDAYS).median()).diff()

def f02_advs_007_log_close_to_rolling_252d_vwap_d1(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap = _safe_div(pv, vv)

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(vwap), days + 1.0).diff()

def f02_advs_008_compound_speed_in_atr_units_from_252d_low_d1(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div((close - rmin) / atr.replace(0, np.nan), days + 1.0).diff()

def f02_advs_009_compound_speed_in_atr_units_from_63d_low_d1(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    atr = _atr(high, low, close, MDAYS)

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(QDAYS, min_periods=MDAYS).apply(_dsm, raw=True)
    return _safe_div((close - rmin) / atr.replace(0, np.nan), days + 1.0).diff()

def f02_advs_010_recovery_speed_from_252d_low_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (rmax - rmin).replace(0, np.nan)

    def _dsm(w):
        return len(w) - 1 - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div((close - rmin) / rng, days + 1.0).diff()

def f02_advs_011_exponential_velocity_ema_21d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return r.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean().diff()

def f02_advs_012_log_arc_height_above_min_low_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    height = (_safe_log(close) - _safe_log(rmin)).clip(lower=0)
    return height.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f02_advs_013_velocity_recent_minus_baseline_21d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    recent = r.rolling(MDAYS, min_periods=WDAYS).mean()
    base = r.rolling(YDAYS, min_periods=QDAYS).mean()
    return (recent - base).diff()

def f02_advs_014_velocity_dispersion_iqr_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q75 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q25 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (q75 - q25).diff()

def f02_advs_015_velocity_skew_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).skew().diff()

def f02_advs_016_velocity_kurt_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).kurt().diff()

def f02_advs_017_velocity_p95_minus_p50_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q95 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)
    return (q95 - q50).diff()

def f02_advs_018_velocity_p50_minus_p5_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)
    q05 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    return (q50 - q05).diff()

def f02_advs_019_velocity_pct_rank_5d_in_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f02_advs_020_velocity_pct_rank_21d_in_252d_d1(close: pd.Series) -> pd.Series:
    r21 = _safe_log(close).diff(MDAYS)
    return r21.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f02_advs_021_velocity_pct_rank_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    r63 = _safe_log(close).diff(QDAYS)
    return r63.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f02_advs_022_velocity_burst_above_2sd_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f02_advs_023_velocity_burst_below_2sd_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z < -2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f02_advs_024_velocity_runs_above_zero_max_252d_d1(close: pd.Series) -> pd.Series:
    pos = (_safe_log(close).diff() > 0).astype(int)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_025_velocity_mad_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff().abs()
    return r.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f02_advs_026_acceleration_max_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_027_acceleration_min_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).min().diff()

def f02_advs_028_acceleration_range_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return (a.rolling(YDAYS, min_periods=QDAYS).max() - a.rolling(YDAYS, min_periods=QDAYS).min()).diff()

def f02_advs_029_acceleration_sign_changes_count_63d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    flip = (np.sign(a) != np.sign(a.shift(1))).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f02_advs_030_acceleration_positive_run_max_252d_d1(close: pd.Series) -> pd.Series:
    pos = (_safe_log(close).diff().diff() > 0).astype(int)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_031_acceleration_negative_run_max_252d_d1(close: pd.Series) -> pd.Series:
    neg = (_safe_log(close).diff().diff() < 0).astype(int)
    grp = (neg == 0).cumsum()
    streak = neg.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_032_terminal_acceleration_21d_zscore_in_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    mr = a.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(mr, YDAYS).diff()

def f02_advs_033_acceleration_dispersion_iqr_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return (a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)).diff()

def f02_advs_034_acceleration_skew_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).skew().diff()

def f02_advs_035_acceleration_kurt_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).kurt().diff()

def f02_advs_036_acceleration_pct_rank_recent_5d_in_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    m5 = a.rolling(WDAYS, min_periods=2).mean()
    return m5.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f02_advs_037_acceleration_above_p95_count_63d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    p95 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return (a > p95).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f02_advs_038_acceleration_autocorr_lag1_63d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()

    def _ac(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        x, y = (w[:-1], w[1:])
        if x.std() == 0 or y.std() == 0:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    return a.rolling(QDAYS, min_periods=MDAYS).apply(_ac, raw=True).diff()

def f02_advs_039_acceleration_autocorr_lag5_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()

    def _ac(w):
        if np.isnan(w).any() or len(w) < 11:
            return np.nan
        x, y = (w[:-5], w[5:])
        if x.std() == 0 or y.std() == 0:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True).diff()

def f02_advs_040_acceleration_velocity_corr_63d_d1(close: pd.Series) -> pd.Series:
    v = _safe_log(close).diff()
    a = v.diff()
    return v.rolling(QDAYS, min_periods=MDAYS).corr(a).diff()

def f02_advs_041_acceleration_vol_corr_63d_d1(close: pd.Series) -> pd.Series:
    v = _safe_log(close).diff()
    a = v.diff()
    return a.rolling(QDAYS, min_periods=MDAYS).corr(v.abs()).diff()

def f02_advs_042_acceleration_zscore_p95_252d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    z = _rolling_zscore(a, YDAYS)
    return z.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).diff()

def f02_advs_043_acceleration_dropoff_5d_vs_21d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return (a.rolling(WDAYS, min_periods=2).mean() - a.rolling(MDAYS, min_periods=WDAYS).mean()).diff()

def f02_advs_044_pre_peak_acceleration_buildup_63d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return _rolling_slope(a, QDAYS).diff()

def f02_advs_045_acceleration_terminal_thrust_5d_zscore_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    m5 = a.rolling(WDAYS, min_periods=2).mean()
    return _rolling_zscore(m5, YDAYS).diff()

def f02_advs_046_max_1d_log_return_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_047_min_1d_log_return_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).min().diff()

def f02_advs_048_max_1d_log_return_zscore_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    mx = r.rolling(YDAYS, min_periods=QDAYS).max()
    return _rolling_zscore(mx, YDAYS).diff()

def f02_advs_049_count_outsize_up_days_z_gt_3_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f02_advs_050_count_outsize_down_days_z_lt_neg3_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z < -3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f02_advs_051_mean_top10_log_returns_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()

    def _t10(w):
        if np.isnan(w).all():
            return np.nan
        ww = w[~np.isnan(w)]
        if len(ww) < 10:
            return np.nan
        return float(np.sort(ww)[-10:].mean())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_t10, raw=True).diff()

def f02_advs_052_mean_bottom10_log_returns_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()

    def _b10(w):
        if np.isnan(w).all():
            return np.nan
        ww = w[~np.isnan(w)]
        if len(ww) < 10:
            return np.nan
        return float(np.sort(ww)[:10].mean())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_b10, raw=True).diff()

def f02_advs_053_ratio_top10_to_bottom10_returns_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()

    def _t10(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[-10:].mean()) if len(ww) >= 10 else np.nan

    def _b10(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[:10].mean()) if len(ww) >= 10 else np.nan
    top = r.rolling(YDAYS, min_periods=QDAYS).apply(_t10, raw=True)
    bot = r.rolling(YDAYS, min_periods=QDAYS).apply(_b10, raw=True)
    return _safe_div(top, bot.abs()).diff()

def f02_advs_054_share_of_252d_log_gain_from_top10_days_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()

    def _t10s(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[-10:].sum()) if len(ww) >= 10 else np.nan
    top_sum = r.rolling(YDAYS, min_periods=QDAYS).apply(_t10s, raw=True)
    total = r.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(top_sum, total).diff()

def f02_advs_055_share_of_252d_log_gain_from_top5_days_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()

    def _t5s(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[-5:].sum()) if len(ww) >= 5 else np.nan
    top_sum = r.rolling(YDAYS, min_periods=QDAYS).apply(_t5s, raw=True)
    total = r.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(top_sum, total).diff()

def f02_advs_056_days_above_3pct_log_return_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return (r > 0.03).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f02_advs_057_days_below_neg3pct_log_return_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    return (r < -0.03).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f02_advs_058_max_3d_log_return_252d_d1(close: pd.Series) -> pd.Series:
    r3 = _safe_log(close).diff(3)
    return r3.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_059_max_5d_log_return_252d_d1(close: pd.Series) -> pd.Series:
    r5 = _safe_log(close).diff(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_060_max_10d_log_return_252d_d1(close: pd.Series) -> pd.Series:
    r10 = _safe_log(close).diff(10)
    return r10.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f02_advs_061_velocity_volume_corr_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lv = _safe_log(volume)
    return r.rolling(QDAYS, min_periods=MDAYS).corr(lv).diff()

def f02_advs_062_velocity_volume_corr_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lv = _safe_log(volume)
    return r.rolling(YDAYS, min_periods=QDAYS).corr(lv).diff()

def f02_advs_063_velocity_per_log_volume_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r21 = _safe_log(close).diff(MDAYS)
    cv = _safe_log(volume).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(r21, cv).diff()

def f02_advs_064_velocity_per_log_volume_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r63 = _safe_log(close).diff(QDAYS)
    cv = _safe_log(volume).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(r63, cv).diff()

def f02_advs_065_fractal_efficiency_21d_d1(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    net = (lp - lp.shift(MDAYS)).abs()
    path = lp.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(net, path).diff()

def f02_advs_066_fractal_efficiency_63d_d1(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    net = (lp - lp.shift(QDAYS)).abs()
    path = lp.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, path).diff()

def f02_advs_067_fractal_efficiency_252d_d1(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    net = (lp - lp.shift(YDAYS)).abs()
    path = lp.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, path).diff()

def f02_advs_068_efficiency_ratio_21d_d1(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    net = lp - lp.shift(MDAYS)
    path = lp.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(net, path).diff()

def f02_advs_069_efficiency_ratio_63d_d1(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    net = lp - lp.shift(QDAYS)
    path = lp.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, path).diff()

def f02_advs_070_efficiency_ratio_change_21d_vs_63d_d1(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    net21 = lp - lp.shift(MDAYS)
    path21 = lp.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    net63 = lp - lp.shift(QDAYS)
    path63 = lp.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(net21, path21) - _safe_div(net63, path63)).diff()

def f02_advs_071_kaufman_efficiency_252d_d1(close: pd.Series) -> pd.Series:
    lp = _safe_log(close)
    net = lp - lp.shift(YDAYS)
    path = lp.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, path).diff()

def f02_advs_072_advance_path_smoothness_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    m = r.rolling(QDAYS, min_periods=MDAYS).mean().abs()
    cv = sd / m.replace(0, np.nan)
    return _safe_div(pd.Series(1.0, index=close.index), 1.0 + cv).diff()

def f02_advs_073_advance_path_smoothness_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    m = r.rolling(YDAYS, min_periods=QDAYS).mean().abs()
    cv = sd / m.replace(0, np.nan)
    return _safe_div(pd.Series(1.0, index=close.index), 1.0 + cv).diff()

def f02_advs_074_log_return_per_atr_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    r = _safe_log(close).diff(YDAYS)
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(r * close, atr).diff()

def f02_advs_075_close_distance_per_atr_from_63d_low_d1(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return ((close - rmin) / atr.replace(0, np.nan)).diff()
ADVANCE_SPEED_D1_REGISTRY_001_075 = {'f02_advs_001_compound_log_speed_from_252d_low_d1': {'inputs': ['close', 'low'], 'func': f02_advs_001_compound_log_speed_from_252d_low_d1}, 'f02_advs_002_compound_log_speed_from_63d_low_d1': {'inputs': ['close', 'low'], 'func': f02_advs_002_compound_log_speed_from_63d_low_d1}, 'f02_advs_003_compound_log_speed_from_1260d_low_d1': {'inputs': ['close', 'low'], 'func': f02_advs_003_compound_log_speed_from_1260d_low_d1}, 'f02_advs_004_ratio_compound_speed_252d_vs_1260d_d1': {'inputs': ['close', 'low'], 'func': f02_advs_004_ratio_compound_speed_252d_vs_1260d_d1}, 'f02_advs_005_compound_log_speed_zscore_in_252d_d1': {'inputs': ['close', 'low'], 'func': f02_advs_005_compound_log_speed_zscore_in_252d_d1}, 'f02_advs_006_compound_speed_excess_vs_baseline_252d_d1': {'inputs': ['close', 'low'], 'func': f02_advs_006_compound_speed_excess_vs_baseline_252d_d1}, 'f02_advs_007_log_close_to_rolling_252d_vwap_d1': {'inputs': ['close', 'volume', 'low'], 'func': f02_advs_007_log_close_to_rolling_252d_vwap_d1}, 'f02_advs_008_compound_speed_in_atr_units_from_252d_low_d1': {'inputs': ['close', 'low', 'high'], 'func': f02_advs_008_compound_speed_in_atr_units_from_252d_low_d1}, 'f02_advs_009_compound_speed_in_atr_units_from_63d_low_d1': {'inputs': ['close', 'low', 'high'], 'func': f02_advs_009_compound_speed_in_atr_units_from_63d_low_d1}, 'f02_advs_010_recovery_speed_from_252d_low_d1': {'inputs': ['close', 'high', 'low'], 'func': f02_advs_010_recovery_speed_from_252d_low_d1}, 'f02_advs_011_exponential_velocity_ema_21d_d1': {'inputs': ['close'], 'func': f02_advs_011_exponential_velocity_ema_21d_d1}, 'f02_advs_012_log_arc_height_above_min_low_252d_d1': {'inputs': ['close', 'low'], 'func': f02_advs_012_log_arc_height_above_min_low_252d_d1}, 'f02_advs_013_velocity_recent_minus_baseline_21d_in_252d_d1': {'inputs': ['close'], 'func': f02_advs_013_velocity_recent_minus_baseline_21d_in_252d_d1}, 'f02_advs_014_velocity_dispersion_iqr_252d_d1': {'inputs': ['close'], 'func': f02_advs_014_velocity_dispersion_iqr_252d_d1}, 'f02_advs_015_velocity_skew_252d_d1': {'inputs': ['close'], 'func': f02_advs_015_velocity_skew_252d_d1}, 'f02_advs_016_velocity_kurt_252d_d1': {'inputs': ['close'], 'func': f02_advs_016_velocity_kurt_252d_d1}, 'f02_advs_017_velocity_p95_minus_p50_252d_d1': {'inputs': ['close'], 'func': f02_advs_017_velocity_p95_minus_p50_252d_d1}, 'f02_advs_018_velocity_p50_minus_p5_252d_d1': {'inputs': ['close'], 'func': f02_advs_018_velocity_p50_minus_p5_252d_d1}, 'f02_advs_019_velocity_pct_rank_5d_in_252d_d1': {'inputs': ['close'], 'func': f02_advs_019_velocity_pct_rank_5d_in_252d_d1}, 'f02_advs_020_velocity_pct_rank_21d_in_252d_d1': {'inputs': ['close'], 'func': f02_advs_020_velocity_pct_rank_21d_in_252d_d1}, 'f02_advs_021_velocity_pct_rank_63d_in_252d_d1': {'inputs': ['close'], 'func': f02_advs_021_velocity_pct_rank_63d_in_252d_d1}, 'f02_advs_022_velocity_burst_above_2sd_count_252d_d1': {'inputs': ['close'], 'func': f02_advs_022_velocity_burst_above_2sd_count_252d_d1}, 'f02_advs_023_velocity_burst_below_2sd_count_252d_d1': {'inputs': ['close'], 'func': f02_advs_023_velocity_burst_below_2sd_count_252d_d1}, 'f02_advs_024_velocity_runs_above_zero_max_252d_d1': {'inputs': ['close'], 'func': f02_advs_024_velocity_runs_above_zero_max_252d_d1}, 'f02_advs_025_velocity_mad_252d_d1': {'inputs': ['close'], 'func': f02_advs_025_velocity_mad_252d_d1}, 'f02_advs_026_acceleration_max_252d_d1': {'inputs': ['close'], 'func': f02_advs_026_acceleration_max_252d_d1}, 'f02_advs_027_acceleration_min_252d_d1': {'inputs': ['close'], 'func': f02_advs_027_acceleration_min_252d_d1}, 'f02_advs_028_acceleration_range_252d_d1': {'inputs': ['close'], 'func': f02_advs_028_acceleration_range_252d_d1}, 'f02_advs_029_acceleration_sign_changes_count_63d_d1': {'inputs': ['close'], 'func': f02_advs_029_acceleration_sign_changes_count_63d_d1}, 'f02_advs_030_acceleration_positive_run_max_252d_d1': {'inputs': ['close'], 'func': f02_advs_030_acceleration_positive_run_max_252d_d1}, 'f02_advs_031_acceleration_negative_run_max_252d_d1': {'inputs': ['close'], 'func': f02_advs_031_acceleration_negative_run_max_252d_d1}, 'f02_advs_032_terminal_acceleration_21d_zscore_in_252d_d1': {'inputs': ['close'], 'func': f02_advs_032_terminal_acceleration_21d_zscore_in_252d_d1}, 'f02_advs_033_acceleration_dispersion_iqr_252d_d1': {'inputs': ['close'], 'func': f02_advs_033_acceleration_dispersion_iqr_252d_d1}, 'f02_advs_034_acceleration_skew_252d_d1': {'inputs': ['close'], 'func': f02_advs_034_acceleration_skew_252d_d1}, 'f02_advs_035_acceleration_kurt_252d_d1': {'inputs': ['close'], 'func': f02_advs_035_acceleration_kurt_252d_d1}, 'f02_advs_036_acceleration_pct_rank_recent_5d_in_252d_d1': {'inputs': ['close'], 'func': f02_advs_036_acceleration_pct_rank_recent_5d_in_252d_d1}, 'f02_advs_037_acceleration_above_p95_count_63d_d1': {'inputs': ['close'], 'func': f02_advs_037_acceleration_above_p95_count_63d_d1}, 'f02_advs_038_acceleration_autocorr_lag1_63d_d1': {'inputs': ['close'], 'func': f02_advs_038_acceleration_autocorr_lag1_63d_d1}, 'f02_advs_039_acceleration_autocorr_lag5_252d_d1': {'inputs': ['close'], 'func': f02_advs_039_acceleration_autocorr_lag5_252d_d1}, 'f02_advs_040_acceleration_velocity_corr_63d_d1': {'inputs': ['close'], 'func': f02_advs_040_acceleration_velocity_corr_63d_d1}, 'f02_advs_041_acceleration_vol_corr_63d_d1': {'inputs': ['close'], 'func': f02_advs_041_acceleration_vol_corr_63d_d1}, 'f02_advs_042_acceleration_zscore_p95_252d_d1': {'inputs': ['close'], 'func': f02_advs_042_acceleration_zscore_p95_252d_d1}, 'f02_advs_043_acceleration_dropoff_5d_vs_21d_d1': {'inputs': ['close'], 'func': f02_advs_043_acceleration_dropoff_5d_vs_21d_d1}, 'f02_advs_044_pre_peak_acceleration_buildup_63d_d1': {'inputs': ['close'], 'func': f02_advs_044_pre_peak_acceleration_buildup_63d_d1}, 'f02_advs_045_acceleration_terminal_thrust_5d_zscore_d1': {'inputs': ['close'], 'func': f02_advs_045_acceleration_terminal_thrust_5d_zscore_d1}, 'f02_advs_046_max_1d_log_return_252d_d1': {'inputs': ['close'], 'func': f02_advs_046_max_1d_log_return_252d_d1}, 'f02_advs_047_min_1d_log_return_252d_d1': {'inputs': ['close'], 'func': f02_advs_047_min_1d_log_return_252d_d1}, 'f02_advs_048_max_1d_log_return_zscore_252d_d1': {'inputs': ['close'], 'func': f02_advs_048_max_1d_log_return_zscore_252d_d1}, 'f02_advs_049_count_outsize_up_days_z_gt_3_252d_d1': {'inputs': ['close'], 'func': f02_advs_049_count_outsize_up_days_z_gt_3_252d_d1}, 'f02_advs_050_count_outsize_down_days_z_lt_neg3_252d_d1': {'inputs': ['close'], 'func': f02_advs_050_count_outsize_down_days_z_lt_neg3_252d_d1}, 'f02_advs_051_mean_top10_log_returns_252d_d1': {'inputs': ['close'], 'func': f02_advs_051_mean_top10_log_returns_252d_d1}, 'f02_advs_052_mean_bottom10_log_returns_252d_d1': {'inputs': ['close'], 'func': f02_advs_052_mean_bottom10_log_returns_252d_d1}, 'f02_advs_053_ratio_top10_to_bottom10_returns_252d_d1': {'inputs': ['close'], 'func': f02_advs_053_ratio_top10_to_bottom10_returns_252d_d1}, 'f02_advs_054_share_of_252d_log_gain_from_top10_days_d1': {'inputs': ['close'], 'func': f02_advs_054_share_of_252d_log_gain_from_top10_days_d1}, 'f02_advs_055_share_of_252d_log_gain_from_top5_days_d1': {'inputs': ['close'], 'func': f02_advs_055_share_of_252d_log_gain_from_top5_days_d1}, 'f02_advs_056_days_above_3pct_log_return_252d_d1': {'inputs': ['close'], 'func': f02_advs_056_days_above_3pct_log_return_252d_d1}, 'f02_advs_057_days_below_neg3pct_log_return_252d_d1': {'inputs': ['close'], 'func': f02_advs_057_days_below_neg3pct_log_return_252d_d1}, 'f02_advs_058_max_3d_log_return_252d_d1': {'inputs': ['close'], 'func': f02_advs_058_max_3d_log_return_252d_d1}, 'f02_advs_059_max_5d_log_return_252d_d1': {'inputs': ['close'], 'func': f02_advs_059_max_5d_log_return_252d_d1}, 'f02_advs_060_max_10d_log_return_252d_d1': {'inputs': ['close'], 'func': f02_advs_060_max_10d_log_return_252d_d1}, 'f02_advs_061_velocity_volume_corr_63d_d1': {'inputs': ['close', 'volume'], 'func': f02_advs_061_velocity_volume_corr_63d_d1}, 'f02_advs_062_velocity_volume_corr_252d_d1': {'inputs': ['close', 'volume'], 'func': f02_advs_062_velocity_volume_corr_252d_d1}, 'f02_advs_063_velocity_per_log_volume_21d_d1': {'inputs': ['close', 'volume'], 'func': f02_advs_063_velocity_per_log_volume_21d_d1}, 'f02_advs_064_velocity_per_log_volume_63d_d1': {'inputs': ['close', 'volume'], 'func': f02_advs_064_velocity_per_log_volume_63d_d1}, 'f02_advs_065_fractal_efficiency_21d_d1': {'inputs': ['close'], 'func': f02_advs_065_fractal_efficiency_21d_d1}, 'f02_advs_066_fractal_efficiency_63d_d1': {'inputs': ['close'], 'func': f02_advs_066_fractal_efficiency_63d_d1}, 'f02_advs_067_fractal_efficiency_252d_d1': {'inputs': ['close'], 'func': f02_advs_067_fractal_efficiency_252d_d1}, 'f02_advs_068_efficiency_ratio_21d_d1': {'inputs': ['close'], 'func': f02_advs_068_efficiency_ratio_21d_d1}, 'f02_advs_069_efficiency_ratio_63d_d1': {'inputs': ['close'], 'func': f02_advs_069_efficiency_ratio_63d_d1}, 'f02_advs_070_efficiency_ratio_change_21d_vs_63d_d1': {'inputs': ['close'], 'func': f02_advs_070_efficiency_ratio_change_21d_vs_63d_d1}, 'f02_advs_071_kaufman_efficiency_252d_d1': {'inputs': ['close'], 'func': f02_advs_071_kaufman_efficiency_252d_d1}, 'f02_advs_072_advance_path_smoothness_63d_d1': {'inputs': ['close'], 'func': f02_advs_072_advance_path_smoothness_63d_d1}, 'f02_advs_073_advance_path_smoothness_252d_d1': {'inputs': ['close'], 'func': f02_advs_073_advance_path_smoothness_252d_d1}, 'f02_advs_074_log_return_per_atr_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f02_advs_074_log_return_per_atr_252d_d1}, 'f02_advs_075_close_distance_per_atr_from_63d_low_d1': {'inputs': ['close', 'low', 'high'], 'func': f02_advs_075_close_distance_per_atr_from_63d_low_d1}}
