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


# 63d z-score of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_z_63d_base_v076_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_z_126d_base_v077_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_z_252d_base_v078_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_z_504d_base_v079_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_z_63d_base_v080_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_z_126d_base_v081_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_z_252d_base_v082_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_z_504d_base_v083_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_z_63d_base_v084_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_z_126d_base_v085_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_z_252d_base_v086_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_z_504d_base_v087_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_z_63d_base_v088_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_z_126d_base_v089_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_z_252d_base_v090_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_z_504d_base_v091_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_z_63d_base_v092_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_z_126d_base_v093_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_z_252d_base_v094_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_z_504d_base_v095_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_z_63d_base_v096_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_z_126d_base_v097_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_z_252d_base_v098_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_z_504d_base_v099_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_z_63d_base_v100_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_z_126d_base_v101_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_z_252d_base_v102_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_z_504d_base_v103_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_distmax_252d_base_v104_signal(ncfcommon, closeadj):
    base = ncfcommon
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_distmax_504d_base_v105_signal(ncfcommon, closeadj):
    base = ncfcommon
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_distmax_252d_base_v106_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_distmax_504d_base_v107_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_distmax_252d_base_v108_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_distmax_504d_base_v109_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_distmax_252d_base_v110_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_distmax_504d_base_v111_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_distmax_252d_base_v112_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_distmax_504d_base_v113_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_distmax_252d_base_v114_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_distmax_504d_base_v115_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_distmax_252d_base_v116_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_distmax_504d_base_v117_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_distmed_126d_base_v118_signal(ncfcommon, closeadj):
    base = ncfcommon
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_distmed_252d_base_v119_signal(ncfcommon, closeadj):
    base = ncfcommon
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_distmed_504d_base_v120_signal(ncfcommon, closeadj):
    base = ncfcommon
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_distmed_126d_base_v121_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_distmed_252d_base_v122_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_distmed_504d_base_v123_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_distmed_126d_base_v124_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_distmed_252d_base_v125_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_distmed_504d_base_v126_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_distmed_126d_base_v127_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_distmed_252d_base_v128_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_distmed_504d_base_v129_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_distmed_126d_base_v130_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_distmed_252d_base_v131_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_distmed_504d_base_v132_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_distmed_126d_base_v133_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_distmed_252d_base_v134_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_distmed_504d_base_v135_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_distmed_126d_base_v136_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_distmed_252d_base_v137_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of issuance_per_dilshare
def f033eic_f033_equity_issuance_cash_issuance_per_dilshare_distmed_504d_base_v138_signal(ncfcommon, shareswadil, closeadj):
    base = ncfcommon / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_chg_63d_base_v139_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ncfcommon_lvl
def f033eic_f033_equity_issuance_cash_ncfcommon_lvl_chg_252d_base_v140_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_chg_63d_base_v141_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in issuance_per_share
def f033eic_f033_equity_issuance_cash_issuance_per_share_chg_252d_base_v142_signal(ncfcommon, sharesbas, closeadj):
    base = _f033_iss_per_share(ncfcommon, sharesbas)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_chg_63d_base_v143_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in issuance_to_mcap
def f033eic_f033_equity_issuance_cash_issuance_to_mcap_chg_252d_base_v144_signal(ncfcommon, marketcap, closeadj):
    base = ncfcommon / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_chg_63d_base_v145_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in issuance_to_ncff
def f033eic_f033_equity_issuance_cash_issuance_to_ncff_chg_252d_base_v146_signal(ncfcommon, ncff, closeadj):
    base = ncfcommon / ncff.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_chg_63d_base_v147_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in issuance_pos_flag
def f033eic_f033_equity_issuance_cash_issuance_pos_flag_chg_252d_base_v148_signal(ncfcommon, closeadj):
    base = (ncfcommon > 0).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_chg_63d_base_v149_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in issuance_to_asset
def f033eic_f033_equity_issuance_cash_issuance_to_asset_chg_252d_base_v150_signal(ncfcommon, assets, closeadj):
    base = ncfcommon / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

