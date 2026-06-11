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
def _f50_oi(ox, rev):
    return ox / rev.replace(0, np.nan)


def _f50_oi_log(ox, rev):
    return np.log(ox.replace(0, np.nan).abs() / rev.replace(0, np.nan).abs())


# 5d curvature of level of opex intensity (opex/rev) (21d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_21d_curv_v001_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of opex intensity (opex/rev) (21d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_21d_curv_v002_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of opex intensity (opex/rev) (21d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_21d_curv_v003_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of opex intensity (opex/rev) (21d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_21d_curv_v004_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of opex intensity (opex/rev) (21d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_21d_curv_v005_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of opex intensity (opex/rev) (63d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_63d_curv_v006_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of opex intensity (opex/rev) (63d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_63d_curv_v007_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of opex intensity (opex/rev) (63d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_63d_curv_v008_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of opex intensity (opex/rev) (63d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_63d_curv_v009_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of opex intensity (opex/rev) (63d mean-centered)
def f50oi_semi_opex_intensity_oxi_level_63d_curv_v010_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_21d_curv_v011_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_21d_curv_v012_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_21d_curv_v013_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_21d_curv_v014_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_21d_curv_v015_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_63d_curv_v016_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_63d_curv_v017_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_63d_curv_v018_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_63d_curv_v019_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_63d_curv_v020_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_126d_curv_v021_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_126d_curv_v022_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_126d_curv_v023_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_126d_curv_v024_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_z_126d_curv_v025_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_rng_63d_curv_v026_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_rng_63d_curv_v027_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_rng_63d_curv_v028_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_rng_63d_curv_v029_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_rng_63d_curv_v030_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of opex intensity (opex/rev) in rolling range
def f50oi_semi_opex_intensity_oxi_pos_63d_curv_v031_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of opex intensity (opex/rev) in rolling range
def f50oi_semi_opex_intensity_oxi_pos_63d_curv_v032_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of opex intensity (opex/rev) in rolling range
def f50oi_semi_opex_intensity_oxi_pos_63d_curv_v033_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of opex intensity (opex/rev) in rolling range
def f50oi_semi_opex_intensity_oxi_pos_63d_curv_v034_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of opex intensity (opex/rev) in rolling range
def f50oi_semi_opex_intensity_oxi_pos_63d_curv_v035_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of opex intensity (opex/rev) from peak
def f50oi_semi_opex_intensity_oxi_dd_63d_curv_v036_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of opex intensity (opex/rev) from peak
def f50oi_semi_opex_intensity_oxi_dd_63d_curv_v037_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of opex intensity (opex/rev) from peak
def f50oi_semi_opex_intensity_oxi_dd_63d_curv_v038_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of opex intensity (opex/rev) from peak
def f50oi_semi_opex_intensity_oxi_dd_63d_curv_v039_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of opex intensity (opex/rev) from peak
def f50oi_semi_opex_intensity_oxi_dd_63d_curv_v040_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of opex intensity (opex/rev) above trough
def f50oi_semi_opex_intensity_oxi_up_63d_curv_v041_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of opex intensity (opex/rev) above trough
def f50oi_semi_opex_intensity_oxi_up_63d_curv_v042_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of opex intensity (opex/rev) above trough
def f50oi_semi_opex_intensity_oxi_up_63d_curv_v043_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of opex intensity (opex/rev) above trough
def f50oi_semi_opex_intensity_oxi_up_63d_curv_v044_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of opex intensity (opex/rev) above trough
def f50oi_semi_opex_intensity_oxi_up_63d_curv_v045_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_std_63d_curv_v046_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_std_63d_curv_v047_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_std_63d_curv_v048_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_std_63d_curv_v049_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_std_63d_curv_v050_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_ema_63d_curv_v051_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_ema_63d_curv_v052_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_ema_63d_curv_v053_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_ema_63d_curv_v054_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_ema_63d_curv_v055_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive opex intensity (opex/rev) changes
def f50oi_semi_opex_intensity_oxi_hit_63d_curv_v056_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive opex intensity (opex/rev) changes
def f50oi_semi_opex_intensity_oxi_hit_63d_curv_v057_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive opex intensity (opex/rev) changes
def f50oi_semi_opex_intensity_oxi_hit_63d_curv_v058_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive opex intensity (opex/rev) changes
def f50oi_semi_opex_intensity_oxi_hit_63d_curv_v059_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive opex intensity (opex/rev) changes
def f50oi_semi_opex_intensity_oxi_hit_63d_curv_v060_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_cumsign_63d_curv_v061_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_cumsign_63d_curv_v062_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_cumsign_63d_curv_v063_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_cumsign_63d_curv_v064_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_cumsign_63d_curv_v065_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_robustz_63d_curv_v066_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_robustz_63d_curv_v067_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_robustz_63d_curv_v068_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_robustz_63d_curv_v069_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_robustz_63d_curv_v070_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_skew_63d_curv_v071_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_skew_63d_curv_v072_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_skew_63d_curv_v073_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_skew_63d_curv_v074_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of opex intensity (opex/rev)
def f50oi_semi_opex_intensity_oxi_skew_63d_curv_v075_signal(opex, revenue, closeadj):
    m = _f50_oi(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log opex intensity (21d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_21d_curv_v076_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log opex intensity (21d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_21d_curv_v077_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log opex intensity (21d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_21d_curv_v078_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log opex intensity (21d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_21d_curv_v079_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log opex intensity (21d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_21d_curv_v080_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log opex intensity (63d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_63d_curv_v081_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log opex intensity (63d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_63d_curv_v082_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log opex intensity (63d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_63d_curv_v083_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log opex intensity (63d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_63d_curv_v084_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log opex intensity (63d mean-centered)
def f50oi_semi_opex_intensity_oxilog_level_63d_curv_v085_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_21d_curv_v086_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_21d_curv_v087_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_21d_curv_v088_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_21d_curv_v089_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_21d_curv_v090_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_63d_curv_v091_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_63d_curv_v092_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_63d_curv_v093_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_63d_curv_v094_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_63d_curv_v095_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_126d_curv_v096_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_126d_curv_v097_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_126d_curv_v098_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_126d_curv_v099_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_z_126d_curv_v100_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of log opex intensity
def f50oi_semi_opex_intensity_oxilog_rng_63d_curv_v101_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of log opex intensity
def f50oi_semi_opex_intensity_oxilog_rng_63d_curv_v102_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of log opex intensity
def f50oi_semi_opex_intensity_oxilog_rng_63d_curv_v103_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of log opex intensity
def f50oi_semi_opex_intensity_oxilog_rng_63d_curv_v104_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of log opex intensity
def f50oi_semi_opex_intensity_oxilog_rng_63d_curv_v105_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of log opex intensity in rolling range
def f50oi_semi_opex_intensity_oxilog_pos_63d_curv_v106_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of log opex intensity in rolling range
def f50oi_semi_opex_intensity_oxilog_pos_63d_curv_v107_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of log opex intensity in rolling range
def f50oi_semi_opex_intensity_oxilog_pos_63d_curv_v108_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of log opex intensity in rolling range
def f50oi_semi_opex_intensity_oxilog_pos_63d_curv_v109_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of log opex intensity in rolling range
def f50oi_semi_opex_intensity_oxilog_pos_63d_curv_v110_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of log opex intensity from peak
def f50oi_semi_opex_intensity_oxilog_dd_63d_curv_v111_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of log opex intensity from peak
def f50oi_semi_opex_intensity_oxilog_dd_63d_curv_v112_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of log opex intensity from peak
def f50oi_semi_opex_intensity_oxilog_dd_63d_curv_v113_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of log opex intensity from peak
def f50oi_semi_opex_intensity_oxilog_dd_63d_curv_v114_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of log opex intensity from peak
def f50oi_semi_opex_intensity_oxilog_dd_63d_curv_v115_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of log opex intensity above trough
def f50oi_semi_opex_intensity_oxilog_up_63d_curv_v116_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of log opex intensity above trough
def f50oi_semi_opex_intensity_oxilog_up_63d_curv_v117_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of log opex intensity above trough
def f50oi_semi_opex_intensity_oxilog_up_63d_curv_v118_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of log opex intensity above trough
def f50oi_semi_opex_intensity_oxilog_up_63d_curv_v119_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of log opex intensity above trough
def f50oi_semi_opex_intensity_oxilog_up_63d_curv_v120_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of log opex intensity
def f50oi_semi_opex_intensity_oxilog_std_63d_curv_v121_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of log opex intensity
def f50oi_semi_opex_intensity_oxilog_std_63d_curv_v122_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of log opex intensity
def f50oi_semi_opex_intensity_oxilog_std_63d_curv_v123_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of log opex intensity
def f50oi_semi_opex_intensity_oxilog_std_63d_curv_v124_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of log opex intensity
def f50oi_semi_opex_intensity_oxilog_std_63d_curv_v125_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of log opex intensity
def f50oi_semi_opex_intensity_oxilog_ema_63d_curv_v126_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of log opex intensity
def f50oi_semi_opex_intensity_oxilog_ema_63d_curv_v127_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of log opex intensity
def f50oi_semi_opex_intensity_oxilog_ema_63d_curv_v128_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of log opex intensity
def f50oi_semi_opex_intensity_oxilog_ema_63d_curv_v129_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of log opex intensity
def f50oi_semi_opex_intensity_oxilog_ema_63d_curv_v130_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive log opex intensity changes
def f50oi_semi_opex_intensity_oxilog_hit_63d_curv_v131_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive log opex intensity changes
def f50oi_semi_opex_intensity_oxilog_hit_63d_curv_v132_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive log opex intensity changes
def f50oi_semi_opex_intensity_oxilog_hit_63d_curv_v133_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive log opex intensity changes
def f50oi_semi_opex_intensity_oxilog_hit_63d_curv_v134_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive log opex intensity changes
def f50oi_semi_opex_intensity_oxilog_hit_63d_curv_v135_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of log opex intensity
def f50oi_semi_opex_intensity_oxilog_cumsign_63d_curv_v136_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of log opex intensity
def f50oi_semi_opex_intensity_oxilog_cumsign_63d_curv_v137_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of log opex intensity
def f50oi_semi_opex_intensity_oxilog_cumsign_63d_curv_v138_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of log opex intensity
def f50oi_semi_opex_intensity_oxilog_cumsign_63d_curv_v139_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of log opex intensity
def f50oi_semi_opex_intensity_oxilog_cumsign_63d_curv_v140_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_robustz_63d_curv_v141_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_robustz_63d_curv_v142_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_robustz_63d_curv_v143_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_robustz_63d_curv_v144_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of log opex intensity
def f50oi_semi_opex_intensity_oxilog_robustz_63d_curv_v145_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of log opex intensity
def f50oi_semi_opex_intensity_oxilog_skew_63d_curv_v146_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of log opex intensity
def f50oi_semi_opex_intensity_oxilog_skew_63d_curv_v147_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of log opex intensity
def f50oi_semi_opex_intensity_oxilog_skew_63d_curv_v148_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of log opex intensity
def f50oi_semi_opex_intensity_oxilog_skew_63d_curv_v149_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of log opex intensity
def f50oi_semi_opex_intensity_oxilog_skew_63d_curv_v150_signal(opex, revenue, closeadj):
    m = _f50_oi_log(opex, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
