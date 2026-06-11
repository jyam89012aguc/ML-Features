"""Family f084 - Identifier continuity (Security Master and Universe) | Sharadar tables: TICKERS | fields: ticker, permaticker, relatedtickers, table, currency | 3rd derivatives 001-150"""
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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _ticker_changes_and_permaticker_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ticker_changes_and_permaticker_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ticker_changes_and_permaticker_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_21d_accel_v001_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_21d_accel_v002_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_21d_accel_v003_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_63d_accel_v004_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_63d_accel_v005_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_63d_accel_v006_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_126d_accel_v007_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_126d_accel_v008_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_126d_accel_v009_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_252d_accel_v010_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_252d_accel_v011_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_252d_accel_v012_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_504d_accel_v013_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_504d_accel_v014_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_raw_504d_accel_v015_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_21d_accel_v016_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_21d_accel_v017_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_21d_accel_v018_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_63d_accel_v019_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_63d_accel_v020_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_63d_accel_v021_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_126d_accel_v022_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_126d_accel_v023_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_126d_accel_v024_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_252d_accel_v025_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_252d_accel_v026_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_252d_accel_v027_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_504d_accel_v028_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_504d_accel_v029_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_log_504d_accel_v030_signal(ticker_change_count, closeadj):
    base = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_21d_accel_v031_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_21d_accel_v032_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_21d_accel_v033_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_63d_accel_v034_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_63d_accel_v035_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_63d_accel_v036_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_126d_accel_v037_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_126d_accel_v038_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_126d_accel_v039_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_252d_accel_v040_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_252d_accel_v041_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_252d_accel_v042_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_504d_accel_v043_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_504d_accel_v044_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_pershare_504d_accel_v045_signal(ticker_change_count, sharesbas, closeadj):
    base = _mean(_ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_21d_accel_v046_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_21d_accel_v047_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_21d_accel_v048_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_63d_accel_v049_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_63d_accel_v050_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_63d_accel_v051_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_126d_accel_v052_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_126d_accel_v053_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_126d_accel_v054_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_252d_accel_v055_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_252d_accel_v056_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_252d_accel_v057_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_504d_accel_v058_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_504d_accel_v059_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_assets_504d_accel_v060_signal(ticker_change_count, assets):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_21d_accel_v061_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_21d_accel_v062_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_21d_accel_v063_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_63d_accel_v064_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_63d_accel_v065_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_63d_accel_v066_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_126d_accel_v067_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_126d_accel_v068_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_126d_accel_v069_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_252d_accel_v070_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_252d_accel_v071_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_252d_accel_v072_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_504d_accel_v073_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_504d_accel_v074_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_504d_accel_v075_signal(ticker_change_count, marketcap):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_21d_accel_v076_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_21d_accel_v077_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_21d_accel_v078_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_63d_accel_v079_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_63d_accel_v080_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_63d_accel_v081_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_126d_accel_v082_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_126d_accel_v083_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_126d_accel_v084_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_252d_accel_v085_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_252d_accel_v086_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_252d_accel_v087_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_504d_accel_v088_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_504d_accel_v089_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_per_equity_504d_accel_v090_signal(ticker_change_count, equity):
    base = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_21d_accel_v091_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_21d_accel_v092_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_21d_accel_v093_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_63d_accel_v094_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_63d_accel_v095_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_63d_accel_v096_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_126d_accel_v097_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_126d_accel_v098_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_126d_accel_v099_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_252d_accel_v100_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_252d_accel_v101_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_252d_accel_v102_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_504d_accel_v103_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_504d_accel_v104_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_std_504d_accel_v105_signal(ticker_change_count, closeadj):
    base = _std(ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_21d_accel_v106_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_21d_accel_v107_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_21d_accel_v108_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_63d_accel_v109_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_63d_accel_v110_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_63d_accel_v111_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_126d_accel_v112_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_126d_accel_v113_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_126d_accel_v114_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_252d_accel_v115_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_252d_accel_v116_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_252d_accel_v117_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_504d_accel_v118_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_504d_accel_v119_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_ewm_504d_accel_v120_signal(ticker_change_count, closeadj):
    base = ticker_change_count.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_21d_accel_v121_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_21d_accel_v122_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_21d_accel_v123_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_63d_accel_v124_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_63d_accel_v125_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_63d_accel_v126_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_126d_accel_v127_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_126d_accel_v128_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_126d_accel_v129_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_252d_accel_v130_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_252d_accel_v131_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_252d_accel_v132_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_504d_accel_v133_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_504d_accel_v134_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_sq_504d_accel_v135_signal(ticker_change_count, closeadj):
    base = _mean(ticker_change_count * ticker_change_count, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_21d_accel_v136_signal(ticker_change_count):
    base = _z(ticker_change_count, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_21d_accel_v137_signal(ticker_change_count):
    base = _z(ticker_change_count, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_21d_accel_v138_signal(ticker_change_count):
    base = _z(ticker_change_count, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_63d_accel_v139_signal(ticker_change_count):
    base = _z(ticker_change_count, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_63d_accel_v140_signal(ticker_change_count):
    base = _z(ticker_change_count, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_63d_accel_v141_signal(ticker_change_count):
    base = _z(ticker_change_count, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_126d_accel_v142_signal(ticker_change_count):
    base = _z(ticker_change_count, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_126d_accel_v143_signal(ticker_change_count):
    base = _z(ticker_change_count, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_126d_accel_v144_signal(ticker_change_count):
    base = _z(ticker_change_count, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_252d_accel_v145_signal(ticker_change_count):
    base = _z(ticker_change_count, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_252d_accel_v146_signal(ticker_change_count):
    base = _z(ticker_change_count, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_252d_accel_v147_signal(ticker_change_count):
    base = _z(ticker_change_count, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_504d_accel_v148_signal(ticker_change_count):
    base = _z(ticker_change_count, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_504d_accel_v149_signal(ticker_change_count):
    base = _z(ticker_change_count, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_504d_accel_v150_signal(ticker_change_count):
    base = _z(ticker_change_count, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
