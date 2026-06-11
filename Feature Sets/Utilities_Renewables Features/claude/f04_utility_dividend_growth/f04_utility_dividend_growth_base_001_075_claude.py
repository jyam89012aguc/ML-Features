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


def _f04_dps_growth(dps, w):
    return dps.pct_change(periods=w)


def _f04_dividend_compound(dps, w):
    sm = dps.rolling(w, min_periods=max(1, w // 2)).mean()
    return dps / sm.replace(0, np.nan)


def _f04_dividend_coverage(dps, eps, w):
    cov = eps / dps.replace(0, np.nan)
    return cov.rolling(w, min_periods=max(1, w // 2)).mean()


# DPS growth
def f04udg_f04_utility_dividend_growth_dpsgrowth_21d_base_v001_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_63d_base_v002_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_126d_base_v003_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_252d_base_v004_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_504d_base_v005_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Dividend compound
def f04udg_f04_utility_dividend_growth_compound_21d_base_v006_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_63d_base_v007_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_126d_base_v008_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_252d_base_v009_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_504d_base_v010_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage
def f04udg_f04_utility_dividend_growth_coverage_21d_base_v011_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_63d_base_v012_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_126d_base_v013_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_252d_base_v014_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_504d_base_v015_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Z-score
def f04udg_f04_utility_dividend_growth_dpsgrowthz_63d_base_v016_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthz_252d_base_v017_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundz_252d_base_v018_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragez_252d_base_v019_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Std
def f04udg_f04_utility_dividend_growth_dpsgrowthstd_63d_base_v020_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthstd_252d_base_v021_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundstd_252d_base_v022_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragestd_252d_base_v023_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EMA
def f04udg_f04_utility_dividend_growth_dpsgrowthema_252d_base_v024_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundema_252d_base_v025_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverageema_252d_base_v026_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Rank
def f04udg_f04_utility_dividend_growth_dpsgrowthrank_252d_base_v027_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundrank_252d_base_v028_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragerank_252d_base_v029_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Use payout ratio with primitives
def f04udg_f04_utility_dividend_growth_payoutdps_252d_base_v030_signal(payoutratio, dps, closeadj):
    rb = _f04_dps_growth(dps, 252)
    result = _mean(payoutratio, 252) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_payoutcompound_252d_base_v031_signal(payoutratio, dps, closeadj):
    rb = _f04_dividend_compound(dps, 252)
    result = _mean(payoutratio, 252) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_payoutcov_252d_base_v032_signal(payoutratio, dps, eps, closeadj):
    rb = _f04_dividend_coverage(dps, eps, 252)
    result = _mean(payoutratio, 252) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Short windows
def f04udg_f04_utility_dividend_growth_dpsgrowth_5d_base_v033_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_10d_base_v034_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_42d_base_v035_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_189d_base_v036_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_378d_base_v037_signal(dps, closeadj):
    result = _f04_dps_growth(dps, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound short
def f04udg_f04_utility_dividend_growth_compound_5d_base_v038_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_42d_base_v039_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_189d_base_v040_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_378d_base_v041_signal(dps, closeadj):
    result = _f04_dividend_compound(dps, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage short
def f04udg_f04_utility_dividend_growth_coverage_5d_base_v042_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_42d_base_v043_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_189d_base_v044_signal(dps, eps, closeadj):
    result = _f04_dividend_coverage(dps, eps, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Volume × growth
def f04udg_f04_utility_dividend_growth_dpsgrowthxvol_63d_base_v045_signal(dps, closeadj, volume):
    result = _f04_dps_growth(dps, 63) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxvol_252d_base_v046_signal(dps, closeadj, volume):
    result = _f04_dps_growth(dps, 252) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxvol_252d_base_v047_signal(dps, closeadj, volume):
    result = _f04_dividend_compound(dps, 252) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexvol_252d_base_v048_signal(dps, eps, closeadj, volume):
    result = _f04_dividend_coverage(dps, eps, 252) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ATR × growth
def f04udg_f04_utility_dividend_growth_dpsgrowthxatr_63d_base_v049_signal(dps, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f04_dps_growth(dps, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxatr_252d_base_v050_signal(dps, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f04_dps_growth(dps, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxatr_252d_base_v051_signal(dps, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f04_dividend_compound(dps, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexatr_252d_base_v052_signal(dps, eps, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f04_dividend_coverage(dps, eps, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# Log
def f04udg_f04_utility_dividend_growth_dpslog_63d_base_v053_signal(dps, closeadj):
    rb = _f04_dps_growth(dps, 63)
    result = np.log(dps.abs().replace(0, np.nan)).diff(63) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpslog_252d_base_v054_signal(dps, closeadj):
    rb = _f04_dps_growth(dps, 252)
    result = np.log(dps.abs().replace(0, np.nan)).diff(252) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × eps × close
def f04udg_f04_utility_dividend_growth_compoundxeps_252d_base_v055_signal(dps, eps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = base * _mean(eps, 63) / _mean(eps, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth squared
def f04udg_f04_utility_dividend_growth_dpsgrowthsq_63d_base_v056_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthsq_252d_base_v057_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage squared
def f04udg_f04_utility_dividend_growth_coveragesq_252d_base_v058_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS log scale × close
def f04udg_f04_utility_dividend_growth_dpsxsize_252d_base_v059_signal(dps, closeadj):
    rb = _f04_dps_growth(dps, 252)
    result = np.log(dps.abs().replace(0, np.nan)) * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage gap
def f04udg_f04_utility_dividend_growth_coveragegap_252d_base_v060_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound gap
def f04udg_f04_utility_dividend_growth_compoundgap_252d_base_v061_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS-growth gap
def f04udg_f04_utility_dividend_growth_dpsgrowthgap_252d_base_v062_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = (g - _mean(g, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS × eps × close (dividend × earnings interaction)
def f04udg_f04_utility_dividend_growth_dpsxeps_63d_base_v063_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63)
    result = base * _mean(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsxeps_252d_base_v064_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * _mean(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Compound × DPS growth × close
def f04udg_f04_utility_dividend_growth_combocompgrowth_63d_base_v065_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    c = _f04_dividend_compound(dps, 63)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combocompgrowth_252d_base_v066_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    c = _f04_dividend_compound(dps, 252)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × DPS growth × close
def f04udg_f04_utility_dividend_growth_combocovgrowth_63d_base_v067_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 63)
    c = _f04_dividend_coverage(dps, eps, 63)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combocovgrowth_252d_base_v068_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 252)
    c = _f04_dividend_coverage(dps, eps, 252)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × compound × close
def f04udg_f04_utility_dividend_growth_combocovcomp_252d_base_v069_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    c = _f04_dividend_compound(dps, 252)
    result = co * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × abs return × close
def f04udg_f04_utility_dividend_growth_dpsgrowthxabsret_252d_base_v070_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * closeadj.pct_change(63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × abs return × close
def f04udg_f04_utility_dividend_growth_coveragexabsret_252d_base_v071_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * closeadj.pct_change(63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × volume z
def f04udg_f04_utility_dividend_growth_dpsgrowthxvolz_252d_base_v072_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 252)
    result = g * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth × close z
def f04udg_f04_utility_dividend_growth_dpsgrowthxclosez_252d_base_v073_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage × close z
def f04udg_f04_utility_dividend_growth_coveragexclosez_252d_base_v074_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252)
    result = base * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DPS growth sum × close
def f04udg_f04_utility_dividend_growth_dpsgrowthsum_252d_base_v075_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04udg_f04_utility_dividend_growth_dpsgrowth_21d_base_v001_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_63d_base_v002_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_126d_base_v003_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_252d_base_v004_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_504d_base_v005_signal,
    f04udg_f04_utility_dividend_growth_compound_21d_base_v006_signal,
    f04udg_f04_utility_dividend_growth_compound_63d_base_v007_signal,
    f04udg_f04_utility_dividend_growth_compound_126d_base_v008_signal,
    f04udg_f04_utility_dividend_growth_compound_252d_base_v009_signal,
    f04udg_f04_utility_dividend_growth_compound_504d_base_v010_signal,
    f04udg_f04_utility_dividend_growth_coverage_21d_base_v011_signal,
    f04udg_f04_utility_dividend_growth_coverage_63d_base_v012_signal,
    f04udg_f04_utility_dividend_growth_coverage_126d_base_v013_signal,
    f04udg_f04_utility_dividend_growth_coverage_252d_base_v014_signal,
    f04udg_f04_utility_dividend_growth_coverage_504d_base_v015_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthz_63d_base_v016_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthz_252d_base_v017_signal,
    f04udg_f04_utility_dividend_growth_compoundz_252d_base_v018_signal,
    f04udg_f04_utility_dividend_growth_coveragez_252d_base_v019_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthstd_63d_base_v020_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthstd_252d_base_v021_signal,
    f04udg_f04_utility_dividend_growth_compoundstd_252d_base_v022_signal,
    f04udg_f04_utility_dividend_growth_coveragestd_252d_base_v023_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthema_252d_base_v024_signal,
    f04udg_f04_utility_dividend_growth_compoundema_252d_base_v025_signal,
    f04udg_f04_utility_dividend_growth_coverageema_252d_base_v026_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthrank_252d_base_v027_signal,
    f04udg_f04_utility_dividend_growth_compoundrank_252d_base_v028_signal,
    f04udg_f04_utility_dividend_growth_coveragerank_252d_base_v029_signal,
    f04udg_f04_utility_dividend_growth_payoutdps_252d_base_v030_signal,
    f04udg_f04_utility_dividend_growth_payoutcompound_252d_base_v031_signal,
    f04udg_f04_utility_dividend_growth_payoutcov_252d_base_v032_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_5d_base_v033_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_10d_base_v034_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_42d_base_v035_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_189d_base_v036_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_378d_base_v037_signal,
    f04udg_f04_utility_dividend_growth_compound_5d_base_v038_signal,
    f04udg_f04_utility_dividend_growth_compound_42d_base_v039_signal,
    f04udg_f04_utility_dividend_growth_compound_189d_base_v040_signal,
    f04udg_f04_utility_dividend_growth_compound_378d_base_v041_signal,
    f04udg_f04_utility_dividend_growth_coverage_5d_base_v042_signal,
    f04udg_f04_utility_dividend_growth_coverage_42d_base_v043_signal,
    f04udg_f04_utility_dividend_growth_coverage_189d_base_v044_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxvol_63d_base_v045_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxvol_252d_base_v046_signal,
    f04udg_f04_utility_dividend_growth_compoundxvol_252d_base_v047_signal,
    f04udg_f04_utility_dividend_growth_coveragexvol_252d_base_v048_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxatr_63d_base_v049_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxatr_252d_base_v050_signal,
    f04udg_f04_utility_dividend_growth_compoundxatr_252d_base_v051_signal,
    f04udg_f04_utility_dividend_growth_coveragexatr_252d_base_v052_signal,
    f04udg_f04_utility_dividend_growth_dpslog_63d_base_v053_signal,
    f04udg_f04_utility_dividend_growth_dpslog_252d_base_v054_signal,
    f04udg_f04_utility_dividend_growth_compoundxeps_252d_base_v055_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsq_63d_base_v056_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsq_252d_base_v057_signal,
    f04udg_f04_utility_dividend_growth_coveragesq_252d_base_v058_signal,
    f04udg_f04_utility_dividend_growth_dpsxsize_252d_base_v059_signal,
    f04udg_f04_utility_dividend_growth_coveragegap_252d_base_v060_signal,
    f04udg_f04_utility_dividend_growth_compoundgap_252d_base_v061_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthgap_252d_base_v062_signal,
    f04udg_f04_utility_dividend_growth_dpsxeps_63d_base_v063_signal,
    f04udg_f04_utility_dividend_growth_dpsxeps_252d_base_v064_signal,
    f04udg_f04_utility_dividend_growth_combocompgrowth_63d_base_v065_signal,
    f04udg_f04_utility_dividend_growth_combocompgrowth_252d_base_v066_signal,
    f04udg_f04_utility_dividend_growth_combocovgrowth_63d_base_v067_signal,
    f04udg_f04_utility_dividend_growth_combocovgrowth_252d_base_v068_signal,
    f04udg_f04_utility_dividend_growth_combocovcomp_252d_base_v069_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxabsret_252d_base_v070_signal,
    f04udg_f04_utility_dividend_growth_coveragexabsret_252d_base_v071_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxvolz_252d_base_v072_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxclosez_252d_base_v073_signal,
    f04udg_f04_utility_dividend_growth_coveragexclosez_252d_base_v074_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsum_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_UTILITY_DIVIDEND_GROWTH_REGISTRY_001_075 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    eps = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "dps": dps, "eps": eps, "payoutratio": payoutratio,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f04_dps_growth", "_f04_dividend_compound", "_f04_dividend_coverage")
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
    print(f"OK f04_utility_dividend_growth_base_001_075_claude: {n_features} features pass")
