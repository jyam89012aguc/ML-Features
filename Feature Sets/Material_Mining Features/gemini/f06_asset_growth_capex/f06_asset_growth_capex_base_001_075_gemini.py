"""
Family: Asset Growth Capex
Sector: Capital Intensity
Mathematical Approach: Fundamental/Growth
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

def _f06ag_capex_assets(capex, assets, ppnenet, revenue, w):
    return capex / assets

def _f06ag_capex_ppne(capex, assets, ppnenet, revenue, w):
    return capex / ppnenet

def _f06ag_asset_growth(capex, assets, ppnenet, revenue, w):
    return assets.pct_change(w)

def _f06ag_ppne_growth(capex, assets, ppnenet, revenue, w):
    return ppnenet.pct_change(w)

def _f06ag_capex_intensity(capex, assets, ppnenet, revenue, w):
    return capex.rolling(w).sum() / assets.rolling(w).mean()

def _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, w):
    return capex / assets.diff(w).abs()

def _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, w):
    return revenue / assets

def f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v001_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_asset_growth_63d_base_v002_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v003_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 126))

def f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v004_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 252).diff(5)

def f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v005_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 504)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v006_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_capex_assets_21d_base_v007_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v008_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 63))

def f06ag_f06_asset_growth_capex_asset_growth_126d_base_v009_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 126).diff(5)

def f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v010_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 252)

def f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v011_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v012_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v013_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 21))

def f06ag_f06_asset_growth_capex_capex_assets_63d_base_v014_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 63).diff(5)

def f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v015_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 126)

def f06ag_f06_asset_growth_capex_asset_growth_252d_base_v016_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v017_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v018_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 5))

def f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v019_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 21).diff(5)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v020_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 63)

def f06ag_f06_asset_growth_capex_capex_assets_126d_base_v021_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v022_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_asset_growth_504d_base_v023_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 504))

def f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v024_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 5).diff(5)

def f06ag_f06_asset_growth_capex_capex_intensity_21d_base_v025_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 21)

def f06ag_f06_asset_growth_capex_reinvest_ratio_63d_base_v026_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_126d_base_v027_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_capex_assets_252d_base_v028_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 252))

def f06ag_f06_asset_growth_capex_capex_ppne_504d_base_v029_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 504).diff(5)

def f06ag_f06_asset_growth_capex_asset_growth_5d_base_v030_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 5)

def f06ag_f06_asset_growth_capex_ppne_growth_21d_base_v031_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_capex_intensity_63d_base_v032_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_reinvest_ratio_126d_base_v033_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 126))

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_252d_base_v034_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 252).diff(5)

def f06ag_f06_asset_growth_capex_capex_assets_504d_base_v035_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 504)

def f06ag_f06_asset_growth_capex_capex_ppne_5d_base_v036_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_asset_growth_21d_base_v037_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_ppne_growth_63d_base_v038_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 63))

def f06ag_f06_asset_growth_capex_capex_intensity_126d_base_v039_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 126).diff(5)

def f06ag_f06_asset_growth_capex_reinvest_ratio_252d_base_v040_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 252)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_504d_base_v041_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_capex_assets_5d_base_v042_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v043_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 21))

def f06ag_f06_asset_growth_capex_asset_growth_63d_base_v044_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 63).diff(5)

def f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v045_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 126)

def f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v046_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v047_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v048_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 5))

def f06ag_f06_asset_growth_capex_capex_assets_21d_base_v049_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 21).diff(5)

def f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v050_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 63)

def f06ag_f06_asset_growth_capex_asset_growth_126d_base_v051_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v052_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v053_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 504))

def f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v054_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 5).diff(5)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v055_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 21)

def f06ag_f06_asset_growth_capex_capex_assets_63d_base_v056_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v057_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_asset_growth_252d_base_v058_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 252))

def f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v059_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 504).diff(5)

def f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v060_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 5)

def f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v061_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v062_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_capex_assets_126d_base_v063_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 126))

def f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v064_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 252).diff(5)

def f06ag_f06_asset_growth_capex_asset_growth_504d_base_v065_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 504)

def f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v066_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_capex_intensity_21d_base_v067_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_reinvest_ratio_63d_base_v068_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 63))

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_126d_base_v069_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 126).diff(5)

def f06ag_f06_asset_growth_capex_capex_assets_252d_base_v070_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 252)

def f06ag_f06_asset_growth_capex_capex_ppne_504d_base_v071_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_asset_growth_5d_base_v072_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_ppne_growth_21d_base_v073_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 21))

def f06ag_f06_asset_growth_capex_capex_intensity_63d_base_v074_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 63).diff(5)

def f06ag_f06_asset_growth_capex_reinvest_ratio_126d_base_v075_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 126)

_FEATURES = [
    f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v001_signal,
    f06ag_f06_asset_growth_capex_asset_growth_63d_base_v002_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v003_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v004_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v005_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v006_signal,
    f06ag_f06_asset_growth_capex_capex_assets_21d_base_v007_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v008_signal,
    f06ag_f06_asset_growth_capex_asset_growth_126d_base_v009_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v010_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v011_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v012_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v013_signal,
    f06ag_f06_asset_growth_capex_capex_assets_63d_base_v014_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v015_signal,
    f06ag_f06_asset_growth_capex_asset_growth_252d_base_v016_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v017_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v018_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v019_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v020_signal,
    f06ag_f06_asset_growth_capex_capex_assets_126d_base_v021_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v022_signal,
    f06ag_f06_asset_growth_capex_asset_growth_504d_base_v023_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v024_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_21d_base_v025_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_63d_base_v026_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_126d_base_v027_signal,
    f06ag_f06_asset_growth_capex_capex_assets_252d_base_v028_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_504d_base_v029_signal,
    f06ag_f06_asset_growth_capex_asset_growth_5d_base_v030_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_21d_base_v031_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_63d_base_v032_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_126d_base_v033_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_252d_base_v034_signal,
    f06ag_f06_asset_growth_capex_capex_assets_504d_base_v035_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_5d_base_v036_signal,
    f06ag_f06_asset_growth_capex_asset_growth_21d_base_v037_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_63d_base_v038_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_126d_base_v039_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_252d_base_v040_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_504d_base_v041_signal,
    f06ag_f06_asset_growth_capex_capex_assets_5d_base_v042_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v043_signal,
    f06ag_f06_asset_growth_capex_asset_growth_63d_base_v044_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v045_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v046_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v047_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v048_signal,
    f06ag_f06_asset_growth_capex_capex_assets_21d_base_v049_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v050_signal,
    f06ag_f06_asset_growth_capex_asset_growth_126d_base_v051_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v052_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v053_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v054_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v055_signal,
    f06ag_f06_asset_growth_capex_capex_assets_63d_base_v056_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v057_signal,
    f06ag_f06_asset_growth_capex_asset_growth_252d_base_v058_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v059_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v060_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v061_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v062_signal,
    f06ag_f06_asset_growth_capex_capex_assets_126d_base_v063_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v064_signal,
    f06ag_f06_asset_growth_capex_asset_growth_504d_base_v065_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v066_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_21d_base_v067_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_63d_base_v068_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_126d_base_v069_signal,
    f06ag_f06_asset_growth_capex_capex_assets_252d_base_v070_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_504d_base_v071_signal,
    f06ag_f06_asset_growth_capex_asset_growth_5d_base_v072_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_21d_base_v073_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_63d_base_v074_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_126d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F06_ASSET_GROWTH_CAPEX_REGISTRY = REGISTRY

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
