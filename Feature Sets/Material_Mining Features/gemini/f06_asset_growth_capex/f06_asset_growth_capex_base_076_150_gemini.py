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

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_252d_base_v076_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_capex_assets_504d_base_v077_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_capex_ppne_5d_base_v078_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 5))

def f06ag_f06_asset_growth_capex_asset_growth_21d_base_v079_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 21).diff(5)

def f06ag_f06_asset_growth_capex_ppne_growth_63d_base_v080_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 63)

def f06ag_f06_asset_growth_capex_capex_intensity_126d_base_v081_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_reinvest_ratio_252d_base_v082_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_504d_base_v083_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 504))

def f06ag_f06_asset_growth_capex_capex_assets_5d_base_v084_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 5).diff(5)

def f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v085_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 21)

def f06ag_f06_asset_growth_capex_asset_growth_63d_base_v086_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v087_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v088_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 252))

def f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v089_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 504).diff(5)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v090_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 5)

def f06ag_f06_asset_growth_capex_capex_assets_21d_base_v091_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v092_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_asset_growth_126d_base_v093_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 126))

def f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v094_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 252).diff(5)

def f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v095_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 504)

def f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v096_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v097_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_capex_assets_63d_base_v098_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 63))

def f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v099_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 126).diff(5)

def f06ag_f06_asset_growth_capex_asset_growth_252d_base_v100_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 252)

def f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v101_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v102_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v103_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 21))

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v104_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 63).diff(5)

def f06ag_f06_asset_growth_capex_capex_assets_126d_base_v105_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 126)

def f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v106_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_asset_growth_504d_base_v107_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v108_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 5))

def f06ag_f06_asset_growth_capex_capex_intensity_21d_base_v109_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 21).diff(5)

def f06ag_f06_asset_growth_capex_reinvest_ratio_63d_base_v110_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 63)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_126d_base_v111_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_capex_assets_252d_base_v112_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_capex_ppne_504d_base_v113_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 504))

def f06ag_f06_asset_growth_capex_asset_growth_5d_base_v114_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 5).diff(5)

def f06ag_f06_asset_growth_capex_ppne_growth_21d_base_v115_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 21)

def f06ag_f06_asset_growth_capex_capex_intensity_63d_base_v116_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_reinvest_ratio_126d_base_v117_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_252d_base_v118_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 252))

def f06ag_f06_asset_growth_capex_capex_assets_504d_base_v119_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 504).diff(5)

def f06ag_f06_asset_growth_capex_capex_ppne_5d_base_v120_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 5)

def f06ag_f06_asset_growth_capex_asset_growth_21d_base_v121_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_ppne_growth_63d_base_v122_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_capex_intensity_126d_base_v123_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 126))

def f06ag_f06_asset_growth_capex_reinvest_ratio_252d_base_v124_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 252).diff(5)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_504d_base_v125_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 504)

def f06ag_f06_asset_growth_capex_capex_assets_5d_base_v126_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v127_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 21), 42)

def f06ag_f06_asset_growth_capex_asset_growth_63d_base_v128_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 63))

def f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v129_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 126).diff(5)

def f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v130_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 252)

def f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v131_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v132_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 5), 10)

def f06ag_f06_asset_growth_capex_capex_assets_21d_base_v133_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 21))

def f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v134_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_ppne(capex, assets, ppnenet, revenue, 63).diff(5)

def f06ag_f06_asset_growth_capex_asset_growth_126d_base_v135_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 126)

def f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v136_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v137_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_intensity(capex, assets, ppnenet, revenue, 504), 504)

def f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v138_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 5))

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v139_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 21).diff(5)

def f06ag_f06_asset_growth_capex_capex_assets_63d_base_v140_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_capex_assets(capex, assets, ppnenet, revenue, 63)

def f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v141_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_asset_growth_252d_base_v142_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_asset_growth(capex, assets, ppnenet, revenue, 252), 504)

def f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v143_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_ppne_growth(capex, assets, ppnenet, revenue, 504))

def f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v144_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_capex_intensity(capex, assets, ppnenet, revenue, 5).diff(5)

def f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v145_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_reinvest_ratio(capex, assets, ppnenet, revenue, 21)

def f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v146_signal(capex, assets, ppnenet, revenue):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    result = _z(_f06ag_asset_turnover_proxy(capex, assets, ppnenet, revenue, 63), 126)

def f06ag_f06_asset_growth_capex_capex_assets_126d_base_v147_signal(capex, assets, ppnenet, revenue):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    result = _rank(_f06ag_capex_assets(capex, assets, ppnenet, revenue, 126), 252)

def f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v148_signal(capex, assets, ppnenet, revenue):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_f06ag_capex_ppne(capex, assets, ppnenet, revenue, 252))

def f06ag_f06_asset_growth_capex_asset_growth_504d_base_v149_signal(capex, assets, ppnenet, revenue):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    result = _f06ag_asset_growth(capex, assets, ppnenet, revenue, 504).diff(5)

def f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v150_signal(capex, assets, ppnenet, revenue):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _f06ag_ppne_growth(capex, assets, ppnenet, revenue, 5)

_FEATURES = [
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_252d_base_v076_signal,
    f06ag_f06_asset_growth_capex_capex_assets_504d_base_v077_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_5d_base_v078_signal,
    f06ag_f06_asset_growth_capex_asset_growth_21d_base_v079_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_63d_base_v080_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_126d_base_v081_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_252d_base_v082_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_504d_base_v083_signal,
    f06ag_f06_asset_growth_capex_capex_assets_5d_base_v084_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v085_signal,
    f06ag_f06_asset_growth_capex_asset_growth_63d_base_v086_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v087_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v088_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v089_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v090_signal,
    f06ag_f06_asset_growth_capex_capex_assets_21d_base_v091_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v092_signal,
    f06ag_f06_asset_growth_capex_asset_growth_126d_base_v093_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v094_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v095_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v096_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v097_signal,
    f06ag_f06_asset_growth_capex_capex_assets_63d_base_v098_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v099_signal,
    f06ag_f06_asset_growth_capex_asset_growth_252d_base_v100_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v101_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v102_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v103_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v104_signal,
    f06ag_f06_asset_growth_capex_capex_assets_126d_base_v105_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v106_signal,
    f06ag_f06_asset_growth_capex_asset_growth_504d_base_v107_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v108_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_21d_base_v109_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_63d_base_v110_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_126d_base_v111_signal,
    f06ag_f06_asset_growth_capex_capex_assets_252d_base_v112_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_504d_base_v113_signal,
    f06ag_f06_asset_growth_capex_asset_growth_5d_base_v114_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_21d_base_v115_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_63d_base_v116_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_126d_base_v117_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_252d_base_v118_signal,
    f06ag_f06_asset_growth_capex_capex_assets_504d_base_v119_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_5d_base_v120_signal,
    f06ag_f06_asset_growth_capex_asset_growth_21d_base_v121_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_63d_base_v122_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_126d_base_v123_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_252d_base_v124_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_504d_base_v125_signal,
    f06ag_f06_asset_growth_capex_capex_assets_5d_base_v126_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_21d_base_v127_signal,
    f06ag_f06_asset_growth_capex_asset_growth_63d_base_v128_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_126d_base_v129_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_252d_base_v130_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_504d_base_v131_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_5d_base_v132_signal,
    f06ag_f06_asset_growth_capex_capex_assets_21d_base_v133_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_63d_base_v134_signal,
    f06ag_f06_asset_growth_capex_asset_growth_126d_base_v135_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_252d_base_v136_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_504d_base_v137_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_5d_base_v138_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_21d_base_v139_signal,
    f06ag_f06_asset_growth_capex_capex_assets_63d_base_v140_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_126d_base_v141_signal,
    f06ag_f06_asset_growth_capex_asset_growth_252d_base_v142_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_504d_base_v143_signal,
    f06ag_f06_asset_growth_capex_capex_intensity_5d_base_v144_signal,
    f06ag_f06_asset_growth_capex_reinvest_ratio_21d_base_v145_signal,
    f06ag_f06_asset_growth_capex_asset_turnover_proxy_63d_base_v146_signal,
    f06ag_f06_asset_growth_capex_capex_assets_126d_base_v147_signal,
    f06ag_f06_asset_growth_capex_capex_ppne_252d_base_v148_signal,
    f06ag_f06_asset_growth_capex_asset_growth_504d_base_v149_signal,
    f06ag_f06_asset_growth_capex_ppne_growth_5d_base_v150_signal,
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
