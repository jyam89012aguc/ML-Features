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
def _f081_age(ipo_age_days):
    return ipo_age_days


# 21d mean of ipo_age_d scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_d_mean_21d_base_v001_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ipo_age_d scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_d_mean_63d_base_v002_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ipo_age_d scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_d_mean_126d_base_v003_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ipo_age_d scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_d_mean_252d_base_v004_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ipo_age_d scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_d_mean_504d_base_v005_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ipo_age_log scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_log_mean_21d_base_v006_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ipo_age_log scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_log_mean_63d_base_v007_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ipo_age_log scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_log_mean_126d_base_v008_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ipo_age_log scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_log_mean_252d_base_v009_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ipo_age_log scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_log_mean_504d_base_v010_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ipo_age_above_5y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_mean_21d_base_v011_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ipo_age_above_5y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_mean_63d_base_v012_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ipo_age_above_5y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_mean_126d_base_v013_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ipo_age_above_5y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_mean_252d_base_v014_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ipo_age_above_5y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_mean_504d_base_v015_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ipo_age_under_2y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_mean_21d_base_v016_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ipo_age_under_2y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_mean_63d_base_v017_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ipo_age_under_2y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_mean_126d_base_v018_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ipo_age_under_2y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_mean_252d_base_v019_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ipo_age_under_2y scaled by closeadj
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_mean_504d_base_v020_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of on_nasdaq scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nasdaq_mean_21d_base_v021_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of on_nasdaq scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nasdaq_mean_63d_base_v022_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of on_nasdaq scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nasdaq_mean_126d_base_v023_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of on_nasdaq scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nasdaq_mean_252d_base_v024_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of on_nasdaq scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nasdaq_mean_504d_base_v025_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of on_nyse scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nyse_mean_21d_base_v026_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of on_nyse scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nyse_mean_63d_base_v027_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of on_nyse scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nyse_mean_126d_base_v028_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of on_nyse scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nyse_mean_252d_base_v029_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of on_nyse scaled by closeadj
def f081cim_f081_company_identity_metadata_on_nyse_mean_504d_base_v030_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of scale_mcap_idx scaled by closeadj
def f081cim_f081_company_identity_metadata_scale_mcap_idx_mean_21d_base_v031_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of scale_mcap_idx scaled by closeadj
def f081cim_f081_company_identity_metadata_scale_mcap_idx_mean_63d_base_v032_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of scale_mcap_idx scaled by closeadj
def f081cim_f081_company_identity_metadata_scale_mcap_idx_mean_126d_base_v033_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of scale_mcap_idx scaled by closeadj
def f081cim_f081_company_identity_metadata_scale_mcap_idx_mean_252d_base_v034_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of scale_mcap_idx scaled by closeadj
def f081cim_f081_company_identity_metadata_scale_mcap_idx_mean_504d_base_v035_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_median_63d_base_v036_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_median_252d_base_v037_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_median_504d_base_v038_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_median_63d_base_v039_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_median_252d_base_v040_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_median_504d_base_v041_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_median_63d_base_v042_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_median_252d_base_v043_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_median_504d_base_v044_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_median_63d_base_v045_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_median_252d_base_v046_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_median_504d_base_v047_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_median_63d_base_v048_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_median_252d_base_v049_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_median_504d_base_v050_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_median_63d_base_v051_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_median_252d_base_v052_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_median_504d_base_v053_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_median_63d_base_v054_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_median_252d_base_v055_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_median_504d_base_v056_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_rmax_252d_base_v057_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_rmax_504d_base_v058_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_rmax_252d_base_v059_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_rmax_504d_base_v060_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_rmax_252d_base_v061_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_rmax_504d_base_v062_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_rmax_252d_base_v063_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_rmax_504d_base_v064_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_rmax_252d_base_v065_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_rmax_504d_base_v066_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_rmax_252d_base_v067_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_rmax_504d_base_v068_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_rmax_252d_base_v069_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_rmax_504d_base_v070_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_rmin_252d_base_v071_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_rmin_504d_base_v072_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_rmin_252d_base_v073_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_rmin_504d_base_v074_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_rmin_252d_base_v075_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

