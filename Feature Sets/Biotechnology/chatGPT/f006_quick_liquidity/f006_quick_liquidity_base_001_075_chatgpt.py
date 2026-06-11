"""Family f006 - Inventory-excluded liquidity (Liquidity and Runway) | Sharadar tables: SF1 | fields: assetsc, inventory, liabilitiesc, cashneq | base 001-075"""
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
def _quick_liquidity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _quick_liquidity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _quick_liquidity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed assetsc times closeadj
def ql_f006_quick_liquidity_raw_21d_base_v001_signal(assetsc, closeadj):
    result = _mean(assetsc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed assetsc times closeadj
def ql_f006_quick_liquidity_raw_63d_base_v002_signal(assetsc, closeadj):
    result = _mean(assetsc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed assetsc times closeadj
def ql_f006_quick_liquidity_raw_126d_base_v003_signal(assetsc, closeadj):
    result = _mean(assetsc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed assetsc times closeadj
def ql_f006_quick_liquidity_raw_252d_base_v004_signal(assetsc, closeadj):
    result = _mean(assetsc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed assetsc times closeadj
def ql_f006_quick_liquidity_raw_504d_base_v005_signal(assetsc, closeadj):
    result = _mean(assetsc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(assetsc) times closeadj
def ql_f006_quick_liquidity_log_21d_base_v006_signal(assetsc, closeadj):
    result = _mean(_quick_liquidity_log(assetsc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(assetsc) times closeadj
def ql_f006_quick_liquidity_log_63d_base_v007_signal(assetsc, closeadj):
    result = _mean(_quick_liquidity_log(assetsc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(assetsc) times closeadj
def ql_f006_quick_liquidity_log_126d_base_v008_signal(assetsc, closeadj):
    result = _mean(_quick_liquidity_log(assetsc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(assetsc) times closeadj
def ql_f006_quick_liquidity_log_252d_base_v009_signal(assetsc, closeadj):
    result = _mean(_quick_liquidity_log(assetsc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(assetsc) times closeadj
def ql_f006_quick_liquidity_log_504d_base_v010_signal(assetsc, closeadj):
    result = _mean(_quick_liquidity_log(assetsc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/inventory mean
def ql_f006_quick_liquidity_per_inventory_63d_base_v011_signal(assetsc, inventory):
    result = _mean(_quick_liquidity_scaled(assetsc, inventory), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/inventory mean
def ql_f006_quick_liquidity_per_inventory_252d_base_v012_signal(assetsc, inventory):
    result = _mean(_quick_liquidity_scaled(assetsc, inventory), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetsc/inventory mean
def ql_f006_quick_liquidity_per_inventory_504d_base_v013_signal(assetsc, inventory):
    result = _mean(_quick_liquidity_scaled(assetsc, inventory), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/liabilitiesc mean
def ql_f006_quick_liquidity_per_liabilitiesc_63d_base_v014_signal(assetsc, liabilitiesc):
    result = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/liabilitiesc mean
def ql_f006_quick_liquidity_per_liabilitiesc_252d_base_v015_signal(assetsc, liabilitiesc):
    result = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetsc/liabilitiesc mean
def ql_f006_quick_liquidity_per_liabilitiesc_504d_base_v016_signal(assetsc, liabilitiesc):
    result = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/cashneq mean
def ql_f006_quick_liquidity_per_cashneq_63d_base_v017_signal(assetsc, cashneq):
    result = _mean(_quick_liquidity_scaled(assetsc, cashneq), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/cashneq mean
def ql_f006_quick_liquidity_per_cashneq_252d_base_v018_signal(assetsc, cashneq):
    result = _mean(_quick_liquidity_scaled(assetsc, cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetsc/cashneq mean
def ql_f006_quick_liquidity_per_cashneq_504d_base_v019_signal(assetsc, cashneq):
    result = _mean(_quick_liquidity_scaled(assetsc, cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/assets mean
def ql_f006_quick_liquidity_per_assets_63d_base_v020_signal(assetsc, assets):
    result = _mean(_quick_liquidity_scaled(assetsc, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/assets mean
def ql_f006_quick_liquidity_per_assets_252d_base_v021_signal(assetsc, assets):
    result = _mean(_quick_liquidity_scaled(assetsc, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetsc/assets mean
def ql_f006_quick_liquidity_per_assets_504d_base_v022_signal(assetsc, assets):
    result = _mean(_quick_liquidity_scaled(assetsc, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/marketcap mean
def ql_f006_quick_liquidity_per_marketcap_63d_base_v023_signal(assetsc, marketcap):
    result = _mean(_quick_liquidity_scaled(assetsc, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/marketcap mean
def ql_f006_quick_liquidity_per_marketcap_252d_base_v024_signal(assetsc, marketcap):
    result = _mean(_quick_liquidity_scaled(assetsc, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetsc/marketcap mean
def ql_f006_quick_liquidity_per_marketcap_504d_base_v025_signal(assetsc, marketcap):
    result = _mean(_quick_liquidity_scaled(assetsc, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d assetsc per share times closeadj
def ql_f006_quick_liquidity_pershare_21d_base_v026_signal(assetsc, sharesbas, closeadj):
    ps = _quick_liquidity_per_share(assetsc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc per share times closeadj
def ql_f006_quick_liquidity_pershare_63d_base_v027_signal(assetsc, sharesbas, closeadj):
    ps = _quick_liquidity_per_share(assetsc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d assetsc per share times closeadj
def ql_f006_quick_liquidity_pershare_126d_base_v028_signal(assetsc, sharesbas, closeadj):
    ps = _quick_liquidity_per_share(assetsc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc per share times closeadj
def ql_f006_quick_liquidity_pershare_252d_base_v029_signal(assetsc, sharesbas, closeadj):
    ps = _quick_liquidity_per_share(assetsc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetsc per share times closeadj
def ql_f006_quick_liquidity_pershare_504d_base_v030_signal(assetsc, sharesbas, closeadj):
    ps = _quick_liquidity_per_share(assetsc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of assetsc times closeadj
def ql_f006_quick_liquidity_std_63d_base_v031_signal(assetsc, closeadj):
    result = _std(assetsc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of assetsc times closeadj
def ql_f006_quick_liquidity_std_252d_base_v032_signal(assetsc, closeadj):
    result = _std(assetsc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of assetsc times closeadj
def ql_f006_quick_liquidity_std_504d_base_v033_signal(assetsc, closeadj):
    result = _std(assetsc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of assetsc
def ql_f006_quick_liquidity_z_252d_base_v034_signal(assetsc):
    result = _z(assetsc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of assetsc
def ql_f006_quick_liquidity_z_504d_base_v035_signal(assetsc):
    result = _z(assetsc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(assetsc)
def ql_f006_quick_liquidity_logz_252d_base_v036_signal(assetsc):
    result = _z(_quick_liquidity_log(assetsc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(assetsc)
def ql_f006_quick_liquidity_logz_504d_base_v037_signal(assetsc):
    result = _z(_quick_liquidity_log(assetsc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of assetsc^2 times closeadj
def ql_f006_quick_liquidity_sq_63d_base_v038_signal(assetsc, closeadj):
    result = _mean(assetsc * assetsc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of assetsc^2 times closeadj
def ql_f006_quick_liquidity_sq_252d_base_v039_signal(assetsc, closeadj):
    result = _mean(assetsc * assetsc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(assetsc) times closeadj
def ql_f006_quick_liquidity_sign_21d_base_v040_signal(assetsc, closeadj):
    result = _mean(np.sign(assetsc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(assetsc) times closeadj
def ql_f006_quick_liquidity_sign_63d_base_v041_signal(assetsc, closeadj):
    result = _mean(np.sign(assetsc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(assetsc) times closeadj
def ql_f006_quick_liquidity_sign_252d_base_v042_signal(assetsc, closeadj):
    result = _mean(np.sign(assetsc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/opex mean
def ql_f006_quick_liquidity_per_opex_63d_base_v043_signal(assetsc, opex):
    result = _mean(_quick_liquidity_scaled(assetsc, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/opex mean
def ql_f006_quick_liquidity_per_opex_252d_base_v044_signal(assetsc, opex):
    result = _mean(_quick_liquidity_scaled(assetsc, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/ebitda mean
def ql_f006_quick_liquidity_per_ebitda_63d_base_v045_signal(assetsc, ebitda):
    result = _mean(_quick_liquidity_scaled(assetsc, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/ebitda mean
def ql_f006_quick_liquidity_per_ebitda_252d_base_v046_signal(assetsc, ebitda):
    result = _mean(_quick_liquidity_scaled(assetsc, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/capex mean
def ql_f006_quick_liquidity_per_capex_63d_base_v047_signal(assetsc, capex):
    result = _mean(_quick_liquidity_scaled(assetsc, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/capex mean
def ql_f006_quick_liquidity_per_capex_252d_base_v048_signal(assetsc, capex):
    result = _mean(_quick_liquidity_scaled(assetsc, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetsc/liabilities mean
def ql_f006_quick_liquidity_per_liabilities_63d_base_v049_signal(assetsc, liabilities):
    result = _mean(_quick_liquidity_scaled(assetsc, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetsc/liabilities mean
def ql_f006_quick_liquidity_per_liabilities_252d_base_v050_signal(assetsc, liabilities):
    result = _mean(_quick_liquidity_scaled(assetsc, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# assetsc relative to 252d max times closeadj
def ql_f006_quick_liquidity_relmax_252d_base_v051_signal(assetsc, closeadj):
    peak = assetsc.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (assetsc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetsc relative to 504d max times closeadj
def ql_f006_quick_liquidity_relmax_504d_base_v052_signal(assetsc, closeadj):
    peak = assetsc.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (assetsc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetsc relative to 252d min times closeadj
def ql_f006_quick_liquidity_relmin_252d_base_v053_signal(assetsc, closeadj):
    trough = assetsc.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (assetsc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetsc relative to 504d min times closeadj
def ql_f006_quick_liquidity_relmin_504d_base_v054_signal(assetsc, closeadj):
    trough = assetsc.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (assetsc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of assetsc times closeadj
def ql_f006_quick_liquidity_pct_21d_base_v055_signal(assetsc, closeadj):
    result = _pct_change(assetsc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of assetsc times closeadj
def ql_f006_quick_liquidity_pct_63d_base_v056_signal(assetsc, closeadj):
    result = _pct_change(assetsc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of assetsc times closeadj
def ql_f006_quick_liquidity_pct_252d_base_v057_signal(assetsc, closeadj):
    result = _pct_change(assetsc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of assetsc times closeadj
def ql_f006_quick_liquidity_sum_63d_base_v058_signal(assetsc, closeadj):
    result = assetsc.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of assetsc times closeadj
def ql_f006_quick_liquidity_sum_252d_base_v059_signal(assetsc, closeadj):
    result = assetsc.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of assetsc times closeadj
def ql_f006_quick_liquidity_sum_504d_base_v060_signal(assetsc, closeadj):
    result = assetsc.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetsc(63d) / smoothed inventory(252d) x closeadj
def ql_f006_quick_liquidity_rom_inventory_252_63d_base_v061_signal(assetsc, inventory, closeadj):
    n = _mean(assetsc, 63)
    d = _mean(inventory, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetsc(126d) / smoothed inventory(504d) x closeadj
def ql_f006_quick_liquidity_rom_inventory_504_126d_base_v062_signal(assetsc, inventory, closeadj):
    n = _mean(assetsc, 126)
    d = _mean(inventory, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetsc(63d) / smoothed liabilitiesc(252d) x closeadj
def ql_f006_quick_liquidity_rom_liabilitiesc_252_63d_base_v063_signal(assetsc, liabilitiesc, closeadj):
    n = _mean(assetsc, 63)
    d = _mean(liabilitiesc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetsc(126d) / smoothed liabilitiesc(504d) x closeadj
def ql_f006_quick_liquidity_rom_liabilitiesc_504_126d_base_v064_signal(assetsc, liabilitiesc, closeadj):
    n = _mean(assetsc, 126)
    d = _mean(liabilitiesc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetsc(63d) / smoothed cashneq(252d) x closeadj
def ql_f006_quick_liquidity_rom_cashneq_252_63d_base_v065_signal(assetsc, cashneq, closeadj):
    n = _mean(assetsc, 63)
    d = _mean(cashneq, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetsc(126d) / smoothed cashneq(504d) x closeadj
def ql_f006_quick_liquidity_rom_cashneq_504_126d_base_v066_signal(assetsc, cashneq, closeadj):
    n = _mean(assetsc, 126)
    d = _mean(cashneq, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(assetsc) / std(inventory)
def ql_f006_quick_liquidity_volratio_inventory_252d_base_v067_signal(assetsc, inventory):
    n = _std(assetsc, 252)
    d = _std(inventory, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(assetsc) / std(inventory)
def ql_f006_quick_liquidity_volratio_inventory_504d_base_v068_signal(assetsc, inventory):
    n = _std(assetsc, 504)
    d = _std(inventory, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(assetsc) / std(liabilitiesc)
def ql_f006_quick_liquidity_volratio_liabilitiesc_252d_base_v069_signal(assetsc, liabilitiesc):
    n = _std(assetsc, 252)
    d = _std(liabilitiesc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(assetsc) / std(liabilitiesc)
def ql_f006_quick_liquidity_volratio_liabilitiesc_504d_base_v070_signal(assetsc, liabilitiesc):
    n = _std(assetsc, 504)
    d = _std(liabilitiesc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed assetsc times closeadj
def ql_f006_quick_liquidity_raw_5d_base_v071_signal(assetsc, closeadj):
    result = _mean(assetsc, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed assetsc times closeadj
def ql_f006_quick_liquidity_raw_1008d_base_v072_signal(assetsc, closeadj):
    result = _mean(assetsc, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assetsc/inventory
def ql_f006_quick_liquidity_log_per_inventory_252d_base_v073_signal(assetsc, inventory):
    s = _quick_liquidity_scaled(assetsc, inventory)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of assetsc/inventory
def ql_f006_quick_liquidity_log_per_inventory_504d_base_v074_signal(assetsc, inventory):
    s = _quick_liquidity_scaled(assetsc, inventory)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assetsc/liabilitiesc
def ql_f006_quick_liquidity_log_per_liabilitiesc_252d_base_v075_signal(assetsc, liabilitiesc):
    s = _quick_liquidity_scaled(assetsc, liabilitiesc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
