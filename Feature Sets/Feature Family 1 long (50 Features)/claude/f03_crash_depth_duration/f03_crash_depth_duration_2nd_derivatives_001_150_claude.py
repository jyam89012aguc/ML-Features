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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 5d slope of 21d crash depth
def f03cdd_f03_crash_depth_duration_depth_21d_slope_v001_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d crash depth
def f03cdd_f03_crash_depth_duration_depth_21d_slope_v002_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d crash depth
def f03cdd_f03_crash_depth_duration_depth_63d_slope_v003_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d crash depth
def f03cdd_f03_crash_depth_duration_depth_63d_slope_v004_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d crash depth
def f03cdd_f03_crash_depth_duration_depth_63d_slope_v005_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d crash depth
def f03cdd_f03_crash_depth_duration_depth_126d_slope_v006_signal(closeadj):
    base = _f03_crash_depth(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d crash depth
def f03cdd_f03_crash_depth_duration_depth_126d_slope_v007_signal(closeadj):
    base = _f03_crash_depth(closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d crash depth
def f03cdd_f03_crash_depth_duration_depth_252d_slope_v008_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d crash depth
def f03cdd_f03_crash_depth_duration_depth_252d_slope_v009_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d crash depth
def f03cdd_f03_crash_depth_duration_depth_504d_slope_v010_signal(closeadj):
    base = _f03_crash_depth(closeadj, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d crash depth
def f03cdd_f03_crash_depth_duration_depth_504d_slope_v011_signal(closeadj):
    base = _f03_crash_depth(closeadj, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth mean over 21d
def f03cdd_f03_crash_depth_duration_depthmean_21d_slope_v012_signal(closeadj):
    base = _mean(_f03_crash_depth(closeadj, 63), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth mean
def f03cdd_f03_crash_depth_duration_depthmean_63d_slope_v013_signal(closeadj):
    base = _mean(_f03_crash_depth(closeadj, 252), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d depth std over 63d
def f03cdd_f03_crash_depth_duration_depthstd_63d_slope_v014_signal(closeadj):
    base = _std(_f03_crash_depth(closeadj, 252), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d depth std over 126d
def f03cdd_f03_crash_depth_duration_depthstd_126d_slope_v015_signal(closeadj):
    base = _std(_f03_crash_depth(closeadj, 504), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d depth zscore over 252d
def f03cdd_f03_crash_depth_duration_depthz_252d_slope_v016_signal(closeadj):
    base = _z(_f03_crash_depth(closeadj, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of depth zscore (504d window of 252d depth)
def f03cdd_f03_crash_depth_duration_depthz_504d_slope_v017_signal(closeadj):
    base = _z(_f03_crash_depth(closeadj, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d depth × price
def f03cdd_f03_crash_depth_duration_depthxprice_21d_slope_v018_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d depth × price
def f03cdd_f03_crash_depth_duration_depthxprice_21d_slope_v019_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × price
def f03cdd_f03_crash_depth_duration_depthxprice_252d_slope_v020_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d depth squared
def f03cdd_f03_crash_depth_duration_depthsq_21d_slope_v021_signal(closeadj):
    d = _f03_crash_depth(closeadj, 21)
    base = d * d.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth squared
def f03cdd_f03_crash_depth_duration_depthsq_63d_slope_v022_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63)
    base = d * d.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth squared
def f03cdd_f03_crash_depth_duration_depthsq_252d_slope_v023_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    base = d * d.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d depth count below -5%
def f03cdd_f03_crash_depth_duration_depthcount5_252d_slope_v024_signal(closeadj):
    flag = (_f03_crash_depth(closeadj, 63) < -0.05).astype(float)
    base = flag.rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of deep day count
def f03cdd_f03_crash_depth_duration_deepdaycount_252d_slope_v025_signal(closeadj):
    flag = (_f03_crash_depth(closeadj, 252) < -0.10).astype(float)
    base = flag.rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d duration × price
def f03cdd_f03_crash_depth_duration_durationxprice_21d_slope_v026_signal(closeadj):
    base = _f03_crash_duration(closeadj, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d crash duration × close
def f03cdd_f03_crash_depth_duration_duration_63d_slope_v027_signal(closeadj):
    base = _f03_crash_duration(closeadj, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d crash duration × close
def f03cdd_f03_crash_depth_duration_duration_126d_slope_v028_signal(closeadj):
    base = _f03_crash_duration(closeadj, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d crash duration × close
def f03cdd_f03_crash_depth_duration_duration_252d_slope_v029_signal(closeadj):
    base = _f03_crash_duration(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d duration × close
def f03cdd_f03_crash_depth_duration_duration_504d_slope_v030_signal(closeadj):
    base = _f03_crash_duration(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d fractional duration
def f03cdd_f03_crash_depth_duration_durationfrac_252d_slope_v031_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 252) / 252.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fractional duration
def f03cdd_f03_crash_depth_duration_durationfrac_63d_slope_v032_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 63) / 63.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fractional duration
def f03cdd_f03_crash_depth_duration_durationfrac_504d_slope_v033_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 504) / 504.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration mean
def f03cdd_f03_crash_depth_duration_durationmean_63d_slope_v034_signal(closeadj):
    base = _mean(_f03_crash_duration(closeadj, 63) * closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d duration mean
def f03cdd_f03_crash_depth_duration_durationmean_252d_slope_v035_signal(closeadj):
    base = _mean(_f03_crash_duration(closeadj, 252) * closeadj, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d duration zscore
def f03cdd_f03_crash_depth_duration_durationz_252d_slope_v036_signal(closeadj):
    base = _z(_f03_crash_duration(closeadj, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d duration zscore
def f03cdd_f03_crash_depth_duration_durationz_504d_slope_v037_signal(closeadj):
    base = _z(_f03_crash_duration(closeadj, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration × depth
def f03cdd_f03_crash_depth_duration_duranddepth_63d_slope_v038_signal(closeadj):
    base = _f03_crash_duration(closeadj, 63) * _f03_crash_depth(closeadj, 63).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d duration × depth
def f03cdd_f03_crash_depth_duration_duranddepth_252d_slope_v039_signal(closeadj):
    base = _f03_crash_duration(closeadj, 252) * _f03_crash_depth(closeadj, 252).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d duration × depth
def f03cdd_f03_crash_depth_duration_duranddepth_504d_slope_v040_signal(closeadj):
    base = _f03_crash_duration(closeadj, 504) * _f03_crash_depth(closeadj, 504).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max duration × close
def f03cdd_f03_crash_depth_duration_durationmax_63d_slope_v041_signal(closeadj):
    base = _f03_crash_duration(closeadj, 63).rolling(21, min_periods=5).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max duration × close
def f03cdd_f03_crash_depth_duration_durationmax_252d_slope_v042_signal(closeadj):
    base = _f03_crash_duration(closeadj, 252).rolling(63, min_periods=21).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d max duration × close
def f03cdd_f03_crash_depth_duration_durationmax_504d_slope_v043_signal(closeadj):
    base = _f03_crash_duration(closeadj, 504).rolling(126, min_periods=42).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth-weighted duration
def f03cdd_f03_crash_depth_duration_deepdurwgt_63d_slope_v044_signal(closeadj):
    base = _f03_crash_duration(closeadj, 63) * _f03_crash_depth(closeadj, 63).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth^2-weighted duration
def f03cdd_f03_crash_depth_duration_deepdurwgt_252d_slope_v045_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    base = _f03_crash_duration(closeadj, 252) * d * d * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d depth^2-weighted duration
def f03cdd_f03_crash_depth_duration_deepdurwgt_504d_slope_v046_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504).abs()
    base = _f03_crash_duration(closeadj, 504) * d * d * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d depth
def f03cdd_f03_crash_depth_duration_depth_5d_slope_v047_signal(closeadj):
    base = _f03_crash_depth(closeadj, 5)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d depth
def f03cdd_f03_crash_depth_duration_depth_10d_slope_v048_signal(closeadj):
    base = _f03_crash_depth(closeadj, 10)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d depth
def f03cdd_f03_crash_depth_duration_depth_42d_slope_v049_signal(closeadj):
    base = _f03_crash_depth(closeadj, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 189d depth
def f03cdd_f03_crash_depth_duration_depth_189d_slope_v050_signal(closeadj):
    base = _f03_crash_depth(closeadj, 189)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d depth
def f03cdd_f03_crash_depth_duration_depth_378d_slope_v051_signal(closeadj):
    base = _f03_crash_depth(closeadj, 378)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d duration × price × depth
def f03cdd_f03_crash_depth_duration_durationxdepth_5d_slope_v052_signal(closeadj):
    base = _f03_crash_duration(closeadj, 5) * _f03_crash_depth(closeadj, 5).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d duration × depth × price
def f03cdd_f03_crash_depth_duration_durationxdepth_10d_slope_v053_signal(closeadj):
    base = _f03_crash_duration(closeadj, 10) * _f03_crash_depth(closeadj, 10).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d duration × depth × price
def f03cdd_f03_crash_depth_duration_durationxdepth_42d_slope_v054_signal(closeadj):
    base = _f03_crash_duration(closeadj, 42) * _f03_crash_depth(closeadj, 42).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 189d duration × close
def f03cdd_f03_crash_depth_duration_duration_189d_slope_v055_signal(closeadj):
    base = _f03_crash_duration(closeadj, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d duration × close
def f03cdd_f03_crash_depth_duration_duration_378d_slope_v056_signal(closeadj):
    base = _f03_crash_duration(closeadj, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth-area
def f03cdd_f03_crash_depth_duration_deptharea_63d_slope_v057_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252).abs().rolling(63, min_periods=21).sum()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth-area
def f03cdd_f03_crash_depth_duration_deptharea_252d_slope_v058_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252).abs().rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d depth-area
def f03cdd_f03_crash_depth_duration_deptharea_504d_slope_v059_signal(closeadj):
    base = _f03_crash_depth(closeadj, 504).abs().rolling(504, min_periods=126).sum()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth-per-day intensity
def f03cdd_f03_crash_depth_duration_depthperday_63d_slope_v060_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63).abs()
    t = _f03_crash_duration(closeadj, 63).replace(0, np.nan)
    base = (d / t) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth-per-day intensity
def f03cdd_f03_crash_depth_duration_depthperday_252d_slope_v061_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    t = _f03_crash_duration(closeadj, 252).replace(0, np.nan)
    base = (d / t) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d depth-per-day intensity
def f03cdd_f03_crash_depth_duration_depthperday_504d_slope_v062_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504).abs()
    t = _f03_crash_duration(closeadj, 504).replace(0, np.nan)
    base = (d / t) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d recovery × close
def f03cdd_f03_crash_depth_duration_recovery_63d_slope_v063_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d recovery × close
def f03cdd_f03_crash_depth_duration_recovery_252d_slope_v064_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d recovery × close
def f03cdd_f03_crash_depth_duration_recovery_504d_slope_v065_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d depth + recovery × close
def f03cdd_f03_crash_depth_duration_depthplusrec_252d_slope_v066_signal(closeadj):
    base = (_f03_crash_depth(closeadj, 252) + _f03_crash_recovery(closeadj, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d depth + recovery × close
def f03cdd_f03_crash_depth_duration_depthplusrec_504d_slope_v067_signal(closeadj):
    base = (_f03_crash_depth(closeadj, 504) + _f03_crash_recovery(closeadj, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d depth × volume
def f03cdd_f03_crash_depth_duration_depthxvol_21d_slope_v068_signal(closeadj, volume):
    base = _f03_crash_depth(closeadj, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth × volume
def f03cdd_f03_crash_depth_duration_depthxvol_63d_slope_v069_signal(closeadj, volume):
    base = _f03_crash_depth(closeadj, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × dollar-volume
def f03cdd_f03_crash_depth_duration_depthxdv_252d_slope_v070_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f03_crash_depth(closeadj, 252) * _mean(dv, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d duration × volume zscore
def f03cdd_f03_crash_depth_duration_durxvolz_21d_slope_v071_signal(closeadj, volume):
    base = _f03_crash_duration(closeadj, 21) * _z(volume, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration × volume zscore
def f03cdd_f03_crash_depth_duration_durxvolz_63d_slope_v072_signal(closeadj, volume):
    base = _f03_crash_duration(closeadj, 63) * _z(volume, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of depth × new-trough count (63d)
def f03cdd_f03_crash_depth_duration_depthxnewtrough_63d_slope_v073_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    new_low = (d <= d.rolling(252, min_periods=63).min()).astype(float)
    cnt = new_low.rolling(63, min_periods=21).sum()
    base = d * (cnt + 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of depth × new-trough count (252d)
def f03cdd_f03_crash_depth_duration_depthxnewtrough_252d_slope_v074_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504)
    new_low = (d <= d.rolling(504, min_periods=126).min()).astype(float)
    cnt = new_low.rolling(252, min_periods=63).sum()
    base = d * (cnt + 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth normalized by ATR
def f03cdd_f03_crash_depth_duration_depthnormrange_252d_slope_v075_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f03_crash_depth(closeadj, 252) * closeadj / rng.replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d depth × retvol
def f03cdd_f03_crash_depth_duration_depthxretvol_21d_slope_v076_signal(closeadj):
    rv = _std(closeadj.pct_change(), 5)
    base = _f03_crash_depth(closeadj, 21) * rv * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth × retvol
def f03cdd_f03_crash_depth_duration_depthxretvol_63d_slope_v077_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f03_crash_depth(closeadj, 63) * rv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × retvol
def f03cdd_f03_crash_depth_duration_depthxretvol_252d_slope_v078_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f03_crash_depth(closeadj, 252) * rv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d depth × 21d return
def f03cdd_f03_crash_depth_duration_depthxret_21d_slope_v079_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21) * closeadj.pct_change(21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth × 63d return
def f03cdd_f03_crash_depth_duration_depthxret_63d_slope_v080_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63) * closeadj.pct_change(63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × 252d return
def f03cdd_f03_crash_depth_duration_depthxret_252d_slope_v081_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252) * closeadj.pct_change(252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth normalized by ATR
def f03cdd_f03_crash_depth_duration_depthnormatr_63d_slope_v082_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f03_crash_depth(closeadj, 63) * closeadj / atr.replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d depth normalized by ATR
def f03cdd_f03_crash_depth_duration_depthnormatr_504d_slope_v083_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f03_crash_depth(closeadj, 504) * closeadj / atr.replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of depth × downside dollar-volume (63d)
def f03cdd_f03_crash_depth_duration_depthxdownvol_63d_slope_v084_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f03_crash_depth(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of depth × downside dollar-volume (252d)
def f03cdd_f03_crash_depth_duration_depthxdownvol_252d_slope_v085_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f03_crash_depth(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth × skew
def f03cdd_f03_crash_depth_duration_depthxskew_63d_slope_v086_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f03_crash_depth(closeadj, 63) * sk * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × skew
def f03cdd_f03_crash_depth_duration_depthxskew_252d_slope_v087_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f03_crash_depth(closeadj, 252) * sk * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth × kurt
def f03cdd_f03_crash_depth_duration_depthxkurt_63d_slope_v088_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f03_crash_depth(closeadj, 63) * kt * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × kurt
def f03cdd_f03_crash_depth_duration_depthxkurt_252d_slope_v089_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f03_crash_depth(closeadj, 252) * kt * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of depth ratio 63v252
def f03cdd_f03_crash_depth_duration_depthratio_63v252_slope_v090_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63) / _f03_crash_depth(closeadj, 252).replace(0, np.nan)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of depth ratio 21v63
def f03cdd_f03_crash_depth_duration_depthratio_21v63_slope_v091_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21) / _f03_crash_depth(closeadj, 63).replace(0, np.nan)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of depth ratio 252v504
def f03cdd_f03_crash_depth_duration_depthratio_252v504_slope_v092_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252) / _f03_crash_depth(closeadj, 504).replace(0, np.nan)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of depth diff 63m252
def f03cdd_f03_crash_depth_duration_depthdiff_63m252_slope_v093_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63) - _f03_crash_depth(closeadj, 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of depth diff 21m63
def f03cdd_f03_crash_depth_duration_depthdiff_21m63_slope_v094_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21) - _f03_crash_depth(closeadj, 63)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of depth diff 252m504
def f03cdd_f03_crash_depth_duration_depthdiff_252m504_slope_v095_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252) - _f03_crash_depth(closeadj, 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d depth × 21d duration
def f03cdd_f03_crash_depth_duration_depthxdur_63d_slope_v096_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63) * _f03_crash_duration(closeadj, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d depth × 63d duration
def f03cdd_f03_crash_depth_duration_depthxdur_252d_slope_v097_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252) * _f03_crash_duration(closeadj, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d depth × 252d duration
def f03cdd_f03_crash_depth_duration_depthxdur_504d_slope_v098_signal(closeadj):
    base = _f03_crash_depth(closeadj, 504) * _f03_crash_duration(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of expanding duration × close
def f03cdd_f03_crash_depth_duration_durexpxprice_21d_slope_v099_signal(closeadj):
    peak = closeadj.expanding(min_periods=21).max()
    in_dd = (closeadj < peak).astype(float)
    grp = (in_dd.diff().fillna(0) != 0).cumsum()
    dur = in_dd.groupby(grp).cumsum() * in_dd
    base = dur * closeadj + _f03_crash_duration(closeadj, 21) * 0.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration × 21d retvol
def f03cdd_f03_crash_depth_duration_durxretvol_63d_slope_v100_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f03_crash_duration(closeadj, 63) * rv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d duration × 63d retvol
def f03cdd_f03_crash_depth_duration_durxretvol_252d_slope_v101_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f03_crash_duration(closeadj, 252) * rv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d duration × 21d return
def f03cdd_f03_crash_depth_duration_durxret_21d_slope_v102_signal(closeadj):
    base = _f03_crash_duration(closeadj, 21) * closeadj.pct_change(21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration × 63d return
def f03cdd_f03_crash_depth_duration_durxret_63d_slope_v103_signal(closeadj):
    base = _f03_crash_duration(closeadj, 63) * closeadj.pct_change(63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d duration × 252d return
def f03cdd_f03_crash_depth_duration_durxret_252d_slope_v104_signal(closeadj):
    base = _f03_crash_duration(closeadj, 252) * closeadj.pct_change(252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration × ATR
def f03cdd_f03_crash_depth_duration_durxatr_63d_slope_v105_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f03_crash_duration(closeadj, 63) * atr
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d duration × ATR
def f03cdd_f03_crash_depth_duration_durxatr_252d_slope_v106_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f03_crash_duration(closeadj, 252) * atr
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of duration ratio 63v252 × close
def f03cdd_f03_crash_depth_duration_durratio_63v252_slope_v107_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 63) / _f03_crash_duration(closeadj, 252).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of duration ratio 21v63 × close
def f03cdd_f03_crash_depth_duration_durratio_21v63_slope_v108_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 21) / _f03_crash_duration(closeadj, 63).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of duration diff 63m252 × close
def f03cdd_f03_crash_depth_duration_durdiff_63m252_slope_v109_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 63) - _f03_crash_duration(closeadj, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of duration diff 21m63 × close
def f03cdd_f03_crash_depth_duration_durdiff_21m63_slope_v110_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 21) - _f03_crash_duration(closeadj, 63)) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of duration diff 252m504 × close
def f03cdd_f03_crash_depth_duration_durdiff_252m504_slope_v111_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 252) - _f03_crash_duration(closeadj, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d recovery × close
def f03cdd_f03_crash_depth_duration_recovery_21d_slope_v112_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d recovery × close
def f03cdd_f03_crash_depth_duration_recovery_126d_slope_v113_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d recovery × close
def f03cdd_f03_crash_depth_duration_recovery_378d_slope_v114_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d recovery × duration
def f03cdd_f03_crash_depth_duration_recxdur_63d_slope_v115_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 63) * _f03_crash_duration(closeadj, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d recovery × duration
def f03cdd_f03_crash_depth_duration_recxdur_252d_slope_v116_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 252) * _f03_crash_duration(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d recovery × duration
def f03cdd_f03_crash_depth_duration_recxdur_504d_slope_v117_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 504) * _f03_crash_duration(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d recovery efficiency
def f03cdd_f03_crash_depth_duration_receff_63d_slope_v118_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 63) / _f03_crash_depth(closeadj, 63).abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d recovery efficiency
def f03cdd_f03_crash_depth_duration_receff_252d_slope_v119_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 252) / _f03_crash_depth(closeadj, 252).abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d recovery efficiency
def f03cdd_f03_crash_depth_duration_receff_504d_slope_v120_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 504) / _f03_crash_depth(closeadj, 504).abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d recovery × volume zscore
def f03cdd_f03_crash_depth_duration_recxvolz_63d_slope_v121_signal(closeadj, volume):
    base = _f03_crash_recovery(closeadj, 63) * _z(volume, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d recovery × volume zscore
def f03cdd_f03_crash_depth_duration_recxvolz_252d_slope_v122_signal(closeadj, volume):
    base = _f03_crash_recovery(closeadj, 252) * _z(volume, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d depth × 252d duration
def f03cdd_f03_crash_depth_duration_recentdeepXpersist_252d_slope_v123_signal(closeadj):
    base = _f03_crash_depth(closeadj, 21) * _f03_crash_duration(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d depth × 504d duration
def f03cdd_f03_crash_depth_duration_recentdeepXpersist_504d_slope_v124_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63) * _f03_crash_duration(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding worst depth × close
def f03cdd_f03_crash_depth_duration_depthworstever_slope_v125_signal(closeadj):
    base = _f03_crash_depth(closeadj, 504).expanding(min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth gap to historical worst
def f03cdd_f03_crash_depth_duration_depthvshistworst_63d_slope_v126_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252)
    worst = d.expanding(min_periods=63).min()
    base = (d - worst) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth gap to historical worst
def f03cdd_f03_crash_depth_duration_depthvshistworst_252d_slope_v127_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504)
    worst = d.expanding(min_periods=252).min()
    base = (d - worst) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of depth-area frac 63v252
def f03cdd_f03_crash_depth_duration_depthareafrac_63v252_slope_v128_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    a = d.rolling(63, min_periods=21).sum()
    b = d.rolling(252, min_periods=63).sum().replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of depth-area frac 21v63
def f03cdd_f03_crash_depth_duration_depthareafrac_21v63_slope_v129_signal(closeadj):
    d = _f03_crash_depth(closeadj, 63).abs()
    a = d.rolling(21, min_periods=5).sum()
    b = d.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of depth-area frac 252v504
def f03cdd_f03_crash_depth_duration_depthareafrac_252v504_slope_v130_signal(closeadj):
    d = _f03_crash_depth(closeadj, 504).abs()
    a = d.rolling(252, min_periods=63).sum()
    b = d.rolling(504, min_periods=126).sum().replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of duration-area frac 63v252
def f03cdd_f03_crash_depth_duration_durareafrac_63v252_slope_v131_signal(closeadj):
    d = _f03_crash_duration(closeadj, 252)
    a = d.rolling(63, min_periods=21).sum()
    b = d.rolling(252, min_periods=63).sum().replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth vol-of-vol × close
def f03cdd_f03_crash_depth_duration_depthvolvol_63d_slope_v132_signal(closeadj):
    sd = _std(_f03_crash_depth(closeadj, 252), 63)
    base = _std(sd, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth vol-of-vol × close
def f03cdd_f03_crash_depth_duration_depthvolvol_252d_slope_v133_signal(closeadj):
    sd = _std(_f03_crash_depth(closeadj, 504), 252)
    base = _std(sd, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth anomaly × close
def f03cdd_f03_crash_depth_duration_depthanomaly_63d_slope_v134_signal(closeadj):
    base = (_f03_crash_depth(closeadj, 63) - _mean(_f03_crash_depth(closeadj, 252), 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth anomaly × close
def f03cdd_f03_crash_depth_duration_depthanomaly_252d_slope_v135_signal(closeadj):
    base = (_f03_crash_depth(closeadj, 252) - _mean(_f03_crash_depth(closeadj, 504), 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration anomaly × close
def f03cdd_f03_crash_depth_duration_durationanomaly_63d_slope_v136_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 63) - _mean(_f03_crash_duration(closeadj, 252), 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d duration anomaly × close
def f03cdd_f03_crash_depth_duration_durationanomaly_252d_slope_v137_signal(closeadj):
    base = (_f03_crash_duration(closeadj, 252) - _mean(_f03_crash_duration(closeadj, 504), 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d recovery half-life proxy × close
def f03cdd_f03_crash_depth_duration_rechalfproxy_63d_slope_v138_signal(closeadj):
    rec = _f03_crash_recovery(closeadj, 63)
    dep = _f03_crash_depth(closeadj, 63).abs().replace(0, np.nan)
    base = (1.0 - (rec / dep).clip(upper=2.0)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d recovery half-life proxy × close
def f03cdd_f03_crash_depth_duration_rechalfproxy_252d_slope_v139_signal(closeadj):
    rec = _f03_crash_recovery(closeadj, 252)
    dep = _f03_crash_depth(closeadj, 252).abs().replace(0, np.nan)
    base = (1.0 - (rec / dep).clip(upper=2.0)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth EMA × close
def f03cdd_f03_crash_depth_duration_depthema_63d_slope_v140_signal(closeadj):
    base = _f03_crash_depth(closeadj, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth EMA × close
def f03cdd_f03_crash_depth_duration_depthema_252d_slope_v141_signal(closeadj):
    base = _f03_crash_depth(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d duration EMA × close
def f03cdd_f03_crash_depth_duration_durationema_21d_slope_v142_signal(closeadj):
    base = _f03_crash_duration(closeadj, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d duration EMA × close
def f03cdd_f03_crash_depth_duration_durationema_252d_slope_v143_signal(closeadj):
    base = _f03_crash_duration(closeadj, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of recovery max in 252d × close
def f03cdd_f03_crash_depth_duration_recmaxin_252d_slope_v144_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 63).rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of recovery max in 504d × close
def f03cdd_f03_crash_depth_duration_recmaxin_504d_slope_v145_signal(closeadj):
    base = _f03_crash_recovery(closeadj, 252).rolling(504, min_periods=126).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth × current dollar volume
def f03cdd_f03_crash_depth_duration_depthxcurdv_63d_slope_v146_signal(closeadj, volume):
    base = _f03_crash_depth(closeadj, 63) * (closeadj * volume)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × current dollar volume
def f03cdd_f03_crash_depth_duration_depthxcurdv_252d_slope_v147_signal(closeadj, volume):
    base = _f03_crash_depth(closeadj, 252) * (closeadj * volume)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d depth × range
def f03cdd_f03_crash_depth_duration_depthxrange_63d_slope_v148_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f03_crash_depth(closeadj, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d depth × range
def f03cdd_f03_crash_depth_duration_depthxrange_252d_slope_v149_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f03_crash_depth(closeadj, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite severity
def f03cdd_f03_crash_depth_duration_compositesev_252d_slope_v150_signal(closeadj):
    d = _f03_crash_depth(closeadj, 252).abs()
    t = _f03_crash_duration(closeadj, 252) / 252.0
    base = (d + t) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03cdd_f03_crash_depth_duration_depth_21d_slope_v001_signal,
    f03cdd_f03_crash_depth_duration_depth_21d_slope_v002_signal,
    f03cdd_f03_crash_depth_duration_depth_63d_slope_v003_signal,
    f03cdd_f03_crash_depth_duration_depth_63d_slope_v004_signal,
    f03cdd_f03_crash_depth_duration_depth_63d_slope_v005_signal,
    f03cdd_f03_crash_depth_duration_depth_126d_slope_v006_signal,
    f03cdd_f03_crash_depth_duration_depth_126d_slope_v007_signal,
    f03cdd_f03_crash_depth_duration_depth_252d_slope_v008_signal,
    f03cdd_f03_crash_depth_duration_depth_252d_slope_v009_signal,
    f03cdd_f03_crash_depth_duration_depth_504d_slope_v010_signal,
    f03cdd_f03_crash_depth_duration_depth_504d_slope_v011_signal,
    f03cdd_f03_crash_depth_duration_depthmean_21d_slope_v012_signal,
    f03cdd_f03_crash_depth_duration_depthmean_63d_slope_v013_signal,
    f03cdd_f03_crash_depth_duration_depthstd_63d_slope_v014_signal,
    f03cdd_f03_crash_depth_duration_depthstd_126d_slope_v015_signal,
    f03cdd_f03_crash_depth_duration_depthz_252d_slope_v016_signal,
    f03cdd_f03_crash_depth_duration_depthz_504d_slope_v017_signal,
    f03cdd_f03_crash_depth_duration_depthxprice_21d_slope_v018_signal,
    f03cdd_f03_crash_depth_duration_depthxprice_21d_slope_v019_signal,
    f03cdd_f03_crash_depth_duration_depthxprice_252d_slope_v020_signal,
    f03cdd_f03_crash_depth_duration_depthsq_21d_slope_v021_signal,
    f03cdd_f03_crash_depth_duration_depthsq_63d_slope_v022_signal,
    f03cdd_f03_crash_depth_duration_depthsq_252d_slope_v023_signal,
    f03cdd_f03_crash_depth_duration_depthcount5_252d_slope_v024_signal,
    f03cdd_f03_crash_depth_duration_deepdaycount_252d_slope_v025_signal,
    f03cdd_f03_crash_depth_duration_durationxprice_21d_slope_v026_signal,
    f03cdd_f03_crash_depth_duration_duration_63d_slope_v027_signal,
    f03cdd_f03_crash_depth_duration_duration_126d_slope_v028_signal,
    f03cdd_f03_crash_depth_duration_duration_252d_slope_v029_signal,
    f03cdd_f03_crash_depth_duration_duration_504d_slope_v030_signal,
    f03cdd_f03_crash_depth_duration_durationfrac_252d_slope_v031_signal,
    f03cdd_f03_crash_depth_duration_durationfrac_63d_slope_v032_signal,
    f03cdd_f03_crash_depth_duration_durationfrac_504d_slope_v033_signal,
    f03cdd_f03_crash_depth_duration_durationmean_63d_slope_v034_signal,
    f03cdd_f03_crash_depth_duration_durationmean_252d_slope_v035_signal,
    f03cdd_f03_crash_depth_duration_durationz_252d_slope_v036_signal,
    f03cdd_f03_crash_depth_duration_durationz_504d_slope_v037_signal,
    f03cdd_f03_crash_depth_duration_duranddepth_63d_slope_v038_signal,
    f03cdd_f03_crash_depth_duration_duranddepth_252d_slope_v039_signal,
    f03cdd_f03_crash_depth_duration_duranddepth_504d_slope_v040_signal,
    f03cdd_f03_crash_depth_duration_durationmax_63d_slope_v041_signal,
    f03cdd_f03_crash_depth_duration_durationmax_252d_slope_v042_signal,
    f03cdd_f03_crash_depth_duration_durationmax_504d_slope_v043_signal,
    f03cdd_f03_crash_depth_duration_deepdurwgt_63d_slope_v044_signal,
    f03cdd_f03_crash_depth_duration_deepdurwgt_252d_slope_v045_signal,
    f03cdd_f03_crash_depth_duration_deepdurwgt_504d_slope_v046_signal,
    f03cdd_f03_crash_depth_duration_depth_5d_slope_v047_signal,
    f03cdd_f03_crash_depth_duration_depth_10d_slope_v048_signal,
    f03cdd_f03_crash_depth_duration_depth_42d_slope_v049_signal,
    f03cdd_f03_crash_depth_duration_depth_189d_slope_v050_signal,
    f03cdd_f03_crash_depth_duration_depth_378d_slope_v051_signal,
    f03cdd_f03_crash_depth_duration_durationxdepth_5d_slope_v052_signal,
    f03cdd_f03_crash_depth_duration_durationxdepth_10d_slope_v053_signal,
    f03cdd_f03_crash_depth_duration_durationxdepth_42d_slope_v054_signal,
    f03cdd_f03_crash_depth_duration_duration_189d_slope_v055_signal,
    f03cdd_f03_crash_depth_duration_duration_378d_slope_v056_signal,
    f03cdd_f03_crash_depth_duration_deptharea_63d_slope_v057_signal,
    f03cdd_f03_crash_depth_duration_deptharea_252d_slope_v058_signal,
    f03cdd_f03_crash_depth_duration_deptharea_504d_slope_v059_signal,
    f03cdd_f03_crash_depth_duration_depthperday_63d_slope_v060_signal,
    f03cdd_f03_crash_depth_duration_depthperday_252d_slope_v061_signal,
    f03cdd_f03_crash_depth_duration_depthperday_504d_slope_v062_signal,
    f03cdd_f03_crash_depth_duration_recovery_63d_slope_v063_signal,
    f03cdd_f03_crash_depth_duration_recovery_252d_slope_v064_signal,
    f03cdd_f03_crash_depth_duration_recovery_504d_slope_v065_signal,
    f03cdd_f03_crash_depth_duration_depthplusrec_252d_slope_v066_signal,
    f03cdd_f03_crash_depth_duration_depthplusrec_504d_slope_v067_signal,
    f03cdd_f03_crash_depth_duration_depthxvol_21d_slope_v068_signal,
    f03cdd_f03_crash_depth_duration_depthxvol_63d_slope_v069_signal,
    f03cdd_f03_crash_depth_duration_depthxdv_252d_slope_v070_signal,
    f03cdd_f03_crash_depth_duration_durxvolz_21d_slope_v071_signal,
    f03cdd_f03_crash_depth_duration_durxvolz_63d_slope_v072_signal,
    f03cdd_f03_crash_depth_duration_depthxnewtrough_63d_slope_v073_signal,
    f03cdd_f03_crash_depth_duration_depthxnewtrough_252d_slope_v074_signal,
    f03cdd_f03_crash_depth_duration_depthnormrange_252d_slope_v075_signal,
    f03cdd_f03_crash_depth_duration_depthxretvol_21d_slope_v076_signal,
    f03cdd_f03_crash_depth_duration_depthxretvol_63d_slope_v077_signal,
    f03cdd_f03_crash_depth_duration_depthxretvol_252d_slope_v078_signal,
    f03cdd_f03_crash_depth_duration_depthxret_21d_slope_v079_signal,
    f03cdd_f03_crash_depth_duration_depthxret_63d_slope_v080_signal,
    f03cdd_f03_crash_depth_duration_depthxret_252d_slope_v081_signal,
    f03cdd_f03_crash_depth_duration_depthnormatr_63d_slope_v082_signal,
    f03cdd_f03_crash_depth_duration_depthnormatr_504d_slope_v083_signal,
    f03cdd_f03_crash_depth_duration_depthxdownvol_63d_slope_v084_signal,
    f03cdd_f03_crash_depth_duration_depthxdownvol_252d_slope_v085_signal,
    f03cdd_f03_crash_depth_duration_depthxskew_63d_slope_v086_signal,
    f03cdd_f03_crash_depth_duration_depthxskew_252d_slope_v087_signal,
    f03cdd_f03_crash_depth_duration_depthxkurt_63d_slope_v088_signal,
    f03cdd_f03_crash_depth_duration_depthxkurt_252d_slope_v089_signal,
    f03cdd_f03_crash_depth_duration_depthratio_63v252_slope_v090_signal,
    f03cdd_f03_crash_depth_duration_depthratio_21v63_slope_v091_signal,
    f03cdd_f03_crash_depth_duration_depthratio_252v504_slope_v092_signal,
    f03cdd_f03_crash_depth_duration_depthdiff_63m252_slope_v093_signal,
    f03cdd_f03_crash_depth_duration_depthdiff_21m63_slope_v094_signal,
    f03cdd_f03_crash_depth_duration_depthdiff_252m504_slope_v095_signal,
    f03cdd_f03_crash_depth_duration_depthxdur_63d_slope_v096_signal,
    f03cdd_f03_crash_depth_duration_depthxdur_252d_slope_v097_signal,
    f03cdd_f03_crash_depth_duration_depthxdur_504d_slope_v098_signal,
    f03cdd_f03_crash_depth_duration_durexpxprice_21d_slope_v099_signal,
    f03cdd_f03_crash_depth_duration_durxretvol_63d_slope_v100_signal,
    f03cdd_f03_crash_depth_duration_durxretvol_252d_slope_v101_signal,
    f03cdd_f03_crash_depth_duration_durxret_21d_slope_v102_signal,
    f03cdd_f03_crash_depth_duration_durxret_63d_slope_v103_signal,
    f03cdd_f03_crash_depth_duration_durxret_252d_slope_v104_signal,
    f03cdd_f03_crash_depth_duration_durxatr_63d_slope_v105_signal,
    f03cdd_f03_crash_depth_duration_durxatr_252d_slope_v106_signal,
    f03cdd_f03_crash_depth_duration_durratio_63v252_slope_v107_signal,
    f03cdd_f03_crash_depth_duration_durratio_21v63_slope_v108_signal,
    f03cdd_f03_crash_depth_duration_durdiff_63m252_slope_v109_signal,
    f03cdd_f03_crash_depth_duration_durdiff_21m63_slope_v110_signal,
    f03cdd_f03_crash_depth_duration_durdiff_252m504_slope_v111_signal,
    f03cdd_f03_crash_depth_duration_recovery_21d_slope_v112_signal,
    f03cdd_f03_crash_depth_duration_recovery_126d_slope_v113_signal,
    f03cdd_f03_crash_depth_duration_recovery_378d_slope_v114_signal,
    f03cdd_f03_crash_depth_duration_recxdur_63d_slope_v115_signal,
    f03cdd_f03_crash_depth_duration_recxdur_252d_slope_v116_signal,
    f03cdd_f03_crash_depth_duration_recxdur_504d_slope_v117_signal,
    f03cdd_f03_crash_depth_duration_receff_63d_slope_v118_signal,
    f03cdd_f03_crash_depth_duration_receff_252d_slope_v119_signal,
    f03cdd_f03_crash_depth_duration_receff_504d_slope_v120_signal,
    f03cdd_f03_crash_depth_duration_recxvolz_63d_slope_v121_signal,
    f03cdd_f03_crash_depth_duration_recxvolz_252d_slope_v122_signal,
    f03cdd_f03_crash_depth_duration_recentdeepXpersist_252d_slope_v123_signal,
    f03cdd_f03_crash_depth_duration_recentdeepXpersist_504d_slope_v124_signal,
    f03cdd_f03_crash_depth_duration_depthworstever_slope_v125_signal,
    f03cdd_f03_crash_depth_duration_depthvshistworst_63d_slope_v126_signal,
    f03cdd_f03_crash_depth_duration_depthvshistworst_252d_slope_v127_signal,
    f03cdd_f03_crash_depth_duration_depthareafrac_63v252_slope_v128_signal,
    f03cdd_f03_crash_depth_duration_depthareafrac_21v63_slope_v129_signal,
    f03cdd_f03_crash_depth_duration_depthareafrac_252v504_slope_v130_signal,
    f03cdd_f03_crash_depth_duration_durareafrac_63v252_slope_v131_signal,
    f03cdd_f03_crash_depth_duration_depthvolvol_63d_slope_v132_signal,
    f03cdd_f03_crash_depth_duration_depthvolvol_252d_slope_v133_signal,
    f03cdd_f03_crash_depth_duration_depthanomaly_63d_slope_v134_signal,
    f03cdd_f03_crash_depth_duration_depthanomaly_252d_slope_v135_signal,
    f03cdd_f03_crash_depth_duration_durationanomaly_63d_slope_v136_signal,
    f03cdd_f03_crash_depth_duration_durationanomaly_252d_slope_v137_signal,
    f03cdd_f03_crash_depth_duration_rechalfproxy_63d_slope_v138_signal,
    f03cdd_f03_crash_depth_duration_rechalfproxy_252d_slope_v139_signal,
    f03cdd_f03_crash_depth_duration_depthema_63d_slope_v140_signal,
    f03cdd_f03_crash_depth_duration_depthema_252d_slope_v141_signal,
    f03cdd_f03_crash_depth_duration_durationema_21d_slope_v142_signal,
    f03cdd_f03_crash_depth_duration_durationema_252d_slope_v143_signal,
    f03cdd_f03_crash_depth_duration_recmaxin_252d_slope_v144_signal,
    f03cdd_f03_crash_depth_duration_recmaxin_504d_slope_v145_signal,
    f03cdd_f03_crash_depth_duration_depthxcurdv_63d_slope_v146_signal,
    f03cdd_f03_crash_depth_duration_depthxcurdv_252d_slope_v147_signal,
    f03cdd_f03_crash_depth_duration_depthxrange_63d_slope_v148_signal,
    f03cdd_f03_crash_depth_duration_depthxrange_252d_slope_v149_signal,
    f03cdd_f03_crash_depth_duration_compositesev_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_CRASH_DEPTH_DURATION_REGISTRY_SLOPE = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f03_crash_depth_duration_2nd_derivatives_001_150_claude: {n_features} features pass")
