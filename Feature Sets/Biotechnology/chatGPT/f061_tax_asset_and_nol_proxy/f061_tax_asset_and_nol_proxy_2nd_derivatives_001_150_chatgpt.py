"""Family f061 - Tax assets and NOL proxy (Earnings and Quality) | Sharadar tables: SF1 | fields: taxassets, taxexp, ebt, assets | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_21d_slope_v001_signal(taxassets, closeadj):
    base = _mean(taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_21d_slope_v002_signal(taxassets, closeadj):
    base = _mean(taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_21d_slope_v003_signal(taxassets, closeadj):
    base = _mean(taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_63d_slope_v004_signal(taxassets, closeadj):
    base = _mean(taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_63d_slope_v005_signal(taxassets, closeadj):
    base = _mean(taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_63d_slope_v006_signal(taxassets, closeadj):
    base = _mean(taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_126d_slope_v007_signal(taxassets, closeadj):
    base = _mean(taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_126d_slope_v008_signal(taxassets, closeadj):
    base = _mean(taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_126d_slope_v009_signal(taxassets, closeadj):
    base = _mean(taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_252d_slope_v010_signal(taxassets, closeadj):
    base = _mean(taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_252d_slope_v011_signal(taxassets, closeadj):
    base = _mean(taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_252d_slope_v012_signal(taxassets, closeadj):
    base = _mean(taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_504d_slope_v013_signal(taxassets, closeadj):
    base = _mean(taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_504d_slope_v014_signal(taxassets, closeadj):
    base = _mean(taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw taxassets
def taan_f061_tax_asset_and_nol_proxy_raw_504d_slope_v015_signal(taxassets, closeadj):
    base = _mean(taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_21d_slope_v016_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_21d_slope_v017_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_21d_slope_v018_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_63d_slope_v019_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_63d_slope_v020_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_63d_slope_v021_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_126d_slope_v022_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_126d_slope_v023_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_126d_slope_v024_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_252d_slope_v025_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_252d_slope_v026_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_252d_slope_v027_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_504d_slope_v028_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_504d_slope_v029_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log taxassets
def taan_f061_tax_asset_and_nol_proxy_log_504d_slope_v030_signal(taxassets, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_log(taxassets), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_21d_slope_v031_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_21d_slope_v032_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_21d_slope_v033_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_63d_slope_v034_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_63d_slope_v035_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_63d_slope_v036_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_126d_slope_v037_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_126d_slope_v038_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_126d_slope_v039_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_252d_slope_v040_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_252d_slope_v041_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_252d_slope_v042_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_504d_slope_v043_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_504d_slope_v044_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare taxassets
def taan_f061_tax_asset_and_nol_proxy_pershare_504d_slope_v045_signal(taxassets, sharesbas, closeadj):
    base = _mean(_tax_asset_and_nol_proxy_per_share(taxassets, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_21d_slope_v046_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_21d_slope_v047_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_21d_slope_v048_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_63d_slope_v049_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_63d_slope_v050_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_63d_slope_v051_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_126d_slope_v052_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_126d_slope_v053_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_126d_slope_v054_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_252d_slope_v055_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_252d_slope_v056_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_252d_slope_v057_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_504d_slope_v058_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_504d_slope_v059_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_taxexp taxassets
def taan_f061_tax_asset_and_nol_proxy_per_taxexp_504d_slope_v060_signal(taxassets, taxexp):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, taxexp), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_21d_slope_v061_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_21d_slope_v062_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_21d_slope_v063_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_63d_slope_v064_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_63d_slope_v065_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_63d_slope_v066_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_126d_slope_v067_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_126d_slope_v068_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_126d_slope_v069_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_252d_slope_v070_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_252d_slope_v071_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_252d_slope_v072_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_504d_slope_v073_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_504d_slope_v074_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_ebt taxassets
def taan_f061_tax_asset_and_nol_proxy_per_ebt_504d_slope_v075_signal(taxassets, ebt):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, ebt), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_21d_slope_v076_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_21d_slope_v077_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_21d_slope_v078_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_63d_slope_v079_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_63d_slope_v080_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_63d_slope_v081_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_126d_slope_v082_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_126d_slope_v083_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_126d_slope_v084_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_252d_slope_v085_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_252d_slope_v086_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_252d_slope_v087_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_504d_slope_v088_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_504d_slope_v089_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets taxassets
def taan_f061_tax_asset_and_nol_proxy_per_assets_504d_slope_v090_signal(taxassets, assets):
    base = _mean(_tax_asset_and_nol_proxy_scaled(taxassets, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_21d_slope_v091_signal(taxassets, closeadj):
    base = _std(taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_21d_slope_v092_signal(taxassets, closeadj):
    base = _std(taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_21d_slope_v093_signal(taxassets, closeadj):
    base = _std(taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_63d_slope_v094_signal(taxassets, closeadj):
    base = _std(taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_63d_slope_v095_signal(taxassets, closeadj):
    base = _std(taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_63d_slope_v096_signal(taxassets, closeadj):
    base = _std(taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_126d_slope_v097_signal(taxassets, closeadj):
    base = _std(taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_126d_slope_v098_signal(taxassets, closeadj):
    base = _std(taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_126d_slope_v099_signal(taxassets, closeadj):
    base = _std(taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_252d_slope_v100_signal(taxassets, closeadj):
    base = _std(taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_252d_slope_v101_signal(taxassets, closeadj):
    base = _std(taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_252d_slope_v102_signal(taxassets, closeadj):
    base = _std(taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_504d_slope_v103_signal(taxassets, closeadj):
    base = _std(taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_504d_slope_v104_signal(taxassets, closeadj):
    base = _std(taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std taxassets
def taan_f061_tax_asset_and_nol_proxy_std_504d_slope_v105_signal(taxassets, closeadj):
    base = _std(taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_21d_slope_v106_signal(taxassets, closeadj):
    base = taxassets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_21d_slope_v107_signal(taxassets, closeadj):
    base = taxassets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_21d_slope_v108_signal(taxassets, closeadj):
    base = taxassets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_63d_slope_v109_signal(taxassets, closeadj):
    base = taxassets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_63d_slope_v110_signal(taxassets, closeadj):
    base = taxassets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_63d_slope_v111_signal(taxassets, closeadj):
    base = taxassets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_126d_slope_v112_signal(taxassets, closeadj):
    base = taxassets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_126d_slope_v113_signal(taxassets, closeadj):
    base = taxassets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_126d_slope_v114_signal(taxassets, closeadj):
    base = taxassets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_252d_slope_v115_signal(taxassets, closeadj):
    base = taxassets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_252d_slope_v116_signal(taxassets, closeadj):
    base = taxassets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_252d_slope_v117_signal(taxassets, closeadj):
    base = taxassets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_504d_slope_v118_signal(taxassets, closeadj):
    base = taxassets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_504d_slope_v119_signal(taxassets, closeadj):
    base = taxassets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm taxassets
def taan_f061_tax_asset_and_nol_proxy_ewm_504d_slope_v120_signal(taxassets, closeadj):
    base = taxassets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_21d_slope_v121_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_21d_slope_v122_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_21d_slope_v123_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_63d_slope_v124_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_63d_slope_v125_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_63d_slope_v126_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_126d_slope_v127_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_126d_slope_v128_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_126d_slope_v129_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_252d_slope_v130_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_252d_slope_v131_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_252d_slope_v132_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_504d_slope_v133_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_504d_slope_v134_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq taxassets
def taan_f061_tax_asset_and_nol_proxy_sq_504d_slope_v135_signal(taxassets, closeadj):
    base = _mean(taxassets * taxassets, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_21d_slope_v136_signal(taxassets):
    base = _z(taxassets, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_21d_slope_v137_signal(taxassets):
    base = _z(taxassets, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_21d_slope_v138_signal(taxassets):
    base = _z(taxassets, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_63d_slope_v139_signal(taxassets):
    base = _z(taxassets, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_63d_slope_v140_signal(taxassets):
    base = _z(taxassets, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_63d_slope_v141_signal(taxassets):
    base = _z(taxassets, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_126d_slope_v142_signal(taxassets):
    base = _z(taxassets, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_126d_slope_v143_signal(taxassets):
    base = _z(taxassets, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_126d_slope_v144_signal(taxassets):
    base = _z(taxassets, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_252d_slope_v145_signal(taxassets):
    base = _z(taxassets, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_252d_slope_v146_signal(taxassets):
    base = _z(taxassets, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_252d_slope_v147_signal(taxassets):
    base = _z(taxassets, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_504d_slope_v148_signal(taxassets):
    base = _z(taxassets, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_504d_slope_v149_signal(taxassets):
    base = _z(taxassets, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z taxassets
def taan_f061_tax_asset_and_nol_proxy_z_504d_slope_v150_signal(taxassets):
    base = _z(taxassets, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
