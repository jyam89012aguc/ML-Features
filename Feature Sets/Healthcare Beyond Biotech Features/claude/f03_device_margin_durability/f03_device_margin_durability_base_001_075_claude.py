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
def _f03_margin_floor(grossmargin, w):
    g = grossmargin.pct_change(periods=w)
    return g - g.shift(w)


def _f03_margin_durability(grossmargin, w):
    base = grossmargin.rolling(w * 4, min_periods=max(1, w)).mean()
    return (grossmargin - base) / base.replace(0, np.nan).abs()


def _f03_margin_consistency(grossmargin, ebitdamargin, w):
    gm_g = grossmargin.pct_change(periods=w)
    em_g = ebitdamargin.pct_change(periods=w)
    return gm_g - 0.5 * em_g


# v001: 21d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_21d_base_v001_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 63d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_63d_base_v002_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 126d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_126d_base_v003_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 252d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_252d_base_v004_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 21d grossmargin acceleration rolling mean over 63d * closeadj
def f03dmd_f03_device_margin_durability_accelmean_21d_base_v005_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 63d grossmargin acceleration rolling mean over 126d * closeadj
def f03dmd_f03_device_margin_durability_accelmean_63d_base_v006_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 21d grossmargin acceleration rolling std over 63d * closeadj
def f03dmd_f03_device_margin_durability_accelstd_21d_base_v007_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 63d grossmargin acceleration rolling std over 252d * closeadj
def f03dmd_f03_device_margin_durability_accelstd_63d_base_v008_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: 21d grossmargin acceleration zscore over 252d
def f03dmd_f03_device_margin_durability_accelz_21d_base_v009_signal(grossmargin):
    base = _f03_margin_floor(grossmargin, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: 63d grossmargin acceleration zscore over 504d
def f03dmd_f03_device_margin_durability_accelz_63d_base_v010_signal(grossmargin):
    base = _f03_margin_floor(grossmargin, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 21d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_21d_base_v011_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: 63d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_63d_base_v012_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 126d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_126d_base_v013_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 252d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_252d_base_v014_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 5d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_5d_base_v015_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 21d launch pulse rolling mean 63d * closeadj
def f03dmd_f03_device_margin_durability_pulsemean_21d_base_v016_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 63d launch pulse rolling mean 252d * closeadj
def f03dmd_f03_device_margin_durability_pulsemean_63d_base_v017_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 21d launch pulse std 126d * closeadj
def f03dmd_f03_device_margin_durability_pulsestd_21d_base_v018_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 63d launch pulse std 252d * closeadj
def f03dmd_f03_device_margin_durability_pulsestd_63d_base_v019_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 21d launch pulse zscore 252d
def f03dmd_f03_device_margin_durability_pulsez_21d_base_v020_signal(grossmargin):
    base = _f03_margin_durability(grossmargin, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: 63d launch pulse zscore 504d
def f03dmd_f03_device_margin_durability_pulsez_63d_base_v021_signal(grossmargin):
    base = _f03_margin_durability(grossmargin, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: 21d commercialization signature * closeadj
def f03dmd_f03_device_margin_durability_sig_21d_base_v022_signal(grossmargin, ebitdamargin, closeadj):
    result = _f03_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: 63d commercialization signature * closeadj
def f03dmd_f03_device_margin_durability_sig_63d_base_v023_signal(grossmargin, ebitdamargin, closeadj):
    result = _f03_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: 126d commercialization signature * closeadj
def f03dmd_f03_device_margin_durability_sig_126d_base_v024_signal(grossmargin, ebitdamargin, closeadj):
    result = _f03_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: 252d commercialization signature * closeadj
def f03dmd_f03_device_margin_durability_sig_252d_base_v025_signal(grossmargin, ebitdamargin, closeadj):
    result = _f03_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: 21d signature mean 63d * closeadj
def f03dmd_f03_device_margin_durability_sigmean_21d_base_v026_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: 63d signature mean 252d * closeadj
def f03dmd_f03_device_margin_durability_sigmean_63d_base_v027_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: 21d signature std 126d * closeadj
def f03dmd_f03_device_margin_durability_sigstd_21d_base_v028_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: 63d signature std 252d * closeadj
def f03dmd_f03_device_margin_durability_sigstd_63d_base_v029_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 21d signature zscore 252d
def f03dmd_f03_device_margin_durability_sigz_21d_base_v030_signal(grossmargin, ebitdamargin):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 63d signature zscore 504d
def f03dmd_f03_device_margin_durability_sigz_63d_base_v031_signal(grossmargin, ebitdamargin):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: 21d accel × netmargin / closeadj
def f03dmd_f03_device_margin_durability_accelxinstal_21d_base_v032_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = base * netmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: 63d accel × netmargin / closeadj
def f03dmd_f03_device_margin_durability_accelxinstal_63d_base_v033_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63)
    result = base * netmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: 21d pulse × netmargin / closeadj
def f03dmd_f03_device_margin_durability_pulsexinstal_21d_base_v034_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = base * netmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 63d pulse × netmargin / closeadj
def f03dmd_f03_device_margin_durability_pulsexinstal_63d_base_v035_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    result = base * netmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 21d signature × netmargin / closeadj
def f03dmd_f03_device_margin_durability_sigxinstal_21d_base_v036_signal(grossmargin, ebitdamargin, netmargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    result = base * netmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: 63d signature × netmargin / closeadj
def f03dmd_f03_device_margin_durability_sigxinstal_63d_base_v037_signal(grossmargin, ebitdamargin, netmargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63)
    result = base * netmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: 42d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_42d_base_v038_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: 189d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_189d_base_v039_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: 378d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_378d_base_v040_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: 504d grossmargin acceleration * closeadj
def f03dmd_f03_device_margin_durability_accel_504d_base_v041_signal(grossmargin, closeadj):
    result = _f03_margin_floor(grossmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: 42d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_42d_base_v042_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: 189d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_189d_base_v043_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: 378d launch pulse * closeadj
def f03dmd_f03_device_margin_durability_pulse_378d_base_v044_signal(grossmargin, closeadj):
    result = _f03_margin_durability(grossmargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: 42d signature * closeadj
def f03dmd_f03_device_margin_durability_sig_42d_base_v045_signal(grossmargin, ebitdamargin, closeadj):
    result = _f03_margin_consistency(grossmargin, ebitdamargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: 189d signature * closeadj
def f03dmd_f03_device_margin_durability_sig_189d_base_v046_signal(grossmargin, ebitdamargin, closeadj):
    result = _f03_margin_consistency(grossmargin, ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: 378d signature * closeadj
def f03dmd_f03_device_margin_durability_sig_378d_base_v047_signal(grossmargin, ebitdamargin, closeadj):
    result = _f03_margin_consistency(grossmargin, ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: 21d accel × ebitdamargin / closeadj
def f03dmd_f03_device_margin_durability_accelxebitdamargin_21d_base_v048_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = base * ebitdamargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: 63d accel × ebitdamargin / closeadj
def f03dmd_f03_device_margin_durability_accelxebitdamargin_63d_base_v049_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63)
    result = base * ebitdamargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: 21d pulse × ebitdamargin / closeadj
def f03dmd_f03_device_margin_durability_pulsexebitdamargin_21d_base_v050_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = base * ebitdamargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: 63d pulse × ebitdamargin / closeadj
def f03dmd_f03_device_margin_durability_pulsexebitdamargin_63d_base_v051_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    result = base * ebitdamargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: 21d accel squared (signed) * closeadj
def f03dmd_f03_device_margin_durability_accelsq_21d_base_v052_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: 63d accel squared (signed) * closeadj
def f03dmd_f03_device_margin_durability_accelsq_63d_base_v053_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: 21d pulse squared * closeadj
def f03dmd_f03_device_margin_durability_pulsesq_21d_base_v054_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: 63d pulse squared * closeadj
def f03dmd_f03_device_margin_durability_pulsesq_63d_base_v055_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 21d signature squared * closeadj
def f03dmd_f03_device_margin_durability_sigsq_21d_base_v056_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 63d signature squared * closeadj
def f03dmd_f03_device_margin_durability_sigsq_63d_base_v057_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: 21d accel × grossmargin / closeadj (grossmargin absolute scaling)
def f03dmd_f03_device_margin_durability_accelxrev_21d_base_v058_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: 63d accel × grossmargin / closeadj
def f03dmd_f03_device_margin_durability_accelxrev_63d_base_v059_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: 21d pulse × grossmargin / closeadj
def f03dmd_f03_device_margin_durability_pulsexrev_21d_base_v060_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: 63d pulse × grossmargin / closeadj
def f03dmd_f03_device_margin_durability_pulsexrev_63d_base_v061_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: 21d signature × grossmargin / closeadj
def f03dmd_f03_device_margin_durability_sigxrev_21d_base_v062_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: 63d signature × grossmargin / closeadj
def f03dmd_f03_device_margin_durability_sigxrev_63d_base_v063_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 63)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: 252d accel mean 252d * closeadj
def f03dmd_f03_device_margin_durability_accelmean_252d_base_v064_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: 126d pulse mean 252d * closeadj
def f03dmd_f03_device_margin_durability_pulsemean_126d_base_v065_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: 126d signature mean 252d * closeadj
def f03dmd_f03_device_margin_durability_sigmean_126d_base_v066_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: 21d accel ÷ netmargin (asset-light growth proxy) * closeadj^2
def f03dmd_f03_device_margin_durability_accelovinst_21d_base_v067_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = base / netmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: 63d accel ÷ netmargin * closeadj^2
def f03dmd_f03_device_margin_durability_accelovinst_63d_base_v068_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 63)
    result = base / netmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: 21d pulse ÷ netmargin * closeadj^2
def f03dmd_f03_device_margin_durability_pulseovinst_21d_base_v069_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = base / netmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 63d pulse ÷ netmargin * closeadj^2
def f03dmd_f03_device_margin_durability_pulseovinst_63d_base_v070_signal(grossmargin, netmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    result = base / netmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: 21d accel × sign(rev growth) × closeadj
def f03dmd_f03_device_margin_durability_accelsign_21d_base_v071_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    sg = np.sign(grossmargin.pct_change(periods=21))
    result = base * sg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: 63d pulse × sign(rev growth) × closeadj
def f03dmd_f03_device_margin_durability_pulsesign_63d_base_v072_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 63)
    sg = np.sign(grossmargin.pct_change(periods=63))
    result = base * sg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: 21d signature std 63d * closeadj
def f03dmd_f03_device_margin_durability_sigstd_21dshort_base_v073_signal(grossmargin, ebitdamargin, closeadj):
    base = _f03_margin_consistency(grossmargin, ebitdamargin, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: 21d launch pulse rolling mean 21d * closeadj
def f03dmd_f03_device_margin_durability_pulsemean_21dshort_base_v074_signal(grossmargin, closeadj):
    base = _f03_margin_durability(grossmargin, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: 21d grossmargin acceleration mean 21d * closeadj
def f03dmd_f03_device_margin_durability_accelmean_21dshort_base_v075_signal(grossmargin, closeadj):
    base = _f03_margin_floor(grossmargin, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03dmd_f03_device_margin_durability_accel_21d_base_v001_signal,
    f03dmd_f03_device_margin_durability_accel_63d_base_v002_signal,
    f03dmd_f03_device_margin_durability_accel_126d_base_v003_signal,
    f03dmd_f03_device_margin_durability_accel_252d_base_v004_signal,
    f03dmd_f03_device_margin_durability_accelmean_21d_base_v005_signal,
    f03dmd_f03_device_margin_durability_accelmean_63d_base_v006_signal,
    f03dmd_f03_device_margin_durability_accelstd_21d_base_v007_signal,
    f03dmd_f03_device_margin_durability_accelstd_63d_base_v008_signal,
    f03dmd_f03_device_margin_durability_accelz_21d_base_v009_signal,
    f03dmd_f03_device_margin_durability_accelz_63d_base_v010_signal,
    f03dmd_f03_device_margin_durability_pulse_21d_base_v011_signal,
    f03dmd_f03_device_margin_durability_pulse_63d_base_v012_signal,
    f03dmd_f03_device_margin_durability_pulse_126d_base_v013_signal,
    f03dmd_f03_device_margin_durability_pulse_252d_base_v014_signal,
    f03dmd_f03_device_margin_durability_pulse_5d_base_v015_signal,
    f03dmd_f03_device_margin_durability_pulsemean_21d_base_v016_signal,
    f03dmd_f03_device_margin_durability_pulsemean_63d_base_v017_signal,
    f03dmd_f03_device_margin_durability_pulsestd_21d_base_v018_signal,
    f03dmd_f03_device_margin_durability_pulsestd_63d_base_v019_signal,
    f03dmd_f03_device_margin_durability_pulsez_21d_base_v020_signal,
    f03dmd_f03_device_margin_durability_pulsez_63d_base_v021_signal,
    f03dmd_f03_device_margin_durability_sig_21d_base_v022_signal,
    f03dmd_f03_device_margin_durability_sig_63d_base_v023_signal,
    f03dmd_f03_device_margin_durability_sig_126d_base_v024_signal,
    f03dmd_f03_device_margin_durability_sig_252d_base_v025_signal,
    f03dmd_f03_device_margin_durability_sigmean_21d_base_v026_signal,
    f03dmd_f03_device_margin_durability_sigmean_63d_base_v027_signal,
    f03dmd_f03_device_margin_durability_sigstd_21d_base_v028_signal,
    f03dmd_f03_device_margin_durability_sigstd_63d_base_v029_signal,
    f03dmd_f03_device_margin_durability_sigz_21d_base_v030_signal,
    f03dmd_f03_device_margin_durability_sigz_63d_base_v031_signal,
    f03dmd_f03_device_margin_durability_accelxinstal_21d_base_v032_signal,
    f03dmd_f03_device_margin_durability_accelxinstal_63d_base_v033_signal,
    f03dmd_f03_device_margin_durability_pulsexinstal_21d_base_v034_signal,
    f03dmd_f03_device_margin_durability_pulsexinstal_63d_base_v035_signal,
    f03dmd_f03_device_margin_durability_sigxinstal_21d_base_v036_signal,
    f03dmd_f03_device_margin_durability_sigxinstal_63d_base_v037_signal,
    f03dmd_f03_device_margin_durability_accel_42d_base_v038_signal,
    f03dmd_f03_device_margin_durability_accel_189d_base_v039_signal,
    f03dmd_f03_device_margin_durability_accel_378d_base_v040_signal,
    f03dmd_f03_device_margin_durability_accel_504d_base_v041_signal,
    f03dmd_f03_device_margin_durability_pulse_42d_base_v042_signal,
    f03dmd_f03_device_margin_durability_pulse_189d_base_v043_signal,
    f03dmd_f03_device_margin_durability_pulse_378d_base_v044_signal,
    f03dmd_f03_device_margin_durability_sig_42d_base_v045_signal,
    f03dmd_f03_device_margin_durability_sig_189d_base_v046_signal,
    f03dmd_f03_device_margin_durability_sig_378d_base_v047_signal,
    f03dmd_f03_device_margin_durability_accelxebitdamargin_21d_base_v048_signal,
    f03dmd_f03_device_margin_durability_accelxebitdamargin_63d_base_v049_signal,
    f03dmd_f03_device_margin_durability_pulsexebitdamargin_21d_base_v050_signal,
    f03dmd_f03_device_margin_durability_pulsexebitdamargin_63d_base_v051_signal,
    f03dmd_f03_device_margin_durability_accelsq_21d_base_v052_signal,
    f03dmd_f03_device_margin_durability_accelsq_63d_base_v053_signal,
    f03dmd_f03_device_margin_durability_pulsesq_21d_base_v054_signal,
    f03dmd_f03_device_margin_durability_pulsesq_63d_base_v055_signal,
    f03dmd_f03_device_margin_durability_sigsq_21d_base_v056_signal,
    f03dmd_f03_device_margin_durability_sigsq_63d_base_v057_signal,
    f03dmd_f03_device_margin_durability_accelxrev_21d_base_v058_signal,
    f03dmd_f03_device_margin_durability_accelxrev_63d_base_v059_signal,
    f03dmd_f03_device_margin_durability_pulsexrev_21d_base_v060_signal,
    f03dmd_f03_device_margin_durability_pulsexrev_63d_base_v061_signal,
    f03dmd_f03_device_margin_durability_sigxrev_21d_base_v062_signal,
    f03dmd_f03_device_margin_durability_sigxrev_63d_base_v063_signal,
    f03dmd_f03_device_margin_durability_accelmean_252d_base_v064_signal,
    f03dmd_f03_device_margin_durability_pulsemean_126d_base_v065_signal,
    f03dmd_f03_device_margin_durability_sigmean_126d_base_v066_signal,
    f03dmd_f03_device_margin_durability_accelovinst_21d_base_v067_signal,
    f03dmd_f03_device_margin_durability_accelovinst_63d_base_v068_signal,
    f03dmd_f03_device_margin_durability_pulseovinst_21d_base_v069_signal,
    f03dmd_f03_device_margin_durability_pulseovinst_63d_base_v070_signal,
    f03dmd_f03_device_margin_durability_accelsign_21d_base_v071_signal,
    f03dmd_f03_device_margin_durability_pulsesign_63d_base_v072_signal,
    f03dmd_f03_device_margin_durability_sigstd_21dshort_base_v073_signal,
    f03dmd_f03_device_margin_durability_pulsemean_21dshort_base_v074_signal,
    f03dmd_f03_device_margin_durability_accelmean_21dshort_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_DEVICE_MARGIN_DURABILITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {"closeadj": closeadj, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f03_margin_floor", "_f03_margin_durability", "_f03_margin_consistency")
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
    print(f"OK f03_device_margin_durability_base_001_075_claude: {n_features} features pass")
