"""Family f091 - Fund and ETF price context (Market Context from Sharadar Prices) | Sharadar tables: SFP | fields: date, ticker, close, closeadj, volume | 2nd derivatives 001-150"""
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
def _fund_prices_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _fund_prices_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _fund_prices_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw close
def fpc_f091_fund_prices_context_raw_21d_slope_v001_signal(close, closeadj):
    base = _mean(close, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw close
def fpc_f091_fund_prices_context_raw_21d_slope_v002_signal(close, closeadj):
    base = _mean(close, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw close
def fpc_f091_fund_prices_context_raw_21d_slope_v003_signal(close, closeadj):
    base = _mean(close, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw close
def fpc_f091_fund_prices_context_raw_63d_slope_v004_signal(close, closeadj):
    base = _mean(close, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw close
def fpc_f091_fund_prices_context_raw_63d_slope_v005_signal(close, closeadj):
    base = _mean(close, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw close
def fpc_f091_fund_prices_context_raw_63d_slope_v006_signal(close, closeadj):
    base = _mean(close, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw close
def fpc_f091_fund_prices_context_raw_126d_slope_v007_signal(close, closeadj):
    base = _mean(close, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw close
def fpc_f091_fund_prices_context_raw_126d_slope_v008_signal(close, closeadj):
    base = _mean(close, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw close
def fpc_f091_fund_prices_context_raw_126d_slope_v009_signal(close, closeadj):
    base = _mean(close, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw close
def fpc_f091_fund_prices_context_raw_252d_slope_v010_signal(close, closeadj):
    base = _mean(close, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw close
def fpc_f091_fund_prices_context_raw_252d_slope_v011_signal(close, closeadj):
    base = _mean(close, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw close
def fpc_f091_fund_prices_context_raw_252d_slope_v012_signal(close, closeadj):
    base = _mean(close, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw close
def fpc_f091_fund_prices_context_raw_504d_slope_v013_signal(close, closeadj):
    base = _mean(close, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw close
def fpc_f091_fund_prices_context_raw_504d_slope_v014_signal(close, closeadj):
    base = _mean(close, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw close
def fpc_f091_fund_prices_context_raw_504d_slope_v015_signal(close, closeadj):
    base = _mean(close, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log close
def fpc_f091_fund_prices_context_log_21d_slope_v016_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log close
def fpc_f091_fund_prices_context_log_21d_slope_v017_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log close
def fpc_f091_fund_prices_context_log_21d_slope_v018_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log close
def fpc_f091_fund_prices_context_log_63d_slope_v019_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log close
def fpc_f091_fund_prices_context_log_63d_slope_v020_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log close
def fpc_f091_fund_prices_context_log_63d_slope_v021_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log close
def fpc_f091_fund_prices_context_log_126d_slope_v022_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log close
def fpc_f091_fund_prices_context_log_126d_slope_v023_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log close
def fpc_f091_fund_prices_context_log_126d_slope_v024_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log close
def fpc_f091_fund_prices_context_log_252d_slope_v025_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log close
def fpc_f091_fund_prices_context_log_252d_slope_v026_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log close
def fpc_f091_fund_prices_context_log_252d_slope_v027_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log close
def fpc_f091_fund_prices_context_log_504d_slope_v028_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log close
def fpc_f091_fund_prices_context_log_504d_slope_v029_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log close
def fpc_f091_fund_prices_context_log_504d_slope_v030_signal(close, closeadj):
    base = _mean(_fund_prices_context_log(close), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare close
def fpc_f091_fund_prices_context_pershare_21d_slope_v031_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare close
def fpc_f091_fund_prices_context_pershare_21d_slope_v032_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare close
def fpc_f091_fund_prices_context_pershare_21d_slope_v033_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare close
def fpc_f091_fund_prices_context_pershare_63d_slope_v034_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare close
def fpc_f091_fund_prices_context_pershare_63d_slope_v035_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare close
def fpc_f091_fund_prices_context_pershare_63d_slope_v036_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare close
def fpc_f091_fund_prices_context_pershare_126d_slope_v037_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare close
def fpc_f091_fund_prices_context_pershare_126d_slope_v038_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare close
def fpc_f091_fund_prices_context_pershare_126d_slope_v039_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare close
def fpc_f091_fund_prices_context_pershare_252d_slope_v040_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare close
def fpc_f091_fund_prices_context_pershare_252d_slope_v041_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare close
def fpc_f091_fund_prices_context_pershare_252d_slope_v042_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare close
def fpc_f091_fund_prices_context_pershare_504d_slope_v043_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare close
def fpc_f091_fund_prices_context_pershare_504d_slope_v044_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare close
def fpc_f091_fund_prices_context_pershare_504d_slope_v045_signal(close, sharesbas, closeadj):
    base = _mean(_fund_prices_context_per_share(close, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_21d_slope_v046_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_21d_slope_v047_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_21d_slope_v048_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_63d_slope_v049_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_63d_slope_v050_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_63d_slope_v051_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_126d_slope_v052_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_126d_slope_v053_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_126d_slope_v054_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_252d_slope_v055_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_252d_slope_v056_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_252d_slope_v057_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_504d_slope_v058_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_504d_slope_v059_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_closeadj close
def fpc_f091_fund_prices_context_per_closeadj_504d_slope_v060_signal(close, closeadj):
    base = _mean(_fund_prices_context_scaled(close, closeadj), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_volume close
def fpc_f091_fund_prices_context_per_volume_21d_slope_v061_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_volume close
def fpc_f091_fund_prices_context_per_volume_21d_slope_v062_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_volume close
def fpc_f091_fund_prices_context_per_volume_21d_slope_v063_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_volume close
def fpc_f091_fund_prices_context_per_volume_63d_slope_v064_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_volume close
def fpc_f091_fund_prices_context_per_volume_63d_slope_v065_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_volume close
def fpc_f091_fund_prices_context_per_volume_63d_slope_v066_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_volume close
def fpc_f091_fund_prices_context_per_volume_126d_slope_v067_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_volume close
def fpc_f091_fund_prices_context_per_volume_126d_slope_v068_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_volume close
def fpc_f091_fund_prices_context_per_volume_126d_slope_v069_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_volume close
def fpc_f091_fund_prices_context_per_volume_252d_slope_v070_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_volume close
def fpc_f091_fund_prices_context_per_volume_252d_slope_v071_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_volume close
def fpc_f091_fund_prices_context_per_volume_252d_slope_v072_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_volume close
def fpc_f091_fund_prices_context_per_volume_504d_slope_v073_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_volume close
def fpc_f091_fund_prices_context_per_volume_504d_slope_v074_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_volume close
def fpc_f091_fund_prices_context_per_volume_504d_slope_v075_signal(close, volume):
    base = _mean(_fund_prices_context_scaled(close, volume), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets close
def fpc_f091_fund_prices_context_per_assets_21d_slope_v076_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets close
def fpc_f091_fund_prices_context_per_assets_21d_slope_v077_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets close
def fpc_f091_fund_prices_context_per_assets_21d_slope_v078_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets close
def fpc_f091_fund_prices_context_per_assets_63d_slope_v079_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets close
def fpc_f091_fund_prices_context_per_assets_63d_slope_v080_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets close
def fpc_f091_fund_prices_context_per_assets_63d_slope_v081_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets close
def fpc_f091_fund_prices_context_per_assets_126d_slope_v082_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets close
def fpc_f091_fund_prices_context_per_assets_126d_slope_v083_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets close
def fpc_f091_fund_prices_context_per_assets_126d_slope_v084_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets close
def fpc_f091_fund_prices_context_per_assets_252d_slope_v085_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets close
def fpc_f091_fund_prices_context_per_assets_252d_slope_v086_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets close
def fpc_f091_fund_prices_context_per_assets_252d_slope_v087_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets close
def fpc_f091_fund_prices_context_per_assets_504d_slope_v088_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets close
def fpc_f091_fund_prices_context_per_assets_504d_slope_v089_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets close
def fpc_f091_fund_prices_context_per_assets_504d_slope_v090_signal(close, assets):
    base = _mean(_fund_prices_context_scaled(close, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std close
def fpc_f091_fund_prices_context_std_21d_slope_v091_signal(close, closeadj):
    base = _std(close, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std close
def fpc_f091_fund_prices_context_std_21d_slope_v092_signal(close, closeadj):
    base = _std(close, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std close
def fpc_f091_fund_prices_context_std_21d_slope_v093_signal(close, closeadj):
    base = _std(close, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std close
def fpc_f091_fund_prices_context_std_63d_slope_v094_signal(close, closeadj):
    base = _std(close, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std close
def fpc_f091_fund_prices_context_std_63d_slope_v095_signal(close, closeadj):
    base = _std(close, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std close
def fpc_f091_fund_prices_context_std_63d_slope_v096_signal(close, closeadj):
    base = _std(close, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std close
def fpc_f091_fund_prices_context_std_126d_slope_v097_signal(close, closeadj):
    base = _std(close, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std close
def fpc_f091_fund_prices_context_std_126d_slope_v098_signal(close, closeadj):
    base = _std(close, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std close
def fpc_f091_fund_prices_context_std_126d_slope_v099_signal(close, closeadj):
    base = _std(close, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std close
def fpc_f091_fund_prices_context_std_252d_slope_v100_signal(close, closeadj):
    base = _std(close, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std close
def fpc_f091_fund_prices_context_std_252d_slope_v101_signal(close, closeadj):
    base = _std(close, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std close
def fpc_f091_fund_prices_context_std_252d_slope_v102_signal(close, closeadj):
    base = _std(close, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std close
def fpc_f091_fund_prices_context_std_504d_slope_v103_signal(close, closeadj):
    base = _std(close, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std close
def fpc_f091_fund_prices_context_std_504d_slope_v104_signal(close, closeadj):
    base = _std(close, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std close
def fpc_f091_fund_prices_context_std_504d_slope_v105_signal(close, closeadj):
    base = _std(close, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm close
def fpc_f091_fund_prices_context_ewm_21d_slope_v106_signal(close, closeadj):
    base = close.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm close
def fpc_f091_fund_prices_context_ewm_21d_slope_v107_signal(close, closeadj):
    base = close.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm close
def fpc_f091_fund_prices_context_ewm_21d_slope_v108_signal(close, closeadj):
    base = close.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm close
def fpc_f091_fund_prices_context_ewm_63d_slope_v109_signal(close, closeadj):
    base = close.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm close
def fpc_f091_fund_prices_context_ewm_63d_slope_v110_signal(close, closeadj):
    base = close.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm close
def fpc_f091_fund_prices_context_ewm_63d_slope_v111_signal(close, closeadj):
    base = close.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm close
def fpc_f091_fund_prices_context_ewm_126d_slope_v112_signal(close, closeadj):
    base = close.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm close
def fpc_f091_fund_prices_context_ewm_126d_slope_v113_signal(close, closeadj):
    base = close.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm close
def fpc_f091_fund_prices_context_ewm_126d_slope_v114_signal(close, closeadj):
    base = close.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm close
def fpc_f091_fund_prices_context_ewm_252d_slope_v115_signal(close, closeadj):
    base = close.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm close
def fpc_f091_fund_prices_context_ewm_252d_slope_v116_signal(close, closeadj):
    base = close.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm close
def fpc_f091_fund_prices_context_ewm_252d_slope_v117_signal(close, closeadj):
    base = close.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm close
def fpc_f091_fund_prices_context_ewm_504d_slope_v118_signal(close, closeadj):
    base = close.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm close
def fpc_f091_fund_prices_context_ewm_504d_slope_v119_signal(close, closeadj):
    base = close.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm close
def fpc_f091_fund_prices_context_ewm_504d_slope_v120_signal(close, closeadj):
    base = close.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq close
def fpc_f091_fund_prices_context_sq_21d_slope_v121_signal(close, closeadj):
    base = _mean(close * close, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq close
def fpc_f091_fund_prices_context_sq_21d_slope_v122_signal(close, closeadj):
    base = _mean(close * close, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq close
def fpc_f091_fund_prices_context_sq_21d_slope_v123_signal(close, closeadj):
    base = _mean(close * close, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq close
def fpc_f091_fund_prices_context_sq_63d_slope_v124_signal(close, closeadj):
    base = _mean(close * close, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq close
def fpc_f091_fund_prices_context_sq_63d_slope_v125_signal(close, closeadj):
    base = _mean(close * close, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq close
def fpc_f091_fund_prices_context_sq_63d_slope_v126_signal(close, closeadj):
    base = _mean(close * close, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq close
def fpc_f091_fund_prices_context_sq_126d_slope_v127_signal(close, closeadj):
    base = _mean(close * close, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq close
def fpc_f091_fund_prices_context_sq_126d_slope_v128_signal(close, closeadj):
    base = _mean(close * close, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq close
def fpc_f091_fund_prices_context_sq_126d_slope_v129_signal(close, closeadj):
    base = _mean(close * close, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq close
def fpc_f091_fund_prices_context_sq_252d_slope_v130_signal(close, closeadj):
    base = _mean(close * close, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq close
def fpc_f091_fund_prices_context_sq_252d_slope_v131_signal(close, closeadj):
    base = _mean(close * close, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq close
def fpc_f091_fund_prices_context_sq_252d_slope_v132_signal(close, closeadj):
    base = _mean(close * close, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq close
def fpc_f091_fund_prices_context_sq_504d_slope_v133_signal(close, closeadj):
    base = _mean(close * close, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq close
def fpc_f091_fund_prices_context_sq_504d_slope_v134_signal(close, closeadj):
    base = _mean(close * close, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq close
def fpc_f091_fund_prices_context_sq_504d_slope_v135_signal(close, closeadj):
    base = _mean(close * close, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z close
def fpc_f091_fund_prices_context_z_21d_slope_v136_signal(close):
    base = _z(close, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z close
def fpc_f091_fund_prices_context_z_21d_slope_v137_signal(close):
    base = _z(close, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z close
def fpc_f091_fund_prices_context_z_21d_slope_v138_signal(close):
    base = _z(close, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z close
def fpc_f091_fund_prices_context_z_63d_slope_v139_signal(close):
    base = _z(close, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z close
def fpc_f091_fund_prices_context_z_63d_slope_v140_signal(close):
    base = _z(close, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z close
def fpc_f091_fund_prices_context_z_63d_slope_v141_signal(close):
    base = _z(close, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z close
def fpc_f091_fund_prices_context_z_126d_slope_v142_signal(close):
    base = _z(close, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z close
def fpc_f091_fund_prices_context_z_126d_slope_v143_signal(close):
    base = _z(close, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z close
def fpc_f091_fund_prices_context_z_126d_slope_v144_signal(close):
    base = _z(close, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z close
def fpc_f091_fund_prices_context_z_252d_slope_v145_signal(close):
    base = _z(close, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z close
def fpc_f091_fund_prices_context_z_252d_slope_v146_signal(close):
    base = _z(close, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z close
def fpc_f091_fund_prices_context_z_252d_slope_v147_signal(close):
    base = _z(close, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z close
def fpc_f091_fund_prices_context_z_504d_slope_v148_signal(close):
    base = _z(close, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z close
def fpc_f091_fund_prices_context_z_504d_slope_v149_signal(close):
    base = _z(close, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z close
def fpc_f091_fund_prices_context_z_504d_slope_v150_signal(close):
    base = _z(close, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
