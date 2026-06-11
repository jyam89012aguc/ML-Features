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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f98hbm_gm_expand(gp, rev, n=63):
    return (gp / rev.replace(0, np.nan)).diff(periods=n)


def _f98hbm_capex_spike(cx, n=63):
    return cx.pct_change(periods=n)


def _f98hbm_combo(gp, rev, cx, n=63):
    gme = (gp / rev.replace(0, np.nan)).diff(periods=n)
    cxs = cx.pct_change(periods=n)
    return gme * cxs


# 5d curv of 21d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_21d_curv_v001_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_21d_curv_v002_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_21d_curv_v003_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_21d_curv_v004_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_21d_curv_v005_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_63d_curv_v006_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_63d_curv_v007_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_63d_curv_v008_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_63d_curv_v009_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_63d_curv_v010_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_126d_curv_v011_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_126d_curv_v012_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_126d_curv_v013_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_126d_curv_v014_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_126d_curv_v015_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_252d_curv_v016_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_252d_curv_v017_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_252d_curv_v018_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_252d_curv_v019_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_252d_curv_v020_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_504d_curv_v021_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_504d_curv_v022_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_504d_curv_v023_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_504d_curv_v024_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d lvl
def f98hbm_f98_semi_hbm_advanced_packaging_signal_lvl_504d_curv_v025_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _mean(x, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_21d_curv_v026_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_21d_curv_v027_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_21d_curv_v028_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_21d_curv_v029_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_21d_curv_v030_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_63d_curv_v031_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_63d_curv_v032_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_63d_curv_v033_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_63d_curv_v034_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_63d_curv_v035_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_126d_curv_v036_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_126d_curv_v037_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_126d_curv_v038_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_126d_curv_v039_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_126d_curv_v040_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_252d_curv_v041_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_252d_curv_v042_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_252d_curv_v043_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_252d_curv_v044_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_252d_curv_v045_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_504d_curv_v046_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_504d_curv_v047_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_504d_curv_v048_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_504d_curv_v049_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d z
def f98hbm_f98_semi_hbm_advanced_packaging_signal_z_504d_curv_v050_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _z(x, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_63d_curv_v051_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_63d_curv_v052_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_63d_curv_v053_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_63d_curv_v054_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_63d_curv_v055_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_126d_curv_v056_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_126d_curv_v057_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_126d_curv_v058_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_126d_curv_v059_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_126d_curv_v060_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_252d_curv_v061_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_252d_curv_v062_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_252d_curv_v063_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_252d_curv_v064_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d dd
def f98hbm_f98_semi_hbm_advanced_packaging_signal_dd_252d_curv_v065_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _max(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_63d_curv_v066_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_63d_curv_v067_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_63d_curv_v068_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_63d_curv_v069_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_63d_curv_v070_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_126d_curv_v071_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_126d_curv_v072_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_126d_curv_v073_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_126d_curv_v074_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d runup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_runup_126d_curv_v075_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x - _min(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_63d_curv_v076_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_63d_curv_v077_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_63d_curv_v078_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_63d_curv_v079_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_63d_curv_v080_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_126d_curv_v081_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_126d_curv_v082_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_126d_curv_v083_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_126d_curv_v084_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d rng
def f98hbm_f98_semi_hbm_advanced_packaging_signal_rng_126d_curv_v085_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d pos
def f98hbm_f98_semi_hbm_advanced_packaging_signal_pos_126d_curv_v086_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d pos
def f98hbm_f98_semi_hbm_advanced_packaging_signal_pos_126d_curv_v087_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d pos
def f98hbm_f98_semi_hbm_advanced_packaging_signal_pos_126d_curv_v088_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d pos
def f98hbm_f98_semi_hbm_advanced_packaging_signal_pos_126d_curv_v089_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d pos
def f98hbm_f98_semi_hbm_advanced_packaging_signal_pos_126d_curv_v090_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_63d_curv_v091_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_63d_curv_v092_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_63d_curv_v093_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_63d_curv_v094_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_63d_curv_v095_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_126d_curv_v096_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_126d_curv_v097_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_126d_curv_v098_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_126d_curv_v099_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_126d_curv_v100_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_252d_curv_v101_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_252d_curv_v102_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_252d_curv_v103_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_252d_curv_v104_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d std
def f98hbm_f98_semi_hbm_advanced_packaging_signal_std_252d_curv_v105_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = _std(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_63d_curv_v106_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_63d_curv_v107_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_63d_curv_v108_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_63d_curv_v109_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_63d_curv_v110_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_126d_curv_v111_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_126d_curv_v112_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_126d_curv_v113_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_126d_curv_v114_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d hit
def f98hbm_f98_semi_hbm_advanced_packaging_signal_hit_126d_curv_v115_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d signcum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_signcum_126d_curv_v116_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d signcum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_signcum_126d_curv_v117_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d signcum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_signcum_126d_curv_v118_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d signcum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_signcum_126d_curv_v119_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d signcum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_signcum_126d_curv_v120_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_63d_curv_v121_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_63d_curv_v122_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_63d_curv_v123_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_63d_curv_v124_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_63d_curv_v125_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_252d_curv_v126_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_252d_curv_v127_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_252d_curv_v128_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_252d_curv_v129_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d cum
def f98hbm_f98_semi_hbm_advanced_packaging_signal_cum_252d_curv_v130_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d condup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_condup_126d_curv_v131_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d condup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_condup_126d_curv_v132_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d condup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_condup_126d_curv_v133_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d condup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_condup_126d_curv_v134_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d condup
def f98hbm_f98_semi_hbm_advanced_packaging_signal_condup_126d_curv_v135_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d conddn
def f98hbm_f98_semi_hbm_advanced_packaging_signal_conddn_126d_curv_v136_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d conddn
def f98hbm_f98_semi_hbm_advanced_packaging_signal_conddn_126d_curv_v137_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d conddn
def f98hbm_f98_semi_hbm_advanced_packaging_signal_conddn_126d_curv_v138_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d conddn
def f98hbm_f98_semi_hbm_advanced_packaging_signal_conddn_126d_curv_v139_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d conddn
def f98hbm_f98_semi_hbm_advanced_packaging_signal_conddn_126d_curv_v140_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d corr
def f98hbm_f98_semi_hbm_advanced_packaging_signal_corr_126d_curv_v141_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d corr
def f98hbm_f98_semi_hbm_advanced_packaging_signal_corr_126d_curv_v142_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d corr
def f98hbm_f98_semi_hbm_advanced_packaging_signal_corr_126d_curv_v143_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d corr
def f98hbm_f98_semi_hbm_advanced_packaging_signal_corr_126d_curv_v144_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d corr
def f98hbm_f98_semi_hbm_advanced_packaging_signal_corr_126d_curv_v145_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d ratio
def f98hbm_f98_semi_hbm_advanced_packaging_signal_ratio_126d_curv_v146_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d ratio
def f98hbm_f98_semi_hbm_advanced_packaging_signal_ratio_126d_curv_v147_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d ratio
def f98hbm_f98_semi_hbm_advanced_packaging_signal_ratio_126d_curv_v148_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d ratio
def f98hbm_f98_semi_hbm_advanced_packaging_signal_ratio_126d_curv_v149_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d ratio
def f98hbm_f98_semi_hbm_advanced_packaging_signal_ratio_126d_curv_v150_signal(gp, revenue, capex, closeadj):
    x = _f98hbm_combo(gp, revenue, capex, 63)
    y = _f98hbm_gm_expand(gp, revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
