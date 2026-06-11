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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f30_distress_proxy(equity, assets, w):
    eqr = equity / assets.replace(0, np.nan)
    return eqr - eqr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_roa_collapse(roa, w):
    return roa - roa.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_distress_score(roa, de, w):
    score = roa - de / 10.0
    return score - score.rolling(w, min_periods=max(1, w // 2)).mean()


def f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v001_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v002_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v003_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v004_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v005_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v006_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v007_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v008_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v009_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v010_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v011_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v012_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v013_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v014_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v015_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v016_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v017_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v018_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v019_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v020_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v021_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v022_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v023_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v024_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v025_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v026_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v027_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v028_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v029_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v030_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v031_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v032_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v033_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v034_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v035_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v036_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v037_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v038_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v039_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v040_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v041_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v042_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v043_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v044_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v045_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v046_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v047_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v048_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v049_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v050_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v051_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v052_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v053_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v054_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v055_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v056_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v057_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v058_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v059_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v060_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v061_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v062_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v063_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v064_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v065_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v066_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v067_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v068_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v069_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v070_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v071_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v072_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v073_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v074_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v075_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v076_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v077_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v078_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v079_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v080_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v081_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v082_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v083_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v084_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v085_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v086_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v087_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v088_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v089_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v090_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v091_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v092_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v093_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v094_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v095_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v096_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v097_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v098_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v099_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v100_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v101_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v102_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v103_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v104_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v105_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v106_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v107_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v108_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v109_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v110_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v111_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v112_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v113_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v114_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v115_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v116_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v117_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v118_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v119_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v120_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v121_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v122_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v123_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v124_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v125_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v126_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v127_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v128_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v129_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v130_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v131_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v132_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v133_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v134_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v135_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v136_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v137_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v138_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v139_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v140_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v141_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v142_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v143_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v144_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v145_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v146_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v147_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_jerk_v148_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v149_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v150_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v001_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v002_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v003_signal,
    f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v004_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v005_signal,
    f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v006_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v007_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v008_signal,
    f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v009_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v010_signal,
    f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v011_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v012_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v013_signal,
    f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v014_signal,
    f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v015_signal,
    f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v016_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v017_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v018_signal,
    f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v019_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v020_signal,
    f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v021_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v022_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v023_signal,
    f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v024_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v025_signal,
    f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v026_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v027_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v028_signal,
    f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v029_signal,
    f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v030_signal,
    f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v031_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v032_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v033_signal,
    f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v034_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v035_signal,
    f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v036_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v037_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v038_signal,
    f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v039_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v040_signal,
    f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v041_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v042_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v043_signal,
    f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v044_signal,
    f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v045_signal,
    f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v046_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v047_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v048_signal,
    f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v049_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v050_signal,
    f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v051_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v052_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v053_signal,
    f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v054_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v055_signal,
    f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v056_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v057_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v058_signal,
    f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v059_signal,
    f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v060_signal,
    f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v061_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v062_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v063_signal,
    f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v064_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v065_signal,
    f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v066_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v067_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v068_signal,
    f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v069_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v070_signal,
    f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v071_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v072_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v073_signal,
    f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v074_signal,
    f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v075_signal,
    f30bds_f30_bank_distress_signature_distproxraw_21d_jerk_v076_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v077_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v078_signal,
    f30bds_f30_bank_distress_signature_distproxabs_21d_jerk_v079_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_21d_jerk_v080_signal,
    f30bds_f30_bank_distress_signature_roacollraw_21d_jerk_v081_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v082_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v083_signal,
    f30bds_f30_bank_distress_signature_roacollabs_21d_jerk_v084_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_21d_jerk_v085_signal,
    f30bds_f30_bank_distress_signature_distscraw_21d_jerk_v086_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v087_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v088_signal,
    f30bds_f30_bank_distress_signature_distscabs_21d_jerk_v089_signal,
    f30bds_f30_bank_distress_signature_distscscaled_21d_jerk_v090_signal,
    f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v091_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v092_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v093_signal,
    f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v094_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v095_signal,
    f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v096_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v097_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v098_signal,
    f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v099_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v100_signal,
    f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v101_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v102_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v103_signal,
    f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v104_signal,
    f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v105_signal,
    f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v106_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v107_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v108_signal,
    f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v109_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v110_signal,
    f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v111_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v112_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v113_signal,
    f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v114_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v115_signal,
    f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v116_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v117_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v118_signal,
    f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v119_signal,
    f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v120_signal,
    f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v121_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v122_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v123_signal,
    f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v124_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v125_signal,
    f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v126_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v127_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v128_signal,
    f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v129_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v130_signal,
    f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v131_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v132_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v133_signal,
    f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v134_signal,
    f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v135_signal,
    f30bds_f30_bank_distress_signature_distproxraw_42d_jerk_v136_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_jerk_v137_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_jerk_v138_signal,
    f30bds_f30_bank_distress_signature_distproxabs_42d_jerk_v139_signal,
    f30bds_f30_bank_distress_signature_distproxscaled_42d_jerk_v140_signal,
    f30bds_f30_bank_distress_signature_roacollraw_42d_jerk_v141_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_jerk_v142_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_jerk_v143_signal,
    f30bds_f30_bank_distress_signature_roacollabs_42d_jerk_v144_signal,
    f30bds_f30_bank_distress_signature_roacollscaled_42d_jerk_v145_signal,
    f30bds_f30_bank_distress_signature_distscraw_42d_jerk_v146_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_jerk_v147_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_jerk_v148_signal,
    f30bds_f30_bank_distress_signature_distscabs_42d_jerk_v149_signal,
    f30bds_f30_bank_distress_signature_distscscaled_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_BANK_DISTRESS_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    de = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"roa": roa, "de": de, "equity": equity, "assets": assets, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_distress_proxy", "_f30_roa_collapse", "_f30_distress_score")
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
    print(f"OK f30_bank_distress_signature_3rd_derivatives_001_150_claude: {n_features} features pass")
