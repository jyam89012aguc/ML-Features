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

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f52_fca(ox, rev):
    return ox / rev.replace(0, np.nan)


def _f52_abs_scale(ox, rev):
    return (ox / rev.replace(0, np.nan)) * np.log(rev.replace(0, np.nan).abs())


# 5d curvature of level of opex per revenue dollar (fixed cost absorption) (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_21d_curv_v001_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of opex per revenue dollar (fixed cost absorption) (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_21d_curv_v002_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of opex per revenue dollar (fixed cost absorption) (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_21d_curv_v003_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of opex per revenue dollar (fixed cost absorption) (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_21d_curv_v004_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of opex per revenue dollar (fixed cost absorption) (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_21d_curv_v005_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of opex per revenue dollar (fixed cost absorption) (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_63d_curv_v006_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of opex per revenue dollar (fixed cost absorption) (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_63d_curv_v007_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of opex per revenue dollar (fixed cost absorption) (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_63d_curv_v008_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of opex per revenue dollar (fixed cost absorption) (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_63d_curv_v009_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of opex per revenue dollar (fixed cost absorption) (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fca_level_63d_curv_v010_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_21d_curv_v011_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_21d_curv_v012_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_21d_curv_v013_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_21d_curv_v014_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_21d_curv_v015_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_63d_curv_v016_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_63d_curv_v017_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_63d_curv_v018_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_63d_curv_v019_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_63d_curv_v020_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_126d_curv_v021_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_126d_curv_v022_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_126d_curv_v023_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_126d_curv_v024_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_z_126d_curv_v025_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_rng_63d_curv_v026_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_rng_63d_curv_v027_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_rng_63d_curv_v028_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_rng_63d_curv_v029_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_rng_63d_curv_v030_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of opex per revenue dollar (fixed cost absorption) in rolling range
def f52fca_semi_fixed_cost_absorption_fca_pos_63d_curv_v031_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of opex per revenue dollar (fixed cost absorption) in rolling range
def f52fca_semi_fixed_cost_absorption_fca_pos_63d_curv_v032_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of opex per revenue dollar (fixed cost absorption) in rolling range
def f52fca_semi_fixed_cost_absorption_fca_pos_63d_curv_v033_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of opex per revenue dollar (fixed cost absorption) in rolling range
def f52fca_semi_fixed_cost_absorption_fca_pos_63d_curv_v034_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of opex per revenue dollar (fixed cost absorption) in rolling range
def f52fca_semi_fixed_cost_absorption_fca_pos_63d_curv_v035_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of opex per revenue dollar (fixed cost absorption) from peak
def f52fca_semi_fixed_cost_absorption_fca_dd_63d_curv_v036_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of opex per revenue dollar (fixed cost absorption) from peak
def f52fca_semi_fixed_cost_absorption_fca_dd_63d_curv_v037_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of opex per revenue dollar (fixed cost absorption) from peak
def f52fca_semi_fixed_cost_absorption_fca_dd_63d_curv_v038_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of opex per revenue dollar (fixed cost absorption) from peak
def f52fca_semi_fixed_cost_absorption_fca_dd_63d_curv_v039_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of opex per revenue dollar (fixed cost absorption) from peak
def f52fca_semi_fixed_cost_absorption_fca_dd_63d_curv_v040_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of opex per revenue dollar (fixed cost absorption) above trough
def f52fca_semi_fixed_cost_absorption_fca_up_63d_curv_v041_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of opex per revenue dollar (fixed cost absorption) above trough
def f52fca_semi_fixed_cost_absorption_fca_up_63d_curv_v042_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of opex per revenue dollar (fixed cost absorption) above trough
def f52fca_semi_fixed_cost_absorption_fca_up_63d_curv_v043_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of opex per revenue dollar (fixed cost absorption) above trough
def f52fca_semi_fixed_cost_absorption_fca_up_63d_curv_v044_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of opex per revenue dollar (fixed cost absorption) above trough
def f52fca_semi_fixed_cost_absorption_fca_up_63d_curv_v045_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_std_63d_curv_v046_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_std_63d_curv_v047_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_std_63d_curv_v048_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_std_63d_curv_v049_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_std_63d_curv_v050_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_ema_63d_curv_v051_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_ema_63d_curv_v052_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_ema_63d_curv_v053_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_ema_63d_curv_v054_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_ema_63d_curv_v055_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive opex per revenue dollar (fixed cost absorption) changes
def f52fca_semi_fixed_cost_absorption_fca_hit_63d_curv_v056_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive opex per revenue dollar (fixed cost absorption) changes
def f52fca_semi_fixed_cost_absorption_fca_hit_63d_curv_v057_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive opex per revenue dollar (fixed cost absorption) changes
def f52fca_semi_fixed_cost_absorption_fca_hit_63d_curv_v058_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive opex per revenue dollar (fixed cost absorption) changes
def f52fca_semi_fixed_cost_absorption_fca_hit_63d_curv_v059_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive opex per revenue dollar (fixed cost absorption) changes
def f52fca_semi_fixed_cost_absorption_fca_hit_63d_curv_v060_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_cumsign_63d_curv_v061_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_cumsign_63d_curv_v062_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_cumsign_63d_curv_v063_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_cumsign_63d_curv_v064_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_cumsign_63d_curv_v065_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_robustz_63d_curv_v066_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_robustz_63d_curv_v067_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_robustz_63d_curv_v068_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_robustz_63d_curv_v069_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_robustz_63d_curv_v070_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_skew_63d_curv_v071_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_skew_63d_curv_v072_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_skew_63d_curv_v073_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_skew_63d_curv_v074_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of opex per revenue dollar (fixed cost absorption)
def f52fca_semi_fixed_cost_absorption_fca_skew_63d_curv_v075_signal(opex, revenue, closeadj):
    m = _f52_fca(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of fixed cost absorption scaled by log revenue (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_21d_curv_v076_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of fixed cost absorption scaled by log revenue (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_21d_curv_v077_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of fixed cost absorption scaled by log revenue (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_21d_curv_v078_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of fixed cost absorption scaled by log revenue (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_21d_curv_v079_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of fixed cost absorption scaled by log revenue (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_21d_curv_v080_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of fixed cost absorption scaled by log revenue (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_63d_curv_v081_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of fixed cost absorption scaled by log revenue (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_63d_curv_v082_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of fixed cost absorption scaled by log revenue (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_63d_curv_v083_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of fixed cost absorption scaled by log revenue (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_63d_curv_v084_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of fixed cost absorption scaled by log revenue (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_63d_curv_v085_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_21d_curv_v086_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_21d_curv_v087_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_21d_curv_v088_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_21d_curv_v089_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_21d_curv_v090_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_63d_curv_v091_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_63d_curv_v092_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_63d_curv_v093_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_63d_curv_v094_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_63d_curv_v095_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_126d_curv_v096_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_126d_curv_v097_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_126d_curv_v098_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_126d_curv_v099_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_126d_curv_v100_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_rng_63d_curv_v101_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_rng_63d_curv_v102_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_rng_63d_curv_v103_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_rng_63d_curv_v104_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_rng_63d_curv_v105_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of fixed cost absorption scaled by log revenue in rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_63d_curv_v106_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of fixed cost absorption scaled by log revenue in rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_63d_curv_v107_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of fixed cost absorption scaled by log revenue in rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_63d_curv_v108_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of fixed cost absorption scaled by log revenue in rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_63d_curv_v109_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of fixed cost absorption scaled by log revenue in rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_63d_curv_v110_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of fixed cost absorption scaled by log revenue from peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_63d_curv_v111_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of fixed cost absorption scaled by log revenue from peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_63d_curv_v112_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of fixed cost absorption scaled by log revenue from peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_63d_curv_v113_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of fixed cost absorption scaled by log revenue from peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_63d_curv_v114_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of fixed cost absorption scaled by log revenue from peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_63d_curv_v115_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of fixed cost absorption scaled by log revenue above trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_63d_curv_v116_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of fixed cost absorption scaled by log revenue above trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_63d_curv_v117_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of fixed cost absorption scaled by log revenue above trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_63d_curv_v118_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of fixed cost absorption scaled by log revenue above trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_63d_curv_v119_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of fixed cost absorption scaled by log revenue above trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_63d_curv_v120_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_std_63d_curv_v121_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_std_63d_curv_v122_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_std_63d_curv_v123_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_std_63d_curv_v124_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_std_63d_curv_v125_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_ema_63d_curv_v126_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_ema_63d_curv_v127_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_ema_63d_curv_v128_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_ema_63d_curv_v129_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_ema_63d_curv_v130_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_63d_curv_v131_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_63d_curv_v132_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_63d_curv_v133_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_63d_curv_v134_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_63d_curv_v135_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_63d_curv_v136_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_63d_curv_v137_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_63d_curv_v138_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_63d_curv_v139_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_63d_curv_v140_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_63d_curv_v141_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_63d_curv_v142_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_63d_curv_v143_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_63d_curv_v144_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_63d_curv_v145_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_63d_curv_v146_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_63d_curv_v147_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_63d_curv_v148_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_63d_curv_v149_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_63d_curv_v150_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
