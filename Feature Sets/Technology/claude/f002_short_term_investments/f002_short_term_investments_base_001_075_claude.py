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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f002_sti(investmentsc):
    return investmentsc.fillna(0)


def _f002_liquid_pool(cashneq, investmentsc):
    return cashneq.fillna(0) + investmentsc.fillna(0)


def _f002_sti_to_total_inv(investmentsc, investments):
    return investmentsc / investments.replace(0, np.nan).abs()


# 21d mean of sti_lvl scaled by closeadj
def f002sti_f002_short_term_investments_sti_lvl_mean_21d_base_v001_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sti_lvl scaled by closeadj
def f002sti_f002_short_term_investments_sti_lvl_mean_63d_base_v002_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sti_lvl scaled by closeadj
def f002sti_f002_short_term_investments_sti_lvl_mean_126d_base_v003_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sti_lvl scaled by closeadj
def f002sti_f002_short_term_investments_sti_lvl_mean_252d_base_v004_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sti_lvl scaled by closeadj
def f002sti_f002_short_term_investments_sti_lvl_mean_504d_base_v005_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liqpool scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_mean_21d_base_v006_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liqpool scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_mean_63d_base_v007_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liqpool scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_mean_126d_base_v008_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liqpool scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_mean_252d_base_v009_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liqpool scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_mean_504d_base_v010_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liqpool_to_asset scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_asset_mean_21d_base_v011_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liqpool_to_asset scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_asset_mean_63d_base_v012_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liqpool_to_asset scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_asset_mean_126d_base_v013_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liqpool_to_asset scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_asset_mean_252d_base_v014_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liqpool_to_asset scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_asset_mean_504d_base_v015_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liqpool_to_mcap scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_mcap_mean_21d_base_v016_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liqpool_to_mcap scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_mcap_mean_63d_base_v017_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liqpool_to_mcap scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_mcap_mean_126d_base_v018_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liqpool_to_mcap scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_mcap_mean_252d_base_v019_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liqpool_to_mcap scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_mcap_mean_504d_base_v020_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of liqpool_to_liab scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_liab_mean_21d_base_v021_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of liqpool_to_liab scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_liab_mean_63d_base_v022_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of liqpool_to_liab scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_liab_mean_126d_base_v023_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of liqpool_to_liab scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_liab_mean_252d_base_v024_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of liqpool_to_liab scaled by closeadj
def f002sti_f002_short_term_investments_liqpool_to_liab_mean_504d_base_v025_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sti_to_total_inv scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_total_inv_mean_21d_base_v026_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sti_to_total_inv scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_total_inv_mean_63d_base_v027_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sti_to_total_inv scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_total_inv_mean_126d_base_v028_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sti_to_total_inv scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_total_inv_mean_252d_base_v029_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sti_to_total_inv scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_total_inv_mean_504d_base_v030_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sti_to_assetc scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_assetc_mean_21d_base_v031_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sti_to_assetc scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_assetc_mean_63d_base_v032_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sti_to_assetc scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_assetc_mean_126d_base_v033_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sti_to_assetc scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_assetc_mean_252d_base_v034_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sti_to_assetc scaled by closeadj
def f002sti_f002_short_term_investments_sti_to_assetc_mean_504d_base_v035_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_median_63d_base_v036_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_median_252d_base_v037_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_median_504d_base_v038_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liqpool
def f002sti_f002_short_term_investments_liqpool_median_63d_base_v039_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liqpool
def f002sti_f002_short_term_investments_liqpool_median_252d_base_v040_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liqpool
def f002sti_f002_short_term_investments_liqpool_median_504d_base_v041_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_median_63d_base_v042_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_median_252d_base_v043_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_median_504d_base_v044_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_median_63d_base_v045_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_median_252d_base_v046_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_median_504d_base_v047_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_median_63d_base_v048_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_median_252d_base_v049_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_median_504d_base_v050_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_median_63d_base_v051_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_median_252d_base_v052_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_median_504d_base_v053_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_median_63d_base_v054_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_median_252d_base_v055_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_median_504d_base_v056_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_rmax_252d_base_v057_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_rmax_504d_base_v058_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liqpool
def f002sti_f002_short_term_investments_liqpool_rmax_252d_base_v059_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liqpool
def f002sti_f002_short_term_investments_liqpool_rmax_504d_base_v060_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_rmax_252d_base_v061_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_rmax_504d_base_v062_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_rmax_252d_base_v063_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_rmax_504d_base_v064_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_rmax_252d_base_v065_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_rmax_504d_base_v066_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_rmax_252d_base_v067_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_rmax_504d_base_v068_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_rmax_252d_base_v069_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_rmax_504d_base_v070_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_rmin_252d_base_v071_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_rmin_504d_base_v072_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of liqpool
def f002sti_f002_short_term_investments_liqpool_rmin_252d_base_v073_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of liqpool
def f002sti_f002_short_term_investments_liqpool_rmin_504d_base_v074_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_rmin_252d_base_v075_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

