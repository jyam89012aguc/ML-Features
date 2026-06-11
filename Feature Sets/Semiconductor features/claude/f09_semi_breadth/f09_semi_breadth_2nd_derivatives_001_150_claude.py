import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f09_brd_diff(brd, n):
    return brd - brd.shift(n)


def _f09_brd_dev(brd, w):
    return brd - brd.rolling(w, min_periods=max(1, w // 2)).mean()


# 5d slope of 21d brdmean
def f09br_f09_semi_breadth_brdmean_21d_slope_v001_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d brdmean
def f09br_f09_semi_breadth_brdmean_21d_slope_v002_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d brdmean
def f09br_f09_semi_breadth_brdmean_21d_slope_v003_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d brdmean
def f09br_f09_semi_breadth_brdmean_21d_slope_v004_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d brdmean
def f09br_f09_semi_breadth_brdmean_21d_slope_v005_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdmean
def f09br_f09_semi_breadth_brdmean_63d_slope_v006_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdmean
def f09br_f09_semi_breadth_brdmean_63d_slope_v007_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdmean
def f09br_f09_semi_breadth_brdmean_63d_slope_v008_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdmean
def f09br_f09_semi_breadth_brdmean_63d_slope_v009_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdmean
def f09br_f09_semi_breadth_brdmean_63d_slope_v010_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d brdmean
def f09br_f09_semi_breadth_brdmean_126d_slope_v011_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d brdmean
def f09br_f09_semi_breadth_brdmean_126d_slope_v012_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d brdmean
def f09br_f09_semi_breadth_brdmean_126d_slope_v013_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d brdmean
def f09br_f09_semi_breadth_brdmean_126d_slope_v014_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d brdmean
def f09br_f09_semi_breadth_brdmean_126d_slope_v015_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brdmean
def f09br_f09_semi_breadth_brdmean_252d_slope_v016_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brdmean
def f09br_f09_semi_breadth_brdmean_252d_slope_v017_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brdmean
def f09br_f09_semi_breadth_brdmean_252d_slope_v018_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brdmean
def f09br_f09_semi_breadth_brdmean_252d_slope_v019_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brdmean
def f09br_f09_semi_breadth_brdmean_252d_slope_v020_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _mean(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d brdz
def f09br_f09_semi_breadth_brdz_21d_slope_v021_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d brdz
def f09br_f09_semi_breadth_brdz_21d_slope_v022_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d brdz
def f09br_f09_semi_breadth_brdz_21d_slope_v023_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d brdz
def f09br_f09_semi_breadth_brdz_21d_slope_v024_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d brdz
def f09br_f09_semi_breadth_brdz_21d_slope_v025_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdz
def f09br_f09_semi_breadth_brdz_63d_slope_v026_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdz
def f09br_f09_semi_breadth_brdz_63d_slope_v027_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdz
def f09br_f09_semi_breadth_brdz_63d_slope_v028_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdz
def f09br_f09_semi_breadth_brdz_63d_slope_v029_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdz
def f09br_f09_semi_breadth_brdz_63d_slope_v030_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d brdz
def f09br_f09_semi_breadth_brdz_126d_slope_v031_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d brdz
def f09br_f09_semi_breadth_brdz_126d_slope_v032_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d brdz
def f09br_f09_semi_breadth_brdz_126d_slope_v033_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d brdz
def f09br_f09_semi_breadth_brdz_126d_slope_v034_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d brdz
def f09br_f09_semi_breadth_brdz_126d_slope_v035_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brdz
def f09br_f09_semi_breadth_brdz_252d_slope_v036_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brdz
def f09br_f09_semi_breadth_brdz_252d_slope_v037_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brdz
def f09br_f09_semi_breadth_brdz_252d_slope_v038_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brdz
def f09br_f09_semi_breadth_brdz_252d_slope_v039_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brdz
def f09br_f09_semi_breadth_brdz_252d_slope_v040_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _z(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d brddev
def f09br_f09_semi_breadth_brddev_21d_slope_v041_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d brddev
def f09br_f09_semi_breadth_brddev_21d_slope_v042_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d brddev
def f09br_f09_semi_breadth_brddev_21d_slope_v043_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d brddev
def f09br_f09_semi_breadth_brddev_21d_slope_v044_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d brddev
def f09br_f09_semi_breadth_brddev_21d_slope_v045_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brddev
def f09br_f09_semi_breadth_brddev_63d_slope_v046_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brddev
def f09br_f09_semi_breadth_brddev_63d_slope_v047_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brddev
def f09br_f09_semi_breadth_brddev_63d_slope_v048_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brddev
def f09br_f09_semi_breadth_brddev_63d_slope_v049_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brddev
def f09br_f09_semi_breadth_brddev_63d_slope_v050_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d brddev
def f09br_f09_semi_breadth_brddev_126d_slope_v051_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d brddev
def f09br_f09_semi_breadth_brddev_126d_slope_v052_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d brddev
def f09br_f09_semi_breadth_brddev_126d_slope_v053_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d brddev
def f09br_f09_semi_breadth_brddev_126d_slope_v054_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d brddev
def f09br_f09_semi_breadth_brddev_126d_slope_v055_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _mean(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d brdstd
def f09br_f09_semi_breadth_brdstd_21d_slope_v056_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d brdstd
def f09br_f09_semi_breadth_brdstd_21d_slope_v057_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d brdstd
def f09br_f09_semi_breadth_brdstd_21d_slope_v058_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d brdstd
def f09br_f09_semi_breadth_brdstd_21d_slope_v059_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d brdstd
def f09br_f09_semi_breadth_brdstd_21d_slope_v060_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdstd
def f09br_f09_semi_breadth_brdstd_63d_slope_v061_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdstd
def f09br_f09_semi_breadth_brdstd_63d_slope_v062_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdstd
def f09br_f09_semi_breadth_brdstd_63d_slope_v063_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdstd
def f09br_f09_semi_breadth_brdstd_63d_slope_v064_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdstd
def f09br_f09_semi_breadth_brdstd_63d_slope_v065_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d brdstd
def f09br_f09_semi_breadth_brdstd_126d_slope_v066_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d brdstd
def f09br_f09_semi_breadth_brdstd_126d_slope_v067_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d brdstd
def f09br_f09_semi_breadth_brdstd_126d_slope_v068_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d brdstd
def f09br_f09_semi_breadth_brdstd_126d_slope_v069_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d brdstd
def f09br_f09_semi_breadth_brdstd_126d_slope_v070_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brdstd
def f09br_f09_semi_breadth_brdstd_252d_slope_v071_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brdstd
def f09br_f09_semi_breadth_brdstd_252d_slope_v072_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brdstd
def f09br_f09_semi_breadth_brdstd_252d_slope_v073_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brdstd
def f09br_f09_semi_breadth_brdstd_252d_slope_v074_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brdstd
def f09br_f09_semi_breadth_brdstd_252d_slope_v075_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _std(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_21d_slope_v076_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_21d_slope_v077_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_21d_slope_v078_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_21d_slope_v079_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_21d_slope_v080_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_63d_slope_v081_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_63d_slope_v082_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_63d_slope_v083_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_63d_slope_v084_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_63d_slope_v085_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_126d_slope_v086_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_126d_slope_v087_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_126d_slope_v088_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_126d_slope_v089_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_126d_slope_v090_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_252d_slope_v091_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_252d_slope_v092_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_252d_slope_v093_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_252d_slope_v094_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brdthrustup
def f09br_f09_semi_breadth_brdthrustup_252d_slope_v095_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth > 0.5).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdrng
def f09br_f09_semi_breadth_brdrng_63d_slope_v096_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 63) - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdrng
def f09br_f09_semi_breadth_brdrng_63d_slope_v097_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 63) - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdrng
def f09br_f09_semi_breadth_brdrng_63d_slope_v098_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 63) - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdrng
def f09br_f09_semi_breadth_brdrng_63d_slope_v099_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 63) - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdrng
def f09br_f09_semi_breadth_brdrng_63d_slope_v100_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 63) - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d brdrng
def f09br_f09_semi_breadth_brdrng_126d_slope_v101_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 126) - _min(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d brdrng
def f09br_f09_semi_breadth_brdrng_126d_slope_v102_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 126) - _min(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d brdrng
def f09br_f09_semi_breadth_brdrng_126d_slope_v103_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 126) - _min(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d brdrng
def f09br_f09_semi_breadth_brdrng_126d_slope_v104_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 126) - _min(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d brdrng
def f09br_f09_semi_breadth_brdrng_126d_slope_v105_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 126) - _min(semi_basket_breadth, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brdrng
def f09br_f09_semi_breadth_brdrng_252d_slope_v106_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 252) - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brdrng
def f09br_f09_semi_breadth_brdrng_252d_slope_v107_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 252) - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brdrng
def f09br_f09_semi_breadth_brdrng_252d_slope_v108_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 252) - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brdrng
def f09br_f09_semi_breadth_brdrng_252d_slope_v109_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 252) - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brdrng
def f09br_f09_semi_breadth_brdrng_252d_slope_v110_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = _max(semi_basket_breadth, 252) - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdpos
def f09br_f09_semi_breadth_brdpos_63d_slope_v111_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 63)
    hi = _max(semi_basket_breadth, 63)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdpos
def f09br_f09_semi_breadth_brdpos_63d_slope_v112_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 63)
    hi = _max(semi_basket_breadth, 63)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdpos
def f09br_f09_semi_breadth_brdpos_63d_slope_v113_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 63)
    hi = _max(semi_basket_breadth, 63)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdpos
def f09br_f09_semi_breadth_brdpos_63d_slope_v114_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 63)
    hi = _max(semi_basket_breadth, 63)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdpos
def f09br_f09_semi_breadth_brdpos_63d_slope_v115_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 63)
    hi = _max(semi_basket_breadth, 63)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brdpos
def f09br_f09_semi_breadth_brdpos_252d_slope_v116_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 252)
    hi = _max(semi_basket_breadth, 252)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brdpos
def f09br_f09_semi_breadth_brdpos_252d_slope_v117_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 252)
    hi = _max(semi_basket_breadth, 252)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brdpos
def f09br_f09_semi_breadth_brdpos_252d_slope_v118_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 252)
    hi = _max(semi_basket_breadth, 252)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brdpos
def f09br_f09_semi_breadth_brdpos_252d_slope_v119_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 252)
    hi = _max(semi_basket_breadth, 252)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brdpos
def f09br_f09_semi_breadth_brdpos_252d_slope_v120_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    lo = _min(semi_basket_breadth, 252)
    hi = _max(semi_basket_breadth, 252)
    base = (semi_basket_breadth - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brddd
def f09br_f09_semi_breadth_brddd_63d_slope_v121_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brddd
def f09br_f09_semi_breadth_brddd_63d_slope_v122_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brddd
def f09br_f09_semi_breadth_brddd_63d_slope_v123_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brddd
def f09br_f09_semi_breadth_brddd_63d_slope_v124_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brddd
def f09br_f09_semi_breadth_brddd_63d_slope_v125_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brddd
def f09br_f09_semi_breadth_brddd_252d_slope_v126_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brddd
def f09br_f09_semi_breadth_brddd_252d_slope_v127_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brddd
def f09br_f09_semi_breadth_brddd_252d_slope_v128_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brddd
def f09br_f09_semi_breadth_brddd_252d_slope_v129_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brddd
def f09br_f09_semi_breadth_brddd_252d_slope_v130_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _max(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdup
def f09br_f09_semi_breadth_brdup_63d_slope_v131_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdup
def f09br_f09_semi_breadth_brdup_63d_slope_v132_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdup
def f09br_f09_semi_breadth_brdup_63d_slope_v133_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdup
def f09br_f09_semi_breadth_brdup_63d_slope_v134_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdup
def f09br_f09_semi_breadth_brdup_63d_slope_v135_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d brdup
def f09br_f09_semi_breadth_brdup_252d_slope_v136_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d brdup
def f09br_f09_semi_breadth_brdup_252d_slope_v137_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d brdup
def f09br_f09_semi_breadth_brdup_252d_slope_v138_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d brdup
def f09br_f09_semi_breadth_brdup_252d_slope_v139_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d brdup
def f09br_f09_semi_breadth_brdup_252d_slope_v140_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - _min(semi_basket_breadth, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdadv
def f09br_f09_semi_breadth_brdadv_63d_slope_v141_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth.diff() > 0).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdadv
def f09br_f09_semi_breadth_brdadv_63d_slope_v142_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth.diff() > 0).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdadv
def f09br_f09_semi_breadth_brdadv_63d_slope_v143_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth.diff() > 0).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdadv
def f09br_f09_semi_breadth_brdadv_63d_slope_v144_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth.diff() > 0).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdadv
def f09br_f09_semi_breadth_brdadv_63d_slope_v145_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = (semi_basket_breadth.diff() > 0).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d brdroc
def f09br_f09_semi_breadth_brdroc_63d_slope_v146_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - semi_basket_breadth.shift(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d brdroc
def f09br_f09_semi_breadth_brdroc_63d_slope_v147_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - semi_basket_breadth.shift(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d brdroc
def f09br_f09_semi_breadth_brdroc_63d_slope_v148_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - semi_basket_breadth.shift(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d brdroc
def f09br_f09_semi_breadth_brdroc_63d_slope_v149_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - semi_basket_breadth.shift(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d brdroc
def f09br_f09_semi_breadth_brdroc_63d_slope_v150_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    base = semi_basket_breadth - semi_basket_breadth.shift(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
