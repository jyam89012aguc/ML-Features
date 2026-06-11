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
def _f30_distress_proxy(equity, assets, w):
    eqr = equity / assets.replace(0, np.nan)
    return eqr - eqr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_roa_collapse(roa, w):
    return roa - roa.rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_distress_score(roa, de, w):
    score = roa - de / 10.0
    return score - score.rolling(w, min_periods=max(1, w // 2)).mean()


def f30bds_f30_bank_distress_signature_distproxraw_21d_base_v001_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_base_v002_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxstd_21d_base_v003_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_base_v004_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_21d_base_v005_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsq_21d_base_v006_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsign_21d_base_v007_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxlog_21d_base_v008_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrng_21d_base_v009_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxdv_21d_base_v010_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxpos_21d_base_v011_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxneg_21d_base_v012_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_21d_base_v013_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_base_v014_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollstd_21d_base_v015_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_base_v016_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_21d_base_v017_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsq_21d_base_v018_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsign_21d_base_v019_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolllog_21d_base_v020_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrng_21d_base_v021_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolldv_21d_base_v022_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollpos_21d_base_v023_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollneg_21d_base_v024_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_21d_base_v025_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_base_v026_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscstd_21d_base_v027_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_base_v028_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_21d_base_v029_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsq_21d_base_v030_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsign_21d_base_v031_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsclog_21d_base_v032_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrng_21d_base_v033_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    rng = base.rolling(21, min_periods=max(1, 21 // 2)).max() - base.rolling(21, min_periods=max(1, 21 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscdv_21d_base_v034_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = base * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscpos_21d_base_v035_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscneg_21d_base_v036_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 21) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_42d_base_v037_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_base_v038_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxstd_21d_base_v039_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxz_21d_base_v040_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxabs_42d_base_v041_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsq_42d_base_v042_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsign_21d_base_v043_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxlog_42d_base_v044_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxrng_21d_base_v045_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxdv_21d_base_v046_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxpos_21d_base_v047_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxneg_21d_base_v048_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollraw_42d_base_v049_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsm_21d_base_v050_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollstd_21d_base_v051_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollz_21d_base_v052_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollabs_42d_base_v053_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsq_42d_base_v054_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollsign_21d_base_v055_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolllog_42d_base_v056_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollrng_21d_base_v057_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacolldv_21d_base_v058_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollpos_21d_base_v059_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_roacollneg_21d_base_v060_signal(roa, closeadj):
    base = _f30_roa_collapse(roa, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscraw_42d_base_v061_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsm_21d_base_v062_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscstd_21d_base_v063_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscz_21d_base_v064_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscabs_42d_base_v065_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsq_42d_base_v066_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscsign_21d_base_v067_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distsclog_42d_base_v068_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 42)
    result = np.sign(base) * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscrng_21d_base_v069_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    rng = base.rolling(63, min_periods=max(1, 63 // 2)).max() - base.rolling(63, min_periods=max(1, 63 // 2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscdv_21d_base_v070_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscpos_21d_base_v071_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base > med).astype(float) * closeadj + base * 0.0005 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distscneg_21d_base_v072_signal(roa, de, closeadj):
    base = _f30_distress_score(roa, de, 21)
    med = base.rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (base < med).astype(float) * _mean(closeadj, 63) + base * 0.001 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxraw_63d_base_v073_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxsm_21d_base_v074_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f30bds_f30_bank_distress_signature_distproxstd_21d_base_v075_signal(equity, assets, closeadj):
    base = _f30_distress_proxy(equity, assets, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f30bds_f30_bank_distress_signature_distproxraw_21d_base_v001_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_base_v002_signal,
    f30bds_f30_bank_distress_signature_distproxstd_21d_base_v003_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_base_v004_signal,
    f30bds_f30_bank_distress_signature_distproxabs_21d_base_v005_signal,
    f30bds_f30_bank_distress_signature_distproxsq_21d_base_v006_signal,
    f30bds_f30_bank_distress_signature_distproxsign_21d_base_v007_signal,
    f30bds_f30_bank_distress_signature_distproxlog_21d_base_v008_signal,
    f30bds_f30_bank_distress_signature_distproxrng_21d_base_v009_signal,
    f30bds_f30_bank_distress_signature_distproxdv_21d_base_v010_signal,
    f30bds_f30_bank_distress_signature_distproxpos_21d_base_v011_signal,
    f30bds_f30_bank_distress_signature_distproxneg_21d_base_v012_signal,
    f30bds_f30_bank_distress_signature_roacollraw_21d_base_v013_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_base_v014_signal,
    f30bds_f30_bank_distress_signature_roacollstd_21d_base_v015_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_base_v016_signal,
    f30bds_f30_bank_distress_signature_roacollabs_21d_base_v017_signal,
    f30bds_f30_bank_distress_signature_roacollsq_21d_base_v018_signal,
    f30bds_f30_bank_distress_signature_roacollsign_21d_base_v019_signal,
    f30bds_f30_bank_distress_signature_roacolllog_21d_base_v020_signal,
    f30bds_f30_bank_distress_signature_roacollrng_21d_base_v021_signal,
    f30bds_f30_bank_distress_signature_roacolldv_21d_base_v022_signal,
    f30bds_f30_bank_distress_signature_roacollpos_21d_base_v023_signal,
    f30bds_f30_bank_distress_signature_roacollneg_21d_base_v024_signal,
    f30bds_f30_bank_distress_signature_distscraw_21d_base_v025_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_base_v026_signal,
    f30bds_f30_bank_distress_signature_distscstd_21d_base_v027_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_base_v028_signal,
    f30bds_f30_bank_distress_signature_distscabs_21d_base_v029_signal,
    f30bds_f30_bank_distress_signature_distscsq_21d_base_v030_signal,
    f30bds_f30_bank_distress_signature_distscsign_21d_base_v031_signal,
    f30bds_f30_bank_distress_signature_distsclog_21d_base_v032_signal,
    f30bds_f30_bank_distress_signature_distscrng_21d_base_v033_signal,
    f30bds_f30_bank_distress_signature_distscdv_21d_base_v034_signal,
    f30bds_f30_bank_distress_signature_distscpos_21d_base_v035_signal,
    f30bds_f30_bank_distress_signature_distscneg_21d_base_v036_signal,
    f30bds_f30_bank_distress_signature_distproxraw_42d_base_v037_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_base_v038_signal,
    f30bds_f30_bank_distress_signature_distproxstd_21d_base_v039_signal,
    f30bds_f30_bank_distress_signature_distproxz_21d_base_v040_signal,
    f30bds_f30_bank_distress_signature_distproxabs_42d_base_v041_signal,
    f30bds_f30_bank_distress_signature_distproxsq_42d_base_v042_signal,
    f30bds_f30_bank_distress_signature_distproxsign_21d_base_v043_signal,
    f30bds_f30_bank_distress_signature_distproxlog_42d_base_v044_signal,
    f30bds_f30_bank_distress_signature_distproxrng_21d_base_v045_signal,
    f30bds_f30_bank_distress_signature_distproxdv_21d_base_v046_signal,
    f30bds_f30_bank_distress_signature_distproxpos_21d_base_v047_signal,
    f30bds_f30_bank_distress_signature_distproxneg_21d_base_v048_signal,
    f30bds_f30_bank_distress_signature_roacollraw_42d_base_v049_signal,
    f30bds_f30_bank_distress_signature_roacollsm_21d_base_v050_signal,
    f30bds_f30_bank_distress_signature_roacollstd_21d_base_v051_signal,
    f30bds_f30_bank_distress_signature_roacollz_21d_base_v052_signal,
    f30bds_f30_bank_distress_signature_roacollabs_42d_base_v053_signal,
    f30bds_f30_bank_distress_signature_roacollsq_42d_base_v054_signal,
    f30bds_f30_bank_distress_signature_roacollsign_21d_base_v055_signal,
    f30bds_f30_bank_distress_signature_roacolllog_42d_base_v056_signal,
    f30bds_f30_bank_distress_signature_roacollrng_21d_base_v057_signal,
    f30bds_f30_bank_distress_signature_roacolldv_21d_base_v058_signal,
    f30bds_f30_bank_distress_signature_roacollpos_21d_base_v059_signal,
    f30bds_f30_bank_distress_signature_roacollneg_21d_base_v060_signal,
    f30bds_f30_bank_distress_signature_distscraw_42d_base_v061_signal,
    f30bds_f30_bank_distress_signature_distscsm_21d_base_v062_signal,
    f30bds_f30_bank_distress_signature_distscstd_21d_base_v063_signal,
    f30bds_f30_bank_distress_signature_distscz_21d_base_v064_signal,
    f30bds_f30_bank_distress_signature_distscabs_42d_base_v065_signal,
    f30bds_f30_bank_distress_signature_distscsq_42d_base_v066_signal,
    f30bds_f30_bank_distress_signature_distscsign_21d_base_v067_signal,
    f30bds_f30_bank_distress_signature_distsclog_42d_base_v068_signal,
    f30bds_f30_bank_distress_signature_distscrng_21d_base_v069_signal,
    f30bds_f30_bank_distress_signature_distscdv_21d_base_v070_signal,
    f30bds_f30_bank_distress_signature_distscpos_21d_base_v071_signal,
    f30bds_f30_bank_distress_signature_distscneg_21d_base_v072_signal,
    f30bds_f30_bank_distress_signature_distproxraw_63d_base_v073_signal,
    f30bds_f30_bank_distress_signature_distproxsm_21d_base_v074_signal,
    f30bds_f30_bank_distress_signature_distproxstd_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_BANK_DISTRESS_SIGNATURE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f30_bank_distress_signature_base_001_075_claude: {n_features} features pass")
