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
def _f023_debt_log(debt):
    return np.log(debt.abs().replace(0, np.nan))


# 21d mean of debt_lvl scaled by closeadj
def f023dbl_f023_debt_level_debt_lvl_mean_21d_base_v001_signal(debt, closeadj):
    base = debt
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_lvl scaled by closeadj
def f023dbl_f023_debt_level_debt_lvl_mean_63d_base_v002_signal(debt, closeadj):
    base = debt
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_lvl scaled by closeadj
def f023dbl_f023_debt_level_debt_lvl_mean_126d_base_v003_signal(debt, closeadj):
    base = debt
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_lvl scaled by closeadj
def f023dbl_f023_debt_level_debt_lvl_mean_252d_base_v004_signal(debt, closeadj):
    base = debt
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_lvl scaled by closeadj
def f023dbl_f023_debt_level_debt_lvl_mean_504d_base_v005_signal(debt, closeadj):
    base = debt
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of log_debt scaled by closeadj
def f023dbl_f023_debt_level_log_debt_mean_21d_base_v006_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of log_debt scaled by closeadj
def f023dbl_f023_debt_level_log_debt_mean_63d_base_v007_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of log_debt scaled by closeadj
def f023dbl_f023_debt_level_log_debt_mean_126d_base_v008_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of log_debt scaled by closeadj
def f023dbl_f023_debt_level_log_debt_mean_252d_base_v009_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of log_debt scaled by closeadj
def f023dbl_f023_debt_level_log_debt_mean_504d_base_v010_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debt_to_asset scaled by closeadj
def f023dbl_f023_debt_level_debt_to_asset_mean_21d_base_v011_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_to_asset scaled by closeadj
def f023dbl_f023_debt_level_debt_to_asset_mean_63d_base_v012_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_to_asset scaled by closeadj
def f023dbl_f023_debt_level_debt_to_asset_mean_126d_base_v013_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_to_asset scaled by closeadj
def f023dbl_f023_debt_level_debt_to_asset_mean_252d_base_v014_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_to_asset scaled by closeadj
def f023dbl_f023_debt_level_debt_to_asset_mean_504d_base_v015_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debt_to_equity scaled by closeadj
def f023dbl_f023_debt_level_debt_to_equity_mean_21d_base_v016_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_to_equity scaled by closeadj
def f023dbl_f023_debt_level_debt_to_equity_mean_63d_base_v017_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_to_equity scaled by closeadj
def f023dbl_f023_debt_level_debt_to_equity_mean_126d_base_v018_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_to_equity scaled by closeadj
def f023dbl_f023_debt_level_debt_to_equity_mean_252d_base_v019_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_to_equity scaled by closeadj
def f023dbl_f023_debt_level_debt_to_equity_mean_504d_base_v020_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debt_to_mcap scaled by closeadj
def f023dbl_f023_debt_level_debt_to_mcap_mean_21d_base_v021_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_to_mcap scaled by closeadj
def f023dbl_f023_debt_level_debt_to_mcap_mean_63d_base_v022_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_to_mcap scaled by closeadj
def f023dbl_f023_debt_level_debt_to_mcap_mean_126d_base_v023_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_to_mcap scaled by closeadj
def f023dbl_f023_debt_level_debt_to_mcap_mean_252d_base_v024_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_to_mcap scaled by closeadj
def f023dbl_f023_debt_level_debt_to_mcap_mean_504d_base_v025_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debt_to_revenue scaled by closeadj
def f023dbl_f023_debt_level_debt_to_revenue_mean_21d_base_v026_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_to_revenue scaled by closeadj
def f023dbl_f023_debt_level_debt_to_revenue_mean_63d_base_v027_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_to_revenue scaled by closeadj
def f023dbl_f023_debt_level_debt_to_revenue_mean_126d_base_v028_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_to_revenue scaled by closeadj
def f023dbl_f023_debt_level_debt_to_revenue_mean_252d_base_v029_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_to_revenue scaled by closeadj
def f023dbl_f023_debt_level_debt_to_revenue_mean_504d_base_v030_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debt_to_ebitda scaled by closeadj
def f023dbl_f023_debt_level_debt_to_ebitda_mean_21d_base_v031_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debt_to_ebitda scaled by closeadj
def f023dbl_f023_debt_level_debt_to_ebitda_mean_63d_base_v032_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debt_to_ebitda scaled by closeadj
def f023dbl_f023_debt_level_debt_to_ebitda_mean_126d_base_v033_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debt_to_ebitda scaled by closeadj
def f023dbl_f023_debt_level_debt_to_ebitda_mean_252d_base_v034_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debt_to_ebitda scaled by closeadj
def f023dbl_f023_debt_level_debt_to_ebitda_mean_504d_base_v035_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_lvl
def f023dbl_f023_debt_level_debt_lvl_median_63d_base_v036_signal(debt, closeadj):
    base = debt
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_lvl
def f023dbl_f023_debt_level_debt_lvl_median_252d_base_v037_signal(debt, closeadj):
    base = debt
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_lvl
def f023dbl_f023_debt_level_debt_lvl_median_504d_base_v038_signal(debt, closeadj):
    base = debt
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of log_debt
def f023dbl_f023_debt_level_log_debt_median_63d_base_v039_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of log_debt
def f023dbl_f023_debt_level_log_debt_median_252d_base_v040_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of log_debt
def f023dbl_f023_debt_level_log_debt_median_504d_base_v041_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_to_asset
def f023dbl_f023_debt_level_debt_to_asset_median_63d_base_v042_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_to_asset
def f023dbl_f023_debt_level_debt_to_asset_median_252d_base_v043_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_to_asset
def f023dbl_f023_debt_level_debt_to_asset_median_504d_base_v044_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_to_equity
def f023dbl_f023_debt_level_debt_to_equity_median_63d_base_v045_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_to_equity
def f023dbl_f023_debt_level_debt_to_equity_median_252d_base_v046_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_to_equity
def f023dbl_f023_debt_level_debt_to_equity_median_504d_base_v047_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_to_mcap
def f023dbl_f023_debt_level_debt_to_mcap_median_63d_base_v048_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_to_mcap
def f023dbl_f023_debt_level_debt_to_mcap_median_252d_base_v049_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_to_mcap
def f023dbl_f023_debt_level_debt_to_mcap_median_504d_base_v050_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_to_revenue
def f023dbl_f023_debt_level_debt_to_revenue_median_63d_base_v051_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_to_revenue
def f023dbl_f023_debt_level_debt_to_revenue_median_252d_base_v052_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_to_revenue
def f023dbl_f023_debt_level_debt_to_revenue_median_504d_base_v053_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debt_to_ebitda
def f023dbl_f023_debt_level_debt_to_ebitda_median_63d_base_v054_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debt_to_ebitda
def f023dbl_f023_debt_level_debt_to_ebitda_median_252d_base_v055_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debt_to_ebitda
def f023dbl_f023_debt_level_debt_to_ebitda_median_504d_base_v056_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debt_lvl
def f023dbl_f023_debt_level_debt_lvl_rmax_252d_base_v057_signal(debt, closeadj):
    base = debt
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debt_lvl
def f023dbl_f023_debt_level_debt_lvl_rmax_504d_base_v058_signal(debt, closeadj):
    base = debt
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of log_debt
def f023dbl_f023_debt_level_log_debt_rmax_252d_base_v059_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of log_debt
def f023dbl_f023_debt_level_log_debt_rmax_504d_base_v060_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debt_to_asset
def f023dbl_f023_debt_level_debt_to_asset_rmax_252d_base_v061_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debt_to_asset
def f023dbl_f023_debt_level_debt_to_asset_rmax_504d_base_v062_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debt_to_equity
def f023dbl_f023_debt_level_debt_to_equity_rmax_252d_base_v063_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debt_to_equity
def f023dbl_f023_debt_level_debt_to_equity_rmax_504d_base_v064_signal(debt, equity, closeadj):
    base = debt / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debt_to_mcap
def f023dbl_f023_debt_level_debt_to_mcap_rmax_252d_base_v065_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debt_to_mcap
def f023dbl_f023_debt_level_debt_to_mcap_rmax_504d_base_v066_signal(debt, marketcap, closeadj):
    base = debt / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debt_to_revenue
def f023dbl_f023_debt_level_debt_to_revenue_rmax_252d_base_v067_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debt_to_revenue
def f023dbl_f023_debt_level_debt_to_revenue_rmax_504d_base_v068_signal(debt, revenue, closeadj):
    base = debt / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debt_to_ebitda
def f023dbl_f023_debt_level_debt_to_ebitda_rmax_252d_base_v069_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debt_to_ebitda
def f023dbl_f023_debt_level_debt_to_ebitda_rmax_504d_base_v070_signal(debt, ebitda, closeadj):
    base = debt / ebitda.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of debt_lvl
def f023dbl_f023_debt_level_debt_lvl_rmin_252d_base_v071_signal(debt, closeadj):
    base = debt
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of debt_lvl
def f023dbl_f023_debt_level_debt_lvl_rmin_504d_base_v072_signal(debt, closeadj):
    base = debt
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of log_debt
def f023dbl_f023_debt_level_log_debt_rmin_252d_base_v073_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of log_debt
def f023dbl_f023_debt_level_log_debt_rmin_504d_base_v074_signal(debt, closeadj):
    base = _f023_debt_log(debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of debt_to_asset
def f023dbl_f023_debt_level_debt_to_asset_rmin_252d_base_v075_signal(debt, assets, closeadj):
    base = debt / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

