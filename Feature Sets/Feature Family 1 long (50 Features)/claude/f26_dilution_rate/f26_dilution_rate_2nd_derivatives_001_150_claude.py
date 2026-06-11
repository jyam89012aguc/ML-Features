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
    return s.diff(periods=w)


def _jerk(s, w):
    sl = s.diff(periods=w)
    return sl.diff(periods=w)


# ===== folder domain primitives =====

def _f26_dilution_rate(sharesbas, w):
    return sharesbas.diff(w) / sharesbas.shift(w).abs().replace(0, np.nan)


def _f26_share_growth(sharesbas, w):
    return sharesbas.pct_change(w)

# 5d slope of raw 21d primitive
def f26dr_f26_dilution_rate_raw_21d_roc5_21d_slope_v001_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 21d primitive
def f26dr_f26_dilution_rate_raw_21d_roc21_21d_slope_v002_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean21 21d primitive
def f26dr_f26_dilution_rate_mean21_21d_roc5_21d_slope_v003_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 21d primitive
def f26dr_f26_dilution_rate_mean21_21d_roc21_21d_slope_v004_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean63 21d primitive
def f26dr_f26_dilution_rate_mean63_21d_roc5_21d_slope_v005_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 21d primitive
def f26dr_f26_dilution_rate_mean63_21d_roc21_21d_slope_v006_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of std63 21d primitive
def f26dr_f26_dilution_rate_std63_21d_roc5_21d_slope_v007_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 21d primitive
def f26dr_f26_dilution_rate_std63_21d_roc21_21d_slope_v008_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z63 21d primitive
def f26dr_f26_dilution_rate_z63_21d_roc5_21d_slope_v009_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 21d primitive
def f26dr_f26_dilution_rate_z63_21d_roc21_21d_slope_v010_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z252 21d primitive
def f26dr_f26_dilution_rate_z252_21d_roc5_21d_slope_v011_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 252) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 21d primitive
def f26dr_f26_dilution_rate_z252_21d_roc21_21d_slope_v012_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema21 21d primitive
def f26dr_f26_dilution_rate_ema21_21d_roc5_21d_slope_v013_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 21d primitive
def f26dr_f26_dilution_rate_ema21_21d_roc21_21d_slope_v014_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema63 21d primitive
def f26dr_f26_dilution_rate_ema63_21d_roc5_21d_slope_v015_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 21d primitive
def f26dr_f26_dilution_rate_ema63_21d_roc21_21d_slope_v016_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of absmean63 21d primitive
def f26dr_f26_dilution_rate_absmean63_21d_roc5_21d_slope_v017_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 21d primitive
def f26dr_f26_dilution_rate_absmean63_21d_roc21_21d_slope_v018_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of sqrmean63 21d primitive
def f26dr_f26_dilution_rate_sqrmean63_21d_roc5_21d_slope_v019_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 21)) * (_f26_dilution_rate(sharesbas, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 21d primitive
def f26dr_f26_dilution_rate_sqrmean63_21d_roc21_21d_slope_v020_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 21)) * (_f26_dilution_rate(sharesbas, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of raw 63d primitive
def f26dr_f26_dilution_rate_raw_63d_roc5_63d_slope_v021_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 63d primitive
def f26dr_f26_dilution_rate_raw_63d_roc21_63d_slope_v022_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 63d primitive
def f26dr_f26_dilution_rate_raw_63d_roc63_63d_slope_v023_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean21 63d primitive
def f26dr_f26_dilution_rate_mean21_63d_roc5_63d_slope_v024_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 63), 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 63d primitive
def f26dr_f26_dilution_rate_mean21_63d_roc21_63d_slope_v025_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 63), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 63d primitive
def f26dr_f26_dilution_rate_mean21_63d_roc63_63d_slope_v026_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 63), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean63 63d primitive
def f26dr_f26_dilution_rate_mean63_63d_roc5_63d_slope_v027_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 63d primitive
def f26dr_f26_dilution_rate_mean63_63d_roc21_63d_slope_v028_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 63d primitive
def f26dr_f26_dilution_rate_mean63_63d_roc63_63d_slope_v029_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of std63 63d primitive
def f26dr_f26_dilution_rate_std63_63d_roc5_63d_slope_v030_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 63d primitive
def f26dr_f26_dilution_rate_std63_63d_roc21_63d_slope_v031_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 63d primitive
def f26dr_f26_dilution_rate_std63_63d_roc63_63d_slope_v032_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z63 63d primitive
def f26dr_f26_dilution_rate_z63_63d_roc5_63d_slope_v033_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 63d primitive
def f26dr_f26_dilution_rate_z63_63d_roc21_63d_slope_v034_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 63d primitive
def f26dr_f26_dilution_rate_z63_63d_roc63_63d_slope_v035_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z252 63d primitive
def f26dr_f26_dilution_rate_z252_63d_roc5_63d_slope_v036_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 63), 252) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 63d primitive
def f26dr_f26_dilution_rate_z252_63d_roc21_63d_slope_v037_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 63), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 63d primitive
def f26dr_f26_dilution_rate_z252_63d_roc63_63d_slope_v038_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 63), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema21 63d primitive
def f26dr_f26_dilution_rate_ema21_63d_roc5_63d_slope_v039_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 63d primitive
def f26dr_f26_dilution_rate_ema21_63d_roc21_63d_slope_v040_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 63d primitive
def f26dr_f26_dilution_rate_ema21_63d_roc63_63d_slope_v041_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema63 63d primitive
def f26dr_f26_dilution_rate_ema63_63d_roc5_63d_slope_v042_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 63d primitive
def f26dr_f26_dilution_rate_ema63_63d_roc21_63d_slope_v043_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 63d primitive
def f26dr_f26_dilution_rate_ema63_63d_roc63_63d_slope_v044_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of absmean63 63d primitive
def f26dr_f26_dilution_rate_absmean63_63d_roc5_63d_slope_v045_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 63d primitive
def f26dr_f26_dilution_rate_absmean63_63d_roc21_63d_slope_v046_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 63d primitive
def f26dr_f26_dilution_rate_absmean63_63d_roc63_63d_slope_v047_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 63)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of sqrmean63 63d primitive
def f26dr_f26_dilution_rate_sqrmean63_63d_roc5_63d_slope_v048_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 63)) * (_f26_dilution_rate(sharesbas, 63)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 63d primitive
def f26dr_f26_dilution_rate_sqrmean63_63d_roc21_63d_slope_v049_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 63)) * (_f26_dilution_rate(sharesbas, 63)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 63d primitive
def f26dr_f26_dilution_rate_sqrmean63_63d_roc63_63d_slope_v050_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 63)) * (_f26_dilution_rate(sharesbas, 63)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 126d primitive
def f26dr_f26_dilution_rate_raw_126d_roc21_126d_slope_v051_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 126d primitive
def f26dr_f26_dilution_rate_raw_126d_roc63_126d_slope_v052_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 126d primitive
def f26dr_f26_dilution_rate_mean21_126d_roc21_126d_slope_v053_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 126), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 126d primitive
def f26dr_f26_dilution_rate_mean21_126d_roc63_126d_slope_v054_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 126), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 126d primitive
def f26dr_f26_dilution_rate_mean63_126d_roc21_126d_slope_v055_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 126), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 126d primitive
def f26dr_f26_dilution_rate_mean63_126d_roc63_126d_slope_v056_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 126), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 126d primitive
def f26dr_f26_dilution_rate_std63_126d_roc21_126d_slope_v057_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 126), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 126d primitive
def f26dr_f26_dilution_rate_std63_126d_roc63_126d_slope_v058_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 126), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 126d primitive
def f26dr_f26_dilution_rate_z63_126d_roc21_126d_slope_v059_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 126), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 126d primitive
def f26dr_f26_dilution_rate_z63_126d_roc63_126d_slope_v060_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 126), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 126d primitive
def f26dr_f26_dilution_rate_z252_126d_roc21_126d_slope_v061_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 126), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 126d primitive
def f26dr_f26_dilution_rate_z252_126d_roc63_126d_slope_v062_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 126), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 126d primitive
def f26dr_f26_dilution_rate_ema21_126d_roc21_126d_slope_v063_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 126d primitive
def f26dr_f26_dilution_rate_ema21_126d_roc63_126d_slope_v064_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 126d primitive
def f26dr_f26_dilution_rate_ema63_126d_roc21_126d_slope_v065_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 126d primitive
def f26dr_f26_dilution_rate_ema63_126d_roc63_126d_slope_v066_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 126d primitive
def f26dr_f26_dilution_rate_absmean63_126d_roc21_126d_slope_v067_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 126d primitive
def f26dr_f26_dilution_rate_absmean63_126d_roc63_126d_slope_v068_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 126)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 126d primitive
def f26dr_f26_dilution_rate_sqrmean63_126d_roc21_126d_slope_v069_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 126)) * (_f26_dilution_rate(sharesbas, 126)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 126d primitive
def f26dr_f26_dilution_rate_sqrmean63_126d_roc63_126d_slope_v070_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 126)) * (_f26_dilution_rate(sharesbas, 126)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 252d primitive
def f26dr_f26_dilution_rate_raw_252d_roc21_252d_slope_v071_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 252d primitive
def f26dr_f26_dilution_rate_raw_252d_roc63_252d_slope_v072_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 252d primitive
def f26dr_f26_dilution_rate_mean21_252d_roc21_252d_slope_v073_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 252), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 252d primitive
def f26dr_f26_dilution_rate_mean21_252d_roc63_252d_slope_v074_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 252), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 252d primitive
def f26dr_f26_dilution_rate_mean63_252d_roc21_252d_slope_v075_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 252), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 252d primitive
def f26dr_f26_dilution_rate_mean63_252d_roc63_252d_slope_v076_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 252), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 252d primitive
def f26dr_f26_dilution_rate_std63_252d_roc21_252d_slope_v077_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 252), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 252d primitive
def f26dr_f26_dilution_rate_std63_252d_roc63_252d_slope_v078_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 252), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 252d primitive
def f26dr_f26_dilution_rate_z63_252d_roc21_252d_slope_v079_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 252), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 252d primitive
def f26dr_f26_dilution_rate_z63_252d_roc63_252d_slope_v080_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 252), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 252d primitive
def f26dr_f26_dilution_rate_z252_252d_roc21_252d_slope_v081_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 252), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 252d primitive
def f26dr_f26_dilution_rate_z252_252d_roc63_252d_slope_v082_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 252), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 252d primitive
def f26dr_f26_dilution_rate_ema21_252d_roc21_252d_slope_v083_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 252d primitive
def f26dr_f26_dilution_rate_ema21_252d_roc63_252d_slope_v084_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 252d primitive
def f26dr_f26_dilution_rate_ema63_252d_roc21_252d_slope_v085_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 252d primitive
def f26dr_f26_dilution_rate_ema63_252d_roc63_252d_slope_v086_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 252d primitive
def f26dr_f26_dilution_rate_absmean63_252d_roc21_252d_slope_v087_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 252d primitive
def f26dr_f26_dilution_rate_absmean63_252d_roc63_252d_slope_v088_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 252)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 252d primitive
def f26dr_f26_dilution_rate_sqrmean63_252d_roc21_252d_slope_v089_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 252)) * (_f26_dilution_rate(sharesbas, 252)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 252d primitive
def f26dr_f26_dilution_rate_sqrmean63_252d_roc63_252d_slope_v090_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 252)) * (_f26_dilution_rate(sharesbas, 252)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 504d primitive
def f26dr_f26_dilution_rate_raw_504d_roc21_504d_slope_v091_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 504d primitive
def f26dr_f26_dilution_rate_raw_504d_roc63_504d_slope_v092_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of raw 504d primitive
def f26dr_f26_dilution_rate_raw_504d_roc126_504d_slope_v093_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 504d primitive
def f26dr_f26_dilution_rate_mean21_504d_roc21_504d_slope_v094_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 504), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 504d primitive
def f26dr_f26_dilution_rate_mean21_504d_roc63_504d_slope_v095_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 504), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mean21 504d primitive
def f26dr_f26_dilution_rate_mean21_504d_roc126_504d_slope_v096_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 504), 21) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 504d primitive
def f26dr_f26_dilution_rate_mean63_504d_roc21_504d_slope_v097_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 504d primitive
def f26dr_f26_dilution_rate_mean63_504d_roc63_504d_slope_v098_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of mean63 504d primitive
def f26dr_f26_dilution_rate_mean63_504d_roc126_504d_slope_v099_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 504d primitive
def f26dr_f26_dilution_rate_std63_504d_roc21_504d_slope_v100_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 504d primitive
def f26dr_f26_dilution_rate_std63_504d_roc63_504d_slope_v101_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of std63 504d primitive
def f26dr_f26_dilution_rate_std63_504d_roc126_504d_slope_v102_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 504d primitive
def f26dr_f26_dilution_rate_z63_504d_roc21_504d_slope_v103_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 504d primitive
def f26dr_f26_dilution_rate_z63_504d_roc63_504d_slope_v104_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of z63 504d primitive
def f26dr_f26_dilution_rate_z63_504d_roc126_504d_slope_v105_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 504), 63) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 504d primitive
def f26dr_f26_dilution_rate_z252_504d_roc21_504d_slope_v106_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 504), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 504d primitive
def f26dr_f26_dilution_rate_z252_504d_roc63_504d_slope_v107_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 504), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of z252 504d primitive
def f26dr_f26_dilution_rate_z252_504d_roc126_504d_slope_v108_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 504), 252) * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 504d primitive
def f26dr_f26_dilution_rate_ema21_504d_roc21_504d_slope_v109_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 504d primitive
def f26dr_f26_dilution_rate_ema21_504d_roc63_504d_slope_v110_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ema21 504d primitive
def f26dr_f26_dilution_rate_ema21_504d_roc126_504d_slope_v111_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 504d primitive
def f26dr_f26_dilution_rate_ema63_504d_roc21_504d_slope_v112_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 504d primitive
def f26dr_f26_dilution_rate_ema63_504d_roc63_504d_slope_v113_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ema63 504d primitive
def f26dr_f26_dilution_rate_ema63_504d_roc126_504d_slope_v114_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 504d primitive
def f26dr_f26_dilution_rate_absmean63_504d_roc21_504d_slope_v115_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 504d primitive
def f26dr_f26_dilution_rate_absmean63_504d_roc63_504d_slope_v116_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of absmean63 504d primitive
def f26dr_f26_dilution_rate_absmean63_504d_roc126_504d_slope_v117_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 504)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 504d primitive
def f26dr_f26_dilution_rate_sqrmean63_504d_roc21_504d_slope_v118_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 504)) * (_f26_dilution_rate(sharesbas, 504)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 504d primitive
def f26dr_f26_dilution_rate_sqrmean63_504d_roc63_504d_slope_v119_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 504)) * (_f26_dilution_rate(sharesbas, 504)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sqrmean63 504d primitive
def f26dr_f26_dilution_rate_sqrmean63_504d_roc126_504d_slope_v120_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 504)) * (_f26_dilution_rate(sharesbas, 504)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of raw 21d primitive
def f26dr_f26_dilution_rate_raw_21d_roc5_21d_slope_v121_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of raw 21d primitive
def f26dr_f26_dilution_rate_raw_21d_roc21_21d_slope_v122_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of raw 21d primitive
def f26dr_f26_dilution_rate_raw_21d_roc63_21d_slope_v123_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean21 21d primitive
def f26dr_f26_dilution_rate_mean21_21d_roc5_21d_slope_v124_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 21) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean21 21d primitive
def f26dr_f26_dilution_rate_mean21_21d_roc21_21d_slope_v125_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 21) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean21 21d primitive
def f26dr_f26_dilution_rate_mean21_21d_roc63_21d_slope_v126_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 21) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of mean63 21d primitive
def f26dr_f26_dilution_rate_mean63_21d_roc5_21d_slope_v127_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of mean63 21d primitive
def f26dr_f26_dilution_rate_mean63_21d_roc21_21d_slope_v128_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of mean63 21d primitive
def f26dr_f26_dilution_rate_mean63_21d_roc63_21d_slope_v129_signal(sharesbas, closeadj):
    base = _mean(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of std63 21d primitive
def f26dr_f26_dilution_rate_std63_21d_roc5_21d_slope_v130_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of std63 21d primitive
def f26dr_f26_dilution_rate_std63_21d_roc21_21d_slope_v131_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of std63 21d primitive
def f26dr_f26_dilution_rate_std63_21d_roc63_21d_slope_v132_signal(sharesbas, closeadj):
    base = _std(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z63 21d primitive
def f26dr_f26_dilution_rate_z63_21d_roc5_21d_slope_v133_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z63 21d primitive
def f26dr_f26_dilution_rate_z63_21d_roc21_21d_slope_v134_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z63 21d primitive
def f26dr_f26_dilution_rate_z63_21d_roc63_21d_slope_v135_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 63) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of z252 21d primitive
def f26dr_f26_dilution_rate_z252_21d_roc5_21d_slope_v136_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 252) * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of z252 21d primitive
def f26dr_f26_dilution_rate_z252_21d_roc21_21d_slope_v137_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 252) * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of z252 21d primitive
def f26dr_f26_dilution_rate_z252_21d_roc63_21d_slope_v138_signal(sharesbas, closeadj):
    base = _z(_f26_dilution_rate(sharesbas, 21), 252) * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema21 21d primitive
def f26dr_f26_dilution_rate_ema21_21d_roc5_21d_slope_v139_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema21 21d primitive
def f26dr_f26_dilution_rate_ema21_21d_roc21_21d_slope_v140_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema21 21d primitive
def f26dr_f26_dilution_rate_ema21_21d_roc63_21d_slope_v141_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of ema63 21d primitive
def f26dr_f26_dilution_rate_ema63_21d_roc5_21d_slope_v142_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ema63 21d primitive
def f26dr_f26_dilution_rate_ema63_21d_roc21_21d_slope_v143_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ema63 21d primitive
def f26dr_f26_dilution_rate_ema63_21d_roc63_21d_slope_v144_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of absmean63 21d primitive
def f26dr_f26_dilution_rate_absmean63_21d_roc5_21d_slope_v145_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of absmean63 21d primitive
def f26dr_f26_dilution_rate_absmean63_21d_roc21_21d_slope_v146_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of absmean63 21d primitive
def f26dr_f26_dilution_rate_absmean63_21d_roc63_21d_slope_v147_signal(sharesbas, closeadj):
    base = (_f26_dilution_rate(sharesbas, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of sqrmean63 21d primitive
def f26dr_f26_dilution_rate_sqrmean63_21d_roc5_21d_slope_v148_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 21)) * (_f26_dilution_rate(sharesbas, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sqrmean63 21d primitive
def f26dr_f26_dilution_rate_sqrmean63_21d_roc21_21d_slope_v149_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 21)) * (_f26_dilution_rate(sharesbas, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sqrmean63 21d primitive
def f26dr_f26_dilution_rate_sqrmean63_21d_roc63_21d_slope_v150_signal(sharesbas, closeadj):
    base = ((_f26_dilution_rate(sharesbas, 21)) * (_f26_dilution_rate(sharesbas, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f26dr_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    cols = {"sharesbas": sharesbas, "closeadj": closeadj}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_dilution_rate", "_f26_share_growth",)
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f26_dilution_rate_2nd_derivatives_001_150_claude: {n_features} features pass")
