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
def _f82_pb(pb):
    return pb


# 5d curv of 21d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_21d_curv_v001_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_21d_curv_v002_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_21d_curv_v003_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_21d_curv_v004_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_21d_curv_v005_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_63d_curv_v006_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_63d_curv_v007_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_63d_curv_v008_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_63d_curv_v009_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_63d_curv_v010_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_126d_curv_v011_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_126d_curv_v012_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_126d_curv_v013_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_126d_curv_v014_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_126d_curv_v015_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_252d_curv_v016_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_252d_curv_v017_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_252d_curv_v018_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_252d_curv_v019_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_252d_curv_v020_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_504d_curv_v021_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_504d_curv_v022_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_504d_curv_v023_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_504d_curv_v024_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d pbr level
def f82pb_f82_semi_pb_5y_range_pbr_level_504d_curv_v025_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_21d_curv_v026_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_21d_curv_v027_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_21d_curv_v028_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_21d_curv_v029_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_21d_curv_v030_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_63d_curv_v031_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_63d_curv_v032_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_63d_curv_v033_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_63d_curv_v034_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_63d_curv_v035_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_126d_curv_v036_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_126d_curv_v037_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_126d_curv_v038_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_126d_curv_v039_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_126d_curv_v040_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_252d_curv_v041_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_252d_curv_v042_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_252d_curv_v043_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_252d_curv_v044_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_252d_curv_v045_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_504d_curv_v046_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_504d_curv_v047_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_504d_curv_v048_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_504d_curv_v049_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d pbr z
def f82pb_f82_semi_pb_5y_range_pbr_z_504d_curv_v050_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_21d_curv_v051_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_21d_curv_v052_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_21d_curv_v053_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_21d_curv_v054_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_21d_curv_v055_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_63d_curv_v056_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_63d_curv_v057_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_63d_curv_v058_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_63d_curv_v059_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_63d_curv_v060_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_126d_curv_v061_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_126d_curv_v062_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_126d_curv_v063_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_126d_curv_v064_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_126d_curv_v065_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_252d_curv_v066_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_252d_curv_v067_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_252d_curv_v068_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_252d_curv_v069_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_252d_curv_v070_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_504d_curv_v071_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_504d_curv_v072_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_504d_curv_v073_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_504d_curv_v074_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d pbr max
def f82pb_f82_semi_pb_5y_range_pbr_max_504d_curv_v075_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_21d_curv_v076_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_21d_curv_v077_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_21d_curv_v078_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_21d_curv_v079_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_21d_curv_v080_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_63d_curv_v081_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_63d_curv_v082_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_63d_curv_v083_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_63d_curv_v084_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_63d_curv_v085_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_126d_curv_v086_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_126d_curv_v087_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_126d_curv_v088_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_126d_curv_v089_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_126d_curv_v090_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_252d_curv_v091_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_252d_curv_v092_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_252d_curv_v093_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_252d_curv_v094_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_252d_curv_v095_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_504d_curv_v096_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_504d_curv_v097_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_504d_curv_v098_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_504d_curv_v099_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d pbr min
def f82pb_f82_semi_pb_5y_range_pbr_min_504d_curv_v100_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_21d_curv_v101_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_21d_curv_v102_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_21d_curv_v103_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_21d_curv_v104_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_21d_curv_v105_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_63d_curv_v106_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_63d_curv_v107_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_63d_curv_v108_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_63d_curv_v109_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_63d_curv_v110_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_126d_curv_v111_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_126d_curv_v112_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_126d_curv_v113_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_126d_curv_v114_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_126d_curv_v115_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_252d_curv_v116_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_252d_curv_v117_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_252d_curv_v118_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_252d_curv_v119_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_252d_curv_v120_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_504d_curv_v121_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_504d_curv_v122_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_504d_curv_v123_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_504d_curv_v124_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d pbr rng
def f82pb_f82_semi_pb_5y_range_pbr_rng_504d_curv_v125_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_21d_curv_v126_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_21d_curv_v127_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_21d_curv_v128_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_21d_curv_v129_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_21d_curv_v130_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_63d_curv_v131_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_63d_curv_v132_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_63d_curv_v133_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_63d_curv_v134_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_63d_curv_v135_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_126d_curv_v136_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_126d_curv_v137_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_126d_curv_v138_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_126d_curv_v139_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_126d_curv_v140_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_252d_curv_v141_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_252d_curv_v142_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_252d_curv_v143_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_252d_curv_v144_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_252d_curv_v145_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_504d_curv_v146_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_504d_curv_v147_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_504d_curv_v148_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_504d_curv_v149_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d pbr dd
def f82pb_f82_semi_pb_5y_range_pbr_dd_504d_curv_v150_signal(pb, closeadj):
    r = _f82_pb(pb)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
