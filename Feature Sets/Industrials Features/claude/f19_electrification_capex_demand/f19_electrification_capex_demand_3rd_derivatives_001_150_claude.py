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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f19_asset_growth(assets, w):
    return assets.pct_change(periods=w) * _mean(assets, w)

def _f19_capex_sustained(capex, w):
    return _mean(capex, w) * (capex / _mean(capex, max(w, 21)).replace(0, np.nan))

def _f19_capex_intensity_uplift(capex, revenue, w):
    ratio = capex / revenue.replace(0, np.nan)
    return ratio - _mean(ratio, w)


# ===== features =====
def f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v001_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v002_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v003_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v004_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v005_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v006_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v007_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v008_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v009_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v010_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v011_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v012_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v013_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v014_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v015_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v016_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v017_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v018_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v019_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v020_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v021_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v022_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v023_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v024_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v025_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v026_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v027_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v028_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v029_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v030_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v031_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v032_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 378) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v033_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v034_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v035_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v036_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v037_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v038_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v039_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v040_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v041_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 100) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v042_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 100) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v043_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 100) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v044_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 100) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v045_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 100) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v046_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 150) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v047_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 150) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v048_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 150) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v049_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 150) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v050_signal(assets, closeadj):
    base = _f19_asset_growth(assets, 150) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v051_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v052_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v053_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v054_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v055_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v056_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v057_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v058_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v059_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v060_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v061_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v062_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v063_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v064_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v065_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v066_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v067_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v068_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v069_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v070_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v071_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v072_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v073_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v074_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v075_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v076_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v077_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v078_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v079_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v080_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v081_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v082_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 378) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v083_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v084_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v085_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v086_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v087_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 504) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v088_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v089_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v090_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v091_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 100) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v092_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 100) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v093_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 100) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v094_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 100) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v095_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 100) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v096_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 150) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v097_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 150) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v098_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 150) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v099_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 150) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v100_signal(capex, closeadj):
    base = _f19_capex_sustained(capex, 150) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v101_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v102_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v103_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v104_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v105_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v106_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v107_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v108_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v109_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v110_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v111_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v112_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v113_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v114_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v115_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v116_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v117_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v118_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v119_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v120_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v121_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v122_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 189) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v123_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v124_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v125_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v126_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v127_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v128_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v129_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v130_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v131_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v132_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 378) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v133_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v134_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v135_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v136_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v137_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 504) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v138_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v139_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v140_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v141_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 100) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v142_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 100) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v143_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 100) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v144_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 100) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v145_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 100) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v146_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 150) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v147_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 150) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v148_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 150) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v149_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 150) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v150_signal(capex, revenue, closeadj):
    base = _f19_capex_intensity_uplift(capex, revenue, 150) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v001_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v002_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v003_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v004_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_21d_jerk_v005_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v006_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v007_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v008_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v009_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_42d_jerk_v010_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v011_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v012_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v013_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v014_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_63d_jerk_v015_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v016_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v017_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v018_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v019_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_126d_jerk_v020_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v021_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v022_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v023_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v024_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_189d_jerk_v025_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v026_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v027_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v028_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v029_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_252d_jerk_v030_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v031_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v032_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v033_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v034_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_378d_jerk_v035_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v036_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v037_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v038_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v039_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_504d_jerk_v040_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v041_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v042_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v043_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v044_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_100d_jerk_v045_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v046_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v047_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v048_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v049_signal,
    f19ecd_f19_electrification_capex_demand_asset_growth_150d_jerk_v050_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v051_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v052_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v053_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v054_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_21d_jerk_v055_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v056_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v057_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v058_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v059_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_42d_jerk_v060_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v061_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v062_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v063_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v064_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_63d_jerk_v065_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v066_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v067_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v068_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v069_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_126d_jerk_v070_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v071_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v072_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v073_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v074_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_189d_jerk_v075_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v076_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v077_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v078_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v079_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_252d_jerk_v080_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v081_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v082_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v083_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v084_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_378d_jerk_v085_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v086_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v087_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v088_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v089_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_504d_jerk_v090_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v091_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v092_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v093_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v094_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_100d_jerk_v095_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v096_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v097_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v098_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v099_signal,
    f19ecd_f19_electrification_capex_demand_capex_sustained_150d_jerk_v100_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v101_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v102_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v103_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v104_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_21d_jerk_v105_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v106_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v107_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v108_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v109_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_42d_jerk_v110_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v111_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v112_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v113_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v114_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_63d_jerk_v115_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v116_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v117_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v118_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v119_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_126d_jerk_v120_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v121_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v122_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v123_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v124_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_189d_jerk_v125_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v126_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v127_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v128_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v129_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_252d_jerk_v130_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v131_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v132_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v133_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v134_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_378d_jerk_v135_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v136_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v137_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v138_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v139_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_504d_jerk_v140_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v141_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v142_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v143_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v144_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_100d_jerk_v145_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v146_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v147_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v148_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v149_signal,
    f19ecd_f19_electrification_capex_demand_capex_intensity_uplift_150d_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_ELECTRIFICATION_CAPEX_DEMAND_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f19_electrification_capex_demand_3rd_derivatives_001_150_claude: {n_features} features pass")
