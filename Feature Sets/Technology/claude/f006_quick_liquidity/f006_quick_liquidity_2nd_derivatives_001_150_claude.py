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
def _f006_quick_assets(assetsc, inventory):
    return assetsc - inventory.fillna(0)


def _f006_quick_ratio(assetsc, inventory, liabilitiesc):
    qa = assetsc - inventory.fillna(0)
    return qa / liabilitiesc.replace(0, np.nan).abs()


def _f006_cash_only_quick(cashneq, liabilitiesc):
    return cashneq / liabilitiesc.replace(0, np.nan).abs()


# 21d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slope_21d_2d_v001_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slope_63d_2d_v002_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slope_126d_2d_v003_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slope_252d_2d_v004_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slope_504d_2d_v005_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slope_21d_2d_v006_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slope_63d_2d_v007_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slope_126d_2d_v008_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slope_252d_2d_v009_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slope_504d_2d_v010_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slope_21d_2d_v011_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slope_63d_2d_v012_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slope_126d_2d_v013_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slope_252d_2d_v014_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slope_504d_2d_v015_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slope_21d_2d_v016_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slope_63d_2d_v017_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slope_126d_2d_v018_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slope_252d_2d_v019_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slope_504d_2d_v020_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slope_21d_2d_v021_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slope_63d_2d_v022_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slope_126d_2d_v023_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slope_252d_2d_v024_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slope_504d_2d_v025_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slope_21d_2d_v026_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slope_63d_2d_v027_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slope_126d_2d_v028_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slope_252d_2d_v029_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slope_504d_2d_v030_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slope_21d_2d_v031_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slope_63d_2d_v032_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slope_126d_2d_v033_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slope_252d_2d_v034_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slope_504d_2d_v035_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sm21_sl21_2d_v036_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f006_quick_ratio(assetsc, inventory, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sm63_sl21_2d_v037_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f006_quick_ratio(assetsc, inventory, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sm63_sl63_2d_v038_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f006_quick_ratio(assetsc, inventory, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sm252_sl63_2d_v039_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f006_quick_ratio(assetsc, inventory, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sm252_sl126_2d_v040_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _mean(_f006_quick_ratio(assetsc, inventory, liabilitiesc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sm21_sl21_2d_v041_signal(cashneq, liabilitiesc, closeadj):
    base = _mean(_f006_cash_only_quick(cashneq, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sm63_sl21_2d_v042_signal(cashneq, liabilitiesc, closeadj):
    base = _mean(_f006_cash_only_quick(cashneq, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sm63_sl63_2d_v043_signal(cashneq, liabilitiesc, closeadj):
    base = _mean(_f006_cash_only_quick(cashneq, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sm252_sl63_2d_v044_signal(cashneq, liabilitiesc, closeadj):
    base = _mean(_f006_cash_only_quick(cashneq, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sm252_sl126_2d_v045_signal(cashneq, liabilitiesc, closeadj):
    base = _mean(_f006_cash_only_quick(cashneq, liabilitiesc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sm21_sl21_2d_v046_signal(assetsc, inventory, assets, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sm63_sl21_2d_v047_signal(assetsc, inventory, assets, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sm63_sl63_2d_v048_signal(assetsc, inventory, assets, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sm252_sl63_2d_v049_signal(assetsc, inventory, assets, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sm252_sl126_2d_v050_signal(assetsc, inventory, assets, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sm21_sl21_2d_v051_signal(inventory, assetsc, closeadj):
    base = _mean(inventory.fillna(0) / assetsc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sm63_sl21_2d_v052_signal(inventory, assetsc, closeadj):
    base = _mean(inventory.fillna(0) / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sm63_sl63_2d_v053_signal(inventory, assetsc, closeadj):
    base = _mean(inventory.fillna(0) / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sm252_sl63_2d_v054_signal(inventory, assetsc, closeadj):
    base = _mean(inventory.fillna(0) / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sm252_sl126_2d_v055_signal(inventory, assetsc, closeadj):
    base = _mean(inventory.fillna(0) / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sm21_sl21_2d_v056_signal(assetsc, inventory, marketcap, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sm63_sl21_2d_v057_signal(assetsc, inventory, marketcap, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sm63_sl63_2d_v058_signal(assetsc, inventory, marketcap, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sm252_sl63_2d_v059_signal(assetsc, inventory, marketcap, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sm252_sl126_2d_v060_signal(assetsc, inventory, marketcap, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sm21_sl21_2d_v061_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = _mean(liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sm63_sl21_2d_v062_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = _mean(liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sm63_sl63_2d_v063_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = _mean(liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sm252_sl63_2d_v064_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = _mean(liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sm252_sl126_2d_v065_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = _mean(liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sm21_sl21_2d_v066_signal(assetsc, inventory, revenue, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sm63_sl21_2d_v067_signal(assetsc, inventory, revenue, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sm63_sl63_2d_v068_signal(assetsc, inventory, revenue, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sm252_sl63_2d_v069_signal(assetsc, inventory, revenue, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sm252_sl126_2d_v070_signal(assetsc, inventory, revenue, closeadj):
    base = _mean(_f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_pctslope_21d_2d_v071_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_pctslope_63d_2d_v072_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_pctslope_252d_2d_v073_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_pctslope_21d_2d_v074_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_pctslope_63d_2d_v075_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_pctslope_252d_2d_v076_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_pctslope_21d_2d_v077_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_pctslope_63d_2d_v078_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_pctslope_252d_2d_v079_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_pctslope_21d_2d_v080_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_pctslope_63d_2d_v081_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_pctslope_252d_2d_v082_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_pctslope_21d_2d_v083_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_pctslope_63d_2d_v084_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_pctslope_252d_2d_v085_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_pctslope_21d_2d_v086_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_pctslope_63d_2d_v087_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_pctslope_252d_2d_v088_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_pctslope_21d_2d_v089_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_pctslope_63d_2d_v090_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_pctslope_252d_2d_v091_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sgnslope_21d_2d_v092_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sgnslope_63d_2d_v093_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_sgnslope_252d_2d_v094_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sgnslope_21d_2d_v095_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sgnslope_63d_2d_v096_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_sgnslope_252d_2d_v097_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sgnslope_21d_2d_v098_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sgnslope_63d_2d_v099_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_sgnslope_252d_2d_v100_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sgnslope_21d_2d_v101_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sgnslope_63d_2d_v102_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_sgnslope_252d_2d_v103_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sgnslope_21d_2d_v104_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sgnslope_63d_2d_v105_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_sgnslope_252d_2d_v106_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sgnslope_21d_2d_v107_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sgnslope_63d_2d_v108_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_sgnslope_252d_2d_v109_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sgnslope_21d_2d_v110_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sgnslope_63d_2d_v111_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_sgnslope_252d_2d_v112_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_logmagslope_21d_2d_v113_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_logmagslope_63d_2d_v114_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_logmagslope_252d_2d_v115_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_logmagslope_21d_2d_v116_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_logmagslope_63d_2d_v117_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_logmagslope_252d_2d_v118_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_logmagslope_21d_2d_v119_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_logmagslope_63d_2d_v120_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_logmagslope_252d_2d_v121_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_logmagslope_21d_2d_v122_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_logmagslope_63d_2d_v123_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_logmagslope_252d_2d_v124_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_logmagslope_21d_2d_v125_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_logmagslope_63d_2d_v126_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_logmagslope_252d_2d_v127_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_logmagslope_21d_2d_v128_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_logmagslope_63d_2d_v129_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_logmagslope_252d_2d_v130_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_logmagslope_21d_2d_v131_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_logmagslope_63d_2d_v132_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_logmagslope_252d_2d_v133_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|quick_ratio|
def f006ql_f006_quick_liquidity_quick_ratio_logslope_63d_2d_v134_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = np.log((_f006_quick_ratio(assetsc, inventory, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|quick_ratio|
def f006ql_f006_quick_liquidity_quick_ratio_logslope_252d_2d_v135_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = np.log((_f006_quick_ratio(assetsc, inventory, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|cash_only_quick|
def f006ql_f006_quick_liquidity_cash_only_quick_logslope_63d_2d_v136_signal(cashneq, liabilitiesc, closeadj):
    base = np.log((_f006_cash_only_quick(cashneq, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|cash_only_quick|
def f006ql_f006_quick_liquidity_cash_only_quick_logslope_252d_2d_v137_signal(cashneq, liabilitiesc, closeadj):
    base = np.log((_f006_cash_only_quick(cashneq, liabilitiesc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|qa_to_asset|
def f006ql_f006_quick_liquidity_qa_to_asset_logslope_63d_2d_v138_signal(assetsc, inventory, assets, closeadj):
    base = np.log((_f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|qa_to_asset|
def f006ql_f006_quick_liquidity_qa_to_asset_logslope_252d_2d_v139_signal(assetsc, inventory, assets, closeadj):
    base = np.log((_f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_share_curasset|
def f006ql_f006_quick_liquidity_inv_share_curasset_logslope_63d_2d_v140_signal(inventory, assetsc, closeadj):
    base = np.log((inventory.fillna(0) / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_share_curasset|
def f006ql_f006_quick_liquidity_inv_share_curasset_logslope_252d_2d_v141_signal(inventory, assetsc, closeadj):
    base = np.log((inventory.fillna(0) / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|qa_to_mcap|
def f006ql_f006_quick_liquidity_qa_to_mcap_logslope_63d_2d_v142_signal(assetsc, inventory, marketcap, closeadj):
    base = np.log((_f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|qa_to_mcap|
def f006ql_f006_quick_liquidity_qa_to_mcap_logslope_252d_2d_v143_signal(assetsc, inventory, marketcap, closeadj):
    base = np.log((_f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|liabc_to_qa|
def f006ql_f006_quick_liquidity_liabc_to_qa_logslope_63d_2d_v144_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = np.log((liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|liabc_to_qa|
def f006ql_f006_quick_liquidity_liabc_to_qa_logslope_252d_2d_v145_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = np.log((liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|qa_to_revenue|
def f006ql_f006_quick_liquidity_qa_to_revenue_logslope_63d_2d_v146_signal(assetsc, inventory, revenue, closeadj):
    base = np.log((_f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|qa_to_revenue|
def f006ql_f006_quick_liquidity_qa_to_revenue_logslope_252d_2d_v147_signal(assetsc, inventory, revenue, closeadj):
    base = np.log((_f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

