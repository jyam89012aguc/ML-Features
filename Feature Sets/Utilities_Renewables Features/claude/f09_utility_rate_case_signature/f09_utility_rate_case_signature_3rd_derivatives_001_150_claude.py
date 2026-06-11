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


def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w5_s0_jerk_v001_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w5_s1_jerk_v002_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w5_s2_jerk_v003_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w21_s0_jerk_v004_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w21_s1_jerk_v005_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w21_s2_jerk_v006_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w63_s0_jerk_v007_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w63_s1_jerk_v008_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w63_s2_jerk_v009_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w42_s0_jerk_v010_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w42_s1_jerk_v011_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w42_s2_jerk_v012_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w126_s0_jerk_v013_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w126_s1_jerk_v014_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w126_s2_jerk_v015_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 21)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w5_s0_jerk_v016_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w5_s1_jerk_v017_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w5_s2_jerk_v018_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w21_s0_jerk_v019_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w21_s1_jerk_v020_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w21_s2_jerk_v021_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w63_s0_jerk_v022_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w63_s1_jerk_v023_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w63_s2_jerk_v024_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w42_s0_jerk_v025_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w42_s1_jerk_v026_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w42_s2_jerk_v027_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w126_s0_jerk_v028_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w126_s1_jerk_v029_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w126_s2_jerk_v030_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 63)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w5_s0_jerk_v031_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w5_s1_jerk_v032_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w5_s2_jerk_v033_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w21_s0_jerk_v034_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w21_s1_jerk_v035_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w21_s2_jerk_v036_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w63_s0_jerk_v037_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w63_s1_jerk_v038_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w63_s2_jerk_v039_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w42_s0_jerk_v040_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w42_s1_jerk_v041_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w42_s2_jerk_v042_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w126_s0_jerk_v043_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w126_s1_jerk_v044_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w126_s2_jerk_v045_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 126)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w5_s0_jerk_v046_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w5_s1_jerk_v047_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w5_s2_jerk_v048_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w21_s0_jerk_v049_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w21_s1_jerk_v050_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w21_s2_jerk_v051_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w63_s0_jerk_v052_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w63_s1_jerk_v053_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w63_s2_jerk_v054_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w42_s0_jerk_v055_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w42_s1_jerk_v056_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w42_s2_jerk_v057_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w126_s0_jerk_v058_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w126_s1_jerk_v059_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w126_s2_jerk_v060_signal(ebitdamargin, closeadj):
    base = _f09_margin_floor(ebitdamargin, 252)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w5_s0_jerk_v061_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w5_s1_jerk_v062_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w5_s2_jerk_v063_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w21_s0_jerk_v064_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w21_s1_jerk_v065_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w21_s2_jerk_v066_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w63_s0_jerk_v067_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w63_s1_jerk_v068_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w63_s2_jerk_v069_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w42_s0_jerk_v070_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w42_s1_jerk_v071_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w42_s2_jerk_v072_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w126_s0_jerk_v073_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w126_s1_jerk_v074_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w126_s2_jerk_v075_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 21)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w5_s0_jerk_v076_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w5_s1_jerk_v077_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w5_s2_jerk_v078_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w21_s0_jerk_v079_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w21_s1_jerk_v080_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w21_s2_jerk_v081_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w63_s0_jerk_v082_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w63_s1_jerk_v083_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w63_s2_jerk_v084_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w42_s0_jerk_v085_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w42_s1_jerk_v086_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w42_s2_jerk_v087_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w126_s0_jerk_v088_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w126_s1_jerk_v089_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w126_s2_jerk_v090_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 63)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w5_s0_jerk_v091_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w5_s1_jerk_v092_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w5_s2_jerk_v093_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w21_s0_jerk_v094_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w21_s1_jerk_v095_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w21_s2_jerk_v096_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w63_s0_jerk_v097_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w63_s1_jerk_v098_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w63_s2_jerk_v099_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w42_s0_jerk_v100_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w42_s1_jerk_v101_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w42_s2_jerk_v102_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w126_s0_jerk_v103_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w126_s1_jerk_v104_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w126_s2_jerk_v105_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 126)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w5_s0_jerk_v106_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w5_s1_jerk_v107_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w5_s2_jerk_v108_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w21_s0_jerk_v109_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w21_s1_jerk_v110_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w21_s2_jerk_v111_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w63_s0_jerk_v112_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w63_s1_jerk_v113_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w63_s2_jerk_v114_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w42_s0_jerk_v115_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w42_s1_jerk_v116_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w42_s2_jerk_v117_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w126_s0_jerk_v118_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w126_s1_jerk_v119_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w126_s2_jerk_v120_signal(ebitdamargin, closeadj):
    base = _f09_margin_recovery(ebitdamargin, 252)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w5_s0_jerk_v121_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w5_s1_jerk_v122_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w5_s2_jerk_v123_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w21_s0_jerk_v124_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w21_s1_jerk_v125_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w21_s2_jerk_v126_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w63_s0_jerk_v127_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w63_s1_jerk_v128_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w63_s2_jerk_v129_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w42_s0_jerk_v130_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w42_s1_jerk_v131_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w42_s2_jerk_v132_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w126_s0_jerk_v133_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w126_s1_jerk_v134_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w126_s2_jerk_v135_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 21)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w5_s0_jerk_v136_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w5_s1_jerk_v137_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w5_s2_jerk_v138_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w21_s0_jerk_v139_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w21_s1_jerk_v140_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w21_s2_jerk_v141_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w63_s0_jerk_v142_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w63_s1_jerk_v143_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w63_s2_jerk_v144_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w42_s0_jerk_v145_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w42_s1_jerk_v146_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w42_s2_jerk_v147_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 42) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w126_s0_jerk_v148_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w126_s1_jerk_v149_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w126_s2_jerk_v150_signal(grossmargin, ebitdamargin, closeadj):
    base = _f09_margin_durability(grossmargin, ebitdamargin, 63)
    result = _jerk(base, 126) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w5_s0_jerk_v001_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w5_s1_jerk_v002_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w5_s2_jerk_v003_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w21_s0_jerk_v004_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w21_s1_jerk_v005_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w21_s2_jerk_v006_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w63_s0_jerk_v007_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w63_s1_jerk_v008_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w63_s2_jerk_v009_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w42_s0_jerk_v010_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w42_s1_jerk_v011_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w42_s2_jerk_v012_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w126_s0_jerk_v013_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w126_s1_jerk_v014_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_21d_jerk_w126_s2_jerk_v015_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w5_s0_jerk_v016_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w5_s1_jerk_v017_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w5_s2_jerk_v018_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w21_s0_jerk_v019_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w21_s1_jerk_v020_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w21_s2_jerk_v021_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w63_s0_jerk_v022_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w63_s1_jerk_v023_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w63_s2_jerk_v024_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w42_s0_jerk_v025_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w42_s1_jerk_v026_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w42_s2_jerk_v027_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w126_s0_jerk_v028_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w126_s1_jerk_v029_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_63d_jerk_w126_s2_jerk_v030_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w5_s0_jerk_v031_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w5_s1_jerk_v032_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w5_s2_jerk_v033_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w21_s0_jerk_v034_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w21_s1_jerk_v035_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w21_s2_jerk_v036_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w63_s0_jerk_v037_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w63_s1_jerk_v038_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w63_s2_jerk_v039_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w42_s0_jerk_v040_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w42_s1_jerk_v041_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w42_s2_jerk_v042_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w126_s0_jerk_v043_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w126_s1_jerk_v044_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_126d_jerk_w126_s2_jerk_v045_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w5_s0_jerk_v046_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w5_s1_jerk_v047_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w5_s2_jerk_v048_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w21_s0_jerk_v049_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w21_s1_jerk_v050_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w21_s2_jerk_v051_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w63_s0_jerk_v052_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w63_s1_jerk_v053_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w63_s2_jerk_v054_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w42_s0_jerk_v055_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w42_s1_jerk_v056_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w42_s2_jerk_v057_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w126_s0_jerk_v058_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w126_s1_jerk_v059_signal,
    f09urc_f09_utility_rate_case_signature_mfloor_252d_jerk_w126_s2_jerk_v060_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w5_s0_jerk_v061_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w5_s1_jerk_v062_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w5_s2_jerk_v063_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w21_s0_jerk_v064_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w21_s1_jerk_v065_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w21_s2_jerk_v066_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w63_s0_jerk_v067_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w63_s1_jerk_v068_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w63_s2_jerk_v069_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w42_s0_jerk_v070_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w42_s1_jerk_v071_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w42_s2_jerk_v072_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w126_s0_jerk_v073_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w126_s1_jerk_v074_signal,
    f09urc_f09_utility_rate_case_signature_mrec_21d_jerk_w126_s2_jerk_v075_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w5_s0_jerk_v076_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w5_s1_jerk_v077_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w5_s2_jerk_v078_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w21_s0_jerk_v079_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w21_s1_jerk_v080_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w21_s2_jerk_v081_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w63_s0_jerk_v082_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w63_s1_jerk_v083_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w63_s2_jerk_v084_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w42_s0_jerk_v085_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w42_s1_jerk_v086_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w42_s2_jerk_v087_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w126_s0_jerk_v088_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w126_s1_jerk_v089_signal,
    f09urc_f09_utility_rate_case_signature_mrec_63d_jerk_w126_s2_jerk_v090_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w5_s0_jerk_v091_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w5_s1_jerk_v092_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w5_s2_jerk_v093_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w21_s0_jerk_v094_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w21_s1_jerk_v095_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w21_s2_jerk_v096_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w63_s0_jerk_v097_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w63_s1_jerk_v098_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w63_s2_jerk_v099_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w42_s0_jerk_v100_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w42_s1_jerk_v101_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w42_s2_jerk_v102_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w126_s0_jerk_v103_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w126_s1_jerk_v104_signal,
    f09urc_f09_utility_rate_case_signature_mrec_126d_jerk_w126_s2_jerk_v105_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w5_s0_jerk_v106_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w5_s1_jerk_v107_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w5_s2_jerk_v108_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w21_s0_jerk_v109_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w21_s1_jerk_v110_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w21_s2_jerk_v111_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w63_s0_jerk_v112_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w63_s1_jerk_v113_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w63_s2_jerk_v114_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w42_s0_jerk_v115_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w42_s1_jerk_v116_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w42_s2_jerk_v117_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w126_s0_jerk_v118_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w126_s1_jerk_v119_signal,
    f09urc_f09_utility_rate_case_signature_mrec_252d_jerk_w126_s2_jerk_v120_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w5_s0_jerk_v121_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w5_s1_jerk_v122_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w5_s2_jerk_v123_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w21_s0_jerk_v124_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w21_s1_jerk_v125_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w21_s2_jerk_v126_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w63_s0_jerk_v127_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w63_s1_jerk_v128_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w63_s2_jerk_v129_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w42_s0_jerk_v130_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w42_s1_jerk_v131_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w42_s2_jerk_v132_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w126_s0_jerk_v133_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w126_s1_jerk_v134_signal,
    f09urc_f09_utility_rate_case_signature_mdur_21d_jerk_w126_s2_jerk_v135_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w5_s0_jerk_v136_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w5_s1_jerk_v137_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w5_s2_jerk_v138_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w21_s0_jerk_v139_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w21_s1_jerk_v140_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w21_s2_jerk_v141_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w63_s0_jerk_v142_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w63_s1_jerk_v143_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w63_s2_jerk_v144_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w42_s0_jerk_v145_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w42_s1_jerk_v146_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w42_s2_jerk_v147_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w126_s0_jerk_v148_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w126_s1_jerk_v149_signal,
    f09urc_f09_utility_rate_case_signature_mdur_63d_jerk_w126_s2_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_UTILITY_RATE_CASE_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


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
    print(f"OK f09_utility_rate_case_signature_3rd_derivatives_001_150_claude: {n_features} features pass")
