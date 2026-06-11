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
def _f06_debt_ebitda(debt, ebitda):
    return debt / ebitda.replace(0, np.nan)


def _f06_credit_quality(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return -lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_solvency_score(debt, ebitda, fcf, w):
    de_ratio = debt / ebitda.replace(0, np.nan)
    fcf_cov = fcf / debt.replace(0, np.nan)
    de_smooth = de_ratio.rolling(w, min_periods=max(1, w // 2)).mean()
    fcf_smooth = fcf_cov.rolling(w, min_periods=max(1, w // 2)).mean()
    return fcf_smooth - de_smooth


# v076: 21d debt/ebitda × closeadj^2 normalized
def f06ucq_f06_utility_credit_quality_debtebitda_21d_csq_base_v076_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 21) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v077: 63d debt/ebitda × closeadj^2 normalized
def f06ucq_f06_utility_credit_quality_debtebitda_63d_csq_base_v077_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 63) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v078: 252d debt/ebitda × closeadj^2 normalized
def f06ucq_f06_utility_credit_quality_debtebitda_252d_csq_base_v078_signal(debt, ebitda, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 252) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v079: 21d debt/ebitda + 21d closeadj momentum
def f06ucq_f06_utility_credit_quality_debtebitda_21d_mom_base_v079_signal(debt, ebitda, closeadj):
    mom = closeadj / closeadj.shift(21) - 1.0
    result = _mean(_f06_debt_ebitda(debt, ebitda), 21) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: 63d debt/ebitda + 63d closeadj momentum
def f06ucq_f06_utility_credit_quality_debtebitda_63d_mom_base_v080_signal(debt, ebitda, closeadj):
    mom = closeadj / closeadj.shift(63) - 1.0
    result = _mean(_f06_debt_ebitda(debt, ebitda), 63) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: 252d debt/ebitda + 252d closeadj momentum
def f06ucq_f06_utility_credit_quality_debtebitda_252d_mom_base_v081_signal(debt, ebitda, closeadj):
    mom = closeadj / closeadj.shift(252) - 1.0
    result = _mean(_f06_debt_ebitda(debt, ebitda), 252) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: 21d cred-q × closeadj^2
def f06ucq_f06_utility_credit_quality_creditq_21d_csq_base_v082_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 21) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v083: 63d cred-q × closeadj^2
def f06ucq_f06_utility_credit_quality_creditq_63d_csq_base_v083_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 63) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v084: 252d cred-q × closeadj^2
def f06ucq_f06_utility_credit_quality_creditq_252d_csq_base_v084_signal(debt, equity, closeadj):
    result = _f06_credit_quality(debt, equity, 252) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v085: 21d solvency × closeadj^2
def f06ucq_f06_utility_credit_quality_solv_21d_csq_base_v085_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 21) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v086: 63d solvency × closeadj^2
def f06ucq_f06_utility_credit_quality_solv_63d_csq_base_v086_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 63) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v087: 252d solvency × closeadj^2
def f06ucq_f06_utility_credit_quality_solv_252d_csq_base_v087_signal(debt, ebitda, fcf, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 252) * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v088: change-over-window debt/ebitda 21d × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_dchg_base_v088_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = (de_r - de_r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: change-over-window debt/ebitda 63d × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_dchg_base_v089_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = (de_r - de_r.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: change-over-window debt/ebitda 252d × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_dchg_base_v090_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = (de_r - de_r.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: change-over-window cred-q 21d × closeadj
def f06ucq_f06_utility_credit_quality_creditq_21d_dchg_base_v091_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 21)
    result = (cq - cq.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: change-over-window cred-q 63d × closeadj
def f06ucq_f06_utility_credit_quality_creditq_63d_dchg_base_v092_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 63)
    result = (cq - cq.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: change-over-window cred-q 252d × closeadj
def f06ucq_f06_utility_credit_quality_creditq_252d_dchg_base_v093_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 252)
    result = (cq - cq.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: solvency 21d delta × closeadj
def f06ucq_f06_utility_credit_quality_solv_21d_dchg_base_v094_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = (sv - sv.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: solvency 63d delta × closeadj
def f06ucq_f06_utility_credit_quality_solv_63d_dchg_base_v095_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 63)
    result = (sv - sv.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: solvency 252d delta × closeadj
def f06ucq_f06_utility_credit_quality_solv_252d_dchg_base_v096_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 252)
    result = (sv - sv.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: 21d debt/ebitda × sign(de) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_signde_base_v097_signal(debt, ebitda, de, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 21) * np.sign(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: 63d debt/ebitda × tanh(de) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_tanhde_base_v098_signal(debt, ebitda, de, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 63) * np.tanh(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: 252d debt/ebitda × tanh(de) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_tanhde_base_v099_signal(debt, ebitda, de, closeadj):
    result = _mean(_f06_debt_ebitda(debt, ebitda), 252) * np.tanh(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: 21d cred-q × tanh(de)
def f06ucq_f06_utility_credit_quality_creditq_21d_tanhde_base_v100_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 21) * np.tanh(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: 63d cred-q × tanh(de)
def f06ucq_f06_utility_credit_quality_creditq_63d_tanhde_base_v101_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 63) * np.tanh(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: 252d cred-q × tanh(de)
def f06ucq_f06_utility_credit_quality_creditq_252d_tanhde_base_v102_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 252) * np.tanh(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: 63d solv × tanh(de) × closeadj
def f06ucq_f06_utility_credit_quality_solv_63d_tanhde_base_v103_signal(debt, ebitda, fcf, de, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 63) * np.tanh(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: 252d solv × tanh(de) × closeadj
def f06ucq_f06_utility_credit_quality_solv_252d_tanhde_base_v104_signal(debt, ebitda, fcf, de, closeadj):
    result = _f06_solvency_score(debt, ebitda, fcf, 252) * np.tanh(de) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: 21d debt/ebitda ratio of fcf cover × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_fcfdiv_base_v105_signal(debt, ebitda, fcf, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    cov = fcf.rolling(21, min_periods=11).mean() / ebitda.replace(0, np.nan)
    result = de_r / (1.0 + cov.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: 63d debt/ebitda ratio of fcf cover × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_fcfdiv_base_v106_signal(debt, ebitda, fcf, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    cov = fcf.rolling(63, min_periods=32).mean() / ebitda.replace(0, np.nan)
    result = de_r / (1.0 + cov.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: 252d debt/ebitda ratio of fcf cover × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_fcfdiv_base_v107_signal(debt, ebitda, fcf, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    cov = fcf.rolling(252, min_periods=126).mean() / ebitda.replace(0, np.nan)
    result = de_r / (1.0 + cov.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: 21d log(debt/ebitda) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_log_base_v108_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda).abs()
    result = _mean(np.log(de_r.replace(0, np.nan)), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: 63d log(debt/ebitda) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_log_base_v109_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda).abs()
    result = _mean(np.log(de_r.replace(0, np.nan)), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: 252d log(debt/ebitda) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_log_base_v110_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda).abs()
    result = _mean(np.log(de_r.replace(0, np.nan)), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: 21d sqrt(debt/ebitda) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_sqrt_base_v111_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda).abs()
    result = _mean(np.sqrt(de_r), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: 63d sqrt(debt/ebitda) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_sqrt_base_v112_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda).abs()
    result = _mean(np.sqrt(de_r), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: 252d sqrt(debt/ebitda) × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_sqrt_base_v113_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda).abs()
    result = _mean(np.sqrt(de_r), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: 21d cred-q max
def f06ucq_f06_utility_credit_quality_creditq_21d_max_base_v114_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 21)
    result = cq.rolling(21, min_periods=11).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: 63d cred-q max
def f06ucq_f06_utility_credit_quality_creditq_63d_max_base_v115_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 63)
    result = cq.rolling(63, min_periods=32).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: 252d cred-q max
def f06ucq_f06_utility_credit_quality_creditq_252d_max_base_v116_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 252)
    result = cq.rolling(252, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: 21d cred-q min
def f06ucq_f06_utility_credit_quality_creditq_21d_min_base_v117_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 21)
    result = cq.rolling(21, min_periods=11).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: 63d cred-q min
def f06ucq_f06_utility_credit_quality_creditq_63d_min_base_v118_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 63)
    result = cq.rolling(63, min_periods=32).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: 252d cred-q min
def f06ucq_f06_utility_credit_quality_creditq_252d_min_base_v119_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 252)
    result = cq.rolling(252, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: 21d solvency max × closeadj
def f06ucq_f06_utility_credit_quality_solv_21d_max_base_v120_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = sv.rolling(21, min_periods=11).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: 63d solvency max × closeadj
def f06ucq_f06_utility_credit_quality_solv_63d_max_base_v121_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 63)
    result = sv.rolling(63, min_periods=32).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: 252d solvency max × closeadj
def f06ucq_f06_utility_credit_quality_solv_252d_max_base_v122_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 252)
    result = sv.rolling(252, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: 21d solvency min × closeadj
def f06ucq_f06_utility_credit_quality_solv_21d_min_base_v123_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 21)
    result = sv.rolling(21, min_periods=11).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: 63d solvency min × closeadj
def f06ucq_f06_utility_credit_quality_solv_63d_min_base_v124_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 63)
    result = sv.rolling(63, min_periods=32).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: 252d solvency min × closeadj
def f06ucq_f06_utility_credit_quality_solv_252d_min_base_v125_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 252)
    result = sv.rolling(252, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: 21d debt/ebitda max range × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_rng_base_v126_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = (de_r.rolling(21, min_periods=11).max() - de_r.rolling(21, min_periods=11).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: 63d debt/ebitda max range × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_rng_base_v127_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = (de_r.rolling(63, min_periods=32).max() - de_r.rolling(63, min_periods=32).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: 252d debt/ebitda max range × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_rng_base_v128_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = (de_r.rolling(252, min_periods=126).max() - de_r.rolling(252, min_periods=126).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: 21d debt/ebitda median × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_21d_med_base_v129_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = de_r.rolling(21, min_periods=11).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: 63d debt/ebitda median × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_med_base_v130_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = de_r.rolling(63, min_periods=32).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: 252d debt/ebitda median × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_med_base_v131_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = de_r.rolling(252, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: cred-q vs its 252d rank × closeadj
def f06ucq_f06_utility_credit_quality_creditq_252d_rank_base_v132_signal(debt, equity, closeadj):
    cq = _f06_credit_quality(debt, equity, 63)
    result = cq.rolling(252, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: debt/ebitda vs its 252d rank × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_rank_base_v133_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    result = de_r.rolling(252, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: solv vs its 252d rank × closeadj
def f06ucq_f06_utility_credit_quality_solv_252d_rank_base_v134_signal(debt, ebitda, fcf, closeadj):
    sv = _f06_solvency_score(debt, ebitda, fcf, 63)
    result = sv.rolling(252, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: 21d ratio cred-q / |de| × closeadj
def f06ucq_f06_utility_credit_quality_creditq_21d_div_de_base_v135_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 21) / (1.0 + de.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: 63d ratio cred-q / |de| × closeadj
def f06ucq_f06_utility_credit_quality_creditq_63d_div_de_base_v136_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 63) / (1.0 + de.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: 252d ratio cred-q / |de| × closeadj
def f06ucq_f06_utility_credit_quality_creditq_252d_div_de_base_v137_signal(debt, equity, de, closeadj):
    result = _f06_credit_quality(debt, equity, 252) / (1.0 + de.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: 63d solv × debt growth × closeadj
def f06ucq_f06_utility_credit_quality_solv_debtgr_63d_base_v138_signal(debt, ebitda, fcf, closeadj):
    gr = debt.pct_change(63)
    result = _f06_solvency_score(debt, ebitda, fcf, 63) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: 252d solv × debt growth × closeadj
def f06ucq_f06_utility_credit_quality_solv_debtgr_252d_base_v139_signal(debt, ebitda, fcf, closeadj):
    gr = debt.pct_change(252)
    result = _f06_solvency_score(debt, ebitda, fcf, 252) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140: 21d debt/ebitda × equity growth × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_eqgr_21d_base_v140_signal(debt, ebitda, equity, closeadj):
    gr = equity.pct_change(21)
    result = _f06_debt_ebitda(debt, ebitda) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: 63d debt/ebitda × equity growth × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_eqgr_63d_base_v141_signal(debt, ebitda, equity, closeadj):
    gr = equity.pct_change(63)
    result = _f06_debt_ebitda(debt, ebitda) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142: 252d debt/ebitda × equity growth × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_eqgr_252d_base_v142_signal(debt, ebitda, equity, closeadj):
    gr = equity.pct_change(252)
    result = _f06_debt_ebitda(debt, ebitda) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: 21d cred-q × equity growth × closeadj
def f06ucq_f06_utility_credit_quality_creditq_eqgr_21d_base_v143_signal(debt, equity, closeadj):
    gr = equity.pct_change(21)
    result = _f06_credit_quality(debt, equity, 21) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: 63d cred-q × equity growth × closeadj
def f06ucq_f06_utility_credit_quality_creditq_eqgr_63d_base_v144_signal(debt, equity, closeadj):
    gr = equity.pct_change(63)
    result = _f06_credit_quality(debt, equity, 63) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: 252d cred-q × equity growth × closeadj
def f06ucq_f06_utility_credit_quality_creditq_eqgr_252d_base_v145_signal(debt, equity, closeadj):
    gr = equity.pct_change(252)
    result = _f06_credit_quality(debt, equity, 252) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: 21d solvency × fcf growth × closeadj
def f06ucq_f06_utility_credit_quality_solv_fcfgr_21d_base_v146_signal(debt, ebitda, fcf, closeadj):
    gr = fcf.pct_change(21)
    result = _f06_solvency_score(debt, ebitda, fcf, 21) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: 63d solvency × fcf growth × closeadj
def f06ucq_f06_utility_credit_quality_solv_fcfgr_63d_base_v147_signal(debt, ebitda, fcf, closeadj):
    gr = fcf.pct_change(63)
    result = _f06_solvency_score(debt, ebitda, fcf, 63) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: 252d solvency × fcf growth × closeadj
def f06ucq_f06_utility_credit_quality_solv_fcfgr_252d_base_v148_signal(debt, ebitda, fcf, closeadj):
    gr = fcf.pct_change(252)
    result = _f06_solvency_score(debt, ebitda, fcf, 252) * gr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: 63d coeff variation of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_63d_cv_base_v149_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    cv = _std(de_r, 63) / _mean(de_r, 63).abs().replace(0, np.nan)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: 252d coeff variation of debt/ebitda × closeadj
def f06ucq_f06_utility_credit_quality_debtebitda_252d_cv_base_v150_signal(debt, ebitda, closeadj):
    de_r = _f06_debt_ebitda(debt, ebitda)
    cv = _std(de_r, 252) / _mean(de_r, 252).abs().replace(0, np.nan)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06ucq_f06_utility_credit_quality_debtebitda_21d_csq_base_v076_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_csq_base_v077_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_csq_base_v078_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_mom_base_v079_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_mom_base_v080_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_mom_base_v081_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_csq_base_v082_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_csq_base_v083_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_csq_base_v084_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_csq_base_v085_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_csq_base_v086_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_csq_base_v087_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_dchg_base_v088_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_dchg_base_v089_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_dchg_base_v090_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_dchg_base_v091_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_dchg_base_v092_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_dchg_base_v093_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_dchg_base_v094_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_dchg_base_v095_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_dchg_base_v096_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_signde_base_v097_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_tanhde_base_v098_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_tanhde_base_v099_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_tanhde_base_v100_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_tanhde_base_v101_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_tanhde_base_v102_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_tanhde_base_v103_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_tanhde_base_v104_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_fcfdiv_base_v105_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_fcfdiv_base_v106_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_fcfdiv_base_v107_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_log_base_v108_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_log_base_v109_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_log_base_v110_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_sqrt_base_v111_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_sqrt_base_v112_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_sqrt_base_v113_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_max_base_v114_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_max_base_v115_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_max_base_v116_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_min_base_v117_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_min_base_v118_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_min_base_v119_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_max_base_v120_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_max_base_v121_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_max_base_v122_signal,
    f06ucq_f06_utility_credit_quality_solv_21d_min_base_v123_signal,
    f06ucq_f06_utility_credit_quality_solv_63d_min_base_v124_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_min_base_v125_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_rng_base_v126_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_rng_base_v127_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_rng_base_v128_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_21d_med_base_v129_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_med_base_v130_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_med_base_v131_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_rank_base_v132_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_rank_base_v133_signal,
    f06ucq_f06_utility_credit_quality_solv_252d_rank_base_v134_signal,
    f06ucq_f06_utility_credit_quality_creditq_21d_div_de_base_v135_signal,
    f06ucq_f06_utility_credit_quality_creditq_63d_div_de_base_v136_signal,
    f06ucq_f06_utility_credit_quality_creditq_252d_div_de_base_v137_signal,
    f06ucq_f06_utility_credit_quality_solv_debtgr_63d_base_v138_signal,
    f06ucq_f06_utility_credit_quality_solv_debtgr_252d_base_v139_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_eqgr_21d_base_v140_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_eqgr_63d_base_v141_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_eqgr_252d_base_v142_signal,
    f06ucq_f06_utility_credit_quality_creditq_eqgr_21d_base_v143_signal,
    f06ucq_f06_utility_credit_quality_creditq_eqgr_63d_base_v144_signal,
    f06ucq_f06_utility_credit_quality_creditq_eqgr_252d_base_v145_signal,
    f06ucq_f06_utility_credit_quality_solv_fcfgr_21d_base_v146_signal,
    f06ucq_f06_utility_credit_quality_solv_fcfgr_63d_base_v147_signal,
    f06ucq_f06_utility_credit_quality_solv_fcfgr_252d_base_v148_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_63d_cv_base_v149_signal,
    f06ucq_f06_utility_credit_quality_debtebitda_252d_cv_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_UTILITY_CREDIT_QUALITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    de = pd.Series(0.6 + 0.2 * np.sin(np.arange(n) / 250.0) + 0.05 * np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj, "ebitda": ebitda, "fcf": fcf, "equity": equity,
        "debt": debt, "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_debt_ebitda", "_f06_credit_quality", "_f06_solvency_score")
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
    print(f"OK f06_utility_credit_quality_base_076_150_claude: {n_features} features pass")
