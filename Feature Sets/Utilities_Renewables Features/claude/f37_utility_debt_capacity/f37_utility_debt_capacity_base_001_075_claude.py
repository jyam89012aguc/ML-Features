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

# p0_xclose window=5
def f37udc_f37_utility_debt_capacity_p0_xclose_5d_base_v001_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 5)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=10
def f37udc_f37_utility_debt_capacity_p0_xclose_10d_base_v002_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=21
def f37udc_f37_utility_debt_capacity_p0_xclose_21d_base_v003_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=42
def f37udc_f37_utility_debt_capacity_p0_xclose_42d_base_v004_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=63
def f37udc_f37_utility_debt_capacity_p0_xclose_63d_base_v005_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=126
def f37udc_f37_utility_debt_capacity_p0_xclose_126d_base_v006_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=189
def f37udc_f37_utility_debt_capacity_p0_xclose_189d_base_v007_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 189)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=252
def f37udc_f37_utility_debt_capacity_p0_xclose_252d_base_v008_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=378
def f37udc_f37_utility_debt_capacity_p0_xclose_378d_base_v009_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 378)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_xclose window=504
def f37udc_f37_utility_debt_capacity_p0_xclose_504d_base_v010_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)) * _mean(closeadj, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=5
def f37udc_f37_utility_debt_capacity_p0_meanw_5d_base_v011_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=10
def f37udc_f37_utility_debt_capacity_p0_meanw_10d_base_v012_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=21
def f37udc_f37_utility_debt_capacity_p0_meanw_21d_base_v013_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=42
def f37udc_f37_utility_debt_capacity_p0_meanw_42d_base_v014_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=63
def f37udc_f37_utility_debt_capacity_p0_meanw_63d_base_v015_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=126
def f37udc_f37_utility_debt_capacity_p0_meanw_126d_base_v016_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=189
def f37udc_f37_utility_debt_capacity_p0_meanw_189d_base_v017_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=252
def f37udc_f37_utility_debt_capacity_p0_meanw_252d_base_v018_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=378
def f37udc_f37_utility_debt_capacity_p0_meanw_378d_base_v019_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_meanw window=504
def f37udc_f37_utility_debt_capacity_p0_meanw_504d_base_v020_signal(closeadj, debt, ebitda):
    base = _mean(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=5
def f37udc_f37_utility_debt_capacity_p0_stdw_5d_base_v021_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=10
def f37udc_f37_utility_debt_capacity_p0_stdw_10d_base_v022_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=21
def f37udc_f37_utility_debt_capacity_p0_stdw_21d_base_v023_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=42
def f37udc_f37_utility_debt_capacity_p0_stdw_42d_base_v024_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=63
def f37udc_f37_utility_debt_capacity_p0_stdw_63d_base_v025_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=126
def f37udc_f37_utility_debt_capacity_p0_stdw_126d_base_v026_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=189
def f37udc_f37_utility_debt_capacity_p0_stdw_189d_base_v027_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=252
def f37udc_f37_utility_debt_capacity_p0_stdw_252d_base_v028_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=378
def f37udc_f37_utility_debt_capacity_p0_stdw_378d_base_v029_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_stdw window=504
def f37udc_f37_utility_debt_capacity_p0_stdw_504d_base_v030_signal(closeadj, debt, ebitda):
    base = _std(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=5
def f37udc_f37_utility_debt_capacity_p0_zw_5d_base_v031_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 5) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=10
def f37udc_f37_utility_debt_capacity_p0_zw_10d_base_v032_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 10) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=21
def f37udc_f37_utility_debt_capacity_p0_zw_21d_base_v033_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 21) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=42
def f37udc_f37_utility_debt_capacity_p0_zw_42d_base_v034_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 42) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=63
def f37udc_f37_utility_debt_capacity_p0_zw_63d_base_v035_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 63) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=126
def f37udc_f37_utility_debt_capacity_p0_zw_126d_base_v036_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 126) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=189
def f37udc_f37_utility_debt_capacity_p0_zw_189d_base_v037_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 189) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=252
def f37udc_f37_utility_debt_capacity_p0_zw_252d_base_v038_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 252) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=378
def f37udc_f37_utility_debt_capacity_p0_zw_378d_base_v039_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 378) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_zw window=504
def f37udc_f37_utility_debt_capacity_p0_zw_504d_base_v040_signal(closeadj, debt, ebitda):
    base = _z(_f37_debt_ebitda(debt, ebitda), 504) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=5
def f37udc_f37_utility_debt_capacity_p0_emaw_5d_base_v041_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=5, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=10
def f37udc_f37_utility_debt_capacity_p0_emaw_10d_base_v042_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=10, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=21
def f37udc_f37_utility_debt_capacity_p0_emaw_21d_base_v043_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=21, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=42
def f37udc_f37_utility_debt_capacity_p0_emaw_42d_base_v044_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=42, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=63
def f37udc_f37_utility_debt_capacity_p0_emaw_63d_base_v045_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=63, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=126
def f37udc_f37_utility_debt_capacity_p0_emaw_126d_base_v046_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=126, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=189
def f37udc_f37_utility_debt_capacity_p0_emaw_189d_base_v047_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=189, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=252
def f37udc_f37_utility_debt_capacity_p0_emaw_252d_base_v048_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=252, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=378
def f37udc_f37_utility_debt_capacity_p0_emaw_378d_base_v049_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=378, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_emaw window=504
def f37udc_f37_utility_debt_capacity_p0_emaw_504d_base_v050_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).ewm(span=504, adjust=False).mean() * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=5
def f37udc_f37_utility_debt_capacity_p0_logabs_5d_base_v051_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 5)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=10
def f37udc_f37_utility_debt_capacity_p0_logabs_10d_base_v052_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=21
def f37udc_f37_utility_debt_capacity_p0_logabs_21d_base_v053_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=42
def f37udc_f37_utility_debt_capacity_p0_logabs_42d_base_v054_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=63
def f37udc_f37_utility_debt_capacity_p0_logabs_63d_base_v055_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=126
def f37udc_f37_utility_debt_capacity_p0_logabs_126d_base_v056_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=189
def f37udc_f37_utility_debt_capacity_p0_logabs_189d_base_v057_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 189)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=252
def f37udc_f37_utility_debt_capacity_p0_logabs_252d_base_v058_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=378
def f37udc_f37_utility_debt_capacity_p0_logabs_378d_base_v059_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 378)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_logabs window=504
def f37udc_f37_utility_debt_capacity_p0_logabs_504d_base_v060_signal(closeadj, debt, ebitda):
    base = np.log((_f37_debt_ebitda(debt, ebitda)).abs() + 1.0) * _mean(closeadj, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=5
def f37udc_f37_utility_debt_capacity_p0_signsq_5d_base_v061_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 5)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=10
def f37udc_f37_utility_debt_capacity_p0_signsq_10d_base_v062_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 10)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=21
def f37udc_f37_utility_debt_capacity_p0_signsq_21d_base_v063_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=42
def f37udc_f37_utility_debt_capacity_p0_signsq_42d_base_v064_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 42)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=63
def f37udc_f37_utility_debt_capacity_p0_signsq_63d_base_v065_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=126
def f37udc_f37_utility_debt_capacity_p0_signsq_126d_base_v066_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=189
def f37udc_f37_utility_debt_capacity_p0_signsq_189d_base_v067_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 189)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=252
def f37udc_f37_utility_debt_capacity_p0_signsq_252d_base_v068_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=378
def f37udc_f37_utility_debt_capacity_p0_signsq_378d_base_v069_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 378)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_signsq window=504
def f37udc_f37_utility_debt_capacity_p0_signsq_504d_base_v070_signal(closeadj, debt, ebitda):
    b = _f37_debt_ebitda(debt, ebitda)
    base = np.sign(b) * b.abs() * _mean(closeadj, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=5
def f37udc_f37_utility_debt_capacity_p0_qrank_5d_base_v071_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).rolling(5, min_periods=max(1, 5//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=10
def f37udc_f37_utility_debt_capacity_p0_qrank_10d_base_v072_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).rolling(10, min_periods=max(1, 10//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=21
def f37udc_f37_utility_debt_capacity_p0_qrank_21d_base_v073_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).rolling(21, min_periods=max(1, 21//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=42
def f37udc_f37_utility_debt_capacity_p0_qrank_42d_base_v074_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).rolling(42, min_periods=max(1, 42//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# p0_qrank window=63
def f37udc_f37_utility_debt_capacity_p0_qrank_63d_base_v075_signal(closeadj, debt, ebitda):
    base = (_f37_debt_ebitda(debt, ebitda)).rolling(63, min_periods=max(1, 63//2)).rank(pct=True) * closeadj
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37udc_f37_utility_debt_capacity_p0_xclose_5d_base_v001_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_10d_base_v002_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_21d_base_v003_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_42d_base_v004_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_63d_base_v005_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_126d_base_v006_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_189d_base_v007_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_252d_base_v008_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_378d_base_v009_signal,
    f37udc_f37_utility_debt_capacity_p0_xclose_504d_base_v010_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_5d_base_v011_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_10d_base_v012_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_21d_base_v013_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_42d_base_v014_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_63d_base_v015_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_126d_base_v016_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_189d_base_v017_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_252d_base_v018_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_378d_base_v019_signal,
    f37udc_f37_utility_debt_capacity_p0_meanw_504d_base_v020_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_5d_base_v021_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_10d_base_v022_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_21d_base_v023_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_42d_base_v024_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_63d_base_v025_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_126d_base_v026_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_189d_base_v027_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_252d_base_v028_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_378d_base_v029_signal,
    f37udc_f37_utility_debt_capacity_p0_stdw_504d_base_v030_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_5d_base_v031_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_10d_base_v032_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_21d_base_v033_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_42d_base_v034_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_63d_base_v035_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_126d_base_v036_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_189d_base_v037_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_252d_base_v038_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_378d_base_v039_signal,
    f37udc_f37_utility_debt_capacity_p0_zw_504d_base_v040_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_5d_base_v041_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_10d_base_v042_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_21d_base_v043_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_42d_base_v044_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_63d_base_v045_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_126d_base_v046_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_189d_base_v047_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_252d_base_v048_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_378d_base_v049_signal,
    f37udc_f37_utility_debt_capacity_p0_emaw_504d_base_v050_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_5d_base_v051_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_10d_base_v052_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_21d_base_v053_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_42d_base_v054_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_63d_base_v055_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_126d_base_v056_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_189d_base_v057_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_252d_base_v058_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_378d_base_v059_signal,
    f37udc_f37_utility_debt_capacity_p0_logabs_504d_base_v060_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_5d_base_v061_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_10d_base_v062_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_21d_base_v063_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_42d_base_v064_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_63d_base_v065_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_126d_base_v066_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_189d_base_v067_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_252d_base_v068_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_378d_base_v069_signal,
    f37udc_f37_utility_debt_capacity_p0_signsq_504d_base_v070_signal,
    f37udc_f37_utility_debt_capacity_p0_qrank_5d_base_v071_signal,
    f37udc_f37_utility_debt_capacity_p0_qrank_10d_base_v072_signal,
    f37udc_f37_utility_debt_capacity_p0_qrank_21d_base_v073_signal,
    f37udc_f37_utility_debt_capacity_p0_qrank_42d_base_v074_signal,
    f37udc_f37_utility_debt_capacity_p0_qrank_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_UTILITY_DEBT_CAPACITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f37_utility_debt_capacity_base_001_075_claude: {n_features} features pass")
