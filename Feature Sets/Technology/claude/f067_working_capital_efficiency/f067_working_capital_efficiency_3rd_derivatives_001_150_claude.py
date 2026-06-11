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
def _f067_wc_to_rev(workingcapital, revenue):
    return workingcapital / revenue.abs().replace(0, np.nan)


# 21d acceleration of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_accel_21d_3d_v001_signal(workingcapital, closeadj):
    base = workingcapital
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_accel_63d_3d_v002_signal(workingcapital, closeadj):
    base = workingcapital
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_accel_126d_3d_v003_signal(workingcapital, closeadj):
    base = workingcapital
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_accel_252d_3d_v004_signal(workingcapital, closeadj):
    base = workingcapital
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_accel_21d_3d_v005_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_accel_63d_3d_v006_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_accel_126d_3d_v007_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_accel_252d_3d_v008_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_accel_21d_3d_v009_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_accel_63d_3d_v010_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_accel_126d_3d_v011_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_accel_252d_3d_v012_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_accel_21d_3d_v013_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_accel_63d_3d_v014_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_accel_126d_3d_v015_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_accel_252d_3d_v016_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_accel_21d_3d_v017_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_accel_63d_3d_v018_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_accel_126d_3d_v019_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_accel_252d_3d_v020_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_accel_21d_3d_v021_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_accel_63d_3d_v022_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_accel_126d_3d_v023_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_accel_252d_3d_v024_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_accel_21d_3d_v025_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_accel_63d_3d_v026_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_accel_126d_3d_v027_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_accel_252d_3d_v028_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slopez_21d_z126_3d_v029_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slopez_63d_z252_3d_v030_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slopez_126d_z252_3d_v031_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slopez_252d_z504_3d_v032_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slopez_21d_z126_3d_v033_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slopez_63d_z252_3d_v034_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slopez_126d_z252_3d_v035_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slopez_252d_z504_3d_v036_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slopez_21d_z126_3d_v037_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slopez_63d_z252_3d_v038_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slopez_126d_z252_3d_v039_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slopez_252d_z504_3d_v040_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slopez_21d_z126_3d_v041_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slopez_63d_z252_3d_v042_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slopez_126d_z252_3d_v043_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slopez_252d_z504_3d_v044_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slopez_21d_z126_3d_v045_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slopez_63d_z252_3d_v046_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slopez_126d_z252_3d_v047_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slopez_252d_z504_3d_v048_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slopez_21d_z126_3d_v049_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slopez_63d_z252_3d_v050_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slopez_126d_z252_3d_v051_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slopez_252d_z504_3d_v052_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slopez_21d_z126_3d_v053_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slopez_63d_z252_3d_v054_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slopez_126d_z252_3d_v055_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slopez_252d_z504_3d_v056_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_jerk_21d_3d_v057_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_jerk_63d_3d_v058_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_jerk_126d_3d_v059_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_jerk_21d_3d_v060_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_jerk_63d_3d_v061_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_jerk_126d_3d_v062_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_jerk_21d_3d_v063_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_jerk_63d_3d_v064_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_jerk_126d_3d_v065_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_jerk_21d_3d_v066_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_jerk_63d_3d_v067_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_jerk_126d_3d_v068_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_jerk_21d_3d_v069_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_jerk_63d_3d_v070_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_jerk_126d_3d_v071_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_jerk_21d_3d_v072_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_jerk_63d_3d_v073_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_jerk_126d_3d_v074_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_jerk_21d_3d_v075_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_jerk_63d_3d_v076_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_jerk_126d_3d_v077_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of wc_lvl smoothed over 252d
def f067wce_f067_working_capital_efficiency_wc_lvl_smoothaccel_63d_sm252_3d_v078_signal(workingcapital, closeadj):
    base = workingcapital
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of wc_lvl smoothed over 504d
def f067wce_f067_working_capital_efficiency_wc_lvl_smoothaccel_252d_sm504_3d_v079_signal(workingcapital, closeadj):
    base = workingcapital
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of wc_to_rev smoothed over 252d
def f067wce_f067_working_capital_efficiency_wc_to_rev_smoothaccel_63d_sm252_3d_v080_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of wc_to_rev smoothed over 504d
def f067wce_f067_working_capital_efficiency_wc_to_rev_smoothaccel_252d_sm504_3d_v081_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of wc_to_asset smoothed over 252d
def f067wce_f067_working_capital_efficiency_wc_to_asset_smoothaccel_63d_sm252_3d_v082_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of wc_to_asset smoothed over 504d
def f067wce_f067_working_capital_efficiency_wc_to_asset_smoothaccel_252d_sm504_3d_v083_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of wc_yoy_chg smoothed over 252d
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_smoothaccel_63d_sm252_3d_v084_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of wc_yoy_chg smoothed over 504d
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_smoothaccel_252d_sm504_3d_v085_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of wc_sign smoothed over 252d
def f067wce_f067_working_capital_efficiency_wc_sign_smoothaccel_63d_sm252_3d_v086_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of wc_sign smoothed over 504d
def f067wce_f067_working_capital_efficiency_wc_sign_smoothaccel_252d_sm504_3d_v087_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of wc_to_mcap smoothed over 252d
def f067wce_f067_working_capital_efficiency_wc_to_mcap_smoothaccel_63d_sm252_3d_v088_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of wc_to_mcap smoothed over 504d
def f067wce_f067_working_capital_efficiency_wc_to_mcap_smoothaccel_252d_sm504_3d_v089_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of wc_growth smoothed over 252d
def f067wce_f067_working_capital_efficiency_wc_growth_smoothaccel_63d_sm252_3d_v090_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of wc_growth smoothed over 504d
def f067wce_f067_working_capital_efficiency_wc_growth_smoothaccel_252d_sm504_3d_v091_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_accelz_21d_z252_3d_v092_signal(workingcapital, closeadj):
    base = workingcapital
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_accelz_63d_z504_3d_v093_signal(workingcapital, closeadj):
    base = workingcapital
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_accelz_21d_z252_3d_v094_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_accelz_63d_z504_3d_v095_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_accelz_21d_z252_3d_v096_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_accelz_63d_z504_3d_v097_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_accelz_21d_z252_3d_v098_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_accelz_63d_z504_3d_v099_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_accelz_21d_z252_3d_v100_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_accelz_63d_z504_3d_v101_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_accelz_21d_z252_3d_v102_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_accelz_63d_z504_3d_v103_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_accelz_21d_z252_3d_v104_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_accelz_63d_z504_3d_v105_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in wc_lvl (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_lvl_signflip_63d_3d_v106_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in wc_lvl (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_lvl_signflip_252d_3d_v107_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in wc_to_rev (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_to_rev_signflip_63d_3d_v108_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in wc_to_rev (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_to_rev_signflip_252d_3d_v109_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in wc_to_asset (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_to_asset_signflip_63d_3d_v110_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in wc_to_asset (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_to_asset_signflip_252d_3d_v111_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in wc_yoy_chg (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_signflip_63d_3d_v112_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in wc_yoy_chg (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_signflip_252d_3d_v113_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in wc_sign (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_sign_signflip_63d_3d_v114_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in wc_sign (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_sign_signflip_252d_3d_v115_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in wc_to_mcap (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_to_mcap_signflip_63d_3d_v116_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in wc_to_mcap (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_to_mcap_signflip_252d_3d_v117_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in wc_growth (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_growth_signflip_63d_3d_v118_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in wc_growth (raw count, no price scaling)
def f067wce_f067_working_capital_efficiency_wc_growth_signflip_252d_3d_v119_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_lvl normalized by 252d range
def f067wce_f067_working_capital_efficiency_wc_lvl_rngaccel_63d_r252_3d_v120_signal(workingcapital, closeadj):
    base = workingcapital
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_lvl normalized by 504d range
def f067wce_f067_working_capital_efficiency_wc_lvl_rngaccel_252d_r504_3d_v121_signal(workingcapital, closeadj):
    base = workingcapital
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_to_rev normalized by 252d range
def f067wce_f067_working_capital_efficiency_wc_to_rev_rngaccel_63d_r252_3d_v122_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_to_rev normalized by 504d range
def f067wce_f067_working_capital_efficiency_wc_to_rev_rngaccel_252d_r504_3d_v123_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_to_asset normalized by 252d range
def f067wce_f067_working_capital_efficiency_wc_to_asset_rngaccel_63d_r252_3d_v124_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_to_asset normalized by 504d range
def f067wce_f067_working_capital_efficiency_wc_to_asset_rngaccel_252d_r504_3d_v125_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_yoy_chg normalized by 252d range
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_rngaccel_63d_r252_3d_v126_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_yoy_chg normalized by 504d range
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_rngaccel_252d_r504_3d_v127_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_sign normalized by 252d range
def f067wce_f067_working_capital_efficiency_wc_sign_rngaccel_63d_r252_3d_v128_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_sign normalized by 504d range
def f067wce_f067_working_capital_efficiency_wc_sign_rngaccel_252d_r504_3d_v129_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_to_mcap normalized by 252d range
def f067wce_f067_working_capital_efficiency_wc_to_mcap_rngaccel_63d_r252_3d_v130_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_to_mcap normalized by 504d range
def f067wce_f067_working_capital_efficiency_wc_to_mcap_rngaccel_252d_r504_3d_v131_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of wc_growth normalized by 252d range
def f067wce_f067_working_capital_efficiency_wc_growth_rngaccel_63d_r252_3d_v132_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of wc_growth normalized by 504d range
def f067wce_f067_working_capital_efficiency_wc_growth_rngaccel_252d_r504_3d_v133_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_cumslope_21d_3d_v134_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_cumslope_63d_3d_v135_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_cumslope_252d_3d_v136_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_cumslope_21d_3d_v137_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_cumslope_63d_3d_v138_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_cumslope_252d_3d_v139_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_cumslope_21d_3d_v140_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_cumslope_63d_3d_v141_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_cumslope_252d_3d_v142_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_cumslope_21d_3d_v143_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_cumslope_63d_3d_v144_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_cumslope_252d_3d_v145_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_cumslope_21d_3d_v146_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_cumslope_63d_3d_v147_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_cumslope_252d_3d_v148_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_cumslope_21d_3d_v149_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_cumslope_63d_3d_v150_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

