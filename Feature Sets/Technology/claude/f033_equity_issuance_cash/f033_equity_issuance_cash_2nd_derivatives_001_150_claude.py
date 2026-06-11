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
def _f033_iss_per_share(ncfcommon, sharesbas):
    return ncfcommon / sharesbas.replace(0, np.nan).abs()


# 21d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slope_21d_2d_v001_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slope_63d_2d_v002_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slope_126d_2d_v003_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slope_252d_2d_v004_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slope_504d_2d_v005_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slope_21d_2d_v006_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slope_63d_2d_v007_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slope_126d_2d_v008_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slope_252d_2d_v009_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slope_504d_2d_v010_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slope_21d_2d_v011_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slope_63d_2d_v012_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slope_126d_2d_v013_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slope_252d_2d_v014_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slope_504d_2d_v015_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slope_21d_2d_v016_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slope_63d_2d_v017_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slope_126d_2d_v018_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slope_252d_2d_v019_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slope_504d_2d_v020_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slope_21d_2d_v021_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slope_63d_2d_v022_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slope_126d_2d_v023_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slope_252d_2d_v024_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slope_504d_2d_v025_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slope_21d_2d_v026_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slope_63d_2d_v027_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slope_126d_2d_v028_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slope_252d_2d_v029_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slope_504d_2d_v030_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slope_21d_2d_v031_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slope_63d_2d_v032_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slope_126d_2d_v033_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slope_252d_2d_v034_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slope_504d_2d_v035_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sm21_sl21_2d_v036_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sm63_sl21_2d_v037_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sm63_sl63_2d_v038_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sm252_sl63_2d_v039_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sm252_sl126_2d_v040_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sm21_sl21_2d_v041_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_f033_iss_per_share(ncfcommon, sharesbas), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sm63_sl21_2d_v042_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_f033_iss_per_share(ncfcommon, sharesbas), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sm63_sl63_2d_v043_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_f033_iss_per_share(ncfcommon, sharesbas), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sm252_sl63_2d_v044_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_f033_iss_per_share(ncfcommon, sharesbas), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sm252_sl126_2d_v045_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_f033_iss_per_share(ncfcommon, sharesbas), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sm21_sl21_2d_v046_signal(ncfcommon, marketcap, closeadj):
    base = _mean(ncfcommon / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sm63_sl21_2d_v047_signal(ncfcommon, marketcap, closeadj):
    base = _mean(ncfcommon / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sm63_sl63_2d_v048_signal(ncfcommon, marketcap, closeadj):
    base = _mean(ncfcommon / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sm252_sl63_2d_v049_signal(ncfcommon, marketcap, closeadj):
    base = _mean(ncfcommon / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sm252_sl126_2d_v050_signal(ncfcommon, marketcap, closeadj):
    base = _mean(ncfcommon / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sm21_sl21_2d_v051_signal(ncfcommon, ncff, closeadj):
    base = _mean(ncfcommon / ncff.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sm63_sl21_2d_v052_signal(ncfcommon, ncff, closeadj):
    base = _mean(ncfcommon / ncff.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sm63_sl63_2d_v053_signal(ncfcommon, ncff, closeadj):
    base = _mean(ncfcommon / ncff.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sm252_sl63_2d_v054_signal(ncfcommon, ncff, closeadj):
    base = _mean(ncfcommon / ncff.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sm252_sl126_2d_v055_signal(ncfcommon, ncff, closeadj):
    base = _mean(ncfcommon / ncff.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sm21_sl21_2d_v056_signal(ncfcommon, closeadj):
    base = _mean((ncfcommon > 0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sm63_sl21_2d_v057_signal(ncfcommon, closeadj):
    base = _mean((ncfcommon > 0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sm63_sl63_2d_v058_signal(ncfcommon, closeadj):
    base = _mean((ncfcommon > 0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sm252_sl63_2d_v059_signal(ncfcommon, closeadj):
    base = _mean((ncfcommon > 0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sm252_sl126_2d_v060_signal(ncfcommon, closeadj):
    base = _mean((ncfcommon > 0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sm21_sl21_2d_v061_signal(ncfcommon, assets, closeadj):
    base = _mean(ncfcommon / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sm63_sl21_2d_v062_signal(ncfcommon, assets, closeadj):
    base = _mean(ncfcommon / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sm63_sl63_2d_v063_signal(ncfcommon, assets, closeadj):
    base = _mean(ncfcommon / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sm252_sl63_2d_v064_signal(ncfcommon, assets, closeadj):
    base = _mean(ncfcommon / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sm252_sl126_2d_v065_signal(ncfcommon, assets, closeadj):
    base = _mean(ncfcommon / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sm21_sl21_2d_v066_signal(ncfcommon, shareswadil, closeadj):
    base = _mean(ncfcommon / shareswadil.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sm63_sl21_2d_v067_signal(ncfcommon, shareswadil, closeadj):
    base = _mean(ncfcommon / shareswadil.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sm63_sl63_2d_v068_signal(ncfcommon, shareswadil, closeadj):
    base = _mean(ncfcommon / shareswadil.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sm252_sl63_2d_v069_signal(ncfcommon, shareswadil, closeadj):
    base = _mean(ncfcommon / shareswadil.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sm252_sl126_2d_v070_signal(ncfcommon, shareswadil, closeadj):
    base = _mean(ncfcommon / shareswadil.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_pctslope_21d_2d_v071_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_pctslope_63d_2d_v072_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_pctslope_252d_2d_v073_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_pctslope_21d_2d_v074_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_pctslope_63d_2d_v075_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_pctslope_252d_2d_v076_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_pctslope_21d_2d_v077_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_pctslope_63d_2d_v078_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_pctslope_252d_2d_v079_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_pctslope_21d_2d_v080_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_pctslope_63d_2d_v081_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_pctslope_252d_2d_v082_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_pctslope_21d_2d_v083_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_pctslope_63d_2d_v084_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_pctslope_252d_2d_v085_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_pctslope_21d_2d_v086_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_pctslope_63d_2d_v087_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_pctslope_252d_2d_v088_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_pctslope_21d_2d_v089_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_pctslope_63d_2d_v090_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_pctslope_252d_2d_v091_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sgnslope_21d_2d_v092_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sgnslope_63d_2d_v093_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_sgnslope_252d_2d_v094_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sgnslope_21d_2d_v095_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sgnslope_63d_2d_v096_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_sgnslope_252d_2d_v097_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sgnslope_21d_2d_v098_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sgnslope_63d_2d_v099_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_sgnslope_252d_2d_v100_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sgnslope_21d_2d_v101_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sgnslope_63d_2d_v102_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_sgnslope_252d_2d_v103_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sgnslope_21d_2d_v104_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sgnslope_63d_2d_v105_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_sgnslope_252d_2d_v106_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sgnslope_21d_2d_v107_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sgnslope_63d_2d_v108_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_sgnslope_252d_2d_v109_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sgnslope_21d_2d_v110_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sgnslope_63d_2d_v111_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_sgnslope_252d_2d_v112_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_logmagslope_21d_2d_v113_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_logmagslope_63d_2d_v114_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_logmagslope_252d_2d_v115_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_logmagslope_21d_2d_v116_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_logmagslope_63d_2d_v117_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_logmagslope_252d_2d_v118_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_logmagslope_21d_2d_v119_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_logmagslope_63d_2d_v120_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_logmagslope_252d_2d_v121_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_logmagslope_21d_2d_v122_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_logmagslope_63d_2d_v123_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_logmagslope_252d_2d_v124_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_logmagslope_21d_2d_v125_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_logmagslope_63d_2d_v126_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_logmagslope_252d_2d_v127_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_logmagslope_21d_2d_v128_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_logmagslope_63d_2d_v129_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_logmagslope_252d_2d_v130_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_logmagslope_21d_2d_v131_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_logmagslope_63d_2d_v132_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_logmagslope_252d_2d_v133_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ncfcommon_lvl|
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_logslope_63d_2d_v134_signal(ncfcommon, closeadj):
    base = np.log((ncfcommon).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ncfcommon_lvl|
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_logslope_252d_2d_v135_signal(ncfcommon, closeadj):
    base = np.log((ncfcommon).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|issuance_per_share|
def f033eic_f033_equity_issuance_cash_issuance_per_share_logslope_63d_2d_v136_signal(ncfcommon, sharesbas, closeadj):
    base = np.log((_f033_iss_per_share(ncfcommon, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|issuance_per_share|
def f033eic_f033_equity_issuance_cash_issuance_per_share_logslope_252d_2d_v137_signal(ncfcommon, sharesbas, closeadj):
    base = np.log((_f033_iss_per_share(ncfcommon, sharesbas)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|issuance_to_mcap|
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_logslope_63d_2d_v138_signal(ncfcommon, marketcap, closeadj):
    base = np.log((ncfcommon / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|issuance_to_mcap|
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_logslope_252d_2d_v139_signal(ncfcommon, marketcap, closeadj):
    base = np.log((ncfcommon / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|issuance_to_ncff|
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_logslope_63d_2d_v140_signal(ncfcommon, ncff, closeadj):
    base = np.log((ncfcommon / ncff.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|issuance_to_ncff|
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_logslope_252d_2d_v141_signal(ncfcommon, ncff, closeadj):
    base = np.log((ncfcommon / ncff.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|issuance_pos_flag|
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_logslope_63d_2d_v142_signal(ncfcommon, closeadj):
    base = np.log(((ncfcommon > 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|issuance_pos_flag|
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_logslope_252d_2d_v143_signal(ncfcommon, closeadj):
    base = np.log(((ncfcommon > 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|issuance_to_asset|
def f033eic_f033_equity_issuance_cash_issuance_to_asset_logslope_63d_2d_v144_signal(ncfcommon, assets, closeadj):
    base = np.log((ncfcommon / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|issuance_to_asset|
def f033eic_f033_equity_issuance_cash_issuance_to_asset_logslope_252d_2d_v145_signal(ncfcommon, assets, closeadj):
    base = np.log((ncfcommon / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|issuance_per_dilshare|
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_logslope_63d_2d_v146_signal(ncfcommon, shareswadil, closeadj):
    base = np.log((ncfcommon / shareswadil.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|issuance_per_dilshare|
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_logslope_252d_2d_v147_signal(ncfcommon, shareswadil, closeadj):
    base = np.log((ncfcommon / shareswadil.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

