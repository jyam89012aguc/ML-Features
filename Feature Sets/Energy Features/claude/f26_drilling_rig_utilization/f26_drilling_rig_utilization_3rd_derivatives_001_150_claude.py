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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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

def f26dru_f26_drilling_rig_utilization_rpa_base_xc_jsw5_jerk_v001_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xc_jsw5_jerk_v002_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc_jsw5_jerk_v003_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xc_jsw5_jerk_v004_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc_jsw5_jerk_v005_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xc_jsw5_jerk_v006_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc_jsw5_jerk_v007_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xc_jsw5_jerk_v008_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc_jsw5_jerk_v009_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xc_jsw5_jerk_v010_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc_jsw5_jerk_v011_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xc_jsw5_jerk_v012_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc_jsw5_jerk_v013_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xc_jsw5_jerk_v014_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc_jsw5_jerk_v015_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xc_jsw5_jerk_v016_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc_jsw5_jerk_v017_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xc_jsw5_jerk_v018_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc_jsw5_jerk_v019_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xc_jsw5_jerk_v020_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc_jsw5_jerk_v021_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xc_jsw5_jerk_v022_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc_jsw5_jerk_v023_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_xc2_jsw5_jerk_v024_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xc2_jsw5_jerk_v025_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc2_jsw5_jerk_v026_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xc2_jsw5_jerk_v027_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc2_jsw5_jerk_v028_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xc2_jsw5_jerk_v029_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc2_jsw5_jerk_v030_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xc2_jsw5_jerk_v031_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc2_jsw5_jerk_v032_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xc2_jsw5_jerk_v033_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc2_jsw5_jerk_v034_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xc2_jsw5_jerk_v035_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc2_jsw5_jerk_v036_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xc2_jsw5_jerk_v037_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc2_jsw5_jerk_v038_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xc2_jsw5_jerk_v039_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc2_jsw5_jerk_v040_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xc2_jsw5_jerk_v041_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc2_jsw5_jerk_v042_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xc2_jsw5_jerk_v043_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc2_jsw5_jerk_v044_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xc2_jsw5_jerk_v045_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc2_jsw5_jerk_v046_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_xmc_jsw5_jerk_v047_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xmc_jsw5_jerk_v048_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xmc_jsw5_jerk_v049_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xmc_jsw5_jerk_v050_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xmc_jsw5_jerk_v051_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xmc_jsw5_jerk_v052_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xmc_jsw5_jerk_v053_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xmc_jsw5_jerk_v054_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xmc_jsw5_jerk_v055_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xmc_jsw5_jerk_v056_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xmc_jsw5_jerk_v057_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xmc_jsw5_jerk_v058_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xmc_jsw5_jerk_v059_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xmc_jsw5_jerk_v060_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xmc_jsw5_jerk_v061_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xmc_jsw5_jerk_v062_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xmc_jsw5_jerk_v063_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xmc_jsw5_jerk_v064_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xmc_jsw5_jerk_v065_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xmc_jsw5_jerk_v066_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xmc_jsw5_jerk_v067_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xmc_jsw5_jerk_v068_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xmc_jsw5_jerk_v069_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_xzc_jsw5_jerk_v070_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_xzc_jsw5_jerk_v071_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_xzc_jsw5_jerk_v072_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_xzc_jsw5_jerk_v073_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_xzc_jsw5_jerk_v074_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_xzc_jsw5_jerk_v075_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xzc_jsw5_jerk_v076_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xzc_jsw5_jerk_v077_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xzc_jsw5_jerk_v078_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xzc_jsw5_jerk_v079_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xzc_jsw5_jerk_v080_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xzc_jsw5_jerk_v081_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xzc_jsw5_jerk_v082_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xzc_jsw5_jerk_v083_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xzc_jsw5_jerk_v084_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xzc_jsw5_jerk_v085_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xzc_jsw5_jerk_v086_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xzc_jsw5_jerk_v087_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xzc_jsw5_jerk_v088_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xzc_jsw5_jerk_v089_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xzc_jsw5_jerk_v090_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xzc_jsw5_jerk_v091_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xzc_jsw5_jerk_v092_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_dmc_jsw5_jerk_v093_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_dmc_jsw5_jerk_v094_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_dmc_jsw5_jerk_v095_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_dmc_jsw5_jerk_v096_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_dmc_jsw5_jerk_v097_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_dmc_jsw5_jerk_v098_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_dmc_jsw5_jerk_v099_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_dmc_jsw5_jerk_v100_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_dmc_jsw5_jerk_v101_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_dmc_jsw5_jerk_v102_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_dmc_jsw5_jerk_v103_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_dmc_jsw5_jerk_v104_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_dmc_jsw5_jerk_v105_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_dmc_jsw5_jerk_v106_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_dmc_jsw5_jerk_v107_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_dmc_jsw5_jerk_v108_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_dmc_jsw5_jerk_v109_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_dmc_jsw5_jerk_v110_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_dmc_jsw5_jerk_v111_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_dmc_jsw5_jerk_v112_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_dmc_jsw5_jerk_v113_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_dmc_jsw5_jerk_v114_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_dmc_jsw5_jerk_v115_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_m21_xc_jsw5_jerk_v116_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_m21_xc_jsw5_jerk_v117_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc_jsw5_jerk_v118_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_m21_xc_jsw5_jerk_v119_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc_jsw5_jerk_v120_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_m21_xc_jsw5_jerk_v121_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc_jsw5_jerk_v122_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_m21_xc_jsw5_jerk_v123_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc_jsw5_jerk_v124_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_m21_xc_jsw5_jerk_v125_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc_jsw5_jerk_v126_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_m21_xc_jsw5_jerk_v127_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_m21_xc_jsw5_jerk_v128_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_m21_xc_jsw5_jerk_v129_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_m21_xc_jsw5_jerk_v130_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_m21_xc_jsw5_jerk_v131_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_m21_xc_jsw5_jerk_v132_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_m21_xc_jsw5_jerk_v133_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_m21_xc_jsw5_jerk_v134_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_m21_xc_jsw5_jerk_v135_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_m21_xc_jsw5_jerk_v136_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_m21_xc_jsw5_jerk_v137_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_m21_xc_jsw5_jerk_v138_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    base = (_mean(base, 21)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_m21_xc2_jsw5_jerk_v139_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_m21_xc2_jsw5_jerk_v140_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc2_jsw5_jerk_v141_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_m21_xc2_jsw5_jerk_v142_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc2_jsw5_jerk_v143_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_m21_xc2_jsw5_jerk_v144_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc2_jsw5_jerk_v145_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_m21_xc2_jsw5_jerk_v146_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc2_jsw5_jerk_v147_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_m21_xc2_jsw5_jerk_v148_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc2_jsw5_jerk_v149_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_m21_xc2_jsw5_jerk_v150_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    base = (_mean(base, 21)) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26dru_f26_drilling_rig_utilization_rpa_base_xc_jsw5_jerk_v001_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xc_jsw5_jerk_v002_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc_jsw5_jerk_v003_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xc_jsw5_jerk_v004_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc_jsw5_jerk_v005_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xc_jsw5_jerk_v006_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc_jsw5_jerk_v007_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xc_jsw5_jerk_v008_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc_jsw5_jerk_v009_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xc_jsw5_jerk_v010_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc_jsw5_jerk_v011_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xc_jsw5_jerk_v012_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc_jsw5_jerk_v013_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xc_jsw5_jerk_v014_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc_jsw5_jerk_v015_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xc_jsw5_jerk_v016_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc_jsw5_jerk_v017_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xc_jsw5_jerk_v018_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc_jsw5_jerk_v019_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xc_jsw5_jerk_v020_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc_jsw5_jerk_v021_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xc_jsw5_jerk_v022_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc_jsw5_jerk_v023_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_xc2_jsw5_jerk_v024_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xc2_jsw5_jerk_v025_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xc2_jsw5_jerk_v026_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xc2_jsw5_jerk_v027_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xc2_jsw5_jerk_v028_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xc2_jsw5_jerk_v029_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xc2_jsw5_jerk_v030_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xc2_jsw5_jerk_v031_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xc2_jsw5_jerk_v032_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xc2_jsw5_jerk_v033_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xc2_jsw5_jerk_v034_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xc2_jsw5_jerk_v035_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xc2_jsw5_jerk_v036_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xc2_jsw5_jerk_v037_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xc2_jsw5_jerk_v038_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xc2_jsw5_jerk_v039_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xc2_jsw5_jerk_v040_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xc2_jsw5_jerk_v041_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xc2_jsw5_jerk_v042_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xc2_jsw5_jerk_v043_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xc2_jsw5_jerk_v044_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xc2_jsw5_jerk_v045_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xc2_jsw5_jerk_v046_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_xmc_jsw5_jerk_v047_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xmc_jsw5_jerk_v048_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xmc_jsw5_jerk_v049_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xmc_jsw5_jerk_v050_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xmc_jsw5_jerk_v051_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xmc_jsw5_jerk_v052_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xmc_jsw5_jerk_v053_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xmc_jsw5_jerk_v054_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xmc_jsw5_jerk_v055_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xmc_jsw5_jerk_v056_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xmc_jsw5_jerk_v057_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xmc_jsw5_jerk_v058_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xmc_jsw5_jerk_v059_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xmc_jsw5_jerk_v060_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xmc_jsw5_jerk_v061_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xmc_jsw5_jerk_v062_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xmc_jsw5_jerk_v063_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xmc_jsw5_jerk_v064_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xmc_jsw5_jerk_v065_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xmc_jsw5_jerk_v066_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xmc_jsw5_jerk_v067_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xmc_jsw5_jerk_v068_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xmc_jsw5_jerk_v069_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_xzc_jsw5_jerk_v070_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_xzc_jsw5_jerk_v071_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_xzc_jsw5_jerk_v072_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_xzc_jsw5_jerk_v073_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_xzc_jsw5_jerk_v074_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_xzc_jsw5_jerk_v075_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xzc_jsw5_jerk_v076_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xzc_jsw5_jerk_v077_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xzc_jsw5_jerk_v078_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xzc_jsw5_jerk_v079_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xzc_jsw5_jerk_v080_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xzc_jsw5_jerk_v081_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xzc_jsw5_jerk_v082_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xzc_jsw5_jerk_v083_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xzc_jsw5_jerk_v084_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xzc_jsw5_jerk_v085_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xzc_jsw5_jerk_v086_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xzc_jsw5_jerk_v087_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xzc_jsw5_jerk_v088_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xzc_jsw5_jerk_v089_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xzc_jsw5_jerk_v090_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xzc_jsw5_jerk_v091_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xzc_jsw5_jerk_v092_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_dmc_jsw5_jerk_v093_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_dmc_jsw5_jerk_v094_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_dmc_jsw5_jerk_v095_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_dmc_jsw5_jerk_v096_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_dmc_jsw5_jerk_v097_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_dmc_jsw5_jerk_v098_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_dmc_jsw5_jerk_v099_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_dmc_jsw5_jerk_v100_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_dmc_jsw5_jerk_v101_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_dmc_jsw5_jerk_v102_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_dmc_jsw5_jerk_v103_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_dmc_jsw5_jerk_v104_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_dmc_jsw5_jerk_v105_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_dmc_jsw5_jerk_v106_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_dmc_jsw5_jerk_v107_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_dmc_jsw5_jerk_v108_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_dmc_jsw5_jerk_v109_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_dmc_jsw5_jerk_v110_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_dmc_jsw5_jerk_v111_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_dmc_jsw5_jerk_v112_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_dmc_jsw5_jerk_v113_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_dmc_jsw5_jerk_v114_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_dmc_jsw5_jerk_v115_signal,
    f26dru_f26_drilling_rig_utilization_rpa_m21_xc_jsw5_jerk_v116_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_m21_xc_jsw5_jerk_v117_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc_jsw5_jerk_v118_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_m21_xc_jsw5_jerk_v119_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc_jsw5_jerk_v120_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_m21_xc_jsw5_jerk_v121_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc_jsw5_jerk_v122_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_m21_xc_jsw5_jerk_v123_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc_jsw5_jerk_v124_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_m21_xc_jsw5_jerk_v125_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc_jsw5_jerk_v126_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_m21_xc_jsw5_jerk_v127_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_m21_xc_jsw5_jerk_v128_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_m21_xc_jsw5_jerk_v129_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_m21_xc_jsw5_jerk_v130_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_m21_xc_jsw5_jerk_v131_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_m21_xc_jsw5_jerk_v132_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_m21_xc_jsw5_jerk_v133_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_m21_xc_jsw5_jerk_v134_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_m21_xc_jsw5_jerk_v135_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_m21_xc_jsw5_jerk_v136_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_m21_xc_jsw5_jerk_v137_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_m21_xc_jsw5_jerk_v138_signal,
    f26dru_f26_drilling_rig_utilization_rpa_m21_xc2_jsw5_jerk_v139_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_m21_xc2_jsw5_jerk_v140_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc2_jsw5_jerk_v141_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_m21_xc2_jsw5_jerk_v142_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc2_jsw5_jerk_v143_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_m21_xc2_jsw5_jerk_v144_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc2_jsw5_jerk_v145_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_m21_xc2_jsw5_jerk_v146_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc2_jsw5_jerk_v147_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_m21_xc2_jsw5_jerk_v148_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc2_jsw5_jerk_v149_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_m21_xc2_jsw5_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_DRILLING_RIG_UTILIZATION_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f26_drilling_rig_utilization_3rd_derivatives_001_150_claude: {n_features} features pass")
