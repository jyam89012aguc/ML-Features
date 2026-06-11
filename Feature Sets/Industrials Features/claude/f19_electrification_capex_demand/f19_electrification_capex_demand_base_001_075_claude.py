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
def f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v001_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v002_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v003_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v004_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v005_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 5)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v006_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v007_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v008_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v009_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v010_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 10)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v011_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v012_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v013_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v014_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v015_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v016_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v017_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v018_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v019_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v020_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v021_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v022_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v023_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v024_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v025_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v026_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v027_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v028_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v029_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v030_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 5)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v031_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v032_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v033_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v034_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v035_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 10)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v036_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v037_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v038_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v039_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v040_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v041_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v042_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v043_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v044_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v045_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v046_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v047_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v048_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v049_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v050_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v051_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v052_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 5)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v053_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 5)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v054_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 5)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v055_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 5)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v056_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v057_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v058_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v059_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v060_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 10)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v061_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v062_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v063_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v064_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v065_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v066_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v067_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v068_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v069_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v070_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v071_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v072_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v073_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v074_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v075_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63)
    result = base * closeadj + closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v001_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v002_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v003_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v004_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_5d_base_v005_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v006_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v007_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v008_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v009_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_10d_base_v010_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v011_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v012_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v013_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v014_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_base_v015_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v016_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v017_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v018_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v019_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_base_v020_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v021_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v022_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v023_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v024_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_base_v025_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v026_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v027_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v028_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v029_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_5d_base_v030_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v031_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v032_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v033_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v034_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_10d_base_v035_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v036_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v037_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v038_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v039_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_base_v040_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v041_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v042_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v043_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v044_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_base_v045_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v046_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v047_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v048_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v049_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_base_v050_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v051_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v052_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v053_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v054_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_5d_base_v055_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v056_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v057_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v058_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v059_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_10d_base_v060_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v061_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v062_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v063_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v064_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_base_v065_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v066_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v067_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v068_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v069_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_base_v070_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v071_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v072_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v073_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v074_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_ELECTRIFICATION_CAPEX_DEMAND_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f19_electrification_capex_demand_base_001_075_claude: {n_features} features pass")
