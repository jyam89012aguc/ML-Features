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


# 63d z-score of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_z_63d_base_v076_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_z_126d_base_v077_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_z_252d_base_v078_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_z_504d_base_v079_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_z_63d_base_v080_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_z_126d_base_v081_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_z_252d_base_v082_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_z_504d_base_v083_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_z_63d_base_v084_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_z_126d_base_v085_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_z_252d_base_v086_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_z_504d_base_v087_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_z_63d_base_v088_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_z_126d_base_v089_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_z_252d_base_v090_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_z_504d_base_v091_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_z_63d_base_v092_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_z_126d_base_v093_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_z_252d_base_v094_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_z_504d_base_v095_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_z_63d_base_v096_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_z_126d_base_v097_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_z_252d_base_v098_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_z_504d_base_v099_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_z_63d_base_v100_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_z_126d_base_v101_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_z_252d_base_v102_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_z_504d_base_v103_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_distmax_252d_base_v104_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_distmax_504d_base_v105_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_distmax_252d_base_v106_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_distmax_504d_base_v107_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_distmax_252d_base_v108_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_distmax_504d_base_v109_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_distmax_252d_base_v110_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_distmax_504d_base_v111_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_distmax_252d_base_v112_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_distmax_504d_base_v113_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_distmax_252d_base_v114_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_distmax_504d_base_v115_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_distmax_252d_base_v116_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_distmax_504d_base_v117_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_distmed_126d_base_v118_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_distmed_252d_base_v119_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_distmed_504d_base_v120_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_distmed_126d_base_v121_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_distmed_252d_base_v122_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_distmed_504d_base_v123_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_distmed_126d_base_v124_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_distmed_252d_base_v125_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_distmed_504d_base_v126_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_distmed_126d_base_v127_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_distmed_252d_base_v128_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_distmed_504d_base_v129_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_distmed_126d_base_v130_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_distmed_252d_base_v131_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_distmed_504d_base_v132_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_distmed_126d_base_v133_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_distmed_252d_base_v134_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_distmed_504d_base_v135_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_distmed_126d_base_v136_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_distmed_252d_base_v137_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of scale_mcap_idx
def f081cim_f081_company_identity_metadata_scale_mcap_idx_distmed_504d_base_v138_signal(scale_mcap_index, closeadj):
    base = scale_mcap_index
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_chg_63d_base_v139_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ipo_age_d
def f081cim_f081_company_identity_metadata_ipo_age_d_chg_252d_base_v140_signal(ipo_age_days, closeadj):
    base = ipo_age_days
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_chg_63d_base_v141_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ipo_age_log
def f081cim_f081_company_identity_metadata_ipo_age_log_chg_252d_base_v142_signal(ipo_age_days, closeadj):
    base = np.log(ipo_age_days.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_chg_63d_base_v143_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ipo_age_above_5y
def f081cim_f081_company_identity_metadata_ipo_age_above_5y_chg_252d_base_v144_signal(ipo_age_days, closeadj):
    base = (ipo_age_days > 1825).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_chg_63d_base_v145_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ipo_age_under_2y
def f081cim_f081_company_identity_metadata_ipo_age_under_2y_chg_252d_base_v146_signal(ipo_age_days, closeadj):
    base = (ipo_age_days < 730).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_chg_63d_base_v147_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in on_nasdaq
def f081cim_f081_company_identity_metadata_on_nasdaq_chg_252d_base_v148_signal(exchange_code, closeadj):
    base = (exchange_code == 1).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_chg_63d_base_v149_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in on_nyse
def f081cim_f081_company_identity_metadata_on_nyse_chg_252d_base_v150_signal(exchange_code, closeadj):
    base = (exchange_code == 2).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

