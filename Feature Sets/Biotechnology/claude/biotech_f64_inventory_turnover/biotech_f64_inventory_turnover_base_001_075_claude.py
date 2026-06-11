"""Family f64 - Inventory turnover / days  (K_WorkingCapital) | base 001-075"""
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
def _inventory_turnover_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _inventory_turnover_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _inventory_turnover_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed inventory times closeadj
def it_f64_inventory_turnover_raw_21d_base_v001_signal(inventory, closeadj):
    result = _mean(inventory, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed inventory times closeadj
def it_f64_inventory_turnover_raw_63d_base_v002_signal(inventory, closeadj):
    result = _mean(inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed inventory times closeadj
def it_f64_inventory_turnover_raw_126d_base_v003_signal(inventory, closeadj):
    result = _mean(inventory, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed inventory times closeadj
def it_f64_inventory_turnover_raw_252d_base_v004_signal(inventory, closeadj):
    result = _mean(inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed inventory times closeadj
def it_f64_inventory_turnover_raw_504d_base_v005_signal(inventory, closeadj):
    result = _mean(inventory, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(inventory) times closeadj
def it_f64_inventory_turnover_log_21d_base_v006_signal(inventory, closeadj):
    result = _mean(_inventory_turnover_log(inventory), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(inventory) times closeadj
def it_f64_inventory_turnover_log_63d_base_v007_signal(inventory, closeadj):
    result = _mean(_inventory_turnover_log(inventory), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(inventory) times closeadj
def it_f64_inventory_turnover_log_126d_base_v008_signal(inventory, closeadj):
    result = _mean(_inventory_turnover_log(inventory), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(inventory) times closeadj
def it_f64_inventory_turnover_log_252d_base_v009_signal(inventory, closeadj):
    result = _mean(_inventory_turnover_log(inventory), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(inventory) times closeadj
def it_f64_inventory_turnover_log_504d_base_v010_signal(inventory, closeadj):
    result = _mean(_inventory_turnover_log(inventory), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/assets mean
def it_f64_inventory_turnover_per_assets_63d_base_v011_signal(inventory, assets):
    result = _mean(_inventory_turnover_scaled(inventory, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/assets mean
def it_f64_inventory_turnover_per_assets_252d_base_v012_signal(inventory, assets):
    result = _mean(_inventory_turnover_scaled(inventory, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/assets mean
def it_f64_inventory_turnover_per_assets_504d_base_v013_signal(inventory, assets):
    result = _mean(_inventory_turnover_scaled(inventory, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/marketcap mean
def it_f64_inventory_turnover_per_marketcap_63d_base_v014_signal(inventory, marketcap):
    result = _mean(_inventory_turnover_scaled(inventory, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/marketcap mean
def it_f64_inventory_turnover_per_marketcap_252d_base_v015_signal(inventory, marketcap):
    result = _mean(_inventory_turnover_scaled(inventory, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/marketcap mean
def it_f64_inventory_turnover_per_marketcap_504d_base_v016_signal(inventory, marketcap):
    result = _mean(_inventory_turnover_scaled(inventory, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/equity mean
def it_f64_inventory_turnover_per_equity_63d_base_v017_signal(inventory, equity):
    result = _mean(_inventory_turnover_scaled(inventory, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/equity mean
def it_f64_inventory_turnover_per_equity_252d_base_v018_signal(inventory, equity):
    result = _mean(_inventory_turnover_scaled(inventory, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/equity mean
def it_f64_inventory_turnover_per_equity_504d_base_v019_signal(inventory, equity):
    result = _mean(_inventory_turnover_scaled(inventory, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/debt mean
def it_f64_inventory_turnover_per_debt_63d_base_v020_signal(inventory, debt):
    result = _mean(_inventory_turnover_scaled(inventory, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/debt mean
def it_f64_inventory_turnover_per_debt_252d_base_v021_signal(inventory, debt):
    result = _mean(_inventory_turnover_scaled(inventory, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/debt mean
def it_f64_inventory_turnover_per_debt_504d_base_v022_signal(inventory, debt):
    result = _mean(_inventory_turnover_scaled(inventory, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/revenue mean
def it_f64_inventory_turnover_per_revenue_63d_base_v023_signal(inventory, revenue):
    result = _mean(_inventory_turnover_scaled(inventory, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/revenue mean
def it_f64_inventory_turnover_per_revenue_252d_base_v024_signal(inventory, revenue):
    result = _mean(_inventory_turnover_scaled(inventory, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/revenue mean
def it_f64_inventory_turnover_per_revenue_504d_base_v025_signal(inventory, revenue):
    result = _mean(_inventory_turnover_scaled(inventory, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d inventory per share times closeadj
def it_f64_inventory_turnover_pershare_21d_base_v026_signal(inventory, sharesbas, closeadj):
    ps = _inventory_turnover_per_share(inventory, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory per share times closeadj
def it_f64_inventory_turnover_pershare_63d_base_v027_signal(inventory, sharesbas, closeadj):
    ps = _inventory_turnover_per_share(inventory, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d inventory per share times closeadj
def it_f64_inventory_turnover_pershare_126d_base_v028_signal(inventory, sharesbas, closeadj):
    ps = _inventory_turnover_per_share(inventory, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory per share times closeadj
def it_f64_inventory_turnover_pershare_252d_base_v029_signal(inventory, sharesbas, closeadj):
    ps = _inventory_turnover_per_share(inventory, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory per share times closeadj
def it_f64_inventory_turnover_pershare_504d_base_v030_signal(inventory, sharesbas, closeadj):
    ps = _inventory_turnover_per_share(inventory, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of inventory times closeadj
def it_f64_inventory_turnover_std_63d_base_v031_signal(inventory, closeadj):
    result = _std(inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of inventory times closeadj
def it_f64_inventory_turnover_std_252d_base_v032_signal(inventory, closeadj):
    result = _std(inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of inventory times closeadj
def it_f64_inventory_turnover_std_504d_base_v033_signal(inventory, closeadj):
    result = _std(inventory, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of inventory
def it_f64_inventory_turnover_z_252d_base_v034_signal(inventory):
    result = _z(inventory, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of inventory
def it_f64_inventory_turnover_z_504d_base_v035_signal(inventory):
    result = _z(inventory, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(inventory)
def it_f64_inventory_turnover_logz_252d_base_v036_signal(inventory):
    result = _z(_inventory_turnover_log(inventory), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(inventory)
def it_f64_inventory_turnover_logz_504d_base_v037_signal(inventory):
    result = _z(_inventory_turnover_log(inventory), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of inventory^2 times closeadj
def it_f64_inventory_turnover_sq_63d_base_v038_signal(inventory, closeadj):
    result = _mean(inventory * inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of inventory^2 times closeadj
def it_f64_inventory_turnover_sq_252d_base_v039_signal(inventory, closeadj):
    result = _mean(inventory * inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(inventory) times closeadj
def it_f64_inventory_turnover_sign_21d_base_v040_signal(inventory, closeadj):
    result = _mean(np.sign(inventory), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(inventory) times closeadj
def it_f64_inventory_turnover_sign_63d_base_v041_signal(inventory, closeadj):
    result = _mean(np.sign(inventory), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(inventory) times closeadj
def it_f64_inventory_turnover_sign_252d_base_v042_signal(inventory, closeadj):
    result = _mean(np.sign(inventory), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/opex mean
def it_f64_inventory_turnover_per_opex_63d_base_v043_signal(inventory, opex):
    result = _mean(_inventory_turnover_scaled(inventory, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/opex mean
def it_f64_inventory_turnover_per_opex_252d_base_v044_signal(inventory, opex):
    result = _mean(_inventory_turnover_scaled(inventory, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/ebitda mean
def it_f64_inventory_turnover_per_ebitda_63d_base_v045_signal(inventory, ebitda):
    result = _mean(_inventory_turnover_scaled(inventory, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/ebitda mean
def it_f64_inventory_turnover_per_ebitda_252d_base_v046_signal(inventory, ebitda):
    result = _mean(_inventory_turnover_scaled(inventory, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/capex mean
def it_f64_inventory_turnover_per_capex_63d_base_v047_signal(inventory, capex):
    result = _mean(_inventory_turnover_scaled(inventory, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/capex mean
def it_f64_inventory_turnover_per_capex_252d_base_v048_signal(inventory, capex):
    result = _mean(_inventory_turnover_scaled(inventory, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/liabilities mean
def it_f64_inventory_turnover_per_liabilities_63d_base_v049_signal(inventory, liabilities):
    result = _mean(_inventory_turnover_scaled(inventory, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/liabilities mean
def it_f64_inventory_turnover_per_liabilities_252d_base_v050_signal(inventory, liabilities):
    result = _mean(_inventory_turnover_scaled(inventory, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 252d max times closeadj
def it_f64_inventory_turnover_relmax_252d_base_v051_signal(inventory, closeadj):
    peak = inventory.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (inventory / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 504d max times closeadj
def it_f64_inventory_turnover_relmax_504d_base_v052_signal(inventory, closeadj):
    peak = inventory.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (inventory / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 252d min times closeadj
def it_f64_inventory_turnover_relmin_252d_base_v053_signal(inventory, closeadj):
    trough = inventory.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (inventory / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 504d min times closeadj
def it_f64_inventory_turnover_relmin_504d_base_v054_signal(inventory, closeadj):
    trough = inventory.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (inventory / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of inventory times closeadj
def it_f64_inventory_turnover_pct_21d_base_v055_signal(inventory, closeadj):
    result = _pct_change(inventory, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of inventory times closeadj
def it_f64_inventory_turnover_pct_63d_base_v056_signal(inventory, closeadj):
    result = _pct_change(inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of inventory times closeadj
def it_f64_inventory_turnover_pct_252d_base_v057_signal(inventory, closeadj):
    result = _pct_change(inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of inventory times closeadj
def it_f64_inventory_turnover_sum_63d_base_v058_signal(inventory, closeadj):
    result = inventory.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of inventory times closeadj
def it_f64_inventory_turnover_sum_252d_base_v059_signal(inventory, closeadj):
    result = inventory.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of inventory times closeadj
def it_f64_inventory_turnover_sum_504d_base_v060_signal(inventory, closeadj):
    result = inventory.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(63d) / smoothed assets(252d) x closeadj
def it_f64_inventory_turnover_rom_assets_252_63d_base_v061_signal(inventory, assets, closeadj):
    n = _mean(inventory, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(126d) / smoothed assets(504d) x closeadj
def it_f64_inventory_turnover_rom_assets_504_126d_base_v062_signal(inventory, assets, closeadj):
    n = _mean(inventory, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(63d) / smoothed marketcap(252d) x closeadj
def it_f64_inventory_turnover_rom_marketcap_252_63d_base_v063_signal(inventory, marketcap, closeadj):
    n = _mean(inventory, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(126d) / smoothed marketcap(504d) x closeadj
def it_f64_inventory_turnover_rom_marketcap_504_126d_base_v064_signal(inventory, marketcap, closeadj):
    n = _mean(inventory, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(63d) / smoothed equity(252d) x closeadj
def it_f64_inventory_turnover_rom_equity_252_63d_base_v065_signal(inventory, equity, closeadj):
    n = _mean(inventory, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(126d) / smoothed equity(504d) x closeadj
def it_f64_inventory_turnover_rom_equity_504_126d_base_v066_signal(inventory, equity, closeadj):
    n = _mean(inventory, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(inventory) / std(assets)
def it_f64_inventory_turnover_volratio_assets_252d_base_v067_signal(inventory, assets):
    n = _std(inventory, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(inventory) / std(assets)
def it_f64_inventory_turnover_volratio_assets_504d_base_v068_signal(inventory, assets):
    n = _std(inventory, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(inventory) / std(marketcap)
def it_f64_inventory_turnover_volratio_marketcap_252d_base_v069_signal(inventory, marketcap):
    n = _std(inventory, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(inventory) / std(marketcap)
def it_f64_inventory_turnover_volratio_marketcap_504d_base_v070_signal(inventory, marketcap):
    n = _std(inventory, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed inventory times closeadj
def it_f64_inventory_turnover_raw_5d_base_v071_signal(inventory, closeadj):
    result = _mean(inventory, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed inventory times closeadj
def it_f64_inventory_turnover_raw_1008d_base_v072_signal(inventory, closeadj):
    result = _mean(inventory, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of inventory/assets
def it_f64_inventory_turnover_log_per_assets_252d_base_v073_signal(inventory, assets):
    s = _inventory_turnover_scaled(inventory, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of inventory/assets
def it_f64_inventory_turnover_log_per_assets_504d_base_v074_signal(inventory, assets):
    s = _inventory_turnover_scaled(inventory, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of inventory/marketcap
def it_f64_inventory_turnover_log_per_marketcap_252d_base_v075_signal(inventory, marketcap):
    s = _inventory_turnover_scaled(inventory, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
