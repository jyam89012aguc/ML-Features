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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


# ===== folder domain primitives =====
def _f20_small_base_acceleration(revenue, w):
    g = revenue.pct_change(periods=w)
    base = _mean(revenue, w * 2 if w * 2 > 21 else 21)
    return g.diff(periods=w) / (np.log(base.abs().replace(0, np.nan) + 1.0))

def _f20_growth_on_small_base(revenue, assets, w):
    g = revenue.pct_change(periods=w)
    base = _mean(assets, w)
    return g * np.log(base.abs().replace(0, np.nan) + 1.0)

def _f20_buildout_momentum(revenue, capex, w):
    rev_g = revenue.pct_change(periods=w)
    cap_g = capex.pct_change(periods=w)
    return (rev_g + cap_g) * _mean(revenue, w)


# ===== features =====
def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v076_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 10)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v077_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 10)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v078_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 10)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v079_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 10)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v080_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 10)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v081_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 21)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v082_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 21)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v083_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 21)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v084_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 21)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v085_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 21)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v086_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 42)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v087_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 42)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v088_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 42)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v089_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 42)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v090_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 42)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v091_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 63)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v092_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 63)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v093_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 63)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v094_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 63)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v095_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 63)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v096_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 126)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v097_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 126)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v098_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 126)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v099_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 126)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v100_signal(revenue, closeadj):
    base = _f20_small_base_acceleration(revenue, 126)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v101_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 10)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v102_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 10)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v103_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 10)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v104_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 10)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v105_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 10)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v106_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 21)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v107_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 21)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v108_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 21)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v109_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 21)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v110_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 21)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v111_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 42)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v112_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 42)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v113_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 42)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v114_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 42)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v115_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 42)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v116_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 63)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v117_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 63)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v118_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 63)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v119_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 63)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v120_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 63)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v121_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 126)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v122_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 126)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v123_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 126)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v124_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 126)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v125_signal(revenue, assets, closeadj):
    base = _f20_growth_on_small_base(revenue, assets, 126)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v126_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 10)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v127_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 10)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v128_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 10)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v129_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 10)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v130_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 10)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v131_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 21)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v132_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 21)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v133_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 21)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v134_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 21)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v135_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 21)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v136_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 42)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v137_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 42)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v138_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 42)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v139_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 42)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v140_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 42)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v141_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 63)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v142_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 63)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v143_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 63)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v144_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 63)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v145_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 63)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v146_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 126)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v147_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 126)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v148_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 126)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v149_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 126)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v150_signal(revenue, capex, closeadj):
    base = _f20_buildout_momentum(revenue, capex, 126)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v076_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v077_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v078_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v079_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_10d_base_v080_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v081_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v082_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v083_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v084_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_21d_base_v085_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v086_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v087_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v088_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v089_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_42d_base_v090_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v091_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v092_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v093_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v094_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_63d_base_v095_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v096_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v097_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v098_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v099_signal,
    f20rgb_f20_renewable_grid_buildout_signal_small_base_acceleration_126d_base_v100_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v101_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v102_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v103_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v104_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_10d_base_v105_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v106_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v107_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v108_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v109_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_21d_base_v110_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v111_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v112_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v113_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v114_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_42d_base_v115_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v116_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v117_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v118_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v119_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_63d_base_v120_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v121_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v122_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v123_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v124_signal,
    f20rgb_f20_renewable_grid_buildout_signal_growth_on_small_base_126d_base_v125_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v126_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v127_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v128_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v129_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_10d_base_v130_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v131_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v132_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v133_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v134_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_21d_base_v135_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v136_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v137_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v138_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v139_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_42d_base_v140_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v141_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v142_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v143_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v144_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_63d_base_v145_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v146_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v147_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v148_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v149_signal,
    f20rgb_f20_renewable_grid_buildout_signal_buildout_momentum_126d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_RENEWABLE_GRID_BUILDOUT_SIGNAL_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "capex": capex, "assets": assets,
        "ppnenet": ppnenet, "deferredrev": deferredrev,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f20_small_base_acceleration", "_f20_growth_on_small_base", "_f20_buildout_momentum")
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
    print(f"OK f20_renewable_grid_buildout_signal_base_076_150_claude: {n_features} features pass")
