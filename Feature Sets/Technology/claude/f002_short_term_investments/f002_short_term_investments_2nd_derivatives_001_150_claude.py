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
def _f002_sti(investmentsc):
    return investmentsc.fillna(0)


def _f002_liquid_pool(cashneq, investmentsc):
    return cashneq.fillna(0) + investmentsc.fillna(0)


def _f002_sti_to_total_inv(investmentsc, investments):
    return investmentsc / investments.replace(0, np.nan).abs()


# 21d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slope_21d_2d_v001_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slope_63d_2d_v002_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slope_126d_2d_v003_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slope_252d_2d_v004_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slope_504d_2d_v005_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_slope_21d_2d_v006_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_slope_63d_2d_v007_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_slope_126d_2d_v008_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_slope_252d_2d_v009_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_slope_504d_2d_v010_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slope_21d_2d_v011_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slope_63d_2d_v012_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slope_126d_2d_v013_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slope_252d_2d_v014_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slope_504d_2d_v015_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slope_21d_2d_v016_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slope_63d_2d_v017_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slope_126d_2d_v018_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slope_252d_2d_v019_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slope_504d_2d_v020_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slope_21d_2d_v021_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slope_63d_2d_v022_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slope_126d_2d_v023_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slope_252d_2d_v024_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slope_504d_2d_v025_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slope_21d_2d_v026_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slope_63d_2d_v027_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slope_126d_2d_v028_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slope_252d_2d_v029_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slope_504d_2d_v030_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slope_21d_2d_v031_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slope_63d_2d_v032_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slope_126d_2d_v033_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slope_252d_2d_v034_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slope_504d_2d_v035_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sm21_sl21_2d_v036_signal(investmentsc, closeadj):
    base = _mean(_f002_sti(investmentsc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sm63_sl21_2d_v037_signal(investmentsc, closeadj):
    base = _mean(_f002_sti(investmentsc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sm63_sl63_2d_v038_signal(investmentsc, closeadj):
    base = _mean(_f002_sti(investmentsc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sm252_sl63_2d_v039_signal(investmentsc, closeadj):
    base = _mean(_f002_sti(investmentsc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sm252_sl126_2d_v040_signal(investmentsc, closeadj):
    base = _mean(_f002_sti(investmentsc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sm21_sl21_2d_v041_signal(cashneq, investmentsc, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sm63_sl21_2d_v042_signal(cashneq, investmentsc, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sm63_sl63_2d_v043_signal(cashneq, investmentsc, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sm252_sl63_2d_v044_signal(cashneq, investmentsc, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sm252_sl126_2d_v045_signal(cashneq, investmentsc, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sm21_sl21_2d_v046_signal(cashneq, investmentsc, assets, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sm63_sl21_2d_v047_signal(cashneq, investmentsc, assets, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sm63_sl63_2d_v048_signal(cashneq, investmentsc, assets, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sm252_sl63_2d_v049_signal(cashneq, investmentsc, assets, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sm252_sl126_2d_v050_signal(cashneq, investmentsc, assets, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sm21_sl21_2d_v051_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sm63_sl21_2d_v052_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sm63_sl63_2d_v053_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sm252_sl63_2d_v054_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sm252_sl126_2d_v055_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sm21_sl21_2d_v056_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sm63_sl21_2d_v057_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sm63_sl63_2d_v058_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sm252_sl63_2d_v059_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sm252_sl126_2d_v060_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _mean(_f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sm21_sl21_2d_v061_signal(investmentsc, investments, closeadj):
    base = _mean(_f002_sti_to_total_inv(investmentsc, investments), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sm63_sl21_2d_v062_signal(investmentsc, investments, closeadj):
    base = _mean(_f002_sti_to_total_inv(investmentsc, investments), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sm63_sl63_2d_v063_signal(investmentsc, investments, closeadj):
    base = _mean(_f002_sti_to_total_inv(investmentsc, investments), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sm252_sl63_2d_v064_signal(investmentsc, investments, closeadj):
    base = _mean(_f002_sti_to_total_inv(investmentsc, investments), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sm252_sl126_2d_v065_signal(investmentsc, investments, closeadj):
    base = _mean(_f002_sti_to_total_inv(investmentsc, investments), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sm21_sl21_2d_v066_signal(investmentsc, assetsc, closeadj):
    base = _mean(investmentsc / assetsc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sm63_sl21_2d_v067_signal(investmentsc, assetsc, closeadj):
    base = _mean(investmentsc / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sm63_sl63_2d_v068_signal(investmentsc, assetsc, closeadj):
    base = _mean(investmentsc / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sm252_sl63_2d_v069_signal(investmentsc, assetsc, closeadj):
    base = _mean(investmentsc / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sm252_sl126_2d_v070_signal(investmentsc, assetsc, closeadj):
    base = _mean(investmentsc / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_pctslope_21d_2d_v071_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_pctslope_63d_2d_v072_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_pctslope_252d_2d_v073_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liqpool
def f002sti_f002_short_term_investments_liqpool_pctslope_21d_2d_v074_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liqpool
def f002sti_f002_short_term_investments_liqpool_pctslope_63d_2d_v075_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liqpool
def f002sti_f002_short_term_investments_liqpool_pctslope_252d_2d_v076_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_pctslope_21d_2d_v077_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_pctslope_63d_2d_v078_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_pctslope_252d_2d_v079_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_pctslope_21d_2d_v080_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_pctslope_63d_2d_v081_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_pctslope_252d_2d_v082_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_pctslope_21d_2d_v083_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_pctslope_63d_2d_v084_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_pctslope_252d_2d_v085_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_pctslope_21d_2d_v086_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_pctslope_63d_2d_v087_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_pctslope_252d_2d_v088_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_pctslope_21d_2d_v089_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_pctslope_63d_2d_v090_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_pctslope_252d_2d_v091_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sgnslope_21d_2d_v092_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sgnslope_63d_2d_v093_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_sgnslope_252d_2d_v094_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sgnslope_21d_2d_v095_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sgnslope_63d_2d_v096_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_sgnslope_252d_2d_v097_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sgnslope_21d_2d_v098_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sgnslope_63d_2d_v099_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_sgnslope_252d_2d_v100_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sgnslope_21d_2d_v101_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sgnslope_63d_2d_v102_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_sgnslope_252d_2d_v103_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sgnslope_21d_2d_v104_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sgnslope_63d_2d_v105_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_sgnslope_252d_2d_v106_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sgnslope_21d_2d_v107_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sgnslope_63d_2d_v108_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_sgnslope_252d_2d_v109_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sgnslope_21d_2d_v110_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sgnslope_63d_2d_v111_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_sgnslope_252d_2d_v112_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_logmagslope_21d_2d_v113_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_logmagslope_63d_2d_v114_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_logmagslope_252d_2d_v115_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_logmagslope_21d_2d_v116_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_logmagslope_63d_2d_v117_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liqpool
def f002sti_f002_short_term_investments_liqpool_logmagslope_252d_2d_v118_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_logmagslope_21d_2d_v119_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_logmagslope_63d_2d_v120_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_logmagslope_252d_2d_v121_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_logmagslope_21d_2d_v122_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_logmagslope_63d_2d_v123_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_logmagslope_252d_2d_v124_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_logmagslope_21d_2d_v125_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_logmagslope_63d_2d_v126_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_logmagslope_252d_2d_v127_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_logmagslope_21d_2d_v128_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_logmagslope_63d_2d_v129_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_logmagslope_252d_2d_v130_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_logmagslope_21d_2d_v131_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_logmagslope_63d_2d_v132_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_logmagslope_252d_2d_v133_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sti_lvl|
def f002sti_f002_short_term_investments_sti_lvl_logslope_63d_2d_v134_signal(investmentsc, closeadj):
    base = np.log((_f002_sti(investmentsc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sti_lvl|
def f002sti_f002_short_term_investments_sti_lvl_logslope_252d_2d_v135_signal(investmentsc, closeadj):
    base = np.log((_f002_sti(investmentsc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liqpool|
def f002sti_f002_short_term_investments_liqpool_logslope_63d_2d_v136_signal(cashneq, investmentsc, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liqpool|
def f002sti_f002_short_term_investments_liqpool_logslope_252d_2d_v137_signal(cashneq, investmentsc, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liqpool_to_asset|
def f002sti_f002_short_term_investments_liqpool_to_asset_logslope_63d_2d_v138_signal(cashneq, investmentsc, assets, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liqpool_to_asset|
def f002sti_f002_short_term_investments_liqpool_to_asset_logslope_252d_2d_v139_signal(cashneq, investmentsc, assets, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liqpool_to_mcap|
def f002sti_f002_short_term_investments_liqpool_to_mcap_logslope_63d_2d_v140_signal(cashneq, investmentsc, marketcap, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liqpool_to_mcap|
def f002sti_f002_short_term_investments_liqpool_to_mcap_logslope_252d_2d_v141_signal(cashneq, investmentsc, marketcap, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liqpool_to_liab|
def f002sti_f002_short_term_investments_liqpool_to_liab_logslope_63d_2d_v142_signal(cashneq, investmentsc, liabilities, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liqpool_to_liab|
def f002sti_f002_short_term_investments_liqpool_to_liab_logslope_252d_2d_v143_signal(cashneq, investmentsc, liabilities, closeadj):
    base = np.log((_f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sti_to_total_inv|
def f002sti_f002_short_term_investments_sti_to_total_inv_logslope_63d_2d_v144_signal(investmentsc, investments, closeadj):
    base = np.log((_f002_sti_to_total_inv(investmentsc, investments)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sti_to_total_inv|
def f002sti_f002_short_term_investments_sti_to_total_inv_logslope_252d_2d_v145_signal(investmentsc, investments, closeadj):
    base = np.log((_f002_sti_to_total_inv(investmentsc, investments)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sti_to_assetc|
def f002sti_f002_short_term_investments_sti_to_assetc_logslope_63d_2d_v146_signal(investmentsc, assetsc, closeadj):
    base = np.log((investmentsc / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sti_to_assetc|
def f002sti_f002_short_term_investments_sti_to_assetc_logslope_252d_2d_v147_signal(investmentsc, assetsc, closeadj):
    base = np.log((investmentsc / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

