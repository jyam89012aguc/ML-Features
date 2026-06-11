"""
Family: Resource Quality Degradation
Sector: Mining
Mathematical Approach: Operational/Quality
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

def _resource_quality_degradation_velocity(cor, revenue, assets, w):
    return cor.diff(w) / revenue.rolling(w).mean().abs()

def _resource_quality_degradation_impulse(cor, revenue, assets, w):
    return _z(cor, w) - _z(revenue, w)

def _resource_quality_degradation_regime(cor, revenue, assets, w):
    return cor.pct_change(w)

def _resource_quality_degradation_dispersion(cor, revenue, assets, w):
    return np.log(cor.replace(0, np.nan) / cor.rolling(w).mean())

def _resource_quality_degradation_efficiency(cor, revenue, assets, w):
    return cor.rolling(w).std() / cor.rolling(w).mean().abs()

def f27rq_f27_resource_quality_degradation_prim2_21d_base_v001_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_63d_base_v002_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_126d_base_v003_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 126))

def f27rq_f27_resource_quality_degradation_prim5_252d_base_v004_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_504d_base_v005_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 504)

def f27rq_f27_resource_quality_degradation_prim2_5d_base_v006_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_21d_base_v007_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_63d_base_v008_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 63))

def f27rq_f27_resource_quality_degradation_prim5_126d_base_v009_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_252d_base_v010_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 252)

def f27rq_f27_resource_quality_degradation_prim2_504d_base_v011_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_5d_base_v012_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_21d_base_v013_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 21))

def f27rq_f27_resource_quality_degradation_prim5_63d_base_v014_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_126d_base_v015_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 126)

def f27rq_f27_resource_quality_degradation_prim2_252d_base_v016_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 252)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_504d_base_v017_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 504)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_5d_base_v018_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 5))

def f27rq_f27_resource_quality_degradation_prim5_21d_base_v019_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 21)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_63d_base_v020_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 63)

def f27rq_f27_resource_quality_degradation_prim2_126d_base_v021_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 126)
    result = _z(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_252d_base_v022_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 252)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_504d_base_v023_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 504))

def f27rq_f27_resource_quality_degradation_prim5_5d_base_v024_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 5)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_21d_base_v025_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 21)

def f27rq_f27_resource_quality_degradation_prim2_63d_base_v026_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 63)
    result = _z(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_126d_base_v027_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 126)
    result = _rank(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_252d_base_v028_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 252))

def f27rq_f27_resource_quality_degradation_prim5_504d_base_v029_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 504)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_5d_base_v030_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 5)

def f27rq_f27_resource_quality_degradation_prim2_21d_base_v031_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_63d_base_v032_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_126d_base_v033_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 126))

def f27rq_f27_resource_quality_degradation_prim5_252d_base_v034_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_504d_base_v035_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 504)

def f27rq_f27_resource_quality_degradation_prim2_5d_base_v036_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_21d_base_v037_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_63d_base_v038_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 63))

def f27rq_f27_resource_quality_degradation_prim5_126d_base_v039_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_252d_base_v040_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 252)

def f27rq_f27_resource_quality_degradation_prim2_504d_base_v041_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_5d_base_v042_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_21d_base_v043_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 21))

def f27rq_f27_resource_quality_degradation_prim5_63d_base_v044_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_126d_base_v045_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 126)

def f27rq_f27_resource_quality_degradation_prim2_252d_base_v046_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 252)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_504d_base_v047_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 504)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_5d_base_v048_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 5))

def f27rq_f27_resource_quality_degradation_prim5_21d_base_v049_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 21)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_63d_base_v050_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 63)

def f27rq_f27_resource_quality_degradation_prim2_126d_base_v051_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 126)
    result = _z(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_252d_base_v052_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 252)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_504d_base_v053_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 504))

def f27rq_f27_resource_quality_degradation_prim5_5d_base_v054_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 5)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_21d_base_v055_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 21)

def f27rq_f27_resource_quality_degradation_prim2_63d_base_v056_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 63)
    result = _z(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_126d_base_v057_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 126)
    result = _rank(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_252d_base_v058_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 252))

def f27rq_f27_resource_quality_degradation_prim5_504d_base_v059_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 504)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_5d_base_v060_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 5)

def f27rq_f27_resource_quality_degradation_prim2_21d_base_v061_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_63d_base_v062_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_126d_base_v063_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 126))

def f27rq_f27_resource_quality_degradation_prim5_252d_base_v064_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_504d_base_v065_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 504)

def f27rq_f27_resource_quality_degradation_prim2_5d_base_v066_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_21d_base_v067_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_63d_base_v068_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 63))

def f27rq_f27_resource_quality_degradation_prim5_126d_base_v069_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_252d_base_v070_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 252)

def f27rq_f27_resource_quality_degradation_prim2_504d_base_v071_signal(cor, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _resource_quality_degradation_impulse(cor, revenue, assets, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim3_5d_base_v072_signal(cor, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _resource_quality_degradation_regime(cor, revenue, assets, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim4_21d_base_v073_signal(cor, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_resource_quality_degradation_dispersion(cor, revenue, assets, 21))

def f27rq_f27_resource_quality_degradation_prim5_63d_base_v074_signal(cor, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _resource_quality_degradation_efficiency(cor, revenue, assets, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27rq_f27_resource_quality_degradation_prim1_126d_base_v075_signal(cor, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _resource_quality_degradation_velocity(cor, revenue, assets, 126)

_FEATURES = [
    f27rq_f27_resource_quality_degradation_prim2_21d_base_v001_signal,
    f27rq_f27_resource_quality_degradation_prim3_63d_base_v002_signal,
    f27rq_f27_resource_quality_degradation_prim4_126d_base_v003_signal,
    f27rq_f27_resource_quality_degradation_prim5_252d_base_v004_signal,
    f27rq_f27_resource_quality_degradation_prim1_504d_base_v005_signal,
    f27rq_f27_resource_quality_degradation_prim2_5d_base_v006_signal,
    f27rq_f27_resource_quality_degradation_prim3_21d_base_v007_signal,
    f27rq_f27_resource_quality_degradation_prim4_63d_base_v008_signal,
    f27rq_f27_resource_quality_degradation_prim5_126d_base_v009_signal,
    f27rq_f27_resource_quality_degradation_prim1_252d_base_v010_signal,
    f27rq_f27_resource_quality_degradation_prim2_504d_base_v011_signal,
    f27rq_f27_resource_quality_degradation_prim3_5d_base_v012_signal,
    f27rq_f27_resource_quality_degradation_prim4_21d_base_v013_signal,
    f27rq_f27_resource_quality_degradation_prim5_63d_base_v014_signal,
    f27rq_f27_resource_quality_degradation_prim1_126d_base_v015_signal,
    f27rq_f27_resource_quality_degradation_prim2_252d_base_v016_signal,
    f27rq_f27_resource_quality_degradation_prim3_504d_base_v017_signal,
    f27rq_f27_resource_quality_degradation_prim4_5d_base_v018_signal,
    f27rq_f27_resource_quality_degradation_prim5_21d_base_v019_signal,
    f27rq_f27_resource_quality_degradation_prim1_63d_base_v020_signal,
    f27rq_f27_resource_quality_degradation_prim2_126d_base_v021_signal,
    f27rq_f27_resource_quality_degradation_prim3_252d_base_v022_signal,
    f27rq_f27_resource_quality_degradation_prim4_504d_base_v023_signal,
    f27rq_f27_resource_quality_degradation_prim5_5d_base_v024_signal,
    f27rq_f27_resource_quality_degradation_prim1_21d_base_v025_signal,
    f27rq_f27_resource_quality_degradation_prim2_63d_base_v026_signal,
    f27rq_f27_resource_quality_degradation_prim3_126d_base_v027_signal,
    f27rq_f27_resource_quality_degradation_prim4_252d_base_v028_signal,
    f27rq_f27_resource_quality_degradation_prim5_504d_base_v029_signal,
    f27rq_f27_resource_quality_degradation_prim1_5d_base_v030_signal,
    f27rq_f27_resource_quality_degradation_prim2_21d_base_v031_signal,
    f27rq_f27_resource_quality_degradation_prim3_63d_base_v032_signal,
    f27rq_f27_resource_quality_degradation_prim4_126d_base_v033_signal,
    f27rq_f27_resource_quality_degradation_prim5_252d_base_v034_signal,
    f27rq_f27_resource_quality_degradation_prim1_504d_base_v035_signal,
    f27rq_f27_resource_quality_degradation_prim2_5d_base_v036_signal,
    f27rq_f27_resource_quality_degradation_prim3_21d_base_v037_signal,
    f27rq_f27_resource_quality_degradation_prim4_63d_base_v038_signal,
    f27rq_f27_resource_quality_degradation_prim5_126d_base_v039_signal,
    f27rq_f27_resource_quality_degradation_prim1_252d_base_v040_signal,
    f27rq_f27_resource_quality_degradation_prim2_504d_base_v041_signal,
    f27rq_f27_resource_quality_degradation_prim3_5d_base_v042_signal,
    f27rq_f27_resource_quality_degradation_prim4_21d_base_v043_signal,
    f27rq_f27_resource_quality_degradation_prim5_63d_base_v044_signal,
    f27rq_f27_resource_quality_degradation_prim1_126d_base_v045_signal,
    f27rq_f27_resource_quality_degradation_prim2_252d_base_v046_signal,
    f27rq_f27_resource_quality_degradation_prim3_504d_base_v047_signal,
    f27rq_f27_resource_quality_degradation_prim4_5d_base_v048_signal,
    f27rq_f27_resource_quality_degradation_prim5_21d_base_v049_signal,
    f27rq_f27_resource_quality_degradation_prim1_63d_base_v050_signal,
    f27rq_f27_resource_quality_degradation_prim2_126d_base_v051_signal,
    f27rq_f27_resource_quality_degradation_prim3_252d_base_v052_signal,
    f27rq_f27_resource_quality_degradation_prim4_504d_base_v053_signal,
    f27rq_f27_resource_quality_degradation_prim5_5d_base_v054_signal,
    f27rq_f27_resource_quality_degradation_prim1_21d_base_v055_signal,
    f27rq_f27_resource_quality_degradation_prim2_63d_base_v056_signal,
    f27rq_f27_resource_quality_degradation_prim3_126d_base_v057_signal,
    f27rq_f27_resource_quality_degradation_prim4_252d_base_v058_signal,
    f27rq_f27_resource_quality_degradation_prim5_504d_base_v059_signal,
    f27rq_f27_resource_quality_degradation_prim1_5d_base_v060_signal,
    f27rq_f27_resource_quality_degradation_prim2_21d_base_v061_signal,
    f27rq_f27_resource_quality_degradation_prim3_63d_base_v062_signal,
    f27rq_f27_resource_quality_degradation_prim4_126d_base_v063_signal,
    f27rq_f27_resource_quality_degradation_prim5_252d_base_v064_signal,
    f27rq_f27_resource_quality_degradation_prim1_504d_base_v065_signal,
    f27rq_f27_resource_quality_degradation_prim2_5d_base_v066_signal,
    f27rq_f27_resource_quality_degradation_prim3_21d_base_v067_signal,
    f27rq_f27_resource_quality_degradation_prim4_63d_base_v068_signal,
    f27rq_f27_resource_quality_degradation_prim5_126d_base_v069_signal,
    f27rq_f27_resource_quality_degradation_prim1_252d_base_v070_signal,
    f27rq_f27_resource_quality_degradation_prim2_504d_base_v071_signal,
    f27rq_f27_resource_quality_degradation_prim3_5d_base_v072_signal,
    f27rq_f27_resource_quality_degradation_prim4_21d_base_v073_signal,
    f27rq_f27_resource_quality_degradation_prim5_63d_base_v074_signal,
    f27rq_f27_resource_quality_degradation_prim1_126d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F27_RESOURCE_QUALITY_DEGRADATION_REGISTRY = REGISTRY

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
