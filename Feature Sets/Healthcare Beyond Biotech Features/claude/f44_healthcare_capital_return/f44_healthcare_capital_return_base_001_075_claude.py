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

# v001: dpsg_21d
def f44hcr_f44_healthcare_capital_return_dpsg_21d_base_v001_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: dpsg_63d
def f44hcr_f44_healthcare_capital_return_dpsg_63d_base_v002_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: dpsg_126d
def f44hcr_f44_healthcare_capital_return_dpsg_126d_base_v003_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: dpsg_252d
def f44hcr_f44_healthcare_capital_return_dpsg_252d_base_v004_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: dpsg_504d
def f44hcr_f44_healthcare_capital_return_dpsg_504d_base_v005_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: bb_21d
def f44hcr_f44_healthcare_capital_return_bb_21d_base_v006_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: bb_63d
def f44hcr_f44_healthcare_capital_return_bb_63d_base_v007_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: bb_126d
def f44hcr_f44_healthcare_capital_return_bb_126d_base_v008_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: bb_252d
def f44hcr_f44_healthcare_capital_return_bb_252d_base_v009_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: bb_504d
def f44hcr_f44_healthcare_capital_return_bb_504d_base_v010_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: trq_21d
def f44hcr_f44_healthcare_capital_return_trq_21d_base_v011_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: trq_63d
def f44hcr_f44_healthcare_capital_return_trq_63d_base_v012_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: trq_126d
def f44hcr_f44_healthcare_capital_return_trq_126d_base_v013_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: trq_252d
def f44hcr_f44_healthcare_capital_return_trq_252d_base_v014_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: trq_504d
def f44hcr_f44_healthcare_capital_return_trq_504d_base_v015_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: dpsgsq_21d
def f44hcr_f44_healthcare_capital_return_dpsgsq_21d_base_v016_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: dpsgsq_63d
def f44hcr_f44_healthcare_capital_return_dpsgsq_63d_base_v017_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: dpsgsq_252d
def f44hcr_f44_healthcare_capital_return_dpsgsq_252d_base_v018_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 252).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: bbsq_21d
def f44hcr_f44_healthcare_capital_return_bbsq_21d_base_v019_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: bbsq_63d
def f44hcr_f44_healthcare_capital_return_bbsq_63d_base_v020_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021: bbsq_252d
def f44hcr_f44_healthcare_capital_return_bbsq_252d_base_v021_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 252).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: trqsq_21d
def f44hcr_f44_healthcare_capital_return_trqsq_21d_base_v022_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: trqsq_63d
def f44hcr_f44_healthcare_capital_return_trqsq_63d_base_v023_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: trqsq_252d
def f44hcr_f44_healthcare_capital_return_trqsq_252d_base_v024_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 252).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: dpsgz_21d
def f44hcr_f44_healthcare_capital_return_dpsgz_21d_base_v025_signal(dps, closeadj):
    result = _z(_f44_dps_growth(dps, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: dpsgz_63d
def f44hcr_f44_healthcare_capital_return_dpsgz_63d_base_v026_signal(dps, closeadj):
    result = _z(_f44_dps_growth(dps, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: dpsgz_252d
def f44hcr_f44_healthcare_capital_return_dpsgz_252d_base_v027_signal(dps, closeadj):
    result = _z(_f44_dps_growth(dps, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: bbz_21d
def f44hcr_f44_healthcare_capital_return_bbz_21d_base_v028_signal(sharesbas, closeadj):
    result = _z(_f44_share_buyback_intensity(sharesbas, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: bbz_63d
def f44hcr_f44_healthcare_capital_return_bbz_63d_base_v029_signal(sharesbas, closeadj):
    result = _z(_f44_share_buyback_intensity(sharesbas, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: bbz_252d
def f44hcr_f44_healthcare_capital_return_bbz_252d_base_v030_signal(sharesbas, closeadj):
    result = _z(_f44_share_buyback_intensity(sharesbas, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031: trqz_21d
def f44hcr_f44_healthcare_capital_return_trqz_21d_base_v031_signal(dps, sharesbas, closeadj):
    result = _z(_f44_total_return_quality(dps, sharesbas, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: trqz_63d
def f44hcr_f44_healthcare_capital_return_trqz_63d_base_v032_signal(dps, sharesbas, closeadj):
    result = _z(_f44_total_return_quality(dps, sharesbas, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: trqz_252d
def f44hcr_f44_healthcare_capital_return_trqz_252d_base_v033_signal(dps, sharesbas, closeadj):
    result = _z(_f44_total_return_quality(dps, sharesbas, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: dpsxbb_21d
def f44hcr_f44_healthcare_capital_return_dpsxbb_21d_base_v034_signal(dps, sharesbas, closeadj):
    result = _f44_dps_growth(dps, 21) * _f44_share_buyback_intensity(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: dpsxbb_63d
def f44hcr_f44_healthcare_capital_return_dpsxbb_63d_base_v035_signal(dps, sharesbas, closeadj):
    result = _f44_dps_growth(dps, 63) * _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036: dpsxbb_252d
def f44hcr_f44_healthcare_capital_return_dpsxbb_252d_base_v036_signal(dps, sharesbas, closeadj):
    result = _f44_dps_growth(dps, 252) * _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037: dpsxeps_21d
def f44hcr_f44_healthcare_capital_return_dpsxeps_21d_base_v037_signal(dps, eps, closeadj):
    result = _f44_dps_growth(dps, 21) * _mean(eps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038: dpsxeps_63d
def f44hcr_f44_healthcare_capital_return_dpsxeps_63d_base_v038_signal(dps, eps, closeadj):
    result = _f44_dps_growth(dps, 63) * _mean(eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: dpsxeps_252d
def f44hcr_f44_healthcare_capital_return_dpsxeps_252d_base_v039_signal(dps, eps, closeadj):
    result = _f44_dps_growth(dps, 252) * _mean(eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: bbxeps_21d
def f44hcr_f44_healthcare_capital_return_bbxeps_21d_base_v040_signal(sharesbas, eps, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21) * _mean(eps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: bbxeps_63d
def f44hcr_f44_healthcare_capital_return_bbxeps_63d_base_v041_signal(sharesbas, eps, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63) * _mean(eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: bbxeps_252d
def f44hcr_f44_healthcare_capital_return_bbxeps_252d_base_v042_signal(sharesbas, eps, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 252) * _mean(eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: trqxeps_21d
def f44hcr_f44_healthcare_capital_return_trqxeps_21d_base_v043_signal(dps, sharesbas, eps, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21) * _mean(eps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: trqxeps_63d
def f44hcr_f44_healthcare_capital_return_trqxeps_63d_base_v044_signal(dps, sharesbas, eps, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63) * _mean(eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: trqxeps_252d
def f44hcr_f44_healthcare_capital_return_trqxeps_252d_base_v045_signal(dps, sharesbas, eps, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 252) * _mean(eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: dpsgema_21d
def f44hcr_f44_healthcare_capital_return_dpsgema_21d_base_v046_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: dpsgema_63d
def f44hcr_f44_healthcare_capital_return_dpsgema_63d_base_v047_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: dpsgema_252d
def f44hcr_f44_healthcare_capital_return_dpsgema_252d_base_v048_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: bbema_21d
def f44hcr_f44_healthcare_capital_return_bbema_21d_base_v049_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: bbema_63d
def f44hcr_f44_healthcare_capital_return_bbema_63d_base_v050_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: bbema_252d
def f44hcr_f44_healthcare_capital_return_bbema_252d_base_v051_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: trqema_21d
def f44hcr_f44_healthcare_capital_return_trqema_21d_base_v052_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: trqema_63d
def f44hcr_f44_healthcare_capital_return_trqema_63d_base_v053_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: trqema_252d
def f44hcr_f44_healthcare_capital_return_trqema_252d_base_v054_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: dpsgstd_21d
def f44hcr_f44_healthcare_capital_return_dpsgstd_21d_base_v055_signal(dps, closeadj):
    result = _std(_f44_dps_growth(dps, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: dpsgstd_63d
def f44hcr_f44_healthcare_capital_return_dpsgstd_63d_base_v056_signal(dps, closeadj):
    result = _std(_f44_dps_growth(dps, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: dpsgstd_126d
def f44hcr_f44_healthcare_capital_return_dpsgstd_126d_base_v057_signal(dps, closeadj):
    result = _std(_f44_dps_growth(dps, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: bbstd_21d
def f44hcr_f44_healthcare_capital_return_bbstd_21d_base_v058_signal(sharesbas, closeadj):
    result = _std(_f44_share_buyback_intensity(sharesbas, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059: bbstd_63d
def f44hcr_f44_healthcare_capital_return_bbstd_63d_base_v059_signal(sharesbas, closeadj):
    result = _std(_f44_share_buyback_intensity(sharesbas, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060: bbstd_126d
def f44hcr_f44_healthcare_capital_return_bbstd_126d_base_v060_signal(sharesbas, closeadj):
    result = _std(_f44_share_buyback_intensity(sharesbas, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061: trqstd_21d
def f44hcr_f44_healthcare_capital_return_trqstd_21d_base_v061_signal(dps, sharesbas, closeadj):
    result = _std(_f44_total_return_quality(dps, sharesbas, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062: trqstd_63d
def f44hcr_f44_healthcare_capital_return_trqstd_63d_base_v062_signal(dps, sharesbas, closeadj):
    result = _std(_f44_total_return_quality(dps, sharesbas, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: trqstd_126d
def f44hcr_f44_healthcare_capital_return_trqstd_126d_base_v063_signal(dps, sharesbas, closeadj):
    result = _std(_f44_total_return_quality(dps, sharesbas, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064: dpsgqr_21d
def f44hcr_f44_healthcare_capital_return_dpsgqr_21d_base_v064_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: dpsgqr_63d
def f44hcr_f44_healthcare_capital_return_dpsgqr_63d_base_v065_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: dpsgqr_252d
def f44hcr_f44_healthcare_capital_return_dpsgqr_252d_base_v066_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: bbqr_21d
def f44hcr_f44_healthcare_capital_return_bbqr_21d_base_v067_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: bbqr_63d
def f44hcr_f44_healthcare_capital_return_bbqr_63d_base_v068_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: bbqr_252d
def f44hcr_f44_healthcare_capital_return_bbqr_252d_base_v069_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: trqqr_21d
def f44hcr_f44_healthcare_capital_return_trqqr_21d_base_v070_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: trqqr_63d
def f44hcr_f44_healthcare_capital_return_trqqr_63d_base_v071_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63).rolling(252, min_periods=84).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: trqqr_252d
def f44hcr_f44_healthcare_capital_return_trqqr_252d_base_v072_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 252).rolling(504, min_periods=168).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: composite_63d
def f44hcr_f44_healthcare_capital_return_composite_63d_base_v073_signal(dps, sharesbas, closeadj):
    result = (_z(_f44_dps_growth(dps, 63), 252) + _z(_f44_share_buyback_intensity(sharesbas, 63), 252) + _z(_f44_total_return_quality(dps, sharesbas, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: composite_252d
def f44hcr_f44_healthcare_capital_return_composite_252d_base_v074_signal(dps, sharesbas, closeadj):
    result = (_z(_f44_dps_growth(dps, 252), 504) + _z(_f44_share_buyback_intensity(sharesbas, 252), 504) + _z(_f44_total_return_quality(dps, sharesbas, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: composite_126d
def f44hcr_f44_healthcare_capital_return_composite_126d_base_v075_signal(dps, sharesbas, closeadj):
    result = (_z(_f44_dps_growth(dps, 126), 252) + _z(_f44_share_buyback_intensity(sharesbas, 126), 252) + _z(_f44_total_return_quality(dps, sharesbas, 126), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44hcr_f44_healthcare_capital_return_dpsg_21d_base_v001_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_63d_base_v002_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_126d_base_v003_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_252d_base_v004_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_504d_base_v005_signal,
    f44hcr_f44_healthcare_capital_return_bb_21d_base_v006_signal,
    f44hcr_f44_healthcare_capital_return_bb_63d_base_v007_signal,
    f44hcr_f44_healthcare_capital_return_bb_126d_base_v008_signal,
    f44hcr_f44_healthcare_capital_return_bb_252d_base_v009_signal,
    f44hcr_f44_healthcare_capital_return_bb_504d_base_v010_signal,
    f44hcr_f44_healthcare_capital_return_trq_21d_base_v011_signal,
    f44hcr_f44_healthcare_capital_return_trq_63d_base_v012_signal,
    f44hcr_f44_healthcare_capital_return_trq_126d_base_v013_signal,
    f44hcr_f44_healthcare_capital_return_trq_252d_base_v014_signal,
    f44hcr_f44_healthcare_capital_return_trq_504d_base_v015_signal,
    f44hcr_f44_healthcare_capital_return_dpsgsq_21d_base_v016_signal,
    f44hcr_f44_healthcare_capital_return_dpsgsq_63d_base_v017_signal,
    f44hcr_f44_healthcare_capital_return_dpsgsq_252d_base_v018_signal,
    f44hcr_f44_healthcare_capital_return_bbsq_21d_base_v019_signal,
    f44hcr_f44_healthcare_capital_return_bbsq_63d_base_v020_signal,
    f44hcr_f44_healthcare_capital_return_bbsq_252d_base_v021_signal,
    f44hcr_f44_healthcare_capital_return_trqsq_21d_base_v022_signal,
    f44hcr_f44_healthcare_capital_return_trqsq_63d_base_v023_signal,
    f44hcr_f44_healthcare_capital_return_trqsq_252d_base_v024_signal,
    f44hcr_f44_healthcare_capital_return_dpsgz_21d_base_v025_signal,
    f44hcr_f44_healthcare_capital_return_dpsgz_63d_base_v026_signal,
    f44hcr_f44_healthcare_capital_return_dpsgz_252d_base_v027_signal,
    f44hcr_f44_healthcare_capital_return_bbz_21d_base_v028_signal,
    f44hcr_f44_healthcare_capital_return_bbz_63d_base_v029_signal,
    f44hcr_f44_healthcare_capital_return_bbz_252d_base_v030_signal,
    f44hcr_f44_healthcare_capital_return_trqz_21d_base_v031_signal,
    f44hcr_f44_healthcare_capital_return_trqz_63d_base_v032_signal,
    f44hcr_f44_healthcare_capital_return_trqz_252d_base_v033_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_21d_base_v034_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_63d_base_v035_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_252d_base_v036_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_21d_base_v037_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_63d_base_v038_signal,
    f44hcr_f44_healthcare_capital_return_dpsxeps_252d_base_v039_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_21d_base_v040_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_63d_base_v041_signal,
    f44hcr_f44_healthcare_capital_return_bbxeps_252d_base_v042_signal,
    f44hcr_f44_healthcare_capital_return_trqxeps_21d_base_v043_signal,
    f44hcr_f44_healthcare_capital_return_trqxeps_63d_base_v044_signal,
    f44hcr_f44_healthcare_capital_return_trqxeps_252d_base_v045_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_21d_base_v046_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_63d_base_v047_signal,
    f44hcr_f44_healthcare_capital_return_dpsgema_252d_base_v048_signal,
    f44hcr_f44_healthcare_capital_return_bbema_21d_base_v049_signal,
    f44hcr_f44_healthcare_capital_return_bbema_63d_base_v050_signal,
    f44hcr_f44_healthcare_capital_return_bbema_252d_base_v051_signal,
    f44hcr_f44_healthcare_capital_return_trqema_21d_base_v052_signal,
    f44hcr_f44_healthcare_capital_return_trqema_63d_base_v053_signal,
    f44hcr_f44_healthcare_capital_return_trqema_252d_base_v054_signal,
    f44hcr_f44_healthcare_capital_return_dpsgstd_21d_base_v055_signal,
    f44hcr_f44_healthcare_capital_return_dpsgstd_63d_base_v056_signal,
    f44hcr_f44_healthcare_capital_return_dpsgstd_126d_base_v057_signal,
    f44hcr_f44_healthcare_capital_return_bbstd_21d_base_v058_signal,
    f44hcr_f44_healthcare_capital_return_bbstd_63d_base_v059_signal,
    f44hcr_f44_healthcare_capital_return_bbstd_126d_base_v060_signal,
    f44hcr_f44_healthcare_capital_return_trqstd_21d_base_v061_signal,
    f44hcr_f44_healthcare_capital_return_trqstd_63d_base_v062_signal,
    f44hcr_f44_healthcare_capital_return_trqstd_126d_base_v063_signal,
    f44hcr_f44_healthcare_capital_return_dpsgqr_21d_base_v064_signal,
    f44hcr_f44_healthcare_capital_return_dpsgqr_63d_base_v065_signal,
    f44hcr_f44_healthcare_capital_return_dpsgqr_252d_base_v066_signal,
    f44hcr_f44_healthcare_capital_return_bbqr_21d_base_v067_signal,
    f44hcr_f44_healthcare_capital_return_bbqr_63d_base_v068_signal,
    f44hcr_f44_healthcare_capital_return_bbqr_252d_base_v069_signal,
    f44hcr_f44_healthcare_capital_return_trqqr_21d_base_v070_signal,
    f44hcr_f44_healthcare_capital_return_trqqr_63d_base_v071_signal,
    f44hcr_f44_healthcare_capital_return_trqqr_252d_base_v072_signal,
    f44hcr_f44_healthcare_capital_return_composite_63d_base_v073_signal,
    f44hcr_f44_healthcare_capital_return_composite_252d_base_v074_signal,
    f44hcr_f44_healthcare_capital_return_composite_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_HEALTHCARE_CAPITAL_RETURN_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f44_healthcare_capital_return_base_001_075_claude: {n_features} features pass")
