"""
Family: Junior Financing Dilution
Sector: Mining/Junior
Mathematical Approach: Fundamental/Dilution
"""


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

def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5

def _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, w):
    return sharesbas.pct_change(w)

def _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, w):
    return -ncfcommon.rolling(w).sum() / ncfo.rolling(w).sum().abs().replace(0, np.nan)

def _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, w):
    return cashneq / ncfo.rolling(w).mean().abs()

def _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, w):
    return (sharesbas.diff() > 0).astype(float).rolling(w).sum()

def _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, w):
    return -ncfcommon / (sharesbas * closeadj).rolling(w).mean()

def _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, w):
    return ncfo.diff(w)

def _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, w):
    return cashneq / assets

def f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v001_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v002_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v003_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v004_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v005_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v006_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v007_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v008_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v009_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v010_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v011_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v012_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v013_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v014_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v015_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v016_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v017_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v018_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v019_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v020_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v021_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v022_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v023_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v024_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_21d_3rd_derivatives_v025_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_63d_3rd_derivatives_v026_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_126d_3rd_derivatives_v027_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_252d_3rd_derivatives_v028_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_504d_3rd_derivatives_v029_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_5d_3rd_derivatives_v030_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_21d_3rd_derivatives_v031_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_63d_3rd_derivatives_v032_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_126d_3rd_derivatives_v033_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_252d_3rd_derivatives_v034_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_504d_3rd_derivatives_v035_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_5d_3rd_derivatives_v036_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_21d_3rd_derivatives_v037_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_63d_3rd_derivatives_v038_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_126d_3rd_derivatives_v039_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_252d_3rd_derivatives_v040_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_504d_3rd_derivatives_v041_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_5d_3rd_derivatives_v042_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v043_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v044_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v045_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v046_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v047_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v048_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v049_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v050_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v051_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v052_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v053_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v054_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v055_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v056_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v057_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v058_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v059_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v060_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v061_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v062_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v063_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v064_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v065_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v066_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_21d_3rd_derivatives_v067_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_63d_3rd_derivatives_v068_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_126d_3rd_derivatives_v069_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_252d_3rd_derivatives_v070_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_504d_3rd_derivatives_v071_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_5d_3rd_derivatives_v072_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_21d_3rd_derivatives_v073_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_63d_3rd_derivatives_v074_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_126d_3rd_derivatives_v075_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_252d_3rd_derivatives_v076_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_504d_3rd_derivatives_v077_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_5d_3rd_derivatives_v078_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_21d_3rd_derivatives_v079_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_63d_3rd_derivatives_v080_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_126d_3rd_derivatives_v081_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_252d_3rd_derivatives_v082_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_504d_3rd_derivatives_v083_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_5d_3rd_derivatives_v084_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v085_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v086_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v087_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v088_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v089_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v090_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v091_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v092_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v093_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v094_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v095_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v096_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v097_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v098_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v099_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v100_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v101_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v102_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v103_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v104_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v105_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v106_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v107_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v108_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_21d_3rd_derivatives_v109_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_63d_3rd_derivatives_v110_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_126d_3rd_derivatives_v111_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_252d_3rd_derivatives_v112_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_504d_3rd_derivatives_v113_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_5d_3rd_derivatives_v114_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_21d_3rd_derivatives_v115_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_63d_3rd_derivatives_v116_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_126d_3rd_derivatives_v117_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_252d_3rd_derivatives_v118_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_504d_3rd_derivatives_v119_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_5d_3rd_derivatives_v120_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_21d_3rd_derivatives_v121_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_63d_3rd_derivatives_v122_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_126d_3rd_derivatives_v123_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_252d_3rd_derivatives_v124_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_504d_3rd_derivatives_v125_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_5d_3rd_derivatives_v126_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v127_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v128_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v129_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v130_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v131_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v132_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v133_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v134_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v135_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v136_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v137_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v138_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v139_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v140_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v141_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v142_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v143_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v144_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_issuance_cap(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v145_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_burn_accel(sharesbas, ncfcommon, cashneq, ncfo, 21).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v146_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_cash_buffer(sharesbas, ncfcommon, cashneq, ncfo, 63).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v147_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dilution(sharesbas, ncfcommon, cashneq, ncfo, 126).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v148_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_raise_burn(sharesbas, ncfcommon, cashneq, ncfo, 252).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v149_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_runway(sharesbas, ncfcommon, cashneq, ncfo, 504).diff(5).diff(5).diff(5) / 125.0

def f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v150_signal(sharesbas, ncfcommon, cashneq, ncfo):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    result = _f03jfd_dil_streak(sharesbas, ncfcommon, cashneq, ncfo, 5).diff(5).diff(5).diff(5) / 125.0

_FEATURES = [
    f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v001_signal,
    f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v002_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v003_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v004_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v005_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v006_signal,
    f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v007_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v008_signal,
    f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v009_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v010_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v011_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v012_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v013_signal,
    f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v014_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v015_signal,
    f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v016_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v017_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v018_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v019_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v020_signal,
    f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v021_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v022_signal,
    f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v023_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v024_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_21d_3rd_derivatives_v025_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_63d_3rd_derivatives_v026_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_126d_3rd_derivatives_v027_signal,
    f03jfd_f03_junior_financing_dilution_dilution_252d_3rd_derivatives_v028_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_504d_3rd_derivatives_v029_signal,
    f03jfd_f03_junior_financing_dilution_runway_5d_3rd_derivatives_v030_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_21d_3rd_derivatives_v031_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_63d_3rd_derivatives_v032_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_126d_3rd_derivatives_v033_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_252d_3rd_derivatives_v034_signal,
    f03jfd_f03_junior_financing_dilution_dilution_504d_3rd_derivatives_v035_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_5d_3rd_derivatives_v036_signal,
    f03jfd_f03_junior_financing_dilution_runway_21d_3rd_derivatives_v037_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_63d_3rd_derivatives_v038_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_126d_3rd_derivatives_v039_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_252d_3rd_derivatives_v040_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_504d_3rd_derivatives_v041_signal,
    f03jfd_f03_junior_financing_dilution_dilution_5d_3rd_derivatives_v042_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v043_signal,
    f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v044_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v045_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v046_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v047_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v048_signal,
    f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v049_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v050_signal,
    f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v051_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v052_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v053_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v054_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v055_signal,
    f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v056_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v057_signal,
    f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v058_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v059_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v060_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v061_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v062_signal,
    f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v063_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v064_signal,
    f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v065_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v066_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_21d_3rd_derivatives_v067_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_63d_3rd_derivatives_v068_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_126d_3rd_derivatives_v069_signal,
    f03jfd_f03_junior_financing_dilution_dilution_252d_3rd_derivatives_v070_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_504d_3rd_derivatives_v071_signal,
    f03jfd_f03_junior_financing_dilution_runway_5d_3rd_derivatives_v072_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_21d_3rd_derivatives_v073_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_63d_3rd_derivatives_v074_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_126d_3rd_derivatives_v075_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_252d_3rd_derivatives_v076_signal,
    f03jfd_f03_junior_financing_dilution_dilution_504d_3rd_derivatives_v077_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_5d_3rd_derivatives_v078_signal,
    f03jfd_f03_junior_financing_dilution_runway_21d_3rd_derivatives_v079_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_63d_3rd_derivatives_v080_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_126d_3rd_derivatives_v081_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_252d_3rd_derivatives_v082_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_504d_3rd_derivatives_v083_signal,
    f03jfd_f03_junior_financing_dilution_dilution_5d_3rd_derivatives_v084_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v085_signal,
    f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v086_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v087_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v088_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v089_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v090_signal,
    f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v091_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v092_signal,
    f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v093_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v094_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v095_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v096_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v097_signal,
    f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v098_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v099_signal,
    f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v100_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v101_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v102_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v103_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v104_signal,
    f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v105_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v106_signal,
    f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v107_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v108_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_21d_3rd_derivatives_v109_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_63d_3rd_derivatives_v110_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_126d_3rd_derivatives_v111_signal,
    f03jfd_f03_junior_financing_dilution_dilution_252d_3rd_derivatives_v112_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_504d_3rd_derivatives_v113_signal,
    f03jfd_f03_junior_financing_dilution_runway_5d_3rd_derivatives_v114_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_21d_3rd_derivatives_v115_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_63d_3rd_derivatives_v116_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_126d_3rd_derivatives_v117_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_252d_3rd_derivatives_v118_signal,
    f03jfd_f03_junior_financing_dilution_dilution_504d_3rd_derivatives_v119_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_5d_3rd_derivatives_v120_signal,
    f03jfd_f03_junior_financing_dilution_runway_21d_3rd_derivatives_v121_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_63d_3rd_derivatives_v122_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_126d_3rd_derivatives_v123_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_252d_3rd_derivatives_v124_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_504d_3rd_derivatives_v125_signal,
    f03jfd_f03_junior_financing_dilution_dilution_5d_3rd_derivatives_v126_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_21d_3rd_derivatives_v127_signal,
    f03jfd_f03_junior_financing_dilution_runway_63d_3rd_derivatives_v128_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_126d_3rd_derivatives_v129_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_252d_3rd_derivatives_v130_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_504d_3rd_derivatives_v131_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_5d_3rd_derivatives_v132_signal,
    f03jfd_f03_junior_financing_dilution_dilution_21d_3rd_derivatives_v133_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_63d_3rd_derivatives_v134_signal,
    f03jfd_f03_junior_financing_dilution_runway_126d_3rd_derivatives_v135_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_252d_3rd_derivatives_v136_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_504d_3rd_derivatives_v137_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_5d_3rd_derivatives_v138_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_21d_3rd_derivatives_v139_signal,
    f03jfd_f03_junior_financing_dilution_dilution_63d_3rd_derivatives_v140_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_126d_3rd_derivatives_v141_signal,
    f03jfd_f03_junior_financing_dilution_runway_252d_3rd_derivatives_v142_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_504d_3rd_derivatives_v143_signal,
    f03jfd_f03_junior_financing_dilution_issuance_cap_5d_3rd_derivatives_v144_signal,
    f03jfd_f03_junior_financing_dilution_burn_accel_21d_3rd_derivatives_v145_signal,
    f03jfd_f03_junior_financing_dilution_cash_buffer_63d_3rd_derivatives_v146_signal,
    f03jfd_f03_junior_financing_dilution_dilution_126d_3rd_derivatives_v147_signal,
    f03jfd_f03_junior_financing_dilution_raise_burn_252d_3rd_derivatives_v148_signal,
    f03jfd_f03_junior_financing_dilution_runway_504d_3rd_derivatives_v149_signal,
    f03jfd_f03_junior_financing_dilution_dil_streak_5d_3rd_derivatives_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F03_JUNIOR_FINANCING_DILUTION_REGISTRY = REGISTRY

if __name__ == "__main__":
    import os
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg: s = s - base * 0.5
        return pd.Series(s, name=None)

    cols = {
        "closeadj": closeadj, "close": close, "open": openp,
        "high": high, "low": low, "volume": volume,
        "opinc": _fund(1, allow_neg=True), "revenue": _fund(2), "opex": _fund(3),
        "gp": _fund(4, allow_neg=True), "ebit": _fund(5, allow_neg=True),
        "sharesbas": _fund(6, base=1e7, vol=0.02), "ncfcommon": _fund(7, base=1e6, allow_neg=True),
        "cashneq": _fund(8), "ncfo": _fund(9, allow_neg=True),
        "capex": _fund(10), "assets": _fund(11), "ppnenet": _fund(12),
        "pe": _fund(13, base=15, vol=0.1), "evebitda": _fund(14, base=10, vol=0.1),
        "marketcap": _fund(15, base=1e9), "inventory": _fund(16), "cor": _fund(17),
        "debt": _fund(18), "liabilities": _fund(19), "equity": _fund(20),
        "netinc": _fund(21, allow_neg=True), "ebitda": _fund(22, allow_neg=True),
        "roic": _fund(23, base=0.1, vol=0.05, allow_neg=True),
        "fcf": _fund(24, allow_neg=True), "pb": _fund(25, base=2, vol=0.1),
        "shrholders": _fund(26, base=100, vol=0.05), "totalvalue": _fund(27, base=1e8),
        "percentoftotal": _fund(28, base=0.2, vol=0.02), "currentratio": _fund(29, base=1.5, vol=0.1),
        "workingcapital": _fund(30, allow_neg=True), "retearn": _fund(31, allow_neg=True),
        "ncff": _fund(32, allow_neg=True), "ncfi": _fund(33, allow_neg=True),
        "debtusd": _fund(34), "tangibles": _fund(35), "intangibles": _fund(36),
        "rnd": _fund(37), "sgna": _fund(38), "receivables": _fund(39), "payables": _fund(40),
        "assetsc": _fund(41), "investmentsnc": _fund(42), "depamor": _fund(43),
        "eps": _fund(44, allow_neg=True), "fcfps": _fund(45, allow_neg=True),
        "ev": _fund(46, base=1.2e9), "shrvalue": _fund(47, base=1e7), "shrunits": _fund(48, base=1e5),
        "fndholders": _fund(49, base=50), "undholders": _fund(50, base=10), "prfholders": _fund(51, base=5),
        "dbtholders": _fund(52, base=20)
    }

    n_features = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y = fn(*args)
        q = y.iloc[504:].dropna()
        if len(q) > 0 and q.nunique() > 10:
            results[name] = y.iloc[504:]
            n_features += 1

    print(f"OK {os.path.basename(__file__)}: {n_features} features pass")
