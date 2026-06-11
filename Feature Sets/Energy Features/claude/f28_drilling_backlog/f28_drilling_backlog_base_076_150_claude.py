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
def _f28_backlog_growth(deferredrev, w):
    return deferredrev.pct_change(periods=w)


def _f28_backlog_to_revenue(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


def _f28_drilling_backlog_score(deferredrev, w):
    g = deferredrev.pct_change(periods=w)
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return (g - m) / sd.replace(0, np.nan)


# ===== features =====

def f28dbk_f28_drilling_backlog_backg_42d_base_xzc_base_v076_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_base_xzc_base_v077_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_base_xzc_base_v078_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_base_xzc_base_v079_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_base_xzc_base_v080_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_base_xzc_base_v081_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_base_xzc_base_v082_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_base_xzc_base_v083_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_base_xzc_base_v084_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_base_xzc_base_v085_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_base_xzc_base_v086_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_base_xzc_base_v087_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_base_xzc_base_v088_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_base_xzc_base_v089_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_base_xzc_base_v090_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_base_xzc_base_v091_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_base_xzc_base_v092_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_base_dmc_base_v093_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_base_dmc_base_v094_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_base_dmc_base_v095_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_base_dmc_base_v096_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_base_dmc_base_v097_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_base_dmc_base_v098_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_base_dmc_base_v099_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_base_dmc_base_v100_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_base_dmc_base_v101_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_base_dmc_base_v102_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_base_dmc_base_v103_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_base_dmc_base_v104_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_base_dmc_base_v105_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_base_dmc_base_v106_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_base_dmc_base_v107_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_base_dmc_base_v108_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_base_dmc_base_v109_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_base_dmc_base_v110_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_base_dmc_base_v111_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_base_dmc_base_v112_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_base_dmc_base_v113_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_base_dmc_base_v114_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_base_dmc_base_v115_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_m21_xc_base_v116_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_m21_xc_base_v117_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_m21_xc_base_v118_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_m21_xc_base_v119_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_m21_xc_base_v120_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_m21_xc_base_v121_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_m21_xc_base_v122_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_m21_xc_base_v123_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_m21_xc_base_v124_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_m21_xc_base_v125_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_m21_xc_base_v126_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_m21_xc_base_v127_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_126d_m21_xc_base_v128_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_126d_m21_xc_base_v129_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_189d_m21_xc_base_v130_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 189)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_189d_m21_xc_base_v131_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 189)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_252d_m21_xc_base_v132_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 252)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_252d_m21_xc_base_v133_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 252)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_378d_m21_xc_base_v134_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 378)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_378d_m21_xc_base_v135_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 378)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_504d_m21_xc_base_v136_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 504)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_504d_m21_xc_base_v137_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 504)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_btr_m21_xc_base_v138_signal(deferredrev, revenue, closeadj):
    base = _f28_backlog_to_revenue(deferredrev, revenue)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_5d_m21_xc2_base_v139_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 5)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_5d_m21_xc2_base_v140_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 5)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_10d_m21_xc2_base_v141_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 10)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_10d_m21_xc2_base_v142_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 10)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_21d_m21_xc2_base_v143_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 21)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_21d_m21_xc2_base_v144_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 21)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_42d_m21_xc2_base_v145_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_42d_m21_xc2_base_v146_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_63d_m21_xc2_base_v147_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 63)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_63d_m21_xc2_base_v148_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 63)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backg_84d_m21_xc2_base_v149_signal(deferredrev, closeadj):
    base = _f28_backlog_growth(deferredrev, 84)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f28dbk_f28_drilling_backlog_backscore_84d_m21_xc2_base_v150_signal(deferredrev, closeadj):
    base = _f28_drilling_backlog_score(deferredrev, 84)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28dbk_f28_drilling_backlog_backg_42d_base_xzc_base_v076_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_base_xzc_base_v077_signal,
    f28dbk_f28_drilling_backlog_backg_63d_base_xzc_base_v078_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_base_xzc_base_v079_signal,
    f28dbk_f28_drilling_backlog_backg_84d_base_xzc_base_v080_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_base_xzc_base_v081_signal,
    f28dbk_f28_drilling_backlog_backg_126d_base_xzc_base_v082_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_base_xzc_base_v083_signal,
    f28dbk_f28_drilling_backlog_backg_189d_base_xzc_base_v084_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_base_xzc_base_v085_signal,
    f28dbk_f28_drilling_backlog_backg_252d_base_xzc_base_v086_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_base_xzc_base_v087_signal,
    f28dbk_f28_drilling_backlog_backg_378d_base_xzc_base_v088_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_base_xzc_base_v089_signal,
    f28dbk_f28_drilling_backlog_backg_504d_base_xzc_base_v090_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_base_xzc_base_v091_signal,
    f28dbk_f28_drilling_backlog_btr_base_xzc_base_v092_signal,
    f28dbk_f28_drilling_backlog_backg_5d_base_dmc_base_v093_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_base_dmc_base_v094_signal,
    f28dbk_f28_drilling_backlog_backg_10d_base_dmc_base_v095_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_base_dmc_base_v096_signal,
    f28dbk_f28_drilling_backlog_backg_21d_base_dmc_base_v097_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_base_dmc_base_v098_signal,
    f28dbk_f28_drilling_backlog_backg_42d_base_dmc_base_v099_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_base_dmc_base_v100_signal,
    f28dbk_f28_drilling_backlog_backg_63d_base_dmc_base_v101_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_base_dmc_base_v102_signal,
    f28dbk_f28_drilling_backlog_backg_84d_base_dmc_base_v103_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_base_dmc_base_v104_signal,
    f28dbk_f28_drilling_backlog_backg_126d_base_dmc_base_v105_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_base_dmc_base_v106_signal,
    f28dbk_f28_drilling_backlog_backg_189d_base_dmc_base_v107_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_base_dmc_base_v108_signal,
    f28dbk_f28_drilling_backlog_backg_252d_base_dmc_base_v109_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_base_dmc_base_v110_signal,
    f28dbk_f28_drilling_backlog_backg_378d_base_dmc_base_v111_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_base_dmc_base_v112_signal,
    f28dbk_f28_drilling_backlog_backg_504d_base_dmc_base_v113_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_base_dmc_base_v114_signal,
    f28dbk_f28_drilling_backlog_btr_base_dmc_base_v115_signal,
    f28dbk_f28_drilling_backlog_backg_5d_m21_xc_base_v116_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_m21_xc_base_v117_signal,
    f28dbk_f28_drilling_backlog_backg_10d_m21_xc_base_v118_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_m21_xc_base_v119_signal,
    f28dbk_f28_drilling_backlog_backg_21d_m21_xc_base_v120_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_m21_xc_base_v121_signal,
    f28dbk_f28_drilling_backlog_backg_42d_m21_xc_base_v122_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_m21_xc_base_v123_signal,
    f28dbk_f28_drilling_backlog_backg_63d_m21_xc_base_v124_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_m21_xc_base_v125_signal,
    f28dbk_f28_drilling_backlog_backg_84d_m21_xc_base_v126_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_m21_xc_base_v127_signal,
    f28dbk_f28_drilling_backlog_backg_126d_m21_xc_base_v128_signal,
    f28dbk_f28_drilling_backlog_backscore_126d_m21_xc_base_v129_signal,
    f28dbk_f28_drilling_backlog_backg_189d_m21_xc_base_v130_signal,
    f28dbk_f28_drilling_backlog_backscore_189d_m21_xc_base_v131_signal,
    f28dbk_f28_drilling_backlog_backg_252d_m21_xc_base_v132_signal,
    f28dbk_f28_drilling_backlog_backscore_252d_m21_xc_base_v133_signal,
    f28dbk_f28_drilling_backlog_backg_378d_m21_xc_base_v134_signal,
    f28dbk_f28_drilling_backlog_backscore_378d_m21_xc_base_v135_signal,
    f28dbk_f28_drilling_backlog_backg_504d_m21_xc_base_v136_signal,
    f28dbk_f28_drilling_backlog_backscore_504d_m21_xc_base_v137_signal,
    f28dbk_f28_drilling_backlog_btr_m21_xc_base_v138_signal,
    f28dbk_f28_drilling_backlog_backg_5d_m21_xc2_base_v139_signal,
    f28dbk_f28_drilling_backlog_backscore_5d_m21_xc2_base_v140_signal,
    f28dbk_f28_drilling_backlog_backg_10d_m21_xc2_base_v141_signal,
    f28dbk_f28_drilling_backlog_backscore_10d_m21_xc2_base_v142_signal,
    f28dbk_f28_drilling_backlog_backg_21d_m21_xc2_base_v143_signal,
    f28dbk_f28_drilling_backlog_backscore_21d_m21_xc2_base_v144_signal,
    f28dbk_f28_drilling_backlog_backg_42d_m21_xc2_base_v145_signal,
    f28dbk_f28_drilling_backlog_backscore_42d_m21_xc2_base_v146_signal,
    f28dbk_f28_drilling_backlog_backg_63d_m21_xc2_base_v147_signal,
    f28dbk_f28_drilling_backlog_backscore_63d_m21_xc2_base_v148_signal,
    f28dbk_f28_drilling_backlog_backg_84d_m21_xc2_base_v149_signal,
    f28dbk_f28_drilling_backlog_backscore_84d_m21_xc2_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_DRILLING_BACKLOG_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f28_backlog_growth', '_f28_backlog_to_revenue', '_f28_drilling_backlog_score',)
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
    print(f"OK f28_drilling_backlog_base_076_150_claude: {n_features} features pass")
