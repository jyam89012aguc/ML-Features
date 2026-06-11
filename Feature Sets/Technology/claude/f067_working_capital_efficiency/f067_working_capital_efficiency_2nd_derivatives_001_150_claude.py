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


# 21d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slope_21d_2d_v001_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slope_63d_2d_v002_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slope_126d_2d_v003_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slope_252d_2d_v004_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_slope_504d_2d_v005_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slope_21d_2d_v006_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slope_63d_2d_v007_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slope_126d_2d_v008_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slope_252d_2d_v009_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_slope_504d_2d_v010_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slope_21d_2d_v011_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slope_63d_2d_v012_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slope_126d_2d_v013_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slope_252d_2d_v014_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_slope_504d_2d_v015_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slope_21d_2d_v016_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slope_63d_2d_v017_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slope_126d_2d_v018_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slope_252d_2d_v019_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_slope_504d_2d_v020_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slope_21d_2d_v021_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slope_63d_2d_v022_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slope_126d_2d_v023_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slope_252d_2d_v024_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_slope_504d_2d_v025_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slope_21d_2d_v026_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slope_63d_2d_v027_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slope_126d_2d_v028_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slope_252d_2d_v029_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_slope_504d_2d_v030_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slope_21d_2d_v031_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slope_63d_2d_v032_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slope_126d_2d_v033_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slope_252d_2d_v034_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_slope_504d_2d_v035_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sm21_sl21_2d_v036_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sm63_sl21_2d_v037_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sm63_sl63_2d_v038_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sm252_sl63_2d_v039_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sm252_sl126_2d_v040_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sm21_sl21_2d_v041_signal(workingcapital, revenue, closeadj):
    base = _mean(_f067_wc_to_rev(workingcapital, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sm63_sl21_2d_v042_signal(workingcapital, revenue, closeadj):
    base = _mean(_f067_wc_to_rev(workingcapital, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sm63_sl63_2d_v043_signal(workingcapital, revenue, closeadj):
    base = _mean(_f067_wc_to_rev(workingcapital, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sm252_sl63_2d_v044_signal(workingcapital, revenue, closeadj):
    base = _mean(_f067_wc_to_rev(workingcapital, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sm252_sl126_2d_v045_signal(workingcapital, revenue, closeadj):
    base = _mean(_f067_wc_to_rev(workingcapital, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sm21_sl21_2d_v046_signal(workingcapital, assets, closeadj):
    base = _mean(workingcapital / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sm63_sl21_2d_v047_signal(workingcapital, assets, closeadj):
    base = _mean(workingcapital / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sm63_sl63_2d_v048_signal(workingcapital, assets, closeadj):
    base = _mean(workingcapital / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sm252_sl63_2d_v049_signal(workingcapital, assets, closeadj):
    base = _mean(workingcapital / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sm252_sl126_2d_v050_signal(workingcapital, assets, closeadj):
    base = _mean(workingcapital / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sm21_sl21_2d_v051_signal(workingcapital, closeadj):
    base = _mean(workingcapital.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sm63_sl21_2d_v052_signal(workingcapital, closeadj):
    base = _mean(workingcapital.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sm63_sl63_2d_v053_signal(workingcapital, closeadj):
    base = _mean(workingcapital.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sm252_sl63_2d_v054_signal(workingcapital, closeadj):
    base = _mean(workingcapital.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sm252_sl126_2d_v055_signal(workingcapital, closeadj):
    base = _mean(workingcapital.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sm21_sl21_2d_v056_signal(workingcapital, closeadj):
    base = _mean(np.sign(workingcapital), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sm63_sl21_2d_v057_signal(workingcapital, closeadj):
    base = _mean(np.sign(workingcapital), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sm63_sl63_2d_v058_signal(workingcapital, closeadj):
    base = _mean(np.sign(workingcapital), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sm252_sl63_2d_v059_signal(workingcapital, closeadj):
    base = _mean(np.sign(workingcapital), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sm252_sl126_2d_v060_signal(workingcapital, closeadj):
    base = _mean(np.sign(workingcapital), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sm21_sl21_2d_v061_signal(workingcapital, marketcap, closeadj):
    base = _mean(workingcapital / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sm63_sl21_2d_v062_signal(workingcapital, marketcap, closeadj):
    base = _mean(workingcapital / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sm63_sl63_2d_v063_signal(workingcapital, marketcap, closeadj):
    base = _mean(workingcapital / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sm252_sl63_2d_v064_signal(workingcapital, marketcap, closeadj):
    base = _mean(workingcapital / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sm252_sl126_2d_v065_signal(workingcapital, marketcap, closeadj):
    base = _mean(workingcapital / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sm21_sl21_2d_v066_signal(workingcapital, closeadj):
    base = _mean(workingcapital.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sm63_sl21_2d_v067_signal(workingcapital, closeadj):
    base = _mean(workingcapital.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sm63_sl63_2d_v068_signal(workingcapital, closeadj):
    base = _mean(workingcapital.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sm252_sl63_2d_v069_signal(workingcapital, closeadj):
    base = _mean(workingcapital.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sm252_sl126_2d_v070_signal(workingcapital, closeadj):
    base = _mean(workingcapital.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_pctslope_21d_2d_v071_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_pctslope_63d_2d_v072_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_pctslope_252d_2d_v073_signal(workingcapital, closeadj):
    base = workingcapital
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_pctslope_21d_2d_v074_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_pctslope_63d_2d_v075_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_pctslope_252d_2d_v076_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_pctslope_21d_2d_v077_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_pctslope_63d_2d_v078_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_pctslope_252d_2d_v079_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_pctslope_21d_2d_v080_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_pctslope_63d_2d_v081_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_pctslope_252d_2d_v082_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_pctslope_21d_2d_v083_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_pctslope_63d_2d_v084_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_pctslope_252d_2d_v085_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_pctslope_21d_2d_v086_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_pctslope_63d_2d_v087_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_pctslope_252d_2d_v088_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_pctslope_21d_2d_v089_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_pctslope_63d_2d_v090_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_pctslope_252d_2d_v091_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sgnslope_21d_2d_v092_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sgnslope_63d_2d_v093_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_sgnslope_252d_2d_v094_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sgnslope_21d_2d_v095_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sgnslope_63d_2d_v096_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_sgnslope_252d_2d_v097_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sgnslope_21d_2d_v098_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sgnslope_63d_2d_v099_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_sgnslope_252d_2d_v100_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sgnslope_21d_2d_v101_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sgnslope_63d_2d_v102_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_sgnslope_252d_2d_v103_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sgnslope_21d_2d_v104_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sgnslope_63d_2d_v105_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_sgnslope_252d_2d_v106_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sgnslope_21d_2d_v107_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sgnslope_63d_2d_v108_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_sgnslope_252d_2d_v109_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sgnslope_21d_2d_v110_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sgnslope_63d_2d_v111_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_sgnslope_252d_2d_v112_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_logmagslope_21d_2d_v113_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_logmagslope_63d_2d_v114_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_logmagslope_252d_2d_v115_signal(workingcapital, closeadj):
    base = workingcapital
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_logmagslope_21d_2d_v116_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_logmagslope_63d_2d_v117_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_logmagslope_252d_2d_v118_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_logmagslope_21d_2d_v119_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_logmagslope_63d_2d_v120_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_logmagslope_252d_2d_v121_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_logmagslope_21d_2d_v122_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_logmagslope_63d_2d_v123_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_logmagslope_252d_2d_v124_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_logmagslope_21d_2d_v125_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_logmagslope_63d_2d_v126_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_logmagslope_252d_2d_v127_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_logmagslope_21d_2d_v128_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_logmagslope_63d_2d_v129_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_logmagslope_252d_2d_v130_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_logmagslope_21d_2d_v131_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_logmagslope_63d_2d_v132_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_logmagslope_252d_2d_v133_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|wc_lvl|
def f067wce_f067_working_capital_efficiency_wc_lvl_logslope_63d_2d_v134_signal(workingcapital, closeadj):
    base = np.log((workingcapital).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|wc_lvl|
def f067wce_f067_working_capital_efficiency_wc_lvl_logslope_252d_2d_v135_signal(workingcapital, closeadj):
    base = np.log((workingcapital).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|wc_to_rev|
def f067wce_f067_working_capital_efficiency_wc_to_rev_logslope_63d_2d_v136_signal(workingcapital, revenue, closeadj):
    base = np.log((_f067_wc_to_rev(workingcapital, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|wc_to_rev|
def f067wce_f067_working_capital_efficiency_wc_to_rev_logslope_252d_2d_v137_signal(workingcapital, revenue, closeadj):
    base = np.log((_f067_wc_to_rev(workingcapital, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|wc_to_asset|
def f067wce_f067_working_capital_efficiency_wc_to_asset_logslope_63d_2d_v138_signal(workingcapital, assets, closeadj):
    base = np.log((workingcapital / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|wc_to_asset|
def f067wce_f067_working_capital_efficiency_wc_to_asset_logslope_252d_2d_v139_signal(workingcapital, assets, closeadj):
    base = np.log((workingcapital / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|wc_yoy_chg|
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_logslope_63d_2d_v140_signal(workingcapital, closeadj):
    base = np.log((workingcapital.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|wc_yoy_chg|
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_logslope_252d_2d_v141_signal(workingcapital, closeadj):
    base = np.log((workingcapital.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|wc_sign|
def f067wce_f067_working_capital_efficiency_wc_sign_logslope_63d_2d_v142_signal(workingcapital, closeadj):
    base = np.log((np.sign(workingcapital)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|wc_sign|
def f067wce_f067_working_capital_efficiency_wc_sign_logslope_252d_2d_v143_signal(workingcapital, closeadj):
    base = np.log((np.sign(workingcapital)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|wc_to_mcap|
def f067wce_f067_working_capital_efficiency_wc_to_mcap_logslope_63d_2d_v144_signal(workingcapital, marketcap, closeadj):
    base = np.log((workingcapital / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|wc_to_mcap|
def f067wce_f067_working_capital_efficiency_wc_to_mcap_logslope_252d_2d_v145_signal(workingcapital, marketcap, closeadj):
    base = np.log((workingcapital / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|wc_growth|
def f067wce_f067_working_capital_efficiency_wc_growth_logslope_63d_2d_v146_signal(workingcapital, closeadj):
    base = np.log((workingcapital.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|wc_growth|
def f067wce_f067_working_capital_efficiency_wc_growth_logslope_252d_2d_v147_signal(workingcapital, closeadj):
    base = np.log((workingcapital.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

