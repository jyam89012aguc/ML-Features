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


# 63d z-score of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_z_63d_base_v076_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_z_126d_base_v077_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_z_252d_base_v078_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_z_504d_base_v079_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of age_log
def f079rrc_f079_reporting_recency_age_log_z_63d_base_v080_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of age_log
def f079rrc_f079_reporting_recency_age_log_z_126d_base_v081_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of age_log
def f079rrc_f079_reporting_recency_age_log_z_252d_base_v082_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of age_log
def f079rrc_f079_reporting_recency_age_log_z_504d_base_v083_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_z_63d_base_v084_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_z_126d_base_v085_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_z_252d_base_v086_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_z_504d_base_v087_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_z_63d_base_v088_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_z_126d_base_v089_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_z_252d_base_v090_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_z_504d_base_v091_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of age_change
def f079rrc_f079_reporting_recency_age_change_z_63d_base_v092_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of age_change
def f079rrc_f079_reporting_recency_age_change_z_126d_base_v093_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of age_change
def f079rrc_f079_reporting_recency_age_change_z_252d_base_v094_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of age_change
def f079rrc_f079_reporting_recency_age_change_z_504d_base_v095_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_z_63d_base_v096_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_z_126d_base_v097_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_z_252d_base_v098_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_z_504d_base_v099_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_z_63d_base_v100_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_z_126d_base_v101_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_z_252d_base_v102_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_z_504d_base_v103_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_distmax_252d_base_v104_signal(stale_age_days, closeadj):
    base = stale_age_days
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_distmax_504d_base_v105_signal(stale_age_days, closeadj):
    base = stale_age_days
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of age_log
def f079rrc_f079_reporting_recency_age_log_distmax_252d_base_v106_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of age_log
def f079rrc_f079_reporting_recency_age_log_distmax_504d_base_v107_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_distmax_252d_base_v108_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_distmax_504d_base_v109_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_distmax_252d_base_v110_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_distmax_504d_base_v111_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of age_change
def f079rrc_f079_reporting_recency_age_change_distmax_252d_base_v112_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of age_change
def f079rrc_f079_reporting_recency_age_change_distmax_504d_base_v113_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_distmax_252d_base_v114_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_distmax_504d_base_v115_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_distmax_252d_base_v116_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_distmax_504d_base_v117_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_distmed_126d_base_v118_signal(stale_age_days, closeadj):
    base = stale_age_days
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_distmed_252d_base_v119_signal(stale_age_days, closeadj):
    base = stale_age_days
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_distmed_504d_base_v120_signal(stale_age_days, closeadj):
    base = stale_age_days
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of age_log
def f079rrc_f079_reporting_recency_age_log_distmed_126d_base_v121_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of age_log
def f079rrc_f079_reporting_recency_age_log_distmed_252d_base_v122_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of age_log
def f079rrc_f079_reporting_recency_age_log_distmed_504d_base_v123_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_distmed_126d_base_v124_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_distmed_252d_base_v125_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of age_above90d
def f079rrc_f079_reporting_recency_age_above90d_distmed_504d_base_v126_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_distmed_126d_base_v127_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_distmed_252d_base_v128_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of age_above180d
def f079rrc_f079_reporting_recency_age_above180d_distmed_504d_base_v129_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of age_change
def f079rrc_f079_reporting_recency_age_change_distmed_126d_base_v130_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of age_change
def f079rrc_f079_reporting_recency_age_change_distmed_252d_base_v131_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of age_change
def f079rrc_f079_reporting_recency_age_change_distmed_504d_base_v132_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_distmed_126d_base_v133_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_distmed_252d_base_v134_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_distmed_504d_base_v135_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_distmed_126d_base_v136_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_distmed_252d_base_v137_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of avg_age_252
def f079rrc_f079_reporting_recency_avg_age_252_distmed_504d_base_v138_signal(stale_age_days, closeadj):
    base = stale_age_days.rolling(252, min_periods=63).mean()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_chg_63d_base_v139_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in filing_age_d
def f079rrc_f079_reporting_recency_filing_age_d_chg_252d_base_v140_signal(stale_age_days, closeadj):
    base = stale_age_days
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in age_log
def f079rrc_f079_reporting_recency_age_log_chg_63d_base_v141_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in age_log
def f079rrc_f079_reporting_recency_age_log_chg_252d_base_v142_signal(stale_age_days, closeadj):
    base = np.log(stale_age_days.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in age_above90d
def f079rrc_f079_reporting_recency_age_above90d_chg_63d_base_v143_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in age_above90d
def f079rrc_f079_reporting_recency_age_above90d_chg_252d_base_v144_signal(stale_age_days, closeadj):
    base = (stale_age_days > 90).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in age_above180d
def f079rrc_f079_reporting_recency_age_above180d_chg_63d_base_v145_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in age_above180d
def f079rrc_f079_reporting_recency_age_above180d_chg_252d_base_v146_signal(stale_age_days, closeadj):
    base = (stale_age_days > 180).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in age_change
def f079rrc_f079_reporting_recency_age_change_chg_63d_base_v147_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in age_change
def f079rrc_f079_reporting_recency_age_change_chg_252d_base_v148_signal(stale_age_days, closeadj):
    base = stale_age_days.diff()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_chg_63d_base_v149_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in age_to_qend
def f079rrc_f079_reporting_recency_age_to_qend_chg_252d_base_v150_signal(stale_age_days, closeadj):
    base = stale_age_days % 90
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

