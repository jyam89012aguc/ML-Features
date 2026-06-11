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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f86_evc(ev, capex):
    return ev / capex.abs().replace(0, np.nan)


# 5d slope of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_slope_v001_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_slope_v002_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_slope_v003_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_slope_v004_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_slope_v005_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_slope_v006_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_slope_v007_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_slope_v008_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_slope_v009_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_slope_v010_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_slope_v011_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_slope_v012_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_slope_v013_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_slope_v014_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_slope_v015_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_slope_v016_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_slope_v017_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_slope_v018_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_slope_v019_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_slope_v020_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_slope_v021_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_slope_v022_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_slope_v023_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_slope_v024_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_slope_v025_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_slope_v026_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_slope_v027_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_slope_v028_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_slope_v029_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_slope_v030_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_slope_v031_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_slope_v032_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_slope_v033_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_slope_v034_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_slope_v035_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_slope_v036_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_slope_v037_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_slope_v038_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_slope_v039_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_slope_v040_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_slope_v041_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_slope_v042_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_slope_v043_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_slope_v044_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_slope_v045_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_slope_v046_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_slope_v047_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_slope_v048_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_slope_v049_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_slope_v050_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_slope_v051_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_slope_v052_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_slope_v053_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_slope_v054_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_slope_v055_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_slope_v056_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_slope_v057_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_slope_v058_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_slope_v059_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_slope_v060_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_slope_v061_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_slope_v062_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_slope_v063_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_slope_v064_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_slope_v065_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_slope_v066_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_slope_v067_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_slope_v068_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_slope_v069_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_slope_v070_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_slope_v071_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_slope_v072_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_slope_v073_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_slope_v074_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_slope_v075_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_slope_v076_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_slope_v077_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_slope_v078_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_slope_v079_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_slope_v080_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_slope_v081_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_slope_v082_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_slope_v083_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_slope_v084_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_slope_v085_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_slope_v086_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_slope_v087_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_slope_v088_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_slope_v089_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_slope_v090_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_slope_v091_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_slope_v092_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_slope_v093_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_slope_v094_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_slope_v095_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_slope_v096_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_slope_v097_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_slope_v098_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_slope_v099_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_slope_v100_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_slope_v101_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_slope_v102_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_slope_v103_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_slope_v104_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_slope_v105_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_slope_v106_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_slope_v107_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_slope_v108_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_slope_v109_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_slope_v110_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_slope_v111_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_slope_v112_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_slope_v113_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_slope_v114_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_slope_v115_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_slope_v116_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_slope_v117_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_slope_v118_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_slope_v119_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_slope_v120_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_slope_v121_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_slope_v122_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_slope_v123_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_slope_v124_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_slope_v125_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_slope_v126_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_slope_v127_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_slope_v128_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_slope_v129_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_slope_v130_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_slope_v131_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_slope_v132_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_slope_v133_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_slope_v134_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_slope_v135_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_slope_v136_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_slope_v137_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_slope_v138_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_slope_v139_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_slope_v140_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_slope_v141_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_slope_v142_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_slope_v143_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_slope_v144_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_slope_v145_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_slope_v146_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_slope_v147_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_slope_v148_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_slope_v149_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_slope_v150_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
