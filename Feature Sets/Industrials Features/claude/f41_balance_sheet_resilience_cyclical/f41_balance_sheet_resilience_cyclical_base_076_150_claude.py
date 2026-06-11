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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f41_net_debt_to_ebitda(debt, cashneq, ebitda):
    nd = debt - cashneq
    return nd / ebitda.replace(0, np.nan)


def _f41_leverage_position(debt, equity, w):
    lev = debt / equity.replace(0, np.nan).abs()
    return lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_debt_capacity(debt, cashneq, fcf, w):
    nd = debt - cashneq
    cap = fcf.rolling(w, min_periods=max(1, w // 2)).sum() / nd.replace(0, np.nan).abs()
    return cap

# feature 76: debt_cap_21d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xclog_base_v076_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 77: debt_cap_21d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xcm21_base_v077_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 78: debt_cap_42d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xc_base_v078_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 79: debt_cap_42d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xclog_base_v079_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 80: debt_cap_42d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xcm21_base_v080_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 81: debt_cap_63d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xc_base_v081_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 82: debt_cap_63d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xclog_base_v082_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 83: debt_cap_63d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xcm21_base_v083_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 84: debt_cap_126d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xc_base_v084_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 85: debt_cap_126d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xclog_base_v085_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 86: debt_cap_126d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xcm21_base_v086_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 87: debt_cap_189d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xc_base_v087_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 189)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 88: debt_cap_189d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xclog_base_v088_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 189)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 89: debt_cap_189d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xcm21_base_v089_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 189)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 90: debt_cap_252d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xc_base_v090_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 91: debt_cap_252d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xclog_base_v091_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 92: debt_cap_252d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xcm21_base_v092_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 93: debt_cap_378d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xc_base_v093_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 378)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 94: debt_cap_378d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xclog_base_v094_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 378)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 95: debt_cap_378d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xcm21_base_v095_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 378)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 96: debt_cap_504d_xc
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xc_base_v096_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 97: debt_cap_504d_xclog
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xclog_base_v097_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 98: debt_cap_504d_xcm21
def f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xcm21_base_v098_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 99: levxcap_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_21d_base_v099_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 21)
    b = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = a / b.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 100: ndebtxlev_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_21d_base_v100_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 101: ndebt_ema_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_21d_base_v101_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 102: lev_ema_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_21d_base_v102_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 103: cap_ema_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_21d_base_v103_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 104: levxcap_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_63d_base_v104_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 63)
    b = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = a / b.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 105: ndebtxlev_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_63d_base_v105_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 106: ndebt_ema_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_63d_base_v106_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 107: lev_ema_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_63d_base_v107_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 108: cap_ema_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_63d_base_v108_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 109: levxcap_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_126d_base_v109_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 126)
    b = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = a / b.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 110: ndebtxlev_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_126d_base_v110_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 111: ndebt_ema_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_126d_base_v111_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 112: lev_ema_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_126d_base_v112_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 113: cap_ema_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_126d_base_v113_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 114: levxcap_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_252d_base_v114_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 252)
    b = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = a / b.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 115: ndebtxlev_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_252d_base_v115_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 116: ndebt_ema_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_252d_base_v116_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 117: lev_ema_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_252d_base_v117_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 118: cap_ema_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_252d_base_v118_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 119: levxcap_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_504d_base_v119_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_leverage_position(debt, equity, 504)
    b = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = a / b.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 120: ndebtxlev_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_504d_base_v120_signal(debt, cashneq, ebitda, equity, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_leverage_position(debt, equity, 504)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 121: ndebt_ema_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_504d_base_v121_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 122: lev_ema_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_504d_base_v122_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 123: cap_ema_504d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_504d_base_v123_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 504)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 124: ndebt_sq_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_21d_base_v124_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 21)
    result = sm * sm.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 125: lev_z_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_21d_base_v125_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 126: cap_z_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_21d_base_v126_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 127: ndebt_sq_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_42d_base_v127_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 42)
    result = sm * sm.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 128: lev_z_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_42d_base_v128_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 129: cap_z_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_42d_base_v129_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 130: ndebt_sq_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_63d_base_v130_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 63)
    result = sm * sm.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 131: lev_z_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_63d_base_v131_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 132: cap_z_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_63d_base_v132_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 133: ndebt_sq_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_126d_base_v133_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 126)
    result = sm * sm.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 134: lev_z_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_126d_base_v134_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 135: cap_z_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_126d_base_v135_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 136: ndebt_sq_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_252d_base_v136_signal(debt, cashneq, ebitda, closeadj):
    base = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    sm = _mean(base, 252)
    result = sm * sm.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 137: lev_z_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_252d_base_v137_signal(debt, equity, closeadj):
    base = _f41_leverage_position(debt, equity, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 138: cap_z_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_252d_base_v138_signal(debt, cashneq, fcf, closeadj):
    base = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 139: capxlev_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_21d_base_v139_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 21)
    b = _f41_leverage_position(debt, equity, 21)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 140: ndebtxcap_21d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_21d_base_v140_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 141: capxlev_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_42d_base_v141_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 42)
    b = _f41_leverage_position(debt, equity, 42)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 142: ndebtxcap_42d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_42d_base_v142_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 42)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 143: capxlev_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_63d_base_v143_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 63)
    b = _f41_leverage_position(debt, equity, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 144: ndebtxcap_63d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_63d_base_v144_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 145: capxlev_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_126d_base_v145_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 126)
    b = _f41_leverage_position(debt, equity, 126)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 146: ndebtxcap_126d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_126d_base_v146_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 126)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 147: capxlev_189d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_189d_base_v147_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 189)
    b = _f41_leverage_position(debt, equity, 189)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 148: ndebtxcap_189d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_189d_base_v148_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 189)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 149: capxlev_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_252d_base_v149_signal(debt, cashneq, fcf, equity, closeadj):
    a = _f41_debt_capacity(debt, cashneq, fcf, 252)
    b = _f41_leverage_position(debt, equity, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# feature 150: ndebtxcap_252d
def f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_252d_base_v150_signal(debt, cashneq, ebitda, fcf, closeadj):
    a = _f41_net_debt_to_ebitda(debt, cashneq, ebitda)
    b = _f41_debt_capacity(debt, cashneq, fcf, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xclog_base_v076_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_21d_xcm21_base_v077_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xc_base_v078_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xclog_base_v079_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_42d_xcm21_base_v080_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xc_base_v081_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xclog_base_v082_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_63d_xcm21_base_v083_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xc_base_v084_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xclog_base_v085_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_126d_xcm21_base_v086_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xc_base_v087_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xclog_base_v088_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_189d_xcm21_base_v089_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xc_base_v090_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xclog_base_v091_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_252d_xcm21_base_v092_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xc_base_v093_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xclog_base_v094_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_378d_xcm21_base_v095_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xc_base_v096_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xclog_base_v097_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_debt_cap_504d_xcm21_base_v098_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_21d_base_v099_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_21d_base_v100_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_21d_base_v101_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_21d_base_v102_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_21d_base_v103_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_63d_base_v104_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_63d_base_v105_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_63d_base_v106_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_63d_base_v107_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_63d_base_v108_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_126d_base_v109_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_126d_base_v110_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_126d_base_v111_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_126d_base_v112_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_126d_base_v113_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_252d_base_v114_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_252d_base_v115_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_252d_base_v116_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_252d_base_v117_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_252d_base_v118_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_levxcap_504d_base_v119_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxlev_504d_base_v120_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_ema_504d_base_v121_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_ema_504d_base_v122_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_ema_504d_base_v123_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_21d_base_v124_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_21d_base_v125_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_21d_base_v126_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_42d_base_v127_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_42d_base_v128_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_42d_base_v129_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_63d_base_v130_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_63d_base_v131_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_63d_base_v132_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_126d_base_v133_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_126d_base_v134_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_126d_base_v135_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebt_sq_252d_base_v136_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_lev_z_252d_base_v137_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_cap_z_252d_base_v138_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_21d_base_v139_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_21d_base_v140_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_42d_base_v141_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_42d_base_v142_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_63d_base_v143_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_63d_base_v144_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_126d_base_v145_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_126d_base_v146_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_189d_base_v147_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_189d_base_v148_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_capxlev_252d_base_v149_signal,
    f41bsr_f41_balance_sheet_resilience_cyclical_ndebtxcap_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_BALANCE_SHEET_RESILIENCE_CYCLICAL_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f41_net_debt_to_ebitda', '_f41_leverage_position', '_f41_debt_capacity')
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
    print(f"OK f41_balance_sheet_resilience_cyclical_base_076_150_claude: {n_features} features pass")
