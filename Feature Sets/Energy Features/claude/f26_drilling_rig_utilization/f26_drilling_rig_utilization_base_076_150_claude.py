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

def f26dru_f26_drilling_rig_utilization_rigint_21d_base_xzc_base_v076_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_xzc_base_v077_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_xzc_base_v078_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_xzc_base_v079_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_xzc_base_v080_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_xzc_base_v081_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_xzc_base_v082_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_xzc_base_v083_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_xzc_base_v084_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_xzc_base_v085_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_xzc_base_v086_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_xzc_base_v087_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_xzc_base_v088_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_xzc_base_v089_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_xzc_base_v090_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_xzc_base_v091_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_xzc_base_v092_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_base_dmc_base_v093_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_base_dmc_base_v094_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_base_dmc_base_v095_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_base_dmc_base_v096_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_base_dmc_base_v097_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_base_dmc_base_v098_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_base_dmc_base_v099_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_base_dmc_base_v100_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_base_dmc_base_v101_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_base_dmc_base_v102_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_base_dmc_base_v103_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_base_dmc_base_v104_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_base_dmc_base_v105_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_base_dmc_base_v106_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_base_dmc_base_v107_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_base_dmc_base_v108_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_base_dmc_base_v109_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_base_dmc_base_v110_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_base_dmc_base_v111_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_base_dmc_base_v112_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_base_dmc_base_v113_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_base_dmc_base_v114_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_base_dmc_base_v115_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_m21_xc_base_v116_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_m21_xc_base_v117_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc_base_v118_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_m21_xc_base_v119_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc_base_v120_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_m21_xc_base_v121_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc_base_v122_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_m21_xc_base_v123_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc_base_v124_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_m21_xc_base_v125_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc_base_v126_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_m21_xc_base_v127_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_84d_m21_xc_base_v128_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 84)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_126d_m21_xc_base_v129_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_126d_m21_xc_base_v130_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_189d_m21_xc_base_v131_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 189)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_189d_m21_xc_base_v132_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 189)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_252d_m21_xc_base_v133_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 252)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_252d_m21_xc_base_v134_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 252)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_378d_m21_xc_base_v135_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 378)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_378d_m21_xc_base_v136_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 378)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_504d_m21_xc_base_v137_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 504)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_504d_m21_xc_base_v138_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 504)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rpa_m21_xc2_base_v139_signal(revenue, assets, closeadj):
    base = _f26_revenue_per_asset(revenue, assets)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_5d_m21_xc2_base_v140_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 5)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc2_base_v141_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 5)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_10d_m21_xc2_base_v142_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 10)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc2_base_v143_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 10)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_21d_m21_xc2_base_v144_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 21)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc2_base_v145_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 21)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_42d_m21_xc2_base_v146_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc2_base_v147_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_63d_m21_xc2_base_v148_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 63)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc2_base_v149_signal(revenue, ppnenet, closeadj):
    base = _f26_rig_intensity(revenue, ppnenet, 63)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f26dru_f26_drilling_rig_utilization_util_84d_m21_xc2_base_v150_signal(revenue, ppnenet, closeadj):
    base = _f26_utilization_proxy(revenue, ppnenet, 84)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_xzc_base_v076_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_xzc_base_v077_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_xzc_base_v078_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_xzc_base_v079_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_xzc_base_v080_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_xzc_base_v081_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_xzc_base_v082_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_xzc_base_v083_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_xzc_base_v084_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_xzc_base_v085_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_xzc_base_v086_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_xzc_base_v087_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_xzc_base_v088_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_xzc_base_v089_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_xzc_base_v090_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_xzc_base_v091_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_xzc_base_v092_signal,
    f26dru_f26_drilling_rig_utilization_rpa_base_dmc_base_v093_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_base_dmc_base_v094_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_base_dmc_base_v095_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_base_dmc_base_v096_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_base_dmc_base_v097_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_base_dmc_base_v098_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_base_dmc_base_v099_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_base_dmc_base_v100_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_base_dmc_base_v101_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_base_dmc_base_v102_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_base_dmc_base_v103_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_base_dmc_base_v104_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_base_dmc_base_v105_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_base_dmc_base_v106_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_base_dmc_base_v107_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_base_dmc_base_v108_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_base_dmc_base_v109_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_base_dmc_base_v110_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_base_dmc_base_v111_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_base_dmc_base_v112_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_base_dmc_base_v113_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_base_dmc_base_v114_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_base_dmc_base_v115_signal,
    f26dru_f26_drilling_rig_utilization_rpa_m21_xc_base_v116_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_m21_xc_base_v117_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc_base_v118_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_m21_xc_base_v119_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc_base_v120_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_m21_xc_base_v121_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc_base_v122_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_m21_xc_base_v123_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc_base_v124_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_m21_xc_base_v125_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc_base_v126_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_m21_xc_base_v127_signal,
    f26dru_f26_drilling_rig_utilization_rigint_84d_m21_xc_base_v128_signal,
    f26dru_f26_drilling_rig_utilization_util_126d_m21_xc_base_v129_signal,
    f26dru_f26_drilling_rig_utilization_rigint_126d_m21_xc_base_v130_signal,
    f26dru_f26_drilling_rig_utilization_util_189d_m21_xc_base_v131_signal,
    f26dru_f26_drilling_rig_utilization_rigint_189d_m21_xc_base_v132_signal,
    f26dru_f26_drilling_rig_utilization_util_252d_m21_xc_base_v133_signal,
    f26dru_f26_drilling_rig_utilization_rigint_252d_m21_xc_base_v134_signal,
    f26dru_f26_drilling_rig_utilization_util_378d_m21_xc_base_v135_signal,
    f26dru_f26_drilling_rig_utilization_rigint_378d_m21_xc_base_v136_signal,
    f26dru_f26_drilling_rig_utilization_util_504d_m21_xc_base_v137_signal,
    f26dru_f26_drilling_rig_utilization_rigint_504d_m21_xc_base_v138_signal,
    f26dru_f26_drilling_rig_utilization_rpa_m21_xc2_base_v139_signal,
    f26dru_f26_drilling_rig_utilization_util_5d_m21_xc2_base_v140_signal,
    f26dru_f26_drilling_rig_utilization_rigint_5d_m21_xc2_base_v141_signal,
    f26dru_f26_drilling_rig_utilization_util_10d_m21_xc2_base_v142_signal,
    f26dru_f26_drilling_rig_utilization_rigint_10d_m21_xc2_base_v143_signal,
    f26dru_f26_drilling_rig_utilization_util_21d_m21_xc2_base_v144_signal,
    f26dru_f26_drilling_rig_utilization_rigint_21d_m21_xc2_base_v145_signal,
    f26dru_f26_drilling_rig_utilization_util_42d_m21_xc2_base_v146_signal,
    f26dru_f26_drilling_rig_utilization_rigint_42d_m21_xc2_base_v147_signal,
    f26dru_f26_drilling_rig_utilization_util_63d_m21_xc2_base_v148_signal,
    f26dru_f26_drilling_rig_utilization_rigint_63d_m21_xc2_base_v149_signal,
    f26dru_f26_drilling_rig_utilization_util_84d_m21_xc2_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_DRILLING_RIG_UTILIZATION_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f26_drilling_rig_utilization_base_076_150_claude: {n_features} features pass")
