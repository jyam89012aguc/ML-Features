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


def _f04_dps_growth(dps, w):
    return dps.pct_change(periods=w)


def _f04_dividend_compound(dps, w):
    sm = dps.rolling(w, min_periods=max(1, w // 2)).mean()
    return dps / sm.replace(0, np.nan)


def _f04_dividend_coverage(dps, eps, w):
    cov = eps / dps.replace(0, np.nan)
    return cov.rolling(w, min_periods=max(1, w // 2)).mean()


# DPS growth slope variants
def f04udg_f04_utility_dividend_growth_dpsgrowth_21d_jerk_v001_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_21d_jerk_v002_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_63d_jerk_v003_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_63d_jerk_v004_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_63d_jerk_v005_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_252d_jerk_v006_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_252d_jerk_v007_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_252d_jerk_v008_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_504d_jerk_v009_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowth_504d_jerk_v010_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Compound slopes
def f04udg_f04_utility_dividend_growth_compound_21d_jerk_v011_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_21d_jerk_v012_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_63d_jerk_v013_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_63d_jerk_v014_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_252d_jerk_v015_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_252d_jerk_v016_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_252d_jerk_v017_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_504d_jerk_v018_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_504d_jerk_v019_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage slopes
def f04udg_f04_utility_dividend_growth_coverage_21d_jerk_v020_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_21d_jerk_v021_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_63d_jerk_v022_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_63d_jerk_v023_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_252d_jerk_v024_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_252d_jerk_v025_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_252d_jerk_v026_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_504d_jerk_v027_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_504d_jerk_v028_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Volume variants
def f04udg_f04_utility_dividend_growth_dpsgrowthxvol_63d_jerk_v029_signal(dps, closeadj, volume):
    base = _f04_dps_growth(dps, 63) * _mean(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxvol_252d_jerk_v030_signal(dps, closeadj, volume):
    base = _f04_dps_growth(dps, 252) * _mean(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxvol_63d_jerk_v031_signal(dps, closeadj, volume):
    base = _f04_dividend_compound(dps, 63) * _mean(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxvol_252d_jerk_v032_signal(dps, closeadj, volume):
    base = _f04_dividend_compound(dps, 252) * _mean(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexvol_63d_jerk_v033_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 63) * _mean(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexvol_252d_jerk_v034_signal(dps, eps, closeadj, volume):
    base = _f04_dividend_coverage(dps, eps, 252) * _mean(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR
def f04udg_f04_utility_dividend_growth_dpsgrowthxatr_63d_jerk_v035_signal(dps, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f04_dps_growth(dps, 63) * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxatr_252d_jerk_v036_signal(dps, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f04_dps_growth(dps, 252) * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxatr_63d_jerk_v037_signal(dps, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f04_dividend_compound(dps, 63) * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxatr_252d_jerk_v038_signal(dps, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f04_dividend_compound(dps, 252) * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexatr_63d_jerk_v039_signal(dps, eps, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f04_dividend_coverage(dps, eps, 63) * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexatr_252d_jerk_v040_signal(dps, eps, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f04_dividend_coverage(dps, eps, 252) * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA
def f04udg_f04_utility_dividend_growth_dpsgrowthema_63d_jerk_v041_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63).ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthema_252d_jerk_v042_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252).ewm(span=63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundema_63d_jerk_v043_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63).ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundema_252d_jerk_v044_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252).ewm(span=63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverageema_63d_jerk_v045_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63).ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverageema_252d_jerk_v046_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252).ewm(span=63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Squared
def f04udg_f04_utility_dividend_growth_dpsgrowthsq_63d_jerk_v047_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = g * g.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthsq_252d_jerk_v048_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundsq_63d_jerk_v049_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 63)
    base = c * c.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundsq_252d_jerk_v050_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    base = c * c.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragesq_63d_jerk_v051_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = co * co.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragesq_252d_jerk_v052_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = co * co.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Z-score
def f04udg_f04_utility_dividend_growth_dpsgrowthz_63d_jerk_v053_signal(dps, closeadj):
    base = _z(_f04_dps_growth(dps, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthz_252d_jerk_v054_signal(dps, closeadj):
    base = _z(_f04_dps_growth(dps, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundz_63d_jerk_v055_signal(dps, closeadj):
    base = _z(_f04_dividend_compound(dps, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundz_252d_jerk_v056_signal(dps, closeadj):
    base = _z(_f04_dividend_compound(dps, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragez_63d_jerk_v057_signal(dps, eps, closeadj):
    base = _z(_f04_dividend_coverage(dps, eps, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragez_252d_jerk_v058_signal(dps, eps, closeadj):
    base = _z(_f04_dividend_coverage(dps, eps, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Rank
def f04udg_f04_utility_dividend_growth_dpsgrowthrank_63d_jerk_v059_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthrank_252d_jerk_v060_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundrank_63d_jerk_v061_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundrank_252d_jerk_v062_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragerank_63d_jerk_v063_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragerank_252d_jerk_v064_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Gap
def f04udg_f04_utility_dividend_growth_dpsgrowthgap_63d_jerk_v065_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = (g - _mean(g, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthgap_252d_jerk_v066_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = (g - _mean(g, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundgap_63d_jerk_v067_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 63)
    base = (c - _mean(c, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundgap_252d_jerk_v068_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    base = (c - _mean(c, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragegap_63d_jerk_v069_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = (co - _mean(co, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragegap_252d_jerk_v070_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = (co - _mean(co, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo
def f04udg_f04_utility_dividend_growth_combocompgrowth_63d_jerk_v071_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    c = _f04_dividend_compound(dps, 63)
    base = g * c * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combocompgrowth_252d_jerk_v072_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    c = _f04_dividend_compound(dps, 252)
    base = g * c * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combocovgrowth_63d_jerk_v073_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 63)
    co = _f04_dividend_coverage(dps, eps, 63)
    base = g * co * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combocovgrowth_252d_jerk_v074_signal(dps, eps, closeadj):
    g = _f04_dps_growth(dps, 252)
    co = _f04_dividend_coverage(dps, eps, 252)
    base = g * co * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Compound Ã— coverage
def f04udg_f04_utility_dividend_growth_combocovcomp_63d_jerk_v075_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    c = _f04_dividend_compound(dps, 63)
    base = co * c * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combocovcomp_252d_jerk_v076_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    c = _f04_dividend_compound(dps, 252)
    base = co * c * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Dollar volume
def f04udg_f04_utility_dividend_growth_dpsgrowthxdv_63d_jerk_v077_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 63)
    dv = closeadj * volume
    base = g * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxdv_252d_jerk_v078_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 252)
    dv = closeadj * volume
    base = g * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxdv_63d_jerk_v079_signal(dps, closeadj, volume):
    c = _f04_dividend_compound(dps, 63)
    dv = closeadj * volume
    base = c * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxdv_252d_jerk_v080_signal(dps, closeadj, volume):
    c = _f04_dividend_compound(dps, 252)
    dv = closeadj * volume
    base = c * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexdv_63d_jerk_v081_signal(dps, eps, closeadj, volume):
    co = _f04_dividend_coverage(dps, eps, 63)
    dv = closeadj * volume
    base = co * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexdv_252d_jerk_v082_signal(dps, eps, closeadj, volume):
    co = _f04_dividend_coverage(dps, eps, 252)
    dv = closeadj * volume
    base = co * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Std
def f04udg_f04_utility_dividend_growth_dpsgrowthstd_63d_jerk_v083_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = _std(g, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthstd_252d_jerk_v084_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = _std(g, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundstd_63d_jerk_v085_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 63)
    base = _std(c, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundstd_252d_jerk_v086_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    base = _std(c, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragestd_63d_jerk_v087_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = _std(co, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragestd_252d_jerk_v088_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = _std(co, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Size weighted
def f04udg_f04_utility_dividend_growth_dpsgrowthxsize_63d_jerk_v089_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = g * np.log(dps.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxsize_252d_jerk_v090_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = g * np.log(dps.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxsize_63d_jerk_v091_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 63)
    base = c * np.log(dps.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxsize_252d_jerk_v092_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    base = c * np.log(dps.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Closez
def f04udg_f04_utility_dividend_growth_dpsgrowthxclosez_63d_jerk_v093_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = g * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxclosez_252d_jerk_v094_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = g * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxclosez_63d_jerk_v095_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 63)
    base = c * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxclosez_252d_jerk_v096_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    base = c * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexclosez_63d_jerk_v097_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = co * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexclosez_252d_jerk_v098_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = co * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Return
def f04udg_f04_utility_dividend_growth_dpsgrowthxret_63d_jerk_v099_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = g * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxret_252d_jerk_v100_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = g * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxret_63d_jerk_v101_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 63)
    base = c * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundxret_252d_jerk_v102_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    base = c * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexret_63d_jerk_v103_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = co * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexret_252d_jerk_v104_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = co * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Abs return
def f04udg_f04_utility_dividend_growth_dpsgrowthxabsret_63d_jerk_v105_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = g * closeadj.pct_change(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxabsret_252d_jerk_v106_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = g * closeadj.pct_change(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexabsret_63d_jerk_v107_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = co * closeadj.pct_change(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragexabsret_252d_jerk_v108_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = co * closeadj.pct_change(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Acceleration
def f04udg_f04_utility_dividend_growth_dpsgrowthaccel_63d_jerk_v109_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = (g - g.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthaccel_252d_jerk_v110_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = (g - g.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundaccel_63d_jerk_v111_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 63)
    base = (c - c.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compoundaccel_252d_jerk_v112_signal(dps, closeadj):
    c = _f04_dividend_compound(dps, 252)
    base = (c - c.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverageaccel_63d_jerk_v113_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = (co - co.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverageaccel_252d_jerk_v114_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = (co - co.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Inv price
def f04udg_f04_utility_dividend_growth_dpsgrowthxinv_63d_jerk_v115_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = g * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthxinv_252d_jerk_v116_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 252)
    base = g * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# MA cross
def f04udg_f04_utility_dividend_growth_dpsgrowthcross_21_252_jerk_v117_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 21) - _f04_dps_growth(dps, 252)
    base = g * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthcross_63_252_jerk_v118_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63) - _f04_dps_growth(dps, 252)
    base = g * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragecross_63_252_jerk_v119_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63) - _f04_dividend_coverage(dps, eps, 252)
    base = co * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Spread vs target
def f04udg_f04_utility_dividend_growth_dpsgrowthspread_63d_jerk_v120_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = (g - 0.05) * closeadj * _mean(g, 63) / _mean(g, 252).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragespread_63d_jerk_v121_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 63)
    base = (co - 2.0) * closeadj * _mean(co, 63) / _mean(co, 252).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Sum
def f04udg_f04_utility_dividend_growth_dpsgrowthsum_63d_jerk_v122_signal(dps, closeadj):
    g = _f04_dps_growth(dps, 63)
    base = g.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragesum_252d_jerk_v123_signal(dps, eps, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = co.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Sign Ã— vol
def f04udg_f04_utility_dividend_growth_dpsgrowthsignxvol_63d_jerk_v124_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 63)
    base = np.sign(g) * _mean(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthsignxvol_252d_jerk_v125_signal(dps, closeadj, volume):
    g = _f04_dps_growth(dps, 252)
    base = np.sign(g) * _mean(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Diff-norm (slope-then-jerk for distinction)
def f04udg_f04_utility_dividend_growth_dpsgrowthdn_63d_jerk_v126_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63) * closeadj
    sl = _slope(base, 21)
    result = _jerk(sl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpsgrowthdn_252d_jerk_v127_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252) * closeadj
    sl = _slope(base, 63)
    result = _jerk(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compounddn_63d_jerk_v128_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63) * closeadj
    sl = _slope(base, 21)
    result = _jerk(sl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compounddn_252d_jerk_v129_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252) * closeadj
    sl = _slope(base, 63)
    result = _jerk(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragedn_63d_jerk_v130_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63) * closeadj
    sl = _slope(base, 21)
    result = _jerk(sl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coveragedn_252d_jerk_v131_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252) * closeadj
    sl = _slope(base, 63)
    result = _jerk(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d
def f04udg_f04_utility_dividend_growth_dpsgrowth_5d_jerk_v132_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_5d_jerk_v133_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_5d_jerk_v134_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d
def f04udg_f04_utility_dividend_growth_dpsgrowth_10d_jerk_v135_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_10d_jerk_v136_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_10d_jerk_v137_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d
def f04udg_f04_utility_dividend_growth_dpsgrowth_42d_jerk_v138_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_42d_jerk_v139_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_42d_jerk_v140_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d
def f04udg_f04_utility_dividend_growth_dpsgrowth_189d_jerk_v141_signal(dps, closeadj):
    base = _f04_dps_growth(dps, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_compound_189d_jerk_v142_signal(dps, closeadj):
    base = _f04_dividend_compound(dps, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_coverage_189d_jerk_v143_signal(dps, eps, closeadj):
    base = _f04_dividend_coverage(dps, eps, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo with ATR
def f04udg_f04_utility_dividend_growth_combo_atr_63d_jerk_v144_signal(dps, eps, closeadj, high, low):
    co = _f04_dividend_coverage(dps, eps, 63)
    c = _f04_dividend_compound(dps, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = co * c * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combo_atr_252d_jerk_v145_signal(dps, eps, closeadj, high, low):
    co = _f04_dividend_coverage(dps, eps, 252)
    c = _f04_dividend_compound(dps, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = co * c * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo with dv
def f04udg_f04_utility_dividend_growth_combo_dv_63d_jerk_v146_signal(dps, eps, closeadj, volume):
    co = _f04_dividend_coverage(dps, eps, 63)
    g = _f04_dps_growth(dps, 63)
    dv = closeadj * volume
    base = co * g * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_combo_dv_252d_jerk_v147_signal(dps, eps, closeadj, volume):
    co = _f04_dividend_coverage(dps, eps, 252)
    g = _f04_dps_growth(dps, 252)
    dv = closeadj * volume
    base = co * g * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Dps log
def f04udg_f04_utility_dividend_growth_dpslog_63d_jerk_v148_signal(dps, closeadj):
    rb = _f04_dps_growth(dps, 63)
    base = np.log(dps.abs().replace(0, np.nan)) * closeadj + rb * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f04udg_f04_utility_dividend_growth_dpslog_252d_jerk_v149_signal(dps, closeadj):
    rb = _f04_dps_growth(dps, 252)
    base = np.log(dps.abs().replace(0, np.nan)) * _mean(closeadj, 63) + rb * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Coverage Ã— payout
def f04udg_f04_utility_dividend_growth_coveragexpayout_252d_jerk_v150_signal(dps, eps, payoutratio, closeadj):
    co = _f04_dividend_coverage(dps, eps, 252)
    base = co * _mean(payoutratio, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04udg_f04_utility_dividend_growth_dpsgrowth_21d_jerk_v001_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_21d_jerk_v002_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_63d_jerk_v003_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_63d_jerk_v004_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_63d_jerk_v005_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_252d_jerk_v006_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_252d_jerk_v007_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_252d_jerk_v008_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_504d_jerk_v009_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_504d_jerk_v010_signal,
    f04udg_f04_utility_dividend_growth_compound_21d_jerk_v011_signal,
    f04udg_f04_utility_dividend_growth_compound_21d_jerk_v012_signal,
    f04udg_f04_utility_dividend_growth_compound_63d_jerk_v013_signal,
    f04udg_f04_utility_dividend_growth_compound_63d_jerk_v014_signal,
    f04udg_f04_utility_dividend_growth_compound_252d_jerk_v015_signal,
    f04udg_f04_utility_dividend_growth_compound_252d_jerk_v016_signal,
    f04udg_f04_utility_dividend_growth_compound_252d_jerk_v017_signal,
    f04udg_f04_utility_dividend_growth_compound_504d_jerk_v018_signal,
    f04udg_f04_utility_dividend_growth_compound_504d_jerk_v019_signal,
    f04udg_f04_utility_dividend_growth_coverage_21d_jerk_v020_signal,
    f04udg_f04_utility_dividend_growth_coverage_21d_jerk_v021_signal,
    f04udg_f04_utility_dividend_growth_coverage_63d_jerk_v022_signal,
    f04udg_f04_utility_dividend_growth_coverage_63d_jerk_v023_signal,
    f04udg_f04_utility_dividend_growth_coverage_252d_jerk_v024_signal,
    f04udg_f04_utility_dividend_growth_coverage_252d_jerk_v025_signal,
    f04udg_f04_utility_dividend_growth_coverage_252d_jerk_v026_signal,
    f04udg_f04_utility_dividend_growth_coverage_504d_jerk_v027_signal,
    f04udg_f04_utility_dividend_growth_coverage_504d_jerk_v028_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxvol_63d_jerk_v029_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxvol_252d_jerk_v030_signal,
    f04udg_f04_utility_dividend_growth_compoundxvol_63d_jerk_v031_signal,
    f04udg_f04_utility_dividend_growth_compoundxvol_252d_jerk_v032_signal,
    f04udg_f04_utility_dividend_growth_coveragexvol_63d_jerk_v033_signal,
    f04udg_f04_utility_dividend_growth_coveragexvol_252d_jerk_v034_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxatr_63d_jerk_v035_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxatr_252d_jerk_v036_signal,
    f04udg_f04_utility_dividend_growth_compoundxatr_63d_jerk_v037_signal,
    f04udg_f04_utility_dividend_growth_compoundxatr_252d_jerk_v038_signal,
    f04udg_f04_utility_dividend_growth_coveragexatr_63d_jerk_v039_signal,
    f04udg_f04_utility_dividend_growth_coveragexatr_252d_jerk_v040_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthema_63d_jerk_v041_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthema_252d_jerk_v042_signal,
    f04udg_f04_utility_dividend_growth_compoundema_63d_jerk_v043_signal,
    f04udg_f04_utility_dividend_growth_compoundema_252d_jerk_v044_signal,
    f04udg_f04_utility_dividend_growth_coverageema_63d_jerk_v045_signal,
    f04udg_f04_utility_dividend_growth_coverageema_252d_jerk_v046_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsq_63d_jerk_v047_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsq_252d_jerk_v048_signal,
    f04udg_f04_utility_dividend_growth_compoundsq_63d_jerk_v049_signal,
    f04udg_f04_utility_dividend_growth_compoundsq_252d_jerk_v050_signal,
    f04udg_f04_utility_dividend_growth_coveragesq_63d_jerk_v051_signal,
    f04udg_f04_utility_dividend_growth_coveragesq_252d_jerk_v052_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthz_63d_jerk_v053_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthz_252d_jerk_v054_signal,
    f04udg_f04_utility_dividend_growth_compoundz_63d_jerk_v055_signal,
    f04udg_f04_utility_dividend_growth_compoundz_252d_jerk_v056_signal,
    f04udg_f04_utility_dividend_growth_coveragez_63d_jerk_v057_signal,
    f04udg_f04_utility_dividend_growth_coveragez_252d_jerk_v058_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthrank_63d_jerk_v059_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthrank_252d_jerk_v060_signal,
    f04udg_f04_utility_dividend_growth_compoundrank_63d_jerk_v061_signal,
    f04udg_f04_utility_dividend_growth_compoundrank_252d_jerk_v062_signal,
    f04udg_f04_utility_dividend_growth_coveragerank_63d_jerk_v063_signal,
    f04udg_f04_utility_dividend_growth_coveragerank_252d_jerk_v064_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthgap_63d_jerk_v065_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthgap_252d_jerk_v066_signal,
    f04udg_f04_utility_dividend_growth_compoundgap_63d_jerk_v067_signal,
    f04udg_f04_utility_dividend_growth_compoundgap_252d_jerk_v068_signal,
    f04udg_f04_utility_dividend_growth_coveragegap_63d_jerk_v069_signal,
    f04udg_f04_utility_dividend_growth_coveragegap_252d_jerk_v070_signal,
    f04udg_f04_utility_dividend_growth_combocompgrowth_63d_jerk_v071_signal,
    f04udg_f04_utility_dividend_growth_combocompgrowth_252d_jerk_v072_signal,
    f04udg_f04_utility_dividend_growth_combocovgrowth_63d_jerk_v073_signal,
    f04udg_f04_utility_dividend_growth_combocovgrowth_252d_jerk_v074_signal,
    f04udg_f04_utility_dividend_growth_combocovcomp_63d_jerk_v075_signal,
    f04udg_f04_utility_dividend_growth_combocovcomp_252d_jerk_v076_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxdv_63d_jerk_v077_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxdv_252d_jerk_v078_signal,
    f04udg_f04_utility_dividend_growth_compoundxdv_63d_jerk_v079_signal,
    f04udg_f04_utility_dividend_growth_compoundxdv_252d_jerk_v080_signal,
    f04udg_f04_utility_dividend_growth_coveragexdv_63d_jerk_v081_signal,
    f04udg_f04_utility_dividend_growth_coveragexdv_252d_jerk_v082_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthstd_63d_jerk_v083_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthstd_252d_jerk_v084_signal,
    f04udg_f04_utility_dividend_growth_compoundstd_63d_jerk_v085_signal,
    f04udg_f04_utility_dividend_growth_compoundstd_252d_jerk_v086_signal,
    f04udg_f04_utility_dividend_growth_coveragestd_63d_jerk_v087_signal,
    f04udg_f04_utility_dividend_growth_coveragestd_252d_jerk_v088_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxsize_63d_jerk_v089_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxsize_252d_jerk_v090_signal,
    f04udg_f04_utility_dividend_growth_compoundxsize_63d_jerk_v091_signal,
    f04udg_f04_utility_dividend_growth_compoundxsize_252d_jerk_v092_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxclosez_63d_jerk_v093_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxclosez_252d_jerk_v094_signal,
    f04udg_f04_utility_dividend_growth_compoundxclosez_63d_jerk_v095_signal,
    f04udg_f04_utility_dividend_growth_compoundxclosez_252d_jerk_v096_signal,
    f04udg_f04_utility_dividend_growth_coveragexclosez_63d_jerk_v097_signal,
    f04udg_f04_utility_dividend_growth_coveragexclosez_252d_jerk_v098_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxret_63d_jerk_v099_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxret_252d_jerk_v100_signal,
    f04udg_f04_utility_dividend_growth_compoundxret_63d_jerk_v101_signal,
    f04udg_f04_utility_dividend_growth_compoundxret_252d_jerk_v102_signal,
    f04udg_f04_utility_dividend_growth_coveragexret_63d_jerk_v103_signal,
    f04udg_f04_utility_dividend_growth_coveragexret_252d_jerk_v104_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxabsret_63d_jerk_v105_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxabsret_252d_jerk_v106_signal,
    f04udg_f04_utility_dividend_growth_coveragexabsret_63d_jerk_v107_signal,
    f04udg_f04_utility_dividend_growth_coveragexabsret_252d_jerk_v108_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthaccel_63d_jerk_v109_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthaccel_252d_jerk_v110_signal,
    f04udg_f04_utility_dividend_growth_compoundaccel_63d_jerk_v111_signal,
    f04udg_f04_utility_dividend_growth_compoundaccel_252d_jerk_v112_signal,
    f04udg_f04_utility_dividend_growth_coverageaccel_63d_jerk_v113_signal,
    f04udg_f04_utility_dividend_growth_coverageaccel_252d_jerk_v114_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxinv_63d_jerk_v115_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthxinv_252d_jerk_v116_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthcross_21_252_jerk_v117_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthcross_63_252_jerk_v118_signal,
    f04udg_f04_utility_dividend_growth_coveragecross_63_252_jerk_v119_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthspread_63d_jerk_v120_signal,
    f04udg_f04_utility_dividend_growth_coveragespread_63d_jerk_v121_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsum_63d_jerk_v122_signal,
    f04udg_f04_utility_dividend_growth_coveragesum_252d_jerk_v123_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsignxvol_63d_jerk_v124_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthsignxvol_252d_jerk_v125_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthdn_63d_jerk_v126_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowthdn_252d_jerk_v127_signal,
    f04udg_f04_utility_dividend_growth_compounddn_63d_jerk_v128_signal,
    f04udg_f04_utility_dividend_growth_compounddn_252d_jerk_v129_signal,
    f04udg_f04_utility_dividend_growth_coveragedn_63d_jerk_v130_signal,
    f04udg_f04_utility_dividend_growth_coveragedn_252d_jerk_v131_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_5d_jerk_v132_signal,
    f04udg_f04_utility_dividend_growth_compound_5d_jerk_v133_signal,
    f04udg_f04_utility_dividend_growth_coverage_5d_jerk_v134_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_10d_jerk_v135_signal,
    f04udg_f04_utility_dividend_growth_compound_10d_jerk_v136_signal,
    f04udg_f04_utility_dividend_growth_coverage_10d_jerk_v137_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_42d_jerk_v138_signal,
    f04udg_f04_utility_dividend_growth_compound_42d_jerk_v139_signal,
    f04udg_f04_utility_dividend_growth_coverage_42d_jerk_v140_signal,
    f04udg_f04_utility_dividend_growth_dpsgrowth_189d_jerk_v141_signal,
    f04udg_f04_utility_dividend_growth_compound_189d_jerk_v142_signal,
    f04udg_f04_utility_dividend_growth_coverage_189d_jerk_v143_signal,
    f04udg_f04_utility_dividend_growth_combo_atr_63d_jerk_v144_signal,
    f04udg_f04_utility_dividend_growth_combo_atr_252d_jerk_v145_signal,
    f04udg_f04_utility_dividend_growth_combo_dv_63d_jerk_v146_signal,
    f04udg_f04_utility_dividend_growth_combo_dv_252d_jerk_v147_signal,
    f04udg_f04_utility_dividend_growth_dpslog_63d_jerk_v148_signal,
    f04udg_f04_utility_dividend_growth_dpslog_252d_jerk_v149_signal,
    f04udg_f04_utility_dividend_growth_coveragexpayout_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_UTILITY_DIVIDEND_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f04_utility_dividend_growth_3rd_derivatives_001_150_claude: {n_features} features pass")

