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
def _f084_chg(ticker_change_count):
    return ticker_change_count


# 63d z-score of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_z_63d_base_v076_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_z_126d_base_v077_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_z_252d_base_v078_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_z_504d_base_v079_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_z_63d_base_v080_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_z_126d_base_v081_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_z_252d_base_v082_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_z_504d_base_v083_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_z_63d_base_v084_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_z_126d_base_v085_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_z_252d_base_v086_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_z_504d_base_v087_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_z_63d_base_v088_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_z_126d_base_v089_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_z_252d_base_v090_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_z_504d_base_v091_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_z_63d_base_v092_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_z_126d_base_v093_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_z_252d_base_v094_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_z_504d_base_v095_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_z_63d_base_v096_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_z_126d_base_v097_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_z_252d_base_v098_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_z_504d_base_v099_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_z_63d_base_v100_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_z_126d_base_v101_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_z_252d_base_v102_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_z_504d_base_v103_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_distmax_252d_base_v104_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_distmax_504d_base_v105_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_distmax_252d_base_v106_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_distmax_504d_base_v107_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_distmax_252d_base_v108_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_distmax_504d_base_v109_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_distmax_252d_base_v110_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_distmax_504d_base_v111_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_distmax_252d_base_v112_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_distmax_504d_base_v113_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_distmax_252d_base_v114_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_distmax_504d_base_v115_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_distmax_252d_base_v116_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_distmax_504d_base_v117_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_distmed_126d_base_v118_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_distmed_252d_base_v119_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_distmed_504d_base_v120_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_distmed_126d_base_v121_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_distmed_252d_base_v122_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_distmed_504d_base_v123_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_distmed_126d_base_v124_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_distmed_252d_base_v125_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_distmed_504d_base_v126_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_distmed_126d_base_v127_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_distmed_252d_base_v128_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_distmed_504d_base_v129_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_distmed_126d_base_v130_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_distmed_252d_base_v131_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_distmed_504d_base_v132_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_distmed_126d_base_v133_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_distmed_252d_base_v134_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_distmed_504d_base_v135_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_distmed_126d_base_v136_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_distmed_252d_base_v137_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_distmed_504d_base_v138_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_chg_63d_base_v139_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_chg_252d_base_v140_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_chg_63d_base_v141_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_chg_252d_base_v142_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_chg_63d_base_v143_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_chg_252d_base_v144_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_chg_63d_base_v145_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_chg_252d_base_v146_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_chg_63d_base_v147_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_chg_252d_base_v148_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_chg_63d_base_v149_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_chg_252d_base_v150_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

