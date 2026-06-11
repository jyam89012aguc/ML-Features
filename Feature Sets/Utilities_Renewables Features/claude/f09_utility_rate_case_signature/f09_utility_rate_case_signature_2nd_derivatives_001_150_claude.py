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
def _f09_margin_floor(ebitdamargin, w):
    return ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f09_margin_recovery(ebitdamargin, w):
    # current vs rolling min — how far margin recovered from trough
    trough = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - trough


def _f09_margin_durability(grossmargin, ebitdamargin, w):
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    gm_std = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    em_std = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm + em) - (gm_std + em_std)


def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w5_s0_slope_v001_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w5_s1_slope_v002_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w5_s2_slope_v003_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w21_s0_slope_v004_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w21_s1_slope_v005_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w21_s2_slope_v006_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w63_s0_slope_v007_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w63_s1_slope_v008_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w63_s2_slope_v009_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w5_s0_slope_v010_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w5_s1_slope_v011_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w5_s2_slope_v012_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w21_s0_slope_v013_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w21_s1_slope_v014_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w21_s2_slope_v015_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w63_s0_slope_v016_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w63_s1_slope_v017_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w63_s2_slope_v018_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w5_s0_slope_v019_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w5_s1_slope_v020_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w5_s2_slope_v021_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w21_s0_slope_v022_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w21_s1_slope_v023_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w21_s2_slope_v024_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w63_s0_slope_v025_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w63_s1_slope_v026_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w63_s2_slope_v027_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w5_s0_slope_v028_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w5_s1_slope_v029_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w5_s2_slope_v030_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w21_s0_slope_v031_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w21_s1_slope_v032_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w21_s2_slope_v033_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w63_s0_slope_v034_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w63_s1_slope_v035_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w63_s2_slope_v036_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w5_s0_slope_v037_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w5_s1_slope_v038_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w5_s2_slope_v039_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w21_s0_slope_v040_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w21_s1_slope_v041_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w21_s2_slope_v042_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w63_s0_slope_v043_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w63_s1_slope_v044_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w63_s2_slope_v045_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w5_s0_slope_v046_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w5_s1_slope_v047_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w5_s2_slope_v048_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w21_s0_slope_v049_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w21_s1_slope_v050_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w21_s2_slope_v051_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w63_s0_slope_v052_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w63_s1_slope_v053_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w63_s2_slope_v054_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w5_s0_slope_v055_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w5_s1_slope_v056_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w5_s2_slope_v057_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w21_s0_slope_v058_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w21_s1_slope_v059_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w21_s2_slope_v060_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w63_s0_slope_v061_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w63_s1_slope_v062_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w63_s2_slope_v063_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w5_s0_slope_v064_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w5_s1_slope_v065_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w5_s2_slope_v066_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w21_s0_slope_v067_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w21_s1_slope_v068_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w21_s2_slope_v069_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w63_s0_slope_v070_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w63_s1_slope_v071_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w63_s2_slope_v072_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w5_s0_slope_v073_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w5_s1_slope_v074_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w5_s2_slope_v075_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w21_s0_slope_v076_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w21_s1_slope_v077_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w21_s2_slope_v078_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w63_s0_slope_v079_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w63_s1_slope_v080_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w63_s2_slope_v081_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w5_s0_slope_v082_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w5_s1_slope_v083_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w5_s2_slope_v084_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w21_s0_slope_v085_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w21_s1_slope_v086_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w21_s2_slope_v087_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w63_s0_slope_v088_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w63_s1_slope_v089_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w63_s2_slope_v090_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w5_s0_slope_v091_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w5_s1_slope_v092_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w5_s2_slope_v093_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w21_s0_slope_v094_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w21_s1_slope_v095_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w21_s2_slope_v096_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w63_s0_slope_v097_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w63_s1_slope_v098_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w63_s2_slope_v099_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w5_s0_slope_v100_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w5_s1_slope_v101_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w5_s2_slope_v102_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w21_s0_slope_v103_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w21_s1_slope_v104_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w21_s2_slope_v105_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w63_s0_slope_v106_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w63_s1_slope_v107_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w63_s2_slope_v108_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w5_s0_slope_v109_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w5_s1_slope_v110_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w5_s2_slope_v111_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w21_s0_slope_v112_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w21_s1_slope_v113_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w21_s2_slope_v114_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w63_s0_slope_v115_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w63_s1_slope_v116_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w63_s2_slope_v117_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w5_s0_slope_v118_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w5_s1_slope_v119_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w5_s2_slope_v120_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w21_s0_slope_v121_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w21_s1_slope_v122_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w21_s2_slope_v123_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w63_s0_slope_v124_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w63_s1_slope_v125_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w63_s2_slope_v126_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w5_s0_slope_v127_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w5_s1_slope_v128_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w5_s2_slope_v129_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w21_s0_slope_v130_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w21_s1_slope_v131_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w21_s2_slope_v132_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w63_s0_slope_v133_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w63_s1_slope_v134_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w63_s2_slope_v135_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w5_s0_slope_v136_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w5_s1_slope_v137_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w5_s2_slope_v138_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w21_s0_slope_v139_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w21_s1_slope_v140_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w21_s2_slope_v141_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w63_s0_slope_v142_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w63_s1_slope_v143_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w63_s2_slope_v144_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w5_s0_slope_v145_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w5_s1_slope_v146_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w5_s2_slope_v147_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w21_s0_slope_v148_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w21_s1_slope_v149_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w21_s2_slope_v150_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w5_s0_slope_v001_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w5_s1_slope_v002_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w5_s2_slope_v003_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w21_s0_slope_v004_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w21_s1_slope_v005_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w21_s2_slope_v006_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w63_s0_slope_v007_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w63_s1_slope_v008_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_pct_w63_s2_slope_v009_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w5_s0_slope_v010_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w5_s1_slope_v011_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w5_s2_slope_v012_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w21_s0_slope_v013_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w21_s1_slope_v014_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w21_s2_slope_v015_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w63_s0_slope_v016_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w63_s1_slope_v017_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_slope_diff_norm_w63_s2_slope_v018_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w5_s0_slope_v019_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w5_s1_slope_v020_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w5_s2_slope_v021_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w21_s0_slope_v022_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w21_s1_slope_v023_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w21_s2_slope_v024_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w63_s0_slope_v025_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w63_s1_slope_v026_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_pct_w63_s2_slope_v027_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w5_s0_slope_v028_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w5_s1_slope_v029_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w5_s2_slope_v030_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w21_s0_slope_v031_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w21_s1_slope_v032_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w21_s2_slope_v033_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w63_s0_slope_v034_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w63_s1_slope_v035_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_slope_diff_norm_w63_s2_slope_v036_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w5_s0_slope_v037_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w5_s1_slope_v038_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w5_s2_slope_v039_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w21_s0_slope_v040_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w21_s1_slope_v041_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w21_s2_slope_v042_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w63_s0_slope_v043_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w63_s1_slope_v044_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_pct_w63_s2_slope_v045_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w5_s0_slope_v046_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w5_s1_slope_v047_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w5_s2_slope_v048_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w21_s0_slope_v049_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w21_s1_slope_v050_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w21_s2_slope_v051_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w63_s0_slope_v052_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w63_s1_slope_v053_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_slope_diff_norm_w63_s2_slope_v054_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w5_s0_slope_v055_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w5_s1_slope_v056_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w5_s2_slope_v057_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w21_s0_slope_v058_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w21_s1_slope_v059_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w21_s2_slope_v060_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w63_s0_slope_v061_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w63_s1_slope_v062_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_pct_w63_s2_slope_v063_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w5_s0_slope_v064_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w5_s1_slope_v065_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w5_s2_slope_v066_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w21_s0_slope_v067_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w21_s1_slope_v068_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w21_s2_slope_v069_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w63_s0_slope_v070_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w63_s1_slope_v071_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_slope_diff_norm_w63_s2_slope_v072_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w5_s0_slope_v073_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w5_s1_slope_v074_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w5_s2_slope_v075_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w21_s0_slope_v076_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w21_s1_slope_v077_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w21_s2_slope_v078_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w63_s0_slope_v079_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w63_s1_slope_v080_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_pct_w63_s2_slope_v081_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w5_s0_slope_v082_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w5_s1_slope_v083_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w5_s2_slope_v084_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w21_s0_slope_v085_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w21_s1_slope_v086_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w21_s2_slope_v087_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w63_s0_slope_v088_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w63_s1_slope_v089_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_slope_diff_norm_w63_s2_slope_v090_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w5_s0_slope_v091_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w5_s1_slope_v092_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w5_s2_slope_v093_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w21_s0_slope_v094_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w21_s1_slope_v095_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w21_s2_slope_v096_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w63_s0_slope_v097_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w63_s1_slope_v098_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_pct_w63_s2_slope_v099_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w5_s0_slope_v100_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w5_s1_slope_v101_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w5_s2_slope_v102_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w21_s0_slope_v103_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w21_s1_slope_v104_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w21_s2_slope_v105_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w63_s0_slope_v106_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w63_s1_slope_v107_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_slope_diff_norm_w63_s2_slope_v108_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w5_s0_slope_v109_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w5_s1_slope_v110_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w5_s2_slope_v111_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w21_s0_slope_v112_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w21_s1_slope_v113_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w21_s2_slope_v114_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w63_s0_slope_v115_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w63_s1_slope_v116_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_pct_w63_s2_slope_v117_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w5_s0_slope_v118_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w5_s1_slope_v119_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w5_s2_slope_v120_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w21_s0_slope_v121_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w21_s1_slope_v122_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w21_s2_slope_v123_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w63_s0_slope_v124_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w63_s1_slope_v125_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_slope_diff_norm_w63_s2_slope_v126_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w5_s0_slope_v127_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w5_s1_slope_v128_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w5_s2_slope_v129_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w21_s0_slope_v130_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w21_s1_slope_v131_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w21_s2_slope_v132_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w63_s0_slope_v133_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w63_s1_slope_v134_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_pct_w63_s2_slope_v135_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w5_s0_slope_v136_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w5_s1_slope_v137_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w5_s2_slope_v138_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w21_s0_slope_v139_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w21_s1_slope_v140_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w21_s2_slope_v141_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w63_s0_slope_v142_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w63_s1_slope_v143_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_slope_diff_norm_w63_s2_slope_v144_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w5_s0_slope_v145_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w5_s1_slope_v146_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w5_s2_slope_v147_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w21_s0_slope_v148_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w21_s1_slope_v149_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_slope_pct_w21_s2_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_UTILITY_RATE_CASE_SIGNATURE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "grossmargin": grossmargin,
        "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_margin_floor", "_f09_margin_recovery", "_f09_margin_durability",)
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
    print(f"OK f09_utility_rate_case_signature_2nd_derivatives_001_150_claude: {n_features} features pass")
