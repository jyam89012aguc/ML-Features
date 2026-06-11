"""Family f092 - Insider transaction net flow (Insiders and Ownership) | Sharadar tables: SF2 | fields: transactioncode, transactionshares, transactionvalue, transactionpricepershare | 2nd derivatives 001-150"""
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
def _insider_transaction_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_transaction_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_transaction_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw transactioncode
def itf_f092_insider_transaction_flow_raw_21d_slope_v001_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw transactioncode
def itf_f092_insider_transaction_flow_raw_21d_slope_v002_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw transactioncode
def itf_f092_insider_transaction_flow_raw_21d_slope_v003_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw transactioncode
def itf_f092_insider_transaction_flow_raw_63d_slope_v004_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw transactioncode
def itf_f092_insider_transaction_flow_raw_63d_slope_v005_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw transactioncode
def itf_f092_insider_transaction_flow_raw_63d_slope_v006_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw transactioncode
def itf_f092_insider_transaction_flow_raw_126d_slope_v007_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw transactioncode
def itf_f092_insider_transaction_flow_raw_126d_slope_v008_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw transactioncode
def itf_f092_insider_transaction_flow_raw_126d_slope_v009_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw transactioncode
def itf_f092_insider_transaction_flow_raw_252d_slope_v010_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw transactioncode
def itf_f092_insider_transaction_flow_raw_252d_slope_v011_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw transactioncode
def itf_f092_insider_transaction_flow_raw_252d_slope_v012_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw transactioncode
def itf_f092_insider_transaction_flow_raw_504d_slope_v013_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw transactioncode
def itf_f092_insider_transaction_flow_raw_504d_slope_v014_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw transactioncode
def itf_f092_insider_transaction_flow_raw_504d_slope_v015_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log transactioncode
def itf_f092_insider_transaction_flow_log_21d_slope_v016_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log transactioncode
def itf_f092_insider_transaction_flow_log_21d_slope_v017_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log transactioncode
def itf_f092_insider_transaction_flow_log_21d_slope_v018_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log transactioncode
def itf_f092_insider_transaction_flow_log_63d_slope_v019_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log transactioncode
def itf_f092_insider_transaction_flow_log_63d_slope_v020_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log transactioncode
def itf_f092_insider_transaction_flow_log_63d_slope_v021_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log transactioncode
def itf_f092_insider_transaction_flow_log_126d_slope_v022_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log transactioncode
def itf_f092_insider_transaction_flow_log_126d_slope_v023_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log transactioncode
def itf_f092_insider_transaction_flow_log_126d_slope_v024_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log transactioncode
def itf_f092_insider_transaction_flow_log_252d_slope_v025_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log transactioncode
def itf_f092_insider_transaction_flow_log_252d_slope_v026_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log transactioncode
def itf_f092_insider_transaction_flow_log_252d_slope_v027_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log transactioncode
def itf_f092_insider_transaction_flow_log_504d_slope_v028_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log transactioncode
def itf_f092_insider_transaction_flow_log_504d_slope_v029_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log transactioncode
def itf_f092_insider_transaction_flow_log_504d_slope_v030_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_21d_slope_v031_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_21d_slope_v032_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_21d_slope_v033_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_63d_slope_v034_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_63d_slope_v035_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_63d_slope_v036_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_126d_slope_v037_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_126d_slope_v038_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_126d_slope_v039_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_252d_slope_v040_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_252d_slope_v041_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_252d_slope_v042_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_504d_slope_v043_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_504d_slope_v044_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_504d_slope_v045_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_21d_slope_v046_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_21d_slope_v047_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_21d_slope_v048_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_63d_slope_v049_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_63d_slope_v050_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_63d_slope_v051_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_126d_slope_v052_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_126d_slope_v053_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_126d_slope_v054_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_252d_slope_v055_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_252d_slope_v056_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_252d_slope_v057_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_504d_slope_v058_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_504d_slope_v059_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_504d_slope_v060_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_21d_slope_v061_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_21d_slope_v062_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_21d_slope_v063_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_63d_slope_v064_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_63d_slope_v065_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_63d_slope_v066_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_126d_slope_v067_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_126d_slope_v068_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_126d_slope_v069_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_252d_slope_v070_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_252d_slope_v071_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_252d_slope_v072_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_504d_slope_v073_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_504d_slope_v074_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_504d_slope_v075_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_21d_slope_v076_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_21d_slope_v077_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_21d_slope_v078_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_63d_slope_v079_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_63d_slope_v080_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_63d_slope_v081_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_126d_slope_v082_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_126d_slope_v083_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_126d_slope_v084_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_252d_slope_v085_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_252d_slope_v086_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_252d_slope_v087_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_504d_slope_v088_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_504d_slope_v089_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_504d_slope_v090_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std transactioncode
def itf_f092_insider_transaction_flow_std_21d_slope_v091_signal(transactioncode, closeadj):
    base = _std(transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std transactioncode
def itf_f092_insider_transaction_flow_std_21d_slope_v092_signal(transactioncode, closeadj):
    base = _std(transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std transactioncode
def itf_f092_insider_transaction_flow_std_21d_slope_v093_signal(transactioncode, closeadj):
    base = _std(transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std transactioncode
def itf_f092_insider_transaction_flow_std_63d_slope_v094_signal(transactioncode, closeadj):
    base = _std(transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std transactioncode
def itf_f092_insider_transaction_flow_std_63d_slope_v095_signal(transactioncode, closeadj):
    base = _std(transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std transactioncode
def itf_f092_insider_transaction_flow_std_63d_slope_v096_signal(transactioncode, closeadj):
    base = _std(transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std transactioncode
def itf_f092_insider_transaction_flow_std_126d_slope_v097_signal(transactioncode, closeadj):
    base = _std(transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std transactioncode
def itf_f092_insider_transaction_flow_std_126d_slope_v098_signal(transactioncode, closeadj):
    base = _std(transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std transactioncode
def itf_f092_insider_transaction_flow_std_126d_slope_v099_signal(transactioncode, closeadj):
    base = _std(transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std transactioncode
def itf_f092_insider_transaction_flow_std_252d_slope_v100_signal(transactioncode, closeadj):
    base = _std(transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std transactioncode
def itf_f092_insider_transaction_flow_std_252d_slope_v101_signal(transactioncode, closeadj):
    base = _std(transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std transactioncode
def itf_f092_insider_transaction_flow_std_252d_slope_v102_signal(transactioncode, closeadj):
    base = _std(transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std transactioncode
def itf_f092_insider_transaction_flow_std_504d_slope_v103_signal(transactioncode, closeadj):
    base = _std(transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std transactioncode
def itf_f092_insider_transaction_flow_std_504d_slope_v104_signal(transactioncode, closeadj):
    base = _std(transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std transactioncode
def itf_f092_insider_transaction_flow_std_504d_slope_v105_signal(transactioncode, closeadj):
    base = _std(transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_21d_slope_v106_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_21d_slope_v107_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_21d_slope_v108_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_63d_slope_v109_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_63d_slope_v110_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_63d_slope_v111_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_126d_slope_v112_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_126d_slope_v113_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_126d_slope_v114_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_252d_slope_v115_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_252d_slope_v116_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_252d_slope_v117_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_504d_slope_v118_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_504d_slope_v119_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_504d_slope_v120_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq transactioncode
def itf_f092_insider_transaction_flow_sq_21d_slope_v121_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq transactioncode
def itf_f092_insider_transaction_flow_sq_21d_slope_v122_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq transactioncode
def itf_f092_insider_transaction_flow_sq_21d_slope_v123_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq transactioncode
def itf_f092_insider_transaction_flow_sq_63d_slope_v124_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq transactioncode
def itf_f092_insider_transaction_flow_sq_63d_slope_v125_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq transactioncode
def itf_f092_insider_transaction_flow_sq_63d_slope_v126_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq transactioncode
def itf_f092_insider_transaction_flow_sq_126d_slope_v127_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq transactioncode
def itf_f092_insider_transaction_flow_sq_126d_slope_v128_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq transactioncode
def itf_f092_insider_transaction_flow_sq_126d_slope_v129_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq transactioncode
def itf_f092_insider_transaction_flow_sq_252d_slope_v130_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq transactioncode
def itf_f092_insider_transaction_flow_sq_252d_slope_v131_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq transactioncode
def itf_f092_insider_transaction_flow_sq_252d_slope_v132_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq transactioncode
def itf_f092_insider_transaction_flow_sq_504d_slope_v133_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq transactioncode
def itf_f092_insider_transaction_flow_sq_504d_slope_v134_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq transactioncode
def itf_f092_insider_transaction_flow_sq_504d_slope_v135_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z transactioncode
def itf_f092_insider_transaction_flow_z_21d_slope_v136_signal(transactioncode):
    base = _z(transactioncode, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z transactioncode
def itf_f092_insider_transaction_flow_z_21d_slope_v137_signal(transactioncode):
    base = _z(transactioncode, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z transactioncode
def itf_f092_insider_transaction_flow_z_21d_slope_v138_signal(transactioncode):
    base = _z(transactioncode, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z transactioncode
def itf_f092_insider_transaction_flow_z_63d_slope_v139_signal(transactioncode):
    base = _z(transactioncode, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z transactioncode
def itf_f092_insider_transaction_flow_z_63d_slope_v140_signal(transactioncode):
    base = _z(transactioncode, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z transactioncode
def itf_f092_insider_transaction_flow_z_63d_slope_v141_signal(transactioncode):
    base = _z(transactioncode, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z transactioncode
def itf_f092_insider_transaction_flow_z_126d_slope_v142_signal(transactioncode):
    base = _z(transactioncode, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z transactioncode
def itf_f092_insider_transaction_flow_z_126d_slope_v143_signal(transactioncode):
    base = _z(transactioncode, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z transactioncode
def itf_f092_insider_transaction_flow_z_126d_slope_v144_signal(transactioncode):
    base = _z(transactioncode, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z transactioncode
def itf_f092_insider_transaction_flow_z_252d_slope_v145_signal(transactioncode):
    base = _z(transactioncode, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z transactioncode
def itf_f092_insider_transaction_flow_z_252d_slope_v146_signal(transactioncode):
    base = _z(transactioncode, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z transactioncode
def itf_f092_insider_transaction_flow_z_252d_slope_v147_signal(transactioncode):
    base = _z(transactioncode, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z transactioncode
def itf_f092_insider_transaction_flow_z_504d_slope_v148_signal(transactioncode):
    base = _z(transactioncode, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z transactioncode
def itf_f092_insider_transaction_flow_z_504d_slope_v149_signal(transactioncode):
    base = _z(transactioncode, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z transactioncode
def itf_f092_insider_transaction_flow_z_504d_slope_v150_signal(transactioncode):
    base = _z(transactioncode, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
