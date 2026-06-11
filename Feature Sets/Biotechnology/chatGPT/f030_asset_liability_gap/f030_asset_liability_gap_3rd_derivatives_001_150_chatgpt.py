"""Family f030 - Asset-liability solvency gap (Capital Structure) | Sharadar tables: SF1 | fields: assets, liabilities, equity | 3rd derivatives 001-150"""
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
def _asset_liability_gap_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _asset_liability_gap_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _asset_liability_gap_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw assets
def alg_f030_asset_liability_gap_raw_21d_accel_v001_signal(assets, closeadj):
    base = _mean(assets, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw assets
def alg_f030_asset_liability_gap_raw_21d_accel_v002_signal(assets, closeadj):
    base = _mean(assets, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw assets
def alg_f030_asset_liability_gap_raw_21d_accel_v003_signal(assets, closeadj):
    base = _mean(assets, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw assets
def alg_f030_asset_liability_gap_raw_63d_accel_v004_signal(assets, closeadj):
    base = _mean(assets, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw assets
def alg_f030_asset_liability_gap_raw_63d_accel_v005_signal(assets, closeadj):
    base = _mean(assets, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw assets
def alg_f030_asset_liability_gap_raw_63d_accel_v006_signal(assets, closeadj):
    base = _mean(assets, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw assets
def alg_f030_asset_liability_gap_raw_126d_accel_v007_signal(assets, closeadj):
    base = _mean(assets, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw assets
def alg_f030_asset_liability_gap_raw_126d_accel_v008_signal(assets, closeadj):
    base = _mean(assets, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw assets
def alg_f030_asset_liability_gap_raw_126d_accel_v009_signal(assets, closeadj):
    base = _mean(assets, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw assets
def alg_f030_asset_liability_gap_raw_252d_accel_v010_signal(assets, closeadj):
    base = _mean(assets, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw assets
def alg_f030_asset_liability_gap_raw_252d_accel_v011_signal(assets, closeadj):
    base = _mean(assets, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw assets
def alg_f030_asset_liability_gap_raw_252d_accel_v012_signal(assets, closeadj):
    base = _mean(assets, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw assets
def alg_f030_asset_liability_gap_raw_504d_accel_v013_signal(assets, closeadj):
    base = _mean(assets, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw assets
def alg_f030_asset_liability_gap_raw_504d_accel_v014_signal(assets, closeadj):
    base = _mean(assets, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw assets
def alg_f030_asset_liability_gap_raw_504d_accel_v015_signal(assets, closeadj):
    base = _mean(assets, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log assets
def alg_f030_asset_liability_gap_log_21d_accel_v016_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log assets
def alg_f030_asset_liability_gap_log_21d_accel_v017_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log assets
def alg_f030_asset_liability_gap_log_21d_accel_v018_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log assets
def alg_f030_asset_liability_gap_log_63d_accel_v019_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log assets
def alg_f030_asset_liability_gap_log_63d_accel_v020_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log assets
def alg_f030_asset_liability_gap_log_63d_accel_v021_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log assets
def alg_f030_asset_liability_gap_log_126d_accel_v022_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log assets
def alg_f030_asset_liability_gap_log_126d_accel_v023_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log assets
def alg_f030_asset_liability_gap_log_126d_accel_v024_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log assets
def alg_f030_asset_liability_gap_log_252d_accel_v025_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log assets
def alg_f030_asset_liability_gap_log_252d_accel_v026_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log assets
def alg_f030_asset_liability_gap_log_252d_accel_v027_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log assets
def alg_f030_asset_liability_gap_log_504d_accel_v028_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log assets
def alg_f030_asset_liability_gap_log_504d_accel_v029_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log assets
def alg_f030_asset_liability_gap_log_504d_accel_v030_signal(assets, closeadj):
    base = _mean(_asset_liability_gap_log(assets), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare assets
def alg_f030_asset_liability_gap_pershare_21d_accel_v031_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare assets
def alg_f030_asset_liability_gap_pershare_21d_accel_v032_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare assets
def alg_f030_asset_liability_gap_pershare_21d_accel_v033_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare assets
def alg_f030_asset_liability_gap_pershare_63d_accel_v034_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare assets
def alg_f030_asset_liability_gap_pershare_63d_accel_v035_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare assets
def alg_f030_asset_liability_gap_pershare_63d_accel_v036_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare assets
def alg_f030_asset_liability_gap_pershare_126d_accel_v037_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare assets
def alg_f030_asset_liability_gap_pershare_126d_accel_v038_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare assets
def alg_f030_asset_liability_gap_pershare_126d_accel_v039_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare assets
def alg_f030_asset_liability_gap_pershare_252d_accel_v040_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare assets
def alg_f030_asset_liability_gap_pershare_252d_accel_v041_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare assets
def alg_f030_asset_liability_gap_pershare_252d_accel_v042_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare assets
def alg_f030_asset_liability_gap_pershare_504d_accel_v043_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare assets
def alg_f030_asset_liability_gap_pershare_504d_accel_v044_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare assets
def alg_f030_asset_liability_gap_pershare_504d_accel_v045_signal(assets, sharesbas, closeadj):
    base = _mean(_asset_liability_gap_per_share(assets, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity assets
def alg_f030_asset_liability_gap_per_equity_21d_accel_v046_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity assets
def alg_f030_asset_liability_gap_per_equity_21d_accel_v047_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity assets
def alg_f030_asset_liability_gap_per_equity_21d_accel_v048_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity assets
def alg_f030_asset_liability_gap_per_equity_63d_accel_v049_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity assets
def alg_f030_asset_liability_gap_per_equity_63d_accel_v050_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity assets
def alg_f030_asset_liability_gap_per_equity_63d_accel_v051_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity assets
def alg_f030_asset_liability_gap_per_equity_126d_accel_v052_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity assets
def alg_f030_asset_liability_gap_per_equity_126d_accel_v053_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity assets
def alg_f030_asset_liability_gap_per_equity_126d_accel_v054_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity assets
def alg_f030_asset_liability_gap_per_equity_252d_accel_v055_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity assets
def alg_f030_asset_liability_gap_per_equity_252d_accel_v056_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity assets
def alg_f030_asset_liability_gap_per_equity_252d_accel_v057_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity assets
def alg_f030_asset_liability_gap_per_equity_504d_accel_v058_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity assets
def alg_f030_asset_liability_gap_per_equity_504d_accel_v059_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity assets
def alg_f030_asset_liability_gap_per_equity_504d_accel_v060_signal(assets, equity):
    base = _mean(_asset_liability_gap_scaled(assets, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_21d_accel_v061_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_21d_accel_v062_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_21d_accel_v063_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_63d_accel_v064_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_63d_accel_v065_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_63d_accel_v066_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_126d_accel_v067_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_126d_accel_v068_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_126d_accel_v069_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_252d_accel_v070_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_252d_accel_v071_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_252d_accel_v072_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_504d_accel_v073_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_504d_accel_v074_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap assets
def alg_f030_asset_liability_gap_per_marketcap_504d_accel_v075_signal(assets, marketcap):
    base = _mean(_asset_liability_gap_scaled(assets, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_debt assets
def alg_f030_asset_liability_gap_per_debt_21d_accel_v076_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_debt assets
def alg_f030_asset_liability_gap_per_debt_21d_accel_v077_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_debt assets
def alg_f030_asset_liability_gap_per_debt_21d_accel_v078_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_debt assets
def alg_f030_asset_liability_gap_per_debt_63d_accel_v079_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_debt assets
def alg_f030_asset_liability_gap_per_debt_63d_accel_v080_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_debt assets
def alg_f030_asset_liability_gap_per_debt_63d_accel_v081_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_debt assets
def alg_f030_asset_liability_gap_per_debt_126d_accel_v082_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_debt assets
def alg_f030_asset_liability_gap_per_debt_126d_accel_v083_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_debt assets
def alg_f030_asset_liability_gap_per_debt_126d_accel_v084_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_debt assets
def alg_f030_asset_liability_gap_per_debt_252d_accel_v085_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_debt assets
def alg_f030_asset_liability_gap_per_debt_252d_accel_v086_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_debt assets
def alg_f030_asset_liability_gap_per_debt_252d_accel_v087_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_debt assets
def alg_f030_asset_liability_gap_per_debt_504d_accel_v088_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_debt assets
def alg_f030_asset_liability_gap_per_debt_504d_accel_v089_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_debt assets
def alg_f030_asset_liability_gap_per_debt_504d_accel_v090_signal(assets, debt):
    base = _mean(_asset_liability_gap_scaled(assets, debt), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std assets
def alg_f030_asset_liability_gap_std_21d_accel_v091_signal(assets, closeadj):
    base = _std(assets, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std assets
def alg_f030_asset_liability_gap_std_21d_accel_v092_signal(assets, closeadj):
    base = _std(assets, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std assets
def alg_f030_asset_liability_gap_std_21d_accel_v093_signal(assets, closeadj):
    base = _std(assets, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std assets
def alg_f030_asset_liability_gap_std_63d_accel_v094_signal(assets, closeadj):
    base = _std(assets, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std assets
def alg_f030_asset_liability_gap_std_63d_accel_v095_signal(assets, closeadj):
    base = _std(assets, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std assets
def alg_f030_asset_liability_gap_std_63d_accel_v096_signal(assets, closeadj):
    base = _std(assets, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std assets
def alg_f030_asset_liability_gap_std_126d_accel_v097_signal(assets, closeadj):
    base = _std(assets, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std assets
def alg_f030_asset_liability_gap_std_126d_accel_v098_signal(assets, closeadj):
    base = _std(assets, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std assets
def alg_f030_asset_liability_gap_std_126d_accel_v099_signal(assets, closeadj):
    base = _std(assets, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std assets
def alg_f030_asset_liability_gap_std_252d_accel_v100_signal(assets, closeadj):
    base = _std(assets, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std assets
def alg_f030_asset_liability_gap_std_252d_accel_v101_signal(assets, closeadj):
    base = _std(assets, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std assets
def alg_f030_asset_liability_gap_std_252d_accel_v102_signal(assets, closeadj):
    base = _std(assets, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std assets
def alg_f030_asset_liability_gap_std_504d_accel_v103_signal(assets, closeadj):
    base = _std(assets, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std assets
def alg_f030_asset_liability_gap_std_504d_accel_v104_signal(assets, closeadj):
    base = _std(assets, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std assets
def alg_f030_asset_liability_gap_std_504d_accel_v105_signal(assets, closeadj):
    base = _std(assets, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm assets
def alg_f030_asset_liability_gap_ewm_21d_accel_v106_signal(assets, closeadj):
    base = assets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm assets
def alg_f030_asset_liability_gap_ewm_21d_accel_v107_signal(assets, closeadj):
    base = assets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm assets
def alg_f030_asset_liability_gap_ewm_21d_accel_v108_signal(assets, closeadj):
    base = assets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm assets
def alg_f030_asset_liability_gap_ewm_63d_accel_v109_signal(assets, closeadj):
    base = assets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm assets
def alg_f030_asset_liability_gap_ewm_63d_accel_v110_signal(assets, closeadj):
    base = assets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm assets
def alg_f030_asset_liability_gap_ewm_63d_accel_v111_signal(assets, closeadj):
    base = assets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm assets
def alg_f030_asset_liability_gap_ewm_126d_accel_v112_signal(assets, closeadj):
    base = assets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm assets
def alg_f030_asset_liability_gap_ewm_126d_accel_v113_signal(assets, closeadj):
    base = assets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm assets
def alg_f030_asset_liability_gap_ewm_126d_accel_v114_signal(assets, closeadj):
    base = assets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm assets
def alg_f030_asset_liability_gap_ewm_252d_accel_v115_signal(assets, closeadj):
    base = assets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm assets
def alg_f030_asset_liability_gap_ewm_252d_accel_v116_signal(assets, closeadj):
    base = assets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm assets
def alg_f030_asset_liability_gap_ewm_252d_accel_v117_signal(assets, closeadj):
    base = assets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm assets
def alg_f030_asset_liability_gap_ewm_504d_accel_v118_signal(assets, closeadj):
    base = assets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm assets
def alg_f030_asset_liability_gap_ewm_504d_accel_v119_signal(assets, closeadj):
    base = assets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm assets
def alg_f030_asset_liability_gap_ewm_504d_accel_v120_signal(assets, closeadj):
    base = assets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq assets
def alg_f030_asset_liability_gap_sq_21d_accel_v121_signal(assets, closeadj):
    base = _mean(assets * assets, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq assets
def alg_f030_asset_liability_gap_sq_21d_accel_v122_signal(assets, closeadj):
    base = _mean(assets * assets, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq assets
def alg_f030_asset_liability_gap_sq_21d_accel_v123_signal(assets, closeadj):
    base = _mean(assets * assets, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq assets
def alg_f030_asset_liability_gap_sq_63d_accel_v124_signal(assets, closeadj):
    base = _mean(assets * assets, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq assets
def alg_f030_asset_liability_gap_sq_63d_accel_v125_signal(assets, closeadj):
    base = _mean(assets * assets, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq assets
def alg_f030_asset_liability_gap_sq_63d_accel_v126_signal(assets, closeadj):
    base = _mean(assets * assets, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq assets
def alg_f030_asset_liability_gap_sq_126d_accel_v127_signal(assets, closeadj):
    base = _mean(assets * assets, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq assets
def alg_f030_asset_liability_gap_sq_126d_accel_v128_signal(assets, closeadj):
    base = _mean(assets * assets, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq assets
def alg_f030_asset_liability_gap_sq_126d_accel_v129_signal(assets, closeadj):
    base = _mean(assets * assets, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq assets
def alg_f030_asset_liability_gap_sq_252d_accel_v130_signal(assets, closeadj):
    base = _mean(assets * assets, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq assets
def alg_f030_asset_liability_gap_sq_252d_accel_v131_signal(assets, closeadj):
    base = _mean(assets * assets, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq assets
def alg_f030_asset_liability_gap_sq_252d_accel_v132_signal(assets, closeadj):
    base = _mean(assets * assets, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq assets
def alg_f030_asset_liability_gap_sq_504d_accel_v133_signal(assets, closeadj):
    base = _mean(assets * assets, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq assets
def alg_f030_asset_liability_gap_sq_504d_accel_v134_signal(assets, closeadj):
    base = _mean(assets * assets, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq assets
def alg_f030_asset_liability_gap_sq_504d_accel_v135_signal(assets, closeadj):
    base = _mean(assets * assets, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z assets
def alg_f030_asset_liability_gap_z_21d_accel_v136_signal(assets):
    base = _z(assets, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z assets
def alg_f030_asset_liability_gap_z_21d_accel_v137_signal(assets):
    base = _z(assets, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z assets
def alg_f030_asset_liability_gap_z_21d_accel_v138_signal(assets):
    base = _z(assets, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z assets
def alg_f030_asset_liability_gap_z_63d_accel_v139_signal(assets):
    base = _z(assets, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z assets
def alg_f030_asset_liability_gap_z_63d_accel_v140_signal(assets):
    base = _z(assets, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z assets
def alg_f030_asset_liability_gap_z_63d_accel_v141_signal(assets):
    base = _z(assets, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z assets
def alg_f030_asset_liability_gap_z_126d_accel_v142_signal(assets):
    base = _z(assets, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z assets
def alg_f030_asset_liability_gap_z_126d_accel_v143_signal(assets):
    base = _z(assets, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z assets
def alg_f030_asset_liability_gap_z_126d_accel_v144_signal(assets):
    base = _z(assets, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z assets
def alg_f030_asset_liability_gap_z_252d_accel_v145_signal(assets):
    base = _z(assets, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z assets
def alg_f030_asset_liability_gap_z_252d_accel_v146_signal(assets):
    base = _z(assets, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z assets
def alg_f030_asset_liability_gap_z_252d_accel_v147_signal(assets):
    base = _z(assets, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z assets
def alg_f030_asset_liability_gap_z_504d_accel_v148_signal(assets):
    base = _z(assets, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z assets
def alg_f030_asset_liability_gap_z_504d_accel_v149_signal(assets):
    base = _z(assets, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z assets
def alg_f030_asset_liability_gap_z_504d_accel_v150_signal(assets):
    base = _z(assets, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
