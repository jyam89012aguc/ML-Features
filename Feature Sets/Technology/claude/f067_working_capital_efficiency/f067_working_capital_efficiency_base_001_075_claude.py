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


# 21d mean of wc_lvl scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_lvl_mean_21d_base_v001_signal(workingcapital, closeadj):
    base = workingcapital
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of wc_lvl scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_lvl_mean_63d_base_v002_signal(workingcapital, closeadj):
    base = workingcapital
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of wc_lvl scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_lvl_mean_126d_base_v003_signal(workingcapital, closeadj):
    base = workingcapital
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of wc_lvl scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_lvl_mean_252d_base_v004_signal(workingcapital, closeadj):
    base = workingcapital
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of wc_lvl scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_lvl_mean_504d_base_v005_signal(workingcapital, closeadj):
    base = workingcapital
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of wc_to_rev scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_rev_mean_21d_base_v006_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of wc_to_rev scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_rev_mean_63d_base_v007_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of wc_to_rev scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_rev_mean_126d_base_v008_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of wc_to_rev scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_rev_mean_252d_base_v009_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of wc_to_rev scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_rev_mean_504d_base_v010_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of wc_to_asset scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_asset_mean_21d_base_v011_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of wc_to_asset scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_asset_mean_63d_base_v012_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of wc_to_asset scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_asset_mean_126d_base_v013_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of wc_to_asset scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_asset_mean_252d_base_v014_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of wc_to_asset scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_asset_mean_504d_base_v015_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of wc_yoy_chg scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_mean_21d_base_v016_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of wc_yoy_chg scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_mean_63d_base_v017_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of wc_yoy_chg scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_mean_126d_base_v018_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of wc_yoy_chg scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_mean_252d_base_v019_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of wc_yoy_chg scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_mean_504d_base_v020_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of wc_sign scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_sign_mean_21d_base_v021_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of wc_sign scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_sign_mean_63d_base_v022_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of wc_sign scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_sign_mean_126d_base_v023_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of wc_sign scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_sign_mean_252d_base_v024_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of wc_sign scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_sign_mean_504d_base_v025_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of wc_to_mcap scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_mcap_mean_21d_base_v026_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of wc_to_mcap scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_mcap_mean_63d_base_v027_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of wc_to_mcap scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_mcap_mean_126d_base_v028_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of wc_to_mcap scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_mcap_mean_252d_base_v029_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of wc_to_mcap scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_to_mcap_mean_504d_base_v030_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of wc_growth scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_growth_mean_21d_base_v031_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of wc_growth scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_growth_mean_63d_base_v032_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of wc_growth scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_growth_mean_126d_base_v033_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of wc_growth scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_growth_mean_252d_base_v034_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of wc_growth scaled by closeadj
def f067wce_f067_working_capital_efficiency_wc_growth_mean_504d_base_v035_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_median_63d_base_v036_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_median_252d_base_v037_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_median_504d_base_v038_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_median_63d_base_v039_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_median_252d_base_v040_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_median_504d_base_v041_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_median_63d_base_v042_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_median_252d_base_v043_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_median_504d_base_v044_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_median_63d_base_v045_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_median_252d_base_v046_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_median_504d_base_v047_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_median_63d_base_v048_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_median_252d_base_v049_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_median_504d_base_v050_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_median_63d_base_v051_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_median_252d_base_v052_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_median_504d_base_v053_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_median_63d_base_v054_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_median_252d_base_v055_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_median_504d_base_v056_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_rmax_252d_base_v057_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_rmax_504d_base_v058_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_rmax_252d_base_v059_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_rmax_504d_base_v060_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_rmax_252d_base_v061_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_rmax_504d_base_v062_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_rmax_252d_base_v063_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of wc_yoy_chg
def f067wce_f067_working_capital_efficiency_wc_yoy_chg_rmax_504d_base_v064_signal(workingcapital, closeadj):
    base = workingcapital.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_rmax_252d_base_v065_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of wc_sign
def f067wce_f067_working_capital_efficiency_wc_sign_rmax_504d_base_v066_signal(workingcapital, closeadj):
    base = np.sign(workingcapital)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_rmax_252d_base_v067_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of wc_to_mcap
def f067wce_f067_working_capital_efficiency_wc_to_mcap_rmax_504d_base_v068_signal(workingcapital, marketcap, closeadj):
    base = workingcapital / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_rmax_252d_base_v069_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of wc_growth
def f067wce_f067_working_capital_efficiency_wc_growth_rmax_504d_base_v070_signal(workingcapital, closeadj):
    base = workingcapital.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_rmin_252d_base_v071_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of wc_lvl
def f067wce_f067_working_capital_efficiency_wc_lvl_rmin_504d_base_v072_signal(workingcapital, closeadj):
    base = workingcapital
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_rmin_252d_base_v073_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of wc_to_rev
def f067wce_f067_working_capital_efficiency_wc_to_rev_rmin_504d_base_v074_signal(workingcapital, revenue, closeadj):
    base = _f067_wc_to_rev(workingcapital, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of wc_to_asset
def f067wce_f067_working_capital_efficiency_wc_to_asset_rmin_252d_base_v075_signal(workingcapital, assets, closeadj):
    base = workingcapital / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

