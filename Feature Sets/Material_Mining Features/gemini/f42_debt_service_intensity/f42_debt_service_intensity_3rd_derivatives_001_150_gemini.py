"""
Family: Debt Service Intensity
Sector: Financial
Mathematical Approach: Fundamental/Leverage
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

def _debt_service_intensity_velocity(ebit, ncfdebt, debt, w):
    return ebit.diff(w) / ncfdebt.rolling(w).mean().abs()

def _debt_service_intensity_impulse(ebit, ncfdebt, debt, w):
    return _z(ebit, w) - _z(ncfdebt, w)

def _debt_service_intensity_regime(ebit, ncfdebt, debt, w):
    return ebit.pct_change(w)

def _debt_service_intensity_dispersion(ebit, ncfdebt, debt, w):
    return np.log(ebit.replace(0, np.nan) / ebit.rolling(w).mean())

def _debt_service_intensity_efficiency(ebit, ncfdebt, debt, w):
    return ebit.rolling(w).std() / ebit.rolling(w).mean().abs()

def f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v001_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v002_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v003_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v004_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v005_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v006_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v007_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v008_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v009_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v010_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v011_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v012_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v013_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v014_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v015_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v016_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v017_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v018_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v019_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v020_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v021_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v022_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v023_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v024_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v025_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v026_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v027_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v028_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v029_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v030_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v031_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v032_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v033_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v034_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v035_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v036_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v037_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v038_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v039_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v040_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v041_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v042_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v043_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v044_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v045_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v046_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v047_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v048_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v049_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v050_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v051_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v052_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v053_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v054_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v055_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v056_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v057_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v058_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v059_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v060_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v061_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v062_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v063_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v064_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v065_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v066_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v067_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v068_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v069_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v070_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v071_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v072_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v073_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v074_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v075_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v076_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v077_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v078_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v079_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v080_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v081_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v082_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v083_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v084_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v085_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v086_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v087_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v088_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v089_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v090_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v091_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v092_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v093_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v094_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v095_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v096_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v097_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v098_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v099_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v100_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v101_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v102_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v103_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v104_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v105_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v106_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v107_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v108_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v109_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v110_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v111_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v112_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v113_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v114_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v115_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v116_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v117_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v118_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v119_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v120_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v121_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v122_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v123_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v124_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v125_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v126_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v127_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v128_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v129_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v130_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v131_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v132_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v133_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v134_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v135_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v136_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v137_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v138_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v139_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v140_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v141_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v142_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v143_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v144_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v145_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v146_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_impulse(ebit, ncfdebt, debt, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v147_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_regime(ebit, ncfdebt, debt, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v148_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_dispersion(ebit, ncfdebt, debt, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v149_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_efficiency(ebit, ncfdebt, debt, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v150_signal(ebit, ncfdebt, debt):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _debt_service_intensity_velocity(ebit, ncfdebt, debt, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v001_signal,
    f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v002_signal,
    f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v003_signal,
    f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v004_signal,
    f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v005_signal,
    f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v006_signal,
    f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v007_signal,
    f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v008_signal,
    f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v009_signal,
    f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v010_signal,
    f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v011_signal,
    f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v012_signal,
    f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v013_signal,
    f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v014_signal,
    f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v015_signal,
    f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v016_signal,
    f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v017_signal,
    f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v018_signal,
    f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v019_signal,
    f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v020_signal,
    f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v021_signal,
    f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v022_signal,
    f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v023_signal,
    f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v024_signal,
    f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v025_signal,
    f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v026_signal,
    f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v027_signal,
    f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v028_signal,
    f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v029_signal,
    f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v030_signal,
    f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v031_signal,
    f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v032_signal,
    f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v033_signal,
    f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v034_signal,
    f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v035_signal,
    f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v036_signal,
    f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v037_signal,
    f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v038_signal,
    f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v039_signal,
    f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v040_signal,
    f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v041_signal,
    f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v042_signal,
    f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v043_signal,
    f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v044_signal,
    f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v045_signal,
    f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v046_signal,
    f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v047_signal,
    f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v048_signal,
    f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v049_signal,
    f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v050_signal,
    f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v051_signal,
    f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v052_signal,
    f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v053_signal,
    f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v054_signal,
    f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v055_signal,
    f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v056_signal,
    f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v057_signal,
    f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v058_signal,
    f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v059_signal,
    f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v060_signal,
    f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v061_signal,
    f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v062_signal,
    f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v063_signal,
    f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v064_signal,
    f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v065_signal,
    f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v066_signal,
    f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v067_signal,
    f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v068_signal,
    f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v069_signal,
    f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v070_signal,
    f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v071_signal,
    f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v072_signal,
    f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v073_signal,
    f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v074_signal,
    f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v075_signal,
    f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v076_signal,
    f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v077_signal,
    f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v078_signal,
    f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v079_signal,
    f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v080_signal,
    f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v081_signal,
    f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v082_signal,
    f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v083_signal,
    f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v084_signal,
    f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v085_signal,
    f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v086_signal,
    f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v087_signal,
    f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v088_signal,
    f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v089_signal,
    f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v090_signal,
    f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v091_signal,
    f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v092_signal,
    f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v093_signal,
    f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v094_signal,
    f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v095_signal,
    f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v096_signal,
    f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v097_signal,
    f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v098_signal,
    f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v099_signal,
    f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v100_signal,
    f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v101_signal,
    f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v102_signal,
    f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v103_signal,
    f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v104_signal,
    f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v105_signal,
    f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v106_signal,
    f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v107_signal,
    f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v108_signal,
    f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v109_signal,
    f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v110_signal,
    f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v111_signal,
    f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v112_signal,
    f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v113_signal,
    f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v114_signal,
    f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v115_signal,
    f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v116_signal,
    f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v117_signal,
    f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v118_signal,
    f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v119_signal,
    f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v120_signal,
    f42ds_f42_debt_service_intensity_prim2_21d_3rd_derivatives_v121_signal,
    f42ds_f42_debt_service_intensity_prim3_63d_3rd_derivatives_v122_signal,
    f42ds_f42_debt_service_intensity_prim4_126d_3rd_derivatives_v123_signal,
    f42ds_f42_debt_service_intensity_prim5_252d_3rd_derivatives_v124_signal,
    f42ds_f42_debt_service_intensity_prim1_504d_3rd_derivatives_v125_signal,
    f42ds_f42_debt_service_intensity_prim2_5d_3rd_derivatives_v126_signal,
    f42ds_f42_debt_service_intensity_prim3_21d_3rd_derivatives_v127_signal,
    f42ds_f42_debt_service_intensity_prim4_63d_3rd_derivatives_v128_signal,
    f42ds_f42_debt_service_intensity_prim5_126d_3rd_derivatives_v129_signal,
    f42ds_f42_debt_service_intensity_prim1_252d_3rd_derivatives_v130_signal,
    f42ds_f42_debt_service_intensity_prim2_504d_3rd_derivatives_v131_signal,
    f42ds_f42_debt_service_intensity_prim3_5d_3rd_derivatives_v132_signal,
    f42ds_f42_debt_service_intensity_prim4_21d_3rd_derivatives_v133_signal,
    f42ds_f42_debt_service_intensity_prim5_63d_3rd_derivatives_v134_signal,
    f42ds_f42_debt_service_intensity_prim1_126d_3rd_derivatives_v135_signal,
    f42ds_f42_debt_service_intensity_prim2_252d_3rd_derivatives_v136_signal,
    f42ds_f42_debt_service_intensity_prim3_504d_3rd_derivatives_v137_signal,
    f42ds_f42_debt_service_intensity_prim4_5d_3rd_derivatives_v138_signal,
    f42ds_f42_debt_service_intensity_prim5_21d_3rd_derivatives_v139_signal,
    f42ds_f42_debt_service_intensity_prim1_63d_3rd_derivatives_v140_signal,
    f42ds_f42_debt_service_intensity_prim2_126d_3rd_derivatives_v141_signal,
    f42ds_f42_debt_service_intensity_prim3_252d_3rd_derivatives_v142_signal,
    f42ds_f42_debt_service_intensity_prim4_504d_3rd_derivatives_v143_signal,
    f42ds_f42_debt_service_intensity_prim5_5d_3rd_derivatives_v144_signal,
    f42ds_f42_debt_service_intensity_prim1_21d_3rd_derivatives_v145_signal,
    f42ds_f42_debt_service_intensity_prim2_63d_3rd_derivatives_v146_signal,
    f42ds_f42_debt_service_intensity_prim3_126d_3rd_derivatives_v147_signal,
    f42ds_f42_debt_service_intensity_prim4_252d_3rd_derivatives_v148_signal,
    f42ds_f42_debt_service_intensity_prim5_504d_3rd_derivatives_v149_signal,
    f42ds_f42_debt_service_intensity_prim1_5d_3rd_derivatives_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F42_DEBT_SERVICE_INTENSITY_REGISTRY = REGISTRY

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
