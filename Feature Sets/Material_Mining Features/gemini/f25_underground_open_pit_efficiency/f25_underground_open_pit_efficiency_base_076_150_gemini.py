"""
Family: Underground Open Pit Efficiency
Sector: Operations
Mathematical Approach: Operational/Efficiency
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

def _underground_open_pit_efficiency_velocity(opinc, revenue, assets, w):
    return opinc.diff(w) / revenue.rolling(w).mean().abs()

def _underground_open_pit_efficiency_impulse(opinc, revenue, assets, w):
    return _z(opinc, w) - _z(revenue, w)

def _underground_open_pit_efficiency_regime(opinc, revenue, assets, w):
    return opinc.pct_change(w)

def _underground_open_pit_efficiency_dispersion(opinc, revenue, assets, w):
    return np.log(opinc.replace(0, np.nan) / opinc.rolling(w).mean())

def _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, w):
    return opinc.rolling(w).std() / opinc.rolling(w).mean().abs()

def f25uo_f25_underground_open_pit_efficiency_prim2_252d_base_v076_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 252)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_504d_base_v077_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 504)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_5d_base_v078_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 5))

def f25uo_f25_underground_open_pit_efficiency_prim5_21d_base_v079_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 21)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_63d_base_v080_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 63)

def f25uo_f25_underground_open_pit_efficiency_prim2_126d_base_v081_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 126)
    result = _z(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_252d_base_v082_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 252)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_504d_base_v083_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 504))

def f25uo_f25_underground_open_pit_efficiency_prim5_5d_base_v084_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 5)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_21d_base_v085_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 21)

def f25uo_f25_underground_open_pit_efficiency_prim2_63d_base_v086_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 63)
    result = _z(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_126d_base_v087_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 126)
    result = _rank(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_252d_base_v088_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 252))

def f25uo_f25_underground_open_pit_efficiency_prim5_504d_base_v089_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 504)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_5d_base_v090_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 5)

def f25uo_f25_underground_open_pit_efficiency_prim2_21d_base_v091_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_63d_base_v092_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_126d_base_v093_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 126))

def f25uo_f25_underground_open_pit_efficiency_prim5_252d_base_v094_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_504d_base_v095_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 504)

def f25uo_f25_underground_open_pit_efficiency_prim2_5d_base_v096_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_21d_base_v097_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_63d_base_v098_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 63))

def f25uo_f25_underground_open_pit_efficiency_prim5_126d_base_v099_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_252d_base_v100_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 252)

def f25uo_f25_underground_open_pit_efficiency_prim2_504d_base_v101_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_5d_base_v102_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_21d_base_v103_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 21))

def f25uo_f25_underground_open_pit_efficiency_prim5_63d_base_v104_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_126d_base_v105_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 126)

def f25uo_f25_underground_open_pit_efficiency_prim2_252d_base_v106_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 252)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_504d_base_v107_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 504)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_5d_base_v108_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 5))

def f25uo_f25_underground_open_pit_efficiency_prim5_21d_base_v109_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 21)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_63d_base_v110_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 63)

def f25uo_f25_underground_open_pit_efficiency_prim2_126d_base_v111_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 126)
    result = _z(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_252d_base_v112_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 252)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_504d_base_v113_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 504))

def f25uo_f25_underground_open_pit_efficiency_prim5_5d_base_v114_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 5)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_21d_base_v115_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 21)

def f25uo_f25_underground_open_pit_efficiency_prim2_63d_base_v116_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 63)
    result = _z(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_126d_base_v117_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 126)
    result = _rank(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_252d_base_v118_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 252))

def f25uo_f25_underground_open_pit_efficiency_prim5_504d_base_v119_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 504)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_5d_base_v120_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 5)

def f25uo_f25_underground_open_pit_efficiency_prim2_21d_base_v121_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 21)
    result = _z(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_63d_base_v122_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 63)
    result = _rank(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_126d_base_v123_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 126))

def f25uo_f25_underground_open_pit_efficiency_prim5_252d_base_v124_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 252)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_504d_base_v125_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 504)

def f25uo_f25_underground_open_pit_efficiency_prim2_5d_base_v126_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 5)
    result = _z(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_21d_base_v127_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 21)
    result = _rank(raw_input, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_63d_base_v128_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 63))

def f25uo_f25_underground_open_pit_efficiency_prim5_126d_base_v129_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 126)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_252d_base_v130_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 252)

def f25uo_f25_underground_open_pit_efficiency_prim2_504d_base_v131_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 504)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_5d_base_v132_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 5)
    result = _rank(raw_input, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_21d_base_v133_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 21))

def f25uo_f25_underground_open_pit_efficiency_prim5_63d_base_v134_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 63)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_126d_base_v135_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 126)

def f25uo_f25_underground_open_pit_efficiency_prim2_252d_base_v136_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 252)
    result = _z(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_504d_base_v137_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 504)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_5d_base_v138_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 5))

def f25uo_f25_underground_open_pit_efficiency_prim5_21d_base_v139_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 21)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_63d_base_v140_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 63)

def f25uo_f25_underground_open_pit_efficiency_prim2_126d_base_v141_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 126)
    result = _z(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_252d_base_v142_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 252)
    result = _rank(raw_input, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_504d_base_v143_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 504))

def f25uo_f25_underground_open_pit_efficiency_prim5_5d_base_v144_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 5)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_21d_base_v145_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 21)

def f25uo_f25_underground_open_pit_efficiency_prim2_63d_base_v146_signal(opinc, revenue, assets):
    """Normalizes the signal relative to historical variance to identify statistical outliers."""
    raw_input = _underground_open_pit_efficiency_impulse(opinc, revenue, assets, 63)
    result = _z(raw_input, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim3_126d_base_v147_signal(opinc, revenue, assets):
    """Provides a relative percentile ranking to gauge the signal's strength within a rolling window."""
    raw_input = _underground_open_pit_efficiency_regime(opinc, revenue, assets, 126)
    result = _rank(raw_input, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim4_252d_base_v148_signal(opinc, revenue, assets):
    """Applies a non-linear transformation to bound the signal and dampen extreme outlier effects."""
    result = np.tanh(_underground_open_pit_efficiency_dispersion(opinc, revenue, assets, 252))

def f25uo_f25_underground_open_pit_efficiency_prim5_504d_base_v149_signal(opinc, revenue, assets):
    """Captures the rate of change or momentum in the underlying domain primitive."""
    base_signal = _underground_open_pit_efficiency_efficiency(opinc, revenue, assets, 504)
    result = base_signal.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f25uo_f25_underground_open_pit_efficiency_prim1_5d_base_v150_signal(opinc, revenue, assets):
    """Synthesizes multiple domain primitives into a high-conviction analytical signal."""
    result = _underground_open_pit_efficiency_velocity(opinc, revenue, assets, 5)

_FEATURES = [
    f25uo_f25_underground_open_pit_efficiency_prim2_252d_base_v076_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_504d_base_v077_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_5d_base_v078_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_21d_base_v079_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_63d_base_v080_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_126d_base_v081_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_252d_base_v082_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_504d_base_v083_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_5d_base_v084_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_21d_base_v085_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_63d_base_v086_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_126d_base_v087_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_252d_base_v088_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_504d_base_v089_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_5d_base_v090_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_21d_base_v091_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_63d_base_v092_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_126d_base_v093_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_252d_base_v094_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_504d_base_v095_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_5d_base_v096_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_21d_base_v097_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_63d_base_v098_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_126d_base_v099_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_252d_base_v100_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_504d_base_v101_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_5d_base_v102_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_21d_base_v103_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_63d_base_v104_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_126d_base_v105_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_252d_base_v106_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_504d_base_v107_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_5d_base_v108_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_21d_base_v109_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_63d_base_v110_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_126d_base_v111_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_252d_base_v112_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_504d_base_v113_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_5d_base_v114_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_21d_base_v115_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_63d_base_v116_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_126d_base_v117_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_252d_base_v118_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_504d_base_v119_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_5d_base_v120_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_21d_base_v121_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_63d_base_v122_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_126d_base_v123_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_252d_base_v124_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_504d_base_v125_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_5d_base_v126_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_21d_base_v127_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_63d_base_v128_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_126d_base_v129_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_252d_base_v130_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_504d_base_v131_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_5d_base_v132_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_21d_base_v133_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_63d_base_v134_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_126d_base_v135_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_252d_base_v136_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_504d_base_v137_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_5d_base_v138_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_21d_base_v139_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_63d_base_v140_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_126d_base_v141_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_252d_base_v142_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_504d_base_v143_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_5d_base_v144_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_21d_base_v145_signal,
    f25uo_f25_underground_open_pit_efficiency_prim2_63d_base_v146_signal,
    f25uo_f25_underground_open_pit_efficiency_prim3_126d_base_v147_signal,
    f25uo_f25_underground_open_pit_efficiency_prim4_252d_base_v148_signal,
    f25uo_f25_underground_open_pit_efficiency_prim5_504d_base_v149_signal,
    f25uo_f25_underground_open_pit_efficiency_prim1_5d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F25_UNDERGROUND_OPEN_PIT_EFFICIENCY_REGISTRY = REGISTRY

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
