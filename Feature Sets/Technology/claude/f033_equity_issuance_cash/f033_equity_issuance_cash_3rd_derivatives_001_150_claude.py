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


# 21d acceleration of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_accel_21d_3d_v001_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_accel_63d_3d_v002_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_accel_126d_3d_v003_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_accel_252d_3d_v004_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_accel_21d_3d_v005_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_accel_63d_3d_v006_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_accel_126d_3d_v007_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_accel_252d_3d_v008_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_accel_21d_3d_v009_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_accel_63d_3d_v010_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_accel_126d_3d_v011_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_accel_252d_3d_v012_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_accel_21d_3d_v013_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_accel_63d_3d_v014_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_accel_126d_3d_v015_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_accel_252d_3d_v016_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_accel_21d_3d_v017_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_accel_63d_3d_v018_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_accel_126d_3d_v019_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_accel_252d_3d_v020_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_accel_21d_3d_v021_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_accel_63d_3d_v022_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_accel_126d_3d_v023_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_accel_252d_3d_v024_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_accel_21d_3d_v025_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_accel_63d_3d_v026_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_accel_126d_3d_v027_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_accel_252d_3d_v028_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slopez_21d_z126_3d_v029_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slopez_63d_z252_3d_v030_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slopez_126d_z252_3d_v031_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_slopez_252d_z504_3d_v032_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slopez_21d_z126_3d_v033_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slopez_63d_z252_3d_v034_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slopez_126d_z252_3d_v035_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_slopez_252d_z504_3d_v036_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slopez_21d_z126_3d_v037_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slopez_63d_z252_3d_v038_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slopez_126d_z252_3d_v039_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_slopez_252d_z504_3d_v040_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slopez_21d_z126_3d_v041_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slopez_63d_z252_3d_v042_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slopez_126d_z252_3d_v043_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_slopez_252d_z504_3d_v044_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slopez_21d_z126_3d_v045_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slopez_63d_z252_3d_v046_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slopez_126d_z252_3d_v047_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_slopez_252d_z504_3d_v048_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slopez_21d_z126_3d_v049_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slopez_63d_z252_3d_v050_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slopez_126d_z252_3d_v051_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_slopez_252d_z504_3d_v052_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slopez_21d_z126_3d_v053_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slopez_63d_z252_3d_v054_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slopez_126d_z252_3d_v055_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_slopez_252d_z504_3d_v056_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_jerk_21d_3d_v057_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_jerk_63d_3d_v058_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_jerk_126d_3d_v059_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_jerk_21d_3d_v060_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_jerk_63d_3d_v061_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_jerk_126d_3d_v062_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_jerk_21d_3d_v063_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_jerk_63d_3d_v064_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_jerk_126d_3d_v065_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_jerk_21d_3d_v066_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_jerk_63d_3d_v067_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_jerk_126d_3d_v068_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_jerk_21d_3d_v069_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_jerk_63d_3d_v070_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_jerk_126d_3d_v071_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_jerk_21d_3d_v072_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_jerk_63d_3d_v073_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_jerk_126d_3d_v074_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_jerk_21d_3d_v075_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_jerk_63d_3d_v076_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_jerk_126d_3d_v077_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ncfcommon_lvl smoothed over 252d
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_smoothaccel_63d_sm252_3d_v078_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ncfcommon_lvl smoothed over 504d
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_smoothaccel_252d_sm504_3d_v079_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of issuance_per_share smoothed over 252d
def f033eic_f033_equity_issuance_cash_issuance_per_share_smoothaccel_63d_sm252_3d_v080_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of issuance_per_share smoothed over 504d
def f033eic_f033_equity_issuance_cash_issuance_per_share_smoothaccel_252d_sm504_3d_v081_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of issuance_to_mcap smoothed over 252d
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_smoothaccel_63d_sm252_3d_v082_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of issuance_to_mcap smoothed over 504d
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_smoothaccel_252d_sm504_3d_v083_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of issuance_to_ncff smoothed over 252d
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_smoothaccel_63d_sm252_3d_v084_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of issuance_to_ncff smoothed over 504d
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_smoothaccel_252d_sm504_3d_v085_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of issuance_pos_flag smoothed over 252d
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_smoothaccel_63d_sm252_3d_v086_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of issuance_pos_flag smoothed over 504d
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_smoothaccel_252d_sm504_3d_v087_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of issuance_to_asset smoothed over 252d
def f033eic_f033_equity_issuance_cash_issuance_to_asset_smoothaccel_63d_sm252_3d_v088_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of issuance_to_asset smoothed over 504d
def f033eic_f033_equity_issuance_cash_issuance_to_asset_smoothaccel_252d_sm504_3d_v089_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of issuance_per_dilshare smoothed over 252d
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_smoothaccel_63d_sm252_3d_v090_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of issuance_per_dilshare smoothed over 504d
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_smoothaccel_252d_sm504_3d_v091_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_accelz_21d_z252_3d_v092_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_accelz_63d_z504_3d_v093_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_accelz_21d_z252_3d_v094_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_accelz_63d_z504_3d_v095_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_accelz_21d_z252_3d_v096_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_accelz_63d_z504_3d_v097_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_accelz_21d_z252_3d_v098_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_accelz_63d_z504_3d_v099_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_accelz_21d_z252_3d_v100_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_accelz_63d_z504_3d_v101_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_accelz_21d_z252_3d_v102_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_accelz_63d_z504_3d_v103_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_accelz_21d_z252_3d_v104_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_accelz_63d_z504_3d_v105_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ncfcommon_lvl (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_signflip_63d_3d_v106_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ncfcommon_lvl (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_signflip_252d_3d_v107_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in issuance_per_share (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_per_share_signflip_63d_3d_v108_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in issuance_per_share (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_per_share_signflip_252d_3d_v109_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in issuance_to_mcap (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_signflip_63d_3d_v110_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in issuance_to_mcap (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_signflip_252d_3d_v111_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in issuance_to_ncff (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_signflip_63d_3d_v112_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in issuance_to_ncff (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_signflip_252d_3d_v113_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in issuance_pos_flag (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_signflip_63d_3d_v114_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in issuance_pos_flag (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_signflip_252d_3d_v115_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in issuance_to_asset (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_to_asset_signflip_63d_3d_v116_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in issuance_to_asset (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_to_asset_signflip_252d_3d_v117_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in issuance_per_dilshare (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_signflip_63d_3d_v118_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in issuance_per_dilshare (raw count, no price scaling)
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_signflip_252d_3d_v119_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ncfcommon_lvl normalized by 252d range
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_rngaccel_63d_r252_3d_v120_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ncfcommon_lvl normalized by 504d range
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_rngaccel_252d_r504_3d_v121_signal(ncfcommon, closeadj):
    base = ncfcommon
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_per_share normalized by 252d range
def f033eic_f033_equity_issuance_cash_issuance_per_share_rngaccel_63d_r252_3d_v122_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_per_share normalized by 504d range
def f033eic_f033_equity_issuance_cash_issuance_per_share_rngaccel_252d_r504_3d_v123_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_to_mcap normalized by 252d range
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_rngaccel_63d_r252_3d_v124_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_to_mcap normalized by 504d range
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_rngaccel_252d_r504_3d_v125_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_to_ncff normalized by 252d range
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_rngaccel_63d_r252_3d_v126_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_to_ncff normalized by 504d range
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_rngaccel_252d_r504_3d_v127_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_pos_flag normalized by 252d range
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_rngaccel_63d_r252_3d_v128_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_pos_flag normalized by 504d range
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_rngaccel_252d_r504_3d_v129_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_to_asset normalized by 252d range
def f033eic_f033_equity_issuance_cash_issuance_to_asset_rngaccel_63d_r252_3d_v130_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_to_asset normalized by 504d range
def f033eic_f033_equity_issuance_cash_issuance_to_asset_rngaccel_252d_r504_3d_v131_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of issuance_per_dilshare normalized by 252d range
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_rngaccel_63d_r252_3d_v132_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of issuance_per_dilshare normalized by 504d range
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_rngaccel_252d_r504_3d_v133_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_cumslope_21d_3d_v134_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_cumslope_63d_3d_v135_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_cumslope_252d_3d_v136_signal(ncfcommon, closeadj):
    base = ncfcommon
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_cumslope_21d_3d_v137_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_cumslope_63d_3d_v138_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_cumslope_252d_3d_v139_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_cumslope_21d_3d_v140_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_cumslope_63d_3d_v141_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_cumslope_252d_3d_v142_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_cumslope_21d_3d_v143_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_cumslope_63d_3d_v144_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_cumslope_252d_3d_v145_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_cumslope_21d_3d_v146_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_cumslope_63d_3d_v147_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_cumslope_252d_3d_v148_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_cumslope_21d_3d_v149_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_cumslope_63d_3d_v150_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

