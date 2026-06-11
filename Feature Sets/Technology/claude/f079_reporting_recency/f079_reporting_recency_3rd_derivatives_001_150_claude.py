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


# 21d acceleration of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_accel_21d_3d_v001_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_accel_63d_3d_v002_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_accel_126d_3d_v003_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_accel_252d_3d_v004_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of age_log
def f079rrc_f079_reporting_recency_age_log_accel_21d_3d_v005_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_log
def f079rrc_f079_reporting_recency_age_log_accel_63d_3d_v006_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of age_log
def f079rrc_f079_reporting_recency_age_log_accel_126d_3d_v007_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_log
def f079rrc_f079_reporting_recency_age_log_accel_252d_3d_v008_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_accel_21d_3d_v009_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_accel_63d_3d_v010_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_accel_126d_3d_v011_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_accel_252d_3d_v012_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_accel_21d_3d_v013_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_accel_63d_3d_v014_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_accel_126d_3d_v015_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_accel_252d_3d_v016_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of age_change
def f079rrc_f079_reporting_recency_age_change_accel_21d_3d_v017_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_change
def f079rrc_f079_reporting_recency_age_change_accel_63d_3d_v018_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of age_change
def f079rrc_f079_reporting_recency_age_change_accel_126d_3d_v019_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_change
def f079rrc_f079_reporting_recency_age_change_accel_252d_3d_v020_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_accel_21d_3d_v021_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_accel_63d_3d_v022_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_accel_126d_3d_v023_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_accel_252d_3d_v024_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_accel_21d_3d_v025_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_accel_63d_3d_v026_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_accel_126d_3d_v027_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_accel_252d_3d_v028_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slopez_21d_z126_3d_v029_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slopez_63d_z252_3d_v030_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slopez_126d_z252_3d_v031_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_slopez_252d_z504_3d_v032_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of age_log
def f079rrc_f079_reporting_recency_age_log_slopez_21d_z126_3d_v033_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of age_log
def f079rrc_f079_reporting_recency_age_log_slopez_63d_z252_3d_v034_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of age_log
def f079rrc_f079_reporting_recency_age_log_slopez_126d_z252_3d_v035_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of age_log
def f079rrc_f079_reporting_recency_age_log_slopez_252d_z504_3d_v036_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slopez_21d_z126_3d_v037_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slopez_63d_z252_3d_v038_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slopez_126d_z252_3d_v039_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_slopez_252d_z504_3d_v040_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slopez_21d_z126_3d_v041_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slopez_63d_z252_3d_v042_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slopez_126d_z252_3d_v043_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_slopez_252d_z504_3d_v044_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of age_change
def f079rrc_f079_reporting_recency_age_change_slopez_21d_z126_3d_v045_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of age_change
def f079rrc_f079_reporting_recency_age_change_slopez_63d_z252_3d_v046_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of age_change
def f079rrc_f079_reporting_recency_age_change_slopez_126d_z252_3d_v047_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of age_change
def f079rrc_f079_reporting_recency_age_change_slopez_252d_z504_3d_v048_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slopez_21d_z126_3d_v049_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slopez_63d_z252_3d_v050_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slopez_126d_z252_3d_v051_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_slopez_252d_z504_3d_v052_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slopez_21d_z126_3d_v053_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slopez_63d_z252_3d_v054_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slopez_126d_z252_3d_v055_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_slopez_252d_z504_3d_v056_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_jerk_21d_3d_v057_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_jerk_63d_3d_v058_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_jerk_126d_3d_v059_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of age_log
def f079rrc_f079_reporting_recency_age_log_jerk_21d_3d_v060_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of age_log
def f079rrc_f079_reporting_recency_age_log_jerk_63d_3d_v061_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of age_log
def f079rrc_f079_reporting_recency_age_log_jerk_126d_3d_v062_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_jerk_21d_3d_v063_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_jerk_63d_3d_v064_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_jerk_126d_3d_v065_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_jerk_21d_3d_v066_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_jerk_63d_3d_v067_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_jerk_126d_3d_v068_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of age_change
def f079rrc_f079_reporting_recency_age_change_jerk_21d_3d_v069_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of age_change
def f079rrc_f079_reporting_recency_age_change_jerk_63d_3d_v070_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of age_change
def f079rrc_f079_reporting_recency_age_change_jerk_126d_3d_v071_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_jerk_21d_3d_v072_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_jerk_63d_3d_v073_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_jerk_126d_3d_v074_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_jerk_21d_3d_v075_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_jerk_63d_3d_v076_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_jerk_126d_3d_v077_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of filing_age_d smoothed over 252d
def f079rrc_f079_reporting_recency_filing_age_d_smoothaccel_63d_sm252_3d_v078_signal(stale_age_days, closeadj):
    base = stale_age_days
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of filing_age_d smoothed over 504d
def f079rrc_f079_reporting_recency_filing_age_d_smoothaccel_252d_sm504_3d_v079_signal(stale_age_days, closeadj):
    base = stale_age_days
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of age_log smoothed over 252d
def f079rrc_f079_reporting_recency_age_log_smoothaccel_63d_sm252_3d_v080_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of age_log smoothed over 504d
def f079rrc_f079_reporting_recency_age_log_smoothaccel_252d_sm504_3d_v081_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of age_above90d smoothed over 252d
def f079rrc_f079_reporting_recency_age_above90d_smoothaccel_63d_sm252_3d_v082_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of age_above90d smoothed over 504d
def f079rrc_f079_reporting_recency_age_above90d_smoothaccel_252d_sm504_3d_v083_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of age_above180d smoothed over 252d
def f079rrc_f079_reporting_recency_age_above180d_smoothaccel_63d_sm252_3d_v084_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of age_above180d smoothed over 504d
def f079rrc_f079_reporting_recency_age_above180d_smoothaccel_252d_sm504_3d_v085_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of age_change smoothed over 252d
def f079rrc_f079_reporting_recency_age_change_smoothaccel_63d_sm252_3d_v086_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of age_change smoothed over 504d
def f079rrc_f079_reporting_recency_age_change_smoothaccel_252d_sm504_3d_v087_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of age_to_qend smoothed over 252d
def f079rrc_f079_reporting_recency_age_to_qend_smoothaccel_63d_sm252_3d_v088_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of age_to_qend smoothed over 504d
def f079rrc_f079_reporting_recency_age_to_qend_smoothaccel_252d_sm504_3d_v089_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of avg_age_252 smoothed over 252d
def f079rrc_f079_reporting_recency_avg_age_252_smoothaccel_63d_sm252_3d_v090_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of avg_age_252 smoothed over 504d
def f079rrc_f079_reporting_recency_avg_age_252_smoothaccel_252d_sm504_3d_v091_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_accelz_21d_z252_3d_v092_signal(stale_age_days, closeadj):
    base = stale_age_days
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_accelz_63d_z504_3d_v093_signal(stale_age_days, closeadj):
    base = stale_age_days
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of age_log
def f079rrc_f079_reporting_recency_age_log_accelz_21d_z252_3d_v094_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of age_log
def f079rrc_f079_reporting_recency_age_log_accelz_63d_z504_3d_v095_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_accelz_21d_z252_3d_v096_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_accelz_63d_z504_3d_v097_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_accelz_21d_z252_3d_v098_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_accelz_63d_z504_3d_v099_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of age_change
def f079rrc_f079_reporting_recency_age_change_accelz_21d_z252_3d_v100_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of age_change
def f079rrc_f079_reporting_recency_age_change_accelz_63d_z504_3d_v101_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_accelz_21d_z252_3d_v102_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_accelz_63d_z504_3d_v103_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_accelz_21d_z252_3d_v104_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_accelz_63d_z504_3d_v105_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in filing_age_d (raw count, no price scaling)
def f079rrc_f079_reporting_recency_filing_age_d_signflip_63d_3d_v106_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in filing_age_d (raw count, no price scaling)
def f079rrc_f079_reporting_recency_filing_age_d_signflip_252d_3d_v107_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in age_log (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_log_signflip_63d_3d_v108_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in age_log (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_log_signflip_252d_3d_v109_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in age_above90d (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_above90d_signflip_63d_3d_v110_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in age_above90d (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_above90d_signflip_252d_3d_v111_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in age_above180d (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_above180d_signflip_63d_3d_v112_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in age_above180d (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_above180d_signflip_252d_3d_v113_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in age_change (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_change_signflip_63d_3d_v114_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in age_change (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_change_signflip_252d_3d_v115_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in age_to_qend (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_to_qend_signflip_63d_3d_v116_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in age_to_qend (raw count, no price scaling)
def f079rrc_f079_reporting_recency_age_to_qend_signflip_252d_3d_v117_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in avg_age_252 (raw count, no price scaling)
def f079rrc_f079_reporting_recency_avg_age_252_signflip_63d_3d_v118_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in avg_age_252 (raw count, no price scaling)
def f079rrc_f079_reporting_recency_avg_age_252_signflip_252d_3d_v119_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of filing_age_d normalized by 252d range
def f079rrc_f079_reporting_recency_filing_age_d_rngaccel_63d_r252_3d_v120_signal(stale_age_days, closeadj):
    base = stale_age_days
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of filing_age_d normalized by 504d range
def f079rrc_f079_reporting_recency_filing_age_d_rngaccel_252d_r504_3d_v121_signal(stale_age_days, closeadj):
    base = stale_age_days
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_log normalized by 252d range
def f079rrc_f079_reporting_recency_age_log_rngaccel_63d_r252_3d_v122_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_log normalized by 504d range
def f079rrc_f079_reporting_recency_age_log_rngaccel_252d_r504_3d_v123_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_above90d normalized by 252d range
def f079rrc_f079_reporting_recency_age_above90d_rngaccel_63d_r252_3d_v124_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_above90d normalized by 504d range
def f079rrc_f079_reporting_recency_age_above90d_rngaccel_252d_r504_3d_v125_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_above180d normalized by 252d range
def f079rrc_f079_reporting_recency_age_above180d_rngaccel_63d_r252_3d_v126_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_above180d normalized by 504d range
def f079rrc_f079_reporting_recency_age_above180d_rngaccel_252d_r504_3d_v127_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_change normalized by 252d range
def f079rrc_f079_reporting_recency_age_change_rngaccel_63d_r252_3d_v128_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_change normalized by 504d range
def f079rrc_f079_reporting_recency_age_change_rngaccel_252d_r504_3d_v129_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of age_to_qend normalized by 252d range
def f079rrc_f079_reporting_recency_age_to_qend_rngaccel_63d_r252_3d_v130_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of age_to_qend normalized by 504d range
def f079rrc_f079_reporting_recency_age_to_qend_rngaccel_252d_r504_3d_v131_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of avg_age_252 normalized by 252d range
def f079rrc_f079_reporting_recency_avg_age_252_rngaccel_63d_r252_3d_v132_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of avg_age_252 normalized by 504d range
def f079rrc_f079_reporting_recency_avg_age_252_rngaccel_252d_r504_3d_v133_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_cumslope_21d_3d_v134_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_cumslope_63d_3d_v135_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_cumslope_252d_3d_v136_signal(stale_age_days, closeadj):
    base = stale_age_days
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of age_log
def f079rrc_f079_reporting_recency_age_log_cumslope_21d_3d_v137_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of age_log
def f079rrc_f079_reporting_recency_age_log_cumslope_63d_3d_v138_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of age_log
def f079rrc_f079_reporting_recency_age_log_cumslope_252d_3d_v139_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_cumslope_21d_3d_v140_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_cumslope_63d_3d_v141_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_cumslope_252d_3d_v142_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_cumslope_21d_3d_v143_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_cumslope_63d_3d_v144_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_cumslope_252d_3d_v145_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of age_change
def f079rrc_f079_reporting_recency_age_change_cumslope_21d_3d_v146_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of age_change
def f079rrc_f079_reporting_recency_age_change_cumslope_63d_3d_v147_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of age_change
def f079rrc_f079_reporting_recency_age_change_cumslope_252d_3d_v148_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_cumslope_21d_3d_v149_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_cumslope_63d_3d_v150_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

