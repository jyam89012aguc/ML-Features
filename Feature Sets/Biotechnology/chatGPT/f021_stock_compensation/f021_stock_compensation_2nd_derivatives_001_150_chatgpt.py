"""Family f021 - Stock-based compensation burden (R&D and Innovation) | Sharadar tables: SF1 | fields: sbcomp, rnd, sgna, opex, sharesbas | 2nd derivatives 001-150"""
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
def _stock_compensation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _stock_compensation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _stock_compensation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw sbcomp
def sc_f021_stock_compensation_raw_21d_slope_v001_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sbcomp
def sc_f021_stock_compensation_raw_21d_slope_v002_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sbcomp
def sc_f021_stock_compensation_raw_21d_slope_v003_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sbcomp
def sc_f021_stock_compensation_raw_63d_slope_v004_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sbcomp
def sc_f021_stock_compensation_raw_63d_slope_v005_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sbcomp
def sc_f021_stock_compensation_raw_63d_slope_v006_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sbcomp
def sc_f021_stock_compensation_raw_126d_slope_v007_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sbcomp
def sc_f021_stock_compensation_raw_126d_slope_v008_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sbcomp
def sc_f021_stock_compensation_raw_126d_slope_v009_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sbcomp
def sc_f021_stock_compensation_raw_252d_slope_v010_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sbcomp
def sc_f021_stock_compensation_raw_252d_slope_v011_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sbcomp
def sc_f021_stock_compensation_raw_252d_slope_v012_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sbcomp
def sc_f021_stock_compensation_raw_504d_slope_v013_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sbcomp
def sc_f021_stock_compensation_raw_504d_slope_v014_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sbcomp
def sc_f021_stock_compensation_raw_504d_slope_v015_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sbcomp
def sc_f021_stock_compensation_log_21d_slope_v016_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sbcomp
def sc_f021_stock_compensation_log_21d_slope_v017_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sbcomp
def sc_f021_stock_compensation_log_21d_slope_v018_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sbcomp
def sc_f021_stock_compensation_log_63d_slope_v019_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sbcomp
def sc_f021_stock_compensation_log_63d_slope_v020_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sbcomp
def sc_f021_stock_compensation_log_63d_slope_v021_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sbcomp
def sc_f021_stock_compensation_log_126d_slope_v022_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sbcomp
def sc_f021_stock_compensation_log_126d_slope_v023_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sbcomp
def sc_f021_stock_compensation_log_126d_slope_v024_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sbcomp
def sc_f021_stock_compensation_log_252d_slope_v025_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sbcomp
def sc_f021_stock_compensation_log_252d_slope_v026_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sbcomp
def sc_f021_stock_compensation_log_252d_slope_v027_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sbcomp
def sc_f021_stock_compensation_log_504d_slope_v028_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sbcomp
def sc_f021_stock_compensation_log_504d_slope_v029_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sbcomp
def sc_f021_stock_compensation_log_504d_slope_v030_signal(sbcomp, closeadj):
    base = _mean(_stock_compensation_log(sbcomp), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sbcomp
def sc_f021_stock_compensation_pershare_21d_slope_v031_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sbcomp
def sc_f021_stock_compensation_pershare_21d_slope_v032_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sbcomp
def sc_f021_stock_compensation_pershare_21d_slope_v033_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sbcomp
def sc_f021_stock_compensation_pershare_63d_slope_v034_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sbcomp
def sc_f021_stock_compensation_pershare_63d_slope_v035_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sbcomp
def sc_f021_stock_compensation_pershare_63d_slope_v036_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sbcomp
def sc_f021_stock_compensation_pershare_126d_slope_v037_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sbcomp
def sc_f021_stock_compensation_pershare_126d_slope_v038_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sbcomp
def sc_f021_stock_compensation_pershare_126d_slope_v039_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sbcomp
def sc_f021_stock_compensation_pershare_252d_slope_v040_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sbcomp
def sc_f021_stock_compensation_pershare_252d_slope_v041_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sbcomp
def sc_f021_stock_compensation_pershare_252d_slope_v042_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sbcomp
def sc_f021_stock_compensation_pershare_504d_slope_v043_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sbcomp
def sc_f021_stock_compensation_pershare_504d_slope_v044_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sbcomp
def sc_f021_stock_compensation_pershare_504d_slope_v045_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_stock_compensation_per_share(sbcomp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_21d_slope_v046_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_21d_slope_v047_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_21d_slope_v048_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_63d_slope_v049_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_63d_slope_v050_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_63d_slope_v051_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_126d_slope_v052_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_126d_slope_v053_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_126d_slope_v054_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_252d_slope_v055_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_252d_slope_v056_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_252d_slope_v057_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_504d_slope_v058_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_504d_slope_v059_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_rnd sbcomp
def sc_f021_stock_compensation_per_rnd_504d_slope_v060_signal(sbcomp, rnd):
    base = _mean(_stock_compensation_scaled(sbcomp, rnd), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_21d_slope_v061_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_21d_slope_v062_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_21d_slope_v063_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_63d_slope_v064_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_63d_slope_v065_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_63d_slope_v066_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_126d_slope_v067_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_126d_slope_v068_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_126d_slope_v069_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_252d_slope_v070_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_252d_slope_v071_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_252d_slope_v072_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_504d_slope_v073_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_504d_slope_v074_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sgna sbcomp
def sc_f021_stock_compensation_per_sgna_504d_slope_v075_signal(sbcomp, sgna):
    base = _mean(_stock_compensation_scaled(sbcomp, sgna), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_21d_slope_v076_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_21d_slope_v077_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_21d_slope_v078_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_63d_slope_v079_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_63d_slope_v080_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_63d_slope_v081_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_126d_slope_v082_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_126d_slope_v083_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_126d_slope_v084_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_252d_slope_v085_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_252d_slope_v086_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_252d_slope_v087_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_504d_slope_v088_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_504d_slope_v089_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sharesbas sbcomp
def sc_f021_stock_compensation_per_sharesbas_504d_slope_v090_signal(sbcomp, sharesbas):
    base = _mean(_stock_compensation_scaled(sbcomp, sharesbas), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sbcomp
def sc_f021_stock_compensation_std_21d_slope_v091_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sbcomp
def sc_f021_stock_compensation_std_21d_slope_v092_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sbcomp
def sc_f021_stock_compensation_std_21d_slope_v093_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sbcomp
def sc_f021_stock_compensation_std_63d_slope_v094_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sbcomp
def sc_f021_stock_compensation_std_63d_slope_v095_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sbcomp
def sc_f021_stock_compensation_std_63d_slope_v096_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sbcomp
def sc_f021_stock_compensation_std_126d_slope_v097_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sbcomp
def sc_f021_stock_compensation_std_126d_slope_v098_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sbcomp
def sc_f021_stock_compensation_std_126d_slope_v099_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sbcomp
def sc_f021_stock_compensation_std_252d_slope_v100_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sbcomp
def sc_f021_stock_compensation_std_252d_slope_v101_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sbcomp
def sc_f021_stock_compensation_std_252d_slope_v102_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sbcomp
def sc_f021_stock_compensation_std_504d_slope_v103_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sbcomp
def sc_f021_stock_compensation_std_504d_slope_v104_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sbcomp
def sc_f021_stock_compensation_std_504d_slope_v105_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sbcomp
def sc_f021_stock_compensation_ewm_21d_slope_v106_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sbcomp
def sc_f021_stock_compensation_ewm_21d_slope_v107_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sbcomp
def sc_f021_stock_compensation_ewm_21d_slope_v108_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sbcomp
def sc_f021_stock_compensation_ewm_63d_slope_v109_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sbcomp
def sc_f021_stock_compensation_ewm_63d_slope_v110_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sbcomp
def sc_f021_stock_compensation_ewm_63d_slope_v111_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sbcomp
def sc_f021_stock_compensation_ewm_126d_slope_v112_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sbcomp
def sc_f021_stock_compensation_ewm_126d_slope_v113_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sbcomp
def sc_f021_stock_compensation_ewm_126d_slope_v114_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sbcomp
def sc_f021_stock_compensation_ewm_252d_slope_v115_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sbcomp
def sc_f021_stock_compensation_ewm_252d_slope_v116_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sbcomp
def sc_f021_stock_compensation_ewm_252d_slope_v117_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sbcomp
def sc_f021_stock_compensation_ewm_504d_slope_v118_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sbcomp
def sc_f021_stock_compensation_ewm_504d_slope_v119_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sbcomp
def sc_f021_stock_compensation_ewm_504d_slope_v120_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sbcomp
def sc_f021_stock_compensation_sq_21d_slope_v121_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sbcomp
def sc_f021_stock_compensation_sq_21d_slope_v122_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sbcomp
def sc_f021_stock_compensation_sq_21d_slope_v123_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sbcomp
def sc_f021_stock_compensation_sq_63d_slope_v124_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sbcomp
def sc_f021_stock_compensation_sq_63d_slope_v125_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sbcomp
def sc_f021_stock_compensation_sq_63d_slope_v126_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sbcomp
def sc_f021_stock_compensation_sq_126d_slope_v127_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sbcomp
def sc_f021_stock_compensation_sq_126d_slope_v128_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sbcomp
def sc_f021_stock_compensation_sq_126d_slope_v129_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sbcomp
def sc_f021_stock_compensation_sq_252d_slope_v130_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sbcomp
def sc_f021_stock_compensation_sq_252d_slope_v131_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sbcomp
def sc_f021_stock_compensation_sq_252d_slope_v132_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sbcomp
def sc_f021_stock_compensation_sq_504d_slope_v133_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sbcomp
def sc_f021_stock_compensation_sq_504d_slope_v134_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sbcomp
def sc_f021_stock_compensation_sq_504d_slope_v135_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sbcomp
def sc_f021_stock_compensation_z_21d_slope_v136_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sbcomp
def sc_f021_stock_compensation_z_21d_slope_v137_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sbcomp
def sc_f021_stock_compensation_z_21d_slope_v138_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sbcomp
def sc_f021_stock_compensation_z_63d_slope_v139_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sbcomp
def sc_f021_stock_compensation_z_63d_slope_v140_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sbcomp
def sc_f021_stock_compensation_z_63d_slope_v141_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sbcomp
def sc_f021_stock_compensation_z_126d_slope_v142_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sbcomp
def sc_f021_stock_compensation_z_126d_slope_v143_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sbcomp
def sc_f021_stock_compensation_z_126d_slope_v144_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sbcomp
def sc_f021_stock_compensation_z_252d_slope_v145_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sbcomp
def sc_f021_stock_compensation_z_252d_slope_v146_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sbcomp
def sc_f021_stock_compensation_z_252d_slope_v147_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sbcomp
def sc_f021_stock_compensation_z_504d_slope_v148_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sbcomp
def sc_f021_stock_compensation_z_504d_slope_v149_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sbcomp
def sc_f021_stock_compensation_z_504d_slope_v150_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
