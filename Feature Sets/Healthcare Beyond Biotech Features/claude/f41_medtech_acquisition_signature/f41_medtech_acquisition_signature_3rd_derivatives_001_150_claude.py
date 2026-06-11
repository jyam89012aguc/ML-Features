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
def _f41_intangibles_growth(intangibles, w):
    base = _mean(intangibles, max(2, w // 4))
    return base.pct_change(periods=w)


def _f41_asset_pulse(assets, intangibles, w):
    intang_share = intangibles / assets.replace(0, np.nan)
    return intang_share - intang_share.rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_acquisition_score(intangibles, capex, w):
    intang_diff = intangibles.diff(periods=w)
    spend = (intang_diff + capex.rolling(w, min_periods=max(1, w // 2)).sum())
    return spend / (intangibles.rolling(w, min_periods=max(1, w // 2)).mean()).replace(0, np.nan)

# v001: jerk window 5 of intanggr_21d
def f41mas_f41_medtech_acquisition_signature_intanggr_21d_jerk_v001_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002: jerk window 21 of intanggr_21d
def f41mas_f41_medtech_acquisition_signature_intanggr_21d_jerk_v002_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003: jerk window 63 of intanggr_21d
def f41mas_f41_medtech_acquisition_signature_intanggr_21d_jerk_v003_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v004: jerk window 5 of intanggr_63d
def f41mas_f41_medtech_acquisition_signature_intanggr_63d_jerk_v004_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v005: jerk window 21 of intanggr_63d
def f41mas_f41_medtech_acquisition_signature_intanggr_63d_jerk_v005_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v006: jerk window 63 of intanggr_63d
def f41mas_f41_medtech_acquisition_signature_intanggr_63d_jerk_v006_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007: jerk window 5 of intanggr_126d
def f41mas_f41_medtech_acquisition_signature_intanggr_126d_jerk_v007_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008: jerk window 21 of intanggr_126d
def f41mas_f41_medtech_acquisition_signature_intanggr_126d_jerk_v008_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009: jerk window 63 of intanggr_126d
def f41mas_f41_medtech_acquisition_signature_intanggr_126d_jerk_v009_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: jerk window 5 of intanggr_252d
def f41mas_f41_medtech_acquisition_signature_intanggr_252d_jerk_v010_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: jerk window 21 of intanggr_252d
def f41mas_f41_medtech_acquisition_signature_intanggr_252d_jerk_v011_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012: jerk window 63 of intanggr_252d
def f41mas_f41_medtech_acquisition_signature_intanggr_252d_jerk_v012_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013: jerk window 5 of intanggr_504d
def f41mas_f41_medtech_acquisition_signature_intanggr_504d_jerk_v013_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v014: jerk window 21 of intanggr_504d
def f41mas_f41_medtech_acquisition_signature_intanggr_504d_jerk_v014_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015: jerk window 63 of intanggr_504d
def f41mas_f41_medtech_acquisition_signature_intanggr_504d_jerk_v015_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016: jerk window 5 of assetpulse_21d
def f41mas_f41_medtech_acquisition_signature_assetpulse_21d_jerk_v016_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: jerk window 21 of assetpulse_21d
def f41mas_f41_medtech_acquisition_signature_assetpulse_21d_jerk_v017_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: jerk window 63 of assetpulse_21d
def f41mas_f41_medtech_acquisition_signature_assetpulse_21d_jerk_v018_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: jerk window 5 of assetpulse_63d
def f41mas_f41_medtech_acquisition_signature_assetpulse_63d_jerk_v019_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: jerk window 21 of assetpulse_63d
def f41mas_f41_medtech_acquisition_signature_assetpulse_63d_jerk_v020_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: jerk window 63 of assetpulse_63d
def f41mas_f41_medtech_acquisition_signature_assetpulse_63d_jerk_v021_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: jerk window 5 of assetpulse_126d
def f41mas_f41_medtech_acquisition_signature_assetpulse_126d_jerk_v022_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v023: jerk window 21 of assetpulse_126d
def f41mas_f41_medtech_acquisition_signature_assetpulse_126d_jerk_v023_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024: jerk window 63 of assetpulse_126d
def f41mas_f41_medtech_acquisition_signature_assetpulse_126d_jerk_v024_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025: jerk window 5 of assetpulse_252d
def f41mas_f41_medtech_acquisition_signature_assetpulse_252d_jerk_v025_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v026: jerk window 21 of assetpulse_252d
def f41mas_f41_medtech_acquisition_signature_assetpulse_252d_jerk_v026_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027: jerk window 63 of assetpulse_252d
def f41mas_f41_medtech_acquisition_signature_assetpulse_252d_jerk_v027_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028: jerk window 5 of assetpulse_504d
def f41mas_f41_medtech_acquisition_signature_assetpulse_504d_jerk_v028_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: jerk window 21 of assetpulse_504d
def f41mas_f41_medtech_acquisition_signature_assetpulse_504d_jerk_v029_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: jerk window 63 of assetpulse_504d
def f41mas_f41_medtech_acquisition_signature_assetpulse_504d_jerk_v030_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: jerk window 5 of acqscore_21d
def f41mas_f41_medtech_acquisition_signature_acqscore_21d_jerk_v031_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: jerk window 21 of acqscore_21d
def f41mas_f41_medtech_acquisition_signature_acqscore_21d_jerk_v032_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: jerk window 63 of acqscore_21d
def f41mas_f41_medtech_acquisition_signature_acqscore_21d_jerk_v033_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: jerk window 5 of acqscore_63d
def f41mas_f41_medtech_acquisition_signature_acqscore_63d_jerk_v034_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: jerk window 21 of acqscore_63d
def f41mas_f41_medtech_acquisition_signature_acqscore_63d_jerk_v035_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: jerk window 63 of acqscore_63d
def f41mas_f41_medtech_acquisition_signature_acqscore_63d_jerk_v036_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: jerk window 5 of acqscore_126d
def f41mas_f41_medtech_acquisition_signature_acqscore_126d_jerk_v037_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: jerk window 21 of acqscore_126d
def f41mas_f41_medtech_acquisition_signature_acqscore_126d_jerk_v038_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: jerk window 63 of acqscore_126d
def f41mas_f41_medtech_acquisition_signature_acqscore_126d_jerk_v039_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: jerk window 5 of acqscore_252d
def f41mas_f41_medtech_acquisition_signature_acqscore_252d_jerk_v040_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: jerk window 21 of acqscore_252d
def f41mas_f41_medtech_acquisition_signature_acqscore_252d_jerk_v041_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: jerk window 63 of acqscore_252d
def f41mas_f41_medtech_acquisition_signature_acqscore_252d_jerk_v042_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043: jerk window 5 of acqscore_504d
def f41mas_f41_medtech_acquisition_signature_acqscore_504d_jerk_v043_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v044: jerk window 21 of acqscore_504d
def f41mas_f41_medtech_acquisition_signature_acqscore_504d_jerk_v044_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045: jerk window 63 of acqscore_504d
def f41mas_f41_medtech_acquisition_signature_acqscore_504d_jerk_v045_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046: jerk window 5 of acqxgr_21d
def f41mas_f41_medtech_acquisition_signature_acqxgr_21d_jerk_v046_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _f41_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047: jerk window 21 of acqxgr_21d
def f41mas_f41_medtech_acquisition_signature_acqxgr_21d_jerk_v047_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _f41_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048: jerk window 63 of acqxgr_21d
def f41mas_f41_medtech_acquisition_signature_acqxgr_21d_jerk_v048_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _f41_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: jerk window 5 of acqxgr_63d
def f41mas_f41_medtech_acquisition_signature_acqxgr_63d_jerk_v049_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _f41_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: jerk window 21 of acqxgr_63d
def f41mas_f41_medtech_acquisition_signature_acqxgr_63d_jerk_v050_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _f41_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: jerk window 63 of acqxgr_63d
def f41mas_f41_medtech_acquisition_signature_acqxgr_63d_jerk_v051_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _f41_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: jerk window 5 of acqxgr_252d
def f41mas_f41_medtech_acquisition_signature_acqxgr_252d_jerk_v052_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _f41_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053: jerk window 21 of acqxgr_252d
def f41mas_f41_medtech_acquisition_signature_acqxgr_252d_jerk_v053_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _f41_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054: jerk window 63 of acqxgr_252d
def f41mas_f41_medtech_acquisition_signature_acqxgr_252d_jerk_v054_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _f41_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055: jerk window 5 of acqxpulse_21d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_jerk_v055_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v056: jerk window 21 of acqxpulse_21d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_jerk_v056_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057: jerk window 63 of acqxpulse_21d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_jerk_v057_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058: jerk window 5 of acqxpulse_63d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_jerk_v058_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: jerk window 21 of acqxpulse_63d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_jerk_v059_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: jerk window 63 of acqxpulse_63d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_jerk_v060_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: jerk window 5 of acqxpulse_252d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_jerk_v061_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: jerk window 21 of acqxpulse_252d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_jerk_v062_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: jerk window 63 of acqxpulse_252d
def f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_jerk_v063_signal(intangibles, capex, assets, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: jerk window 5 of grxpulse_21d
def f41mas_f41_medtech_acquisition_signature_grxpulse_21d_jerk_v064_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: jerk window 21 of grxpulse_21d
def f41mas_f41_medtech_acquisition_signature_grxpulse_21d_jerk_v065_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066: jerk window 63 of grxpulse_21d
def f41mas_f41_medtech_acquisition_signature_grxpulse_21d_jerk_v066_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * _f41_asset_pulse(assets, intangibles, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067: jerk window 5 of grxpulse_63d
def f41mas_f41_medtech_acquisition_signature_grxpulse_63d_jerk_v067_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v068: jerk window 21 of grxpulse_63d
def f41mas_f41_medtech_acquisition_signature_grxpulse_63d_jerk_v068_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069: jerk window 63 of grxpulse_63d
def f41mas_f41_medtech_acquisition_signature_grxpulse_63d_jerk_v069_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * _f41_asset_pulse(assets, intangibles, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070: jerk window 5 of grxpulse_252d
def f41mas_f41_medtech_acquisition_signature_grxpulse_252d_jerk_v070_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v071: jerk window 21 of grxpulse_252d
def f41mas_f41_medtech_acquisition_signature_grxpulse_252d_jerk_v071_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072: jerk window 63 of grxpulse_252d
def f41mas_f41_medtech_acquisition_signature_grxpulse_252d_jerk_v072_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * _f41_asset_pulse(assets, intangibles, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073: jerk window 5 of grema_21d
def f41mas_f41_medtech_acquisition_signature_grema_21d_jerk_v073_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v074: jerk window 21 of grema_21d
def f41mas_f41_medtech_acquisition_signature_grema_21d_jerk_v074_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075: jerk window 63 of grema_21d
def f41mas_f41_medtech_acquisition_signature_grema_21d_jerk_v075_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076: jerk window 5 of grema_63d
def f41mas_f41_medtech_acquisition_signature_grema_63d_jerk_v076_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v077: jerk window 21 of grema_63d
def f41mas_f41_medtech_acquisition_signature_grema_63d_jerk_v077_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078: jerk window 63 of grema_63d
def f41mas_f41_medtech_acquisition_signature_grema_63d_jerk_v078_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079: jerk window 5 of grema_252d
def f41mas_f41_medtech_acquisition_signature_grema_252d_jerk_v079_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v080: jerk window 21 of grema_252d
def f41mas_f41_medtech_acquisition_signature_grema_252d_jerk_v080_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081: jerk window 63 of grema_252d
def f41mas_f41_medtech_acquisition_signature_grema_252d_jerk_v081_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082: jerk window 5 of acqema_21d
def f41mas_f41_medtech_acquisition_signature_acqema_21d_jerk_v082_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v083: jerk window 21 of acqema_21d
def f41mas_f41_medtech_acquisition_signature_acqema_21d_jerk_v083_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084: jerk window 63 of acqema_21d
def f41mas_f41_medtech_acquisition_signature_acqema_21d_jerk_v084_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v085: jerk window 5 of acqema_63d
def f41mas_f41_medtech_acquisition_signature_acqema_63d_jerk_v085_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: jerk window 21 of acqema_63d
def f41mas_f41_medtech_acquisition_signature_acqema_63d_jerk_v086_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: jerk window 63 of acqema_63d
def f41mas_f41_medtech_acquisition_signature_acqema_63d_jerk_v087_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: jerk window 5 of acqema_252d
def f41mas_f41_medtech_acquisition_signature_acqema_252d_jerk_v088_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v089: jerk window 21 of acqema_252d
def f41mas_f41_medtech_acquisition_signature_acqema_252d_jerk_v089_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090: jerk window 63 of acqema_252d
def f41mas_f41_medtech_acquisition_signature_acqema_252d_jerk_v090_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091: jerk window 5 of pulseema_21d
def f41mas_f41_medtech_acquisition_signature_pulseema_21d_jerk_v091_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v092: jerk window 21 of pulseema_21d
def f41mas_f41_medtech_acquisition_signature_pulseema_21d_jerk_v092_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093: jerk window 63 of pulseema_21d
def f41mas_f41_medtech_acquisition_signature_pulseema_21d_jerk_v093_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094: jerk window 5 of pulseema_63d
def f41mas_f41_medtech_acquisition_signature_pulseema_63d_jerk_v094_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v095: jerk window 21 of pulseema_63d
def f41mas_f41_medtech_acquisition_signature_pulseema_63d_jerk_v095_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096: jerk window 63 of pulseema_63d
def f41mas_f41_medtech_acquisition_signature_pulseema_63d_jerk_v096_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097: jerk window 5 of pulseema_252d
def f41mas_f41_medtech_acquisition_signature_pulseema_252d_jerk_v097_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v098: jerk window 21 of pulseema_252d
def f41mas_f41_medtech_acquisition_signature_pulseema_252d_jerk_v098_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099: jerk window 63 of pulseema_252d
def f41mas_f41_medtech_acquisition_signature_pulseema_252d_jerk_v099_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100: jerk window 5 of grcum_21d
def f41mas_f41_medtech_acquisition_signature_grcum_21d_jerk_v100_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: jerk window 21 of grcum_21d
def f41mas_f41_medtech_acquisition_signature_grcum_21d_jerk_v101_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: jerk window 63 of grcum_21d
def f41mas_f41_medtech_acquisition_signature_grcum_21d_jerk_v102_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: jerk window 5 of grcum_63d
def f41mas_f41_medtech_acquisition_signature_grcum_63d_jerk_v103_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v104: jerk window 21 of grcum_63d
def f41mas_f41_medtech_acquisition_signature_grcum_63d_jerk_v104_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105: jerk window 63 of grcum_63d
def f41mas_f41_medtech_acquisition_signature_grcum_63d_jerk_v105_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106: jerk window 5 of grcum_126d
def f41mas_f41_medtech_acquisition_signature_grcum_126d_jerk_v106_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v107: jerk window 21 of grcum_126d
def f41mas_f41_medtech_acquisition_signature_grcum_126d_jerk_v107_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v108: jerk window 63 of grcum_126d
def f41mas_f41_medtech_acquisition_signature_grcum_126d_jerk_v108_signal(intangibles, closeadj):
    base = _f41_intangibles_growth(intangibles, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109: jerk window 5 of pulsecum_21d
def f41mas_f41_medtech_acquisition_signature_pulsecum_21d_jerk_v109_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v110: jerk window 21 of pulsecum_21d
def f41mas_f41_medtech_acquisition_signature_pulsecum_21d_jerk_v110_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111: jerk window 63 of pulsecum_21d
def f41mas_f41_medtech_acquisition_signature_pulsecum_21d_jerk_v111_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112: jerk window 5 of pulsecum_63d
def f41mas_f41_medtech_acquisition_signature_pulsecum_63d_jerk_v112_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v113: jerk window 21 of pulsecum_63d
def f41mas_f41_medtech_acquisition_signature_pulsecum_63d_jerk_v113_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114: jerk window 63 of pulsecum_63d
def f41mas_f41_medtech_acquisition_signature_pulsecum_63d_jerk_v114_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115: jerk window 5 of pulsecum_126d
def f41mas_f41_medtech_acquisition_signature_pulsecum_126d_jerk_v115_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v116: jerk window 21 of pulsecum_126d
def f41mas_f41_medtech_acquisition_signature_pulsecum_126d_jerk_v116_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117: jerk window 63 of pulsecum_126d
def f41mas_f41_medtech_acquisition_signature_pulsecum_126d_jerk_v117_signal(assets, intangibles, closeadj):
    base = _f41_asset_pulse(assets, intangibles, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118: jerk window 5 of acqcum_21d
def f41mas_f41_medtech_acquisition_signature_acqcum_21d_jerk_v118_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v119: jerk window 21 of acqcum_21d
def f41mas_f41_medtech_acquisition_signature_acqcum_21d_jerk_v119_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120: jerk window 63 of acqcum_21d
def f41mas_f41_medtech_acquisition_signature_acqcum_21d_jerk_v120_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121: jerk window 5 of acqcum_63d
def f41mas_f41_medtech_acquisition_signature_acqcum_63d_jerk_v121_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v122: jerk window 21 of acqcum_63d
def f41mas_f41_medtech_acquisition_signature_acqcum_63d_jerk_v122_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123: jerk window 63 of acqcum_63d
def f41mas_f41_medtech_acquisition_signature_acqcum_63d_jerk_v123_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: jerk window 5 of acqcum_126d
def f41mas_f41_medtech_acquisition_signature_acqcum_126d_jerk_v124_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: jerk window 21 of acqcum_126d
def f41mas_f41_medtech_acquisition_signature_acqcum_126d_jerk_v125_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126: jerk window 63 of acqcum_126d
def f41mas_f41_medtech_acquisition_signature_acqcum_126d_jerk_v126_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127: jerk window 5 of composite_63d
def f41mas_f41_medtech_acquisition_signature_composite_63d_jerk_v127_signal(intangibles, capex, assets, closeadj):
    base = (_z(_f41_intangibles_growth(intangibles, 63), 252) + _z(_f41_asset_pulse(assets, intangibles, 63), 252) + _z(_f41_acquisition_score(intangibles, capex, 63), 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v128: jerk window 21 of composite_63d
def f41mas_f41_medtech_acquisition_signature_composite_63d_jerk_v128_signal(intangibles, capex, assets, closeadj):
    base = (_z(_f41_intangibles_growth(intangibles, 63), 252) + _z(_f41_asset_pulse(assets, intangibles, 63), 252) + _z(_f41_acquisition_score(intangibles, capex, 63), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129: jerk window 63 of composite_63d
def f41mas_f41_medtech_acquisition_signature_composite_63d_jerk_v129_signal(intangibles, capex, assets, closeadj):
    base = (_z(_f41_intangibles_growth(intangibles, 63), 252) + _z(_f41_asset_pulse(assets, intangibles, 63), 252) + _z(_f41_acquisition_score(intangibles, capex, 63), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130: jerk window 5 of composite_252d
def f41mas_f41_medtech_acquisition_signature_composite_252d_jerk_v130_signal(intangibles, capex, assets, closeadj):
    base = (_z(_f41_intangibles_growth(intangibles, 252), 504) + _z(_f41_asset_pulse(assets, intangibles, 252), 504) + _z(_f41_acquisition_score(intangibles, capex, 252), 504)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v131: jerk window 21 of composite_252d
def f41mas_f41_medtech_acquisition_signature_composite_252d_jerk_v131_signal(intangibles, capex, assets, closeadj):
    base = (_z(_f41_intangibles_growth(intangibles, 252), 504) + _z(_f41_asset_pulse(assets, intangibles, 252), 504) + _z(_f41_acquisition_score(intangibles, capex, 252), 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132: jerk window 63 of composite_252d
def f41mas_f41_medtech_acquisition_signature_composite_252d_jerk_v132_signal(intangibles, capex, assets, closeadj):
    base = (_z(_f41_intangibles_growth(intangibles, 252), 504) + _z(_f41_asset_pulse(assets, intangibles, 252), 504) + _z(_f41_acquisition_score(intangibles, capex, 252), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133: jerk window 5 of grxshare_21d
def f41mas_f41_medtech_acquisition_signature_grxshare_21d_jerk_v133_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 21) * 0.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v134: jerk window 21 of grxshare_21d
def f41mas_f41_medtech_acquisition_signature_grxshare_21d_jerk_v134_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135: jerk window 63 of grxshare_21d
def f41mas_f41_medtech_acquisition_signature_grxshare_21d_jerk_v135_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 21) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 21) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136: jerk window 5 of grxshare_63d
def f41mas_f41_medtech_acquisition_signature_grxshare_63d_jerk_v136_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 63) * 0.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v137: jerk window 21 of grxshare_63d
def f41mas_f41_medtech_acquisition_signature_grxshare_63d_jerk_v137_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138: jerk window 63 of grxshare_63d
def f41mas_f41_medtech_acquisition_signature_grxshare_63d_jerk_v138_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 63) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139: jerk window 5 of grxshare_252d
def f41mas_f41_medtech_acquisition_signature_grxshare_252d_jerk_v139_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 252) * 0.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v140: jerk window 21 of grxshare_252d
def f41mas_f41_medtech_acquisition_signature_grxshare_252d_jerk_v140_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 252) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141: jerk window 63 of grxshare_252d
def f41mas_f41_medtech_acquisition_signature_grxshare_252d_jerk_v141_signal(intangibles, assets, closeadj):
    base = _f41_intangibles_growth(intangibles, 252) * (intangibles / assets.replace(0, np.nan)) * closeadj + _f41_asset_pulse(assets, intangibles, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: jerk window 5 of acqxcapex_21d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_21d_jerk_v142_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: jerk window 21 of acqxcapex_21d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_21d_jerk_v143_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v144: jerk window 63 of acqxcapex_21d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_21d_jerk_v144_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145: jerk window 5 of acqxcapex_63d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_63d_jerk_v145_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146: jerk window 21 of acqxcapex_63d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_63d_jerk_v146_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v147: jerk window 63 of acqxcapex_63d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_63d_jerk_v147_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v148: jerk window 5 of acqxcapex_252d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_252d_jerk_v148_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: jerk window 21 of acqxcapex_252d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_252d_jerk_v149_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: jerk window 63 of acqxcapex_252d
def f41mas_f41_medtech_acquisition_signature_acqxcapex_252d_jerk_v150_signal(intangibles, capex, closeadj):
    base = _f41_acquisition_score(intangibles, capex, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41mas_f41_medtech_acquisition_signature_intanggr_21d_jerk_v001_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_21d_jerk_v002_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_21d_jerk_v003_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_63d_jerk_v004_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_63d_jerk_v005_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_63d_jerk_v006_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_126d_jerk_v007_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_126d_jerk_v008_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_126d_jerk_v009_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_252d_jerk_v010_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_252d_jerk_v011_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_252d_jerk_v012_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_504d_jerk_v013_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_504d_jerk_v014_signal,
    f41mas_f41_medtech_acquisition_signature_intanggr_504d_jerk_v015_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_21d_jerk_v016_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_21d_jerk_v017_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_21d_jerk_v018_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_63d_jerk_v019_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_63d_jerk_v020_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_63d_jerk_v021_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_126d_jerk_v022_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_126d_jerk_v023_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_126d_jerk_v024_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_252d_jerk_v025_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_252d_jerk_v026_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_252d_jerk_v027_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_504d_jerk_v028_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_504d_jerk_v029_signal,
    f41mas_f41_medtech_acquisition_signature_assetpulse_504d_jerk_v030_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_21d_jerk_v031_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_21d_jerk_v032_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_21d_jerk_v033_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_63d_jerk_v034_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_63d_jerk_v035_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_63d_jerk_v036_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_126d_jerk_v037_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_126d_jerk_v038_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_126d_jerk_v039_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_252d_jerk_v040_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_252d_jerk_v041_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_252d_jerk_v042_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_504d_jerk_v043_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_504d_jerk_v044_signal,
    f41mas_f41_medtech_acquisition_signature_acqscore_504d_jerk_v045_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_21d_jerk_v046_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_21d_jerk_v047_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_21d_jerk_v048_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_63d_jerk_v049_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_63d_jerk_v050_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_63d_jerk_v051_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_252d_jerk_v052_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_252d_jerk_v053_signal,
    f41mas_f41_medtech_acquisition_signature_acqxgr_252d_jerk_v054_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_jerk_v055_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_jerk_v056_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_21d_jerk_v057_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_jerk_v058_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_jerk_v059_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_63d_jerk_v060_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_jerk_v061_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_jerk_v062_signal,
    f41mas_f41_medtech_acquisition_signature_acqxpulse_252d_jerk_v063_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_21d_jerk_v064_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_21d_jerk_v065_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_21d_jerk_v066_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_63d_jerk_v067_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_63d_jerk_v068_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_63d_jerk_v069_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_252d_jerk_v070_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_252d_jerk_v071_signal,
    f41mas_f41_medtech_acquisition_signature_grxpulse_252d_jerk_v072_signal,
    f41mas_f41_medtech_acquisition_signature_grema_21d_jerk_v073_signal,
    f41mas_f41_medtech_acquisition_signature_grema_21d_jerk_v074_signal,
    f41mas_f41_medtech_acquisition_signature_grema_21d_jerk_v075_signal,
    f41mas_f41_medtech_acquisition_signature_grema_63d_jerk_v076_signal,
    f41mas_f41_medtech_acquisition_signature_grema_63d_jerk_v077_signal,
    f41mas_f41_medtech_acquisition_signature_grema_63d_jerk_v078_signal,
    f41mas_f41_medtech_acquisition_signature_grema_252d_jerk_v079_signal,
    f41mas_f41_medtech_acquisition_signature_grema_252d_jerk_v080_signal,
    f41mas_f41_medtech_acquisition_signature_grema_252d_jerk_v081_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_21d_jerk_v082_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_21d_jerk_v083_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_21d_jerk_v084_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_63d_jerk_v085_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_63d_jerk_v086_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_63d_jerk_v087_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_252d_jerk_v088_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_252d_jerk_v089_signal,
    f41mas_f41_medtech_acquisition_signature_acqema_252d_jerk_v090_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_21d_jerk_v091_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_21d_jerk_v092_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_21d_jerk_v093_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_63d_jerk_v094_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_63d_jerk_v095_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_63d_jerk_v096_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_252d_jerk_v097_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_252d_jerk_v098_signal,
    f41mas_f41_medtech_acquisition_signature_pulseema_252d_jerk_v099_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_21d_jerk_v100_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_21d_jerk_v101_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_21d_jerk_v102_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_63d_jerk_v103_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_63d_jerk_v104_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_63d_jerk_v105_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_126d_jerk_v106_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_126d_jerk_v107_signal,
    f41mas_f41_medtech_acquisition_signature_grcum_126d_jerk_v108_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_21d_jerk_v109_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_21d_jerk_v110_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_21d_jerk_v111_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_63d_jerk_v112_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_63d_jerk_v113_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_63d_jerk_v114_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_126d_jerk_v115_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_126d_jerk_v116_signal,
    f41mas_f41_medtech_acquisition_signature_pulsecum_126d_jerk_v117_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_21d_jerk_v118_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_21d_jerk_v119_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_21d_jerk_v120_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_63d_jerk_v121_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_63d_jerk_v122_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_63d_jerk_v123_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_126d_jerk_v124_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_126d_jerk_v125_signal,
    f41mas_f41_medtech_acquisition_signature_acqcum_126d_jerk_v126_signal,
    f41mas_f41_medtech_acquisition_signature_composite_63d_jerk_v127_signal,
    f41mas_f41_medtech_acquisition_signature_composite_63d_jerk_v128_signal,
    f41mas_f41_medtech_acquisition_signature_composite_63d_jerk_v129_signal,
    f41mas_f41_medtech_acquisition_signature_composite_252d_jerk_v130_signal,
    f41mas_f41_medtech_acquisition_signature_composite_252d_jerk_v131_signal,
    f41mas_f41_medtech_acquisition_signature_composite_252d_jerk_v132_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_21d_jerk_v133_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_21d_jerk_v134_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_21d_jerk_v135_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_63d_jerk_v136_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_63d_jerk_v137_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_63d_jerk_v138_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_252d_jerk_v139_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_252d_jerk_v140_signal,
    f41mas_f41_medtech_acquisition_signature_grxshare_252d_jerk_v141_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_21d_jerk_v142_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_21d_jerk_v143_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_21d_jerk_v144_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_63d_jerk_v145_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_63d_jerk_v146_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_63d_jerk_v147_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_252d_jerk_v148_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_252d_jerk_v149_signal,
    f41mas_f41_medtech_acquisition_signature_acqxcapex_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_MEDTECH_ACQUISITION_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")

    cols = {
        "assets": assets,
        "capex": capex,
        "closeadj": closeadj,
        "intangibles": intangibles,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f41_intangibles_growth', '_f41_asset_pulse', '_f41_acquisition_score',)
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
    print(f"OK f41_medtech_acquisition_signature_3rd_derivatives_001_150_claude: {n_features} features pass")
