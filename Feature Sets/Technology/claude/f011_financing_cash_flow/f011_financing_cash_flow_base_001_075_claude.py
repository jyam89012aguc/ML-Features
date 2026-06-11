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
def _f011_fin_to_asset(ncff, assets):
    return ncff / assets.replace(0, np.nan).abs()


def _f011_equity_share(ncfcommon, ncff):
    return ncfcommon / ncff.replace(0, np.nan).abs()


def _f011_debt_share(ncfdebt, ncff):
    return ncfdebt / ncff.replace(0, np.nan).abs()


# 21d mean of ncff_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_lvl_mean_21d_base_v001_signal(ncff, closeadj):
    base = ncff
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncff_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_lvl_mean_63d_base_v002_signal(ncff, closeadj):
    base = ncff
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncff_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_lvl_mean_126d_base_v003_signal(ncff, closeadj):
    base = ncff
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncff_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_lvl_mean_252d_base_v004_signal(ncff, closeadj):
    base = ncff
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncff_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_lvl_mean_504d_base_v005_signal(ncff, closeadj):
    base = ncff
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncff_to_asset scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_asset_mean_21d_base_v006_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncff_to_asset scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_asset_mean_63d_base_v007_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncff_to_asset scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_asset_mean_126d_base_v008_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncff_to_asset scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_asset_mean_252d_base_v009_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncff_to_asset scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_asset_mean_504d_base_v010_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncfcommon_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_mean_21d_base_v011_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncfcommon_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_mean_63d_base_v012_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncfcommon_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_mean_126d_base_v013_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncfcommon_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_mean_252d_base_v014_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncfcommon_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_mean_504d_base_v015_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncfdebt_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_mean_21d_base_v016_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncfdebt_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_mean_63d_base_v017_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncfdebt_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_mean_126d_base_v018_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncfdebt_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_mean_252d_base_v019_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncfdebt_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_mean_504d_base_v020_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncfdiv_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_mean_21d_base_v021_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncfdiv_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_mean_63d_base_v022_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncfdiv_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_mean_126d_base_v023_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncfdiv_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_mean_252d_base_v024_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncfdiv_lvl scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_mean_504d_base_v025_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of equity_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_equity_share_fin_mean_21d_base_v026_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of equity_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_equity_share_fin_mean_63d_base_v027_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of equity_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_equity_share_fin_mean_126d_base_v028_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of equity_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_equity_share_fin_mean_252d_base_v029_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of equity_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_equity_share_fin_mean_504d_base_v030_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debt_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_debt_share_fin_mean_21d_base_v031_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_debt_share_fin_mean_63d_base_v032_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_debt_share_fin_mean_126d_base_v033_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_debt_share_fin_mean_252d_base_v034_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_share_fin scaled by closeadj
def f011fnc_f011_financing_cash_flow_debt_share_fin_mean_504d_base_v035_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ncff_to_mcap scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_mean_21d_base_v036_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncff_to_mcap scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_mean_63d_base_v037_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncff_to_mcap scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_mean_126d_base_v038_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncff_to_mcap scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_mean_252d_base_v039_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncff_to_mcap scaled by closeadj
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_mean_504d_base_v040_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_median_63d_base_v041_signal(ncff, closeadj):
    base = ncff
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_median_252d_base_v042_signal(ncff, closeadj):
    base = ncff
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_median_504d_base_v043_signal(ncff, closeadj):
    base = ncff
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_median_63d_base_v044_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_median_252d_base_v045_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_median_504d_base_v046_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_median_63d_base_v047_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_median_252d_base_v048_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_median_504d_base_v049_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_median_63d_base_v050_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_median_252d_base_v051_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_median_504d_base_v052_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_median_63d_base_v053_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_median_252d_base_v054_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_median_504d_base_v055_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_median_63d_base_v056_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_median_252d_base_v057_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_median_504d_base_v058_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_median_63d_base_v059_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_median_252d_base_v060_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_median_504d_base_v061_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_median_63d_base_v062_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_median_252d_base_v063_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_median_504d_base_v064_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_rmax_252d_base_v065_signal(ncff, closeadj):
    base = ncff
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_rmax_504d_base_v066_signal(ncff, closeadj):
    base = ncff
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_rmax_252d_base_v067_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_rmax_504d_base_v068_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_rmax_252d_base_v069_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_rmax_504d_base_v070_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_rmax_252d_base_v071_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_rmax_504d_base_v072_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_rmax_252d_base_v073_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_rmax_504d_base_v074_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_rmax_252d_base_v075_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

