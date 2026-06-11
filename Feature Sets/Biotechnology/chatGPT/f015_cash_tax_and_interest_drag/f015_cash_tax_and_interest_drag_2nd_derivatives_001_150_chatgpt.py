"""Family f015 - Cash interest and tax drag (Cash Flow and Burn) | Sharadar tables: SF1 | fields: intexp, taxexp, ncfo, debt | 2nd derivatives 001-150"""
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
def _cash_tax_and_interest_drag_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_tax_and_interest_drag_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_tax_and_interest_drag_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_21d_slope_v001_signal(intexp, closeadj):
    base = _mean(intexp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_21d_slope_v002_signal(intexp, closeadj):
    base = _mean(intexp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_21d_slope_v003_signal(intexp, closeadj):
    base = _mean(intexp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_63d_slope_v004_signal(intexp, closeadj):
    base = _mean(intexp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_63d_slope_v005_signal(intexp, closeadj):
    base = _mean(intexp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_63d_slope_v006_signal(intexp, closeadj):
    base = _mean(intexp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_126d_slope_v007_signal(intexp, closeadj):
    base = _mean(intexp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_126d_slope_v008_signal(intexp, closeadj):
    base = _mean(intexp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_126d_slope_v009_signal(intexp, closeadj):
    base = _mean(intexp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_252d_slope_v010_signal(intexp, closeadj):
    base = _mean(intexp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_252d_slope_v011_signal(intexp, closeadj):
    base = _mean(intexp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_252d_slope_v012_signal(intexp, closeadj):
    base = _mean(intexp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_504d_slope_v013_signal(intexp, closeadj):
    base = _mean(intexp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_504d_slope_v014_signal(intexp, closeadj):
    base = _mean(intexp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw intexp
def ctai_f015_cash_tax_and_interest_drag_raw_504d_slope_v015_signal(intexp, closeadj):
    base = _mean(intexp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_21d_slope_v016_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_21d_slope_v017_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_21d_slope_v018_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_63d_slope_v019_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_63d_slope_v020_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_63d_slope_v021_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_126d_slope_v022_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_126d_slope_v023_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_126d_slope_v024_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_252d_slope_v025_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_252d_slope_v026_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_252d_slope_v027_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_504d_slope_v028_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_504d_slope_v029_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log intexp
def ctai_f015_cash_tax_and_interest_drag_log_504d_slope_v030_signal(intexp, closeadj):
    base = _mean(_cash_tax_and_interest_drag_log(intexp), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_21d_slope_v031_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_21d_slope_v032_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_21d_slope_v033_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_63d_slope_v034_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_63d_slope_v035_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_63d_slope_v036_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_126d_slope_v037_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_126d_slope_v038_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_126d_slope_v039_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_252d_slope_v040_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_252d_slope_v041_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_252d_slope_v042_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_504d_slope_v043_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_504d_slope_v044_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare intexp
def ctai_f015_cash_tax_and_interest_drag_pershare_504d_slope_v045_signal(intexp, sharesbas, closeadj):
    base = _mean(_cash_tax_and_interest_drag_per_share(intexp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_21d_slope_v046_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_21d_slope_v047_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_21d_slope_v048_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_63d_slope_v049_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_63d_slope_v050_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_63d_slope_v051_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_126d_slope_v052_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_126d_slope_v053_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_126d_slope_v054_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_252d_slope_v055_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_252d_slope_v056_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_252d_slope_v057_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_504d_slope_v058_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_504d_slope_v059_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_taxexp intexp
def ctai_f015_cash_tax_and_interest_drag_per_taxexp_504d_slope_v060_signal(intexp, taxexp):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, taxexp), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_21d_slope_v061_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_21d_slope_v062_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_21d_slope_v063_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_63d_slope_v064_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_63d_slope_v065_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_63d_slope_v066_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_126d_slope_v067_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_126d_slope_v068_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_126d_slope_v069_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_252d_slope_v070_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_252d_slope_v071_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_252d_slope_v072_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_504d_slope_v073_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_504d_slope_v074_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_ncfo intexp
def ctai_f015_cash_tax_and_interest_drag_per_ncfo_504d_slope_v075_signal(intexp, ncfo):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, ncfo), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_21d_slope_v076_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_21d_slope_v077_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_21d_slope_v078_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_63d_slope_v079_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_63d_slope_v080_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_63d_slope_v081_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_126d_slope_v082_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_126d_slope_v083_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_126d_slope_v084_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_252d_slope_v085_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_252d_slope_v086_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_252d_slope_v087_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_504d_slope_v088_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_504d_slope_v089_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_debt intexp
def ctai_f015_cash_tax_and_interest_drag_per_debt_504d_slope_v090_signal(intexp, debt):
    base = _mean(_cash_tax_and_interest_drag_scaled(intexp, debt), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_21d_slope_v091_signal(intexp, closeadj):
    base = _std(intexp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_21d_slope_v092_signal(intexp, closeadj):
    base = _std(intexp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_21d_slope_v093_signal(intexp, closeadj):
    base = _std(intexp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_63d_slope_v094_signal(intexp, closeadj):
    base = _std(intexp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_63d_slope_v095_signal(intexp, closeadj):
    base = _std(intexp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_63d_slope_v096_signal(intexp, closeadj):
    base = _std(intexp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_126d_slope_v097_signal(intexp, closeadj):
    base = _std(intexp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_126d_slope_v098_signal(intexp, closeadj):
    base = _std(intexp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_126d_slope_v099_signal(intexp, closeadj):
    base = _std(intexp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_252d_slope_v100_signal(intexp, closeadj):
    base = _std(intexp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_252d_slope_v101_signal(intexp, closeadj):
    base = _std(intexp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_252d_slope_v102_signal(intexp, closeadj):
    base = _std(intexp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_504d_slope_v103_signal(intexp, closeadj):
    base = _std(intexp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_504d_slope_v104_signal(intexp, closeadj):
    base = _std(intexp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std intexp
def ctai_f015_cash_tax_and_interest_drag_std_504d_slope_v105_signal(intexp, closeadj):
    base = _std(intexp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_21d_slope_v106_signal(intexp, closeadj):
    base = intexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_21d_slope_v107_signal(intexp, closeadj):
    base = intexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_21d_slope_v108_signal(intexp, closeadj):
    base = intexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_63d_slope_v109_signal(intexp, closeadj):
    base = intexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_63d_slope_v110_signal(intexp, closeadj):
    base = intexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_63d_slope_v111_signal(intexp, closeadj):
    base = intexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_126d_slope_v112_signal(intexp, closeadj):
    base = intexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_126d_slope_v113_signal(intexp, closeadj):
    base = intexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_126d_slope_v114_signal(intexp, closeadj):
    base = intexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_252d_slope_v115_signal(intexp, closeadj):
    base = intexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_252d_slope_v116_signal(intexp, closeadj):
    base = intexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_252d_slope_v117_signal(intexp, closeadj):
    base = intexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_504d_slope_v118_signal(intexp, closeadj):
    base = intexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_504d_slope_v119_signal(intexp, closeadj):
    base = intexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm intexp
def ctai_f015_cash_tax_and_interest_drag_ewm_504d_slope_v120_signal(intexp, closeadj):
    base = intexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_21d_slope_v121_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_21d_slope_v122_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_21d_slope_v123_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_63d_slope_v124_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_63d_slope_v125_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_63d_slope_v126_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_126d_slope_v127_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_126d_slope_v128_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_126d_slope_v129_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_252d_slope_v130_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_252d_slope_v131_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_252d_slope_v132_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_504d_slope_v133_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_504d_slope_v134_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq intexp
def ctai_f015_cash_tax_and_interest_drag_sq_504d_slope_v135_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_21d_slope_v136_signal(intexp):
    base = _z(intexp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_21d_slope_v137_signal(intexp):
    base = _z(intexp, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_21d_slope_v138_signal(intexp):
    base = _z(intexp, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_63d_slope_v139_signal(intexp):
    base = _z(intexp, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_63d_slope_v140_signal(intexp):
    base = _z(intexp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_63d_slope_v141_signal(intexp):
    base = _z(intexp, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_126d_slope_v142_signal(intexp):
    base = _z(intexp, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_126d_slope_v143_signal(intexp):
    base = _z(intexp, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_126d_slope_v144_signal(intexp):
    base = _z(intexp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_252d_slope_v145_signal(intexp):
    base = _z(intexp, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_252d_slope_v146_signal(intexp):
    base = _z(intexp, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_252d_slope_v147_signal(intexp):
    base = _z(intexp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_504d_slope_v148_signal(intexp):
    base = _z(intexp, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_504d_slope_v149_signal(intexp):
    base = _z(intexp, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z intexp
def ctai_f015_cash_tax_and_interest_drag_z_504d_slope_v150_signal(intexp):
    base = _z(intexp, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
