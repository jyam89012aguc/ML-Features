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
def _f084_chg(ticker_change_count):
    return ticker_change_count


# 21d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slope_21d_2d_v001_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slope_63d_2d_v002_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slope_126d_2d_v003_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slope_252d_2d_v004_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slope_504d_2d_v005_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slope_21d_2d_v006_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slope_63d_2d_v007_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slope_126d_2d_v008_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slope_252d_2d_v009_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slope_504d_2d_v010_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slope_21d_2d_v011_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slope_63d_2d_v012_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slope_126d_2d_v013_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slope_252d_2d_v014_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slope_504d_2d_v015_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slope_21d_2d_v016_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slope_63d_2d_v017_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slope_126d_2d_v018_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slope_252d_2d_v019_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slope_504d_2d_v020_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slope_21d_2d_v021_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slope_63d_2d_v022_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slope_126d_2d_v023_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slope_252d_2d_v024_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slope_504d_2d_v025_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slope_21d_2d_v026_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slope_63d_2d_v027_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slope_126d_2d_v028_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slope_252d_2d_v029_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slope_504d_2d_v030_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slope_21d_2d_v031_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slope_63d_2d_v032_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slope_126d_2d_v033_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slope_252d_2d_v034_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slope_504d_2d_v035_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sm21_sl21_2d_v036_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sm63_sl21_2d_v037_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sm63_sl63_2d_v038_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sm252_sl63_2d_v039_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sm252_sl126_2d_v040_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sm21_sl21_2d_v041_signal(related_ticker_count, closeadj):
    base = _mean(related_ticker_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sm63_sl21_2d_v042_signal(related_ticker_count, closeadj):
    base = _mean(related_ticker_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sm63_sl63_2d_v043_signal(related_ticker_count, closeadj):
    base = _mean(related_ticker_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sm252_sl63_2d_v044_signal(related_ticker_count, closeadj):
    base = _mean(related_ticker_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sm252_sl126_2d_v045_signal(related_ticker_count, closeadj):
    base = _mean(related_ticker_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sm21_sl21_2d_v046_signal(currency_code, closeadj):
    base = _mean((currency_code != 'USD').astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sm63_sl21_2d_v047_signal(currency_code, closeadj):
    base = _mean((currency_code != 'USD').astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sm63_sl63_2d_v048_signal(currency_code, closeadj):
    base = _mean((currency_code != 'USD').astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sm252_sl63_2d_v049_signal(currency_code, closeadj):
    base = _mean((currency_code != 'USD').astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sm252_sl126_2d_v050_signal(currency_code, closeadj):
    base = _mean((currency_code != 'USD').astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sm21_sl21_2d_v051_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=504), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sm63_sl21_2d_v052_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=504), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sm63_sl63_2d_v053_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=504), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sm252_sl63_2d_v054_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=504), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sm252_sl126_2d_v055_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=504), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sm21_sl21_2d_v056_signal(related_ticker_count, closeadj):
    base = _mean(np.log(related_ticker_count.abs().replace(0, np.nan) + 1), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sm63_sl21_2d_v057_signal(related_ticker_count, closeadj):
    base = _mean(np.log(related_ticker_count.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sm63_sl63_2d_v058_signal(related_ticker_count, closeadj):
    base = _mean(np.log(related_ticker_count.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sm252_sl63_2d_v059_signal(related_ticker_count, closeadj):
    base = _mean(np.log(related_ticker_count.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sm252_sl126_2d_v060_signal(related_ticker_count, closeadj):
    base = _mean(np.log(related_ticker_count.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sm21_sl21_2d_v061_signal(permaticker_age_days, closeadj):
    base = _mean(permaticker_age_days, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sm63_sl21_2d_v062_signal(permaticker_age_days, closeadj):
    base = _mean(permaticker_age_days, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sm63_sl63_2d_v063_signal(permaticker_age_days, closeadj):
    base = _mean(permaticker_age_days, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sm252_sl63_2d_v064_signal(permaticker_age_days, closeadj):
    base = _mean(permaticker_age_days, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sm252_sl126_2d_v065_signal(permaticker_age_days, closeadj):
    base = _mean(permaticker_age_days, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sm21_sl21_2d_v066_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sm63_sl21_2d_v067_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sm63_sl63_2d_v068_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sm252_sl63_2d_v069_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sm252_sl126_2d_v070_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_pctslope_21d_2d_v071_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_pctslope_63d_2d_v072_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_pctslope_252d_2d_v073_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_pctslope_21d_2d_v074_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_pctslope_63d_2d_v075_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_pctslope_252d_2d_v076_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_pctslope_21d_2d_v077_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_pctslope_63d_2d_v078_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_pctslope_252d_2d_v079_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_pctslope_21d_2d_v080_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_pctslope_63d_2d_v081_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_pctslope_252d_2d_v082_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_pctslope_21d_2d_v083_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_pctslope_63d_2d_v084_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_pctslope_252d_2d_v085_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_pctslope_21d_2d_v086_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_pctslope_63d_2d_v087_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_pctslope_252d_2d_v088_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_pctslope_21d_2d_v089_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_pctslope_63d_2d_v090_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_pctslope_252d_2d_v091_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sgnslope_21d_2d_v092_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sgnslope_63d_2d_v093_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_sgnslope_252d_2d_v094_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sgnslope_21d_2d_v095_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sgnslope_63d_2d_v096_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_sgnslope_252d_2d_v097_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sgnslope_21d_2d_v098_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sgnslope_63d_2d_v099_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_sgnslope_252d_2d_v100_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sgnslope_21d_2d_v101_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sgnslope_63d_2d_v102_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_sgnslope_252d_2d_v103_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sgnslope_21d_2d_v104_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sgnslope_63d_2d_v105_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_sgnslope_252d_2d_v106_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sgnslope_21d_2d_v107_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sgnslope_63d_2d_v108_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_sgnslope_252d_2d_v109_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sgnslope_21d_2d_v110_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sgnslope_63d_2d_v111_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_sgnslope_252d_2d_v112_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_logmagslope_21d_2d_v113_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_logmagslope_63d_2d_v114_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_logmagslope_252d_2d_v115_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_logmagslope_21d_2d_v116_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_logmagslope_63d_2d_v117_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_logmagslope_252d_2d_v118_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_logmagslope_21d_2d_v119_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_logmagslope_63d_2d_v120_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_logmagslope_252d_2d_v121_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_logmagslope_21d_2d_v122_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_logmagslope_63d_2d_v123_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_logmagslope_252d_2d_v124_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_logmagslope_21d_2d_v125_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_logmagslope_63d_2d_v126_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_logmagslope_252d_2d_v127_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_logmagslope_21d_2d_v128_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_logmagslope_63d_2d_v129_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_logmagslope_252d_2d_v130_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_logmagslope_21d_2d_v131_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_logmagslope_63d_2d_v132_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_logmagslope_252d_2d_v133_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ticker_change_cnt|
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_logslope_63d_2d_v134_signal(ticker_change_count, closeadj):
    base = np.log((ticker_change_count).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ticker_change_cnt|
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_logslope_252d_2d_v135_signal(ticker_change_count, closeadj):
    base = np.log((ticker_change_count).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|related_ticker_cnt|
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_logslope_63d_2d_v136_signal(related_ticker_count, closeadj):
    base = np.log((related_ticker_count).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|related_ticker_cnt|
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_logslope_252d_2d_v137_signal(related_ticker_count, closeadj):
    base = np.log((related_ticker_count).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|nonusd_flag|
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_logslope_63d_2d_v138_signal(currency_code, closeadj):
    base = np.log(((currency_code != 'USD').astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|nonusd_flag|
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_logslope_252d_2d_v139_signal(currency_code, closeadj):
    base = np.log(((currency_code != 'USD').astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|change_rate_504d|
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_logslope_63d_2d_v140_signal(ticker_change_count, closeadj):
    base = np.log((ticker_change_count.diff(periods=504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|change_rate_504d|
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_logslope_252d_2d_v141_signal(ticker_change_count, closeadj):
    base = np.log((ticker_change_count.diff(periods=504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|related_log|
def f084tcp_f084_ticker_changes_and_permaticker_related_log_logslope_63d_2d_v142_signal(related_ticker_count, closeadj):
    base = np.log((np.log(related_ticker_count.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|related_log|
def f084tcp_f084_ticker_changes_and_permaticker_related_log_logslope_252d_2d_v143_signal(related_ticker_count, closeadj):
    base = np.log((np.log(related_ticker_count.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|permaticker_age|
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_logslope_63d_2d_v144_signal(permaticker_age_days, closeadj):
    base = np.log((permaticker_age_days).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|permaticker_age|
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_logslope_252d_2d_v145_signal(permaticker_age_days, closeadj):
    base = np.log((permaticker_age_days).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|change_recent_252|
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_logslope_63d_2d_v146_signal(ticker_change_count, closeadj):
    base = np.log((ticker_change_count.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|change_recent_252|
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_logslope_252d_2d_v147_signal(ticker_change_count, closeadj):
    base = np.log((ticker_change_count.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

