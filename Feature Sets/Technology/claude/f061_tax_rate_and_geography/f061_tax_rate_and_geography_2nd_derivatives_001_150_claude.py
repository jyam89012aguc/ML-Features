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


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f061_eff_tax(taxexp, ebt):
    return taxexp / ebt.replace(0, np.nan).abs()


# 21d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slope_21d_2d_v001_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slope_63d_2d_v002_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slope_126d_2d_v003_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slope_252d_2d_v004_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_slope_504d_2d_v005_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slope_21d_2d_v006_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slope_63d_2d_v007_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slope_126d_2d_v008_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slope_252d_2d_v009_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_slope_504d_2d_v010_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slope_21d_2d_v011_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slope_63d_2d_v012_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slope_126d_2d_v013_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slope_252d_2d_v014_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_slope_504d_2d_v015_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slope_21d_2d_v016_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slope_63d_2d_v017_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slope_126d_2d_v018_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slope_252d_2d_v019_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_slope_504d_2d_v020_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slope_21d_2d_v021_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slope_63d_2d_v022_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slope_126d_2d_v023_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slope_252d_2d_v024_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_slope_504d_2d_v025_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slope_21d_2d_v026_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slope_63d_2d_v027_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slope_126d_2d_v028_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slope_252d_2d_v029_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_slope_504d_2d_v030_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slope_21d_2d_v031_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slope_63d_2d_v032_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slope_126d_2d_v033_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slope_252d_2d_v034_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_slope_504d_2d_v035_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sm21_sl21_2d_v036_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sm63_sl21_2d_v037_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sm63_sl63_2d_v038_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sm252_sl63_2d_v039_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sm252_sl126_2d_v040_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sm21_sl21_2d_v041_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sm63_sl21_2d_v042_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sm63_sl63_2d_v043_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sm252_sl63_2d_v044_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sm252_sl126_2d_v045_signal(taxexp, ebt, closeadj):
    base = _mean(_f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sm21_sl21_2d_v046_signal(taxassets, assets, closeadj):
    base = _mean(taxassets / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sm63_sl21_2d_v047_signal(taxassets, assets, closeadj):
    base = _mean(taxassets / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sm63_sl63_2d_v048_signal(taxassets, assets, closeadj):
    base = _mean(taxassets / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sm252_sl63_2d_v049_signal(taxassets, assets, closeadj):
    base = _mean(taxassets / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sm252_sl126_2d_v050_signal(taxassets, assets, closeadj):
    base = _mean(taxassets / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sm21_sl21_2d_v051_signal(taxliabilities, liabilities, closeadj):
    base = _mean(taxliabilities / liabilities.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sm63_sl21_2d_v052_signal(taxliabilities, liabilities, closeadj):
    base = _mean(taxliabilities / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sm63_sl63_2d_v053_signal(taxliabilities, liabilities, closeadj):
    base = _mean(taxliabilities / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sm252_sl63_2d_v054_signal(taxliabilities, liabilities, closeadj):
    base = _mean(taxliabilities / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sm252_sl126_2d_v055_signal(taxliabilities, liabilities, closeadj):
    base = _mean(taxliabilities / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sm21_sl21_2d_v056_signal(taxassets, taxliabilities, closeadj):
    base = _mean(taxassets - taxliabilities, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sm63_sl21_2d_v057_signal(taxassets, taxliabilities, closeadj):
    base = _mean(taxassets - taxliabilities, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sm63_sl63_2d_v058_signal(taxassets, taxliabilities, closeadj):
    base = _mean(taxassets - taxliabilities, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sm252_sl63_2d_v059_signal(taxassets, taxliabilities, closeadj):
    base = _mean(taxassets - taxliabilities, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sm252_sl126_2d_v060_signal(taxassets, taxliabilities, closeadj):
    base = _mean(taxassets - taxliabilities, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sm21_sl21_2d_v061_signal(taxexp, revenue, closeadj):
    base = _mean(taxexp / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sm63_sl21_2d_v062_signal(taxexp, revenue, closeadj):
    base = _mean(taxexp / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sm63_sl63_2d_v063_signal(taxexp, revenue, closeadj):
    base = _mean(taxexp / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sm252_sl63_2d_v064_signal(taxexp, revenue, closeadj):
    base = _mean(taxexp / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sm252_sl126_2d_v065_signal(taxexp, revenue, closeadj):
    base = _mean(taxexp / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sm21_sl21_2d_v066_signal(taxexp, closeadj):
    base = _mean(taxexp.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sm63_sl21_2d_v067_signal(taxexp, closeadj):
    base = _mean(taxexp.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sm63_sl63_2d_v068_signal(taxexp, closeadj):
    base = _mean(taxexp.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sm252_sl63_2d_v069_signal(taxexp, closeadj):
    base = _mean(taxexp.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sm252_sl126_2d_v070_signal(taxexp, closeadj):
    base = _mean(taxexp.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_pctslope_21d_2d_v071_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_pctslope_63d_2d_v072_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_pctslope_252d_2d_v073_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_pctslope_21d_2d_v074_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_pctslope_63d_2d_v075_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_pctslope_252d_2d_v076_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_pctslope_21d_2d_v077_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_pctslope_63d_2d_v078_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_pctslope_252d_2d_v079_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_pctslope_21d_2d_v080_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_pctslope_63d_2d_v081_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_pctslope_252d_2d_v082_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_pctslope_21d_2d_v083_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_pctslope_63d_2d_v084_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_pctslope_252d_2d_v085_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_pctslope_21d_2d_v086_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_pctslope_63d_2d_v087_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_pctslope_252d_2d_v088_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_pctslope_21d_2d_v089_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_pctslope_63d_2d_v090_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_pctslope_252d_2d_v091_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sgnslope_21d_2d_v092_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sgnslope_63d_2d_v093_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_sgnslope_252d_2d_v094_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sgnslope_21d_2d_v095_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sgnslope_63d_2d_v096_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_sgnslope_252d_2d_v097_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sgnslope_21d_2d_v098_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sgnslope_63d_2d_v099_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_sgnslope_252d_2d_v100_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sgnslope_21d_2d_v101_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sgnslope_63d_2d_v102_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_sgnslope_252d_2d_v103_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sgnslope_21d_2d_v104_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sgnslope_63d_2d_v105_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_sgnslope_252d_2d_v106_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sgnslope_21d_2d_v107_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sgnslope_63d_2d_v108_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_sgnslope_252d_2d_v109_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sgnslope_21d_2d_v110_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sgnslope_63d_2d_v111_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_sgnslope_252d_2d_v112_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_logmagslope_21d_2d_v113_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_logmagslope_63d_2d_v114_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eff_tax_rate
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_logmagslope_252d_2d_v115_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_logmagslope_21d_2d_v116_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_logmagslope_63d_2d_v117_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tax_vol_252
def f061trx_f061_tax_rate_and_geography_tax_vol_252_logmagslope_252d_2d_v118_signal(taxexp, ebt, closeadj):
    base = _f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_logmagslope_21d_2d_v119_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_logmagslope_63d_2d_v120_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tax_assets_share
def f061trx_f061_tax_rate_and_geography_tax_assets_share_logmagslope_252d_2d_v121_signal(taxassets, assets, closeadj):
    base = taxassets / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_logmagslope_21d_2d_v122_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_logmagslope_63d_2d_v123_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tax_liab_share
def f061trx_f061_tax_rate_and_geography_tax_liab_share_logmagslope_252d_2d_v124_signal(taxliabilities, liabilities, closeadj):
    base = taxliabilities / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_logmagslope_21d_2d_v125_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_logmagslope_63d_2d_v126_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of net_tax_pos
def f061trx_f061_tax_rate_and_geography_net_tax_pos_logmagslope_252d_2d_v127_signal(taxassets, taxliabilities, closeadj):
    base = taxassets - taxliabilities
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_logmagslope_21d_2d_v128_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_logmagslope_63d_2d_v129_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tax_to_rev
def f061trx_f061_tax_rate_and_geography_tax_to_rev_logmagslope_252d_2d_v130_signal(taxexp, revenue, closeadj):
    base = taxexp / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_logmagslope_21d_2d_v131_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_logmagslope_63d_2d_v132_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tax_yoy_chg
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_logmagslope_252d_2d_v133_signal(taxexp, closeadj):
    base = taxexp.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eff_tax_rate|
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_logslope_63d_2d_v134_signal(taxexp, ebt, closeadj):
    base = np.log((_f061_eff_tax(taxexp, ebt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eff_tax_rate|
def f061trx_f061_tax_rate_and_geography_eff_tax_rate_logslope_252d_2d_v135_signal(taxexp, ebt, closeadj):
    base = np.log((_f061_eff_tax(taxexp, ebt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tax_vol_252|
def f061trx_f061_tax_rate_and_geography_tax_vol_252_logslope_63d_2d_v136_signal(taxexp, ebt, closeadj):
    base = np.log((_f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tax_vol_252|
def f061trx_f061_tax_rate_and_geography_tax_vol_252_logslope_252d_2d_v137_signal(taxexp, ebt, closeadj):
    base = np.log((_f061_eff_tax(taxexp, ebt).rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tax_assets_share|
def f061trx_f061_tax_rate_and_geography_tax_assets_share_logslope_63d_2d_v138_signal(taxassets, assets, closeadj):
    base = np.log((taxassets / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tax_assets_share|
def f061trx_f061_tax_rate_and_geography_tax_assets_share_logslope_252d_2d_v139_signal(taxassets, assets, closeadj):
    base = np.log((taxassets / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tax_liab_share|
def f061trx_f061_tax_rate_and_geography_tax_liab_share_logslope_63d_2d_v140_signal(taxliabilities, liabilities, closeadj):
    base = np.log((taxliabilities / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tax_liab_share|
def f061trx_f061_tax_rate_and_geography_tax_liab_share_logslope_252d_2d_v141_signal(taxliabilities, liabilities, closeadj):
    base = np.log((taxliabilities / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|net_tax_pos|
def f061trx_f061_tax_rate_and_geography_net_tax_pos_logslope_63d_2d_v142_signal(taxassets, taxliabilities, closeadj):
    base = np.log((taxassets - taxliabilities).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|net_tax_pos|
def f061trx_f061_tax_rate_and_geography_net_tax_pos_logslope_252d_2d_v143_signal(taxassets, taxliabilities, closeadj):
    base = np.log((taxassets - taxliabilities).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tax_to_rev|
def f061trx_f061_tax_rate_and_geography_tax_to_rev_logslope_63d_2d_v144_signal(taxexp, revenue, closeadj):
    base = np.log((taxexp / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tax_to_rev|
def f061trx_f061_tax_rate_and_geography_tax_to_rev_logslope_252d_2d_v145_signal(taxexp, revenue, closeadj):
    base = np.log((taxexp / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tax_yoy_chg|
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_logslope_63d_2d_v146_signal(taxexp, closeadj):
    base = np.log((taxexp.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tax_yoy_chg|
def f061trx_f061_tax_rate_and_geography_tax_yoy_chg_logslope_252d_2d_v147_signal(taxexp, closeadj):
    base = np.log((taxexp.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

