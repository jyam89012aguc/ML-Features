"""Family f23 - Net debt & leverage  (D_Capital_Debt) | 2nd derivatives 001-150"""
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
def _net_debt_leverage_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _net_debt_leverage_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _net_debt_leverage_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw debt
def ndl_f23_net_debt_leverage_raw_21d_slope_v001_signal(debt, closeadj):
    base = _mean(debt, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw debt
def ndl_f23_net_debt_leverage_raw_21d_slope_v002_signal(debt, closeadj):
    base = _mean(debt, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw debt
def ndl_f23_net_debt_leverage_raw_21d_slope_v003_signal(debt, closeadj):
    base = _mean(debt, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw debt
def ndl_f23_net_debt_leverage_raw_63d_slope_v004_signal(debt, closeadj):
    base = _mean(debt, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw debt
def ndl_f23_net_debt_leverage_raw_63d_slope_v005_signal(debt, closeadj):
    base = _mean(debt, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw debt
def ndl_f23_net_debt_leverage_raw_63d_slope_v006_signal(debt, closeadj):
    base = _mean(debt, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw debt
def ndl_f23_net_debt_leverage_raw_126d_slope_v007_signal(debt, closeadj):
    base = _mean(debt, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw debt
def ndl_f23_net_debt_leverage_raw_126d_slope_v008_signal(debt, closeadj):
    base = _mean(debt, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw debt
def ndl_f23_net_debt_leverage_raw_126d_slope_v009_signal(debt, closeadj):
    base = _mean(debt, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw debt
def ndl_f23_net_debt_leverage_raw_252d_slope_v010_signal(debt, closeadj):
    base = _mean(debt, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw debt
def ndl_f23_net_debt_leverage_raw_252d_slope_v011_signal(debt, closeadj):
    base = _mean(debt, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw debt
def ndl_f23_net_debt_leverage_raw_252d_slope_v012_signal(debt, closeadj):
    base = _mean(debt, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw debt
def ndl_f23_net_debt_leverage_raw_504d_slope_v013_signal(debt, closeadj):
    base = _mean(debt, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw debt
def ndl_f23_net_debt_leverage_raw_504d_slope_v014_signal(debt, closeadj):
    base = _mean(debt, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw debt
def ndl_f23_net_debt_leverage_raw_504d_slope_v015_signal(debt, closeadj):
    base = _mean(debt, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log debt
def ndl_f23_net_debt_leverage_log_21d_slope_v016_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log debt
def ndl_f23_net_debt_leverage_log_21d_slope_v017_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log debt
def ndl_f23_net_debt_leverage_log_21d_slope_v018_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log debt
def ndl_f23_net_debt_leverage_log_63d_slope_v019_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log debt
def ndl_f23_net_debt_leverage_log_63d_slope_v020_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log debt
def ndl_f23_net_debt_leverage_log_63d_slope_v021_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log debt
def ndl_f23_net_debt_leverage_log_126d_slope_v022_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log debt
def ndl_f23_net_debt_leverage_log_126d_slope_v023_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log debt
def ndl_f23_net_debt_leverage_log_126d_slope_v024_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log debt
def ndl_f23_net_debt_leverage_log_252d_slope_v025_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log debt
def ndl_f23_net_debt_leverage_log_252d_slope_v026_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log debt
def ndl_f23_net_debt_leverage_log_252d_slope_v027_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log debt
def ndl_f23_net_debt_leverage_log_504d_slope_v028_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log debt
def ndl_f23_net_debt_leverage_log_504d_slope_v029_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log debt
def ndl_f23_net_debt_leverage_log_504d_slope_v030_signal(debt, closeadj):
    base = _mean(_net_debt_leverage_log(debt), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare debt
def ndl_f23_net_debt_leverage_pershare_21d_slope_v031_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare debt
def ndl_f23_net_debt_leverage_pershare_21d_slope_v032_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare debt
def ndl_f23_net_debt_leverage_pershare_21d_slope_v033_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare debt
def ndl_f23_net_debt_leverage_pershare_63d_slope_v034_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare debt
def ndl_f23_net_debt_leverage_pershare_63d_slope_v035_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare debt
def ndl_f23_net_debt_leverage_pershare_63d_slope_v036_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare debt
def ndl_f23_net_debt_leverage_pershare_126d_slope_v037_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare debt
def ndl_f23_net_debt_leverage_pershare_126d_slope_v038_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare debt
def ndl_f23_net_debt_leverage_pershare_126d_slope_v039_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare debt
def ndl_f23_net_debt_leverage_pershare_252d_slope_v040_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare debt
def ndl_f23_net_debt_leverage_pershare_252d_slope_v041_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare debt
def ndl_f23_net_debt_leverage_pershare_252d_slope_v042_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare debt
def ndl_f23_net_debt_leverage_pershare_504d_slope_v043_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare debt
def ndl_f23_net_debt_leverage_pershare_504d_slope_v044_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare debt
def ndl_f23_net_debt_leverage_pershare_504d_slope_v045_signal(debt, sharesbas, closeadj):
    base = _mean(_net_debt_leverage_per_share(debt, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_21d_slope_v046_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_21d_slope_v047_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_21d_slope_v048_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_63d_slope_v049_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_63d_slope_v050_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_63d_slope_v051_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_126d_slope_v052_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_126d_slope_v053_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_126d_slope_v054_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_252d_slope_v055_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_252d_slope_v056_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_252d_slope_v057_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_504d_slope_v058_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_504d_slope_v059_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets debt
def ndl_f23_net_debt_leverage_per_assets_504d_slope_v060_signal(debt, assets):
    base = _mean(_net_debt_leverage_scaled(debt, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_21d_slope_v061_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_21d_slope_v062_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_21d_slope_v063_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_63d_slope_v064_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_63d_slope_v065_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_63d_slope_v066_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_126d_slope_v067_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_126d_slope_v068_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_126d_slope_v069_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_252d_slope_v070_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_252d_slope_v071_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_252d_slope_v072_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_504d_slope_v073_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_504d_slope_v074_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap debt
def ndl_f23_net_debt_leverage_per_marketcap_504d_slope_v075_signal(debt, marketcap):
    base = _mean(_net_debt_leverage_scaled(debt, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_21d_slope_v076_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_21d_slope_v077_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_21d_slope_v078_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_63d_slope_v079_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_63d_slope_v080_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_63d_slope_v081_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_126d_slope_v082_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_126d_slope_v083_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_126d_slope_v084_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_252d_slope_v085_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_252d_slope_v086_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_252d_slope_v087_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_504d_slope_v088_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_504d_slope_v089_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity debt
def ndl_f23_net_debt_leverage_per_equity_504d_slope_v090_signal(debt, equity):
    base = _mean(_net_debt_leverage_scaled(debt, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std debt
def ndl_f23_net_debt_leverage_std_21d_slope_v091_signal(debt, closeadj):
    base = _std(debt, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std debt
def ndl_f23_net_debt_leverage_std_21d_slope_v092_signal(debt, closeadj):
    base = _std(debt, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std debt
def ndl_f23_net_debt_leverage_std_21d_slope_v093_signal(debt, closeadj):
    base = _std(debt, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std debt
def ndl_f23_net_debt_leverage_std_63d_slope_v094_signal(debt, closeadj):
    base = _std(debt, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std debt
def ndl_f23_net_debt_leverage_std_63d_slope_v095_signal(debt, closeadj):
    base = _std(debt, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std debt
def ndl_f23_net_debt_leverage_std_63d_slope_v096_signal(debt, closeadj):
    base = _std(debt, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std debt
def ndl_f23_net_debt_leverage_std_126d_slope_v097_signal(debt, closeadj):
    base = _std(debt, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std debt
def ndl_f23_net_debt_leverage_std_126d_slope_v098_signal(debt, closeadj):
    base = _std(debt, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std debt
def ndl_f23_net_debt_leverage_std_126d_slope_v099_signal(debt, closeadj):
    base = _std(debt, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std debt
def ndl_f23_net_debt_leverage_std_252d_slope_v100_signal(debt, closeadj):
    base = _std(debt, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std debt
def ndl_f23_net_debt_leverage_std_252d_slope_v101_signal(debt, closeadj):
    base = _std(debt, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std debt
def ndl_f23_net_debt_leverage_std_252d_slope_v102_signal(debt, closeadj):
    base = _std(debt, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std debt
def ndl_f23_net_debt_leverage_std_504d_slope_v103_signal(debt, closeadj):
    base = _std(debt, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std debt
def ndl_f23_net_debt_leverage_std_504d_slope_v104_signal(debt, closeadj):
    base = _std(debt, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std debt
def ndl_f23_net_debt_leverage_std_504d_slope_v105_signal(debt, closeadj):
    base = _std(debt, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm debt
def ndl_f23_net_debt_leverage_ewm_21d_slope_v106_signal(debt, closeadj):
    base = debt.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm debt
def ndl_f23_net_debt_leverage_ewm_21d_slope_v107_signal(debt, closeadj):
    base = debt.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm debt
def ndl_f23_net_debt_leverage_ewm_21d_slope_v108_signal(debt, closeadj):
    base = debt.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm debt
def ndl_f23_net_debt_leverage_ewm_63d_slope_v109_signal(debt, closeadj):
    base = debt.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm debt
def ndl_f23_net_debt_leverage_ewm_63d_slope_v110_signal(debt, closeadj):
    base = debt.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm debt
def ndl_f23_net_debt_leverage_ewm_63d_slope_v111_signal(debt, closeadj):
    base = debt.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm debt
def ndl_f23_net_debt_leverage_ewm_126d_slope_v112_signal(debt, closeadj):
    base = debt.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm debt
def ndl_f23_net_debt_leverage_ewm_126d_slope_v113_signal(debt, closeadj):
    base = debt.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm debt
def ndl_f23_net_debt_leverage_ewm_126d_slope_v114_signal(debt, closeadj):
    base = debt.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm debt
def ndl_f23_net_debt_leverage_ewm_252d_slope_v115_signal(debt, closeadj):
    base = debt.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm debt
def ndl_f23_net_debt_leverage_ewm_252d_slope_v116_signal(debt, closeadj):
    base = debt.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm debt
def ndl_f23_net_debt_leverage_ewm_252d_slope_v117_signal(debt, closeadj):
    base = debt.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm debt
def ndl_f23_net_debt_leverage_ewm_504d_slope_v118_signal(debt, closeadj):
    base = debt.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm debt
def ndl_f23_net_debt_leverage_ewm_504d_slope_v119_signal(debt, closeadj):
    base = debt.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm debt
def ndl_f23_net_debt_leverage_ewm_504d_slope_v120_signal(debt, closeadj):
    base = debt.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq debt
def ndl_f23_net_debt_leverage_sq_21d_slope_v121_signal(debt, closeadj):
    base = _mean(debt * debt, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq debt
def ndl_f23_net_debt_leverage_sq_21d_slope_v122_signal(debt, closeadj):
    base = _mean(debt * debt, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq debt
def ndl_f23_net_debt_leverage_sq_21d_slope_v123_signal(debt, closeadj):
    base = _mean(debt * debt, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq debt
def ndl_f23_net_debt_leverage_sq_63d_slope_v124_signal(debt, closeadj):
    base = _mean(debt * debt, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq debt
def ndl_f23_net_debt_leverage_sq_63d_slope_v125_signal(debt, closeadj):
    base = _mean(debt * debt, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq debt
def ndl_f23_net_debt_leverage_sq_63d_slope_v126_signal(debt, closeadj):
    base = _mean(debt * debt, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq debt
def ndl_f23_net_debt_leverage_sq_126d_slope_v127_signal(debt, closeadj):
    base = _mean(debt * debt, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq debt
def ndl_f23_net_debt_leverage_sq_126d_slope_v128_signal(debt, closeadj):
    base = _mean(debt * debt, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq debt
def ndl_f23_net_debt_leverage_sq_126d_slope_v129_signal(debt, closeadj):
    base = _mean(debt * debt, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq debt
def ndl_f23_net_debt_leverage_sq_252d_slope_v130_signal(debt, closeadj):
    base = _mean(debt * debt, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq debt
def ndl_f23_net_debt_leverage_sq_252d_slope_v131_signal(debt, closeadj):
    base = _mean(debt * debt, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq debt
def ndl_f23_net_debt_leverage_sq_252d_slope_v132_signal(debt, closeadj):
    base = _mean(debt * debt, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq debt
def ndl_f23_net_debt_leverage_sq_504d_slope_v133_signal(debt, closeadj):
    base = _mean(debt * debt, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq debt
def ndl_f23_net_debt_leverage_sq_504d_slope_v134_signal(debt, closeadj):
    base = _mean(debt * debt, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq debt
def ndl_f23_net_debt_leverage_sq_504d_slope_v135_signal(debt, closeadj):
    base = _mean(debt * debt, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z debt
def ndl_f23_net_debt_leverage_z_21d_slope_v136_signal(debt):
    base = _z(debt, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z debt
def ndl_f23_net_debt_leverage_z_21d_slope_v137_signal(debt):
    base = _z(debt, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z debt
def ndl_f23_net_debt_leverage_z_21d_slope_v138_signal(debt):
    base = _z(debt, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z debt
def ndl_f23_net_debt_leverage_z_63d_slope_v139_signal(debt):
    base = _z(debt, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z debt
def ndl_f23_net_debt_leverage_z_63d_slope_v140_signal(debt):
    base = _z(debt, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z debt
def ndl_f23_net_debt_leverage_z_63d_slope_v141_signal(debt):
    base = _z(debt, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z debt
def ndl_f23_net_debt_leverage_z_126d_slope_v142_signal(debt):
    base = _z(debt, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z debt
def ndl_f23_net_debt_leverage_z_126d_slope_v143_signal(debt):
    base = _z(debt, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z debt
def ndl_f23_net_debt_leverage_z_126d_slope_v144_signal(debt):
    base = _z(debt, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z debt
def ndl_f23_net_debt_leverage_z_252d_slope_v145_signal(debt):
    base = _z(debt, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z debt
def ndl_f23_net_debt_leverage_z_252d_slope_v146_signal(debt):
    base = _z(debt, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z debt
def ndl_f23_net_debt_leverage_z_252d_slope_v147_signal(debt):
    base = _z(debt, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z debt
def ndl_f23_net_debt_leverage_z_504d_slope_v148_signal(debt):
    base = _z(debt, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z debt
def ndl_f23_net_debt_leverage_z_504d_slope_v149_signal(debt):
    base = _z(debt, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z debt
def ndl_f23_net_debt_leverage_z_504d_slope_v150_signal(debt):
    base = _z(debt, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
