"""Family f093 - Insider role and cluster behavior (Insiders and Ownership) | Sharadar tables: SF2 | fields: ownername, officertitle, isdirector, isofficer, transactiondate | 2nd derivatives 001-150"""
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
def _insider_role_clusters_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_role_clusters_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_role_clusters_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw isdirector
def irc_f093_insider_role_clusters_raw_21d_slope_v001_signal(isdirector, closeadj):
    base = _mean(isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw isdirector
def irc_f093_insider_role_clusters_raw_21d_slope_v002_signal(isdirector, closeadj):
    base = _mean(isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw isdirector
def irc_f093_insider_role_clusters_raw_21d_slope_v003_signal(isdirector, closeadj):
    base = _mean(isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw isdirector
def irc_f093_insider_role_clusters_raw_63d_slope_v004_signal(isdirector, closeadj):
    base = _mean(isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw isdirector
def irc_f093_insider_role_clusters_raw_63d_slope_v005_signal(isdirector, closeadj):
    base = _mean(isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw isdirector
def irc_f093_insider_role_clusters_raw_63d_slope_v006_signal(isdirector, closeadj):
    base = _mean(isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw isdirector
def irc_f093_insider_role_clusters_raw_126d_slope_v007_signal(isdirector, closeadj):
    base = _mean(isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw isdirector
def irc_f093_insider_role_clusters_raw_126d_slope_v008_signal(isdirector, closeadj):
    base = _mean(isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw isdirector
def irc_f093_insider_role_clusters_raw_126d_slope_v009_signal(isdirector, closeadj):
    base = _mean(isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw isdirector
def irc_f093_insider_role_clusters_raw_252d_slope_v010_signal(isdirector, closeadj):
    base = _mean(isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw isdirector
def irc_f093_insider_role_clusters_raw_252d_slope_v011_signal(isdirector, closeadj):
    base = _mean(isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw isdirector
def irc_f093_insider_role_clusters_raw_252d_slope_v012_signal(isdirector, closeadj):
    base = _mean(isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw isdirector
def irc_f093_insider_role_clusters_raw_504d_slope_v013_signal(isdirector, closeadj):
    base = _mean(isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw isdirector
def irc_f093_insider_role_clusters_raw_504d_slope_v014_signal(isdirector, closeadj):
    base = _mean(isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw isdirector
def irc_f093_insider_role_clusters_raw_504d_slope_v015_signal(isdirector, closeadj):
    base = _mean(isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log isdirector
def irc_f093_insider_role_clusters_log_21d_slope_v016_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log isdirector
def irc_f093_insider_role_clusters_log_21d_slope_v017_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log isdirector
def irc_f093_insider_role_clusters_log_21d_slope_v018_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log isdirector
def irc_f093_insider_role_clusters_log_63d_slope_v019_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log isdirector
def irc_f093_insider_role_clusters_log_63d_slope_v020_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log isdirector
def irc_f093_insider_role_clusters_log_63d_slope_v021_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log isdirector
def irc_f093_insider_role_clusters_log_126d_slope_v022_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log isdirector
def irc_f093_insider_role_clusters_log_126d_slope_v023_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log isdirector
def irc_f093_insider_role_clusters_log_126d_slope_v024_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log isdirector
def irc_f093_insider_role_clusters_log_252d_slope_v025_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log isdirector
def irc_f093_insider_role_clusters_log_252d_slope_v026_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log isdirector
def irc_f093_insider_role_clusters_log_252d_slope_v027_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log isdirector
def irc_f093_insider_role_clusters_log_504d_slope_v028_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log isdirector
def irc_f093_insider_role_clusters_log_504d_slope_v029_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log isdirector
def irc_f093_insider_role_clusters_log_504d_slope_v030_signal(isdirector, closeadj):
    base = _mean(_insider_role_clusters_log(isdirector), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare isdirector
def irc_f093_insider_role_clusters_pershare_21d_slope_v031_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare isdirector
def irc_f093_insider_role_clusters_pershare_21d_slope_v032_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare isdirector
def irc_f093_insider_role_clusters_pershare_21d_slope_v033_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare isdirector
def irc_f093_insider_role_clusters_pershare_63d_slope_v034_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare isdirector
def irc_f093_insider_role_clusters_pershare_63d_slope_v035_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare isdirector
def irc_f093_insider_role_clusters_pershare_63d_slope_v036_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare isdirector
def irc_f093_insider_role_clusters_pershare_126d_slope_v037_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare isdirector
def irc_f093_insider_role_clusters_pershare_126d_slope_v038_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare isdirector
def irc_f093_insider_role_clusters_pershare_126d_slope_v039_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare isdirector
def irc_f093_insider_role_clusters_pershare_252d_slope_v040_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare isdirector
def irc_f093_insider_role_clusters_pershare_252d_slope_v041_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare isdirector
def irc_f093_insider_role_clusters_pershare_252d_slope_v042_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare isdirector
def irc_f093_insider_role_clusters_pershare_504d_slope_v043_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare isdirector
def irc_f093_insider_role_clusters_pershare_504d_slope_v044_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare isdirector
def irc_f093_insider_role_clusters_pershare_504d_slope_v045_signal(isdirector, sharesbas, closeadj):
    base = _mean(_insider_role_clusters_per_share(isdirector, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_21d_slope_v046_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_21d_slope_v047_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_21d_slope_v048_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_63d_slope_v049_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_63d_slope_v050_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_63d_slope_v051_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_126d_slope_v052_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_126d_slope_v053_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_126d_slope_v054_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_252d_slope_v055_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_252d_slope_v056_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_252d_slope_v057_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_504d_slope_v058_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_504d_slope_v059_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_isofficer isdirector
def irc_f093_insider_role_clusters_per_isofficer_504d_slope_v060_signal(isdirector, isofficer):
    base = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_21d_slope_v061_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_21d_slope_v062_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_21d_slope_v063_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_63d_slope_v064_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_63d_slope_v065_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_63d_slope_v066_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_126d_slope_v067_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_126d_slope_v068_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_126d_slope_v069_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_252d_slope_v070_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_252d_slope_v071_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_252d_slope_v072_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_504d_slope_v073_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_504d_slope_v074_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_transactiondate isdirector
def irc_f093_insider_role_clusters_per_transactiondate_504d_slope_v075_signal(isdirector, transactiondate):
    base = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_21d_slope_v076_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_21d_slope_v077_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_21d_slope_v078_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_63d_slope_v079_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_63d_slope_v080_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_63d_slope_v081_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_126d_slope_v082_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_126d_slope_v083_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_126d_slope_v084_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_252d_slope_v085_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_252d_slope_v086_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_252d_slope_v087_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_504d_slope_v088_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_504d_slope_v089_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets isdirector
def irc_f093_insider_role_clusters_per_assets_504d_slope_v090_signal(isdirector, assets):
    base = _mean(_insider_role_clusters_scaled(isdirector, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std isdirector
def irc_f093_insider_role_clusters_std_21d_slope_v091_signal(isdirector, closeadj):
    base = _std(isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std isdirector
def irc_f093_insider_role_clusters_std_21d_slope_v092_signal(isdirector, closeadj):
    base = _std(isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std isdirector
def irc_f093_insider_role_clusters_std_21d_slope_v093_signal(isdirector, closeadj):
    base = _std(isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std isdirector
def irc_f093_insider_role_clusters_std_63d_slope_v094_signal(isdirector, closeadj):
    base = _std(isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std isdirector
def irc_f093_insider_role_clusters_std_63d_slope_v095_signal(isdirector, closeadj):
    base = _std(isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std isdirector
def irc_f093_insider_role_clusters_std_63d_slope_v096_signal(isdirector, closeadj):
    base = _std(isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std isdirector
def irc_f093_insider_role_clusters_std_126d_slope_v097_signal(isdirector, closeadj):
    base = _std(isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std isdirector
def irc_f093_insider_role_clusters_std_126d_slope_v098_signal(isdirector, closeadj):
    base = _std(isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std isdirector
def irc_f093_insider_role_clusters_std_126d_slope_v099_signal(isdirector, closeadj):
    base = _std(isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std isdirector
def irc_f093_insider_role_clusters_std_252d_slope_v100_signal(isdirector, closeadj):
    base = _std(isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std isdirector
def irc_f093_insider_role_clusters_std_252d_slope_v101_signal(isdirector, closeadj):
    base = _std(isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std isdirector
def irc_f093_insider_role_clusters_std_252d_slope_v102_signal(isdirector, closeadj):
    base = _std(isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std isdirector
def irc_f093_insider_role_clusters_std_504d_slope_v103_signal(isdirector, closeadj):
    base = _std(isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std isdirector
def irc_f093_insider_role_clusters_std_504d_slope_v104_signal(isdirector, closeadj):
    base = _std(isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std isdirector
def irc_f093_insider_role_clusters_std_504d_slope_v105_signal(isdirector, closeadj):
    base = _std(isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm isdirector
def irc_f093_insider_role_clusters_ewm_21d_slope_v106_signal(isdirector, closeadj):
    base = isdirector.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm isdirector
def irc_f093_insider_role_clusters_ewm_21d_slope_v107_signal(isdirector, closeadj):
    base = isdirector.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm isdirector
def irc_f093_insider_role_clusters_ewm_21d_slope_v108_signal(isdirector, closeadj):
    base = isdirector.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm isdirector
def irc_f093_insider_role_clusters_ewm_63d_slope_v109_signal(isdirector, closeadj):
    base = isdirector.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm isdirector
def irc_f093_insider_role_clusters_ewm_63d_slope_v110_signal(isdirector, closeadj):
    base = isdirector.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm isdirector
def irc_f093_insider_role_clusters_ewm_63d_slope_v111_signal(isdirector, closeadj):
    base = isdirector.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm isdirector
def irc_f093_insider_role_clusters_ewm_126d_slope_v112_signal(isdirector, closeadj):
    base = isdirector.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm isdirector
def irc_f093_insider_role_clusters_ewm_126d_slope_v113_signal(isdirector, closeadj):
    base = isdirector.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm isdirector
def irc_f093_insider_role_clusters_ewm_126d_slope_v114_signal(isdirector, closeadj):
    base = isdirector.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm isdirector
def irc_f093_insider_role_clusters_ewm_252d_slope_v115_signal(isdirector, closeadj):
    base = isdirector.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm isdirector
def irc_f093_insider_role_clusters_ewm_252d_slope_v116_signal(isdirector, closeadj):
    base = isdirector.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm isdirector
def irc_f093_insider_role_clusters_ewm_252d_slope_v117_signal(isdirector, closeadj):
    base = isdirector.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm isdirector
def irc_f093_insider_role_clusters_ewm_504d_slope_v118_signal(isdirector, closeadj):
    base = isdirector.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm isdirector
def irc_f093_insider_role_clusters_ewm_504d_slope_v119_signal(isdirector, closeadj):
    base = isdirector.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm isdirector
def irc_f093_insider_role_clusters_ewm_504d_slope_v120_signal(isdirector, closeadj):
    base = isdirector.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq isdirector
def irc_f093_insider_role_clusters_sq_21d_slope_v121_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq isdirector
def irc_f093_insider_role_clusters_sq_21d_slope_v122_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq isdirector
def irc_f093_insider_role_clusters_sq_21d_slope_v123_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq isdirector
def irc_f093_insider_role_clusters_sq_63d_slope_v124_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq isdirector
def irc_f093_insider_role_clusters_sq_63d_slope_v125_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq isdirector
def irc_f093_insider_role_clusters_sq_63d_slope_v126_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq isdirector
def irc_f093_insider_role_clusters_sq_126d_slope_v127_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq isdirector
def irc_f093_insider_role_clusters_sq_126d_slope_v128_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq isdirector
def irc_f093_insider_role_clusters_sq_126d_slope_v129_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq isdirector
def irc_f093_insider_role_clusters_sq_252d_slope_v130_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq isdirector
def irc_f093_insider_role_clusters_sq_252d_slope_v131_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq isdirector
def irc_f093_insider_role_clusters_sq_252d_slope_v132_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq isdirector
def irc_f093_insider_role_clusters_sq_504d_slope_v133_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq isdirector
def irc_f093_insider_role_clusters_sq_504d_slope_v134_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq isdirector
def irc_f093_insider_role_clusters_sq_504d_slope_v135_signal(isdirector, closeadj):
    base = _mean(isdirector * isdirector, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z isdirector
def irc_f093_insider_role_clusters_z_21d_slope_v136_signal(isdirector):
    base = _z(isdirector, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z isdirector
def irc_f093_insider_role_clusters_z_21d_slope_v137_signal(isdirector):
    base = _z(isdirector, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z isdirector
def irc_f093_insider_role_clusters_z_21d_slope_v138_signal(isdirector):
    base = _z(isdirector, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z isdirector
def irc_f093_insider_role_clusters_z_63d_slope_v139_signal(isdirector):
    base = _z(isdirector, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z isdirector
def irc_f093_insider_role_clusters_z_63d_slope_v140_signal(isdirector):
    base = _z(isdirector, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z isdirector
def irc_f093_insider_role_clusters_z_63d_slope_v141_signal(isdirector):
    base = _z(isdirector, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z isdirector
def irc_f093_insider_role_clusters_z_126d_slope_v142_signal(isdirector):
    base = _z(isdirector, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z isdirector
def irc_f093_insider_role_clusters_z_126d_slope_v143_signal(isdirector):
    base = _z(isdirector, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z isdirector
def irc_f093_insider_role_clusters_z_126d_slope_v144_signal(isdirector):
    base = _z(isdirector, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z isdirector
def irc_f093_insider_role_clusters_z_252d_slope_v145_signal(isdirector):
    base = _z(isdirector, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z isdirector
def irc_f093_insider_role_clusters_z_252d_slope_v146_signal(isdirector):
    base = _z(isdirector, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z isdirector
def irc_f093_insider_role_clusters_z_252d_slope_v147_signal(isdirector):
    base = _z(isdirector, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z isdirector
def irc_f093_insider_role_clusters_z_504d_slope_v148_signal(isdirector):
    base = _z(isdirector, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z isdirector
def irc_f093_insider_role_clusters_z_504d_slope_v149_signal(isdirector):
    base = _z(isdirector, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z isdirector
def irc_f093_insider_role_clusters_z_504d_slope_v150_signal(isdirector):
    base = _z(isdirector, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
