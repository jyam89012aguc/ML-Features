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


# 21d lag-1 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac1_21d_base_v001_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(21, min_periods=10).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac1_63d_base_v002_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(63, min_periods=31).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac1_126d_base_v003_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac1_252d_base_v004_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac1_504d_base_v005_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-2 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac2_21d_base_v006_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(21, min_periods=10).corr(r.shift(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-2 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac2_63d_base_v007_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(63, min_periods=31).corr(r.shift(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-2 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac2_126d_base_v008_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(126, min_periods=63).corr(r.shift(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-2 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac2_252d_base_v009_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(252, min_periods=126).corr(r.shift(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-2 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac2_504d_base_v010_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(504, min_periods=252).corr(r.shift(2))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-5 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac5_21d_base_v011_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(21, min_periods=10).corr(r.shift(5))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-5 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac5_63d_base_v012_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(63, min_periods=31).corr(r.shift(5))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-5 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac5_126d_base_v013_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(126, min_periods=63).corr(r.shift(5))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-5 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac5_252d_base_v014_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(252, min_periods=126).corr(r.shift(5))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-5 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac5_504d_base_v015_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(504, min_periods=252).corr(r.shift(5))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-21 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac21_21d_base_v016_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(21, min_periods=10).corr(r.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-21 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac21_63d_base_v017_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(63, min_periods=31).corr(r.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-21 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac21_126d_base_v018_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(126, min_periods=63).corr(r.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-21 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac21_252d_base_v019_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(252, min_periods=126).corr(r.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-21 autocorr of returns
def f10mp_f10_semi_momentum_persistence_ac21_504d_base_v020_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(504, min_periods=252).corr(r.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorr of |returns| (vol clustering)
def f10mp_f10_semi_momentum_persistence_absac1_21d_base_v021_signal(closeadj):
    r = closeadj.pct_change().abs()
    result = r.rolling(21, min_periods=10).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorr of |returns| (vol clustering)
def f10mp_f10_semi_momentum_persistence_absac1_63d_base_v022_signal(closeadj):
    r = closeadj.pct_change().abs()
    result = r.rolling(63, min_periods=31).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorr of |returns| (vol clustering)
def f10mp_f10_semi_momentum_persistence_absac1_126d_base_v023_signal(closeadj):
    r = closeadj.pct_change().abs()
    result = r.rolling(126, min_periods=63).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorr of |returns| (vol clustering)
def f10mp_f10_semi_momentum_persistence_absac1_252d_base_v024_signal(closeadj):
    r = closeadj.pct_change().abs()
    result = r.rolling(252, min_periods=126).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorr of |returns| (vol clustering)
def f10mp_f10_semi_momentum_persistence_absac1_504d_base_v025_signal(closeadj):
    r = closeadj.pct_change().abs()
    result = r.rolling(504, min_periods=252).corr(r.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorr of return sign
def f10mp_f10_semi_momentum_persistence_signac1_21d_base_v026_signal(closeadj):
    s = pd.Series(np.sign(closeadj.pct_change()), index=closeadj.index)
    result = s.rolling(21, min_periods=10).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorr of return sign
def f10mp_f10_semi_momentum_persistence_signac1_63d_base_v027_signal(closeadj):
    s = pd.Series(np.sign(closeadj.pct_change()), index=closeadj.index)
    result = s.rolling(63, min_periods=31).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorr of return sign
def f10mp_f10_semi_momentum_persistence_signac1_126d_base_v028_signal(closeadj):
    s = pd.Series(np.sign(closeadj.pct_change()), index=closeadj.index)
    result = s.rolling(126, min_periods=63).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorr of return sign
def f10mp_f10_semi_momentum_persistence_signac1_252d_base_v029_signal(closeadj):
    s = pd.Series(np.sign(closeadj.pct_change()), index=closeadj.index)
    result = s.rolling(252, min_periods=126).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorr of return sign
def f10mp_f10_semi_momentum_persistence_signac1_504d_base_v030_signal(closeadj):
    s = pd.Series(np.sign(closeadj.pct_change()), index=closeadj.index)
    result = s.rolling(504, min_periods=252).corr(s.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmean_21d_base_v031_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmean_63d_base_v032_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmean_126d_base_v033_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmean_252d_base_v034_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmean_504d_base_v035_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmean_21d_base_v036_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmean_63d_base_v037_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmean_126d_base_v038_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmean_252d_base_v039_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmean_504d_base_v040_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmax_21d_base_v041_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(21, min_periods=11).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmax_63d_base_v042_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(63, min_periods=32).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmax_126d_base_v043_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(126, min_periods=63).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmax_252d_base_v044_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(252, min_periods=126).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max up-streak length
def f10mp_f10_semi_momentum_persistence_upstreakmax_504d_base_v045_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = sign.groupby(grp).cumsum().where(sign > 0, 0.0)
    result = streak.rolling(504, min_periods=252).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmax_21d_base_v046_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(21, min_periods=11).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmax_63d_base_v047_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(63, min_periods=32).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmax_126d_base_v048_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(126, min_periods=63).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmax_252d_base_v049_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(252, min_periods=126).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max down-streak length
def f10mp_f10_semi_momentum_persistence_dnstreakmax_504d_base_v050_signal(closeadj):
    r = closeadj.pct_change()
    sign = (r > 0).astype(int) - (r < 0).astype(int)
    grp = (sign != sign.shift()).cumsum()
    streak = (-sign.groupby(grp).cumsum()).where(sign < 0, 0.0)
    result = streak.rolling(504, min_periods=252).max()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive returns
def f10mp_f10_semi_momentum_persistence_poshit_21d_base_v051_signal(closeadj):
    r = closeadj.pct_change()
    result = (r > 0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive returns
def f10mp_f10_semi_momentum_persistence_poshit_63d_base_v052_signal(closeadj):
    r = closeadj.pct_change()
    result = (r > 0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive returns
def f10mp_f10_semi_momentum_persistence_poshit_126d_base_v053_signal(closeadj):
    r = closeadj.pct_change()
    result = (r > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive returns
def f10mp_f10_semi_momentum_persistence_poshit_252d_base_v054_signal(closeadj):
    r = closeadj.pct_change()
    result = (r > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive returns
def f10mp_f10_semi_momentum_persistence_poshit_504d_base_v055_signal(closeadj):
    r = closeadj.pct_change()
    result = (r > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of up-days to down-days
def f10mp_f10_semi_momentum_persistence_uddratio_21d_base_v056_signal(closeadj):
    r = closeadj.pct_change()
    u = (r > 0).astype(float).rolling(21, min_periods=11).sum()
    d = (r < 0).astype(float).rolling(21, min_periods=11).sum()
    result = u / d.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of up-days to down-days
def f10mp_f10_semi_momentum_persistence_uddratio_63d_base_v057_signal(closeadj):
    r = closeadj.pct_change()
    u = (r > 0).astype(float).rolling(63, min_periods=32).sum()
    d = (r < 0).astype(float).rolling(63, min_periods=32).sum()
    result = u / d.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio of up-days to down-days
def f10mp_f10_semi_momentum_persistence_uddratio_126d_base_v058_signal(closeadj):
    r = closeadj.pct_change()
    u = (r > 0).astype(float).rolling(126, min_periods=63).sum()
    d = (r < 0).astype(float).rolling(126, min_periods=63).sum()
    result = u / d.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of up-days to down-days
def f10mp_f10_semi_momentum_persistence_uddratio_252d_base_v059_signal(closeadj):
    r = closeadj.pct_change()
    u = (r > 0).astype(float).rolling(252, min_periods=126).sum()
    d = (r < 0).astype(float).rolling(252, min_periods=126).sum()
    result = u / d.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of up-days to down-days
def f10mp_f10_semi_momentum_persistence_uddratio_504d_base_v060_signal(closeadj):
    r = closeadj.pct_change()
    u = (r > 0).astype(float).rolling(504, min_periods=252).sum()
    d = (r < 0).astype(float).rolling(504, min_periods=252).sum()
    result = u / d.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d variance ratio (5d vs 1d, mean reversion)
def f10mp_f10_semi_momentum_persistence_varratio5_21d_base_v061_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(21, min_periods=10).var()
    v5 = r5.rolling(21, min_periods=10).var()
    result = v5 / (5 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d variance ratio (5d vs 1d, mean reversion)
def f10mp_f10_semi_momentum_persistence_varratio5_63d_base_v062_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(63, min_periods=31).var()
    v5 = r5.rolling(63, min_periods=31).var()
    result = v5 / (5 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d variance ratio (5d vs 1d, mean reversion)
def f10mp_f10_semi_momentum_persistence_varratio5_126d_base_v063_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(126, min_periods=63).var()
    v5 = r5.rolling(126, min_periods=63).var()
    result = v5 / (5 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d variance ratio (5d vs 1d, mean reversion)
def f10mp_f10_semi_momentum_persistence_varratio5_252d_base_v064_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(252, min_periods=126).var()
    v5 = r5.rolling(252, min_periods=126).var()
    result = v5 / (5 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d variance ratio (5d vs 1d, mean reversion)
def f10mp_f10_semi_momentum_persistence_varratio5_504d_base_v065_signal(closeadj):
    r1 = closeadj.pct_change()
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(504, min_periods=252).var()
    v5 = r5.rolling(504, min_periods=252).var()
    result = v5 / (5 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d variance ratio (21d vs 1d)
def f10mp_f10_semi_momentum_persistence_varratio21_21d_base_v066_signal(closeadj):
    r1 = closeadj.pct_change()
    r21 = closeadj.pct_change(21)
    v1 = r1.rolling(21, min_periods=10).var()
    v21 = r21.rolling(21, min_periods=10).var()
    result = v21 / (21 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d variance ratio (21d vs 1d)
def f10mp_f10_semi_momentum_persistence_varratio21_63d_base_v067_signal(closeadj):
    r1 = closeadj.pct_change()
    r21 = closeadj.pct_change(21)
    v1 = r1.rolling(63, min_periods=31).var()
    v21 = r21.rolling(63, min_periods=31).var()
    result = v21 / (21 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d variance ratio (21d vs 1d)
def f10mp_f10_semi_momentum_persistence_varratio21_126d_base_v068_signal(closeadj):
    r1 = closeadj.pct_change()
    r21 = closeadj.pct_change(21)
    v1 = r1.rolling(126, min_periods=63).var()
    v21 = r21.rolling(126, min_periods=63).var()
    result = v21 / (21 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d variance ratio (21d vs 1d)
def f10mp_f10_semi_momentum_persistence_varratio21_252d_base_v069_signal(closeadj):
    r1 = closeadj.pct_change()
    r21 = closeadj.pct_change(21)
    v1 = r1.rolling(252, min_periods=126).var()
    v21 = r21.rolling(252, min_periods=126).var()
    result = v21 / (21 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d variance ratio (21d vs 1d)
def f10mp_f10_semi_momentum_persistence_varratio21_504d_base_v070_signal(closeadj):
    r1 = closeadj.pct_change()
    r21 = closeadj.pct_change(21)
    v1 = r1.rolling(504, min_periods=252).var()
    v21 = r21.rolling(504, min_periods=252).var()
    result = v21 / (21 * v1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d efficiency ratio (net move / total path)
def f10mp_f10_semi_momentum_persistence_effratio_21d_base_v071_signal(closeadj):
    r = closeadj.pct_change()
    num = r.rolling(21, min_periods=11).sum()
    den = r.abs().rolling(21, min_periods=11).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d efficiency ratio (net move / total path)
def f10mp_f10_semi_momentum_persistence_effratio_63d_base_v072_signal(closeadj):
    r = closeadj.pct_change()
    num = r.rolling(63, min_periods=32).sum()
    den = r.abs().rolling(63, min_periods=32).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d efficiency ratio (net move / total path)
def f10mp_f10_semi_momentum_persistence_effratio_126d_base_v073_signal(closeadj):
    r = closeadj.pct_change()
    num = r.rolling(126, min_periods=63).sum()
    den = r.abs().rolling(126, min_periods=63).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d efficiency ratio (net move / total path)
def f10mp_f10_semi_momentum_persistence_effratio_252d_base_v074_signal(closeadj):
    r = closeadj.pct_change()
    num = r.rolling(252, min_periods=126).sum()
    den = r.abs().rolling(252, min_periods=126).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d efficiency ratio (net move / total path)
def f10mp_f10_semi_momentum_persistence_effratio_504d_base_v075_signal(closeadj):
    r = closeadj.pct_change()
    num = r.rolling(504, min_periods=252).sum()
    den = r.abs().rolling(504, min_periods=252).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
