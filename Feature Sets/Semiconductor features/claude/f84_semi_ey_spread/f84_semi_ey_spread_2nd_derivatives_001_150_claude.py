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


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f84ey_own_ey(pe):
    return 1.0 / pe.replace(0, np.nan)


def _f84ey_spread(pe, sp500_ey_avg):
    return (1.0 / pe.replace(0, np.nan)) - sp500_ey_avg


def _f84ey_ratio(pe, sp500_ey_avg):
    return (1.0 / pe.replace(0, np.nan)) / sp500_ey_avg.replace(0, np.nan)


def _f84ey_log_ratio(pe, sp500_ey_avg):
    own = 1.0 / pe.replace(0, np.nan)
    return np.log(own.abs() / sp500_ey_avg.replace(0, np.nan).abs())


# 5d slope of 21d own_ey level
def f84ey_f84_semi_ey_spread_owney_21d_slope_v001_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_own_ey(pe), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d own_ey level
def f84ey_f84_semi_ey_spread_owney_21d_slope_v002_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_own_ey(pe), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d own_ey level
def f84ey_f84_semi_ey_spread_owney_63d_slope_v003_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_own_ey(pe), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d own_ey level
def f84ey_f84_semi_ey_spread_owney_126d_slope_v004_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_own_ey(pe), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d own_ey level
def f84ey_f84_semi_ey_spread_owney_252d_slope_v005_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_own_ey(pe), 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EY spread mean
def f84ey_f84_semi_ey_spread_spread_21d_slope_v006_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_spread(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d EY spread mean
def f84ey_f84_semi_ey_spread_spread_21d_slope_v007_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_spread(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EY spread mean
def f84ey_f84_semi_ey_spread_spread_63d_slope_v008_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_spread(pe, sp500_ey_avg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EY spread mean
def f84ey_f84_semi_ey_spread_spread_126d_slope_v009_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_spread(pe, sp500_ey_avg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d EY spread mean
def f84ey_f84_semi_ey_spread_spread_252d_slope_v010_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_spread(pe, sp500_ey_avg), 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EY spread z-score
def f84ey_f84_semi_ey_spread_spreadz_21d_slope_v011_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_spread(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EY spread z-score
def f84ey_f84_semi_ey_spread_spreadz_63d_slope_v012_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_spread(pe, sp500_ey_avg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EY spread z-score
def f84ey_f84_semi_ey_spread_spreadz_126d_slope_v013_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_spread(pe, sp500_ey_avg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EY spread z-score
def f84ey_f84_semi_ey_spread_spreadz_252d_slope_v014_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_spread(pe, sp500_ey_avg), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EY spread z-score
def f84ey_f84_semi_ey_spread_spreadz_504d_slope_v015_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_spread(pe, sp500_ey_avg), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EY spread max
def f84ey_f84_semi_ey_spread_spreadmax_21d_slope_v016_signal(pe, sp500_ey_avg, closeadj):
    base = _max(_f84ey_spread(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EY spread max
def f84ey_f84_semi_ey_spread_spreadmax_63d_slope_v017_signal(pe, sp500_ey_avg, closeadj):
    base = _max(_f84ey_spread(pe, sp500_ey_avg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EY spread max
def f84ey_f84_semi_ey_spread_spreadmax_126d_slope_v018_signal(pe, sp500_ey_avg, closeadj):
    base = _max(_f84ey_spread(pe, sp500_ey_avg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EY spread max
def f84ey_f84_semi_ey_spread_spreadmax_252d_slope_v019_signal(pe, sp500_ey_avg, closeadj):
    base = _max(_f84ey_spread(pe, sp500_ey_avg), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EY spread max
def f84ey_f84_semi_ey_spread_spreadmax_504d_slope_v020_signal(pe, sp500_ey_avg, closeadj):
    base = _max(_f84ey_spread(pe, sp500_ey_avg), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EY spread min
def f84ey_f84_semi_ey_spread_spreadmin_21d_slope_v021_signal(pe, sp500_ey_avg, closeadj):
    base = _min(_f84ey_spread(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EY spread min
def f84ey_f84_semi_ey_spread_spreadmin_63d_slope_v022_signal(pe, sp500_ey_avg, closeadj):
    base = _min(_f84ey_spread(pe, sp500_ey_avg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EY spread min
def f84ey_f84_semi_ey_spread_spreadmin_126d_slope_v023_signal(pe, sp500_ey_avg, closeadj):
    base = _min(_f84ey_spread(pe, sp500_ey_avg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EY spread min
def f84ey_f84_semi_ey_spread_spreadmin_252d_slope_v024_signal(pe, sp500_ey_avg, closeadj):
    base = _min(_f84ey_spread(pe, sp500_ey_avg), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EY spread min
def f84ey_f84_semi_ey_spread_spreadmin_504d_slope_v025_signal(pe, sp500_ey_avg, closeadj):
    base = _min(_f84ey_spread(pe, sp500_ey_avg), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EY spread range
def f84ey_f84_semi_ey_spread_spreadrng_21d_slope_v026_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _max(sp, 21) - _min(sp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EY spread range
def f84ey_f84_semi_ey_spread_spreadrng_63d_slope_v027_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _max(sp, 63) - _min(sp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EY spread range
def f84ey_f84_semi_ey_spread_spreadrng_126d_slope_v028_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _max(sp, 126) - _min(sp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EY spread range
def f84ey_f84_semi_ey_spread_spreadrng_252d_slope_v029_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _max(sp, 252) - _min(sp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EY spread range
def f84ey_f84_semi_ey_spread_spreadrng_504d_slope_v030_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _max(sp, 504) - _min(sp, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d position-in-range
def f84ey_f84_semi_ey_spread_spreadpos_21d_slope_v031_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 21)
    hi = _max(sp, 21)
    base = (sp - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position-in-range
def f84ey_f84_semi_ey_spread_spreadpos_63d_slope_v032_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 63)
    hi = _max(sp, 63)
    base = (sp - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d position-in-range
def f84ey_f84_semi_ey_spread_spreadpos_126d_slope_v033_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 126)
    hi = _max(sp, 126)
    base = (sp - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d position-in-range
def f84ey_f84_semi_ey_spread_spreadpos_252d_slope_v034_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 252)
    hi = _max(sp, 252)
    base = (sp - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d position-in-range
def f84ey_f84_semi_ey_spread_spreadpos_504d_slope_v035_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    lo = _min(sp, 504)
    hi = _max(sp, 504)
    base = (sp - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d drawdown
def f84ey_f84_semi_ey_spread_spreaddd_21d_slope_v036_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _max(sp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown
def f84ey_f84_semi_ey_spread_spreaddd_63d_slope_v037_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _max(sp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d drawdown
def f84ey_f84_semi_ey_spread_spreaddd_126d_slope_v038_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _max(sp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown
def f84ey_f84_semi_ey_spread_spreaddd_252d_slope_v039_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _max(sp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d drawdown
def f84ey_f84_semi_ey_spread_spreaddd_504d_slope_v040_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _max(sp, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d run-up
def f84ey_f84_semi_ey_spread_spreadup_21d_slope_v041_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _min(sp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up
def f84ey_f84_semi_ey_spread_spreadup_63d_slope_v042_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _min(sp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d run-up
def f84ey_f84_semi_ey_spread_spreadup_126d_slope_v043_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _min(sp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d run-up
def f84ey_f84_semi_ey_spread_spreadup_252d_slope_v044_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _min(sp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d run-up
def f84ey_f84_semi_ey_spread_spreadup_504d_slope_v045_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - _min(sp, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EY spread sign avg
def f84ey_f84_semi_ey_spread_spreadsign_21d_slope_v046_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = pd.Series(np.sign(sp), index=sp.index).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EY spread sign avg
def f84ey_f84_semi_ey_spread_spreadsign_63d_slope_v047_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = pd.Series(np.sign(sp), index=sp.index).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EY spread sign avg
def f84ey_f84_semi_ey_spread_spreadsign_126d_slope_v048_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = pd.Series(np.sign(sp), index=sp.index).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EY spread sign avg
def f84ey_f84_semi_ey_spread_spreadsign_252d_slope_v049_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = pd.Series(np.sign(sp), index=sp.index).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EY spread sign avg
def f84ey_f84_semi_ey_spread_spreadsign_504d_slope_v050_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = pd.Series(np.sign(sp), index=sp.index).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d cheaper-day streak
def f84ey_f84_semi_ey_spread_spreadstreak_21d_slope_v051_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = (sp > 0).astype(float).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cheaper-day streak
def f84ey_f84_semi_ey_spread_spreadstreak_63d_slope_v052_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = (sp > 0).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d cheaper-day streak
def f84ey_f84_semi_ey_spread_spreadstreak_126d_slope_v053_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = (sp > 0).astype(float).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d cheaper-day streak
def f84ey_f84_semi_ey_spread_spreadstreak_252d_slope_v054_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = (sp > 0).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d cheaper-day streak
def f84ey_f84_semi_ey_spread_spreadstreak_504d_slope_v055_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = (sp > 0).astype(float).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ratio (own_ey / sp500_ey)
def f84ey_f84_semi_ey_spread_ratio_21d_slope_v056_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_ratio(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ratio
def f84ey_f84_semi_ey_spread_ratio_63d_slope_v057_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_ratio(pe, sp500_ey_avg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ratio
def f84ey_f84_semi_ey_spread_ratio_126d_slope_v058_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_ratio(pe, sp500_ey_avg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ratio
def f84ey_f84_semi_ey_spread_ratio_252d_slope_v059_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_ratio(pe, sp500_ey_avg), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ratio
def f84ey_f84_semi_ey_spread_ratio_504d_slope_v060_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_ratio(pe, sp500_ey_avg), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log-ratio
def f84ey_f84_semi_ey_spread_logratio_21d_slope_v061_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_log_ratio(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log-ratio
def f84ey_f84_semi_ey_spread_logratio_63d_slope_v062_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_log_ratio(pe, sp500_ey_avg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log-ratio
def f84ey_f84_semi_ey_spread_logratio_126d_slope_v063_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_log_ratio(pe, sp500_ey_avg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log-ratio
def f84ey_f84_semi_ey_spread_logratio_252d_slope_v064_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_log_ratio(pe, sp500_ey_avg), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d log-ratio
def f84ey_f84_semi_ey_spread_logratio_504d_slope_v065_signal(pe, sp500_ey_avg, closeadj):
    base = _mean(_f84ey_log_ratio(pe, sp500_ey_avg), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5v21 EMA crossover of EY spread
def f84ey_f84_semi_ey_spread_spreadema_5v21_slope_v066_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.ewm(span=5, adjust=False).mean() - sp.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21v63 EMA crossover
def f84ey_f84_semi_ey_spread_spreadema_21v63_slope_v067_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.ewm(span=21, adjust=False).mean() - sp.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63v126 EMA crossover
def f84ey_f84_semi_ey_spread_spreadema_63v126_slope_v068_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.ewm(span=63, adjust=False).mean() - sp.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126v252 EMA crossover
def f84ey_f84_semi_ey_spread_spreadema_126v252_slope_v069_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.ewm(span=126, adjust=False).mean() - sp.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252v504 EMA crossover
def f84ey_f84_semi_ey_spread_spreadema_252v504_slope_v070_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.ewm(span=252, adjust=False).mean() - sp.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d spread std
def f84ey_f84_semi_ey_spread_spreadstd_21d_slope_v071_signal(pe, sp500_ey_avg, closeadj):
    base = _std(_f84ey_spread(pe, sp500_ey_avg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread std
def f84ey_f84_semi_ey_spread_spreadstd_63d_slope_v072_signal(pe, sp500_ey_avg, closeadj):
    base = _std(_f84ey_spread(pe, sp500_ey_avg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d spread std
def f84ey_f84_semi_ey_spread_spreadstd_126d_slope_v073_signal(pe, sp500_ey_avg, closeadj):
    base = _std(_f84ey_spread(pe, sp500_ey_avg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d spread std
def f84ey_f84_semi_ey_spread_spreadstd_252d_slope_v074_signal(pe, sp500_ey_avg, closeadj):
    base = _std(_f84ey_spread(pe, sp500_ey_avg), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d spread std
def f84ey_f84_semi_ey_spread_spreadstd_504d_slope_v075_signal(pe, sp500_ey_avg, closeadj):
    base = _std(_f84ey_spread(pe, sp500_ey_avg), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d spread skew
def f84ey_f84_semi_ey_spread_spreadskew_21d_slope_v076_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(21, min_periods=11).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread skew
def f84ey_f84_semi_ey_spread_spreadskew_63d_slope_v077_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d spread skew
def f84ey_f84_semi_ey_spread_spreadskew_126d_slope_v078_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d spread skew
def f84ey_f84_semi_ey_spread_spreadskew_252d_slope_v079_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(252, min_periods=126).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d spread skew
def f84ey_f84_semi_ey_spread_spreadskew_504d_slope_v080_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(504, min_periods=252).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d spread kurtosis
def f84ey_f84_semi_ey_spread_spreadkurt_21d_slope_v081_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(21, min_periods=11).kurt()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread kurtosis
def f84ey_f84_semi_ey_spread_spreadkurt_63d_slope_v082_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d spread kurtosis
def f84ey_f84_semi_ey_spread_spreadkurt_126d_slope_v083_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(126, min_periods=63).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d spread kurtosis
def f84ey_f84_semi_ey_spread_spreadkurt_252d_slope_v084_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d spread kurtosis
def f84ey_f84_semi_ey_spread_spreadkurt_504d_slope_v085_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.rolling(504, min_periods=252).kurt()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d own_ey z-score
def f84ey_f84_semi_ey_spread_owneyz_21d_slope_v086_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_own_ey(pe), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d own_ey z-score
def f84ey_f84_semi_ey_spread_owneyz_63d_slope_v087_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_own_ey(pe), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d own_ey z-score
def f84ey_f84_semi_ey_spread_owneyz_126d_slope_v088_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_own_ey(pe), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d own_ey z-score
def f84ey_f84_semi_ey_spread_owneyz_252d_slope_v089_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_own_ey(pe), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d own_ey z-score
def f84ey_f84_semi_ey_spread_owneyz_504d_slope_v090_signal(pe, sp500_ey_avg, closeadj):
    base = _z(_f84ey_own_ey(pe), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sp500_ey z-score
def f84ey_f84_semi_ey_spread_spxeyz_21d_slope_v091_signal(pe, sp500_ey_avg, closeadj):
    base = _z(sp500_ey_avg, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sp500_ey z-score
def f84ey_f84_semi_ey_spread_spxeyz_63d_slope_v092_signal(pe, sp500_ey_avg, closeadj):
    base = _z(sp500_ey_avg, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sp500_ey z-score
def f84ey_f84_semi_ey_spread_spxeyz_126d_slope_v093_signal(pe, sp500_ey_avg, closeadj):
    base = _z(sp500_ey_avg, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sp500_ey z-score
def f84ey_f84_semi_ey_spread_spxeyz_252d_slope_v094_signal(pe, sp500_ey_avg, closeadj):
    base = _z(sp500_ey_avg, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d sp500_ey z-score
def f84ey_f84_semi_ey_spread_spxeyz_504d_slope_v095_signal(pe, sp500_ey_avg, closeadj):
    base = _z(sp500_ey_avg, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d cond-rise spread
def f84ey_f84_semi_ey_spread_condrise_21d_slope_v096_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    base = _mean(sp.where(mask), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cond-rise spread
def f84ey_f84_semi_ey_spread_condrise_63d_slope_v097_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    base = _mean(sp.where(mask), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d cond-rise spread
def f84ey_f84_semi_ey_spread_condrise_126d_slope_v098_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    base = _mean(sp.where(mask), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d cond-rise spread
def f84ey_f84_semi_ey_spread_condrise_252d_slope_v099_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    base = _mean(sp.where(mask), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d cond-rise spread
def f84ey_f84_semi_ey_spread_condrise_504d_slope_v100_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    base = _mean(sp.where(mask), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d cond-fall spread
def f84ey_f84_semi_ey_spread_condfall_21d_slope_v101_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    base = _mean(sp.where(mask), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cond-fall spread
def f84ey_f84_semi_ey_spread_condfall_63d_slope_v102_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    base = _mean(sp.where(mask), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d cond-fall spread
def f84ey_f84_semi_ey_spread_condfall_126d_slope_v103_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    base = _mean(sp.where(mask), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d cond-fall spread
def f84ey_f84_semi_ey_spread_condfall_252d_slope_v104_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    base = _mean(sp.where(mask), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d cond-fall spread
def f84ey_f84_semi_ey_spread_condfall_504d_slope_v105_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    base = _mean(sp.where(mask), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d spread diff
def f84ey_f84_semi_ey_spread_spreaddiff_21d_slope_v106_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.shift(21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d spread diff
def f84ey_f84_semi_ey_spread_spreaddiff_63d_slope_v107_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.shift(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d spread diff
def f84ey_f84_semi_ey_spread_spreaddiff_126d_slope_v108_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.shift(126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d spread diff
def f84ey_f84_semi_ey_spread_spreaddiff_252d_slope_v109_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.shift(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d spread diff
def f84ey_f84_semi_ey_spread_spreaddiff_504d_slope_v110_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.shift(504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d positive-spread sum
def f84ey_f84_semi_ey_spread_spreadpossum_21d_slope_v111_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(lower=0).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d positive-spread sum
def f84ey_f84_semi_ey_spread_spreadpossum_63d_slope_v112_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(lower=0).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d positive-spread sum
def f84ey_f84_semi_ey_spread_spreadpossum_126d_slope_v113_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(lower=0).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d positive-spread sum
def f84ey_f84_semi_ey_spread_spreadpossum_252d_slope_v114_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(lower=0).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d positive-spread sum
def f84ey_f84_semi_ey_spread_spreadpossum_504d_slope_v115_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(lower=0).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d negative-spread sum
def f84ey_f84_semi_ey_spread_spreadnegsum_21d_slope_v116_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(upper=0).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d negative-spread sum
def f84ey_f84_semi_ey_spread_spreadnegsum_63d_slope_v117_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(upper=0).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d negative-spread sum
def f84ey_f84_semi_ey_spread_spreadnegsum_126d_slope_v118_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(upper=0).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d negative-spread sum
def f84ey_f84_semi_ey_spread_spreadnegsum_252d_slope_v119_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(upper=0).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d negative-spread sum
def f84ey_f84_semi_ey_spread_spreadnegsum_504d_slope_v120_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp.clip(upper=0).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EMA deviation
def f84ey_f84_semi_ey_spread_spreaddev_21d_slope_v121_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EMA deviation
def f84ey_f84_semi_ey_spread_spreaddev_63d_slope_v122_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EMA deviation
def f84ey_f84_semi_ey_spread_spreaddev_126d_slope_v123_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EMA deviation
def f84ey_f84_semi_ey_spread_spreaddev_252d_slope_v124_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EMA deviation
def f84ey_f84_semi_ey_spread_spreaddev_504d_slope_v125_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = sp - sp.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d corr(own_ey, sp500_ey)
def f84ey_f84_semi_ey_spread_corr_21d_slope_v126_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    base = own.rolling(21, min_periods=11).corr(sp500_ey_avg)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d corr
def f84ey_f84_semi_ey_spread_corr_63d_slope_v127_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    base = own.rolling(63, min_periods=32).corr(sp500_ey_avg)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d corr
def f84ey_f84_semi_ey_spread_corr_126d_slope_v128_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    base = own.rolling(126, min_periods=63).corr(sp500_ey_avg)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d corr
def f84ey_f84_semi_ey_spread_corr_252d_slope_v129_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    base = own.rolling(252, min_periods=126).corr(sp500_ey_avg)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d corr
def f84ey_f84_semi_ey_spread_corr_504d_slope_v130_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    base = own.rolling(504, min_periods=252).corr(sp500_ey_avg)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d beta(own_ey on sp500_ey)
def f84ey_f84_semi_ey_spread_beta_21d_slope_v131_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(21, min_periods=11).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(21, min_periods=11).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d beta
def f84ey_f84_semi_ey_spread_beta_63d_slope_v132_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(63, min_periods=32).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(63, min_periods=32).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d beta
def f84ey_f84_semi_ey_spread_beta_126d_slope_v133_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(126, min_periods=63).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(126, min_periods=63).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d beta
def f84ey_f84_semi_ey_spread_beta_252d_slope_v134_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(252, min_periods=126).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(252, min_periods=126).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d beta
def f84ey_f84_semi_ey_spread_beta_504d_slope_v135_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(504, min_periods=252).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(504, min_periods=252).var()
    base = cov / var.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d robust z
def f84ey_f84_semi_ey_spread_spreadrobustz_21d_slope_v136_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(21, min_periods=11).median()
    mad = (sp - med).abs().rolling(21, min_periods=11).median()
    base = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z
def f84ey_f84_semi_ey_spread_spreadrobustz_63d_slope_v137_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(63, min_periods=32).median()
    mad = (sp - med).abs().rolling(63, min_periods=32).median()
    base = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d robust z
def f84ey_f84_semi_ey_spread_spreadrobustz_126d_slope_v138_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(126, min_periods=63).median()
    mad = (sp - med).abs().rolling(126, min_periods=63).median()
    base = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d robust z
def f84ey_f84_semi_ey_spread_spreadrobustz_252d_slope_v139_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(252, min_periods=126).median()
    mad = (sp - med).abs().rolling(252, min_periods=126).median()
    base = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d robust z
def f84ey_f84_semi_ey_spread_spreadrobustz_504d_slope_v140_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    med = sp.rolling(504, min_periods=252).median()
    mad = (sp - med).abs().rolling(504, min_periods=252).median()
    base = (sp - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d EY spread halflife proxy
def f84ey_f84_semi_ey_spread_halflife_21d_slope_v141_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = 1.0 - sp.rolling(21, min_periods=11).corr(sp.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EY spread halflife proxy
def f84ey_f84_semi_ey_spread_halflife_63d_slope_v142_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = 1.0 - sp.rolling(63, min_periods=32).corr(sp.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d EY spread halflife proxy
def f84ey_f84_semi_ey_spread_halflife_126d_slope_v143_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = 1.0 - sp.rolling(126, min_periods=63).corr(sp.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EY spread halflife proxy
def f84ey_f84_semi_ey_spread_halflife_252d_slope_v144_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = 1.0 - sp.rolling(252, min_periods=126).corr(sp.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EY spread halflife proxy
def f84ey_f84_semi_ey_spread_halflife_504d_slope_v145_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = 1.0 - sp.rolling(504, min_periods=252).corr(sp.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of composite short z-sum
def f84ey_f84_semi_ey_spread_compshort_slope_v146_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _z(sp, 21) + _z(sp, 63) + _z(sp, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite long z-sum
def f84ey_f84_semi_ey_spread_complong_slope_v147_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _z(sp, 63) + _z(sp, 126) + _z(sp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d normalized by price (closeadj-anchored)
def f84ey_f84_semi_ey_spread_priceanchor_21d_slope_v148_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    base = _mean(sp, 21) * closeadj.pct_change(21).abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d quality
def f84ey_f84_semi_ey_spread_quality_63d_slope_v149_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    z = _z(sp, 63)
    regime = np.sign(sp.ewm(span=21, adjust=False).mean() - sp.ewm(span=63, adjust=False).mean())
    base = z * pd.Series(regime, index=sp.index)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d quality
def f84ey_f84_semi_ey_spread_quality_252d_slope_v150_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    z = _z(sp, 252)
    regime = np.sign(sp.ewm(span=126, adjust=False).mean() - sp.ewm(span=252, adjust=False).mean())
    base = z * pd.Series(regime, index=sp.index)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)
