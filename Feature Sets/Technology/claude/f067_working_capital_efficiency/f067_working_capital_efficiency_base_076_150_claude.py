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
def _f067_wc_to_rev(workingcapital, revenue):
    return workingcapital / revenue.abs().replace(0, np.nan)


# 63d z-score of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_z_63d_base_v076_signal(workingcapital, closeadj):
    base = workingcapital
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_z_126d_base_v077_signal(workingcapital, closeadj):
    base = workingcapital
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_z_252d_base_v078_signal(workingcapital, closeadj):
    base = workingcapital
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_z_504d_base_v079_signal(workingcapital, closeadj):
    base = workingcapital
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_z_63d_base_v080_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_z_126d_base_v081_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_z_252d_base_v082_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_z_504d_base_v083_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_z_63d_base_v084_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_z_126d_base_v085_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_z_252d_base_v086_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_z_504d_base_v087_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_z_63d_base_v088_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_z_126d_base_v089_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_z_252d_base_v090_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_z_504d_base_v091_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_z_63d_base_v092_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_z_126d_base_v093_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_z_252d_base_v094_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_z_504d_base_v095_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_z_63d_base_v096_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_z_126d_base_v097_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_z_252d_base_v098_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_z_504d_base_v099_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_z_63d_base_v100_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_z_126d_base_v101_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_z_252d_base_v102_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_z_504d_base_v103_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_distmax_252d_base_v104_signal(workingcapital, closeadj):
    base = workingcapital
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_distmax_504d_base_v105_signal(workingcapital, closeadj):
    base = workingcapital
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_distmax_252d_base_v106_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_distmax_504d_base_v107_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_distmax_252d_base_v108_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_distmax_504d_base_v109_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_distmax_252d_base_v110_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_distmax_504d_base_v111_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_distmax_252d_base_v112_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_distmax_504d_base_v113_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_distmax_252d_base_v114_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_distmax_504d_base_v115_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_distmax_252d_base_v116_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_distmax_504d_base_v117_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_distmed_126d_base_v118_signal(workingcapital, closeadj):
    base = workingcapital
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_distmed_252d_base_v119_signal(workingcapital, closeadj):
    base = workingcapital
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_distmed_504d_base_v120_signal(workingcapital, closeadj):
    base = workingcapital
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_distmed_126d_base_v121_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_distmed_252d_base_v122_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_distmed_504d_base_v123_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_distmed_126d_base_v124_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_distmed_252d_base_v125_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_distmed_504d_base_v126_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_distmed_126d_base_v127_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_distmed_252d_base_v128_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_distmed_504d_base_v129_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_distmed_126d_base_v130_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_distmed_252d_base_v131_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_distmed_504d_base_v132_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_distmed_126d_base_v133_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_distmed_252d_base_v134_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_distmed_504d_base_v135_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_distmed_126d_base_v136_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_distmed_252d_base_v137_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_distmed_504d_base_v138_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_chg_63d_base_v139_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_chg_252d_base_v140_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_chg_63d_base_v141_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_chg_252d_base_v142_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_chg_63d_base_v143_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_chg_252d_base_v144_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_chg_63d_base_v145_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_chg_252d_base_v146_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_chg_63d_base_v147_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_chg_252d_base_v148_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_chg_63d_base_v149_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_chg_252d_base_v150_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

