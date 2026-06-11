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
def _f034_sf_chg(sharefactor):
    return sharefactor.diff()


# 21d acceleration of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_accel_21d_3d_v001_signal(sharefactor, closeadj):
    base = sharefactor
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_accel_63d_3d_v002_signal(sharefactor, closeadj):
    base = sharefactor
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_accel_126d_3d_v003_signal(sharefactor, closeadj):
    base = sharefactor
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_accel_252d_3d_v004_signal(sharefactor, closeadj):
    base = sharefactor
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_accel_21d_3d_v005_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_accel_63d_3d_v006_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_accel_126d_3d_v007_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_accel_252d_3d_v008_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sf_log
def f034sfs_f034_share_factor_splits_sf_log_accel_21d_3d_v009_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_log
def f034sfs_f034_share_factor_splits_sf_log_accel_63d_3d_v010_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf_log
def f034sfs_f034_share_factor_splits_sf_log_accel_126d_3d_v011_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_log
def f034sfs_f034_share_factor_splits_sf_log_accel_252d_3d_v012_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_accel_21d_3d_v013_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_accel_63d_3d_v014_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_accel_126d_3d_v015_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_accel_252d_3d_v016_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_accel_21d_3d_v017_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_accel_63d_3d_v018_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_accel_126d_3d_v019_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_accel_252d_3d_v020_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_accel_21d_3d_v021_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_accel_63d_3d_v022_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_accel_126d_3d_v023_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_accel_252d_3d_v024_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_accel_21d_3d_v025_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_accel_63d_3d_v026_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_accel_126d_3d_v027_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_accel_252d_3d_v028_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slopez_21d_z126_3d_v029_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slopez_63d_z252_3d_v030_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slopez_126d_z252_3d_v031_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slopez_252d_z504_3d_v032_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slopez_21d_z126_3d_v033_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slopez_63d_z252_3d_v034_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slopez_126d_z252_3d_v035_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slopez_252d_z504_3d_v036_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slopez_21d_z126_3d_v037_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slopez_63d_z252_3d_v038_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slopez_126d_z252_3d_v039_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slopez_252d_z504_3d_v040_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slopez_21d_z126_3d_v041_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slopez_63d_z252_3d_v042_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slopez_126d_z252_3d_v043_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slopez_252d_z504_3d_v044_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slopez_21d_z126_3d_v045_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slopez_63d_z252_3d_v046_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slopez_126d_z252_3d_v047_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slopez_252d_z504_3d_v048_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slopez_21d_z126_3d_v049_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slopez_63d_z252_3d_v050_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slopez_126d_z252_3d_v051_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slopez_252d_z504_3d_v052_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slopez_21d_z126_3d_v053_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slopez_63d_z252_3d_v054_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slopez_126d_z252_3d_v055_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slopez_252d_z504_3d_v056_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_jerk_21d_3d_v057_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_jerk_63d_3d_v058_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_jerk_126d_3d_v059_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_jerk_21d_3d_v060_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_jerk_63d_3d_v061_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_jerk_126d_3d_v062_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf_log
def f034sfs_f034_share_factor_splits_sf_log_jerk_21d_3d_v063_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf_log
def f034sfs_f034_share_factor_splits_sf_log_jerk_63d_3d_v064_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf_log
def f034sfs_f034_share_factor_splits_sf_log_jerk_126d_3d_v065_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_jerk_21d_3d_v066_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_jerk_63d_3d_v067_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_jerk_126d_3d_v068_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_jerk_21d_3d_v069_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_jerk_63d_3d_v070_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_jerk_126d_3d_v071_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_jerk_21d_3d_v072_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_jerk_63d_3d_v073_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_jerk_126d_3d_v074_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_jerk_21d_3d_v075_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_jerk_63d_3d_v076_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_jerk_126d_3d_v077_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf_lvl smoothed over 252d
def f034sfs_f034_share_factor_splits_sf_lvl_smoothaccel_63d_sm252_3d_v078_signal(sharefactor, closeadj):
    base = sharefactor
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf_lvl smoothed over 504d
def f034sfs_f034_share_factor_splits_sf_lvl_smoothaccel_252d_sm504_3d_v079_signal(sharefactor, closeadj):
    base = sharefactor
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf_chg smoothed over 252d
def f034sfs_f034_share_factor_splits_sf_chg_smoothaccel_63d_sm252_3d_v080_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf_chg smoothed over 504d
def f034sfs_f034_share_factor_splits_sf_chg_smoothaccel_252d_sm504_3d_v081_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf_log smoothed over 252d
def f034sfs_f034_share_factor_splits_sf_log_smoothaccel_63d_sm252_3d_v082_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf_log smoothed over 504d
def f034sfs_f034_share_factor_splits_sf_log_smoothaccel_252d_sm504_3d_v083_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf_above1 smoothed over 252d
def f034sfs_f034_share_factor_splits_sf_above1_smoothaccel_63d_sm252_3d_v084_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf_above1 smoothed over 504d
def f034sfs_f034_share_factor_splits_sf_above1_smoothaccel_252d_sm504_3d_v085_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf_below1 smoothed over 252d
def f034sfs_f034_share_factor_splits_sf_below1_smoothaccel_63d_sm252_3d_v086_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf_below1 smoothed over 504d
def f034sfs_f034_share_factor_splits_sf_below1_smoothaccel_252d_sm504_3d_v087_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf_cum_252d smoothed over 252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_smoothaccel_63d_sm252_3d_v088_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf_cum_252d smoothed over 504d
def f034sfs_f034_share_factor_splits_sf_cum_252d_smoothaccel_252d_sm504_3d_v089_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf_event_density_252d smoothed over 252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_smoothaccel_63d_sm252_3d_v090_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf_event_density_252d smoothed over 504d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_smoothaccel_252d_sm504_3d_v091_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_accelz_21d_z252_3d_v092_signal(sharefactor, closeadj):
    base = sharefactor
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_accelz_63d_z504_3d_v093_signal(sharefactor, closeadj):
    base = sharefactor
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_accelz_21d_z252_3d_v094_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_accelz_63d_z504_3d_v095_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf_log
def f034sfs_f034_share_factor_splits_sf_log_accelz_21d_z252_3d_v096_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf_log
def f034sfs_f034_share_factor_splits_sf_log_accelz_63d_z504_3d_v097_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_accelz_21d_z252_3d_v098_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_accelz_63d_z504_3d_v099_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_accelz_21d_z252_3d_v100_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_accelz_63d_z504_3d_v101_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_accelz_21d_z252_3d_v102_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_accelz_63d_z504_3d_v103_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_accelz_21d_z252_3d_v104_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_accelz_63d_z504_3d_v105_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf_lvl (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_lvl_signflip_63d_3d_v106_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf_lvl (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_lvl_signflip_252d_3d_v107_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf_chg (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_chg_signflip_63d_3d_v108_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf_chg (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_chg_signflip_252d_3d_v109_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf_log (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_log_signflip_63d_3d_v110_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf_log (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_log_signflip_252d_3d_v111_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf_above1 (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_above1_signflip_63d_3d_v112_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf_above1 (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_above1_signflip_252d_3d_v113_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf_below1 (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_below1_signflip_63d_3d_v114_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf_below1 (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_below1_signflip_252d_3d_v115_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf_cum_252d (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_cum_252d_signflip_63d_3d_v116_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf_cum_252d (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_cum_252d_signflip_252d_3d_v117_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf_event_density_252d (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_event_density_252d_signflip_63d_3d_v118_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf_event_density_252d (raw count, no price scaling)
def f034sfs_f034_share_factor_splits_sf_event_density_252d_signflip_252d_3d_v119_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_lvl normalized by 252d range
def f034sfs_f034_share_factor_splits_sf_lvl_rngaccel_63d_r252_3d_v120_signal(sharefactor, closeadj):
    base = sharefactor
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_lvl normalized by 504d range
def f034sfs_f034_share_factor_splits_sf_lvl_rngaccel_252d_r504_3d_v121_signal(sharefactor, closeadj):
    base = sharefactor
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_chg normalized by 252d range
def f034sfs_f034_share_factor_splits_sf_chg_rngaccel_63d_r252_3d_v122_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_chg normalized by 504d range
def f034sfs_f034_share_factor_splits_sf_chg_rngaccel_252d_r504_3d_v123_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_log normalized by 252d range
def f034sfs_f034_share_factor_splits_sf_log_rngaccel_63d_r252_3d_v124_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_log normalized by 504d range
def f034sfs_f034_share_factor_splits_sf_log_rngaccel_252d_r504_3d_v125_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_above1 normalized by 252d range
def f034sfs_f034_share_factor_splits_sf_above1_rngaccel_63d_r252_3d_v126_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_above1 normalized by 504d range
def f034sfs_f034_share_factor_splits_sf_above1_rngaccel_252d_r504_3d_v127_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_below1 normalized by 252d range
def f034sfs_f034_share_factor_splits_sf_below1_rngaccel_63d_r252_3d_v128_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_below1 normalized by 504d range
def f034sfs_f034_share_factor_splits_sf_below1_rngaccel_252d_r504_3d_v129_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_cum_252d normalized by 252d range
def f034sfs_f034_share_factor_splits_sf_cum_252d_rngaccel_63d_r252_3d_v130_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_cum_252d normalized by 504d range
def f034sfs_f034_share_factor_splits_sf_cum_252d_rngaccel_252d_r504_3d_v131_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf_event_density_252d normalized by 252d range
def f034sfs_f034_share_factor_splits_sf_event_density_252d_rngaccel_63d_r252_3d_v132_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf_event_density_252d normalized by 504d range
def f034sfs_f034_share_factor_splits_sf_event_density_252d_rngaccel_252d_r504_3d_v133_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_cumslope_21d_3d_v134_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_cumslope_63d_3d_v135_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_cumslope_252d_3d_v136_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_cumslope_21d_3d_v137_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_cumslope_63d_3d_v138_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_cumslope_252d_3d_v139_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_cumslope_21d_3d_v140_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_cumslope_63d_3d_v141_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_cumslope_252d_3d_v142_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_cumslope_21d_3d_v143_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_cumslope_63d_3d_v144_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_cumslope_252d_3d_v145_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_cumslope_21d_3d_v146_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_cumslope_63d_3d_v147_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_cumslope_252d_3d_v148_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_cumslope_21d_3d_v149_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_cumslope_63d_3d_v150_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

