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
def _f44_gm(gp, rev):
    return gp / rev.replace(0, np.nan)


def _f44_gm_chg(gp, rev):
    g = gp / rev.replace(0, np.nan)
    return g.diff()


# 5d slope of level of gross margin (vol metric) (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_21d_slope_v001_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of gross margin (vol metric) (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_21d_slope_v002_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of gross margin (vol metric) (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_21d_slope_v003_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of gross margin (vol metric) (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_21d_slope_v004_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of gross margin (vol metric) (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_21d_slope_v005_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of gross margin (vol metric) (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_63d_slope_v006_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of gross margin (vol metric) (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_63d_slope_v007_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of gross margin (vol metric) (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_63d_slope_v008_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of gross margin (vol metric) (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_63d_slope_v009_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of gross margin (vol metric) (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmvol_level_63d_slope_v010_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_21d_slope_v011_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_21d_slope_v012_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_21d_slope_v013_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_21d_slope_v014_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_21d_slope_v015_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_63d_slope_v016_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_63d_slope_v017_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_63d_slope_v018_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_63d_slope_v019_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_63d_slope_v020_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_126d_slope_v021_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_126d_slope_v022_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_126d_slope_v023_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_126d_slope_v024_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_z_126d_slope_v025_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_rng_63d_slope_v026_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_rng_63d_slope_v027_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_rng_63d_slope_v028_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_rng_63d_slope_v029_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_rng_63d_slope_v030_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d position of gross margin (vol metric) in rolling range
def f44gmv_semi_gross_margin_volatility_gmvol_pos_63d_slope_v031_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position of gross margin (vol metric) in rolling range
def f44gmv_semi_gross_margin_volatility_gmvol_pos_63d_slope_v032_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d position of gross margin (vol metric) in rolling range
def f44gmv_semi_gross_margin_volatility_gmvol_pos_63d_slope_v033_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d position of gross margin (vol metric) in rolling range
def f44gmv_semi_gross_margin_volatility_gmvol_pos_63d_slope_v034_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d position of gross margin (vol metric) in rolling range
def f44gmv_semi_gross_margin_volatility_gmvol_pos_63d_slope_v035_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown of gross margin (vol metric) from peak
def f44gmv_semi_gross_margin_volatility_gmvol_dd_63d_slope_v036_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown of gross margin (vol metric) from peak
def f44gmv_semi_gross_margin_volatility_gmvol_dd_63d_slope_v037_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown of gross margin (vol metric) from peak
def f44gmv_semi_gross_margin_volatility_gmvol_dd_63d_slope_v038_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown of gross margin (vol metric) from peak
def f44gmv_semi_gross_margin_volatility_gmvol_dd_63d_slope_v039_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown of gross margin (vol metric) from peak
def f44gmv_semi_gross_margin_volatility_gmvol_dd_63d_slope_v040_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d run-up of gross margin (vol metric) above trough
def f44gmv_semi_gross_margin_volatility_gmvol_up_63d_slope_v041_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up of gross margin (vol metric) above trough
def f44gmv_semi_gross_margin_volatility_gmvol_up_63d_slope_v042_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d run-up of gross margin (vol metric) above trough
def f44gmv_semi_gross_margin_volatility_gmvol_up_63d_slope_v043_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d run-up of gross margin (vol metric) above trough
def f44gmv_semi_gross_margin_volatility_gmvol_up_63d_slope_v044_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d run-up of gross margin (vol metric) above trough
def f44gmv_semi_gross_margin_volatility_gmvol_up_63d_slope_v045_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_std_63d_slope_v046_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_std_63d_slope_v047_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_std_63d_slope_v048_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_std_63d_slope_v049_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_std_63d_slope_v050_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d EMA-crossover of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_ema_63d_slope_v051_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EMA-crossover of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_ema_63d_slope_v052_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d EMA-crossover of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_ema_63d_slope_v053_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d EMA-crossover of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_ema_63d_slope_v054_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d EMA-crossover of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_ema_63d_slope_v055_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-ratio of positive gross margin (vol metric) changes
def f44gmv_semi_gross_margin_volatility_gmvol_hit_63d_slope_v056_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-ratio of positive gross margin (vol metric) changes
def f44gmv_semi_gross_margin_volatility_gmvol_hit_63d_slope_v057_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-ratio of positive gross margin (vol metric) changes
def f44gmv_semi_gross_margin_volatility_gmvol_hit_63d_slope_v058_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-ratio of positive gross margin (vol metric) changes
def f44gmv_semi_gross_margin_volatility_gmvol_hit_63d_slope_v059_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-ratio of positive gross margin (vol metric) changes
def f44gmv_semi_gross_margin_volatility_gmvol_hit_63d_slope_v060_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d signed cumulative changes of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_cumsign_63d_slope_v061_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed cumulative changes of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_cumsign_63d_slope_v062_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d signed cumulative changes of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_cumsign_63d_slope_v063_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d signed cumulative changes of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_cumsign_63d_slope_v064_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d signed cumulative changes of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_cumsign_63d_slope_v065_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robust z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_robustz_63d_slope_v066_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_robustz_63d_slope_v067_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robust z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_robustz_63d_slope_v068_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robust z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_robustz_63d_slope_v069_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d robust z-score of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_robustz_63d_slope_v070_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_skew_63d_slope_v071_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_skew_63d_slope_v072_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_skew_63d_slope_v073_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_skew_63d_slope_v074_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew of gross margin (vol metric)
def f44gmv_semi_gross_margin_volatility_gmvol_skew_63d_slope_v075_signal(gp, revenue, closeadj):
    m = _f44_gm(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of gross margin daily change (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_21d_slope_v076_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of gross margin daily change (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_21d_slope_v077_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of gross margin daily change (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_21d_slope_v078_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of gross margin daily change (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_21d_slope_v079_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of gross margin daily change (21d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_21d_slope_v080_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level of gross margin daily change (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_63d_slope_v081_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of level of gross margin daily change (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_63d_slope_v082_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level of gross margin daily change (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_63d_slope_v083_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level of gross margin daily change (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_63d_slope_v084_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of level of gross margin daily change (63d mean-centered)
def f44gmv_semi_gross_margin_volatility_gmchg_level_63d_slope_v085_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_21d_slope_v086_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_21d_slope_v087_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_21d_slope_v088_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_21d_slope_v089_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_21d_slope_v090_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_63d_slope_v091_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_63d_slope_v092_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_63d_slope_v093_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_63d_slope_v094_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_63d_slope_v095_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_126d_slope_v096_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_126d_slope_v097_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_126d_slope_v098_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_126d_slope_v099_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_z_126d_slope_v100_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_rng_63d_slope_v101_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_rng_63d_slope_v102_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_rng_63d_slope_v103_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_rng_63d_slope_v104_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_rng_63d_slope_v105_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d position of gross margin daily change in rolling range
def f44gmv_semi_gross_margin_volatility_gmchg_pos_63d_slope_v106_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position of gross margin daily change in rolling range
def f44gmv_semi_gross_margin_volatility_gmchg_pos_63d_slope_v107_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d position of gross margin daily change in rolling range
def f44gmv_semi_gross_margin_volatility_gmchg_pos_63d_slope_v108_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d position of gross margin daily change in rolling range
def f44gmv_semi_gross_margin_volatility_gmchg_pos_63d_slope_v109_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d position of gross margin daily change in rolling range
def f44gmv_semi_gross_margin_volatility_gmchg_pos_63d_slope_v110_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown of gross margin daily change from peak
def f44gmv_semi_gross_margin_volatility_gmchg_dd_63d_slope_v111_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown of gross margin daily change from peak
def f44gmv_semi_gross_margin_volatility_gmchg_dd_63d_slope_v112_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown of gross margin daily change from peak
def f44gmv_semi_gross_margin_volatility_gmchg_dd_63d_slope_v113_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown of gross margin daily change from peak
def f44gmv_semi_gross_margin_volatility_gmchg_dd_63d_slope_v114_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown of gross margin daily change from peak
def f44gmv_semi_gross_margin_volatility_gmchg_dd_63d_slope_v115_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d run-up of gross margin daily change above trough
def f44gmv_semi_gross_margin_volatility_gmchg_up_63d_slope_v116_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up of gross margin daily change above trough
def f44gmv_semi_gross_margin_volatility_gmchg_up_63d_slope_v117_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d run-up of gross margin daily change above trough
def f44gmv_semi_gross_margin_volatility_gmchg_up_63d_slope_v118_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d run-up of gross margin daily change above trough
def f44gmv_semi_gross_margin_volatility_gmchg_up_63d_slope_v119_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d run-up of gross margin daily change above trough
def f44gmv_semi_gross_margin_volatility_gmchg_up_63d_slope_v120_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_std_63d_slope_v121_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_std_63d_slope_v122_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_std_63d_slope_v123_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_std_63d_slope_v124_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_std_63d_slope_v125_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d EMA-crossover of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_ema_63d_slope_v126_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EMA-crossover of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_ema_63d_slope_v127_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d EMA-crossover of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_ema_63d_slope_v128_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d EMA-crossover of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_ema_63d_slope_v129_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d EMA-crossover of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_ema_63d_slope_v130_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d hit-ratio of positive gross margin daily change changes
def f44gmv_semi_gross_margin_volatility_gmchg_hit_63d_slope_v131_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit-ratio of positive gross margin daily change changes
def f44gmv_semi_gross_margin_volatility_gmchg_hit_63d_slope_v132_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d hit-ratio of positive gross margin daily change changes
def f44gmv_semi_gross_margin_volatility_gmchg_hit_63d_slope_v133_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d hit-ratio of positive gross margin daily change changes
def f44gmv_semi_gross_margin_volatility_gmchg_hit_63d_slope_v134_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d hit-ratio of positive gross margin daily change changes
def f44gmv_semi_gross_margin_volatility_gmchg_hit_63d_slope_v135_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d signed cumulative changes of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_cumsign_63d_slope_v136_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed cumulative changes of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_cumsign_63d_slope_v137_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d signed cumulative changes of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_cumsign_63d_slope_v138_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d signed cumulative changes of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_cumsign_63d_slope_v139_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d signed cumulative changes of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_cumsign_63d_slope_v140_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robust z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_robustz_63d_slope_v141_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_robustz_63d_slope_v142_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robust z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_robustz_63d_slope_v143_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robust z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_robustz_63d_slope_v144_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d robust z-score of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_robustz_63d_slope_v145_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_skew_63d_slope_v146_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_skew_63d_slope_v147_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_skew_63d_slope_v148_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_skew_63d_slope_v149_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew of gross margin daily change
def f44gmv_semi_gross_margin_volatility_gmchg_skew_63d_slope_v150_signal(gp, revenue, closeadj):
    m = _f44_gm_chg(gp, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
