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
def _f02_revenue_smoothness(revenue, w):
    g = revenue.pct_change(periods=w)
    return -g.rolling(w, min_periods=max(1, w // 2)).std()


def _f02_recurring_signature(revenue, w):
    floor = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - floor) / revenue.replace(0, np.nan).abs() - 0.5


def _f02_replacement_score(revenue, grossmargin, w):
    g = revenue.pct_change(periods=w)
    return g * (grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean())


# v001: 21d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_21d_base_v001_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 63d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_63d_base_v002_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 126d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_126d_base_v003_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 252d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_252d_base_v004_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 21d revenue acceleration rolling mean over 63d * closeadj
def f02drc_f02_device_replacement_cycle_accelmean_21d_base_v005_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 63d revenue acceleration rolling mean over 126d * closeadj
def f02drc_f02_device_replacement_cycle_accelmean_63d_base_v006_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 21d revenue acceleration rolling std over 63d * closeadj
def f02drc_f02_device_replacement_cycle_accelstd_21d_base_v007_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 63d revenue acceleration rolling std over 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelstd_63d_base_v008_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: 21d revenue acceleration zscore over 252d
def f02drc_f02_device_replacement_cycle_accelz_21d_base_v009_signal(revenue):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: 63d revenue acceleration zscore over 504d
def f02drc_f02_device_replacement_cycle_accelz_63d_base_v010_signal(revenue):
    base = _f02_revenue_smoothness(revenue, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 21d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_21d_base_v011_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: 63d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_63d_base_v012_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 126d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_126d_base_v013_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 252d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_252d_base_v014_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 5d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_5d_base_v015_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 21d launch pulse rolling mean 63d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemean_21d_base_v016_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 63d launch pulse rolling mean 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemean_63d_base_v017_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 21d launch pulse std 126d * closeadj
def f02drc_f02_device_replacement_cycle_pulsestd_21d_base_v018_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 63d launch pulse std 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsestd_63d_base_v019_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 21d launch pulse zscore 252d
def f02drc_f02_device_replacement_cycle_pulsez_21d_base_v020_signal(revenue):
    base = _f02_recurring_signature(revenue, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: 63d launch pulse zscore 504d
def f02drc_f02_device_replacement_cycle_pulsez_63d_base_v021_signal(revenue):
    base = _f02_recurring_signature(revenue, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: 21d commercialization signature * closeadj
def f02drc_f02_device_replacement_cycle_sig_21d_base_v022_signal(revenue, grossmargin, closeadj):
    result = _f02_replacement_score(revenue, grossmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: 63d commercialization signature * closeadj
def f02drc_f02_device_replacement_cycle_sig_63d_base_v023_signal(revenue, grossmargin, closeadj):
    result = _f02_replacement_score(revenue, grossmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: 126d commercialization signature * closeadj
def f02drc_f02_device_replacement_cycle_sig_126d_base_v024_signal(revenue, grossmargin, closeadj):
    result = _f02_replacement_score(revenue, grossmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: 252d commercialization signature * closeadj
def f02drc_f02_device_replacement_cycle_sig_252d_base_v025_signal(revenue, grossmargin, closeadj):
    result = _f02_replacement_score(revenue, grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: 21d signature mean 63d * closeadj
def f02drc_f02_device_replacement_cycle_sigmean_21d_base_v026_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: 63d signature mean 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigmean_63d_base_v027_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: 21d signature std 126d * closeadj
def f02drc_f02_device_replacement_cycle_sigstd_21d_base_v028_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: 63d signature std 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigstd_63d_base_v029_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 21d signature zscore 252d
def f02drc_f02_device_replacement_cycle_sigz_21d_base_v030_signal(revenue, grossmargin):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 63d signature zscore 504d
def f02drc_f02_device_replacement_cycle_sigz_63d_base_v031_signal(revenue, grossmargin):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: 21d accel × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_accelxinstal_21d_base_v032_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: 63d accel × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_accelxinstal_63d_base_v033_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: 21d pulse × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_pulsexinstal_21d_base_v034_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 63d pulse × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_pulsexinstal_63d_base_v035_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 21d signature × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_sigxinstal_21d_base_v036_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = base * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: 63d signature × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_sigxinstal_63d_base_v037_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = base * (grossmargin * 100.0) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: 42d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_42d_base_v038_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: 189d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_189d_base_v039_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: 378d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_378d_base_v040_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: 504d revenue acceleration * closeadj
def f02drc_f02_device_replacement_cycle_accel_504d_base_v041_signal(revenue, closeadj):
    result = _f02_revenue_smoothness(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: 42d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_42d_base_v042_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: 189d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_189d_base_v043_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: 378d launch pulse * closeadj
def f02drc_f02_device_replacement_cycle_pulse_378d_base_v044_signal(revenue, closeadj):
    result = _f02_recurring_signature(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: 42d signature * closeadj
def f02drc_f02_device_replacement_cycle_sig_42d_base_v045_signal(revenue, grossmargin, closeadj):
    result = _f02_replacement_score(revenue, grossmargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: 189d signature * closeadj
def f02drc_f02_device_replacement_cycle_sig_189d_base_v046_signal(revenue, grossmargin, closeadj):
    result = _f02_replacement_score(revenue, grossmargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: 378d signature * closeadj
def f02drc_f02_device_replacement_cycle_sig_378d_base_v047_signal(revenue, grossmargin, closeadj):
    result = _f02_replacement_score(revenue, grossmargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: 21d accel × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_accelxgrossmargin_21d_base_v048_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: 63d accel × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_accelxgrossmargin_63d_base_v049_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: 21d pulse × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_pulsexgrossmargin_21d_base_v050_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: 63d pulse × grossmargin / closeadj
def f02drc_f02_device_replacement_cycle_pulsexgrossmargin_63d_base_v051_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base * grossmargin / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: 21d accel squared (signed) * closeadj
def f02drc_f02_device_replacement_cycle_accelsq_21d_base_v052_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: 63d accel squared (signed) * closeadj
def f02drc_f02_device_replacement_cycle_accelsq_63d_base_v053_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: 21d pulse squared * closeadj
def f02drc_f02_device_replacement_cycle_pulsesq_21d_base_v054_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: 63d pulse squared * closeadj
def f02drc_f02_device_replacement_cycle_pulsesq_63d_base_v055_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 21d signature squared * closeadj
def f02drc_f02_device_replacement_cycle_sigsq_21d_base_v056_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 63d signature squared * closeadj
def f02drc_f02_device_replacement_cycle_sigsq_63d_base_v057_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: 21d accel × revenue / closeadj (revenue absolute scaling)
def f02drc_f02_device_replacement_cycle_accelxrev_21d_base_v058_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base * revenue / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: 63d accel × revenue / closeadj
def f02drc_f02_device_replacement_cycle_accelxrev_63d_base_v059_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base * revenue / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: 21d pulse × revenue / closeadj
def f02drc_f02_device_replacement_cycle_pulsexrev_21d_base_v060_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base * revenue / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: 63d pulse × revenue / closeadj
def f02drc_f02_device_replacement_cycle_pulsexrev_63d_base_v061_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base * revenue / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: 21d signature × revenue / closeadj
def f02drc_f02_device_replacement_cycle_sigxrev_21d_base_v062_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = base * revenue / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: 63d signature × revenue / closeadj
def f02drc_f02_device_replacement_cycle_sigxrev_63d_base_v063_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 63)
    result = base * revenue / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: 252d accel mean 252d * closeadj
def f02drc_f02_device_replacement_cycle_accelmean_252d_base_v064_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: 126d pulse mean 252d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemean_126d_base_v065_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: 126d signature mean 252d * closeadj
def f02drc_f02_device_replacement_cycle_sigmean_126d_base_v066_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 126)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: 21d accel ÷ grossmargin (asset-light growth proxy) * closeadj^2
def f02drc_f02_device_replacement_cycle_accelovinst_21d_base_v067_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = base / grossmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: 63d accel ÷ grossmargin * closeadj^2
def f02drc_f02_device_replacement_cycle_accelovinst_63d_base_v068_signal(revenue, grossmargin, closeadj):
    base = _f02_revenue_smoothness(revenue, 63)
    result = base / grossmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: 21d pulse ÷ grossmargin * closeadj^2
def f02drc_f02_device_replacement_cycle_pulseovinst_21d_base_v069_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = base / grossmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 63d pulse ÷ grossmargin * closeadj^2
def f02drc_f02_device_replacement_cycle_pulseovinst_63d_base_v070_signal(revenue, grossmargin, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    result = base / grossmargin.replace(0, np.nan) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: 21d accel × sign(rev growth) × closeadj
def f02drc_f02_device_replacement_cycle_accelsign_21d_base_v071_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    sg = np.sign(revenue.pct_change(periods=21))
    result = base * sg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: 63d pulse × sign(rev growth) × closeadj
def f02drc_f02_device_replacement_cycle_pulsesign_63d_base_v072_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 63)
    sg = np.sign(revenue.pct_change(periods=63))
    result = base * sg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: 21d signature std 63d * closeadj
def f02drc_f02_device_replacement_cycle_sigstd_21dshort_base_v073_signal(revenue, grossmargin, closeadj):
    base = _f02_replacement_score(revenue, grossmargin, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: 21d launch pulse rolling mean 21d * closeadj
def f02drc_f02_device_replacement_cycle_pulsemean_21dshort_base_v074_signal(revenue, closeadj):
    base = _f02_recurring_signature(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: 21d revenue acceleration mean 21d * closeadj
def f02drc_f02_device_replacement_cycle_accelmean_21dshort_base_v075_signal(revenue, closeadj):
    base = _f02_revenue_smoothness(revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02drc_f02_device_replacement_cycle_accel_21d_base_v001_signal,
    f02drc_f02_device_replacement_cycle_accel_63d_base_v002_signal,
    f02drc_f02_device_replacement_cycle_accel_126d_base_v003_signal,
    f02drc_f02_device_replacement_cycle_accel_252d_base_v004_signal,
    f02drc_f02_device_replacement_cycle_accelmean_21d_base_v005_signal,
    f02drc_f02_device_replacement_cycle_accelmean_63d_base_v006_signal,
    f02drc_f02_device_replacement_cycle_accelstd_21d_base_v007_signal,
    f02drc_f02_device_replacement_cycle_accelstd_63d_base_v008_signal,
    f02drc_f02_device_replacement_cycle_accelz_21d_base_v009_signal,
    f02drc_f02_device_replacement_cycle_accelz_63d_base_v010_signal,
    f02drc_f02_device_replacement_cycle_pulse_21d_base_v011_signal,
    f02drc_f02_device_replacement_cycle_pulse_63d_base_v012_signal,
    f02drc_f02_device_replacement_cycle_pulse_126d_base_v013_signal,
    f02drc_f02_device_replacement_cycle_pulse_252d_base_v014_signal,
    f02drc_f02_device_replacement_cycle_pulse_5d_base_v015_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_21d_base_v016_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_63d_base_v017_signal,
    f02drc_f02_device_replacement_cycle_pulsestd_21d_base_v018_signal,
    f02drc_f02_device_replacement_cycle_pulsestd_63d_base_v019_signal,
    f02drc_f02_device_replacement_cycle_pulsez_21d_base_v020_signal,
    f02drc_f02_device_replacement_cycle_pulsez_63d_base_v021_signal,
    f02drc_f02_device_replacement_cycle_sig_21d_base_v022_signal,
    f02drc_f02_device_replacement_cycle_sig_63d_base_v023_signal,
    f02drc_f02_device_replacement_cycle_sig_126d_base_v024_signal,
    f02drc_f02_device_replacement_cycle_sig_252d_base_v025_signal,
    f02drc_f02_device_replacement_cycle_sigmean_21d_base_v026_signal,
    f02drc_f02_device_replacement_cycle_sigmean_63d_base_v027_signal,
    f02drc_f02_device_replacement_cycle_sigstd_21d_base_v028_signal,
    f02drc_f02_device_replacement_cycle_sigstd_63d_base_v029_signal,
    f02drc_f02_device_replacement_cycle_sigz_21d_base_v030_signal,
    f02drc_f02_device_replacement_cycle_sigz_63d_base_v031_signal,
    f02drc_f02_device_replacement_cycle_accelxinstal_21d_base_v032_signal,
    f02drc_f02_device_replacement_cycle_accelxinstal_63d_base_v033_signal,
    f02drc_f02_device_replacement_cycle_pulsexinstal_21d_base_v034_signal,
    f02drc_f02_device_replacement_cycle_pulsexinstal_63d_base_v035_signal,
    f02drc_f02_device_replacement_cycle_sigxinstal_21d_base_v036_signal,
    f02drc_f02_device_replacement_cycle_sigxinstal_63d_base_v037_signal,
    f02drc_f02_device_replacement_cycle_accel_42d_base_v038_signal,
    f02drc_f02_device_replacement_cycle_accel_189d_base_v039_signal,
    f02drc_f02_device_replacement_cycle_accel_378d_base_v040_signal,
    f02drc_f02_device_replacement_cycle_accel_504d_base_v041_signal,
    f02drc_f02_device_replacement_cycle_pulse_42d_base_v042_signal,
    f02drc_f02_device_replacement_cycle_pulse_189d_base_v043_signal,
    f02drc_f02_device_replacement_cycle_pulse_378d_base_v044_signal,
    f02drc_f02_device_replacement_cycle_sig_42d_base_v045_signal,
    f02drc_f02_device_replacement_cycle_sig_189d_base_v046_signal,
    f02drc_f02_device_replacement_cycle_sig_378d_base_v047_signal,
    f02drc_f02_device_replacement_cycle_accelxgrossmargin_21d_base_v048_signal,
    f02drc_f02_device_replacement_cycle_accelxgrossmargin_63d_base_v049_signal,
    f02drc_f02_device_replacement_cycle_pulsexgrossmargin_21d_base_v050_signal,
    f02drc_f02_device_replacement_cycle_pulsexgrossmargin_63d_base_v051_signal,
    f02drc_f02_device_replacement_cycle_accelsq_21d_base_v052_signal,
    f02drc_f02_device_replacement_cycle_accelsq_63d_base_v053_signal,
    f02drc_f02_device_replacement_cycle_pulsesq_21d_base_v054_signal,
    f02drc_f02_device_replacement_cycle_pulsesq_63d_base_v055_signal,
    f02drc_f02_device_replacement_cycle_sigsq_21d_base_v056_signal,
    f02drc_f02_device_replacement_cycle_sigsq_63d_base_v057_signal,
    f02drc_f02_device_replacement_cycle_accelxrev_21d_base_v058_signal,
    f02drc_f02_device_replacement_cycle_accelxrev_63d_base_v059_signal,
    f02drc_f02_device_replacement_cycle_pulsexrev_21d_base_v060_signal,
    f02drc_f02_device_replacement_cycle_pulsexrev_63d_base_v061_signal,
    f02drc_f02_device_replacement_cycle_sigxrev_21d_base_v062_signal,
    f02drc_f02_device_replacement_cycle_sigxrev_63d_base_v063_signal,
    f02drc_f02_device_replacement_cycle_accelmean_252d_base_v064_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_126d_base_v065_signal,
    f02drc_f02_device_replacement_cycle_sigmean_126d_base_v066_signal,
    f02drc_f02_device_replacement_cycle_accelovinst_21d_base_v067_signal,
    f02drc_f02_device_replacement_cycle_accelovinst_63d_base_v068_signal,
    f02drc_f02_device_replacement_cycle_pulseovinst_21d_base_v069_signal,
    f02drc_f02_device_replacement_cycle_pulseovinst_63d_base_v070_signal,
    f02drc_f02_device_replacement_cycle_accelsign_21d_base_v071_signal,
    f02drc_f02_device_replacement_cycle_pulsesign_63d_base_v072_signal,
    f02drc_f02_device_replacement_cycle_sigstd_21dshort_base_v073_signal,
    f02drc_f02_device_replacement_cycle_pulsemean_21dshort_base_v074_signal,
    f02drc_f02_device_replacement_cycle_accelmean_21dshort_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_DEVICE_REPLACEMENT_CYCLE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "grossmargin": grossmargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f02_revenue_smoothness", "_f02_recurring_signature", "_f02_replacement_score")
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
    print(f"OK f02_device_replacement_cycle_base_001_075_claude: {n_features} features pass")
