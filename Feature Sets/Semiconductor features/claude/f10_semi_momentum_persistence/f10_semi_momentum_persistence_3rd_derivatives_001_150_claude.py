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


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f10_own_ret(s):
    return s.pct_change()


def _f10_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f10_streak_up(r):
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    return sign.groupby(grp).cumsum().where(sign > 0, 0.0)


def _f10_streak_dn(r):
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    return (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)


def _f10_autocorr(r, w, lag):
    return r.rolling(w, min_periods=max(2, w // 2)).corr(r.shift(lag))


# 5d curvature of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_curv_v001_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_curv_v002_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_curv_v003_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_curv_v004_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_curv_v005_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_curv_v006_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_curv_v007_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_curv_v008_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_curv_v009_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_curv_v010_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_curv_v011_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_curv_v012_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_curv_v013_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_curv_v014_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_curv_v015_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_curv_v016_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_curv_v017_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_curv_v018_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_curv_v019_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_curv_v020_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_curv_v021_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_curv_v022_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_curv_v023_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_curv_v024_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_curv_v025_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_curv_v026_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_curv_v027_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_curv_v028_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_curv_v029_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_curv_v030_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_curv_v031_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_curv_v032_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_curv_v033_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_curv_v034_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_curv_v035_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_curv_v036_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_curv_v037_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_curv_v038_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_curv_v039_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_curv_v040_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_curv_v041_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_curv_v042_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_curv_v043_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_curv_v044_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_curv_v045_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_curv_v046_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_curv_v047_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_curv_v048_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_curv_v049_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_curv_v050_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_curv_v051_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_curv_v052_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_curv_v053_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_curv_v054_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_curv_v055_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_curv_v056_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_curv_v057_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_curv_v058_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_curv_v059_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_curv_v060_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_curv_v061_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_curv_v062_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_curv_v063_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_curv_v064_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_curv_v065_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_curv_v066_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_curv_v067_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_curv_v068_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_curv_v069_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_curv_v070_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_curv_v071_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_curv_v072_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_curv_v073_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_curv_v074_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_curv_v075_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_curv_v076_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_curv_v077_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_curv_v078_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_curv_v079_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_curv_v080_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_curv_v081_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_curv_v082_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_curv_v083_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_curv_v084_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_curv_v085_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_curv_v086_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_curv_v087_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_curv_v088_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_curv_v089_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_curv_v090_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_curv_v091_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_curv_v092_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_curv_v093_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_curv_v094_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_curv_v095_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_curv_v096_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_curv_v097_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_curv_v098_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_curv_v099_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_curv_v100_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_curv_v101_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_curv_v102_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_curv_v103_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_curv_v104_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_curv_v105_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_curv_v106_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_curv_v107_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_curv_v108_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_curv_v109_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_curv_v110_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_curv_v111_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_curv_v112_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_curv_v113_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_curv_v114_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_curv_v115_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_curv_v116_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_curv_v117_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_curv_v118_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_curv_v119_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_curv_v120_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_curv_v121_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_curv_v122_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_curv_v123_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_curv_v124_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_curv_v125_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_curv_v126_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_curv_v127_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_curv_v128_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_curv_v129_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_curv_v130_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_curv_v131_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_curv_v132_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_curv_v133_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_curv_v134_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_curv_v135_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_curv_v136_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_curv_v137_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_curv_v138_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_curv_v139_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_curv_v140_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_curv_v141_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_curv_v142_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_curv_v143_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_curv_v144_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_curv_v145_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_curv_v146_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_curv_v147_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_curv_v148_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_curv_v149_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_curv_v150_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
