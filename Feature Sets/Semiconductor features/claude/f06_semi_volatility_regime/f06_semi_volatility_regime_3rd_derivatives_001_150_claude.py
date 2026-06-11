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


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f06_ret(s):
    return s.pct_change()


def _f06_logret(s):
    return np.log(s / s.shift(1))


def _f06_realvol(r, w):
    return r.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(252)

# 5d curv of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_curv_v001_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_curv_v002_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_curv_v003_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_curv_v004_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d realized vol
def f06vr_f06_semi_volatility_regime_realvol_21d_curv_v005_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_curv_v006_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_curv_v007_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_curv_v008_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_curv_v009_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d realized vol
def f06vr_f06_semi_volatility_regime_realvol_63d_curv_v010_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_curv_v011_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_curv_v012_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_curv_v013_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_curv_v014_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d realized vol
def f06vr_f06_semi_volatility_regime_realvol_126d_curv_v015_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_curv_v016_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_curv_v017_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_curv_v018_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_curv_v019_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d realized vol
def f06vr_f06_semi_volatility_regime_realvol_252d_curv_v020_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_curv_v021_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_curv_v022_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_curv_v023_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_curv_v024_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d realized vol
def f06vr_f06_semi_volatility_regime_realvol_504d_curv_v025_signal(closeadj):
    r = _f06_ret(closeadj)
    base = _f06_realvol(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_curv_v026_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_curv_v027_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_curv_v028_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_curv_v029_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d vol z-score
def f06vr_f06_semi_volatility_regime_volz_21d_curv_v030_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = (v_ - v_.rolling(63, min_periods=max(1, 63 // 2)).mean()) / v_.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_curv_v031_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_curv_v032_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_curv_v033_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_curv_v034_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d vol z-score
def f06vr_f06_semi_volatility_regime_volz_63d_curv_v035_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = (v_ - v_.rolling(126, min_periods=max(1, 126 // 2)).mean()) / v_.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_curv_v036_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_curv_v037_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_curv_v038_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_curv_v039_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d vol z-score
def f06vr_f06_semi_volatility_regime_volz_126d_curv_v040_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = (v_ - v_.rolling(252, min_periods=max(1, 252 // 2)).mean()) / v_.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_curv_v041_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_curv_v042_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_curv_v043_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_curv_v044_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d vol z-score
def f06vr_f06_semi_volatility_regime_volz_252d_curv_v045_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = (v_ - v_.rolling(504, min_periods=max(1, 504 // 2)).mean()) / v_.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_curv_v046_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_curv_v047_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_curv_v048_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_curv_v049_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d vol z-score
def f06vr_f06_semi_volatility_regime_volz_504d_curv_v050_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = (v_ - v_.rolling(756, min_periods=max(1, 756 // 2)).mean()) / v_.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_curv_v051_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_curv_v052_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_curv_v053_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_curv_v054_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_21d_curv_v055_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = v_ - _mean(v_, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_curv_v056_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_curv_v057_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_curv_v058_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_curv_v059_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_63d_curv_v060_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = v_ - _mean(v_, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_curv_v061_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_curv_v062_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_curv_v063_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_curv_v064_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_126d_curv_v065_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = v_ - _mean(v_, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_curv_v066_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_curv_v067_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_curv_v068_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_curv_v069_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_252d_curv_v070_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = v_ - _mean(v_, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_curv_v071_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_curv_v072_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_curv_v073_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_curv_v074_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d vol deviation
def f06vr_f06_semi_volatility_regime_voldev_504d_curv_v075_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = v_ - _mean(v_, 756)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_curv_v076_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_curv_v077_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_curv_v078_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_curv_v079_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_21d_curv_v080_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 21)
    base = _std(v_, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_curv_v081_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_curv_v082_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_curv_v083_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_curv_v084_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_63d_curv_v085_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 63)
    base = _std(v_, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_curv_v086_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_curv_v087_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_curv_v088_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_curv_v089_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_126d_curv_v090_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 126)
    base = _std(v_, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_curv_v091_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_curv_v092_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_curv_v093_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_curv_v094_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_252d_curv_v095_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 252)
    base = _std(v_, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_curv_v096_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_curv_v097_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_curv_v098_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_curv_v099_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d vol-of-vol
def f06vr_f06_semi_volatility_regime_volofvol_504d_curv_v100_signal(closeadj):
    r = _f06_ret(closeadj)
    v_ = _f06_realvol(r, 504)
    base = _std(v_, 756)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_curv_v101_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_curv_v102_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_curv_v103_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_curv_v104_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d downside vol
def f06vr_f06_semi_volatility_regime_downvol_21d_curv_v105_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 21) * np.sqrt(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_curv_v106_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_curv_v107_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_curv_v108_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_curv_v109_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d downside vol
def f06vr_f06_semi_volatility_regime_downvol_63d_curv_v110_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 63) * np.sqrt(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_curv_v111_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_curv_v112_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_curv_v113_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_curv_v114_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d downside vol
def f06vr_f06_semi_volatility_regime_downvol_126d_curv_v115_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 126) * np.sqrt(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_curv_v116_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_curv_v117_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_curv_v118_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_curv_v119_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d downside vol
def f06vr_f06_semi_volatility_regime_downvol_252d_curv_v120_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 252) * np.sqrt(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_curv_v121_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_curv_v122_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_curv_v123_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_curv_v124_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d downside vol
def f06vr_f06_semi_volatility_regime_downvol_504d_curv_v125_signal(closeadj):
    r = _f06_ret(closeadj)
    neg = r.where(r < 0)
    base = _std(neg, 504) * np.sqrt(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_curv_v126_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_curv_v127_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_curv_v128_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_curv_v129_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_21d_curv_v130_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 21) * np.sqrt(252)
    uv = _std(r.where(r > 0), 21) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_curv_v131_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_curv_v132_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_curv_v133_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_curv_v134_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_63d_curv_v135_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 63) * np.sqrt(252)
    uv = _std(r.where(r > 0), 63) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_curv_v136_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_curv_v137_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_curv_v138_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_curv_v139_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_126d_curv_v140_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 126) * np.sqrt(252)
    uv = _std(r.where(r > 0), 126) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_curv_v141_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_curv_v142_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_curv_v143_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_curv_v144_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_252d_curv_v145_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 252) * np.sqrt(252)
    uv = _std(r.where(r > 0), 252) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_curv_v146_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_curv_v147_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_curv_v148_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_curv_v149_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d vol asymmetry
def f06vr_f06_semi_volatility_regime_volasym_504d_curv_v150_signal(closeadj):
    r = _f06_ret(closeadj)
    dv = _std(r.where(r < 0), 504) * np.sqrt(252)
    uv = _std(r.where(r > 0), 504) * np.sqrt(252)
    base = dv - uv
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


