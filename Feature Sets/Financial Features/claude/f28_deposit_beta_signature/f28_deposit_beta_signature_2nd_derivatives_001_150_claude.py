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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f28_funding_cost_proxy(opex, deposits):
    return opex / deposits.replace(0, np.nan)


def _f28_deposit_beta(opex, deposits, w):
    fc = opex / deposits.replace(0, np.nan)
    return fc - fc.rolling(w, min_periods=max(1, w // 2)).mean()


def _f28_funding_sensitivity(opex, deposits, w):
    fc = opex / deposits.replace(0, np.nan)
    return fc.rolling(w, min_periods=max(1, w // 2)).std()


def f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v001_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v002_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v003_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v004_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v005_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v006_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v007_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v008_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v009_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v010_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v011_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v012_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v013_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v014_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v015_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v016_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v017_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v018_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v019_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v020_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v021_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v022_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v023_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v024_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v025_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v026_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v027_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v028_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v029_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v030_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v031_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v032_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v033_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v034_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v035_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v036_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v037_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v038_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v039_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v040_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v041_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v042_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v043_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v044_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v045_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v046_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v047_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v048_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v049_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v050_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v051_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v052_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v053_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v054_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v055_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v056_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v057_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v058_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v059_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v060_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v061_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v062_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v063_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v064_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v065_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v066_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v067_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v068_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v069_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v070_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v071_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v072_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v073_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v074_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v075_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v076_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v077_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v078_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v079_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v080_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v081_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v082_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v083_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v084_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v085_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v086_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v087_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v088_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v089_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v090_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v091_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v092_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v093_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v094_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v095_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v096_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v097_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v098_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v099_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v100_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v101_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v102_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v103_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v104_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v105_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v106_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v107_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v108_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v109_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v110_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v111_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v112_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v113_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v114_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v115_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v116_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v117_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v118_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v119_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v120_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v121_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v122_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v123_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v124_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v125_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v126_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v127_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v128_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v129_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v130_signal(opex, deposits, closeadj):
    base = _f28_funding_cost_proxy(opex, deposits)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v131_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v132_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v133_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v134_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v135_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v136_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v137_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v138_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v139_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v140_signal(opex, deposits, closeadj):
    base = _f28_deposit_beta(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v141_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v142_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v143_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v144_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v145_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v146_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v147_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v148_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v149_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v150_signal(opex, deposits, closeadj):
    base = _f28_funding_sensitivity(opex, deposits, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v001_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v002_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v003_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v004_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v005_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v006_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v007_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v008_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v009_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v010_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v011_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v012_signal,
    f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v013_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v014_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v015_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v016_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v017_signal,
    f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v018_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v019_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v020_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v021_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v022_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v023_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v024_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v025_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v026_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v027_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v028_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v029_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v030_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v031_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v032_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v033_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v034_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v035_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v036_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v037_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v038_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v039_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v040_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v041_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v042_signal,
    f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v043_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v044_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v045_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v046_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v047_signal,
    f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v048_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v049_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v050_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v051_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v052_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v053_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v054_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v055_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v056_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v057_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v058_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v059_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v060_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v061_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v062_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v063_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v064_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v065_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v066_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v067_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v068_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v069_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v070_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v071_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v072_signal,
    f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v073_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v074_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v075_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v076_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v077_signal,
    f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v078_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v079_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v080_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v081_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v082_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v083_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v084_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v085_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v086_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v087_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v088_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v089_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v090_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v091_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v092_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v093_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v094_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v095_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v096_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v097_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v098_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v099_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v100_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v101_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v102_signal,
    f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v103_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v104_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v105_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v106_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v107_signal,
    f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v108_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v109_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v110_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v111_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v112_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v113_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v114_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v115_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v116_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v117_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v118_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v119_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v120_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawsdn_fix_slope_v121_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmsdn_fix_slope_v122_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzsdn_fix_slope_v123_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabssdn_fix_slope_v124_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledsdn_fix_slope_v125_signal,
    f28dbs_f28_deposit_beta_signature_fundcostrawpct_fix_slope_v126_signal,
    f28dbs_f28_deposit_beta_signature_fundcostsmpct_fix_slope_v127_signal,
    f28dbs_f28_deposit_beta_signature_fundcostzpct_fix_slope_v128_signal,
    f28dbs_f28_deposit_beta_signature_fundcostabspct_fix_slope_v129_signal,
    f28dbs_f28_deposit_beta_signature_fundcostscaledpct_fix_slope_v130_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawsdn_21d_slope_v131_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmsdn_21d_slope_v132_signal,
    f28dbs_f28_deposit_beta_signature_depbetazsdn_21d_slope_v133_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabssdn_21d_slope_v134_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledsdn_21d_slope_v135_signal,
    f28dbs_f28_deposit_beta_signature_depbetarawpct_21d_slope_v136_signal,
    f28dbs_f28_deposit_beta_signature_depbetasmpct_21d_slope_v137_signal,
    f28dbs_f28_deposit_beta_signature_depbetazpct_21d_slope_v138_signal,
    f28dbs_f28_deposit_beta_signature_depbetaabspct_21d_slope_v139_signal,
    f28dbs_f28_deposit_beta_signature_depbetascaledpct_21d_slope_v140_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawsdn_21d_slope_v141_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmsdn_21d_slope_v142_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszsdn_21d_slope_v143_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabssdn_21d_slope_v144_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledsdn_21d_slope_v145_signal,
    f28dbs_f28_deposit_beta_signature_fundsensrawpct_21d_slope_v146_signal,
    f28dbs_f28_deposit_beta_signature_fundsenssmpct_21d_slope_v147_signal,
    f28dbs_f28_deposit_beta_signature_fundsenszpct_21d_slope_v148_signal,
    f28dbs_f28_deposit_beta_signature_fundsensabspct_21d_slope_v149_signal,
    f28dbs_f28_deposit_beta_signature_fundsensscaledpct_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_DEPOSIT_BETA_SIGNATURE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK f28_deposit_beta_signature_2nd_derivatives_001_150_claude: {n_features} features pass")
