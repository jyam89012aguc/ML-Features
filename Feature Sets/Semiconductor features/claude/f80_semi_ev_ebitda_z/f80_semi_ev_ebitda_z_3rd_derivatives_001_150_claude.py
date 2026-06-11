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
def _f80_ee(evebitda):
    return evebitda


# 5d curv of 21d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_21d_curv_v001_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_21d_curv_v002_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_21d_curv_v003_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_21d_curv_v004_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_21d_curv_v005_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_63d_curv_v006_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_63d_curv_v007_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_63d_curv_v008_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_63d_curv_v009_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_63d_curv_v010_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_126d_curv_v011_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_126d_curv_v012_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_126d_curv_v013_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_126d_curv_v014_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_126d_curv_v015_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_252d_curv_v016_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_252d_curv_v017_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_252d_curv_v018_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_252d_curv_v019_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_252d_curv_v020_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_504d_curv_v021_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_504d_curv_v022_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_504d_curv_v023_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_504d_curv_v024_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d eez level
def f80ee_f80_semi_ev_ebitda_z_eez_level_504d_curv_v025_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_21d_curv_v026_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_21d_curv_v027_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_21d_curv_v028_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_21d_curv_v029_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_21d_curv_v030_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_63d_curv_v031_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_63d_curv_v032_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_63d_curv_v033_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_63d_curv_v034_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_63d_curv_v035_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_126d_curv_v036_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_126d_curv_v037_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_126d_curv_v038_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_126d_curv_v039_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_126d_curv_v040_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_252d_curv_v041_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_252d_curv_v042_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_252d_curv_v043_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_252d_curv_v044_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_252d_curv_v045_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_504d_curv_v046_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_504d_curv_v047_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_504d_curv_v048_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_504d_curv_v049_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d eez z
def f80ee_f80_semi_ev_ebitda_z_eez_z_504d_curv_v050_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_21d_curv_v051_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_21d_curv_v052_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_21d_curv_v053_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_21d_curv_v054_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_21d_curv_v055_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_63d_curv_v056_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_63d_curv_v057_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_63d_curv_v058_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_63d_curv_v059_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_63d_curv_v060_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_126d_curv_v061_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_126d_curv_v062_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_126d_curv_v063_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_126d_curv_v064_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_126d_curv_v065_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_252d_curv_v066_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_252d_curv_v067_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_252d_curv_v068_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_252d_curv_v069_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_252d_curv_v070_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_504d_curv_v071_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_504d_curv_v072_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_504d_curv_v073_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_504d_curv_v074_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d eez max
def f80ee_f80_semi_ev_ebitda_z_eez_max_504d_curv_v075_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_21d_curv_v076_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_21d_curv_v077_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_21d_curv_v078_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_21d_curv_v079_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_21d_curv_v080_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_63d_curv_v081_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_63d_curv_v082_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_63d_curv_v083_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_63d_curv_v084_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_63d_curv_v085_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_126d_curv_v086_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_126d_curv_v087_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_126d_curv_v088_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_126d_curv_v089_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_126d_curv_v090_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_252d_curv_v091_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_252d_curv_v092_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_252d_curv_v093_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_252d_curv_v094_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_252d_curv_v095_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_504d_curv_v096_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_504d_curv_v097_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_504d_curv_v098_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_504d_curv_v099_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d eez min
def f80ee_f80_semi_ev_ebitda_z_eez_min_504d_curv_v100_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_21d_curv_v101_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_21d_curv_v102_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_21d_curv_v103_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_21d_curv_v104_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_21d_curv_v105_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_63d_curv_v106_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_63d_curv_v107_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_63d_curv_v108_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_63d_curv_v109_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_63d_curv_v110_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_126d_curv_v111_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_126d_curv_v112_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_126d_curv_v113_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_126d_curv_v114_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_126d_curv_v115_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_252d_curv_v116_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_252d_curv_v117_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_252d_curv_v118_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_252d_curv_v119_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_252d_curv_v120_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_504d_curv_v121_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_504d_curv_v122_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_504d_curv_v123_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_504d_curv_v124_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d eez rng
def f80ee_f80_semi_ev_ebitda_z_eez_rng_504d_curv_v125_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_21d_curv_v126_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_21d_curv_v127_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_21d_curv_v128_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_21d_curv_v129_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_21d_curv_v130_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_63d_curv_v131_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_63d_curv_v132_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_63d_curv_v133_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_63d_curv_v134_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_63d_curv_v135_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_126d_curv_v136_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_126d_curv_v137_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_126d_curv_v138_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_126d_curv_v139_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_126d_curv_v140_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_252d_curv_v141_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_252d_curv_v142_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_252d_curv_v143_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_252d_curv_v144_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_252d_curv_v145_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_504d_curv_v146_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_504d_curv_v147_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_504d_curv_v148_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_504d_curv_v149_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d eez dd
def f80ee_f80_semi_ev_ebitda_z_eez_dd_504d_curv_v150_signal(evebitda, closeadj):
    r = _f80_ee(evebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
