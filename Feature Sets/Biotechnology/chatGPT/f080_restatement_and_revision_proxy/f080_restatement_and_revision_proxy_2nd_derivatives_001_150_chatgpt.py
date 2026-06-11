"""Family f080 - Revision and restatement proxy (Fundamental Dynamics) | Sharadar tables: SF1 | fields: datekey, lastupdated, reportperiod, dimension | 2nd derivatives 001-150"""
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
def _restatement_and_revision_proxy_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _restatement_and_revision_proxy_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _restatement_and_revision_proxy_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_21d_slope_v001_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_21d_slope_v002_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_21d_slope_v003_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_63d_slope_v004_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_63d_slope_v005_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_63d_slope_v006_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_126d_slope_v007_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_126d_slope_v008_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_126d_slope_v009_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_252d_slope_v010_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_252d_slope_v011_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_252d_slope_v012_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_504d_slope_v013_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_504d_slope_v014_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_504d_slope_v015_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_21d_slope_v016_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_21d_slope_v017_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_21d_slope_v018_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_63d_slope_v019_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_63d_slope_v020_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_63d_slope_v021_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_126d_slope_v022_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_126d_slope_v023_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_126d_slope_v024_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_252d_slope_v025_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_252d_slope_v026_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_252d_slope_v027_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_504d_slope_v028_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_504d_slope_v029_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_504d_slope_v030_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_21d_slope_v031_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_21d_slope_v032_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_21d_slope_v033_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_63d_slope_v034_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_63d_slope_v035_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_63d_slope_v036_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_126d_slope_v037_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_126d_slope_v038_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_126d_slope_v039_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_252d_slope_v040_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_252d_slope_v041_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_252d_slope_v042_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_504d_slope_v043_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_504d_slope_v044_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_504d_slope_v045_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_21d_slope_v046_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_21d_slope_v047_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_21d_slope_v048_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_63d_slope_v049_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_63d_slope_v050_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_63d_slope_v051_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_126d_slope_v052_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_126d_slope_v053_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_126d_slope_v054_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_252d_slope_v055_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_252d_slope_v056_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_252d_slope_v057_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_504d_slope_v058_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_504d_slope_v059_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_504d_slope_v060_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_21d_slope_v061_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_21d_slope_v062_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_21d_slope_v063_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_63d_slope_v064_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_63d_slope_v065_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_63d_slope_v066_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_126d_slope_v067_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_126d_slope_v068_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_126d_slope_v069_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_252d_slope_v070_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_252d_slope_v071_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_252d_slope_v072_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_504d_slope_v073_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_504d_slope_v074_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_504d_slope_v075_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_21d_slope_v076_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_21d_slope_v077_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_21d_slope_v078_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_63d_slope_v079_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_63d_slope_v080_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_63d_slope_v081_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_126d_slope_v082_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_126d_slope_v083_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_126d_slope_v084_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_252d_slope_v085_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_252d_slope_v086_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_252d_slope_v087_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_504d_slope_v088_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_504d_slope_v089_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_504d_slope_v090_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_21d_slope_v091_signal(revisioncount, closeadj):
    base = _std(revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_21d_slope_v092_signal(revisioncount, closeadj):
    base = _std(revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_21d_slope_v093_signal(revisioncount, closeadj):
    base = _std(revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_63d_slope_v094_signal(revisioncount, closeadj):
    base = _std(revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_63d_slope_v095_signal(revisioncount, closeadj):
    base = _std(revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_63d_slope_v096_signal(revisioncount, closeadj):
    base = _std(revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_126d_slope_v097_signal(revisioncount, closeadj):
    base = _std(revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_126d_slope_v098_signal(revisioncount, closeadj):
    base = _std(revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_126d_slope_v099_signal(revisioncount, closeadj):
    base = _std(revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_252d_slope_v100_signal(revisioncount, closeadj):
    base = _std(revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_252d_slope_v101_signal(revisioncount, closeadj):
    base = _std(revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_252d_slope_v102_signal(revisioncount, closeadj):
    base = _std(revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_504d_slope_v103_signal(revisioncount, closeadj):
    base = _std(revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_504d_slope_v104_signal(revisioncount, closeadj):
    base = _std(revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_504d_slope_v105_signal(revisioncount, closeadj):
    base = _std(revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_21d_slope_v106_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_21d_slope_v107_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_21d_slope_v108_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_63d_slope_v109_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_63d_slope_v110_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_63d_slope_v111_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_126d_slope_v112_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_126d_slope_v113_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_126d_slope_v114_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_252d_slope_v115_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_252d_slope_v116_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_252d_slope_v117_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_504d_slope_v118_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_504d_slope_v119_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_504d_slope_v120_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_21d_slope_v121_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_21d_slope_v122_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_21d_slope_v123_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_63d_slope_v124_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_63d_slope_v125_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_63d_slope_v126_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_126d_slope_v127_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_126d_slope_v128_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_126d_slope_v129_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_252d_slope_v130_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_252d_slope_v131_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_252d_slope_v132_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_504d_slope_v133_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_504d_slope_v134_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_504d_slope_v135_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_21d_slope_v136_signal(revisioncount):
    base = _z(revisioncount, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_21d_slope_v137_signal(revisioncount):
    base = _z(revisioncount, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_21d_slope_v138_signal(revisioncount):
    base = _z(revisioncount, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_63d_slope_v139_signal(revisioncount):
    base = _z(revisioncount, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_63d_slope_v140_signal(revisioncount):
    base = _z(revisioncount, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_63d_slope_v141_signal(revisioncount):
    base = _z(revisioncount, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_126d_slope_v142_signal(revisioncount):
    base = _z(revisioncount, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_126d_slope_v143_signal(revisioncount):
    base = _z(revisioncount, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_126d_slope_v144_signal(revisioncount):
    base = _z(revisioncount, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_252d_slope_v145_signal(revisioncount):
    base = _z(revisioncount, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_252d_slope_v146_signal(revisioncount):
    base = _z(revisioncount, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_252d_slope_v147_signal(revisioncount):
    base = _z(revisioncount, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_504d_slope_v148_signal(revisioncount):
    base = _z(revisioncount, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_504d_slope_v149_signal(revisioncount):
    base = _z(revisioncount, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_504d_slope_v150_signal(revisioncount):
    base = _z(revisioncount, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
