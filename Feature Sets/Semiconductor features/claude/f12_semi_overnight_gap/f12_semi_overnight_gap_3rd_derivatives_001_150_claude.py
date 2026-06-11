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
def _f12_gap(open_p, close_p):
    return open_p / close_p.shift(1) - 1.0


def _f12_gap_log(open_p, close_p):
    return np.log(open_p.replace(0, np.nan) / close_p.shift(1).replace(0, np.nan))


def _f12_intraday(open_p, close_p):
    return close_p / open_p - 1.0


def _f12_overnight_idx(open_p, close_p):
    g = open_p / close_p.shift(1) - 1.0
    return (1.0 + g).cumprod()


# 5d curvature of 21d cumgap
def f12og_f12_semi_overnight_gap_cumgap_21d_curv_v001_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(21, min_periods=11).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d cumgap
def f12og_f12_semi_overnight_gap_cumgap_21d_curv_v002_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(21, min_periods=11).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d cumgap
def f12og_f12_semi_overnight_gap_cumgap_21d_curv_v003_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(21, min_periods=11).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d cumgap
def f12og_f12_semi_overnight_gap_cumgap_21d_curv_v004_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(21, min_periods=11).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d cumgap
def f12og_f12_semi_overnight_gap_cumgap_21d_curv_v005_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(21, min_periods=11).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d cumgap
def f12og_f12_semi_overnight_gap_cumgap_63d_curv_v006_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cumgap
def f12og_f12_semi_overnight_gap_cumgap_63d_curv_v007_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d cumgap
def f12og_f12_semi_overnight_gap_cumgap_63d_curv_v008_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d cumgap
def f12og_f12_semi_overnight_gap_cumgap_63d_curv_v009_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d cumgap
def f12og_f12_semi_overnight_gap_cumgap_63d_curv_v010_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d cumgap
def f12og_f12_semi_overnight_gap_cumgap_126d_curv_v011_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d cumgap
def f12og_f12_semi_overnight_gap_cumgap_126d_curv_v012_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d cumgap
def f12og_f12_semi_overnight_gap_cumgap_126d_curv_v013_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d cumgap
def f12og_f12_semi_overnight_gap_cumgap_126d_curv_v014_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d cumgap
def f12og_f12_semi_overnight_gap_cumgap_126d_curv_v015_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d cumgap
def f12og_f12_semi_overnight_gap_cumgap_252d_curv_v016_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d cumgap
def f12og_f12_semi_overnight_gap_cumgap_252d_curv_v017_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d cumgap
def f12og_f12_semi_overnight_gap_cumgap_252d_curv_v018_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d cumgap
def f12og_f12_semi_overnight_gap_cumgap_252d_curv_v019_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d cumgap
def f12og_f12_semi_overnight_gap_cumgap_252d_curv_v020_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = g.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d meangap
def f12og_f12_semi_overnight_gap_meangap_21d_curv_v021_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d meangap
def f12og_f12_semi_overnight_gap_meangap_21d_curv_v022_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d meangap
def f12og_f12_semi_overnight_gap_meangap_21d_curv_v023_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d meangap
def f12og_f12_semi_overnight_gap_meangap_21d_curv_v024_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d meangap
def f12og_f12_semi_overnight_gap_meangap_21d_curv_v025_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d meangap
def f12og_f12_semi_overnight_gap_meangap_63d_curv_v026_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d meangap
def f12og_f12_semi_overnight_gap_meangap_63d_curv_v027_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d meangap
def f12og_f12_semi_overnight_gap_meangap_63d_curv_v028_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d meangap
def f12og_f12_semi_overnight_gap_meangap_63d_curv_v029_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d meangap
def f12og_f12_semi_overnight_gap_meangap_63d_curv_v030_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d meangap
def f12og_f12_semi_overnight_gap_meangap_126d_curv_v031_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d meangap
def f12og_f12_semi_overnight_gap_meangap_126d_curv_v032_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d meangap
def f12og_f12_semi_overnight_gap_meangap_126d_curv_v033_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d meangap
def f12og_f12_semi_overnight_gap_meangap_126d_curv_v034_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d meangap
def f12og_f12_semi_overnight_gap_meangap_126d_curv_v035_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d meangap
def f12og_f12_semi_overnight_gap_meangap_252d_curv_v036_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d meangap
def f12og_f12_semi_overnight_gap_meangap_252d_curv_v037_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d meangap
def f12og_f12_semi_overnight_gap_meangap_252d_curv_v038_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d meangap
def f12og_f12_semi_overnight_gap_meangap_252d_curv_v039_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d meangap
def f12og_f12_semi_overnight_gap_meangap_252d_curv_v040_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d stdgap
def f12og_f12_semi_overnight_gap_stdgap_21d_curv_v041_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d stdgap
def f12og_f12_semi_overnight_gap_stdgap_21d_curv_v042_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d stdgap
def f12og_f12_semi_overnight_gap_stdgap_21d_curv_v043_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d stdgap
def f12og_f12_semi_overnight_gap_stdgap_21d_curv_v044_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d stdgap
def f12og_f12_semi_overnight_gap_stdgap_21d_curv_v045_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d stdgap
def f12og_f12_semi_overnight_gap_stdgap_63d_curv_v046_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d stdgap
def f12og_f12_semi_overnight_gap_stdgap_63d_curv_v047_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d stdgap
def f12og_f12_semi_overnight_gap_stdgap_63d_curv_v048_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d stdgap
def f12og_f12_semi_overnight_gap_stdgap_63d_curv_v049_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d stdgap
def f12og_f12_semi_overnight_gap_stdgap_63d_curv_v050_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d stdgap
def f12og_f12_semi_overnight_gap_stdgap_126d_curv_v051_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d stdgap
def f12og_f12_semi_overnight_gap_stdgap_126d_curv_v052_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d stdgap
def f12og_f12_semi_overnight_gap_stdgap_126d_curv_v053_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d stdgap
def f12og_f12_semi_overnight_gap_stdgap_126d_curv_v054_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d stdgap
def f12og_f12_semi_overnight_gap_stdgap_126d_curv_v055_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d stdgap
def f12og_f12_semi_overnight_gap_stdgap_252d_curv_v056_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d stdgap
def f12og_f12_semi_overnight_gap_stdgap_252d_curv_v057_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d stdgap
def f12og_f12_semi_overnight_gap_stdgap_252d_curv_v058_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d stdgap
def f12og_f12_semi_overnight_gap_stdgap_252d_curv_v059_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d stdgap
def f12og_f12_semi_overnight_gap_stdgap_252d_curv_v060_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _std(g, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d zgap
def f12og_f12_semi_overnight_gap_zgap_21d_curv_v061_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d zgap
def f12og_f12_semi_overnight_gap_zgap_21d_curv_v062_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d zgap
def f12og_f12_semi_overnight_gap_zgap_21d_curv_v063_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d zgap
def f12og_f12_semi_overnight_gap_zgap_21d_curv_v064_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d zgap
def f12og_f12_semi_overnight_gap_zgap_21d_curv_v065_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d zgap
def f12og_f12_semi_overnight_gap_zgap_63d_curv_v066_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d zgap
def f12og_f12_semi_overnight_gap_zgap_63d_curv_v067_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d zgap
def f12og_f12_semi_overnight_gap_zgap_63d_curv_v068_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d zgap
def f12og_f12_semi_overnight_gap_zgap_63d_curv_v069_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d zgap
def f12og_f12_semi_overnight_gap_zgap_63d_curv_v070_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d zgap
def f12og_f12_semi_overnight_gap_zgap_126d_curv_v071_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d zgap
def f12og_f12_semi_overnight_gap_zgap_126d_curv_v072_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d zgap
def f12og_f12_semi_overnight_gap_zgap_126d_curv_v073_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d zgap
def f12og_f12_semi_overnight_gap_zgap_126d_curv_v074_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d zgap
def f12og_f12_semi_overnight_gap_zgap_126d_curv_v075_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _z(g, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_21d_curv_v076_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_21d_curv_v077_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_21d_curv_v078_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_21d_curv_v079_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_21d_curv_v080_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(21, min_periods=11).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_63d_curv_v081_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_63d_curv_v082_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_63d_curv_v083_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_63d_curv_v084_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_63d_curv_v085_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_126d_curv_v086_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_126d_curv_v087_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_126d_curv_v088_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_126d_curv_v089_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_126d_curv_v090_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_252d_curv_v091_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_252d_curv_v092_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_252d_curv_v093_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_252d_curv_v094_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d posgaphit
def f12og_f12_semi_overnight_gap_posgaphit_252d_curv_v095_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d rnggap
def f12og_f12_semi_overnight_gap_rnggap_63d_curv_v096_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 63) - _min(g, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d rnggap
def f12og_f12_semi_overnight_gap_rnggap_63d_curv_v097_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 63) - _min(g, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d rnggap
def f12og_f12_semi_overnight_gap_rnggap_63d_curv_v098_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 63) - _min(g, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d rnggap
def f12og_f12_semi_overnight_gap_rnggap_63d_curv_v099_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 63) - _min(g, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d rnggap
def f12og_f12_semi_overnight_gap_rnggap_63d_curv_v100_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 63) - _min(g, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d rnggap
def f12og_f12_semi_overnight_gap_rnggap_252d_curv_v101_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 252) - _min(g, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d rnggap
def f12og_f12_semi_overnight_gap_rnggap_252d_curv_v102_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 252) - _min(g, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d rnggap
def f12og_f12_semi_overnight_gap_rnggap_252d_curv_v103_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 252) - _min(g, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d rnggap
def f12og_f12_semi_overnight_gap_rnggap_252d_curv_v104_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 252) - _min(g, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d rnggap
def f12og_f12_semi_overnight_gap_rnggap_252d_curv_v105_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _max(g, 252) - _min(g, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d posgap
def f12og_f12_semi_overnight_gap_posgap_63d_curv_v106_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d posgap
def f12og_f12_semi_overnight_gap_posgap_63d_curv_v107_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d posgap
def f12og_f12_semi_overnight_gap_posgap_63d_curv_v108_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d posgap
def f12og_f12_semi_overnight_gap_posgap_63d_curv_v109_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d posgap
def f12og_f12_semi_overnight_gap_posgap_63d_curv_v110_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d posgap
def f12og_f12_semi_overnight_gap_posgap_252d_curv_v111_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d posgap
def f12og_f12_semi_overnight_gap_posgap_252d_curv_v112_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d posgap
def f12og_f12_semi_overnight_gap_posgap_252d_curv_v113_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d posgap
def f12og_f12_semi_overnight_gap_posgap_252d_curv_v114_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d posgap
def f12og_f12_semi_overnight_gap_posgap_252d_curv_v115_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_63d_curv_v116_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_63d_curv_v117_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_63d_curv_v118_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_63d_curv_v119_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_63d_curv_v120_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_252d_curv_v121_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_252d_curv_v122_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_252d_curv_v123_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_252d_curv_v124_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d signgapcum
def f12og_f12_semi_overnight_gap_signgapcum_252d_curv_v125_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = pd.Series(np.sign(g), index=g.index).rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d gapir
def f12og_f12_semi_overnight_gap_gapir_63d_curv_v126_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63) / _std(g, 63).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d gapir
def f12og_f12_semi_overnight_gap_gapir_63d_curv_v127_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63) / _std(g, 63).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d gapir
def f12og_f12_semi_overnight_gap_gapir_63d_curv_v128_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63) / _std(g, 63).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d gapir
def f12og_f12_semi_overnight_gap_gapir_63d_curv_v129_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63) / _std(g, 63).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d gapir
def f12og_f12_semi_overnight_gap_gapir_63d_curv_v130_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 63) / _std(g, 63).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d gapir
def f12og_f12_semi_overnight_gap_gapir_252d_curv_v131_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d gapir
def f12og_f12_semi_overnight_gap_gapir_252d_curv_v132_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d gapir
def f12og_f12_semi_overnight_gap_gapir_252d_curv_v133_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d gapir
def f12og_f12_semi_overnight_gap_gapir_252d_curv_v134_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d gapir
def f12og_f12_semi_overnight_gap_gapir_252d_curv_v135_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d ovncumdd
def f12og_f12_semi_overnight_gap_ovncumdd_63d_curv_v136_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _max(cum, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d ovncumdd
def f12og_f12_semi_overnight_gap_ovncumdd_63d_curv_v137_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _max(cum, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d ovncumdd
def f12og_f12_semi_overnight_gap_ovncumdd_63d_curv_v138_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _max(cum, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d ovncumdd
def f12og_f12_semi_overnight_gap_ovncumdd_63d_curv_v139_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _max(cum, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d ovncumdd
def f12og_f12_semi_overnight_gap_ovncumdd_63d_curv_v140_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _max(cum, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d ovncumup
def f12og_f12_semi_overnight_gap_ovncumup_63d_curv_v141_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _min(cum, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d ovncumup
def f12og_f12_semi_overnight_gap_ovncumup_63d_curv_v142_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _min(cum, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d ovncumup
def f12og_f12_semi_overnight_gap_ovncumup_63d_curv_v143_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _min(cum, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d ovncumup
def f12og_f12_semi_overnight_gap_ovncumup_63d_curv_v144_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _min(cum, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d ovncumup
def f12og_f12_semi_overnight_gap_ovncumup_63d_curv_v145_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    cum = g.rolling(63, min_periods=32).sum()
    base = cum - _min(cum, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d gapshare
def f12og_f12_semi_overnight_gap_gapshare_63d_curv_v146_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    base = _mean(num / den.replace(0, np.nan), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d gapshare
def f12og_f12_semi_overnight_gap_gapshare_63d_curv_v147_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    base = _mean(num / den.replace(0, np.nan), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d gapshare
def f12og_f12_semi_overnight_gap_gapshare_63d_curv_v148_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    base = _mean(num / den.replace(0, np.nan), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d gapshare
def f12og_f12_semi_overnight_gap_gapshare_63d_curv_v149_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    base = _mean(num / den.replace(0, np.nan), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d gapshare
def f12og_f12_semi_overnight_gap_gapshare_63d_curv_v150_signal(open, closeadj):
    g = _f12_gap(open, closeadj)
    intra = closeadj / open - 1.0
    num = g.abs()
    den = g.abs() + intra.abs()
    base = _mean(num / den.replace(0, np.nan), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
