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
def _f48_self_smoothed_baseline(closeadj, w):
    return _mean(closeadj, w)


def _f48_self_momentum_excess(closeadj, w):
    base = _mean(closeadj, w)
    return closeadj - base


def _f48_momentum_persistence(closeadj, w):
    ret_short = closeadj.pct_change(w)
    ret_long = _mean(closeadj.pct_change(w), w)
    return ret_short - ret_long


# v001-v009: smoothed baseline gap × close
def f48srm_f48_sector_relative_momentum_base_21d_base_v001_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 21)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_63d_base_v002_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 63)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_126d_base_v003_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 126)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_252d_base_v004_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 252)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_504d_base_v005_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 504)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_5d_base_v006_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 5)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_42d_base_v007_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 42)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_189d_base_v008_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 189)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_378d_base_v009_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 378)
    result = (closeadj - base)
    return result.replace([np.inf, -np.inf], np.nan)


# v010-v018: momentum excess × close
def f48srm_f48_sector_relative_momentum_excess_21d_base_v010_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 21)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_63d_base_v011_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_126d_base_v012_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 126)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_252d_base_v013_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_504d_base_v014_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 504)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_5d_base_v015_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 5)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_42d_base_v016_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 42)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_189d_base_v017_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 189)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_378d_base_v018_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 378)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019-v027: persistence
def f48srm_f48_sector_relative_momentum_pers_21d_base_v019_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_63d_base_v020_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_126d_base_v021_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_252d_base_v022_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_504d_base_v023_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_5d_base_v024_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_42d_base_v025_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_189d_base_v026_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_378d_base_v027_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028-v035: z-score variants
def f48srm_f48_sector_relative_momentum_excessz_63d_base_v028_signal(closeadj):
    base = _z(_f48_self_momentum_excess(closeadj, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessz_252d_base_v029_signal(closeadj):
    base = _z(_f48_self_momentum_excess(closeadj, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basez_63d_base_v030_signal(closeadj):
    base = _z(_f48_self_smoothed_baseline(closeadj, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basez_252d_base_v031_signal(closeadj):
    base = _z(_f48_self_smoothed_baseline(closeadj, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persz_63d_base_v032_signal(closeadj):
    base = _z(_f48_momentum_persistence(closeadj, 63), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persz_252d_base_v033_signal(closeadj):
    base = _z(_f48_momentum_persistence(closeadj, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessz_21d_base_v034_signal(closeadj):
    base = _z(_f48_self_momentum_excess(closeadj, 21), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persz_21d_base_v035_signal(closeadj):
    base = _z(_f48_momentum_persistence(closeadj, 21), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036-v041: std variants
def f48srm_f48_sector_relative_momentum_excessstd_63d_base_v036_signal(closeadj):
    base = _std(_f48_self_momentum_excess(closeadj, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessstd_252d_base_v037_signal(closeadj):
    base = _std(_f48_self_momentum_excess(closeadj, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persstd_252d_base_v038_signal(closeadj):
    base = _std(_f48_momentum_persistence(closeadj, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basestd_252d_base_v039_signal(closeadj):
    base = _std(_f48_self_smoothed_baseline(closeadj, 21), 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessstd_504d_base_v040_signal(closeadj):
    base = _std(_f48_self_momentum_excess(closeadj, 63), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basestd_504d_base_v041_signal(closeadj):
    base = _std(_f48_self_smoothed_baseline(closeadj, 63), 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# v042-v047: diffs and ratios between long/short baselines
def f48srm_f48_sector_relative_momentum_basediff_63m252_base_v042_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 63)
    lg = _f48_self_smoothed_baseline(closeadj, 252)
    result = (sh - lg)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basediff_21m63_base_v043_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 21)
    lg = _f48_self_smoothed_baseline(closeadj, 63)
    result = (sh - lg)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basediff_252m504_base_v044_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 252)
    lg = _f48_self_smoothed_baseline(closeadj, 504)
    result = (sh - lg)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baseratio_63v252_base_v045_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 63)
    lg = _f48_self_smoothed_baseline(closeadj, 252)
    result = sh / lg.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessdiff_63m252_base_v046_signal(closeadj):
    sh = _f48_self_momentum_excess(closeadj, 63)
    lg = _f48_self_momentum_excess(closeadj, 252)
    result = (sh - lg) * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persdiff_63m252_base_v047_signal(closeadj):
    sh = _f48_momentum_persistence(closeadj, 63)
    lg = _f48_momentum_persistence(closeadj, 252)
    result = (sh - lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048-v053: EMAs
def f48srm_f48_sector_relative_momentum_excessema_63d_base_v048_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessema_252d_base_v049_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persema_63d_base_v050_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persema_252d_base_v051_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baseema_63d_base_v052_signal(closeadj):
    g = _f48_self_smoothed_baseline(closeadj, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baseema_252d_base_v053_signal(closeadj):
    g = _f48_self_smoothed_baseline(closeadj, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# v054-v057: ranks
def f48srm_f48_sector_relative_momentum_excessrank_252d_base_v054_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrank_504d_base_v055_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persrank_252d_base_v056_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baserank_252d_base_v057_signal(closeadj):
    g = _f48_self_smoothed_baseline(closeadj, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058-v065: volume-interaction
def f48srm_f48_sector_relative_momentum_excessxvolz_63d_base_v058_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * _z(volume, 63)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvolz_252d_base_v059_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252) * _z(volume, 252)
    result = base * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxdv_63d_base_v060_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * _mean(closeadj * volume, 21)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxdv_252d_base_v061_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252) * _mean(closeadj * volume, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxvolz_63d_base_v062_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 63) * _z(volume, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxdv_252d_base_v063_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 252) * _mean(closeadj * volume, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxlogvol_63d_base_v064_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * np.log(volume.abs().replace(0, np.nan))
    result = base / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxlogvol_63d_base_v065_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 63) * np.log(volume.abs().replace(0, np.nan))
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066-v075: min/max/range/skew/kurt and squared/lograw
def f48srm_f48_sector_relative_momentum_excessmin_63d_base_v066_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(63, min_periods=21).min()
    result = base + g * 0.1
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessmax_252d_base_v067_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(252, min_periods=63).max()
    result = base + g * 0.1
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrange_252d_base_v068_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    result = rng + g * 0.1
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persrange_252d_base_v069_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessskew_252d_base_v070_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(252, min_periods=63).skew()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excesskurt_252d_base_v071_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(252, min_periods=63).kurt()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_sqexcess_252d_base_v072_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    result = g * g.abs() / closeadj.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_sqpers_252d_base_v073_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_logexcess_252d_base_v074_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    result = np.sign(g) * np.log1p(g.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_composite_252d_base_v075_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 252)
    b = _f48_momentum_persistence(closeadj, 252)
    result = (a + b * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48srm_f48_sector_relative_momentum_base_21d_base_v001_signal,
    f48srm_f48_sector_relative_momentum_base_63d_base_v002_signal,
    f48srm_f48_sector_relative_momentum_base_126d_base_v003_signal,
    f48srm_f48_sector_relative_momentum_base_252d_base_v004_signal,
    f48srm_f48_sector_relative_momentum_base_504d_base_v005_signal,
    f48srm_f48_sector_relative_momentum_base_5d_base_v006_signal,
    f48srm_f48_sector_relative_momentum_base_42d_base_v007_signal,
    f48srm_f48_sector_relative_momentum_base_189d_base_v008_signal,
    f48srm_f48_sector_relative_momentum_base_378d_base_v009_signal,
    f48srm_f48_sector_relative_momentum_excess_21d_base_v010_signal,
    f48srm_f48_sector_relative_momentum_excess_63d_base_v011_signal,
    f48srm_f48_sector_relative_momentum_excess_126d_base_v012_signal,
    f48srm_f48_sector_relative_momentum_excess_252d_base_v013_signal,
    f48srm_f48_sector_relative_momentum_excess_504d_base_v014_signal,
    f48srm_f48_sector_relative_momentum_excess_5d_base_v015_signal,
    f48srm_f48_sector_relative_momentum_excess_42d_base_v016_signal,
    f48srm_f48_sector_relative_momentum_excess_189d_base_v017_signal,
    f48srm_f48_sector_relative_momentum_excess_378d_base_v018_signal,
    f48srm_f48_sector_relative_momentum_pers_21d_base_v019_signal,
    f48srm_f48_sector_relative_momentum_pers_63d_base_v020_signal,
    f48srm_f48_sector_relative_momentum_pers_126d_base_v021_signal,
    f48srm_f48_sector_relative_momentum_pers_252d_base_v022_signal,
    f48srm_f48_sector_relative_momentum_pers_504d_base_v023_signal,
    f48srm_f48_sector_relative_momentum_pers_5d_base_v024_signal,
    f48srm_f48_sector_relative_momentum_pers_42d_base_v025_signal,
    f48srm_f48_sector_relative_momentum_pers_189d_base_v026_signal,
    f48srm_f48_sector_relative_momentum_pers_378d_base_v027_signal,
    f48srm_f48_sector_relative_momentum_excessz_63d_base_v028_signal,
    f48srm_f48_sector_relative_momentum_excessz_252d_base_v029_signal,
    f48srm_f48_sector_relative_momentum_basez_63d_base_v030_signal,
    f48srm_f48_sector_relative_momentum_basez_252d_base_v031_signal,
    f48srm_f48_sector_relative_momentum_persz_63d_base_v032_signal,
    f48srm_f48_sector_relative_momentum_persz_252d_base_v033_signal,
    f48srm_f48_sector_relative_momentum_excessz_21d_base_v034_signal,
    f48srm_f48_sector_relative_momentum_persz_21d_base_v035_signal,
    f48srm_f48_sector_relative_momentum_excessstd_63d_base_v036_signal,
    f48srm_f48_sector_relative_momentum_excessstd_252d_base_v037_signal,
    f48srm_f48_sector_relative_momentum_persstd_252d_base_v038_signal,
    f48srm_f48_sector_relative_momentum_basestd_252d_base_v039_signal,
    f48srm_f48_sector_relative_momentum_excessstd_504d_base_v040_signal,
    f48srm_f48_sector_relative_momentum_basestd_504d_base_v041_signal,
    f48srm_f48_sector_relative_momentum_basediff_63m252_base_v042_signal,
    f48srm_f48_sector_relative_momentum_basediff_21m63_base_v043_signal,
    f48srm_f48_sector_relative_momentum_basediff_252m504_base_v044_signal,
    f48srm_f48_sector_relative_momentum_baseratio_63v252_base_v045_signal,
    f48srm_f48_sector_relative_momentum_excessdiff_63m252_base_v046_signal,
    f48srm_f48_sector_relative_momentum_persdiff_63m252_base_v047_signal,
    f48srm_f48_sector_relative_momentum_excessema_63d_base_v048_signal,
    f48srm_f48_sector_relative_momentum_excessema_252d_base_v049_signal,
    f48srm_f48_sector_relative_momentum_persema_63d_base_v050_signal,
    f48srm_f48_sector_relative_momentum_persema_252d_base_v051_signal,
    f48srm_f48_sector_relative_momentum_baseema_63d_base_v052_signal,
    f48srm_f48_sector_relative_momentum_baseema_252d_base_v053_signal,
    f48srm_f48_sector_relative_momentum_excessrank_252d_base_v054_signal,
    f48srm_f48_sector_relative_momentum_excessrank_504d_base_v055_signal,
    f48srm_f48_sector_relative_momentum_persrank_252d_base_v056_signal,
    f48srm_f48_sector_relative_momentum_baserank_252d_base_v057_signal,
    f48srm_f48_sector_relative_momentum_excessxvolz_63d_base_v058_signal,
    f48srm_f48_sector_relative_momentum_excessxvolz_252d_base_v059_signal,
    f48srm_f48_sector_relative_momentum_excessxdv_63d_base_v060_signal,
    f48srm_f48_sector_relative_momentum_excessxdv_252d_base_v061_signal,
    f48srm_f48_sector_relative_momentum_persxvolz_63d_base_v062_signal,
    f48srm_f48_sector_relative_momentum_persxdv_252d_base_v063_signal,
    f48srm_f48_sector_relative_momentum_excessxlogvol_63d_base_v064_signal,
    f48srm_f48_sector_relative_momentum_persxlogvol_63d_base_v065_signal,
    f48srm_f48_sector_relative_momentum_excessmin_63d_base_v066_signal,
    f48srm_f48_sector_relative_momentum_excessmax_252d_base_v067_signal,
    f48srm_f48_sector_relative_momentum_excessrange_252d_base_v068_signal,
    f48srm_f48_sector_relative_momentum_persrange_252d_base_v069_signal,
    f48srm_f48_sector_relative_momentum_excessskew_252d_base_v070_signal,
    f48srm_f48_sector_relative_momentum_excesskurt_252d_base_v071_signal,
    f48srm_f48_sector_relative_momentum_sqexcess_252d_base_v072_signal,
    f48srm_f48_sector_relative_momentum_sqpers_252d_base_v073_signal,
    f48srm_f48_sector_relative_momentum_logexcess_252d_base_v074_signal,
    f48srm_f48_sector_relative_momentum_composite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_SECTOR_RELATIVE_MOMENTUM_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_self_smoothed_baseline", "_f48_self_momentum_excess", "_f48_momentum_persistence")
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
    print(f"OK f48_sector_relative_momentum_base_001_075_claude: {n_features} features pass")
