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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f43_share_count_change(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f43_buyback_intensity(sharesbas, closeadj, w):
    chg = -sharesbas.pct_change(periods=w)
    return chg * closeadj


def _f43_buyback_timing_quality(sharesbas, closeadj, w):
    chg = -sharesbas.pct_change(periods=w)
    pr_z = (closeadj - closeadj.rolling(w, min_periods=max(1, w // 2)).mean()) / closeadj.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return chg * (-pr_z)

# feature 1: sccchg_5d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_5d_xc_base_v001_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 5)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 2: sccchg_5d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_5d_xclog_base_v002_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 5)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 3: sccchg_5d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_5d_xcm21_base_v003_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 5)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 4: sccchg_10d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_10d_xc_base_v004_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 10)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 5: sccchg_10d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_10d_xclog_base_v005_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 10)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 6: sccchg_10d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_10d_xcm21_base_v006_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 10)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 7: sccchg_21d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_21d_xc_base_v007_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 21)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 8: sccchg_21d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_21d_xclog_base_v008_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 21)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 9: sccchg_21d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_21d_xcm21_base_v009_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 21)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 10: sccchg_42d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_42d_xc_base_v010_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 42)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 11: sccchg_42d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_42d_xclog_base_v011_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 42)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 12: sccchg_42d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_42d_xcm21_base_v012_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 42)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 13: sccchg_63d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_63d_xc_base_v013_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 63)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 14: sccchg_63d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_63d_xclog_base_v014_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 63)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 15: sccchg_63d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_63d_xcm21_base_v015_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 63)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 16: sccchg_126d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_126d_xc_base_v016_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 126)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 17: sccchg_126d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_126d_xclog_base_v017_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 126)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 18: sccchg_126d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_126d_xcm21_base_v018_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 126)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 19: sccchg_189d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_189d_xc_base_v019_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 189)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 20: sccchg_189d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_189d_xclog_base_v020_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 189)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 21: sccchg_189d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_189d_xcm21_base_v021_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 189)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 22: sccchg_252d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_252d_xc_base_v022_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 252)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 23: sccchg_252d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_252d_xclog_base_v023_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 252)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 24: sccchg_252d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_252d_xcm21_base_v024_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 252)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 25: sccchg_378d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_378d_xc_base_v025_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 378)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 26: sccchg_378d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_378d_xclog_base_v026_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 378)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 27: sccchg_378d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_378d_xcm21_base_v027_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 378)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 28: sccchg_504d_xc
def f43bct_f43_buyback_cycle_timing_sccchg_504d_xc_base_v028_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 504)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 29: sccchg_504d_xclog
def f43bct_f43_buyback_cycle_timing_sccchg_504d_xclog_base_v029_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 504)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 30: sccchg_504d_xcm21
def f43bct_f43_buyback_cycle_timing_sccchg_504d_xcm21_base_v030_signal(sharesbas, closeadj):
    base = _f43_share_count_change(sharesbas, 504)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 31: bbi_5d_xc
def f43bct_f43_buyback_cycle_timing_bbi_5d_xc_base_v031_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 5)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 32: bbi_5d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_5d_xclog_base_v032_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 5)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 33: bbi_5d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_5d_xcm21_base_v033_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 5)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 34: bbi_10d_xc
def f43bct_f43_buyback_cycle_timing_bbi_10d_xc_base_v034_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 10)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 35: bbi_10d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_10d_xclog_base_v035_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 10)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 36: bbi_10d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_10d_xcm21_base_v036_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 10)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 37: bbi_21d_xc
def f43bct_f43_buyback_cycle_timing_bbi_21d_xc_base_v037_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 21)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 38: bbi_21d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_21d_xclog_base_v038_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 21)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 39: bbi_21d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_21d_xcm21_base_v039_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 21)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 40: bbi_42d_xc
def f43bct_f43_buyback_cycle_timing_bbi_42d_xc_base_v040_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 42)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 41: bbi_42d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_42d_xclog_base_v041_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 42)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 42: bbi_42d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_42d_xcm21_base_v042_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 42)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 43: bbi_63d_xc
def f43bct_f43_buyback_cycle_timing_bbi_63d_xc_base_v043_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 63)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 44: bbi_63d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_63d_xclog_base_v044_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 63)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 45: bbi_63d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_63d_xcm21_base_v045_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 63)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 46: bbi_126d_xc
def f43bct_f43_buyback_cycle_timing_bbi_126d_xc_base_v046_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 126)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 47: bbi_126d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_126d_xclog_base_v047_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 126)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 48: bbi_126d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_126d_xcm21_base_v048_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 126)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 49: bbi_189d_xc
def f43bct_f43_buyback_cycle_timing_bbi_189d_xc_base_v049_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 189)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 50: bbi_189d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_189d_xclog_base_v050_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 189)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 51: bbi_189d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_189d_xcm21_base_v051_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 189)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 52: bbi_252d_xc
def f43bct_f43_buyback_cycle_timing_bbi_252d_xc_base_v052_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 252)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 53: bbi_252d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_252d_xclog_base_v053_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 252)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 54: bbi_252d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_252d_xcm21_base_v054_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 252)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 55: bbi_378d_xc
def f43bct_f43_buyback_cycle_timing_bbi_378d_xc_base_v055_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 378)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 56: bbi_378d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_378d_xclog_base_v056_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 378)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 57: bbi_378d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_378d_xcm21_base_v057_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 378)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 58: bbi_504d_xc
def f43bct_f43_buyback_cycle_timing_bbi_504d_xc_base_v058_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 504)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 59: bbi_504d_xclog
def f43bct_f43_buyback_cycle_timing_bbi_504d_xclog_base_v059_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 504)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 60: bbi_504d_xcm21
def f43bct_f43_buyback_cycle_timing_bbi_504d_xcm21_base_v060_signal(sharesbas, closeadj):
    base = _f43_buyback_intensity(sharesbas, closeadj, 504)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 61: bbq_5d_xc
def f43bct_f43_buyback_cycle_timing_bbq_5d_xc_base_v061_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 5)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 62: bbq_5d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_5d_xclog_base_v062_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 5)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 63: bbq_5d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_5d_xcm21_base_v063_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 5)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 64: bbq_10d_xc
def f43bct_f43_buyback_cycle_timing_bbq_10d_xc_base_v064_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 10)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 65: bbq_10d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_10d_xclog_base_v065_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 10)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 66: bbq_10d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_10d_xcm21_base_v066_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 10)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 67: bbq_21d_xc
def f43bct_f43_buyback_cycle_timing_bbq_21d_xc_base_v067_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 21)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 68: bbq_21d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_21d_xclog_base_v068_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 21)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 69: bbq_21d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_21d_xcm21_base_v069_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 21)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 70: bbq_42d_xc
def f43bct_f43_buyback_cycle_timing_bbq_42d_xc_base_v070_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 42)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 71: bbq_42d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_42d_xclog_base_v071_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 42)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 72: bbq_42d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_42d_xcm21_base_v072_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 42)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 73: bbq_63d_xc
def f43bct_f43_buyback_cycle_timing_bbq_63d_xc_base_v073_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 63)
    result = base * (closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# feature 74: bbq_63d_xclog
def f43bct_f43_buyback_cycle_timing_bbq_63d_xclog_base_v074_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 63)
    result = base * (np.log(closeadj.abs()+1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# feature 75: bbq_63d_xcm21
def f43bct_f43_buyback_cycle_timing_bbq_63d_xcm21_base_v075_signal(sharesbas, closeadj):
    base = _f43_buyback_timing_quality(sharesbas, closeadj, 63)
    result = base * (_mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43bct_f43_buyback_cycle_timing_sccchg_5d_xc_base_v001_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_5d_xclog_base_v002_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_5d_xcm21_base_v003_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_10d_xc_base_v004_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_10d_xclog_base_v005_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_10d_xcm21_base_v006_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_21d_xc_base_v007_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_21d_xclog_base_v008_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_21d_xcm21_base_v009_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_42d_xc_base_v010_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_42d_xclog_base_v011_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_42d_xcm21_base_v012_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_63d_xc_base_v013_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_63d_xclog_base_v014_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_63d_xcm21_base_v015_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_126d_xc_base_v016_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_126d_xclog_base_v017_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_126d_xcm21_base_v018_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_189d_xc_base_v019_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_189d_xclog_base_v020_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_189d_xcm21_base_v021_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_252d_xc_base_v022_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_252d_xclog_base_v023_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_252d_xcm21_base_v024_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_378d_xc_base_v025_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_378d_xclog_base_v026_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_378d_xcm21_base_v027_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_504d_xc_base_v028_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_504d_xclog_base_v029_signal,
    f43bct_f43_buyback_cycle_timing_sccchg_504d_xcm21_base_v030_signal,
    f43bct_f43_buyback_cycle_timing_bbi_5d_xc_base_v031_signal,
    f43bct_f43_buyback_cycle_timing_bbi_5d_xclog_base_v032_signal,
    f43bct_f43_buyback_cycle_timing_bbi_5d_xcm21_base_v033_signal,
    f43bct_f43_buyback_cycle_timing_bbi_10d_xc_base_v034_signal,
    f43bct_f43_buyback_cycle_timing_bbi_10d_xclog_base_v035_signal,
    f43bct_f43_buyback_cycle_timing_bbi_10d_xcm21_base_v036_signal,
    f43bct_f43_buyback_cycle_timing_bbi_21d_xc_base_v037_signal,
    f43bct_f43_buyback_cycle_timing_bbi_21d_xclog_base_v038_signal,
    f43bct_f43_buyback_cycle_timing_bbi_21d_xcm21_base_v039_signal,
    f43bct_f43_buyback_cycle_timing_bbi_42d_xc_base_v040_signal,
    f43bct_f43_buyback_cycle_timing_bbi_42d_xclog_base_v041_signal,
    f43bct_f43_buyback_cycle_timing_bbi_42d_xcm21_base_v042_signal,
    f43bct_f43_buyback_cycle_timing_bbi_63d_xc_base_v043_signal,
    f43bct_f43_buyback_cycle_timing_bbi_63d_xclog_base_v044_signal,
    f43bct_f43_buyback_cycle_timing_bbi_63d_xcm21_base_v045_signal,
    f43bct_f43_buyback_cycle_timing_bbi_126d_xc_base_v046_signal,
    f43bct_f43_buyback_cycle_timing_bbi_126d_xclog_base_v047_signal,
    f43bct_f43_buyback_cycle_timing_bbi_126d_xcm21_base_v048_signal,
    f43bct_f43_buyback_cycle_timing_bbi_189d_xc_base_v049_signal,
    f43bct_f43_buyback_cycle_timing_bbi_189d_xclog_base_v050_signal,
    f43bct_f43_buyback_cycle_timing_bbi_189d_xcm21_base_v051_signal,
    f43bct_f43_buyback_cycle_timing_bbi_252d_xc_base_v052_signal,
    f43bct_f43_buyback_cycle_timing_bbi_252d_xclog_base_v053_signal,
    f43bct_f43_buyback_cycle_timing_bbi_252d_xcm21_base_v054_signal,
    f43bct_f43_buyback_cycle_timing_bbi_378d_xc_base_v055_signal,
    f43bct_f43_buyback_cycle_timing_bbi_378d_xclog_base_v056_signal,
    f43bct_f43_buyback_cycle_timing_bbi_378d_xcm21_base_v057_signal,
    f43bct_f43_buyback_cycle_timing_bbi_504d_xc_base_v058_signal,
    f43bct_f43_buyback_cycle_timing_bbi_504d_xclog_base_v059_signal,
    f43bct_f43_buyback_cycle_timing_bbi_504d_xcm21_base_v060_signal,
    f43bct_f43_buyback_cycle_timing_bbq_5d_xc_base_v061_signal,
    f43bct_f43_buyback_cycle_timing_bbq_5d_xclog_base_v062_signal,
    f43bct_f43_buyback_cycle_timing_bbq_5d_xcm21_base_v063_signal,
    f43bct_f43_buyback_cycle_timing_bbq_10d_xc_base_v064_signal,
    f43bct_f43_buyback_cycle_timing_bbq_10d_xclog_base_v065_signal,
    f43bct_f43_buyback_cycle_timing_bbq_10d_xcm21_base_v066_signal,
    f43bct_f43_buyback_cycle_timing_bbq_21d_xc_base_v067_signal,
    f43bct_f43_buyback_cycle_timing_bbq_21d_xclog_base_v068_signal,
    f43bct_f43_buyback_cycle_timing_bbq_21d_xcm21_base_v069_signal,
    f43bct_f43_buyback_cycle_timing_bbq_42d_xc_base_v070_signal,
    f43bct_f43_buyback_cycle_timing_bbq_42d_xclog_base_v071_signal,
    f43bct_f43_buyback_cycle_timing_bbq_42d_xcm21_base_v072_signal,
    f43bct_f43_buyback_cycle_timing_bbq_63d_xc_base_v073_signal,
    f43bct_f43_buyback_cycle_timing_bbq_63d_xclog_base_v074_signal,
    f43bct_f43_buyback_cycle_timing_bbq_63d_xcm21_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_BUYBACK_CYCLE_TIMING_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f43_share_count_change', '_f43_buyback_intensity', '_f43_buyback_timing_quality')
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f43_buyback_cycle_timing_base_001_075_claude: {n_features} features pass")
