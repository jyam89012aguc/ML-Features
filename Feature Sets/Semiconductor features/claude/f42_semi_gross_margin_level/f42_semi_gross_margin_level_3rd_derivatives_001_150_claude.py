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
def _f42_gm(gp, rev):
    return gp / rev.replace(0, np.nan)


def _f42_gm_log(gp, rev):
    return np.log(gp.replace(0, np.nan).abs() / rev.replace(0, np.nan).abs())


# 5d curvature of level of gross margin (gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_21d_curv_v001_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of gross margin (gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_21d_curv_v002_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of gross margin (gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_21d_curv_v003_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of gross margin (gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_21d_curv_v004_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of gross margin (gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_21d_curv_v005_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of gross margin (gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_63d_curv_v006_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of gross margin (gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_63d_curv_v007_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of gross margin (gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_63d_curv_v008_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of gross margin (gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_63d_curv_v009_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of gross margin (gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gm_level_63d_curv_v010_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_21d_curv_v011_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_21d_curv_v012_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_21d_curv_v013_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_21d_curv_v014_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_21d_curv_v015_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_63d_curv_v016_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_63d_curv_v017_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_63d_curv_v018_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_63d_curv_v019_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_63d_curv_v020_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_126d_curv_v021_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_126d_curv_v022_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_126d_curv_v023_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_126d_curv_v024_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_z_126d_curv_v025_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_rng_63d_curv_v026_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_rng_63d_curv_v027_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_rng_63d_curv_v028_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_rng_63d_curv_v029_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_rng_63d_curv_v030_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of gross margin (gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gm_pos_63d_curv_v031_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of gross margin (gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gm_pos_63d_curv_v032_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of gross margin (gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gm_pos_63d_curv_v033_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of gross margin (gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gm_pos_63d_curv_v034_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of gross margin (gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gm_pos_63d_curv_v035_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of gross margin (gp/rev) from peak
def f42gml_semi_gross_margin_level_gm_dd_63d_curv_v036_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of gross margin (gp/rev) from peak
def f42gml_semi_gross_margin_level_gm_dd_63d_curv_v037_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of gross margin (gp/rev) from peak
def f42gml_semi_gross_margin_level_gm_dd_63d_curv_v038_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of gross margin (gp/rev) from peak
def f42gml_semi_gross_margin_level_gm_dd_63d_curv_v039_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of gross margin (gp/rev) from peak
def f42gml_semi_gross_margin_level_gm_dd_63d_curv_v040_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of gross margin (gp/rev) above trough
def f42gml_semi_gross_margin_level_gm_up_63d_curv_v041_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of gross margin (gp/rev) above trough
def f42gml_semi_gross_margin_level_gm_up_63d_curv_v042_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of gross margin (gp/rev) above trough
def f42gml_semi_gross_margin_level_gm_up_63d_curv_v043_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of gross margin (gp/rev) above trough
def f42gml_semi_gross_margin_level_gm_up_63d_curv_v044_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of gross margin (gp/rev) above trough
def f42gml_semi_gross_margin_level_gm_up_63d_curv_v045_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_std_63d_curv_v046_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_std_63d_curv_v047_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_std_63d_curv_v048_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_std_63d_curv_v049_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_std_63d_curv_v050_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_ema_63d_curv_v051_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_ema_63d_curv_v052_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_ema_63d_curv_v053_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_ema_63d_curv_v054_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_ema_63d_curv_v055_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive gross margin (gp/rev) changes
def f42gml_semi_gross_margin_level_gm_hit_63d_curv_v056_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive gross margin (gp/rev) changes
def f42gml_semi_gross_margin_level_gm_hit_63d_curv_v057_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive gross margin (gp/rev) changes
def f42gml_semi_gross_margin_level_gm_hit_63d_curv_v058_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive gross margin (gp/rev) changes
def f42gml_semi_gross_margin_level_gm_hit_63d_curv_v059_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive gross margin (gp/rev) changes
def f42gml_semi_gross_margin_level_gm_hit_63d_curv_v060_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_cumsign_63d_curv_v061_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_cumsign_63d_curv_v062_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_cumsign_63d_curv_v063_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_cumsign_63d_curv_v064_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_cumsign_63d_curv_v065_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_robustz_63d_curv_v066_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_robustz_63d_curv_v067_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_robustz_63d_curv_v068_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_robustz_63d_curv_v069_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_robustz_63d_curv_v070_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_skew_63d_curv_v071_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_skew_63d_curv_v072_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_skew_63d_curv_v073_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_skew_63d_curv_v074_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of gross margin (gp/rev)
def f42gml_semi_gross_margin_level_gm_skew_63d_curv_v075_signal(gp, revenue, closeadj):
    m = _f42_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log gross margin (log gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_21d_curv_v076_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log gross margin (log gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_21d_curv_v077_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log gross margin (log gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_21d_curv_v078_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log gross margin (log gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_21d_curv_v079_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log gross margin (log gp/rev) (21d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_21d_curv_v080_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log gross margin (log gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_63d_curv_v081_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log gross margin (log gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_63d_curv_v082_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log gross margin (log gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_63d_curv_v083_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log gross margin (log gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_63d_curv_v084_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log gross margin (log gp/rev) (63d mean-centered)
def f42gml_semi_gross_margin_level_gmlog_level_63d_curv_v085_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_21d_curv_v086_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_21d_curv_v087_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_21d_curv_v088_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_21d_curv_v089_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_21d_curv_v090_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_63d_curv_v091_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_63d_curv_v092_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_63d_curv_v093_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_63d_curv_v094_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_63d_curv_v095_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_126d_curv_v096_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_126d_curv_v097_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_126d_curv_v098_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_126d_curv_v099_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_z_126d_curv_v100_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_rng_63d_curv_v101_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_rng_63d_curv_v102_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_rng_63d_curv_v103_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_rng_63d_curv_v104_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_rng_63d_curv_v105_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of log gross margin (log gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gmlog_pos_63d_curv_v106_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of log gross margin (log gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gmlog_pos_63d_curv_v107_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of log gross margin (log gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gmlog_pos_63d_curv_v108_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of log gross margin (log gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gmlog_pos_63d_curv_v109_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of log gross margin (log gp/rev) in rolling range
def f42gml_semi_gross_margin_level_gmlog_pos_63d_curv_v110_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of log gross margin (log gp/rev) from peak
def f42gml_semi_gross_margin_level_gmlog_dd_63d_curv_v111_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of log gross margin (log gp/rev) from peak
def f42gml_semi_gross_margin_level_gmlog_dd_63d_curv_v112_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of log gross margin (log gp/rev) from peak
def f42gml_semi_gross_margin_level_gmlog_dd_63d_curv_v113_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of log gross margin (log gp/rev) from peak
def f42gml_semi_gross_margin_level_gmlog_dd_63d_curv_v114_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of log gross margin (log gp/rev) from peak
def f42gml_semi_gross_margin_level_gmlog_dd_63d_curv_v115_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of log gross margin (log gp/rev) above trough
def f42gml_semi_gross_margin_level_gmlog_up_63d_curv_v116_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of log gross margin (log gp/rev) above trough
def f42gml_semi_gross_margin_level_gmlog_up_63d_curv_v117_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of log gross margin (log gp/rev) above trough
def f42gml_semi_gross_margin_level_gmlog_up_63d_curv_v118_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of log gross margin (log gp/rev) above trough
def f42gml_semi_gross_margin_level_gmlog_up_63d_curv_v119_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of log gross margin (log gp/rev) above trough
def f42gml_semi_gross_margin_level_gmlog_up_63d_curv_v120_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_std_63d_curv_v121_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_std_63d_curv_v122_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_std_63d_curv_v123_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_std_63d_curv_v124_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_std_63d_curv_v125_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_ema_63d_curv_v126_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_ema_63d_curv_v127_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_ema_63d_curv_v128_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_ema_63d_curv_v129_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_ema_63d_curv_v130_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive log gross margin (log gp/rev) changes
def f42gml_semi_gross_margin_level_gmlog_hit_63d_curv_v131_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive log gross margin (log gp/rev) changes
def f42gml_semi_gross_margin_level_gmlog_hit_63d_curv_v132_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive log gross margin (log gp/rev) changes
def f42gml_semi_gross_margin_level_gmlog_hit_63d_curv_v133_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive log gross margin (log gp/rev) changes
def f42gml_semi_gross_margin_level_gmlog_hit_63d_curv_v134_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive log gross margin (log gp/rev) changes
def f42gml_semi_gross_margin_level_gmlog_hit_63d_curv_v135_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_cumsign_63d_curv_v136_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_cumsign_63d_curv_v137_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_cumsign_63d_curv_v138_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_cumsign_63d_curv_v139_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_cumsign_63d_curv_v140_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_robustz_63d_curv_v141_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_robustz_63d_curv_v142_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_robustz_63d_curv_v143_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_robustz_63d_curv_v144_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_robustz_63d_curv_v145_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_skew_63d_curv_v146_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_skew_63d_curv_v147_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_skew_63d_curv_v148_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_skew_63d_curv_v149_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of log gross margin (log gp/rev)
def f42gml_semi_gross_margin_level_gmlog_skew_63d_curv_v150_signal(gp, revenue, closeadj):
    m = _f42_gm_log(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
