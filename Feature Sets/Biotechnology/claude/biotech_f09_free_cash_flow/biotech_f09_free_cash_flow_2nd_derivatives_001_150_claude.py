"""Family f09 - Free cash flow  (B_CashFlow_Burn) | 2nd derivatives 001-150"""
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
def _free_cash_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _free_cash_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _free_cash_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw fcf
def fcf_f09_free_cash_flow_raw_21d_slope_v001_signal(fcf, closeadj):
    base = _mean(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw fcf
def fcf_f09_free_cash_flow_raw_21d_slope_v002_signal(fcf, closeadj):
    base = _mean(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw fcf
def fcf_f09_free_cash_flow_raw_21d_slope_v003_signal(fcf, closeadj):
    base = _mean(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw fcf
def fcf_f09_free_cash_flow_raw_63d_slope_v004_signal(fcf, closeadj):
    base = _mean(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw fcf
def fcf_f09_free_cash_flow_raw_63d_slope_v005_signal(fcf, closeadj):
    base = _mean(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw fcf
def fcf_f09_free_cash_flow_raw_63d_slope_v006_signal(fcf, closeadj):
    base = _mean(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw fcf
def fcf_f09_free_cash_flow_raw_126d_slope_v007_signal(fcf, closeadj):
    base = _mean(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw fcf
def fcf_f09_free_cash_flow_raw_126d_slope_v008_signal(fcf, closeadj):
    base = _mean(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw fcf
def fcf_f09_free_cash_flow_raw_126d_slope_v009_signal(fcf, closeadj):
    base = _mean(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw fcf
def fcf_f09_free_cash_flow_raw_252d_slope_v010_signal(fcf, closeadj):
    base = _mean(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw fcf
def fcf_f09_free_cash_flow_raw_252d_slope_v011_signal(fcf, closeadj):
    base = _mean(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw fcf
def fcf_f09_free_cash_flow_raw_252d_slope_v012_signal(fcf, closeadj):
    base = _mean(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw fcf
def fcf_f09_free_cash_flow_raw_504d_slope_v013_signal(fcf, closeadj):
    base = _mean(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw fcf
def fcf_f09_free_cash_flow_raw_504d_slope_v014_signal(fcf, closeadj):
    base = _mean(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw fcf
def fcf_f09_free_cash_flow_raw_504d_slope_v015_signal(fcf, closeadj):
    base = _mean(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log fcf
def fcf_f09_free_cash_flow_log_21d_slope_v016_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log fcf
def fcf_f09_free_cash_flow_log_21d_slope_v017_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log fcf
def fcf_f09_free_cash_flow_log_21d_slope_v018_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log fcf
def fcf_f09_free_cash_flow_log_63d_slope_v019_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log fcf
def fcf_f09_free_cash_flow_log_63d_slope_v020_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log fcf
def fcf_f09_free_cash_flow_log_63d_slope_v021_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log fcf
def fcf_f09_free_cash_flow_log_126d_slope_v022_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log fcf
def fcf_f09_free_cash_flow_log_126d_slope_v023_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log fcf
def fcf_f09_free_cash_flow_log_126d_slope_v024_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log fcf
def fcf_f09_free_cash_flow_log_252d_slope_v025_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log fcf
def fcf_f09_free_cash_flow_log_252d_slope_v026_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log fcf
def fcf_f09_free_cash_flow_log_252d_slope_v027_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log fcf
def fcf_f09_free_cash_flow_log_504d_slope_v028_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log fcf
def fcf_f09_free_cash_flow_log_504d_slope_v029_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log fcf
def fcf_f09_free_cash_flow_log_504d_slope_v030_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_log(fcf), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare fcf
def fcf_f09_free_cash_flow_pershare_21d_slope_v031_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare fcf
def fcf_f09_free_cash_flow_pershare_21d_slope_v032_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare fcf
def fcf_f09_free_cash_flow_pershare_21d_slope_v033_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare fcf
def fcf_f09_free_cash_flow_pershare_63d_slope_v034_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare fcf
def fcf_f09_free_cash_flow_pershare_63d_slope_v035_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare fcf
def fcf_f09_free_cash_flow_pershare_63d_slope_v036_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare fcf
def fcf_f09_free_cash_flow_pershare_126d_slope_v037_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare fcf
def fcf_f09_free_cash_flow_pershare_126d_slope_v038_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare fcf
def fcf_f09_free_cash_flow_pershare_126d_slope_v039_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare fcf
def fcf_f09_free_cash_flow_pershare_252d_slope_v040_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare fcf
def fcf_f09_free_cash_flow_pershare_252d_slope_v041_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare fcf
def fcf_f09_free_cash_flow_pershare_252d_slope_v042_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare fcf
def fcf_f09_free_cash_flow_pershare_504d_slope_v043_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare fcf
def fcf_f09_free_cash_flow_pershare_504d_slope_v044_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare fcf
def fcf_f09_free_cash_flow_pershare_504d_slope_v045_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_per_share(fcf, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_21d_slope_v046_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_21d_slope_v047_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_21d_slope_v048_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_63d_slope_v049_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_63d_slope_v050_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_63d_slope_v051_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_126d_slope_v052_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_126d_slope_v053_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_126d_slope_v054_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_252d_slope_v055_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_252d_slope_v056_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_252d_slope_v057_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_504d_slope_v058_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_504d_slope_v059_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets fcf
def fcf_f09_free_cash_flow_per_assets_504d_slope_v060_signal(fcf, assets):
    base = _mean(_free_cash_flow_scaled(fcf, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_21d_slope_v061_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_21d_slope_v062_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_21d_slope_v063_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_63d_slope_v064_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_63d_slope_v065_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_63d_slope_v066_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_126d_slope_v067_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_126d_slope_v068_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_126d_slope_v069_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_252d_slope_v070_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_252d_slope_v071_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_252d_slope_v072_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_504d_slope_v073_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_504d_slope_v074_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap fcf
def fcf_f09_free_cash_flow_per_marketcap_504d_slope_v075_signal(fcf, marketcap):
    base = _mean(_free_cash_flow_scaled(fcf, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_21d_slope_v076_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_21d_slope_v077_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_21d_slope_v078_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_63d_slope_v079_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_63d_slope_v080_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_63d_slope_v081_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_126d_slope_v082_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_126d_slope_v083_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_126d_slope_v084_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_252d_slope_v085_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_252d_slope_v086_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_252d_slope_v087_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_504d_slope_v088_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_504d_slope_v089_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity fcf
def fcf_f09_free_cash_flow_per_equity_504d_slope_v090_signal(fcf, equity):
    base = _mean(_free_cash_flow_scaled(fcf, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std fcf
def fcf_f09_free_cash_flow_std_21d_slope_v091_signal(fcf, closeadj):
    base = _std(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std fcf
def fcf_f09_free_cash_flow_std_21d_slope_v092_signal(fcf, closeadj):
    base = _std(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std fcf
def fcf_f09_free_cash_flow_std_21d_slope_v093_signal(fcf, closeadj):
    base = _std(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std fcf
def fcf_f09_free_cash_flow_std_63d_slope_v094_signal(fcf, closeadj):
    base = _std(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std fcf
def fcf_f09_free_cash_flow_std_63d_slope_v095_signal(fcf, closeadj):
    base = _std(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std fcf
def fcf_f09_free_cash_flow_std_63d_slope_v096_signal(fcf, closeadj):
    base = _std(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std fcf
def fcf_f09_free_cash_flow_std_126d_slope_v097_signal(fcf, closeadj):
    base = _std(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std fcf
def fcf_f09_free_cash_flow_std_126d_slope_v098_signal(fcf, closeadj):
    base = _std(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std fcf
def fcf_f09_free_cash_flow_std_126d_slope_v099_signal(fcf, closeadj):
    base = _std(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std fcf
def fcf_f09_free_cash_flow_std_252d_slope_v100_signal(fcf, closeadj):
    base = _std(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std fcf
def fcf_f09_free_cash_flow_std_252d_slope_v101_signal(fcf, closeadj):
    base = _std(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std fcf
def fcf_f09_free_cash_flow_std_252d_slope_v102_signal(fcf, closeadj):
    base = _std(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std fcf
def fcf_f09_free_cash_flow_std_504d_slope_v103_signal(fcf, closeadj):
    base = _std(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std fcf
def fcf_f09_free_cash_flow_std_504d_slope_v104_signal(fcf, closeadj):
    base = _std(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std fcf
def fcf_f09_free_cash_flow_std_504d_slope_v105_signal(fcf, closeadj):
    base = _std(fcf, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm fcf
def fcf_f09_free_cash_flow_ewm_21d_slope_v106_signal(fcf, closeadj):
    base = fcf.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm fcf
def fcf_f09_free_cash_flow_ewm_21d_slope_v107_signal(fcf, closeadj):
    base = fcf.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm fcf
def fcf_f09_free_cash_flow_ewm_21d_slope_v108_signal(fcf, closeadj):
    base = fcf.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm fcf
def fcf_f09_free_cash_flow_ewm_63d_slope_v109_signal(fcf, closeadj):
    base = fcf.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm fcf
def fcf_f09_free_cash_flow_ewm_63d_slope_v110_signal(fcf, closeadj):
    base = fcf.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm fcf
def fcf_f09_free_cash_flow_ewm_63d_slope_v111_signal(fcf, closeadj):
    base = fcf.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm fcf
def fcf_f09_free_cash_flow_ewm_126d_slope_v112_signal(fcf, closeadj):
    base = fcf.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm fcf
def fcf_f09_free_cash_flow_ewm_126d_slope_v113_signal(fcf, closeadj):
    base = fcf.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm fcf
def fcf_f09_free_cash_flow_ewm_126d_slope_v114_signal(fcf, closeadj):
    base = fcf.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm fcf
def fcf_f09_free_cash_flow_ewm_252d_slope_v115_signal(fcf, closeadj):
    base = fcf.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm fcf
def fcf_f09_free_cash_flow_ewm_252d_slope_v116_signal(fcf, closeadj):
    base = fcf.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm fcf
def fcf_f09_free_cash_flow_ewm_252d_slope_v117_signal(fcf, closeadj):
    base = fcf.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm fcf
def fcf_f09_free_cash_flow_ewm_504d_slope_v118_signal(fcf, closeadj):
    base = fcf.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm fcf
def fcf_f09_free_cash_flow_ewm_504d_slope_v119_signal(fcf, closeadj):
    base = fcf.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm fcf
def fcf_f09_free_cash_flow_ewm_504d_slope_v120_signal(fcf, closeadj):
    base = fcf.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq fcf
def fcf_f09_free_cash_flow_sq_21d_slope_v121_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq fcf
def fcf_f09_free_cash_flow_sq_21d_slope_v122_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq fcf
def fcf_f09_free_cash_flow_sq_21d_slope_v123_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq fcf
def fcf_f09_free_cash_flow_sq_63d_slope_v124_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq fcf
def fcf_f09_free_cash_flow_sq_63d_slope_v125_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq fcf
def fcf_f09_free_cash_flow_sq_63d_slope_v126_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq fcf
def fcf_f09_free_cash_flow_sq_126d_slope_v127_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq fcf
def fcf_f09_free_cash_flow_sq_126d_slope_v128_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq fcf
def fcf_f09_free_cash_flow_sq_126d_slope_v129_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq fcf
def fcf_f09_free_cash_flow_sq_252d_slope_v130_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq fcf
def fcf_f09_free_cash_flow_sq_252d_slope_v131_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq fcf
def fcf_f09_free_cash_flow_sq_252d_slope_v132_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq fcf
def fcf_f09_free_cash_flow_sq_504d_slope_v133_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq fcf
def fcf_f09_free_cash_flow_sq_504d_slope_v134_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq fcf
def fcf_f09_free_cash_flow_sq_504d_slope_v135_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z fcf
def fcf_f09_free_cash_flow_z_21d_slope_v136_signal(fcf):
    base = _z(fcf, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z fcf
def fcf_f09_free_cash_flow_z_21d_slope_v137_signal(fcf):
    base = _z(fcf, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z fcf
def fcf_f09_free_cash_flow_z_21d_slope_v138_signal(fcf):
    base = _z(fcf, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z fcf
def fcf_f09_free_cash_flow_z_63d_slope_v139_signal(fcf):
    base = _z(fcf, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z fcf
def fcf_f09_free_cash_flow_z_63d_slope_v140_signal(fcf):
    base = _z(fcf, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z fcf
def fcf_f09_free_cash_flow_z_63d_slope_v141_signal(fcf):
    base = _z(fcf, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z fcf
def fcf_f09_free_cash_flow_z_126d_slope_v142_signal(fcf):
    base = _z(fcf, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z fcf
def fcf_f09_free_cash_flow_z_126d_slope_v143_signal(fcf):
    base = _z(fcf, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z fcf
def fcf_f09_free_cash_flow_z_126d_slope_v144_signal(fcf):
    base = _z(fcf, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z fcf
def fcf_f09_free_cash_flow_z_252d_slope_v145_signal(fcf):
    base = _z(fcf, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z fcf
def fcf_f09_free_cash_flow_z_252d_slope_v146_signal(fcf):
    base = _z(fcf, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z fcf
def fcf_f09_free_cash_flow_z_252d_slope_v147_signal(fcf):
    base = _z(fcf, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z fcf
def fcf_f09_free_cash_flow_z_504d_slope_v148_signal(fcf):
    base = _z(fcf, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z fcf
def fcf_f09_free_cash_flow_z_504d_slope_v149_signal(fcf):
    base = _z(fcf, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z fcf
def fcf_f09_free_cash_flow_z_504d_slope_v150_signal(fcf):
    base = _z(fcf, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
