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


# 21d acceleration of curratio
def f005cl_f005_current_liquidity_curratio_accel_21d_3d_v001_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of curratio
def f005cl_f005_current_liquidity_curratio_accel_63d_3d_v002_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of curratio
def f005cl_f005_current_liquidity_curratio_accel_126d_3d_v003_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of curratio
def f005cl_f005_current_liquidity_curratio_accel_252d_3d_v004_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_accel_21d_3d_v005_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_accel_63d_3d_v006_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_accel_126d_3d_v007_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_accel_252d_3d_v008_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cashquick
def f005cl_f005_current_liquidity_cashquick_accel_21d_3d_v009_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashquick
def f005cl_f005_current_liquidity_cashquick_accel_63d_3d_v010_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cashquick
def f005cl_f005_current_liquidity_cashquick_accel_126d_3d_v011_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashquick
def f005cl_f005_current_liquidity_cashquick_accel_252d_3d_v012_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_accel_21d_3d_v013_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_accel_63d_3d_v014_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_accel_126d_3d_v015_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_accel_252d_3d_v016_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_accel_21d_3d_v017_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_accel_63d_3d_v018_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_accel_126d_3d_v019_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_accel_252d_3d_v020_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_accel_21d_3d_v021_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_accel_63d_3d_v022_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_accel_126d_3d_v023_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_accel_252d_3d_v024_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_accel_21d_3d_v025_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_accel_63d_3d_v026_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_accel_126d_3d_v027_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_accel_252d_3d_v028_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of curratio
def f005cl_f005_current_liquidity_curratio_slopez_21d_z126_3d_v029_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of curratio
def f005cl_f005_current_liquidity_curratio_slopez_63d_z252_3d_v030_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of curratio
def f005cl_f005_current_liquidity_curratio_slopez_126d_z252_3d_v031_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of curratio
def f005cl_f005_current_liquidity_curratio_slopez_252d_z504_3d_v032_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slopez_21d_z126_3d_v033_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slopez_63d_z252_3d_v034_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slopez_126d_z252_3d_v035_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_slopez_252d_z504_3d_v036_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cashquick
def f005cl_f005_current_liquidity_cashquick_slopez_21d_z126_3d_v037_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cashquick
def f005cl_f005_current_liquidity_cashquick_slopez_63d_z252_3d_v038_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cashquick
def f005cl_f005_current_liquidity_cashquick_slopez_126d_z252_3d_v039_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cashquick
def f005cl_f005_current_liquidity_cashquick_slopez_252d_z504_3d_v040_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slopez_21d_z126_3d_v041_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slopez_63d_z252_3d_v042_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slopez_126d_z252_3d_v043_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_slopez_252d_z504_3d_v044_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slopez_21d_z126_3d_v045_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slopez_63d_z252_3d_v046_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slopez_126d_z252_3d_v047_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_slopez_252d_z504_3d_v048_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slopez_21d_z126_3d_v049_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slopez_63d_z252_3d_v050_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slopez_126d_z252_3d_v051_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_slopez_252d_z504_3d_v052_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slopez_21d_z126_3d_v053_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slopez_63d_z252_3d_v054_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slopez_126d_z252_3d_v055_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_slopez_252d_z504_3d_v056_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of curratio
def f005cl_f005_current_liquidity_curratio_jerk_21d_3d_v057_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of curratio
def f005cl_f005_current_liquidity_curratio_jerk_63d_3d_v058_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of curratio
def f005cl_f005_current_liquidity_curratio_jerk_126d_3d_v059_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_jerk_21d_3d_v060_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_jerk_63d_3d_v061_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_jerk_126d_3d_v062_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cashquick
def f005cl_f005_current_liquidity_cashquick_jerk_21d_3d_v063_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cashquick
def f005cl_f005_current_liquidity_cashquick_jerk_63d_3d_v064_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cashquick
def f005cl_f005_current_liquidity_cashquick_jerk_126d_3d_v065_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_jerk_21d_3d_v066_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_jerk_63d_3d_v067_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_jerk_126d_3d_v068_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_jerk_21d_3d_v069_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_jerk_63d_3d_v070_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_jerk_126d_3d_v071_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_jerk_21d_3d_v072_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_jerk_63d_3d_v073_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_jerk_126d_3d_v074_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_jerk_21d_3d_v075_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_jerk_63d_3d_v076_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_jerk_126d_3d_v077_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of curratio smoothed over 252d
def f005cl_f005_current_liquidity_curratio_smoothaccel_63d_sm252_3d_v078_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of curratio smoothed over 504d
def f005cl_f005_current_liquidity_curratio_smoothaccel_252d_sm504_3d_v079_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of qac_ratio smoothed over 252d
def f005cl_f005_current_liquidity_qac_ratio_smoothaccel_63d_sm252_3d_v080_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of qac_ratio smoothed over 504d
def f005cl_f005_current_liquidity_qac_ratio_smoothaccel_252d_sm504_3d_v081_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of cashquick smoothed over 252d
def f005cl_f005_current_liquidity_cashquick_smoothaccel_63d_sm252_3d_v082_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of cashquick smoothed over 504d
def f005cl_f005_current_liquidity_cashquick_smoothaccel_252d_sm504_3d_v083_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netwc_to_asset smoothed over 252d
def f005cl_f005_current_liquidity_netwc_to_asset_smoothaccel_63d_sm252_3d_v084_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netwc_to_asset smoothed over 504d
def f005cl_f005_current_liquidity_netwc_to_asset_smoothaccel_252d_sm504_3d_v085_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netwc_to_mcap smoothed over 252d
def f005cl_f005_current_liquidity_netwc_to_mcap_smoothaccel_63d_sm252_3d_v086_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netwc_to_mcap smoothed over 504d
def f005cl_f005_current_liquidity_netwc_to_mcap_smoothaccel_252d_sm504_3d_v087_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of liabc_to_asset smoothed over 252d
def f005cl_f005_current_liquidity_liabc_to_asset_smoothaccel_63d_sm252_3d_v088_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of liabc_to_asset smoothed over 504d
def f005cl_f005_current_liquidity_liabc_to_asset_smoothaccel_252d_sm504_3d_v089_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of curratio_minus_1 smoothed over 252d
def f005cl_f005_current_liquidity_curratio_minus_1_smoothaccel_63d_sm252_3d_v090_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of curratio_minus_1 smoothed over 504d
def f005cl_f005_current_liquidity_curratio_minus_1_smoothaccel_252d_sm504_3d_v091_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of curratio
def f005cl_f005_current_liquidity_curratio_accelz_21d_z252_3d_v092_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of curratio
def f005cl_f005_current_liquidity_curratio_accelz_63d_z504_3d_v093_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_accelz_21d_z252_3d_v094_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_accelz_63d_z504_3d_v095_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of cashquick
def f005cl_f005_current_liquidity_cashquick_accelz_21d_z252_3d_v096_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of cashquick
def f005cl_f005_current_liquidity_cashquick_accelz_63d_z504_3d_v097_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_accelz_21d_z252_3d_v098_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_accelz_63d_z504_3d_v099_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_accelz_21d_z252_3d_v100_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_accelz_63d_z504_3d_v101_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_accelz_21d_z252_3d_v102_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_accelz_63d_z504_3d_v103_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_accelz_21d_z252_3d_v104_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of curratio_minus_1
def f005cl_f005_current_liquidity_curratio_minus_1_accelz_63d_z504_3d_v105_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in curratio (raw count, no price scaling)
def f005cl_f005_current_liquidity_curratio_signflip_63d_3d_v106_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in curratio (raw count, no price scaling)
def f005cl_f005_current_liquidity_curratio_signflip_252d_3d_v107_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in qac_ratio (raw count, no price scaling)
def f005cl_f005_current_liquidity_qac_ratio_signflip_63d_3d_v108_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in qac_ratio (raw count, no price scaling)
def f005cl_f005_current_liquidity_qac_ratio_signflip_252d_3d_v109_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in cashquick (raw count, no price scaling)
def f005cl_f005_current_liquidity_cashquick_signflip_63d_3d_v110_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in cashquick (raw count, no price scaling)
def f005cl_f005_current_liquidity_cashquick_signflip_252d_3d_v111_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netwc_to_asset (raw count, no price scaling)
def f005cl_f005_current_liquidity_netwc_to_asset_signflip_63d_3d_v112_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netwc_to_asset (raw count, no price scaling)
def f005cl_f005_current_liquidity_netwc_to_asset_signflip_252d_3d_v113_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netwc_to_mcap (raw count, no price scaling)
def f005cl_f005_current_liquidity_netwc_to_mcap_signflip_63d_3d_v114_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netwc_to_mcap (raw count, no price scaling)
def f005cl_f005_current_liquidity_netwc_to_mcap_signflip_252d_3d_v115_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in liabc_to_asset (raw count, no price scaling)
def f005cl_f005_current_liquidity_liabc_to_asset_signflip_63d_3d_v116_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in liabc_to_asset (raw count, no price scaling)
def f005cl_f005_current_liquidity_liabc_to_asset_signflip_252d_3d_v117_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in curratio_minus_1 (raw count, no price scaling)
def f005cl_f005_current_liquidity_curratio_minus_1_signflip_63d_3d_v118_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in curratio_minus_1 (raw count, no price scaling)
def f005cl_f005_current_liquidity_curratio_minus_1_signflip_252d_3d_v119_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of curratio normalized by 252d range
def f005cl_f005_current_liquidity_curratio_rngaccel_63d_r252_3d_v120_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of curratio normalized by 504d range
def f005cl_f005_current_liquidity_curratio_rngaccel_252d_r504_3d_v121_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of qac_ratio normalized by 252d range
def f005cl_f005_current_liquidity_qac_ratio_rngaccel_63d_r252_3d_v122_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of qac_ratio normalized by 504d range
def f005cl_f005_current_liquidity_qac_ratio_rngaccel_252d_r504_3d_v123_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cashquick normalized by 252d range
def f005cl_f005_current_liquidity_cashquick_rngaccel_63d_r252_3d_v124_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cashquick normalized by 504d range
def f005cl_f005_current_liquidity_cashquick_rngaccel_252d_r504_3d_v125_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netwc_to_asset normalized by 252d range
def f005cl_f005_current_liquidity_netwc_to_asset_rngaccel_63d_r252_3d_v126_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netwc_to_asset normalized by 504d range
def f005cl_f005_current_liquidity_netwc_to_asset_rngaccel_252d_r504_3d_v127_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netwc_to_mcap normalized by 252d range
def f005cl_f005_current_liquidity_netwc_to_mcap_rngaccel_63d_r252_3d_v128_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netwc_to_mcap normalized by 504d range
def f005cl_f005_current_liquidity_netwc_to_mcap_rngaccel_252d_r504_3d_v129_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of liabc_to_asset normalized by 252d range
def f005cl_f005_current_liquidity_liabc_to_asset_rngaccel_63d_r252_3d_v130_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of liabc_to_asset normalized by 504d range
def f005cl_f005_current_liquidity_liabc_to_asset_rngaccel_252d_r504_3d_v131_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of curratio_minus_1 normalized by 252d range
def f005cl_f005_current_liquidity_curratio_minus_1_rngaccel_63d_r252_3d_v132_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of curratio_minus_1 normalized by 504d range
def f005cl_f005_current_liquidity_curratio_minus_1_rngaccel_252d_r504_3d_v133_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of curratio
def f005cl_f005_current_liquidity_curratio_cumslope_21d_3d_v134_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of curratio
def f005cl_f005_current_liquidity_curratio_cumslope_63d_3d_v135_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of curratio
def f005cl_f005_current_liquidity_curratio_cumslope_252d_3d_v136_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_cumslope_21d_3d_v137_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_cumslope_63d_3d_v138_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of qac_ratio
def f005cl_f005_current_liquidity_qac_ratio_cumslope_252d_3d_v139_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of cashquick
def f005cl_f005_current_liquidity_cashquick_cumslope_21d_3d_v140_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of cashquick
def f005cl_f005_current_liquidity_cashquick_cumslope_63d_3d_v141_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of cashquick
def f005cl_f005_current_liquidity_cashquick_cumslope_252d_3d_v142_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_cumslope_21d_3d_v143_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_cumslope_63d_3d_v144_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of netwc_to_asset
def f005cl_f005_current_liquidity_netwc_to_asset_cumslope_252d_3d_v145_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_cumslope_21d_3d_v146_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_cumslope_63d_3d_v147_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of netwc_to_mcap
def f005cl_f005_current_liquidity_netwc_to_mcap_cumslope_252d_3d_v148_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_cumslope_21d_3d_v149_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of liabc_to_asset
def f005cl_f005_current_liquidity_liabc_to_asset_cumslope_63d_3d_v150_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

