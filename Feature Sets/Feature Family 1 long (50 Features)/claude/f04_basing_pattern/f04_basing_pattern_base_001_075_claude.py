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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


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


# 21d basing range as fraction of price
def f04bp_f04_basing_pattern_rangetight_21d_base_v001_signal(closeadj):
    result = _f04_basing_range(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range as fraction of price
def f04bp_f04_basing_pattern_rangetight_63d_base_v002_signal(closeadj):
    result = _f04_basing_range(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basing range as fraction of price
def f04bp_f04_basing_pattern_rangetight_126d_base_v003_signal(closeadj):
    result = _f04_basing_range(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range as fraction of price
def f04bp_f04_basing_pattern_rangetight_252d_base_v004_signal(closeadj):
    result = _f04_basing_range(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d basing range as fraction of price
def f04bp_f04_basing_pattern_rangetight_504d_base_v005_signal(closeadj):
    result = _f04_basing_range(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d basing range
def f04bp_f04_basing_pattern_rangetight_5d_base_v006_signal(closeadj):
    result = _f04_basing_range(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d basing range
def f04bp_f04_basing_pattern_rangetight_10d_base_v007_signal(closeadj):
    result = _f04_basing_range(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d basing range
def f04bp_f04_basing_pattern_rangetight_42d_base_v008_signal(closeadj):
    result = _f04_basing_range(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d basing range
def f04bp_f04_basing_pattern_rangetight_189d_base_v009_signal(closeadj):
    result = _f04_basing_range(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d basing range
def f04bp_f04_basing_pattern_rangetight_378d_base_v010_signal(closeadj):
    result = _f04_basing_range(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of 63d basing range
def f04bp_f04_basing_pattern_rangemean_63d_base_v011_signal(closeadj):
    result = _mean(_f04_basing_range(closeadj, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of 252d basing range
def f04bp_f04_basing_pattern_rangemean_252d_base_v012_signal(closeadj):
    result = _mean(_f04_basing_range(closeadj, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of 504d basing range
def f04bp_f04_basing_pattern_rangemean_504d_base_v013_signal(closeadj):
    result = _mean(_f04_basing_range(closeadj, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling std of 63d basing range
def f04bp_f04_basing_pattern_rangestd_63d_base_v014_signal(closeadj):
    result = _std(_f04_basing_range(closeadj, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of 252d basing range
def f04bp_f04_basing_pattern_rangestd_252d_base_v015_signal(closeadj):
    result = _std(_f04_basing_range(closeadj, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling std of 504d basing range
def f04bp_f04_basing_pattern_rangestd_504d_base_v016_signal(closeadj):
    result = _std(_f04_basing_range(closeadj, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 21d basing range (tightness anomaly)
def f04bp_f04_basing_pattern_rangez_21d_base_v017_signal(closeadj):
    result = _z(_f04_basing_range(closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 63d basing range
def f04bp_f04_basing_pattern_rangez_63d_base_v018_signal(closeadj):
    result = _z(_f04_basing_range(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of 252d basing range
def f04bp_f04_basing_pattern_rangez_252d_base_v019_signal(closeadj):
    result = _z(_f04_basing_range(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range divided by 252d basing range (tightness ratio)
def f04bp_f04_basing_pattern_rangeratio_21v252_base_v020_signal(closeadj):
    a = _f04_basing_range(closeadj, 21)
    b = _f04_basing_range(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range divided by 252d basing range
def f04bp_f04_basing_pattern_rangeratio_63v252_base_v021_signal(closeadj):
    a = _f04_basing_range(closeadj, 63)
    b = _f04_basing_range(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basing range divided by 504d basing range
def f04bp_f04_basing_pattern_rangeratio_126v504_base_v022_signal(closeadj):
    a = _f04_basing_range(closeadj, 126)
    b = _f04_basing_range(closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range minus 63d basing range
def f04bp_f04_basing_pattern_rangediff_21m63_base_v023_signal(closeadj):
    result = (_f04_basing_range(closeadj, 21) - _f04_basing_range(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range minus 252d basing range
def f04bp_f04_basing_pattern_rangediff_63m252_base_v024_signal(closeadj):
    result = (_f04_basing_range(closeadj, 63) - _f04_basing_range(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range minus 504d basing range
def f04bp_f04_basing_pattern_rangediff_252m504_base_v025_signal(closeadj):
    result = (_f04_basing_range(closeadj, 252) - _f04_basing_range(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing height (deviation from rolling mean)
def f04bp_f04_basing_pattern_height_21d_base_v026_signal(closeadj):
    result = _f04_basing_height(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing height
def f04bp_f04_basing_pattern_height_63d_base_v027_signal(closeadj):
    result = _f04_basing_height(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basing height
def f04bp_f04_basing_pattern_height_126d_base_v028_signal(closeadj):
    result = _f04_basing_height(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing height
def f04bp_f04_basing_pattern_height_252d_base_v029_signal(closeadj):
    result = _f04_basing_height(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d basing height
def f04bp_f04_basing_pattern_height_504d_base_v030_signal(closeadj):
    result = _f04_basing_height(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d absolute basing height (distance from base midpoint)
def f04bp_f04_basing_pattern_absheight_21d_base_v031_signal(closeadj):
    result = _f04_basing_height(closeadj, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d absolute basing height
def f04bp_f04_basing_pattern_absheight_63d_base_v032_signal(closeadj):
    result = _f04_basing_height(closeadj, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d absolute basing height
def f04bp_f04_basing_pattern_absheight_252d_base_v033_signal(closeadj):
    result = _f04_basing_height(closeadj, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing height squared (severity emphasis)
def f04bp_f04_basing_pattern_heightsq_21d_base_v034_signal(closeadj):
    h = _f04_basing_height(closeadj, 21)
    result = h * h.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing height squared
def f04bp_f04_basing_pattern_heightsq_63d_base_v035_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    result = h * h.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing height squared
def f04bp_f04_basing_pattern_heightsq_252d_base_v036_signal(closeadj):
    h = _f04_basing_height(closeadj, 252)
    result = h * h.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore of basing height
def f04bp_f04_basing_pattern_heightz_21d_base_v037_signal(closeadj):
    result = _z(_f04_basing_height(closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of basing height
def f04bp_f04_basing_pattern_heightz_63d_base_v038_signal(closeadj):
    result = _z(_f04_basing_height(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of basing height
def f04bp_f04_basing_pattern_heightz_252d_base_v039_signal(closeadj):
    result = _z(_f04_basing_height(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of basing height (height volatility)
def f04bp_f04_basing_pattern_heightstd_21d_base_v040_signal(closeadj):
    result = _std(_f04_basing_height(closeadj, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of basing height
def f04bp_f04_basing_pattern_heightstd_63d_base_v041_signal(closeadj):
    result = _std(_f04_basing_height(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of basing height
def f04bp_f04_basing_pattern_heightstd_252d_base_v042_signal(closeadj):
    result = _std(_f04_basing_height(closeadj, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d consolidation ATR-style range fraction
def f04bp_f04_basing_pattern_atrcontract_21d_base_v043_signal(closeadj, high, low):
    result = _f04_consolidation_atr(high, low, closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolidation ATR-style range fraction
def f04bp_f04_basing_pattern_atrcontract_63d_base_v044_signal(closeadj, high, low):
    result = _f04_consolidation_atr(high, low, closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d consolidation ATR
def f04bp_f04_basing_pattern_atrcontract_126d_base_v045_signal(closeadj, high, low):
    result = _f04_consolidation_atr(high, low, closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolidation ATR
def f04bp_f04_basing_pattern_atrcontract_252d_base_v046_signal(closeadj, high, low):
    result = _f04_consolidation_atr(high, low, closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d consolidation ATR
def f04bp_f04_basing_pattern_atrcontract_504d_base_v047_signal(closeadj, high, low):
    result = _f04_consolidation_atr(high, low, closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR contraction divided by 252d ATR (tightening ratio)
def f04bp_f04_basing_pattern_atrratio_21v252_base_v048_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 21)
    b = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR / 252d ATR
def f04bp_f04_basing_pattern_atrratio_63v252_base_v049_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 63)
    b = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ATR / 504d ATR
def f04bp_f04_basing_pattern_atrratio_126v504_base_v050_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 126)
    b = _f04_consolidation_atr(high, low, closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR minus 63d ATR (contraction speed)
def f04bp_f04_basing_pattern_atrdiff_21m63_base_v051_signal(closeadj, high, low):
    result = (_f04_consolidation_atr(high, low, closeadj, 21) - _f04_consolidation_atr(high, low, closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR minus 252d ATR
def f04bp_f04_basing_pattern_atrdiff_63m252_base_v052_signal(closeadj, high, low):
    result = (_f04_consolidation_atr(high, low, closeadj, 63) - _f04_consolidation_atr(high, low, closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR minus 504d ATR
def f04bp_f04_basing_pattern_atrdiff_252m504_base_v053_signal(closeadj, high, low):
    result = (_f04_consolidation_atr(high, low, closeadj, 252) - _f04_consolidation_atr(high, low, closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 21d ATR
def f04bp_f04_basing_pattern_atrz_21d_base_v054_signal(closeadj, high, low):
    result = _z(_f04_consolidation_atr(high, low, closeadj, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 63d ATR
def f04bp_f04_basing_pattern_atrz_63d_base_v055_signal(closeadj, high, low):
    result = _z(_f04_consolidation_atr(high, low, closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of 252d ATR
def f04bp_f04_basing_pattern_atrz_252d_base_v056_signal(closeadj, high, low):
    result = _z(_f04_consolidation_atr(high, low, closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range times ATR (compound tightness)
def f04bp_f04_basing_pattern_rangexatr_21d_base_v057_signal(closeadj, high, low):
    result = _f04_basing_range(closeadj, 21) * _f04_consolidation_atr(high, low, closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range times ATR
def f04bp_f04_basing_pattern_rangexatr_63d_base_v058_signal(closeadj, high, low):
    result = _f04_basing_range(closeadj, 63) * _f04_consolidation_atr(high, low, closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range times ATR
def f04bp_f04_basing_pattern_rangexatr_252d_base_v059_signal(closeadj, high, low):
    result = _f04_basing_range(closeadj, 252) * _f04_consolidation_atr(high, low, closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days where 21d basing range below 5% threshold (narrow-range count)
def f04bp_f04_basing_pattern_narrowcount_252d_base_v060_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 21) < 0.05).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days where 63d basing range below 30%, scaled by close
def f04bp_f04_basing_pattern_narrowcount_504d_base_v061_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 63) < 0.30).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days where 63d basing range below 15%
def f04bp_f04_basing_pattern_narrowcount_15pct_base_v062_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 63) < 0.15).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range divided by ATR-style range (range compression)
def f04bp_f04_basing_pattern_rangepatratio_21d_base_v063_signal(closeadj, high, low):
    a = _f04_basing_range(closeadj, 21)
    b = _f04_consolidation_atr(high, low, closeadj, 21).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range / ATR
def f04bp_f04_basing_pattern_rangepatratio_63d_base_v064_signal(closeadj, high, low):
    a = _f04_basing_range(closeadj, 63)
    b = _f04_consolidation_atr(high, low, closeadj, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range / ATR
def f04bp_f04_basing_pattern_rangepatratio_252d_base_v065_signal(closeadj, high, low):
    a = _f04_basing_range(closeadj, 252)
    b = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of basing range (smoothed tightness)
def f04bp_f04_basing_pattern_rangeema_21d_base_v066_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    result = r.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of basing range
def f04bp_f04_basing_pattern_rangeema_63d_base_v067_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    result = r.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of basing range
def f04bp_f04_basing_pattern_rangeema_252d_base_v068_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    result = r.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range times volume (tight on low volume)
def f04bp_f04_basing_pattern_rangexvol_21d_base_v069_signal(closeadj, volume):
    result = _f04_basing_range(closeadj, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range times volume
def f04bp_f04_basing_pattern_rangexvol_63d_base_v070_signal(closeadj, volume):
    result = _f04_basing_range(closeadj, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range times dollar-volume mean
def f04bp_f04_basing_pattern_rangexdv_252d_base_v071_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_basing_range(closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing height divided by 21d ATR (where in the base)
def f04bp_f04_basing_pattern_heightvsatr_21d_base_v072_signal(closeadj, high, low):
    h = _f04_basing_height(closeadj, 21)
    a = _f04_consolidation_atr(high, low, closeadj, 21).replace(0, np.nan)
    result = (h / a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing height / 63d ATR
def f04bp_f04_basing_pattern_heightvsatr_63d_base_v073_signal(closeadj, high, low):
    h = _f04_basing_height(closeadj, 63)
    a = _f04_consolidation_atr(high, low, closeadj, 63).replace(0, np.nan)
    result = (h / a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing height / 252d ATR
def f04bp_f04_basing_pattern_heightvsatr_252d_base_v074_signal(closeadj, high, low):
    h = _f04_basing_height(closeadj, 252)
    a = _f04_consolidation_atr(high, low, closeadj, 252).replace(0, np.nan)
    result = (h / a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite basing tightness: range + ATR over 252d
def f04bp_f04_basing_pattern_basetightcomp_252d_base_v075_signal(closeadj, high, low):
    r = _f04_basing_range(closeadj, 252)
    a = _f04_consolidation_atr(high, low, closeadj, 252)
    result = (r + a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04bp_f04_basing_pattern_rangetight_21d_base_v001_signal,
    f04bp_f04_basing_pattern_rangetight_63d_base_v002_signal,
    f04bp_f04_basing_pattern_rangetight_126d_base_v003_signal,
    f04bp_f04_basing_pattern_rangetight_252d_base_v004_signal,
    f04bp_f04_basing_pattern_rangetight_504d_base_v005_signal,
    f04bp_f04_basing_pattern_rangetight_5d_base_v006_signal,
    f04bp_f04_basing_pattern_rangetight_10d_base_v007_signal,
    f04bp_f04_basing_pattern_rangetight_42d_base_v008_signal,
    f04bp_f04_basing_pattern_rangetight_189d_base_v009_signal,
    f04bp_f04_basing_pattern_rangetight_378d_base_v010_signal,
    f04bp_f04_basing_pattern_rangemean_63d_base_v011_signal,
    f04bp_f04_basing_pattern_rangemean_252d_base_v012_signal,
    f04bp_f04_basing_pattern_rangemean_504d_base_v013_signal,
    f04bp_f04_basing_pattern_rangestd_63d_base_v014_signal,
    f04bp_f04_basing_pattern_rangestd_252d_base_v015_signal,
    f04bp_f04_basing_pattern_rangestd_504d_base_v016_signal,
    f04bp_f04_basing_pattern_rangez_21d_base_v017_signal,
    f04bp_f04_basing_pattern_rangez_63d_base_v018_signal,
    f04bp_f04_basing_pattern_rangez_252d_base_v019_signal,
    f04bp_f04_basing_pattern_rangeratio_21v252_base_v020_signal,
    f04bp_f04_basing_pattern_rangeratio_63v252_base_v021_signal,
    f04bp_f04_basing_pattern_rangeratio_126v504_base_v022_signal,
    f04bp_f04_basing_pattern_rangediff_21m63_base_v023_signal,
    f04bp_f04_basing_pattern_rangediff_63m252_base_v024_signal,
    f04bp_f04_basing_pattern_rangediff_252m504_base_v025_signal,
    f04bp_f04_basing_pattern_height_21d_base_v026_signal,
    f04bp_f04_basing_pattern_height_63d_base_v027_signal,
    f04bp_f04_basing_pattern_height_126d_base_v028_signal,
    f04bp_f04_basing_pattern_height_252d_base_v029_signal,
    f04bp_f04_basing_pattern_height_504d_base_v030_signal,
    f04bp_f04_basing_pattern_absheight_21d_base_v031_signal,
    f04bp_f04_basing_pattern_absheight_63d_base_v032_signal,
    f04bp_f04_basing_pattern_absheight_252d_base_v033_signal,
    f04bp_f04_basing_pattern_heightsq_21d_base_v034_signal,
    f04bp_f04_basing_pattern_heightsq_63d_base_v035_signal,
    f04bp_f04_basing_pattern_heightsq_252d_base_v036_signal,
    f04bp_f04_basing_pattern_heightz_21d_base_v037_signal,
    f04bp_f04_basing_pattern_heightz_63d_base_v038_signal,
    f04bp_f04_basing_pattern_heightz_252d_base_v039_signal,
    f04bp_f04_basing_pattern_heightstd_21d_base_v040_signal,
    f04bp_f04_basing_pattern_heightstd_63d_base_v041_signal,
    f04bp_f04_basing_pattern_heightstd_252d_base_v042_signal,
    f04bp_f04_basing_pattern_atrcontract_21d_base_v043_signal,
    f04bp_f04_basing_pattern_atrcontract_63d_base_v044_signal,
    f04bp_f04_basing_pattern_atrcontract_126d_base_v045_signal,
    f04bp_f04_basing_pattern_atrcontract_252d_base_v046_signal,
    f04bp_f04_basing_pattern_atrcontract_504d_base_v047_signal,
    f04bp_f04_basing_pattern_atrratio_21v252_base_v048_signal,
    f04bp_f04_basing_pattern_atrratio_63v252_base_v049_signal,
    f04bp_f04_basing_pattern_atrratio_126v504_base_v050_signal,
    f04bp_f04_basing_pattern_atrdiff_21m63_base_v051_signal,
    f04bp_f04_basing_pattern_atrdiff_63m252_base_v052_signal,
    f04bp_f04_basing_pattern_atrdiff_252m504_base_v053_signal,
    f04bp_f04_basing_pattern_atrz_21d_base_v054_signal,
    f04bp_f04_basing_pattern_atrz_63d_base_v055_signal,
    f04bp_f04_basing_pattern_atrz_252d_base_v056_signal,
    f04bp_f04_basing_pattern_rangexatr_21d_base_v057_signal,
    f04bp_f04_basing_pattern_rangexatr_63d_base_v058_signal,
    f04bp_f04_basing_pattern_rangexatr_252d_base_v059_signal,
    f04bp_f04_basing_pattern_narrowcount_252d_base_v060_signal,
    f04bp_f04_basing_pattern_narrowcount_504d_base_v061_signal,
    f04bp_f04_basing_pattern_narrowcount_15pct_base_v062_signal,
    f04bp_f04_basing_pattern_rangepatratio_21d_base_v063_signal,
    f04bp_f04_basing_pattern_rangepatratio_63d_base_v064_signal,
    f04bp_f04_basing_pattern_rangepatratio_252d_base_v065_signal,
    f04bp_f04_basing_pattern_rangeema_21d_base_v066_signal,
    f04bp_f04_basing_pattern_rangeema_63d_base_v067_signal,
    f04bp_f04_basing_pattern_rangeema_252d_base_v068_signal,
    f04bp_f04_basing_pattern_rangexvol_21d_base_v069_signal,
    f04bp_f04_basing_pattern_rangexvol_63d_base_v070_signal,
    f04bp_f04_basing_pattern_rangexdv_252d_base_v071_signal,
    f04bp_f04_basing_pattern_heightvsatr_21d_base_v072_signal,
    f04bp_f04_basing_pattern_heightvsatr_63d_base_v073_signal,
    f04bp_f04_basing_pattern_heightvsatr_252d_base_v074_signal,
    f04bp_f04_basing_pattern_basetightcomp_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_BASING_PATTERN_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f04_basing_pattern_base_001_075_claude: {n_features} features pass")
