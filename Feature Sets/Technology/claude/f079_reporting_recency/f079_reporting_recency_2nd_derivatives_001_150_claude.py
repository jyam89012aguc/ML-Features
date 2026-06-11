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
def _f079_age(stale_age_days):
    return stale_age_days


# 21d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slope_21d_2d_v001_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slope_63d_2d_v002_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slope_126d_2d_v003_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slope_252d_2d_v004_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slope_504d_2d_v005_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of age_log
def f079rrc_f079_reporting_recency_age_log_slope_21d_2d_v006_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of age_log
def f079rrc_f079_reporting_recency_age_log_slope_63d_2d_v007_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of age_log
def f079rrc_f079_reporting_recency_age_log_slope_126d_2d_v008_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of age_log
def f079rrc_f079_reporting_recency_age_log_slope_252d_2d_v009_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of age_log
def f079rrc_f079_reporting_recency_age_log_slope_504d_2d_v010_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slope_21d_2d_v011_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slope_63d_2d_v012_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slope_126d_2d_v013_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slope_252d_2d_v014_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slope_504d_2d_v015_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slope_21d_2d_v016_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slope_63d_2d_v017_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slope_126d_2d_v018_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slope_252d_2d_v019_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slope_504d_2d_v020_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of age_change
def f079rrc_f079_reporting_recency_age_change_slope_21d_2d_v021_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of age_change
def f079rrc_f079_reporting_recency_age_change_slope_63d_2d_v022_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of age_change
def f079rrc_f079_reporting_recency_age_change_slope_126d_2d_v023_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of age_change
def f079rrc_f079_reporting_recency_age_change_slope_252d_2d_v024_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of age_change
def f079rrc_f079_reporting_recency_age_change_slope_504d_2d_v025_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slope_21d_2d_v026_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slope_63d_2d_v027_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slope_126d_2d_v028_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slope_252d_2d_v029_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slope_504d_2d_v030_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slope_21d_2d_v031_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slope_63d_2d_v032_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slope_126d_2d_v033_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slope_252d_2d_v034_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slope_504d_2d_v035_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sm21_sl21_2d_v036_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sm63_sl21_2d_v037_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sm63_sl63_2d_v038_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sm252_sl63_2d_v039_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sm252_sl126_2d_v040_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sm21_sl21_2d_v041_signal(stale_age_days, closeadj):
    base = _mean(np.log(stale_age_days.abs().replace(0, np.nan) + 1), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sm63_sl21_2d_v042_signal(stale_age_days, closeadj):
    base = _mean(np.log(stale_age_days.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sm63_sl63_2d_v043_signal(stale_age_days, closeadj):
    base = _mean(np.log(stale_age_days.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sm252_sl63_2d_v044_signal(stale_age_days, closeadj):
    base = _mean(np.log(stale_age_days.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sm252_sl126_2d_v045_signal(stale_age_days, closeadj):
    base = _mean(np.log(stale_age_days.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sm21_sl21_2d_v046_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 90).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sm63_sl21_2d_v047_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 90).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sm63_sl63_2d_v048_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 90).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sm252_sl63_2d_v049_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 90).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sm252_sl126_2d_v050_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 90).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sm21_sl21_2d_v051_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 180).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sm63_sl21_2d_v052_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 180).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sm63_sl63_2d_v053_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 180).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sm252_sl63_2d_v054_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 180).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sm252_sl126_2d_v055_signal(stale_age_days, closeadj):
    base = _mean((stale_age_days > 180).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sm21_sl21_2d_v056_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.diff(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sm63_sl21_2d_v057_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.diff(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sm63_sl63_2d_v058_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.diff(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sm252_sl63_2d_v059_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.diff(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sm252_sl126_2d_v060_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.diff(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sm21_sl21_2d_v061_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days % 90, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sm63_sl21_2d_v062_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days % 90, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sm63_sl63_2d_v063_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days % 90, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sm252_sl63_2d_v064_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days % 90, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sm252_sl126_2d_v065_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days % 90, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sm21_sl21_2d_v066_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.rolling(252, min_periods=63).mean(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sm63_sl21_2d_v067_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sm63_sl63_2d_v068_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sm252_sl63_2d_v069_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sm252_sl126_2d_v070_signal(stale_age_days, closeadj):
    base = _mean(stale_age_days.rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_pctslope_21d_2d_v071_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_pctslope_63d_2d_v072_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_pctslope_252d_2d_v073_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of age_log
def f079rrc_f079_reporting_recency_age_log_pctslope_21d_2d_v074_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of age_log
def f079rrc_f079_reporting_recency_age_log_pctslope_63d_2d_v075_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of age_log
def f079rrc_f079_reporting_recency_age_log_pctslope_252d_2d_v076_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_pctslope_21d_2d_v077_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_pctslope_63d_2d_v078_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_pctslope_252d_2d_v079_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_pctslope_21d_2d_v080_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_pctslope_63d_2d_v081_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_pctslope_252d_2d_v082_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of age_change
def f079rrc_f079_reporting_recency_age_change_pctslope_21d_2d_v083_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of age_change
def f079rrc_f079_reporting_recency_age_change_pctslope_63d_2d_v084_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of age_change
def f079rrc_f079_reporting_recency_age_change_pctslope_252d_2d_v085_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_pctslope_21d_2d_v086_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_pctslope_63d_2d_v087_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_pctslope_252d_2d_v088_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_pctslope_21d_2d_v089_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_pctslope_63d_2d_v090_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_pctslope_252d_2d_v091_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sgnslope_21d_2d_v092_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sgnslope_63d_2d_v093_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_sgnslope_252d_2d_v094_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sgnslope_21d_2d_v095_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sgnslope_63d_2d_v096_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of age_log
def f079rrc_f079_reporting_recency_age_log_sgnslope_252d_2d_v097_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sgnslope_21d_2d_v098_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sgnslope_63d_2d_v099_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_sgnslope_252d_2d_v100_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sgnslope_21d_2d_v101_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sgnslope_63d_2d_v102_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_sgnslope_252d_2d_v103_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sgnslope_21d_2d_v104_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sgnslope_63d_2d_v105_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of age_change
def f079rrc_f079_reporting_recency_age_change_sgnslope_252d_2d_v106_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sgnslope_21d_2d_v107_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sgnslope_63d_2d_v108_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_sgnslope_252d_2d_v109_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sgnslope_21d_2d_v110_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sgnslope_63d_2d_v111_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_sgnslope_252d_2d_v112_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_logmagslope_21d_2d_v113_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_logmagslope_63d_2d_v114_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_logmagslope_252d_2d_v115_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of age_log
def f079rrc_f079_reporting_recency_age_log_logmagslope_21d_2d_v116_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of age_log
def f079rrc_f079_reporting_recency_age_log_logmagslope_63d_2d_v117_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of age_log
def f079rrc_f079_reporting_recency_age_log_logmagslope_252d_2d_v118_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_logmagslope_21d_2d_v119_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_logmagslope_63d_2d_v120_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_logmagslope_252d_2d_v121_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_logmagslope_21d_2d_v122_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_logmagslope_63d_2d_v123_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_logmagslope_252d_2d_v124_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of age_change
def f079rrc_f079_reporting_recency_age_change_logmagslope_21d_2d_v125_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of age_change
def f079rrc_f079_reporting_recency_age_change_logmagslope_63d_2d_v126_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of age_change
def f079rrc_f079_reporting_recency_age_change_logmagslope_252d_2d_v127_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_logmagslope_21d_2d_v128_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_logmagslope_63d_2d_v129_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_logmagslope_252d_2d_v130_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_logmagslope_21d_2d_v131_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_logmagslope_63d_2d_v132_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_logmagslope_252d_2d_v133_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|filing_age_d|
def f079rrc_f079_reporting_recency_filing_age_d_logslope_63d_2d_v134_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|filing_age_d|
def f079rrc_f079_reporting_recency_filing_age_d_logslope_252d_2d_v135_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|age_log|
def f079rrc_f079_reporting_recency_age_log_logslope_63d_2d_v136_signal(stale_age_days, closeadj):
    base = np.log((np.log(stale_age_days.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|age_log|
def f079rrc_f079_reporting_recency_age_log_logslope_252d_2d_v137_signal(stale_age_days, closeadj):
    base = np.log((np.log(stale_age_days.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|age_above90d|
def f079rrc_f079_reporting_recency_age_above90d_logslope_63d_2d_v138_signal(stale_age_days, closeadj):
    base = np.log(((stale_age_days > 90).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|age_above90d|
def f079rrc_f079_reporting_recency_age_above90d_logslope_252d_2d_v139_signal(stale_age_days, closeadj):
    base = np.log(((stale_age_days > 90).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|age_above180d|
def f079rrc_f079_reporting_recency_age_above180d_logslope_63d_2d_v140_signal(stale_age_days, closeadj):
    base = np.log(((stale_age_days > 180).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|age_above180d|
def f079rrc_f079_reporting_recency_age_above180d_logslope_252d_2d_v141_signal(stale_age_days, closeadj):
    base = np.log(((stale_age_days > 180).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|age_change|
def f079rrc_f079_reporting_recency_age_change_logslope_63d_2d_v142_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days.diff()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|age_change|
def f079rrc_f079_reporting_recency_age_change_logslope_252d_2d_v143_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days.diff()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|age_to_qend|
def f079rrc_f079_reporting_recency_age_to_qend_logslope_63d_2d_v144_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days % 90).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|age_to_qend|
def f079rrc_f079_reporting_recency_age_to_qend_logslope_252d_2d_v145_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days % 90).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|avg_age_252|
def f079rrc_f079_reporting_recency_avg_age_252_logslope_63d_2d_v146_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days.rolling(252, min_periods=63).mean()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|avg_age_252|
def f079rrc_f079_reporting_recency_avg_age_252_logslope_252d_2d_v147_signal(stale_age_days, closeadj):
    base = np.log((stale_age_days.rolling(252, min_periods=63).mean()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

