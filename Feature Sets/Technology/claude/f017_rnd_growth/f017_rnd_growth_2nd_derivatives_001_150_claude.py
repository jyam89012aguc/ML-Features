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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f017_qchg(rnd):
    return rnd.diff(periods=63)


def _f017_ychg(rnd):
    return rnd.diff(periods=252)


# 21d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slope_21d_2d_v001_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slope_63d_2d_v002_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slope_126d_2d_v003_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slope_252d_2d_v004_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slope_504d_2d_v005_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slope_21d_2d_v006_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slope_63d_2d_v007_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slope_126d_2d_v008_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slope_252d_2d_v009_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slope_504d_2d_v010_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slope_21d_2d_v011_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slope_63d_2d_v012_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slope_126d_2d_v013_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slope_252d_2d_v014_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slope_504d_2d_v015_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slope_21d_2d_v016_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slope_63d_2d_v017_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slope_126d_2d_v018_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slope_252d_2d_v019_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slope_504d_2d_v020_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slope_21d_2d_v021_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slope_63d_2d_v022_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slope_126d_2d_v023_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slope_252d_2d_v024_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slope_504d_2d_v025_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slope_21d_2d_v026_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slope_63d_2d_v027_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slope_126d_2d_v028_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slope_252d_2d_v029_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slope_504d_2d_v030_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slope_21d_2d_v031_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slope_63d_2d_v032_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slope_126d_2d_v033_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slope_252d_2d_v034_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slope_504d_2d_v035_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sm21_sl21_2d_v036_signal(rnd, closeadj):
    base = _mean(_f017_qchg(rnd), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sm63_sl21_2d_v037_signal(rnd, closeadj):
    base = _mean(_f017_qchg(rnd), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sm63_sl63_2d_v038_signal(rnd, closeadj):
    base = _mean(_f017_qchg(rnd), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sm252_sl63_2d_v039_signal(rnd, closeadj):
    base = _mean(_f017_qchg(rnd), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sm252_sl126_2d_v040_signal(rnd, closeadj):
    base = _mean(_f017_qchg(rnd), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sm21_sl21_2d_v041_signal(rnd, closeadj):
    base = _mean(_f017_ychg(rnd), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sm63_sl21_2d_v042_signal(rnd, closeadj):
    base = _mean(_f017_ychg(rnd), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sm63_sl63_2d_v043_signal(rnd, closeadj):
    base = _mean(_f017_ychg(rnd), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sm252_sl63_2d_v044_signal(rnd, closeadj):
    base = _mean(_f017_ychg(rnd), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sm252_sl126_2d_v045_signal(rnd, closeadj):
    base = _mean(_f017_ychg(rnd), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sm21_sl21_2d_v046_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sm63_sl21_2d_v047_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sm63_sl63_2d_v048_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sm252_sl63_2d_v049_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sm252_sl126_2d_v050_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sm21_sl21_2d_v051_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sm63_sl21_2d_v052_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sm63_sl63_2d_v053_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sm252_sl63_2d_v054_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sm252_sl126_2d_v055_signal(rnd, closeadj):
    base = _mean(rnd.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sm21_sl21_2d_v056_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252) - revenue.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sm63_sl21_2d_v057_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sm63_sl63_2d_v058_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sm252_sl63_2d_v059_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sm252_sl126_2d_v060_signal(rnd, revenue, closeadj):
    base = _mean(rnd.pct_change(periods=252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sm21_sl21_2d_v061_signal(rnd, closeadj):
    base = _mean(rnd / rnd.shift(252).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sm63_sl21_2d_v062_signal(rnd, closeadj):
    base = _mean(rnd / rnd.shift(252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sm63_sl63_2d_v063_signal(rnd, closeadj):
    base = _mean(rnd / rnd.shift(252).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sm252_sl63_2d_v064_signal(rnd, closeadj):
    base = _mean(rnd / rnd.shift(252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sm252_sl126_2d_v065_signal(rnd, closeadj):
    base = _mean(rnd / rnd.shift(252).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sm21_sl21_2d_v066_signal(rnd, closeadj):
    base = _mean(np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sm63_sl21_2d_v067_signal(rnd, closeadj):
    base = _mean(np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sm63_sl63_2d_v068_signal(rnd, closeadj):
    base = _mean(np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sm252_sl63_2d_v069_signal(rnd, closeadj):
    base = _mean(np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sm252_sl126_2d_v070_signal(rnd, closeadj):
    base = _mean(np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_pctslope_21d_2d_v071_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_pctslope_63d_2d_v072_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_pctslope_252d_2d_v073_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_pctslope_21d_2d_v074_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_pctslope_63d_2d_v075_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_pctslope_252d_2d_v076_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_pctslope_21d_2d_v077_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_pctslope_63d_2d_v078_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_pctslope_252d_2d_v079_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_pctslope_21d_2d_v080_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_pctslope_63d_2d_v081_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_pctslope_252d_2d_v082_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_pctslope_21d_2d_v083_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_pctslope_63d_2d_v084_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_pctslope_252d_2d_v085_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_pctslope_21d_2d_v086_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_pctslope_63d_2d_v087_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_pctslope_252d_2d_v088_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_pctslope_21d_2d_v089_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_pctslope_63d_2d_v090_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_pctslope_252d_2d_v091_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sgnslope_21d_2d_v092_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sgnslope_63d_2d_v093_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_sgnslope_252d_2d_v094_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sgnslope_21d_2d_v095_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sgnslope_63d_2d_v096_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_sgnslope_252d_2d_v097_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sgnslope_21d_2d_v098_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sgnslope_63d_2d_v099_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_sgnslope_252d_2d_v100_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sgnslope_21d_2d_v101_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sgnslope_63d_2d_v102_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_sgnslope_252d_2d_v103_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sgnslope_21d_2d_v104_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sgnslope_63d_2d_v105_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_sgnslope_252d_2d_v106_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sgnslope_21d_2d_v107_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sgnslope_63d_2d_v108_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_sgnslope_252d_2d_v109_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sgnslope_21d_2d_v110_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sgnslope_63d_2d_v111_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_sgnslope_252d_2d_v112_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_logmagslope_21d_2d_v113_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_logmagslope_63d_2d_v114_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_logmagslope_252d_2d_v115_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_logmagslope_21d_2d_v116_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_logmagslope_63d_2d_v117_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_logmagslope_252d_2d_v118_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_logmagslope_21d_2d_v119_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_logmagslope_63d_2d_v120_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_logmagslope_252d_2d_v121_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_logmagslope_21d_2d_v122_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_logmagslope_63d_2d_v123_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_logmagslope_252d_2d_v124_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_logmagslope_21d_2d_v125_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_logmagslope_63d_2d_v126_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_logmagslope_252d_2d_v127_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_logmagslope_21d_2d_v128_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_logmagslope_63d_2d_v129_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_logmagslope_252d_2d_v130_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_logmagslope_21d_2d_v131_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_logmagslope_63d_2d_v132_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_logmagslope_252d_2d_v133_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_qchg|
def f017rdg_f017_rnd_growth_rnd_qchg_logslope_63d_2d_v134_signal(rnd, closeadj):
    base = np.log((_f017_qchg(rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_qchg|
def f017rdg_f017_rnd_growth_rnd_qchg_logslope_252d_2d_v135_signal(rnd, closeadj):
    base = np.log((_f017_qchg(rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_ychg|
def f017rdg_f017_rnd_growth_rnd_ychg_logslope_63d_2d_v136_signal(rnd, closeadj):
    base = np.log((_f017_ychg(rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_ychg|
def f017rdg_f017_rnd_growth_rnd_ychg_logslope_252d_2d_v137_signal(rnd, closeadj):
    base = np.log((_f017_ychg(rnd)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_pct_q|
def f017rdg_f017_rnd_growth_rnd_pct_q_logslope_63d_2d_v138_signal(rnd, closeadj):
    base = np.log((rnd.pct_change(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_pct_q|
def f017rdg_f017_rnd_growth_rnd_pct_q_logslope_252d_2d_v139_signal(rnd, closeadj):
    base = np.log((rnd.pct_change(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_pct_y|
def f017rdg_f017_rnd_growth_rnd_pct_y_logslope_63d_2d_v140_signal(rnd, closeadj):
    base = np.log((rnd.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_pct_y|
def f017rdg_f017_rnd_growth_rnd_pct_y_logslope_252d_2d_v141_signal(rnd, closeadj):
    base = np.log((rnd.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_growth_to_rev_growth|
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_logslope_63d_2d_v142_signal(rnd, revenue, closeadj):
    base = np.log((rnd.pct_change(periods=252) - revenue.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_growth_to_rev_growth|
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_logslope_252d_2d_v143_signal(rnd, revenue, closeadj):
    base = np.log((rnd.pct_change(periods=252) - revenue.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_to_prior|
def f017rdg_f017_rnd_growth_rnd_to_prior_logslope_63d_2d_v144_signal(rnd, closeadj):
    base = np.log((rnd / rnd.shift(252).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_to_prior|
def f017rdg_f017_rnd_growth_rnd_to_prior_logslope_252d_2d_v145_signal(rnd, closeadj):
    base = np.log((rnd / rnd.shift(252).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rnd_log_growth|
def f017rdg_f017_rnd_growth_rnd_log_growth_logslope_63d_2d_v146_signal(rnd, closeadj):
    base = np.log((np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rnd_log_growth|
def f017rdg_f017_rnd_growth_rnd_log_growth_logslope_252d_2d_v147_signal(rnd, closeadj):
    base = np.log((np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

