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


# 21d mean of ticker_change_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_mean_21d_base_v001_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ticker_change_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_mean_63d_base_v002_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ticker_change_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_mean_126d_base_v003_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ticker_change_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_mean_252d_base_v004_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ticker_change_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_mean_504d_base_v005_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of related_ticker_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_mean_21d_base_v006_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of related_ticker_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_mean_63d_base_v007_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of related_ticker_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_mean_126d_base_v008_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of related_ticker_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_mean_252d_base_v009_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of related_ticker_cnt scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_mean_504d_base_v010_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nonusd_flag scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_mean_21d_base_v011_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nonusd_flag scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_mean_63d_base_v012_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nonusd_flag scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_mean_126d_base_v013_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nonusd_flag scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_mean_252d_base_v014_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nonusd_flag scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_mean_504d_base_v015_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of change_rate_504d scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_mean_21d_base_v016_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of change_rate_504d scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_mean_63d_base_v017_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of change_rate_504d scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_mean_126d_base_v018_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of change_rate_504d scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_mean_252d_base_v019_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of change_rate_504d scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_mean_504d_base_v020_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of related_log scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_log_mean_21d_base_v021_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of related_log scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_log_mean_63d_base_v022_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of related_log scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_log_mean_126d_base_v023_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of related_log scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_log_mean_252d_base_v024_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of related_log scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_related_log_mean_504d_base_v025_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of permaticker_age scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_mean_21d_base_v026_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of permaticker_age scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_mean_63d_base_v027_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of permaticker_age scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_mean_126d_base_v028_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of permaticker_age scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_mean_252d_base_v029_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of permaticker_age scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_mean_504d_base_v030_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of change_recent_252 scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_mean_21d_base_v031_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of change_recent_252 scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_mean_63d_base_v032_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of change_recent_252 scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_mean_126d_base_v033_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of change_recent_252 scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_mean_252d_base_v034_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of change_recent_252 scaled by closeadj
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_mean_504d_base_v035_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_median_63d_base_v036_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_median_252d_base_v037_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_median_504d_base_v038_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_median_63d_base_v039_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_median_252d_base_v040_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_median_504d_base_v041_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_median_63d_base_v042_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_median_252d_base_v043_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_median_504d_base_v044_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_median_63d_base_v045_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_median_252d_base_v046_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_median_504d_base_v047_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_median_63d_base_v048_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_median_252d_base_v049_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_median_504d_base_v050_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_median_63d_base_v051_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_median_252d_base_v052_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_median_504d_base_v053_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_median_63d_base_v054_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_median_252d_base_v055_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_median_504d_base_v056_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_rmax_252d_base_v057_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_rmax_504d_base_v058_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_rmax_252d_base_v059_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_rmax_504d_base_v060_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_rmax_252d_base_v061_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_rmax_504d_base_v062_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_rmax_252d_base_v063_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_rmax_504d_base_v064_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_rmax_252d_base_v065_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_rmax_504d_base_v066_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_rmax_252d_base_v067_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_rmax_504d_base_v068_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_rmax_252d_base_v069_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_rmax_504d_base_v070_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_rmin_252d_base_v071_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_rmin_504d_base_v072_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_rmin_252d_base_v073_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_rmin_504d_base_v074_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_rmin_252d_base_v075_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

