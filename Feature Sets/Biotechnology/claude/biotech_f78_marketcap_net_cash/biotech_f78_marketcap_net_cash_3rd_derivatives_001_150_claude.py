"""Family f78 - Market cap / net cash  (M_Valuation) | 3rd derivatives 001-150"""
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
def _marketcap_net_cash_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _marketcap_net_cash_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _marketcap_net_cash_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw marketcap
def mnc_f78_marketcap_net_cash_raw_21d_accel_v001_signal(marketcap, closeadj):
    base = _mean(marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw marketcap
def mnc_f78_marketcap_net_cash_raw_21d_accel_v002_signal(marketcap, closeadj):
    base = _mean(marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw marketcap
def mnc_f78_marketcap_net_cash_raw_21d_accel_v003_signal(marketcap, closeadj):
    base = _mean(marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw marketcap
def mnc_f78_marketcap_net_cash_raw_63d_accel_v004_signal(marketcap, closeadj):
    base = _mean(marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw marketcap
def mnc_f78_marketcap_net_cash_raw_63d_accel_v005_signal(marketcap, closeadj):
    base = _mean(marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw marketcap
def mnc_f78_marketcap_net_cash_raw_63d_accel_v006_signal(marketcap, closeadj):
    base = _mean(marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw marketcap
def mnc_f78_marketcap_net_cash_raw_126d_accel_v007_signal(marketcap, closeadj):
    base = _mean(marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw marketcap
def mnc_f78_marketcap_net_cash_raw_126d_accel_v008_signal(marketcap, closeadj):
    base = _mean(marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw marketcap
def mnc_f78_marketcap_net_cash_raw_126d_accel_v009_signal(marketcap, closeadj):
    base = _mean(marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw marketcap
def mnc_f78_marketcap_net_cash_raw_252d_accel_v010_signal(marketcap, closeadj):
    base = _mean(marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw marketcap
def mnc_f78_marketcap_net_cash_raw_252d_accel_v011_signal(marketcap, closeadj):
    base = _mean(marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw marketcap
def mnc_f78_marketcap_net_cash_raw_252d_accel_v012_signal(marketcap, closeadj):
    base = _mean(marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw marketcap
def mnc_f78_marketcap_net_cash_raw_504d_accel_v013_signal(marketcap, closeadj):
    base = _mean(marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw marketcap
def mnc_f78_marketcap_net_cash_raw_504d_accel_v014_signal(marketcap, closeadj):
    base = _mean(marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw marketcap
def mnc_f78_marketcap_net_cash_raw_504d_accel_v015_signal(marketcap, closeadj):
    base = _mean(marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log marketcap
def mnc_f78_marketcap_net_cash_log_21d_accel_v016_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log marketcap
def mnc_f78_marketcap_net_cash_log_21d_accel_v017_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log marketcap
def mnc_f78_marketcap_net_cash_log_21d_accel_v018_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log marketcap
def mnc_f78_marketcap_net_cash_log_63d_accel_v019_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log marketcap
def mnc_f78_marketcap_net_cash_log_63d_accel_v020_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log marketcap
def mnc_f78_marketcap_net_cash_log_63d_accel_v021_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log marketcap
def mnc_f78_marketcap_net_cash_log_126d_accel_v022_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log marketcap
def mnc_f78_marketcap_net_cash_log_126d_accel_v023_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log marketcap
def mnc_f78_marketcap_net_cash_log_126d_accel_v024_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log marketcap
def mnc_f78_marketcap_net_cash_log_252d_accel_v025_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log marketcap
def mnc_f78_marketcap_net_cash_log_252d_accel_v026_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log marketcap
def mnc_f78_marketcap_net_cash_log_252d_accel_v027_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log marketcap
def mnc_f78_marketcap_net_cash_log_504d_accel_v028_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log marketcap
def mnc_f78_marketcap_net_cash_log_504d_accel_v029_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log marketcap
def mnc_f78_marketcap_net_cash_log_504d_accel_v030_signal(marketcap, closeadj):
    base = _mean(_marketcap_net_cash_log(marketcap), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_21d_accel_v031_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_21d_accel_v032_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_21d_accel_v033_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_63d_accel_v034_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_63d_accel_v035_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_63d_accel_v036_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_126d_accel_v037_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_126d_accel_v038_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_126d_accel_v039_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_252d_accel_v040_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_252d_accel_v041_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_252d_accel_v042_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_504d_accel_v043_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_504d_accel_v044_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare marketcap
def mnc_f78_marketcap_net_cash_pershare_504d_accel_v045_signal(marketcap, sharesbas, closeadj):
    base = _mean(_marketcap_net_cash_per_share(marketcap, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_21d_accel_v046_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_21d_accel_v047_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_21d_accel_v048_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_63d_accel_v049_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_63d_accel_v050_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_63d_accel_v051_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_126d_accel_v052_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_126d_accel_v053_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_126d_accel_v054_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_252d_accel_v055_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_252d_accel_v056_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_252d_accel_v057_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_504d_accel_v058_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_504d_accel_v059_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets marketcap
def mnc_f78_marketcap_net_cash_per_assets_504d_accel_v060_signal(marketcap, assets):
    base = _mean(_marketcap_net_cash_scaled(marketcap, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_21d_accel_v061_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_21d_accel_v062_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_21d_accel_v063_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_63d_accel_v064_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_63d_accel_v065_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_63d_accel_v066_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_126d_accel_v067_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_126d_accel_v068_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_126d_accel_v069_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_252d_accel_v070_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_252d_accel_v071_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_252d_accel_v072_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_504d_accel_v073_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_504d_accel_v074_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap marketcap
def mnc_f78_marketcap_net_cash_per_marketcap_504d_accel_v075_signal(marketcap):
    base = _mean(_marketcap_net_cash_scaled(marketcap, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_21d_accel_v076_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_21d_accel_v077_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_21d_accel_v078_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_63d_accel_v079_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_63d_accel_v080_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_63d_accel_v081_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_126d_accel_v082_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_126d_accel_v083_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_126d_accel_v084_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_252d_accel_v085_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_252d_accel_v086_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_252d_accel_v087_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_504d_accel_v088_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_504d_accel_v089_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity marketcap
def mnc_f78_marketcap_net_cash_per_equity_504d_accel_v090_signal(marketcap, equity):
    base = _mean(_marketcap_net_cash_scaled(marketcap, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std marketcap
def mnc_f78_marketcap_net_cash_std_21d_accel_v091_signal(marketcap, closeadj):
    base = _std(marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std marketcap
def mnc_f78_marketcap_net_cash_std_21d_accel_v092_signal(marketcap, closeadj):
    base = _std(marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std marketcap
def mnc_f78_marketcap_net_cash_std_21d_accel_v093_signal(marketcap, closeadj):
    base = _std(marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std marketcap
def mnc_f78_marketcap_net_cash_std_63d_accel_v094_signal(marketcap, closeadj):
    base = _std(marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std marketcap
def mnc_f78_marketcap_net_cash_std_63d_accel_v095_signal(marketcap, closeadj):
    base = _std(marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std marketcap
def mnc_f78_marketcap_net_cash_std_63d_accel_v096_signal(marketcap, closeadj):
    base = _std(marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std marketcap
def mnc_f78_marketcap_net_cash_std_126d_accel_v097_signal(marketcap, closeadj):
    base = _std(marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std marketcap
def mnc_f78_marketcap_net_cash_std_126d_accel_v098_signal(marketcap, closeadj):
    base = _std(marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std marketcap
def mnc_f78_marketcap_net_cash_std_126d_accel_v099_signal(marketcap, closeadj):
    base = _std(marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std marketcap
def mnc_f78_marketcap_net_cash_std_252d_accel_v100_signal(marketcap, closeadj):
    base = _std(marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std marketcap
def mnc_f78_marketcap_net_cash_std_252d_accel_v101_signal(marketcap, closeadj):
    base = _std(marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std marketcap
def mnc_f78_marketcap_net_cash_std_252d_accel_v102_signal(marketcap, closeadj):
    base = _std(marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std marketcap
def mnc_f78_marketcap_net_cash_std_504d_accel_v103_signal(marketcap, closeadj):
    base = _std(marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std marketcap
def mnc_f78_marketcap_net_cash_std_504d_accel_v104_signal(marketcap, closeadj):
    base = _std(marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std marketcap
def mnc_f78_marketcap_net_cash_std_504d_accel_v105_signal(marketcap, closeadj):
    base = _std(marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_21d_accel_v106_signal(marketcap, closeadj):
    base = marketcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_21d_accel_v107_signal(marketcap, closeadj):
    base = marketcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_21d_accel_v108_signal(marketcap, closeadj):
    base = marketcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_63d_accel_v109_signal(marketcap, closeadj):
    base = marketcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_63d_accel_v110_signal(marketcap, closeadj):
    base = marketcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_63d_accel_v111_signal(marketcap, closeadj):
    base = marketcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_126d_accel_v112_signal(marketcap, closeadj):
    base = marketcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_126d_accel_v113_signal(marketcap, closeadj):
    base = marketcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_126d_accel_v114_signal(marketcap, closeadj):
    base = marketcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_252d_accel_v115_signal(marketcap, closeadj):
    base = marketcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_252d_accel_v116_signal(marketcap, closeadj):
    base = marketcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_252d_accel_v117_signal(marketcap, closeadj):
    base = marketcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_504d_accel_v118_signal(marketcap, closeadj):
    base = marketcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_504d_accel_v119_signal(marketcap, closeadj):
    base = marketcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm marketcap
def mnc_f78_marketcap_net_cash_ewm_504d_accel_v120_signal(marketcap, closeadj):
    base = marketcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq marketcap
def mnc_f78_marketcap_net_cash_sq_21d_accel_v121_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq marketcap
def mnc_f78_marketcap_net_cash_sq_21d_accel_v122_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq marketcap
def mnc_f78_marketcap_net_cash_sq_21d_accel_v123_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq marketcap
def mnc_f78_marketcap_net_cash_sq_63d_accel_v124_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq marketcap
def mnc_f78_marketcap_net_cash_sq_63d_accel_v125_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq marketcap
def mnc_f78_marketcap_net_cash_sq_63d_accel_v126_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq marketcap
def mnc_f78_marketcap_net_cash_sq_126d_accel_v127_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq marketcap
def mnc_f78_marketcap_net_cash_sq_126d_accel_v128_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq marketcap
def mnc_f78_marketcap_net_cash_sq_126d_accel_v129_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq marketcap
def mnc_f78_marketcap_net_cash_sq_252d_accel_v130_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq marketcap
def mnc_f78_marketcap_net_cash_sq_252d_accel_v131_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq marketcap
def mnc_f78_marketcap_net_cash_sq_252d_accel_v132_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq marketcap
def mnc_f78_marketcap_net_cash_sq_504d_accel_v133_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq marketcap
def mnc_f78_marketcap_net_cash_sq_504d_accel_v134_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq marketcap
def mnc_f78_marketcap_net_cash_sq_504d_accel_v135_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z marketcap
def mnc_f78_marketcap_net_cash_z_21d_accel_v136_signal(marketcap):
    base = _z(marketcap, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z marketcap
def mnc_f78_marketcap_net_cash_z_21d_accel_v137_signal(marketcap):
    base = _z(marketcap, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z marketcap
def mnc_f78_marketcap_net_cash_z_21d_accel_v138_signal(marketcap):
    base = _z(marketcap, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z marketcap
def mnc_f78_marketcap_net_cash_z_63d_accel_v139_signal(marketcap):
    base = _z(marketcap, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z marketcap
def mnc_f78_marketcap_net_cash_z_63d_accel_v140_signal(marketcap):
    base = _z(marketcap, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z marketcap
def mnc_f78_marketcap_net_cash_z_63d_accel_v141_signal(marketcap):
    base = _z(marketcap, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z marketcap
def mnc_f78_marketcap_net_cash_z_126d_accel_v142_signal(marketcap):
    base = _z(marketcap, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z marketcap
def mnc_f78_marketcap_net_cash_z_126d_accel_v143_signal(marketcap):
    base = _z(marketcap, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z marketcap
def mnc_f78_marketcap_net_cash_z_126d_accel_v144_signal(marketcap):
    base = _z(marketcap, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z marketcap
def mnc_f78_marketcap_net_cash_z_252d_accel_v145_signal(marketcap):
    base = _z(marketcap, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z marketcap
def mnc_f78_marketcap_net_cash_z_252d_accel_v146_signal(marketcap):
    base = _z(marketcap, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z marketcap
def mnc_f78_marketcap_net_cash_z_252d_accel_v147_signal(marketcap):
    base = _z(marketcap, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z marketcap
def mnc_f78_marketcap_net_cash_z_504d_accel_v148_signal(marketcap):
    base = _z(marketcap, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z marketcap
def mnc_f78_marketcap_net_cash_z_504d_accel_v149_signal(marketcap):
    base = _z(marketcap, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z marketcap
def mnc_f78_marketcap_net_cash_z_504d_accel_v150_signal(marketcap):
    base = _z(marketcap, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
