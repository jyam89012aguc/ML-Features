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


# 21d acceleration of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_accel_21d_3d_v001_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_accel_63d_3d_v002_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_accel_126d_3d_v003_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_accel_252d_3d_v004_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_accel_21d_3d_v005_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_accel_63d_3d_v006_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_accel_126d_3d_v007_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_accel_252d_3d_v008_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_accel_21d_3d_v009_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_accel_63d_3d_v010_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_accel_126d_3d_v011_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_accel_252d_3d_v012_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_accel_21d_3d_v013_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_accel_63d_3d_v014_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_accel_126d_3d_v015_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_accel_252d_3d_v016_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_accel_21d_3d_v017_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_accel_63d_3d_v018_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_accel_126d_3d_v019_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_accel_252d_3d_v020_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_accel_21d_3d_v021_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_accel_63d_3d_v022_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_accel_126d_3d_v023_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_accel_252d_3d_v024_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_accel_21d_3d_v025_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_accel_63d_3d_v026_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_accel_126d_3d_v027_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_accel_252d_3d_v028_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slopez_21d_z126_3d_v029_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slopez_63d_z252_3d_v030_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slopez_126d_z252_3d_v031_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_slopez_252d_z504_3d_v032_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slopez_21d_z126_3d_v033_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slopez_63d_z252_3d_v034_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slopez_126d_z252_3d_v035_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_slopez_252d_z504_3d_v036_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slopez_21d_z126_3d_v037_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slopez_63d_z252_3d_v038_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slopez_126d_z252_3d_v039_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_slopez_252d_z504_3d_v040_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slopez_21d_z126_3d_v041_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slopez_63d_z252_3d_v042_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slopez_126d_z252_3d_v043_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_slopez_252d_z504_3d_v044_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slopez_21d_z126_3d_v045_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slopez_63d_z252_3d_v046_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slopez_126d_z252_3d_v047_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_slopez_252d_z504_3d_v048_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slopez_21d_z126_3d_v049_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slopez_63d_z252_3d_v050_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slopez_126d_z252_3d_v051_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_slopez_252d_z504_3d_v052_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slopez_21d_z126_3d_v053_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slopez_63d_z252_3d_v054_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slopez_126d_z252_3d_v055_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_slopez_252d_z504_3d_v056_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_jerk_21d_3d_v057_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_jerk_63d_3d_v058_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_jerk_126d_3d_v059_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_jerk_21d_3d_v060_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_jerk_63d_3d_v061_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_jerk_126d_3d_v062_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_jerk_21d_3d_v063_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_jerk_63d_3d_v064_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_jerk_126d_3d_v065_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_jerk_21d_3d_v066_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_jerk_63d_3d_v067_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_jerk_126d_3d_v068_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_jerk_21d_3d_v069_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_jerk_63d_3d_v070_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_jerk_126d_3d_v071_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_jerk_21d_3d_v072_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_jerk_63d_3d_v073_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_jerk_126d_3d_v074_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_jerk_21d_3d_v075_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_jerk_63d_3d_v076_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_jerk_126d_3d_v077_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_qchg smoothed over 252d
def f017rdg_f017_rnd_growth_rnd_qchg_smoothaccel_63d_sm252_3d_v078_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_qchg smoothed over 504d
def f017rdg_f017_rnd_growth_rnd_qchg_smoothaccel_252d_sm504_3d_v079_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_ychg smoothed over 252d
def f017rdg_f017_rnd_growth_rnd_ychg_smoothaccel_63d_sm252_3d_v080_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_ychg smoothed over 504d
def f017rdg_f017_rnd_growth_rnd_ychg_smoothaccel_252d_sm504_3d_v081_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_pct_q smoothed over 252d
def f017rdg_f017_rnd_growth_rnd_pct_q_smoothaccel_63d_sm252_3d_v082_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_pct_q smoothed over 504d
def f017rdg_f017_rnd_growth_rnd_pct_q_smoothaccel_252d_sm504_3d_v083_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_pct_y smoothed over 252d
def f017rdg_f017_rnd_growth_rnd_pct_y_smoothaccel_63d_sm252_3d_v084_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_pct_y smoothed over 504d
def f017rdg_f017_rnd_growth_rnd_pct_y_smoothaccel_252d_sm504_3d_v085_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_growth_to_rev_growth smoothed over 252d
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_smoothaccel_63d_sm252_3d_v086_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_growth_to_rev_growth smoothed over 504d
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_smoothaccel_252d_sm504_3d_v087_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_to_prior smoothed over 252d
def f017rdg_f017_rnd_growth_rnd_to_prior_smoothaccel_63d_sm252_3d_v088_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_to_prior smoothed over 504d
def f017rdg_f017_rnd_growth_rnd_to_prior_smoothaccel_252d_sm504_3d_v089_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_log_growth smoothed over 252d
def f017rdg_f017_rnd_growth_rnd_log_growth_smoothaccel_63d_sm252_3d_v090_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_log_growth smoothed over 504d
def f017rdg_f017_rnd_growth_rnd_log_growth_smoothaccel_252d_sm504_3d_v091_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_accelz_21d_z252_3d_v092_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_accelz_63d_z504_3d_v093_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_accelz_21d_z252_3d_v094_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_accelz_63d_z504_3d_v095_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_accelz_21d_z252_3d_v096_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_accelz_63d_z504_3d_v097_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_accelz_21d_z252_3d_v098_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_accelz_63d_z504_3d_v099_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_accelz_21d_z252_3d_v100_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_accelz_63d_z504_3d_v101_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_accelz_21d_z252_3d_v102_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_accelz_63d_z504_3d_v103_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_accelz_21d_z252_3d_v104_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_accelz_63d_z504_3d_v105_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_qchg (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_qchg_signflip_63d_3d_v106_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_qchg (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_qchg_signflip_252d_3d_v107_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_ychg (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_ychg_signflip_63d_3d_v108_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_ychg (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_ychg_signflip_252d_3d_v109_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_pct_q (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_pct_q_signflip_63d_3d_v110_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_pct_q (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_pct_q_signflip_252d_3d_v111_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_pct_y (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_pct_y_signflip_63d_3d_v112_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_pct_y (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_pct_y_signflip_252d_3d_v113_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_growth_to_rev_growth (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_signflip_63d_3d_v114_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_growth_to_rev_growth (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_signflip_252d_3d_v115_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_to_prior (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_to_prior_signflip_63d_3d_v116_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_to_prior (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_to_prior_signflip_252d_3d_v117_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_log_growth (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_log_growth_signflip_63d_3d_v118_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_log_growth (raw count, no price scaling)
def f017rdg_f017_rnd_growth_rnd_log_growth_signflip_252d_3d_v119_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_qchg normalized by 252d range
def f017rdg_f017_rnd_growth_rnd_qchg_rngaccel_63d_r252_3d_v120_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_qchg normalized by 504d range
def f017rdg_f017_rnd_growth_rnd_qchg_rngaccel_252d_r504_3d_v121_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_ychg normalized by 252d range
def f017rdg_f017_rnd_growth_rnd_ychg_rngaccel_63d_r252_3d_v122_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_ychg normalized by 504d range
def f017rdg_f017_rnd_growth_rnd_ychg_rngaccel_252d_r504_3d_v123_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_pct_q normalized by 252d range
def f017rdg_f017_rnd_growth_rnd_pct_q_rngaccel_63d_r252_3d_v124_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_pct_q normalized by 504d range
def f017rdg_f017_rnd_growth_rnd_pct_q_rngaccel_252d_r504_3d_v125_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_pct_y normalized by 252d range
def f017rdg_f017_rnd_growth_rnd_pct_y_rngaccel_63d_r252_3d_v126_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_pct_y normalized by 504d range
def f017rdg_f017_rnd_growth_rnd_pct_y_rngaccel_252d_r504_3d_v127_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_growth_to_rev_growth normalized by 252d range
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_rngaccel_63d_r252_3d_v128_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_growth_to_rev_growth normalized by 504d range
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_rngaccel_252d_r504_3d_v129_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_to_prior normalized by 252d range
def f017rdg_f017_rnd_growth_rnd_to_prior_rngaccel_63d_r252_3d_v130_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_to_prior normalized by 504d range
def f017rdg_f017_rnd_growth_rnd_to_prior_rngaccel_252d_r504_3d_v131_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_log_growth normalized by 252d range
def f017rdg_f017_rnd_growth_rnd_log_growth_rngaccel_63d_r252_3d_v132_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_log_growth normalized by 504d range
def f017rdg_f017_rnd_growth_rnd_log_growth_rngaccel_252d_r504_3d_v133_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_cumslope_21d_3d_v134_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_cumslope_63d_3d_v135_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_cumslope_252d_3d_v136_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_cumslope_21d_3d_v137_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_cumslope_63d_3d_v138_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_cumslope_252d_3d_v139_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_cumslope_21d_3d_v140_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_cumslope_63d_3d_v141_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_cumslope_252d_3d_v142_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_cumslope_21d_3d_v143_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_cumslope_63d_3d_v144_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_cumslope_252d_3d_v145_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_cumslope_21d_3d_v146_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_cumslope_63d_3d_v147_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_cumslope_252d_3d_v148_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_cumslope_21d_3d_v149_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_cumslope_63d_3d_v150_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

