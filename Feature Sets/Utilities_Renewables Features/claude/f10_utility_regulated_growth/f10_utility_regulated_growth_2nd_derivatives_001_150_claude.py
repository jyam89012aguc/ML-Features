import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f10_long_cycle_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f10_compounding_quality(revenue, w):
    g = revenue.pct_change(periods=w)
    g_mean = g.rolling(w, min_periods=max(1, w // 2)).mean()
    g_std = g.rolling(w, min_periods=max(1, w // 2)).std()
    return g_mean / g_std.replace(0, np.nan)


def _f10_revenue_compound(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return (rg + eg) * 0.5


def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w5_s0_slope_v001_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w5_s1_slope_v002_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w5_s2_slope_v003_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w21_s0_slope_v004_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w21_s1_slope_v005_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w21_s2_slope_v006_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w63_s0_slope_v007_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w63_s1_slope_v008_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w63_s2_slope_v009_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w5_s0_slope_v010_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w5_s1_slope_v011_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w5_s2_slope_v012_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w21_s0_slope_v013_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w21_s1_slope_v014_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w21_s2_slope_v015_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w63_s0_slope_v016_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w63_s1_slope_v017_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w63_s2_slope_v018_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w5_s0_slope_v019_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w5_s1_slope_v020_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w5_s2_slope_v021_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w21_s0_slope_v022_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w21_s1_slope_v023_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w21_s2_slope_v024_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w63_s0_slope_v025_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w63_s1_slope_v026_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w63_s2_slope_v027_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w5_s0_slope_v028_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w5_s1_slope_v029_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w5_s2_slope_v030_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w21_s0_slope_v031_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w21_s1_slope_v032_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w21_s2_slope_v033_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w63_s0_slope_v034_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w63_s1_slope_v035_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w63_s2_slope_v036_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w5_s0_slope_v037_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w5_s1_slope_v038_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w5_s2_slope_v039_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w21_s0_slope_v040_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w21_s1_slope_v041_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w21_s2_slope_v042_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w63_s0_slope_v043_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w63_s1_slope_v044_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w63_s2_slope_v045_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w5_s0_slope_v046_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w5_s1_slope_v047_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w5_s2_slope_v048_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w21_s0_slope_v049_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w21_s1_slope_v050_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w21_s2_slope_v051_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w63_s0_slope_v052_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w63_s1_slope_v053_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w63_s2_slope_v054_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w5_s0_slope_v055_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w5_s1_slope_v056_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w5_s2_slope_v057_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w21_s0_slope_v058_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w21_s1_slope_v059_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w21_s2_slope_v060_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w63_s0_slope_v061_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w63_s1_slope_v062_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w63_s2_slope_v063_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w5_s0_slope_v064_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w5_s1_slope_v065_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w5_s2_slope_v066_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w21_s0_slope_v067_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w21_s1_slope_v068_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w21_s2_slope_v069_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w63_s0_slope_v070_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w63_s1_slope_v071_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w63_s2_slope_v072_signal(revenue, closeadj):
    base = _f10_long_cycle_growth(revenue, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w5_s0_slope_v073_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w5_s1_slope_v074_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w5_s2_slope_v075_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w21_s0_slope_v076_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w21_s1_slope_v077_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w21_s2_slope_v078_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w63_s0_slope_v079_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w63_s1_slope_v080_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w63_s2_slope_v081_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w5_s0_slope_v082_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w5_s1_slope_v083_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w5_s2_slope_v084_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w21_s0_slope_v085_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w21_s1_slope_v086_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w21_s2_slope_v087_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w63_s0_slope_v088_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w63_s1_slope_v089_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w63_s2_slope_v090_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w5_s0_slope_v091_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w5_s1_slope_v092_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w5_s2_slope_v093_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w21_s0_slope_v094_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w21_s1_slope_v095_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w21_s2_slope_v096_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w63_s0_slope_v097_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w63_s1_slope_v098_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w63_s2_slope_v099_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w5_s0_slope_v100_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w5_s1_slope_v101_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w5_s2_slope_v102_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w21_s0_slope_v103_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w21_s1_slope_v104_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w21_s2_slope_v105_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w63_s0_slope_v106_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w63_s1_slope_v107_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w63_s2_slope_v108_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w5_s0_slope_v109_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w5_s1_slope_v110_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w5_s2_slope_v111_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w21_s0_slope_v112_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w21_s1_slope_v113_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w21_s2_slope_v114_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w63_s0_slope_v115_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w63_s1_slope_v116_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w63_s2_slope_v117_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w5_s0_slope_v118_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w5_s1_slope_v119_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w5_s2_slope_v120_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w21_s0_slope_v121_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w21_s1_slope_v122_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w21_s2_slope_v123_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w63_s0_slope_v124_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w63_s1_slope_v125_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w63_s2_slope_v126_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w5_s0_slope_v127_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w5_s1_slope_v128_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w5_s2_slope_v129_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w21_s0_slope_v130_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w21_s1_slope_v131_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w21_s2_slope_v132_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w63_s0_slope_v133_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w63_s1_slope_v134_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w63_s2_slope_v135_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w5_s0_slope_v136_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w5_s1_slope_v137_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w5_s2_slope_v138_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w21_s0_slope_v139_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w21_s1_slope_v140_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w21_s2_slope_v141_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w63_s0_slope_v142_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w63_s1_slope_v143_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w63_s2_slope_v144_signal(revenue, closeadj):
    base = _f10_compounding_quality(revenue, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w5_s0_slope_v145_signal(revenue, ebitda, closeadj):
    base = _f10_revenue_compound(revenue, ebitda, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w5_s1_slope_v146_signal(revenue, ebitda, closeadj):
    base = _f10_revenue_compound(revenue, ebitda, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w5_s2_slope_v147_signal(revenue, ebitda, closeadj):
    base = _f10_revenue_compound(revenue, ebitda, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w21_s0_slope_v148_signal(revenue, ebitda, closeadj):
    base = _f10_revenue_compound(revenue, ebitda, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w21_s1_slope_v149_signal(revenue, ebitda, closeadj):
    base = _f10_revenue_compound(revenue, ebitda, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w21_s2_slope_v150_signal(revenue, ebitda, closeadj):
    base = _f10_revenue_compound(revenue, ebitda, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w5_s0_slope_v001_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w5_s1_slope_v002_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w5_s2_slope_v003_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w21_s0_slope_v004_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w21_s1_slope_v005_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w21_s2_slope_v006_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w63_s0_slope_v007_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w63_s1_slope_v008_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_pct_w63_s2_slope_v009_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w5_s0_slope_v010_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w5_s1_slope_v011_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w5_s2_slope_v012_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w21_s0_slope_v013_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w21_s1_slope_v014_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w21_s2_slope_v015_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w63_s0_slope_v016_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w63_s1_slope_v017_signal,
    f10urg_f10_utility_regulated_growth_longg_21d_slope_diff_norm_w63_s2_slope_v018_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w5_s0_slope_v019_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w5_s1_slope_v020_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w5_s2_slope_v021_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w21_s0_slope_v022_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w21_s1_slope_v023_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w21_s2_slope_v024_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w63_s0_slope_v025_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w63_s1_slope_v026_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_pct_w63_s2_slope_v027_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w5_s0_slope_v028_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w5_s1_slope_v029_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w5_s2_slope_v030_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w21_s0_slope_v031_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w21_s1_slope_v032_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w21_s2_slope_v033_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w63_s0_slope_v034_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w63_s1_slope_v035_signal,
    f10urg_f10_utility_regulated_growth_longg_63d_slope_diff_norm_w63_s2_slope_v036_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w5_s0_slope_v037_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w5_s1_slope_v038_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w5_s2_slope_v039_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w21_s0_slope_v040_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w21_s1_slope_v041_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w21_s2_slope_v042_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w63_s0_slope_v043_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w63_s1_slope_v044_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_pct_w63_s2_slope_v045_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w5_s0_slope_v046_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w5_s1_slope_v047_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w5_s2_slope_v048_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w21_s0_slope_v049_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w21_s1_slope_v050_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w21_s2_slope_v051_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w63_s0_slope_v052_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w63_s1_slope_v053_signal,
    f10urg_f10_utility_regulated_growth_longg_126d_slope_diff_norm_w63_s2_slope_v054_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w5_s0_slope_v055_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w5_s1_slope_v056_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w5_s2_slope_v057_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w21_s0_slope_v058_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w21_s1_slope_v059_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w21_s2_slope_v060_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w63_s0_slope_v061_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w63_s1_slope_v062_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_pct_w63_s2_slope_v063_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w5_s0_slope_v064_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w5_s1_slope_v065_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w5_s2_slope_v066_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w21_s0_slope_v067_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w21_s1_slope_v068_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w21_s2_slope_v069_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w63_s0_slope_v070_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w63_s1_slope_v071_signal,
    f10urg_f10_utility_regulated_growth_longg_252d_slope_diff_norm_w63_s2_slope_v072_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w5_s0_slope_v073_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w5_s1_slope_v074_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w5_s2_slope_v075_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w21_s0_slope_v076_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w21_s1_slope_v077_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w21_s2_slope_v078_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w63_s0_slope_v079_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w63_s1_slope_v080_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_pct_w63_s2_slope_v081_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w5_s0_slope_v082_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w5_s1_slope_v083_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w5_s2_slope_v084_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w21_s0_slope_v085_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w21_s1_slope_v086_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w21_s2_slope_v087_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w63_s0_slope_v088_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w63_s1_slope_v089_signal,
    f10urg_f10_utility_regulated_growth_compq_21d_slope_diff_norm_w63_s2_slope_v090_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w5_s0_slope_v091_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w5_s1_slope_v092_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w5_s2_slope_v093_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w21_s0_slope_v094_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w21_s1_slope_v095_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w21_s2_slope_v096_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w63_s0_slope_v097_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w63_s1_slope_v098_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_pct_w63_s2_slope_v099_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w5_s0_slope_v100_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w5_s1_slope_v101_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w5_s2_slope_v102_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w21_s0_slope_v103_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w21_s1_slope_v104_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w21_s2_slope_v105_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w63_s0_slope_v106_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w63_s1_slope_v107_signal,
    f10urg_f10_utility_regulated_growth_compq_63d_slope_diff_norm_w63_s2_slope_v108_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w5_s0_slope_v109_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w5_s1_slope_v110_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w5_s2_slope_v111_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w21_s0_slope_v112_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w21_s1_slope_v113_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w21_s2_slope_v114_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w63_s0_slope_v115_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w63_s1_slope_v116_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_pct_w63_s2_slope_v117_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w5_s0_slope_v118_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w5_s1_slope_v119_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w5_s2_slope_v120_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w21_s0_slope_v121_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w21_s1_slope_v122_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w21_s2_slope_v123_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w63_s0_slope_v124_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w63_s1_slope_v125_signal,
    f10urg_f10_utility_regulated_growth_compq_126d_slope_diff_norm_w63_s2_slope_v126_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w5_s0_slope_v127_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w5_s1_slope_v128_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w5_s2_slope_v129_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w21_s0_slope_v130_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w21_s1_slope_v131_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w21_s2_slope_v132_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w63_s0_slope_v133_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w63_s1_slope_v134_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_pct_w63_s2_slope_v135_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w5_s0_slope_v136_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w5_s1_slope_v137_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w5_s2_slope_v138_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w21_s0_slope_v139_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w21_s1_slope_v140_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w21_s2_slope_v141_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w63_s0_slope_v142_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w63_s1_slope_v143_signal,
    f10urg_f10_utility_regulated_growth_compq_252d_slope_diff_norm_w63_s2_slope_v144_signal,
    f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w5_s0_slope_v145_signal,
    f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w5_s1_slope_v146_signal,
    f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w5_s2_slope_v147_signal,
    f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w21_s0_slope_v148_signal,
    f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w21_s1_slope_v149_signal,
    f10urg_f10_utility_regulated_growth_revcomp_21d_slope_pct_w21_s2_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_UTILITY_REGULATED_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f10_long_cycle_growth", "_f10_compounding_quality", "_f10_revenue_compound",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f10_utility_regulated_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
