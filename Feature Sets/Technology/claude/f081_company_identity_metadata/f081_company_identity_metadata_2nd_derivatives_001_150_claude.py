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


# 21d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slope_21d_2d_v001_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slope_63d_2d_v002_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slope_126d_2d_v003_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slope_252d_2d_v004_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_slope_504d_2d_v005_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slope_21d_2d_v006_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slope_63d_2d_v007_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slope_126d_2d_v008_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slope_252d_2d_v009_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_slope_504d_2d_v010_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slope_21d_2d_v011_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slope_63d_2d_v012_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slope_126d_2d_v013_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slope_252d_2d_v014_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_slope_504d_2d_v015_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slope_21d_2d_v016_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slope_63d_2d_v017_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slope_126d_2d_v018_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slope_252d_2d_v019_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_slope_504d_2d_v020_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slope_21d_2d_v021_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slope_63d_2d_v022_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slope_126d_2d_v023_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slope_252d_2d_v024_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_slope_504d_2d_v025_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slope_21d_2d_v026_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slope_63d_2d_v027_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slope_126d_2d_v028_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slope_252d_2d_v029_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_slope_504d_2d_v030_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slope_21d_2d_v031_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slope_63d_2d_v032_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slope_126d_2d_v033_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slope_252d_2d_v034_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_slope_504d_2d_v035_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sm21_sl21_2d_v036_signal(ipo_age_days, closeadj):
    base = _mean(ipo_age_days, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sm63_sl21_2d_v037_signal(ipo_age_days, closeadj):
    base = _mean(ipo_age_days, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sm63_sl63_2d_v038_signal(ipo_age_days, closeadj):
    base = _mean(ipo_age_days, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sm252_sl63_2d_v039_signal(ipo_age_days, closeadj):
    base = _mean(ipo_age_days, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sm252_sl126_2d_v040_signal(ipo_age_days, closeadj):
    base = _mean(ipo_age_days, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sm21_sl21_2d_v041_signal(ipo_age_days, closeadj):
    base = _mean(np.log(ipo_age_days.abs().replace(0, np.nan) + 1), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sm63_sl21_2d_v042_signal(ipo_age_days, closeadj):
    base = _mean(np.log(ipo_age_days.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sm63_sl63_2d_v043_signal(ipo_age_days, closeadj):
    base = _mean(np.log(ipo_age_days.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sm252_sl63_2d_v044_signal(ipo_age_days, closeadj):
    base = _mean(np.log(ipo_age_days.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sm252_sl126_2d_v045_signal(ipo_age_days, closeadj):
    base = _mean(np.log(ipo_age_days.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sm21_sl21_2d_v046_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days > 1825).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sm63_sl21_2d_v047_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days > 1825).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sm63_sl63_2d_v048_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days > 1825).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sm252_sl63_2d_v049_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days > 1825).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sm252_sl126_2d_v050_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days > 1825).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sm21_sl21_2d_v051_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days < 730).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sm63_sl21_2d_v052_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days < 730).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sm63_sl63_2d_v053_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days < 730).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sm252_sl63_2d_v054_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days < 730).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sm252_sl126_2d_v055_signal(ipo_age_days, closeadj):
    base = _mean((ipo_age_days < 730).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sm21_sl21_2d_v056_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 1).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sm63_sl21_2d_v057_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 1).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sm63_sl63_2d_v058_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 1).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sm252_sl63_2d_v059_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 1).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sm252_sl126_2d_v060_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 1).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sm21_sl21_2d_v061_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 2).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sm63_sl21_2d_v062_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 2).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sm63_sl63_2d_v063_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 2).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sm252_sl63_2d_v064_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 2).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sm252_sl126_2d_v065_signal(exchange_code, closeadj):
    base = _mean((exchange_code == 2).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sm21_sl21_2d_v066_signal(scale_mcap_index, closeadj):
    base = _mean(scale_mcap_index, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sm63_sl21_2d_v067_signal(scale_mcap_index, closeadj):
    base = _mean(scale_mcap_index, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sm63_sl63_2d_v068_signal(scale_mcap_index, closeadj):
    base = _mean(scale_mcap_index, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sm252_sl63_2d_v069_signal(scale_mcap_index, closeadj):
    base = _mean(scale_mcap_index, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sm252_sl126_2d_v070_signal(scale_mcap_index, closeadj):
    base = _mean(scale_mcap_index, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_pctslope_21d_2d_v071_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_pctslope_63d_2d_v072_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_pctslope_252d_2d_v073_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_pctslope_21d_2d_v074_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_pctslope_63d_2d_v075_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_pctslope_252d_2d_v076_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_pctslope_21d_2d_v077_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_pctslope_63d_2d_v078_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_pctslope_252d_2d_v079_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_pctslope_21d_2d_v080_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_pctslope_63d_2d_v081_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_pctslope_252d_2d_v082_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_pctslope_21d_2d_v083_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_pctslope_63d_2d_v084_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_pctslope_252d_2d_v085_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_pctslope_21d_2d_v086_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_pctslope_63d_2d_v087_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_pctslope_252d_2d_v088_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_pctslope_21d_2d_v089_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_pctslope_63d_2d_v090_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_pctslope_252d_2d_v091_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sgnslope_21d_2d_v092_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sgnslope_63d_2d_v093_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_sgnslope_252d_2d_v094_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sgnslope_21d_2d_v095_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sgnslope_63d_2d_v096_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_sgnslope_252d_2d_v097_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sgnslope_21d_2d_v098_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sgnslope_63d_2d_v099_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_sgnslope_252d_2d_v100_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sgnslope_21d_2d_v101_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sgnslope_63d_2d_v102_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_sgnslope_252d_2d_v103_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sgnslope_21d_2d_v104_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sgnslope_63d_2d_v105_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_sgnslope_252d_2d_v106_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sgnslope_21d_2d_v107_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sgnslope_63d_2d_v108_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_sgnslope_252d_2d_v109_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sgnslope_21d_2d_v110_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sgnslope_63d_2d_v111_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_sgnslope_252d_2d_v112_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_logmagslope_21d_2d_v113_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_logmagslope_63d_2d_v114_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_logmagslope_252d_2d_v115_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_logmagslope_21d_2d_v116_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_logmagslope_63d_2d_v117_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_logmagslope_252d_2d_v118_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_logmagslope_21d_2d_v119_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_logmagslope_63d_2d_v120_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_logmagslope_252d_2d_v121_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_logmagslope_21d_2d_v122_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_logmagslope_63d_2d_v123_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_logmagslope_252d_2d_v124_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_logmagslope_21d_2d_v125_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_logmagslope_63d_2d_v126_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_logmagslope_252d_2d_v127_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_logmagslope_21d_2d_v128_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_logmagslope_63d_2d_v129_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_logmagslope_252d_2d_v130_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_logmagslope_21d_2d_v131_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_logmagslope_63d_2d_v132_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_logmagslope_252d_2d_v133_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ipo_age_d|
def f081cim_f081_company_identity_metadata_ipo_age_d_logslope_63d_2d_v134_signal(ipo_age_days, closeadj):
    base = np.log((ipo_age_days).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ipo_age_d|
def f081cim_f081_company_identity_metadata_ipo_age_d_logslope_252d_2d_v135_signal(ipo_age_days, closeadj):
    base = np.log((ipo_age_days).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ipo_age_log|
def f081cim_f081_company_identity_metadata_ipo_age_log_logslope_63d_2d_v136_signal(ipo_age_days, closeadj):
    base = np.log((np.log(ipo_age_days.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ipo_age_log|
def f081cim_f081_company_identity_metadata_ipo_age_log_logslope_252d_2d_v137_signal(ipo_age_days, closeadj):
    base = np.log((np.log(ipo_age_days.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ipo_age_above_5y|
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_logslope_63d_2d_v138_signal(ipo_age_days, closeadj):
    base = np.log(((ipo_age_days > 1825).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ipo_age_above_5y|
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_logslope_252d_2d_v139_signal(ipo_age_days, closeadj):
    base = np.log(((ipo_age_days > 1825).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ipo_age_under_2y|
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_logslope_63d_2d_v140_signal(ipo_age_days, closeadj):
    base = np.log(((ipo_age_days < 730).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ipo_age_under_2y|
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_logslope_252d_2d_v141_signal(ipo_age_days, closeadj):
    base = np.log(((ipo_age_days < 730).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|on_nasdaq|
def f081cim_f081_company_identity_metadata_on_nasdaq_logslope_63d_2d_v142_signal(exchange_code, closeadj):
    base = np.log(((exchange_code == 1).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|on_nasdaq|
def f081cim_f081_company_identity_metadata_on_nasdaq_logslope_252d_2d_v143_signal(exchange_code, closeadj):
    base = np.log(((exchange_code == 1).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|on_nyse|
def f081cim_f081_company_identity_metadata_on_nyse_logslope_63d_2d_v144_signal(exchange_code, closeadj):
    base = np.log(((exchange_code == 2).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|on_nyse|
def f081cim_f081_company_identity_metadata_on_nyse_logslope_252d_2d_v145_signal(exchange_code, closeadj):
    base = np.log(((exchange_code == 2).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|scale_mcap_idx|
def f081cim_f081_company_identity_metadata_scale_mcap_idx_logslope_63d_2d_v146_signal(scale_mcap_index, closeadj):
    base = np.log((scale_mcap_index).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|scale_mcap_idx|
def f081cim_f081_company_identity_metadata_scale_mcap_idx_logslope_252d_2d_v147_signal(scale_mcap_index, closeadj):
    base = np.log((scale_mcap_index).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

