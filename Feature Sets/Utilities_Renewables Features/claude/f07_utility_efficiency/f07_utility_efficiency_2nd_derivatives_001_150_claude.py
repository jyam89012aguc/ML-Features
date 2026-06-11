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
def _f07_opex_intensity(opex, revenue):
    return opex / revenue.replace(0, np.nan)


def _f07_efficiency_trend(opex, revenue, w):
    oi = opex / revenue.replace(0, np.nan)
    return -oi.rolling(w, min_periods=max(1, w // 2)).mean()


def _f07_efficiency_score(opex, sgna, revenue, w):
    oi = opex / revenue.replace(0, np.nan)
    si = sgna / revenue.replace(0, np.nan)
    combined = (oi + si) * 0.5
    return -combined.rolling(w, min_periods=max(1, w // 2)).mean()


def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w5_s0_slope_v001_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w5_s1_slope_v002_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w5_s2_slope_v003_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w21_s0_slope_v004_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w21_s1_slope_v005_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w21_s2_slope_v006_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w63_s0_slope_v007_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w63_s1_slope_v008_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w63_s2_slope_v009_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w5_s0_slope_v010_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w5_s1_slope_v011_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w5_s2_slope_v012_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w21_s0_slope_v013_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w21_s1_slope_v014_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w21_s2_slope_v015_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w63_s0_slope_v016_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w63_s1_slope_v017_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w63_s2_slope_v018_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w5_s0_slope_v019_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w5_s1_slope_v020_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w5_s2_slope_v021_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w21_s0_slope_v022_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w21_s1_slope_v023_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w21_s2_slope_v024_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w63_s0_slope_v025_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w63_s1_slope_v026_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w63_s2_slope_v027_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w5_s0_slope_v028_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w5_s1_slope_v029_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w5_s2_slope_v030_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w21_s0_slope_v031_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w21_s1_slope_v032_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w21_s2_slope_v033_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w63_s0_slope_v034_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w63_s1_slope_v035_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w63_s2_slope_v036_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w5_s0_slope_v037_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w5_s1_slope_v038_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w5_s2_slope_v039_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w21_s0_slope_v040_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w21_s1_slope_v041_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w21_s2_slope_v042_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w63_s0_slope_v043_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w63_s1_slope_v044_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w63_s2_slope_v045_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w5_s0_slope_v046_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w5_s1_slope_v047_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w5_s2_slope_v048_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w21_s0_slope_v049_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w21_s1_slope_v050_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w21_s2_slope_v051_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w63_s0_slope_v052_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w63_s1_slope_v053_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w63_s2_slope_v054_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w5_s0_slope_v055_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w5_s1_slope_v056_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w5_s2_slope_v057_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w21_s0_slope_v058_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w21_s1_slope_v059_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w21_s2_slope_v060_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w63_s0_slope_v061_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w63_s1_slope_v062_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w63_s2_slope_v063_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w5_s0_slope_v064_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w5_s1_slope_v065_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w5_s2_slope_v066_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w21_s0_slope_v067_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w21_s1_slope_v068_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w21_s2_slope_v069_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w63_s0_slope_v070_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w63_s1_slope_v071_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w63_s2_slope_v072_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w5_s0_slope_v073_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w5_s1_slope_v074_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w5_s2_slope_v075_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w21_s0_slope_v076_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w21_s1_slope_v077_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w21_s2_slope_v078_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w63_s0_slope_v079_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w63_s1_slope_v080_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w63_s2_slope_v081_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w5_s0_slope_v082_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w5_s1_slope_v083_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w5_s2_slope_v084_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w21_s0_slope_v085_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w21_s1_slope_v086_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w21_s2_slope_v087_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w63_s0_slope_v088_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w63_s1_slope_v089_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w63_s2_slope_v090_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w5_s0_slope_v091_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w5_s1_slope_v092_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w5_s2_slope_v093_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w21_s0_slope_v094_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w21_s1_slope_v095_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w21_s2_slope_v096_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w63_s0_slope_v097_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w63_s1_slope_v098_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w63_s2_slope_v099_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w5_s0_slope_v100_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w5_s1_slope_v101_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w5_s2_slope_v102_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w21_s0_slope_v103_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w21_s1_slope_v104_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w21_s2_slope_v105_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w63_s0_slope_v106_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w63_s1_slope_v107_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w63_s2_slope_v108_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w5_s0_slope_v109_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w5_s1_slope_v110_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w5_s2_slope_v111_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w21_s0_slope_v112_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w21_s1_slope_v113_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w21_s2_slope_v114_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w63_s0_slope_v115_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w63_s1_slope_v116_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w63_s2_slope_v117_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w5_s0_slope_v118_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w5_s1_slope_v119_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w5_s2_slope_v120_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w21_s0_slope_v121_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w21_s1_slope_v122_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w21_s2_slope_v123_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w63_s0_slope_v124_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w63_s1_slope_v125_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w63_s2_slope_v126_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w5_s0_slope_v127_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w5_s1_slope_v128_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w5_s2_slope_v129_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w21_s0_slope_v130_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w21_s1_slope_v131_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w21_s2_slope_v132_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w63_s0_slope_v133_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w63_s1_slope_v134_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w63_s2_slope_v135_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w5_s0_slope_v136_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w5_s1_slope_v137_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w5_s2_slope_v138_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w21_s0_slope_v139_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w21_s1_slope_v140_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w21_s2_slope_v141_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w63_s0_slope_v142_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w63_s1_slope_v143_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w63_s2_slope_v144_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w5_s0_slope_v145_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w5_s1_slope_v146_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w5_s2_slope_v147_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w21_s0_slope_v148_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w21_s1_slope_v149_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w21_s2_slope_v150_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w5_s0_slope_v001_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w5_s1_slope_v002_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w5_s2_slope_v003_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w21_s0_slope_v004_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w21_s1_slope_v005_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w21_s2_slope_v006_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w63_s0_slope_v007_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w63_s1_slope_v008_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_pct_w63_s2_slope_v009_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w5_s0_slope_v010_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w5_s1_slope_v011_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w5_s2_slope_v012_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w21_s0_slope_v013_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w21_s1_slope_v014_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w21_s2_slope_v015_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w63_s0_slope_v016_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w63_s1_slope_v017_signal,
    f07uef_f07_utility_efficiency_opexint_21d_slope_diff_norm_w63_s2_slope_v018_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w5_s0_slope_v019_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w5_s1_slope_v020_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w5_s2_slope_v021_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w21_s0_slope_v022_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w21_s1_slope_v023_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w21_s2_slope_v024_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w63_s0_slope_v025_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w63_s1_slope_v026_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_pct_w63_s2_slope_v027_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w5_s0_slope_v028_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w5_s1_slope_v029_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w5_s2_slope_v030_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w21_s0_slope_v031_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w21_s1_slope_v032_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w21_s2_slope_v033_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w63_s0_slope_v034_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w63_s1_slope_v035_signal,
    f07uef_f07_utility_efficiency_opexint_63d_slope_diff_norm_w63_s2_slope_v036_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w5_s0_slope_v037_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w5_s1_slope_v038_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w5_s2_slope_v039_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w21_s0_slope_v040_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w21_s1_slope_v041_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w21_s2_slope_v042_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w63_s0_slope_v043_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w63_s1_slope_v044_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_pct_w63_s2_slope_v045_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w5_s0_slope_v046_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w5_s1_slope_v047_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w5_s2_slope_v048_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w21_s0_slope_v049_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w21_s1_slope_v050_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w21_s2_slope_v051_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w63_s0_slope_v052_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w63_s1_slope_v053_signal,
    f07uef_f07_utility_efficiency_opexint_126d_slope_diff_norm_w63_s2_slope_v054_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w5_s0_slope_v055_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w5_s1_slope_v056_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w5_s2_slope_v057_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w21_s0_slope_v058_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w21_s1_slope_v059_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w21_s2_slope_v060_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w63_s0_slope_v061_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w63_s1_slope_v062_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_pct_w63_s2_slope_v063_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w5_s0_slope_v064_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w5_s1_slope_v065_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w5_s2_slope_v066_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w21_s0_slope_v067_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w21_s1_slope_v068_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w21_s2_slope_v069_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w63_s0_slope_v070_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w63_s1_slope_v071_signal,
    f07uef_f07_utility_efficiency_opexint_252d_slope_diff_norm_w63_s2_slope_v072_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w5_s0_slope_v073_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w5_s1_slope_v074_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w5_s2_slope_v075_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w21_s0_slope_v076_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w21_s1_slope_v077_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w21_s2_slope_v078_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w63_s0_slope_v079_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w63_s1_slope_v080_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_pct_w63_s2_slope_v081_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w5_s0_slope_v082_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w5_s1_slope_v083_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w5_s2_slope_v084_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w21_s0_slope_v085_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w21_s1_slope_v086_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w21_s2_slope_v087_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w63_s0_slope_v088_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w63_s1_slope_v089_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_slope_diff_norm_w63_s2_slope_v090_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w5_s0_slope_v091_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w5_s1_slope_v092_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w5_s2_slope_v093_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w21_s0_slope_v094_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w21_s1_slope_v095_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w21_s2_slope_v096_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w63_s0_slope_v097_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w63_s1_slope_v098_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_pct_w63_s2_slope_v099_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w5_s0_slope_v100_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w5_s1_slope_v101_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w5_s2_slope_v102_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w21_s0_slope_v103_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w21_s1_slope_v104_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w21_s2_slope_v105_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w63_s0_slope_v106_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w63_s1_slope_v107_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_slope_diff_norm_w63_s2_slope_v108_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w5_s0_slope_v109_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w5_s1_slope_v110_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w5_s2_slope_v111_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w21_s0_slope_v112_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w21_s1_slope_v113_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w21_s2_slope_v114_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w63_s0_slope_v115_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w63_s1_slope_v116_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_pct_w63_s2_slope_v117_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w5_s0_slope_v118_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w5_s1_slope_v119_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w5_s2_slope_v120_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w21_s0_slope_v121_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w21_s1_slope_v122_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w21_s2_slope_v123_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w63_s0_slope_v124_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w63_s1_slope_v125_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_slope_diff_norm_w63_s2_slope_v126_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w5_s0_slope_v127_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w5_s1_slope_v128_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w5_s2_slope_v129_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w21_s0_slope_v130_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w21_s1_slope_v131_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w21_s2_slope_v132_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w63_s0_slope_v133_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w63_s1_slope_v134_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_pct_w63_s2_slope_v135_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w5_s0_slope_v136_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w5_s1_slope_v137_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w5_s2_slope_v138_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w21_s0_slope_v139_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w21_s1_slope_v140_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w21_s2_slope_v141_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w63_s0_slope_v142_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w63_s1_slope_v143_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_slope_diff_norm_w63_s2_slope_v144_signal,
    f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w5_s0_slope_v145_signal,
    f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w5_s1_slope_v146_signal,
    f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w5_s2_slope_v147_signal,
    f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w21_s0_slope_v148_signal,
    f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w21_s1_slope_v149_signal,
    f07uef_f07_utility_efficiency_effsc_21d_slope_pct_w21_s2_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_UTILITY_EFFICIENCY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "sgna": sgna, "opex": opex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f07_opex_intensity", "_f07_efficiency_trend", "_f07_efficiency_score",)
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
    print(f"OK f07_utility_efficiency_2nd_derivatives_001_150_claude: {n_features} features pass")
