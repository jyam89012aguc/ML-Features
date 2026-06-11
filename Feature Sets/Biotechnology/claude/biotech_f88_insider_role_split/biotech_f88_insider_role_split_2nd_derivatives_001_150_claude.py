"""Family f88 - Role-split activity  (O_Insider_SF2) | 2nd derivatives 001-150"""
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
def _insider_role_split_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_role_split_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_role_split_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw transactionvalue
def irs_f88_insider_role_split_raw_21d_slope_v001_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw transactionvalue
def irs_f88_insider_role_split_raw_21d_slope_v002_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw transactionvalue
def irs_f88_insider_role_split_raw_21d_slope_v003_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw transactionvalue
def irs_f88_insider_role_split_raw_63d_slope_v004_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw transactionvalue
def irs_f88_insider_role_split_raw_63d_slope_v005_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw transactionvalue
def irs_f88_insider_role_split_raw_63d_slope_v006_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw transactionvalue
def irs_f88_insider_role_split_raw_126d_slope_v007_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw transactionvalue
def irs_f88_insider_role_split_raw_126d_slope_v008_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw transactionvalue
def irs_f88_insider_role_split_raw_126d_slope_v009_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw transactionvalue
def irs_f88_insider_role_split_raw_252d_slope_v010_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw transactionvalue
def irs_f88_insider_role_split_raw_252d_slope_v011_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw transactionvalue
def irs_f88_insider_role_split_raw_252d_slope_v012_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw transactionvalue
def irs_f88_insider_role_split_raw_504d_slope_v013_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw transactionvalue
def irs_f88_insider_role_split_raw_504d_slope_v014_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw transactionvalue
def irs_f88_insider_role_split_raw_504d_slope_v015_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log transactionvalue
def irs_f88_insider_role_split_log_21d_slope_v016_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log transactionvalue
def irs_f88_insider_role_split_log_21d_slope_v017_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log transactionvalue
def irs_f88_insider_role_split_log_21d_slope_v018_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log transactionvalue
def irs_f88_insider_role_split_log_63d_slope_v019_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log transactionvalue
def irs_f88_insider_role_split_log_63d_slope_v020_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log transactionvalue
def irs_f88_insider_role_split_log_63d_slope_v021_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log transactionvalue
def irs_f88_insider_role_split_log_126d_slope_v022_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log transactionvalue
def irs_f88_insider_role_split_log_126d_slope_v023_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log transactionvalue
def irs_f88_insider_role_split_log_126d_slope_v024_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log transactionvalue
def irs_f88_insider_role_split_log_252d_slope_v025_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log transactionvalue
def irs_f88_insider_role_split_log_252d_slope_v026_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log transactionvalue
def irs_f88_insider_role_split_log_252d_slope_v027_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log transactionvalue
def irs_f88_insider_role_split_log_504d_slope_v028_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log transactionvalue
def irs_f88_insider_role_split_log_504d_slope_v029_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log transactionvalue
def irs_f88_insider_role_split_log_504d_slope_v030_signal(transactionvalue, closeadj):
    base = _mean(_insider_role_split_log(transactionvalue), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare transactionvalue
def irs_f88_insider_role_split_pershare_21d_slope_v031_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare transactionvalue
def irs_f88_insider_role_split_pershare_21d_slope_v032_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare transactionvalue
def irs_f88_insider_role_split_pershare_21d_slope_v033_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare transactionvalue
def irs_f88_insider_role_split_pershare_63d_slope_v034_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare transactionvalue
def irs_f88_insider_role_split_pershare_63d_slope_v035_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare transactionvalue
def irs_f88_insider_role_split_pershare_63d_slope_v036_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare transactionvalue
def irs_f88_insider_role_split_pershare_126d_slope_v037_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare transactionvalue
def irs_f88_insider_role_split_pershare_126d_slope_v038_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare transactionvalue
def irs_f88_insider_role_split_pershare_126d_slope_v039_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare transactionvalue
def irs_f88_insider_role_split_pershare_252d_slope_v040_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare transactionvalue
def irs_f88_insider_role_split_pershare_252d_slope_v041_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare transactionvalue
def irs_f88_insider_role_split_pershare_252d_slope_v042_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare transactionvalue
def irs_f88_insider_role_split_pershare_504d_slope_v043_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare transactionvalue
def irs_f88_insider_role_split_pershare_504d_slope_v044_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare transactionvalue
def irs_f88_insider_role_split_pershare_504d_slope_v045_signal(transactionvalue, sharesbas, closeadj):
    base = _mean(_insider_role_split_per_share(transactionvalue, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_21d_slope_v046_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_21d_slope_v047_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_21d_slope_v048_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_63d_slope_v049_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_63d_slope_v050_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_63d_slope_v051_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_126d_slope_v052_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_126d_slope_v053_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_126d_slope_v054_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_252d_slope_v055_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_252d_slope_v056_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_252d_slope_v057_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_504d_slope_v058_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_504d_slope_v059_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets transactionvalue
def irs_f88_insider_role_split_per_assets_504d_slope_v060_signal(transactionvalue, assets):
    base = _mean(_insider_role_split_scaled(transactionvalue, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_21d_slope_v061_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_21d_slope_v062_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_21d_slope_v063_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_63d_slope_v064_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_63d_slope_v065_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_63d_slope_v066_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_126d_slope_v067_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_126d_slope_v068_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_126d_slope_v069_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_252d_slope_v070_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_252d_slope_v071_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_252d_slope_v072_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_504d_slope_v073_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_504d_slope_v074_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap transactionvalue
def irs_f88_insider_role_split_per_marketcap_504d_slope_v075_signal(transactionvalue, marketcap):
    base = _mean(_insider_role_split_scaled(transactionvalue, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_21d_slope_v076_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_21d_slope_v077_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_21d_slope_v078_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_63d_slope_v079_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_63d_slope_v080_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_63d_slope_v081_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_126d_slope_v082_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_126d_slope_v083_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_126d_slope_v084_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_252d_slope_v085_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_252d_slope_v086_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_252d_slope_v087_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_504d_slope_v088_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_504d_slope_v089_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity transactionvalue
def irs_f88_insider_role_split_per_equity_504d_slope_v090_signal(transactionvalue, equity):
    base = _mean(_insider_role_split_scaled(transactionvalue, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std transactionvalue
def irs_f88_insider_role_split_std_21d_slope_v091_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std transactionvalue
def irs_f88_insider_role_split_std_21d_slope_v092_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std transactionvalue
def irs_f88_insider_role_split_std_21d_slope_v093_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std transactionvalue
def irs_f88_insider_role_split_std_63d_slope_v094_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std transactionvalue
def irs_f88_insider_role_split_std_63d_slope_v095_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std transactionvalue
def irs_f88_insider_role_split_std_63d_slope_v096_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std transactionvalue
def irs_f88_insider_role_split_std_126d_slope_v097_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std transactionvalue
def irs_f88_insider_role_split_std_126d_slope_v098_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std transactionvalue
def irs_f88_insider_role_split_std_126d_slope_v099_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std transactionvalue
def irs_f88_insider_role_split_std_252d_slope_v100_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std transactionvalue
def irs_f88_insider_role_split_std_252d_slope_v101_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std transactionvalue
def irs_f88_insider_role_split_std_252d_slope_v102_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std transactionvalue
def irs_f88_insider_role_split_std_504d_slope_v103_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std transactionvalue
def irs_f88_insider_role_split_std_504d_slope_v104_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std transactionvalue
def irs_f88_insider_role_split_std_504d_slope_v105_signal(transactionvalue, closeadj):
    base = _std(transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm transactionvalue
def irs_f88_insider_role_split_ewm_21d_slope_v106_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm transactionvalue
def irs_f88_insider_role_split_ewm_21d_slope_v107_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm transactionvalue
def irs_f88_insider_role_split_ewm_21d_slope_v108_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm transactionvalue
def irs_f88_insider_role_split_ewm_63d_slope_v109_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm transactionvalue
def irs_f88_insider_role_split_ewm_63d_slope_v110_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm transactionvalue
def irs_f88_insider_role_split_ewm_63d_slope_v111_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm transactionvalue
def irs_f88_insider_role_split_ewm_126d_slope_v112_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm transactionvalue
def irs_f88_insider_role_split_ewm_126d_slope_v113_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm transactionvalue
def irs_f88_insider_role_split_ewm_126d_slope_v114_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm transactionvalue
def irs_f88_insider_role_split_ewm_252d_slope_v115_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm transactionvalue
def irs_f88_insider_role_split_ewm_252d_slope_v116_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm transactionvalue
def irs_f88_insider_role_split_ewm_252d_slope_v117_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm transactionvalue
def irs_f88_insider_role_split_ewm_504d_slope_v118_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm transactionvalue
def irs_f88_insider_role_split_ewm_504d_slope_v119_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm transactionvalue
def irs_f88_insider_role_split_ewm_504d_slope_v120_signal(transactionvalue, closeadj):
    base = transactionvalue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq transactionvalue
def irs_f88_insider_role_split_sq_21d_slope_v121_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq transactionvalue
def irs_f88_insider_role_split_sq_21d_slope_v122_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq transactionvalue
def irs_f88_insider_role_split_sq_21d_slope_v123_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq transactionvalue
def irs_f88_insider_role_split_sq_63d_slope_v124_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq transactionvalue
def irs_f88_insider_role_split_sq_63d_slope_v125_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq transactionvalue
def irs_f88_insider_role_split_sq_63d_slope_v126_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq transactionvalue
def irs_f88_insider_role_split_sq_126d_slope_v127_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq transactionvalue
def irs_f88_insider_role_split_sq_126d_slope_v128_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq transactionvalue
def irs_f88_insider_role_split_sq_126d_slope_v129_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq transactionvalue
def irs_f88_insider_role_split_sq_252d_slope_v130_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq transactionvalue
def irs_f88_insider_role_split_sq_252d_slope_v131_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq transactionvalue
def irs_f88_insider_role_split_sq_252d_slope_v132_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq transactionvalue
def irs_f88_insider_role_split_sq_504d_slope_v133_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq transactionvalue
def irs_f88_insider_role_split_sq_504d_slope_v134_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq transactionvalue
def irs_f88_insider_role_split_sq_504d_slope_v135_signal(transactionvalue, closeadj):
    base = _mean(transactionvalue * transactionvalue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z transactionvalue
def irs_f88_insider_role_split_z_21d_slope_v136_signal(transactionvalue):
    base = _z(transactionvalue, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z transactionvalue
def irs_f88_insider_role_split_z_21d_slope_v137_signal(transactionvalue):
    base = _z(transactionvalue, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z transactionvalue
def irs_f88_insider_role_split_z_21d_slope_v138_signal(transactionvalue):
    base = _z(transactionvalue, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z transactionvalue
def irs_f88_insider_role_split_z_63d_slope_v139_signal(transactionvalue):
    base = _z(transactionvalue, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z transactionvalue
def irs_f88_insider_role_split_z_63d_slope_v140_signal(transactionvalue):
    base = _z(transactionvalue, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z transactionvalue
def irs_f88_insider_role_split_z_63d_slope_v141_signal(transactionvalue):
    base = _z(transactionvalue, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z transactionvalue
def irs_f88_insider_role_split_z_126d_slope_v142_signal(transactionvalue):
    base = _z(transactionvalue, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z transactionvalue
def irs_f88_insider_role_split_z_126d_slope_v143_signal(transactionvalue):
    base = _z(transactionvalue, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z transactionvalue
def irs_f88_insider_role_split_z_126d_slope_v144_signal(transactionvalue):
    base = _z(transactionvalue, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z transactionvalue
def irs_f88_insider_role_split_z_252d_slope_v145_signal(transactionvalue):
    base = _z(transactionvalue, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z transactionvalue
def irs_f88_insider_role_split_z_252d_slope_v146_signal(transactionvalue):
    base = _z(transactionvalue, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z transactionvalue
def irs_f88_insider_role_split_z_252d_slope_v147_signal(transactionvalue):
    base = _z(transactionvalue, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z transactionvalue
def irs_f88_insider_role_split_z_504d_slope_v148_signal(transactionvalue):
    base = _z(transactionvalue, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z transactionvalue
def irs_f88_insider_role_split_z_504d_slope_v149_signal(transactionvalue):
    base = _z(transactionvalue, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z transactionvalue
def irs_f88_insider_role_split_z_504d_slope_v150_signal(transactionvalue):
    base = _z(transactionvalue, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
