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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f036_vwap(close, volume, w):
    pv = (close * volume).rolling(w, min_periods=max(1, w // 2)).sum()
    vv = volume.rolling(w, min_periods=max(1, w // 2)).sum()
    return pv / vv.replace(0, np.nan)


def _f036_vwap_distance(close, volume, w):
    vwap = _f036_vwap(close, volume, w)
    return (close - vwap) / vwap.replace(0, np.nan).abs()


def _f036_vwap_slope(close, volume, w):
    vwap = _f036_vwap(close, volume, w)
    return vwap.diff(periods=w) / vwap.abs().replace(0, np.nan)


def _build_slope_features():
    funcs = []
    # primitive 1: _f036_vwap — vary base window and slope window
    # primitive 2: _f036_vwap_distance — vary base window and slope window
    # primitive 3: _f036_vwap_slope — vary base window and slope window
    return funcs


# --- vwap level slope features (50) ---
# 5d slope of 21d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v001_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v002_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v003_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v004_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v005_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v006_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v007_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v008_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v009_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v010_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v011_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v012_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v013_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v014_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_504d_slope_v015_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_504d_slope_v016_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d vwap
def f036vds_f036_vwap_distance_slope_vwaplev_504d_slope_v017_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pct-slope of 21d vwap × close
def f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v018_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-slope of 63d vwap × close
def f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v019_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-slope of 252d vwap × close
def f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v020_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap gap (close − 21d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_21d_slope_v021_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap gap (close − 63d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_63d_slope_v022_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap gap (close − 126d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_126d_slope_v023_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap gap (close − 252d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_252d_slope_v024_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap gap (close − 504d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_504d_slope_v025_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap gap (close − 5d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_5d_slope_v026_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 5)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap gap (close − 10d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_10d_slope_v027_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 10)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap gap (close − 42d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_42d_slope_v028_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap gap (close − 189d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_189d_slope_v029_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 189)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap gap (close − 378d vwap)
def f036vds_f036_vwap_distance_slope_vwapgap_378d_slope_v030_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 378)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_vwapdist_21d_slope_v031_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_vwapdist_21d_slope_v032_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_vwapdist_21d_slope_v033_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap distance × close (63d)
def f036vds_f036_vwap_distance_slope_vwapdist_63d_slope_v034_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap distance × close (63d)
def f036vds_f036_vwap_distance_slope_vwapdist_63d_slope_v035_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap distance × close (126d)
def f036vds_f036_vwap_distance_slope_vwapdist_126d_slope_v036_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap distance × close (126d)
def f036vds_f036_vwap_distance_slope_vwapdist_126d_slope_v037_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap distance × close (252d)
def f036vds_f036_vwap_distance_slope_vwapdist_252d_slope_v038_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap distance × close (252d)
def f036vds_f036_vwap_distance_slope_vwapdist_252d_slope_v039_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap distance × close (504d)
def f036vds_f036_vwap_distance_slope_vwapdist_504d_slope_v040_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap distance × close (5d)
def f036vds_f036_vwap_distance_slope_vwapdist_5d_slope_v041_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap distance × close (10d)
def f036vds_f036_vwap_distance_slope_vwapdist_10d_slope_v042_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap distance × close (42d)
def f036vds_f036_vwap_distance_slope_vwapdist_42d_slope_v043_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap distance × close (189d)
def f036vds_f036_vwap_distance_slope_vwapdist_189d_slope_v044_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap distance × close (378d)
def f036vds_f036_vwap_distance_slope_vwapdist_378d_slope_v045_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap distance × volume (21d)
def f036vds_f036_vwap_distance_slope_distxvol_21d_slope_v046_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * volume
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap distance × volume (63d)
def f036vds_f036_vwap_distance_slope_distxvol_63d_slope_v047_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * volume
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap distance × dollar volume (21d)
def f036vds_f036_vwap_distance_slope_distxdv_21d_slope_v048_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * (closeadj * volume)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap distance × dollar volume (63d)
def f036vds_f036_vwap_distance_slope_distxdv_63d_slope_v049_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * (closeadj * volume)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mean vwap distance (21d, smooth 21d)
def f036vds_f036_vwap_distance_slope_meandist_21d_slope_v050_signal(closeadj, volume):
    base = _mean(_f036_vwap_distance(closeadj, volume, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mean vwap distance (63d, smooth 21d)
def f036vds_f036_vwap_distance_slope_meandist_63d_slope_v051_signal(closeadj, volume):
    base = _mean(_f036_vwap_distance(closeadj, volume, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mean vwap distance (126d, smooth 63d)
def f036vds_f036_vwap_distance_slope_meandist_126d_slope_v052_signal(closeadj, volume):
    base = _mean(_f036_vwap_distance(closeadj, volume, 126), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mean vwap distance (252d, smooth 63d)
def f036vds_f036_vwap_distance_slope_meandist_252d_slope_v053_signal(closeadj, volume):
    base = _mean(_f036_vwap_distance(closeadj, volume, 252), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of std vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_stddist_21d_slope_v054_signal(closeadj, volume):
    base = _std(_f036_vwap_distance(closeadj, volume, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of std vwap distance × close (63d)
def f036vds_f036_vwap_distance_slope_stddist_63d_slope_v055_signal(closeadj, volume):
    base = _std(_f036_vwap_distance(closeadj, volume, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of z vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_zdist_21d_slope_v056_signal(closeadj, volume):
    base = _z(_f036_vwap_distance(closeadj, volume, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of z vwap distance × close (63d)
def f036vds_f036_vwap_distance_slope_zdist_63d_slope_v057_signal(closeadj, volume):
    base = _z(_f036_vwap_distance(closeadj, volume, 63), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of abs vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_absdist_21d_slope_v058_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of abs vwap distance × close (63d)
def f036vds_f036_vwap_distance_slope_absdist_63d_slope_v059_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of abs vwap distance × close (252d)
def f036vds_f036_vwap_distance_slope_absdist_252d_slope_v060_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 252).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of squared vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_distsq_21d_slope_v061_signal(closeadj, volume):
    d = _f036_vwap_distance(closeadj, volume, 21)
    base = d * d.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of squared vwap distance × close (63d)
def f036vds_f036_vwap_distance_slope_distsq_63d_slope_v062_signal(closeadj, volume):
    d = _f036_vwap_distance(closeadj, volume, 63)
    base = d * d.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EMA vwap distance × close (21d)
def f036vds_f036_vwap_distance_slope_emadist_21d_slope_v063_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EMA vwap distance × close (63d)
def f036vds_f036_vwap_distance_slope_emadist_63d_slope_v064_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × log volume (21d)
def f036vds_f036_vwap_distance_slope_distxlogv_21d_slope_v065_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × log volume (63d)
def f036vds_f036_vwap_distance_slope_distxlogv_63d_slope_v066_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of close × vwap distance (5d distance)
def f036vds_f036_vwap_distance_slope_distxcl_5d_slope_v067_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of close × vwap distance (10d distance)
def f036vds_f036_vwap_distance_slope_distxcl_10d_slope_v068_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 10) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of close × vwap distance (42d distance)
def f036vds_f036_vwap_distance_slope_distxcl_42d_slope_v069_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of close × vwap distance (189d distance) with mean(close,21)
def f036vds_f036_vwap_distance_slope_distxcl_189d_slope_v070_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 189) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of close × vwap distance (378d distance) with mean(close,63)
def f036vds_f036_vwap_distance_slope_distxcl_378d_slope_v071_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 378) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of (close - vwap42) × volume
def f036vds_f036_vwap_distance_slope_gapxvol_42d_slope_v072_signal(closeadj, volume):
    base = (closeadj - _f036_vwap(closeadj, volume, 42)) * volume
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (close - vwap189) × dollar volume
def f036vds_f036_vwap_distance_slope_gapxdv_189d_slope_v073_signal(closeadj, volume):
    base = (closeadj - _f036_vwap(closeadj, volume, 189)) * (closeadj * volume)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × volume_z (21d)
def f036vds_f036_vwap_distance_slope_distxvolz_21d_slope_v074_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × volume_z (63d)
def f036vds_f036_vwap_distance_slope_distxvolz_63d_slope_v075_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_slope_21d_slope_v076_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_slope_21d_slope_v077_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_slope_21d_slope_v078_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_slope_63d_slope_v079_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_slope_63d_slope_v080_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_slope_63d_slope_v081_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap-slope × close (126d slope)
def f036vds_f036_vwap_distance_slope_slope_126d_slope_v082_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap-slope × close (126d slope)
def f036vds_f036_vwap_distance_slope_slope_126d_slope_v083_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap-slope × close (126d slope)
def f036vds_f036_vwap_distance_slope_slope_126d_slope_v084_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap-slope × close (252d slope)
def f036vds_f036_vwap_distance_slope_slope_252d_slope_v085_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap-slope × close (252d slope)
def f036vds_f036_vwap_distance_slope_slope_252d_slope_v086_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap-slope × close (504d slope)
def f036vds_f036_vwap_distance_slope_slope_504d_slope_v087_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap-slope × close (5d slope)
def f036vds_f036_vwap_distance_slope_slope_5d_slope_v088_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of vwap-slope × close (10d slope)
def f036vds_f036_vwap_distance_slope_slope_10d_slope_v089_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 10) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap-slope × close (42d slope)
def f036vds_f036_vwap_distance_slope_slope_42d_slope_v090_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap-slope × close (189d slope)
def f036vds_f036_vwap_distance_slope_slope_189d_slope_v091_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap-slope × close (378d slope)
def f036vds_f036_vwap_distance_slope_slope_378d_slope_v092_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap-slope × volume (21d slope)
def f036vds_f036_vwap_distance_slope_slopexvol_21d_slope_v093_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * volume
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap-slope × volume (63d slope)
def f036vds_f036_vwap_distance_slope_slopexvol_63d_slope_v094_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * volume
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap-slope × dollar volume (21d slope)
def f036vds_f036_vwap_distance_slope_slopexdv_21d_slope_v095_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * (closeadj * volume)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap-slope × dollar volume (63d slope)
def f036vds_f036_vwap_distance_slope_slopexdv_63d_slope_v096_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * (closeadj * volume)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mean vwap-slope × close (21d slope, smooth 21d)
def f036vds_f036_vwap_distance_slope_meanslope_21d_slope_v097_signal(closeadj, volume):
    base = _mean(_f036_vwap_slope(closeadj, volume, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mean vwap-slope × close (63d slope, smooth 21d)
def f036vds_f036_vwap_distance_slope_meanslope_63d_slope_v098_signal(closeadj, volume):
    base = _mean(_f036_vwap_slope(closeadj, volume, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mean vwap-slope × close (126d slope, smooth 63d)
def f036vds_f036_vwap_distance_slope_meanslope_126d_slope_v099_signal(closeadj, volume):
    base = _mean(_f036_vwap_slope(closeadj, volume, 126), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of std vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_stdslope_21d_slope_v100_signal(closeadj, volume):
    base = _std(_f036_vwap_slope(closeadj, volume, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of std vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_stdslope_63d_slope_v101_signal(closeadj, volume):
    base = _std(_f036_vwap_slope(closeadj, volume, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of z vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_zslope_21d_slope_v102_signal(closeadj, volume):
    base = _z(_f036_vwap_slope(closeadj, volume, 21), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of z vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_zslope_63d_slope_v103_signal(closeadj, volume):
    base = _z(_f036_vwap_slope(closeadj, volume, 63), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of abs vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_absslope_21d_slope_v104_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of abs vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_absslope_63d_slope_v105_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of abs vwap-slope × close (252d slope)
def f036vds_f036_vwap_distance_slope_absslope_252d_slope_v106_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 252).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of squared vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_slopesq_21d_slope_v107_signal(closeadj, volume):
    s = _f036_vwap_slope(closeadj, volume, 21)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of squared vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_slopesq_63d_slope_v108_signal(closeadj, volume):
    s = _f036_vwap_slope(closeadj, volume, 63)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EMA vwap-slope × close (21d slope)
def f036vds_f036_vwap_distance_slope_emaslope_21d_slope_v109_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21).ewm(span=21, adjust=False, min_periods=5).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EMA vwap-slope × close (63d slope)
def f036vds_f036_vwap_distance_slope_emaslope_63d_slope_v110_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63).ewm(span=63, adjust=False, min_periods=10).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_slope × log volume (21d)
def f036vds_f036_vwap_distance_slope_slopexlogv_21d_slope_v111_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_slope × log volume (63d)
def f036vds_f036_vwap_distance_slope_slopexlogv_63d_slope_v112_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * np.log(volume.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of (close − vwap5)
def f036vds_f036_vwap_distance_slope_vwapgap_5d_slope_v113_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of (close − vwap42)
def f036vds_f036_vwap_distance_slope_vwapgap_42d_slope_v114_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 42)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of (close − vwap189)
def f036vds_f036_vwap_distance_slope_vwapgap_189d_slope_v115_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 189)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (close − vwap378)
def f036vds_f036_vwap_distance_slope_vwapgap_378d_slope_v116_signal(closeadj, volume):
    base = closeadj - _f036_vwap(closeadj, volume, 378)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × close roll-mean (21d)
def f036vds_f036_vwap_distance_slope_distxclmean_21d_slope_v117_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × close roll-mean (63d)
def f036vds_f036_vwap_distance_slope_distxclmean_63d_slope_v118_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_slope × close roll-mean (21d)
def f036vds_f036_vwap_distance_slope_slopexclmean_21d_slope_v119_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_slope × close roll-mean (63d)
def f036vds_f036_vwap_distance_slope_slopexclmean_63d_slope_v120_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × volume mean (21d)
def f036vds_f036_vwap_distance_slope_distxvmean_21d_slope_v121_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * _mean(volume, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × volume mean (63d)
def f036vds_f036_vwap_distance_slope_distxvmean_63d_slope_v122_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * _mean(volume, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_slope × volume mean (21d)
def f036vds_f036_vwap_distance_slope_slopexvmean_21d_slope_v123_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * _mean(volume, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_slope × volume mean (63d)
def f036vds_f036_vwap_distance_slope_slopexvmean_63d_slope_v124_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * _mean(volume, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × close std (21d)
def f036vds_f036_vwap_distance_slope_distxclstd_21d_slope_v125_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × close std (63d)
def f036vds_f036_vwap_distance_slope_distxclstd_63d_slope_v126_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_slope × close std (21d)
def f036vds_f036_vwap_distance_slope_slopexclstd_21d_slope_v127_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * _std(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_slope × close std (63d)
def f036vds_f036_vwap_distance_slope_slopexclstd_63d_slope_v128_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × z-close (21d)
def f036vds_f036_vwap_distance_slope_distxzcl_21d_slope_v129_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * _z(closeadj, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × z-close (63d)
def f036vds_f036_vwap_distance_slope_distxzcl_63d_slope_v130_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * _z(closeadj, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × volume × close (21d)
def f036vds_f036_vwap_distance_slope_distxvolxcl_21d_slope_v131_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * volume * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × volume × close (63d)
def f036vds_f036_vwap_distance_slope_distxvolxcl_63d_slope_v132_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * volume * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_slope × volume × close (21d)
def f036vds_f036_vwap_distance_slope_slopexvolxcl_21d_slope_v133_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 21) * volume * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_slope × volume × close (63d)
def f036vds_f036_vwap_distance_slope_slopexvolxcl_63d_slope_v134_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * volume * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of dist × cum dollar-volume mean (21d)
def f036vds_f036_vwap_distance_slope_distxcumcl_21d_slope_v135_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * _mean(closeadj * volume, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of slope × cum dollar-volume mean (63d)
def f036vds_f036_vwap_distance_slope_slopexcumcl_63d_slope_v136_signal(closeadj, volume):
    base = _f036_vwap_slope(closeadj, volume, 63) * _mean(closeadj * volume, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_minus_short_long (21 - 252)
def f036vds_f036_vwap_distance_slope_vwapminus_21_252_slope_v137_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 21) - _f036_vwap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_minus_short_long (63 - 252)
def f036vds_f036_vwap_distance_slope_vwapminus_63_252_slope_v138_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 63) - _f036_vwap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap_minus_short_long (126 - 504)
def f036vds_f036_vwap_distance_slope_vwapminus_126_504_slope_v139_signal(closeadj, volume):
    base = _f036_vwap(closeadj, volume, 126) - _f036_vwap(closeadj, volume, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_ratio (close/vwap21) × close
def f036vds_f036_vwap_distance_slope_vwapratio_21d_slope_v140_signal(closeadj, volume):
    base = _safe_div(closeadj, _f036_vwap(closeadj, volume, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_ratio (close/vwap63) × close
def f036vds_f036_vwap_distance_slope_vwapratio_63d_slope_v141_signal(closeadj, volume):
    base = _safe_div(closeadj, _f036_vwap(closeadj, volume, 63)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of vwap_ratio (close/vwap252) × close
def f036vds_f036_vwap_distance_slope_vwapratio_252d_slope_v142_signal(closeadj, volume):
    base = _safe_div(closeadj, _f036_vwap(closeadj, volume, 252)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of sign vwap_distance × close (21d)
def f036vds_f036_vwap_distance_slope_signdist_21d_slope_v143_signal(closeadj, volume):
    base = np.sign(_f036_vwap_distance(closeadj, volume, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sign vwap_distance × close (63d)
def f036vds_f036_vwap_distance_slope_signdist_63d_slope_v144_signal(closeadj, volume):
    base = np.sign(_f036_vwap_distance(closeadj, volume, 63)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of sign vwap_slope × close (21d)
def f036vds_f036_vwap_distance_slope_signslope_21d_slope_v145_signal(closeadj, volume):
    base = np.sign(_f036_vwap_slope(closeadj, volume, 21)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sign vwap_slope × close (63d)
def f036vds_f036_vwap_distance_slope_signslope_63d_slope_v146_signal(closeadj, volume):
    base = np.sign(_f036_vwap_slope(closeadj, volume, 63)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vwap_distance × vwap_slope (21d × 21d)
def f036vds_f036_vwap_distance_slope_distxslope_21d_slope_v147_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 21) * _f036_vwap_slope(closeadj, volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vwap_distance × vwap_slope (63d × 63d)
def f036vds_f036_vwap_distance_slope_distxslope_63d_slope_v148_signal(closeadj, volume):
    base = _f036_vwap_distance(closeadj, volume, 63) * _f036_vwap_slope(closeadj, volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of log vwap × close (21d)
def f036vds_f036_vwap_distance_slope_logvwap_21d_slope_v149_signal(closeadj, volume):
    base = np.log(_f036_vwap(closeadj, volume, 21).abs().replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log vwap × close (63d)
def f036vds_f036_vwap_distance_slope_logvwap_63d_slope_v150_signal(closeadj, volume):
    base = np.log(_f036_vwap(closeadj, volume, 63).abs().replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v001_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v002_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v003_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v004_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v005_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v006_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v007_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v008_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v009_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_126d_slope_v010_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v011_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v012_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v013_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v014_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_504d_slope_v015_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_504d_slope_v016_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_504d_slope_v017_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_21d_slope_v018_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_63d_slope_v019_signal,
    f036vds_f036_vwap_distance_slope_vwaplev_252d_slope_v020_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_21d_slope_v021_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_63d_slope_v022_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_126d_slope_v023_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_252d_slope_v024_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_504d_slope_v025_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_5d_slope_v026_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_10d_slope_v027_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_42d_slope_v028_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_189d_slope_v029_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_378d_slope_v030_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_21d_slope_v031_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_21d_slope_v032_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_21d_slope_v033_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_63d_slope_v034_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_63d_slope_v035_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_126d_slope_v036_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_126d_slope_v037_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_252d_slope_v038_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_252d_slope_v039_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_504d_slope_v040_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_5d_slope_v041_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_10d_slope_v042_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_42d_slope_v043_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_189d_slope_v044_signal,
    f036vds_f036_vwap_distance_slope_vwapdist_378d_slope_v045_signal,
    f036vds_f036_vwap_distance_slope_distxvol_21d_slope_v046_signal,
    f036vds_f036_vwap_distance_slope_distxvol_63d_slope_v047_signal,
    f036vds_f036_vwap_distance_slope_distxdv_21d_slope_v048_signal,
    f036vds_f036_vwap_distance_slope_distxdv_63d_slope_v049_signal,
    f036vds_f036_vwap_distance_slope_meandist_21d_slope_v050_signal,
    f036vds_f036_vwap_distance_slope_meandist_63d_slope_v051_signal,
    f036vds_f036_vwap_distance_slope_meandist_126d_slope_v052_signal,
    f036vds_f036_vwap_distance_slope_meandist_252d_slope_v053_signal,
    f036vds_f036_vwap_distance_slope_stddist_21d_slope_v054_signal,
    f036vds_f036_vwap_distance_slope_stddist_63d_slope_v055_signal,
    f036vds_f036_vwap_distance_slope_zdist_21d_slope_v056_signal,
    f036vds_f036_vwap_distance_slope_zdist_63d_slope_v057_signal,
    f036vds_f036_vwap_distance_slope_absdist_21d_slope_v058_signal,
    f036vds_f036_vwap_distance_slope_absdist_63d_slope_v059_signal,
    f036vds_f036_vwap_distance_slope_absdist_252d_slope_v060_signal,
    f036vds_f036_vwap_distance_slope_distsq_21d_slope_v061_signal,
    f036vds_f036_vwap_distance_slope_distsq_63d_slope_v062_signal,
    f036vds_f036_vwap_distance_slope_emadist_21d_slope_v063_signal,
    f036vds_f036_vwap_distance_slope_emadist_63d_slope_v064_signal,
    f036vds_f036_vwap_distance_slope_distxlogv_21d_slope_v065_signal,
    f036vds_f036_vwap_distance_slope_distxlogv_63d_slope_v066_signal,
    f036vds_f036_vwap_distance_slope_distxcl_5d_slope_v067_signal,
    f036vds_f036_vwap_distance_slope_distxcl_10d_slope_v068_signal,
    f036vds_f036_vwap_distance_slope_distxcl_42d_slope_v069_signal,
    f036vds_f036_vwap_distance_slope_distxcl_189d_slope_v070_signal,
    f036vds_f036_vwap_distance_slope_distxcl_378d_slope_v071_signal,
    f036vds_f036_vwap_distance_slope_gapxvol_42d_slope_v072_signal,
    f036vds_f036_vwap_distance_slope_gapxdv_189d_slope_v073_signal,
    f036vds_f036_vwap_distance_slope_distxvolz_21d_slope_v074_signal,
    f036vds_f036_vwap_distance_slope_distxvolz_63d_slope_v075_signal,
    f036vds_f036_vwap_distance_slope_slope_21d_slope_v076_signal,
    f036vds_f036_vwap_distance_slope_slope_21d_slope_v077_signal,
    f036vds_f036_vwap_distance_slope_slope_21d_slope_v078_signal,
    f036vds_f036_vwap_distance_slope_slope_63d_slope_v079_signal,
    f036vds_f036_vwap_distance_slope_slope_63d_slope_v080_signal,
    f036vds_f036_vwap_distance_slope_slope_63d_slope_v081_signal,
    f036vds_f036_vwap_distance_slope_slope_126d_slope_v082_signal,
    f036vds_f036_vwap_distance_slope_slope_126d_slope_v083_signal,
    f036vds_f036_vwap_distance_slope_slope_126d_slope_v084_signal,
    f036vds_f036_vwap_distance_slope_slope_252d_slope_v085_signal,
    f036vds_f036_vwap_distance_slope_slope_252d_slope_v086_signal,
    f036vds_f036_vwap_distance_slope_slope_504d_slope_v087_signal,
    f036vds_f036_vwap_distance_slope_slope_5d_slope_v088_signal,
    f036vds_f036_vwap_distance_slope_slope_10d_slope_v089_signal,
    f036vds_f036_vwap_distance_slope_slope_42d_slope_v090_signal,
    f036vds_f036_vwap_distance_slope_slope_189d_slope_v091_signal,
    f036vds_f036_vwap_distance_slope_slope_378d_slope_v092_signal,
    f036vds_f036_vwap_distance_slope_slopexvol_21d_slope_v093_signal,
    f036vds_f036_vwap_distance_slope_slopexvol_63d_slope_v094_signal,
    f036vds_f036_vwap_distance_slope_slopexdv_21d_slope_v095_signal,
    f036vds_f036_vwap_distance_slope_slopexdv_63d_slope_v096_signal,
    f036vds_f036_vwap_distance_slope_meanslope_21d_slope_v097_signal,
    f036vds_f036_vwap_distance_slope_meanslope_63d_slope_v098_signal,
    f036vds_f036_vwap_distance_slope_meanslope_126d_slope_v099_signal,
    f036vds_f036_vwap_distance_slope_stdslope_21d_slope_v100_signal,
    f036vds_f036_vwap_distance_slope_stdslope_63d_slope_v101_signal,
    f036vds_f036_vwap_distance_slope_zslope_21d_slope_v102_signal,
    f036vds_f036_vwap_distance_slope_zslope_63d_slope_v103_signal,
    f036vds_f036_vwap_distance_slope_absslope_21d_slope_v104_signal,
    f036vds_f036_vwap_distance_slope_absslope_63d_slope_v105_signal,
    f036vds_f036_vwap_distance_slope_absslope_252d_slope_v106_signal,
    f036vds_f036_vwap_distance_slope_slopesq_21d_slope_v107_signal,
    f036vds_f036_vwap_distance_slope_slopesq_63d_slope_v108_signal,
    f036vds_f036_vwap_distance_slope_emaslope_21d_slope_v109_signal,
    f036vds_f036_vwap_distance_slope_emaslope_63d_slope_v110_signal,
    f036vds_f036_vwap_distance_slope_slopexlogv_21d_slope_v111_signal,
    f036vds_f036_vwap_distance_slope_slopexlogv_63d_slope_v112_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_5d_slope_v113_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_42d_slope_v114_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_189d_slope_v115_signal,
    f036vds_f036_vwap_distance_slope_vwapgap_378d_slope_v116_signal,
    f036vds_f036_vwap_distance_slope_distxclmean_21d_slope_v117_signal,
    f036vds_f036_vwap_distance_slope_distxclmean_63d_slope_v118_signal,
    f036vds_f036_vwap_distance_slope_slopexclmean_21d_slope_v119_signal,
    f036vds_f036_vwap_distance_slope_slopexclmean_63d_slope_v120_signal,
    f036vds_f036_vwap_distance_slope_distxvmean_21d_slope_v121_signal,
    f036vds_f036_vwap_distance_slope_distxvmean_63d_slope_v122_signal,
    f036vds_f036_vwap_distance_slope_slopexvmean_21d_slope_v123_signal,
    f036vds_f036_vwap_distance_slope_slopexvmean_63d_slope_v124_signal,
    f036vds_f036_vwap_distance_slope_distxclstd_21d_slope_v125_signal,
    f036vds_f036_vwap_distance_slope_distxclstd_63d_slope_v126_signal,
    f036vds_f036_vwap_distance_slope_slopexclstd_21d_slope_v127_signal,
    f036vds_f036_vwap_distance_slope_slopexclstd_63d_slope_v128_signal,
    f036vds_f036_vwap_distance_slope_distxzcl_21d_slope_v129_signal,
    f036vds_f036_vwap_distance_slope_distxzcl_63d_slope_v130_signal,
    f036vds_f036_vwap_distance_slope_distxvolxcl_21d_slope_v131_signal,
    f036vds_f036_vwap_distance_slope_distxvolxcl_63d_slope_v132_signal,
    f036vds_f036_vwap_distance_slope_slopexvolxcl_21d_slope_v133_signal,
    f036vds_f036_vwap_distance_slope_slopexvolxcl_63d_slope_v134_signal,
    f036vds_f036_vwap_distance_slope_distxcumcl_21d_slope_v135_signal,
    f036vds_f036_vwap_distance_slope_slopexcumcl_63d_slope_v136_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_21_252_slope_v137_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_63_252_slope_v138_signal,
    f036vds_f036_vwap_distance_slope_vwapminus_126_504_slope_v139_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_21d_slope_v140_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_63d_slope_v141_signal,
    f036vds_f036_vwap_distance_slope_vwapratio_252d_slope_v142_signal,
    f036vds_f036_vwap_distance_slope_signdist_21d_slope_v143_signal,
    f036vds_f036_vwap_distance_slope_signdist_63d_slope_v144_signal,
    f036vds_f036_vwap_distance_slope_signslope_21d_slope_v145_signal,
    f036vds_f036_vwap_distance_slope_signslope_63d_slope_v146_signal,
    f036vds_f036_vwap_distance_slope_distxslope_21d_slope_v147_signal,
    f036vds_f036_vwap_distance_slope_distxslope_63d_slope_v148_signal,
    f036vds_f036_vwap_distance_slope_logvwap_21d_slope_v149_signal,
    f036vds_f036_vwap_distance_slope_logvwap_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F036_VWAP_DISTANCE_SLOPE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f036_vwap", "_f036_vwap_distance", "_f036_vwap_slope")
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
    print(f"OK f036_vwap_distance_slope_2nd_derivatives_001_150_claude: {n_features} features pass")
