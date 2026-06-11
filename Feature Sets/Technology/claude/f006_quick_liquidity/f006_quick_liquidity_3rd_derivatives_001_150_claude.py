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


# 21d acceleration of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_accel_21d_3d_v001_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_accel_63d_3d_v002_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_accel_126d_3d_v003_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_accel_252d_3d_v004_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_accel_21d_3d_v005_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_accel_63d_3d_v006_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_accel_126d_3d_v007_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_accel_252d_3d_v008_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_accel_21d_3d_v009_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_accel_63d_3d_v010_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_accel_126d_3d_v011_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_accel_252d_3d_v012_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_accel_21d_3d_v013_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_accel_63d_3d_v014_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_accel_126d_3d_v015_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_accel_252d_3d_v016_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_accel_21d_3d_v017_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_accel_63d_3d_v018_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_accel_126d_3d_v019_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_accel_252d_3d_v020_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_accel_21d_3d_v021_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_accel_63d_3d_v022_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_accel_126d_3d_v023_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_accel_252d_3d_v024_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_accel_21d_3d_v025_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_accel_63d_3d_v026_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_accel_126d_3d_v027_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_accel_252d_3d_v028_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slopez_21d_z126_3d_v029_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slopez_63d_z252_3d_v030_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slopez_126d_z252_3d_v031_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_slopez_252d_z504_3d_v032_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slopez_21d_z126_3d_v033_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slopez_63d_z252_3d_v034_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slopez_126d_z252_3d_v035_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_slopez_252d_z504_3d_v036_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slopez_21d_z126_3d_v037_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slopez_63d_z252_3d_v038_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slopez_126d_z252_3d_v039_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_slopez_252d_z504_3d_v040_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slopez_21d_z126_3d_v041_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slopez_63d_z252_3d_v042_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slopez_126d_z252_3d_v043_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_slopez_252d_z504_3d_v044_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slopez_21d_z126_3d_v045_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slopez_63d_z252_3d_v046_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slopez_126d_z252_3d_v047_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_slopez_252d_z504_3d_v048_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slopez_21d_z126_3d_v049_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slopez_63d_z252_3d_v050_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slopez_126d_z252_3d_v051_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_slopez_252d_z504_3d_v052_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slopez_21d_z126_3d_v053_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slopez_63d_z252_3d_v054_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slopez_126d_z252_3d_v055_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_slopez_252d_z504_3d_v056_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_jerk_21d_3d_v057_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_jerk_63d_3d_v058_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_jerk_126d_3d_v059_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_jerk_21d_3d_v060_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_jerk_63d_3d_v061_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_jerk_126d_3d_v062_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_jerk_21d_3d_v063_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_jerk_63d_3d_v064_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_jerk_126d_3d_v065_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_jerk_21d_3d_v066_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_jerk_63d_3d_v067_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_jerk_126d_3d_v068_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_jerk_21d_3d_v069_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_jerk_63d_3d_v070_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_jerk_126d_3d_v071_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_jerk_21d_3d_v072_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_jerk_63d_3d_v073_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_jerk_126d_3d_v074_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_jerk_21d_3d_v075_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_jerk_63d_3d_v076_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_jerk_126d_3d_v077_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of quick_ratio smoothed over 252d
def f006ql_f006_quick_liquidity_quick_ratio_smoothaccel_63d_sm252_3d_v078_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of quick_ratio smoothed over 504d
def f006ql_f006_quick_liquidity_quick_ratio_smoothaccel_252d_sm504_3d_v079_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cash_only_quick smoothed over 252d
def f006ql_f006_quick_liquidity_cash_only_quick_smoothaccel_63d_sm252_3d_v080_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cash_only_quick smoothed over 504d
def f006ql_f006_quick_liquidity_cash_only_quick_smoothaccel_252d_sm504_3d_v081_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of qa_to_asset smoothed over 252d
def f006ql_f006_quick_liquidity_qa_to_asset_smoothaccel_63d_sm252_3d_v082_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of qa_to_asset smoothed over 504d
def f006ql_f006_quick_liquidity_qa_to_asset_smoothaccel_252d_sm504_3d_v083_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_share_curasset smoothed over 252d
def f006ql_f006_quick_liquidity_inv_share_curasset_smoothaccel_63d_sm252_3d_v084_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_share_curasset smoothed over 504d
def f006ql_f006_quick_liquidity_inv_share_curasset_smoothaccel_252d_sm504_3d_v085_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of qa_to_mcap smoothed over 252d
def f006ql_f006_quick_liquidity_qa_to_mcap_smoothaccel_63d_sm252_3d_v086_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of qa_to_mcap smoothed over 504d
def f006ql_f006_quick_liquidity_qa_to_mcap_smoothaccel_252d_sm504_3d_v087_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liabc_to_qa smoothed over 252d
def f006ql_f006_quick_liquidity_liabc_to_qa_smoothaccel_63d_sm252_3d_v088_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liabc_to_qa smoothed over 504d
def f006ql_f006_quick_liquidity_liabc_to_qa_smoothaccel_252d_sm504_3d_v089_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of qa_to_revenue smoothed over 252d
def f006ql_f006_quick_liquidity_qa_to_revenue_smoothaccel_63d_sm252_3d_v090_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of qa_to_revenue smoothed over 504d
def f006ql_f006_quick_liquidity_qa_to_revenue_smoothaccel_252d_sm504_3d_v091_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_accelz_21d_z252_3d_v092_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_accelz_63d_z504_3d_v093_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_accelz_21d_z252_3d_v094_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_accelz_63d_z504_3d_v095_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_accelz_21d_z252_3d_v096_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_accelz_63d_z504_3d_v097_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_accelz_21d_z252_3d_v098_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_accelz_63d_z504_3d_v099_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_accelz_21d_z252_3d_v100_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_accelz_63d_z504_3d_v101_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_accelz_21d_z252_3d_v102_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_accelz_63d_z504_3d_v103_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_accelz_21d_z252_3d_v104_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_accelz_63d_z504_3d_v105_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in quick_ratio (raw count, no price scaling)
def f006ql_f006_quick_liquidity_quick_ratio_signflip_63d_3d_v106_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in quick_ratio (raw count, no price scaling)
def f006ql_f006_quick_liquidity_quick_ratio_signflip_252d_3d_v107_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cash_only_quick (raw count, no price scaling)
def f006ql_f006_quick_liquidity_cash_only_quick_signflip_63d_3d_v108_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cash_only_quick (raw count, no price scaling)
def f006ql_f006_quick_liquidity_cash_only_quick_signflip_252d_3d_v109_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in qa_to_asset (raw count, no price scaling)
def f006ql_f006_quick_liquidity_qa_to_asset_signflip_63d_3d_v110_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in qa_to_asset (raw count, no price scaling)
def f006ql_f006_quick_liquidity_qa_to_asset_signflip_252d_3d_v111_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_share_curasset (raw count, no price scaling)
def f006ql_f006_quick_liquidity_inv_share_curasset_signflip_63d_3d_v112_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_share_curasset (raw count, no price scaling)
def f006ql_f006_quick_liquidity_inv_share_curasset_signflip_252d_3d_v113_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in qa_to_mcap (raw count, no price scaling)
def f006ql_f006_quick_liquidity_qa_to_mcap_signflip_63d_3d_v114_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in qa_to_mcap (raw count, no price scaling)
def f006ql_f006_quick_liquidity_qa_to_mcap_signflip_252d_3d_v115_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liabc_to_qa (raw count, no price scaling)
def f006ql_f006_quick_liquidity_liabc_to_qa_signflip_63d_3d_v116_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liabc_to_qa (raw count, no price scaling)
def f006ql_f006_quick_liquidity_liabc_to_qa_signflip_252d_3d_v117_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in qa_to_revenue (raw count, no price scaling)
def f006ql_f006_quick_liquidity_qa_to_revenue_signflip_63d_3d_v118_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in qa_to_revenue (raw count, no price scaling)
def f006ql_f006_quick_liquidity_qa_to_revenue_signflip_252d_3d_v119_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quick_ratio normalized by 252d range
def f006ql_f006_quick_liquidity_quick_ratio_rngaccel_63d_r252_3d_v120_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quick_ratio normalized by 504d range
def f006ql_f006_quick_liquidity_quick_ratio_rngaccel_252d_r504_3d_v121_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cash_only_quick normalized by 252d range
def f006ql_f006_quick_liquidity_cash_only_quick_rngaccel_63d_r252_3d_v122_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cash_only_quick normalized by 504d range
def f006ql_f006_quick_liquidity_cash_only_quick_rngaccel_252d_r504_3d_v123_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qa_to_asset normalized by 252d range
def f006ql_f006_quick_liquidity_qa_to_asset_rngaccel_63d_r252_3d_v124_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qa_to_asset normalized by 504d range
def f006ql_f006_quick_liquidity_qa_to_asset_rngaccel_252d_r504_3d_v125_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_share_curasset normalized by 252d range
def f006ql_f006_quick_liquidity_inv_share_curasset_rngaccel_63d_r252_3d_v126_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_share_curasset normalized by 504d range
def f006ql_f006_quick_liquidity_inv_share_curasset_rngaccel_252d_r504_3d_v127_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qa_to_mcap normalized by 252d range
def f006ql_f006_quick_liquidity_qa_to_mcap_rngaccel_63d_r252_3d_v128_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qa_to_mcap normalized by 504d range
def f006ql_f006_quick_liquidity_qa_to_mcap_rngaccel_252d_r504_3d_v129_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liabc_to_qa normalized by 252d range
def f006ql_f006_quick_liquidity_liabc_to_qa_rngaccel_63d_r252_3d_v130_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liabc_to_qa normalized by 504d range
def f006ql_f006_quick_liquidity_liabc_to_qa_rngaccel_252d_r504_3d_v131_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qa_to_revenue normalized by 252d range
def f006ql_f006_quick_liquidity_qa_to_revenue_rngaccel_63d_r252_3d_v132_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qa_to_revenue normalized by 504d range
def f006ql_f006_quick_liquidity_qa_to_revenue_rngaccel_252d_r504_3d_v133_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_cumslope_21d_3d_v134_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_cumslope_63d_3d_v135_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_cumslope_252d_3d_v136_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_cumslope_21d_3d_v137_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_cumslope_63d_3d_v138_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_cumslope_252d_3d_v139_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_cumslope_21d_3d_v140_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_cumslope_63d_3d_v141_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_cumslope_252d_3d_v142_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_cumslope_21d_3d_v143_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_cumslope_63d_3d_v144_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_cumslope_252d_3d_v145_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_cumslope_21d_3d_v146_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_cumslope_63d_3d_v147_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_cumslope_252d_3d_v148_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_cumslope_21d_3d_v149_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_cumslope_63d_3d_v150_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

