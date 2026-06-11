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
def _f079_age(stale_age_days):
    return stale_age_days


# 21d mean of filing_age_d scaled by closeadj
def f079rrc_f079_reporting_recency_filing_age_d_mean_21d_base_v001_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of filing_age_d scaled by closeadj
def f079rrc_f079_reporting_recency_filing_age_d_mean_63d_base_v002_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of filing_age_d scaled by closeadj
def f079rrc_f079_reporting_recency_filing_age_d_mean_126d_base_v003_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of filing_age_d scaled by closeadj
def f079rrc_f079_reporting_recency_filing_age_d_mean_252d_base_v004_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of filing_age_d scaled by closeadj
def f079rrc_f079_reporting_recency_filing_age_d_mean_504d_base_v005_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of age_log scaled by closeadj
def f079rrc_f079_reporting_recency_age_log_mean_21d_base_v006_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of age_log scaled by closeadj
def f079rrc_f079_reporting_recency_age_log_mean_63d_base_v007_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of age_log scaled by closeadj
def f079rrc_f079_reporting_recency_age_log_mean_126d_base_v008_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of age_log scaled by closeadj
def f079rrc_f079_reporting_recency_age_log_mean_252d_base_v009_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of age_log scaled by closeadj
def f079rrc_f079_reporting_recency_age_log_mean_504d_base_v010_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of age_above90d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above90d_mean_21d_base_v011_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of age_above90d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above90d_mean_63d_base_v012_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of age_above90d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above90d_mean_126d_base_v013_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of age_above90d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above90d_mean_252d_base_v014_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of age_above90d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above90d_mean_504d_base_v015_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of age_above180d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above180d_mean_21d_base_v016_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of age_above180d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above180d_mean_63d_base_v017_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of age_above180d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above180d_mean_126d_base_v018_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of age_above180d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above180d_mean_252d_base_v019_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of age_above180d scaled by closeadj
def f079rrc_f079_reporting_recency_age_above180d_mean_504d_base_v020_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of age_change scaled by closeadj
def f079rrc_f079_reporting_recency_age_change_mean_21d_base_v021_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of age_change scaled by closeadj
def f079rrc_f079_reporting_recency_age_change_mean_63d_base_v022_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of age_change scaled by closeadj
def f079rrc_f079_reporting_recency_age_change_mean_126d_base_v023_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of age_change scaled by closeadj
def f079rrc_f079_reporting_recency_age_change_mean_252d_base_v024_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of age_change scaled by closeadj
def f079rrc_f079_reporting_recency_age_change_mean_504d_base_v025_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of age_to_qend scaled by closeadj
def f079rrc_f079_reporting_recency_age_to_qend_mean_21d_base_v026_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of age_to_qend scaled by closeadj
def f079rrc_f079_reporting_recency_age_to_qend_mean_63d_base_v027_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of age_to_qend scaled by closeadj
def f079rrc_f079_reporting_recency_age_to_qend_mean_126d_base_v028_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of age_to_qend scaled by closeadj
def f079rrc_f079_reporting_recency_age_to_qend_mean_252d_base_v029_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of age_to_qend scaled by closeadj
def f079rrc_f079_reporting_recency_age_to_qend_mean_504d_base_v030_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of avg_age_252 scaled by closeadj
def f079rrc_f079_reporting_recency_avg_age_252_mean_21d_base_v031_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of avg_age_252 scaled by closeadj
def f079rrc_f079_reporting_recency_avg_age_252_mean_63d_base_v032_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of avg_age_252 scaled by closeadj
def f079rrc_f079_reporting_recency_avg_age_252_mean_126d_base_v033_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of avg_age_252 scaled by closeadj
def f079rrc_f079_reporting_recency_avg_age_252_mean_252d_base_v034_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of avg_age_252 scaled by closeadj
def f079rrc_f079_reporting_recency_avg_age_252_mean_504d_base_v035_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_median_63d_base_v036_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_median_252d_base_v037_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_median_504d_base_v038_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of age_log
def f079rrc_f079_reporting_recency_age_log_median_63d_base_v039_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of age_log
def f079rrc_f079_reporting_recency_age_log_median_252d_base_v040_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of age_log
def f079rrc_f079_reporting_recency_age_log_median_504d_base_v041_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_median_63d_base_v042_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_median_252d_base_v043_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_median_504d_base_v044_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_median_63d_base_v045_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_median_252d_base_v046_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_median_504d_base_v047_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of age_change
def f079rrc_f079_reporting_recency_age_change_median_63d_base_v048_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of age_change
def f079rrc_f079_reporting_recency_age_change_median_252d_base_v049_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of age_change
def f079rrc_f079_reporting_recency_age_change_median_504d_base_v050_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_median_63d_base_v051_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_median_252d_base_v052_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_median_504d_base_v053_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_median_63d_base_v054_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_median_252d_base_v055_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_median_504d_base_v056_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_rmax_252d_base_v057_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_rmax_504d_base_v058_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of age_log
def f079rrc_f079_reporting_recency_age_log_rmax_252d_base_v059_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of age_log
def f079rrc_f079_reporting_recency_age_log_rmax_504d_base_v060_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_rmax_252d_base_v061_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_rmax_504d_base_v062_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_rmax_252d_base_v063_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_rmax_504d_base_v064_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of age_change
def f079rrc_f079_reporting_recency_age_change_rmax_252d_base_v065_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of age_change
def f079rrc_f079_reporting_recency_age_change_rmax_504d_base_v066_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_rmax_252d_base_v067_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_rmax_504d_base_v068_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_rmax_252d_base_v069_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_rmax_504d_base_v070_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_rmin_252d_base_v071_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_rmin_504d_base_v072_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of age_log
def f079rrc_f079_reporting_recency_age_log_rmin_252d_base_v073_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of age_log
def f079rrc_f079_reporting_recency_age_log_rmin_504d_base_v074_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_rmin_252d_base_v075_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

