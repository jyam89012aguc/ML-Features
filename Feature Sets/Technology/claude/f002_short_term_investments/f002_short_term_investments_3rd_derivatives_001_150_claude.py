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


# 21d acceleration of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_accel_21d_3d_v001_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_accel_63d_3d_v002_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_accel_126d_3d_v003_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_accel_252d_3d_v004_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liqpool
def f002sti_f002_short_term_investments_liqpool_accel_21d_3d_v005_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool
def f002sti_f002_short_term_investments_liqpool_accel_63d_3d_v006_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liqpool
def f002sti_f002_short_term_investments_liqpool_accel_126d_3d_v007_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool
def f002sti_f002_short_term_investments_liqpool_accel_252d_3d_v008_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_accel_21d_3d_v009_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_accel_63d_3d_v010_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_accel_126d_3d_v011_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_accel_252d_3d_v012_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_accel_21d_3d_v013_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_accel_63d_3d_v014_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_accel_126d_3d_v015_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_accel_252d_3d_v016_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_accel_21d_3d_v017_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_accel_63d_3d_v018_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_accel_126d_3d_v019_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_accel_252d_3d_v020_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_accel_21d_3d_v021_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_accel_63d_3d_v022_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_accel_126d_3d_v023_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_accel_252d_3d_v024_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_accel_21d_3d_v025_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_accel_63d_3d_v026_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_accel_126d_3d_v027_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_accel_252d_3d_v028_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slopez_21d_z126_3d_v029_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slopez_63d_z252_3d_v030_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slopez_126d_z252_3d_v031_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_slopez_252d_z504_3d_v032_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liqpool
def f002sti_f002_short_term_investments_liqpool_slopez_21d_z126_3d_v033_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liqpool
def f002sti_f002_short_term_investments_liqpool_slopez_63d_z252_3d_v034_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liqpool
def f002sti_f002_short_term_investments_liqpool_slopez_126d_z252_3d_v035_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liqpool
def f002sti_f002_short_term_investments_liqpool_slopez_252d_z504_3d_v036_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slopez_21d_z126_3d_v037_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slopez_63d_z252_3d_v038_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slopez_126d_z252_3d_v039_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_slopez_252d_z504_3d_v040_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slopez_21d_z126_3d_v041_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slopez_63d_z252_3d_v042_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slopez_126d_z252_3d_v043_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_slopez_252d_z504_3d_v044_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slopez_21d_z126_3d_v045_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slopez_63d_z252_3d_v046_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slopez_126d_z252_3d_v047_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_slopez_252d_z504_3d_v048_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slopez_21d_z126_3d_v049_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slopez_63d_z252_3d_v050_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slopez_126d_z252_3d_v051_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_slopez_252d_z504_3d_v052_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slopez_21d_z126_3d_v053_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slopez_63d_z252_3d_v054_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slopez_126d_z252_3d_v055_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_slopez_252d_z504_3d_v056_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_jerk_21d_3d_v057_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_jerk_63d_3d_v058_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_jerk_126d_3d_v059_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liqpool
def f002sti_f002_short_term_investments_liqpool_jerk_21d_3d_v060_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liqpool
def f002sti_f002_short_term_investments_liqpool_jerk_63d_3d_v061_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liqpool
def f002sti_f002_short_term_investments_liqpool_jerk_126d_3d_v062_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_jerk_21d_3d_v063_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_jerk_63d_3d_v064_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_jerk_126d_3d_v065_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_jerk_21d_3d_v066_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_jerk_63d_3d_v067_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_jerk_126d_3d_v068_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_jerk_21d_3d_v069_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_jerk_63d_3d_v070_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_jerk_126d_3d_v071_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_jerk_21d_3d_v072_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_jerk_63d_3d_v073_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_jerk_126d_3d_v074_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_jerk_21d_3d_v075_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_jerk_63d_3d_v076_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_jerk_126d_3d_v077_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sti_lvl smoothed over 252d
def f002sti_f002_short_term_investments_sti_lvl_smoothaccel_63d_sm252_3d_v078_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sti_lvl smoothed over 504d
def f002sti_f002_short_term_investments_sti_lvl_smoothaccel_252d_sm504_3d_v079_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liqpool smoothed over 252d
def f002sti_f002_short_term_investments_liqpool_smoothaccel_63d_sm252_3d_v080_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liqpool smoothed over 504d
def f002sti_f002_short_term_investments_liqpool_smoothaccel_252d_sm504_3d_v081_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liqpool_to_asset smoothed over 252d
def f002sti_f002_short_term_investments_liqpool_to_asset_smoothaccel_63d_sm252_3d_v082_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liqpool_to_asset smoothed over 504d
def f002sti_f002_short_term_investments_liqpool_to_asset_smoothaccel_252d_sm504_3d_v083_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liqpool_to_mcap smoothed over 252d
def f002sti_f002_short_term_investments_liqpool_to_mcap_smoothaccel_63d_sm252_3d_v084_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liqpool_to_mcap smoothed over 504d
def f002sti_f002_short_term_investments_liqpool_to_mcap_smoothaccel_252d_sm504_3d_v085_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liqpool_to_liab smoothed over 252d
def f002sti_f002_short_term_investments_liqpool_to_liab_smoothaccel_63d_sm252_3d_v086_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liqpool_to_liab smoothed over 504d
def f002sti_f002_short_term_investments_liqpool_to_liab_smoothaccel_252d_sm504_3d_v087_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sti_to_total_inv smoothed over 252d
def f002sti_f002_short_term_investments_sti_to_total_inv_smoothaccel_63d_sm252_3d_v088_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sti_to_total_inv smoothed over 504d
def f002sti_f002_short_term_investments_sti_to_total_inv_smoothaccel_252d_sm504_3d_v089_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sti_to_assetc smoothed over 252d
def f002sti_f002_short_term_investments_sti_to_assetc_smoothaccel_63d_sm252_3d_v090_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sti_to_assetc smoothed over 504d
def f002sti_f002_short_term_investments_sti_to_assetc_smoothaccel_252d_sm504_3d_v091_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_accelz_21d_z252_3d_v092_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_accelz_63d_z504_3d_v093_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liqpool
def f002sti_f002_short_term_investments_liqpool_accelz_21d_z252_3d_v094_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liqpool
def f002sti_f002_short_term_investments_liqpool_accelz_63d_z504_3d_v095_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_accelz_21d_z252_3d_v096_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_accelz_63d_z504_3d_v097_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_accelz_21d_z252_3d_v098_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_accelz_63d_z504_3d_v099_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_accelz_21d_z252_3d_v100_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_accelz_63d_z504_3d_v101_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_accelz_21d_z252_3d_v102_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_accelz_63d_z504_3d_v103_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_accelz_21d_z252_3d_v104_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sti_to_assetc
def f002sti_f002_short_term_investments_sti_to_assetc_accelz_63d_z504_3d_v105_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sti_lvl (raw count, no price scaling)
def f002sti_f002_short_term_investments_sti_lvl_signflip_63d_3d_v106_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sti_lvl (raw count, no price scaling)
def f002sti_f002_short_term_investments_sti_lvl_signflip_252d_3d_v107_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liqpool (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_signflip_63d_3d_v108_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liqpool (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_signflip_252d_3d_v109_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liqpool_to_asset (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_to_asset_signflip_63d_3d_v110_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liqpool_to_asset (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_to_asset_signflip_252d_3d_v111_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liqpool_to_mcap (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_to_mcap_signflip_63d_3d_v112_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liqpool_to_mcap (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_to_mcap_signflip_252d_3d_v113_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liqpool_to_liab (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_to_liab_signflip_63d_3d_v114_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liqpool_to_liab (raw count, no price scaling)
def f002sti_f002_short_term_investments_liqpool_to_liab_signflip_252d_3d_v115_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sti_to_total_inv (raw count, no price scaling)
def f002sti_f002_short_term_investments_sti_to_total_inv_signflip_63d_3d_v116_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sti_to_total_inv (raw count, no price scaling)
def f002sti_f002_short_term_investments_sti_to_total_inv_signflip_252d_3d_v117_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sti_to_assetc (raw count, no price scaling)
def f002sti_f002_short_term_investments_sti_to_assetc_signflip_63d_3d_v118_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sti_to_assetc (raw count, no price scaling)
def f002sti_f002_short_term_investments_sti_to_assetc_signflip_252d_3d_v119_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sti_lvl normalized by 252d range
def f002sti_f002_short_term_investments_sti_lvl_rngaccel_63d_r252_3d_v120_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sti_lvl normalized by 504d range
def f002sti_f002_short_term_investments_sti_lvl_rngaccel_252d_r504_3d_v121_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool normalized by 252d range
def f002sti_f002_short_term_investments_liqpool_rngaccel_63d_r252_3d_v122_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool normalized by 504d range
def f002sti_f002_short_term_investments_liqpool_rngaccel_252d_r504_3d_v123_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool_to_asset normalized by 252d range
def f002sti_f002_short_term_investments_liqpool_to_asset_rngaccel_63d_r252_3d_v124_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool_to_asset normalized by 504d range
def f002sti_f002_short_term_investments_liqpool_to_asset_rngaccel_252d_r504_3d_v125_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool_to_mcap normalized by 252d range
def f002sti_f002_short_term_investments_liqpool_to_mcap_rngaccel_63d_r252_3d_v126_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool_to_mcap normalized by 504d range
def f002sti_f002_short_term_investments_liqpool_to_mcap_rngaccel_252d_r504_3d_v127_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liqpool_to_liab normalized by 252d range
def f002sti_f002_short_term_investments_liqpool_to_liab_rngaccel_63d_r252_3d_v128_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liqpool_to_liab normalized by 504d range
def f002sti_f002_short_term_investments_liqpool_to_liab_rngaccel_252d_r504_3d_v129_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sti_to_total_inv normalized by 252d range
def f002sti_f002_short_term_investments_sti_to_total_inv_rngaccel_63d_r252_3d_v130_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sti_to_total_inv normalized by 504d range
def f002sti_f002_short_term_investments_sti_to_total_inv_rngaccel_252d_r504_3d_v131_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sti_to_assetc normalized by 252d range
def f002sti_f002_short_term_investments_sti_to_assetc_rngaccel_63d_r252_3d_v132_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sti_to_assetc normalized by 504d range
def f002sti_f002_short_term_investments_sti_to_assetc_rngaccel_252d_r504_3d_v133_signal(investmentsc, assetsc, closeadj):
    base = investmentsc / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_cumslope_21d_3d_v134_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_cumslope_63d_3d_v135_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sti_lvl
def f002sti_f002_short_term_investments_sti_lvl_cumslope_252d_3d_v136_signal(investmentsc, closeadj):
    base = _f002_sti(investmentsc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liqpool
def f002sti_f002_short_term_investments_liqpool_cumslope_21d_3d_v137_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liqpool
def f002sti_f002_short_term_investments_liqpool_cumslope_63d_3d_v138_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of liqpool
def f002sti_f002_short_term_investments_liqpool_cumslope_252d_3d_v139_signal(cashneq, investmentsc, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_cumslope_21d_3d_v140_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_cumslope_63d_3d_v141_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of liqpool_to_asset
def f002sti_f002_short_term_investments_liqpool_to_asset_cumslope_252d_3d_v142_signal(cashneq, investmentsc, assets, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_cumslope_21d_3d_v143_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_cumslope_63d_3d_v144_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of liqpool_to_mcap
def f002sti_f002_short_term_investments_liqpool_to_mcap_cumslope_252d_3d_v145_signal(cashneq, investmentsc, marketcap, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_cumslope_21d_3d_v146_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_cumslope_63d_3d_v147_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of liqpool_to_liab
def f002sti_f002_short_term_investments_liqpool_to_liab_cumslope_252d_3d_v148_signal(cashneq, investmentsc, liabilities, closeadj):
    base = _f002_liquid_pool(cashneq, investmentsc) / liabilities.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_cumslope_21d_3d_v149_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sti_to_total_inv
def f002sti_f002_short_term_investments_sti_to_total_inv_cumslope_63d_3d_v150_signal(investmentsc, investments, closeadj):
    base = _f002_sti_to_total_inv(investmentsc, investments)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

