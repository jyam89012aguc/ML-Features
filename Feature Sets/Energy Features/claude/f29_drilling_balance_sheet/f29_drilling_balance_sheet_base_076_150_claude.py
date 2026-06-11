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
def _f29_net_debt(debt, cashneq):
    return debt - cashneq


def _f29_leverage_dynamics(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f29_balance_sheet_resilience(debt, ebitda, w):
    ratio = ebitda / debt.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====

def f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xzc_base_v076_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 21)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xzc_base_v077_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xzc_base_v078_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 42)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xzc_base_v079_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xzc_base_v080_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 63)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xzc_base_v081_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xzc_base_v082_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 84)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xzc_base_v083_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xzc_base_v084_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 126)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xzc_base_v085_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xzc_base_v086_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 189)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xzc_base_v087_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xzc_base_v088_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 252)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xzc_base_v089_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xzc_base_v090_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 378)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xzc_base_v091_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xzc_base_v092_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 504)
    result = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_netdebt_base_dmc_base_v093_signal(debt, cashneq, closeadj):
    base = _f29_net_debt(debt, cashneq)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_dmc_base_v094_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_5d_base_dmc_base_v095_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 5)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_dmc_base_v096_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_10d_base_dmc_base_v097_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 10)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_dmc_base_v098_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_21d_base_dmc_base_v099_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 21)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_dmc_base_v100_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_42d_base_dmc_base_v101_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 42)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_dmc_base_v102_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_63d_base_dmc_base_v103_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 63)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_dmc_base_v104_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_84d_base_dmc_base_v105_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 84)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_dmc_base_v106_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 126)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_126d_base_dmc_base_v107_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 126)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_dmc_base_v108_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 189)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_189d_base_dmc_base_v109_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 189)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_dmc_base_v110_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 252)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_252d_base_dmc_base_v111_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 252)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_dmc_base_v112_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 378)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_378d_base_dmc_base_v113_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 378)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_dmc_base_v114_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 504)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_504d_base_dmc_base_v115_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 504)
    result = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_netdebt_m21_xc_base_v116_signal(debt, cashneq, closeadj):
    base = _f29_net_debt(debt, cashneq)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_5d_m21_xc_base_v117_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 5)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_5d_m21_xc_base_v118_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 5)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_10d_m21_xc_base_v119_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 10)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_10d_m21_xc_base_v120_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 10)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_21d_m21_xc_base_v121_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 21)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_21d_m21_xc_base_v122_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 21)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_42d_m21_xc_base_v123_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 42)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_42d_m21_xc_base_v124_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 42)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_63d_m21_xc_base_v125_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_63d_m21_xc_base_v126_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 63)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_84d_m21_xc_base_v127_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 84)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_84d_m21_xc_base_v128_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 84)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_126d_m21_xc_base_v129_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_126d_m21_xc_base_v130_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 126)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_189d_m21_xc_base_v131_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 189)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_189d_m21_xc_base_v132_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 189)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_252d_m21_xc_base_v133_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 252)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_252d_m21_xc_base_v134_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 252)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_378d_m21_xc_base_v135_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 378)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_378d_m21_xc_base_v136_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 378)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_504d_m21_xc_base_v137_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 504)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_504d_m21_xc_base_v138_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 504)
    result = (_mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_netdebt_m21_xc2_base_v139_signal(debt, cashneq, closeadj):
    base = _f29_net_debt(debt, cashneq)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_5d_m21_xc2_base_v140_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 5)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_5d_m21_xc2_base_v141_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 5)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_10d_m21_xc2_base_v142_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 10)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_10d_m21_xc2_base_v143_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 10)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_21d_m21_xc2_base_v144_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 21)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_21d_m21_xc2_base_v145_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 21)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_42d_m21_xc2_base_v146_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_42d_m21_xc2_base_v147_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 42)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_63d_m21_xc2_base_v148_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 63)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_bsres_63d_m21_xc2_base_v149_signal(debt, ebitda, closeadj):
    base = _f29_balance_sheet_resilience(debt, ebitda, 63)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f29dbs_f29_drilling_balance_sheet_levdyn_84d_m21_xc2_base_v150_signal(debt, equity, closeadj):
    base = _f29_leverage_dynamics(debt, equity, 84)
    result = (_mean(base, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29dbs_f29_drilling_balance_sheet_bsres_21d_base_xzc_base_v076_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_xzc_base_v077_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_42d_base_xzc_base_v078_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_xzc_base_v079_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_63d_base_xzc_base_v080_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_xzc_base_v081_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_84d_base_xzc_base_v082_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_xzc_base_v083_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_126d_base_xzc_base_v084_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_xzc_base_v085_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_189d_base_xzc_base_v086_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_xzc_base_v087_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_252d_base_xzc_base_v088_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_xzc_base_v089_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_378d_base_xzc_base_v090_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_xzc_base_v091_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_504d_base_xzc_base_v092_signal,
    f29dbs_f29_drilling_balance_sheet_netdebt_base_dmc_base_v093_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_5d_base_dmc_base_v094_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_5d_base_dmc_base_v095_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_10d_base_dmc_base_v096_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_10d_base_dmc_base_v097_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_21d_base_dmc_base_v098_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_21d_base_dmc_base_v099_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_42d_base_dmc_base_v100_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_42d_base_dmc_base_v101_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_63d_base_dmc_base_v102_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_63d_base_dmc_base_v103_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_84d_base_dmc_base_v104_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_84d_base_dmc_base_v105_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_126d_base_dmc_base_v106_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_126d_base_dmc_base_v107_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_189d_base_dmc_base_v108_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_189d_base_dmc_base_v109_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_252d_base_dmc_base_v110_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_252d_base_dmc_base_v111_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_378d_base_dmc_base_v112_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_378d_base_dmc_base_v113_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_504d_base_dmc_base_v114_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_504d_base_dmc_base_v115_signal,
    f29dbs_f29_drilling_balance_sheet_netdebt_m21_xc_base_v116_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_5d_m21_xc_base_v117_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_5d_m21_xc_base_v118_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_10d_m21_xc_base_v119_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_10d_m21_xc_base_v120_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_21d_m21_xc_base_v121_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_21d_m21_xc_base_v122_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_42d_m21_xc_base_v123_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_42d_m21_xc_base_v124_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_63d_m21_xc_base_v125_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_63d_m21_xc_base_v126_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_84d_m21_xc_base_v127_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_84d_m21_xc_base_v128_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_126d_m21_xc_base_v129_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_126d_m21_xc_base_v130_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_189d_m21_xc_base_v131_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_189d_m21_xc_base_v132_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_252d_m21_xc_base_v133_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_252d_m21_xc_base_v134_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_378d_m21_xc_base_v135_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_378d_m21_xc_base_v136_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_504d_m21_xc_base_v137_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_504d_m21_xc_base_v138_signal,
    f29dbs_f29_drilling_balance_sheet_netdebt_m21_xc2_base_v139_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_5d_m21_xc2_base_v140_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_5d_m21_xc2_base_v141_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_10d_m21_xc2_base_v142_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_10d_m21_xc2_base_v143_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_21d_m21_xc2_base_v144_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_21d_m21_xc2_base_v145_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_42d_m21_xc2_base_v146_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_42d_m21_xc2_base_v147_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_63d_m21_xc2_base_v148_signal,
    f29dbs_f29_drilling_balance_sheet_bsres_63d_m21_xc2_base_v149_signal,
    f29dbs_f29_drilling_balance_sheet_levdyn_84d_m21_xc2_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_DRILLING_BALANCE_SHEET_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f29_net_debt', '_f29_leverage_dynamics', '_f29_balance_sheet_resilience',)
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
    print(f"OK f29_drilling_balance_sheet_base_076_150_claude: {n_features} features pass")
