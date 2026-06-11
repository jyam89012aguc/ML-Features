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
def _f081_age(ipo_age_days):
    return ipo_age_days


# 21d acceleration of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_accel_21d_3d_v001_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_accel_63d_3d_v002_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_accel_126d_3d_v003_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_accel_252d_3d_v004_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_accel_21d_3d_v005_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_accel_63d_3d_v006_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_accel_126d_3d_v007_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_accel_252d_3d_v008_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_accel_21d_3d_v009_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_accel_63d_3d_v010_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_accel_126d_3d_v011_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_accel_252d_3d_v012_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_accel_21d_3d_v013_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_accel_63d_3d_v014_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_accel_126d_3d_v015_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_accel_252d_3d_v016_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_accel_21d_3d_v017_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_accel_63d_3d_v018_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_accel_126d_3d_v019_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_accel_252d_3d_v020_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_accel_21d_3d_v021_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_accel_63d_3d_v022_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_accel_126d_3d_v023_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_accel_252d_3d_v024_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_accel_21d_3d_v025_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_accel_63d_3d_v026_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_accel_126d_3d_v027_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_accel_252d_3d_v028_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slopez_21d_z126_3d_v029_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slopez_63d_z252_3d_v030_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slopez_126d_z252_3d_v031_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slopez_252d_z504_3d_v032_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slopez_21d_z126_3d_v033_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slopez_63d_z252_3d_v034_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slopez_126d_z252_3d_v035_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slopez_252d_z504_3d_v036_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slopez_21d_z126_3d_v037_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slopez_63d_z252_3d_v038_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slopez_126d_z252_3d_v039_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slopez_252d_z504_3d_v040_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slopez_21d_z126_3d_v041_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slopez_63d_z252_3d_v042_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slopez_126d_z252_3d_v043_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slopez_252d_z504_3d_v044_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slopez_21d_z126_3d_v045_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slopez_63d_z252_3d_v046_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slopez_126d_z252_3d_v047_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slopez_252d_z504_3d_v048_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slopez_21d_z126_3d_v049_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slopez_63d_z252_3d_v050_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slopez_126d_z252_3d_v051_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slopez_252d_z504_3d_v052_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slopez_21d_z126_3d_v053_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slopez_63d_z252_3d_v054_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slopez_126d_z252_3d_v055_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slopez_252d_z504_3d_v056_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_jerk_21d_3d_v057_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_jerk_63d_3d_v058_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_jerk_126d_3d_v059_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_jerk_21d_3d_v060_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_jerk_63d_3d_v061_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_jerk_126d_3d_v062_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_jerk_21d_3d_v063_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_jerk_63d_3d_v064_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_jerk_126d_3d_v065_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_jerk_21d_3d_v066_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_jerk_63d_3d_v067_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_jerk_126d_3d_v068_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_jerk_21d_3d_v069_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_jerk_63d_3d_v070_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_jerk_126d_3d_v071_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_jerk_21d_3d_v072_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_jerk_63d_3d_v073_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_jerk_126d_3d_v074_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_jerk_21d_3d_v075_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_jerk_63d_3d_v076_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_jerk_126d_3d_v077_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ipo_age_d smoothed over 252d
def f081cim_f081_company_identity_metadata_ipo_age_d_smoothaccel_63d_sm252_3d_v078_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ipo_age_d smoothed over 504d
def f081cim_f081_company_identity_metadata_ipo_age_d_smoothaccel_252d_sm504_3d_v079_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ipo_age_log smoothed over 252d
def f081cim_f081_company_identity_metadata_ipo_age_log_smoothaccel_63d_sm252_3d_v080_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ipo_age_log smoothed over 504d
def f081cim_f081_company_identity_metadata_ipo_age_log_smoothaccel_252d_sm504_3d_v081_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ipo_age_above_5y smoothed over 252d
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_smoothaccel_63d_sm252_3d_v082_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ipo_age_above_5y smoothed over 504d
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_smoothaccel_252d_sm504_3d_v083_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ipo_age_under_2y smoothed over 252d
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_smoothaccel_63d_sm252_3d_v084_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ipo_age_under_2y smoothed over 504d
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_smoothaccel_252d_sm504_3d_v085_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of on_nasdaq smoothed over 252d
def f081cim_f081_company_identity_metadata_on_nasdaq_smoothaccel_63d_sm252_3d_v086_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of on_nasdaq smoothed over 504d
def f081cim_f081_company_identity_metadata_on_nasdaq_smoothaccel_252d_sm504_3d_v087_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of on_nyse smoothed over 252d
def f081cim_f081_company_identity_metadata_on_nyse_smoothaccel_63d_sm252_3d_v088_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of on_nyse smoothed over 504d
def f081cim_f081_company_identity_metadata_on_nyse_smoothaccel_252d_sm504_3d_v089_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of scale_mcap_idx smoothed over 252d
def f081cim_f081_company_identity_metadata_scale_mcap_idx_smoothaccel_63d_sm252_3d_v090_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of scale_mcap_idx smoothed over 504d
def f081cim_f081_company_identity_metadata_scale_mcap_idx_smoothaccel_252d_sm504_3d_v091_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_accelz_21d_z252_3d_v092_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_accelz_63d_z504_3d_v093_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_accelz_21d_z252_3d_v094_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_accelz_63d_z504_3d_v095_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_accelz_21d_z252_3d_v096_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_accelz_63d_z504_3d_v097_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_accelz_21d_z252_3d_v098_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_accelz_63d_z504_3d_v099_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_accelz_21d_z252_3d_v100_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_accelz_63d_z504_3d_v101_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_accelz_21d_z252_3d_v102_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_accelz_63d_z504_3d_v103_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_accelz_21d_z252_3d_v104_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_accelz_63d_z504_3d_v105_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ipo_age_d (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_d_signflip_63d_3d_v106_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ipo_age_d (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_d_signflip_252d_3d_v107_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ipo_age_log (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_log_signflip_63d_3d_v108_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ipo_age_log (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_log_signflip_252d_3d_v109_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ipo_age_above_5y (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_signflip_63d_3d_v110_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ipo_age_above_5y (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_signflip_252d_3d_v111_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ipo_age_under_2y (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_signflip_63d_3d_v112_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ipo_age_under_2y (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_signflip_252d_3d_v113_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in on_nasdaq (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_on_nasdaq_signflip_63d_3d_v114_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in on_nasdaq (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_on_nasdaq_signflip_252d_3d_v115_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in on_nyse (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_on_nyse_signflip_63d_3d_v116_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in on_nyse (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_on_nyse_signflip_252d_3d_v117_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in scale_mcap_idx (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_scale_mcap_idx_signflip_63d_3d_v118_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in scale_mcap_idx (raw count, no price scaling)
def f081cim_f081_company_identity_metadata_scale_mcap_idx_signflip_252d_3d_v119_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_d normalized by 252d range
def f081cim_f081_company_identity_metadata_ipo_age_d_rngaccel_63d_r252_3d_v120_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_d normalized by 504d range
def f081cim_f081_company_identity_metadata_ipo_age_d_rngaccel_252d_r504_3d_v121_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_log normalized by 252d range
def f081cim_f081_company_identity_metadata_ipo_age_log_rngaccel_63d_r252_3d_v122_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_log normalized by 504d range
def f081cim_f081_company_identity_metadata_ipo_age_log_rngaccel_252d_r504_3d_v123_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_above_5y normalized by 252d range
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_rngaccel_63d_r252_3d_v124_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_above_5y normalized by 504d range
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_rngaccel_252d_r504_3d_v125_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ipo_age_under_2y normalized by 252d range
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_rngaccel_63d_r252_3d_v126_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ipo_age_under_2y normalized by 504d range
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_rngaccel_252d_r504_3d_v127_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of on_nasdaq normalized by 252d range
def f081cim_f081_company_identity_metadata_on_nasdaq_rngaccel_63d_r252_3d_v128_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of on_nasdaq normalized by 504d range
def f081cim_f081_company_identity_metadata_on_nasdaq_rngaccel_252d_r504_3d_v129_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of on_nyse normalized by 252d range
def f081cim_f081_company_identity_metadata_on_nyse_rngaccel_63d_r252_3d_v130_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of on_nyse normalized by 504d range
def f081cim_f081_company_identity_metadata_on_nyse_rngaccel_252d_r504_3d_v131_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of scale_mcap_idx normalized by 252d range
def f081cim_f081_company_identity_metadata_scale_mcap_idx_rngaccel_63d_r252_3d_v132_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of scale_mcap_idx normalized by 504d range
def f081cim_f081_company_identity_metadata_scale_mcap_idx_rngaccel_252d_r504_3d_v133_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_cumslope_21d_3d_v134_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_cumslope_63d_3d_v135_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_cumslope_252d_3d_v136_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_cumslope_21d_3d_v137_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_cumslope_63d_3d_v138_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_cumslope_252d_3d_v139_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_cumslope_21d_3d_v140_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_cumslope_63d_3d_v141_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_cumslope_252d_3d_v142_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_cumslope_21d_3d_v143_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_cumslope_63d_3d_v144_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_cumslope_252d_3d_v145_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_cumslope_21d_3d_v146_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_cumslope_63d_3d_v147_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_cumslope_252d_3d_v148_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_cumslope_21d_3d_v149_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_cumslope_63d_3d_v150_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

