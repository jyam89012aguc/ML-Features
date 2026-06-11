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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f26_housing_cycle_proxy(revenue, w):
    growth = revenue.pct_change(periods=w)
    long_growth = growth.rolling(max(2 * w, 21), min_periods=max(1, w // 2)).mean()
    return growth - long_growth


def _f26_demand_seasonality(revenue, w):
    annual = revenue.rolling(252, min_periods=63).mean()
    dev = (revenue - annual) / annual.replace(0, np.nan).abs()
    return dev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_housing_growth_signal(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return (rg + eg) / 2.0


# === Cycle-based slopes ===
def f26bph_f26_building_products_housing_cycle_21d_slope_v001_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_21d_slope_v002_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_63d_slope_v003_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_63d_slope_v004_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_126d_slope_v005_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_126d_slope_v006_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_252d_slope_v007_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_252d_slope_v008_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_252d_slope_v009_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_504d_slope_v010_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_504d_slope_v011_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_5d_slope_v012_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_42d_slope_v013_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_42d_slope_v014_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 42) * closeadj
    result = _slope_pct(base.abs() + 1.0, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_189d_slope_v015_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycle_378d_slope_v016_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Cycle EMA slope
def f26bph_f26_building_products_housing_cyclema_63d_slope_v017_signal(revenue, closeadj):
    base = _mean(_f26_housing_cycle_proxy(revenue, 63), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclema_252d_slope_v018_signal(revenue, closeadj):
    base = _mean(_f26_housing_cycle_proxy(revenue, 252), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclestd_63d_slope_v019_signal(revenue, closeadj):
    base = _std(_f26_housing_cycle_proxy(revenue, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclestd_252d_slope_v020_signal(revenue, closeadj):
    base = _std(_f26_housing_cycle_proxy(revenue, 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclez_63d_slope_v021_signal(revenue, closeadj):
    base = _z(_f26_housing_cycle_proxy(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclez_252d_slope_v022_signal(revenue, closeadj):
    base = _z(_f26_housing_cycle_proxy(revenue, 252), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycleabs_63d_slope_v023_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycleabs_252d_slope_v024_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclesq_63d_slope_v025_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    base = c * c.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclesq_252d_slope_v026_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    base = c * c.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexcapex_63d_slope_v027_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * capex / revenue.replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexcapex_252d_slope_v028_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * capex / revenue.replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexebitda_63d_slope_v029_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * (ebitda / revenue.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexebitda_252d_slope_v030_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * (ebitda / revenue.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexpx_63d_slope_v031_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * closeadj.pct_change(63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexpx_252d_slope_v032_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * closeadj.pct_change(252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclelogpx_63d_slope_v033_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclelogpx_252d_slope_v034_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexdv_63d_slope_v035_signal(revenue, volume, closeadj):
    dv = closeadj * volume
    base = _f26_housing_cycle_proxy(revenue, 63) * _mean(dv, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexdv_252d_slope_v036_signal(revenue, volume, closeadj):
    dv = closeadj * volume
    base = _f26_housing_cycle_proxy(revenue, 252) * _mean(dv, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclerank_252d_slope_v037_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    base = c.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclerank_504d_slope_v038_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    base = c.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclediff_63d_slope_v039_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63).diff(21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclediff_252d_slope_v040_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252).diff(63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycleema_21_slope_v041_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycleema_63_slope_v042_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexvol_63d_slope_v043_signal(revenue, volume, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexvol_252d_slope_v044_signal(revenue, volume, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * _z(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclevsstd_63d_slope_v045_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * closeadj / _std(closeadj, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclevsstd_252d_slope_v046_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * closeadj / _std(closeadj, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexpkgap_252d_slope_v047_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    b = base * gap * closeadj
    result = _slope_diff_norm(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexlogcap_252d_slope_v048_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 252) * np.log(capex.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexrange_252d_slope_v049_signal(revenue, closeadj):
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    base = _f26_housing_cycle_proxy(revenue, 252) * rng
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexpxdet_252d_slope_v050_signal(revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    base = _f26_housing_cycle_proxy(revenue, 252) * det * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# === Seasonality slopes ===
def f26bph_f26_building_products_housing_season_21d_slope_v051_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_63d_slope_v052_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_63d_slope_v053_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_126d_slope_v054_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_126d_slope_v055_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_252d_slope_v056_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_252d_slope_v057_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_5d_slope_v058_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_42d_slope_v059_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_189d_slope_v060_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_season_378d_slope_v061_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 378) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonma_21d_slope_v062_signal(revenue, closeadj):
    base = _mean(_f26_demand_seasonality(revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonma_126d_slope_v063_signal(revenue, closeadj):
    base = _mean(_f26_demand_seasonality(revenue, 126), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonstd_252d_slope_v064_signal(revenue, closeadj):
    base = _std(_f26_demand_seasonality(revenue, 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonz_63d_slope_v065_signal(revenue, closeadj):
    base = _z(_f26_demand_seasonality(revenue, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonz_252d_slope_v066_signal(revenue, closeadj):
    base = _z(_f26_demand_seasonality(revenue, 252), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonabs_63d_slope_v067_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonsq_63d_slope_v068_signal(revenue, closeadj):
    s = _f26_demand_seasonality(revenue, 63)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonsq_252d_slope_v069_signal(revenue, closeadj):
    s = _f26_demand_seasonality(revenue, 252)
    base = s * s.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxcapex_63d_slope_v070_signal(revenue, capex, closeadj):
    base = _f26_demand_seasonality(revenue, 63) * capex / revenue.replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxcapex_252d_slope_v071_signal(revenue, capex, closeadj):
    base = _f26_demand_seasonality(revenue, 252) * capex / revenue.replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonlogpx_63d_slope_v072_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxdv_63d_slope_v073_signal(revenue, volume, closeadj):
    dv = closeadj * volume
    base = _f26_demand_seasonality(revenue, 63) * _mean(dv, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxvolz_252d_slope_v074_signal(revenue, volume, closeadj):
    base = _f26_demand_seasonality(revenue, 252) * _z(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonema_21_slope_v075_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonema_63_slope_v076_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonrank_252d_slope_v077_signal(revenue, closeadj):
    s = _f26_demand_seasonality(revenue, 63)
    base = s.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonrank_504d_slope_v078_signal(revenue, closeadj):
    s = _f26_demand_seasonality(revenue, 63)
    base = s.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxpkgap_252d_slope_v079_signal(revenue, closeadj):
    s = _f26_demand_seasonality(revenue, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    base = s * gap * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxlogcap_252d_slope_v080_signal(revenue, capex, closeadj):
    base = _f26_demand_seasonality(revenue, 252) * np.log(capex.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxrange_63d_slope_v081_signal(revenue, closeadj):
    rng = closeadj.rolling(63, min_periods=21).max() - closeadj.rolling(63, min_periods=21).min()
    base = _f26_demand_seasonality(revenue, 63) * rng
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxpxdet_252d_slope_v082_signal(revenue, closeadj):
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    base = _f26_demand_seasonality(revenue, 252) * det * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxrevg_252d_slope_v083_signal(revenue, closeadj):
    base = _f26_demand_seasonality(revenue, 252) * (1.0 + revenue.pct_change(252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxebitg_252d_slope_v084_signal(revenue, ebitda, closeadj):
    base = _f26_demand_seasonality(revenue, 252) * ebitda.pct_change(252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasondev_252d_slope_v085_signal(revenue, closeadj):
    s = _f26_demand_seasonality(revenue, 252)
    base = (s - _mean(s, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# === Growth slopes ===
def f26bph_f26_building_products_housing_growth_21d_slope_v086_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_63d_slope_v087_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_63d_slope_v088_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_126d_slope_v089_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_126d_slope_v090_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_252d_slope_v091_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_252d_slope_v092_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_5d_slope_v093_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_42d_slope_v094_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_189d_slope_v095_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growth_504d_slope_v096_signal(revenue, ebitda, closeadj):
    base = _f26_housing_growth_signal(revenue, ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthma_63d_slope_v097_signal(revenue, ebitda, closeadj):
    base = _mean(_f26_housing_growth_signal(revenue, ebitda, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthstd_252d_slope_v098_signal(revenue, ebitda, closeadj):
    base = _std(_f26_housing_growth_signal(revenue, ebitda, 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthz_63d_slope_v099_signal(revenue, ebitda, closeadj):
    base = _z(_f26_housing_growth_signal(revenue, ebitda, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthz_252d_slope_v100_signal(revenue, ebitda, closeadj):
    base = _z(_f26_housing_growth_signal(revenue, ebitda, 252), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthsq_63d_slope_v101_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthsq_252d_slope_v102_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = g * g.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxcapex_63d_slope_v103_signal(revenue, ebitda, capex, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g * _z(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxcaprev_63d_slope_v104_signal(revenue, ebitda, capex, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    capr = capex / revenue.replace(0, np.nan)
    base = g * _z(capr, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthlogpx_63d_slope_v105_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxdv_252d_slope_v106_signal(revenue, ebitda, volume, closeadj):
    dv = closeadj * volume
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = g * _mean(dv, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthrank_252d_slope_v107_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthrank_504d_slope_v108_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthema_21_slope_v109_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthema_63_slope_v110_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxpxgap_252d_slope_v111_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    px_gap = closeadj - _mean(closeadj, 252)
    base = g * px_gap
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxpkgap_252d_slope_v112_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    peak = closeadj.rolling(252, min_periods=63).max()
    gap = (closeadj - peak) / peak.replace(0, np.nan).abs()
    base = g * gap * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxlogcap_63d_slope_v113_signal(revenue, ebitda, capex, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = g * np.log(capex.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxratio_63d_slope_v114_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    rat = ebitda / revenue.replace(0, np.nan)
    base = g * rat * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxrevg_63d_slope_v115_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    rg = revenue.pct_change(63)
    base = g * rg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthdev_252d_slope_v116_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = (g - _mean(g, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxpxdet_252d_slope_v117_signal(revenue, ebitda, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    det = closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0
    base = g * det * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# === Composite slopes ===
def f26bph_f26_building_products_housing_compo_63d_slope_v118_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = (c + g) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_compo_252d_slope_v119_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = (c + g) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyseason_63d_slope_v120_signal(revenue, closeadj):
    a = _f26_housing_cycle_proxy(revenue, 63)
    b = _f26_demand_seasonality(revenue, 63)
    base = (a - b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyseason_252d_slope_v121_signal(revenue, closeadj):
    a = _f26_housing_cycle_proxy(revenue, 252)
    b = _f26_demand_seasonality(revenue, 252)
    base = a * b * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycplusg_252d_slope_v122_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = (0.6 * c + 0.4 * g) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycplusg_63d_slope_v123_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    base = (0.6 * c + 0.4 * g) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyminussns_21d_slope_v124_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 21)
    s = _f26_demand_seasonality(revenue, 21)
    base = (c - s) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyminussns_126d_slope_v125_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 126)
    s = _f26_demand_seasonality(revenue, 126)
    base = (c - s) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_compo3_252d_slope_v126_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    s = _f26_demand_seasonality(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = (c + s + g) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_compow_252d_slope_v127_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    s = _f26_demand_seasonality(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = (0.5 * c + 0.3 * s + 0.2 * g) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexseason_252d_slope_v128_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    s = _f26_demand_seasonality(revenue, 252)
    base = c * s * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexgrowth_252d_slope_v129_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = c * g * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxgrowth_252d_slope_v130_signal(revenue, ebitda, closeadj):
    s = _f26_demand_seasonality(revenue, 252)
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = s * g * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexcapsign_63d_slope_v131_signal(revenue, capex, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    cap_sign = np.sign(capex.diff(63))
    base = c * cap_sign * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexrevg_63d_slope_v132_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    rg = revenue.pct_change(63)
    base = c * (1.0 + rg) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexratio_252d_slope_v133_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    rat = ebitda / revenue.replace(0, np.nan)
    base = c * rat * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexebitg_63d_slope_v134_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    eg = ebitda.pct_change(63)
    base = c * eg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexebitg_252d_slope_v135_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    eg = ebitda.pct_change(252)
    base = c * eg * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexcapexlvl_63d_slope_v136_signal(revenue, capex, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * _mean(capex, 63) / _mean(revenue, 63).replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclevsebitda_63d_slope_v137_signal(revenue, ebitda, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) / (ebitda / revenue.replace(0, np.nan)).replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexrev_63d_slope_v138_signal(revenue, closeadj):
    base = _f26_housing_cycle_proxy(revenue, 63) * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxrev_63d_slope_v139_signal(revenue, closeadj):
    s = _f26_demand_seasonality(revenue, 63)
    rev_chg = revenue.pct_change(21)
    base = s * rev_chg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cycledev_252d_slope_v140_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    base = (c - _mean(c, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclesignxvol_63d_slope_v141_signal(revenue, volume, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    sg = np.sign(c)
    base = sg * closeadj * _z(volume, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxvol_252d_slope_v142_signal(revenue, ebitda, volume, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 252)
    base = g * _z(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexvolclose_63d_slope_v143_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 63)
    base = c * _std(closeadj, 63) * np.sign(closeadj)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxebmgn_63d_slope_v144_signal(revenue, ebitda, closeadj):
    s = _f26_demand_seasonality(revenue, 63)
    em = ebitda / revenue.replace(0, np.nan)
    base = s * em * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexlogrev_252d_slope_v145_signal(revenue, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    base = c * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexcapexz_252d_slope_v146_signal(revenue, capex, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    base = c * _z(capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_cyclexebitval_252d_slope_v147_signal(revenue, ebitda, closeadj):
    c = _f26_housing_cycle_proxy(revenue, 252)
    base = c * np.log(ebitda.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxebitval_63d_slope_v148_signal(revenue, ebitda, closeadj):
    s = _f26_demand_seasonality(revenue, 63)
    base = s * np.log(ebitda.replace(0, np.nan).abs()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_seasonxcaprev_252d_slope_v149_signal(revenue, capex, closeadj):
    s = _f26_demand_seasonality(revenue, 252)
    capr = capex / revenue.replace(0, np.nan)
    base = s * _z(capr, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f26bph_f26_building_products_housing_growthxcaprev_63d_slope_v150_signal(revenue, ebitda, capex, closeadj):
    g = _f26_housing_growth_signal(revenue, ebitda, 63)
    capr = capex / revenue.replace(0, np.nan)
    base = g * _z(capr, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26bph_f26_building_products_housing_cycle_21d_slope_v001_signal,
    f26bph_f26_building_products_housing_cycle_21d_slope_v002_signal,
    f26bph_f26_building_products_housing_cycle_63d_slope_v003_signal,
    f26bph_f26_building_products_housing_cycle_63d_slope_v004_signal,
    f26bph_f26_building_products_housing_cycle_126d_slope_v005_signal,
    f26bph_f26_building_products_housing_cycle_126d_slope_v006_signal,
    f26bph_f26_building_products_housing_cycle_252d_slope_v007_signal,
    f26bph_f26_building_products_housing_cycle_252d_slope_v008_signal,
    f26bph_f26_building_products_housing_cycle_252d_slope_v009_signal,
    f26bph_f26_building_products_housing_cycle_504d_slope_v010_signal,
    f26bph_f26_building_products_housing_cycle_504d_slope_v011_signal,
    f26bph_f26_building_products_housing_cycle_5d_slope_v012_signal,
    f26bph_f26_building_products_housing_cycle_42d_slope_v013_signal,
    f26bph_f26_building_products_housing_cycle_42d_slope_v014_signal,
    f26bph_f26_building_products_housing_cycle_189d_slope_v015_signal,
    f26bph_f26_building_products_housing_cycle_378d_slope_v016_signal,
    f26bph_f26_building_products_housing_cyclema_63d_slope_v017_signal,
    f26bph_f26_building_products_housing_cyclema_252d_slope_v018_signal,
    f26bph_f26_building_products_housing_cyclestd_63d_slope_v019_signal,
    f26bph_f26_building_products_housing_cyclestd_252d_slope_v020_signal,
    f26bph_f26_building_products_housing_cyclez_63d_slope_v021_signal,
    f26bph_f26_building_products_housing_cyclez_252d_slope_v022_signal,
    f26bph_f26_building_products_housing_cycleabs_63d_slope_v023_signal,
    f26bph_f26_building_products_housing_cycleabs_252d_slope_v024_signal,
    f26bph_f26_building_products_housing_cyclesq_63d_slope_v025_signal,
    f26bph_f26_building_products_housing_cyclesq_252d_slope_v026_signal,
    f26bph_f26_building_products_housing_cyclexcapex_63d_slope_v027_signal,
    f26bph_f26_building_products_housing_cyclexcapex_252d_slope_v028_signal,
    f26bph_f26_building_products_housing_cyclexebitda_63d_slope_v029_signal,
    f26bph_f26_building_products_housing_cyclexebitda_252d_slope_v030_signal,
    f26bph_f26_building_products_housing_cyclexpx_63d_slope_v031_signal,
    f26bph_f26_building_products_housing_cyclexpx_252d_slope_v032_signal,
    f26bph_f26_building_products_housing_cyclelogpx_63d_slope_v033_signal,
    f26bph_f26_building_products_housing_cyclelogpx_252d_slope_v034_signal,
    f26bph_f26_building_products_housing_cyclexdv_63d_slope_v035_signal,
    f26bph_f26_building_products_housing_cyclexdv_252d_slope_v036_signal,
    f26bph_f26_building_products_housing_cyclerank_252d_slope_v037_signal,
    f26bph_f26_building_products_housing_cyclerank_504d_slope_v038_signal,
    f26bph_f26_building_products_housing_cyclediff_63d_slope_v039_signal,
    f26bph_f26_building_products_housing_cyclediff_252d_slope_v040_signal,
    f26bph_f26_building_products_housing_cycleema_21_slope_v041_signal,
    f26bph_f26_building_products_housing_cycleema_63_slope_v042_signal,
    f26bph_f26_building_products_housing_cyclexvol_63d_slope_v043_signal,
    f26bph_f26_building_products_housing_cyclexvol_252d_slope_v044_signal,
    f26bph_f26_building_products_housing_cyclevsstd_63d_slope_v045_signal,
    f26bph_f26_building_products_housing_cyclevsstd_252d_slope_v046_signal,
    f26bph_f26_building_products_housing_cyclexpkgap_252d_slope_v047_signal,
    f26bph_f26_building_products_housing_cyclexlogcap_252d_slope_v048_signal,
    f26bph_f26_building_products_housing_cyclexrange_252d_slope_v049_signal,
    f26bph_f26_building_products_housing_cyclexpxdet_252d_slope_v050_signal,
    f26bph_f26_building_products_housing_season_21d_slope_v051_signal,
    f26bph_f26_building_products_housing_season_63d_slope_v052_signal,
    f26bph_f26_building_products_housing_season_63d_slope_v053_signal,
    f26bph_f26_building_products_housing_season_126d_slope_v054_signal,
    f26bph_f26_building_products_housing_season_126d_slope_v055_signal,
    f26bph_f26_building_products_housing_season_252d_slope_v056_signal,
    f26bph_f26_building_products_housing_season_252d_slope_v057_signal,
    f26bph_f26_building_products_housing_season_5d_slope_v058_signal,
    f26bph_f26_building_products_housing_season_42d_slope_v059_signal,
    f26bph_f26_building_products_housing_season_189d_slope_v060_signal,
    f26bph_f26_building_products_housing_season_378d_slope_v061_signal,
    f26bph_f26_building_products_housing_seasonma_21d_slope_v062_signal,
    f26bph_f26_building_products_housing_seasonma_126d_slope_v063_signal,
    f26bph_f26_building_products_housing_seasonstd_252d_slope_v064_signal,
    f26bph_f26_building_products_housing_seasonz_63d_slope_v065_signal,
    f26bph_f26_building_products_housing_seasonz_252d_slope_v066_signal,
    f26bph_f26_building_products_housing_seasonabs_63d_slope_v067_signal,
    f26bph_f26_building_products_housing_seasonsq_63d_slope_v068_signal,
    f26bph_f26_building_products_housing_seasonsq_252d_slope_v069_signal,
    f26bph_f26_building_products_housing_seasonxcapex_63d_slope_v070_signal,
    f26bph_f26_building_products_housing_seasonxcapex_252d_slope_v071_signal,
    f26bph_f26_building_products_housing_seasonlogpx_63d_slope_v072_signal,
    f26bph_f26_building_products_housing_seasonxdv_63d_slope_v073_signal,
    f26bph_f26_building_products_housing_seasonxvolz_252d_slope_v074_signal,
    f26bph_f26_building_products_housing_seasonema_21_slope_v075_signal,
    f26bph_f26_building_products_housing_seasonema_63_slope_v076_signal,
    f26bph_f26_building_products_housing_seasonrank_252d_slope_v077_signal,
    f26bph_f26_building_products_housing_seasonrank_504d_slope_v078_signal,
    f26bph_f26_building_products_housing_seasonxpkgap_252d_slope_v079_signal,
    f26bph_f26_building_products_housing_seasonxlogcap_252d_slope_v080_signal,
    f26bph_f26_building_products_housing_seasonxrange_63d_slope_v081_signal,
    f26bph_f26_building_products_housing_seasonxpxdet_252d_slope_v082_signal,
    f26bph_f26_building_products_housing_seasonxrevg_252d_slope_v083_signal,
    f26bph_f26_building_products_housing_seasonxebitg_252d_slope_v084_signal,
    f26bph_f26_building_products_housing_seasondev_252d_slope_v085_signal,
    f26bph_f26_building_products_housing_growth_21d_slope_v086_signal,
    f26bph_f26_building_products_housing_growth_63d_slope_v087_signal,
    f26bph_f26_building_products_housing_growth_63d_slope_v088_signal,
    f26bph_f26_building_products_housing_growth_126d_slope_v089_signal,
    f26bph_f26_building_products_housing_growth_126d_slope_v090_signal,
    f26bph_f26_building_products_housing_growth_252d_slope_v091_signal,
    f26bph_f26_building_products_housing_growth_252d_slope_v092_signal,
    f26bph_f26_building_products_housing_growth_5d_slope_v093_signal,
    f26bph_f26_building_products_housing_growth_42d_slope_v094_signal,
    f26bph_f26_building_products_housing_growth_189d_slope_v095_signal,
    f26bph_f26_building_products_housing_growth_504d_slope_v096_signal,
    f26bph_f26_building_products_housing_growthma_63d_slope_v097_signal,
    f26bph_f26_building_products_housing_growthstd_252d_slope_v098_signal,
    f26bph_f26_building_products_housing_growthz_63d_slope_v099_signal,
    f26bph_f26_building_products_housing_growthz_252d_slope_v100_signal,
    f26bph_f26_building_products_housing_growthsq_63d_slope_v101_signal,
    f26bph_f26_building_products_housing_growthsq_252d_slope_v102_signal,
    f26bph_f26_building_products_housing_growthxcapex_63d_slope_v103_signal,
    f26bph_f26_building_products_housing_growthxcaprev_63d_slope_v104_signal,
    f26bph_f26_building_products_housing_growthlogpx_63d_slope_v105_signal,
    f26bph_f26_building_products_housing_growthxdv_252d_slope_v106_signal,
    f26bph_f26_building_products_housing_growthrank_252d_slope_v107_signal,
    f26bph_f26_building_products_housing_growthrank_504d_slope_v108_signal,
    f26bph_f26_building_products_housing_growthema_21_slope_v109_signal,
    f26bph_f26_building_products_housing_growthema_63_slope_v110_signal,
    f26bph_f26_building_products_housing_growthxpxgap_252d_slope_v111_signal,
    f26bph_f26_building_products_housing_growthxpkgap_252d_slope_v112_signal,
    f26bph_f26_building_products_housing_growthxlogcap_63d_slope_v113_signal,
    f26bph_f26_building_products_housing_growthxratio_63d_slope_v114_signal,
    f26bph_f26_building_products_housing_growthxrevg_63d_slope_v115_signal,
    f26bph_f26_building_products_housing_growthdev_252d_slope_v116_signal,
    f26bph_f26_building_products_housing_growthxpxdet_252d_slope_v117_signal,
    f26bph_f26_building_products_housing_compo_63d_slope_v118_signal,
    f26bph_f26_building_products_housing_compo_252d_slope_v119_signal,
    f26bph_f26_building_products_housing_cyseason_63d_slope_v120_signal,
    f26bph_f26_building_products_housing_cyseason_252d_slope_v121_signal,
    f26bph_f26_building_products_housing_cycplusg_252d_slope_v122_signal,
    f26bph_f26_building_products_housing_cycplusg_63d_slope_v123_signal,
    f26bph_f26_building_products_housing_cyminussns_21d_slope_v124_signal,
    f26bph_f26_building_products_housing_cyminussns_126d_slope_v125_signal,
    f26bph_f26_building_products_housing_compo3_252d_slope_v126_signal,
    f26bph_f26_building_products_housing_compow_252d_slope_v127_signal,
    f26bph_f26_building_products_housing_cyclexseason_252d_slope_v128_signal,
    f26bph_f26_building_products_housing_cyclexgrowth_252d_slope_v129_signal,
    f26bph_f26_building_products_housing_seasonxgrowth_252d_slope_v130_signal,
    f26bph_f26_building_products_housing_cyclexcapsign_63d_slope_v131_signal,
    f26bph_f26_building_products_housing_cyclexrevg_63d_slope_v132_signal,
    f26bph_f26_building_products_housing_cyclexratio_252d_slope_v133_signal,
    f26bph_f26_building_products_housing_cyclexebitg_63d_slope_v134_signal,
    f26bph_f26_building_products_housing_cyclexebitg_252d_slope_v135_signal,
    f26bph_f26_building_products_housing_cyclexcapexlvl_63d_slope_v136_signal,
    f26bph_f26_building_products_housing_cyclevsebitda_63d_slope_v137_signal,
    f26bph_f26_building_products_housing_cyclexrev_63d_slope_v138_signal,
    f26bph_f26_building_products_housing_seasonxrev_63d_slope_v139_signal,
    f26bph_f26_building_products_housing_cycledev_252d_slope_v140_signal,
    f26bph_f26_building_products_housing_cyclesignxvol_63d_slope_v141_signal,
    f26bph_f26_building_products_housing_growthxvol_252d_slope_v142_signal,
    f26bph_f26_building_products_housing_cyclexvolclose_63d_slope_v143_signal,
    f26bph_f26_building_products_housing_seasonxebmgn_63d_slope_v144_signal,
    f26bph_f26_building_products_housing_cyclexlogrev_252d_slope_v145_signal,
    f26bph_f26_building_products_housing_cyclexcapexz_252d_slope_v146_signal,
    f26bph_f26_building_products_housing_cyclexebitval_252d_slope_v147_signal,
    f26bph_f26_building_products_housing_seasonxebitval_63d_slope_v148_signal,
    f26bph_f26_building_products_housing_seasonxcaprev_252d_slope_v149_signal,
    f26bph_f26_building_products_housing_growthxcaprev_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_BUILDING_PRODUCTS_HOUSING_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "capex": capex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_housing_cycle_proxy", "_f26_demand_seasonality", "_f26_housing_growth_signal")
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
    print(f"OK f26_building_products_housing_2nd_derivatives_001_150_claude: {n_features} features pass")
