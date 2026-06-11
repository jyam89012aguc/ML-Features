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
def _f78_buf(cashneq, opex):
    return cashneq / (opex / 12.0).replace(0, np.nan)


# 5d curv of 21d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_21d_curv_v001_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_21d_curv_v002_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_21d_curv_v003_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_21d_curv_v004_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_21d_curv_v005_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_63d_curv_v006_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_63d_curv_v007_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_63d_curv_v008_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_63d_curv_v009_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_63d_curv_v010_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_126d_curv_v011_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_126d_curv_v012_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_126d_curv_v013_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_126d_curv_v014_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_126d_curv_v015_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_252d_curv_v016_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_252d_curv_v017_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_252d_curv_v018_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_252d_curv_v019_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_252d_curv_v020_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_504d_curv_v021_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_504d_curv_v022_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_504d_curv_v023_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_504d_curv_v024_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d lbuf level
def f78lb_f78_semi_liquidity_buffer_lbuf_level_504d_curv_v025_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_21d_curv_v026_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_21d_curv_v027_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_21d_curv_v028_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_21d_curv_v029_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_21d_curv_v030_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_63d_curv_v031_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_63d_curv_v032_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_63d_curv_v033_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_63d_curv_v034_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_63d_curv_v035_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_126d_curv_v036_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_126d_curv_v037_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_126d_curv_v038_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_126d_curv_v039_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_126d_curv_v040_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_252d_curv_v041_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_252d_curv_v042_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_252d_curv_v043_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_252d_curv_v044_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_252d_curv_v045_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_504d_curv_v046_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_504d_curv_v047_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_504d_curv_v048_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_504d_curv_v049_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d lbuf z
def f78lb_f78_semi_liquidity_buffer_lbuf_z_504d_curv_v050_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_21d_curv_v051_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_21d_curv_v052_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_21d_curv_v053_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_21d_curv_v054_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_21d_curv_v055_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_63d_curv_v056_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_63d_curv_v057_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_63d_curv_v058_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_63d_curv_v059_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_63d_curv_v060_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_126d_curv_v061_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_126d_curv_v062_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_126d_curv_v063_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_126d_curv_v064_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_126d_curv_v065_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_252d_curv_v066_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_252d_curv_v067_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_252d_curv_v068_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_252d_curv_v069_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_252d_curv_v070_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_504d_curv_v071_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_504d_curv_v072_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_504d_curv_v073_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_504d_curv_v074_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d lbuf max
def f78lb_f78_semi_liquidity_buffer_lbuf_max_504d_curv_v075_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_21d_curv_v076_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_21d_curv_v077_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_21d_curv_v078_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_21d_curv_v079_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_21d_curv_v080_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_63d_curv_v081_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_63d_curv_v082_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_63d_curv_v083_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_63d_curv_v084_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_63d_curv_v085_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_126d_curv_v086_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_126d_curv_v087_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_126d_curv_v088_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_126d_curv_v089_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_126d_curv_v090_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_252d_curv_v091_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_252d_curv_v092_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_252d_curv_v093_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_252d_curv_v094_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_252d_curv_v095_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_504d_curv_v096_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_504d_curv_v097_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_504d_curv_v098_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_504d_curv_v099_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d lbuf min
def f78lb_f78_semi_liquidity_buffer_lbuf_min_504d_curv_v100_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_21d_curv_v101_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_21d_curv_v102_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_21d_curv_v103_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_21d_curv_v104_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_21d_curv_v105_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_63d_curv_v106_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_63d_curv_v107_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_63d_curv_v108_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_63d_curv_v109_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_63d_curv_v110_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_126d_curv_v111_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_126d_curv_v112_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_126d_curv_v113_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_126d_curv_v114_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_126d_curv_v115_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_252d_curv_v116_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_252d_curv_v117_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_252d_curv_v118_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_252d_curv_v119_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_252d_curv_v120_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_504d_curv_v121_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_504d_curv_v122_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_504d_curv_v123_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_504d_curv_v124_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d lbuf rng
def f78lb_f78_semi_liquidity_buffer_lbuf_rng_504d_curv_v125_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_21d_curv_v126_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_21d_curv_v127_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_21d_curv_v128_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_21d_curv_v129_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_21d_curv_v130_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_63d_curv_v131_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_63d_curv_v132_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_63d_curv_v133_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_63d_curv_v134_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_63d_curv_v135_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_126d_curv_v136_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_126d_curv_v137_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_126d_curv_v138_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_126d_curv_v139_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_126d_curv_v140_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_252d_curv_v141_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_252d_curv_v142_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_252d_curv_v143_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_252d_curv_v144_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_252d_curv_v145_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_504d_curv_v146_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_504d_curv_v147_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_504d_curv_v148_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_504d_curv_v149_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d lbuf dd
def f78lb_f78_semi_liquidity_buffer_lbuf_dd_504d_curv_v150_signal(cashneq, opex, closeadj):
    r = _f78_buf(cashneq, opex)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
