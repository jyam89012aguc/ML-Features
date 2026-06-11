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
def _f28_funding_cost_proxy(opex, deposits):
    return opex / deposits.replace(0, np.nan)


def _f28_deposit_beta(opex, deposits, w):
    fc = opex / deposits.replace(0, np.nan)
    return fc - fc.rolling(w, min_periods=max(1, w // 2)).mean()


def _f28_funding_sensitivity(opex, deposits, w):
    fc = opex / deposits.replace(0, np.nan)
    return fc.rolling(w, min_periods=max(1, w // 2)).std()


def f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v076_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_63d_base_v077_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v078_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v079_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v080_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_63d_base_v081_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasq_63d_base_v082_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v083_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetalog_63d_base_v084_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v085_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v086_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v087_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v088_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_63d_base_v089_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v090_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v091_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v092_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_63d_base_v093_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssq_63d_base_v094_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v095_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenslog_63d_base_v096_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v097_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v098_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v099_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v100_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v101_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v102_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v103_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v104_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v105_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v106_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v107_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v108_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_126d_base_v109_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v110_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v111_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v112_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_126d_base_v113_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasq_126d_base_v114_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v115_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetalog_126d_base_v116_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v117_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v118_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v119_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v120_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_126d_base_v121_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v122_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v123_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v124_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_126d_base_v125_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssq_126d_base_v126_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v127_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenslog_126d_base_v128_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v129_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v130_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v131_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v132_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v133_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v134_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v135_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v136_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = np.sign(base) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v137_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    rng = base.rolling(504, min_periods=max(1, 504 // 2)).max() - base.rolling(504, min_periods=max(1, 504 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v138_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v139_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v140_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 504) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_189d_base_v141_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v142_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v143_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v144_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_189d_base_v145_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasq_189d_base_v146_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 189)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v147_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetalog_189d_base_v148_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 189)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v149_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    rng = base.rolling(504, min_periods=max(1, 504 // 2)).max() - base.rolling(504, min_periods=max(1, 504 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v150_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v076_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_63d_base_v077_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v078_signal,
    f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v079_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v080_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_63d_base_v081_signal,
    f28dbs_f28_deposit_beta_signature_depbetasq_63d_base_v082_signal,
    f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v083_signal,
    f28dbs_f28_deposit_beta_signature_depbetalog_63d_base_v084_signal,
    f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v085_signal,
    f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v086_signal,
    f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v087_signal,
    f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v088_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_63d_base_v089_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v090_signal,
    f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v091_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v092_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_63d_base_v093_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssq_63d_base_v094_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v095_signal,
    f28dbs_f28_deposit_beta_signature_fundsenslog_63d_base_v096_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v097_signal,
    f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v098_signal,
    f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v099_signal,
    f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v100_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v101_signal,
    f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v102_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v103_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v104_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v105_signal,
    f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v106_signal,
    f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v107_signal,
    f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v108_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_126d_base_v109_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v110_signal,
    f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v111_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v112_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_126d_base_v113_signal,
    f28dbs_f28_deposit_beta_signature_depbetasq_126d_base_v114_signal,
    f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v115_signal,
    f28dbs_f28_deposit_beta_signature_depbetalog_126d_base_v116_signal,
    f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v117_signal,
    f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v118_signal,
    f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v119_signal,
    f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v120_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_126d_base_v121_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v122_signal,
    f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v123_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v124_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_126d_base_v125_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssq_126d_base_v126_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v127_signal,
    f28dbs_f28_deposit_beta_signature_fundsenslog_126d_base_v128_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v129_signal,
    f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v130_signal,
    f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v131_signal,
    f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v132_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v133_signal,
    f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v134_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v135_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v136_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v137_signal,
    f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v138_signal,
    f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v139_signal,
    f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v140_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_189d_base_v141_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v142_signal,
    f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v143_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v144_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_189d_base_v145_signal,
    f28dbs_f28_deposit_beta_signature_depbetasq_189d_base_v146_signal,
    f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v147_signal,
    f28dbs_f28_deposit_beta_signature_depbetalog_189d_base_v148_signal,
    f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v149_signal,
    f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_DEPOSIT_BETA_SIGNATURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    opex = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    deposits = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="deposits")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"opex": opex, "deposits": deposits, "debt": debt, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_funding_cost_proxy", "_f28_deposit_beta", "_f28_funding_sensitivity")
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
    print(f"OK f28_deposit_beta_signature_base_076_150_claude: {n_features} features pass")
