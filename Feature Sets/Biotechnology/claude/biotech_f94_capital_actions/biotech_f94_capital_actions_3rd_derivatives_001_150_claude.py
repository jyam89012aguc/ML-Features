"""Family f94 - Capital-structure actions  (Q_Actions_Events) | 3rd derivatives 001-150"""
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


# 5d accel of 21d raw actionvalue
def ca_f94_capital_actions_raw_21d_accel_v001_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw actionvalue
def ca_f94_capital_actions_raw_21d_accel_v002_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw actionvalue
def ca_f94_capital_actions_raw_21d_accel_v003_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw actionvalue
def ca_f94_capital_actions_raw_63d_accel_v004_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw actionvalue
def ca_f94_capital_actions_raw_63d_accel_v005_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw actionvalue
def ca_f94_capital_actions_raw_63d_accel_v006_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw actionvalue
def ca_f94_capital_actions_raw_126d_accel_v007_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw actionvalue
def ca_f94_capital_actions_raw_126d_accel_v008_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw actionvalue
def ca_f94_capital_actions_raw_126d_accel_v009_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw actionvalue
def ca_f94_capital_actions_raw_252d_accel_v010_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw actionvalue
def ca_f94_capital_actions_raw_252d_accel_v011_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw actionvalue
def ca_f94_capital_actions_raw_252d_accel_v012_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw actionvalue
def ca_f94_capital_actions_raw_504d_accel_v013_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw actionvalue
def ca_f94_capital_actions_raw_504d_accel_v014_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw actionvalue
def ca_f94_capital_actions_raw_504d_accel_v015_signal(actionvalue, closeadj):
    base = _mean(actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log actionvalue
def ca_f94_capital_actions_log_21d_accel_v016_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log actionvalue
def ca_f94_capital_actions_log_21d_accel_v017_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log actionvalue
def ca_f94_capital_actions_log_21d_accel_v018_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log actionvalue
def ca_f94_capital_actions_log_63d_accel_v019_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log actionvalue
def ca_f94_capital_actions_log_63d_accel_v020_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log actionvalue
def ca_f94_capital_actions_log_63d_accel_v021_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log actionvalue
def ca_f94_capital_actions_log_126d_accel_v022_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log actionvalue
def ca_f94_capital_actions_log_126d_accel_v023_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log actionvalue
def ca_f94_capital_actions_log_126d_accel_v024_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log actionvalue
def ca_f94_capital_actions_log_252d_accel_v025_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log actionvalue
def ca_f94_capital_actions_log_252d_accel_v026_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log actionvalue
def ca_f94_capital_actions_log_252d_accel_v027_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log actionvalue
def ca_f94_capital_actions_log_504d_accel_v028_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log actionvalue
def ca_f94_capital_actions_log_504d_accel_v029_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log actionvalue
def ca_f94_capital_actions_log_504d_accel_v030_signal(actionvalue, closeadj):
    base = _mean(_capital_actions_log(actionvalue), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare actionvalue
def ca_f94_capital_actions_pershare_21d_accel_v031_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare actionvalue
def ca_f94_capital_actions_pershare_21d_accel_v032_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare actionvalue
def ca_f94_capital_actions_pershare_21d_accel_v033_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare actionvalue
def ca_f94_capital_actions_pershare_63d_accel_v034_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare actionvalue
def ca_f94_capital_actions_pershare_63d_accel_v035_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare actionvalue
def ca_f94_capital_actions_pershare_63d_accel_v036_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare actionvalue
def ca_f94_capital_actions_pershare_126d_accel_v037_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare actionvalue
def ca_f94_capital_actions_pershare_126d_accel_v038_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare actionvalue
def ca_f94_capital_actions_pershare_126d_accel_v039_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare actionvalue
def ca_f94_capital_actions_pershare_252d_accel_v040_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare actionvalue
def ca_f94_capital_actions_pershare_252d_accel_v041_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare actionvalue
def ca_f94_capital_actions_pershare_252d_accel_v042_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare actionvalue
def ca_f94_capital_actions_pershare_504d_accel_v043_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare actionvalue
def ca_f94_capital_actions_pershare_504d_accel_v044_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare actionvalue
def ca_f94_capital_actions_pershare_504d_accel_v045_signal(actionvalue, sharesbas, closeadj):
    base = _mean(_capital_actions_per_share(actionvalue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets actionvalue
def ca_f94_capital_actions_per_assets_21d_accel_v046_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets actionvalue
def ca_f94_capital_actions_per_assets_21d_accel_v047_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets actionvalue
def ca_f94_capital_actions_per_assets_21d_accel_v048_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets actionvalue
def ca_f94_capital_actions_per_assets_63d_accel_v049_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets actionvalue
def ca_f94_capital_actions_per_assets_63d_accel_v050_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets actionvalue
def ca_f94_capital_actions_per_assets_63d_accel_v051_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets actionvalue
def ca_f94_capital_actions_per_assets_126d_accel_v052_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets actionvalue
def ca_f94_capital_actions_per_assets_126d_accel_v053_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets actionvalue
def ca_f94_capital_actions_per_assets_126d_accel_v054_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets actionvalue
def ca_f94_capital_actions_per_assets_252d_accel_v055_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets actionvalue
def ca_f94_capital_actions_per_assets_252d_accel_v056_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets actionvalue
def ca_f94_capital_actions_per_assets_252d_accel_v057_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets actionvalue
def ca_f94_capital_actions_per_assets_504d_accel_v058_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets actionvalue
def ca_f94_capital_actions_per_assets_504d_accel_v059_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets actionvalue
def ca_f94_capital_actions_per_assets_504d_accel_v060_signal(actionvalue, assets):
    base = _mean(_capital_actions_scaled(actionvalue, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_21d_accel_v061_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_21d_accel_v062_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_21d_accel_v063_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_63d_accel_v064_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_63d_accel_v065_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_63d_accel_v066_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_126d_accel_v067_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_126d_accel_v068_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_126d_accel_v069_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_252d_accel_v070_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_252d_accel_v071_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_252d_accel_v072_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_504d_accel_v073_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_504d_accel_v074_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap actionvalue
def ca_f94_capital_actions_per_marketcap_504d_accel_v075_signal(actionvalue, marketcap):
    base = _mean(_capital_actions_scaled(actionvalue, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity actionvalue
def ca_f94_capital_actions_per_equity_21d_accel_v076_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity actionvalue
def ca_f94_capital_actions_per_equity_21d_accel_v077_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity actionvalue
def ca_f94_capital_actions_per_equity_21d_accel_v078_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity actionvalue
def ca_f94_capital_actions_per_equity_63d_accel_v079_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity actionvalue
def ca_f94_capital_actions_per_equity_63d_accel_v080_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity actionvalue
def ca_f94_capital_actions_per_equity_63d_accel_v081_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity actionvalue
def ca_f94_capital_actions_per_equity_126d_accel_v082_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity actionvalue
def ca_f94_capital_actions_per_equity_126d_accel_v083_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity actionvalue
def ca_f94_capital_actions_per_equity_126d_accel_v084_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity actionvalue
def ca_f94_capital_actions_per_equity_252d_accel_v085_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity actionvalue
def ca_f94_capital_actions_per_equity_252d_accel_v086_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity actionvalue
def ca_f94_capital_actions_per_equity_252d_accel_v087_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity actionvalue
def ca_f94_capital_actions_per_equity_504d_accel_v088_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity actionvalue
def ca_f94_capital_actions_per_equity_504d_accel_v089_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity actionvalue
def ca_f94_capital_actions_per_equity_504d_accel_v090_signal(actionvalue, equity):
    base = _mean(_capital_actions_scaled(actionvalue, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std actionvalue
def ca_f94_capital_actions_std_21d_accel_v091_signal(actionvalue, closeadj):
    base = _std(actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std actionvalue
def ca_f94_capital_actions_std_21d_accel_v092_signal(actionvalue, closeadj):
    base = _std(actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std actionvalue
def ca_f94_capital_actions_std_21d_accel_v093_signal(actionvalue, closeadj):
    base = _std(actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std actionvalue
def ca_f94_capital_actions_std_63d_accel_v094_signal(actionvalue, closeadj):
    base = _std(actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std actionvalue
def ca_f94_capital_actions_std_63d_accel_v095_signal(actionvalue, closeadj):
    base = _std(actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std actionvalue
def ca_f94_capital_actions_std_63d_accel_v096_signal(actionvalue, closeadj):
    base = _std(actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std actionvalue
def ca_f94_capital_actions_std_126d_accel_v097_signal(actionvalue, closeadj):
    base = _std(actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std actionvalue
def ca_f94_capital_actions_std_126d_accel_v098_signal(actionvalue, closeadj):
    base = _std(actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std actionvalue
def ca_f94_capital_actions_std_126d_accel_v099_signal(actionvalue, closeadj):
    base = _std(actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std actionvalue
def ca_f94_capital_actions_std_252d_accel_v100_signal(actionvalue, closeadj):
    base = _std(actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std actionvalue
def ca_f94_capital_actions_std_252d_accel_v101_signal(actionvalue, closeadj):
    base = _std(actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std actionvalue
def ca_f94_capital_actions_std_252d_accel_v102_signal(actionvalue, closeadj):
    base = _std(actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std actionvalue
def ca_f94_capital_actions_std_504d_accel_v103_signal(actionvalue, closeadj):
    base = _std(actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std actionvalue
def ca_f94_capital_actions_std_504d_accel_v104_signal(actionvalue, closeadj):
    base = _std(actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std actionvalue
def ca_f94_capital_actions_std_504d_accel_v105_signal(actionvalue, closeadj):
    base = _std(actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm actionvalue
def ca_f94_capital_actions_ewm_21d_accel_v106_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm actionvalue
def ca_f94_capital_actions_ewm_21d_accel_v107_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm actionvalue
def ca_f94_capital_actions_ewm_21d_accel_v108_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm actionvalue
def ca_f94_capital_actions_ewm_63d_accel_v109_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm actionvalue
def ca_f94_capital_actions_ewm_63d_accel_v110_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm actionvalue
def ca_f94_capital_actions_ewm_63d_accel_v111_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm actionvalue
def ca_f94_capital_actions_ewm_126d_accel_v112_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm actionvalue
def ca_f94_capital_actions_ewm_126d_accel_v113_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm actionvalue
def ca_f94_capital_actions_ewm_126d_accel_v114_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm actionvalue
def ca_f94_capital_actions_ewm_252d_accel_v115_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm actionvalue
def ca_f94_capital_actions_ewm_252d_accel_v116_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm actionvalue
def ca_f94_capital_actions_ewm_252d_accel_v117_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm actionvalue
def ca_f94_capital_actions_ewm_504d_accel_v118_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm actionvalue
def ca_f94_capital_actions_ewm_504d_accel_v119_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm actionvalue
def ca_f94_capital_actions_ewm_504d_accel_v120_signal(actionvalue, closeadj):
    base = actionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq actionvalue
def ca_f94_capital_actions_sq_21d_accel_v121_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq actionvalue
def ca_f94_capital_actions_sq_21d_accel_v122_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq actionvalue
def ca_f94_capital_actions_sq_21d_accel_v123_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq actionvalue
def ca_f94_capital_actions_sq_63d_accel_v124_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq actionvalue
def ca_f94_capital_actions_sq_63d_accel_v125_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq actionvalue
def ca_f94_capital_actions_sq_63d_accel_v126_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq actionvalue
def ca_f94_capital_actions_sq_126d_accel_v127_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq actionvalue
def ca_f94_capital_actions_sq_126d_accel_v128_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq actionvalue
def ca_f94_capital_actions_sq_126d_accel_v129_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq actionvalue
def ca_f94_capital_actions_sq_252d_accel_v130_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq actionvalue
def ca_f94_capital_actions_sq_252d_accel_v131_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq actionvalue
def ca_f94_capital_actions_sq_252d_accel_v132_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq actionvalue
def ca_f94_capital_actions_sq_504d_accel_v133_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq actionvalue
def ca_f94_capital_actions_sq_504d_accel_v134_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq actionvalue
def ca_f94_capital_actions_sq_504d_accel_v135_signal(actionvalue, closeadj):
    base = _mean(actionvalue * actionvalue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z actionvalue
def ca_f94_capital_actions_z_21d_accel_v136_signal(actionvalue):
    base = _z(actionvalue, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z actionvalue
def ca_f94_capital_actions_z_21d_accel_v137_signal(actionvalue):
    base = _z(actionvalue, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z actionvalue
def ca_f94_capital_actions_z_21d_accel_v138_signal(actionvalue):
    base = _z(actionvalue, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z actionvalue
def ca_f94_capital_actions_z_63d_accel_v139_signal(actionvalue):
    base = _z(actionvalue, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z actionvalue
def ca_f94_capital_actions_z_63d_accel_v140_signal(actionvalue):
    base = _z(actionvalue, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z actionvalue
def ca_f94_capital_actions_z_63d_accel_v141_signal(actionvalue):
    base = _z(actionvalue, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z actionvalue
def ca_f94_capital_actions_z_126d_accel_v142_signal(actionvalue):
    base = _z(actionvalue, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z actionvalue
def ca_f94_capital_actions_z_126d_accel_v143_signal(actionvalue):
    base = _z(actionvalue, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z actionvalue
def ca_f94_capital_actions_z_126d_accel_v144_signal(actionvalue):
    base = _z(actionvalue, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z actionvalue
def ca_f94_capital_actions_z_252d_accel_v145_signal(actionvalue):
    base = _z(actionvalue, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z actionvalue
def ca_f94_capital_actions_z_252d_accel_v146_signal(actionvalue):
    base = _z(actionvalue, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z actionvalue
def ca_f94_capital_actions_z_252d_accel_v147_signal(actionvalue):
    base = _z(actionvalue, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z actionvalue
def ca_f94_capital_actions_z_504d_accel_v148_signal(actionvalue):
    base = _z(actionvalue, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z actionvalue
def ca_f94_capital_actions_z_504d_accel_v149_signal(actionvalue):
    base = _z(actionvalue, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z actionvalue
def ca_f94_capital_actions_z_504d_accel_v150_signal(actionvalue):
    base = _z(actionvalue, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
