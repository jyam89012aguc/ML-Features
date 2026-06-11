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


def f28dbs_f28_deposit_beta_signature_fundcostraw_fix_base_v001_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v002_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v003_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v004_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabs_fix_base_v005_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsq_fix_base_v006_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v007_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostlog_fix_base_v008_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v009_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v010_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v011_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v012_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_21d_base_v013_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v014_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v015_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v016_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_21d_base_v017_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasq_21d_base_v018_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v019_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetalog_21d_base_v020_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v021_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v022_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v023_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v024_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_21d_base_v025_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v026_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v027_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v028_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_21d_base_v029_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssq_21d_base_v030_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v031_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenslog_21d_base_v032_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v033_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v034_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v035_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v036_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v037_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v038_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v039_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v040_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v041_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v042_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v043_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v044_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_42d_base_v045_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v046_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v047_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v048_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_42d_base_v049_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasq_42d_base_v050_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v051_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetalog_42d_base_v052_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v053_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v054_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v055_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v056_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_42d_base_v057_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v058_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v059_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v060_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_42d_base_v061_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssq_42d_base_v062_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v063_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenslog_42d_base_v064_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v065_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v066_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v067_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v068_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v069_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v070_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v071_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v072_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = np.sign(base) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v073_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    rng = base.rolling(126, min_periods=max(1, 126 // 2)).max() - base.rolling(126, min_periods=max(1, 126 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v074_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = base * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v075_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    med = base.rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f28dbs_f28_deposit_beta_signature_fundcostraw_fix_base_v001_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v002_signal,
    f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v003_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v004_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabs_fix_base_v005_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsq_fix_base_v006_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v007_signal,
    f28dbs_f28_deposit_beta_signature_fundcostlog_fix_base_v008_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v009_signal,
    f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v010_signal,
    f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v011_signal,
    f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v012_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_21d_base_v013_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v014_signal,
    f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v015_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v016_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_21d_base_v017_signal,
    f28dbs_f28_deposit_beta_signature_depbetasq_21d_base_v018_signal,
    f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v019_signal,
    f28dbs_f28_deposit_beta_signature_depbetalog_21d_base_v020_signal,
    f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v021_signal,
    f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v022_signal,
    f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v023_signal,
    f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v024_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_21d_base_v025_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v026_signal,
    f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v027_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v028_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_21d_base_v029_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssq_21d_base_v030_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v031_signal,
    f28dbs_f28_deposit_beta_signature_fundsenslog_21d_base_v032_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v033_signal,
    f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v034_signal,
    f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v035_signal,
    f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v036_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v037_signal,
    f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v038_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v039_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v040_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v041_signal,
    f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v042_signal,
    f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v043_signal,
    f28dbs_f28_deposit_beta_signature_fundcostneg_fix_base_v044_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_42d_base_v045_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_base_v046_signal,
    f28dbs_f28_deposit_beta_signature_depbetastd_21d_base_v047_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_base_v048_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_42d_base_v049_signal,
    f28dbs_f28_deposit_beta_signature_depbetasq_42d_base_v050_signal,
    f28dbs_f28_deposit_beta_signature_depbetasign_21d_base_v051_signal,
    f28dbs_f28_deposit_beta_signature_depbetalog_42d_base_v052_signal,
    f28dbs_f28_deposit_beta_signature_depbetarng_21d_base_v053_signal,
    f28dbs_f28_deposit_beta_signature_depbetadv_21d_base_v054_signal,
    f28dbs_f28_deposit_beta_signature_depbetapos_21d_base_v055_signal,
    f28dbs_f28_deposit_beta_signature_depbetaneg_21d_base_v056_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_42d_base_v057_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_base_v058_signal,
    f28dbs_f28_deposit_beta_signature_fundsensstd_21d_base_v059_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_base_v060_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_42d_base_v061_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssq_42d_base_v062_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssign_21d_base_v063_signal,
    f28dbs_f28_deposit_beta_signature_fundsenslog_42d_base_v064_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrng_21d_base_v065_signal,
    f28dbs_f28_deposit_beta_signature_fundsensdv_21d_base_v066_signal,
    f28dbs_f28_deposit_beta_signature_fundsenspos_21d_base_v067_signal,
    f28dbs_f28_deposit_beta_signature_fundsensneg_21d_base_v068_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_base_v069_signal,
    f28dbs_f28_deposit_beta_signature_fundcoststd_fix_base_v070_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_base_v071_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsign_fix_base_v072_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrng_fix_base_v073_signal,
    f28dbs_f28_deposit_beta_signature_fundcostdv_fix_base_v074_signal,
    f28dbs_f28_deposit_beta_signature_fundcostpos_fix_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_DEPOSIT_BETA_SIGNATURE_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f28_deposit_beta_signature_base_001_075_claude: {n_features} features pass")
