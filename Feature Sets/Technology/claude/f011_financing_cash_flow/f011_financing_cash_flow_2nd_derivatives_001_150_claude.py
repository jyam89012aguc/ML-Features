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


# 21d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slope_21d_2d_v001_signal(ncff, closeadj):
    base = ncff
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slope_63d_2d_v002_signal(ncff, closeadj):
    base = ncff
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slope_126d_2d_v003_signal(ncff, closeadj):
    base = ncff
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slope_252d_2d_v004_signal(ncff, closeadj):
    base = ncff
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_slope_504d_2d_v005_signal(ncff, closeadj):
    base = ncff
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slope_21d_2d_v006_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slope_63d_2d_v007_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slope_126d_2d_v008_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slope_252d_2d_v009_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_slope_504d_2d_v010_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slope_21d_2d_v011_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slope_63d_2d_v012_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slope_126d_2d_v013_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slope_252d_2d_v014_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_slope_504d_2d_v015_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slope_21d_2d_v016_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slope_63d_2d_v017_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slope_126d_2d_v018_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slope_252d_2d_v019_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_slope_504d_2d_v020_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slope_21d_2d_v021_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slope_63d_2d_v022_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slope_126d_2d_v023_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slope_252d_2d_v024_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_slope_504d_2d_v025_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slope_21d_2d_v026_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slope_63d_2d_v027_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slope_126d_2d_v028_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slope_252d_2d_v029_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_slope_504d_2d_v030_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slope_21d_2d_v031_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slope_63d_2d_v032_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slope_126d_2d_v033_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slope_252d_2d_v034_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_slope_504d_2d_v035_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slope_21d_2d_v036_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slope_63d_2d_v037_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slope_126d_2d_v038_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slope_252d_2d_v039_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_slope_504d_2d_v040_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sm21_sl21_2d_v041_signal(ncff, closeadj):
    base = _mean(ncff, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sm63_sl21_2d_v042_signal(ncff, closeadj):
    base = _mean(ncff, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sm63_sl63_2d_v043_signal(ncff, closeadj):
    base = _mean(ncff, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sm252_sl63_2d_v044_signal(ncff, closeadj):
    base = _mean(ncff, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sm252_sl126_2d_v045_signal(ncff, closeadj):
    base = _mean(ncff, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sm21_sl21_2d_v046_signal(ncff, assets, closeadj):
    base = _mean(_f011_fin_to_asset(ncff, assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sm63_sl21_2d_v047_signal(ncff, assets, closeadj):
    base = _mean(_f011_fin_to_asset(ncff, assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sm63_sl63_2d_v048_signal(ncff, assets, closeadj):
    base = _mean(_f011_fin_to_asset(ncff, assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sm252_sl63_2d_v049_signal(ncff, assets, closeadj):
    base = _mean(_f011_fin_to_asset(ncff, assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sm252_sl126_2d_v050_signal(ncff, assets, closeadj):
    base = _mean(_f011_fin_to_asset(ncff, assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sm21_sl21_2d_v051_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sm63_sl21_2d_v052_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sm63_sl63_2d_v053_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sm252_sl63_2d_v054_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sm252_sl126_2d_v055_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sm21_sl21_2d_v056_signal(ncfdebt, closeadj):
    base = _mean(ncfdebt, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sm63_sl21_2d_v057_signal(ncfdebt, closeadj):
    base = _mean(ncfdebt, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sm63_sl63_2d_v058_signal(ncfdebt, closeadj):
    base = _mean(ncfdebt, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sm252_sl63_2d_v059_signal(ncfdebt, closeadj):
    base = _mean(ncfdebt, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sm252_sl126_2d_v060_signal(ncfdebt, closeadj):
    base = _mean(ncfdebt, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sm21_sl21_2d_v061_signal(ncfdiv, closeadj):
    base = _mean(ncfdiv, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sm63_sl21_2d_v062_signal(ncfdiv, closeadj):
    base = _mean(ncfdiv, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sm63_sl63_2d_v063_signal(ncfdiv, closeadj):
    base = _mean(ncfdiv, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sm252_sl63_2d_v064_signal(ncfdiv, closeadj):
    base = _mean(ncfdiv, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sm252_sl126_2d_v065_signal(ncfdiv, closeadj):
    base = _mean(ncfdiv, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sm21_sl21_2d_v066_signal(ncfcommon, ncff, closeadj):
    base = _mean(_f011_equity_share(ncfcommon, ncff), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sm63_sl21_2d_v067_signal(ncfcommon, ncff, closeadj):
    base = _mean(_f011_equity_share(ncfcommon, ncff), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sm63_sl63_2d_v068_signal(ncfcommon, ncff, closeadj):
    base = _mean(_f011_equity_share(ncfcommon, ncff), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sm252_sl63_2d_v069_signal(ncfcommon, ncff, closeadj):
    base = _mean(_f011_equity_share(ncfcommon, ncff), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sm252_sl126_2d_v070_signal(ncfcommon, ncff, closeadj):
    base = _mean(_f011_equity_share(ncfcommon, ncff), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sm21_sl21_2d_v071_signal(ncfdebt, ncff, closeadj):
    base = _mean(_f011_debt_share(ncfdebt, ncff), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sm63_sl21_2d_v072_signal(ncfdebt, ncff, closeadj):
    base = _mean(_f011_debt_share(ncfdebt, ncff), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sm63_sl63_2d_v073_signal(ncfdebt, ncff, closeadj):
    base = _mean(_f011_debt_share(ncfdebt, ncff), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sm252_sl63_2d_v074_signal(ncfdebt, ncff, closeadj):
    base = _mean(_f011_debt_share(ncfdebt, ncff), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sm252_sl126_2d_v075_signal(ncfdebt, ncff, closeadj):
    base = _mean(_f011_debt_share(ncfdebt, ncff), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sm21_sl21_2d_v076_signal(ncff, marketcap, closeadj):
    base = _mean(ncff / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sm63_sl21_2d_v077_signal(ncff, marketcap, closeadj):
    base = _mean(ncff / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sm63_sl63_2d_v078_signal(ncff, marketcap, closeadj):
    base = _mean(ncff / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sm252_sl63_2d_v079_signal(ncff, marketcap, closeadj):
    base = _mean(ncff / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sm252_sl126_2d_v080_signal(ncff, marketcap, closeadj):
    base = _mean(ncff / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_pctslope_21d_2d_v081_signal(ncff, closeadj):
    base = ncff
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_pctslope_63d_2d_v082_signal(ncff, closeadj):
    base = ncff
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_pctslope_252d_2d_v083_signal(ncff, closeadj):
    base = ncff
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_pctslope_21d_2d_v084_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_pctslope_63d_2d_v085_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_pctslope_252d_2d_v086_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_pctslope_21d_2d_v087_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_pctslope_63d_2d_v088_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_pctslope_252d_2d_v089_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_pctslope_21d_2d_v090_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_pctslope_63d_2d_v091_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_pctslope_252d_2d_v092_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_pctslope_21d_2d_v093_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_pctslope_63d_2d_v094_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_pctslope_252d_2d_v095_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_pctslope_21d_2d_v096_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_pctslope_63d_2d_v097_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_pctslope_252d_2d_v098_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_pctslope_21d_2d_v099_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_pctslope_63d_2d_v100_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_pctslope_252d_2d_v101_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_pctslope_21d_2d_v102_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_pctslope_63d_2d_v103_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_pctslope_252d_2d_v104_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sgnslope_21d_2d_v105_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sgnslope_63d_2d_v106_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_sgnslope_252d_2d_v107_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sgnslope_21d_2d_v108_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sgnslope_63d_2d_v109_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_sgnslope_252d_2d_v110_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sgnslope_21d_2d_v111_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sgnslope_63d_2d_v112_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_sgnslope_252d_2d_v113_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sgnslope_21d_2d_v114_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sgnslope_63d_2d_v115_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_sgnslope_252d_2d_v116_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sgnslope_21d_2d_v117_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sgnslope_63d_2d_v118_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_sgnslope_252d_2d_v119_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sgnslope_21d_2d_v120_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sgnslope_63d_2d_v121_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_sgnslope_252d_2d_v122_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sgnslope_21d_2d_v123_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sgnslope_63d_2d_v124_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_sgnslope_252d_2d_v125_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sgnslope_21d_2d_v126_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sgnslope_63d_2d_v127_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_sgnslope_252d_2d_v128_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_logmagslope_21d_2d_v129_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_logmagslope_63d_2d_v130_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_logmagslope_252d_2d_v131_signal(ncff, closeadj):
    base = ncff
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_logmagslope_21d_2d_v132_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_logmagslope_63d_2d_v133_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_logmagslope_252d_2d_v134_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_logmagslope_21d_2d_v135_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_logmagslope_63d_2d_v136_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_logmagslope_252d_2d_v137_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_logmagslope_21d_2d_v138_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_logmagslope_63d_2d_v139_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_logmagslope_252d_2d_v140_signal(ncfdebt, closeadj):
    base = ncfdebt
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_logmagslope_21d_2d_v141_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_logmagslope_63d_2d_v142_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_logmagslope_252d_2d_v143_signal(ncfdiv, closeadj):
    base = ncfdiv
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_logmagslope_21d_2d_v144_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_logmagslope_63d_2d_v145_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_logmagslope_252d_2d_v146_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_logmagslope_21d_2d_v147_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_logmagslope_63d_2d_v148_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_logmagslope_252d_2d_v149_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_logmagslope_21d_2d_v150_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

