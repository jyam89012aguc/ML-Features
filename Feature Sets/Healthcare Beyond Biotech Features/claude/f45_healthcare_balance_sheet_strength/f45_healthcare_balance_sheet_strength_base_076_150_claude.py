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
def _f45_net_debt(debt, cashneq):
    return debt - cashneq


def _f45_bs_strength(equity, debt, w):
    return _mean(equity, w) / _mean(debt, w).replace(0, np.nan)


def _f45_solvency_proxy(equity, liabilities, w):
    return _mean(equity, w) / _mean(liabilities, w).replace(0, np.nan)

# v076: bsstrqr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrqr_21d_base_v076_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: bsstrqr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrqr_63d_base_v077_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: bsstrqr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrqr_252d_base_v078_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: solvqr_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvqr_21d_base_v079_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: solvqr_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvqr_63d_base_v080_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: solvqr_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvqr_252d_base_v081_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: composite_63d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_base_v082_signal(debt, cashneq, equity, liabilities, closeadj):
    result = (_z(_mean(_f45_net_debt(debt, cashneq), 63), 252) + _z(_f45_bs_strength(equity, debt, 63), 252) + _z(_f45_solvency_proxy(equity, liabilities, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: composite_252d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_base_v083_signal(debt, cashneq, equity, liabilities, closeadj):
    result = (_z(_mean(_f45_net_debt(debt, cashneq), 252), 504) + _z(_f45_bs_strength(equity, debt, 252), 504) + _z(_f45_solvency_proxy(equity, liabilities, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: composite_126d
def f45hbs_f45_healthcare_balance_sheet_strength_composite_126d_base_v084_signal(debt, cashneq, equity, liabilities, closeadj):
    result = (_z(_mean(_f45_net_debt(debt, cashneq), 126), 252) + _z(_f45_bs_strength(equity, debt, 126), 252) + _z(_f45_solvency_proxy(equity, liabilities, 126), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: bsstr_5d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_5d_alt_base_v085_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v086: bsstr_10d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_10d_alt_base_v086_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v087: bsstr_42d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_42d_alt_base_v087_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v088: bsstr_189d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_189d_alt_base_v088_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v089: bsstr_378d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_bsstr_378d_alt_base_v089_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 378) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v090: solv_5d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_solv_5d_alt_base_v090_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v091: solv_10d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_solv_10d_alt_base_v091_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v092: solv_42d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_solv_42d_alt_base_v092_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v093: solv_189d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_solv_189d_alt_base_v093_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v094: netdebtlog_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtlog_21d_base_v094_signal(debt, cashneq, closeadj):
    result = np.sign(_mean(_f45_net_debt(debt, cashneq), 21)) * np.log1p(_mean(_f45_net_debt(debt, cashneq), 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: netdebtlog_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtlog_63d_base_v095_signal(debt, cashneq, closeadj):
    result = np.sign(_mean(_f45_net_debt(debt, cashneq), 63)) * np.log1p(_mean(_f45_net_debt(debt, cashneq), 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: netdebtlog_252d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtlog_252d_base_v096_signal(debt, cashneq, closeadj):
    result = np.sign(_mean(_f45_net_debt(debt, cashneq), 252)) * np.log1p(_mean(_f45_net_debt(debt, cashneq), 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: bsstrlog_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrlog_21d_base_v097_signal(equity, debt, closeadj):
    result = np.log1p(_f45_bs_strength(equity, debt, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: bsstrlog_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrlog_63d_base_v098_signal(equity, debt, closeadj):
    result = np.log1p(_f45_bs_strength(equity, debt, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: bsstrlog_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrlog_252d_base_v099_signal(equity, debt, closeadj):
    result = np.log1p(_f45_bs_strength(equity, debt, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: solvlog_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvlog_21d_base_v100_signal(equity, liabilities, closeadj):
    result = np.log1p(_f45_solvency_proxy(equity, liabilities, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: solvlog_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvlog_63d_base_v101_signal(equity, liabilities, closeadj):
    result = np.log1p(_f45_solvency_proxy(equity, liabilities, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: solvlog_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvlog_252d_base_v102_signal(equity, liabilities, closeadj):
    result = np.log1p(_f45_solvency_proxy(equity, liabilities, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: bsstrx_21x63
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_21x63_base_v103_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 21) * _f45_bs_strength(equity, debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: bsstrx_21x252
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_21x252_base_v104_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 21) * _f45_bs_strength(equity, debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: bsstrx_63x252
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_63x252_base_v105_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 63) * _f45_bs_strength(equity, debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: bsstrx_63x504
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_63x504_base_v106_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 63) * _f45_bs_strength(equity, debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: bsstrx_126x504
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_126x504_base_v107_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 126) * _f45_bs_strength(equity, debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: solvx_21x63
def f45hbs_f45_healthcare_balance_sheet_strength_solvx_21x63_base_v108_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 21) * _f45_solvency_proxy(equity, liabilities, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: solvx_21x252
def f45hbs_f45_healthcare_balance_sheet_strength_solvx_21x252_base_v109_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 21) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: solvx_63x252
def f45hbs_f45_healthcare_balance_sheet_strength_solvx_63x252_base_v110_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 63) * _f45_solvency_proxy(equity, liabilities, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: solvx_63x504
def f45hbs_f45_healthcare_balance_sheet_strength_solvx_63x504_base_v111_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 63) * _f45_solvency_proxy(equity, liabilities, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: solvx_126x504
def f45hbs_f45_healthcare_balance_sheet_strength_solvx_126x504_base_v112_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 126) * _f45_solvency_proxy(equity, liabilities, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: netdebtx_21x63
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_21x63_base_v113_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 21) * _mean(_f45_net_debt(debt, cashneq), 63) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v114: netdebtx_21x252
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_21x252_base_v114_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 21) * _mean(_f45_net_debt(debt, cashneq), 252) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v115: netdebtx_63x252
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_63x252_base_v115_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 63) * _mean(_f45_net_debt(debt, cashneq), 252) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v116: netdebtx_63x504
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_63x504_base_v116_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 63) * _mean(_f45_net_debt(debt, cashneq), 504) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v117: netdebtx_126x504
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_126x504_base_v117_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 126) * _mean(_f45_net_debt(debt, cashneq), 504) * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v118: bsstrtri_2163252
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrtri_2163252_base_v118_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 21) + _f45_bs_strength(equity, debt, 63) + _f45_bs_strength(equity, debt, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v119: bsstrtri_63126252
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrtri_63126252_base_v119_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 63) + _f45_bs_strength(equity, debt, 126) + _f45_bs_strength(equity, debt, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v120: bsstrtri_126252504
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrtri_126252504_base_v120_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 126) + _f45_bs_strength(equity, debt, 252) + _f45_bs_strength(equity, debt, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v121: solvtri_2163252
def f45hbs_f45_healthcare_balance_sheet_strength_solvtri_2163252_base_v121_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 21) + _f45_solvency_proxy(equity, liabilities, 63) + _f45_solvency_proxy(equity, liabilities, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v122: solvtri_63126252
def f45hbs_f45_healthcare_balance_sheet_strength_solvtri_63126252_base_v122_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 63) + _f45_solvency_proxy(equity, liabilities, 126) + _f45_solvency_proxy(equity, liabilities, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v123: solvtri_126252504
def f45hbs_f45_healthcare_balance_sheet_strength_solvtri_126252504_base_v123_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 126) + _f45_solvency_proxy(equity, liabilities, 252) + _f45_solvency_proxy(equity, liabilities, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v124: netdebttri_2163252
def f45hbs_f45_healthcare_balance_sheet_strength_netdebttri_2163252_base_v124_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 21) + _mean(_f45_net_debt(debt, cashneq), 63) + _mean(_f45_net_debt(debt, cashneq), 252)) * closeadj / 3e9
    return result.replace([np.inf, -np.inf], np.nan)


# v125: netdebttri_63126252
def f45hbs_f45_healthcare_balance_sheet_strength_netdebttri_63126252_base_v125_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 63) + _mean(_f45_net_debt(debt, cashneq), 126) + _mean(_f45_net_debt(debt, cashneq), 252)) * closeadj / 3e9
    return result.replace([np.inf, -np.inf], np.nan)


# v126: netdebttri_126252504
def f45hbs_f45_healthcare_balance_sheet_strength_netdebttri_126252504_base_v126_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 126) + _mean(_f45_net_debt(debt, cashneq), 252) + _mean(_f45_net_debt(debt, cashneq), 504)) * closeadj / 3e9
    return result.replace([np.inf, -np.inf], np.nan)


# v127: bsstrdiff_21_21
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrdiff_21_21_base_v127_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 21) - _f45_bs_strength(equity, debt, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: bsstrdiff_63_63
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrdiff_63_63_base_v128_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 63) - _f45_bs_strength(equity, debt, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: bsstrdiff_252_63
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrdiff_252_63_base_v129_signal(equity, debt, closeadj):
    result = (_f45_bs_strength(equity, debt, 252) - _f45_bs_strength(equity, debt, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: solvdiff_21_21
def f45hbs_f45_healthcare_balance_sheet_strength_solvdiff_21_21_base_v130_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 21) - _f45_solvency_proxy(equity, liabilities, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: solvdiff_63_63
def f45hbs_f45_healthcare_balance_sheet_strength_solvdiff_63_63_base_v131_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 63) - _f45_solvency_proxy(equity, liabilities, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: solvdiff_252_63
def f45hbs_f45_healthcare_balance_sheet_strength_solvdiff_252_63_base_v132_signal(equity, liabilities, closeadj):
    result = (_f45_solvency_proxy(equity, liabilities, 252) - _f45_solvency_proxy(equity, liabilities, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: bsstrxprice2_42d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxprice2_42d_base_v133_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: bsstrxprice2_126d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxprice2_126d_base_v134_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: bsstrxprice2_378d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrxprice2_378d_base_v135_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 378) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: solvxprice2_42d
def f45hbs_f45_healthcare_balance_sheet_strength_solvxprice2_42d_base_v136_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: solvxprice2_126d
def f45hbs_f45_healthcare_balance_sheet_strength_solvxprice2_126d_base_v137_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: solvxprice2_378d
def f45hbs_f45_healthcare_balance_sheet_strength_solvxprice2_378d_base_v138_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 378) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: netdebtxprice_42d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxprice_42d_base_v139_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 42) * closeadj * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v140: netdebtxprice_126d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxprice_126d_base_v140_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 126) * closeadj * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v141: netdebtxprice_378d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtxprice_378d_base_v141_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 378) * closeadj * closeadj / 1e18
    return result.replace([np.inf, -np.inf], np.nan)


# v142: netdebt_378d_alt
def f45hbs_f45_healthcare_balance_sheet_strength_netdebt_378d_alt_base_v142_signal(debt, cashneq, closeadj):
    result = _mean(_f45_net_debt(debt, cashneq), 378) * closeadj * 1.0 / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v143: bsstrpos_21d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrpos_21d_base_v143_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 21).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: bsstrpos_63d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrpos_63d_base_v144_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 63).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: bsstrpos_252d
def f45hbs_f45_healthcare_balance_sheet_strength_bsstrpos_252d_base_v145_signal(equity, debt, closeadj):
    result = _f45_bs_strength(equity, debt, 252).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: solvpos_21d
def f45hbs_f45_healthcare_balance_sheet_strength_solvpos_21d_base_v146_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 21).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: solvpos_63d
def f45hbs_f45_healthcare_balance_sheet_strength_solvpos_63d_base_v147_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 63).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: solvpos_252d
def f45hbs_f45_healthcare_balance_sheet_strength_solvpos_252d_base_v148_signal(equity, liabilities, closeadj):
    result = _f45_solvency_proxy(equity, liabilities, 252).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: netdebtneg_21d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtneg_21d_base_v149_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 21) - _mean(_f45_net_debt(debt, cashneq), 84)) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# v150: netdebtneg_63d
def f45hbs_f45_healthcare_balance_sheet_strength_netdebtneg_63d_base_v150_signal(debt, cashneq, closeadj):
    result = (_mean(_f45_net_debt(debt, cashneq), 63) - _mean(_f45_net_debt(debt, cashneq), 252)) * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrqr_21d_base_v076_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrqr_63d_base_v077_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrqr_252d_base_v078_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvqr_21d_base_v079_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvqr_63d_base_v080_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvqr_252d_base_v081_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_63d_base_v082_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_252d_base_v083_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_composite_126d_base_v084_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_5d_alt_base_v085_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_10d_alt_base_v086_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_42d_alt_base_v087_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_189d_alt_base_v088_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstr_378d_alt_base_v089_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_5d_alt_base_v090_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_10d_alt_base_v091_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_42d_alt_base_v092_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solv_189d_alt_base_v093_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtlog_21d_base_v094_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtlog_63d_base_v095_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtlog_252d_base_v096_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrlog_21d_base_v097_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrlog_63d_base_v098_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrlog_252d_base_v099_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvlog_21d_base_v100_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvlog_63d_base_v101_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvlog_252d_base_v102_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_21x63_base_v103_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_21x252_base_v104_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_63x252_base_v105_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_63x504_base_v106_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrx_126x504_base_v107_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvx_21x63_base_v108_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvx_21x252_base_v109_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvx_63x252_base_v110_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvx_63x504_base_v111_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvx_126x504_base_v112_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_21x63_base_v113_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_21x252_base_v114_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_63x252_base_v115_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_63x504_base_v116_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtx_126x504_base_v117_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrtri_2163252_base_v118_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrtri_63126252_base_v119_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrtri_126252504_base_v120_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvtri_2163252_base_v121_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvtri_63126252_base_v122_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvtri_126252504_base_v123_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebttri_2163252_base_v124_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebttri_63126252_base_v125_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebttri_126252504_base_v126_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrdiff_21_21_base_v127_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrdiff_63_63_base_v128_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrdiff_252_63_base_v129_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvdiff_21_21_base_v130_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvdiff_63_63_base_v131_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvdiff_252_63_base_v132_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxprice2_42d_base_v133_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxprice2_126d_base_v134_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrxprice2_378d_base_v135_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvxprice2_42d_base_v136_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvxprice2_126d_base_v137_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvxprice2_378d_base_v138_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxprice_42d_base_v139_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxprice_126d_base_v140_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtxprice_378d_base_v141_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebt_378d_alt_base_v142_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrpos_21d_base_v143_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrpos_63d_base_v144_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_bsstrpos_252d_base_v145_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvpos_21d_base_v146_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvpos_63d_base_v147_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_solvpos_252d_base_v148_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtneg_21d_base_v149_signal,
    f45hbs_f45_healthcare_balance_sheet_strength_netdebtneg_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_HEALTHCARE_BALANCE_SHEET_STRENGTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    liabilities = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")

    cols = {
        "cashneq": cashneq,
        "closeadj": closeadj,
        "debt": debt,
        "equity": equity,
        "liabilities": liabilities,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f45_net_debt', '_f45_bs_strength', '_f45_solvency_proxy',)
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
    print(f"OK f45_healthcare_balance_sheet_strength_base_076_150_claude: {n_features} features pass")
