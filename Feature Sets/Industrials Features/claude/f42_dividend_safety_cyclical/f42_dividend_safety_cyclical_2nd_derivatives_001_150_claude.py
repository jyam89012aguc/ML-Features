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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f42_payout_coverage(payoutratio, fcfps, dps):
    cov = fcfps / dps.replace(0, np.nan).abs()
    return cov * (1.0 - payoutratio)


def _f42_dividend_safety_score(dps, eps, fcfps, w):
    eps_cov = eps / dps.replace(0, np.nan).abs()
    fcf_cov = fcfps / dps.replace(0, np.nan).abs()
    score = (eps_cov + fcf_cov) / 2.0
    return score.rolling(w, min_periods=max(1, w // 2)).mean()


def _f42_payout_durability(payoutratio, w):
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).std()

# slope feature 1: payout_cov_sm5d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm5d_xc_5d_slope_v001_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 2: payout_cov_sm5d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm5d_xclog_10d_slope_v002_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 5)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 3: payout_cov_sm5d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm5d_xcm21_21d_slope_v003_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 4: payout_cov_sm10d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm10d_xc_42d_slope_v004_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 10)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 5: payout_cov_sm10d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm10d_xclog_63d_slope_v005_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 10)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 6: payout_cov_sm10d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm10d_xcm21_126d_slope_v006_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 10)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 7: payout_cov_sm21d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm21d_xc_5d_slope_v007_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 8: payout_cov_sm21d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm21d_xclog_10d_slope_v008_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 9: payout_cov_sm21d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm21d_xcm21_21d_slope_v009_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 10: payout_cov_sm42d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm42d_xc_42d_slope_v010_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 11: payout_cov_sm42d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm42d_xclog_63d_slope_v011_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 12: payout_cov_sm42d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm42d_xcm21_126d_slope_v012_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 13: payout_cov_sm63d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm63d_xc_5d_slope_v013_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 14: payout_cov_sm63d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm63d_xclog_10d_slope_v014_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 15: payout_cov_sm63d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm63d_xcm21_21d_slope_v015_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 16: payout_cov_sm126d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm126d_xc_42d_slope_v016_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 17: payout_cov_sm126d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm126d_xclog_63d_slope_v017_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 18: payout_cov_sm126d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm126d_xcm21_126d_slope_v018_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 19: payout_cov_sm189d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm189d_xc_5d_slope_v019_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 189)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 20: payout_cov_sm189d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm189d_xclog_10d_slope_v020_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 189)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 21: payout_cov_sm189d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm189d_xcm21_21d_slope_v021_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 189)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 22: payout_cov_sm252d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm252d_xc_42d_slope_v022_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 23: payout_cov_sm252d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm252d_xclog_63d_slope_v023_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 24: payout_cov_sm252d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm252d_xcm21_126d_slope_v024_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 25: payout_cov_sm378d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm378d_xc_5d_slope_v025_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 26: payout_cov_sm378d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm378d_xclog_10d_slope_v026_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 27: payout_cov_sm378d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm378d_xcm21_21d_slope_v027_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 28: payout_cov_sm504d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm504d_xc_42d_slope_v028_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 504)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 29: payout_cov_sm504d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm504d_xclog_63d_slope_v029_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 30: payout_cov_sm504d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_cov_sm504d_xcm21_126d_slope_v030_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 31: div_safety_5d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_5d_xc_5d_slope_v031_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 32: div_safety_5d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_5d_xclog_10d_slope_v032_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 5)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 33: div_safety_5d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_5d_xcm21_21d_slope_v033_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 34: div_safety_10d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_10d_xc_42d_slope_v034_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 10)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 35: div_safety_10d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_10d_xclog_63d_slope_v035_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 10)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 36: div_safety_10d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_10d_xcm21_126d_slope_v036_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 10)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 37: div_safety_21d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_21d_xc_5d_slope_v037_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 38: div_safety_21d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_21d_xclog_10d_slope_v038_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 39: div_safety_21d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_21d_xcm21_21d_slope_v039_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 40: div_safety_42d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_42d_xc_42d_slope_v040_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 41: div_safety_42d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_42d_xclog_63d_slope_v041_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 42: div_safety_42d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_42d_xcm21_126d_slope_v042_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 43: div_safety_63d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_63d_xc_5d_slope_v043_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 44: div_safety_63d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_63d_xclog_10d_slope_v044_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 45: div_safety_63d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_63d_xcm21_21d_slope_v045_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 46: div_safety_126d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_126d_xc_42d_slope_v046_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 47: div_safety_126d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_126d_xclog_63d_slope_v047_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 48: div_safety_126d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_126d_xcm21_126d_slope_v048_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 49: div_safety_189d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_189d_xc_5d_slope_v049_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 189)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 50: div_safety_189d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_189d_xclog_10d_slope_v050_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 189)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 51: div_safety_189d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_189d_xcm21_21d_slope_v051_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 189)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 52: div_safety_252d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_252d_xc_42d_slope_v052_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 53: div_safety_252d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_252d_xclog_63d_slope_v053_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 54: div_safety_252d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_252d_xcm21_126d_slope_v054_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 55: div_safety_378d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_378d_xc_5d_slope_v055_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 56: div_safety_378d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_378d_xclog_10d_slope_v056_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 57: div_safety_378d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_378d_xcm21_21d_slope_v057_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 58: div_safety_504d_xc
def f42dsc_f42_dividend_safety_cyclical_div_safety_504d_xc_42d_slope_v058_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 504)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 59: div_safety_504d_xclog
def f42dsc_f42_dividend_safety_cyclical_div_safety_504d_xclog_63d_slope_v059_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 60: div_safety_504d_xcm21
def f42dsc_f42_dividend_safety_cyclical_div_safety_504d_xcm21_126d_slope_v060_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 61: payout_dur_5d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_5d_xc_5d_slope_v061_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 5)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 62: payout_dur_5d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_5d_xclog_10d_slope_v062_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 5)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 63: payout_dur_5d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_5d_xcm21_21d_slope_v063_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 64: payout_dur_10d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_10d_xc_42d_slope_v064_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 10)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 65: payout_dur_10d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_10d_xclog_63d_slope_v065_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 10)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 66: payout_dur_10d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_10d_xcm21_126d_slope_v066_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 10)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 67: payout_dur_21d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_21d_xc_5d_slope_v067_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 68: payout_dur_21d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_21d_xclog_10d_slope_v068_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 69: payout_dur_21d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_21d_xcm21_21d_slope_v069_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 70: payout_dur_42d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_42d_xc_42d_slope_v070_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 71: payout_dur_42d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_42d_xclog_63d_slope_v071_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 72: payout_dur_42d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_42d_xcm21_126d_slope_v072_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 73: payout_dur_63d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_63d_xc_5d_slope_v073_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 63)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 74: payout_dur_63d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_63d_xclog_10d_slope_v074_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 75: payout_dur_63d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_63d_xcm21_21d_slope_v075_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 76: payout_dur_126d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_126d_xc_42d_slope_v076_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 126)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 77: payout_dur_126d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_126d_xclog_63d_slope_v077_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 78: payout_dur_126d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_126d_xcm21_126d_slope_v078_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 79: payout_dur_189d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_189d_xc_5d_slope_v079_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 189)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 80: payout_dur_189d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_189d_xclog_10d_slope_v080_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 189)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 81: payout_dur_189d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_189d_xcm21_21d_slope_v081_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 189)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 82: payout_dur_252d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_252d_xc_42d_slope_v082_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 83: payout_dur_252d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_252d_xclog_63d_slope_v083_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 84: payout_dur_252d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_252d_xcm21_126d_slope_v084_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 85: payout_dur_378d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_378d_xc_5d_slope_v085_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 378)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 86: payout_dur_378d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_378d_xclog_10d_slope_v086_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 378)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 87: payout_dur_378d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_378d_xcm21_21d_slope_v087_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 378)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 88: payout_dur_504d_xc
def f42dsc_f42_dividend_safety_cyclical_payout_dur_504d_xc_42d_slope_v088_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 504)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 89: payout_dur_504d_xclog
def f42dsc_f42_dividend_safety_cyclical_payout_dur_504d_xclog_63d_slope_v089_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 90: payout_dur_504d_xcm21
def f42dsc_f42_dividend_safety_cyclical_payout_dur_504d_xcm21_126d_slope_v090_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 91: cov_z_21d
def f42dsc_f42_dividend_safety_cyclical_cov_z_21d_5d_slope_v091_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 92: safety_z_21d
def f42dsc_f42_dividend_safety_cyclical_safety_z_21d_10d_slope_v092_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 93: dur_z_21d
def f42dsc_f42_dividend_safety_cyclical_dur_z_21d_21d_slope_v093_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 94: cov_ema_21d
def f42dsc_f42_dividend_safety_cyclical_cov_ema_21d_42d_slope_v094_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 95: safety_ema_21d
def f42dsc_f42_dividend_safety_cyclical_safety_ema_21d_63d_slope_v095_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 96: dur_ema_21d
def f42dsc_f42_dividend_safety_cyclical_dur_ema_21d_126d_slope_v096_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 97: cov_z_42d
def f42dsc_f42_dividend_safety_cyclical_cov_z_42d_5d_slope_v097_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 98: safety_z_42d
def f42dsc_f42_dividend_safety_cyclical_safety_z_42d_10d_slope_v098_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 99: dur_z_42d
def f42dsc_f42_dividend_safety_cyclical_dur_z_42d_21d_slope_v099_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 42)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 100: cov_ema_42d
def f42dsc_f42_dividend_safety_cyclical_cov_ema_42d_42d_slope_v100_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 101: safety_ema_42d
def f42dsc_f42_dividend_safety_cyclical_safety_ema_42d_63d_slope_v101_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 102: dur_ema_42d
def f42dsc_f42_dividend_safety_cyclical_dur_ema_42d_126d_slope_v102_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 42)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 103: cov_z_63d
def f42dsc_f42_dividend_safety_cyclical_cov_z_63d_5d_slope_v103_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 104: safety_z_63d
def f42dsc_f42_dividend_safety_cyclical_safety_z_63d_10d_slope_v104_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 105: dur_z_63d
def f42dsc_f42_dividend_safety_cyclical_dur_z_63d_21d_slope_v105_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 106: cov_ema_63d
def f42dsc_f42_dividend_safety_cyclical_cov_ema_63d_42d_slope_v106_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 107: safety_ema_63d
def f42dsc_f42_dividend_safety_cyclical_safety_ema_63d_63d_slope_v107_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 108: dur_ema_63d
def f42dsc_f42_dividend_safety_cyclical_dur_ema_63d_126d_slope_v108_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 109: cov_z_126d
def f42dsc_f42_dividend_safety_cyclical_cov_z_126d_5d_slope_v109_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 110: safety_z_126d
def f42dsc_f42_dividend_safety_cyclical_safety_z_126d_10d_slope_v110_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 111: dur_z_126d
def f42dsc_f42_dividend_safety_cyclical_dur_z_126d_21d_slope_v111_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 112: cov_ema_126d
def f42dsc_f42_dividend_safety_cyclical_cov_ema_126d_42d_slope_v112_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 113: safety_ema_126d
def f42dsc_f42_dividend_safety_cyclical_safety_ema_126d_63d_slope_v113_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 114: dur_ema_126d
def f42dsc_f42_dividend_safety_cyclical_dur_ema_126d_126d_slope_v114_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 115: cov_z_252d
def f42dsc_f42_dividend_safety_cyclical_cov_z_252d_5d_slope_v115_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 116: safety_z_252d
def f42dsc_f42_dividend_safety_cyclical_safety_z_252d_10d_slope_v116_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 252)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 117: dur_z_252d
def f42dsc_f42_dividend_safety_cyclical_dur_z_252d_21d_slope_v117_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 118: cov_ema_252d
def f42dsc_f42_dividend_safety_cyclical_cov_ema_252d_42d_slope_v118_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 119: safety_ema_252d
def f42dsc_f42_dividend_safety_cyclical_safety_ema_252d_63d_slope_v119_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 120: dur_ema_252d
def f42dsc_f42_dividend_safety_cyclical_dur_ema_252d_126d_slope_v120_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 121: cov_z_504d
def f42dsc_f42_dividend_safety_cyclical_cov_z_504d_5d_slope_v121_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 122: safety_z_504d
def f42dsc_f42_dividend_safety_cyclical_safety_z_504d_10d_slope_v122_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 504)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 123: dur_z_504d
def f42dsc_f42_dividend_safety_cyclical_dur_z_504d_21d_slope_v123_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 124: cov_ema_504d
def f42dsc_f42_dividend_safety_cyclical_cov_ema_504d_42d_slope_v124_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 125: safety_ema_504d
def f42dsc_f42_dividend_safety_cyclical_safety_ema_504d_63d_slope_v125_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 126: dur_ema_504d
def f42dsc_f42_dividend_safety_cyclical_dur_ema_504d_126d_slope_v126_signal(payoutratio, closeadj):
    base = _f42_payout_durability(payoutratio, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 127: cov_sq_21d
def f42dsc_f42_dividend_safety_cyclical_cov_sq_21d_5d_slope_v127_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 21)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 128: safety_sq_21d
def f42dsc_f42_dividend_safety_cyclical_safety_sq_21d_10d_slope_v128_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 129: cov_sq_42d
def f42dsc_f42_dividend_safety_cyclical_cov_sq_42d_21d_slope_v129_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 42)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 130: safety_sq_42d
def f42dsc_f42_dividend_safety_cyclical_safety_sq_42d_42d_slope_v130_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 131: cov_sq_63d
def f42dsc_f42_dividend_safety_cyclical_cov_sq_63d_63d_slope_v131_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 132: safety_sq_63d
def f42dsc_f42_dividend_safety_cyclical_safety_sq_63d_126d_slope_v132_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 133: cov_sq_126d
def f42dsc_f42_dividend_safety_cyclical_cov_sq_126d_5d_slope_v133_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 126)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 134: safety_sq_126d
def f42dsc_f42_dividend_safety_cyclical_safety_sq_126d_10d_slope_v134_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 135: cov_sq_252d
def f42dsc_f42_dividend_safety_cyclical_cov_sq_252d_21d_slope_v135_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 136: safety_sq_252d
def f42dsc_f42_dividend_safety_cyclical_safety_sq_252d_42d_slope_v136_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 252)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 137: cov_sq_504d
def f42dsc_f42_dividend_safety_cyclical_cov_sq_504d_63d_slope_v137_signal(payoutratio, fcfps, dps, closeadj):
    base = _f42_payout_coverage(payoutratio, fcfps, dps)
    sm = _mean(base, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 138: safety_sq_504d
def f42dsc_f42_dividend_safety_cyclical_safety_sq_504d_126d_slope_v138_signal(dps, eps, fcfps, closeadj):
    base = _f42_dividend_safety_score(dps, eps, fcfps, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 139: covxsafety_21d
def f42dsc_f42_dividend_safety_cyclical_covxsafety_21d_5d_slope_v139_signal(payoutratio, fcfps, dps, eps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    base = (a * b)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 140: safetyxdur_21d
def f42dsc_f42_dividend_safety_cyclical_safetyxdur_21d_10d_slope_v140_signal(dps, eps, fcfps, payoutratio, closeadj):
    a = _f42_dividend_safety_score(dps, eps, fcfps, 21)
    b = _f42_payout_durability(payoutratio, 21)
    base = (a * b)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 141: covxdur_21d
def f42dsc_f42_dividend_safety_cyclical_covxdur_21d_21d_slope_v141_signal(payoutratio, fcfps, dps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_payout_durability(payoutratio, 21)
    base = (a * b)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 142: covxsafety_42d
def f42dsc_f42_dividend_safety_cyclical_covxsafety_42d_42d_slope_v142_signal(payoutratio, fcfps, dps, eps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    base = (a * b)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 143: safetyxdur_42d
def f42dsc_f42_dividend_safety_cyclical_safetyxdur_42d_63d_slope_v143_signal(dps, eps, fcfps, payoutratio, closeadj):
    a = _f42_dividend_safety_score(dps, eps, fcfps, 42)
    b = _f42_payout_durability(payoutratio, 42)
    base = (a * b)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 144: covxdur_42d
def f42dsc_f42_dividend_safety_cyclical_covxdur_42d_126d_slope_v144_signal(payoutratio, fcfps, dps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_payout_durability(payoutratio, 42)
    base = (a * b)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 145: covxsafety_63d
def f42dsc_f42_dividend_safety_cyclical_covxsafety_63d_5d_slope_v145_signal(payoutratio, fcfps, dps, eps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    base = (a * b)
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 146: safetyxdur_63d
def f42dsc_f42_dividend_safety_cyclical_safetyxdur_63d_10d_slope_v146_signal(dps, eps, fcfps, payoutratio, closeadj):
    a = _f42_dividend_safety_score(dps, eps, fcfps, 63)
    b = _f42_payout_durability(payoutratio, 63)
    base = (a * b)
    result = _slope_diff_norm(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 147: covxdur_63d
def f42dsc_f42_dividend_safety_cyclical_covxdur_63d_21d_slope_v147_signal(payoutratio, fcfps, dps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_payout_durability(payoutratio, 63)
    base = (a * b)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 148: covxsafety_126d
def f42dsc_f42_dividend_safety_cyclical_covxsafety_126d_42d_slope_v148_signal(payoutratio, fcfps, dps, eps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    base = (a * b)
    result = _slope_diff_norm(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 149: safetyxdur_126d
def f42dsc_f42_dividend_safety_cyclical_safetyxdur_126d_63d_slope_v149_signal(dps, eps, fcfps, payoutratio, closeadj):
    a = _f42_dividend_safety_score(dps, eps, fcfps, 126)
    b = _f42_payout_durability(payoutratio, 126)
    base = (a * b)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope feature 150: covxdur_126d
def f42dsc_f42_dividend_safety_cyclical_covxdur_126d_126d_slope_v150_signal(payoutratio, fcfps, dps, closeadj):
    a = _f42_payout_coverage(payoutratio, fcfps, dps)
    b = _f42_payout_durability(payoutratio, 126)
    base = (a * b)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm5d_xc_5d_slope_v001_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm5d_xclog_10d_slope_v002_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm5d_xcm21_21d_slope_v003_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm10d_xc_42d_slope_v004_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm10d_xclog_63d_slope_v005_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm10d_xcm21_126d_slope_v006_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm21d_xc_5d_slope_v007_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm21d_xclog_10d_slope_v008_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm21d_xcm21_21d_slope_v009_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm42d_xc_42d_slope_v010_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm42d_xclog_63d_slope_v011_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm42d_xcm21_126d_slope_v012_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm63d_xc_5d_slope_v013_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm63d_xclog_10d_slope_v014_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm63d_xcm21_21d_slope_v015_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm126d_xc_42d_slope_v016_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm126d_xclog_63d_slope_v017_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm126d_xcm21_126d_slope_v018_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm189d_xc_5d_slope_v019_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm189d_xclog_10d_slope_v020_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm189d_xcm21_21d_slope_v021_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm252d_xc_42d_slope_v022_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm252d_xclog_63d_slope_v023_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm252d_xcm21_126d_slope_v024_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm378d_xc_5d_slope_v025_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm378d_xclog_10d_slope_v026_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm378d_xcm21_21d_slope_v027_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm504d_xc_42d_slope_v028_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm504d_xclog_63d_slope_v029_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_cov_sm504d_xcm21_126d_slope_v030_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_5d_xc_5d_slope_v031_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_5d_xclog_10d_slope_v032_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_5d_xcm21_21d_slope_v033_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_10d_xc_42d_slope_v034_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_10d_xclog_63d_slope_v035_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_10d_xcm21_126d_slope_v036_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_21d_xc_5d_slope_v037_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_21d_xclog_10d_slope_v038_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_21d_xcm21_21d_slope_v039_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_42d_xc_42d_slope_v040_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_42d_xclog_63d_slope_v041_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_42d_xcm21_126d_slope_v042_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_63d_xc_5d_slope_v043_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_63d_xclog_10d_slope_v044_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_63d_xcm21_21d_slope_v045_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_126d_xc_42d_slope_v046_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_126d_xclog_63d_slope_v047_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_126d_xcm21_126d_slope_v048_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_189d_xc_5d_slope_v049_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_189d_xclog_10d_slope_v050_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_189d_xcm21_21d_slope_v051_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_252d_xc_42d_slope_v052_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_252d_xclog_63d_slope_v053_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_252d_xcm21_126d_slope_v054_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_378d_xc_5d_slope_v055_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_378d_xclog_10d_slope_v056_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_378d_xcm21_21d_slope_v057_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_504d_xc_42d_slope_v058_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_504d_xclog_63d_slope_v059_signal,
    f42dsc_f42_dividend_safety_cyclical_div_safety_504d_xcm21_126d_slope_v060_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_5d_xc_5d_slope_v061_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_5d_xclog_10d_slope_v062_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_5d_xcm21_21d_slope_v063_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_10d_xc_42d_slope_v064_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_10d_xclog_63d_slope_v065_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_10d_xcm21_126d_slope_v066_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_21d_xc_5d_slope_v067_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_21d_xclog_10d_slope_v068_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_21d_xcm21_21d_slope_v069_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_42d_xc_42d_slope_v070_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_42d_xclog_63d_slope_v071_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_42d_xcm21_126d_slope_v072_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_63d_xc_5d_slope_v073_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_63d_xclog_10d_slope_v074_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_63d_xcm21_21d_slope_v075_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_126d_xc_42d_slope_v076_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_126d_xclog_63d_slope_v077_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_126d_xcm21_126d_slope_v078_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_189d_xc_5d_slope_v079_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_189d_xclog_10d_slope_v080_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_189d_xcm21_21d_slope_v081_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_252d_xc_42d_slope_v082_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_252d_xclog_63d_slope_v083_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_252d_xcm21_126d_slope_v084_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_378d_xc_5d_slope_v085_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_378d_xclog_10d_slope_v086_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_378d_xcm21_21d_slope_v087_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_504d_xc_42d_slope_v088_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_504d_xclog_63d_slope_v089_signal,
    f42dsc_f42_dividend_safety_cyclical_payout_dur_504d_xcm21_126d_slope_v090_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_z_21d_5d_slope_v091_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_z_21d_10d_slope_v092_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_z_21d_21d_slope_v093_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_ema_21d_42d_slope_v094_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_ema_21d_63d_slope_v095_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_ema_21d_126d_slope_v096_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_z_42d_5d_slope_v097_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_z_42d_10d_slope_v098_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_z_42d_21d_slope_v099_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_ema_42d_42d_slope_v100_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_ema_42d_63d_slope_v101_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_ema_42d_126d_slope_v102_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_z_63d_5d_slope_v103_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_z_63d_10d_slope_v104_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_z_63d_21d_slope_v105_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_ema_63d_42d_slope_v106_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_ema_63d_63d_slope_v107_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_ema_63d_126d_slope_v108_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_z_126d_5d_slope_v109_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_z_126d_10d_slope_v110_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_z_126d_21d_slope_v111_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_ema_126d_42d_slope_v112_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_ema_126d_63d_slope_v113_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_ema_126d_126d_slope_v114_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_z_252d_5d_slope_v115_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_z_252d_10d_slope_v116_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_z_252d_21d_slope_v117_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_ema_252d_42d_slope_v118_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_ema_252d_63d_slope_v119_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_ema_252d_126d_slope_v120_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_z_504d_5d_slope_v121_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_z_504d_10d_slope_v122_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_z_504d_21d_slope_v123_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_ema_504d_42d_slope_v124_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_ema_504d_63d_slope_v125_signal,
    f42dsc_f42_dividend_safety_cyclical_dur_ema_504d_126d_slope_v126_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_sq_21d_5d_slope_v127_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_sq_21d_10d_slope_v128_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_sq_42d_21d_slope_v129_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_sq_42d_42d_slope_v130_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_sq_63d_63d_slope_v131_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_sq_63d_126d_slope_v132_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_sq_126d_5d_slope_v133_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_sq_126d_10d_slope_v134_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_sq_252d_21d_slope_v135_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_sq_252d_42d_slope_v136_signal,
    f42dsc_f42_dividend_safety_cyclical_cov_sq_504d_63d_slope_v137_signal,
    f42dsc_f42_dividend_safety_cyclical_safety_sq_504d_126d_slope_v138_signal,
    f42dsc_f42_dividend_safety_cyclical_covxsafety_21d_5d_slope_v139_signal,
    f42dsc_f42_dividend_safety_cyclical_safetyxdur_21d_10d_slope_v140_signal,
    f42dsc_f42_dividend_safety_cyclical_covxdur_21d_21d_slope_v141_signal,
    f42dsc_f42_dividend_safety_cyclical_covxsafety_42d_42d_slope_v142_signal,
    f42dsc_f42_dividend_safety_cyclical_safetyxdur_42d_63d_slope_v143_signal,
    f42dsc_f42_dividend_safety_cyclical_covxdur_42d_126d_slope_v144_signal,
    f42dsc_f42_dividend_safety_cyclical_covxsafety_63d_5d_slope_v145_signal,
    f42dsc_f42_dividend_safety_cyclical_safetyxdur_63d_10d_slope_v146_signal,
    f42dsc_f42_dividend_safety_cyclical_covxdur_63d_21d_slope_v147_signal,
    f42dsc_f42_dividend_safety_cyclical_covxsafety_126d_42d_slope_v148_signal,
    f42dsc_f42_dividend_safety_cyclical_safetyxdur_126d_63d_slope_v149_signal,
    f42dsc_f42_dividend_safety_cyclical_covxdur_126d_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_DIVIDEND_SAFETY_CYCLICAL_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f42_payout_coverage', '_f42_dividend_safety_score', '_f42_payout_durability')
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
    print(f"OK f42_dividend_safety_cyclical_2nd_derivatives_001_150_claude: {n_features} features pass")
