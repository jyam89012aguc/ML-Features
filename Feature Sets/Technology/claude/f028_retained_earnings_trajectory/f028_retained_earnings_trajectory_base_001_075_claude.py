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
def _f028_retearn_share(retearn, equity):
    return retearn / equity.replace(0, np.nan).abs()


# 21d mean of retearn_lvl scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_mean_21d_base_v001_signal(retearn, closeadj):
    base = retearn
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retearn_lvl scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_mean_63d_base_v002_signal(retearn, closeadj):
    base = retearn
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retearn_lvl scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_mean_126d_base_v003_signal(retearn, closeadj):
    base = retearn
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retearn_lvl scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_mean_252d_base_v004_signal(retearn, closeadj):
    base = retearn
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retearn_lvl scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_mean_504d_base_v005_signal(retearn, closeadj):
    base = retearn
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of retearn_to_equity scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_mean_21d_base_v006_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retearn_to_equity scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_mean_63d_base_v007_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retearn_to_equity scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_mean_126d_base_v008_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retearn_to_equity scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_mean_252d_base_v009_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retearn_to_equity scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_mean_504d_base_v010_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of retearn_to_asset scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_mean_21d_base_v011_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retearn_to_asset scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_mean_63d_base_v012_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retearn_to_asset scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_mean_126d_base_v013_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retearn_to_asset scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_mean_252d_base_v014_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retearn_to_asset scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_mean_504d_base_v015_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of retearn_chg_yoy scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_mean_21d_base_v016_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retearn_chg_yoy scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_mean_63d_base_v017_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retearn_chg_yoy scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_mean_126d_base_v018_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retearn_chg_yoy scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_mean_252d_base_v019_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retearn_chg_yoy scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_mean_504d_base_v020_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of retearn_sign scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_sign_mean_21d_base_v021_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retearn_sign scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_sign_mean_63d_base_v022_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retearn_sign scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_sign_mean_126d_base_v023_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retearn_sign scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_sign_mean_252d_base_v024_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retearn_sign scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_sign_mean_504d_base_v025_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of retearn_log_abs scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_mean_21d_base_v026_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retearn_log_abs scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_mean_63d_base_v027_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retearn_log_abs scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_mean_126d_base_v028_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retearn_log_abs scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_mean_252d_base_v029_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retearn_log_abs scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_mean_504d_base_v030_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of retearn_per_share scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_mean_21d_base_v031_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of retearn_per_share scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_mean_63d_base_v032_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of retearn_per_share scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_mean_126d_base_v033_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of retearn_per_share scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_mean_252d_base_v034_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of retearn_per_share scaled by closeadj
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_mean_504d_base_v035_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_median_63d_base_v036_signal(retearn, closeadj):
    base = retearn
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_median_252d_base_v037_signal(retearn, closeadj):
    base = retearn
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_median_504d_base_v038_signal(retearn, closeadj):
    base = retearn
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_median_63d_base_v039_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_median_252d_base_v040_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_median_504d_base_v041_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_median_63d_base_v042_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_median_252d_base_v043_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_median_504d_base_v044_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_median_63d_base_v045_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_median_252d_base_v046_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_median_504d_base_v047_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_median_63d_base_v048_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_median_252d_base_v049_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_median_504d_base_v050_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_median_63d_base_v051_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_median_252d_base_v052_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_median_504d_base_v053_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_median_63d_base_v054_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_median_252d_base_v055_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_median_504d_base_v056_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_rmax_252d_base_v057_signal(retearn, closeadj):
    base = retearn
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_rmax_504d_base_v058_signal(retearn, closeadj):
    base = retearn
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_rmax_252d_base_v059_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_rmax_504d_base_v060_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_rmax_252d_base_v061_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_rmax_504d_base_v062_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_rmax_252d_base_v063_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_rmax_504d_base_v064_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_rmax_252d_base_v065_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_rmax_504d_base_v066_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_rmax_252d_base_v067_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_rmax_504d_base_v068_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_rmax_252d_base_v069_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_rmax_504d_base_v070_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_rmin_252d_base_v071_signal(retearn, closeadj):
    base = retearn
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_rmin_504d_base_v072_signal(retearn, closeadj):
    base = retearn
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_rmin_252d_base_v073_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_rmin_504d_base_v074_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_rmin_252d_base_v075_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

