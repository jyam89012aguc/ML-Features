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
def _f033_iss_per_share(ncfcommon, sharesbas):
    return ncfcommon / sharesbas.replace(0, np.nan).abs()


# 21d mean of ncfcommon_lvl scaled by closeadj
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_mean_21d_base_v001_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ncfcommon_lvl scaled by closeadj
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_mean_63d_base_v002_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ncfcommon_lvl scaled by closeadj
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_mean_126d_base_v003_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ncfcommon_lvl scaled by closeadj
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_mean_252d_base_v004_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ncfcommon_lvl scaled by closeadj
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_mean_504d_base_v005_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of issuance_per_share scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_share_mean_21d_base_v006_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of issuance_per_share scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_share_mean_63d_base_v007_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of issuance_per_share scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_share_mean_126d_base_v008_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of issuance_per_share scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_share_mean_252d_base_v009_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of issuance_per_share scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_share_mean_504d_base_v010_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of issuance_to_mcap scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_mean_21d_base_v011_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of issuance_to_mcap scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_mean_63d_base_v012_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of issuance_to_mcap scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_mean_126d_base_v013_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of issuance_to_mcap scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_mean_252d_base_v014_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of issuance_to_mcap scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_mean_504d_base_v015_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of issuance_to_ncff scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_mean_21d_base_v016_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of issuance_to_ncff scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_mean_63d_base_v017_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of issuance_to_ncff scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_mean_126d_base_v018_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of issuance_to_ncff scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_mean_252d_base_v019_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of issuance_to_ncff scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_mean_504d_base_v020_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of issuance_pos_flag scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_mean_21d_base_v021_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of issuance_pos_flag scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_mean_63d_base_v022_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of issuance_pos_flag scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_mean_126d_base_v023_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of issuance_pos_flag scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_mean_252d_base_v024_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of issuance_pos_flag scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_mean_504d_base_v025_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of issuance_to_asset scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_asset_mean_21d_base_v026_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of issuance_to_asset scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_asset_mean_63d_base_v027_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of issuance_to_asset scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_asset_mean_126d_base_v028_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of issuance_to_asset scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_asset_mean_252d_base_v029_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of issuance_to_asset scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_to_asset_mean_504d_base_v030_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of issuance_per_dilshare scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_mean_21d_base_v031_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of issuance_per_dilshare scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_mean_63d_base_v032_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of issuance_per_dilshare scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_mean_126d_base_v033_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of issuance_per_dilshare scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_mean_252d_base_v034_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of issuance_per_dilshare scaled by closeadj
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_mean_504d_base_v035_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_median_63d_base_v036_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_median_252d_base_v037_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_median_504d_base_v038_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_median_63d_base_v039_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_median_252d_base_v040_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_median_504d_base_v041_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_median_63d_base_v042_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_median_252d_base_v043_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_median_504d_base_v044_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_median_63d_base_v045_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_median_252d_base_v046_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_median_504d_base_v047_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_median_63d_base_v048_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_median_252d_base_v049_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_median_504d_base_v050_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_median_63d_base_v051_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_median_252d_base_v052_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_median_504d_base_v053_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_median_63d_base_v054_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_median_252d_base_v055_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_median_504d_base_v056_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_rmax_252d_base_v057_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_rmax_504d_base_v058_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_rmax_252d_base_v059_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_rmax_504d_base_v060_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_rmax_252d_base_v061_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_rmax_504d_base_v062_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_rmax_252d_base_v063_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_rmax_504d_base_v064_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_rmax_252d_base_v065_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_rmax_504d_base_v066_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_rmax_252d_base_v067_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_rmax_504d_base_v068_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_rmax_252d_base_v069_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_rmax_504d_base_v070_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_rmin_252d_base_v071_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_rmin_504d_base_v072_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_rmin_252d_base_v073_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_rmin_504d_base_v074_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_rmin_252d_base_v075_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

