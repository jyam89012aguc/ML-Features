"""
Family: Inventory Liquidation Stress
Sector: Operations
Mathematical Approach: Liquidity/Fundamental
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

def _inventory_liquidation_stress_velocity(inventory, cashneq, cor, w):
    return inventory.diff(w) / cashneq.rolling(w).mean().abs()

def _inventory_liquidation_stress_impulse(inventory, cashneq, cor, w):
    return _z(inventory, w) - _z(cashneq, w)

def _inventory_liquidation_stress_regime(inventory, cashneq, cor, w):
    return inventory.pct_change(w)

def _inventory_liquidation_stress_dispersion(inventory, cashneq, cor, w):
    return np.log(inventory.replace(0, np.nan) / inventory.rolling(w).mean())

def _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, w):
    return inventory.rolling(w).std() / inventory.rolling(w).mean().abs()

def f41il_f41_inventory_liquidation_stress_prim2_21d_base_v001_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_63d_base_v002_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_126d_base_v003_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 126))

def f41il_f41_inventory_liquidation_stress_prim5_252d_base_v004_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_504d_base_v005_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 504)

def f41il_f41_inventory_liquidation_stress_prim2_5d_base_v006_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_21d_base_v007_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_63d_base_v008_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 63))

def f41il_f41_inventory_liquidation_stress_prim5_126d_base_v009_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_252d_base_v010_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 252)

def f41il_f41_inventory_liquidation_stress_prim2_504d_base_v011_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_5d_base_v012_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_21d_base_v013_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 21))

def f41il_f41_inventory_liquidation_stress_prim5_63d_base_v014_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_126d_base_v015_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 126)

def f41il_f41_inventory_liquidation_stress_prim2_252d_base_v016_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 252)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_504d_base_v017_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 504)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_5d_base_v018_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 5))

def f41il_f41_inventory_liquidation_stress_prim5_21d_base_v019_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 21)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_63d_base_v020_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 63)

def f41il_f41_inventory_liquidation_stress_prim2_126d_base_v021_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 126)
    result = _z(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_252d_base_v022_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 252)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_504d_base_v023_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 504))

def f41il_f41_inventory_liquidation_stress_prim5_5d_base_v024_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 5)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_21d_base_v025_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 21)

def f41il_f41_inventory_liquidation_stress_prim2_63d_base_v026_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 63)
    result = _z(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_126d_base_v027_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 126)
    result = _rank(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_252d_base_v028_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 252))

def f41il_f41_inventory_liquidation_stress_prim5_504d_base_v029_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 504)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_5d_base_v030_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 5)

def f41il_f41_inventory_liquidation_stress_prim2_21d_base_v031_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_63d_base_v032_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_126d_base_v033_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 126))

def f41il_f41_inventory_liquidation_stress_prim5_252d_base_v034_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_504d_base_v035_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 504)

def f41il_f41_inventory_liquidation_stress_prim2_5d_base_v036_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_21d_base_v037_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_63d_base_v038_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 63))

def f41il_f41_inventory_liquidation_stress_prim5_126d_base_v039_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_252d_base_v040_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 252)

def f41il_f41_inventory_liquidation_stress_prim2_504d_base_v041_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_5d_base_v042_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_21d_base_v043_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 21))

def f41il_f41_inventory_liquidation_stress_prim5_63d_base_v044_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_126d_base_v045_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 126)

def f41il_f41_inventory_liquidation_stress_prim2_252d_base_v046_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 252)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_504d_base_v047_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 504)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_5d_base_v048_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 5))

def f41il_f41_inventory_liquidation_stress_prim5_21d_base_v049_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 21)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_63d_base_v050_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 63)

def f41il_f41_inventory_liquidation_stress_prim2_126d_base_v051_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 126)
    result = _z(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_252d_base_v052_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 252)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_504d_base_v053_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 504))

def f41il_f41_inventory_liquidation_stress_prim5_5d_base_v054_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 5)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_21d_base_v055_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 21)

def f41il_f41_inventory_liquidation_stress_prim2_63d_base_v056_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 63)
    result = _z(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_126d_base_v057_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 126)
    result = _rank(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_252d_base_v058_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 252))

def f41il_f41_inventory_liquidation_stress_prim5_504d_base_v059_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 504)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_5d_base_v060_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 5)

def f41il_f41_inventory_liquidation_stress_prim2_21d_base_v061_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_63d_base_v062_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_126d_base_v063_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 126))

def f41il_f41_inventory_liquidation_stress_prim5_252d_base_v064_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_504d_base_v065_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 504)

def f41il_f41_inventory_liquidation_stress_prim2_5d_base_v066_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_21d_base_v067_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_63d_base_v068_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 63))

def f41il_f41_inventory_liquidation_stress_prim5_126d_base_v069_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_252d_base_v070_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 252)

def f41il_f41_inventory_liquidation_stress_prim2_504d_base_v071_signal(inventory, cashneq, cor):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _inventory_liquidation_stress_impulse(inventory, cashneq, cor, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim3_5d_base_v072_signal(inventory, cashneq, cor):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _inventory_liquidation_stress_regime(inventory, cashneq, cor, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim4_21d_base_v073_signal(inventory, cashneq, cor):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_inventory_liquidation_stress_dispersion(inventory, cashneq, cor, 21))

def f41il_f41_inventory_liquidation_stress_prim5_63d_base_v074_signal(inventory, cashneq, cor):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _inventory_liquidation_stress_efficiency(inventory, cashneq, cor, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f41il_f41_inventory_liquidation_stress_prim1_126d_base_v075_signal(inventory, cashneq, cor):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _inventory_liquidation_stress_velocity(inventory, cashneq, cor, 126)

_FEATURES = [
    f41il_f41_inventory_liquidation_stress_prim2_21d_base_v001_signal,
    f41il_f41_inventory_liquidation_stress_prim3_63d_base_v002_signal,
    f41il_f41_inventory_liquidation_stress_prim4_126d_base_v003_signal,
    f41il_f41_inventory_liquidation_stress_prim5_252d_base_v004_signal,
    f41il_f41_inventory_liquidation_stress_prim1_504d_base_v005_signal,
    f41il_f41_inventory_liquidation_stress_prim2_5d_base_v006_signal,
    f41il_f41_inventory_liquidation_stress_prim3_21d_base_v007_signal,
    f41il_f41_inventory_liquidation_stress_prim4_63d_base_v008_signal,
    f41il_f41_inventory_liquidation_stress_prim5_126d_base_v009_signal,
    f41il_f41_inventory_liquidation_stress_prim1_252d_base_v010_signal,
    f41il_f41_inventory_liquidation_stress_prim2_504d_base_v011_signal,
    f41il_f41_inventory_liquidation_stress_prim3_5d_base_v012_signal,
    f41il_f41_inventory_liquidation_stress_prim4_21d_base_v013_signal,
    f41il_f41_inventory_liquidation_stress_prim5_63d_base_v014_signal,
    f41il_f41_inventory_liquidation_stress_prim1_126d_base_v015_signal,
    f41il_f41_inventory_liquidation_stress_prim2_252d_base_v016_signal,
    f41il_f41_inventory_liquidation_stress_prim3_504d_base_v017_signal,
    f41il_f41_inventory_liquidation_stress_prim4_5d_base_v018_signal,
    f41il_f41_inventory_liquidation_stress_prim5_21d_base_v019_signal,
    f41il_f41_inventory_liquidation_stress_prim1_63d_base_v020_signal,
    f41il_f41_inventory_liquidation_stress_prim2_126d_base_v021_signal,
    f41il_f41_inventory_liquidation_stress_prim3_252d_base_v022_signal,
    f41il_f41_inventory_liquidation_stress_prim4_504d_base_v023_signal,
    f41il_f41_inventory_liquidation_stress_prim5_5d_base_v024_signal,
    f41il_f41_inventory_liquidation_stress_prim1_21d_base_v025_signal,
    f41il_f41_inventory_liquidation_stress_prim2_63d_base_v026_signal,
    f41il_f41_inventory_liquidation_stress_prim3_126d_base_v027_signal,
    f41il_f41_inventory_liquidation_stress_prim4_252d_base_v028_signal,
    f41il_f41_inventory_liquidation_stress_prim5_504d_base_v029_signal,
    f41il_f41_inventory_liquidation_stress_prim1_5d_base_v030_signal,
    f41il_f41_inventory_liquidation_stress_prim2_21d_base_v031_signal,
    f41il_f41_inventory_liquidation_stress_prim3_63d_base_v032_signal,
    f41il_f41_inventory_liquidation_stress_prim4_126d_base_v033_signal,
    f41il_f41_inventory_liquidation_stress_prim5_252d_base_v034_signal,
    f41il_f41_inventory_liquidation_stress_prim1_504d_base_v035_signal,
    f41il_f41_inventory_liquidation_stress_prim2_5d_base_v036_signal,
    f41il_f41_inventory_liquidation_stress_prim3_21d_base_v037_signal,
    f41il_f41_inventory_liquidation_stress_prim4_63d_base_v038_signal,
    f41il_f41_inventory_liquidation_stress_prim5_126d_base_v039_signal,
    f41il_f41_inventory_liquidation_stress_prim1_252d_base_v040_signal,
    f41il_f41_inventory_liquidation_stress_prim2_504d_base_v041_signal,
    f41il_f41_inventory_liquidation_stress_prim3_5d_base_v042_signal,
    f41il_f41_inventory_liquidation_stress_prim4_21d_base_v043_signal,
    f41il_f41_inventory_liquidation_stress_prim5_63d_base_v044_signal,
    f41il_f41_inventory_liquidation_stress_prim1_126d_base_v045_signal,
    f41il_f41_inventory_liquidation_stress_prim2_252d_base_v046_signal,
    f41il_f41_inventory_liquidation_stress_prim3_504d_base_v047_signal,
    f41il_f41_inventory_liquidation_stress_prim4_5d_base_v048_signal,
    f41il_f41_inventory_liquidation_stress_prim5_21d_base_v049_signal,
    f41il_f41_inventory_liquidation_stress_prim1_63d_base_v050_signal,
    f41il_f41_inventory_liquidation_stress_prim2_126d_base_v051_signal,
    f41il_f41_inventory_liquidation_stress_prim3_252d_base_v052_signal,
    f41il_f41_inventory_liquidation_stress_prim4_504d_base_v053_signal,
    f41il_f41_inventory_liquidation_stress_prim5_5d_base_v054_signal,
    f41il_f41_inventory_liquidation_stress_prim1_21d_base_v055_signal,
    f41il_f41_inventory_liquidation_stress_prim2_63d_base_v056_signal,
    f41il_f41_inventory_liquidation_stress_prim3_126d_base_v057_signal,
    f41il_f41_inventory_liquidation_stress_prim4_252d_base_v058_signal,
    f41il_f41_inventory_liquidation_stress_prim5_504d_base_v059_signal,
    f41il_f41_inventory_liquidation_stress_prim1_5d_base_v060_signal,
    f41il_f41_inventory_liquidation_stress_prim2_21d_base_v061_signal,
    f41il_f41_inventory_liquidation_stress_prim3_63d_base_v062_signal,
    f41il_f41_inventory_liquidation_stress_prim4_126d_base_v063_signal,
    f41il_f41_inventory_liquidation_stress_prim5_252d_base_v064_signal,
    f41il_f41_inventory_liquidation_stress_prim1_504d_base_v065_signal,
    f41il_f41_inventory_liquidation_stress_prim2_5d_base_v066_signal,
    f41il_f41_inventory_liquidation_stress_prim3_21d_base_v067_signal,
    f41il_f41_inventory_liquidation_stress_prim4_63d_base_v068_signal,
    f41il_f41_inventory_liquidation_stress_prim5_126d_base_v069_signal,
    f41il_f41_inventory_liquidation_stress_prim1_252d_base_v070_signal,
    f41il_f41_inventory_liquidation_stress_prim2_504d_base_v071_signal,
    f41il_f41_inventory_liquidation_stress_prim3_5d_base_v072_signal,
    f41il_f41_inventory_liquidation_stress_prim4_21d_base_v073_signal,
    f41il_f41_inventory_liquidation_stress_prim5_63d_base_v074_signal,
    f41il_f41_inventory_liquidation_stress_prim1_126d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F41_INVENTORY_LIQUIDATION_STRESS_REGISTRY = REGISTRY

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
