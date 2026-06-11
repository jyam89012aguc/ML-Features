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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f28_funding_cost_proxy(opex, deposits):
    return opex / deposits.replace(0, np.nan)


def _f28_deposit_beta(opex, deposits, w):
    fc = opex / deposits.replace(0, np.nan)
    return fc - fc.rolling(w, min_periods=max(1, w // 2)).mean()


def _f28_funding_sensitivity(opex, deposits, w):
    fc = opex / deposits.replace(0, np.nan)
    return fc.rolling(w, min_periods=max(1, w // 2)).std()


def f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v001_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v002_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v003_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v004_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v005_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v006_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v007_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v008_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v009_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v010_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v011_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v012_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v013_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v014_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v015_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v016_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v017_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v018_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v019_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v020_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v021_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v022_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v023_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v024_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v025_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v026_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v027_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v028_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v029_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v030_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v031_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v032_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v033_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v034_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v035_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v036_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v037_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v038_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v039_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v040_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v041_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v042_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v043_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v044_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v045_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v046_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v047_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v048_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v049_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v050_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v051_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v052_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v053_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v054_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v055_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v056_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v057_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v058_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v059_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v060_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v061_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v062_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v063_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v064_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v065_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v066_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v067_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v068_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v069_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v070_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v071_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v072_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v073_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v074_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v075_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v076_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v077_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v078_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v079_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v080_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v081_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v082_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v083_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v084_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v085_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v086_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v087_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v088_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v089_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v090_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v091_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v092_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v093_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v094_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v095_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v096_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v097_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v098_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v099_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v100_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v101_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v102_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v103_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v104_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v105_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v106_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v107_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v108_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v109_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v110_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v111_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v112_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v113_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v114_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v115_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v116_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v117_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v118_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v119_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v120_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v121_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v122_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v123_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v124_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v125_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v126_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v127_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v128_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v129_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v130_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v131_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v132_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v133_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v134_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v135_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v136_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v137_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v138_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v139_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v140_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v141_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v142_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v143_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v144_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v145_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v146_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v147_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v148_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v149_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v150_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 42)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v001_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v002_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v003_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v004_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v005_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v006_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v007_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v008_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v009_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v010_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v011_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v012_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v013_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v014_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v015_signal,
    f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v016_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v017_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v018_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v019_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v020_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v021_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v022_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v023_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v024_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v025_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v026_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v027_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v028_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v029_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v030_signal,
    f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v031_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v032_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v033_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v034_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v035_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v036_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v037_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v038_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v039_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v040_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v041_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v042_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v043_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v044_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v045_signal,
    f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v046_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v047_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v048_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v049_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v050_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v051_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v052_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v053_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v054_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v055_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v056_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v057_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v058_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v059_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v060_signal,
    f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v061_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v062_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v063_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v064_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v065_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v066_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v067_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v068_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v069_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v070_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v071_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v072_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v073_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v074_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v075_signal,
    f28dbs_f28_deposit_beta_signature_fundcostraw_fix_jerk_v076_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v077_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v078_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabs_fix_jerk_v079_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaled_fix_jerk_v080_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_21d_jerk_v081_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v082_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v083_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_21d_jerk_v084_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_21d_jerk_v085_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_21d_jerk_v086_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v087_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v088_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_21d_jerk_v089_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_21d_jerk_v090_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v091_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v092_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v093_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v094_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v095_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v096_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v097_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v098_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v099_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v100_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v101_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v102_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v103_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v104_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v105_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v106_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v107_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v108_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v109_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v110_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v111_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v112_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v113_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v114_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v115_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v116_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v117_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v118_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v119_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v120_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v121_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v122_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v123_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v124_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v125_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v126_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v127_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v128_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v129_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v130_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v131_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v132_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v133_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v134_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v135_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v136_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v137_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v138_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsm_fix_jerk_v139_signal,
    f28dbs_f28_deposit_beta_signature_fundcostz_fix_jerk_v140_signal,
    f28dbs_f28_deposit_beta_signature_depbetaraw_42d_jerk_v141_signal,
    f28dbs_f28_deposit_beta_signature_depbetasm_21d_jerk_v142_signal,
    f28dbs_f28_deposit_beta_signature_depbetaz_21d_jerk_v143_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabs_42d_jerk_v144_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaled_42d_jerk_v145_signal,
    f28dbs_f28_deposit_beta_signature_fundsensraw_42d_jerk_v146_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssm_21d_jerk_v147_signal,
    f28dbs_f28_deposit_beta_signature_fundsensz_21d_jerk_v148_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabs_42d_jerk_v149_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaled_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_DEPOSIT_BETA_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f28_deposit_beta_signature_3rd_derivatives_001_150_claude: {n_features} features pass")
