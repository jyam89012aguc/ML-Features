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
def _f37_debt_ebitda(debt, ebitda):
    return debt / ebitda.replace(0, np.nan).abs()


def _f37_debt_capacity(debt, ebitda, w):
    ratio = debt / ebitda.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


def _f37_coverage_quality(debt, fcf, ebitda, w):
    cov1 = fcf / debt.replace(0, np.nan).abs()
    cov2 = ebitda / debt.replace(0, np.nan).abs()
    return (cov1 + cov2).rolling(w, min_periods=max(1, w // 2)).mean()

# ===== features =====

# p0_xclose window=5 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v001_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v002_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 5)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v003_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v004_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 5)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v005_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=5 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v006_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v007_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v008_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 10)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v009_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v010_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 10)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v011_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v012_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v013_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v014_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v015_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v016_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v017_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v018_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v019_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v020_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 42)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v021_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v022_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 42)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v023_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v024_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v025_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v026_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 63)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v027_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v028_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 63)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v029_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v030_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v031_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v032_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 126)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v033_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v034_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 126)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v035_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v036_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v037_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v038_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 189)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v039_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v040_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 189)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v041_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v042_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v043_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v044_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 252)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v045_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v046_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 252)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v047_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v048_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v049_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v050_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 378)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v051_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 378)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v052_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 378)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v053_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 378)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v054_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 378)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=5
def f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v055_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=10
def f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v056_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 504)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=21
def f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v057_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 504)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=42
def f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v058_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 504)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=63
def f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v059_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 504)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504 ow=126
def f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v060_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 504)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v061_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v062_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v063_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v064_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v065_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v066_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v067_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v068_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v069_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v070_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v071_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v072_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v073_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v074_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v075_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v076_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v077_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v078_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v079_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v080_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v081_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v082_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v083_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v084_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v085_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v086_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v087_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v088_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v089_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v090_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v091_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v092_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v093_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v094_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v095_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v096_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v097_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v098_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v099_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v100_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v101_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v102_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v103_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v104_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v105_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v106_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v107_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v108_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v109_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v110_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v111_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v112_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v113_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v114_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=5
def f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v115_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=10
def f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v116_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=21
def f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v117_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=42
def f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v118_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=63
def f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v119_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504 ow=126
def f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v120_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=5
def f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v121_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=10
def f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v122_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=21
def f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v123_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=42
def f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v124_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=63
def f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v125_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5 ow=126
def f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v126_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=5
def f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v127_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=10
def f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v128_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=21
def f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v129_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=42
def f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v130_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=63
def f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v131_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10 ow=126
def f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v132_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=5
def f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v133_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=10
def f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v134_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=21
def f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v135_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=42
def f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v136_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=63
def f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v137_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21 ow=126
def f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v138_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=5
def f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v139_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=10
def f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v140_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=21
def f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v141_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=42
def f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v142_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=63
def f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v143_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42 ow=126
def f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v144_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=5
def f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v145_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=10
def f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v146_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=21
def f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v147_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=42
def f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v148_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=63
def f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v149_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63 ow=126
def f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v150_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v001_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v002_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v003_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v004_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v005_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_5d_slope_v006_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v007_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v008_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v009_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v010_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v011_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_10d_slope_v012_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v013_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v014_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v015_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v016_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v017_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_21d_slope_v018_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v019_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v020_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v021_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v022_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v023_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_42d_slope_v024_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v025_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v026_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v027_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v028_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v029_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_63d_slope_v030_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v031_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v032_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v033_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v034_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v035_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_126d_slope_v036_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v037_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v038_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v039_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v040_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v041_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_189d_slope_v042_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v043_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v044_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v045_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v046_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v047_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_252d_slope_v048_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v049_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v050_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v051_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v052_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v053_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_378d_slope_v054_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v055_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v056_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v057_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v058_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v059_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_504d_slope_v060_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v061_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v062_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v063_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v064_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v065_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_5d_slope_v066_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v067_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v068_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v069_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v070_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v071_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_10d_slope_v072_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v073_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v074_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v075_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v076_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v077_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_21d_slope_v078_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v079_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v080_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v081_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v082_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v083_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_42d_slope_v084_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v085_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v086_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v087_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v088_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v089_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_63d_slope_v090_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v091_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v092_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v093_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v094_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v095_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_126d_slope_v096_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v097_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v098_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v099_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v100_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v101_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_189d_slope_v102_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v103_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v104_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v105_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v106_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v107_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_252d_slope_v108_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v109_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v110_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v111_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v112_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v113_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_378d_slope_v114_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v115_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v116_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v117_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v118_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v119_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_504d_slope_v120_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v121_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v122_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v123_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v124_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v125_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_5d_slope_v126_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v127_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v128_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v129_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v130_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v131_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_10d_slope_v132_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v133_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v134_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v135_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v136_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v137_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_21d_slope_v138_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v139_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v140_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v141_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v142_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v143_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_42d_slope_v144_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v145_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v146_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v147_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v148_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v149_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_UTILITY_DEBT_CAPACITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    de        = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj,
        "debt": debt, "equity": equity, "ebitda": ebitda, "fcf": fcf,
        "capex": capex, "sharesbas": sharesbas, "shareswa": shareswa, "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f37_debt_ebitda", "_f37_debt_capacity", "_f37_coverage_quality")
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
    print(f"OK f37_utility_debt_capacity_2nd_derivatives_001_150_claude: {n_features} features pass")
