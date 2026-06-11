"""Family f080 - Revision and restatement proxy (Fundamental Dynamics) | Sharadar tables: SF1 | fields: datekey, lastupdated, reportperiod, dimension | 3rd derivatives 001-150"""
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


# 5d accel of 21d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_21d_accel_v001_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_21d_accel_v002_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_21d_accel_v003_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_63d_accel_v004_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_63d_accel_v005_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_63d_accel_v006_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_126d_accel_v007_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_126d_accel_v008_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_126d_accel_v009_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_252d_accel_v010_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_252d_accel_v011_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_252d_accel_v012_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_504d_accel_v013_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_504d_accel_v014_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw revisioncount
def rarp_f080_restatement_and_revision_proxy_raw_504d_accel_v015_signal(revisioncount, closeadj):
    base = _mean(revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_21d_accel_v016_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_21d_accel_v017_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_21d_accel_v018_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_63d_accel_v019_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_63d_accel_v020_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_63d_accel_v021_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_126d_accel_v022_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_126d_accel_v023_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_126d_accel_v024_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_252d_accel_v025_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_252d_accel_v026_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_252d_accel_v027_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_504d_accel_v028_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_504d_accel_v029_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log revisioncount
def rarp_f080_restatement_and_revision_proxy_log_504d_accel_v030_signal(revisioncount, closeadj):
    base = _mean(_restatement_and_revision_proxy_log(revisioncount), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_21d_accel_v031_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_21d_accel_v032_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_21d_accel_v033_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_63d_accel_v034_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_63d_accel_v035_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_63d_accel_v036_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_126d_accel_v037_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_126d_accel_v038_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_126d_accel_v039_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_252d_accel_v040_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_252d_accel_v041_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_252d_accel_v042_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_504d_accel_v043_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_504d_accel_v044_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare revisioncount
def rarp_f080_restatement_and_revision_proxy_pershare_504d_accel_v045_signal(revisioncount, sharesbas, closeadj):
    base = _mean(_restatement_and_revision_proxy_per_share(revisioncount, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_21d_accel_v046_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_21d_accel_v047_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_21d_accel_v048_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_63d_accel_v049_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_63d_accel_v050_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_63d_accel_v051_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_126d_accel_v052_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_126d_accel_v053_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_126d_accel_v054_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_252d_accel_v055_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_252d_accel_v056_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_252d_accel_v057_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_504d_accel_v058_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_504d_accel_v059_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_datekey revisioncount
def rarp_f080_restatement_and_revision_proxy_per_datekey_504d_accel_v060_signal(revisioncount, datekey):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_21d_accel_v061_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_21d_accel_v062_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_21d_accel_v063_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_63d_accel_v064_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_63d_accel_v065_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_63d_accel_v066_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_126d_accel_v067_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_126d_accel_v068_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_126d_accel_v069_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_252d_accel_v070_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_252d_accel_v071_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_252d_accel_v072_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_504d_accel_v073_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_504d_accel_v074_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_dimension revisioncount
def rarp_f080_restatement_and_revision_proxy_per_dimension_504d_accel_v075_signal(revisioncount, dimension):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_21d_accel_v076_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_21d_accel_v077_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_21d_accel_v078_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_63d_accel_v079_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_63d_accel_v080_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_63d_accel_v081_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_126d_accel_v082_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_126d_accel_v083_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_126d_accel_v084_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_252d_accel_v085_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_252d_accel_v086_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_252d_accel_v087_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_504d_accel_v088_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_504d_accel_v089_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets revisioncount
def rarp_f080_restatement_and_revision_proxy_per_assets_504d_accel_v090_signal(revisioncount, assets):
    base = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_21d_accel_v091_signal(revisioncount, closeadj):
    base = _std(revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_21d_accel_v092_signal(revisioncount, closeadj):
    base = _std(revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_21d_accel_v093_signal(revisioncount, closeadj):
    base = _std(revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_63d_accel_v094_signal(revisioncount, closeadj):
    base = _std(revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_63d_accel_v095_signal(revisioncount, closeadj):
    base = _std(revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_63d_accel_v096_signal(revisioncount, closeadj):
    base = _std(revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_126d_accel_v097_signal(revisioncount, closeadj):
    base = _std(revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_126d_accel_v098_signal(revisioncount, closeadj):
    base = _std(revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_126d_accel_v099_signal(revisioncount, closeadj):
    base = _std(revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_252d_accel_v100_signal(revisioncount, closeadj):
    base = _std(revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_252d_accel_v101_signal(revisioncount, closeadj):
    base = _std(revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_252d_accel_v102_signal(revisioncount, closeadj):
    base = _std(revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_504d_accel_v103_signal(revisioncount, closeadj):
    base = _std(revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_504d_accel_v104_signal(revisioncount, closeadj):
    base = _std(revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std revisioncount
def rarp_f080_restatement_and_revision_proxy_std_504d_accel_v105_signal(revisioncount, closeadj):
    base = _std(revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_21d_accel_v106_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_21d_accel_v107_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_21d_accel_v108_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_63d_accel_v109_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_63d_accel_v110_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_63d_accel_v111_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_126d_accel_v112_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_126d_accel_v113_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_126d_accel_v114_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_252d_accel_v115_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_252d_accel_v116_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_252d_accel_v117_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_504d_accel_v118_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_504d_accel_v119_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm revisioncount
def rarp_f080_restatement_and_revision_proxy_ewm_504d_accel_v120_signal(revisioncount, closeadj):
    base = revisioncount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_21d_accel_v121_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_21d_accel_v122_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_21d_accel_v123_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_63d_accel_v124_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_63d_accel_v125_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_63d_accel_v126_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_126d_accel_v127_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_126d_accel_v128_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_126d_accel_v129_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_252d_accel_v130_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_252d_accel_v131_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_252d_accel_v132_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_504d_accel_v133_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_504d_accel_v134_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq revisioncount
def rarp_f080_restatement_and_revision_proxy_sq_504d_accel_v135_signal(revisioncount, closeadj):
    base = _mean(revisioncount * revisioncount, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_21d_accel_v136_signal(revisioncount):
    base = _z(revisioncount, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_21d_accel_v137_signal(revisioncount):
    base = _z(revisioncount, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_21d_accel_v138_signal(revisioncount):
    base = _z(revisioncount, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_63d_accel_v139_signal(revisioncount):
    base = _z(revisioncount, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_63d_accel_v140_signal(revisioncount):
    base = _z(revisioncount, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_63d_accel_v141_signal(revisioncount):
    base = _z(revisioncount, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_126d_accel_v142_signal(revisioncount):
    base = _z(revisioncount, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_126d_accel_v143_signal(revisioncount):
    base = _z(revisioncount, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_126d_accel_v144_signal(revisioncount):
    base = _z(revisioncount, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_252d_accel_v145_signal(revisioncount):
    base = _z(revisioncount, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_252d_accel_v146_signal(revisioncount):
    base = _z(revisioncount, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_252d_accel_v147_signal(revisioncount):
    base = _z(revisioncount, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_504d_accel_v148_signal(revisioncount):
    base = _z(revisioncount, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_504d_accel_v149_signal(revisioncount):
    base = _z(revisioncount, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z revisioncount
def rarp_f080_restatement_and_revision_proxy_z_504d_accel_v150_signal(revisioncount):
    base = _z(revisioncount, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
