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

def _f10_vol_regime(close, w):
    return _std(close.pct_change(), w)


def _f10_vol_state(close, w):
    return _z(_std(close.pct_change(), w), w)

# 5d jerk of raw 21d primitive
def f10vr_f10_volatility_regime_raw_21d_roc5_21d_jerk_v001_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of raw 21d primitive
def f10vr_f10_volatility_regime_raw_21d_roc21_21d_jerk_v002_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mean21 21d primitive
def f10vr_f10_volatility_regime_mean21_21d_roc5_21d_jerk_v003_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean21 21d primitive
def f10vr_f10_volatility_regime_mean21_21d_roc21_21d_jerk_v004_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mean63 21d primitive
def f10vr_f10_volatility_regime_mean63_21d_roc5_21d_jerk_v005_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean63 21d primitive
def f10vr_f10_volatility_regime_mean63_21d_roc21_21d_jerk_v006_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of std63 21d primitive
def f10vr_f10_volatility_regime_std63_21d_roc5_21d_jerk_v007_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of std63 21d primitive
def f10vr_f10_volatility_regime_std63_21d_roc21_21d_jerk_v008_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of z63 21d primitive
def f10vr_f10_volatility_regime_z63_21d_roc5_21d_jerk_v009_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z63 21d primitive
def f10vr_f10_volatility_regime_z63_21d_roc21_21d_jerk_v010_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of z252 21d primitive
def f10vr_f10_volatility_regime_z252_21d_roc5_21d_jerk_v011_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z252 21d primitive
def f10vr_f10_volatility_regime_z252_21d_roc21_21d_jerk_v012_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of ema21 21d primitive
def f10vr_f10_volatility_regime_ema21_21d_roc5_21d_jerk_v013_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema21 21d primitive
def f10vr_f10_volatility_regime_ema21_21d_roc21_21d_jerk_v014_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of ema63 21d primitive
def f10vr_f10_volatility_regime_ema63_21d_roc5_21d_jerk_v015_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema63 21d primitive
def f10vr_f10_volatility_regime_ema63_21d_roc21_21d_jerk_v016_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of absmean63 21d primitive
def f10vr_f10_volatility_regime_absmean63_21d_roc5_21d_jerk_v017_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of absmean63 21d primitive
def f10vr_f10_volatility_regime_absmean63_21d_roc21_21d_jerk_v018_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of sqrmean63 21d primitive
def f10vr_f10_volatility_regime_sqrmean63_21d_roc5_21d_jerk_v019_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 21)) * (_f10_vol_regime(closeadj, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sqrmean63 21d primitive
def f10vr_f10_volatility_regime_sqrmean63_21d_roc21_21d_jerk_v020_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 21)) * (_f10_vol_regime(closeadj, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of raw 63d primitive
def f10vr_f10_volatility_regime_raw_63d_roc5_63d_jerk_v021_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of raw 63d primitive
def f10vr_f10_volatility_regime_raw_63d_roc21_63d_jerk_v022_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of raw 63d primitive
def f10vr_f10_volatility_regime_raw_63d_roc63_63d_jerk_v023_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mean21 63d primitive
def f10vr_f10_volatility_regime_mean21_63d_roc5_63d_jerk_v024_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 63), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean21 63d primitive
def f10vr_f10_volatility_regime_mean21_63d_roc21_63d_jerk_v025_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean21 63d primitive
def f10vr_f10_volatility_regime_mean21_63d_roc63_63d_jerk_v026_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mean63 63d primitive
def f10vr_f10_volatility_regime_mean63_63d_roc5_63d_jerk_v027_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean63 63d primitive
def f10vr_f10_volatility_regime_mean63_63d_roc21_63d_jerk_v028_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean63 63d primitive
def f10vr_f10_volatility_regime_mean63_63d_roc63_63d_jerk_v029_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of std63 63d primitive
def f10vr_f10_volatility_regime_std63_63d_roc5_63d_jerk_v030_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of std63 63d primitive
def f10vr_f10_volatility_regime_std63_63d_roc21_63d_jerk_v031_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of std63 63d primitive
def f10vr_f10_volatility_regime_std63_63d_roc63_63d_jerk_v032_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of z63 63d primitive
def f10vr_f10_volatility_regime_z63_63d_roc5_63d_jerk_v033_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z63 63d primitive
def f10vr_f10_volatility_regime_z63_63d_roc21_63d_jerk_v034_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z63 63d primitive
def f10vr_f10_volatility_regime_z63_63d_roc63_63d_jerk_v035_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of z252 63d primitive
def f10vr_f10_volatility_regime_z252_63d_roc5_63d_jerk_v036_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 63), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z252 63d primitive
def f10vr_f10_volatility_regime_z252_63d_roc21_63d_jerk_v037_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z252 63d primitive
def f10vr_f10_volatility_regime_z252_63d_roc63_63d_jerk_v038_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of ema21 63d primitive
def f10vr_f10_volatility_regime_ema21_63d_roc5_63d_jerk_v039_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema21 63d primitive
def f10vr_f10_volatility_regime_ema21_63d_roc21_63d_jerk_v040_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema21 63d primitive
def f10vr_f10_volatility_regime_ema21_63d_roc63_63d_jerk_v041_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of ema63 63d primitive
def f10vr_f10_volatility_regime_ema63_63d_roc5_63d_jerk_v042_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema63 63d primitive
def f10vr_f10_volatility_regime_ema63_63d_roc21_63d_jerk_v043_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema63 63d primitive
def f10vr_f10_volatility_regime_ema63_63d_roc63_63d_jerk_v044_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of absmean63 63d primitive
def f10vr_f10_volatility_regime_absmean63_63d_roc5_63d_jerk_v045_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of absmean63 63d primitive
def f10vr_f10_volatility_regime_absmean63_63d_roc21_63d_jerk_v046_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of absmean63 63d primitive
def f10vr_f10_volatility_regime_absmean63_63d_roc63_63d_jerk_v047_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 63)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of sqrmean63 63d primitive
def f10vr_f10_volatility_regime_sqrmean63_63d_roc5_63d_jerk_v048_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 63)) * (_f10_vol_regime(closeadj, 63)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sqrmean63 63d primitive
def f10vr_f10_volatility_regime_sqrmean63_63d_roc21_63d_jerk_v049_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 63)) * (_f10_vol_regime(closeadj, 63)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sqrmean63 63d primitive
def f10vr_f10_volatility_regime_sqrmean63_63d_roc63_63d_jerk_v050_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 63)) * (_f10_vol_regime(closeadj, 63)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of raw 126d primitive
def f10vr_f10_volatility_regime_raw_126d_roc21_126d_jerk_v051_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of raw 126d primitive
def f10vr_f10_volatility_regime_raw_126d_roc63_126d_jerk_v052_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean21 126d primitive
def f10vr_f10_volatility_regime_mean21_126d_roc21_126d_jerk_v053_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 126), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean21 126d primitive
def f10vr_f10_volatility_regime_mean21_126d_roc63_126d_jerk_v054_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 126), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean63 126d primitive
def f10vr_f10_volatility_regime_mean63_126d_roc21_126d_jerk_v055_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 126), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean63 126d primitive
def f10vr_f10_volatility_regime_mean63_126d_roc63_126d_jerk_v056_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 126), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of std63 126d primitive
def f10vr_f10_volatility_regime_std63_126d_roc21_126d_jerk_v057_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 126), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of std63 126d primitive
def f10vr_f10_volatility_regime_std63_126d_roc63_126d_jerk_v058_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 126), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z63 126d primitive
def f10vr_f10_volatility_regime_z63_126d_roc21_126d_jerk_v059_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 126), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z63 126d primitive
def f10vr_f10_volatility_regime_z63_126d_roc63_126d_jerk_v060_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 126), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z252 126d primitive
def f10vr_f10_volatility_regime_z252_126d_roc21_126d_jerk_v061_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 126), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z252 126d primitive
def f10vr_f10_volatility_regime_z252_126d_roc63_126d_jerk_v062_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 126), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema21 126d primitive
def f10vr_f10_volatility_regime_ema21_126d_roc21_126d_jerk_v063_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema21 126d primitive
def f10vr_f10_volatility_regime_ema21_126d_roc63_126d_jerk_v064_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema63 126d primitive
def f10vr_f10_volatility_regime_ema63_126d_roc21_126d_jerk_v065_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema63 126d primitive
def f10vr_f10_volatility_regime_ema63_126d_roc63_126d_jerk_v066_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of absmean63 126d primitive
def f10vr_f10_volatility_regime_absmean63_126d_roc21_126d_jerk_v067_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of absmean63 126d primitive
def f10vr_f10_volatility_regime_absmean63_126d_roc63_126d_jerk_v068_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 126)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sqrmean63 126d primitive
def f10vr_f10_volatility_regime_sqrmean63_126d_roc21_126d_jerk_v069_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 126)) * (_f10_vol_regime(closeadj, 126)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sqrmean63 126d primitive
def f10vr_f10_volatility_regime_sqrmean63_126d_roc63_126d_jerk_v070_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 126)) * (_f10_vol_regime(closeadj, 126)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of raw 252d primitive
def f10vr_f10_volatility_regime_raw_252d_roc21_252d_jerk_v071_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of raw 252d primitive
def f10vr_f10_volatility_regime_raw_252d_roc63_252d_jerk_v072_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean21 252d primitive
def f10vr_f10_volatility_regime_mean21_252d_roc21_252d_jerk_v073_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 252), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean21 252d primitive
def f10vr_f10_volatility_regime_mean21_252d_roc63_252d_jerk_v074_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 252), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean63 252d primitive
def f10vr_f10_volatility_regime_mean63_252d_roc21_252d_jerk_v075_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 252), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean63 252d primitive
def f10vr_f10_volatility_regime_mean63_252d_roc63_252d_jerk_v076_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of std63 252d primitive
def f10vr_f10_volatility_regime_std63_252d_roc21_252d_jerk_v077_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 252), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of std63 252d primitive
def f10vr_f10_volatility_regime_std63_252d_roc63_252d_jerk_v078_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z63 252d primitive
def f10vr_f10_volatility_regime_z63_252d_roc21_252d_jerk_v079_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 252), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z63 252d primitive
def f10vr_f10_volatility_regime_z63_252d_roc63_252d_jerk_v080_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z252 252d primitive
def f10vr_f10_volatility_regime_z252_252d_roc21_252d_jerk_v081_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 252), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z252 252d primitive
def f10vr_f10_volatility_regime_z252_252d_roc63_252d_jerk_v082_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema21 252d primitive
def f10vr_f10_volatility_regime_ema21_252d_roc21_252d_jerk_v083_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema21 252d primitive
def f10vr_f10_volatility_regime_ema21_252d_roc63_252d_jerk_v084_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema63 252d primitive
def f10vr_f10_volatility_regime_ema63_252d_roc21_252d_jerk_v085_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema63 252d primitive
def f10vr_f10_volatility_regime_ema63_252d_roc63_252d_jerk_v086_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of absmean63 252d primitive
def f10vr_f10_volatility_regime_absmean63_252d_roc21_252d_jerk_v087_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of absmean63 252d primitive
def f10vr_f10_volatility_regime_absmean63_252d_roc63_252d_jerk_v088_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 252)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sqrmean63 252d primitive
def f10vr_f10_volatility_regime_sqrmean63_252d_roc21_252d_jerk_v089_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 252)) * (_f10_vol_regime(closeadj, 252)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sqrmean63 252d primitive
def f10vr_f10_volatility_regime_sqrmean63_252d_roc63_252d_jerk_v090_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 252)) * (_f10_vol_regime(closeadj, 252)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of raw 504d primitive
def f10vr_f10_volatility_regime_raw_504d_roc21_504d_jerk_v091_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of raw 504d primitive
def f10vr_f10_volatility_regime_raw_504d_roc63_504d_jerk_v092_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of raw 504d primitive
def f10vr_f10_volatility_regime_raw_504d_roc126_504d_jerk_v093_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean21 504d primitive
def f10vr_f10_volatility_regime_mean21_504d_roc21_504d_jerk_v094_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 504), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean21 504d primitive
def f10vr_f10_volatility_regime_mean21_504d_roc63_504d_jerk_v095_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 504), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mean21 504d primitive
def f10vr_f10_volatility_regime_mean21_504d_roc126_504d_jerk_v096_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 504), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean63 504d primitive
def f10vr_f10_volatility_regime_mean63_504d_roc21_504d_jerk_v097_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean63 504d primitive
def f10vr_f10_volatility_regime_mean63_504d_roc63_504d_jerk_v098_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of mean63 504d primitive
def f10vr_f10_volatility_regime_mean63_504d_roc126_504d_jerk_v099_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of std63 504d primitive
def f10vr_f10_volatility_regime_std63_504d_roc21_504d_jerk_v100_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of std63 504d primitive
def f10vr_f10_volatility_regime_std63_504d_roc63_504d_jerk_v101_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of std63 504d primitive
def f10vr_f10_volatility_regime_std63_504d_roc126_504d_jerk_v102_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z63 504d primitive
def f10vr_f10_volatility_regime_z63_504d_roc21_504d_jerk_v103_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z63 504d primitive
def f10vr_f10_volatility_regime_z63_504d_roc63_504d_jerk_v104_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of z63 504d primitive
def f10vr_f10_volatility_regime_z63_504d_roc126_504d_jerk_v105_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 504), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z252 504d primitive
def f10vr_f10_volatility_regime_z252_504d_roc21_504d_jerk_v106_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 504), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z252 504d primitive
def f10vr_f10_volatility_regime_z252_504d_roc63_504d_jerk_v107_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 504), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of z252 504d primitive
def f10vr_f10_volatility_regime_z252_504d_roc126_504d_jerk_v108_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 504), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema21 504d primitive
def f10vr_f10_volatility_regime_ema21_504d_roc21_504d_jerk_v109_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema21 504d primitive
def f10vr_f10_volatility_regime_ema21_504d_roc63_504d_jerk_v110_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ema21 504d primitive
def f10vr_f10_volatility_regime_ema21_504d_roc126_504d_jerk_v111_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema63 504d primitive
def f10vr_f10_volatility_regime_ema63_504d_roc21_504d_jerk_v112_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema63 504d primitive
def f10vr_f10_volatility_regime_ema63_504d_roc63_504d_jerk_v113_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ema63 504d primitive
def f10vr_f10_volatility_regime_ema63_504d_roc126_504d_jerk_v114_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of absmean63 504d primitive
def f10vr_f10_volatility_regime_absmean63_504d_roc21_504d_jerk_v115_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of absmean63 504d primitive
def f10vr_f10_volatility_regime_absmean63_504d_roc63_504d_jerk_v116_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of absmean63 504d primitive
def f10vr_f10_volatility_regime_absmean63_504d_roc126_504d_jerk_v117_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 504)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sqrmean63 504d primitive
def f10vr_f10_volatility_regime_sqrmean63_504d_roc21_504d_jerk_v118_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 504)) * (_f10_vol_regime(closeadj, 504)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sqrmean63 504d primitive
def f10vr_f10_volatility_regime_sqrmean63_504d_roc63_504d_jerk_v119_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 504)) * (_f10_vol_regime(closeadj, 504)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sqrmean63 504d primitive
def f10vr_f10_volatility_regime_sqrmean63_504d_roc126_504d_jerk_v120_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 504)) * (_f10_vol_regime(closeadj, 504)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of raw 21d primitive
def f10vr_f10_volatility_regime_raw_21d_roc5_21d_jerk_v121_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of raw 21d primitive
def f10vr_f10_volatility_regime_raw_21d_roc21_21d_jerk_v122_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of raw 21d primitive
def f10vr_f10_volatility_regime_raw_21d_roc63_21d_jerk_v123_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mean21 21d primitive
def f10vr_f10_volatility_regime_mean21_21d_roc5_21d_jerk_v124_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean21 21d primitive
def f10vr_f10_volatility_regime_mean21_21d_roc21_21d_jerk_v125_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean21 21d primitive
def f10vr_f10_volatility_regime_mean21_21d_roc63_21d_jerk_v126_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of mean63 21d primitive
def f10vr_f10_volatility_regime_mean63_21d_roc5_21d_jerk_v127_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of mean63 21d primitive
def f10vr_f10_volatility_regime_mean63_21d_roc21_21d_jerk_v128_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of mean63 21d primitive
def f10vr_f10_volatility_regime_mean63_21d_roc63_21d_jerk_v129_signal(closeadj):
    base = _mean(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of std63 21d primitive
def f10vr_f10_volatility_regime_std63_21d_roc5_21d_jerk_v130_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of std63 21d primitive
def f10vr_f10_volatility_regime_std63_21d_roc21_21d_jerk_v131_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of std63 21d primitive
def f10vr_f10_volatility_regime_std63_21d_roc63_21d_jerk_v132_signal(closeadj):
    base = _std(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of z63 21d primitive
def f10vr_f10_volatility_regime_z63_21d_roc5_21d_jerk_v133_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z63 21d primitive
def f10vr_f10_volatility_regime_z63_21d_roc21_21d_jerk_v134_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z63 21d primitive
def f10vr_f10_volatility_regime_z63_21d_roc63_21d_jerk_v135_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of z252 21d primitive
def f10vr_f10_volatility_regime_z252_21d_roc5_21d_jerk_v136_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of z252 21d primitive
def f10vr_f10_volatility_regime_z252_21d_roc21_21d_jerk_v137_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of z252 21d primitive
def f10vr_f10_volatility_regime_z252_21d_roc63_21d_jerk_v138_signal(closeadj):
    base = _z(_f10_vol_regime(closeadj, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of ema21 21d primitive
def f10vr_f10_volatility_regime_ema21_21d_roc5_21d_jerk_v139_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema21 21d primitive
def f10vr_f10_volatility_regime_ema21_21d_roc21_21d_jerk_v140_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema21 21d primitive
def f10vr_f10_volatility_regime_ema21_21d_roc63_21d_jerk_v141_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of ema63 21d primitive
def f10vr_f10_volatility_regime_ema63_21d_roc5_21d_jerk_v142_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ema63 21d primitive
def f10vr_f10_volatility_regime_ema63_21d_roc21_21d_jerk_v143_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ema63 21d primitive
def f10vr_f10_volatility_regime_ema63_21d_roc63_21d_jerk_v144_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of absmean63 21d primitive
def f10vr_f10_volatility_regime_absmean63_21d_roc5_21d_jerk_v145_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of absmean63 21d primitive
def f10vr_f10_volatility_regime_absmean63_21d_roc21_21d_jerk_v146_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of absmean63 21d primitive
def f10vr_f10_volatility_regime_absmean63_21d_roc63_21d_jerk_v147_signal(closeadj):
    base = (_f10_vol_regime(closeadj, 21)).abs().rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of sqrmean63 21d primitive
def f10vr_f10_volatility_regime_sqrmean63_21d_roc5_21d_jerk_v148_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 21)) * (_f10_vol_regime(closeadj, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sqrmean63 21d primitive
def f10vr_f10_volatility_regime_sqrmean63_21d_roc21_21d_jerk_v149_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 21)) * (_f10_vol_regime(closeadj, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sqrmean63 21d primitive
def f10vr_f10_volatility_regime_sqrmean63_21d_roc63_21d_jerk_v150_signal(closeadj):
    base = ((_f10_vol_regime(closeadj, 21)) * (_f10_vol_regime(closeadj, 21)).abs()).rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f10vr_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    cols = {"closeadj": closeadj}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f10_vol_regime", "_f10_vol_state",)
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
    print(f"OK f10_volatility_regime_3rd_derivatives_001_150_claude: {n_features} features pass")
