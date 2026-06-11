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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


# ===== folder domain primitives =====
def _f11_own_ret(s):
    return s.pct_change()


def _f11_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f11_mom(s, n):
    return s / s.shift(n) - 1.0


def _f11_accel(s, n):
    return (s / s.shift(n) - 1.0) - (s.shift(n) / s.shift(2 * n) - 1.0)


# 5d curvature of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_curv_v001_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_curv_v002_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_curv_v003_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_curv_v004_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_curv_v005_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_curv_v006_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_curv_v007_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_curv_v008_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_curv_v009_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_curv_v010_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_curv_v011_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_curv_v012_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_curv_v013_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_curv_v014_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_curv_v015_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_curv_v016_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_curv_v017_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_curv_v018_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_curv_v019_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_curv_v020_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_curv_v021_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_curv_v022_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_curv_v023_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_curv_v024_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_curv_v025_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_curv_v026_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_curv_v027_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_curv_v028_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_curv_v029_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_curv_v030_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_curv_v031_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_curv_v032_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_curv_v033_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_curv_v034_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_curv_v035_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_curv_v036_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_curv_v037_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_curv_v038_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_curv_v039_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_curv_v040_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_curv_v041_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_curv_v042_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_curv_v043_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_curv_v044_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_curv_v045_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_curv_v046_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_curv_v047_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_curv_v048_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_curv_v049_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_curv_v050_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_curv_v051_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_curv_v052_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_curv_v053_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_curv_v054_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_curv_v055_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_curv_v056_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_curv_v057_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_curv_v058_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_curv_v059_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_curv_v060_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_curv_v061_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_curv_v062_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_curv_v063_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_curv_v064_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_curv_v065_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_curv_v066_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_curv_v067_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_curv_v068_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_curv_v069_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_curv_v070_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_curv_v071_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_curv_v072_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_curv_v073_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_curv_v074_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_curv_v075_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_curv_v076_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_curv_v077_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_curv_v078_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_curv_v079_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_curv_v080_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_curv_v081_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_curv_v082_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_curv_v083_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_curv_v084_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_curv_v085_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_curv_v086_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_curv_v087_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_curv_v088_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_curv_v089_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_curv_v090_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_curv_v091_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_curv_v092_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_curv_v093_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_curv_v094_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_curv_v095_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_curv_v096_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_curv_v097_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_curv_v098_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_curv_v099_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_curv_v100_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_curv_v101_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_curv_v102_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_curv_v103_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_curv_v104_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_curv_v105_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_curv_v106_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_curv_v107_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_curv_v108_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_curv_v109_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_curv_v110_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_curv_v111_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_curv_v112_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_curv_v113_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_curv_v114_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_curv_v115_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_curv_v116_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_curv_v117_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_curv_v118_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_curv_v119_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_curv_v120_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_curv_v121_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_curv_v122_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_curv_v123_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_curv_v124_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_curv_v125_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_curv_v126_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_curv_v127_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_curv_v128_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_curv_v129_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_curv_v130_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_curv_v131_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_curv_v132_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_curv_v133_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_curv_v134_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_curv_v135_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_curv_v136_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_curv_v137_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_curv_v138_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_curv_v139_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_curv_v140_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_curv_v141_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_curv_v142_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_curv_v143_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_curv_v144_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_curv_v145_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_curv_v146_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_curv_v147_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_curv_v148_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_curv_v149_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_curv_v150_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
