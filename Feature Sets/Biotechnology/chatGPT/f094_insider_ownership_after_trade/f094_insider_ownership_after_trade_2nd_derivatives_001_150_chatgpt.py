"""Family f094 - Post-transaction insider ownership (Insiders and Ownership) | Sharadar tables: SF2 | fields: sharesownedfollowingtransaction, transactionshares | 2nd derivatives 001-150"""
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
def _insider_ownership_after_trade_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_ownership_after_trade_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_ownership_after_trade_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_21d_slope_v001_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_21d_slope_v002_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_21d_slope_v003_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_63d_slope_v004_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_63d_slope_v005_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_63d_slope_v006_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_126d_slope_v007_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_126d_slope_v008_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_126d_slope_v009_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_252d_slope_v010_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_252d_slope_v011_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_252d_slope_v012_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_504d_slope_v013_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_504d_slope_v014_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_raw_504d_slope_v015_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_21d_slope_v016_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_21d_slope_v017_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_21d_slope_v018_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_63d_slope_v019_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_63d_slope_v020_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_63d_slope_v021_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_126d_slope_v022_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_126d_slope_v023_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_126d_slope_v024_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_252d_slope_v025_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_252d_slope_v026_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_252d_slope_v027_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_504d_slope_v028_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_504d_slope_v029_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_log_504d_slope_v030_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(_insider_ownership_after_trade_log(sharesownedfollowingtransaction), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_21d_slope_v031_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_21d_slope_v032_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_21d_slope_v033_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_63d_slope_v034_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_63d_slope_v035_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_63d_slope_v036_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_126d_slope_v037_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_126d_slope_v038_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_126d_slope_v039_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_252d_slope_v040_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_252d_slope_v041_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_252d_slope_v042_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_504d_slope_v043_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_504d_slope_v044_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_pershare_504d_slope_v045_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    base = _mean(_insider_ownership_after_trade_per_share(sharesownedfollowingtransaction, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_21d_slope_v046_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_21d_slope_v047_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_21d_slope_v048_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_63d_slope_v049_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_63d_slope_v050_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_63d_slope_v051_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_126d_slope_v052_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_126d_slope_v053_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_126d_slope_v054_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_252d_slope_v055_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_252d_slope_v056_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_252d_slope_v057_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_504d_slope_v058_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_504d_slope_v059_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_transactionshares sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_transactionshares_504d_slope_v060_signal(sharesownedfollowingtransaction, transactionshares):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_21d_slope_v061_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_21d_slope_v062_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_21d_slope_v063_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_63d_slope_v064_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_63d_slope_v065_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_63d_slope_v066_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_126d_slope_v067_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_126d_slope_v068_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_126d_slope_v069_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_252d_slope_v070_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_252d_slope_v071_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_252d_slope_v072_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_504d_slope_v073_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_504d_slope_v074_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_assets_504d_slope_v075_signal(sharesownedfollowingtransaction, assets):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_21d_slope_v076_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_21d_slope_v077_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_21d_slope_v078_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_63d_slope_v079_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_63d_slope_v080_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_63d_slope_v081_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_126d_slope_v082_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_126d_slope_v083_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_126d_slope_v084_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_252d_slope_v085_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_252d_slope_v086_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_252d_slope_v087_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_504d_slope_v088_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_504d_slope_v089_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_per_marketcap_504d_slope_v090_signal(sharesownedfollowingtransaction, marketcap):
    base = _mean(_insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_21d_slope_v091_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_21d_slope_v092_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_21d_slope_v093_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_63d_slope_v094_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_63d_slope_v095_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_63d_slope_v096_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_126d_slope_v097_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_126d_slope_v098_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_126d_slope_v099_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_252d_slope_v100_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_252d_slope_v101_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_252d_slope_v102_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_504d_slope_v103_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_504d_slope_v104_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_std_504d_slope_v105_signal(sharesownedfollowingtransaction, closeadj):
    base = _std(sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_21d_slope_v106_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_21d_slope_v107_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_21d_slope_v108_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_63d_slope_v109_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_63d_slope_v110_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_63d_slope_v111_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_126d_slope_v112_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_126d_slope_v113_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_126d_slope_v114_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_252d_slope_v115_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_252d_slope_v116_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_252d_slope_v117_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_504d_slope_v118_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_504d_slope_v119_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_ewm_504d_slope_v120_signal(sharesownedfollowingtransaction, closeadj):
    base = sharesownedfollowingtransaction.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_21d_slope_v121_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_21d_slope_v122_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_21d_slope_v123_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_63d_slope_v124_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_63d_slope_v125_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_63d_slope_v126_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_126d_slope_v127_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_126d_slope_v128_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_126d_slope_v129_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_252d_slope_v130_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_252d_slope_v131_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_252d_slope_v132_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_504d_slope_v133_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_504d_slope_v134_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_sq_504d_slope_v135_signal(sharesownedfollowingtransaction, closeadj):
    base = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_21d_slope_v136_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_21d_slope_v137_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_21d_slope_v138_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_63d_slope_v139_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_63d_slope_v140_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_63d_slope_v141_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_126d_slope_v142_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_126d_slope_v143_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_126d_slope_v144_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_252d_slope_v145_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_252d_slope_v146_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_252d_slope_v147_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_504d_slope_v148_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_504d_slope_v149_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_504d_slope_v150_signal(sharesownedfollowingtransaction):
    base = _z(sharesownedfollowingtransaction, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
