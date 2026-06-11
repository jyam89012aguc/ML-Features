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
def _f85_fpe(pe):
    return pe


# 5d slope of 21d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_21d_slope_v001_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_21d_slope_v002_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_21d_slope_v003_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_21d_slope_v004_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_21d_slope_v005_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_63d_slope_v006_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_63d_slope_v007_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_63d_slope_v008_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_63d_slope_v009_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_63d_slope_v010_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_126d_slope_v011_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_126d_slope_v012_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_126d_slope_v013_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_126d_slope_v014_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_126d_slope_v015_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_252d_slope_v016_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_252d_slope_v017_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_252d_slope_v018_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_252d_slope_v019_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_252d_slope_v020_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_504d_slope_v021_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_504d_slope_v022_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_504d_slope_v023_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_504d_slope_v024_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d fpe level
def f85fpe_f85_semi_fwd_pe_reset_fpe_level_504d_slope_v025_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_21d_slope_v026_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_21d_slope_v027_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_21d_slope_v028_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_21d_slope_v029_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_21d_slope_v030_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_63d_slope_v031_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_63d_slope_v032_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_63d_slope_v033_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_63d_slope_v034_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_63d_slope_v035_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_126d_slope_v036_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_126d_slope_v037_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_126d_slope_v038_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_126d_slope_v039_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_126d_slope_v040_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_252d_slope_v041_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_252d_slope_v042_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_252d_slope_v043_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_252d_slope_v044_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_252d_slope_v045_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_504d_slope_v046_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_504d_slope_v047_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_504d_slope_v048_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_504d_slope_v049_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d fpe z
def f85fpe_f85_semi_fwd_pe_reset_fpe_z_504d_slope_v050_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_21d_slope_v051_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_21d_slope_v052_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_21d_slope_v053_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_21d_slope_v054_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_21d_slope_v055_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_63d_slope_v056_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_63d_slope_v057_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_63d_slope_v058_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_63d_slope_v059_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_63d_slope_v060_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_126d_slope_v061_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_126d_slope_v062_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_126d_slope_v063_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_126d_slope_v064_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_126d_slope_v065_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_252d_slope_v066_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_252d_slope_v067_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_252d_slope_v068_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_252d_slope_v069_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_252d_slope_v070_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_504d_slope_v071_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_504d_slope_v072_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_504d_slope_v073_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_504d_slope_v074_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d fpe max
def f85fpe_f85_semi_fwd_pe_reset_fpe_max_504d_slope_v075_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_21d_slope_v076_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_21d_slope_v077_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_21d_slope_v078_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_21d_slope_v079_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_21d_slope_v080_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_63d_slope_v081_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_63d_slope_v082_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_63d_slope_v083_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_63d_slope_v084_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_63d_slope_v085_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_126d_slope_v086_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_126d_slope_v087_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_126d_slope_v088_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_126d_slope_v089_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_126d_slope_v090_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_252d_slope_v091_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_252d_slope_v092_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_252d_slope_v093_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_252d_slope_v094_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_252d_slope_v095_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_504d_slope_v096_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_504d_slope_v097_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_504d_slope_v098_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_504d_slope_v099_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d fpe min
def f85fpe_f85_semi_fwd_pe_reset_fpe_min_504d_slope_v100_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_21d_slope_v101_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_21d_slope_v102_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_21d_slope_v103_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_21d_slope_v104_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_21d_slope_v105_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_63d_slope_v106_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_63d_slope_v107_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_63d_slope_v108_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_63d_slope_v109_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_63d_slope_v110_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_126d_slope_v111_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_126d_slope_v112_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_126d_slope_v113_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_126d_slope_v114_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_126d_slope_v115_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_252d_slope_v116_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_252d_slope_v117_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_252d_slope_v118_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_252d_slope_v119_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_252d_slope_v120_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_504d_slope_v121_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_504d_slope_v122_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_504d_slope_v123_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_504d_slope_v124_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d fpe rng
def f85fpe_f85_semi_fwd_pe_reset_fpe_rng_504d_slope_v125_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_21d_slope_v126_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_21d_slope_v127_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_21d_slope_v128_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_21d_slope_v129_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_21d_slope_v130_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_63d_slope_v131_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_63d_slope_v132_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_63d_slope_v133_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_63d_slope_v134_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_63d_slope_v135_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_126d_slope_v136_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_126d_slope_v137_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_126d_slope_v138_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_126d_slope_v139_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_126d_slope_v140_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_252d_slope_v141_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_252d_slope_v142_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_252d_slope_v143_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_252d_slope_v144_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_252d_slope_v145_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_504d_slope_v146_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_504d_slope_v147_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_504d_slope_v148_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_504d_slope_v149_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d fpe dd
def f85fpe_f85_semi_fwd_pe_reset_fpe_dd_504d_slope_v150_signal(pe, closeadj):
    r = _f85_fpe(pe)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
