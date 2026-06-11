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
def _f08_payout_floor(payoutratio, w):
    # rolling min as durability floor
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).min()


def _f08_payout_durability(payoutratio, eps, w):
    # stable payoutratio when eps grows; penalize when eps falls
    eg = eps.pct_change(w).fillna(0)
    p_smooth = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    return p_smooth * (1.0 + eg)


def _f08_payout_sustainability(payoutratio, fcfps, w):
    # payout vs fcfps coverage
    p_smooth = payoutratio.rolling(w, min_periods=max(1, w // 2)).mean()
    cov = fcfps.rolling(w, min_periods=max(1, w // 2)).mean() / fcfps.rolling(w, min_periods=max(1, w // 2)).mean().abs().replace(0, np.nan)
    return p_smooth - cov.abs()


def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w5_s0_slope_v001_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w5_s1_slope_v002_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w5_s2_slope_v003_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w21_s0_slope_v004_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w21_s1_slope_v005_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w21_s2_slope_v006_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w63_s0_slope_v007_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w63_s1_slope_v008_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w63_s2_slope_v009_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w5_s0_slope_v010_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w5_s1_slope_v011_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w5_s2_slope_v012_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w21_s0_slope_v013_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w21_s1_slope_v014_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w21_s2_slope_v015_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w63_s0_slope_v016_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w63_s1_slope_v017_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w63_s2_slope_v018_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w5_s0_slope_v019_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w5_s1_slope_v020_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w5_s2_slope_v021_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w21_s0_slope_v022_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w21_s1_slope_v023_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w21_s2_slope_v024_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w63_s0_slope_v025_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w63_s1_slope_v026_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w63_s2_slope_v027_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w5_s0_slope_v028_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w5_s1_slope_v029_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w5_s2_slope_v030_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w21_s0_slope_v031_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w21_s1_slope_v032_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w21_s2_slope_v033_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w63_s0_slope_v034_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w63_s1_slope_v035_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w63_s2_slope_v036_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w5_s0_slope_v037_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w5_s1_slope_v038_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w5_s2_slope_v039_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w21_s0_slope_v040_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w21_s1_slope_v041_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w21_s2_slope_v042_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w63_s0_slope_v043_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w63_s1_slope_v044_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w63_s2_slope_v045_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w5_s0_slope_v046_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w5_s1_slope_v047_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w5_s2_slope_v048_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w21_s0_slope_v049_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w21_s1_slope_v050_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w21_s2_slope_v051_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w63_s0_slope_v052_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w63_s1_slope_v053_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w63_s2_slope_v054_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w5_s0_slope_v055_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w5_s1_slope_v056_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w5_s2_slope_v057_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w21_s0_slope_v058_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w21_s1_slope_v059_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w21_s2_slope_v060_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w63_s0_slope_v061_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w63_s1_slope_v062_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w63_s2_slope_v063_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w5_s0_slope_v064_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w5_s1_slope_v065_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w5_s2_slope_v066_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w21_s0_slope_v067_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w21_s1_slope_v068_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w21_s2_slope_v069_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w63_s0_slope_v070_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w63_s1_slope_v071_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w63_s2_slope_v072_signal(payoutratio, closeadj):
    base = _f08_payout_floor(payoutratio, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w5_s0_slope_v073_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w5_s1_slope_v074_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w5_s2_slope_v075_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w21_s0_slope_v076_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w21_s1_slope_v077_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w21_s2_slope_v078_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w63_s0_slope_v079_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w63_s1_slope_v080_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w63_s2_slope_v081_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w5_s0_slope_v082_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w5_s1_slope_v083_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w5_s2_slope_v084_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w21_s0_slope_v085_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w21_s1_slope_v086_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w21_s2_slope_v087_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w63_s0_slope_v088_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w63_s1_slope_v089_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w63_s2_slope_v090_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w5_s0_slope_v091_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w5_s1_slope_v092_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w5_s2_slope_v093_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w21_s0_slope_v094_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w21_s1_slope_v095_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w21_s2_slope_v096_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w63_s0_slope_v097_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w63_s1_slope_v098_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w63_s2_slope_v099_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w5_s0_slope_v100_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w5_s1_slope_v101_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w5_s2_slope_v102_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w21_s0_slope_v103_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w21_s1_slope_v104_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w21_s2_slope_v105_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w63_s0_slope_v106_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w63_s1_slope_v107_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w63_s2_slope_v108_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w5_s0_slope_v109_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w5_s1_slope_v110_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w5_s2_slope_v111_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w21_s0_slope_v112_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w21_s1_slope_v113_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w21_s2_slope_v114_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w63_s0_slope_v115_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w63_s1_slope_v116_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w63_s2_slope_v117_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w5_s0_slope_v118_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w5_s1_slope_v119_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w5_s2_slope_v120_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w21_s0_slope_v121_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w21_s1_slope_v122_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w21_s2_slope_v123_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w63_s0_slope_v124_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w63_s1_slope_v125_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w63_s2_slope_v126_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w5_s0_slope_v127_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w5_s1_slope_v128_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w5_s2_slope_v129_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w21_s0_slope_v130_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w21_s1_slope_v131_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w21_s2_slope_v132_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w63_s0_slope_v133_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w63_s1_slope_v134_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w63_s2_slope_v135_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w5_s0_slope_v136_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w5_s1_slope_v137_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w5_s2_slope_v138_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w21_s0_slope_v139_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w21_s1_slope_v140_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w21_s2_slope_v141_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w63_s0_slope_v142_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w63_s1_slope_v143_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w63_s2_slope_v144_signal(payoutratio, eps, closeadj):
    base = _f08_payout_durability(payoutratio, eps, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w5_s0_slope_v145_signal(payoutratio, fcfps, closeadj):
    base = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w5_s1_slope_v146_signal(payoutratio, fcfps, closeadj):
    base = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w5_s2_slope_v147_signal(payoutratio, fcfps, closeadj):
    base = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w21_s0_slope_v148_signal(payoutratio, fcfps, closeadj):
    base = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w21_s1_slope_v149_signal(payoutratio, fcfps, closeadj):
    base = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w21_s2_slope_v150_signal(payoutratio, fcfps, closeadj):
    base = _f08_payout_sustainability(payoutratio, fcfps, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w5_s0_slope_v001_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w5_s1_slope_v002_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w5_s2_slope_v003_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w21_s0_slope_v004_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w21_s1_slope_v005_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w21_s2_slope_v006_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w63_s0_slope_v007_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w63_s1_slope_v008_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_pct_w63_s2_slope_v009_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w5_s0_slope_v010_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w5_s1_slope_v011_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w5_s2_slope_v012_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w21_s0_slope_v013_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w21_s1_slope_v014_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w21_s2_slope_v015_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w63_s0_slope_v016_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w63_s1_slope_v017_signal,
    f08upd_f08_utility_payout_durability_pfloor_21d_slope_diff_norm_w63_s2_slope_v018_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w5_s0_slope_v019_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w5_s1_slope_v020_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w5_s2_slope_v021_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w21_s0_slope_v022_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w21_s1_slope_v023_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w21_s2_slope_v024_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w63_s0_slope_v025_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w63_s1_slope_v026_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_pct_w63_s2_slope_v027_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w5_s0_slope_v028_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w5_s1_slope_v029_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w5_s2_slope_v030_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w21_s0_slope_v031_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w21_s1_slope_v032_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w21_s2_slope_v033_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w63_s0_slope_v034_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w63_s1_slope_v035_signal,
    f08upd_f08_utility_payout_durability_pfloor_63d_slope_diff_norm_w63_s2_slope_v036_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w5_s0_slope_v037_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w5_s1_slope_v038_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w5_s2_slope_v039_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w21_s0_slope_v040_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w21_s1_slope_v041_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w21_s2_slope_v042_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w63_s0_slope_v043_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w63_s1_slope_v044_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_pct_w63_s2_slope_v045_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w5_s0_slope_v046_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w5_s1_slope_v047_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w5_s2_slope_v048_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w21_s0_slope_v049_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w21_s1_slope_v050_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w21_s2_slope_v051_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w63_s0_slope_v052_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w63_s1_slope_v053_signal,
    f08upd_f08_utility_payout_durability_pfloor_126d_slope_diff_norm_w63_s2_slope_v054_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w5_s0_slope_v055_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w5_s1_slope_v056_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w5_s2_slope_v057_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w21_s0_slope_v058_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w21_s1_slope_v059_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w21_s2_slope_v060_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w63_s0_slope_v061_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w63_s1_slope_v062_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_pct_w63_s2_slope_v063_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w5_s0_slope_v064_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w5_s1_slope_v065_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w5_s2_slope_v066_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w21_s0_slope_v067_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w21_s1_slope_v068_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w21_s2_slope_v069_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w63_s0_slope_v070_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w63_s1_slope_v071_signal,
    f08upd_f08_utility_payout_durability_pfloor_252d_slope_diff_norm_w63_s2_slope_v072_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w5_s0_slope_v073_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w5_s1_slope_v074_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w5_s2_slope_v075_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w21_s0_slope_v076_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w21_s1_slope_v077_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w21_s2_slope_v078_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w63_s0_slope_v079_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w63_s1_slope_v080_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_pct_w63_s2_slope_v081_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w5_s0_slope_v082_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w5_s1_slope_v083_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w5_s2_slope_v084_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w21_s0_slope_v085_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w21_s1_slope_v086_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w21_s2_slope_v087_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w63_s0_slope_v088_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w63_s1_slope_v089_signal,
    f08upd_f08_utility_payout_durability_pdur_21d_slope_diff_norm_w63_s2_slope_v090_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w5_s0_slope_v091_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w5_s1_slope_v092_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w5_s2_slope_v093_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w21_s0_slope_v094_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w21_s1_slope_v095_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w21_s2_slope_v096_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w63_s0_slope_v097_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w63_s1_slope_v098_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_pct_w63_s2_slope_v099_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w5_s0_slope_v100_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w5_s1_slope_v101_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w5_s2_slope_v102_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w21_s0_slope_v103_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w21_s1_slope_v104_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w21_s2_slope_v105_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w63_s0_slope_v106_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w63_s1_slope_v107_signal,
    f08upd_f08_utility_payout_durability_pdur_63d_slope_diff_norm_w63_s2_slope_v108_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w5_s0_slope_v109_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w5_s1_slope_v110_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w5_s2_slope_v111_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w21_s0_slope_v112_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w21_s1_slope_v113_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w21_s2_slope_v114_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w63_s0_slope_v115_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w63_s1_slope_v116_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_pct_w63_s2_slope_v117_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w5_s0_slope_v118_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w5_s1_slope_v119_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w5_s2_slope_v120_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w21_s0_slope_v121_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w21_s1_slope_v122_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w21_s2_slope_v123_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w63_s0_slope_v124_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w63_s1_slope_v125_signal,
    f08upd_f08_utility_payout_durability_pdur_126d_slope_diff_norm_w63_s2_slope_v126_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w5_s0_slope_v127_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w5_s1_slope_v128_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w5_s2_slope_v129_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w21_s0_slope_v130_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w21_s1_slope_v131_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w21_s2_slope_v132_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w63_s0_slope_v133_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w63_s1_slope_v134_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_pct_w63_s2_slope_v135_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w5_s0_slope_v136_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w5_s1_slope_v137_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w5_s2_slope_v138_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w21_s0_slope_v139_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w21_s1_slope_v140_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w21_s2_slope_v141_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w63_s0_slope_v142_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w63_s1_slope_v143_signal,
    f08upd_f08_utility_payout_durability_pdur_252d_slope_diff_norm_w63_s2_slope_v144_signal,
    f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w5_s0_slope_v145_signal,
    f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w5_s1_slope_v146_signal,
    f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w5_s2_slope_v147_signal,
    f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w21_s0_slope_v148_signal,
    f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w21_s1_slope_v149_signal,
    f08upd_f08_utility_payout_durability_psus_21d_slope_pct_w21_s2_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_UTILITY_PAYOUT_DURABILITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    eps = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    fcfps = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")

    cols = {
        "closeadj": closeadj, "eps": eps, "fcfps": fcfps, "dps": dps,
        "payoutratio": payoutratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_payout_floor", "_f08_payout_durability", "_f08_payout_sustainability",)
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
    print(f"OK f08_utility_payout_durability_2nd_derivatives_001_150_claude: {n_features} features pass")
