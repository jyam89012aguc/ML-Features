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
def _f07_net_debt_ebitda(debt, cashneq, ebitda):
    nd = debt - cashneq
    return nd / ebitda.replace(0, np.nan)


def _f07_leverage_dynamics(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f07_resilience_score(debt, fcf, ebitda, w):
    cover = fcf / debt.replace(0, np.nan)
    ebcov = ebitda / debt.replace(0, np.nan)
    s = (cover + ebcov) / 2.0
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====

# ld sqxcl w=5
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_5d_base_v076_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 5) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=5
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_5d_base_v077_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=5
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_5d_base_v078_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 5)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_10d_base_v079_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_10d_base_v080_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 10), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_10d_base_v081_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_10d_base_v082_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_10d_base_v083_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 10).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_10d_base_v084_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 10) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_10d_base_v085_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 10).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=10
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_10d_base_v086_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 10)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_21d_base_v087_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_21d_base_v088_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_21d_base_v089_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_21d_base_v090_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_21d_base_v091_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_21d_base_v092_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 21) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_21d_base_v093_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 21).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=21
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_21d_base_v094_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 21)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_42d_base_v095_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_42d_base_v096_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_42d_base_v097_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_42d_base_v098_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_42d_base_v099_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 42).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_42d_base_v100_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 42) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_42d_base_v101_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 42).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=42
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_42d_base_v102_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 42)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_63d_base_v103_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_63d_base_v104_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_63d_base_v105_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_63d_base_v106_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_63d_base_v107_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_63d_base_v108_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 63) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_63d_base_v109_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=63
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_63d_base_v110_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 63)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_126d_base_v111_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_126d_base_v112_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_126d_base_v113_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_126d_base_v114_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_126d_base_v115_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 126).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_126d_base_v116_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 126) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_126d_base_v117_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 126).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=126
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_126d_base_v118_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 126)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_189d_base_v119_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_189d_base_v120_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 189), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_189d_base_v121_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 189), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_189d_base_v122_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 189), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_189d_base_v123_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 189).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_189d_base_v124_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 189) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_189d_base_v125_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 189).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=189
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_189d_base_v126_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 189)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_252d_base_v127_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_252d_base_v128_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_252d_base_v129_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_252d_base_v130_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_252d_base_v131_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_252d_base_v132_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 252) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_252d_base_v133_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=252
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_252d_base_v134_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 252)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_378d_base_v135_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_378d_base_v136_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 378), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_378d_base_v137_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 378), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_378d_base_v138_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 378), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_378d_base_v139_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 378).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_378d_base_v140_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 378) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_378d_base_v141_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 378).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=378
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_378d_base_v142_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 378)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld idxcl w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_504d_base_v143_signal(debt, equity, closeadj):
    result = _f07_leverage_dynamics(debt, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld z252xcl w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_504d_base_v144_signal(debt, equity, closeadj):
    result = _z(_f07_leverage_dynamics(debt, equity, 504), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld std63xcl w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_504d_base_v145_signal(debt, equity, closeadj):
    result = _std(_f07_leverage_dynamics(debt, equity, 504), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld mean21xcl w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_504d_base_v146_signal(debt, equity, closeadj):
    result = _mean(_f07_leverage_dynamics(debt, equity, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld logxcl w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_504d_base_v147_signal(debt, equity, closeadj):
    result = np.log1p(_f07_leverage_dynamics(debt, equity, 504).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld sqxcl w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_504d_base_v148_signal(debt, equity, closeadj):
    result = (_f07_leverage_dynamics(debt, equity, 504) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld invxcl w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_504d_base_v149_signal(debt, equity, closeadj):
    result = (1.0 / _f07_leverage_dynamics(debt, equity, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ld ratiomean w=504
def f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_504d_base_v150_signal(debt, equity, closeadj):
    base = _f07_leverage_dynamics(debt, equity, 504)
    result = (base / _mean(base, 63).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_5d_base_v076_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_5d_base_v077_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_5d_base_v078_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_10d_base_v079_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_10d_base_v080_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_10d_base_v081_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_10d_base_v082_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_10d_base_v083_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_10d_base_v084_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_10d_base_v085_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_10d_base_v086_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_21d_base_v087_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_21d_base_v088_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_21d_base_v089_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_21d_base_v090_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_21d_base_v091_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_21d_base_v092_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_21d_base_v093_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_21d_base_v094_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_42d_base_v095_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_42d_base_v096_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_42d_base_v097_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_42d_base_v098_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_42d_base_v099_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_42d_base_v100_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_42d_base_v101_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_42d_base_v102_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_63d_base_v103_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_63d_base_v104_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_63d_base_v105_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_63d_base_v106_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_63d_base_v107_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_63d_base_v108_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_63d_base_v109_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_63d_base_v110_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_126d_base_v111_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_126d_base_v112_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_126d_base_v113_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_126d_base_v114_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_126d_base_v115_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_126d_base_v116_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_126d_base_v117_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_126d_base_v118_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_189d_base_v119_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_189d_base_v120_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_189d_base_v121_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_189d_base_v122_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_189d_base_v123_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_189d_base_v124_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_189d_base_v125_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_189d_base_v126_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_252d_base_v127_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_252d_base_v128_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_252d_base_v129_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_252d_base_v130_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_252d_base_v131_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_252d_base_v132_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_252d_base_v133_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_252d_base_v134_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_378d_base_v135_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_378d_base_v136_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_378d_base_v137_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_378d_base_v138_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_378d_base_v139_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_378d_base_v140_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_378d_base_v141_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_378d_base_v142_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldidxcl_504d_base_v143_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldz252xcl_504d_base_v144_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldstd63xcl_504d_base_v145_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldmean21xcl_504d_base_v146_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldlogxcl_504d_base_v147_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldsqxcl_504d_base_v148_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldinvxcl_504d_base_v149_signal,
    f07ebr_f07_ep_balance_sheet_resilience_ldratiomean_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_EP_BALANCE_SHEET_RESILIENCE_REGISTRY_076_150 = REGISTRY


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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f07_net_debt_ebitda", "_f07_leverage_dynamics", "_f07_resilience_score")
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
    print(f"OK f07_ep_balance_sheet_resilience_base_076_150_claude: {n_features} features pass")
