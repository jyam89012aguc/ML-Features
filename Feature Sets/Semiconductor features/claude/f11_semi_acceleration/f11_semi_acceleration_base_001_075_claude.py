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
def _f11_own_ret(s):
    return s.pct_change()


def _f11_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f11_mom(s, n):
    return s / s.shift(n) - 1.0


def _f11_accel(s, n):
    return (s / s.shift(n) - 1.0) - (s.shift(n) / s.shift(2 * n) - 1.0)


# 21d acceleration (ret_w minus prior ret_w)
def f11ac_f11_semi_acceleration_accel_21d_base_v001_signal(closeadj):
    result = _f11_accel(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration (ret_w minus prior ret_w)
def f11ac_f11_semi_acceleration_accel_63d_base_v002_signal(closeadj):
    result = _f11_accel(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration (ret_w minus prior ret_w)
def f11ac_f11_semi_acceleration_accel_126d_base_v003_signal(closeadj):
    result = _f11_accel(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration (ret_w minus prior ret_w)
def f11ac_f11_semi_acceleration_accel_252d_base_v004_signal(closeadj):
    result = _f11_accel(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration (ret_w minus prior ret_w)
def f11ac_f11_semi_acceleration_accel_504d_base_v005_signal(closeadj):
    result = _f11_accel(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-return acceleration
def f11ac_f11_semi_acceleration_logaccel_21d_base_v006_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    result = lr - lr.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-return acceleration
def f11ac_f11_semi_acceleration_logaccel_63d_base_v007_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(63))
    result = lr - lr.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-return acceleration
def f11ac_f11_semi_acceleration_logaccel_126d_base_v008_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(126))
    result = lr - lr.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-return acceleration
def f11ac_f11_semi_acceleration_logaccel_252d_base_v009_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(252))
    result = lr - lr.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-return acceleration
def f11ac_f11_semi_acceleration_logaccel_504d_base_v010_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(504))
    result = lr - lr.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# momentum spread (return_5 - return_21) acceleration
def f11ac_f11_semi_acceleration_momspread_5v21_base_v011_signal(closeadj):
    short = closeadj / closeadj.shift(5) - 1.0
    long = closeadj / closeadj.shift(21) - 1.0
    result = short - long
    return result.replace([np.inf, -np.inf], np.nan)


# momentum spread (return_21 - return_63) acceleration
def f11ac_f11_semi_acceleration_momspread_21v63_base_v012_signal(closeadj):
    short = closeadj / closeadj.shift(21) - 1.0
    long = closeadj / closeadj.shift(63) - 1.0
    result = short - long
    return result.replace([np.inf, -np.inf], np.nan)


# momentum spread (return_63 - return_126) acceleration
def f11ac_f11_semi_acceleration_momspread_63v126_base_v013_signal(closeadj):
    short = closeadj / closeadj.shift(63) - 1.0
    long = closeadj / closeadj.shift(126) - 1.0
    result = short - long
    return result.replace([np.inf, -np.inf], np.nan)


# momentum spread (return_126 - return_252) acceleration
def f11ac_f11_semi_acceleration_momspread_126v252_base_v014_signal(closeadj):
    short = closeadj / closeadj.shift(126) - 1.0
    long = closeadj / closeadj.shift(252) - 1.0
    result = short - long
    return result.replace([np.inf, -np.inf], np.nan)


# momentum spread (return_252 - return_504) acceleration
def f11ac_f11_semi_acceleration_momspread_252v504_base_v015_signal(closeadj):
    short = closeadj / closeadj.shift(252) - 1.0
    long = closeadj / closeadj.shift(504) - 1.0
    result = short - long
    return result.replace([np.inf, -np.inf], np.nan)


# 21d first-diff of rolling mean return
def f11ac_f11_semi_acceleration_diffmeanret_21d_base_v016_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 21)
    result = m - m.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d first-diff of rolling mean return
def f11ac_f11_semi_acceleration_diffmeanret_63d_base_v017_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 63)
    result = m - m.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d first-diff of rolling mean return
def f11ac_f11_semi_acceleration_diffmeanret_126d_base_v018_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 126)
    result = m - m.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d first-diff of rolling mean return
def f11ac_f11_semi_acceleration_diffmeanret_252d_base_v019_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 252)
    result = m - m.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d first-diff of rolling mean return
def f11ac_f11_semi_acceleration_diffmeanret_504d_base_v020_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 504)
    result = m - m.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of acceleration
def f11ac_f11_semi_acceleration_accelz_21d_base_v021_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _z(a, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of acceleration
def f11ac_f11_semi_acceleration_accelz_63d_base_v022_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    result = _z(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of acceleration
def f11ac_f11_semi_acceleration_accelz_126d_base_v023_signal(closeadj):
    a = _f11_accel(closeadj, 126)
    result = _z(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of acceleration
def f11ac_f11_semi_acceleration_accelz_252d_base_v024_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    result = _z(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of acceleration
def f11ac_f11_semi_acceleration_accelz_504d_base_v025_signal(closeadj):
    a = _f11_accel(closeadj, 504)
    result = _z(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sign of acceleration
def f11ac_f11_semi_acceleration_accelsign_21d_base_v026_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = pd.Series(np.sign(a), index=a.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sign of acceleration
def f11ac_f11_semi_acceleration_accelsign_63d_base_v027_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    result = pd.Series(np.sign(a), index=a.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sign of acceleration
def f11ac_f11_semi_acceleration_accelsign_126d_base_v028_signal(closeadj):
    a = _f11_accel(closeadj, 126)
    result = pd.Series(np.sign(a), index=a.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sign of acceleration
def f11ac_f11_semi_acceleration_accelsign_252d_base_v029_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    result = pd.Series(np.sign(a), index=a.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sign of acceleration
def f11ac_f11_semi_acceleration_accelsign_504d_base_v030_signal(closeadj):
    a = _f11_accel(closeadj, 504)
    result = pd.Series(np.sign(a), index=a.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling sum of 21d acceleration
def f11ac_f11_semi_acceleration_cumaccel21_21d_base_v031_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of 21d acceleration
def f11ac_f11_semi_acceleration_cumaccel21_63d_base_v032_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling sum of 21d acceleration
def f11ac_f11_semi_acceleration_cumaccel21_126d_base_v033_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of 21d acceleration
def f11ac_f11_semi_acceleration_cumaccel21_252d_base_v034_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of 21d acceleration
def f11ac_f11_semi_acceleration_cumaccel21_504d_base_v035_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of 21d acceleration
def f11ac_f11_semi_acceleration_accelstd21_21d_base_v036_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _std(a, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of 21d acceleration
def f11ac_f11_semi_acceleration_accelstd21_63d_base_v037_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _std(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of 21d acceleration
def f11ac_f11_semi_acceleration_accelstd21_126d_base_v038_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _std(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of 21d acceleration
def f11ac_f11_semi_acceleration_accelstd21_252d_base_v039_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _std(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of 21d acceleration
def f11ac_f11_semi_acceleration_accelstd21_504d_base_v040_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _std(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of 21d acceleration
def f11ac_f11_semi_acceleration_accelmax21_21d_base_v041_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _max(a, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of 21d acceleration
def f11ac_f11_semi_acceleration_accelmax21_63d_base_v042_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _max(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of 21d acceleration
def f11ac_f11_semi_acceleration_accelmax21_126d_base_v043_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _max(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of 21d acceleration
def f11ac_f11_semi_acceleration_accelmax21_252d_base_v044_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _max(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of 21d acceleration
def f11ac_f11_semi_acceleration_accelmax21_504d_base_v045_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _max(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of 21d acceleration
def f11ac_f11_semi_acceleration_accelmin21_21d_base_v046_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _min(a, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of 21d acceleration
def f11ac_f11_semi_acceleration_accelmin21_63d_base_v047_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _min(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of 21d acceleration
def f11ac_f11_semi_acceleration_accelmin21_126d_base_v048_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _min(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of 21d acceleration
def f11ac_f11_semi_acceleration_accelmin21_252d_base_v049_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _min(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of 21d acceleration
def f11ac_f11_semi_acceleration_accelmin21_504d_base_v050_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = _min(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio positive acceleration
def f11ac_f11_semi_acceleration_accelposhit_21d_base_v051_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = (a > 0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio positive acceleration
def f11ac_f11_semi_acceleration_accelposhit_63d_base_v052_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = (a > 0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio positive acceleration
def f11ac_f11_semi_acceleration_accelposhit_126d_base_v053_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = (a > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio positive acceleration
def f11ac_f11_semi_acceleration_accelposhit_252d_base_v054_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = (a > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio positive acceleration
def f11ac_f11_semi_acceleration_accelposhit_504d_base_v055_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = (a > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative 21d log-return acceleration
def f11ac_f11_semi_acceleration_cumlogaccel_21d_base_v056_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    a = lr - lr.shift(21)
    result = a.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative 21d log-return acceleration
def f11ac_f11_semi_acceleration_cumlogaccel_63d_base_v057_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    a = lr - lr.shift(21)
    result = a.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative 21d log-return acceleration
def f11ac_f11_semi_acceleration_cumlogaccel_126d_base_v058_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    a = lr - lr.shift(21)
    result = a.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative 21d log-return acceleration
def f11ac_f11_semi_acceleration_cumlogaccel_252d_base_v059_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    a = lr - lr.shift(21)
    result = a.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative 21d log-return acceleration
def f11ac_f11_semi_acceleration_cumlogaccel_504d_base_v060_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(21))
    a = lr - lr.shift(21)
    result = a.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# return EMA crossover (5v21) - speed-of-trend proxy
def f11ac_f11_semi_acceleration_emaaccel_5v21_base_v061_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# return EMA crossover (21v63) - speed-of-trend proxy
def f11ac_f11_semi_acceleration_emaaccel_21v63_base_v062_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# return EMA crossover (63v126) - speed-of-trend proxy
def f11ac_f11_semi_acceleration_emaaccel_63v126_base_v063_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# return EMA crossover (126v252) - speed-of-trend proxy
def f11ac_f11_semi_acceleration_emaaccel_126v252_base_v064_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# return EMA crossover (252v504) - speed-of-trend proxy
def f11ac_f11_semi_acceleration_emaaccel_252v504_base_v065_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk (diff of acceleration)
def f11ac_f11_semi_acceleration_jerk_21d_base_v066_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    result = a - a.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk (diff of acceleration)
def f11ac_f11_semi_acceleration_jerk_63d_base_v067_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    result = a - a.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk (diff of acceleration)
def f11ac_f11_semi_acceleration_jerk_126d_base_v068_signal(closeadj):
    a = _f11_accel(closeadj, 126)
    result = a - a.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d jerk (diff of acceleration)
def f11ac_f11_semi_acceleration_jerk_252d_base_v069_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    result = a - a.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d jerk (diff of acceleration)
def f11ac_f11_semi_acceleration_jerk_504d_base_v070_signal(closeadj):
    a = _f11_accel(closeadj, 504)
    result = a - a.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d normalized acceleration by vol
def f11ac_f11_semi_acceleration_accelnormvol_21d_base_v071_signal(closeadj):
    a = _f11_accel(closeadj, 21)
    v = _std(closeadj.pct_change(), 21)
    result = a / v.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d normalized acceleration by vol
def f11ac_f11_semi_acceleration_accelnormvol_63d_base_v072_signal(closeadj):
    a = _f11_accel(closeadj, 63)
    v = _std(closeadj.pct_change(), 63)
    result = a / v.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d normalized acceleration by vol
def f11ac_f11_semi_acceleration_accelnormvol_126d_base_v073_signal(closeadj):
    a = _f11_accel(closeadj, 126)
    v = _std(closeadj.pct_change(), 126)
    result = a / v.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d normalized acceleration by vol
def f11ac_f11_semi_acceleration_accelnormvol_252d_base_v074_signal(closeadj):
    a = _f11_accel(closeadj, 252)
    v = _std(closeadj.pct_change(), 252)
    result = a / v.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d normalized acceleration by vol
def f11ac_f11_semi_acceleration_accelnormvol_504d_base_v075_signal(closeadj):
    a = _f11_accel(closeadj, 504)
    v = _std(closeadj.pct_change(), 504)
    result = a / v.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
