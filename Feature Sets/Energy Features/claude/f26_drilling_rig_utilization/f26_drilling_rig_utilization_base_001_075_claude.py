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


# ===== folder domain primitives =====
def _f26_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f26_utilization_proxy(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan)
    return rpa.rolling(w, min_periods=max(1, w // 2)).mean()


def _f26_rig_intensity(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan)
    base = rpa.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = rpa.rolling(w, min_periods=max(1, w // 2)).std()
    return base / sd.replace(0, np.nan)


# ===== features =====

def f26dru_f26_drilling_rig_utilization_rpa_base_xc_base_v001_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xc_base_v002_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc_base_v003_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xc_base_v004_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc_base_v005_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xc_base_v006_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc_base_v007_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xc_base_v008_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc_base_v009_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xc_base_v010_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc_base_v011_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xc_base_v012_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc_base_v013_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xc_base_v014_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc_base_v015_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xc_base_v016_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc_base_v017_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xc_base_v018_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc_base_v019_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xc_base_v020_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc_base_v021_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xc_base_v022_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc_base_v023_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    result = (base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_xc2_base_v024_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xc2_base_v025_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc2_base_v026_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xc2_base_v027_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc2_base_v028_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xc2_base_v029_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc2_base_v030_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xc2_base_v031_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc2_base_v032_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xc2_base_v033_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc2_base_v034_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xc2_base_v035_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc2_base_v036_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xc2_base_v037_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc2_base_v038_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xc2_base_v039_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc2_base_v040_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xc2_base_v041_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc2_base_v042_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xc2_base_v043_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc2_base_v044_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xc2_base_v045_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc2_base_v046_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    result = (base) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_xmc_base_v047_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xmc_base_v048_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xmc_base_v049_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xmc_base_v050_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xmc_base_v051_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xmc_base_v052_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xmc_base_v053_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xmc_base_v054_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xmc_base_v055_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xmc_base_v056_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xmc_base_v057_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xmc_base_v058_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xmc_base_v059_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xmc_base_v060_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xmc_base_v061_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xmc_base_v062_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xmc_base_v063_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xmc_base_v064_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xmc_base_v065_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xmc_base_v066_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xmc_base_v067_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xmc_base_v068_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xmc_base_v069_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_xzc_base_v070_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xzc_base_v071_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xzc_base_v072_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xzc_base_v073_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xzc_base_v074_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xzc_base_v075_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26dru_f26_drilling_rig_utilization_rpa_base_xc_base_v001_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xc_base_v002_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc_base_v003_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xc_base_v004_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc_base_v005_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xc_base_v006_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc_base_v007_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xc_base_v008_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc_base_v009_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xc_base_v010_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc_base_v011_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xc_base_v012_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc_base_v013_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xc_base_v014_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc_base_v015_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xc_base_v016_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc_base_v017_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xc_base_v018_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc_base_v019_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xc_base_v020_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc_base_v021_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xc_base_v022_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc_base_v023_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_xc2_base_v024_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xc2_base_v025_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc2_base_v026_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xc2_base_v027_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc2_base_v028_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xc2_base_v029_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc2_base_v030_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xc2_base_v031_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc2_base_v032_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xc2_base_v033_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc2_base_v034_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xc2_base_v035_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc2_base_v036_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xc2_base_v037_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc2_base_v038_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xc2_base_v039_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc2_base_v040_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xc2_base_v041_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc2_base_v042_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xc2_base_v043_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc2_base_v044_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xc2_base_v045_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc2_base_v046_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_xmc_base_v047_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xmc_base_v048_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xmc_base_v049_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xmc_base_v050_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xmc_base_v051_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xmc_base_v052_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xmc_base_v053_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xmc_base_v054_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xmc_base_v055_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xmc_base_v056_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xmc_base_v057_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xmc_base_v058_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xmc_base_v059_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xmc_base_v060_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xmc_base_v061_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xmc_base_v062_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xmc_base_v063_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xmc_base_v064_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xmc_base_v065_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xmc_base_v066_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xmc_base_v067_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xmc_base_v068_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xmc_base_v069_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_xzc_base_v070_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xzc_base_v071_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xzc_base_v072_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xzc_base_v073_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xzc_base_v074_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xzc_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_DRILLING_RIG_UTILIZATION_REGISTRY_001_075 = REGISTRY


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
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda,
        "assets": assets, "equity": equity, "debt": debt, "cashneq": cashneq,
        "deferredrev": deferredrev, "ppnenet": ppnenet, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f26_revenue_per_asset', '_f26_utilization_proxy', '_f26_rig_intensity',)
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
    print(f"OK f26_drilling_rig_utilization_base_001_075_claude: {n_features} features pass")
