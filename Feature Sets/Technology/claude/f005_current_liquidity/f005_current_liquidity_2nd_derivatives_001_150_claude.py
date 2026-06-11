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
def _f005_current_ratio(assetsc, liabilitiesc):
    return assetsc / liabilitiesc.replace(0, np.nan).abs()


def _f005_qac(assetsc, inventory):
    return (assetsc - inventory.fillna(0))


def _f005_cash_quick(cashneq, investmentsc, liabilitiesc):
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / liabilitiesc.replace(0, np.nan).abs()


# 21d slope of curratio
def f005cl_f005_current_liquidity_curratio_slope_21d_2d_v001_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of curratio
def f005cl_f005_current_liquidity_curratio_slope_63d_2d_v002_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of curratio
def f005cl_f005_current_liquidity_curratio_slope_126d_2d_v003_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of curratio
def f005cl_f005_current_liquidity_curratio_slope_252d_2d_v004_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of curratio
def f005cl_f005_current_liquidity_curratio_slope_504d_2d_v005_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slope_21d_2d_v006_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slope_63d_2d_v007_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slope_126d_2d_v008_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slope_252d_2d_v009_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slope_504d_2d_v010_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_slope_21d_2d_v011_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_slope_63d_2d_v012_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_slope_126d_2d_v013_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_slope_252d_2d_v014_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_slope_504d_2d_v015_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slope_21d_2d_v016_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slope_63d_2d_v017_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slope_126d_2d_v018_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slope_252d_2d_v019_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slope_504d_2d_v020_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slope_21d_2d_v021_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slope_63d_2d_v022_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slope_126d_2d_v023_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slope_252d_2d_v024_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slope_504d_2d_v025_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slope_21d_2d_v026_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slope_63d_2d_v027_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slope_126d_2d_v028_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slope_252d_2d_v029_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slope_504d_2d_v030_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slope_21d_2d_v031_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slope_63d_2d_v032_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slope_126d_2d_v033_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slope_252d_2d_v034_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slope_504d_2d_v035_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of curratio
def f005cl_f005_current_liquidity_curratio_sm21_sl21_2d_v036_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of curratio
def f005cl_f005_current_liquidity_curratio_sm63_sl21_2d_v037_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of curratio
def f005cl_f005_current_liquidity_curratio_sm63_sl63_2d_v038_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of curratio
def f005cl_f005_current_liquidity_curratio_sm252_sl63_2d_v039_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of curratio
def f005cl_f005_current_liquidity_curratio_sm252_sl126_2d_v040_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sm21_sl21_2d_v041_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sm63_sl21_2d_v042_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sm63_sl63_2d_v043_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sm252_sl63_2d_v044_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sm252_sl126_2d_v045_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sm21_sl21_2d_v046_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f005_cash_quick(cashneq, investmentsc, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sm63_sl21_2d_v047_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f005_cash_quick(cashneq, investmentsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sm63_sl63_2d_v048_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f005_cash_quick(cashneq, investmentsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sm252_sl63_2d_v049_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f005_cash_quick(cashneq, investmentsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sm252_sl126_2d_v050_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _mean(_f005_cash_quick(cashneq, investmentsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sm21_sl21_2d_v051_signal(assetsc, liabilitiesc, assets, closeadj):
    base = _mean((assetsc - liabilitiesc) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sm63_sl21_2d_v052_signal(assetsc, liabilitiesc, assets, closeadj):
    base = _mean((assetsc - liabilitiesc) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sm63_sl63_2d_v053_signal(assetsc, liabilitiesc, assets, closeadj):
    base = _mean((assetsc - liabilitiesc) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sm252_sl63_2d_v054_signal(assetsc, liabilitiesc, assets, closeadj):
    base = _mean((assetsc - liabilitiesc) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sm252_sl126_2d_v055_signal(assetsc, liabilitiesc, assets, closeadj):
    base = _mean((assetsc - liabilitiesc) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sm21_sl21_2d_v056_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = _mean((assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sm63_sl21_2d_v057_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = _mean((assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sm63_sl63_2d_v058_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = _mean((assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sm252_sl63_2d_v059_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = _mean((assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sm252_sl126_2d_v060_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = _mean((assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sm21_sl21_2d_v061_signal(liabilitiesc, assets, closeadj):
    base = _mean(liabilitiesc / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sm63_sl21_2d_v062_signal(liabilitiesc, assets, closeadj):
    base = _mean(liabilitiesc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sm63_sl63_2d_v063_signal(liabilitiesc, assets, closeadj):
    base = _mean(liabilitiesc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sm252_sl63_2d_v064_signal(liabilitiesc, assets, closeadj):
    base = _mean(liabilitiesc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sm252_sl126_2d_v065_signal(liabilitiesc, assets, closeadj):
    base = _mean(liabilitiesc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sm21_sl21_2d_v066_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc) - 1.0, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sm63_sl21_2d_v067_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc) - 1.0, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sm63_sl63_2d_v068_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc) - 1.0, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sm252_sl63_2d_v069_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc) - 1.0, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sm252_sl126_2d_v070_signal(assetsc, liabilitiesc, closeadj):
    base = _mean(_f005_current_ratio(assetsc, liabilitiesc) - 1.0, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of curratio
def f005cl_f005_current_liquidity_curratio_pctslope_21d_2d_v071_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of curratio
def f005cl_f005_current_liquidity_curratio_pctslope_63d_2d_v072_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of curratio
def f005cl_f005_current_liquidity_curratio_pctslope_252d_2d_v073_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_pctslope_21d_2d_v074_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_pctslope_63d_2d_v075_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_pctslope_252d_2d_v076_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cashquick
def f005cl_f005_current_liquidity_cashquick_pctslope_21d_2d_v077_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cashquick
def f005cl_f005_current_liquidity_cashquick_pctslope_63d_2d_v078_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cashquick
def f005cl_f005_current_liquidity_cashquick_pctslope_252d_2d_v079_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_pctslope_21d_2d_v080_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_pctslope_63d_2d_v081_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_pctslope_252d_2d_v082_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_pctslope_21d_2d_v083_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_pctslope_63d_2d_v084_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_pctslope_252d_2d_v085_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_pctslope_21d_2d_v086_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_pctslope_63d_2d_v087_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_pctslope_252d_2d_v088_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_pctslope_21d_2d_v089_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_pctslope_63d_2d_v090_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_pctslope_252d_2d_v091_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of curratio
def f005cl_f005_current_liquidity_curratio_sgnslope_21d_2d_v092_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of curratio
def f005cl_f005_current_liquidity_curratio_sgnslope_63d_2d_v093_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of curratio
def f005cl_f005_current_liquidity_curratio_sgnslope_252d_2d_v094_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sgnslope_21d_2d_v095_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sgnslope_63d_2d_v096_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_sgnslope_252d_2d_v097_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sgnslope_21d_2d_v098_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sgnslope_63d_2d_v099_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_sgnslope_252d_2d_v100_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sgnslope_21d_2d_v101_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sgnslope_63d_2d_v102_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_sgnslope_252d_2d_v103_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sgnslope_21d_2d_v104_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sgnslope_63d_2d_v105_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_sgnslope_252d_2d_v106_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sgnslope_21d_2d_v107_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sgnslope_63d_2d_v108_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_sgnslope_252d_2d_v109_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sgnslope_21d_2d_v110_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sgnslope_63d_2d_v111_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_sgnslope_252d_2d_v112_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of curratio
def f005cl_f005_current_liquidity_curratio_logmagslope_21d_2d_v113_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of curratio
def f005cl_f005_current_liquidity_curratio_logmagslope_63d_2d_v114_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of curratio
def f005cl_f005_current_liquidity_curratio_logmagslope_252d_2d_v115_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_logmagslope_21d_2d_v116_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_logmagslope_63d_2d_v117_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_logmagslope_252d_2d_v118_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_logmagslope_21d_2d_v119_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_logmagslope_63d_2d_v120_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of cashquick
def f005cl_f005_current_liquidity_cashquick_logmagslope_252d_2d_v121_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_logmagslope_21d_2d_v122_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_logmagslope_63d_2d_v123_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_logmagslope_252d_2d_v124_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_logmagslope_21d_2d_v125_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_logmagslope_63d_2d_v126_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_logmagslope_252d_2d_v127_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_logmagslope_21d_2d_v128_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_logmagslope_63d_2d_v129_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_logmagslope_252d_2d_v130_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_logmagslope_21d_2d_v131_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_logmagslope_63d_2d_v132_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_logmagslope_252d_2d_v133_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|curratio|
def f005cl_f005_current_liquidity_curratio_logslope_63d_2d_v134_signal(assetsc, liabilitiesc, closeadj):
    base = np.log((_f005_current_ratio(assetsc, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|curratio|
def f005cl_f005_current_liquidity_curratio_logslope_252d_2d_v135_signal(assetsc, liabilitiesc, closeadj):
    base = np.log((_f005_current_ratio(assetsc, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|qac_ratio|
def f005cl_f005_current_liquidity_qac_ratio_logslope_63d_2d_v136_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = np.log((_f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|qac_ratio|
def f005cl_f005_current_liquidity_qac_ratio_logslope_252d_2d_v137_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = np.log((_f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|cashquick|
def f005cl_f005_current_liquidity_cashquick_logslope_63d_2d_v138_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = np.log((_f005_cash_quick(cashneq, investmentsc, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|cashquick|
def f005cl_f005_current_liquidity_cashquick_logslope_252d_2d_v139_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = np.log((_f005_cash_quick(cashneq, investmentsc, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netwc_to_asset|
def f005cl_f005_current_liquidity_netwc_to_asset_logslope_63d_2d_v140_signal(assetsc, liabilitiesc, assets, closeadj):
    base = np.log(((assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netwc_to_asset|
def f005cl_f005_current_liquidity_netwc_to_asset_logslope_252d_2d_v141_signal(assetsc, liabilitiesc, assets, closeadj):
    base = np.log(((assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|netwc_to_mcap|
def f005cl_f005_current_liquidity_netwc_to_mcap_logslope_63d_2d_v142_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = np.log(((assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|netwc_to_mcap|
def f005cl_f005_current_liquidity_netwc_to_mcap_logslope_252d_2d_v143_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = np.log(((assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liabc_to_asset|
def f005cl_f005_current_liquidity_liabc_to_asset_logslope_63d_2d_v144_signal(liabilitiesc, assets, closeadj):
    base = np.log((liabilitiesc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liabc_to_asset|
def f005cl_f005_current_liquidity_liabc_to_asset_logslope_252d_2d_v145_signal(liabilitiesc, assets, closeadj):
    base = np.log((liabilitiesc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|curratio_minus_1|
def f005cl_f005_current_liquidity_curratio_minus_1_logslope_63d_2d_v146_signal(assetsc, liabilitiesc, closeadj):
    base = np.log((_f005_current_ratio(assetsc, liabilitiesc) - 1.0).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|curratio_minus_1|
def f005cl_f005_current_liquidity_curratio_minus_1_logslope_252d_2d_v147_signal(assetsc, liabilitiesc, closeadj):
    base = np.log((_f005_current_ratio(assetsc, liabilitiesc) - 1.0).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

