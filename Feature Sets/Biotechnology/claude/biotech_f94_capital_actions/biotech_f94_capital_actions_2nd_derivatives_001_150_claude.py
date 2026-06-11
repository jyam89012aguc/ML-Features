"""Family f94 - Capital-structure actions  (Q_Actions_Events) | 2nd derivatives 001-150"""
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
def _capital_actions_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capital_actions_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capital_actions_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw actionvalue
def ca_f94_capital_actions_raw_21d_slope_v001_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw actionvalue
def ca_f94_capital_actions_raw_21d_slope_v002_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw actionvalue
def ca_f94_capital_actions_raw_21d_slope_v003_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw actionvalue
def ca_f94_capital_actions_raw_63d_slope_v004_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw actionvalue
def ca_f94_capital_actions_raw_63d_slope_v005_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw actionvalue
def ca_f94_capital_actions_raw_63d_slope_v006_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw actionvalue
def ca_f94_capital_actions_raw_126d_slope_v007_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw actionvalue
def ca_f94_capital_actions_raw_126d_slope_v008_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw actionvalue
def ca_f94_capital_actions_raw_126d_slope_v009_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw actionvalue
def ca_f94_capital_actions_raw_252d_slope_v010_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw actionvalue
def ca_f94_capital_actions_raw_252d_slope_v011_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw actionvalue
def ca_f94_capital_actions_raw_252d_slope_v012_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw actionvalue
def ca_f94_capital_actions_raw_504d_slope_v013_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw actionvalue
def ca_f94_capital_actions_raw_504d_slope_v014_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw actionvalue
def ca_f94_capital_actions_raw_504d_slope_v015_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log actionvalue
def ca_f94_capital_actions_log_21d_slope_v016_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log actionvalue
def ca_f94_capital_actions_log_21d_slope_v017_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log actionvalue
def ca_f94_capital_actions_log_21d_slope_v018_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log actionvalue
def ca_f94_capital_actions_log_63d_slope_v019_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log actionvalue
def ca_f94_capital_actions_log_63d_slope_v020_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log actionvalue
def ca_f94_capital_actions_log_63d_slope_v021_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log actionvalue
def ca_f94_capital_actions_log_126d_slope_v022_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log actionvalue
def ca_f94_capital_actions_log_126d_slope_v023_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log actionvalue
def ca_f94_capital_actions_log_126d_slope_v024_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log actionvalue
def ca_f94_capital_actions_log_252d_slope_v025_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log actionvalue
def ca_f94_capital_actions_log_252d_slope_v026_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log actionvalue
def ca_f94_capital_actions_log_252d_slope_v027_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log actionvalue
def ca_f94_capital_actions_log_504d_slope_v028_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log actionvalue
def ca_f94_capital_actions_log_504d_slope_v029_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log actionvalue
def ca_f94_capital_actions_log_504d_slope_v030_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare actionvalue
def ca_f94_capital_actions_pershare_21d_slope_v031_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare actionvalue
def ca_f94_capital_actions_pershare_21d_slope_v032_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare actionvalue
def ca_f94_capital_actions_pershare_21d_slope_v033_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare actionvalue
def ca_f94_capital_actions_pershare_63d_slope_v034_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare actionvalue
def ca_f94_capital_actions_pershare_63d_slope_v035_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare actionvalue
def ca_f94_capital_actions_pershare_63d_slope_v036_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare actionvalue
def ca_f94_capital_actions_pershare_126d_slope_v037_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare actionvalue
def ca_f94_capital_actions_pershare_126d_slope_v038_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare actionvalue
def ca_f94_capital_actions_pershare_126d_slope_v039_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare actionvalue
def ca_f94_capital_actions_pershare_252d_slope_v040_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare actionvalue
def ca_f94_capital_actions_pershare_252d_slope_v041_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare actionvalue
def ca_f94_capital_actions_pershare_252d_slope_v042_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare actionvalue
def ca_f94_capital_actions_pershare_504d_slope_v043_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare actionvalue
def ca_f94_capital_actions_pershare_504d_slope_v044_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare actionvalue
def ca_f94_capital_actions_pershare_504d_slope_v045_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets actionvalue
def ca_f94_capital_actions_per_assets_21d_slope_v046_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets actionvalue
def ca_f94_capital_actions_per_assets_21d_slope_v047_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets actionvalue
def ca_f94_capital_actions_per_assets_21d_slope_v048_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets actionvalue
def ca_f94_capital_actions_per_assets_63d_slope_v049_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets actionvalue
def ca_f94_capital_actions_per_assets_63d_slope_v050_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets actionvalue
def ca_f94_capital_actions_per_assets_63d_slope_v051_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets actionvalue
def ca_f94_capital_actions_per_assets_126d_slope_v052_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets actionvalue
def ca_f94_capital_actions_per_assets_126d_slope_v053_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets actionvalue
def ca_f94_capital_actions_per_assets_126d_slope_v054_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets actionvalue
def ca_f94_capital_actions_per_assets_252d_slope_v055_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets actionvalue
def ca_f94_capital_actions_per_assets_252d_slope_v056_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets actionvalue
def ca_f94_capital_actions_per_assets_252d_slope_v057_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets actionvalue
def ca_f94_capital_actions_per_assets_504d_slope_v058_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets actionvalue
def ca_f94_capital_actions_per_assets_504d_slope_v059_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets actionvalue
def ca_f94_capital_actions_per_assets_504d_slope_v060_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_21d_slope_v061_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_21d_slope_v062_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_21d_slope_v063_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_63d_slope_v064_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_63d_slope_v065_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_63d_slope_v066_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_126d_slope_v067_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_126d_slope_v068_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_126d_slope_v069_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_252d_slope_v070_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_252d_slope_v071_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_252d_slope_v072_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_504d_slope_v073_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_504d_slope_v074_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_504d_slope_v075_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity actionvalue
def ca_f94_capital_actions_per_equity_21d_slope_v076_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity actionvalue
def ca_f94_capital_actions_per_equity_21d_slope_v077_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity actionvalue
def ca_f94_capital_actions_per_equity_21d_slope_v078_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity actionvalue
def ca_f94_capital_actions_per_equity_63d_slope_v079_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity actionvalue
def ca_f94_capital_actions_per_equity_63d_slope_v080_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity actionvalue
def ca_f94_capital_actions_per_equity_63d_slope_v081_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity actionvalue
def ca_f94_capital_actions_per_equity_126d_slope_v082_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity actionvalue
def ca_f94_capital_actions_per_equity_126d_slope_v083_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity actionvalue
def ca_f94_capital_actions_per_equity_126d_slope_v084_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity actionvalue
def ca_f94_capital_actions_per_equity_252d_slope_v085_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity actionvalue
def ca_f94_capital_actions_per_equity_252d_slope_v086_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity actionvalue
def ca_f94_capital_actions_per_equity_252d_slope_v087_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity actionvalue
def ca_f94_capital_actions_per_equity_504d_slope_v088_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity actionvalue
def ca_f94_capital_actions_per_equity_504d_slope_v089_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity actionvalue
def ca_f94_capital_actions_per_equity_504d_slope_v090_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std actionvalue
def ca_f94_capital_actions_std_21d_slope_v091_signal(actionvalue, closeadj):
    base = _std(actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std actionvalue
def ca_f94_capital_actions_std_21d_slope_v092_signal(actionvalue, closeadj):
    base = _std(actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std actionvalue
def ca_f94_capital_actions_std_21d_slope_v093_signal(actionvalue, closeadj):
    base = _std(actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std actionvalue
def ca_f94_capital_actions_std_63d_slope_v094_signal(actionvalue, closeadj):
    base = _std(actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std actionvalue
def ca_f94_capital_actions_std_63d_slope_v095_signal(actionvalue, closeadj):
    base = _std(actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std actionvalue
def ca_f94_capital_actions_std_63d_slope_v096_signal(actionvalue, closeadj):
    base = _std(actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std actionvalue
def ca_f94_capital_actions_std_126d_slope_v097_signal(actionvalue, closeadj):
    base = _std(actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std actionvalue
def ca_f94_capital_actions_std_126d_slope_v098_signal(actionvalue, closeadj):
    base = _std(actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std actionvalue
def ca_f94_capital_actions_std_126d_slope_v099_signal(actionvalue, closeadj):
    base = _std(actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std actionvalue
def ca_f94_capital_actions_std_252d_slope_v100_signal(actionvalue, closeadj):
    base = _std(actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std actionvalue
def ca_f94_capital_actions_std_252d_slope_v101_signal(actionvalue, closeadj):
    base = _std(actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std actionvalue
def ca_f94_capital_actions_std_252d_slope_v102_signal(actionvalue, closeadj):
    base = _std(actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std actionvalue
def ca_f94_capital_actions_std_504d_slope_v103_signal(actionvalue, closeadj):
    base = _std(actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std actionvalue
def ca_f94_capital_actions_std_504d_slope_v104_signal(actionvalue, closeadj):
    base = _std(actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std actionvalue
def ca_f94_capital_actions_std_504d_slope_v105_signal(actionvalue, closeadj):
    base = _std(actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm actionvalue
def ca_f94_capital_actions_ewm_21d_slope_v106_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm actionvalue
def ca_f94_capital_actions_ewm_21d_slope_v107_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm actionvalue
def ca_f94_capital_actions_ewm_21d_slope_v108_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm actionvalue
def ca_f94_capital_actions_ewm_63d_slope_v109_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm actionvalue
def ca_f94_capital_actions_ewm_63d_slope_v110_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm actionvalue
def ca_f94_capital_actions_ewm_63d_slope_v111_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm actionvalue
def ca_f94_capital_actions_ewm_126d_slope_v112_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm actionvalue
def ca_f94_capital_actions_ewm_126d_slope_v113_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm actionvalue
def ca_f94_capital_actions_ewm_126d_slope_v114_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm actionvalue
def ca_f94_capital_actions_ewm_252d_slope_v115_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm actionvalue
def ca_f94_capital_actions_ewm_252d_slope_v116_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm actionvalue
def ca_f94_capital_actions_ewm_252d_slope_v117_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm actionvalue
def ca_f94_capital_actions_ewm_504d_slope_v118_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm actionvalue
def ca_f94_capital_actions_ewm_504d_slope_v119_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm actionvalue
def ca_f94_capital_actions_ewm_504d_slope_v120_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq actionvalue
def ca_f94_capital_actions_sq_21d_slope_v121_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq actionvalue
def ca_f94_capital_actions_sq_21d_slope_v122_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq actionvalue
def ca_f94_capital_actions_sq_21d_slope_v123_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq actionvalue
def ca_f94_capital_actions_sq_63d_slope_v124_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq actionvalue
def ca_f94_capital_actions_sq_63d_slope_v125_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq actionvalue
def ca_f94_capital_actions_sq_63d_slope_v126_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq actionvalue
def ca_f94_capital_actions_sq_126d_slope_v127_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq actionvalue
def ca_f94_capital_actions_sq_126d_slope_v128_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq actionvalue
def ca_f94_capital_actions_sq_126d_slope_v129_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq actionvalue
def ca_f94_capital_actions_sq_252d_slope_v130_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq actionvalue
def ca_f94_capital_actions_sq_252d_slope_v131_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq actionvalue
def ca_f94_capital_actions_sq_252d_slope_v132_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq actionvalue
def ca_f94_capital_actions_sq_504d_slope_v133_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq actionvalue
def ca_f94_capital_actions_sq_504d_slope_v134_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq actionvalue
def ca_f94_capital_actions_sq_504d_slope_v135_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z actionvalue
def ca_f94_capital_actions_z_21d_slope_v136_signal(actionvalue):
    base = _z(actionvalue, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z actionvalue
def ca_f94_capital_actions_z_21d_slope_v137_signal(actionvalue):
    base = _z(actionvalue, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z actionvalue
def ca_f94_capital_actions_z_21d_slope_v138_signal(actionvalue):
    base = _z(actionvalue, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z actionvalue
def ca_f94_capital_actions_z_63d_slope_v139_signal(actionvalue):
    base = _z(actionvalue, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z actionvalue
def ca_f94_capital_actions_z_63d_slope_v140_signal(actionvalue):
    base = _z(actionvalue, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z actionvalue
def ca_f94_capital_actions_z_63d_slope_v141_signal(actionvalue):
    base = _z(actionvalue, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z actionvalue
def ca_f94_capital_actions_z_126d_slope_v142_signal(actionvalue):
    base = _z(actionvalue, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z actionvalue
def ca_f94_capital_actions_z_126d_slope_v143_signal(actionvalue):
    base = _z(actionvalue, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z actionvalue
def ca_f94_capital_actions_z_126d_slope_v144_signal(actionvalue):
    base = _z(actionvalue, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z actionvalue
def ca_f94_capital_actions_z_252d_slope_v145_signal(actionvalue):
    base = _z(actionvalue, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z actionvalue
def ca_f94_capital_actions_z_252d_slope_v146_signal(actionvalue):
    base = _z(actionvalue, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z actionvalue
def ca_f94_capital_actions_z_252d_slope_v147_signal(actionvalue):
    base = _z(actionvalue, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z actionvalue
def ca_f94_capital_actions_z_504d_slope_v148_signal(actionvalue):
    base = _z(actionvalue, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z actionvalue
def ca_f94_capital_actions_z_504d_slope_v149_signal(actionvalue):
    base = _z(actionvalue, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z actionvalue
def ca_f94_capital_actions_z_504d_slope_v150_signal(actionvalue):
    base = _z(actionvalue, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
