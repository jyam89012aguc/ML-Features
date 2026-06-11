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
def _f72_debt_yoy(debt):
    return debt.pct_change(periods=252)


# 5d curv of 21d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_21d_curv_v001_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_21d_curv_v002_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_21d_curv_v003_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_21d_curv_v004_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_21d_curv_v005_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_63d_curv_v006_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_63d_curv_v007_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_63d_curv_v008_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_63d_curv_v009_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_63d_curv_v010_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_126d_curv_v011_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_126d_curv_v012_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_126d_curv_v013_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_126d_curv_v014_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_126d_curv_v015_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_252d_curv_v016_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_252d_curv_v017_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_252d_curv_v018_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_252d_curv_v019_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_252d_curv_v020_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_504d_curv_v021_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_504d_curv_v022_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_504d_curv_v023_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_504d_curv_v024_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dyoy level
def f72dt_f72_semi_debt_trajectory_dyoy_level_504d_curv_v025_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_21d_curv_v026_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_21d_curv_v027_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_21d_curv_v028_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_21d_curv_v029_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_21d_curv_v030_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_63d_curv_v031_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_63d_curv_v032_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_63d_curv_v033_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_63d_curv_v034_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_63d_curv_v035_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_126d_curv_v036_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_126d_curv_v037_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_126d_curv_v038_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_126d_curv_v039_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_126d_curv_v040_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_252d_curv_v041_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_252d_curv_v042_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_252d_curv_v043_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_252d_curv_v044_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_252d_curv_v045_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_504d_curv_v046_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_504d_curv_v047_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_504d_curv_v048_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_504d_curv_v049_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dyoy z
def f72dt_f72_semi_debt_trajectory_dyoy_z_504d_curv_v050_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_21d_curv_v051_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_21d_curv_v052_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_21d_curv_v053_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_21d_curv_v054_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_21d_curv_v055_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_63d_curv_v056_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_63d_curv_v057_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_63d_curv_v058_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_63d_curv_v059_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_63d_curv_v060_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_126d_curv_v061_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_126d_curv_v062_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_126d_curv_v063_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_126d_curv_v064_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_126d_curv_v065_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_252d_curv_v066_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_252d_curv_v067_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_252d_curv_v068_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_252d_curv_v069_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_252d_curv_v070_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_504d_curv_v071_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_504d_curv_v072_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_504d_curv_v073_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_504d_curv_v074_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dyoy max
def f72dt_f72_semi_debt_trajectory_dyoy_max_504d_curv_v075_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_21d_curv_v076_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_21d_curv_v077_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_21d_curv_v078_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_21d_curv_v079_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_21d_curv_v080_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_63d_curv_v081_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_63d_curv_v082_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_63d_curv_v083_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_63d_curv_v084_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_63d_curv_v085_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_126d_curv_v086_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_126d_curv_v087_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_126d_curv_v088_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_126d_curv_v089_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_126d_curv_v090_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_252d_curv_v091_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_252d_curv_v092_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_252d_curv_v093_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_252d_curv_v094_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_252d_curv_v095_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_504d_curv_v096_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_504d_curv_v097_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_504d_curv_v098_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_504d_curv_v099_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dyoy min
def f72dt_f72_semi_debt_trajectory_dyoy_min_504d_curv_v100_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_21d_curv_v101_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_21d_curv_v102_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_21d_curv_v103_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_21d_curv_v104_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_21d_curv_v105_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_63d_curv_v106_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_63d_curv_v107_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_63d_curv_v108_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_63d_curv_v109_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_63d_curv_v110_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_126d_curv_v111_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_126d_curv_v112_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_126d_curv_v113_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_126d_curv_v114_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_126d_curv_v115_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_252d_curv_v116_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_252d_curv_v117_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_252d_curv_v118_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_252d_curv_v119_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_252d_curv_v120_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_504d_curv_v121_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_504d_curv_v122_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_504d_curv_v123_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_504d_curv_v124_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dyoy rng
def f72dt_f72_semi_debt_trajectory_dyoy_rng_504d_curv_v125_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_21d_curv_v126_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_21d_curv_v127_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_21d_curv_v128_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_21d_curv_v129_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_21d_curv_v130_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_63d_curv_v131_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_63d_curv_v132_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_63d_curv_v133_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_63d_curv_v134_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_63d_curv_v135_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_126d_curv_v136_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_126d_curv_v137_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_126d_curv_v138_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_126d_curv_v139_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_126d_curv_v140_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_252d_curv_v141_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_252d_curv_v142_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_252d_curv_v143_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_252d_curv_v144_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_252d_curv_v145_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_504d_curv_v146_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_504d_curv_v147_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_504d_curv_v148_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_504d_curv_v149_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dyoy dd
def f72dt_f72_semi_debt_trajectory_dyoy_dd_504d_curv_v150_signal(debt, closeadj):
    r = _f72_debt_yoy(debt)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
