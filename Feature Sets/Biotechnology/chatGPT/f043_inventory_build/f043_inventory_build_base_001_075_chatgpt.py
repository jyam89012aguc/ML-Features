"""Family f043 - Inventory build and launch readiness (Balance Sheet Composition) | Sharadar tables: SF1 | fields: inventory, revenue, cor, assets | base 001-075"""
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
def _inventory_build_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _inventory_build_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _inventory_build_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed inventory times closeadj
def ib_f043_inventory_build_raw_21d_base_v001_signal(inventory, closeadj):
    result = _mean(inventory, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed inventory times closeadj
def ib_f043_inventory_build_raw_63d_base_v002_signal(inventory, closeadj):
    result = _mean(inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed inventory times closeadj
def ib_f043_inventory_build_raw_126d_base_v003_signal(inventory, closeadj):
    result = _mean(inventory, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed inventory times closeadj
def ib_f043_inventory_build_raw_252d_base_v004_signal(inventory, closeadj):
    result = _mean(inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed inventory times closeadj
def ib_f043_inventory_build_raw_504d_base_v005_signal(inventory, closeadj):
    result = _mean(inventory, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(inventory) times closeadj
def ib_f043_inventory_build_log_21d_base_v006_signal(inventory, closeadj):
    result = _mean(_inventory_build_log(inventory), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(inventory) times closeadj
def ib_f043_inventory_build_log_63d_base_v007_signal(inventory, closeadj):
    result = _mean(_inventory_build_log(inventory), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(inventory) times closeadj
def ib_f043_inventory_build_log_126d_base_v008_signal(inventory, closeadj):
    result = _mean(_inventory_build_log(inventory), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(inventory) times closeadj
def ib_f043_inventory_build_log_252d_base_v009_signal(inventory, closeadj):
    result = _mean(_inventory_build_log(inventory), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(inventory) times closeadj
def ib_f043_inventory_build_log_504d_base_v010_signal(inventory, closeadj):
    result = _mean(_inventory_build_log(inventory), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/revenue mean
def ib_f043_inventory_build_per_revenue_63d_base_v011_signal(inventory, revenue):
    result = _mean(_inventory_build_scaled(inventory, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/revenue mean
def ib_f043_inventory_build_per_revenue_252d_base_v012_signal(inventory, revenue):
    result = _mean(_inventory_build_scaled(inventory, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/revenue mean
def ib_f043_inventory_build_per_revenue_504d_base_v013_signal(inventory, revenue):
    result = _mean(_inventory_build_scaled(inventory, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/cor mean
def ib_f043_inventory_build_per_cor_63d_base_v014_signal(inventory, cor):
    result = _mean(_inventory_build_scaled(inventory, cor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/cor mean
def ib_f043_inventory_build_per_cor_252d_base_v015_signal(inventory, cor):
    result = _mean(_inventory_build_scaled(inventory, cor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/cor mean
def ib_f043_inventory_build_per_cor_504d_base_v016_signal(inventory, cor):
    result = _mean(_inventory_build_scaled(inventory, cor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/assets mean
def ib_f043_inventory_build_per_assets_63d_base_v017_signal(inventory, assets):
    result = _mean(_inventory_build_scaled(inventory, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/assets mean
def ib_f043_inventory_build_per_assets_252d_base_v018_signal(inventory, assets):
    result = _mean(_inventory_build_scaled(inventory, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/assets mean
def ib_f043_inventory_build_per_assets_504d_base_v019_signal(inventory, assets):
    result = _mean(_inventory_build_scaled(inventory, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/marketcap mean
def ib_f043_inventory_build_per_marketcap_63d_base_v020_signal(inventory, marketcap):
    result = _mean(_inventory_build_scaled(inventory, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/marketcap mean
def ib_f043_inventory_build_per_marketcap_252d_base_v021_signal(inventory, marketcap):
    result = _mean(_inventory_build_scaled(inventory, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/marketcap mean
def ib_f043_inventory_build_per_marketcap_504d_base_v022_signal(inventory, marketcap):
    result = _mean(_inventory_build_scaled(inventory, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/equity mean
def ib_f043_inventory_build_per_equity_63d_base_v023_signal(inventory, equity):
    result = _mean(_inventory_build_scaled(inventory, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/equity mean
def ib_f043_inventory_build_per_equity_252d_base_v024_signal(inventory, equity):
    result = _mean(_inventory_build_scaled(inventory, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory/equity mean
def ib_f043_inventory_build_per_equity_504d_base_v025_signal(inventory, equity):
    result = _mean(_inventory_build_scaled(inventory, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d inventory per share times closeadj
def ib_f043_inventory_build_pershare_21d_base_v026_signal(inventory, sharesbas, closeadj):
    ps = _inventory_build_per_share(inventory, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory per share times closeadj
def ib_f043_inventory_build_pershare_63d_base_v027_signal(inventory, sharesbas, closeadj):
    ps = _inventory_build_per_share(inventory, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d inventory per share times closeadj
def ib_f043_inventory_build_pershare_126d_base_v028_signal(inventory, sharesbas, closeadj):
    ps = _inventory_build_per_share(inventory, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory per share times closeadj
def ib_f043_inventory_build_pershare_252d_base_v029_signal(inventory, sharesbas, closeadj):
    ps = _inventory_build_per_share(inventory, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d inventory per share times closeadj
def ib_f043_inventory_build_pershare_504d_base_v030_signal(inventory, sharesbas, closeadj):
    ps = _inventory_build_per_share(inventory, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of inventory times closeadj
def ib_f043_inventory_build_std_63d_base_v031_signal(inventory, closeadj):
    result = _std(inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of inventory times closeadj
def ib_f043_inventory_build_std_252d_base_v032_signal(inventory, closeadj):
    result = _std(inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of inventory times closeadj
def ib_f043_inventory_build_std_504d_base_v033_signal(inventory, closeadj):
    result = _std(inventory, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of inventory
def ib_f043_inventory_build_z_252d_base_v034_signal(inventory):
    result = _z(inventory, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of inventory
def ib_f043_inventory_build_z_504d_base_v035_signal(inventory):
    result = _z(inventory, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(inventory)
def ib_f043_inventory_build_logz_252d_base_v036_signal(inventory):
    result = _z(_inventory_build_log(inventory), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(inventory)
def ib_f043_inventory_build_logz_504d_base_v037_signal(inventory):
    result = _z(_inventory_build_log(inventory), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of inventory^2 times closeadj
def ib_f043_inventory_build_sq_63d_base_v038_signal(inventory, closeadj):
    result = _mean(inventory * inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of inventory^2 times closeadj
def ib_f043_inventory_build_sq_252d_base_v039_signal(inventory, closeadj):
    result = _mean(inventory * inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(inventory) times closeadj
def ib_f043_inventory_build_sign_21d_base_v040_signal(inventory, closeadj):
    result = _mean(np.sign(inventory), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(inventory) times closeadj
def ib_f043_inventory_build_sign_63d_base_v041_signal(inventory, closeadj):
    result = _mean(np.sign(inventory), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(inventory) times closeadj
def ib_f043_inventory_build_sign_252d_base_v042_signal(inventory, closeadj):
    result = _mean(np.sign(inventory), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/opex mean
def ib_f043_inventory_build_per_opex_63d_base_v043_signal(inventory, opex):
    result = _mean(_inventory_build_scaled(inventory, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/opex mean
def ib_f043_inventory_build_per_opex_252d_base_v044_signal(inventory, opex):
    result = _mean(_inventory_build_scaled(inventory, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/ebitda mean
def ib_f043_inventory_build_per_ebitda_63d_base_v045_signal(inventory, ebitda):
    result = _mean(_inventory_build_scaled(inventory, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/ebitda mean
def ib_f043_inventory_build_per_ebitda_252d_base_v046_signal(inventory, ebitda):
    result = _mean(_inventory_build_scaled(inventory, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/capex mean
def ib_f043_inventory_build_per_capex_63d_base_v047_signal(inventory, capex):
    result = _mean(_inventory_build_scaled(inventory, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/capex mean
def ib_f043_inventory_build_per_capex_252d_base_v048_signal(inventory, capex):
    result = _mean(_inventory_build_scaled(inventory, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d inventory/liabilities mean
def ib_f043_inventory_build_per_liabilities_63d_base_v049_signal(inventory, liabilities):
    result = _mean(_inventory_build_scaled(inventory, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d inventory/liabilities mean
def ib_f043_inventory_build_per_liabilities_252d_base_v050_signal(inventory, liabilities):
    result = _mean(_inventory_build_scaled(inventory, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 252d max times closeadj
def ib_f043_inventory_build_relmax_252d_base_v051_signal(inventory, closeadj):
    peak = inventory.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (inventory / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 504d max times closeadj
def ib_f043_inventory_build_relmax_504d_base_v052_signal(inventory, closeadj):
    peak = inventory.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (inventory / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 252d min times closeadj
def ib_f043_inventory_build_relmin_252d_base_v053_signal(inventory, closeadj):
    trough = inventory.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (inventory / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 504d min times closeadj
def ib_f043_inventory_build_relmin_504d_base_v054_signal(inventory, closeadj):
    trough = inventory.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (inventory / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of inventory times closeadj
def ib_f043_inventory_build_pct_21d_base_v055_signal(inventory, closeadj):
    result = _pct_change(inventory, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of inventory times closeadj
def ib_f043_inventory_build_pct_63d_base_v056_signal(inventory, closeadj):
    result = _pct_change(inventory, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of inventory times closeadj
def ib_f043_inventory_build_pct_252d_base_v057_signal(inventory, closeadj):
    result = _pct_change(inventory, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of inventory times closeadj
def ib_f043_inventory_build_sum_63d_base_v058_signal(inventory, closeadj):
    result = inventory.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of inventory times closeadj
def ib_f043_inventory_build_sum_252d_base_v059_signal(inventory, closeadj):
    result = inventory.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of inventory times closeadj
def ib_f043_inventory_build_sum_504d_base_v060_signal(inventory, closeadj):
    result = inventory.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(63d) / smoothed revenue(252d) x closeadj
def ib_f043_inventory_build_rom_revenue_252_63d_base_v061_signal(inventory, revenue, closeadj):
    n = _mean(inventory, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(126d) / smoothed revenue(504d) x closeadj
def ib_f043_inventory_build_rom_revenue_504_126d_base_v062_signal(inventory, revenue, closeadj):
    n = _mean(inventory, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(63d) / smoothed cor(252d) x closeadj
def ib_f043_inventory_build_rom_cor_252_63d_base_v063_signal(inventory, cor, closeadj):
    n = _mean(inventory, 63)
    d = _mean(cor, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(126d) / smoothed cor(504d) x closeadj
def ib_f043_inventory_build_rom_cor_504_126d_base_v064_signal(inventory, cor, closeadj):
    n = _mean(inventory, 126)
    d = _mean(cor, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(63d) / smoothed assets(252d) x closeadj
def ib_f043_inventory_build_rom_assets_252_63d_base_v065_signal(inventory, assets, closeadj):
    n = _mean(inventory, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed inventory(126d) / smoothed assets(504d) x closeadj
def ib_f043_inventory_build_rom_assets_504_126d_base_v066_signal(inventory, assets, closeadj):
    n = _mean(inventory, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(inventory) / std(revenue)
def ib_f043_inventory_build_volratio_revenue_252d_base_v067_signal(inventory, revenue):
    n = _std(inventory, 252)
    d = _std(revenue, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(inventory) / std(revenue)
def ib_f043_inventory_build_volratio_revenue_504d_base_v068_signal(inventory, revenue):
    n = _std(inventory, 504)
    d = _std(revenue, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(inventory) / std(cor)
def ib_f043_inventory_build_volratio_cor_252d_base_v069_signal(inventory, cor):
    n = _std(inventory, 252)
    d = _std(cor, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(inventory) / std(cor)
def ib_f043_inventory_build_volratio_cor_504d_base_v070_signal(inventory, cor):
    n = _std(inventory, 504)
    d = _std(cor, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed inventory times closeadj
def ib_f043_inventory_build_raw_5d_base_v071_signal(inventory, closeadj):
    result = _mean(inventory, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed inventory times closeadj
def ib_f043_inventory_build_raw_1008d_base_v072_signal(inventory, closeadj):
    result = _mean(inventory, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of inventory/revenue
def ib_f043_inventory_build_log_per_revenue_252d_base_v073_signal(inventory, revenue):
    s = _inventory_build_scaled(inventory, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of inventory/revenue
def ib_f043_inventory_build_log_per_revenue_504d_base_v074_signal(inventory, revenue):
    s = _inventory_build_scaled(inventory, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of inventory/cor
def ib_f043_inventory_build_log_per_cor_252d_base_v075_signal(inventory, cor):
    s = _inventory_build_scaled(inventory, cor)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
