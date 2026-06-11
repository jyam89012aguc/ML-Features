"""
Family: Exploration Volatility Shocks
Sector: Exploration
Mathematical Approach: Volatility
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

def _f04ev_range_pct(closeadj, volume, high, low, w):
    return (high - low) / closeadj

def _f04ev_vol_surge(closeadj, volume, high, low, w):
    return volume / volume.rolling(w).mean()

def _f04ev_real_vol(closeadj, volume, high, low, w):
    return closeadj.pct_change().rolling(w).std()

def _f04ev_max_range(closeadj, volume, high, low, w):
    return ((high - low) / closeadj).rolling(w).max()

def _f04ev_vol_mom(closeadj, volume, high, low, w):
    return volume.diff(w) / volume.shift(w)

def _f04ev_shock_score(closeadj, volume, high, low, w):
    return ((high - low) / closeadj) * (volume / volume.rolling(w).mean())

def _f04ev_range_z(closeadj, volume, high, low, w):
    return _z((high-low)/closeadj, w)

def f04ev_f04_exploration_volatility_shocks_vol_surge_21d_base_v001_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_vol_surge(closeadj, volume, high, low, 21), 42)

def f04ev_f04_exploration_volatility_shocks_real_vol_63d_base_v002_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_real_vol(closeadj, volume, high, low, 63), 126)

def f04ev_f04_exploration_volatility_shocks_max_range_126d_base_v003_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_max_range(closeadj, volume, high, low, 126))

def f04ev_f04_exploration_volatility_shocks_vol_mom_252d_base_v004_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_vol_mom(closeadj, volume, high, low, 252).diff(5)

def f04ev_f04_exploration_volatility_shocks_shock_score_504d_base_v005_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_shock_score(closeadj, volume, high, low, 504)

def f04ev_f04_exploration_volatility_shocks_range_z_5d_base_v006_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_range_z(closeadj, volume, high, low, 5), 10)

def f04ev_f04_exploration_volatility_shocks_range_pct_21d_base_v007_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_range_pct(closeadj, volume, high, low, 21), 42)

def f04ev_f04_exploration_volatility_shocks_vol_surge_63d_base_v008_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_vol_surge(closeadj, volume, high, low, 63))

def f04ev_f04_exploration_volatility_shocks_real_vol_126d_base_v009_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_real_vol(closeadj, volume, high, low, 126).diff(5)

def f04ev_f04_exploration_volatility_shocks_max_range_252d_base_v010_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_max_range(closeadj, volume, high, low, 252)

def f04ev_f04_exploration_volatility_shocks_vol_mom_504d_base_v011_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_vol_mom(closeadj, volume, high, low, 504), 504)

def f04ev_f04_exploration_volatility_shocks_shock_score_5d_base_v012_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_shock_score(closeadj, volume, high, low, 5), 10)

def f04ev_f04_exploration_volatility_shocks_range_z_21d_base_v013_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = np.tanh(_f04ev_range_z(closeadj, volume, high, low, 21))

def f04ev_f04_exploration_volatility_shocks_range_pct_63d_base_v014_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_range_pct(closeadj, volume, high, low, 63).diff(5)

def f04ev_f04_exploration_volatility_shocks_vol_surge_126d_base_v015_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_vol_surge(closeadj, volume, high, low, 126)

def f04ev_f04_exploration_volatility_shocks_real_vol_252d_base_v016_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_real_vol(closeadj, volume, high, low, 252), 504)

def f04ev_f04_exploration_volatility_shocks_max_range_504d_base_v017_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_max_range(closeadj, volume, high, low, 504), 504)

def f04ev_f04_exploration_volatility_shocks_vol_mom_5d_base_v018_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_vol_mom(closeadj, volume, high, low, 5))

def f04ev_f04_exploration_volatility_shocks_shock_score_21d_base_v019_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_shock_score(closeadj, volume, high, low, 21).diff(5)

def f04ev_f04_exploration_volatility_shocks_range_z_63d_base_v020_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _f04ev_range_z(closeadj, volume, high, low, 63)

def f04ev_f04_exploration_volatility_shocks_range_pct_126d_base_v021_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_range_pct(closeadj, volume, high, low, 126), 252)

def f04ev_f04_exploration_volatility_shocks_vol_surge_252d_base_v022_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_vol_surge(closeadj, volume, high, low, 252), 504)

def f04ev_f04_exploration_volatility_shocks_real_vol_504d_base_v023_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_real_vol(closeadj, volume, high, low, 504))

def f04ev_f04_exploration_volatility_shocks_max_range_5d_base_v024_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_max_range(closeadj, volume, high, low, 5).diff(5)

def f04ev_f04_exploration_volatility_shocks_vol_mom_21d_base_v025_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_vol_mom(closeadj, volume, high, low, 21)

def f04ev_f04_exploration_volatility_shocks_shock_score_63d_base_v026_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_shock_score(closeadj, volume, high, low, 63), 126)

def f04ev_f04_exploration_volatility_shocks_range_z_126d_base_v027_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _rank(_f04ev_range_z(closeadj, volume, high, low, 126), 252)

def f04ev_f04_exploration_volatility_shocks_range_pct_252d_base_v028_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_range_pct(closeadj, volume, high, low, 252))

def f04ev_f04_exploration_volatility_shocks_vol_surge_504d_base_v029_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_vol_surge(closeadj, volume, high, low, 504).diff(5)

def f04ev_f04_exploration_volatility_shocks_real_vol_5d_base_v030_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_real_vol(closeadj, volume, high, low, 5)

def f04ev_f04_exploration_volatility_shocks_max_range_21d_base_v031_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_max_range(closeadj, volume, high, low, 21), 42)

def f04ev_f04_exploration_volatility_shocks_vol_mom_63d_base_v032_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_vol_mom(closeadj, volume, high, low, 63), 126)

def f04ev_f04_exploration_volatility_shocks_shock_score_126d_base_v033_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_shock_score(closeadj, volume, high, low, 126))

def f04ev_f04_exploration_volatility_shocks_range_z_252d_base_v034_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _f04ev_range_z(closeadj, volume, high, low, 252).diff(5)

def f04ev_f04_exploration_volatility_shocks_range_pct_504d_base_v035_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_range_pct(closeadj, volume, high, low, 504)

def f04ev_f04_exploration_volatility_shocks_vol_surge_5d_base_v036_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_vol_surge(closeadj, volume, high, low, 5), 10)

def f04ev_f04_exploration_volatility_shocks_real_vol_21d_base_v037_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_real_vol(closeadj, volume, high, low, 21), 42)

def f04ev_f04_exploration_volatility_shocks_max_range_63d_base_v038_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_max_range(closeadj, volume, high, low, 63))

def f04ev_f04_exploration_volatility_shocks_vol_mom_126d_base_v039_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_vol_mom(closeadj, volume, high, low, 126).diff(5)

def f04ev_f04_exploration_volatility_shocks_shock_score_252d_base_v040_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_shock_score(closeadj, volume, high, low, 252)

def f04ev_f04_exploration_volatility_shocks_range_z_504d_base_v041_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_range_z(closeadj, volume, high, low, 504), 504)

def f04ev_f04_exploration_volatility_shocks_range_pct_5d_base_v042_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_range_pct(closeadj, volume, high, low, 5), 10)

def f04ev_f04_exploration_volatility_shocks_vol_surge_21d_base_v043_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_vol_surge(closeadj, volume, high, low, 21))

def f04ev_f04_exploration_volatility_shocks_real_vol_63d_base_v044_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_real_vol(closeadj, volume, high, low, 63).diff(5)

def f04ev_f04_exploration_volatility_shocks_max_range_126d_base_v045_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_max_range(closeadj, volume, high, low, 126)

def f04ev_f04_exploration_volatility_shocks_vol_mom_252d_base_v046_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_vol_mom(closeadj, volume, high, low, 252), 504)

def f04ev_f04_exploration_volatility_shocks_shock_score_504d_base_v047_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_shock_score(closeadj, volume, high, low, 504), 504)

def f04ev_f04_exploration_volatility_shocks_range_z_5d_base_v048_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = np.tanh(_f04ev_range_z(closeadj, volume, high, low, 5))

def f04ev_f04_exploration_volatility_shocks_range_pct_21d_base_v049_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_range_pct(closeadj, volume, high, low, 21).diff(5)

def f04ev_f04_exploration_volatility_shocks_vol_surge_63d_base_v050_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_vol_surge(closeadj, volume, high, low, 63)

def f04ev_f04_exploration_volatility_shocks_real_vol_126d_base_v051_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_real_vol(closeadj, volume, high, low, 126), 252)

def f04ev_f04_exploration_volatility_shocks_max_range_252d_base_v052_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_max_range(closeadj, volume, high, low, 252), 504)

def f04ev_f04_exploration_volatility_shocks_vol_mom_504d_base_v053_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_vol_mom(closeadj, volume, high, low, 504))

def f04ev_f04_exploration_volatility_shocks_shock_score_5d_base_v054_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_shock_score(closeadj, volume, high, low, 5).diff(5)

def f04ev_f04_exploration_volatility_shocks_range_z_21d_base_v055_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _f04ev_range_z(closeadj, volume, high, low, 21)

def f04ev_f04_exploration_volatility_shocks_range_pct_63d_base_v056_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_range_pct(closeadj, volume, high, low, 63), 126)

def f04ev_f04_exploration_volatility_shocks_vol_surge_126d_base_v057_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_vol_surge(closeadj, volume, high, low, 126), 252)

def f04ev_f04_exploration_volatility_shocks_real_vol_252d_base_v058_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_real_vol(closeadj, volume, high, low, 252))

def f04ev_f04_exploration_volatility_shocks_max_range_504d_base_v059_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_max_range(closeadj, volume, high, low, 504).diff(5)

def f04ev_f04_exploration_volatility_shocks_vol_mom_5d_base_v060_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_vol_mom(closeadj, volume, high, low, 5)

def f04ev_f04_exploration_volatility_shocks_shock_score_21d_base_v061_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_shock_score(closeadj, volume, high, low, 21), 42)

def f04ev_f04_exploration_volatility_shocks_range_z_63d_base_v062_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _rank(_f04ev_range_z(closeadj, volume, high, low, 63), 126)

def f04ev_f04_exploration_volatility_shocks_range_pct_126d_base_v063_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_range_pct(closeadj, volume, high, low, 126))

def f04ev_f04_exploration_volatility_shocks_vol_surge_252d_base_v064_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_vol_surge(closeadj, volume, high, low, 252).diff(5)

def f04ev_f04_exploration_volatility_shocks_real_vol_504d_base_v065_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_real_vol(closeadj, volume, high, low, 504)

def f04ev_f04_exploration_volatility_shocks_max_range_5d_base_v066_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_max_range(closeadj, volume, high, low, 5), 10)

def f04ev_f04_exploration_volatility_shocks_vol_mom_21d_base_v067_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_vol_mom(closeadj, volume, high, low, 21), 42)

def f04ev_f04_exploration_volatility_shocks_shock_score_63d_base_v068_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_shock_score(closeadj, volume, high, low, 63))

def f04ev_f04_exploration_volatility_shocks_range_z_126d_base_v069_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _f04ev_range_z(closeadj, volume, high, low, 126).diff(5)

def f04ev_f04_exploration_volatility_shocks_range_pct_252d_base_v070_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_range_pct(closeadj, volume, high, low, 252)

def f04ev_f04_exploration_volatility_shocks_vol_surge_504d_base_v071_signal(closeadj, volume, high, low):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f04ev_vol_surge(closeadj, volume, high, low, 504), 504)

def f04ev_f04_exploration_volatility_shocks_real_vol_5d_base_v072_signal(closeadj, volume, high, low):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f04ev_real_vol(closeadj, volume, high, low, 5), 10)

def f04ev_f04_exploration_volatility_shocks_max_range_21d_base_v073_signal(closeadj, volume, high, low):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f04ev_max_range(closeadj, volume, high, low, 21))

def f04ev_f04_exploration_volatility_shocks_vol_mom_63d_base_v074_signal(closeadj, volume, high, low):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f04ev_vol_mom(closeadj, volume, high, low, 63).diff(5)

def f04ev_f04_exploration_volatility_shocks_shock_score_126d_base_v075_signal(closeadj, volume, high, low):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f04ev_shock_score(closeadj, volume, high, low, 126)

_FEATURES = [
    f04ev_f04_exploration_volatility_shocks_vol_surge_21d_base_v001_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_63d_base_v002_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_126d_base_v003_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_252d_base_v004_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_504d_base_v005_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_5d_base_v006_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_21d_base_v007_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_63d_base_v008_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_126d_base_v009_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_252d_base_v010_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_504d_base_v011_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_5d_base_v012_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_21d_base_v013_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_63d_base_v014_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_126d_base_v015_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_252d_base_v016_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_504d_base_v017_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_5d_base_v018_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_21d_base_v019_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_63d_base_v020_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_126d_base_v021_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_252d_base_v022_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_504d_base_v023_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_5d_base_v024_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_21d_base_v025_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_63d_base_v026_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_126d_base_v027_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_252d_base_v028_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_504d_base_v029_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_5d_base_v030_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_21d_base_v031_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_63d_base_v032_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_126d_base_v033_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_252d_base_v034_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_504d_base_v035_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_5d_base_v036_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_21d_base_v037_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_63d_base_v038_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_126d_base_v039_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_252d_base_v040_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_504d_base_v041_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_5d_base_v042_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_21d_base_v043_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_63d_base_v044_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_126d_base_v045_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_252d_base_v046_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_504d_base_v047_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_5d_base_v048_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_21d_base_v049_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_63d_base_v050_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_126d_base_v051_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_252d_base_v052_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_504d_base_v053_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_5d_base_v054_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_21d_base_v055_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_63d_base_v056_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_126d_base_v057_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_252d_base_v058_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_504d_base_v059_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_5d_base_v060_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_21d_base_v061_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_63d_base_v062_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_126d_base_v063_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_252d_base_v064_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_504d_base_v065_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_5d_base_v066_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_21d_base_v067_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_63d_base_v068_signal,
    f04ev_f04_exploration_volatility_shocks_range_z_126d_base_v069_signal,
    f04ev_f04_exploration_volatility_shocks_range_pct_252d_base_v070_signal,
    f04ev_f04_exploration_volatility_shocks_vol_surge_504d_base_v071_signal,
    f04ev_f04_exploration_volatility_shocks_real_vol_5d_base_v072_signal,
    f04ev_f04_exploration_volatility_shocks_max_range_21d_base_v073_signal,
    f04ev_f04_exploration_volatility_shocks_vol_mom_63d_base_v074_signal,
    f04ev_f04_exploration_volatility_shocks_shock_score_126d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F04_EXPLORATION_VOLATILITY_SHOCKS_REGISTRY = REGISTRY

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
