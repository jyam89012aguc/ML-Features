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
def _f006_quick_assets(assetsc, inventory):
    return assetsc - inventory.fillna(0)


def _f006_quick_ratio(assetsc, inventory, liabilitiesc):
    qa = assetsc - inventory.fillna(0)
    return qa / liabilitiesc.replace(0, np.nan).abs()


def _f006_cash_only_quick(cashneq, liabilitiesc):
    return cashneq / liabilitiesc.replace(0, np.nan).abs()


# 63d z-score of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_z_63d_base_v076_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_z_126d_base_v077_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_z_252d_base_v078_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_z_504d_base_v079_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_z_63d_base_v080_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_z_126d_base_v081_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_z_252d_base_v082_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_z_504d_base_v083_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_z_63d_base_v084_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_z_126d_base_v085_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_z_252d_base_v086_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_z_504d_base_v087_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_z_63d_base_v088_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_z_126d_base_v089_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_z_252d_base_v090_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_z_504d_base_v091_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_z_63d_base_v092_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_z_126d_base_v093_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_z_252d_base_v094_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_z_504d_base_v095_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_z_63d_base_v096_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_z_126d_base_v097_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_z_252d_base_v098_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_z_504d_base_v099_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_z_63d_base_v100_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_z_126d_base_v101_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_z_252d_base_v102_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_z_504d_base_v103_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_distmax_252d_base_v104_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_distmax_504d_base_v105_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_distmax_252d_base_v106_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_distmax_504d_base_v107_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_distmax_252d_base_v108_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_distmax_504d_base_v109_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_distmax_252d_base_v110_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_distmax_504d_base_v111_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_distmax_252d_base_v112_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_distmax_504d_base_v113_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_distmax_252d_base_v114_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_distmax_504d_base_v115_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_distmax_252d_base_v116_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_distmax_504d_base_v117_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_distmed_126d_base_v118_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_distmed_252d_base_v119_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_distmed_504d_base_v120_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_distmed_126d_base_v121_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_distmed_252d_base_v122_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_distmed_504d_base_v123_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_distmed_126d_base_v124_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_distmed_252d_base_v125_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_distmed_504d_base_v126_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_distmed_126d_base_v127_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_distmed_252d_base_v128_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_distmed_504d_base_v129_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_distmed_126d_base_v130_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_distmed_252d_base_v131_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_distmed_504d_base_v132_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_distmed_126d_base_v133_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_distmed_252d_base_v134_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_distmed_504d_base_v135_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_distmed_126d_base_v136_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_distmed_252d_base_v137_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of qa_to_revenue
def f006ql_f006_quick_liquidity_qa_to_revenue_distmed_504d_base_v138_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_chg_63d_base_v139_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in quick_ratio
def f006ql_f006_quick_liquidity_quick_ratio_chg_252d_base_v140_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_chg_63d_base_v141_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in cash_only_quick
def f006ql_f006_quick_liquidity_cash_only_quick_chg_252d_base_v142_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_chg_63d_base_v143_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in qa_to_asset
def f006ql_f006_quick_liquidity_qa_to_asset_chg_252d_base_v144_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_chg_63d_base_v145_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in inv_share_curasset
def f006ql_f006_quick_liquidity_inv_share_curasset_chg_252d_base_v146_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_chg_63d_base_v147_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in qa_to_mcap
def f006ql_f006_quick_liquidity_qa_to_mcap_chg_252d_base_v148_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_chg_63d_base_v149_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in liabc_to_qa
def f006ql_f006_quick_liquidity_liabc_to_qa_chg_252d_base_v150_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

