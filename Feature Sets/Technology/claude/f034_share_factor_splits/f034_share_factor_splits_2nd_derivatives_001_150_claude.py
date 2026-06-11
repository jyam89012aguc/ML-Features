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


# 21d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slope_21d_2d_v001_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slope_63d_2d_v002_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slope_126d_2d_v003_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slope_252d_2d_v004_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_slope_504d_2d_v005_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slope_21d_2d_v006_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slope_63d_2d_v007_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slope_126d_2d_v008_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slope_252d_2d_v009_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_slope_504d_2d_v010_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slope_21d_2d_v011_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slope_63d_2d_v012_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slope_126d_2d_v013_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slope_252d_2d_v014_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_slope_504d_2d_v015_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slope_21d_2d_v016_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slope_63d_2d_v017_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slope_126d_2d_v018_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slope_252d_2d_v019_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_slope_504d_2d_v020_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slope_21d_2d_v021_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slope_63d_2d_v022_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slope_126d_2d_v023_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slope_252d_2d_v024_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_slope_504d_2d_v025_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slope_21d_2d_v026_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slope_63d_2d_v027_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slope_126d_2d_v028_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slope_252d_2d_v029_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_slope_504d_2d_v030_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slope_21d_2d_v031_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slope_63d_2d_v032_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slope_126d_2d_v033_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slope_252d_2d_v034_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_slope_504d_2d_v035_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sm21_sl21_2d_v036_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sm63_sl21_2d_v037_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sm63_sl63_2d_v038_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sm252_sl63_2d_v039_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sm252_sl126_2d_v040_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sm21_sl21_2d_v041_signal(sharefactor, closeadj):
    base = _mean(_f034_sf_chg(sharefactor), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sm63_sl21_2d_v042_signal(sharefactor, closeadj):
    base = _mean(_f034_sf_chg(sharefactor), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sm63_sl63_2d_v043_signal(sharefactor, closeadj):
    base = _mean(_f034_sf_chg(sharefactor), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sm252_sl63_2d_v044_signal(sharefactor, closeadj):
    base = _mean(_f034_sf_chg(sharefactor), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sm252_sl126_2d_v045_signal(sharefactor, closeadj):
    base = _mean(_f034_sf_chg(sharefactor), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sm21_sl21_2d_v046_signal(sharefactor, closeadj):
    base = _mean(np.log(sharefactor.abs().replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sm63_sl21_2d_v047_signal(sharefactor, closeadj):
    base = _mean(np.log(sharefactor.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sm63_sl63_2d_v048_signal(sharefactor, closeadj):
    base = _mean(np.log(sharefactor.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sm252_sl63_2d_v049_signal(sharefactor, closeadj):
    base = _mean(np.log(sharefactor.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sm252_sl126_2d_v050_signal(sharefactor, closeadj):
    base = _mean(np.log(sharefactor.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sm21_sl21_2d_v051_signal(sharefactor, closeadj):
    base = _mean((sharefactor > 1).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sm63_sl21_2d_v052_signal(sharefactor, closeadj):
    base = _mean((sharefactor > 1).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sm63_sl63_2d_v053_signal(sharefactor, closeadj):
    base = _mean((sharefactor > 1).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sm252_sl63_2d_v054_signal(sharefactor, closeadj):
    base = _mean((sharefactor > 1).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sm252_sl126_2d_v055_signal(sharefactor, closeadj):
    base = _mean((sharefactor > 1).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sm21_sl21_2d_v056_signal(sharefactor, closeadj):
    base = _mean((sharefactor < 1).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sm63_sl21_2d_v057_signal(sharefactor, closeadj):
    base = _mean((sharefactor < 1).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sm63_sl63_2d_v058_signal(sharefactor, closeadj):
    base = _mean((sharefactor < 1).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sm252_sl63_2d_v059_signal(sharefactor, closeadj):
    base = _mean((sharefactor < 1).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sm252_sl126_2d_v060_signal(sharefactor, closeadj):
    base = _mean((sharefactor < 1).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sm21_sl21_2d_v061_signal(sharefactor, closeadj):
    base = _mean(sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sm63_sl21_2d_v062_signal(sharefactor, closeadj):
    base = _mean(sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sm63_sl63_2d_v063_signal(sharefactor, closeadj):
    base = _mean(sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sm252_sl63_2d_v064_signal(sharefactor, closeadj):
    base = _mean(sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sm252_sl126_2d_v065_signal(sharefactor, closeadj):
    base = _mean(sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sm21_sl21_2d_v066_signal(sharefactor, closeadj):
    base = _mean((sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sm63_sl21_2d_v067_signal(sharefactor, closeadj):
    base = _mean((sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sm63_sl63_2d_v068_signal(sharefactor, closeadj):
    base = _mean((sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sm252_sl63_2d_v069_signal(sharefactor, closeadj):
    base = _mean((sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sm252_sl126_2d_v070_signal(sharefactor, closeadj):
    base = _mean((sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_pctslope_21d_2d_v071_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_pctslope_63d_2d_v072_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_pctslope_252d_2d_v073_signal(sharefactor, closeadj):
    base = sharefactor
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_pctslope_21d_2d_v074_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_pctslope_63d_2d_v075_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_pctslope_252d_2d_v076_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_pctslope_21d_2d_v077_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_pctslope_63d_2d_v078_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_pctslope_252d_2d_v079_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_pctslope_21d_2d_v080_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_pctslope_63d_2d_v081_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_pctslope_252d_2d_v082_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_pctslope_21d_2d_v083_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_pctslope_63d_2d_v084_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_pctslope_252d_2d_v085_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_pctslope_21d_2d_v086_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_pctslope_63d_2d_v087_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_pctslope_252d_2d_v088_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_pctslope_21d_2d_v089_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_pctslope_63d_2d_v090_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_pctslope_252d_2d_v091_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sgnslope_21d_2d_v092_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sgnslope_63d_2d_v093_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_sgnslope_252d_2d_v094_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sgnslope_21d_2d_v095_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sgnslope_63d_2d_v096_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_sgnslope_252d_2d_v097_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sgnslope_21d_2d_v098_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sgnslope_63d_2d_v099_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_sgnslope_252d_2d_v100_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sgnslope_21d_2d_v101_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sgnslope_63d_2d_v102_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_sgnslope_252d_2d_v103_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sgnslope_21d_2d_v104_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sgnslope_63d_2d_v105_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_sgnslope_252d_2d_v106_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sgnslope_21d_2d_v107_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sgnslope_63d_2d_v108_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_sgnslope_252d_2d_v109_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sgnslope_21d_2d_v110_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sgnslope_63d_2d_v111_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_sgnslope_252d_2d_v112_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_logmagslope_21d_2d_v113_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_logmagslope_63d_2d_v114_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_logmagslope_252d_2d_v115_signal(sharefactor, closeadj):
    base = sharefactor
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_logmagslope_21d_2d_v116_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_logmagslope_63d_2d_v117_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_logmagslope_252d_2d_v118_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_logmagslope_21d_2d_v119_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_logmagslope_63d_2d_v120_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf_log
def f034sfs_f034_share_factor_splits_sf_log_logmagslope_252d_2d_v121_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_logmagslope_21d_2d_v122_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_logmagslope_63d_2d_v123_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_logmagslope_252d_2d_v124_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_logmagslope_21d_2d_v125_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_logmagslope_63d_2d_v126_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_logmagslope_252d_2d_v127_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_logmagslope_21d_2d_v128_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_logmagslope_63d_2d_v129_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_logmagslope_252d_2d_v130_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_logmagslope_21d_2d_v131_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_logmagslope_63d_2d_v132_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_logmagslope_252d_2d_v133_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf_lvl|
def f034sfs_f034_share_factor_splits_sf_lvl_logslope_63d_2d_v134_signal(sharefactor, closeadj):
    base = np.log((sharefactor).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf_lvl|
def f034sfs_f034_share_factor_splits_sf_lvl_logslope_252d_2d_v135_signal(sharefactor, closeadj):
    base = np.log((sharefactor).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf_chg|
def f034sfs_f034_share_factor_splits_sf_chg_logslope_63d_2d_v136_signal(sharefactor, closeadj):
    base = np.log((_f034_sf_chg(sharefactor)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf_chg|
def f034sfs_f034_share_factor_splits_sf_chg_logslope_252d_2d_v137_signal(sharefactor, closeadj):
    base = np.log((_f034_sf_chg(sharefactor)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf_log|
def f034sfs_f034_share_factor_splits_sf_log_logslope_63d_2d_v138_signal(sharefactor, closeadj):
    base = np.log((np.log(sharefactor.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf_log|
def f034sfs_f034_share_factor_splits_sf_log_logslope_252d_2d_v139_signal(sharefactor, closeadj):
    base = np.log((np.log(sharefactor.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf_above1|
def f034sfs_f034_share_factor_splits_sf_above1_logslope_63d_2d_v140_signal(sharefactor, closeadj):
    base = np.log(((sharefactor > 1).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf_above1|
def f034sfs_f034_share_factor_splits_sf_above1_logslope_252d_2d_v141_signal(sharefactor, closeadj):
    base = np.log(((sharefactor > 1).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf_below1|
def f034sfs_f034_share_factor_splits_sf_below1_logslope_63d_2d_v142_signal(sharefactor, closeadj):
    base = np.log(((sharefactor < 1).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf_below1|
def f034sfs_f034_share_factor_splits_sf_below1_logslope_252d_2d_v143_signal(sharefactor, closeadj):
    base = np.log(((sharefactor < 1).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf_cum_252d|
def f034sfs_f034_share_factor_splits_sf_cum_252d_logslope_63d_2d_v144_signal(sharefactor, closeadj):
    base = np.log((sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf_cum_252d|
def f034sfs_f034_share_factor_splits_sf_cum_252d_logslope_252d_2d_v145_signal(sharefactor, closeadj):
    base = np.log((sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf_event_density_252d|
def f034sfs_f034_share_factor_splits_sf_event_density_252d_logslope_63d_2d_v146_signal(sharefactor, closeadj):
    base = np.log(((sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf_event_density_252d|
def f034sfs_f034_share_factor_splits_sf_event_density_252d_logslope_252d_2d_v147_signal(sharefactor, closeadj):
    base = np.log(((sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

