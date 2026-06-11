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


def f27ccp_f27_credit_cycle_position_creditproxyraw_21d_base_v001_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v002_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v003_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v004_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_21d_base_v005_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysq_21d_base_v006_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v007_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxylog_21d_base_v008_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v009_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v010_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v011_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v012_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_21d_base_v013_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_base_v014_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintstd_21d_base_v015_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_base_v016_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_21d_base_v017_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsq_21d_base_v018_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsign_21d_base_v019_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintlog_21d_base_v020_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrng_21d_base_v021_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintdv_21d_base_v022_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintpos_21d_base_v023_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintneg_21d_base_v024_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_21d_base_v025_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v026_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v027_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v028_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_21d_base_v029_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresq_21d_base_v030_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v031_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorelog_21d_base_v032_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v033_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v034_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v035_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v036_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_42d_base_v037_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v038_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v039_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v040_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_42d_base_v041_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysq_42d_base_v042_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v043_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxylog_42d_base_v044_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v045_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v046_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v047_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v048_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_42d_base_v049_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_base_v050_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintstd_21d_base_v051_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_base_v052_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_42d_base_v053_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsq_42d_base_v054_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsign_21d_base_v055_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintlog_42d_base_v056_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrng_21d_base_v057_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintdv_21d_base_v058_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintpos_21d_base_v059_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintneg_21d_base_v060_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_42d_base_v061_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v062_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v063_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v064_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_42d_base_v065_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresq_42d_base_v066_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v067_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorelog_42d_base_v068_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v069_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v070_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v071_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v072_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_63d_base_v073_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v074_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v075_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27ccp_f27_credit_cycle_position_creditproxyraw_21d_base_v001_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v002_signal,
    f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v003_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v004_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_21d_base_v005_signal,
    f27ccp_f27_credit_cycle_position_creditproxysq_21d_base_v006_signal,
    f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v007_signal,
    f27ccp_f27_credit_cycle_position_creditproxylog_21d_base_v008_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v009_signal,
    f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v010_signal,
    f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v011_signal,
    f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v012_signal,
    f27ccp_f27_credit_cycle_position_provintraw_21d_base_v013_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_base_v014_signal,
    f27ccp_f27_credit_cycle_position_provintstd_21d_base_v015_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_base_v016_signal,
    f27ccp_f27_credit_cycle_position_provintabs_21d_base_v017_signal,
    f27ccp_f27_credit_cycle_position_provintsq_21d_base_v018_signal,
    f27ccp_f27_credit_cycle_position_provintsign_21d_base_v019_signal,
    f27ccp_f27_credit_cycle_position_provintlog_21d_base_v020_signal,
    f27ccp_f27_credit_cycle_position_provintrng_21d_base_v021_signal,
    f27ccp_f27_credit_cycle_position_provintdv_21d_base_v022_signal,
    f27ccp_f27_credit_cycle_position_provintpos_21d_base_v023_signal,
    f27ccp_f27_credit_cycle_position_provintneg_21d_base_v024_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_21d_base_v025_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v026_signal,
    f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v027_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v028_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_21d_base_v029_signal,
    f27ccp_f27_credit_cycle_position_phasescoresq_21d_base_v030_signal,
    f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v031_signal,
    f27ccp_f27_credit_cycle_position_phasescorelog_21d_base_v032_signal,
    f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v033_signal,
    f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v034_signal,
    f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v035_signal,
    f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v036_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_42d_base_v037_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v038_signal,
    f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v039_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_base_v040_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_42d_base_v041_signal,
    f27ccp_f27_credit_cycle_position_creditproxysq_42d_base_v042_signal,
    f27ccp_f27_credit_cycle_position_creditproxysign_21d_base_v043_signal,
    f27ccp_f27_credit_cycle_position_creditproxylog_42d_base_v044_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrng_21d_base_v045_signal,
    f27ccp_f27_credit_cycle_position_creditproxydv_21d_base_v046_signal,
    f27ccp_f27_credit_cycle_position_creditproxypos_21d_base_v047_signal,
    f27ccp_f27_credit_cycle_position_creditproxyneg_21d_base_v048_signal,
    f27ccp_f27_credit_cycle_position_provintraw_42d_base_v049_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_base_v050_signal,
    f27ccp_f27_credit_cycle_position_provintstd_21d_base_v051_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_base_v052_signal,
    f27ccp_f27_credit_cycle_position_provintabs_42d_base_v053_signal,
    f27ccp_f27_credit_cycle_position_provintsq_42d_base_v054_signal,
    f27ccp_f27_credit_cycle_position_provintsign_21d_base_v055_signal,
    f27ccp_f27_credit_cycle_position_provintlog_42d_base_v056_signal,
    f27ccp_f27_credit_cycle_position_provintrng_21d_base_v057_signal,
    f27ccp_f27_credit_cycle_position_provintdv_21d_base_v058_signal,
    f27ccp_f27_credit_cycle_position_provintpos_21d_base_v059_signal,
    f27ccp_f27_credit_cycle_position_provintneg_21d_base_v060_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_42d_base_v061_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_base_v062_signal,
    f27ccp_f27_credit_cycle_position_phasescorestd_21d_base_v063_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_base_v064_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_42d_base_v065_signal,
    f27ccp_f27_credit_cycle_position_phasescoresq_42d_base_v066_signal,
    f27ccp_f27_credit_cycle_position_phasescoresign_21d_base_v067_signal,
    f27ccp_f27_credit_cycle_position_phasescorelog_42d_base_v068_signal,
    f27ccp_f27_credit_cycle_position_phasescorerng_21d_base_v069_signal,
    f27ccp_f27_credit_cycle_position_phasescoredv_21d_base_v070_signal,
    f27ccp_f27_credit_cycle_position_phasescorepos_21d_base_v071_signal,
    f27ccp_f27_credit_cycle_position_phasescoreneg_21d_base_v072_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_63d_base_v073_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_base_v074_signal,
    f27ccp_f27_credit_cycle_position_creditproxystd_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CREDIT_CYCLE_POSITION_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f27_credit_cycle_position_base_001_075_claude: {n_features} features pass")
