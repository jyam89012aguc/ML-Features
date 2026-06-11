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
def _f30_distress_proxy(equity, assets, w):
    eqr = equity / assets.replace(0, np.nan)
    return eqr - eqr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_roa_collapse(roa, w):
    return roa - roa.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_distress_score(roa, de, w):
    score = roa - de / 10.0
    return score - score.rolling(w, min_periods=max(1, w // 2)).mean()


def f30bds_f30_bank_distress_signature_distproxz_21d_base_v076_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_63d_base_v077_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsq_63d_base_v078_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsign_21d_base_v079_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxlog_63d_base_v080_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrng_21d_base_v081_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxdv_21d_base_v082_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxpos_21d_base_v083_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxneg_21d_base_v084_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_63d_base_v085_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_base_v086_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollstd_21d_base_v087_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_base_v088_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_63d_base_v089_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsq_63d_base_v090_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsign_21d_base_v091_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolllog_63d_base_v092_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrng_21d_base_v093_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolldv_21d_base_v094_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollpos_21d_base_v095_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollneg_21d_base_v096_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_63d_base_v097_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_base_v098_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscstd_21d_base_v099_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_base_v100_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_63d_base_v101_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsq_63d_base_v102_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsign_21d_base_v103_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsclog_63d_base_v104_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrng_21d_base_v105_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscdv_21d_base_v106_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscpos_21d_base_v107_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscneg_21d_base_v108_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_126d_base_v109_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_base_v110_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxstd_21d_base_v111_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_base_v112_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_126d_base_v113_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsq_126d_base_v114_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsign_21d_base_v115_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxlog_126d_base_v116_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrng_21d_base_v117_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxdv_21d_base_v118_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxpos_21d_base_v119_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxneg_21d_base_v120_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_126d_base_v121_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_base_v122_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollstd_21d_base_v123_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_base_v124_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_126d_base_v125_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsq_126d_base_v126_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsign_21d_base_v127_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolllog_126d_base_v128_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrng_21d_base_v129_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolldv_21d_base_v130_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollpos_21d_base_v131_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollneg_21d_base_v132_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_126d_base_v133_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_base_v134_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscstd_21d_base_v135_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_base_v136_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_126d_base_v137_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsq_126d_base_v138_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsign_21d_base_v139_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsclog_126d_base_v140_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrng_21d_base_v141_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscdv_21d_base_v142_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscpos_21d_base_v143_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscneg_21d_base_v144_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_189d_base_v145_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_base_v146_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxstd_21d_base_v147_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_base_v148_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_189d_base_v149_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsq_189d_base_v150_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 189)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f30bds_f30_bank_distress_signature_distproxz_21d_base_v076_signal,
    f30bds_f30_bank_distress_signature_distproxabs_63d_base_v077_signal,
    f30bds_f30_bank_distress_signature_distproxsq_63d_base_v078_signal,
    f30bds_f30_bank_distress_signature_distproxsign_21d_base_v079_signal,
    f30bds_f30_bank_distress_signature_distproxlog_63d_base_v080_signal,
    f30bds_f30_bank_distress_signature_distproxrng_21d_base_v081_signal,
    f30bds_f30_bank_distress_signature_distproxdv_21d_base_v082_signal,
    f30bds_f30_bank_distress_signature_distproxpos_21d_base_v083_signal,
    f30bds_f30_bank_distress_signature_distproxneg_21d_base_v084_signal,
    f30bds_f30_bank_distress_signature_roacollraw_63d_base_v085_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_base_v086_signal,
    f30bds_f30_bank_distress_signature_roacollstd_21d_base_v087_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_base_v088_signal,
    f30bds_f30_bank_distress_signature_roacollabs_63d_base_v089_signal,
    f30bds_f30_bank_distress_signature_roacollsq_63d_base_v090_signal,
    f30bds_f30_bank_distress_signature_roacollsign_21d_base_v091_signal,
    f30bds_f30_bank_distress_signature_roacolllog_63d_base_v092_signal,
    f30bds_f30_bank_distress_signature_roacollrng_21d_base_v093_signal,
    f30bds_f30_bank_distress_signature_roacolldv_21d_base_v094_signal,
    f30bds_f30_bank_distress_signature_roacollpos_21d_base_v095_signal,
    f30bds_f30_bank_distress_signature_roacollneg_21d_base_v096_signal,
    f30bds_f30_bank_distress_signature_distscraw_63d_base_v097_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_base_v098_signal,
    f30bds_f30_bank_distress_signature_distscstd_21d_base_v099_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_base_v100_signal,
    f30bds_f30_bank_distress_signature_distscabs_63d_base_v101_signal,
    f30bds_f30_bank_distress_signature_distscsq_63d_base_v102_signal,
    f30bds_f30_bank_distress_signature_distscsign_21d_base_v103_signal,
    f30bds_f30_bank_distress_signature_distsclog_63d_base_v104_signal,
    f30bds_f30_bank_distress_signature_distscrng_21d_base_v105_signal,
    f30bds_f30_bank_distress_signature_distscdv_21d_base_v106_signal,
    f30bds_f30_bank_distress_signature_distscpos_21d_base_v107_signal,
    f30bds_f30_bank_distress_signature_distscneg_21d_base_v108_signal,
    f30bds_f30_bank_distress_signature_distproxraw_126d_base_v109_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_base_v110_signal,
    f30bds_f30_bank_distress_signature_distproxstd_21d_base_v111_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_base_v112_signal,
    f30bds_f30_bank_distress_signature_distproxabs_126d_base_v113_signal,
    f30bds_f30_bank_distress_signature_distproxsq_126d_base_v114_signal,
    f30bds_f30_bank_distress_signature_distproxsign_21d_base_v115_signal,
    f30bds_f30_bank_distress_signature_distproxlog_126d_base_v116_signal,
    f30bds_f30_bank_distress_signature_distproxrng_21d_base_v117_signal,
    f30bds_f30_bank_distress_signature_distproxdv_21d_base_v118_signal,
    f30bds_f30_bank_distress_signature_distproxpos_21d_base_v119_signal,
    f30bds_f30_bank_distress_signature_distproxneg_21d_base_v120_signal,
    f30bds_f30_bank_distress_signature_roacollraw_126d_base_v121_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_base_v122_signal,
    f30bds_f30_bank_distress_signature_roacollstd_21d_base_v123_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_base_v124_signal,
    f30bds_f30_bank_distress_signature_roacollabs_126d_base_v125_signal,
    f30bds_f30_bank_distress_signature_roacollsq_126d_base_v126_signal,
    f30bds_f30_bank_distress_signature_roacollsign_21d_base_v127_signal,
    f30bds_f30_bank_distress_signature_roacolllog_126d_base_v128_signal,
    f30bds_f30_bank_distress_signature_roacollrng_21d_base_v129_signal,
    f30bds_f30_bank_distress_signature_roacolldv_21d_base_v130_signal,
    f30bds_f30_bank_distress_signature_roacollpos_21d_base_v131_signal,
    f30bds_f30_bank_distress_signature_roacollneg_21d_base_v132_signal,
    f30bds_f30_bank_distress_signature_distscraw_126d_base_v133_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_base_v134_signal,
    f30bds_f30_bank_distress_signature_distscstd_21d_base_v135_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_base_v136_signal,
    f30bds_f30_bank_distress_signature_distscabs_126d_base_v137_signal,
    f30bds_f30_bank_distress_signature_distscsq_126d_base_v138_signal,
    f30bds_f30_bank_distress_signature_distscsign_21d_base_v139_signal,
    f30bds_f30_bank_distress_signature_distsclog_126d_base_v140_signal,
    f30bds_f30_bank_distress_signature_distscrng_21d_base_v141_signal,
    f30bds_f30_bank_distress_signature_distscdv_21d_base_v142_signal,
    f30bds_f30_bank_distress_signature_distscpos_21d_base_v143_signal,
    f30bds_f30_bank_distress_signature_distscneg_21d_base_v144_signal,
    f30bds_f30_bank_distress_signature_distproxraw_189d_base_v145_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_base_v146_signal,
    f30bds_f30_bank_distress_signature_distproxstd_21d_base_v147_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_base_v148_signal,
    f30bds_f30_bank_distress_signature_distproxabs_189d_base_v149_signal,
    f30bds_f30_bank_distress_signature_distproxsq_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_BANK_DISTRESS_SIGNATURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    de = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"roa": roa, "de": de, "equity": equity, "assets": assets, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_distress_proxy", "_f30_roa_collapse", "_f30_distress_score")
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
    print(f"OK f30_bank_distress_signature_base_076_150_claude: {n_features} features pass")
