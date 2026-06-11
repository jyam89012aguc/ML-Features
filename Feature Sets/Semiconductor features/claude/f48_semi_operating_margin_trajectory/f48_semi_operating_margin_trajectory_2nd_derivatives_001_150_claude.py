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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f48_om(oi, rev):
    return oi / rev.replace(0, np.nan)


def _f48_om_yoy(oi, rev):
    o = oi / rev.replace(0, np.nan)
    return o - o.shift(252)


# 5d slope of level of operating margin YoY change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_21d_slope_v001_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of operating margin YoY change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_21d_slope_v002_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of operating margin YoY change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_21d_slope_v003_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of operating margin YoY change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_21d_slope_v004_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of operating margin YoY change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_21d_slope_v005_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of operating margin YoY change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_63d_slope_v006_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of operating margin YoY change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_63d_slope_v007_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of operating margin YoY change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_63d_slope_v008_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of operating margin YoY change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_63d_slope_v009_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of operating margin YoY change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omyoy_level_63d_slope_v010_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_21d_slope_v011_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_21d_slope_v012_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_21d_slope_v013_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_21d_slope_v014_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_21d_slope_v015_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_63d_slope_v016_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_63d_slope_v017_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_63d_slope_v018_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_63d_slope_v019_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_63d_slope_v020_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_126d_slope_v021_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_126d_slope_v022_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_126d_slope_v023_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_126d_slope_v024_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_z_126d_slope_v025_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_rng_63d_slope_v026_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_rng_63d_slope_v027_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_rng_63d_slope_v028_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_rng_63d_slope_v029_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_rng_63d_slope_v030_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d position of operating margin YoY change in rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_63d_slope_v031_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position of operating margin YoY change in rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_63d_slope_v032_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d position of operating margin YoY change in rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_63d_slope_v033_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d position of operating margin YoY change in rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_63d_slope_v034_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d position of operating margin YoY change in rolling range
def f48omt_semi_operating_margin_trajectory_omyoy_pos_63d_slope_v035_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown of operating margin YoY change from peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_63d_slope_v036_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown of operating margin YoY change from peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_63d_slope_v037_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown of operating margin YoY change from peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_63d_slope_v038_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown of operating margin YoY change from peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_63d_slope_v039_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown of operating margin YoY change from peak
def f48omt_semi_operating_margin_trajectory_omyoy_dd_63d_slope_v040_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d run-up of operating margin YoY change above trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_63d_slope_v041_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up of operating margin YoY change above trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_63d_slope_v042_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d run-up of operating margin YoY change above trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_63d_slope_v043_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d run-up of operating margin YoY change above trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_63d_slope_v044_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d run-up of operating margin YoY change above trough
def f48omt_semi_operating_margin_trajectory_omyoy_up_63d_slope_v045_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_std_63d_slope_v046_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_std_63d_slope_v047_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_std_63d_slope_v048_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_std_63d_slope_v049_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_std_63d_slope_v050_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d EMA-crossover of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_ema_63d_slope_v051_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EMA-crossover of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_ema_63d_slope_v052_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d EMA-crossover of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_ema_63d_slope_v053_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d EMA-crossover of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_ema_63d_slope_v054_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d EMA-crossover of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_ema_63d_slope_v055_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_63d_slope_v056_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_63d_slope_v057_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_63d_slope_v058_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_63d_slope_v059_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-ratio of positive operating margin YoY change changes
def f48omt_semi_operating_margin_trajectory_omyoy_hit_63d_slope_v060_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_63d_slope_v061_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_63d_slope_v062_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_63d_slope_v063_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_63d_slope_v064_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d signed cumulative changes of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_cumsign_63d_slope_v065_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robust z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_63d_slope_v066_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_63d_slope_v067_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robust z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_63d_slope_v068_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robust z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_63d_slope_v069_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d robust z-score of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_robustz_63d_slope_v070_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_63d_slope_v071_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_63d_slope_v072_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_63d_slope_v073_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_63d_slope_v074_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew of operating margin YoY change
def f48omt_semi_operating_margin_trajectory_omyoy_skew_63d_slope_v075_signal(opinc, revenue, closeadj):
    m = _f48_om_yoy(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of operating margin QoQ change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_21d_slope_v076_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of operating margin QoQ change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_21d_slope_v077_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of operating margin QoQ change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_21d_slope_v078_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of operating margin QoQ change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_21d_slope_v079_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of operating margin QoQ change (21d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_21d_slope_v080_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of operating margin QoQ change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_63d_slope_v081_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of operating margin QoQ change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_63d_slope_v082_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of operating margin QoQ change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_63d_slope_v083_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of operating margin QoQ change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_63d_slope_v084_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of operating margin QoQ change (63d mean-centered)
def f48omt_semi_operating_margin_trajectory_omqoq_level_63d_slope_v085_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_21d_slope_v086_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_21d_slope_v087_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_21d_slope_v088_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_21d_slope_v089_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_21d_slope_v090_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_63d_slope_v091_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_63d_slope_v092_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_63d_slope_v093_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_63d_slope_v094_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_63d_slope_v095_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_126d_slope_v096_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_126d_slope_v097_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_126d_slope_v098_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_126d_slope_v099_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_z_126d_slope_v100_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_rng_63d_slope_v101_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_rng_63d_slope_v102_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_rng_63d_slope_v103_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_rng_63d_slope_v104_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_rng_63d_slope_v105_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d position of operating margin QoQ change in rolling range
def f48omt_semi_operating_margin_trajectory_omqoq_pos_63d_slope_v106_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position of operating margin QoQ change in rolling range
def f48omt_semi_operating_margin_trajectory_omqoq_pos_63d_slope_v107_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d position of operating margin QoQ change in rolling range
def f48omt_semi_operating_margin_trajectory_omqoq_pos_63d_slope_v108_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d position of operating margin QoQ change in rolling range
def f48omt_semi_operating_margin_trajectory_omqoq_pos_63d_slope_v109_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d position of operating margin QoQ change in rolling range
def f48omt_semi_operating_margin_trajectory_omqoq_pos_63d_slope_v110_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown of operating margin QoQ change from peak
def f48omt_semi_operating_margin_trajectory_omqoq_dd_63d_slope_v111_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown of operating margin QoQ change from peak
def f48omt_semi_operating_margin_trajectory_omqoq_dd_63d_slope_v112_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown of operating margin QoQ change from peak
def f48omt_semi_operating_margin_trajectory_omqoq_dd_63d_slope_v113_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown of operating margin QoQ change from peak
def f48omt_semi_operating_margin_trajectory_omqoq_dd_63d_slope_v114_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown of operating margin QoQ change from peak
def f48omt_semi_operating_margin_trajectory_omqoq_dd_63d_slope_v115_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d run-up of operating margin QoQ change above trough
def f48omt_semi_operating_margin_trajectory_omqoq_up_63d_slope_v116_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up of operating margin QoQ change above trough
def f48omt_semi_operating_margin_trajectory_omqoq_up_63d_slope_v117_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d run-up of operating margin QoQ change above trough
def f48omt_semi_operating_margin_trajectory_omqoq_up_63d_slope_v118_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d run-up of operating margin QoQ change above trough
def f48omt_semi_operating_margin_trajectory_omqoq_up_63d_slope_v119_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d run-up of operating margin QoQ change above trough
def f48omt_semi_operating_margin_trajectory_omqoq_up_63d_slope_v120_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_std_63d_slope_v121_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_std_63d_slope_v122_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_std_63d_slope_v123_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_std_63d_slope_v124_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_std_63d_slope_v125_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d EMA-crossover of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_ema_63d_slope_v126_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EMA-crossover of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_ema_63d_slope_v127_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d EMA-crossover of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_ema_63d_slope_v128_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d EMA-crossover of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_ema_63d_slope_v129_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d EMA-crossover of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_ema_63d_slope_v130_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-ratio of positive operating margin QoQ change changes
def f48omt_semi_operating_margin_trajectory_omqoq_hit_63d_slope_v131_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-ratio of positive operating margin QoQ change changes
def f48omt_semi_operating_margin_trajectory_omqoq_hit_63d_slope_v132_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-ratio of positive operating margin QoQ change changes
def f48omt_semi_operating_margin_trajectory_omqoq_hit_63d_slope_v133_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-ratio of positive operating margin QoQ change changes
def f48omt_semi_operating_margin_trajectory_omqoq_hit_63d_slope_v134_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-ratio of positive operating margin QoQ change changes
def f48omt_semi_operating_margin_trajectory_omqoq_hit_63d_slope_v135_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d signed cumulative changes of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_cumsign_63d_slope_v136_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed cumulative changes of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_cumsign_63d_slope_v137_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d signed cumulative changes of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_cumsign_63d_slope_v138_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d signed cumulative changes of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_cumsign_63d_slope_v139_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d signed cumulative changes of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_cumsign_63d_slope_v140_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robust z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_robustz_63d_slope_v141_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_robustz_63d_slope_v142_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robust z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_robustz_63d_slope_v143_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robust z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_robustz_63d_slope_v144_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d robust z-score of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_robustz_63d_slope_v145_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_skew_63d_slope_v146_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_skew_63d_slope_v147_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_skew_63d_slope_v148_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_skew_63d_slope_v149_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew of operating margin QoQ change
def f48omt_semi_operating_margin_trajectory_omqoq_skew_63d_slope_v150_signal(opinc, revenue, closeadj):
    o = _f48_om(opinc, revenue)
    m = o - o.shift(63)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
