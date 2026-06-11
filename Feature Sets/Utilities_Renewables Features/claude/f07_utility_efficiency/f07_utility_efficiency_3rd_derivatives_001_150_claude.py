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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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


def f07uef_f07_utility_efficiency_opexint_21d_jerk_w5_s0_jerk_v001_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w5_s1_jerk_v002_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w5_s2_jerk_v003_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w21_s0_jerk_v004_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w21_s1_jerk_v005_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w21_s2_jerk_v006_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w63_s0_jerk_v007_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w63_s1_jerk_v008_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w63_s2_jerk_v009_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w42_s0_jerk_v010_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w42_s1_jerk_v011_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w42_s2_jerk_v012_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w126_s0_jerk_v013_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w126_s1_jerk_v014_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_21d_jerk_w126_s2_jerk_v015_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w5_s0_jerk_v016_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w5_s1_jerk_v017_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w5_s2_jerk_v018_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w21_s0_jerk_v019_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w21_s1_jerk_v020_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w21_s2_jerk_v021_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w63_s0_jerk_v022_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w63_s1_jerk_v023_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w63_s2_jerk_v024_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w42_s0_jerk_v025_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w42_s1_jerk_v026_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w42_s2_jerk_v027_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w126_s0_jerk_v028_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w126_s1_jerk_v029_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_63d_jerk_w126_s2_jerk_v030_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w5_s0_jerk_v031_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w5_s1_jerk_v032_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w5_s2_jerk_v033_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w21_s0_jerk_v034_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w21_s1_jerk_v035_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w21_s2_jerk_v036_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w63_s0_jerk_v037_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w63_s1_jerk_v038_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w63_s2_jerk_v039_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w42_s0_jerk_v040_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w42_s1_jerk_v041_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w42_s2_jerk_v042_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w126_s0_jerk_v043_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w126_s1_jerk_v044_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_126d_jerk_w126_s2_jerk_v045_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w5_s0_jerk_v046_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w5_s1_jerk_v047_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w5_s2_jerk_v048_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w21_s0_jerk_v049_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w21_s1_jerk_v050_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w21_s2_jerk_v051_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w63_s0_jerk_v052_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w63_s1_jerk_v053_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w63_s2_jerk_v054_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w42_s0_jerk_v055_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w42_s1_jerk_v056_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w42_s2_jerk_v057_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w126_s0_jerk_v058_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w126_s1_jerk_v059_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_opexint_252d_jerk_w126_s2_jerk_v060_signal(opex, revenue, closeadj):
    base = _f07_opex_intensity(opex, revenue)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w5_s0_jerk_v061_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w5_s1_jerk_v062_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w5_s2_jerk_v063_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w21_s0_jerk_v064_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w21_s1_jerk_v065_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w21_s2_jerk_v066_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w63_s0_jerk_v067_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w63_s1_jerk_v068_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w63_s2_jerk_v069_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w42_s0_jerk_v070_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w42_s1_jerk_v071_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w42_s2_jerk_v072_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w126_s0_jerk_v073_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w126_s1_jerk_v074_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_21d_jerk_w126_s2_jerk_v075_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 21)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w5_s0_jerk_v076_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w5_s1_jerk_v077_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w5_s2_jerk_v078_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w21_s0_jerk_v079_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w21_s1_jerk_v080_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w21_s2_jerk_v081_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w63_s0_jerk_v082_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w63_s1_jerk_v083_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w63_s2_jerk_v084_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w42_s0_jerk_v085_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w42_s1_jerk_v086_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w42_s2_jerk_v087_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w126_s0_jerk_v088_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w126_s1_jerk_v089_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_63d_jerk_w126_s2_jerk_v090_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 63)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w5_s0_jerk_v091_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w5_s1_jerk_v092_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w5_s2_jerk_v093_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w21_s0_jerk_v094_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w21_s1_jerk_v095_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w21_s2_jerk_v096_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w63_s0_jerk_v097_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w63_s1_jerk_v098_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w63_s2_jerk_v099_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w42_s0_jerk_v100_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w42_s1_jerk_v101_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w42_s2_jerk_v102_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w126_s0_jerk_v103_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w126_s1_jerk_v104_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_126d_jerk_w126_s2_jerk_v105_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 126)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w5_s0_jerk_v106_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w5_s1_jerk_v107_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w5_s2_jerk_v108_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w21_s0_jerk_v109_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w21_s1_jerk_v110_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w21_s2_jerk_v111_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w63_s0_jerk_v112_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w63_s1_jerk_v113_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w63_s2_jerk_v114_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w42_s0_jerk_v115_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w42_s1_jerk_v116_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w42_s2_jerk_v117_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w126_s0_jerk_v118_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w126_s1_jerk_v119_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_efftrend_252d_jerk_w126_s2_jerk_v120_signal(opex, revenue, closeadj):
    base = _f07_efficiency_trend(opex, revenue, 252)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w5_s0_jerk_v121_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w5_s1_jerk_v122_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w5_s2_jerk_v123_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w21_s0_jerk_v124_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w21_s1_jerk_v125_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w21_s2_jerk_v126_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w63_s0_jerk_v127_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w63_s1_jerk_v128_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w63_s2_jerk_v129_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w42_s0_jerk_v130_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w42_s1_jerk_v131_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w42_s2_jerk_v132_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w126_s0_jerk_v133_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w126_s1_jerk_v134_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_21d_jerk_w126_s2_jerk_v135_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 21)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w5_s0_jerk_v136_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w5_s1_jerk_v137_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w5_s2_jerk_v138_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w21_s0_jerk_v139_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w21_s1_jerk_v140_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w21_s2_jerk_v141_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w63_s0_jerk_v142_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w63_s1_jerk_v143_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w63_s2_jerk_v144_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w42_s0_jerk_v145_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w42_s1_jerk_v146_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w42_s2_jerk_v147_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w126_s0_jerk_v148_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w126_s1_jerk_v149_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f07uef_f07_utility_efficiency_effsc_63d_jerk_w126_s2_jerk_v150_signal(opex, sgna, revenue, closeadj):
    base = _f07_efficiency_score(opex, sgna, revenue, 63)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w5_s0_jerk_v001_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w5_s1_jerk_v002_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w5_s2_jerk_v003_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w21_s0_jerk_v004_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w21_s1_jerk_v005_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w21_s2_jerk_v006_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w63_s0_jerk_v007_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w63_s1_jerk_v008_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w63_s2_jerk_v009_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w42_s0_jerk_v010_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w42_s1_jerk_v011_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w42_s2_jerk_v012_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w126_s0_jerk_v013_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w126_s1_jerk_v014_signal,
    f07uef_f07_utility_efficiency_opexint_21d_jerk_w126_s2_jerk_v015_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w5_s0_jerk_v016_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w5_s1_jerk_v017_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w5_s2_jerk_v018_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w21_s0_jerk_v019_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w21_s1_jerk_v020_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w21_s2_jerk_v021_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w63_s0_jerk_v022_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w63_s1_jerk_v023_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w63_s2_jerk_v024_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w42_s0_jerk_v025_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w42_s1_jerk_v026_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w42_s2_jerk_v027_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w126_s0_jerk_v028_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w126_s1_jerk_v029_signal,
    f07uef_f07_utility_efficiency_opexint_63d_jerk_w126_s2_jerk_v030_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w5_s0_jerk_v031_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w5_s1_jerk_v032_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w5_s2_jerk_v033_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w21_s0_jerk_v034_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w21_s1_jerk_v035_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w21_s2_jerk_v036_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w63_s0_jerk_v037_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w63_s1_jerk_v038_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w63_s2_jerk_v039_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w42_s0_jerk_v040_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w42_s1_jerk_v041_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w42_s2_jerk_v042_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w126_s0_jerk_v043_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w126_s1_jerk_v044_signal,
    f07uef_f07_utility_efficiency_opexint_126d_jerk_w126_s2_jerk_v045_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w5_s0_jerk_v046_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w5_s1_jerk_v047_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w5_s2_jerk_v048_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w21_s0_jerk_v049_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w21_s1_jerk_v050_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w21_s2_jerk_v051_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w63_s0_jerk_v052_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w63_s1_jerk_v053_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w63_s2_jerk_v054_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w42_s0_jerk_v055_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w42_s1_jerk_v056_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w42_s2_jerk_v057_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w126_s0_jerk_v058_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w126_s1_jerk_v059_signal,
    f07uef_f07_utility_efficiency_opexint_252d_jerk_w126_s2_jerk_v060_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w5_s0_jerk_v061_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w5_s1_jerk_v062_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w5_s2_jerk_v063_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w21_s0_jerk_v064_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w21_s1_jerk_v065_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w21_s2_jerk_v066_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w63_s0_jerk_v067_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w63_s1_jerk_v068_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w63_s2_jerk_v069_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w42_s0_jerk_v070_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w42_s1_jerk_v071_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w42_s2_jerk_v072_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w126_s0_jerk_v073_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w126_s1_jerk_v074_signal,
    f07uef_f07_utility_efficiency_efftrend_21d_jerk_w126_s2_jerk_v075_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w5_s0_jerk_v076_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w5_s1_jerk_v077_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w5_s2_jerk_v078_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w21_s0_jerk_v079_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w21_s1_jerk_v080_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w21_s2_jerk_v081_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w63_s0_jerk_v082_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w63_s1_jerk_v083_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w63_s2_jerk_v084_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w42_s0_jerk_v085_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w42_s1_jerk_v086_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w42_s2_jerk_v087_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w126_s0_jerk_v088_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w126_s1_jerk_v089_signal,
    f07uef_f07_utility_efficiency_efftrend_63d_jerk_w126_s2_jerk_v090_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w5_s0_jerk_v091_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w5_s1_jerk_v092_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w5_s2_jerk_v093_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w21_s0_jerk_v094_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w21_s1_jerk_v095_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w21_s2_jerk_v096_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w63_s0_jerk_v097_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w63_s1_jerk_v098_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w63_s2_jerk_v099_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w42_s0_jerk_v100_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w42_s1_jerk_v101_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w42_s2_jerk_v102_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w126_s0_jerk_v103_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w126_s1_jerk_v104_signal,
    f07uef_f07_utility_efficiency_efftrend_126d_jerk_w126_s2_jerk_v105_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w5_s0_jerk_v106_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w5_s1_jerk_v107_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w5_s2_jerk_v108_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w21_s0_jerk_v109_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w21_s1_jerk_v110_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w21_s2_jerk_v111_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w63_s0_jerk_v112_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w63_s1_jerk_v113_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w63_s2_jerk_v114_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w42_s0_jerk_v115_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w42_s1_jerk_v116_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w42_s2_jerk_v117_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w126_s0_jerk_v118_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w126_s1_jerk_v119_signal,
    f07uef_f07_utility_efficiency_efftrend_252d_jerk_w126_s2_jerk_v120_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w5_s0_jerk_v121_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w5_s1_jerk_v122_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w5_s2_jerk_v123_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w21_s0_jerk_v124_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w21_s1_jerk_v125_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w21_s2_jerk_v126_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w63_s0_jerk_v127_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w63_s1_jerk_v128_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w63_s2_jerk_v129_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w42_s0_jerk_v130_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w42_s1_jerk_v131_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w42_s2_jerk_v132_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w126_s0_jerk_v133_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w126_s1_jerk_v134_signal,
    f07uef_f07_utility_efficiency_effsc_21d_jerk_w126_s2_jerk_v135_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w5_s0_jerk_v136_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w5_s1_jerk_v137_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w5_s2_jerk_v138_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w21_s0_jerk_v139_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w21_s1_jerk_v140_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w21_s2_jerk_v141_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w63_s0_jerk_v142_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w63_s1_jerk_v143_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w63_s2_jerk_v144_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w42_s0_jerk_v145_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w42_s1_jerk_v146_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w42_s2_jerk_v147_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w126_s0_jerk_v148_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w126_s1_jerk_v149_signal,
    f07uef_f07_utility_efficiency_effsc_63d_jerk_w126_s2_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_UTILITY_EFFICIENCY_REGISTRY_JERK_001_150 = REGISTRY


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
    print(f"OK f07_utility_efficiency_3rd_derivatives_001_150_claude: {n_features} features pass")
