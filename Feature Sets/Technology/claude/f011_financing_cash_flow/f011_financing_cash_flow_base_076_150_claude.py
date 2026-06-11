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


# 63d z-score of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_z_63d_base_v076_signal(ncff, closeadj):
    base = ncff
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_z_126d_base_v077_signal(ncff, closeadj):
    base = ncff
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_z_252d_base_v078_signal(ncff, closeadj):
    base = ncff
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_z_504d_base_v079_signal(ncff, closeadj):
    base = ncff
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_z_63d_base_v080_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_z_126d_base_v081_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_z_252d_base_v082_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_z_504d_base_v083_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_z_63d_base_v084_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_z_126d_base_v085_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_z_252d_base_v086_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_z_504d_base_v087_signal(ncfcommon, closeadj):
    base = ncfcommon
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_z_63d_base_v088_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_z_126d_base_v089_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_z_252d_base_v090_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_z_504d_base_v091_signal(ncfdebt, closeadj):
    base = ncfdebt
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_z_63d_base_v092_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_z_126d_base_v093_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_z_252d_base_v094_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_z_504d_base_v095_signal(ncfdiv, closeadj):
    base = ncfdiv
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_z_63d_base_v096_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_z_126d_base_v097_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_z_252d_base_v098_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_z_504d_base_v099_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_z_63d_base_v100_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_z_126d_base_v101_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_z_252d_base_v102_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_z_504d_base_v103_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_z_63d_base_v104_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_z_126d_base_v105_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_z_252d_base_v106_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_z_504d_base_v107_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_distmax_252d_base_v108_signal(ncff, closeadj):
    base = ncff
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_distmax_504d_base_v109_signal(ncff, closeadj):
    base = ncff
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_distmax_252d_base_v110_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_distmax_504d_base_v111_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_distmax_252d_base_v112_signal(ncfcommon, closeadj):
    base = ncfcommon
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_distmax_504d_base_v113_signal(ncfcommon, closeadj):
    base = ncfcommon
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_distmax_252d_base_v114_signal(ncfdebt, closeadj):
    base = ncfdebt
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_distmax_504d_base_v115_signal(ncfdebt, closeadj):
    base = ncfdebt
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_distmax_252d_base_v116_signal(ncfdiv, closeadj):
    base = ncfdiv
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_distmax_504d_base_v117_signal(ncfdiv, closeadj):
    base = ncfdiv
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_distmax_252d_base_v118_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_distmax_504d_base_v119_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_distmax_252d_base_v120_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_distmax_504d_base_v121_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_distmax_252d_base_v122_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_distmax_504d_base_v123_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_distmed_126d_base_v124_signal(ncff, closeadj):
    base = ncff
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_distmed_252d_base_v125_signal(ncff, closeadj):
    base = ncff
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_distmed_504d_base_v126_signal(ncff, closeadj):
    base = ncff
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_distmed_126d_base_v127_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_distmed_252d_base_v128_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_distmed_504d_base_v129_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_distmed_126d_base_v130_signal(ncfcommon, closeadj):
    base = ncfcommon
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_distmed_252d_base_v131_signal(ncfcommon, closeadj):
    base = ncfcommon
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncfcommon_lvl
def f011fnc_f011_financing_cash_flow_ncfcommon_lvl_distmed_504d_base_v132_signal(ncfcommon, closeadj):
    base = ncfcommon
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_distmed_126d_base_v133_signal(ncfdebt, closeadj):
    base = ncfdebt
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_distmed_252d_base_v134_signal(ncfdebt, closeadj):
    base = ncfdebt
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncfdebt_lvl
def f011fnc_f011_financing_cash_flow_ncfdebt_lvl_distmed_504d_base_v135_signal(ncfdebt, closeadj):
    base = ncfdebt
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_distmed_126d_base_v136_signal(ncfdiv, closeadj):
    base = ncfdiv
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_distmed_252d_base_v137_signal(ncfdiv, closeadj):
    base = ncfdiv
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncfdiv_lvl
def f011fnc_f011_financing_cash_flow_ncfdiv_lvl_distmed_504d_base_v138_signal(ncfdiv, closeadj):
    base = ncfdiv
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_distmed_126d_base_v139_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_distmed_252d_base_v140_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of equity_share_fin
def f011fnc_f011_financing_cash_flow_equity_share_fin_distmed_504d_base_v141_signal(ncfcommon, ncff, closeadj):
    base = _f011_equity_share(ncfcommon, ncff)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_distmed_126d_base_v142_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_distmed_252d_base_v143_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of debt_share_fin
def f011fnc_f011_financing_cash_flow_debt_share_fin_distmed_504d_base_v144_signal(ncfdebt, ncff, closeadj):
    base = _f011_debt_share(ncfdebt, ncff)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_distmed_126d_base_v145_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_distmed_252d_base_v146_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ncff_to_mcap
def f011fnc_f011_financing_cash_flow_ncff_to_mcap_distmed_504d_base_v147_signal(ncff, marketcap, closeadj):
    base = ncff / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_chg_63d_base_v148_signal(ncff, closeadj):
    base = ncff
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ncff_lvl
def f011fnc_f011_financing_cash_flow_ncff_lvl_chg_252d_base_v149_signal(ncff, closeadj):
    base = ncff
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ncff_to_asset
def f011fnc_f011_financing_cash_flow_ncff_to_asset_chg_63d_base_v150_signal(ncff, assets, closeadj):
    base = _f011_fin_to_asset(ncff, assets)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

