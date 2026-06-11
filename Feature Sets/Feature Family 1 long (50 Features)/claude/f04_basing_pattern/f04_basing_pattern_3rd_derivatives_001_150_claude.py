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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f04_basing_range(close, w):
    rmax = close.rolling(w, min_periods=max(1, w // 2)).max()
    rmin = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (rmax - rmin) / close.replace(0, np.nan).abs()


def _f04_basing_height(close, w):
    mid = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return (close - mid) / mid.replace(0, np.nan).abs()


def _f04_consolidation_atr(high, low, close, w):
    rng = (high - low) / close.replace(0, np.nan).abs()
    return rng.rolling(w, min_periods=max(1, w // 2)).mean()


# 5d jerk of 21d basing range
def f04bp_f04_basing_pattern_rangetight_21d_jerk_v001_signal(closeadj):
    base = _f04_basing_range(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d basing range
def f04bp_f04_basing_pattern_rangetight_21d_jerk_v002_signal(closeadj):
    base = _f04_basing_range(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 63d basing range
def f04bp_f04_basing_pattern_rangetight_63d_jerk_v003_signal(closeadj):
    base = _f04_basing_range(closeadj, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d basing range
def f04bp_f04_basing_pattern_rangetight_63d_jerk_v004_signal(closeadj):
    base = _f04_basing_range(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d basing range
def f04bp_f04_basing_pattern_rangetight_63d_jerk_v005_signal(closeadj):
    base = _f04_basing_range(closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d basing range
def f04bp_f04_basing_pattern_rangetight_126d_jerk_v006_signal(closeadj):
    base = _f04_basing_range(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d basing range
def f04bp_f04_basing_pattern_rangetight_126d_jerk_v007_signal(closeadj):
    base = _f04_basing_range(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d basing range
def f04bp_f04_basing_pattern_rangetight_252d_jerk_v008_signal(closeadj):
    base = _f04_basing_range(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d basing range
def f04bp_f04_basing_pattern_rangetight_252d_jerk_v009_signal(closeadj):
    base = _f04_basing_range(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d basing range
def f04bp_f04_basing_pattern_rangetight_504d_jerk_v010_signal(closeadj):
    base = _f04_basing_range(closeadj, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d basing range
def f04bp_f04_basing_pattern_rangetight_504d_jerk_v011_signal(closeadj):
    base = _f04_basing_range(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d basing range
def f04bp_f04_basing_pattern_rangetight_5d_jerk_v012_signal(closeadj):
    base = _f04_basing_range(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 10d basing range
def f04bp_f04_basing_pattern_rangetight_10d_jerk_v013_signal(closeadj):
    base = _f04_basing_range(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d basing range
def f04bp_f04_basing_pattern_rangetight_42d_jerk_v014_signal(closeadj):
    base = _f04_basing_range(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 189d basing range
def f04bp_f04_basing_pattern_rangetight_189d_jerk_v015_signal(closeadj):
    base = _f04_basing_range(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 378d basing range
def f04bp_f04_basing_pattern_rangetight_378d_jerk_v016_signal(closeadj):
    base = _f04_basing_range(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d-mean of 63d basing range
def f04bp_f04_basing_pattern_rangemean_63d_jerk_v017_signal(closeadj):
    base = _mean(_f04_basing_range(closeadj, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d-mean of 252d basing range
def f04bp_f04_basing_pattern_rangemean_252d_jerk_v018_signal(closeadj):
    base = _mean(_f04_basing_range(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d-mean of 504d basing range
def f04bp_f04_basing_pattern_rangemean_504d_jerk_v019_signal(closeadj):
    base = _mean(_f04_basing_range(closeadj, 504), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d-std of 63d basing range
def f04bp_f04_basing_pattern_rangestd_63d_jerk_v020_signal(closeadj):
    base = _std(_f04_basing_range(closeadj, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d-std of 252d basing range
def f04bp_f04_basing_pattern_rangestd_252d_jerk_v021_signal(closeadj):
    base = _std(_f04_basing_range(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d-std of 504d basing range
def f04bp_f04_basing_pattern_rangestd_504d_jerk_v022_signal(closeadj):
    base = _std(_f04_basing_range(closeadj, 504), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d zscore of 21d basing range
def f04bp_f04_basing_pattern_rangez_21d_jerk_v023_signal(closeadj):
    base = _z(_f04_basing_range(closeadj, 21), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d zscore of 63d basing range
def f04bp_f04_basing_pattern_rangez_63d_jerk_v024_signal(closeadj):
    base = _z(_f04_basing_range(closeadj, 63), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d zscore of 252d basing range
def f04bp_f04_basing_pattern_rangez_252d_jerk_v025_signal(closeadj):
    base = _z(_f04_basing_range(closeadj, 252), 504)
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v252 basing range ratio
def f04bp_f04_basing_pattern_rangeratio_21v252_jerk_v026_signal(closeadj):
    a = _f04_basing_range(closeadj, 21)
    b = _f04_basing_range(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63v252 basing range ratio
def f04bp_f04_basing_pattern_rangeratio_63v252_jerk_v027_signal(closeadj):
    a = _f04_basing_range(closeadj, 63)
    b = _f04_basing_range(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126v504 basing range ratio
def f04bp_f04_basing_pattern_rangeratio_126v504_jerk_v028_signal(closeadj):
    a = _f04_basing_range(closeadj, 126)
    b = _f04_basing_range(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d-63d basing range diff
def f04bp_f04_basing_pattern_rangediff_21m63_jerk_v029_signal(closeadj):
    base = (_f04_basing_range(closeadj, 21) - _f04_basing_range(closeadj, 63)) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d-252d basing range diff
def f04bp_f04_basing_pattern_rangediff_63m252_jerk_v030_signal(closeadj):
    base = (_f04_basing_range(closeadj, 63) - _f04_basing_range(closeadj, 252)) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d-504d basing range diff
def f04bp_f04_basing_pattern_rangediff_252m504_jerk_v031_signal(closeadj):
    base = (_f04_basing_range(closeadj, 252) - _f04_basing_range(closeadj, 504)) * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d basing height × price
def f04bp_f04_basing_pattern_height_21d_jerk_v032_signal(closeadj):
    base = _f04_basing_height(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d basing height × price
def f04bp_f04_basing_pattern_height_63d_jerk_v033_signal(closeadj):
    base = _f04_basing_height(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d basing height
def f04bp_f04_basing_pattern_height_126d_jerk_v034_signal(closeadj):
    base = _f04_basing_height(closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d basing height
def f04bp_f04_basing_pattern_height_252d_jerk_v035_signal(closeadj):
    base = _f04_basing_height(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d basing height
def f04bp_f04_basing_pattern_height_504d_jerk_v036_signal(closeadj):
    base = _f04_basing_height(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d abs basing height
def f04bp_f04_basing_pattern_absheight_21d_jerk_v037_signal(closeadj):
    base = _f04_basing_height(closeadj, 21).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d abs basing height
def f04bp_f04_basing_pattern_absheight_63d_jerk_v038_signal(closeadj):
    base = _f04_basing_height(closeadj, 63).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d abs basing height
def f04bp_f04_basing_pattern_absheight_252d_jerk_v039_signal(closeadj):
    base = _f04_basing_height(closeadj, 252).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d height squared
def f04bp_f04_basing_pattern_heightsq_21d_jerk_v040_signal(closeadj):
    h = _f04_basing_height(closeadj, 21)
    base = h * h.abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height squared
def f04bp_f04_basing_pattern_heightsq_63d_jerk_v041_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    base = h * h.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d height squared
def f04bp_f04_basing_pattern_heightsq_252d_jerk_v042_signal(closeadj):
    h = _f04_basing_height(closeadj, 252)
    base = h * h.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of basing height z (21d window)
def f04bp_f04_basing_pattern_heightz_21d_jerk_v043_signal(closeadj):
    base = _z(_f04_basing_height(closeadj, 21), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of basing height z (63d window)
def f04bp_f04_basing_pattern_heightz_63d_jerk_v044_signal(closeadj):
    base = _z(_f04_basing_height(closeadj, 63), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of basing height z (252d window)
def f04bp_f04_basing_pattern_heightz_252d_jerk_v045_signal(closeadj):
    base = _z(_f04_basing_height(closeadj, 252), 504)
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d height std
def f04bp_f04_basing_pattern_heightstd_21d_jerk_v046_signal(closeadj):
    base = _std(_f04_basing_height(closeadj, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height std
def f04bp_f04_basing_pattern_heightstd_63d_jerk_v047_signal(closeadj):
    base = _std(_f04_basing_height(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d height std
def f04bp_f04_basing_pattern_heightstd_252d_jerk_v048_signal(closeadj):
    base = _std(_f04_basing_height(closeadj, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ATR contraction
def f04bp_f04_basing_pattern_atrcontract_21d_jerk_v049_signal(closeadj, high, low):
    base = _f04_consolidation_atr(high, low, closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ATR
def f04bp_f04_basing_pattern_atrcontract_21d_jerk_v050_signal(closeadj, high, low):
    base = _f04_consolidation_atr(high, low, closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR
def f04bp_f04_basing_pattern_atrcontract_63d_jerk_v051_signal(closeadj, high, low):
    base = _f04_consolidation_atr(high, low, closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ATR
def f04bp_f04_basing_pattern_atrcontract_63d_jerk_v052_signal(closeadj, high, low):
    base = _f04_consolidation_atr(high, low, closeadj, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d ATR
def f04bp_f04_basing_pattern_atrcontract_126d_jerk_v053_signal(closeadj, high, low):
    base = _f04_consolidation_atr(high, low, closeadj, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ATR
def f04bp_f04_basing_pattern_atrcontract_252d_jerk_v054_signal(closeadj, high, low):
    base = _f04_consolidation_atr(high, low, closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ATR
def f04bp_f04_basing_pattern_atrcontract_504d_jerk_v055_signal(closeadj, high, low):
    base = _f04_consolidation_atr(high, low, closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v252 ATR ratio
def f04bp_f04_basing_pattern_atrratio_21v252_jerk_v056_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 21)
    b = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63v252 ATR ratio
def f04bp_f04_basing_pattern_atrratio_63v252_jerk_v057_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 63)
    b = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126v504 ATR ratio
def f04bp_f04_basing_pattern_atrratio_126v504_jerk_v058_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 126)
    b = _f04_consolidation_atr(high, low, closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ATR diff (21-63)
def f04bp_f04_basing_pattern_atrdiff_21m63_jerk_v059_signal(closeadj, high, low):
    base = (_f04_consolidation_atr(high, low, closeadj, 21) - _f04_consolidation_atr(high, low, closeadj, 63)) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ATR diff (63-252)
def f04bp_f04_basing_pattern_atrdiff_63m252_jerk_v060_signal(closeadj, high, low):
    base = (_f04_consolidation_atr(high, low, closeadj, 63) - _f04_consolidation_atr(high, low, closeadj, 252)) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ATR diff (252-504)
def f04bp_f04_basing_pattern_atrdiff_252m504_jerk_v061_signal(closeadj, high, low):
    base = (_f04_consolidation_atr(high, low, closeadj, 252) - _f04_consolidation_atr(high, low, closeadj, 504)) * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ATR z
def f04bp_f04_basing_pattern_atrz_21d_jerk_v062_signal(closeadj, high, low):
    base = _z(_f04_consolidation_atr(high, low, closeadj, 21), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR z
def f04bp_f04_basing_pattern_atrz_63d_jerk_v063_signal(closeadj, high, low):
    base = _z(_f04_consolidation_atr(high, low, closeadj, 63), 252)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ATR z
def f04bp_f04_basing_pattern_atrz_252d_jerk_v064_signal(closeadj, high, low):
    base = _z(_f04_consolidation_atr(high, low, closeadj, 252), 504)
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d basing range × ATR
def f04bp_f04_basing_pattern_rangexatr_21d_jerk_v065_signal(closeadj, high, low):
    base = _f04_basing_range(closeadj, 21) * _f04_consolidation_atr(high, low, closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d basing range × ATR
def f04bp_f04_basing_pattern_rangexatr_63d_jerk_v066_signal(closeadj, high, low):
    base = _f04_basing_range(closeadj, 63) * _f04_consolidation_atr(high, low, closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d basing range × ATR
def f04bp_f04_basing_pattern_rangexatr_252d_jerk_v067_signal(closeadj, high, low):
    base = _f04_basing_range(closeadj, 252) * _f04_consolidation_atr(high, low, closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of narrow-count over 252d
def f04bp_f04_basing_pattern_narrowcount_252d_jerk_v068_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 21) < 0.05).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * (1.0 + closeadj * 0.001)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of narrow-count over 504d (relaxed threshold)
def f04bp_f04_basing_pattern_narrowcount_504d_jerk_v069_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 63) < 0.30).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of narrow-count 15pct
def f04bp_f04_basing_pattern_narrowcount_15pct_jerk_v070_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 63) < 0.15).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * (1.0 + closeadj * 0.001)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range/ATR ratio
def f04bp_f04_basing_pattern_rangepatratio_21d_jerk_v071_signal(closeadj, high, low):
    a = _f04_basing_range(closeadj, 21)
    b = _f04_consolidation_atr(high, low, closeadj, 21).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range/ATR
def f04bp_f04_basing_pattern_rangepatratio_63d_jerk_v072_signal(closeadj, high, low):
    a = _f04_basing_range(closeadj, 63)
    b = _f04_consolidation_atr(high, low, closeadj, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range/ATR
def f04bp_f04_basing_pattern_rangepatratio_252d_jerk_v073_signal(closeadj, high, low):
    a = _f04_basing_range(closeadj, 252)
    b = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d EMA of basing range
def f04bp_f04_basing_pattern_rangeema_21d_jerk_v074_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    base = r.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EMA of basing range
def f04bp_f04_basing_pattern_rangeema_63d_jerk_v075_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    base = r.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EMA of basing range
def f04bp_f04_basing_pattern_rangeema_252d_jerk_v076_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    base = r.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d basing range × volume
def f04bp_f04_basing_pattern_rangexvol_21d_jerk_v077_signal(closeadj, volume):
    base = _f04_basing_range(closeadj, 21) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d basing range × volume
def f04bp_f04_basing_pattern_rangexvol_63d_jerk_v078_signal(closeadj, volume):
    base = _f04_basing_range(closeadj, 63) * volume
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d basing range × dollar volume
def f04bp_f04_basing_pattern_rangexdv_252d_jerk_v079_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f04_basing_range(closeadj, 252) * _mean(dv, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d height/ATR ratio
def f04bp_f04_basing_pattern_heightvsatr_21d_jerk_v080_signal(closeadj, high, low):
    h = _f04_basing_height(closeadj, 21)
    a = _f04_consolidation_atr(high, low, closeadj, 21).replace(0, np.nan)
    base = (h / a) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height/ATR
def f04bp_f04_basing_pattern_heightvsatr_63d_jerk_v081_signal(closeadj, high, low):
    h = _f04_basing_height(closeadj, 63)
    a = _f04_consolidation_atr(high, low, closeadj, 63).replace(0, np.nan)
    base = (h / a) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d height/ATR
def f04bp_f04_basing_pattern_heightvsatr_252d_jerk_v082_signal(closeadj, high, low):
    h = _f04_basing_height(closeadj, 252)
    a = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    base = (h / a) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d composite tightness
def f04bp_f04_basing_pattern_basetightcomp_252d_jerk_v083_signal(closeadj, high, low):
    r = _f04_basing_range(closeadj, 252)
    a = _f04_consolidation_atr(high, low, closeadj, 252)
    base = (r + a) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × return volatility
def f04bp_f04_basing_pattern_rangexrv_21d_jerk_v084_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f04_basing_range(closeadj, 21) * rv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range × rv
def f04bp_f04_basing_pattern_rangexrv_63d_jerk_v085_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f04_basing_range(closeadj, 63) * rv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range × rv
def f04bp_f04_basing_pattern_rangexrv_252d_jerk_v086_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f04_basing_range(closeadj, 252) * rv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range / rv
def f04bp_f04_basing_pattern_rangedivrv_21d_jerk_v087_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    base = (_f04_basing_range(closeadj, 21) / rv) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range / rv
def f04bp_f04_basing_pattern_rangedivrv_63d_jerk_v088_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = (_f04_basing_range(closeadj, 63) / rv) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range / rv
def f04bp_f04_basing_pattern_rangedivrv_252d_jerk_v089_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = (_f04_basing_range(closeadj, 252) / rv) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ATR / rv
def f04bp_f04_basing_pattern_atrdivrv_21d_jerk_v090_signal(closeadj, high, low):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    base = (_f04_consolidation_atr(high, low, closeadj, 21) / rv) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR / rv
def f04bp_f04_basing_pattern_atrdivrv_63d_jerk_v091_signal(closeadj, high, low):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = (_f04_consolidation_atr(high, low, closeadj, 63) / rv) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × skewness
def f04bp_f04_basing_pattern_rangexskew_63d_jerk_v092_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f04_basing_range(closeadj, 21) * sk * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d range × kurt
def f04bp_f04_basing_pattern_rangexkurt_252d_jerk_v093_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f04_basing_range(closeadj, 63) * kt * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d height × skew
def f04bp_f04_basing_pattern_heightxskew_252d_jerk_v094_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f04_basing_height(closeadj, 252) * sk * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d height/range
def f04bp_f04_basing_pattern_heightoverrange_21d_jerk_v095_signal(closeadj):
    h = _f04_basing_height(closeadj, 21)
    r = _f04_basing_range(closeadj, 21).replace(0, np.nan)
    base = (h / r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height/range
def f04bp_f04_basing_pattern_heightoverrange_63d_jerk_v096_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    r = _f04_basing_range(closeadj, 63).replace(0, np.nan)
    base = (h / r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d height/range
def f04bp_f04_basing_pattern_heightoverrange_252d_jerk_v097_signal(closeadj):
    h = _f04_basing_height(closeadj, 252)
    r = _f04_basing_range(closeadj, 252).replace(0, np.nan)
    base = (h / r) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × abs height
def f04bp_f04_basing_pattern_rangexabsheight_21d_jerk_v098_signal(closeadj):
    base = _f04_basing_range(closeadj, 21) * _f04_basing_height(closeadj, 21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range × abs height
def f04bp_f04_basing_pattern_rangexabsheight_63d_jerk_v099_signal(closeadj):
    base = _f04_basing_range(closeadj, 63) * _f04_basing_height(closeadj, 63).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range × abs height
def f04bp_f04_basing_pattern_rangexabsheight_252d_jerk_v100_signal(closeadj):
    base = _f04_basing_range(closeadj, 252) * _f04_basing_height(closeadj, 252).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of range vs 252d min
def f04bp_f04_basing_pattern_rangevsmin_252d_jerk_v101_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    rmin = r.rolling(252, min_periods=63).min()
    base = (r - rmin) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of range vs 504d min
def f04bp_f04_basing_pattern_rangevsmin_504d_jerk_v102_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    rmin = r.rolling(504, min_periods=126).min()
    base = (r - rmin) * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range vs 504d max
def f04bp_f04_basing_pattern_rangepctmax_504d_jerk_v103_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    rmax = r.rolling(504, min_periods=126).max().replace(0, np.nan)
    base = (r / rmax) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range vs 252d max
def f04bp_f04_basing_pattern_rangepctmax_252d_jerk_v104_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    rmax = r.rolling(252, min_periods=63).max().replace(0, np.nan)
    base = (r / rmax) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding tightest base
def f04bp_f04_basing_pattern_tightestever_jerk_v105_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    base = r.expanding(min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of range vs hist tight
def f04bp_f04_basing_pattern_rangevshisttight_jerk_v106_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    tight = r.expanding(min_periods=63).min()
    base = (r - tight) * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d days-within-narrow
def f04bp_f04_basing_pattern_dayswithinnarrow_63d_jerk_v107_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 21) < 0.10).astype(float)
    base = flag.rolling(63, min_periods=21).sum() * (1.0 + closeadj * 0.001)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d days-within-narrow
def f04bp_f04_basing_pattern_dayswithinnarrow_252d_jerk_v108_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 21) < 0.07).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * (1.0 + closeadj * 0.001)
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d days-within-narrow
def f04bp_f04_basing_pattern_dayswithinnarrow_504d_jerk_v109_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 63) < 0.28).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × current dollar volume
def f04bp_f04_basing_pattern_rangexcurdv_21d_jerk_v110_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f04_basing_range(closeadj, 21) * dv
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range × dollar volume
def f04bp_f04_basing_pattern_rangexcurdv_63d_jerk_v111_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f04_basing_range(closeadj, 63) * dv
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range × dollar volume
def f04bp_f04_basing_pattern_rangexcurdv_252d_jerk_v112_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f04_basing_range(closeadj, 252) * dv
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × volume z
def f04bp_f04_basing_pattern_rangexvolz_21d_jerk_v113_signal(closeadj, volume):
    base = _f04_basing_range(closeadj, 21) * _z(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range × volume z
def f04bp_f04_basing_pattern_rangexvolz_63d_jerk_v114_signal(closeadj, volume):
    base = _f04_basing_range(closeadj, 63) * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range × volume z
def f04bp_f04_basing_pattern_rangexvolz_252d_jerk_v115_signal(closeadj, volume):
    base = _f04_basing_range(closeadj, 252) * _z(volume, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ATR × volume z
def f04bp_f04_basing_pattern_atrxvolz_21d_jerk_v116_signal(closeadj, high, low, volume):
    base = _f04_consolidation_atr(high, low, closeadj, 21) * _z(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR × volume z
def f04bp_f04_basing_pattern_atrxvolz_63d_jerk_v117_signal(closeadj, high, low, volume):
    base = _f04_consolidation_atr(high, low, closeadj, 63) * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ATR × dollar volume
def f04bp_f04_basing_pattern_atrxdv_252d_jerk_v118_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f04_consolidation_atr(high, low, closeadj, 252) * _mean(dv, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ATR EMA
def f04bp_f04_basing_pattern_atrema_21d_jerk_v119_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 21)
    base = a.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR EMA
def f04bp_f04_basing_pattern_atrema_63d_jerk_v120_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 63)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ATR EMA
def f04bp_f04_basing_pattern_atrema_252d_jerk_v121_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 252)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d height EMA
def f04bp_f04_basing_pattern_heightema_21d_jerk_v122_signal(closeadj):
    h = _f04_basing_height(closeadj, 21)
    base = h.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height EMA
def f04bp_f04_basing_pattern_heightema_63d_jerk_v123_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    base = h.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d height EMA
def f04bp_f04_basing_pattern_heightema_252d_jerk_v124_signal(closeadj):
    h = _f04_basing_height(closeadj, 252)
    base = h.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range area
def f04bp_f04_basing_pattern_rangearea_63d_jerk_v125_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    base = r.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range area
def f04bp_f04_basing_pattern_rangearea_252d_jerk_v126_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    base = r.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d range area
def f04bp_f04_basing_pattern_rangearea_504d_jerk_v127_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    base = r.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × 21d return
def f04bp_f04_basing_pattern_rangexret_21d_jerk_v128_signal(closeadj):
    r21 = closeadj.pct_change(21)
    base = _f04_basing_range(closeadj, 21) * r21 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range × return
def f04bp_f04_basing_pattern_rangexret_63d_jerk_v129_signal(closeadj):
    r63 = closeadj.pct_change(63)
    base = _f04_basing_range(closeadj, 63) * r63 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range × return
def f04bp_f04_basing_pattern_rangexret_252d_jerk_v130_signal(closeadj):
    r252 = closeadj.pct_change(252)
    base = _f04_basing_range(closeadj, 252) * r252 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d height × return
def f04bp_f04_basing_pattern_heightxret_21d_jerk_v131_signal(closeadj):
    r21 = closeadj.pct_change(21)
    base = _f04_basing_height(closeadj, 21) * r21 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height × return
def f04bp_f04_basing_pattern_heightxret_63d_jerk_v132_signal(closeadj):
    r63 = closeadj.pct_change(63)
    base = _f04_basing_height(closeadj, 63) * r63 * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d height × return
def f04bp_f04_basing_pattern_heightxret_252d_jerk_v133_signal(closeadj):
    r252 = closeadj.pct_change(252)
    base = _f04_basing_height(closeadj, 252) * r252 * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × log price
def f04bp_f04_basing_pattern_rangexlog_21d_jerk_v134_signal(closeadj):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f04_basing_range(closeadj, 21) * lg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range × log
def f04bp_f04_basing_pattern_rangexlog_63d_jerk_v135_signal(closeadj):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f04_basing_range(closeadj, 63) * lg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ATR × log
def f04bp_f04_basing_pattern_atrxlog_21d_jerk_v136_signal(closeadj, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    base = _f04_consolidation_atr(high, low, closeadj, 21) * lg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of range deviation from EMA
def f04bp_f04_basing_pattern_rangedevema_63d_jerk_v137_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    e = r.ewm(span=252, adjust=False).mean()
    base = (r - e) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range dev EMA
def f04bp_f04_basing_pattern_rangedevema_252d_jerk_v138_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    e = r.ewm(span=504, adjust=False).mean()
    base = (r - e) * closeadj
    result = _diff(_diff(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height dev EMA
def f04bp_f04_basing_pattern_heightdevema_63d_jerk_v139_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    e = h.ewm(span=252, adjust=False).mean()
    base = (h - e) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ATR dev EMA
def f04bp_f04_basing_pattern_atrdevema_21d_jerk_v140_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 21)
    e = a.ewm(span=252, adjust=False).mean()
    base = (a - e) * closeadj
    result = _diff(_diff(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d composite base
def f04bp_f04_basing_pattern_compbase_21d_jerk_v141_signal(closeadj, high, low):
    base = _f04_basing_range(closeadj, 21) * _f04_consolidation_atr(high, low, closeadj, 21) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d composite base
def f04bp_f04_basing_pattern_compbase_63d_jerk_v142_signal(closeadj, high, low):
    base = (_f04_basing_range(closeadj, 63) + _f04_consolidation_atr(high, low, closeadj, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d composite base
def f04bp_f04_basing_pattern_compbase_252d_jerk_v143_signal(closeadj, high, low):
    base = (_f04_basing_range(closeadj, 252) + _f04_consolidation_atr(high, low, closeadj, 252) + _f04_basing_height(closeadj, 252).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range per risk unit
def f04bp_f04_basing_pattern_rangeperriskunit_21d_jerk_v144_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs()).diff()
    rv = lr.rolling(21, min_periods=5).std().replace(0, np.nan)
    base = (_f04_basing_range(closeadj, 21) / rv) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d range per risk unit
def f04bp_f04_basing_pattern_rangeperriskunit_63d_jerk_v145_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs()).diff()
    rv = lr.rolling(63, min_periods=21).std().replace(0, np.nan)
    base = (_f04_basing_range(closeadj, 63) / rv) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range per risk unit
def f04bp_f04_basing_pattern_rangeperriskunit_252d_jerk_v146_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs()).diff()
    rv = lr.rolling(252, min_periods=63).std().replace(0, np.nan)
    base = (_f04_basing_range(closeadj, 252) / rv) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d height × ATR
def f04bp_f04_basing_pattern_heightxatr_21d_jerk_v147_signal(closeadj, high, low):
    base = _f04_basing_height(closeadj, 21) * _f04_consolidation_atr(high, low, closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d height × ATR
def f04bp_f04_basing_pattern_heightxatr_63d_jerk_v148_signal(closeadj, high, low):
    base = _f04_basing_height(closeadj, 63) * _f04_consolidation_atr(high, low, closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d range × height
def f04bp_f04_basing_pattern_rangexheight_21d_jerk_v149_signal(closeadj):
    base = _f04_basing_range(closeadj, 21) * _f04_basing_height(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d range × height
def f04bp_f04_basing_pattern_rangexheight_252d_jerk_v150_signal(closeadj):
    base = _f04_basing_range(closeadj, 252) * _f04_basing_height(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04bp_f04_basing_pattern_rangetight_21d_jerk_v001_signal,
    f04bp_f04_basing_pattern_rangetight_21d_jerk_v002_signal,
    f04bp_f04_basing_pattern_rangetight_63d_jerk_v003_signal,
    f04bp_f04_basing_pattern_rangetight_63d_jerk_v004_signal,
    f04bp_f04_basing_pattern_rangetight_63d_jerk_v005_signal,
    f04bp_f04_basing_pattern_rangetight_126d_jerk_v006_signal,
    f04bp_f04_basing_pattern_rangetight_126d_jerk_v007_signal,
    f04bp_f04_basing_pattern_rangetight_252d_jerk_v008_signal,
    f04bp_f04_basing_pattern_rangetight_252d_jerk_v009_signal,
    f04bp_f04_basing_pattern_rangetight_504d_jerk_v010_signal,
    f04bp_f04_basing_pattern_rangetight_504d_jerk_v011_signal,
    f04bp_f04_basing_pattern_rangetight_5d_jerk_v012_signal,
    f04bp_f04_basing_pattern_rangetight_10d_jerk_v013_signal,
    f04bp_f04_basing_pattern_rangetight_42d_jerk_v014_signal,
    f04bp_f04_basing_pattern_rangetight_189d_jerk_v015_signal,
    f04bp_f04_basing_pattern_rangetight_378d_jerk_v016_signal,
    f04bp_f04_basing_pattern_rangemean_63d_jerk_v017_signal,
    f04bp_f04_basing_pattern_rangemean_252d_jerk_v018_signal,
    f04bp_f04_basing_pattern_rangemean_504d_jerk_v019_signal,
    f04bp_f04_basing_pattern_rangestd_63d_jerk_v020_signal,
    f04bp_f04_basing_pattern_rangestd_252d_jerk_v021_signal,
    f04bp_f04_basing_pattern_rangestd_504d_jerk_v022_signal,
    f04bp_f04_basing_pattern_rangez_21d_jerk_v023_signal,
    f04bp_f04_basing_pattern_rangez_63d_jerk_v024_signal,
    f04bp_f04_basing_pattern_rangez_252d_jerk_v025_signal,
    f04bp_f04_basing_pattern_rangeratio_21v252_jerk_v026_signal,
    f04bp_f04_basing_pattern_rangeratio_63v252_jerk_v027_signal,
    f04bp_f04_basing_pattern_rangeratio_126v504_jerk_v028_signal,
    f04bp_f04_basing_pattern_rangediff_21m63_jerk_v029_signal,
    f04bp_f04_basing_pattern_rangediff_63m252_jerk_v030_signal,
    f04bp_f04_basing_pattern_rangediff_252m504_jerk_v031_signal,
    f04bp_f04_basing_pattern_height_21d_jerk_v032_signal,
    f04bp_f04_basing_pattern_height_63d_jerk_v033_signal,
    f04bp_f04_basing_pattern_height_126d_jerk_v034_signal,
    f04bp_f04_basing_pattern_height_252d_jerk_v035_signal,
    f04bp_f04_basing_pattern_height_504d_jerk_v036_signal,
    f04bp_f04_basing_pattern_absheight_21d_jerk_v037_signal,
    f04bp_f04_basing_pattern_absheight_63d_jerk_v038_signal,
    f04bp_f04_basing_pattern_absheight_252d_jerk_v039_signal,
    f04bp_f04_basing_pattern_heightsq_21d_jerk_v040_signal,
    f04bp_f04_basing_pattern_heightsq_63d_jerk_v041_signal,
    f04bp_f04_basing_pattern_heightsq_252d_jerk_v042_signal,
    f04bp_f04_basing_pattern_heightz_21d_jerk_v043_signal,
    f04bp_f04_basing_pattern_heightz_63d_jerk_v044_signal,
    f04bp_f04_basing_pattern_heightz_252d_jerk_v045_signal,
    f04bp_f04_basing_pattern_heightstd_21d_jerk_v046_signal,
    f04bp_f04_basing_pattern_heightstd_63d_jerk_v047_signal,
    f04bp_f04_basing_pattern_heightstd_252d_jerk_v048_signal,
    f04bp_f04_basing_pattern_atrcontract_21d_jerk_v049_signal,
    f04bp_f04_basing_pattern_atrcontract_21d_jerk_v050_signal,
    f04bp_f04_basing_pattern_atrcontract_63d_jerk_v051_signal,
    f04bp_f04_basing_pattern_atrcontract_63d_jerk_v052_signal,
    f04bp_f04_basing_pattern_atrcontract_126d_jerk_v053_signal,
    f04bp_f04_basing_pattern_atrcontract_252d_jerk_v054_signal,
    f04bp_f04_basing_pattern_atrcontract_504d_jerk_v055_signal,
    f04bp_f04_basing_pattern_atrratio_21v252_jerk_v056_signal,
    f04bp_f04_basing_pattern_atrratio_63v252_jerk_v057_signal,
    f04bp_f04_basing_pattern_atrratio_126v504_jerk_v058_signal,
    f04bp_f04_basing_pattern_atrdiff_21m63_jerk_v059_signal,
    f04bp_f04_basing_pattern_atrdiff_63m252_jerk_v060_signal,
    f04bp_f04_basing_pattern_atrdiff_252m504_jerk_v061_signal,
    f04bp_f04_basing_pattern_atrz_21d_jerk_v062_signal,
    f04bp_f04_basing_pattern_atrz_63d_jerk_v063_signal,
    f04bp_f04_basing_pattern_atrz_252d_jerk_v064_signal,
    f04bp_f04_basing_pattern_rangexatr_21d_jerk_v065_signal,
    f04bp_f04_basing_pattern_rangexatr_63d_jerk_v066_signal,
    f04bp_f04_basing_pattern_rangexatr_252d_jerk_v067_signal,
    f04bp_f04_basing_pattern_narrowcount_252d_jerk_v068_signal,
    f04bp_f04_basing_pattern_narrowcount_504d_jerk_v069_signal,
    f04bp_f04_basing_pattern_narrowcount_15pct_jerk_v070_signal,
    f04bp_f04_basing_pattern_rangepatratio_21d_jerk_v071_signal,
    f04bp_f04_basing_pattern_rangepatratio_63d_jerk_v072_signal,
    f04bp_f04_basing_pattern_rangepatratio_252d_jerk_v073_signal,
    f04bp_f04_basing_pattern_rangeema_21d_jerk_v074_signal,
    f04bp_f04_basing_pattern_rangeema_63d_jerk_v075_signal,
    f04bp_f04_basing_pattern_rangeema_252d_jerk_v076_signal,
    f04bp_f04_basing_pattern_rangexvol_21d_jerk_v077_signal,
    f04bp_f04_basing_pattern_rangexvol_63d_jerk_v078_signal,
    f04bp_f04_basing_pattern_rangexdv_252d_jerk_v079_signal,
    f04bp_f04_basing_pattern_heightvsatr_21d_jerk_v080_signal,
    f04bp_f04_basing_pattern_heightvsatr_63d_jerk_v081_signal,
    f04bp_f04_basing_pattern_heightvsatr_252d_jerk_v082_signal,
    f04bp_f04_basing_pattern_basetightcomp_252d_jerk_v083_signal,
    f04bp_f04_basing_pattern_rangexrv_21d_jerk_v084_signal,
    f04bp_f04_basing_pattern_rangexrv_63d_jerk_v085_signal,
    f04bp_f04_basing_pattern_rangexrv_252d_jerk_v086_signal,
    f04bp_f04_basing_pattern_rangedivrv_21d_jerk_v087_signal,
    f04bp_f04_basing_pattern_rangedivrv_63d_jerk_v088_signal,
    f04bp_f04_basing_pattern_rangedivrv_252d_jerk_v089_signal,
    f04bp_f04_basing_pattern_atrdivrv_21d_jerk_v090_signal,
    f04bp_f04_basing_pattern_atrdivrv_63d_jerk_v091_signal,
    f04bp_f04_basing_pattern_rangexskew_63d_jerk_v092_signal,
    f04bp_f04_basing_pattern_rangexkurt_252d_jerk_v093_signal,
    f04bp_f04_basing_pattern_heightxskew_252d_jerk_v094_signal,
    f04bp_f04_basing_pattern_heightoverrange_21d_jerk_v095_signal,
    f04bp_f04_basing_pattern_heightoverrange_63d_jerk_v096_signal,
    f04bp_f04_basing_pattern_heightoverrange_252d_jerk_v097_signal,
    f04bp_f04_basing_pattern_rangexabsheight_21d_jerk_v098_signal,
    f04bp_f04_basing_pattern_rangexabsheight_63d_jerk_v099_signal,
    f04bp_f04_basing_pattern_rangexabsheight_252d_jerk_v100_signal,
    f04bp_f04_basing_pattern_rangevsmin_252d_jerk_v101_signal,
    f04bp_f04_basing_pattern_rangevsmin_504d_jerk_v102_signal,
    f04bp_f04_basing_pattern_rangepctmax_504d_jerk_v103_signal,
    f04bp_f04_basing_pattern_rangepctmax_252d_jerk_v104_signal,
    f04bp_f04_basing_pattern_tightestever_jerk_v105_signal,
    f04bp_f04_basing_pattern_rangevshisttight_jerk_v106_signal,
    f04bp_f04_basing_pattern_dayswithinnarrow_63d_jerk_v107_signal,
    f04bp_f04_basing_pattern_dayswithinnarrow_252d_jerk_v108_signal,
    f04bp_f04_basing_pattern_dayswithinnarrow_504d_jerk_v109_signal,
    f04bp_f04_basing_pattern_rangexcurdv_21d_jerk_v110_signal,
    f04bp_f04_basing_pattern_rangexcurdv_63d_jerk_v111_signal,
    f04bp_f04_basing_pattern_rangexcurdv_252d_jerk_v112_signal,
    f04bp_f04_basing_pattern_rangexvolz_21d_jerk_v113_signal,
    f04bp_f04_basing_pattern_rangexvolz_63d_jerk_v114_signal,
    f04bp_f04_basing_pattern_rangexvolz_252d_jerk_v115_signal,
    f04bp_f04_basing_pattern_atrxvolz_21d_jerk_v116_signal,
    f04bp_f04_basing_pattern_atrxvolz_63d_jerk_v117_signal,
    f04bp_f04_basing_pattern_atrxdv_252d_jerk_v118_signal,
    f04bp_f04_basing_pattern_atrema_21d_jerk_v119_signal,
    f04bp_f04_basing_pattern_atrema_63d_jerk_v120_signal,
    f04bp_f04_basing_pattern_atrema_252d_jerk_v121_signal,
    f04bp_f04_basing_pattern_heightema_21d_jerk_v122_signal,
    f04bp_f04_basing_pattern_heightema_63d_jerk_v123_signal,
    f04bp_f04_basing_pattern_heightema_252d_jerk_v124_signal,
    f04bp_f04_basing_pattern_rangearea_63d_jerk_v125_signal,
    f04bp_f04_basing_pattern_rangearea_252d_jerk_v126_signal,
    f04bp_f04_basing_pattern_rangearea_504d_jerk_v127_signal,
    f04bp_f04_basing_pattern_rangexret_21d_jerk_v128_signal,
    f04bp_f04_basing_pattern_rangexret_63d_jerk_v129_signal,
    f04bp_f04_basing_pattern_rangexret_252d_jerk_v130_signal,
    f04bp_f04_basing_pattern_heightxret_21d_jerk_v131_signal,
    f04bp_f04_basing_pattern_heightxret_63d_jerk_v132_signal,
    f04bp_f04_basing_pattern_heightxret_252d_jerk_v133_signal,
    f04bp_f04_basing_pattern_rangexlog_21d_jerk_v134_signal,
    f04bp_f04_basing_pattern_rangexlog_63d_jerk_v135_signal,
    f04bp_f04_basing_pattern_atrxlog_21d_jerk_v136_signal,
    f04bp_f04_basing_pattern_rangedevema_63d_jerk_v137_signal,
    f04bp_f04_basing_pattern_rangedevema_252d_jerk_v138_signal,
    f04bp_f04_basing_pattern_heightdevema_63d_jerk_v139_signal,
    f04bp_f04_basing_pattern_atrdevema_21d_jerk_v140_signal,
    f04bp_f04_basing_pattern_compbase_21d_jerk_v141_signal,
    f04bp_f04_basing_pattern_compbase_63d_jerk_v142_signal,
    f04bp_f04_basing_pattern_compbase_252d_jerk_v143_signal,
    f04bp_f04_basing_pattern_rangeperriskunit_21d_jerk_v144_signal,
    f04bp_f04_basing_pattern_rangeperriskunit_63d_jerk_v145_signal,
    f04bp_f04_basing_pattern_rangeperriskunit_252d_jerk_v146_signal,
    f04bp_f04_basing_pattern_heightxatr_21d_jerk_v147_signal,
    f04bp_f04_basing_pattern_heightxatr_63d_jerk_v148_signal,
    f04bp_f04_basing_pattern_rangexheight_21d_jerk_v149_signal,
    f04bp_f04_basing_pattern_rangexheight_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_BASING_PATTERN_REGISTRY_JERK = REGISTRY


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
    domain_primitives = ("_f04_basing_range", "_f04_basing_height", "_f04_consolidation_atr")
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
    print(f"OK f04_basing_pattern_3rd_derivatives_001_150_claude: {n_features} features pass")
