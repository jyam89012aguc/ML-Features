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


# 21d acceleration of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_accel_21d_3d_v001_signal(retearn, closeadj):
    base = retearn
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_accel_63d_3d_v002_signal(retearn, closeadj):
    base = retearn
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_accel_126d_3d_v003_signal(retearn, closeadj):
    base = retearn
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_accel_252d_3d_v004_signal(retearn, closeadj):
    base = retearn
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_accel_21d_3d_v005_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_accel_63d_3d_v006_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_accel_126d_3d_v007_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_accel_252d_3d_v008_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_accel_21d_3d_v009_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_accel_63d_3d_v010_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_accel_126d_3d_v011_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_accel_252d_3d_v012_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_accel_21d_3d_v013_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_accel_63d_3d_v014_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_accel_126d_3d_v015_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_accel_252d_3d_v016_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_accel_21d_3d_v017_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_accel_63d_3d_v018_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_accel_126d_3d_v019_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_accel_252d_3d_v020_signal(retearn, closeadj):
    base = np.sign(retearn)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_accel_21d_3d_v021_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_accel_63d_3d_v022_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_accel_126d_3d_v023_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_accel_252d_3d_v024_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_accel_21d_3d_v025_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_accel_63d_3d_v026_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_accel_126d_3d_v027_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_accel_252d_3d_v028_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slopez_21d_z126_3d_v029_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slopez_63d_z252_3d_v030_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slopez_126d_z252_3d_v031_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_slopez_252d_z504_3d_v032_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slopez_21d_z126_3d_v033_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slopez_63d_z252_3d_v034_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slopez_126d_z252_3d_v035_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_slopez_252d_z504_3d_v036_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slopez_21d_z126_3d_v037_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slopez_63d_z252_3d_v038_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slopez_126d_z252_3d_v039_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_slopez_252d_z504_3d_v040_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slopez_21d_z126_3d_v041_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slopez_63d_z252_3d_v042_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slopez_126d_z252_3d_v043_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_slopez_252d_z504_3d_v044_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slopez_21d_z126_3d_v045_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slopez_63d_z252_3d_v046_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slopez_126d_z252_3d_v047_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_slopez_252d_z504_3d_v048_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slopez_21d_z126_3d_v049_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slopez_63d_z252_3d_v050_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slopez_126d_z252_3d_v051_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_slopez_252d_z504_3d_v052_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slopez_21d_z126_3d_v053_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slopez_63d_z252_3d_v054_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slopez_126d_z252_3d_v055_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_slopez_252d_z504_3d_v056_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_jerk_21d_3d_v057_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_jerk_63d_3d_v058_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_jerk_126d_3d_v059_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_jerk_21d_3d_v060_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_jerk_63d_3d_v061_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_jerk_126d_3d_v062_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_jerk_21d_3d_v063_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_jerk_63d_3d_v064_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_jerk_126d_3d_v065_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_jerk_21d_3d_v066_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_jerk_63d_3d_v067_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_jerk_126d_3d_v068_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_jerk_21d_3d_v069_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_jerk_63d_3d_v070_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_jerk_126d_3d_v071_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_jerk_21d_3d_v072_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_jerk_63d_3d_v073_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_jerk_126d_3d_v074_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_jerk_21d_3d_v075_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_jerk_63d_3d_v076_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_jerk_126d_3d_v077_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retearn_lvl smoothed over 252d
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_smoothaccel_63d_sm252_3d_v078_signal(retearn, closeadj):
    base = retearn
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retearn_lvl smoothed over 504d
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_smoothaccel_252d_sm504_3d_v079_signal(retearn, closeadj):
    base = retearn
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retearn_to_equity smoothed over 252d
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_smoothaccel_63d_sm252_3d_v080_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retearn_to_equity smoothed over 504d
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_smoothaccel_252d_sm504_3d_v081_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retearn_to_asset smoothed over 252d
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_smoothaccel_63d_sm252_3d_v082_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retearn_to_asset smoothed over 504d
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_smoothaccel_252d_sm504_3d_v083_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retearn_chg_yoy smoothed over 252d
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_smoothaccel_63d_sm252_3d_v084_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retearn_chg_yoy smoothed over 504d
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_smoothaccel_252d_sm504_3d_v085_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retearn_sign smoothed over 252d
def f028ret_f028_retained_earnings_trajectory_retearn_sign_smoothaccel_63d_sm252_3d_v086_signal(retearn, closeadj):
    base = np.sign(retearn)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retearn_sign smoothed over 504d
def f028ret_f028_retained_earnings_trajectory_retearn_sign_smoothaccel_252d_sm504_3d_v087_signal(retearn, closeadj):
    base = np.sign(retearn)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retearn_log_abs smoothed over 252d
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_smoothaccel_63d_sm252_3d_v088_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retearn_log_abs smoothed over 504d
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_smoothaccel_252d_sm504_3d_v089_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of retearn_per_share smoothed over 252d
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_smoothaccel_63d_sm252_3d_v090_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of retearn_per_share smoothed over 504d
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_smoothaccel_252d_sm504_3d_v091_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_accelz_21d_z252_3d_v092_signal(retearn, closeadj):
    base = retearn
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_accelz_63d_z504_3d_v093_signal(retearn, closeadj):
    base = retearn
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_accelz_21d_z252_3d_v094_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_accelz_63d_z504_3d_v095_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_accelz_21d_z252_3d_v096_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_accelz_63d_z504_3d_v097_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_accelz_21d_z252_3d_v098_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_accelz_63d_z504_3d_v099_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_accelz_21d_z252_3d_v100_signal(retearn, closeadj):
    base = np.sign(retearn)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_accelz_63d_z504_3d_v101_signal(retearn, closeadj):
    base = np.sign(retearn)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_accelz_21d_z252_3d_v102_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_accelz_63d_z504_3d_v103_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_accelz_21d_z252_3d_v104_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of retearn_per_share
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_accelz_63d_z504_3d_v105_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retearn_lvl (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_signflip_63d_3d_v106_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retearn_lvl (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_signflip_252d_3d_v107_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retearn_to_equity (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_signflip_63d_3d_v108_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retearn_to_equity (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_signflip_252d_3d_v109_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retearn_to_asset (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_signflip_63d_3d_v110_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retearn_to_asset (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_signflip_252d_3d_v111_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retearn_chg_yoy (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_signflip_63d_3d_v112_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retearn_chg_yoy (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_signflip_252d_3d_v113_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retearn_sign (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_sign_signflip_63d_3d_v114_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retearn_sign (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_sign_signflip_252d_3d_v115_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retearn_log_abs (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_signflip_63d_3d_v116_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retearn_log_abs (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_signflip_252d_3d_v117_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in retearn_per_share (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_signflip_63d_3d_v118_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in retearn_per_share (raw count, no price scaling)
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_signflip_252d_3d_v119_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_lvl normalized by 252d range
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_rngaccel_63d_r252_3d_v120_signal(retearn, closeadj):
    base = retearn
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_lvl normalized by 504d range
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_rngaccel_252d_r504_3d_v121_signal(retearn, closeadj):
    base = retearn
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_to_equity normalized by 252d range
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_rngaccel_63d_r252_3d_v122_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_to_equity normalized by 504d range
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_rngaccel_252d_r504_3d_v123_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_to_asset normalized by 252d range
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_rngaccel_63d_r252_3d_v124_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_to_asset normalized by 504d range
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_rngaccel_252d_r504_3d_v125_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_chg_yoy normalized by 252d range
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_rngaccel_63d_r252_3d_v126_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_chg_yoy normalized by 504d range
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_rngaccel_252d_r504_3d_v127_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_sign normalized by 252d range
def f028ret_f028_retained_earnings_trajectory_retearn_sign_rngaccel_63d_r252_3d_v128_signal(retearn, closeadj):
    base = np.sign(retearn)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_sign normalized by 504d range
def f028ret_f028_retained_earnings_trajectory_retearn_sign_rngaccel_252d_r504_3d_v129_signal(retearn, closeadj):
    base = np.sign(retearn)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_log_abs normalized by 252d range
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_rngaccel_63d_r252_3d_v130_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_log_abs normalized by 504d range
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_rngaccel_252d_r504_3d_v131_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of retearn_per_share normalized by 252d range
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_rngaccel_63d_r252_3d_v132_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of retearn_per_share normalized by 504d range
def f028ret_f028_retained_earnings_trajectory_retearn_per_share_rngaccel_252d_r504_3d_v133_signal(retearn, sharesbas, closeadj):
    base = retearn / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_cumslope_21d_3d_v134_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_cumslope_63d_3d_v135_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of retearn_lvl
def f028ret_f028_retained_earnings_trajectory_retearn_lvl_cumslope_252d_3d_v136_signal(retearn, closeadj):
    base = retearn
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_cumslope_21d_3d_v137_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_cumslope_63d_3d_v138_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of retearn_to_equity
def f028ret_f028_retained_earnings_trajectory_retearn_to_equity_cumslope_252d_3d_v139_signal(retearn, equity, closeadj):
    base = _f028_retearn_share(retearn, equity)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_cumslope_21d_3d_v140_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_cumslope_63d_3d_v141_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of retearn_to_asset
def f028ret_f028_retained_earnings_trajectory_retearn_to_asset_cumslope_252d_3d_v142_signal(retearn, assets, closeadj):
    base = retearn / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_cumslope_21d_3d_v143_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_cumslope_63d_3d_v144_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of retearn_chg_yoy
def f028ret_f028_retained_earnings_trajectory_retearn_chg_yoy_cumslope_252d_3d_v145_signal(retearn, closeadj):
    base = retearn.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_cumslope_21d_3d_v146_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_cumslope_63d_3d_v147_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of retearn_sign
def f028ret_f028_retained_earnings_trajectory_retearn_sign_cumslope_252d_3d_v148_signal(retearn, closeadj):
    base = np.sign(retearn)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_cumslope_21d_3d_v149_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of retearn_log_abs
def f028ret_f028_retained_earnings_trajectory_retearn_log_abs_cumslope_63d_3d_v150_signal(retearn, closeadj):
    base = np.log(retearn.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

