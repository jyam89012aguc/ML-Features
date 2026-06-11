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
def _f19_asset_growth(assets, w):
    return assets.pct_change(periods=w) * _mean(assets, w)

def _f19_capex_sustained(capex, w):
    return _mean(capex, w) * (capex / _mean(capex, max(w, 21)).replace(0, np.nan))

def _f19_capex_intensity_uplift(capex, revenue, w):
    ratio = capex / revenue.replace(0, np.nan)
    return ratio - _mean(ratio, w)


# ===== features =====
def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v076_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v077_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v078_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v079_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v080_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v081_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v082_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v083_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v084_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v085_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v086_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v087_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v088_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v089_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v090_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v091_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v092_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v093_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v094_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v095_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v096_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v097_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v098_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v099_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v100_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v101_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v102_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v103_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v104_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v105_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v106_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v107_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v108_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v109_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v110_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v111_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v112_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v113_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v114_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v115_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v116_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v117_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v118_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v119_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v120_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v121_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v122_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v123_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v124_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v125_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v126_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v127_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v128_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v129_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v130_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v131_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v132_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v133_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v134_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v135_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v136_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v137_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v138_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v139_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v140_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v141_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v142_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v143_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v144_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v145_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v146_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126)
    result = base * closeadj + _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v147_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126)
    result = base * closeadj * 1.0 + closeadj * 0.0001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v148_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126)
    result = base * closeadj * (closeadj.pct_change(5).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v149_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126)
    result = base * closeadj + (closeadj - _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v150_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126)
    result = base * closeadj + closeadj.diff(21) * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v076_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v077_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v078_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v079_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v080_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v081_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v082_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v083_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v084_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v085_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v086_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v087_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v088_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v089_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v090_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v091_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v092_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v093_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v094_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v095_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v096_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v097_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v098_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v099_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_base_v100_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v101_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v102_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v103_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v104_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v105_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v106_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v107_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v108_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v109_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v110_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v111_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v112_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v113_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v114_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v115_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v116_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v117_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v118_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v119_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v120_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v121_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v122_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v123_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v124_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_base_v125_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v126_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v127_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v128_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v129_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v130_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v131_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v132_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v133_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v134_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v135_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v136_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v137_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v138_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v139_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v140_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v141_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v142_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v143_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v144_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v145_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v146_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v147_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v148_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v149_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_ELECTRIFICATION_CAPEX_DEMAND_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f19_asset_growth", "_f19_capex_sustained", "_f19_capex_intensity_uplift")
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
    print(f"OK f19_electrification_capex_demand_base_076_150_claude: {n_features} features pass")
