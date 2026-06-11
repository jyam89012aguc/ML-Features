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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f44_dps_growth(dps, w):
    base = _mean(dps, max(2, w // 4))
    return base.pct_change(periods=w)


def _f44_share_buyback_intensity(sharesbas, w):
    base = _mean(sharesbas, max(2, w // 4))
    return -base.pct_change(periods=w)


def _f44_total_return_quality(dps, sharesbas, w):
    dg = _mean(dps, max(2, w // 4)).pct_change(periods=w)
    bb = -_mean(sharesbas, max(2, w // 4)).pct_change(periods=w)
    return dg + bb

# v001: jerk window 5 of dpsg_21d
def f44hcr_f44_healthcare_capital_return_dpsg_21d_jerk_v001_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002: jerk window 21 of dpsg_21d
def f44hcr_f44_healthcare_capital_return_dpsg_21d_jerk_v002_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003: jerk window 63 of dpsg_21d
def f44hcr_f44_healthcare_capital_return_dpsg_21d_jerk_v003_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v004: jerk window 5 of dpsg_63d
def f44hcr_f44_healthcare_capital_return_dpsg_63d_jerk_v004_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v005: jerk window 21 of dpsg_63d
def f44hcr_f44_healthcare_capital_return_dpsg_63d_jerk_v005_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v006: jerk window 63 of dpsg_63d
def f44hcr_f44_healthcare_capital_return_dpsg_63d_jerk_v006_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007: jerk window 5 of dpsg_126d
def f44hcr_f44_healthcare_capital_return_dpsg_126d_jerk_v007_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008: jerk window 21 of dpsg_126d
def f44hcr_f44_healthcare_capital_return_dpsg_126d_jerk_v008_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009: jerk window 63 of dpsg_126d
def f44hcr_f44_healthcare_capital_return_dpsg_126d_jerk_v009_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: jerk window 5 of dpsg_252d
def f44hcr_f44_healthcare_capital_return_dpsg_252d_jerk_v010_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: jerk window 21 of dpsg_252d
def f44hcr_f44_healthcare_capital_return_dpsg_252d_jerk_v011_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012: jerk window 63 of dpsg_252d
def f44hcr_f44_healthcare_capital_return_dpsg_252d_jerk_v012_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013: jerk window 5 of dpsg_504d
def f44hcr_f44_healthcare_capital_return_dpsg_504d_jerk_v013_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v014: jerk window 21 of dpsg_504d
def f44hcr_f44_healthcare_capital_return_dpsg_504d_jerk_v014_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015: jerk window 63 of dpsg_504d
def f44hcr_f44_healthcare_capital_return_dpsg_504d_jerk_v015_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016: jerk window 5 of bb_21d
def f44hcr_f44_healthcare_capital_return_bb_21d_jerk_v016_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: jerk window 21 of bb_21d
def f44hcr_f44_healthcare_capital_return_bb_21d_jerk_v017_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: jerk window 63 of bb_21d
def f44hcr_f44_healthcare_capital_return_bb_21d_jerk_v018_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: jerk window 5 of bb_63d
def f44hcr_f44_healthcare_capital_return_bb_63d_jerk_v019_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: jerk window 21 of bb_63d
def f44hcr_f44_healthcare_capital_return_bb_63d_jerk_v020_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: jerk window 63 of bb_63d
def f44hcr_f44_healthcare_capital_return_bb_63d_jerk_v021_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: jerk window 5 of bb_126d
def f44hcr_f44_healthcare_capital_return_bb_126d_jerk_v022_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v023: jerk window 21 of bb_126d
def f44hcr_f44_healthcare_capital_return_bb_126d_jerk_v023_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024: jerk window 63 of bb_126d
def f44hcr_f44_healthcare_capital_return_bb_126d_jerk_v024_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025: jerk window 5 of bb_252d
def f44hcr_f44_healthcare_capital_return_bb_252d_jerk_v025_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v026: jerk window 21 of bb_252d
def f44hcr_f44_healthcare_capital_return_bb_252d_jerk_v026_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027: jerk window 63 of bb_252d
def f44hcr_f44_healthcare_capital_return_bb_252d_jerk_v027_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028: jerk window 5 of bb_504d
def f44hcr_f44_healthcare_capital_return_bb_504d_jerk_v028_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: jerk window 21 of bb_504d
def f44hcr_f44_healthcare_capital_return_bb_504d_jerk_v029_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: jerk window 63 of bb_504d
def f44hcr_f44_healthcare_capital_return_bb_504d_jerk_v030_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: jerk window 5 of trq_21d
def f44hcr_f44_healthcare_capital_return_trq_21d_jerk_v031_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: jerk window 21 of trq_21d
def f44hcr_f44_healthcare_capital_return_trq_21d_jerk_v032_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: jerk window 63 of trq_21d
def f44hcr_f44_healthcare_capital_return_trq_21d_jerk_v033_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: jerk window 5 of trq_63d
def f44hcr_f44_healthcare_capital_return_trq_63d_jerk_v034_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: jerk window 21 of trq_63d
def f44hcr_f44_healthcare_capital_return_trq_63d_jerk_v035_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: jerk window 63 of trq_63d
def f44hcr_f44_healthcare_capital_return_trq_63d_jerk_v036_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: jerk window 5 of trq_126d
def f44hcr_f44_healthcare_capital_return_trq_126d_jerk_v037_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: jerk window 21 of trq_126d
def f44hcr_f44_healthcare_capital_return_trq_126d_jerk_v038_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: jerk window 63 of trq_126d
def f44hcr_f44_healthcare_capital_return_trq_126d_jerk_v039_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: jerk window 5 of trq_252d
def f44hcr_f44_healthcare_capital_return_trq_252d_jerk_v040_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: jerk window 21 of trq_252d
def f44hcr_f44_healthcare_capital_return_trq_252d_jerk_v041_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: jerk window 63 of trq_252d
def f44hcr_f44_healthcare_capital_return_trq_252d_jerk_v042_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043: jerk window 5 of trq_504d
def f44hcr_f44_healthcare_capital_return_trq_504d_jerk_v043_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v044: jerk window 21 of trq_504d
def f44hcr_f44_healthcare_capital_return_trq_504d_jerk_v044_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045: jerk window 63 of trq_504d
def f44hcr_f44_healthcare_capital_return_trq_504d_jerk_v045_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046: jerk window 5 of dpsxbb_21d
def f44hcr_f44_healthcare_capital_return_dpsxbb_21d_jerk_v046_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 21) * _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047: jerk window 21 of dpsxbb_21d
def f44hcr_f44_healthcare_capital_return_dpsxbb_21d_jerk_v047_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 21) * _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048: jerk window 63 of dpsxbb_21d
def f44hcr_f44_healthcare_capital_return_dpsxbb_21d_jerk_v048_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 21) * _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: jerk window 5 of dpsxbb_63d
def f44hcr_f44_healthcare_capital_return_dpsxbb_63d_jerk_v049_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 63) * _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: jerk window 21 of dpsxbb_63d
def f44hcr_f44_healthcare_capital_return_dpsxbb_63d_jerk_v050_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 63) * _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: jerk window 63 of dpsxbb_63d
def f44hcr_f44_healthcare_capital_return_dpsxbb_63d_jerk_v051_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 63) * _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: jerk window 5 of dpsxbb_252d
def f44hcr_f44_healthcare_capital_return_dpsxbb_252d_jerk_v052_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 252) * _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053: jerk window 21 of dpsxbb_252d
def f44hcr_f44_healthcare_capital_return_dpsxbb_252d_jerk_v053_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 252) * _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054: jerk window 63 of dpsxbb_252d
def f44hcr_f44_healthcare_capital_return_dpsxbb_252d_jerk_v054_signal(dps, sharesbas, closeadj):
    base = _f44_dps_growth(dps, 252) * _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055: jerk window 5 of dpsxeps_21d
def f44hcr_f44_healthcare_capital_return_dpsxeps_21d_jerk_v055_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 21) * _mean(eps, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v056: jerk window 21 of dpsxeps_21d
def f44hcr_f44_healthcare_capital_return_dpsxeps_21d_jerk_v056_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 21) * _mean(eps, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057: jerk window 63 of dpsxeps_21d
def f44hcr_f44_healthcare_capital_return_dpsxeps_21d_jerk_v057_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 21) * _mean(eps, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058: jerk window 5 of dpsxeps_63d
def f44hcr_f44_healthcare_capital_return_dpsxeps_63d_jerk_v058_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 63) * _mean(eps, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: jerk window 21 of dpsxeps_63d
def f44hcr_f44_healthcare_capital_return_dpsxeps_63d_jerk_v059_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 63) * _mean(eps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: jerk window 63 of dpsxeps_63d
def f44hcr_f44_healthcare_capital_return_dpsxeps_63d_jerk_v060_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 63) * _mean(eps, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: jerk window 5 of dpsxeps_252d
def f44hcr_f44_healthcare_capital_return_dpsxeps_252d_jerk_v061_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 252) * _mean(eps, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: jerk window 21 of dpsxeps_252d
def f44hcr_f44_healthcare_capital_return_dpsxeps_252d_jerk_v062_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 252) * _mean(eps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: jerk window 63 of dpsxeps_252d
def f44hcr_f44_healthcare_capital_return_dpsxeps_252d_jerk_v063_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 252) * _mean(eps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: jerk window 5 of bbxeps_21d
def f44hcr_f44_healthcare_capital_return_bbxeps_21d_jerk_v064_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * _mean(eps, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: jerk window 21 of bbxeps_21d
def f44hcr_f44_healthcare_capital_return_bbxeps_21d_jerk_v065_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * _mean(eps, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066: jerk window 63 of bbxeps_21d
def f44hcr_f44_healthcare_capital_return_bbxeps_21d_jerk_v066_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * _mean(eps, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067: jerk window 5 of bbxeps_63d
def f44hcr_f44_healthcare_capital_return_bbxeps_63d_jerk_v067_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * _mean(eps, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v068: jerk window 21 of bbxeps_63d
def f44hcr_f44_healthcare_capital_return_bbxeps_63d_jerk_v068_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * _mean(eps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069: jerk window 63 of bbxeps_63d
def f44hcr_f44_healthcare_capital_return_bbxeps_63d_jerk_v069_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * _mean(eps, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070: jerk window 5 of bbxeps_252d
def f44hcr_f44_healthcare_capital_return_bbxeps_252d_jerk_v070_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * _mean(eps, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v071: jerk window 21 of bbxeps_252d
def f44hcr_f44_healthcare_capital_return_bbxeps_252d_jerk_v071_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * _mean(eps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072: jerk window 63 of bbxeps_252d
def f44hcr_f44_healthcare_capital_return_bbxeps_252d_jerk_v072_signal(sharesbas, eps, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * _mean(eps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073: jerk window 5 of dpsgema_21d
def f44hcr_f44_healthcare_capital_return_dpsgema_21d_jerk_v073_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v074: jerk window 21 of dpsgema_21d
def f44hcr_f44_healthcare_capital_return_dpsgema_21d_jerk_v074_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075: jerk window 63 of dpsgema_21d
def f44hcr_f44_healthcare_capital_return_dpsgema_21d_jerk_v075_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076: jerk window 5 of dpsgema_63d
def f44hcr_f44_healthcare_capital_return_dpsgema_63d_jerk_v076_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v077: jerk window 21 of dpsgema_63d
def f44hcr_f44_healthcare_capital_return_dpsgema_63d_jerk_v077_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078: jerk window 63 of dpsgema_63d
def f44hcr_f44_healthcare_capital_return_dpsgema_63d_jerk_v078_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079: jerk window 5 of dpsgema_252d
def f44hcr_f44_healthcare_capital_return_dpsgema_252d_jerk_v079_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v080: jerk window 21 of dpsgema_252d
def f44hcr_f44_healthcare_capital_return_dpsgema_252d_jerk_v080_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081: jerk window 63 of dpsgema_252d
def f44hcr_f44_healthcare_capital_return_dpsgema_252d_jerk_v081_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082: jerk window 5 of bbema_21d
def f44hcr_f44_healthcare_capital_return_bbema_21d_jerk_v082_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v083: jerk window 21 of bbema_21d
def f44hcr_f44_healthcare_capital_return_bbema_21d_jerk_v083_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084: jerk window 63 of bbema_21d
def f44hcr_f44_healthcare_capital_return_bbema_21d_jerk_v084_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v085: jerk window 5 of bbema_63d
def f44hcr_f44_healthcare_capital_return_bbema_63d_jerk_v085_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: jerk window 21 of bbema_63d
def f44hcr_f44_healthcare_capital_return_bbema_63d_jerk_v086_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: jerk window 63 of bbema_63d
def f44hcr_f44_healthcare_capital_return_bbema_63d_jerk_v087_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: jerk window 5 of bbema_252d
def f44hcr_f44_healthcare_capital_return_bbema_252d_jerk_v088_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v089: jerk window 21 of bbema_252d
def f44hcr_f44_healthcare_capital_return_bbema_252d_jerk_v089_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090: jerk window 63 of bbema_252d
def f44hcr_f44_healthcare_capital_return_bbema_252d_jerk_v090_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091: jerk window 5 of trqema_21d
def f44hcr_f44_healthcare_capital_return_trqema_21d_jerk_v091_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v092: jerk window 21 of trqema_21d
def f44hcr_f44_healthcare_capital_return_trqema_21d_jerk_v092_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093: jerk window 63 of trqema_21d
def f44hcr_f44_healthcare_capital_return_trqema_21d_jerk_v093_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094: jerk window 5 of trqema_63d
def f44hcr_f44_healthcare_capital_return_trqema_63d_jerk_v094_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v095: jerk window 21 of trqema_63d
def f44hcr_f44_healthcare_capital_return_trqema_63d_jerk_v095_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096: jerk window 63 of trqema_63d
def f44hcr_f44_healthcare_capital_return_trqema_63d_jerk_v096_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097: jerk window 5 of trqema_252d
def f44hcr_f44_healthcare_capital_return_trqema_252d_jerk_v097_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v098: jerk window 21 of trqema_252d
def f44hcr_f44_healthcare_capital_return_trqema_252d_jerk_v098_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099: jerk window 63 of trqema_252d
def f44hcr_f44_healthcare_capital_return_trqema_252d_jerk_v099_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100: jerk window 5 of dpsgcum_21d
def f44hcr_f44_healthcare_capital_return_dpsgcum_21d_jerk_v100_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: jerk window 21 of dpsgcum_21d
def f44hcr_f44_healthcare_capital_return_dpsgcum_21d_jerk_v101_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: jerk window 63 of dpsgcum_21d
def f44hcr_f44_healthcare_capital_return_dpsgcum_21d_jerk_v102_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: jerk window 5 of dpsgcum_63d
def f44hcr_f44_healthcare_capital_return_dpsgcum_63d_jerk_v103_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v104: jerk window 21 of dpsgcum_63d
def f44hcr_f44_healthcare_capital_return_dpsgcum_63d_jerk_v104_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105: jerk window 63 of dpsgcum_63d
def f44hcr_f44_healthcare_capital_return_dpsgcum_63d_jerk_v105_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106: jerk window 5 of dpsgcum_126d
def f44hcr_f44_healthcare_capital_return_dpsgcum_126d_jerk_v106_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v107: jerk window 21 of dpsgcum_126d
def f44hcr_f44_healthcare_capital_return_dpsgcum_126d_jerk_v107_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v108: jerk window 63 of dpsgcum_126d
def f44hcr_f44_healthcare_capital_return_dpsgcum_126d_jerk_v108_signal(dps, closeadj):
    base = _f44_dps_growth(dps, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109: jerk window 5 of bbcum_21d
def f44hcr_f44_healthcare_capital_return_bbcum_21d_jerk_v109_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v110: jerk window 21 of bbcum_21d
def f44hcr_f44_healthcare_capital_return_bbcum_21d_jerk_v110_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111: jerk window 63 of bbcum_21d
def f44hcr_f44_healthcare_capital_return_bbcum_21d_jerk_v111_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112: jerk window 5 of bbcum_63d
def f44hcr_f44_healthcare_capital_return_bbcum_63d_jerk_v112_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v113: jerk window 21 of bbcum_63d
def f44hcr_f44_healthcare_capital_return_bbcum_63d_jerk_v113_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114: jerk window 63 of bbcum_63d
def f44hcr_f44_healthcare_capital_return_bbcum_63d_jerk_v114_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115: jerk window 5 of bbcum_126d
def f44hcr_f44_healthcare_capital_return_bbcum_126d_jerk_v115_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v116: jerk window 21 of bbcum_126d
def f44hcr_f44_healthcare_capital_return_bbcum_126d_jerk_v116_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117: jerk window 63 of bbcum_126d
def f44hcr_f44_healthcare_capital_return_bbcum_126d_jerk_v117_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118: jerk window 5 of trqcum_21d
def f44hcr_f44_healthcare_capital_return_trqcum_21d_jerk_v118_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v119: jerk window 21 of trqcum_21d
def f44hcr_f44_healthcare_capital_return_trqcum_21d_jerk_v119_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120: jerk window 63 of trqcum_21d
def f44hcr_f44_healthcare_capital_return_trqcum_21d_jerk_v120_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121: jerk window 5 of trqcum_63d
def f44hcr_f44_healthcare_capital_return_trqcum_63d_jerk_v121_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v122: jerk window 21 of trqcum_63d
def f44hcr_f44_healthcare_capital_return_trqcum_63d_jerk_v122_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123: jerk window 63 of trqcum_63d
def f44hcr_f44_healthcare_capital_return_trqcum_63d_jerk_v123_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: jerk window 5 of trqcum_126d
def f44hcr_f44_healthcare_capital_return_trqcum_126d_jerk_v124_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: jerk window 21 of trqcum_126d
def f44hcr_f44_healthcare_capital_return_trqcum_126d_jerk_v125_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126: jerk window 63 of trqcum_126d
def f44hcr_f44_healthcare_capital_return_trqcum_126d_jerk_v126_signal(dps, sharesbas, closeadj):
    base = _f44_total_return_quality(dps, sharesbas, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127: jerk window 5 of composite_63d
def f44hcr_f44_healthcare_capital_return_composite_63d_jerk_v127_signal(dps, sharesbas, closeadj):
    base = (_z(_f44_dps_growth(dps, 63), 252) + _z(_f44_share_buyback_intensity(sharesbas, 63), 252) + _z(_f44_total_return_quality(dps, sharesbas, 63), 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v128: jerk window 21 of composite_63d
def f44hcr_f44_healthcare_capital_return_composite_63d_jerk_v128_signal(dps, sharesbas, closeadj):
    base = (_z(_f44_dps_growth(dps, 63), 252) + _z(_f44_share_buyback_intensity(sharesbas, 63), 252) + _z(_f44_total_return_quality(dps, sharesbas, 63), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129: jerk window 63 of composite_63d
def f44hcr_f44_healthcare_capital_return_composite_63d_jerk_v129_signal(dps, sharesbas, closeadj):
    base = (_z(_f44_dps_growth(dps, 63), 252) + _z(_f44_share_buyback_intensity(sharesbas, 63), 252) + _z(_f44_total_return_quality(dps, sharesbas, 63), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130: jerk window 5 of composite_252d
def f44hcr_f44_healthcare_capital_return_composite_252d_jerk_v130_signal(dps, sharesbas, closeadj):
    base = (_z(_f44_dps_growth(dps, 252), 504) + _z(_f44_share_buyback_intensity(sharesbas, 252), 504) + _z(_f44_total_return_quality(dps, sharesbas, 252), 504)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v131: jerk window 21 of composite_252d
def f44hcr_f44_healthcare_capital_return_composite_252d_jerk_v131_signal(dps, sharesbas, closeadj):
    base = (_z(_f44_dps_growth(dps, 252), 504) + _z(_f44_share_buyback_intensity(sharesbas, 252), 504) + _z(_f44_total_return_quality(dps, sharesbas, 252), 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132: jerk window 63 of composite_252d
def f44hcr_f44_healthcare_capital_return_composite_252d_jerk_v132_signal(dps, sharesbas, closeadj):
    base = (_z(_f44_dps_growth(dps, 252), 504) + _z(_f44_share_buyback_intensity(sharesbas, 252), 504) + _z(_f44_total_return_quality(dps, sharesbas, 252), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133: jerk window 5 of dpsgxeps2_21d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_21d_jerk_v133_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 21) * eps.rolling(21, min_periods=10).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v134: jerk window 21 of dpsgxeps2_21d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_21d_jerk_v134_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 21) * eps.rolling(21, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135: jerk window 63 of dpsgxeps2_21d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_21d_jerk_v135_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 21) * eps.rolling(21, min_periods=10).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136: jerk window 5 of dpsgxeps2_63d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_63d_jerk_v136_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 63) * eps.rolling(63, min_periods=31).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v137: jerk window 21 of dpsgxeps2_63d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_63d_jerk_v137_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 63) * eps.rolling(63, min_periods=31).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138: jerk window 63 of dpsgxeps2_63d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_63d_jerk_v138_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 63) * eps.rolling(63, min_periods=31).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139: jerk window 5 of dpsgxeps2_252d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_252d_jerk_v139_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 252) * eps.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v140: jerk window 21 of dpsgxeps2_252d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_252d_jerk_v140_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 252) * eps.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141: jerk window 63 of dpsgxeps2_252d
def f44hcr_f44_healthcare_capital_return_dpsgxeps2_252d_jerk_v141_signal(dps, eps, closeadj):
    base = _f44_dps_growth(dps, 252) * eps.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: jerk window 5 of bbxshares_21d
def f44hcr_f44_healthcare_capital_return_bbxshares_21d_jerk_v142_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * _mean(sharesbas, 21) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: jerk window 21 of bbxshares_21d
def f44hcr_f44_healthcare_capital_return_bbxshares_21d_jerk_v143_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * _mean(sharesbas, 21) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v144: jerk window 63 of bbxshares_21d
def f44hcr_f44_healthcare_capital_return_bbxshares_21d_jerk_v144_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 21) * _mean(sharesbas, 21) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145: jerk window 5 of bbxshares_63d
def f44hcr_f44_healthcare_capital_return_bbxshares_63d_jerk_v145_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * _mean(sharesbas, 63) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146: jerk window 21 of bbxshares_63d
def f44hcr_f44_healthcare_capital_return_bbxshares_63d_jerk_v146_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * _mean(sharesbas, 63) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v147: jerk window 63 of bbxshares_63d
def f44hcr_f44_healthcare_capital_return_bbxshares_63d_jerk_v147_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 63) * _mean(sharesbas, 63) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v148: jerk window 5 of bbxshares_252d
def f44hcr_f44_healthcare_capital_return_bbxshares_252d_jerk_v148_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * _mean(sharesbas, 252) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: jerk window 21 of bbxshares_252d
def f44hcr_f44_healthcare_capital_return_bbxshares_252d_jerk_v149_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * _mean(sharesbas, 252) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: jerk window 63 of bbxshares_252d
def f44hcr_f44_healthcare_capital_return_bbxshares_252d_jerk_v150_signal(sharesbas, closeadj):
    base = _f44_share_buyback_intensity(sharesbas, 252) * _mean(sharesbas, 252) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44hcr_f44_healthcare_capital_return_dpsg_21d_jerk_v001_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_21d_jerk_v002_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_21d_jerk_v003_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_63d_jerk_v004_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_63d_jerk_v005_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_63d_jerk_v006_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_126d_jerk_v007_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_126d_jerk_v008_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_126d_jerk_v009_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_252d_jerk_v010_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_252d_jerk_v011_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_252d_jerk_v012_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_504d_jerk_v013_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_504d_jerk_v014_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_504d_jerk_v015_signal,
    f44hcr_f44_healthcare_capital_return_bb_21d_jerk_v016_signal,
    f44hcr_f44_healthcare_capital_return_bb_21d_jerk_v017_signal,
    f44hcr_f44_healthcare_capital_return_bb_21d_jerk_v018_signal,
    f44hcr_f44_healthcare_capital_return_bb_63d_jerk_v019_signal,
    f44hcr_f44_healthcare_capital_return_bb_63d_jerk_v020_signal,
    f44hcr_f44_healthcare_capital_return_bb_63d_jerk_v021_signal,
    f44hcr_f44_healthcare_capital_return_bb_126d_jerk_v022_signal,
    f44hcr_f44_healthcare_capital_return_bb_126d_jerk_v023_signal,
    f44hcr_f44_healthcare_capital_return_bb_126d_jerk_v024_signal,
    f44hcr_f44_healthcare_capital_return_bb_252d_jerk_v025_signal,
    f44hcr_f44_healthcare_capital_return_bb_252d_jerk_v026_signal,
    f44hcr_f44_healthcare_capital_return_bb_252d_jerk_v027_signal,
    f44hcr_f44_healthcare_capital_return_bb_504d_jerk_v028_signal,
    f44hcr_f44_healthcare_capital_return_bb_504d_jerk_v029_signal,
    f44hcr_f44_healthcare_capital_return_bb_504d_jerk_v030_signal,
    f44hcr_f44_healthcare_capital_return_trq_21d_jerk_v031_signal,
    f44hcr_f44_healthcare_capital_return_trq_21d_jerk_v032_signal,
    f44hcr_f44_healthcare_capital_return_trq_21d_jerk_v033_signal,
    f44hcr_f44_healthcare_capital_return_trq_63d_jerk_v034_signal,
    f44hcr_f44_healthcare_capital_return_trq_63d_jerk_v035_signal,
    f44hcr_f44_healthcare_capital_return_trq_63d_jerk_v036_signal,
    f44hcr_f44_healthcare_capital_return_trq_126d_jerk_v037_signal,
    f44hcr_f44_healthcare_capital_return_trq_126d_jerk_v038_signal,
    f44hcr_f44_healthcare_capital_return_trq_126d_jerk_v039_signal,
    f44hcr_f44_healthcare_capital_return_trq_252d_jerk_v040_signal,
    f44hcr_f44_healthcare_capital_return_trq_252d_jerk_v041_signal,
    f44hcr_f44_healthcare_capital_return_trq_252d_jerk_v042_signal,
    f44hcr_f44_healthcare_capital_return_trq_504d_jerk_v043_signal,
    f44hcr_f44_healthcare_capital_return_trq_504d_jerk_v044_signal,
    f44hcr_f44_healthcare_capital_return_trq_504d_jerk_v045_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_21d_jerk_v046_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_21d_jerk_v047_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_21d_jerk_v048_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_63d_jerk_v049_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_63d_jerk_v050_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_63d_jerk_v051_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_252d_jerk_v052_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_252d_jerk_v053_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_252d_jerk_v054_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_21d_jerk_v055_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_21d_jerk_v056_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_21d_jerk_v057_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_63d_jerk_v058_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_63d_jerk_v059_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_63d_jerk_v060_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_252d_jerk_v061_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_252d_jerk_v062_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_252d_jerk_v063_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_21d_jerk_v064_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_21d_jerk_v065_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_21d_jerk_v066_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_63d_jerk_v067_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_63d_jerk_v068_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_63d_jerk_v069_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_252d_jerk_v070_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_252d_jerk_v071_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_252d_jerk_v072_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_21d_jerk_v073_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_21d_jerk_v074_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_21d_jerk_v075_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_63d_jerk_v076_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_63d_jerk_v077_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_63d_jerk_v078_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_252d_jerk_v079_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_252d_jerk_v080_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_252d_jerk_v081_signal,
    f44hcr_f44_healthcare_capital_return_bbema_21d_jerk_v082_signal,
    f44hcr_f44_healthcare_capital_return_bbema_21d_jerk_v083_signal,
    f44hcr_f44_healthcare_capital_return_bbema_21d_jerk_v084_signal,
    f44hcr_f44_healthcare_capital_return_bbema_63d_jerk_v085_signal,
    f44hcr_f44_healthcare_capital_return_bbema_63d_jerk_v086_signal,
    f44hcr_f44_healthcare_capital_return_bbema_63d_jerk_v087_signal,
    f44hcr_f44_healthcare_capital_return_bbema_252d_jerk_v088_signal,
    f44hcr_f44_healthcare_capital_return_bbema_252d_jerk_v089_signal,
    f44hcr_f44_healthcare_capital_return_bbema_252d_jerk_v090_signal,
    f44hcr_f44_healthcare_capital_return_trqema_21d_jerk_v091_signal,
    f44hcr_f44_healthcare_capital_return_trqema_21d_jerk_v092_signal,
    f44hcr_f44_healthcare_capital_return_trqema_21d_jerk_v093_signal,
    f44hcr_f44_healthcare_capital_return_trqema_63d_jerk_v094_signal,
    f44hcr_f44_healthcare_capital_return_trqema_63d_jerk_v095_signal,
    f44hcr_f44_healthcare_capital_return_trqema_63d_jerk_v096_signal,
    f44hcr_f44_healthcare_capital_return_trqema_252d_jerk_v097_signal,
    f44hcr_f44_healthcare_capital_return_trqema_252d_jerk_v098_signal,
    f44hcr_f44_healthcare_capital_return_trqema_252d_jerk_v099_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_21d_jerk_v100_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_21d_jerk_v101_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_21d_jerk_v102_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_63d_jerk_v103_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_63d_jerk_v104_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_63d_jerk_v105_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_126d_jerk_v106_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_126d_jerk_v107_signal,
    f44hcr_f44_healthcare_capital_return_dpsgcum_126d_jerk_v108_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_21d_jerk_v109_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_21d_jerk_v110_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_21d_jerk_v111_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_63d_jerk_v112_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_63d_jerk_v113_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_63d_jerk_v114_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_126d_jerk_v115_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_126d_jerk_v116_signal,
    f44hcr_f44_healthcare_capital_return_bbcum_126d_jerk_v117_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_21d_jerk_v118_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_21d_jerk_v119_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_21d_jerk_v120_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_63d_jerk_v121_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_63d_jerk_v122_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_63d_jerk_v123_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_126d_jerk_v124_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_126d_jerk_v125_signal,
    f44hcr_f44_healthcare_capital_return_trqcum_126d_jerk_v126_signal,
    f44hcr_f44_healthcare_capital_return_composite_63d_jerk_v127_signal,
    f44hcr_f44_healthcare_capital_return_composite_63d_jerk_v128_signal,
    f44hcr_f44_healthcare_capital_return_composite_63d_jerk_v129_signal,
    f44hcr_f44_healthcare_capital_return_composite_252d_jerk_v130_signal,
    f44hcr_f44_healthcare_capital_return_composite_252d_jerk_v131_signal,
    f44hcr_f44_healthcare_capital_return_composite_252d_jerk_v132_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_21d_jerk_v133_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_21d_jerk_v134_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_21d_jerk_v135_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_63d_jerk_v136_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_63d_jerk_v137_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_63d_jerk_v138_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_252d_jerk_v139_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_252d_jerk_v140_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxeps2_252d_jerk_v141_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_21d_jerk_v142_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_21d_jerk_v143_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_21d_jerk_v144_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_63d_jerk_v145_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_63d_jerk_v146_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_63d_jerk_v147_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_252d_jerk_v148_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_252d_jerk_v149_signal,
    f44hcr_f44_healthcare_capital_return_bbxshares_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_HEALTHCARE_CAPITAL_RETURN_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    eps = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")

    cols = {
        "closeadj": closeadj,
        "dps": dps,
        "eps": eps,
        "sharesbas": sharesbas,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f44_dps_growth', '_f44_share_buyback_intensity', '_f44_total_return_quality',)
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f44_healthcare_capital_return_3rd_derivatives_001_150_claude: {n_features} features pass")
