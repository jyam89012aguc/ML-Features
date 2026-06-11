"""Family f061 - Tax assets and NOL proxy (Earnings and Quality) | Sharadar tables: SF1 | fields: taxassets, taxexp, ebt, assets | 3rd derivatives 001-150"""
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
def _tax_asset_and_nol_proxy_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _tax_asset_and_nol_proxy_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _tax_asset_and_nol_proxy_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_21d_accel_v001_signal(taxassets, closeadj):
    base = _mean(taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_21d_accel_v002_signal(taxassets, closeadj):
    base = _mean(taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_21d_accel_v003_signal(taxassets, closeadj):
    base = _mean(taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_63d_accel_v004_signal(taxassets, closeadj):
    base = _mean(taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_63d_accel_v005_signal(taxassets, closeadj):
    base = _mean(taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_63d_accel_v006_signal(taxassets, closeadj):
    base = _mean(taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_126d_accel_v007_signal(taxassets, closeadj):
    base = _mean(taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_126d_accel_v008_signal(taxassets, closeadj):
    base = _mean(taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_126d_accel_v009_signal(taxassets, closeadj):
    base = _mean(taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_252d_accel_v010_signal(taxassets, closeadj):
    base = _mean(taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_252d_accel_v011_signal(taxassets, closeadj):
    base = _mean(taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_252d_accel_v012_signal(taxassets, closeadj):
    base = _mean(taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_504d_accel_v013_signal(taxassets, closeadj):
    base = _mean(taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_504d_accel_v014_signal(taxassets, closeadj):
    base = _mean(taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_504d_accel_v015_signal(taxassets, closeadj):
    base = _mean(taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_21d_accel_v016_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_21d_accel_v017_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_21d_accel_v018_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_63d_accel_v019_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_63d_accel_v020_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_63d_accel_v021_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_126d_accel_v022_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_126d_accel_v023_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_126d_accel_v024_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_252d_accel_v025_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_252d_accel_v026_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_252d_accel_v027_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_504d_accel_v028_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_504d_accel_v029_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_504d_accel_v030_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_21d_accel_v031_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_21d_accel_v032_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_21d_accel_v033_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_63d_accel_v034_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_63d_accel_v035_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_63d_accel_v036_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_126d_accel_v037_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_126d_accel_v038_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_126d_accel_v039_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_252d_accel_v040_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_252d_accel_v041_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_252d_accel_v042_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_504d_accel_v043_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_504d_accel_v044_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_504d_accel_v045_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_21d_accel_v046_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_21d_accel_v047_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_21d_accel_v048_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_63d_accel_v049_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_63d_accel_v050_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_63d_accel_v051_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_126d_accel_v052_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_126d_accel_v053_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_126d_accel_v054_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_252d_accel_v055_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_252d_accel_v056_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_252d_accel_v057_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_504d_accel_v058_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_504d_accel_v059_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_504d_accel_v060_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_21d_accel_v061_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_21d_accel_v062_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_21d_accel_v063_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_63d_accel_v064_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_63d_accel_v065_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_63d_accel_v066_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_126d_accel_v067_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_126d_accel_v068_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_126d_accel_v069_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_252d_accel_v070_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_252d_accel_v071_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_252d_accel_v072_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_504d_accel_v073_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_504d_accel_v074_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_504d_accel_v075_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_21d_accel_v076_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_21d_accel_v077_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_21d_accel_v078_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_63d_accel_v079_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_63d_accel_v080_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_63d_accel_v081_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_126d_accel_v082_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_126d_accel_v083_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_126d_accel_v084_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_252d_accel_v085_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_252d_accel_v086_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_252d_accel_v087_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_504d_accel_v088_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_504d_accel_v089_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_504d_accel_v090_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_21d_accel_v091_signal(taxassets, closeadj):
    base = _std(taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_21d_accel_v092_signal(taxassets, closeadj):
    base = _std(taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_21d_accel_v093_signal(taxassets, closeadj):
    base = _std(taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_63d_accel_v094_signal(taxassets, closeadj):
    base = _std(taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_63d_accel_v095_signal(taxassets, closeadj):
    base = _std(taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_63d_accel_v096_signal(taxassets, closeadj):
    base = _std(taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_126d_accel_v097_signal(taxassets, closeadj):
    base = _std(taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_126d_accel_v098_signal(taxassets, closeadj):
    base = _std(taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_126d_accel_v099_signal(taxassets, closeadj):
    base = _std(taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_252d_accel_v100_signal(taxassets, closeadj):
    base = _std(taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_252d_accel_v101_signal(taxassets, closeadj):
    base = _std(taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_252d_accel_v102_signal(taxassets, closeadj):
    base = _std(taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_504d_accel_v103_signal(taxassets, closeadj):
    base = _std(taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_504d_accel_v104_signal(taxassets, closeadj):
    base = _std(taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_504d_accel_v105_signal(taxassets, closeadj):
    base = _std(taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_21d_accel_v106_signal(taxassets, closeadj):
    base = taxassets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_21d_accel_v107_signal(taxassets, closeadj):
    base = taxassets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_21d_accel_v108_signal(taxassets, closeadj):
    base = taxassets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_63d_accel_v109_signal(taxassets, closeadj):
    base = taxassets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_63d_accel_v110_signal(taxassets, closeadj):
    base = taxassets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_63d_accel_v111_signal(taxassets, closeadj):
    base = taxassets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_126d_accel_v112_signal(taxassets, closeadj):
    base = taxassets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_126d_accel_v113_signal(taxassets, closeadj):
    base = taxassets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_126d_accel_v114_signal(taxassets, closeadj):
    base = taxassets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_252d_accel_v115_signal(taxassets, closeadj):
    base = taxassets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_252d_accel_v116_signal(taxassets, closeadj):
    base = taxassets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_252d_accel_v117_signal(taxassets, closeadj):
    base = taxassets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_504d_accel_v118_signal(taxassets, closeadj):
    base = taxassets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_504d_accel_v119_signal(taxassets, closeadj):
    base = taxassets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_504d_accel_v120_signal(taxassets, closeadj):
    base = taxassets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_21d_accel_v121_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_21d_accel_v122_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_21d_accel_v123_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_63d_accel_v124_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_63d_accel_v125_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_63d_accel_v126_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_126d_accel_v127_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_126d_accel_v128_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_126d_accel_v129_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_252d_accel_v130_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_252d_accel_v131_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_252d_accel_v132_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_504d_accel_v133_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_504d_accel_v134_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_504d_accel_v135_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_21d_accel_v136_signal(taxassets):
    base = _z(taxassets, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_21d_accel_v137_signal(taxassets):
    base = _z(taxassets, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_21d_accel_v138_signal(taxassets):
    base = _z(taxassets, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_63d_accel_v139_signal(taxassets):
    base = _z(taxassets, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_63d_accel_v140_signal(taxassets):
    base = _z(taxassets, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_63d_accel_v141_signal(taxassets):
    base = _z(taxassets, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_126d_accel_v142_signal(taxassets):
    base = _z(taxassets, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_126d_accel_v143_signal(taxassets):
    base = _z(taxassets, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_126d_accel_v144_signal(taxassets):
    base = _z(taxassets, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_252d_accel_v145_signal(taxassets):
    base = _z(taxassets, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_252d_accel_v146_signal(taxassets):
    base = _z(taxassets, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_252d_accel_v147_signal(taxassets):
    base = _z(taxassets, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_504d_accel_v148_signal(taxassets):
    base = _z(taxassets, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_504d_accel_v149_signal(taxassets):
    base = _z(taxassets, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_504d_accel_v150_signal(taxassets):
    base = _z(taxassets, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
