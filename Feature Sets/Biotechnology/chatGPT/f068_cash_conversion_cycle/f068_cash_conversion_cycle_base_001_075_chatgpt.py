"""Family f068 - Cash conversion cycle proxy (Returns and Efficiency) | Sharadar tables: SF1 | fields: receivables, inventory, payables, revenue, cor | base 001-075"""
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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _cash_conversion_cycle_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_conversion_cycle_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_conversion_cycle_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed receivables times closeadj
def ccc_f068_cash_conversion_cycle_raw_21d_base_v001_signal(receivables, closeadj):
    result = _mean(receivables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed receivables times closeadj
def ccc_f068_cash_conversion_cycle_raw_63d_base_v002_signal(receivables, closeadj):
    result = _mean(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed receivables times closeadj
def ccc_f068_cash_conversion_cycle_raw_126d_base_v003_signal(receivables, closeadj):
    result = _mean(receivables, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed receivables times closeadj
def ccc_f068_cash_conversion_cycle_raw_252d_base_v004_signal(receivables, closeadj):
    result = _mean(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed receivables times closeadj
def ccc_f068_cash_conversion_cycle_raw_504d_base_v005_signal(receivables, closeadj):
    result = _mean(receivables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_log_21d_base_v006_signal(receivables, closeadj):
    result = _mean(_cash_conversion_cycle_log(receivables), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_log_63d_base_v007_signal(receivables, closeadj):
    result = _mean(_cash_conversion_cycle_log(receivables), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_log_126d_base_v008_signal(receivables, closeadj):
    result = _mean(_cash_conversion_cycle_log(receivables), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_log_252d_base_v009_signal(receivables, closeadj):
    result = _mean(_cash_conversion_cycle_log(receivables), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_log_504d_base_v010_signal(receivables, closeadj):
    result = _mean(_cash_conversion_cycle_log(receivables), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/inventory mean
def ccc_f068_cash_conversion_cycle_per_inventory_63d_base_v011_signal(receivables, inventory):
    result = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/inventory mean
def ccc_f068_cash_conversion_cycle_per_inventory_252d_base_v012_signal(receivables, inventory):
    result = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/inventory mean
def ccc_f068_cash_conversion_cycle_per_inventory_504d_base_v013_signal(receivables, inventory):
    result = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/payables mean
def ccc_f068_cash_conversion_cycle_per_payables_63d_base_v014_signal(receivables, payables):
    result = _mean(_cash_conversion_cycle_scaled(receivables, payables), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/payables mean
def ccc_f068_cash_conversion_cycle_per_payables_252d_base_v015_signal(receivables, payables):
    result = _mean(_cash_conversion_cycle_scaled(receivables, payables), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/payables mean
def ccc_f068_cash_conversion_cycle_per_payables_504d_base_v016_signal(receivables, payables):
    result = _mean(_cash_conversion_cycle_scaled(receivables, payables), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/revenue mean
def ccc_f068_cash_conversion_cycle_per_revenue_63d_base_v017_signal(receivables, revenue):
    result = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/revenue mean
def ccc_f068_cash_conversion_cycle_per_revenue_252d_base_v018_signal(receivables, revenue):
    result = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/revenue mean
def ccc_f068_cash_conversion_cycle_per_revenue_504d_base_v019_signal(receivables, revenue):
    result = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/cor mean
def ccc_f068_cash_conversion_cycle_per_cor_63d_base_v020_signal(receivables, cor):
    result = _mean(_cash_conversion_cycle_scaled(receivables, cor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/cor mean
def ccc_f068_cash_conversion_cycle_per_cor_252d_base_v021_signal(receivables, cor):
    result = _mean(_cash_conversion_cycle_scaled(receivables, cor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/cor mean
def ccc_f068_cash_conversion_cycle_per_cor_504d_base_v022_signal(receivables, cor):
    result = _mean(_cash_conversion_cycle_scaled(receivables, cor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/assets mean
def ccc_f068_cash_conversion_cycle_per_assets_63d_base_v023_signal(receivables, assets):
    result = _mean(_cash_conversion_cycle_scaled(receivables, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/assets mean
def ccc_f068_cash_conversion_cycle_per_assets_252d_base_v024_signal(receivables, assets):
    result = _mean(_cash_conversion_cycle_scaled(receivables, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/assets mean
def ccc_f068_cash_conversion_cycle_per_assets_504d_base_v025_signal(receivables, assets):
    result = _mean(_cash_conversion_cycle_scaled(receivables, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d receivables per share times closeadj
def ccc_f068_cash_conversion_cycle_pershare_21d_base_v026_signal(receivables, sharesbas, closeadj):
    ps = _cash_conversion_cycle_per_share(receivables, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables per share times closeadj
def ccc_f068_cash_conversion_cycle_pershare_63d_base_v027_signal(receivables, sharesbas, closeadj):
    ps = _cash_conversion_cycle_per_share(receivables, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d receivables per share times closeadj
def ccc_f068_cash_conversion_cycle_pershare_126d_base_v028_signal(receivables, sharesbas, closeadj):
    ps = _cash_conversion_cycle_per_share(receivables, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables per share times closeadj
def ccc_f068_cash_conversion_cycle_pershare_252d_base_v029_signal(receivables, sharesbas, closeadj):
    ps = _cash_conversion_cycle_per_share(receivables, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables per share times closeadj
def ccc_f068_cash_conversion_cycle_pershare_504d_base_v030_signal(receivables, sharesbas, closeadj):
    ps = _cash_conversion_cycle_per_share(receivables, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of receivables times closeadj
def ccc_f068_cash_conversion_cycle_std_63d_base_v031_signal(receivables, closeadj):
    result = _std(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of receivables times closeadj
def ccc_f068_cash_conversion_cycle_std_252d_base_v032_signal(receivables, closeadj):
    result = _std(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of receivables times closeadj
def ccc_f068_cash_conversion_cycle_std_504d_base_v033_signal(receivables, closeadj):
    result = _std(receivables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of receivables
def ccc_f068_cash_conversion_cycle_z_252d_base_v034_signal(receivables):
    result = _z(receivables, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of receivables
def ccc_f068_cash_conversion_cycle_z_504d_base_v035_signal(receivables):
    result = _z(receivables, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(receivables)
def ccc_f068_cash_conversion_cycle_logz_252d_base_v036_signal(receivables):
    result = _z(_cash_conversion_cycle_log(receivables), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(receivables)
def ccc_f068_cash_conversion_cycle_logz_504d_base_v037_signal(receivables):
    result = _z(_cash_conversion_cycle_log(receivables), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of receivables^2 times closeadj
def ccc_f068_cash_conversion_cycle_sq_63d_base_v038_signal(receivables, closeadj):
    result = _mean(receivables * receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of receivables^2 times closeadj
def ccc_f068_cash_conversion_cycle_sq_252d_base_v039_signal(receivables, closeadj):
    result = _mean(receivables * receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_sign_21d_base_v040_signal(receivables, closeadj):
    result = _mean(np.sign(receivables), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_sign_63d_base_v041_signal(receivables, closeadj):
    result = _mean(np.sign(receivables), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(receivables) times closeadj
def ccc_f068_cash_conversion_cycle_sign_252d_base_v042_signal(receivables, closeadj):
    result = _mean(np.sign(receivables), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/opex mean
def ccc_f068_cash_conversion_cycle_per_opex_63d_base_v043_signal(receivables, opex):
    result = _mean(_cash_conversion_cycle_scaled(receivables, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/opex mean
def ccc_f068_cash_conversion_cycle_per_opex_252d_base_v044_signal(receivables, opex):
    result = _mean(_cash_conversion_cycle_scaled(receivables, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/ebitda mean
def ccc_f068_cash_conversion_cycle_per_ebitda_63d_base_v045_signal(receivables, ebitda):
    result = _mean(_cash_conversion_cycle_scaled(receivables, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/ebitda mean
def ccc_f068_cash_conversion_cycle_per_ebitda_252d_base_v046_signal(receivables, ebitda):
    result = _mean(_cash_conversion_cycle_scaled(receivables, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/capex mean
def ccc_f068_cash_conversion_cycle_per_capex_63d_base_v047_signal(receivables, capex):
    result = _mean(_cash_conversion_cycle_scaled(receivables, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/capex mean
def ccc_f068_cash_conversion_cycle_per_capex_252d_base_v048_signal(receivables, capex):
    result = _mean(_cash_conversion_cycle_scaled(receivables, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/liabilities mean
def ccc_f068_cash_conversion_cycle_per_liabilities_63d_base_v049_signal(receivables, liabilities):
    result = _mean(_cash_conversion_cycle_scaled(receivables, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/liabilities mean
def ccc_f068_cash_conversion_cycle_per_liabilities_252d_base_v050_signal(receivables, liabilities):
    result = _mean(_cash_conversion_cycle_scaled(receivables, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 252d max times closeadj
def ccc_f068_cash_conversion_cycle_relmax_252d_base_v051_signal(receivables, closeadj):
    peak = receivables.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (receivables / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 504d max times closeadj
def ccc_f068_cash_conversion_cycle_relmax_504d_base_v052_signal(receivables, closeadj):
    peak = receivables.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (receivables / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 252d min times closeadj
def ccc_f068_cash_conversion_cycle_relmin_252d_base_v053_signal(receivables, closeadj):
    trough = receivables.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (receivables / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 504d min times closeadj
def ccc_f068_cash_conversion_cycle_relmin_504d_base_v054_signal(receivables, closeadj):
    trough = receivables.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (receivables / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of receivables times closeadj
def ccc_f068_cash_conversion_cycle_pct_21d_base_v055_signal(receivables, closeadj):
    result = _pct_change(receivables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of receivables times closeadj
def ccc_f068_cash_conversion_cycle_pct_63d_base_v056_signal(receivables, closeadj):
    result = _pct_change(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of receivables times closeadj
def ccc_f068_cash_conversion_cycle_pct_252d_base_v057_signal(receivables, closeadj):
    result = _pct_change(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of receivables times closeadj
def ccc_f068_cash_conversion_cycle_sum_63d_base_v058_signal(receivables, closeadj):
    result = receivables.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of receivables times closeadj
def ccc_f068_cash_conversion_cycle_sum_252d_base_v059_signal(receivables, closeadj):
    result = receivables.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of receivables times closeadj
def ccc_f068_cash_conversion_cycle_sum_504d_base_v060_signal(receivables, closeadj):
    result = receivables.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(63d) / smoothed inventory(252d) x closeadj
def ccc_f068_cash_conversion_cycle_rom_inventory_252_63d_base_v061_signal(receivables, inventory, closeadj):
    n = _mean(receivables, 63)
    d = _mean(inventory, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(126d) / smoothed inventory(504d) x closeadj
def ccc_f068_cash_conversion_cycle_rom_inventory_504_126d_base_v062_signal(receivables, inventory, closeadj):
    n = _mean(receivables, 126)
    d = _mean(inventory, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(63d) / smoothed payables(252d) x closeadj
def ccc_f068_cash_conversion_cycle_rom_payables_252_63d_base_v063_signal(receivables, payables, closeadj):
    n = _mean(receivables, 63)
    d = _mean(payables, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(126d) / smoothed payables(504d) x closeadj
def ccc_f068_cash_conversion_cycle_rom_payables_504_126d_base_v064_signal(receivables, payables, closeadj):
    n = _mean(receivables, 126)
    d = _mean(payables, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(63d) / smoothed revenue(252d) x closeadj
def ccc_f068_cash_conversion_cycle_rom_revenue_252_63d_base_v065_signal(receivables, revenue, closeadj):
    n = _mean(receivables, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(126d) / smoothed revenue(504d) x closeadj
def ccc_f068_cash_conversion_cycle_rom_revenue_504_126d_base_v066_signal(receivables, revenue, closeadj):
    n = _mean(receivables, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(receivables) / std(inventory)
def ccc_f068_cash_conversion_cycle_volratio_inventory_252d_base_v067_signal(receivables, inventory):
    n = _std(receivables, 252)
    d = _std(inventory, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(receivables) / std(inventory)
def ccc_f068_cash_conversion_cycle_volratio_inventory_504d_base_v068_signal(receivables, inventory):
    n = _std(receivables, 504)
    d = _std(inventory, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(receivables) / std(payables)
def ccc_f068_cash_conversion_cycle_volratio_payables_252d_base_v069_signal(receivables, payables):
    n = _std(receivables, 252)
    d = _std(payables, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(receivables) / std(payables)
def ccc_f068_cash_conversion_cycle_volratio_payables_504d_base_v070_signal(receivables, payables):
    n = _std(receivables, 504)
    d = _std(payables, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed receivables times closeadj
def ccc_f068_cash_conversion_cycle_raw_5d_base_v071_signal(receivables, closeadj):
    result = _mean(receivables, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed receivables times closeadj
def ccc_f068_cash_conversion_cycle_raw_1008d_base_v072_signal(receivables, closeadj):
    result = _mean(receivables, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of receivables/inventory
def ccc_f068_cash_conversion_cycle_log_per_inventory_252d_base_v073_signal(receivables, inventory):
    s = _cash_conversion_cycle_scaled(receivables, inventory)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of receivables/inventory
def ccc_f068_cash_conversion_cycle_log_per_inventory_504d_base_v074_signal(receivables, inventory):
    s = _cash_conversion_cycle_scaled(receivables, inventory)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of receivables/payables
def ccc_f068_cash_conversion_cycle_log_per_payables_252d_base_v075_signal(receivables, payables):
    s = _cash_conversion_cycle_scaled(receivables, payables)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
