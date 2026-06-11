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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f06_ret(s):
    return s.pct_change()


def _f06_logret(s):
    return np.log(s / s.shift(1))


def _f06_realvol(r, w):
    return r.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(252)

# 21d realized vol (annualized)
def f06vr_f06_semi_volatility_regime_realvol_21d_base_v001_signal(closeadj):
    r = _f06_ret(closeadj)
    result = _f06_realvol(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d realized vol (annualized)
def f06vr_f06_semi_volatility_regime_realvol_63d_base_v002_signal(closeadj):
    r = _f06_ret(closeadj)
    result = _f06_realvol(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d realized vol (annualized)
def f06vr_f06_semi_volatility_regime_realvol_126d_base_v003_signal(closeadj):
    r = _f06_ret(closeadj)
    result = _f06_realvol(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d realized vol (annualized)
def f06vr_f06_semi_volatility_regime_realvol_252d_base_v004_signal(closeadj):
    r = _f06_ret(closeadj)
    result = _f06_realvol(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d realized vol (annualized)
def f06vr_f06_semi_volatility_regime_realvol_504d_base_v005_signal(closeadj):
    r = _f06_ret(closeadj)
    result = _f06_realvol(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-return vol (annualized)
def f06vr_f06_semi_volatility_regime_logvol_21d_base_v006_signal(closeadj):
    r = _f06_logret(closeadj)
    result = _f06_realvol(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-return vol (annualized)
def f06vr_f06_semi_volatility_regime_logvol_63d_base_v007_signal(closeadj):
    r = _f06_logret(closeadj)
    result = _f06_realvol(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-return vol (annualized)
def f06vr_f06_semi_volatility_regime_logvol_126d_base_v008_signal(closeadj):
    r = _f06_logret(closeadj)
    result = _f06_realvol(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-return vol (annualized)
def f06vr_f06_semi_volatility_regime_logvol_252d_base_v009_signal(closeadj):
    r = _f06_logret(closeadj)
    result = _f06_realvol(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-return vol (annualized)
def f06vr_f06_semi_volatility_regime_logvol_504d_base_v010_signal(closeadj):
    r = _f06_logret(closeadj)
    result = _f06_realvol(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_base_v011_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = _z(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_base_v012_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = _z(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_base_v013_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = _z(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_base_v014_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = _z(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_base_v015_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = _z(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of vol
def f06vr_f06_semi_volatility_regime_volrobustz_21d_base_v016_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    med = v_.rolling(63, min_periods=max(2, 63 // 2)).median()
    mad = (v_ - med).abs().rolling(63, min_periods=max(2, 63 // 2)).median()
    result = (v_ - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of vol
def f06vr_f06_semi_volatility_regime_volrobustz_63d_base_v017_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    med = v_.rolling(126, min_periods=max(2, 126 // 2)).median()
    mad = (v_ - med).abs().rolling(126, min_periods=max(2, 126 // 2)).median()
    result = (v_ - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of vol
def f06vr_f06_semi_volatility_regime_volrobustz_126d_base_v018_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    med = v_.rolling(252, min_periods=max(2, 252 // 2)).median()
    mad = (v_ - med).abs().rolling(252, min_periods=max(2, 252 // 2)).median()
    result = (v_ - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of vol
def f06vr_f06_semi_volatility_regime_volrobustz_252d_base_v019_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    med = v_.rolling(504, min_periods=max(2, 504 // 2)).median()
    mad = (v_ - med).abs().rolling(504, min_periods=max(2, 504 // 2)).median()
    result = (v_ - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of vol
def f06vr_f06_semi_volatility_regime_volrobustz_504d_base_v020_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    med = v_.rolling(756, min_periods=max(2, 756 // 2)).median()
    mad = (v_ - med).abs().rolling(756, min_periods=max(2, 756 // 2)).median()
    result = (v_ - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol deviation from longer mean
def f06vr_f06_semi_volatility_regime_voldev_21d_base_v021_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = v_ - _mean(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol deviation from longer mean
def f06vr_f06_semi_volatility_regime_voldev_63d_base_v022_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = v_ - _mean(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol deviation from longer mean
def f06vr_f06_semi_volatility_regime_voldev_126d_base_v023_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = v_ - _mean(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol deviation from longer mean
def f06vr_f06_semi_volatility_regime_voldev_252d_base_v024_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = v_ - _mean(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol deviation from longer mean
def f06vr_f06_semi_volatility_regime_voldev_504d_base_v025_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = v_ - _mean(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of high-vol days (vol > rolling median)
def f06vr_f06_semi_volatility_regime_volhi_21d_base_v026_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    thr = v_.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (v_ > thr).astype(float).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of high-vol days (vol > rolling median)
def f06vr_f06_semi_volatility_regime_volhi_63d_base_v027_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    thr = v_.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (v_ > thr).astype(float).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of high-vol days (vol > rolling median)
def f06vr_f06_semi_volatility_regime_volhi_126d_base_v028_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    thr = v_.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (v_ > thr).astype(float).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-vol days (vol > rolling median)
def f06vr_f06_semi_volatility_regime_volhi_252d_base_v029_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    thr = v_.rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (v_ > thr).astype(float).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of high-vol days (vol > rolling median)
def f06vr_f06_semi_volatility_regime_volhi_504d_base_v030_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    thr = v_.rolling(756, min_periods=max(1, 756 // 2)).median()
    result = (v_ > thr).astype(float).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of high-vol days
def f06vr_f06_semi_volatility_regime_volhifrac_21d_base_v031_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    thr = v_.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (v_ > thr).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of high-vol days
def f06vr_f06_semi_volatility_regime_volhifrac_63d_base_v032_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    thr = v_.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (v_ > thr).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of high-vol days
def f06vr_f06_semi_volatility_regime_volhifrac_126d_base_v033_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    thr = v_.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (v_ > thr).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of high-vol days
def f06vr_f06_semi_volatility_regime_volhifrac_252d_base_v034_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    thr = v_.rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (v_ > thr).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of high-vol days
def f06vr_f06_semi_volatility_regime_volhifrac_504d_base_v035_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    thr = v_.rolling(756, min_periods=max(1, 756 // 2)).median()
    result = (v_ > thr).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_base_v036_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = _std(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_base_v037_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = _std(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_base_v038_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = _std(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_base_v039_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = _std(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_base_v040_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = _std(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of rolling vol
def f06vr_f06_semi_volatility_regime_volmax_21d_base_v041_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = _max(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of rolling vol
def f06vr_f06_semi_volatility_regime_volmax_63d_base_v042_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = _max(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of rolling vol
def f06vr_f06_semi_volatility_regime_volmax_126d_base_v043_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = _max(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of rolling vol
def f06vr_f06_semi_volatility_regime_volmax_252d_base_v044_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = _max(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of rolling vol
def f06vr_f06_semi_volatility_regime_volmax_504d_base_v045_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = _max(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of rolling vol
def f06vr_f06_semi_volatility_regime_volmin_21d_base_v046_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = _min(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of rolling vol
def f06vr_f06_semi_volatility_regime_volmin_63d_base_v047_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = _min(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of rolling vol
def f06vr_f06_semi_volatility_regime_volmin_126d_base_v048_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = _min(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of rolling vol
def f06vr_f06_semi_volatility_regime_volmin_252d_base_v049_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = _min(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of rolling vol
def f06vr_f06_semi_volatility_regime_volmin_504d_base_v050_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = _min(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of rolling vol
def f06vr_f06_semi_volatility_regime_volrng_21d_base_v051_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = _max(v_, 63) - _min(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of rolling vol
def f06vr_f06_semi_volatility_regime_volrng_63d_base_v052_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = _max(v_, 126) - _min(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of rolling vol
def f06vr_f06_semi_volatility_regime_volrng_126d_base_v053_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = _max(v_, 252) - _min(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of rolling vol
def f06vr_f06_semi_volatility_regime_volrng_252d_base_v054_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = _max(v_, 504) - _min(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of rolling vol
def f06vr_f06_semi_volatility_regime_volrng_504d_base_v055_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = _max(v_, 756) - _min(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol position in rolling range
def f06vr_f06_semi_volatility_regime_volpos_21d_base_v056_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    lo, hi = _min(v_, 63), _max(v_, 63)
    result = (v_ - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol position in rolling range
def f06vr_f06_semi_volatility_regime_volpos_63d_base_v057_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    lo, hi = _min(v_, 126), _max(v_, 126)
    result = (v_ - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol position in rolling range
def f06vr_f06_semi_volatility_regime_volpos_126d_base_v058_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    lo, hi = _min(v_, 252), _max(v_, 252)
    result = (v_ - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol position in rolling range
def f06vr_f06_semi_volatility_regime_volpos_252d_base_v059_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    lo, hi = _min(v_, 504), _max(v_, 504)
    result = (v_ - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol position in rolling range
def f06vr_f06_semi_volatility_regime_volpos_504d_base_v060_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    lo, hi = _min(v_, 756), _max(v_, 756)
    result = (v_ - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol drop from rolling peak vol
def f06vr_f06_semi_volatility_regime_voldd_21d_base_v061_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = v_ - _max(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol drop from rolling peak vol
def f06vr_f06_semi_volatility_regime_voldd_63d_base_v062_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = v_ - _max(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol drop from rolling peak vol
def f06vr_f06_semi_volatility_regime_voldd_126d_base_v063_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = v_ - _max(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol drop from rolling peak vol
def f06vr_f06_semi_volatility_regime_voldd_252d_base_v064_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = v_ - _max(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol drop from rolling peak vol
def f06vr_f06_semi_volatility_regime_voldd_504d_base_v065_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = v_ - _max(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol rise from rolling trough vol
def f06vr_f06_semi_volatility_regime_volrunup_21d_base_v066_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = v_ - _min(v_, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol rise from rolling trough vol
def f06vr_f06_semi_volatility_regime_volrunup_63d_base_v067_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = v_ - _min(v_, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol rise from rolling trough vol
def f06vr_f06_semi_volatility_regime_volrunup_126d_base_v068_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = v_ - _min(v_, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol rise from rolling trough vol
def f06vr_f06_semi_volatility_regime_volrunup_252d_base_v069_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = v_ - _min(v_, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol rise from rolling trough vol
def f06vr_f06_semi_volatility_regime_volrunup_504d_base_v070_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = v_ - _min(v_, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of 21d vol
def f06vr_f06_semi_volatility_regime_volema_5v21_base_v071_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    result = v_.ewm(span=5, adjust=False).mean() - v_.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of 63d vol
def f06vr_f06_semi_volatility_regime_volema_21v63_base_v072_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    result = v_.ewm(span=21, adjust=False).mean() - v_.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of 126d vol
def f06vr_f06_semi_volatility_regime_volema_63v126_base_v073_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    result = v_.ewm(span=63, adjust=False).mean() - v_.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of 252d vol
def f06vr_f06_semi_volatility_regime_volema_126v252_base_v074_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    result = v_.ewm(span=126, adjust=False).mean() - v_.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of 504d vol
def f06vr_f06_semi_volatility_regime_volema_252v504_base_v075_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    result = v_.ewm(span=252, adjust=False).mean() - v_.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


