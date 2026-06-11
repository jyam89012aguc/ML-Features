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
def _f034_sf_chg(sharefactor):
    return sharefactor.diff()


# 21d mean of sf_lvl scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_lvl_mean_21d_base_v001_signal(sharefactor, closeadj):
    base = sharefactor
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf_lvl scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_lvl_mean_63d_base_v002_signal(sharefactor, closeadj):
    base = sharefactor
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf_lvl scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_lvl_mean_126d_base_v003_signal(sharefactor, closeadj):
    base = sharefactor
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf_lvl scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_lvl_mean_252d_base_v004_signal(sharefactor, closeadj):
    base = sharefactor
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf_lvl scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_lvl_mean_504d_base_v005_signal(sharefactor, closeadj):
    base = sharefactor
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sf_chg scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_chg_mean_21d_base_v006_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf_chg scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_chg_mean_63d_base_v007_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf_chg scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_chg_mean_126d_base_v008_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf_chg scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_chg_mean_252d_base_v009_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf_chg scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_chg_mean_504d_base_v010_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sf_log scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_log_mean_21d_base_v011_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf_log scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_log_mean_63d_base_v012_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf_log scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_log_mean_126d_base_v013_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf_log scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_log_mean_252d_base_v014_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf_log scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_log_mean_504d_base_v015_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sf_above1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_above1_mean_21d_base_v016_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf_above1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_above1_mean_63d_base_v017_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf_above1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_above1_mean_126d_base_v018_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf_above1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_above1_mean_252d_base_v019_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf_above1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_above1_mean_504d_base_v020_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sf_below1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_below1_mean_21d_base_v021_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf_below1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_below1_mean_63d_base_v022_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf_below1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_below1_mean_126d_base_v023_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf_below1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_below1_mean_252d_base_v024_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf_below1 scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_below1_mean_504d_base_v025_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sf_cum_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_cum_252d_mean_21d_base_v026_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf_cum_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_cum_252d_mean_63d_base_v027_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf_cum_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_cum_252d_mean_126d_base_v028_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf_cum_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_cum_252d_mean_252d_base_v029_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf_cum_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_cum_252d_mean_504d_base_v030_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sf_event_density_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_event_density_252d_mean_21d_base_v031_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf_event_density_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_event_density_252d_mean_63d_base_v032_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf_event_density_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_event_density_252d_mean_126d_base_v033_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf_event_density_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_event_density_252d_mean_252d_base_v034_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf_event_density_252d scaled by closeadj
def f034sfs_f034_share_factor_splits_sf_event_density_252d_mean_504d_base_v035_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_median_63d_base_v036_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_median_252d_base_v037_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_median_504d_base_v038_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_median_63d_base_v039_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_median_252d_base_v040_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_median_504d_base_v041_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf_log
def f034sfs_f034_share_factor_splits_sf_log_median_63d_base_v042_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf_log
def f034sfs_f034_share_factor_splits_sf_log_median_252d_base_v043_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf_log
def f034sfs_f034_share_factor_splits_sf_log_median_504d_base_v044_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_median_63d_base_v045_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_median_252d_base_v046_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_median_504d_base_v047_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_median_63d_base_v048_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_median_252d_base_v049_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_median_504d_base_v050_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_median_63d_base_v051_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_median_252d_base_v052_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_median_504d_base_v053_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_median_63d_base_v054_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_median_252d_base_v055_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_median_504d_base_v056_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_rmax_252d_base_v057_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_rmax_504d_base_v058_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_rmax_252d_base_v059_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_rmax_504d_base_v060_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf_log
def f034sfs_f034_share_factor_splits_sf_log_rmax_252d_base_v061_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf_log
def f034sfs_f034_share_factor_splits_sf_log_rmax_504d_base_v062_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_rmax_252d_base_v063_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf_above1
def f034sfs_f034_share_factor_splits_sf_above1_rmax_504d_base_v064_signal(sharefactor, closeadj):
    base = (sharefactor > 1).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_rmax_252d_base_v065_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf_below1
def f034sfs_f034_share_factor_splits_sf_below1_rmax_504d_base_v066_signal(sharefactor, closeadj):
    base = (sharefactor < 1).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_rmax_252d_base_v067_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf_cum_252d
def f034sfs_f034_share_factor_splits_sf_cum_252d_rmax_504d_base_v068_signal(sharefactor, closeadj):
    base = sharefactor.rolling(252, min_periods=63).max() / sharefactor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_rmax_252d_base_v069_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf_event_density_252d
def f034sfs_f034_share_factor_splits_sf_event_density_252d_rmax_504d_base_v070_signal(sharefactor, closeadj):
    base = (sharefactor.diff().abs() > 0.01).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_rmin_252d_base_v071_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sf_lvl
def f034sfs_f034_share_factor_splits_sf_lvl_rmin_504d_base_v072_signal(sharefactor, closeadj):
    base = sharefactor
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_rmin_252d_base_v073_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sf_chg
def f034sfs_f034_share_factor_splits_sf_chg_rmin_504d_base_v074_signal(sharefactor, closeadj):
    base = _f034_sf_chg(sharefactor)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sf_log
def f034sfs_f034_share_factor_splits_sf_log_rmin_252d_base_v075_signal(sharefactor, closeadj):
    base = np.log(sharefactor.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

