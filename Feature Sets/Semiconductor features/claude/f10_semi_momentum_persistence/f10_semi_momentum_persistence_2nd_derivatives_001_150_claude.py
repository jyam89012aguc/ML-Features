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


# 5d slope of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_slope_v001_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_slope_v002_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_slope_v003_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_slope_v004_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d ac1
def f10mp_f10_semi_momentum_persistence_ac1_21d_slope_v005_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(21, min_periods=11).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_slope_v006_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_slope_v007_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_slope_v008_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_slope_v009_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d ac1
def f10mp_f10_semi_momentum_persistence_ac1_63d_slope_v010_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_slope_v011_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_slope_v012_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_slope_v013_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_slope_v014_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d ac1
def f10mp_f10_semi_momentum_persistence_ac1_126d_slope_v015_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_slope_v016_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_slope_v017_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_slope_v018_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_slope_v019_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d ac1
def f10mp_f10_semi_momentum_persistence_ac1_252d_slope_v020_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_slope_v021_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_slope_v022_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_slope_v023_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_slope_v024_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d ac5
def f10mp_f10_semi_momentum_persistence_ac5_63d_slope_v025_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(63, min_periods=32).corr(r.shift(5))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_slope_v026_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_slope_v027_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_slope_v028_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_slope_v029_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d ac5
def f10mp_f10_semi_momentum_persistence_ac5_126d_slope_v030_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(5))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_slope_v031_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_slope_v032_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_slope_v033_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_slope_v034_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d ac5
def f10mp_f10_semi_momentum_persistence_ac5_252d_slope_v035_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(5))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_slope_v036_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_slope_v037_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_slope_v038_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_slope_v039_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d ac21
def f10mp_f10_semi_momentum_persistence_ac21_126d_slope_v040_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(126, min_periods=63).corr(r.shift(21))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_slope_v041_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_slope_v042_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_slope_v043_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_slope_v044_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d ac21
def f10mp_f10_semi_momentum_persistence_ac21_252d_slope_v045_signal(closeadj):
    r = closeadj.pct_change()
    base = r.rolling(252, min_periods=126).corr(r.shift(21))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_slope_v046_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_slope_v047_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_slope_v048_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_slope_v049_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d absac1
def f10mp_f10_semi_momentum_persistence_absac1_63d_slope_v050_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_slope_v051_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_slope_v052_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_slope_v053_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_slope_v054_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d absac1
def f10mp_f10_semi_momentum_persistence_absac1_126d_slope_v055_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(126, min_periods=63).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_slope_v056_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_slope_v057_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_slope_v058_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_slope_v059_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d absac1
def f10mp_f10_semi_momentum_persistence_absac1_252d_slope_v060_signal(closeadj):
    r = closeadj.pct_change().abs()
    base = r.rolling(252, min_periods=126).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_slope_v061_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_slope_v062_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_slope_v063_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_slope_v064_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d poshit
def f10mp_f10_semi_momentum_persistence_poshit_21d_slope_v065_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_slope_v066_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_slope_v067_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_slope_v068_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_slope_v069_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d poshit
def f10mp_f10_semi_momentum_persistence_poshit_63d_slope_v070_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_slope_v071_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_slope_v072_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_slope_v073_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_slope_v074_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d poshit
def f10mp_f10_semi_momentum_persistence_poshit_126d_slope_v075_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_slope_v076_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_slope_v077_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_slope_v078_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_slope_v079_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d poshit
def f10mp_f10_semi_momentum_persistence_poshit_252d_slope_v080_signal(closeadj):
    r = closeadj.pct_change()
    base = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_slope_v081_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_slope_v082_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_slope_v083_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_slope_v084_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d effratio
def f10mp_f10_semi_momentum_persistence_effratio_21d_slope_v085_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(21, min_periods=11).sum()
    d = r.abs().rolling(21, min_periods=11).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_slope_v086_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_slope_v087_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_slope_v088_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_slope_v089_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d effratio
def f10mp_f10_semi_momentum_persistence_effratio_63d_slope_v090_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(63, min_periods=32).sum()
    d = r.abs().rolling(63, min_periods=32).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_slope_v091_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_slope_v092_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_slope_v093_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_slope_v094_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d effratio
def f10mp_f10_semi_momentum_persistence_effratio_126d_slope_v095_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(126, min_periods=63).sum()
    d = r.abs().rolling(126, min_periods=63).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_slope_v096_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_slope_v097_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_slope_v098_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_slope_v099_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d effratio
def f10mp_f10_semi_momentum_persistence_effratio_252d_slope_v100_signal(closeadj):
    r = closeadj.pct_change()
    n = r.rolling(252, min_periods=126).sum()
    d = r.abs().rolling(252, min_periods=126).sum()
    base = n / d.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_slope_v101_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_slope_v102_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_slope_v103_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_slope_v104_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_63d_slope_v105_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=32).var()
    v5 = r5.rolling(63, min_periods=32).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_slope_v106_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_slope_v107_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_slope_v108_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_slope_v109_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d varratio5
def f10mp_f10_semi_momentum_persistence_varratio5_252d_slope_v110_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    base = v5 / (5 * v1).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_slope_v111_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_slope_v112_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_slope_v113_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_slope_v114_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d ker
def f10mp_f10_semi_momentum_persistence_ker_63d_slope_v115_signal(closeadj):
    num = (closeadj - closeadj.shift(63)).abs()
    den = closeadj.diff().abs().rolling(63, min_periods=32).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_slope_v116_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_slope_v117_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_slope_v118_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_slope_v119_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d ker
def f10mp_f10_semi_momentum_persistence_ker_252d_slope_v120_signal(closeadj):
    num = (closeadj - closeadj.shift(252)).abs()
    den = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = num / den.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_slope_v121_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_slope_v122_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_slope_v123_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_slope_v124_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_63d_slope_v125_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 63).abs() / _std(r, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_slope_v126_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_slope_v127_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_slope_v128_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_slope_v129_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d trendstrength
def f10mp_f10_semi_momentum_persistence_trendstrength_252d_slope_v130_signal(closeadj):
    r = closeadj.pct_change()
    base = _mean(r, 252).abs() / _std(r, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_slope_v131_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_slope_v132_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_slope_v133_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_slope_v134_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d turnct
def f10mp_f10_semi_momentum_persistence_turnct_63d_slope_v135_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_slope_v136_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_slope_v137_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_slope_v138_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_slope_v139_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d turnct
def f10mp_f10_semi_momentum_persistence_turnct_252d_slope_v140_signal(closeadj):
    r = closeadj.pct_change()
    sc = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    base = sc.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_slope_v141_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_slope_v142_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_slope_v143_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_slope_v144_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d rsproxy
def f10mp_f10_semi_momentum_persistence_rsproxy_63d_slope_v145_signal(closeadj):
    r = closeadj.pct_change()
    rng = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    sd = r.rolling(63, min_periods=32).std()
    base = rng / sd.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_slope_v146_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_slope_v147_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_slope_v148_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_slope_v149_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d halflife
def f10mp_f10_semi_momentum_persistence_halflife_63d_slope_v150_signal(closeadj):
    r = closeadj.pct_change()
    base = 1.0 - r.rolling(63, min_periods=32).corr(r.shift(1))
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
