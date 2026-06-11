"""Family f49 - Operating margin  (H_Margins) | 3rd derivatives 001-150"""
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
def _operating_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _operating_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _operating_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw opinc
def om_f49_operating_margin_raw_21d_accel_v001_signal(opinc, closeadj):
    base = _mean(opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw opinc
def om_f49_operating_margin_raw_21d_accel_v002_signal(opinc, closeadj):
    base = _mean(opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw opinc
def om_f49_operating_margin_raw_21d_accel_v003_signal(opinc, closeadj):
    base = _mean(opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw opinc
def om_f49_operating_margin_raw_63d_accel_v004_signal(opinc, closeadj):
    base = _mean(opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw opinc
def om_f49_operating_margin_raw_63d_accel_v005_signal(opinc, closeadj):
    base = _mean(opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw opinc
def om_f49_operating_margin_raw_63d_accel_v006_signal(opinc, closeadj):
    base = _mean(opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw opinc
def om_f49_operating_margin_raw_126d_accel_v007_signal(opinc, closeadj):
    base = _mean(opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw opinc
def om_f49_operating_margin_raw_126d_accel_v008_signal(opinc, closeadj):
    base = _mean(opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw opinc
def om_f49_operating_margin_raw_126d_accel_v009_signal(opinc, closeadj):
    base = _mean(opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw opinc
def om_f49_operating_margin_raw_252d_accel_v010_signal(opinc, closeadj):
    base = _mean(opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw opinc
def om_f49_operating_margin_raw_252d_accel_v011_signal(opinc, closeadj):
    base = _mean(opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw opinc
def om_f49_operating_margin_raw_252d_accel_v012_signal(opinc, closeadj):
    base = _mean(opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw opinc
def om_f49_operating_margin_raw_504d_accel_v013_signal(opinc, closeadj):
    base = _mean(opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw opinc
def om_f49_operating_margin_raw_504d_accel_v014_signal(opinc, closeadj):
    base = _mean(opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw opinc
def om_f49_operating_margin_raw_504d_accel_v015_signal(opinc, closeadj):
    base = _mean(opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log opinc
def om_f49_operating_margin_log_21d_accel_v016_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log opinc
def om_f49_operating_margin_log_21d_accel_v017_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log opinc
def om_f49_operating_margin_log_21d_accel_v018_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log opinc
def om_f49_operating_margin_log_63d_accel_v019_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log opinc
def om_f49_operating_margin_log_63d_accel_v020_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log opinc
def om_f49_operating_margin_log_63d_accel_v021_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log opinc
def om_f49_operating_margin_log_126d_accel_v022_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log opinc
def om_f49_operating_margin_log_126d_accel_v023_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log opinc
def om_f49_operating_margin_log_126d_accel_v024_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log opinc
def om_f49_operating_margin_log_252d_accel_v025_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log opinc
def om_f49_operating_margin_log_252d_accel_v026_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log opinc
def om_f49_operating_margin_log_252d_accel_v027_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log opinc
def om_f49_operating_margin_log_504d_accel_v028_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log opinc
def om_f49_operating_margin_log_504d_accel_v029_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log opinc
def om_f49_operating_margin_log_504d_accel_v030_signal(opinc, closeadj):
    base = _mean(_operating_margin_log(opinc), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare opinc
def om_f49_operating_margin_pershare_21d_accel_v031_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare opinc
def om_f49_operating_margin_pershare_21d_accel_v032_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare opinc
def om_f49_operating_margin_pershare_21d_accel_v033_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare opinc
def om_f49_operating_margin_pershare_63d_accel_v034_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare opinc
def om_f49_operating_margin_pershare_63d_accel_v035_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare opinc
def om_f49_operating_margin_pershare_63d_accel_v036_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare opinc
def om_f49_operating_margin_pershare_126d_accel_v037_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare opinc
def om_f49_operating_margin_pershare_126d_accel_v038_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare opinc
def om_f49_operating_margin_pershare_126d_accel_v039_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare opinc
def om_f49_operating_margin_pershare_252d_accel_v040_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare opinc
def om_f49_operating_margin_pershare_252d_accel_v041_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare opinc
def om_f49_operating_margin_pershare_252d_accel_v042_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare opinc
def om_f49_operating_margin_pershare_504d_accel_v043_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare opinc
def om_f49_operating_margin_pershare_504d_accel_v044_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare opinc
def om_f49_operating_margin_pershare_504d_accel_v045_signal(opinc, sharesbas, closeadj):
    base = _mean(_operating_margin_per_share(opinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets opinc
def om_f49_operating_margin_per_assets_21d_accel_v046_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets opinc
def om_f49_operating_margin_per_assets_21d_accel_v047_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets opinc
def om_f49_operating_margin_per_assets_21d_accel_v048_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets opinc
def om_f49_operating_margin_per_assets_63d_accel_v049_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets opinc
def om_f49_operating_margin_per_assets_63d_accel_v050_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets opinc
def om_f49_operating_margin_per_assets_63d_accel_v051_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets opinc
def om_f49_operating_margin_per_assets_126d_accel_v052_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets opinc
def om_f49_operating_margin_per_assets_126d_accel_v053_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets opinc
def om_f49_operating_margin_per_assets_126d_accel_v054_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets opinc
def om_f49_operating_margin_per_assets_252d_accel_v055_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets opinc
def om_f49_operating_margin_per_assets_252d_accel_v056_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets opinc
def om_f49_operating_margin_per_assets_252d_accel_v057_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets opinc
def om_f49_operating_margin_per_assets_504d_accel_v058_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets opinc
def om_f49_operating_margin_per_assets_504d_accel_v059_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets opinc
def om_f49_operating_margin_per_assets_504d_accel_v060_signal(opinc, assets):
    base = _mean(_operating_margin_scaled(opinc, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_21d_accel_v061_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_21d_accel_v062_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_21d_accel_v063_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_63d_accel_v064_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_63d_accel_v065_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_63d_accel_v066_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_126d_accel_v067_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_126d_accel_v068_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_126d_accel_v069_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_252d_accel_v070_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_252d_accel_v071_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_252d_accel_v072_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_504d_accel_v073_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_504d_accel_v074_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap opinc
def om_f49_operating_margin_per_marketcap_504d_accel_v075_signal(opinc, marketcap):
    base = _mean(_operating_margin_scaled(opinc, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity opinc
def om_f49_operating_margin_per_equity_21d_accel_v076_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity opinc
def om_f49_operating_margin_per_equity_21d_accel_v077_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity opinc
def om_f49_operating_margin_per_equity_21d_accel_v078_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity opinc
def om_f49_operating_margin_per_equity_63d_accel_v079_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity opinc
def om_f49_operating_margin_per_equity_63d_accel_v080_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity opinc
def om_f49_operating_margin_per_equity_63d_accel_v081_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity opinc
def om_f49_operating_margin_per_equity_126d_accel_v082_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity opinc
def om_f49_operating_margin_per_equity_126d_accel_v083_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity opinc
def om_f49_operating_margin_per_equity_126d_accel_v084_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity opinc
def om_f49_operating_margin_per_equity_252d_accel_v085_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity opinc
def om_f49_operating_margin_per_equity_252d_accel_v086_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity opinc
def om_f49_operating_margin_per_equity_252d_accel_v087_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity opinc
def om_f49_operating_margin_per_equity_504d_accel_v088_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity opinc
def om_f49_operating_margin_per_equity_504d_accel_v089_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity opinc
def om_f49_operating_margin_per_equity_504d_accel_v090_signal(opinc, equity):
    base = _mean(_operating_margin_scaled(opinc, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std opinc
def om_f49_operating_margin_std_21d_accel_v091_signal(opinc, closeadj):
    base = _std(opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std opinc
def om_f49_operating_margin_std_21d_accel_v092_signal(opinc, closeadj):
    base = _std(opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std opinc
def om_f49_operating_margin_std_21d_accel_v093_signal(opinc, closeadj):
    base = _std(opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std opinc
def om_f49_operating_margin_std_63d_accel_v094_signal(opinc, closeadj):
    base = _std(opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std opinc
def om_f49_operating_margin_std_63d_accel_v095_signal(opinc, closeadj):
    base = _std(opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std opinc
def om_f49_operating_margin_std_63d_accel_v096_signal(opinc, closeadj):
    base = _std(opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std opinc
def om_f49_operating_margin_std_126d_accel_v097_signal(opinc, closeadj):
    base = _std(opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std opinc
def om_f49_operating_margin_std_126d_accel_v098_signal(opinc, closeadj):
    base = _std(opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std opinc
def om_f49_operating_margin_std_126d_accel_v099_signal(opinc, closeadj):
    base = _std(opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std opinc
def om_f49_operating_margin_std_252d_accel_v100_signal(opinc, closeadj):
    base = _std(opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std opinc
def om_f49_operating_margin_std_252d_accel_v101_signal(opinc, closeadj):
    base = _std(opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std opinc
def om_f49_operating_margin_std_252d_accel_v102_signal(opinc, closeadj):
    base = _std(opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std opinc
def om_f49_operating_margin_std_504d_accel_v103_signal(opinc, closeadj):
    base = _std(opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std opinc
def om_f49_operating_margin_std_504d_accel_v104_signal(opinc, closeadj):
    base = _std(opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std opinc
def om_f49_operating_margin_std_504d_accel_v105_signal(opinc, closeadj):
    base = _std(opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm opinc
def om_f49_operating_margin_ewm_21d_accel_v106_signal(opinc, closeadj):
    base = opinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm opinc
def om_f49_operating_margin_ewm_21d_accel_v107_signal(opinc, closeadj):
    base = opinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm opinc
def om_f49_operating_margin_ewm_21d_accel_v108_signal(opinc, closeadj):
    base = opinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm opinc
def om_f49_operating_margin_ewm_63d_accel_v109_signal(opinc, closeadj):
    base = opinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm opinc
def om_f49_operating_margin_ewm_63d_accel_v110_signal(opinc, closeadj):
    base = opinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm opinc
def om_f49_operating_margin_ewm_63d_accel_v111_signal(opinc, closeadj):
    base = opinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm opinc
def om_f49_operating_margin_ewm_126d_accel_v112_signal(opinc, closeadj):
    base = opinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm opinc
def om_f49_operating_margin_ewm_126d_accel_v113_signal(opinc, closeadj):
    base = opinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm opinc
def om_f49_operating_margin_ewm_126d_accel_v114_signal(opinc, closeadj):
    base = opinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm opinc
def om_f49_operating_margin_ewm_252d_accel_v115_signal(opinc, closeadj):
    base = opinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm opinc
def om_f49_operating_margin_ewm_252d_accel_v116_signal(opinc, closeadj):
    base = opinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm opinc
def om_f49_operating_margin_ewm_252d_accel_v117_signal(opinc, closeadj):
    base = opinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm opinc
def om_f49_operating_margin_ewm_504d_accel_v118_signal(opinc, closeadj):
    base = opinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm opinc
def om_f49_operating_margin_ewm_504d_accel_v119_signal(opinc, closeadj):
    base = opinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm opinc
def om_f49_operating_margin_ewm_504d_accel_v120_signal(opinc, closeadj):
    base = opinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq opinc
def om_f49_operating_margin_sq_21d_accel_v121_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq opinc
def om_f49_operating_margin_sq_21d_accel_v122_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq opinc
def om_f49_operating_margin_sq_21d_accel_v123_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq opinc
def om_f49_operating_margin_sq_63d_accel_v124_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq opinc
def om_f49_operating_margin_sq_63d_accel_v125_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq opinc
def om_f49_operating_margin_sq_63d_accel_v126_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq opinc
def om_f49_operating_margin_sq_126d_accel_v127_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq opinc
def om_f49_operating_margin_sq_126d_accel_v128_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq opinc
def om_f49_operating_margin_sq_126d_accel_v129_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq opinc
def om_f49_operating_margin_sq_252d_accel_v130_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq opinc
def om_f49_operating_margin_sq_252d_accel_v131_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq opinc
def om_f49_operating_margin_sq_252d_accel_v132_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq opinc
def om_f49_operating_margin_sq_504d_accel_v133_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq opinc
def om_f49_operating_margin_sq_504d_accel_v134_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq opinc
def om_f49_operating_margin_sq_504d_accel_v135_signal(opinc, closeadj):
    base = _mean(opinc * opinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z opinc
def om_f49_operating_margin_z_21d_accel_v136_signal(opinc):
    base = _z(opinc, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z opinc
def om_f49_operating_margin_z_21d_accel_v137_signal(opinc):
    base = _z(opinc, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z opinc
def om_f49_operating_margin_z_21d_accel_v138_signal(opinc):
    base = _z(opinc, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z opinc
def om_f49_operating_margin_z_63d_accel_v139_signal(opinc):
    base = _z(opinc, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z opinc
def om_f49_operating_margin_z_63d_accel_v140_signal(opinc):
    base = _z(opinc, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z opinc
def om_f49_operating_margin_z_63d_accel_v141_signal(opinc):
    base = _z(opinc, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z opinc
def om_f49_operating_margin_z_126d_accel_v142_signal(opinc):
    base = _z(opinc, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z opinc
def om_f49_operating_margin_z_126d_accel_v143_signal(opinc):
    base = _z(opinc, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z opinc
def om_f49_operating_margin_z_126d_accel_v144_signal(opinc):
    base = _z(opinc, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z opinc
def om_f49_operating_margin_z_252d_accel_v145_signal(opinc):
    base = _z(opinc, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z opinc
def om_f49_operating_margin_z_252d_accel_v146_signal(opinc):
    base = _z(opinc, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z opinc
def om_f49_operating_margin_z_252d_accel_v147_signal(opinc):
    base = _z(opinc, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z opinc
def om_f49_operating_margin_z_504d_accel_v148_signal(opinc):
    base = _z(opinc, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z opinc
def om_f49_operating_margin_z_504d_accel_v149_signal(opinc):
    base = _z(opinc, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z opinc
def om_f49_operating_margin_z_504d_accel_v150_signal(opinc):
    base = _z(opinc, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
