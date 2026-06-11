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
def _f04_rd_efficiency(rnd, revenue, w):
    rev_g = revenue.pct_change(periods=w)
    rd_g = rnd.pct_change(periods=w)
    return rev_g - rd_g


def _f04_rd_intensity(rnd, revenue, w):
    ratio = rnd / revenue.replace(0, np.nan).abs()
    base = ratio.rolling(w * 4, min_periods=max(1, w)).mean()
    return (ratio - base) / base.replace(0, np.nan).abs()


def _f04_rd_productivity(rnd, revenue, w):
    rev_g = revenue.pct_change(periods=w)
    rd_g = rnd.pct_change(periods=w)
    return rev_g - 0.5 * rd_g


# v001: 21d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_21d_base_v001_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 63d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_63d_base_v002_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 126d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_126d_base_v003_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 252d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_252d_base_v004_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 21d rnd acceleration rolling mean over 63d * closeadj
def f04dre_f04_device_rd_efficiency_accelmean_21d_base_v005_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 63d rnd acceleration rolling mean over 126d * closeadj
def f04dre_f04_device_rd_efficiency_accelmean_63d_base_v006_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 21d rnd acceleration rolling std over 63d * closeadj
def f04dre_f04_device_rd_efficiency_accelstd_21d_base_v007_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 63d rnd acceleration rolling std over 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelstd_63d_base_v008_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: 21d rnd acceleration zscore over 252d
def f04dre_f04_device_rd_efficiency_accelz_21d_base_v009_signal(rnd, revenue):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: 63d rnd acceleration zscore over 504d
def f04dre_f04_device_rd_efficiency_accelz_63d_base_v010_signal(rnd, revenue):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 21d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_21d_base_v011_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: 63d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_63d_base_v012_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 126d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_126d_base_v013_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 252d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_252d_base_v014_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 5d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_5d_base_v015_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 21d launch pulse rolling mean 63d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemean_21d_base_v016_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 63d launch pulse rolling mean 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemean_63d_base_v017_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 21d launch pulse std 126d * closeadj
def f04dre_f04_device_rd_efficiency_pulsestd_21d_base_v018_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 63d launch pulse std 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsestd_63d_base_v019_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 21d launch pulse zscore 252d
def f04dre_f04_device_rd_efficiency_pulsez_21d_base_v020_signal(rnd, revenue):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: 63d launch pulse zscore 504d
def f04dre_f04_device_rd_efficiency_pulsez_63d_base_v021_signal(rnd, revenue):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: 21d commercialization signature * closeadj
def f04dre_f04_device_rd_efficiency_sig_21d_base_v022_signal(rnd, closeadj):
    result = _f04_rd_productivity(rnd, rnd, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: 63d commercialization signature * closeadj
def f04dre_f04_device_rd_efficiency_sig_63d_base_v023_signal(rnd, closeadj):
    result = _f04_rd_productivity(rnd, rnd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: 126d commercialization signature * closeadj
def f04dre_f04_device_rd_efficiency_sig_126d_base_v024_signal(rnd, closeadj):
    result = _f04_rd_productivity(rnd, rnd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: 252d commercialization signature * closeadj
def f04dre_f04_device_rd_efficiency_sig_252d_base_v025_signal(rnd, closeadj):
    result = _f04_rd_productivity(rnd, rnd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: 21d signature mean 63d * closeadj
def f04dre_f04_device_rd_efficiency_sigmean_21d_base_v026_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: 63d signature mean 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigmean_63d_base_v027_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: 21d signature std 126d * closeadj
def f04dre_f04_device_rd_efficiency_sigstd_21d_base_v028_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: 63d signature std 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigstd_63d_base_v029_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 21d signature zscore 252d
def f04dre_f04_device_rd_efficiency_sigz_21d_base_v030_signal(rnd):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 63d signature zscore 504d
def f04dre_f04_device_rd_efficiency_sigz_63d_base_v031_signal(rnd):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: 21d accel × rnd / closeadj
def f04dre_f04_device_rd_efficiency_accelxinstal_21d_base_v032_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base * (rnd * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: 63d accel × rnd / closeadj
def f04dre_f04_device_rd_efficiency_accelxinstal_63d_base_v033_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base * (rnd * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: 21d pulse × rnd / closeadj
def f04dre_f04_device_rd_efficiency_pulsexinstal_21d_base_v034_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base * (rnd * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 63d pulse × rnd / closeadj
def f04dre_f04_device_rd_efficiency_pulsexinstal_63d_base_v035_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base * (rnd * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 21d signature × rnd / closeadj
def f04dre_f04_device_rd_efficiency_sigxinstal_21d_base_v036_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = base * (rnd * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: 63d signature × rnd / closeadj
def f04dre_f04_device_rd_efficiency_sigxinstal_63d_base_v037_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = base * (rnd * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: 42d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_42d_base_v038_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: 189d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_189d_base_v039_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: 378d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_378d_base_v040_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: 504d rnd acceleration * closeadj
def f04dre_f04_device_rd_efficiency_accel_504d_base_v041_signal(rnd, revenue, closeadj):
    result = _f04_rd_efficiency(rnd, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: 42d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_42d_base_v042_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: 189d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_189d_base_v043_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: 378d launch pulse * closeadj
def f04dre_f04_device_rd_efficiency_pulse_378d_base_v044_signal(rnd, revenue, closeadj):
    result = _f04_rd_intensity(rnd, revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: 42d signature * closeadj
def f04dre_f04_device_rd_efficiency_sig_42d_base_v045_signal(rnd, closeadj):
    result = _f04_rd_productivity(rnd, rnd, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: 189d signature * closeadj
def f04dre_f04_device_rd_efficiency_sig_189d_base_v046_signal(rnd, closeadj):
    result = _f04_rd_productivity(rnd, rnd, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: 378d signature * closeadj
def f04dre_f04_device_rd_efficiency_sig_378d_base_v047_signal(rnd, closeadj):
    result = _f04_rd_productivity(rnd, rnd, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: 21d accel × rnd / closeadj
def f04dre_f04_device_rd_efficiency_accelxrnd_21d_base_v048_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base * rnd / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: 63d accel × rnd / closeadj
def f04dre_f04_device_rd_efficiency_accelxrnd_63d_base_v049_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base * rnd / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: 21d pulse × rnd / closeadj
def f04dre_f04_device_rd_efficiency_pulsexrnd_21d_base_v050_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base * rnd / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: 63d pulse × rnd / closeadj
def f04dre_f04_device_rd_efficiency_pulsexrnd_63d_base_v051_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base * rnd / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: 21d accel squared (signed) * closeadj
def f04dre_f04_device_rd_efficiency_accelsq_21d_base_v052_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: 63d accel squared (signed) * closeadj
def f04dre_f04_device_rd_efficiency_accelsq_63d_base_v053_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: 21d pulse squared * closeadj
def f04dre_f04_device_rd_efficiency_pulsesq_21d_base_v054_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: 63d pulse squared * closeadj
def f04dre_f04_device_rd_efficiency_pulsesq_63d_base_v055_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 21d signature squared * closeadj
def f04dre_f04_device_rd_efficiency_sigsq_21d_base_v056_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 63d signature squared * closeadj
def f04dre_f04_device_rd_efficiency_sigsq_63d_base_v057_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: 21d accel × rnd / closeadj (rnd absolute scaling)
def f04dre_f04_device_rd_efficiency_accelxrev_21d_base_v058_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base * (rnd * 10.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: 63d accel × rnd / closeadj
def f04dre_f04_device_rd_efficiency_accelxrev_63d_base_v059_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base * (rnd * 10.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: 21d pulse × rnd / closeadj
def f04dre_f04_device_rd_efficiency_pulsexrev_21d_base_v060_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base * (rnd * 10.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: 63d pulse × rnd / closeadj
def f04dre_f04_device_rd_efficiency_pulsexrev_63d_base_v061_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base * (rnd * 10.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: 21d signature × rnd / closeadj
def f04dre_f04_device_rd_efficiency_sigxrev_21d_base_v062_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = base * (rnd * 10.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: 63d signature × rnd / closeadj
def f04dre_f04_device_rd_efficiency_sigxrev_63d_base_v063_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 63)
    result = base * (rnd * 10.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: 252d accel mean 252d * closeadj
def f04dre_f04_device_rd_efficiency_accelmean_252d_base_v064_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: 126d pulse mean 252d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemean_126d_base_v065_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: 126d signature mean 252d * closeadj
def f04dre_f04_device_rd_efficiency_sigmean_126d_base_v066_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: 21d accel ÷ rnd (asset-light growth proxy) * closeadj^2
def f04dre_f04_device_rd_efficiency_accelovinst_21d_base_v067_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = base / rnd.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: 63d accel ÷ rnd * closeadj^2
def f04dre_f04_device_rd_efficiency_accelovinst_63d_base_v068_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 63)
    result = base / rnd.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: 21d pulse ÷ rnd * closeadj^2
def f04dre_f04_device_rd_efficiency_pulseovinst_21d_base_v069_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = base / rnd.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 63d pulse ÷ rnd * closeadj^2
def f04dre_f04_device_rd_efficiency_pulseovinst_63d_base_v070_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    result = base / rnd.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: 21d accel × sign(rev growth) × closeadj
def f04dre_f04_device_rd_efficiency_accelsign_21d_base_v071_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    sg = np.sign(rnd.pct_change(periods=21))
    result = base * sg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: 63d pulse × sign(rev growth) × closeadj
def f04dre_f04_device_rd_efficiency_pulsesign_63d_base_v072_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 63)
    sg = np.sign(rnd.pct_change(periods=63))
    result = base * sg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: 21d signature std 63d * closeadj
def f04dre_f04_device_rd_efficiency_sigstd_21dshort_base_v073_signal(rnd, closeadj):
    base = _f04_rd_productivity(rnd, rnd, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: 21d launch pulse rolling mean 21d * closeadj
def f04dre_f04_device_rd_efficiency_pulsemean_21dshort_base_v074_signal(rnd, revenue, closeadj):
    base = _f04_rd_intensity(rnd, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: 21d rnd acceleration mean 21d * closeadj
def f04dre_f04_device_rd_efficiency_accelmean_21dshort_base_v075_signal(rnd, revenue, closeadj):
    base = _f04_rd_efficiency(rnd, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dre_f04_device_rd_efficiency_accel_21d_base_v001_signal,
    f04dre_f04_device_rd_efficiency_accel_63d_base_v002_signal,
    f04dre_f04_device_rd_efficiency_accel_126d_base_v003_signal,
    f04dre_f04_device_rd_efficiency_accel_252d_base_v004_signal,
    f04dre_f04_device_rd_efficiency_accelmean_21d_base_v005_signal,
    f04dre_f04_device_rd_efficiency_accelmean_63d_base_v006_signal,
    f04dre_f04_device_rd_efficiency_accelstd_21d_base_v007_signal,
    f04dre_f04_device_rd_efficiency_accelstd_63d_base_v008_signal,
    f04dre_f04_device_rd_efficiency_accelz_21d_base_v009_signal,
    f04dre_f04_device_rd_efficiency_accelz_63d_base_v010_signal,
    f04dre_f04_device_rd_efficiency_pulse_21d_base_v011_signal,
    f04dre_f04_device_rd_efficiency_pulse_63d_base_v012_signal,
    f04dre_f04_device_rd_efficiency_pulse_126d_base_v013_signal,
    f04dre_f04_device_rd_efficiency_pulse_252d_base_v014_signal,
    f04dre_f04_device_rd_efficiency_pulse_5d_base_v015_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_21d_base_v016_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_63d_base_v017_signal,
    f04dre_f04_device_rd_efficiency_pulsestd_21d_base_v018_signal,
    f04dre_f04_device_rd_efficiency_pulsestd_63d_base_v019_signal,
    f04dre_f04_device_rd_efficiency_pulsez_21d_base_v020_signal,
    f04dre_f04_device_rd_efficiency_pulsez_63d_base_v021_signal,
    f04dre_f04_device_rd_efficiency_sig_21d_base_v022_signal,
    f04dre_f04_device_rd_efficiency_sig_63d_base_v023_signal,
    f04dre_f04_device_rd_efficiency_sig_126d_base_v024_signal,
    f04dre_f04_device_rd_efficiency_sig_252d_base_v025_signal,
    f04dre_f04_device_rd_efficiency_sigmean_21d_base_v026_signal,
    f04dre_f04_device_rd_efficiency_sigmean_63d_base_v027_signal,
    f04dre_f04_device_rd_efficiency_sigstd_21d_base_v028_signal,
    f04dre_f04_device_rd_efficiency_sigstd_63d_base_v029_signal,
    f04dre_f04_device_rd_efficiency_sigz_21d_base_v030_signal,
    f04dre_f04_device_rd_efficiency_sigz_63d_base_v031_signal,
    f04dre_f04_device_rd_efficiency_accelxinstal_21d_base_v032_signal,
    f04dre_f04_device_rd_efficiency_accelxinstal_63d_base_v033_signal,
    f04dre_f04_device_rd_efficiency_pulsexinstal_21d_base_v034_signal,
    f04dre_f04_device_rd_efficiency_pulsexinstal_63d_base_v035_signal,
    f04dre_f04_device_rd_efficiency_sigxinstal_21d_base_v036_signal,
    f04dre_f04_device_rd_efficiency_sigxinstal_63d_base_v037_signal,
    f04dre_f04_device_rd_efficiency_accel_42d_base_v038_signal,
    f04dre_f04_device_rd_efficiency_accel_189d_base_v039_signal,
    f04dre_f04_device_rd_efficiency_accel_378d_base_v040_signal,
    f04dre_f04_device_rd_efficiency_accel_504d_base_v041_signal,
    f04dre_f04_device_rd_efficiency_pulse_42d_base_v042_signal,
    f04dre_f04_device_rd_efficiency_pulse_189d_base_v043_signal,
    f04dre_f04_device_rd_efficiency_pulse_378d_base_v044_signal,
    f04dre_f04_device_rd_efficiency_sig_42d_base_v045_signal,
    f04dre_f04_device_rd_efficiency_sig_189d_base_v046_signal,
    f04dre_f04_device_rd_efficiency_sig_378d_base_v047_signal,
    f04dre_f04_device_rd_efficiency_accelxrnd_21d_base_v048_signal,
    f04dre_f04_device_rd_efficiency_accelxrnd_63d_base_v049_signal,
    f04dre_f04_device_rd_efficiency_pulsexrnd_21d_base_v050_signal,
    f04dre_f04_device_rd_efficiency_pulsexrnd_63d_base_v051_signal,
    f04dre_f04_device_rd_efficiency_accelsq_21d_base_v052_signal,
    f04dre_f04_device_rd_efficiency_accelsq_63d_base_v053_signal,
    f04dre_f04_device_rd_efficiency_pulsesq_21d_base_v054_signal,
    f04dre_f04_device_rd_efficiency_pulsesq_63d_base_v055_signal,
    f04dre_f04_device_rd_efficiency_sigsq_21d_base_v056_signal,
    f04dre_f04_device_rd_efficiency_sigsq_63d_base_v057_signal,
    f04dre_f04_device_rd_efficiency_accelxrev_21d_base_v058_signal,
    f04dre_f04_device_rd_efficiency_accelxrev_63d_base_v059_signal,
    f04dre_f04_device_rd_efficiency_pulsexrev_21d_base_v060_signal,
    f04dre_f04_device_rd_efficiency_pulsexrev_63d_base_v061_signal,
    f04dre_f04_device_rd_efficiency_sigxrev_21d_base_v062_signal,
    f04dre_f04_device_rd_efficiency_sigxrev_63d_base_v063_signal,
    f04dre_f04_device_rd_efficiency_accelmean_252d_base_v064_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_126d_base_v065_signal,
    f04dre_f04_device_rd_efficiency_sigmean_126d_base_v066_signal,
    f04dre_f04_device_rd_efficiency_accelovinst_21d_base_v067_signal,
    f04dre_f04_device_rd_efficiency_accelovinst_63d_base_v068_signal,
    f04dre_f04_device_rd_efficiency_pulseovinst_21d_base_v069_signal,
    f04dre_f04_device_rd_efficiency_pulseovinst_63d_base_v070_signal,
    f04dre_f04_device_rd_efficiency_accelsign_21d_base_v071_signal,
    f04dre_f04_device_rd_efficiency_pulsesign_63d_base_v072_signal,
    f04dre_f04_device_rd_efficiency_sigstd_21dshort_base_v073_signal,
    f04dre_f04_device_rd_efficiency_pulsemean_21dshort_base_v074_signal,
    f04dre_f04_device_rd_efficiency_accelmean_21dshort_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DEVICE_RD_EFFICIENCY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    rnd = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "rnd": rnd, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f04_rd_efficiency", "_f04_rd_intensity", "_f04_rd_productivity")
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
    print(f"OK f04_device_rd_efficiency_base_001_075_claude: {n_features} features pass")
