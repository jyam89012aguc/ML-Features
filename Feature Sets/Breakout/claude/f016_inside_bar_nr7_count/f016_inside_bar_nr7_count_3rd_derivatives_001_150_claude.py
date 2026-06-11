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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====

def _f016_range_z(high, low, w):
    rng = (high - low).abs()
    return _z(rng, w)


def _f016_narrow_count(high, low, w):
    rng = (high - low).abs()
    med = rng.rolling(w, min_periods=max(1, w // 2)).median()
    nr = (rng < med).astype(float)
    return nr.rolling(w, min_periods=max(1, w // 2)).sum()


def _f016_compression_count(high, low, w):
    rng = (high - low).abs()
    rmin = rng.rolling(7, min_periods=3).min()
    is_nr7 = (rng <= rmin).astype(float)
    return is_nr7.rolling(w, min_periods=max(1, w // 2)).sum()



# ===== features =====
def f016ibn_f016_inside_bar_nr7_count_p2_std126_closesq_jk126_10d_jerk_v001_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = (_std(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std21_closesma63_jk126_252d_jerk_v002_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 252)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z63_closesma63_jk21_189d_jerk_v003_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 189)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesma63_jk5_378d_jerk_v004_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 378)
    inter = (_mean(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_raw_closesma63_jk10_5d_jerk_v005_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (base) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_close_jk126_10d_jerk_v006_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = (_z(base, 126)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff21_closesq_jk10_189d_jerk_v007_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 189)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_diff63_close_jk63_378d_jerk_v008_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 378)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z252_close_jk5_42d_jerk_v009_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 42)
    inter = (_z(base, 252)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z252_close_jk42_189d_jerk_v010_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 189)
    inter = (_z(base, 252)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z126_closesma21_jk10_5d_jerk_v011_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma21_closesma63_jk10_42d_jerk_v012_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 42)
    inter = (_mean(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_diff21_closesma21_jk21_252d_jerk_v013_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 252)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z63_close_jk126_504d_jerk_v014_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 504)
    inter = (_z(base, 63)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z21_closesq_jk5_5d_jerk_v015_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z63_close_jk10_10d_jerk_v016_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 10)
    inter = (_z(base, 63)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z252_closesq_jk63_189d_jerk_v017_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 189)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesma21_jk21_5d_jerk_v018_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma21_close_jk10_504d_jerk_v019_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 504)
    inter = (_mean(base, 21)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff5_closesq_jk5_42d_jerk_v020_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 42)
    inter = ((base).diff(5)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff21_closesma63_jk5_378d_jerk_v021_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 378)
    inter = ((base).diff(21)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z126_close_jk126_378d_jerk_v022_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 378)
    inter = (_z(base, 126)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z63_closesq_jk5_21d_jerk_v023_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 21)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z63_closesma63_jk5_189d_jerk_v024_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 189)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std63_closesq_jk42_126d_jerk_v025_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 126)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff63_close_jk63_10d_jerk_v026_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std126_close_jk42_189d_jerk_v027_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 189)
    inter = (_std(base, 126)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z126_closesma63_jk42_189d_jerk_v028_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 189)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesq_jk63_5d_jerk_v029_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std126_closesma63_jk42_504d_jerk_v030_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 504)
    inter = (_std(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z252_closesq_jk21_5d_jerk_v031_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std21_closesma21_jk10_21d_jerk_v032_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 21)
    inter = (_std(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_closesq_jk63_21d_jerk_v033_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 21)
    inter = (_z(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma63_close_jk10_5d_jerk_v034_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_mean(base, 63)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk21_189d_jerk_v035_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 189)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_diff63_closesma21_jk63_504d_jerk_v036_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 504)
    inter = ((base).diff(63)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z21_closesma63_jk63_5d_jerk_v037_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma63_closesma21_jk42_252d_jerk_v038_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 252)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std126_closesq_jk21_63d_jerk_v039_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 63)
    inter = (_std(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std21_closesma63_jk63_42d_jerk_v040_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 42)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma126_close_jk126_5d_jerk_v041_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_mean(base, 126)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z252_closesma21_jk42_504d_jerk_v042_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 504)
    inter = (_z(base, 252)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std126_closesma21_jk5_252d_jerk_v043_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 252)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std21_close_jk63_63d_jerk_v044_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 63)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std63_closesma21_jk126_126d_jerk_v045_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 126)
    inter = (_std(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma63_jk10_126d_jerk_v046_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 126)
    inter = (_z(base, 252)) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_raw_close_jk21_504d_jerk_v047_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 504)
    inter = (base) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z21_close_jk63_5d_jerk_v048_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (_z(base, 21)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z21_closesma21_jk63_10d_jerk_v049_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std126_close_jk42_10d_jerk_v050_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = (_std(base, 126)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std63_closesma63_jk126_42d_jerk_v051_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 42)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff5_closesma21_jk63_378d_jerk_v052_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 378)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma63_closesma21_jk126_126d_jerk_v053_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 126)
    inter = (_mean(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff63_close_jk42_504d_jerk_v054_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 504)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std21_closesma21_jk63_252d_jerk_v055_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 252)
    inter = (_std(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff63_close_jk10_63d_jerk_v056_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 63)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma21_jk21_5d_jerk_v057_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (_z(base, 252)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_raw_closesq_jk63_126d_jerk_v058_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 126)
    inter = (base) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z252_close_jk21_42d_jerk_v059_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 42)
    inter = (_z(base, 252)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std126_closesma21_jk10_21d_jerk_v060_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 21)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff63_closesq_jk126_378d_jerk_v061_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 378)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z63_closesma21_jk42_378d_jerk_v062_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 378)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesma21_jk126_10d_jerk_v063_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff5_closesma63_jk42_10d_jerk_v064_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = ((base).diff(5)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesma21_jk42_252d_jerk_v065_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 252)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std63_closesma63_jk126_5d_jerk_v066_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma21_closesma63_jk5_5d_jerk_v067_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_mean(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma63_closesq_jk126_126d_jerk_v068_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 126)
    inter = (_mean(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff5_closesma21_jk42_42d_jerk_v069_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 42)
    inter = ((base).diff(5)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma21_jk5_5d_jerk_v070_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (_z(base, 252)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma63_jk10_252d_jerk_v071_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 252)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesma21_jk10_378d_jerk_v072_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 378)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z63_closesq_jk21_10d_jerk_v073_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_raw_closesma21_jk21_21d_jerk_v074_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 21)
    inter = (base) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk63_63d_jerk_v075_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 63)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z63_closesma63_jk5_504d_jerk_v076_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 504)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std21_closesq_jk63_378d_jerk_v077_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 378)
    inter = (_std(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff21_close_jk5_21d_jerk_v078_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 21)
    inter = ((base).diff(21)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma63_close_jk10_252d_jerk_v079_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 252)
    inter = (_mean(base, 63)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std21_close_jk10_5d_jerk_v080_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff63_close_jk21_21d_jerk_v081_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 21)
    inter = ((base).diff(63)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std126_closesma63_jk126_189d_jerk_v082_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 189)
    inter = (_std(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z63_closesq_jk21_21d_jerk_v083_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 21)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_close_jk5_63d_jerk_v084_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 63)
    inter = (_mean(base, 126)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z21_closesq_jk5_189d_jerk_v085_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 189)
    inter = (_z(base, 21)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff5_close_jk10_378d_jerk_v086_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 378)
    inter = ((base).diff(5)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesq_jk42_21d_jerk_v087_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 21)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z252_closesq_jk21_42d_jerk_v088_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 42)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma63_closesq_jk5_42d_jerk_v089_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 42)
    inter = (_mean(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma63_close_jk42_42d_jerk_v090_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 42)
    inter = (_mean(base, 63)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma21_closesma63_jk5_10d_jerk_v091_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = (_mean(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma21_jk126_252d_jerk_v092_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 252)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff21_closesq_jk126_21d_jerk_v093_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 21)
    inter = ((base).diff(21)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std21_close_jk5_5d_jerk_v094_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z63_closesq_jk63_252d_jerk_v095_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 252)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z252_closesq_jk126_10d_jerk_v096_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z252_closesq_jk63_126d_jerk_v097_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 126)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_raw_closesma21_jk10_378d_jerk_v098_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 378)
    inter = (base) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma21_close_jk5_5d_jerk_v099_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_mean(base, 21)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesma63_jk42_10d_jerk_v100_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = (_mean(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_raw_close_jk5_189d_jerk_v101_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 189)
    inter = (base) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff21_close_jk5_504d_jerk_v102_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 504)
    inter = ((base).diff(21)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_raw_close_jk10_10d_jerk_v103_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = (base) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z252_close_jk42_10d_jerk_v104_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = (_z(base, 252)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z21_closesma21_jk42_63d_jerk_v105_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 63)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z252_closesma21_jk63_252d_jerk_v106_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 252)
    inter = (_z(base, 252)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesma63_jk42_21d_jerk_v107_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 21)
    inter = (_mean(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z126_close_jk21_252d_jerk_v108_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 252)
    inter = (_z(base, 126)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma126_close_jk63_252d_jerk_v109_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 252)
    inter = (_mean(base, 126)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z63_closesma63_jk126_21d_jerk_v110_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 21)
    inter = (_z(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff63_closesq_jk21_504d_jerk_v111_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 504)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff63_closesma21_jk63_42d_jerk_v112_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 42)
    inter = ((base).diff(63)) * _mean(closeadj, 21)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma63_jk5_126d_jerk_v113_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 126)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesma21_jk10_10d_jerk_v114_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 10)
    inter = (_mean(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesma63_jk5_63d_jerk_v115_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 63)
    inter = (_mean(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma63_jk63_378d_jerk_v116_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 378)
    inter = (_z(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z63_close_jk42_5d_jerk_v117_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_z(base, 63)) * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk63_5d_jerk_v118_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std21_closesma63_jk63_10d_jerk_v119_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 10)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff21_closesma21_jk42_252d_jerk_v120_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 252)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma21_closesma63_jk10_126d_jerk_v121_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 126)
    inter = (_mean(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std126_closesma21_jk10_10d_jerk_v122_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = (_std(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z21_closesma21_jk126_189d_jerk_v123_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 189)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma21_jk21_378d_jerk_v124_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 378)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std63_closesq_jk63_63d_jerk_v125_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 63)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std21_closesma63_jk42_504d_jerk_v126_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 504)
    inter = (_std(base, 21)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z21_closesma21_jk126_10d_jerk_v127_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 10)
    inter = (_z(base, 21)) * _mean(closeadj, 21)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_close_jk126_5d_jerk_v128_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 5)
    inter = (_mean(base, 126)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_sma63_close_jk10_42d_jerk_v129_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 42)
    inter = (_mean(base, 63)) * closeadj
    result = _jerk(inter, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z21_close_jk126_21d_jerk_v130_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 21)
    inter = (_z(base, 21)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z252_closesq_jk42_21d_jerk_v131_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 21)
    inter = (_z(base, 252)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_std21_close_jk5_126d_jerk_v132_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 126)
    inter = (_std(base, 21)) * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff21_closesma21_jk21_378d_jerk_v133_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 378)
    inter = ((base).diff(21)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_std126_close_jk126_5d_jerk_v134_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_std(base, 126)) * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk42_5d_jerk_v135_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_z(base, 126)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std63_closesma63_jk5_504d_jerk_v136_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 504)
    inter = (_std(base, 63)) * _mean(closeadj, 63)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std63_closesq_jk126_252d_jerk_v137_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 252)
    inter = (_std(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesq_jk63_189d_jerk_v138_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 189)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesq_jk5_5d_jerk_v139_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 5)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesq_jk5_10d_jerk_v140_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = (_mean(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma126_close_jk21_252d_jerk_v141_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 252)
    inter = (_mean(base, 126)) * closeadj
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p3_z63_closesq_jk126_5d_jerk_v142_signal(high, low, closeadj):
    base = _f016_compression_count(high, low, 5)
    inter = (_z(base, 63)) * closeadj * closeadj
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_diff63_closesq_jk42_189d_jerk_v143_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 189)
    inter = ((base).diff(63)) * closeadj * closeadj
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_sma63_close_jk63_126d_jerk_v144_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 126)
    inter = (_mean(base, 63)) * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z126_closesq_jk63_63d_jerk_v145_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 63)
    inter = (_z(base, 126)) * closeadj * closeadj
    result = _jerk(inter, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z126_closesma21_jk5_126d_jerk_v146_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 126)
    inter = (_z(base, 126)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_std63_closesma21_jk5_378d_jerk_v147_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 378)
    inter = (_std(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma63_jk42_378d_jerk_v148_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 378)
    inter = (_z(base, 252)) * _mean(closeadj, 63)
    result = _jerk(inter, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p2_diff63_closesma63_jk126_10d_jerk_v149_signal(high, low, closeadj):
    base = _f016_narrow_count(high, low, 10)
    inter = ((base).diff(63)) * _mean(closeadj, 63)
    result = _jerk(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f016ibn_f016_inside_bar_nr7_count_p1_z63_closesma21_jk21_63d_jerk_v150_signal(high, low, closeadj):
    base = _f016_range_z(high, low, 63)
    inter = (_z(base, 63)) * _mean(closeadj, 21)
    result = _jerk(inter, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f016ibn_f016_inside_bar_nr7_count_p2_std126_closesq_jk126_10d_jerk_v001_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std21_closesma63_jk126_252d_jerk_v002_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z63_closesma63_jk21_189d_jerk_v003_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesma63_jk5_378d_jerk_v004_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_raw_closesma63_jk10_5d_jerk_v005_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_close_jk126_10d_jerk_v006_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff21_closesq_jk10_189d_jerk_v007_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_diff63_close_jk63_378d_jerk_v008_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z252_close_jk5_42d_jerk_v009_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z252_close_jk42_189d_jerk_v010_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z126_closesma21_jk10_5d_jerk_v011_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma21_closesma63_jk10_42d_jerk_v012_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_diff21_closesma21_jk21_252d_jerk_v013_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z63_close_jk126_504d_jerk_v014_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z21_closesq_jk5_5d_jerk_v015_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z63_close_jk10_10d_jerk_v016_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z252_closesq_jk63_189d_jerk_v017_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesma21_jk21_5d_jerk_v018_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma21_close_jk10_504d_jerk_v019_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff5_closesq_jk5_42d_jerk_v020_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff21_closesma63_jk5_378d_jerk_v021_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z126_close_jk126_378d_jerk_v022_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z63_closesq_jk5_21d_jerk_v023_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z63_closesma63_jk5_189d_jerk_v024_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std63_closesq_jk42_126d_jerk_v025_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff63_close_jk63_10d_jerk_v026_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std126_close_jk42_189d_jerk_v027_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z126_closesma63_jk42_189d_jerk_v028_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesq_jk63_5d_jerk_v029_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std126_closesma63_jk42_504d_jerk_v030_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z252_closesq_jk21_5d_jerk_v031_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std21_closesma21_jk10_21d_jerk_v032_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_closesq_jk63_21d_jerk_v033_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma63_close_jk10_5d_jerk_v034_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk21_189d_jerk_v035_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_diff63_closesma21_jk63_504d_jerk_v036_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z21_closesma63_jk63_5d_jerk_v037_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma63_closesma21_jk42_252d_jerk_v038_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std126_closesq_jk21_63d_jerk_v039_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std21_closesma63_jk63_42d_jerk_v040_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma126_close_jk126_5d_jerk_v041_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z252_closesma21_jk42_504d_jerk_v042_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std126_closesma21_jk5_252d_jerk_v043_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std21_close_jk63_63d_jerk_v044_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std63_closesma21_jk126_126d_jerk_v045_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma63_jk10_126d_jerk_v046_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_raw_close_jk21_504d_jerk_v047_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z21_close_jk63_5d_jerk_v048_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z21_closesma21_jk63_10d_jerk_v049_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std126_close_jk42_10d_jerk_v050_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std63_closesma63_jk126_42d_jerk_v051_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff5_closesma21_jk63_378d_jerk_v052_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma63_closesma21_jk126_126d_jerk_v053_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff63_close_jk42_504d_jerk_v054_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std21_closesma21_jk63_252d_jerk_v055_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff63_close_jk10_63d_jerk_v056_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma21_jk21_5d_jerk_v057_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_raw_closesq_jk63_126d_jerk_v058_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z252_close_jk21_42d_jerk_v059_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std126_closesma21_jk10_21d_jerk_v060_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff63_closesq_jk126_378d_jerk_v061_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z63_closesma21_jk42_378d_jerk_v062_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesma21_jk126_10d_jerk_v063_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff5_closesma63_jk42_10d_jerk_v064_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesma21_jk42_252d_jerk_v065_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std63_closesma63_jk126_5d_jerk_v066_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma21_closesma63_jk5_5d_jerk_v067_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma63_closesq_jk126_126d_jerk_v068_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff5_closesma21_jk42_42d_jerk_v069_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma21_jk5_5d_jerk_v070_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma63_jk10_252d_jerk_v071_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesma21_jk10_378d_jerk_v072_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z63_closesq_jk21_10d_jerk_v073_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_raw_closesma21_jk21_21d_jerk_v074_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk63_63d_jerk_v075_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z63_closesma63_jk5_504d_jerk_v076_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std21_closesq_jk63_378d_jerk_v077_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff21_close_jk5_21d_jerk_v078_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma63_close_jk10_252d_jerk_v079_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std21_close_jk10_5d_jerk_v080_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff63_close_jk21_21d_jerk_v081_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std126_closesma63_jk126_189d_jerk_v082_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z63_closesq_jk21_21d_jerk_v083_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_close_jk5_63d_jerk_v084_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z21_closesq_jk5_189d_jerk_v085_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff5_close_jk10_378d_jerk_v086_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesq_jk42_21d_jerk_v087_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z252_closesq_jk21_42d_jerk_v088_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma63_closesq_jk5_42d_jerk_v089_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma63_close_jk42_42d_jerk_v090_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma21_closesma63_jk5_10d_jerk_v091_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma21_jk126_252d_jerk_v092_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff21_closesq_jk126_21d_jerk_v093_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std21_close_jk5_5d_jerk_v094_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z63_closesq_jk63_252d_jerk_v095_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z252_closesq_jk126_10d_jerk_v096_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z252_closesq_jk63_126d_jerk_v097_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_raw_closesma21_jk10_378d_jerk_v098_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma21_close_jk5_5d_jerk_v099_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesma63_jk42_10d_jerk_v100_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_raw_close_jk5_189d_jerk_v101_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff21_close_jk5_504d_jerk_v102_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_raw_close_jk10_10d_jerk_v103_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z252_close_jk42_10d_jerk_v104_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z21_closesma21_jk42_63d_jerk_v105_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z252_closesma21_jk63_252d_jerk_v106_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesma63_jk42_21d_jerk_v107_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z126_close_jk21_252d_jerk_v108_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma126_close_jk63_252d_jerk_v109_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z63_closesma63_jk126_21d_jerk_v110_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff63_closesq_jk21_504d_jerk_v111_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff63_closesma21_jk63_42d_jerk_v112_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma63_jk5_126d_jerk_v113_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesma21_jk10_10d_jerk_v114_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma126_closesma63_jk5_63d_jerk_v115_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z21_closesma63_jk63_378d_jerk_v116_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z63_close_jk42_5d_jerk_v117_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk63_5d_jerk_v118_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std21_closesma63_jk63_10d_jerk_v119_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff21_closesma21_jk42_252d_jerk_v120_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma21_closesma63_jk10_126d_jerk_v121_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std126_closesma21_jk10_10d_jerk_v122_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z21_closesma21_jk126_189d_jerk_v123_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma21_jk21_378d_jerk_v124_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std63_closesq_jk63_63d_jerk_v125_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std21_closesma63_jk42_504d_jerk_v126_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z21_closesma21_jk126_10d_jerk_v127_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_close_jk126_5d_jerk_v128_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_sma63_close_jk10_42d_jerk_v129_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z21_close_jk126_21d_jerk_v130_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z252_closesq_jk42_21d_jerk_v131_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_std21_close_jk5_126d_jerk_v132_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff21_closesma21_jk21_378d_jerk_v133_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_std126_close_jk126_5d_jerk_v134_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_closesma63_jk42_5d_jerk_v135_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std63_closesma63_jk5_504d_jerk_v136_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std63_closesq_jk126_252d_jerk_v137_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesq_jk63_189d_jerk_v138_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_sma126_closesq_jk5_5d_jerk_v139_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_closesq_jk5_10d_jerk_v140_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma126_close_jk21_252d_jerk_v141_signal,
    f016ibn_f016_inside_bar_nr7_count_p3_z63_closesq_jk126_5d_jerk_v142_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_diff63_closesq_jk42_189d_jerk_v143_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_sma63_close_jk63_126d_jerk_v144_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z126_closesq_jk63_63d_jerk_v145_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z126_closesma21_jk5_126d_jerk_v146_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_std63_closesma21_jk5_378d_jerk_v147_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_z252_closesma63_jk42_378d_jerk_v148_signal,
    f016ibn_f016_inside_bar_nr7_count_p2_diff63_closesma63_jk126_10d_jerk_v149_signal,
    f016ibn_f016_inside_bar_nr7_count_p1_z63_closesma21_jk21_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F016_INSIDE_BAR_NR7_COUNT_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f016_range_z', '_f016_narrow_count', '_f016_compression_count')
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
    print(f"OK f016_inside_bar_nr7_count_3rd_derivatives_001_150_claude: {n_features} features pass")
