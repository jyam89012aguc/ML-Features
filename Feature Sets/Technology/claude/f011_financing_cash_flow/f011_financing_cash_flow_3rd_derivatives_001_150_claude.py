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
def _f011_fin_to_asset(ncff, assets):
    return ncff / assets.replace(0, np.nan).abs()


def _f011_equity_share(ncfcommon, ncff):
    return ncfcommon / ncff.replace(0, np.nan).abs()


def _f011_debt_share(ncfdebt, ncff):
    return ncfdebt / ncff.replace(0, np.nan).abs()


# 21d acceleration of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_accel_21d_3d_v001_signal(ncff, closeadj):
    base = ncff
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_accel_63d_3d_v002_signal(ncff, closeadj):
    base = ncff
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_accel_126d_3d_v003_signal(ncff, closeadj):
    base = ncff
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_accel_252d_3d_v004_signal(ncff, closeadj):
    base = ncff
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_accel_21d_3d_v005_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_accel_63d_3d_v006_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_accel_126d_3d_v007_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_accel_252d_3d_v008_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_accel_21d_3d_v009_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_accel_63d_3d_v010_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_accel_126d_3d_v011_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_accel_252d_3d_v012_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_accel_21d_3d_v013_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_accel_63d_3d_v014_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_accel_126d_3d_v015_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_accel_252d_3d_v016_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_accel_21d_3d_v017_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_accel_63d_3d_v018_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_accel_126d_3d_v019_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_accel_252d_3d_v020_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_accel_21d_3d_v021_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_accel_63d_3d_v022_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_accel_126d_3d_v023_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_accel_252d_3d_v024_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_accel_21d_3d_v025_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_accel_63d_3d_v026_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_accel_126d_3d_v027_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_accel_252d_3d_v028_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_accel_21d_3d_v029_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_accel_63d_3d_v030_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_accel_126d_3d_v031_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_accel_252d_3d_v032_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slopez_21d_z126_3d_v033_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slopez_63d_z252_3d_v034_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slopez_126d_z252_3d_v035_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slopez_252d_z504_3d_v036_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slopez_21d_z126_3d_v037_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slopez_63d_z252_3d_v038_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slopez_126d_z252_3d_v039_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slopez_252d_z504_3d_v040_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slopez_21d_z126_3d_v041_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slopez_63d_z252_3d_v042_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slopez_126d_z252_3d_v043_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slopez_252d_z504_3d_v044_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slopez_21d_z126_3d_v045_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slopez_63d_z252_3d_v046_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slopez_126d_z252_3d_v047_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slopez_252d_z504_3d_v048_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slopez_21d_z126_3d_v049_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slopez_63d_z252_3d_v050_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slopez_126d_z252_3d_v051_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slopez_252d_z504_3d_v052_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slopez_21d_z126_3d_v053_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slopez_63d_z252_3d_v054_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slopez_126d_z252_3d_v055_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slopez_252d_z504_3d_v056_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slopez_21d_z126_3d_v057_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slopez_63d_z252_3d_v058_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slopez_126d_z252_3d_v059_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slopez_252d_z504_3d_v060_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slopez_21d_z126_3d_v061_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slopez_63d_z252_3d_v062_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slopez_126d_z252_3d_v063_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slopez_252d_z504_3d_v064_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_jerk_21d_3d_v065_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_jerk_63d_3d_v066_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_jerk_126d_3d_v067_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_jerk_21d_3d_v068_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_jerk_63d_3d_v069_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_jerk_126d_3d_v070_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_jerk_21d_3d_v071_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_jerk_63d_3d_v072_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_jerk_126d_3d_v073_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_jerk_21d_3d_v074_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_jerk_63d_3d_v075_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_jerk_126d_3d_v076_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_jerk_21d_3d_v077_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_jerk_63d_3d_v078_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_jerk_126d_3d_v079_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_jerk_21d_3d_v080_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_jerk_63d_3d_v081_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_jerk_126d_3d_v082_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_jerk_21d_3d_v083_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_jerk_63d_3d_v084_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_jerk_126d_3d_v085_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_jerk_21d_3d_v086_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_jerk_63d_3d_v087_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_jerk_126d_3d_v088_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncff_lvl smoothed over 252d
def f011fnc_f011_financing_cash_flow_ncff_lvl_smoothaccel_63d_sm252_3d_v089_signal(ncff, closeadj):
    base = ncff
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncff_lvl smoothed over 504d
def f011fnc_f011_financing_cash_flow_ncff_lvl_smoothaccel_252d_sm504_3d_v090_signal(ncff, closeadj):
    base = ncff
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncff_to_asset smoothed over 252d
def f011fnc_f011_financing_cash_flow_ncff_to_asset_smoothaccel_63d_sm252_3d_v091_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncff_to_asset smoothed over 504d
def f011fnc_f011_financing_cash_flow_ncff_to_asset_smoothaccel_252d_sm504_3d_v092_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncfcommon_lvl smoothed over 252d
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_smoothaccel_63d_sm252_3d_v093_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncfcommon_lvl smoothed over 504d
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_smoothaccel_252d_sm504_3d_v094_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncfdebt_lvl smoothed over 252d
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_smoothaccel_63d_sm252_3d_v095_signal(ncfdebt, closeadj):
    base = ncfdebt
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncfdebt_lvl smoothed over 504d
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_smoothaccel_252d_sm504_3d_v096_signal(ncfdebt, closeadj):
    base = ncfdebt
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncfdiv_lvl smoothed over 252d
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_smoothaccel_63d_sm252_3d_v097_signal(ncfdiv, closeadj):
    base = ncfdiv
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncfdiv_lvl smoothed over 504d
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_smoothaccel_252d_sm504_3d_v098_signal(ncfdiv, closeadj):
    base = ncfdiv
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of equity_share_fin smoothed over 252d
def f011fnc_f011_financing_cash_flow_equity_share_fin_smoothaccel_63d_sm252_3d_v099_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of equity_share_fin smoothed over 504d
def f011fnc_f011_financing_cash_flow_equity_share_fin_smoothaccel_252d_sm504_3d_v100_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debt_share_fin smoothed over 252d
def f011fnc_f011_financing_cash_flow_debt_share_fin_smoothaccel_63d_sm252_3d_v101_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debt_share_fin smoothed over 504d
def f011fnc_f011_financing_cash_flow_debt_share_fin_smoothaccel_252d_sm504_3d_v102_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncff_to_mcap smoothed over 252d
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_smoothaccel_63d_sm252_3d_v103_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncff_to_mcap smoothed over 504d
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_smoothaccel_252d_sm504_3d_v104_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_accelz_21d_z252_3d_v105_signal(ncff, closeadj):
    base = ncff
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_accelz_63d_z504_3d_v106_signal(ncff, closeadj):
    base = ncff
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_accelz_21d_z252_3d_v107_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_accelz_63d_z504_3d_v108_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_accelz_21d_z252_3d_v109_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_accelz_63d_z504_3d_v110_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_accelz_21d_z252_3d_v111_signal(ncfdebt, closeadj):
    base = ncfdebt
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_accelz_63d_z504_3d_v112_signal(ncfdebt, closeadj):
    base = ncfdebt
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_accelz_21d_z252_3d_v113_signal(ncfdiv, closeadj):
    base = ncfdiv
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_accelz_63d_z504_3d_v114_signal(ncfdiv, closeadj):
    base = ncfdiv
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_accelz_21d_z252_3d_v115_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_accelz_63d_z504_3d_v116_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_accelz_21d_z252_3d_v117_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_accelz_63d_z504_3d_v118_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_accelz_21d_z252_3d_v119_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_accelz_63d_z504_3d_v120_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncff_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncff_lvl_signflip_63d_3d_v121_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncff_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncff_lvl_signflip_252d_3d_v122_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncff_to_asset (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncff_to_asset_signflip_63d_3d_v123_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncff_to_asset (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncff_to_asset_signflip_252d_3d_v124_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncfcommon_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_signflip_63d_3d_v125_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncfcommon_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_signflip_252d_3d_v126_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncfdebt_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_signflip_63d_3d_v127_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncfdebt_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_signflip_252d_3d_v128_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncfdiv_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_signflip_63d_3d_v129_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncfdiv_lvl (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_signflip_252d_3d_v130_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in equity_share_fin (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_equity_share_fin_signflip_63d_3d_v131_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in equity_share_fin (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_equity_share_fin_signflip_252d_3d_v132_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debt_share_fin (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_debt_share_fin_signflip_63d_3d_v133_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debt_share_fin (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_debt_share_fin_signflip_252d_3d_v134_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncff_to_mcap (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_signflip_63d_3d_v135_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncff_to_mcap (raw count, no price scaling)
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_signflip_252d_3d_v136_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncff_lvl normalized by 252d range
def f011fnc_f011_financing_cash_flow_ncff_lvl_rngaccel_63d_r252_3d_v137_signal(ncff, closeadj):
    base = ncff
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncff_lvl normalized by 504d range
def f011fnc_f011_financing_cash_flow_ncff_lvl_rngaccel_252d_r504_3d_v138_signal(ncff, closeadj):
    base = ncff
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncff_to_asset normalized by 252d range
def f011fnc_f011_financing_cash_flow_ncff_to_asset_rngaccel_63d_r252_3d_v139_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncff_to_asset normalized by 504d range
def f011fnc_f011_financing_cash_flow_ncff_to_asset_rngaccel_252d_r504_3d_v140_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfcommon_lvl normalized by 252d range
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_rngaccel_63d_r252_3d_v141_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfcommon_lvl normalized by 504d range
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_rngaccel_252d_r504_3d_v142_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfdebt_lvl normalized by 252d range
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_rngaccel_63d_r252_3d_v143_signal(ncfdebt, closeadj):
    base = ncfdebt
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfdebt_lvl normalized by 504d range
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_rngaccel_252d_r504_3d_v144_signal(ncfdebt, closeadj):
    base = ncfdebt
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfdiv_lvl normalized by 252d range
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_rngaccel_63d_r252_3d_v145_signal(ncfdiv, closeadj):
    base = ncfdiv
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfdiv_lvl normalized by 504d range
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_rngaccel_252d_r504_3d_v146_signal(ncfdiv, closeadj):
    base = ncfdiv
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of equity_share_fin normalized by 252d range
def f011fnc_f011_financing_cash_flow_equity_share_fin_rngaccel_63d_r252_3d_v147_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of equity_share_fin normalized by 504d range
def f011fnc_f011_financing_cash_flow_equity_share_fin_rngaccel_252d_r504_3d_v148_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debt_share_fin normalized by 252d range
def f011fnc_f011_financing_cash_flow_debt_share_fin_rngaccel_63d_r252_3d_v149_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debt_share_fin normalized by 504d range
def f011fnc_f011_financing_cash_flow_debt_share_fin_rngaccel_252d_r504_3d_v150_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

