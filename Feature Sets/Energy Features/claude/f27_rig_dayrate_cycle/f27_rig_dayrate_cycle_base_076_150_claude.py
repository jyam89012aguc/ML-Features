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
def _f27_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f27_dayrate_pulse(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan)
    g = rpa.pct_change(periods=w)
    sd = rpa.rolling(w, min_periods=max(1, w // 2)).std()
    return g * sd


def _f27_dayrate_cycle_position(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return (revenue - m) / sd.replace(0, np.nan)


# ===== features =====

def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xmc_base_v076_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xmc_base_v077_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xmc_base_v078_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xmc_base_v079_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xmc_base_v080_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xmc_base_v081_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xmc_base_v082_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xmc_base_v083_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xmc_base_v084_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xmc_base_v085_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xmc_base_v086_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xmc_base_v087_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 126)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xmc_base_v088_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 189)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xmc_base_v089_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 189)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xmc_base_v090_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 189)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xmc_base_v091_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xmc_base_v092_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xmc_base_v093_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 252)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xmc_base_v094_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xmc_base_v095_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xmc_base_v096_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 378)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xmc_base_v097_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 504)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xmc_base_v098_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 504)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xmc_base_v099_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 504)
    result = (base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xzc_base_v100_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 5)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xzc_base_v101_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 5)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xzc_base_v102_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 5)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xzc_base_v103_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 10)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xzc_base_v104_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 10)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xzc_base_v105_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 10)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xzc_base_v106_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 21)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xzc_base_v107_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 21)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xzc_base_v108_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 21)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xzc_base_v109_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xzc_base_v110_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xzc_base_v111_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xzc_base_v112_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xzc_base_v113_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xzc_base_v114_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xzc_base_v115_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xzc_base_v116_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xzc_base_v117_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xzc_base_v118_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xzc_base_v119_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xzc_base_v120_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xzc_base_v121_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xzc_base_v122_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xzc_base_v123_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xzc_base_v124_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xzc_base_v125_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xzc_base_v126_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xzc_base_v127_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xzc_base_v128_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xzc_base_v129_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xzc_base_v130_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xzc_base_v131_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xzc_base_v132_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_5d_base_dmc_base_v133_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_dmc_base_v134_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_dmc_base_v135_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_10d_base_dmc_base_v136_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_dmc_base_v137_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_dmc_base_v138_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_21d_base_dmc_base_v139_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_dmc_base_v140_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_dmc_base_v141_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_dmc_base_v142_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_dmc_base_v143_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_dmc_base_v144_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_dmc_base_v145_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_dmc_base_v146_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_dmc_base_v147_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_dmc_base_v148_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_dmc_base_v149_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_dmc_base_v150_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xmc_base_v076_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xmc_base_v077_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xmc_base_v078_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xmc_base_v079_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xmc_base_v080_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xmc_base_v081_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xmc_base_v082_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xmc_base_v083_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xmc_base_v084_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xmc_base_v085_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xmc_base_v086_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xmc_base_v087_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xmc_base_v088_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xmc_base_v089_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xmc_base_v090_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xmc_base_v091_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xmc_base_v092_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xmc_base_v093_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xmc_base_v094_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xmc_base_v095_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xmc_base_v096_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xmc_base_v097_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xmc_base_v098_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xmc_base_v099_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xzc_base_v100_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xzc_base_v101_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xzc_base_v102_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xzc_base_v103_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xzc_base_v104_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xzc_base_v105_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xzc_base_v106_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xzc_base_v107_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xzc_base_v108_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xzc_base_v109_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xzc_base_v110_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xzc_base_v111_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xzc_base_v112_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xzc_base_v113_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xzc_base_v114_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xzc_base_v115_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xzc_base_v116_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xzc_base_v117_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xzc_base_v118_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xzc_base_v119_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xzc_base_v120_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xzc_base_v121_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xzc_base_v122_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xzc_base_v123_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xzc_base_v124_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xzc_base_v125_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xzc_base_v126_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xzc_base_v127_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xzc_base_v128_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xzc_base_v129_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xzc_base_v130_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xzc_base_v131_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xzc_base_v132_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_5d_base_dmc_base_v133_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_dmc_base_v134_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_dmc_base_v135_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_10d_base_dmc_base_v136_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_dmc_base_v137_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_dmc_base_v138_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_21d_base_dmc_base_v139_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_dmc_base_v140_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_dmc_base_v141_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_dmc_base_v142_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_dmc_base_v143_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_dmc_base_v144_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_dmc_base_v145_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_dmc_base_v146_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_dmc_base_v147_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_dmc_base_v148_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_dmc_base_v149_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_dmc_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_RIG_DAYRATE_CYCLE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f27_revenue_growth', '_f27_dayrate_pulse', '_f27_dayrate_cycle_position',)
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
    print(f"OK f27_rig_dayrate_cycle_base_076_150_claude: {n_features} features pass")
