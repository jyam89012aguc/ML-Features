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
def _f86_evc(ev, capex):
    return ev / capex.abs().replace(0, np.nan)


# 5d curv of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_curv_v001_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_curv_v002_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_curv_v003_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_curv_v004_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_21d_curv_v005_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_curv_v006_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_curv_v007_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_curv_v008_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_curv_v009_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_63d_curv_v010_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_curv_v011_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_curv_v012_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_curv_v013_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_curv_v014_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_126d_curv_v015_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_curv_v016_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_curv_v017_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_curv_v018_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_curv_v019_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_252d_curv_v020_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_curv_v021_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_curv_v022_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_curv_v023_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_curv_v024_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d evc level
def f86evc_f86_semi_ev_to_capex_evc_level_504d_curv_v025_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_curv_v026_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_curv_v027_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_curv_v028_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_curv_v029_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_21d_curv_v030_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_curv_v031_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_curv_v032_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_curv_v033_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_curv_v034_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_63d_curv_v035_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_curv_v036_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_curv_v037_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_curv_v038_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_curv_v039_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_126d_curv_v040_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_curv_v041_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_curv_v042_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_curv_v043_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_curv_v044_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_252d_curv_v045_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_curv_v046_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_curv_v047_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_curv_v048_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_curv_v049_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d evc z
def f86evc_f86_semi_ev_to_capex_evc_z_504d_curv_v050_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_curv_v051_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_curv_v052_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_curv_v053_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_curv_v054_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_21d_curv_v055_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_curv_v056_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_curv_v057_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_curv_v058_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_curv_v059_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_63d_curv_v060_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_curv_v061_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_curv_v062_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_curv_v063_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_curv_v064_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_126d_curv_v065_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_curv_v066_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_curv_v067_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_curv_v068_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_curv_v069_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_252d_curv_v070_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_curv_v071_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_curv_v072_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_curv_v073_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_curv_v074_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d evc max
def f86evc_f86_semi_ev_to_capex_evc_max_504d_curv_v075_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_curv_v076_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_curv_v077_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_curv_v078_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_curv_v079_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_21d_curv_v080_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_curv_v081_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_curv_v082_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_curv_v083_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_curv_v084_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_63d_curv_v085_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_curv_v086_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_curv_v087_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_curv_v088_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_curv_v089_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_126d_curv_v090_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_curv_v091_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_curv_v092_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_curv_v093_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_curv_v094_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_252d_curv_v095_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_curv_v096_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_curv_v097_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_curv_v098_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_curv_v099_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d evc min
def f86evc_f86_semi_ev_to_capex_evc_min_504d_curv_v100_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_curv_v101_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_curv_v102_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_curv_v103_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_curv_v104_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_21d_curv_v105_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_curv_v106_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_curv_v107_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_curv_v108_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_curv_v109_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_63d_curv_v110_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_curv_v111_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_curv_v112_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_curv_v113_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_curv_v114_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_126d_curv_v115_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_curv_v116_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_curv_v117_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_curv_v118_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_curv_v119_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_252d_curv_v120_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_curv_v121_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_curv_v122_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_curv_v123_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_curv_v124_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d evc rng
def f86evc_f86_semi_ev_to_capex_evc_rng_504d_curv_v125_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_curv_v126_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_curv_v127_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_curv_v128_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_curv_v129_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_21d_curv_v130_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_curv_v131_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_curv_v132_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_curv_v133_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_curv_v134_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_63d_curv_v135_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_curv_v136_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_curv_v137_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_curv_v138_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_curv_v139_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_126d_curv_v140_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_curv_v141_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_curv_v142_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_curv_v143_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_curv_v144_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_252d_curv_v145_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_curv_v146_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_curv_v147_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_curv_v148_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_curv_v149_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d evc dd
def f86evc_f86_semi_ev_to_capex_evc_dd_504d_curv_v150_signal(ev, capex, closeadj):
    r = _f86_evc(ev, capex)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
