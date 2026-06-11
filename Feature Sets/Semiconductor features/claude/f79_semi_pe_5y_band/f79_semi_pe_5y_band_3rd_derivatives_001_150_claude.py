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
def _f79_pe(pe):
    return pe


# 5d curv of 21d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_21d_curv_v001_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_21d_curv_v002_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_21d_curv_v003_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_21d_curv_v004_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_21d_curv_v005_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_63d_curv_v006_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_63d_curv_v007_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_63d_curv_v008_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_63d_curv_v009_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_63d_curv_v010_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_126d_curv_v011_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_126d_curv_v012_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_126d_curv_v013_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_126d_curv_v014_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_126d_curv_v015_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_252d_curv_v016_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_252d_curv_v017_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_252d_curv_v018_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_252d_curv_v019_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_252d_curv_v020_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_504d_curv_v021_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_504d_curv_v022_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_504d_curv_v023_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_504d_curv_v024_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d peb level
def f79pe_f79_semi_pe_5y_band_peb_level_504d_curv_v025_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_21d_curv_v026_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_21d_curv_v027_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_21d_curv_v028_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_21d_curv_v029_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_21d_curv_v030_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_63d_curv_v031_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_63d_curv_v032_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_63d_curv_v033_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_63d_curv_v034_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_63d_curv_v035_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_126d_curv_v036_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_126d_curv_v037_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_126d_curv_v038_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_126d_curv_v039_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_126d_curv_v040_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_252d_curv_v041_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_252d_curv_v042_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_252d_curv_v043_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_252d_curv_v044_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_252d_curv_v045_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_504d_curv_v046_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_504d_curv_v047_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_504d_curv_v048_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_504d_curv_v049_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d peb z
def f79pe_f79_semi_pe_5y_band_peb_z_504d_curv_v050_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_21d_curv_v051_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_21d_curv_v052_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_21d_curv_v053_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_21d_curv_v054_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_21d_curv_v055_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_63d_curv_v056_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_63d_curv_v057_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_63d_curv_v058_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_63d_curv_v059_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_63d_curv_v060_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_126d_curv_v061_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_126d_curv_v062_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_126d_curv_v063_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_126d_curv_v064_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_126d_curv_v065_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_252d_curv_v066_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_252d_curv_v067_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_252d_curv_v068_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_252d_curv_v069_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_252d_curv_v070_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_504d_curv_v071_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_504d_curv_v072_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_504d_curv_v073_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_504d_curv_v074_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d peb max
def f79pe_f79_semi_pe_5y_band_peb_max_504d_curv_v075_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_21d_curv_v076_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_21d_curv_v077_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_21d_curv_v078_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_21d_curv_v079_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_21d_curv_v080_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_63d_curv_v081_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_63d_curv_v082_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_63d_curv_v083_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_63d_curv_v084_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_63d_curv_v085_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_126d_curv_v086_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_126d_curv_v087_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_126d_curv_v088_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_126d_curv_v089_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_126d_curv_v090_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_252d_curv_v091_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_252d_curv_v092_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_252d_curv_v093_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_252d_curv_v094_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_252d_curv_v095_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_504d_curv_v096_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_504d_curv_v097_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_504d_curv_v098_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_504d_curv_v099_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d peb min
def f79pe_f79_semi_pe_5y_band_peb_min_504d_curv_v100_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_21d_curv_v101_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_21d_curv_v102_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_21d_curv_v103_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_21d_curv_v104_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_21d_curv_v105_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_63d_curv_v106_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_63d_curv_v107_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_63d_curv_v108_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_63d_curv_v109_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_63d_curv_v110_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_126d_curv_v111_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_126d_curv_v112_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_126d_curv_v113_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_126d_curv_v114_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_126d_curv_v115_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_252d_curv_v116_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_252d_curv_v117_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_252d_curv_v118_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_252d_curv_v119_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_252d_curv_v120_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_504d_curv_v121_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_504d_curv_v122_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_504d_curv_v123_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_504d_curv_v124_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d peb rng
def f79pe_f79_semi_pe_5y_band_peb_rng_504d_curv_v125_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_21d_curv_v126_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_21d_curv_v127_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_21d_curv_v128_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_21d_curv_v129_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_21d_curv_v130_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_63d_curv_v131_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_63d_curv_v132_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_63d_curv_v133_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_63d_curv_v134_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_63d_curv_v135_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_126d_curv_v136_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_126d_curv_v137_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_126d_curv_v138_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_126d_curv_v139_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_126d_curv_v140_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_252d_curv_v141_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_252d_curv_v142_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_252d_curv_v143_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_252d_curv_v144_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_252d_curv_v145_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_504d_curv_v146_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_504d_curv_v147_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_504d_curv_v148_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_504d_curv_v149_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d peb dd
def f79pe_f79_semi_pe_5y_band_peb_dd_504d_curv_v150_signal(pe, closeadj):
    r = _f79_pe(pe)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
