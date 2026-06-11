"""Family f092 - Insider transaction net flow (Insiders and Ownership) | Sharadar tables: SF2 | fields: transactioncode, transactionshares, transactionvalue, transactionpricepershare | 3rd derivatives 001-150"""
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


# 5d accel of 21d raw transactioncode
def itf_f092_insider_transaction_flow_raw_21d_accel_v001_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw transactioncode
def itf_f092_insider_transaction_flow_raw_21d_accel_v002_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw transactioncode
def itf_f092_insider_transaction_flow_raw_21d_accel_v003_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw transactioncode
def itf_f092_insider_transaction_flow_raw_63d_accel_v004_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw transactioncode
def itf_f092_insider_transaction_flow_raw_63d_accel_v005_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw transactioncode
def itf_f092_insider_transaction_flow_raw_63d_accel_v006_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw transactioncode
def itf_f092_insider_transaction_flow_raw_126d_accel_v007_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw transactioncode
def itf_f092_insider_transaction_flow_raw_126d_accel_v008_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw transactioncode
def itf_f092_insider_transaction_flow_raw_126d_accel_v009_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw transactioncode
def itf_f092_insider_transaction_flow_raw_252d_accel_v010_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw transactioncode
def itf_f092_insider_transaction_flow_raw_252d_accel_v011_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw transactioncode
def itf_f092_insider_transaction_flow_raw_252d_accel_v012_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw transactioncode
def itf_f092_insider_transaction_flow_raw_504d_accel_v013_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw transactioncode
def itf_f092_insider_transaction_flow_raw_504d_accel_v014_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw transactioncode
def itf_f092_insider_transaction_flow_raw_504d_accel_v015_signal(transactioncode, closeadj):
    base = _mean(transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log transactioncode
def itf_f092_insider_transaction_flow_log_21d_accel_v016_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log transactioncode
def itf_f092_insider_transaction_flow_log_21d_accel_v017_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log transactioncode
def itf_f092_insider_transaction_flow_log_21d_accel_v018_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log transactioncode
def itf_f092_insider_transaction_flow_log_63d_accel_v019_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log transactioncode
def itf_f092_insider_transaction_flow_log_63d_accel_v020_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log transactioncode
def itf_f092_insider_transaction_flow_log_63d_accel_v021_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log transactioncode
def itf_f092_insider_transaction_flow_log_126d_accel_v022_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log transactioncode
def itf_f092_insider_transaction_flow_log_126d_accel_v023_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log transactioncode
def itf_f092_insider_transaction_flow_log_126d_accel_v024_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log transactioncode
def itf_f092_insider_transaction_flow_log_252d_accel_v025_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log transactioncode
def itf_f092_insider_transaction_flow_log_252d_accel_v026_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log transactioncode
def itf_f092_insider_transaction_flow_log_252d_accel_v027_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log transactioncode
def itf_f092_insider_transaction_flow_log_504d_accel_v028_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log transactioncode
def itf_f092_insider_transaction_flow_log_504d_accel_v029_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log transactioncode
def itf_f092_insider_transaction_flow_log_504d_accel_v030_signal(transactioncode, closeadj):
    base = _mean(_insider_transaction_flow_log(transactioncode), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_21d_accel_v031_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_21d_accel_v032_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_21d_accel_v033_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_63d_accel_v034_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_63d_accel_v035_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_63d_accel_v036_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_126d_accel_v037_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_126d_accel_v038_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_126d_accel_v039_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_252d_accel_v040_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_252d_accel_v041_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_252d_accel_v042_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_504d_accel_v043_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_504d_accel_v044_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare transactioncode
def itf_f092_insider_transaction_flow_pershare_504d_accel_v045_signal(transactioncode, sharesbas, closeadj):
    base = _mean(_insider_transaction_flow_per_share(transactioncode, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_21d_accel_v046_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_21d_accel_v047_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_21d_accel_v048_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_63d_accel_v049_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_63d_accel_v050_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_63d_accel_v051_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_126d_accel_v052_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_126d_accel_v053_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_126d_accel_v054_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_252d_accel_v055_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_252d_accel_v056_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_252d_accel_v057_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_504d_accel_v058_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_504d_accel_v059_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_transactionshares transactioncode
def itf_f092_insider_transaction_flow_per_transactionshares_504d_accel_v060_signal(transactioncode, transactionshares):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_21d_accel_v061_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_21d_accel_v062_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_21d_accel_v063_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_63d_accel_v064_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_63d_accel_v065_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_63d_accel_v066_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_126d_accel_v067_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_126d_accel_v068_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_126d_accel_v069_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_252d_accel_v070_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_252d_accel_v071_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_252d_accel_v072_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_504d_accel_v073_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_504d_accel_v074_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_transactionvalue transactioncode
def itf_f092_insider_transaction_flow_per_transactionvalue_504d_accel_v075_signal(transactioncode, transactionvalue):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_21d_accel_v076_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_21d_accel_v077_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_21d_accel_v078_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_63d_accel_v079_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_63d_accel_v080_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_63d_accel_v081_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_126d_accel_v082_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_126d_accel_v083_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_126d_accel_v084_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_252d_accel_v085_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_252d_accel_v086_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_252d_accel_v087_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_504d_accel_v088_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_504d_accel_v089_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_transactionprice transactioncode
def itf_f092_insider_transaction_flow_per_transactionprice_504d_accel_v090_signal(transactioncode, transactionpricepershare):
    base = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std transactioncode
def itf_f092_insider_transaction_flow_std_21d_accel_v091_signal(transactioncode, closeadj):
    base = _std(transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std transactioncode
def itf_f092_insider_transaction_flow_std_21d_accel_v092_signal(transactioncode, closeadj):
    base = _std(transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std transactioncode
def itf_f092_insider_transaction_flow_std_21d_accel_v093_signal(transactioncode, closeadj):
    base = _std(transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std transactioncode
def itf_f092_insider_transaction_flow_std_63d_accel_v094_signal(transactioncode, closeadj):
    base = _std(transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std transactioncode
def itf_f092_insider_transaction_flow_std_63d_accel_v095_signal(transactioncode, closeadj):
    base = _std(transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std transactioncode
def itf_f092_insider_transaction_flow_std_63d_accel_v096_signal(transactioncode, closeadj):
    base = _std(transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std transactioncode
def itf_f092_insider_transaction_flow_std_126d_accel_v097_signal(transactioncode, closeadj):
    base = _std(transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std transactioncode
def itf_f092_insider_transaction_flow_std_126d_accel_v098_signal(transactioncode, closeadj):
    base = _std(transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std transactioncode
def itf_f092_insider_transaction_flow_std_126d_accel_v099_signal(transactioncode, closeadj):
    base = _std(transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std transactioncode
def itf_f092_insider_transaction_flow_std_252d_accel_v100_signal(transactioncode, closeadj):
    base = _std(transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std transactioncode
def itf_f092_insider_transaction_flow_std_252d_accel_v101_signal(transactioncode, closeadj):
    base = _std(transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std transactioncode
def itf_f092_insider_transaction_flow_std_252d_accel_v102_signal(transactioncode, closeadj):
    base = _std(transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std transactioncode
def itf_f092_insider_transaction_flow_std_504d_accel_v103_signal(transactioncode, closeadj):
    base = _std(transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std transactioncode
def itf_f092_insider_transaction_flow_std_504d_accel_v104_signal(transactioncode, closeadj):
    base = _std(transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std transactioncode
def itf_f092_insider_transaction_flow_std_504d_accel_v105_signal(transactioncode, closeadj):
    base = _std(transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_21d_accel_v106_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_21d_accel_v107_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_21d_accel_v108_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_63d_accel_v109_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_63d_accel_v110_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_63d_accel_v111_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_126d_accel_v112_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_126d_accel_v113_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_126d_accel_v114_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_252d_accel_v115_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_252d_accel_v116_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_252d_accel_v117_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_504d_accel_v118_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_504d_accel_v119_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm transactioncode
def itf_f092_insider_transaction_flow_ewm_504d_accel_v120_signal(transactioncode, closeadj):
    base = transactioncode.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq transactioncode
def itf_f092_insider_transaction_flow_sq_21d_accel_v121_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq transactioncode
def itf_f092_insider_transaction_flow_sq_21d_accel_v122_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq transactioncode
def itf_f092_insider_transaction_flow_sq_21d_accel_v123_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq transactioncode
def itf_f092_insider_transaction_flow_sq_63d_accel_v124_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq transactioncode
def itf_f092_insider_transaction_flow_sq_63d_accel_v125_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq transactioncode
def itf_f092_insider_transaction_flow_sq_63d_accel_v126_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq transactioncode
def itf_f092_insider_transaction_flow_sq_126d_accel_v127_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq transactioncode
def itf_f092_insider_transaction_flow_sq_126d_accel_v128_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq transactioncode
def itf_f092_insider_transaction_flow_sq_126d_accel_v129_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq transactioncode
def itf_f092_insider_transaction_flow_sq_252d_accel_v130_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq transactioncode
def itf_f092_insider_transaction_flow_sq_252d_accel_v131_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq transactioncode
def itf_f092_insider_transaction_flow_sq_252d_accel_v132_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq transactioncode
def itf_f092_insider_transaction_flow_sq_504d_accel_v133_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq transactioncode
def itf_f092_insider_transaction_flow_sq_504d_accel_v134_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq transactioncode
def itf_f092_insider_transaction_flow_sq_504d_accel_v135_signal(transactioncode, closeadj):
    base = _mean(transactioncode * transactioncode, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z transactioncode
def itf_f092_insider_transaction_flow_z_21d_accel_v136_signal(transactioncode):
    base = _z(transactioncode, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z transactioncode
def itf_f092_insider_transaction_flow_z_21d_accel_v137_signal(transactioncode):
    base = _z(transactioncode, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z transactioncode
def itf_f092_insider_transaction_flow_z_21d_accel_v138_signal(transactioncode):
    base = _z(transactioncode, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z transactioncode
def itf_f092_insider_transaction_flow_z_63d_accel_v139_signal(transactioncode):
    base = _z(transactioncode, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z transactioncode
def itf_f092_insider_transaction_flow_z_63d_accel_v140_signal(transactioncode):
    base = _z(transactioncode, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z transactioncode
def itf_f092_insider_transaction_flow_z_63d_accel_v141_signal(transactioncode):
    base = _z(transactioncode, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z transactioncode
def itf_f092_insider_transaction_flow_z_126d_accel_v142_signal(transactioncode):
    base = _z(transactioncode, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z transactioncode
def itf_f092_insider_transaction_flow_z_126d_accel_v143_signal(transactioncode):
    base = _z(transactioncode, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z transactioncode
def itf_f092_insider_transaction_flow_z_126d_accel_v144_signal(transactioncode):
    base = _z(transactioncode, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z transactioncode
def itf_f092_insider_transaction_flow_z_252d_accel_v145_signal(transactioncode):
    base = _z(transactioncode, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z transactioncode
def itf_f092_insider_transaction_flow_z_252d_accel_v146_signal(transactioncode):
    base = _z(transactioncode, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z transactioncode
def itf_f092_insider_transaction_flow_z_252d_accel_v147_signal(transactioncode):
    base = _z(transactioncode, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z transactioncode
def itf_f092_insider_transaction_flow_z_504d_accel_v148_signal(transactioncode):
    base = _z(transactioncode, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z transactioncode
def itf_f092_insider_transaction_flow_z_504d_accel_v149_signal(transactioncode):
    base = _z(transactioncode, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z transactioncode
def itf_f092_insider_transaction_flow_z_504d_accel_v150_signal(transactioncode):
    base = _z(transactioncode, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
