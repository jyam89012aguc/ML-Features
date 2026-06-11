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
def _f27_credit_cycle_proxy(netinc, revenue, w):
    margin = netinc / revenue.replace(0, np.nan)
    return margin - margin.rolling(w, min_periods=max(1, w // 2)).mean()


def _f27_provision_intensity(revenue, netinc, w):
    gap = (revenue - netinc) / revenue.replace(0, np.nan)
    return gap - gap.rolling(w, min_periods=max(1, w // 2)).mean()


def _f27_cycle_phase_score(revenue, netinc, w):
    rg = revenue.pct_change(periods=w)
    ng = netinc.pct_change(periods=w)
    return ng - rg


def f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v076_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_63d_base_v077_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysq_63d_base_v078_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v079_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxylog_63d_base_v080_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v081_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v082_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v083_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v084_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_63d_base_v085_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_base_v086_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintstd_21d_base_v087_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_base_v088_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_63d_base_v089_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsq_63d_base_v090_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsign_21d_base_v091_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintlog_63d_base_v092_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrng_21d_base_v093_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintdv_21d_base_v094_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintpos_21d_base_v095_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintneg_21d_base_v096_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_63d_base_v097_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v098_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v099_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v100_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_63d_base_v101_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresq_63d_base_v102_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v103_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorelog_63d_base_v104_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 63)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v105_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v106_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v107_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v108_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 126) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_126d_base_v109_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v110_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v111_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v112_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_126d_base_v113_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysq_126d_base_v114_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v115_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxylog_126d_base_v116_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v117_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v118_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v119_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v120_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_126d_base_v121_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_base_v122_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintstd_21d_base_v123_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_base_v124_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_126d_base_v125_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsq_126d_base_v126_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsign_21d_base_v127_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintlog_126d_base_v128_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrng_21d_base_v129_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintdv_21d_base_v130_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintpos_21d_base_v131_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintneg_21d_base_v132_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_126d_base_v133_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v134_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v135_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v136_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_126d_base_v137_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresq_126d_base_v138_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 126)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v139_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorelog_126d_base_v140_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 126)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v141_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    rng = base.rolling(252, min_periods=max(1, 252 // 2)).max() - base.rolling(252, min_periods=max(1, 252 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v142_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v143_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v144_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 252) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_189d_base_v145_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v146_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v147_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v148_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_189d_base_v149_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysq_189d_base_v150_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 189)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v076_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_63d_base_v077_signal,
    f27ccp_f27_credit_cycle_position_creditproxysq_63d_base_v078_signal,
    f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v079_signal,
    f27ccp_f27_credit_cycle_position_creditproxylog_63d_base_v080_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v081_signal,
    f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v082_signal,
    f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v083_signal,
    f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v084_signal,
    f27ccp_f27_credit_cycle_position_provintraw_63d_base_v085_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_base_v086_signal,
    f27ccp_f27_credit_cycle_position_provintstd_21d_base_v087_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_base_v088_signal,
    f27ccp_f27_credit_cycle_position_provintabs_63d_base_v089_signal,
    f27ccp_f27_credit_cycle_position_provintsq_63d_base_v090_signal,
    f27ccp_f27_credit_cycle_position_provintsign_21d_base_v091_signal,
    f27ccp_f27_credit_cycle_position_provintlog_63d_base_v092_signal,
    f27ccp_f27_credit_cycle_position_provintrng_21d_base_v093_signal,
    f27ccp_f27_credit_cycle_position_provintdv_21d_base_v094_signal,
    f27ccp_f27_credit_cycle_position_provintpos_21d_base_v095_signal,
    f27ccp_f27_credit_cycle_position_provintneg_21d_base_v096_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_63d_base_v097_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v098_signal,
    f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v099_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v100_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_63d_base_v101_signal,
    f27ccp_f27_credit_cycle_position_phasescoresq_63d_base_v102_signal,
    f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v103_signal,
    f27ccp_f27_credit_cycle_position_phasescorelog_63d_base_v104_signal,
    f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v105_signal,
    f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v106_signal,
    f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v107_signal,
    f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v108_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_126d_base_v109_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v110_signal,
    f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v111_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v112_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_126d_base_v113_signal,
    f27ccp_f27_credit_cycle_position_creditproxysq_126d_base_v114_signal,
    f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v115_signal,
    f27ccp_f27_credit_cycle_position_creditproxylog_126d_base_v116_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v117_signal,
    f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v118_signal,
    f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v119_signal,
    f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v120_signal,
    f27ccp_f27_credit_cycle_position_provintraw_126d_base_v121_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_base_v122_signal,
    f27ccp_f27_credit_cycle_position_provintstd_21d_base_v123_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_base_v124_signal,
    f27ccp_f27_credit_cycle_position_provintabs_126d_base_v125_signal,
    f27ccp_f27_credit_cycle_position_provintsq_126d_base_v126_signal,
    f27ccp_f27_credit_cycle_position_provintsign_21d_base_v127_signal,
    f27ccp_f27_credit_cycle_position_provintlog_126d_base_v128_signal,
    f27ccp_f27_credit_cycle_position_provintrng_21d_base_v129_signal,
    f27ccp_f27_credit_cycle_position_provintdv_21d_base_v130_signal,
    f27ccp_f27_credit_cycle_position_provintpos_21d_base_v131_signal,
    f27ccp_f27_credit_cycle_position_provintneg_21d_base_v132_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_126d_base_v133_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v134_signal,
    f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v135_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v136_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_126d_base_v137_signal,
    f27ccp_f27_credit_cycle_position_phasescoresq_126d_base_v138_signal,
    f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v139_signal,
    f27ccp_f27_credit_cycle_position_phasescorelog_126d_base_v140_signal,
    f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v141_signal,
    f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v142_signal,
    f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v143_signal,
    f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v144_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_189d_base_v145_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v146_signal,
    f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v147_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v148_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_189d_base_v149_signal,
    f27ccp_f27_credit_cycle_position_creditproxysq_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CREDIT_CYCLE_POSITION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"revenue": revenue, "netinc": netinc, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_credit_cycle_proxy", "_f27_provision_intensity", "_f27_cycle_phase_score")
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
    print(f"OK f27_credit_cycle_position_base_076_150_claude: {n_features} features pass")
