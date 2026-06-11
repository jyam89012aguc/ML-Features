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
def _f47_om(oi, rev):
    return oi / rev.replace(0, np.nan)


def _f47_om_log(oi, rev):
    return np.log(oi.replace(0, np.nan).abs() / rev.replace(0, np.nan).abs())


# 5d curvature of level of operating margin (opinc/rev) (21d mean-centered)
def f47oml_semi_operating_margin_level_om_level_21d_curv_v001_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of operating margin (opinc/rev) (21d mean-centered)
def f47oml_semi_operating_margin_level_om_level_21d_curv_v002_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of operating margin (opinc/rev) (21d mean-centered)
def f47oml_semi_operating_margin_level_om_level_21d_curv_v003_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of operating margin (opinc/rev) (21d mean-centered)
def f47oml_semi_operating_margin_level_om_level_21d_curv_v004_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of operating margin (opinc/rev) (21d mean-centered)
def f47oml_semi_operating_margin_level_om_level_21d_curv_v005_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of operating margin (opinc/rev) (63d mean-centered)
def f47oml_semi_operating_margin_level_om_level_63d_curv_v006_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of operating margin (opinc/rev) (63d mean-centered)
def f47oml_semi_operating_margin_level_om_level_63d_curv_v007_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of operating margin (opinc/rev) (63d mean-centered)
def f47oml_semi_operating_margin_level_om_level_63d_curv_v008_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of operating margin (opinc/rev) (63d mean-centered)
def f47oml_semi_operating_margin_level_om_level_63d_curv_v009_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of operating margin (opinc/rev) (63d mean-centered)
def f47oml_semi_operating_margin_level_om_level_63d_curv_v010_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_21d_curv_v011_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_21d_curv_v012_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_21d_curv_v013_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_21d_curv_v014_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_21d_curv_v015_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_63d_curv_v016_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_63d_curv_v017_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_63d_curv_v018_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_63d_curv_v019_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_63d_curv_v020_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_126d_curv_v021_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_126d_curv_v022_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_126d_curv_v023_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_126d_curv_v024_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_z_126d_curv_v025_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_rng_63d_curv_v026_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_rng_63d_curv_v027_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_rng_63d_curv_v028_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_rng_63d_curv_v029_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_rng_63d_curv_v030_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of operating margin (opinc/rev) in rolling range
def f47oml_semi_operating_margin_level_om_pos_63d_curv_v031_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of operating margin (opinc/rev) in rolling range
def f47oml_semi_operating_margin_level_om_pos_63d_curv_v032_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of operating margin (opinc/rev) in rolling range
def f47oml_semi_operating_margin_level_om_pos_63d_curv_v033_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of operating margin (opinc/rev) in rolling range
def f47oml_semi_operating_margin_level_om_pos_63d_curv_v034_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of operating margin (opinc/rev) in rolling range
def f47oml_semi_operating_margin_level_om_pos_63d_curv_v035_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of operating margin (opinc/rev) from peak
def f47oml_semi_operating_margin_level_om_dd_63d_curv_v036_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of operating margin (opinc/rev) from peak
def f47oml_semi_operating_margin_level_om_dd_63d_curv_v037_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of operating margin (opinc/rev) from peak
def f47oml_semi_operating_margin_level_om_dd_63d_curv_v038_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of operating margin (opinc/rev) from peak
def f47oml_semi_operating_margin_level_om_dd_63d_curv_v039_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of operating margin (opinc/rev) from peak
def f47oml_semi_operating_margin_level_om_dd_63d_curv_v040_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of operating margin (opinc/rev) above trough
def f47oml_semi_operating_margin_level_om_up_63d_curv_v041_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of operating margin (opinc/rev) above trough
def f47oml_semi_operating_margin_level_om_up_63d_curv_v042_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of operating margin (opinc/rev) above trough
def f47oml_semi_operating_margin_level_om_up_63d_curv_v043_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of operating margin (opinc/rev) above trough
def f47oml_semi_operating_margin_level_om_up_63d_curv_v044_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of operating margin (opinc/rev) above trough
def f47oml_semi_operating_margin_level_om_up_63d_curv_v045_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_std_63d_curv_v046_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_std_63d_curv_v047_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_std_63d_curv_v048_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_std_63d_curv_v049_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_std_63d_curv_v050_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_ema_63d_curv_v051_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_ema_63d_curv_v052_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_ema_63d_curv_v053_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_ema_63d_curv_v054_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_ema_63d_curv_v055_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive operating margin (opinc/rev) changes
def f47oml_semi_operating_margin_level_om_hit_63d_curv_v056_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive operating margin (opinc/rev) changes
def f47oml_semi_operating_margin_level_om_hit_63d_curv_v057_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive operating margin (opinc/rev) changes
def f47oml_semi_operating_margin_level_om_hit_63d_curv_v058_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive operating margin (opinc/rev) changes
def f47oml_semi_operating_margin_level_om_hit_63d_curv_v059_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive operating margin (opinc/rev) changes
def f47oml_semi_operating_margin_level_om_hit_63d_curv_v060_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_cumsign_63d_curv_v061_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_cumsign_63d_curv_v062_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_cumsign_63d_curv_v063_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_cumsign_63d_curv_v064_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_cumsign_63d_curv_v065_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_robustz_63d_curv_v066_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_robustz_63d_curv_v067_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_robustz_63d_curv_v068_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_robustz_63d_curv_v069_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_robustz_63d_curv_v070_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_skew_63d_curv_v071_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_skew_63d_curv_v072_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_skew_63d_curv_v073_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_skew_63d_curv_v074_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of operating margin (opinc/rev)
def f47oml_semi_operating_margin_level_om_skew_63d_curv_v075_signal(opinc, revenue, closeadj):
    m = _f47_om(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log operating margin (21d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_21d_curv_v076_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log operating margin (21d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_21d_curv_v077_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log operating margin (21d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_21d_curv_v078_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log operating margin (21d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_21d_curv_v079_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log operating margin (21d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_21d_curv_v080_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log operating margin (63d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_63d_curv_v081_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log operating margin (63d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_63d_curv_v082_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log operating margin (63d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_63d_curv_v083_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log operating margin (63d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_63d_curv_v084_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log operating margin (63d mean-centered)
def f47oml_semi_operating_margin_level_omlog_level_63d_curv_v085_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_21d_curv_v086_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_21d_curv_v087_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_21d_curv_v088_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_21d_curv_v089_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_21d_curv_v090_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_63d_curv_v091_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_63d_curv_v092_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_63d_curv_v093_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_63d_curv_v094_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_63d_curv_v095_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_126d_curv_v096_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_126d_curv_v097_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_126d_curv_v098_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_126d_curv_v099_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_z_126d_curv_v100_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of log operating margin
def f47oml_semi_operating_margin_level_omlog_rng_63d_curv_v101_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of log operating margin
def f47oml_semi_operating_margin_level_omlog_rng_63d_curv_v102_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of log operating margin
def f47oml_semi_operating_margin_level_omlog_rng_63d_curv_v103_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of log operating margin
def f47oml_semi_operating_margin_level_omlog_rng_63d_curv_v104_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of log operating margin
def f47oml_semi_operating_margin_level_omlog_rng_63d_curv_v105_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of log operating margin in rolling range
def f47oml_semi_operating_margin_level_omlog_pos_63d_curv_v106_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of log operating margin in rolling range
def f47oml_semi_operating_margin_level_omlog_pos_63d_curv_v107_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of log operating margin in rolling range
def f47oml_semi_operating_margin_level_omlog_pos_63d_curv_v108_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of log operating margin in rolling range
def f47oml_semi_operating_margin_level_omlog_pos_63d_curv_v109_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of log operating margin in rolling range
def f47oml_semi_operating_margin_level_omlog_pos_63d_curv_v110_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of log operating margin from peak
def f47oml_semi_operating_margin_level_omlog_dd_63d_curv_v111_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of log operating margin from peak
def f47oml_semi_operating_margin_level_omlog_dd_63d_curv_v112_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of log operating margin from peak
def f47oml_semi_operating_margin_level_omlog_dd_63d_curv_v113_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of log operating margin from peak
def f47oml_semi_operating_margin_level_omlog_dd_63d_curv_v114_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of log operating margin from peak
def f47oml_semi_operating_margin_level_omlog_dd_63d_curv_v115_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of log operating margin above trough
def f47oml_semi_operating_margin_level_omlog_up_63d_curv_v116_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of log operating margin above trough
def f47oml_semi_operating_margin_level_omlog_up_63d_curv_v117_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of log operating margin above trough
def f47oml_semi_operating_margin_level_omlog_up_63d_curv_v118_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of log operating margin above trough
def f47oml_semi_operating_margin_level_omlog_up_63d_curv_v119_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of log operating margin above trough
def f47oml_semi_operating_margin_level_omlog_up_63d_curv_v120_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of log operating margin
def f47oml_semi_operating_margin_level_omlog_std_63d_curv_v121_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of log operating margin
def f47oml_semi_operating_margin_level_omlog_std_63d_curv_v122_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of log operating margin
def f47oml_semi_operating_margin_level_omlog_std_63d_curv_v123_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of log operating margin
def f47oml_semi_operating_margin_level_omlog_std_63d_curv_v124_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of log operating margin
def f47oml_semi_operating_margin_level_omlog_std_63d_curv_v125_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of log operating margin
def f47oml_semi_operating_margin_level_omlog_ema_63d_curv_v126_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of log operating margin
def f47oml_semi_operating_margin_level_omlog_ema_63d_curv_v127_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of log operating margin
def f47oml_semi_operating_margin_level_omlog_ema_63d_curv_v128_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of log operating margin
def f47oml_semi_operating_margin_level_omlog_ema_63d_curv_v129_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of log operating margin
def f47oml_semi_operating_margin_level_omlog_ema_63d_curv_v130_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive log operating margin changes
def f47oml_semi_operating_margin_level_omlog_hit_63d_curv_v131_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive log operating margin changes
def f47oml_semi_operating_margin_level_omlog_hit_63d_curv_v132_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive log operating margin changes
def f47oml_semi_operating_margin_level_omlog_hit_63d_curv_v133_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive log operating margin changes
def f47oml_semi_operating_margin_level_omlog_hit_63d_curv_v134_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive log operating margin changes
def f47oml_semi_operating_margin_level_omlog_hit_63d_curv_v135_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of log operating margin
def f47oml_semi_operating_margin_level_omlog_cumsign_63d_curv_v136_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of log operating margin
def f47oml_semi_operating_margin_level_omlog_cumsign_63d_curv_v137_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of log operating margin
def f47oml_semi_operating_margin_level_omlog_cumsign_63d_curv_v138_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of log operating margin
def f47oml_semi_operating_margin_level_omlog_cumsign_63d_curv_v139_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of log operating margin
def f47oml_semi_operating_margin_level_omlog_cumsign_63d_curv_v140_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_robustz_63d_curv_v141_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_robustz_63d_curv_v142_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_robustz_63d_curv_v143_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_robustz_63d_curv_v144_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of log operating margin
def f47oml_semi_operating_margin_level_omlog_robustz_63d_curv_v145_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of log operating margin
def f47oml_semi_operating_margin_level_omlog_skew_63d_curv_v146_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of log operating margin
def f47oml_semi_operating_margin_level_omlog_skew_63d_curv_v147_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of log operating margin
def f47oml_semi_operating_margin_level_omlog_skew_63d_curv_v148_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of log operating margin
def f47oml_semi_operating_margin_level_omlog_skew_63d_curv_v149_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of log operating margin
def f47oml_semi_operating_margin_level_omlog_skew_63d_curv_v150_signal(opinc, revenue, closeadj):
    m = _f47_om_log(opinc, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
