import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f03_crash_depth(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - peak) / peak.replace(0, np.nan).abs()


def _f03_crash_duration(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    in_dd = (close < peak).astype(float)
    grp = (in_dd.diff().fillna(0) != 0).cumsum()
    return in_dd.groupby(grp).cumsum() * in_dd


def _f03_crash_recovery(close, w):
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - trough) / trough.replace(0, np.nan).abs()


# 21d crash depth from rolling peak
def f03cdd_f03_crash_depth_duration_depth_21d_base_v001_signal(closeadj):
    result = _f03_crash_depth(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash depth from rolling peak
def f03cdd_f03_crash_depth_duration_depth_63d_base_v002_signal(closeadj):
    result = _f03_crash_depth(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d crash depth from rolling peak
def f03cdd_f03_crash_depth_duration_depth_126d_base_v003_signal(closeadj):
    result = _f03_crash_depth(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash depth from rolling peak
def f03cdd_f03_crash_depth_duration_depth_252d_base_v004_signal(closeadj):
    result = _f03_crash_depth(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash depth from rolling peak
def f03cdd_f03_crash_depth_duration_depth_504d_base_v005_signal(closeadj):
    result = _f03_crash_depth(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 63d crash depth over 21d
def f03cdd_f03_crash_depth_duration_depthmean_21d_base_v006_signal(closeadj):
    result = _mean(_f03_crash_depth(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 252d crash depth over 63d
def f03cdd_f03_crash_depth_duration_depthmean_63d_base_v007_signal(closeadj):
    result = _mean(_f03_crash_depth(closeadj, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 252d crash depth over 63d
def f03cdd_f03_crash_depth_duration_depthstd_63d_base_v008_signal(closeadj):
    result = _std(_f03_crash_depth(closeadj, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 504d crash depth over 126d
def f03cdd_f03_crash_depth_duration_depthstd_126d_base_v009_signal(closeadj):
    result = _std(_f03_crash_depth(closeadj, 504), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minimum (worst) crash depth over 252d window
def f03cdd_f03_crash_depth_duration_worstdepth_252d_base_v010_signal(closeadj):
    result = _f03_crash_depth(closeadj, 252).rolling(63, min_periods=21).min()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d minimum (worst) crash depth over 63d window
def f03cdd_f03_crash_depth_duration_worstdepth_63d_base_v011_signal(closeadj):
    result = _f03_crash_depth(closeadj, 63).rolling(21, min_periods=5).min()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d minimum (worst) crash depth over 504d
def f03cdd_f03_crash_depth_duration_worstdepth_504d_base_v012_signal(closeadj):
    result = _f03_crash_depth(closeadj, 504).rolling(126, min_periods=42).min()
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d crash depth over 252d
def f03cdd_f03_crash_depth_duration_depthz_252d_base_v013_signal(closeadj):
    result = _z(_f03_crash_depth(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d crash depth over 504d
def f03cdd_f03_crash_depth_duration_depthz_504d_base_v014_signal(closeadj):
    result = _z(_f03_crash_depth(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# crash depth at 21d weighted by closeadj level
def f03cdd_f03_crash_depth_duration_depthxprice_21d_base_v015_signal(closeadj):
    result = _f03_crash_depth(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# crash depth at 252d weighted by closeadj level
def f03cdd_f03_crash_depth_duration_depthxprice_252d_base_v016_signal(closeadj):
    result = _f03_crash_depth(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depth squared (severity emphasis)
def f03cdd_f03_crash_depth_duration_depthsq_21d_base_v017_signal(closeadj):
    d = _f03_crash_depth(closeadj, 21)
    result = d * d.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth squared
def f03cdd_f03_crash_depth_duration_depthsq_63d_base_v018_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63)
    result = d * d.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth squared
def f03cdd_f03_crash_depth_duration_depthsq_252d_base_v019_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    result = d * d.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling count of days with 63d crash depth below -5%
def f03cdd_f03_crash_depth_duration_depthcount5_252d_base_v020_signal(closeadj):
    flag = (_f03_crash_depth(closeadj, 63) < -0.05).astype(float)
    result = flag.rolling(252, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling count of days with 252d crash depth below -15%
def f03cdd_f03_crash_depth_duration_depthcount15_504d_base_v021_signal(closeadj):
    flag = (_f03_crash_depth(closeadj, 252) < -0.15).astype(float)
    result = flag.rolling(504, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling count of days with 252d crash depth below -30%
def f03cdd_f03_crash_depth_duration_depthcount30_504d_base_v022_signal(closeadj):
    flag = (_f03_crash_depth(closeadj, 252) < -0.30).astype(float)
    result = flag.rolling(504, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash depth scaled by 504d worst-ever depth magnitude
def f03cdd_f03_crash_depth_duration_depthrelhist_504d_base_v023_signal(closeadj):
    cur = _f03_crash_depth(closeadj, 252)
    worst = _f03_crash_depth(closeadj, 504).rolling(504, min_periods=126).min()
    result = cur / worst.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days with depth below -20%
def f03cdd_f03_crash_depth_duration_deepdaycount_63d_base_v024_signal(closeadj):
    flag = (_f03_crash_depth(closeadj, 252) < -0.20).astype(float)
    result = flag.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days with depth below -10%
def f03cdd_f03_crash_depth_duration_deepdaycount_252d_base_v025_signal(closeadj):
    flag = (_f03_crash_depth(closeadj, 252) < -0.10).astype(float)
    result = flag.rolling(252, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash duration scaled by 21d closeadj level
def f03cdd_f03_crash_depth_duration_durationxprice_21d_base_v026_signal(closeadj):
    result = _f03_crash_duration(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash duration
def f03cdd_f03_crash_depth_duration_duration_63d_base_v027_signal(closeadj):
    result = _f03_crash_duration(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d crash duration
def f03cdd_f03_crash_depth_duration_duration_126d_base_v028_signal(closeadj):
    result = _f03_crash_duration(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash duration
def f03cdd_f03_crash_depth_duration_duration_252d_base_v029_signal(closeadj):
    result = _f03_crash_duration(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash duration
def f03cdd_f03_crash_depth_duration_duration_504d_base_v030_signal(closeadj):
    result = _f03_crash_duration(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# fractional crash duration vs 252d window
def f03cdd_f03_crash_depth_duration_durationfrac_252d_base_v031_signal(closeadj):
    result = _f03_crash_duration(closeadj, 252) / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# fractional crash duration vs 63d window
def f03cdd_f03_crash_depth_duration_durationfrac_63d_base_v032_signal(closeadj):
    result = _f03_crash_duration(closeadj, 63) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# fractional crash duration vs 504d window
def f03cdd_f03_crash_depth_duration_durationfrac_504d_base_v033_signal(closeadj):
    result = _f03_crash_duration(closeadj, 504) / 504.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 63d duration over 63d
def f03cdd_f03_crash_depth_duration_durationmean_63d_base_v034_signal(closeadj):
    result = _mean(_f03_crash_duration(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 252d duration over 252d
def f03cdd_f03_crash_depth_duration_durationmean_252d_base_v035_signal(closeadj):
    result = _mean(_f03_crash_duration(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d duration over 252d
def f03cdd_f03_crash_depth_duration_durationz_252d_base_v036_signal(closeadj):
    result = _z(_f03_crash_duration(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d duration over 504d
def f03cdd_f03_crash_depth_duration_durationz_504d_base_v037_signal(closeadj):
    result = _z(_f03_crash_duration(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# duration weighted by current depth (severity-time)
def f03cdd_f03_crash_depth_duration_duranddepth_63d_base_v038_signal(closeadj):
    result = _f03_crash_duration(closeadj, 63) * _f03_crash_depth(closeadj, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# duration weighted by current depth at 252d
def f03cdd_f03_crash_depth_duration_duranddepth_252d_base_v039_signal(closeadj):
    result = _f03_crash_duration(closeadj, 252) * _f03_crash_depth(closeadj, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# duration weighted by current depth at 504d
def f03cdd_f03_crash_depth_duration_duranddepth_504d_base_v040_signal(closeadj):
    result = _f03_crash_duration(closeadj, 504) * _f03_crash_depth(closeadj, 504).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max duration in 63d window
def f03cdd_f03_crash_depth_duration_durationmax_63d_base_v041_signal(closeadj):
    result = _f03_crash_duration(closeadj, 63).rolling(21, min_periods=5).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max duration in 252d window
def f03cdd_f03_crash_depth_duration_durationmax_252d_base_v042_signal(closeadj):
    result = _f03_crash_duration(closeadj, 252).rolling(63, min_periods=21).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max duration in 504d window
def f03cdd_f03_crash_depth_duration_durationmax_504d_base_v043_signal(closeadj):
    result = _f03_crash_duration(closeadj, 504).rolling(126, min_periods=42).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash duration weighted by absolute depth (deep-drawdown time)
def f03cdd_f03_crash_depth_duration_deepdurwgt_63d_base_v044_signal(closeadj):
    dur = _f03_crash_duration(closeadj, 63)
    depth = _f03_crash_depth(closeadj, 63).abs()
    result = dur * depth
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration weighted by depth-magnitude squared
def f03cdd_f03_crash_depth_duration_deepdurwgt_252d_base_v045_signal(closeadj):
    dur = _f03_crash_duration(closeadj, 252)
    depth = _f03_crash_depth(closeadj, 252).abs()
    result = dur * depth * depth
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration weighted by depth-magnitude squared
def f03cdd_f03_crash_depth_duration_deepdurwgt_504d_base_v046_signal(closeadj):
    dur = _f03_crash_duration(closeadj, 504)
    depth = _f03_crash_depth(closeadj, 504).abs()
    result = dur * depth * depth
    return result.replace([np.inf, -np.inf], np.nan)


# 5d crash depth (intraweek)
def f03cdd_f03_crash_depth_duration_depth_5d_base_v047_signal(closeadj):
    result = _f03_crash_depth(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d crash depth
def f03cdd_f03_crash_depth_duration_depth_10d_base_v048_signal(closeadj):
    result = _f03_crash_depth(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d crash depth (2mo)
def f03cdd_f03_crash_depth_duration_depth_42d_base_v049_signal(closeadj):
    result = _f03_crash_depth(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d crash depth (~9mo)
def f03cdd_f03_crash_depth_duration_depth_189d_base_v050_signal(closeadj):
    result = _f03_crash_depth(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d crash depth (~1.5y)
def f03cdd_f03_crash_depth_duration_depth_378d_base_v051_signal(closeadj):
    result = _f03_crash_depth(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d crash duration weighted by 5d depth magnitude
def f03cdd_f03_crash_depth_duration_durationxdepth_5d_base_v052_signal(closeadj):
    result = _f03_crash_duration(closeadj, 5) * _f03_crash_depth(closeadj, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d crash duration weighted by 10d depth magnitude
def f03cdd_f03_crash_depth_duration_durationxdepth_10d_base_v053_signal(closeadj):
    result = _f03_crash_duration(closeadj, 10) * _f03_crash_depth(closeadj, 10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d crash duration weighted by 42d depth magnitude
def f03cdd_f03_crash_depth_duration_durationxdepth_42d_base_v054_signal(closeadj):
    result = _f03_crash_duration(closeadj, 42) * _f03_crash_depth(closeadj, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d crash duration
def f03cdd_f03_crash_depth_duration_duration_189d_base_v055_signal(closeadj):
    result = _f03_crash_duration(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d crash duration
def f03cdd_f03_crash_depth_duration_duration_378d_base_v056_signal(closeadj):
    result = _f03_crash_duration(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# average depth-area across 63d window
def f03cdd_f03_crash_depth_duration_deptharea_63d_base_v057_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    result = d.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# average depth-area across 252d window
def f03cdd_f03_crash_depth_duration_deptharea_252d_base_v058_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    result = d.rolling(252, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# average depth-area across 504d window
def f03cdd_f03_crash_depth_duration_deptharea_504d_base_v059_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504).abs()
    result = d.rolling(504, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth times duration ratio
def f03cdd_f03_crash_depth_duration_depthperday_63d_base_v060_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63).abs()
    t = _f03_crash_duration(closeadj, 63).replace(0, np.nan)
    result = d / t
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth times duration ratio
def f03cdd_f03_crash_depth_duration_depthperday_252d_base_v061_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    t = _f03_crash_duration(closeadj, 252).replace(0, np.nan)
    result = d / t
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depth times duration ratio
def f03cdd_f03_crash_depth_duration_depthperday_504d_base_v062_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504).abs()
    t = _f03_crash_duration(closeadj, 504).replace(0, np.nan)
    result = d / t
    return result.replace([np.inf, -np.inf], np.nan)


# rolling crash recovery from 63d trough
def f03cdd_f03_crash_depth_duration_recovery_63d_base_v063_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling crash recovery from 252d trough
def f03cdd_f03_crash_depth_duration_recovery_252d_base_v064_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling crash recovery from 504d trough
def f03cdd_f03_crash_depth_duration_recovery_504d_base_v065_signal(closeadj):
    result = _f03_crash_recovery(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# net depth-recovery gap at 252d (depth + recovery)
def f03cdd_f03_crash_depth_duration_depthplusrec_252d_base_v066_signal(closeadj):
    result = _f03_crash_depth(closeadj, 252) + _f03_crash_recovery(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net depth-recovery gap at 504d
def f03cdd_f03_crash_depth_duration_depthplusrec_504d_base_v067_signal(closeadj):
    result = _f03_crash_depth(closeadj, 504) + _f03_crash_recovery(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depth times volume (capitulation pressure)
def f03cdd_f03_crash_depth_duration_depthxvol_21d_base_v068_signal(closeadj, volume):
    result = _f03_crash_depth(closeadj, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depth times volume
def f03cdd_f03_crash_depth_duration_depthxvol_63d_base_v069_signal(closeadj, volume):
    result = _f03_crash_depth(closeadj, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth times dollar volume
def f03cdd_f03_crash_depth_duration_depthxdv_252d_base_v070_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f03_crash_depth(closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration times volume z (panic-time)
def f03cdd_f03_crash_depth_duration_durxvolz_21d_base_v071_signal(closeadj, volume):
    result = _f03_crash_duration(closeadj, 21) * _z(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration times volume z
def f03cdd_f03_crash_depth_duration_durxvolz_63d_base_v072_signal(closeadj, volume):
    result = _f03_crash_duration(closeadj, 63) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash depth scaled by 63d count of new troughs
def f03cdd_f03_crash_depth_duration_depthxnewtrough_63d_base_v073_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    new_low = (d <= d.rolling(252, min_periods=63).min()).astype(float)
    cnt = new_low.rolling(63, min_periods=21).sum()
    result = d * (cnt + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash depth scaled by 252d count of new troughs
def f03cdd_f03_crash_depth_duration_depthxnewtrough_252d_base_v074_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504)
    new_low = (d <= d.rolling(504, min_periods=126).min()).astype(float)
    cnt = new_low.rolling(252, min_periods=63).sum()
    result = d * (cnt + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depth divided by ATR-style range proxy
def f03cdd_f03_crash_depth_duration_depthnormrange_252d_base_v075_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f03_crash_depth(closeadj, 252) * closeadj / rng.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03cdd_f03_crash_depth_duration_depth_21d_base_v001_signal,
    f03cdd_f03_crash_depth_duration_depth_63d_base_v002_signal,
    f03cdd_f03_crash_depth_duration_depth_126d_base_v003_signal,
    f03cdd_f03_crash_depth_duration_depth_252d_base_v004_signal,
    f03cdd_f03_crash_depth_duration_depth_504d_base_v005_signal,
    f03cdd_f03_crash_depth_duration_depthmean_21d_base_v006_signal,
    f03cdd_f03_crash_depth_duration_depthmean_63d_base_v007_signal,
    f03cdd_f03_crash_depth_duration_depthstd_63d_base_v008_signal,
    f03cdd_f03_crash_depth_duration_depthstd_126d_base_v009_signal,
    f03cdd_f03_crash_depth_duration_worstdepth_252d_base_v010_signal,
    f03cdd_f03_crash_depth_duration_worstdepth_63d_base_v011_signal,
    f03cdd_f03_crash_depth_duration_worstdepth_504d_base_v012_signal,
    f03cdd_f03_crash_depth_duration_depthz_252d_base_v013_signal,
    f03cdd_f03_crash_depth_duration_depthz_504d_base_v014_signal,
    f03cdd_f03_crash_depth_duration_depthxprice_21d_base_v015_signal,
    f03cdd_f03_crash_depth_duration_depthxprice_252d_base_v016_signal,
    f03cdd_f03_crash_depth_duration_depthsq_21d_base_v017_signal,
    f03cdd_f03_crash_depth_duration_depthsq_63d_base_v018_signal,
    f03cdd_f03_crash_depth_duration_depthsq_252d_base_v019_signal,
    f03cdd_f03_crash_depth_duration_depthcount5_252d_base_v020_signal,
    f03cdd_f03_crash_depth_duration_depthcount15_504d_base_v021_signal,
    f03cdd_f03_crash_depth_duration_depthcount30_504d_base_v022_signal,
    f03cdd_f03_crash_depth_duration_depthrelhist_504d_base_v023_signal,
    f03cdd_f03_crash_depth_duration_deepdaycount_63d_base_v024_signal,
    f03cdd_f03_crash_depth_duration_deepdaycount_252d_base_v025_signal,
    f03cdd_f03_crash_depth_duration_durationxprice_21d_base_v026_signal,
    f03cdd_f03_crash_depth_duration_duration_63d_base_v027_signal,
    f03cdd_f03_crash_depth_duration_duration_126d_base_v028_signal,
    f03cdd_f03_crash_depth_duration_duration_252d_base_v029_signal,
    f03cdd_f03_crash_depth_duration_duration_504d_base_v030_signal,
    f03cdd_f03_crash_depth_duration_durationfrac_252d_base_v031_signal,
    f03cdd_f03_crash_depth_duration_durationfrac_63d_base_v032_signal,
    f03cdd_f03_crash_depth_duration_durationfrac_504d_base_v033_signal,
    f03cdd_f03_crash_depth_duration_durationmean_63d_base_v034_signal,
    f03cdd_f03_crash_depth_duration_durationmean_252d_base_v035_signal,
    f03cdd_f03_crash_depth_duration_durationz_252d_base_v036_signal,
    f03cdd_f03_crash_depth_duration_durationz_504d_base_v037_signal,
    f03cdd_f03_crash_depth_duration_duranddepth_63d_base_v038_signal,
    f03cdd_f03_crash_depth_duration_duranddepth_252d_base_v039_signal,
    f03cdd_f03_crash_depth_duration_duranddepth_504d_base_v040_signal,
    f03cdd_f03_crash_depth_duration_durationmax_63d_base_v041_signal,
    f03cdd_f03_crash_depth_duration_durationmax_252d_base_v042_signal,
    f03cdd_f03_crash_depth_duration_durationmax_504d_base_v043_signal,
    f03cdd_f03_crash_depth_duration_deepdurwgt_63d_base_v044_signal,
    f03cdd_f03_crash_depth_duration_deepdurwgt_252d_base_v045_signal,
    f03cdd_f03_crash_depth_duration_deepdurwgt_504d_base_v046_signal,
    f03cdd_f03_crash_depth_duration_depth_5d_base_v047_signal,
    f03cdd_f03_crash_depth_duration_depth_10d_base_v048_signal,
    f03cdd_f03_crash_depth_duration_depth_42d_base_v049_signal,
    f03cdd_f03_crash_depth_duration_depth_189d_base_v050_signal,
    f03cdd_f03_crash_depth_duration_depth_378d_base_v051_signal,
    f03cdd_f03_crash_depth_duration_durationxdepth_5d_base_v052_signal,
    f03cdd_f03_crash_depth_duration_durationxdepth_10d_base_v053_signal,
    f03cdd_f03_crash_depth_duration_durationxdepth_42d_base_v054_signal,
    f03cdd_f03_crash_depth_duration_duration_189d_base_v055_signal,
    f03cdd_f03_crash_depth_duration_duration_378d_base_v056_signal,
    f03cdd_f03_crash_depth_duration_deptharea_63d_base_v057_signal,
    f03cdd_f03_crash_depth_duration_deptharea_252d_base_v058_signal,
    f03cdd_f03_crash_depth_duration_deptharea_504d_base_v059_signal,
    f03cdd_f03_crash_depth_duration_depthperday_63d_base_v060_signal,
    f03cdd_f03_crash_depth_duration_depthperday_252d_base_v061_signal,
    f03cdd_f03_crash_depth_duration_depthperday_504d_base_v062_signal,
    f03cdd_f03_crash_depth_duration_recovery_63d_base_v063_signal,
    f03cdd_f03_crash_depth_duration_recovery_252d_base_v064_signal,
    f03cdd_f03_crash_depth_duration_recovery_504d_base_v065_signal,
    f03cdd_f03_crash_depth_duration_depthplusrec_252d_base_v066_signal,
    f03cdd_f03_crash_depth_duration_depthplusrec_504d_base_v067_signal,
    f03cdd_f03_crash_depth_duration_depthxvol_21d_base_v068_signal,
    f03cdd_f03_crash_depth_duration_depthxvol_63d_base_v069_signal,
    f03cdd_f03_crash_depth_duration_depthxdv_252d_base_v070_signal,
    f03cdd_f03_crash_depth_duration_durxvolz_21d_base_v071_signal,
    f03cdd_f03_crash_depth_duration_durxvolz_63d_base_v072_signal,
    f03cdd_f03_crash_depth_duration_depthxnewtrough_63d_base_v073_signal,
    f03cdd_f03_crash_depth_duration_depthxnewtrough_252d_base_v074_signal,
    f03cdd_f03_crash_depth_duration_depthnormrange_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_CRASH_DEPTH_DURATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f03_crash_depth", "_f03_crash_duration", "_f03_crash_recovery")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f03_crash_depth_duration_base_001_075_claude: {n_features} features pass")
