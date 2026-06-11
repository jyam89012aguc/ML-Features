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
def _f028_retearn_share(retearn, equity):
    return retearn / equity.replace(0, np.nan).abs()


# 21d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slope_21d_2d_v001_signal(retearn, closeadj):
    base = retearn
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slope_63d_2d_v002_signal(retearn, closeadj):
    base = retearn
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slope_126d_2d_v003_signal(retearn, closeadj):
    base = retearn
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slope_252d_2d_v004_signal(retearn, closeadj):
    base = retearn
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slope_504d_2d_v005_signal(retearn, closeadj):
    base = retearn
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slope_21d_2d_v006_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slope_63d_2d_v007_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slope_126d_2d_v008_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slope_252d_2d_v009_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slope_504d_2d_v010_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slope_21d_2d_v011_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slope_63d_2d_v012_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slope_126d_2d_v013_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slope_252d_2d_v014_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slope_504d_2d_v015_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slope_21d_2d_v016_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slope_63d_2d_v017_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slope_126d_2d_v018_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slope_252d_2d_v019_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slope_504d_2d_v020_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slope_21d_2d_v021_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slope_63d_2d_v022_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slope_126d_2d_v023_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slope_252d_2d_v024_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slope_504d_2d_v025_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slope_21d_2d_v026_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slope_63d_2d_v027_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slope_126d_2d_v028_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slope_252d_2d_v029_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slope_504d_2d_v030_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slope_21d_2d_v031_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slope_63d_2d_v032_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slope_126d_2d_v033_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slope_252d_2d_v034_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slope_504d_2d_v035_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sm21_sl21_2d_v036_signal(retearn, closeadj):
    base = _mean(retearn, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sm63_sl21_2d_v037_signal(retearn, closeadj):
    base = _mean(retearn, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sm63_sl63_2d_v038_signal(retearn, closeadj):
    base = _mean(retearn, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sm252_sl63_2d_v039_signal(retearn, closeadj):
    base = _mean(retearn, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sm252_sl126_2d_v040_signal(retearn, closeadj):
    base = _mean(retearn, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sm21_sl21_2d_v041_signal(retearn, equity, closeadj):
    base = _mean(_f028_retearn_share(retearn, equity), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sm63_sl21_2d_v042_signal(retearn, equity, closeadj):
    base = _mean(_f028_retearn_share(retearn, equity), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sm63_sl63_2d_v043_signal(retearn, equity, closeadj):
    base = _mean(_f028_retearn_share(retearn, equity), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sm252_sl63_2d_v044_signal(retearn, equity, closeadj):
    base = _mean(_f028_retearn_share(retearn, equity), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sm252_sl126_2d_v045_signal(retearn, equity, closeadj):
    base = _mean(_f028_retearn_share(retearn, equity), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sm21_sl21_2d_v046_signal(retearn, assets, closeadj):
    base = _mean(retearn / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sm63_sl21_2d_v047_signal(retearn, assets, closeadj):
    base = _mean(retearn / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sm63_sl63_2d_v048_signal(retearn, assets, closeadj):
    base = _mean(retearn / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sm252_sl63_2d_v049_signal(retearn, assets, closeadj):
    base = _mean(retearn / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sm252_sl126_2d_v050_signal(retearn, assets, closeadj):
    base = _mean(retearn / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sm21_sl21_2d_v051_signal(retearn, closeadj):
    base = _mean(retearn.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sm63_sl21_2d_v052_signal(retearn, closeadj):
    base = _mean(retearn.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sm63_sl63_2d_v053_signal(retearn, closeadj):
    base = _mean(retearn.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sm252_sl63_2d_v054_signal(retearn, closeadj):
    base = _mean(retearn.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sm252_sl126_2d_v055_signal(retearn, closeadj):
    base = _mean(retearn.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sm21_sl21_2d_v056_signal(retearn, closeadj):
    base = _mean(np.sign(retearn), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sm63_sl21_2d_v057_signal(retearn, closeadj):
    base = _mean(np.sign(retearn), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sm63_sl63_2d_v058_signal(retearn, closeadj):
    base = _mean(np.sign(retearn), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sm252_sl63_2d_v059_signal(retearn, closeadj):
    base = _mean(np.sign(retearn), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sm252_sl126_2d_v060_signal(retearn, closeadj):
    base = _mean(np.sign(retearn), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sm21_sl21_2d_v061_signal(retearn, closeadj):
    base = _mean(np.log(retearn.abs().replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sm63_sl21_2d_v062_signal(retearn, closeadj):
    base = _mean(np.log(retearn.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sm63_sl63_2d_v063_signal(retearn, closeadj):
    base = _mean(np.log(retearn.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sm252_sl63_2d_v064_signal(retearn, closeadj):
    base = _mean(np.log(retearn.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sm252_sl126_2d_v065_signal(retearn, closeadj):
    base = _mean(np.log(retearn.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sm21_sl21_2d_v066_signal(retearn, sharesbas, closeadj):
    base = _mean(retearn / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sm63_sl21_2d_v067_signal(retearn, sharesbas, closeadj):
    base = _mean(retearn / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sm63_sl63_2d_v068_signal(retearn, sharesbas, closeadj):
    base = _mean(retearn / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sm252_sl63_2d_v069_signal(retearn, sharesbas, closeadj):
    base = _mean(retearn / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sm252_sl126_2d_v070_signal(retearn, sharesbas, closeadj):
    base = _mean(retearn / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_pctslope_21d_2d_v071_signal(retearn, closeadj):
    base = retearn
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_pctslope_63d_2d_v072_signal(retearn, closeadj):
    base = retearn
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_pctslope_252d_2d_v073_signal(retearn, closeadj):
    base = retearn
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_pctslope_21d_2d_v074_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_pctslope_63d_2d_v075_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_pctslope_252d_2d_v076_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_pctslope_21d_2d_v077_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_pctslope_63d_2d_v078_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_pctslope_252d_2d_v079_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_pctslope_21d_2d_v080_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_pctslope_63d_2d_v081_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_pctslope_252d_2d_v082_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_pctslope_21d_2d_v083_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_pctslope_63d_2d_v084_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_pctslope_252d_2d_v085_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_pctslope_21d_2d_v086_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_pctslope_63d_2d_v087_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_pctslope_252d_2d_v088_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_pctslope_21d_2d_v089_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_pctslope_63d_2d_v090_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_pctslope_252d_2d_v091_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sgnslope_21d_2d_v092_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sgnslope_63d_2d_v093_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_sgnslope_252d_2d_v094_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sgnslope_21d_2d_v095_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sgnslope_63d_2d_v096_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_sgnslope_252d_2d_v097_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sgnslope_21d_2d_v098_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sgnslope_63d_2d_v099_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_sgnslope_252d_2d_v100_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sgnslope_21d_2d_v101_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sgnslope_63d_2d_v102_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_sgnslope_252d_2d_v103_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sgnslope_21d_2d_v104_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sgnslope_63d_2d_v105_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_sgnslope_252d_2d_v106_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sgnslope_21d_2d_v107_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sgnslope_63d_2d_v108_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_sgnslope_252d_2d_v109_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sgnslope_21d_2d_v110_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sgnslope_63d_2d_v111_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_sgnslope_252d_2d_v112_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_logmagslope_21d_2d_v113_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_logmagslope_63d_2d_v114_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_logmagslope_252d_2d_v115_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_logmagslope_21d_2d_v116_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_logmagslope_63d_2d_v117_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_logmagslope_252d_2d_v118_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_logmagslope_21d_2d_v119_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_logmagslope_63d_2d_v120_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_logmagslope_252d_2d_v121_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_logmagslope_21d_2d_v122_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_logmagslope_63d_2d_v123_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_logmagslope_252d_2d_v124_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_logmagslope_21d_2d_v125_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_logmagslope_63d_2d_v126_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_logmagslope_252d_2d_v127_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_logmagslope_21d_2d_v128_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_logmagslope_63d_2d_v129_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_logmagslope_252d_2d_v130_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_logmagslope_21d_2d_v131_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_logmagslope_63d_2d_v132_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_logmagslope_252d_2d_v133_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retearn_lvl|
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_logslope_63d_2d_v134_signal(retearn, closeadj):
    base = np.log((retearn).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retearn_lvl|
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_logslope_252d_2d_v135_signal(retearn, closeadj):
    base = np.log((retearn).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retearn_to_equity|
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_logslope_63d_2d_v136_signal(retearn, equity, closeadj):
    base = np.log((_f028_retearn_share(retearn, equity)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retearn_to_equity|
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_logslope_252d_2d_v137_signal(retearn, equity, closeadj):
    base = np.log((_f028_retearn_share(retearn, equity)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retearn_to_asset|
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_logslope_63d_2d_v138_signal(retearn, assets, closeadj):
    base = np.log((retearn / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retearn_to_asset|
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_logslope_252d_2d_v139_signal(retearn, assets, closeadj):
    base = np.log((retearn / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retearn_chg_yoy|
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_logslope_63d_2d_v140_signal(retearn, closeadj):
    base = np.log((retearn.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retearn_chg_yoy|
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_logslope_252d_2d_v141_signal(retearn, closeadj):
    base = np.log((retearn.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retearn_sign|
def f028ret_f028_retained_earnings_trajectory_retearn_sign_logslope_63d_2d_v142_signal(retearn, closeadj):
    base = np.log((np.sign(retearn)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retearn_sign|
def f028ret_f028_retained_earnings_trajectory_retearn_sign_logslope_252d_2d_v143_signal(retearn, closeadj):
    base = np.log((np.sign(retearn)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retearn_log_abs|
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_logslope_63d_2d_v144_signal(retearn, closeadj):
    base = np.log((np.log(retearn.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retearn_log_abs|
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_logslope_252d_2d_v145_signal(retearn, closeadj):
    base = np.log((np.log(retearn.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|retearn_per_share|
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_logslope_63d_2d_v146_signal(retearn, sharesbas, closeadj):
    base = np.log((retearn / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|retearn_per_share|
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_logslope_252d_2d_v147_signal(retearn, sharesbas, closeadj):
    base = np.log((retearn / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

