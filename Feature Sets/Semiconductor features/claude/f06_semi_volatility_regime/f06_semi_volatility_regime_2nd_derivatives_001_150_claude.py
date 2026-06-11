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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f06_ret(s):
    return s.pct_change()


def _f06_logret(s):
    return np.log(s / s.shift(1))


def _f06_realvol(r, w):
    return r.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(252)

# 5d slope of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_slope_v001_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_slope_v002_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_slope_v003_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_slope_v004_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_slope_v005_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_slope_v006_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_slope_v007_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_slope_v008_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_slope_v009_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_slope_v010_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_slope_v011_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_slope_v012_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_slope_v013_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_slope_v014_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_slope_v015_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_slope_v016_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_slope_v017_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_slope_v018_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_slope_v019_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_slope_v020_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_slope_v021_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_slope_v022_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_slope_v023_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_slope_v024_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_slope_v025_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_slope_v026_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_slope_v027_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_slope_v028_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_slope_v029_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_slope_v030_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_slope_v031_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_slope_v032_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_slope_v033_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_slope_v034_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_slope_v035_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_slope_v036_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_slope_v037_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_slope_v038_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_slope_v039_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_slope_v040_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_slope_v041_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_slope_v042_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_slope_v043_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_slope_v044_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_slope_v045_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_slope_v046_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_slope_v047_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_slope_v048_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_slope_v049_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_slope_v050_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_slope_v051_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_slope_v052_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_slope_v053_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_slope_v054_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_slope_v055_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_slope_v056_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_slope_v057_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_slope_v058_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_slope_v059_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_slope_v060_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_slope_v061_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_slope_v062_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_slope_v063_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_slope_v064_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_slope_v065_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_slope_v066_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_slope_v067_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_slope_v068_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_slope_v069_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_slope_v070_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_slope_v071_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_slope_v072_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_slope_v073_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_slope_v074_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_slope_v075_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_slope_v076_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_slope_v077_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_slope_v078_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_slope_v079_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_slope_v080_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_slope_v081_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_slope_v082_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_slope_v083_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_slope_v084_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_slope_v085_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_slope_v086_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_slope_v087_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_slope_v088_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_slope_v089_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_slope_v090_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_slope_v091_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_slope_v092_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_slope_v093_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_slope_v094_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_slope_v095_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_slope_v096_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_slope_v097_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_slope_v098_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_slope_v099_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_slope_v100_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_slope_v101_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_slope_v102_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_slope_v103_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_slope_v104_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_slope_v105_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_slope_v106_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_slope_v107_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_slope_v108_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_slope_v109_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_slope_v110_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_slope_v111_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_slope_v112_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_slope_v113_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_slope_v114_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_slope_v115_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_slope_v116_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_slope_v117_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_slope_v118_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_slope_v119_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_slope_v120_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_slope_v121_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_slope_v122_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_slope_v123_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_slope_v124_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_slope_v125_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_slope_v126_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_slope_v127_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_slope_v128_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_slope_v129_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_slope_v130_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_slope_v131_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_slope_v132_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_slope_v133_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_slope_v134_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_slope_v135_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_slope_v136_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_slope_v137_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_slope_v138_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_slope_v139_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_slope_v140_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_slope_v141_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_slope_v142_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_slope_v143_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_slope_v144_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_slope_v145_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_slope_v146_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_slope_v147_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_slope_v148_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_slope_v149_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_slope_v150_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


