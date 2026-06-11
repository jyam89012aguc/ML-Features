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


# 5d slope of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_slope_v001_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_slope_v002_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_slope_v003_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_slope_v004_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d accel
def f11ac_f11_semi_acceleration_accel_21d_slope_v005_signal(closeadj):
    base = _f11_accel(closeadj, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_slope_v006_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_slope_v007_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_slope_v008_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_slope_v009_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d accel
def f11ac_f11_semi_acceleration_accel_63d_slope_v010_signal(closeadj):
    base = _f11_accel(closeadj, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_slope_v011_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_slope_v012_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_slope_v013_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_slope_v014_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d accel
def f11ac_f11_semi_acceleration_accel_126d_slope_v015_signal(closeadj):
    base = _f11_accel(closeadj, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_slope_v016_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_slope_v017_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_slope_v018_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_slope_v019_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d accel
def f11ac_f11_semi_acceleration_accel_252d_slope_v020_signal(closeadj):
    base = _f11_accel(closeadj, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_slope_v021_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_slope_v022_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_slope_v023_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_slope_v024_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d logaccel
def f11ac_f11_semi_acceleration_logaccel_21d_slope_v025_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    base = lr - lr.shift(21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_slope_v026_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_slope_v027_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_slope_v028_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_slope_v029_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d logaccel
def f11ac_f11_semi_acceleration_logaccel_63d_slope_v030_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    base = lr - lr.shift(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_slope_v031_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_slope_v032_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_slope_v033_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_slope_v034_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d logaccel
def f11ac_f11_semi_acceleration_logaccel_126d_slope_v035_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    base = lr - lr.shift(126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_slope_v036_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_slope_v037_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_slope_v038_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_slope_v039_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d logaccel
def f11ac_f11_semi_acceleration_logaccel_252d_slope_v040_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    base = lr - lr.shift(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_slope_v041_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_slope_v042_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_slope_v043_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_slope_v044_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d accelz
def f11ac_f11_semi_acceleration_accelz_21d_slope_v045_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_slope_v046_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_slope_v047_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_slope_v048_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_slope_v049_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d accelz
def f11ac_f11_semi_acceleration_accelz_63d_slope_v050_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_slope_v051_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_slope_v052_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_slope_v053_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_slope_v054_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d accelz
def f11ac_f11_semi_acceleration_accelz_126d_slope_v055_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_slope_v056_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_slope_v057_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_slope_v058_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_slope_v059_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d accelz
def f11ac_f11_semi_acceleration_accelz_252d_slope_v060_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _z(a, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_slope_v061_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_slope_v062_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_slope_v063_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_slope_v064_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_63d_slope_v065_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_slope_v066_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_slope_v067_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_slope_v068_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_slope_v069_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_126d_slope_v070_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_slope_v071_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_slope_v072_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_slope_v073_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_slope_v074_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d cumaccel21
def f11ac_f11_semi_acceleration_cumaccel21_252d_slope_v075_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_slope_v076_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_slope_v077_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_slope_v078_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_slope_v079_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_21d_slope_v080_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_slope_v081_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_slope_v082_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_slope_v083_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_slope_v084_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_63d_slope_v085_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_slope_v086_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_slope_v087_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_slope_v088_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_slope_v089_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_126d_slope_v090_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_slope_v091_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_slope_v092_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_slope_v093_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_slope_v094_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d accelstd21
def f11ac_f11_semi_acceleration_accelstd21_252d_slope_v095_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _std(a, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_slope_v096_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_slope_v097_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_slope_v098_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_slope_v099_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_63d_slope_v100_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_slope_v101_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_slope_v102_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_slope_v103_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_slope_v104_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d accelposhit
def f11ac_f11_semi_acceleration_accelposhit_252d_slope_v105_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_slope_v106_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_slope_v107_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_slope_v108_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_slope_v109_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_63d_slope_v110_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_slope_v111_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_slope_v112_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_slope_v113_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_slope_v114_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d accelnormvol
def f11ac_f11_semi_acceleration_accelnormvol_252d_slope_v115_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    base = a / v.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_slope_v116_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_slope_v117_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_slope_v118_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_slope_v119_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d jerk
def f11ac_f11_semi_acceleration_jerk_63d_slope_v120_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    base = a - a.shift(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_slope_v121_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_slope_v122_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_slope_v123_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_slope_v124_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d jerk
def f11ac_f11_semi_acceleration_jerk_252d_slope_v125_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    base = a - a.shift(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_slope_v126_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_slope_v127_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_slope_v128_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_slope_v129_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d emaaccel21v63
def f11ac_f11_semi_acceleration_emaaccel21v63_63d_slope_v130_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_slope_v131_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_slope_v132_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_slope_v133_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_slope_v134_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d emaaccel63v126
def f11ac_f11_semi_acceleration_emaaccel63v126_126d_slope_v135_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_slope_v136_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_slope_v137_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_slope_v138_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_slope_v139_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d accelir
def f11ac_f11_semi_acceleration_accelir_63d_slope_v140_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 63) / _std(a, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_slope_v141_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_slope_v142_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_slope_v143_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_slope_v144_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d accelir
def f11ac_f11_semi_acceleration_accelir_252d_slope_v145_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = _mean(a, 252) / _std(a, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_slope_v146_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_slope_v147_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_slope_v148_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_slope_v149_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d acceldd
def f11ac_f11_semi_acceleration_acceldd_63d_slope_v150_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    base = a - _max(a, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
