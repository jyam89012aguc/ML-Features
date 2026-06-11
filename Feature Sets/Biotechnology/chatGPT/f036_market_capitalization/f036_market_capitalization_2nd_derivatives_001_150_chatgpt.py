"""Family f036 - Market capitalization scale (Dilution and Share Count) | Sharadar tables: DAILY,SF1 | fields: marketcap, sharesbas, close | 2nd derivatives 001-150"""
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
def _market_capitalization_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _market_capitalization_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _market_capitalization_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw marketcap
def mc_f036_market_capitalization_raw_21d_slope_v001_signal(marketcap, closeadj):
    base = _mean(marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw marketcap
def mc_f036_market_capitalization_raw_21d_slope_v002_signal(marketcap, closeadj):
    base = _mean(marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw marketcap
def mc_f036_market_capitalization_raw_21d_slope_v003_signal(marketcap, closeadj):
    base = _mean(marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw marketcap
def mc_f036_market_capitalization_raw_63d_slope_v004_signal(marketcap, closeadj):
    base = _mean(marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw marketcap
def mc_f036_market_capitalization_raw_63d_slope_v005_signal(marketcap, closeadj):
    base = _mean(marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw marketcap
def mc_f036_market_capitalization_raw_63d_slope_v006_signal(marketcap, closeadj):
    base = _mean(marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw marketcap
def mc_f036_market_capitalization_raw_126d_slope_v007_signal(marketcap, closeadj):
    base = _mean(marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw marketcap
def mc_f036_market_capitalization_raw_126d_slope_v008_signal(marketcap, closeadj):
    base = _mean(marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw marketcap
def mc_f036_market_capitalization_raw_126d_slope_v009_signal(marketcap, closeadj):
    base = _mean(marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw marketcap
def mc_f036_market_capitalization_raw_252d_slope_v010_signal(marketcap, closeadj):
    base = _mean(marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw marketcap
def mc_f036_market_capitalization_raw_252d_slope_v011_signal(marketcap, closeadj):
    base = _mean(marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw marketcap
def mc_f036_market_capitalization_raw_252d_slope_v012_signal(marketcap, closeadj):
    base = _mean(marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw marketcap
def mc_f036_market_capitalization_raw_504d_slope_v013_signal(marketcap, closeadj):
    base = _mean(marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw marketcap
def mc_f036_market_capitalization_raw_504d_slope_v014_signal(marketcap, closeadj):
    base = _mean(marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw marketcap
def mc_f036_market_capitalization_raw_504d_slope_v015_signal(marketcap, closeadj):
    base = _mean(marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log marketcap
def mc_f036_market_capitalization_log_21d_slope_v016_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log marketcap
def mc_f036_market_capitalization_log_21d_slope_v017_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log marketcap
def mc_f036_market_capitalization_log_21d_slope_v018_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log marketcap
def mc_f036_market_capitalization_log_63d_slope_v019_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log marketcap
def mc_f036_market_capitalization_log_63d_slope_v020_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log marketcap
def mc_f036_market_capitalization_log_63d_slope_v021_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log marketcap
def mc_f036_market_capitalization_log_126d_slope_v022_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log marketcap
def mc_f036_market_capitalization_log_126d_slope_v023_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log marketcap
def mc_f036_market_capitalization_log_126d_slope_v024_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log marketcap
def mc_f036_market_capitalization_log_252d_slope_v025_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log marketcap
def mc_f036_market_capitalization_log_252d_slope_v026_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log marketcap
def mc_f036_market_capitalization_log_252d_slope_v027_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log marketcap
def mc_f036_market_capitalization_log_504d_slope_v028_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log marketcap
def mc_f036_market_capitalization_log_504d_slope_v029_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log marketcap
def mc_f036_market_capitalization_log_504d_slope_v030_signal(marketcap, closeadj):
    base = _mean(_market_capitalization_log(marketcap), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare marketcap
def mc_f036_market_capitalization_pershare_21d_slope_v031_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare marketcap
def mc_f036_market_capitalization_pershare_21d_slope_v032_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare marketcap
def mc_f036_market_capitalization_pershare_21d_slope_v033_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare marketcap
def mc_f036_market_capitalization_pershare_63d_slope_v034_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare marketcap
def mc_f036_market_capitalization_pershare_63d_slope_v035_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare marketcap
def mc_f036_market_capitalization_pershare_63d_slope_v036_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare marketcap
def mc_f036_market_capitalization_pershare_126d_slope_v037_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare marketcap
def mc_f036_market_capitalization_pershare_126d_slope_v038_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare marketcap
def mc_f036_market_capitalization_pershare_126d_slope_v039_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare marketcap
def mc_f036_market_capitalization_pershare_252d_slope_v040_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare marketcap
def mc_f036_market_capitalization_pershare_252d_slope_v041_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare marketcap
def mc_f036_market_capitalization_pershare_252d_slope_v042_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare marketcap
def mc_f036_market_capitalization_pershare_504d_slope_v043_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare marketcap
def mc_f036_market_capitalization_pershare_504d_slope_v044_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare marketcap
def mc_f036_market_capitalization_pershare_504d_slope_v045_signal(marketcap, sharesbas, closeadj):
    base = _mean(_market_capitalization_per_share(marketcap, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_21d_slope_v046_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_21d_slope_v047_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_21d_slope_v048_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_63d_slope_v049_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_63d_slope_v050_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_63d_slope_v051_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_126d_slope_v052_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_126d_slope_v053_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_126d_slope_v054_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_252d_slope_v055_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_252d_slope_v056_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_252d_slope_v057_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_504d_slope_v058_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_504d_slope_v059_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sharesbas marketcap
def mc_f036_market_capitalization_per_sharesbas_504d_slope_v060_signal(marketcap, sharesbas):
    base = _mean(_market_capitalization_scaled(marketcap, sharesbas), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_close marketcap
def mc_f036_market_capitalization_per_close_21d_slope_v061_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_close marketcap
def mc_f036_market_capitalization_per_close_21d_slope_v062_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_close marketcap
def mc_f036_market_capitalization_per_close_21d_slope_v063_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_close marketcap
def mc_f036_market_capitalization_per_close_63d_slope_v064_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_close marketcap
def mc_f036_market_capitalization_per_close_63d_slope_v065_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_close marketcap
def mc_f036_market_capitalization_per_close_63d_slope_v066_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_close marketcap
def mc_f036_market_capitalization_per_close_126d_slope_v067_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_close marketcap
def mc_f036_market_capitalization_per_close_126d_slope_v068_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_close marketcap
def mc_f036_market_capitalization_per_close_126d_slope_v069_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_close marketcap
def mc_f036_market_capitalization_per_close_252d_slope_v070_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_close marketcap
def mc_f036_market_capitalization_per_close_252d_slope_v071_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_close marketcap
def mc_f036_market_capitalization_per_close_252d_slope_v072_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_close marketcap
def mc_f036_market_capitalization_per_close_504d_slope_v073_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_close marketcap
def mc_f036_market_capitalization_per_close_504d_slope_v074_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_close marketcap
def mc_f036_market_capitalization_per_close_504d_slope_v075_signal(marketcap, close):
    base = _mean(_market_capitalization_scaled(marketcap, close), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets marketcap
def mc_f036_market_capitalization_per_assets_21d_slope_v076_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets marketcap
def mc_f036_market_capitalization_per_assets_21d_slope_v077_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets marketcap
def mc_f036_market_capitalization_per_assets_21d_slope_v078_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets marketcap
def mc_f036_market_capitalization_per_assets_63d_slope_v079_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets marketcap
def mc_f036_market_capitalization_per_assets_63d_slope_v080_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets marketcap
def mc_f036_market_capitalization_per_assets_63d_slope_v081_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets marketcap
def mc_f036_market_capitalization_per_assets_126d_slope_v082_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets marketcap
def mc_f036_market_capitalization_per_assets_126d_slope_v083_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets marketcap
def mc_f036_market_capitalization_per_assets_126d_slope_v084_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets marketcap
def mc_f036_market_capitalization_per_assets_252d_slope_v085_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets marketcap
def mc_f036_market_capitalization_per_assets_252d_slope_v086_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets marketcap
def mc_f036_market_capitalization_per_assets_252d_slope_v087_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets marketcap
def mc_f036_market_capitalization_per_assets_504d_slope_v088_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets marketcap
def mc_f036_market_capitalization_per_assets_504d_slope_v089_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets marketcap
def mc_f036_market_capitalization_per_assets_504d_slope_v090_signal(marketcap, assets):
    base = _mean(_market_capitalization_scaled(marketcap, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std marketcap
def mc_f036_market_capitalization_std_21d_slope_v091_signal(marketcap, closeadj):
    base = _std(marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std marketcap
def mc_f036_market_capitalization_std_21d_slope_v092_signal(marketcap, closeadj):
    base = _std(marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std marketcap
def mc_f036_market_capitalization_std_21d_slope_v093_signal(marketcap, closeadj):
    base = _std(marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std marketcap
def mc_f036_market_capitalization_std_63d_slope_v094_signal(marketcap, closeadj):
    base = _std(marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std marketcap
def mc_f036_market_capitalization_std_63d_slope_v095_signal(marketcap, closeadj):
    base = _std(marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std marketcap
def mc_f036_market_capitalization_std_63d_slope_v096_signal(marketcap, closeadj):
    base = _std(marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std marketcap
def mc_f036_market_capitalization_std_126d_slope_v097_signal(marketcap, closeadj):
    base = _std(marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std marketcap
def mc_f036_market_capitalization_std_126d_slope_v098_signal(marketcap, closeadj):
    base = _std(marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std marketcap
def mc_f036_market_capitalization_std_126d_slope_v099_signal(marketcap, closeadj):
    base = _std(marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std marketcap
def mc_f036_market_capitalization_std_252d_slope_v100_signal(marketcap, closeadj):
    base = _std(marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std marketcap
def mc_f036_market_capitalization_std_252d_slope_v101_signal(marketcap, closeadj):
    base = _std(marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std marketcap
def mc_f036_market_capitalization_std_252d_slope_v102_signal(marketcap, closeadj):
    base = _std(marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std marketcap
def mc_f036_market_capitalization_std_504d_slope_v103_signal(marketcap, closeadj):
    base = _std(marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std marketcap
def mc_f036_market_capitalization_std_504d_slope_v104_signal(marketcap, closeadj):
    base = _std(marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std marketcap
def mc_f036_market_capitalization_std_504d_slope_v105_signal(marketcap, closeadj):
    base = _std(marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm marketcap
def mc_f036_market_capitalization_ewm_21d_slope_v106_signal(marketcap, closeadj):
    base = marketcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm marketcap
def mc_f036_market_capitalization_ewm_21d_slope_v107_signal(marketcap, closeadj):
    base = marketcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm marketcap
def mc_f036_market_capitalization_ewm_21d_slope_v108_signal(marketcap, closeadj):
    base = marketcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm marketcap
def mc_f036_market_capitalization_ewm_63d_slope_v109_signal(marketcap, closeadj):
    base = marketcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm marketcap
def mc_f036_market_capitalization_ewm_63d_slope_v110_signal(marketcap, closeadj):
    base = marketcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm marketcap
def mc_f036_market_capitalization_ewm_63d_slope_v111_signal(marketcap, closeadj):
    base = marketcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm marketcap
def mc_f036_market_capitalization_ewm_126d_slope_v112_signal(marketcap, closeadj):
    base = marketcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm marketcap
def mc_f036_market_capitalization_ewm_126d_slope_v113_signal(marketcap, closeadj):
    base = marketcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm marketcap
def mc_f036_market_capitalization_ewm_126d_slope_v114_signal(marketcap, closeadj):
    base = marketcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm marketcap
def mc_f036_market_capitalization_ewm_252d_slope_v115_signal(marketcap, closeadj):
    base = marketcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm marketcap
def mc_f036_market_capitalization_ewm_252d_slope_v116_signal(marketcap, closeadj):
    base = marketcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm marketcap
def mc_f036_market_capitalization_ewm_252d_slope_v117_signal(marketcap, closeadj):
    base = marketcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm marketcap
def mc_f036_market_capitalization_ewm_504d_slope_v118_signal(marketcap, closeadj):
    base = marketcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm marketcap
def mc_f036_market_capitalization_ewm_504d_slope_v119_signal(marketcap, closeadj):
    base = marketcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm marketcap
def mc_f036_market_capitalization_ewm_504d_slope_v120_signal(marketcap, closeadj):
    base = marketcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq marketcap
def mc_f036_market_capitalization_sq_21d_slope_v121_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq marketcap
def mc_f036_market_capitalization_sq_21d_slope_v122_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq marketcap
def mc_f036_market_capitalization_sq_21d_slope_v123_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq marketcap
def mc_f036_market_capitalization_sq_63d_slope_v124_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq marketcap
def mc_f036_market_capitalization_sq_63d_slope_v125_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq marketcap
def mc_f036_market_capitalization_sq_63d_slope_v126_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq marketcap
def mc_f036_market_capitalization_sq_126d_slope_v127_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq marketcap
def mc_f036_market_capitalization_sq_126d_slope_v128_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq marketcap
def mc_f036_market_capitalization_sq_126d_slope_v129_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq marketcap
def mc_f036_market_capitalization_sq_252d_slope_v130_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq marketcap
def mc_f036_market_capitalization_sq_252d_slope_v131_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq marketcap
def mc_f036_market_capitalization_sq_252d_slope_v132_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq marketcap
def mc_f036_market_capitalization_sq_504d_slope_v133_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq marketcap
def mc_f036_market_capitalization_sq_504d_slope_v134_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq marketcap
def mc_f036_market_capitalization_sq_504d_slope_v135_signal(marketcap, closeadj):
    base = _mean(marketcap * marketcap, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z marketcap
def mc_f036_market_capitalization_z_21d_slope_v136_signal(marketcap):
    base = _z(marketcap, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z marketcap
def mc_f036_market_capitalization_z_21d_slope_v137_signal(marketcap):
    base = _z(marketcap, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z marketcap
def mc_f036_market_capitalization_z_21d_slope_v138_signal(marketcap):
    base = _z(marketcap, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z marketcap
def mc_f036_market_capitalization_z_63d_slope_v139_signal(marketcap):
    base = _z(marketcap, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z marketcap
def mc_f036_market_capitalization_z_63d_slope_v140_signal(marketcap):
    base = _z(marketcap, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z marketcap
def mc_f036_market_capitalization_z_63d_slope_v141_signal(marketcap):
    base = _z(marketcap, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z marketcap
def mc_f036_market_capitalization_z_126d_slope_v142_signal(marketcap):
    base = _z(marketcap, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z marketcap
def mc_f036_market_capitalization_z_126d_slope_v143_signal(marketcap):
    base = _z(marketcap, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z marketcap
def mc_f036_market_capitalization_z_126d_slope_v144_signal(marketcap):
    base = _z(marketcap, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z marketcap
def mc_f036_market_capitalization_z_252d_slope_v145_signal(marketcap):
    base = _z(marketcap, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z marketcap
def mc_f036_market_capitalization_z_252d_slope_v146_signal(marketcap):
    base = _z(marketcap, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z marketcap
def mc_f036_market_capitalization_z_252d_slope_v147_signal(marketcap):
    base = _z(marketcap, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z marketcap
def mc_f036_market_capitalization_z_504d_slope_v148_signal(marketcap):
    base = _z(marketcap, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z marketcap
def mc_f036_market_capitalization_z_504d_slope_v149_signal(marketcap):
    base = _z(marketcap, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z marketcap
def mc_f036_market_capitalization_z_504d_slope_v150_signal(marketcap):
    base = _z(marketcap, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
