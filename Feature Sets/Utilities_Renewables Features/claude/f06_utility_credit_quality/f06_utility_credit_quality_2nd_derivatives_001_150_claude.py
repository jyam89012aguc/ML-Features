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
def _f06_debt_ebitda(debt, ebitda):
    return debt / ebitda.replace(0, np.nan)


def _f06_credit_quality(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return -lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_solvency_score(debt, ebitda, fcf, w):
    de_ratio = debt / ebitda.replace(0, np.nan)
    fcf_cov = fcf / debt.replace(0, np.nan)
    de_smooth = de_ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    fcf_smooth = fcf_cov.rolling(w, min_periods=max(1, w // 2)).mean()
    return fcf_smooth - de_smooth


def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w5_s0_slope_v001_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w5_s1_slope_v002_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w5_s2_slope_v003_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w21_s0_slope_v004_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w21_s1_slope_v005_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w21_s2_slope_v006_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w63_s0_slope_v007_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w63_s1_slope_v008_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w63_s2_slope_v009_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w5_s0_slope_v010_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w5_s1_slope_v011_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w5_s2_slope_v012_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w21_s0_slope_v013_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w21_s1_slope_v014_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w21_s2_slope_v015_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w63_s0_slope_v016_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w63_s1_slope_v017_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w63_s2_slope_v018_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(21, min_periods=max(1, 21//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w5_s0_slope_v019_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w5_s1_slope_v020_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w5_s2_slope_v021_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w21_s0_slope_v022_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w21_s1_slope_v023_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w21_s2_slope_v024_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w63_s0_slope_v025_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w63_s1_slope_v026_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w63_s2_slope_v027_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w5_s0_slope_v028_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w5_s1_slope_v029_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w5_s2_slope_v030_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w21_s0_slope_v031_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w21_s1_slope_v032_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w21_s2_slope_v033_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w63_s0_slope_v034_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w63_s1_slope_v035_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w63_s2_slope_v036_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(63, min_periods=max(1, 63//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w5_s0_slope_v037_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w5_s1_slope_v038_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w5_s2_slope_v039_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w21_s0_slope_v040_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w21_s1_slope_v041_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w21_s2_slope_v042_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w63_s0_slope_v043_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w63_s1_slope_v044_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w63_s2_slope_v045_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w5_s0_slope_v046_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w5_s1_slope_v047_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w5_s2_slope_v048_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w21_s0_slope_v049_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w21_s1_slope_v050_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w21_s2_slope_v051_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w63_s0_slope_v052_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w63_s1_slope_v053_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w63_s2_slope_v054_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(126, min_periods=max(1, 126//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w5_s0_slope_v055_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w5_s1_slope_v056_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w5_s2_slope_v057_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w21_s0_slope_v058_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w21_s1_slope_v059_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w21_s2_slope_v060_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w63_s0_slope_v061_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w63_s1_slope_v062_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w63_s2_slope_v063_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w5_s0_slope_v064_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w5_s1_slope_v065_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w5_s2_slope_v066_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w21_s0_slope_v067_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w21_s1_slope_v068_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w21_s2_slope_v069_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w63_s0_slope_v070_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w63_s1_slope_v071_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w63_s2_slope_v072_signal(debt, ebitda, closeadj):
    base = _f06_debt_ebitda(debt, ebitda)
    base = base.rolling(252, min_periods=max(1, 252//2)).mean()
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w5_s0_slope_v073_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w5_s1_slope_v074_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w5_s2_slope_v075_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w21_s0_slope_v076_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w21_s1_slope_v077_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w21_s2_slope_v078_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w63_s0_slope_v079_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w63_s1_slope_v080_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w63_s2_slope_v081_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w5_s0_slope_v082_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w5_s1_slope_v083_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w5_s2_slope_v084_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w21_s0_slope_v085_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w21_s1_slope_v086_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w21_s2_slope_v087_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w63_s0_slope_v088_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w63_s1_slope_v089_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w63_s2_slope_v090_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 21)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w5_s0_slope_v091_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w5_s1_slope_v092_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w5_s2_slope_v093_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w21_s0_slope_v094_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w21_s1_slope_v095_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w21_s2_slope_v096_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w63_s0_slope_v097_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w63_s1_slope_v098_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w63_s2_slope_v099_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w5_s0_slope_v100_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w5_s1_slope_v101_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w5_s2_slope_v102_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w21_s0_slope_v103_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w21_s1_slope_v104_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w21_s2_slope_v105_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w63_s0_slope_v106_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w63_s1_slope_v107_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w63_s2_slope_v108_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 63)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w5_s0_slope_v109_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w5_s1_slope_v110_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w5_s2_slope_v111_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w21_s0_slope_v112_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w21_s1_slope_v113_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w21_s2_slope_v114_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w63_s0_slope_v115_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w63_s1_slope_v116_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w63_s2_slope_v117_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w5_s0_slope_v118_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w5_s1_slope_v119_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w5_s2_slope_v120_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w21_s0_slope_v121_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w21_s1_slope_v122_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w21_s2_slope_v123_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w63_s0_slope_v124_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w63_s1_slope_v125_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w63_s2_slope_v126_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 126)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w5_s0_slope_v127_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w5_s1_slope_v128_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w5_s2_slope_v129_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w21_s0_slope_v130_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w21_s1_slope_v131_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w21_s2_slope_v132_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w63_s0_slope_v133_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w63_s1_slope_v134_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w63_s2_slope_v135_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_pct(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w5_s0_slope_v136_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w5_s1_slope_v137_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w5_s2_slope_v138_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w21_s0_slope_v139_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w21_s1_slope_v140_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w21_s2_slope_v141_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w63_s0_slope_v142_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w63_s1_slope_v143_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w63_s2_slope_v144_signal(debt, equity, closeadj):
    base = _f06_credit_quality(debt, equity, 252)
    result = _slope_diff_norm(base, 63) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w5_s0_slope_v145_signal(debt, ebitda, fcf, closeadj):
    base = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w5_s1_slope_v146_signal(debt, ebitda, fcf, closeadj):
    base = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = _slope_pct(base, 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w5_s2_slope_v147_signal(debt, ebitda, fcf, closeadj):
    base = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = _slope_pct(base, 5) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w21_s0_slope_v148_signal(debt, ebitda, fcf, closeadj):
    base = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w21_s1_slope_v149_signal(debt, ebitda, fcf, closeadj):
    base = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = _slope_pct(base, 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w21_s2_slope_v150_signal(debt, ebitda, fcf, closeadj):
    base = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = _slope_pct(base, 21) * ((1.0 + (closeadj / closeadj.shift(63) - 1.0).fillna(0)) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w5_s0_slope_v001_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w5_s1_slope_v002_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w5_s2_slope_v003_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w21_s0_slope_v004_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w21_s1_slope_v005_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w21_s2_slope_v006_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w63_s0_slope_v007_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w63_s1_slope_v008_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_pct_w63_s2_slope_v009_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w5_s0_slope_v010_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w5_s1_slope_v011_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w5_s2_slope_v012_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w21_s0_slope_v013_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w21_s1_slope_v014_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w21_s2_slope_v015_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w63_s0_slope_v016_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w63_s1_slope_v017_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_slope_diff_norm_w63_s2_slope_v018_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w5_s0_slope_v019_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w5_s1_slope_v020_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w5_s2_slope_v021_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w21_s0_slope_v022_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w21_s1_slope_v023_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w21_s2_slope_v024_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w63_s0_slope_v025_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w63_s1_slope_v026_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_pct_w63_s2_slope_v027_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w5_s0_slope_v028_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w5_s1_slope_v029_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w5_s2_slope_v030_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w21_s0_slope_v031_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w21_s1_slope_v032_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w21_s2_slope_v033_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w63_s0_slope_v034_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w63_s1_slope_v035_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_slope_diff_norm_w63_s2_slope_v036_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w5_s0_slope_v037_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w5_s1_slope_v038_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w5_s2_slope_v039_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w21_s0_slope_v040_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w21_s1_slope_v041_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w21_s2_slope_v042_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w63_s0_slope_v043_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w63_s1_slope_v044_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_pct_w63_s2_slope_v045_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w5_s0_slope_v046_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w5_s1_slope_v047_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w5_s2_slope_v048_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w21_s0_slope_v049_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w21_s1_slope_v050_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w21_s2_slope_v051_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w63_s0_slope_v052_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w63_s1_slope_v053_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_126d_slope_diff_norm_w63_s2_slope_v054_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w5_s0_slope_v055_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w5_s1_slope_v056_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w5_s2_slope_v057_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w21_s0_slope_v058_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w21_s1_slope_v059_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w21_s2_slope_v060_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w63_s0_slope_v061_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w63_s1_slope_v062_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_pct_w63_s2_slope_v063_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w5_s0_slope_v064_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w5_s1_slope_v065_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w5_s2_slope_v066_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w21_s0_slope_v067_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w21_s1_slope_v068_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w21_s2_slope_v069_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w63_s0_slope_v070_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w63_s1_slope_v071_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_slope_diff_norm_w63_s2_slope_v072_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w5_s0_slope_v073_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w5_s1_slope_v074_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w5_s2_slope_v075_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w21_s0_slope_v076_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w21_s1_slope_v077_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w21_s2_slope_v078_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w63_s0_slope_v079_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w63_s1_slope_v080_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_pct_w63_s2_slope_v081_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w5_s0_slope_v082_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w5_s1_slope_v083_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w5_s2_slope_v084_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w21_s0_slope_v085_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w21_s1_slope_v086_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w21_s2_slope_v087_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w63_s0_slope_v088_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w63_s1_slope_v089_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_slope_diff_norm_w63_s2_slope_v090_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w5_s0_slope_v091_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w5_s1_slope_v092_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w5_s2_slope_v093_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w21_s0_slope_v094_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w21_s1_slope_v095_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w21_s2_slope_v096_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w63_s0_slope_v097_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w63_s1_slope_v098_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_pct_w63_s2_slope_v099_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w5_s0_slope_v100_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w5_s1_slope_v101_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w5_s2_slope_v102_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w21_s0_slope_v103_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w21_s1_slope_v104_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w21_s2_slope_v105_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w63_s0_slope_v106_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w63_s1_slope_v107_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_slope_diff_norm_w63_s2_slope_v108_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w5_s0_slope_v109_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w5_s1_slope_v110_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w5_s2_slope_v111_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w21_s0_slope_v112_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w21_s1_slope_v113_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w21_s2_slope_v114_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w63_s0_slope_v115_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w63_s1_slope_v116_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_pct_w63_s2_slope_v117_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w5_s0_slope_v118_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w5_s1_slope_v119_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w5_s2_slope_v120_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w21_s0_slope_v121_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w21_s1_slope_v122_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w21_s2_slope_v123_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w63_s0_slope_v124_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w63_s1_slope_v125_signal,
    f06ucq_f06_utility_credit_quality_creditq_126d_slope_diff_norm_w63_s2_slope_v126_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w5_s0_slope_v127_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w5_s1_slope_v128_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w5_s2_slope_v129_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w21_s0_slope_v130_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w21_s1_slope_v131_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w21_s2_slope_v132_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w63_s0_slope_v133_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w63_s1_slope_v134_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_pct_w63_s2_slope_v135_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w5_s0_slope_v136_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w5_s1_slope_v137_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w5_s2_slope_v138_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w21_s0_slope_v139_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w21_s1_slope_v140_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w21_s2_slope_v141_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w63_s0_slope_v142_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w63_s1_slope_v143_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_slope_diff_norm_w63_s2_slope_v144_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w5_s0_slope_v145_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w5_s1_slope_v146_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w5_s2_slope_v147_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w21_s0_slope_v148_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w21_s1_slope_v149_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_slope_pct_w21_s2_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_UTILITY_CREDIT_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    de = pd.Series(0.6 + 0.2 * np.sin(np.arange(n) / 250.0) + 0.05 * np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj, "ebitda": ebitda, "fcf": fcf, "equity": equity,
        "debt": debt, "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_debt_ebitda", "_f06_credit_quality", "_f06_solvency_score",)
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
    print(f"OK f06_utility_credit_quality_2nd_derivatives_001_150_claude: {n_features} features pass")
