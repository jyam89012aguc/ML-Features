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


def _jerk(s, w):
    return s.pct_change(periods=w)


def _jerk(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _f48_self_smoothed_baseline(closeadj, w):
    return _mean(closeadj, w)


def _f48_self_momentum_excess(closeadj, w):
    base = _mean(closeadj, w)
    return closeadj - base


def _f48_momentum_persistence(closeadj, w):
    ret_short = closeadj.pct_change(w)
    ret_long = _mean(closeadj.pct_change(w), w)
    return ret_short - ret_long


# We generate 150 jerk features each wrapping a base concept

def f48srm_f48_sector_relative_momentum_base_21d_jerk_v001_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_21d_jerk_v002_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_63d_jerk_v003_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_126d_jerk_v004_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 126))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_252d_jerk_v005_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 252))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_504d_jerk_v006_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 504))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_5d_jerk_v007_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 5))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_42d_jerk_v008_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 42))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_189d_jerk_v009_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 189))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_378d_jerk_v010_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 378))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_21d_jerk_v011_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_63d_jerk_v012_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_126d_jerk_v013_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_252d_jerk_v014_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_504d_jerk_v015_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 504)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_5d_jerk_v016_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_42d_jerk_v017_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_189d_jerk_v018_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_378d_jerk_v019_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 378)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_21d_jerk_v020_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_63d_jerk_v021_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_252d_jerk_v022_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_504d_jerk_v023_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_126d_jerk_v024_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_42d_jerk_v025_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_189d_jerk_v026_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_378d_jerk_v027_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessz_63d_jerk_v028_signal(closeadj):
    base = _z(_f48_self_momentum_excess(closeadj, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessz_252d_jerk_v029_signal(closeadj):
    base = _z(_f48_self_momentum_excess(closeadj, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basez_63d_jerk_v030_signal(closeadj):
    base = _z(_f48_self_smoothed_baseline(closeadj, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basez_252d_jerk_v031_signal(closeadj):
    base = _z(_f48_self_smoothed_baseline(closeadj, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persz_63d_jerk_v032_signal(closeadj):
    base = _z(_f48_momentum_persistence(closeadj, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persz_252d_jerk_v033_signal(closeadj):
    base = _z(_f48_momentum_persistence(closeadj, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessstd_63d_jerk_v034_signal(closeadj):
    base = _std(_f48_self_momentum_excess(closeadj, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessstd_252d_jerk_v035_signal(closeadj):
    base = _std(_f48_self_momentum_excess(closeadj, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persstd_252d_jerk_v036_signal(closeadj):
    base = _std(_f48_momentum_persistence(closeadj, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basediff_63m252_jerk_v037_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 63)
    lg = _f48_self_smoothed_baseline(closeadj, 252)
    base = (sh - lg)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basediff_21m63_jerk_v038_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 21)
    lg = _f48_self_smoothed_baseline(closeadj, 63)
    base = (sh - lg)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basediff_252m504_jerk_v039_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 252)
    lg = _f48_self_smoothed_baseline(closeadj, 504)
    base = (sh - lg)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessdiff_63m252_jerk_v040_signal(closeadj):
    sh = _f48_self_momentum_excess(closeadj, 63)
    lg = _f48_self_momentum_excess(closeadj, 252)
    base = (sh - lg)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persdiff_63m252_jerk_v041_signal(closeadj):
    sh = _f48_momentum_persistence(closeadj, 63)
    lg = _f48_momentum_persistence(closeadj, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessema_63d_jerk_v042_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessema_252d_jerk_v043_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persema_63d_jerk_v044_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persema_252d_jerk_v045_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrank_252d_jerk_v046_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persrank_252d_jerk_v047_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvolz_63d_jerk_v048_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * _z(volume, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvolz_252d_jerk_v049_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252) * _z(volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxdv_63d_jerk_v050_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * _mean(closeadj * volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxdv_252d_jerk_v051_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252) * _mean(closeadj * volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxvolz_63d_jerk_v052_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 63) * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxdv_252d_jerk_v053_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 252) * _mean(closeadj * volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessskew_252d_jerk_v054_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excesskurt_252d_jerk_v055_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_sqexcess_252d_jerk_v056_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    base = g * g.abs() / closeadj.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_sqpers_252d_jerk_v057_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_composite_252d_jerk_v058_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 252)
    b = _f48_momentum_persistence(closeadj, 252)
    base = (a + b * closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_composite_504d_jerk_v059_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 504)
    b = _f48_momentum_persistence(closeadj, 504)
    base = (a + b * closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_logexcess_252d_jerk_v060_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    base = np.sign(g) * np.log1p(g.abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxlogvol_63d_jerk_v061_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * np.log(volume.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxlogvol_63d_jerk_v062_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 63) * np.log(volume.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessmin_63d_jerk_v063_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(63, min_periods=21).min()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessmax_252d_jerk_v064_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(252, min_periods=63).max() + g * 0.1
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrange_252d_jerk_v065_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    result = _jerk(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_dualema_21v63_jerk_v066_signal(closeadj):
    ema_s = closeadj.ewm(span=21, adjust=False).mean()
    ema_l = closeadj.ewm(span=63, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 21) + (ema_s - ema_l)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_dualema_63v252_jerk_v067_signal(closeadj):
    ema_s = closeadj.ewm(span=63, adjust=False).mean()
    ema_l = closeadj.ewm(span=252, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 63) + (ema_s - ema_l)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_macdsig_jerk_v068_signal(closeadj):
    ema_s = closeadj.ewm(span=12, adjust=False).mean()
    ema_l = closeadj.ewm(span=26, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 21) + ((ema_s - ema_l) - (ema_s - ema_l).ewm(span=9, adjust=False).mean())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrsi_21d_jerk_v069_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 21)
    up = base.where(base > 0, 0.0)
    dn = (-base).where(base < 0, 0.0)
    rs = _mean(up, 21) / _mean(dn, 21).replace(0, np.nan)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    result = _jerk(rsi + base * 0.0, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessvoladj_252d_jerk_v070_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    vol = _std(closeadj.pct_change(), 252)
    base = g / vol.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persvoladj_252d_jerk_v071_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    vol = _std(closeadj.pct_change(), 252)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_med_252d_jerk_v072_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    base = (g - med)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_hi_252d_jerk_v073_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_diff_long_short_jerk_v074_signal(closeadj):
    base = (_f48_self_smoothed_baseline(closeadj, 21) - _f48_self_smoothed_baseline(closeadj, 504))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_cumsum_252d_jerk_v075_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(252, min_periods=63).sum()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_cumsum_252d_jerk_v076_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 21)
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_lag_excess_252d_jerk_v077_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = (g - g.shift(252))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvol_growth_252d_jerk_v078_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252) * volume.pct_change(252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxvol_growth_63d_jerk_v079_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 63) * volume.pct_change(63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_vw_63d_jerk_v080_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63)
    vw = _mean(closeadj * volume, 21) / _mean(volume, 21).replace(0, np.nan)
    base2 = base + (closeadj - vw)
    result = _jerk(base2, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxlogprice_252d_jerk_v081_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_pct_252d_jerk_v082_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252).pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_sqrt_63d_jerk_v083_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63) * np.sqrt(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_kavg_252d_jerk_v084_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    base = g.rolling(252, min_periods=63).mean() * 0.5 + g * 0.5
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxpers_252d_jerk_v085_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 252)
    b = _f48_momentum_persistence(closeadj, 252)
    base = (a + b * closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxpers_504d_jerk_v086_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 504)
    b = _f48_momentum_persistence(closeadj, 504)
    base = (a + b * closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_smooth_252d_jerk_v087_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = (g - _mean(g, 252))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_smooth_252d_jerk_v088_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 63)
    base = (g - _mean(g, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_dvxprice_252d_jerk_v089_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252) * _mean(closeadj * volume, 63) / closeadj.abs().replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_volz_long_504d_jerk_v090_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 504) * _z(volume, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_logprice_252d_jerk_v091_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    base = g * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basesqrt_252d_jerk_v092_signal(closeadj):
    base = _f48_self_smoothed_baseline(closeadj, 252)
    gap = (closeadj - base)
    base2 = np.sqrt(gap.abs()) * np.sign(gap)
    result = _jerk(base2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_logvolxprice_63d_jerk_v093_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * np.log(volume.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_logvol_252d_jerk_v094_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 252) * np.log(volume.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessabs_252d_jerk_v095_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    result = _jerk(g.abs(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_signxexcess_63d_jerk_v096_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    sg = np.sign(g) * closeadj
    result = _jerk(sg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_10d_jerk_v097_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 10)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_84d_jerk_v098_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_10d_jerk_v099_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 10) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_84d_jerk_v100_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 84) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_msq_252d_jerk_v101_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    base = np.sign(g) * g * g
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_63d_jerk_v102_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_252d_jerk_v103_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrank_504d_jerk_v104_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baserank_252d_jerk_v105_signal(closeadj):
    g = _f48_self_smoothed_baseline(closeadj, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessz_21d_jerk_v106_signal(closeadj):
    base = _z(_f48_self_momentum_excess(closeadj, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persz_21d_jerk_v107_signal(closeadj):
    base = _z(_f48_momentum_persistence(closeadj, 21), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basediff_252m504_jerk_alt_v108_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 252)
    lg = _f48_self_smoothed_baseline(closeadj, 504)
    base = (sh - lg)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessstd_504d_jerk_v109_signal(closeadj):
    base = _std(_f48_self_momentum_excess(closeadj, 63), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basestd_504d_jerk_v110_signal(closeadj):
    base = _std(_f48_self_smoothed_baseline(closeadj, 63), 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baseema_63d_jerk_v111_signal(closeadj):
    g = _f48_self_smoothed_baseline(closeadj, 21)
    base = g.ewm(span=63, adjust=False).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baseema_252d_jerk_v112_signal(closeadj):
    g = _f48_self_smoothed_baseline(closeadj, 63)
    base = g.ewm(span=252, adjust=False).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_lo_252d_jerk_v113_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    base = (lo * g + g * 0.5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_hi_252d_jerk_v114_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_logabs_252d_jerk_v115_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    base = np.log1p(g.abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_logabs_252d_jerk_v116_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    base = np.log1p(g.abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_pct_63d_jerk_v117_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63).pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_pct_252d_jerk_v118_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 252).pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_kavg_63d_jerk_v119_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = g.rolling(63, min_periods=21).mean() * 0.5 + g * 0.5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_long_log_504d_jerk_v120_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 504) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_cumprod_252d_jerk_v121_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 252)
    norm_g = g / closeadj.abs().replace(0, np.nan)
    base = norm_g.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_cumsum_504d_jerk_v122_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 21)
    base = g.rolling(504, min_periods=126).sum()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_cumsum_504d_jerk_v123_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 21)
    base = g.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvol_dv_63d_jerk_v124_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 63) * _z(closeadj * volume, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxvol_dv_252d_jerk_v125_signal(closeadj, volume):
    base = _f48_momentum_persistence(closeadj, 252) * _z(closeadj * volume, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basexvol_z_252d_jerk_v126_signal(closeadj, volume):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 252)) * _z(volume, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_ratiocls_252d_jerk_v127_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252) / closeadj.replace(0, np.nan) * closeadj * 10.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persxprice_sqrt_252d_jerk_v128_signal(closeadj):
    base = _f48_momentum_persistence(closeadj, 252) * np.sqrt(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_macdsig_long_jerk_v129_signal(closeadj):
    ema_s = closeadj.ewm(span=63, adjust=False).mean()
    ema_l = closeadj.ewm(span=189, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 63) + ((ema_s - ema_l) - (ema_s - ema_l).ewm(span=42, adjust=False).mean())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessrsi_63d_jerk_v130_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63)
    up = base.where(base > 0, 0.0)
    dn = (-base).where(base < 0, 0.0)
    rs = _mean(up, 63) / _mean(dn, 63).replace(0, np.nan)
    rsi = 100.0 - (100.0 / (1.0 + rs))
    result = _jerk(rsi + base * 0.0, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessvoladj_63d_jerk_v131_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    vol = _std(closeadj.pct_change(), 63)
    base = g / vol.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_med_252d_jerk_v132_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    base = (g - med) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basediff_21m63_alt_jerk_v133_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 21)
    lg = _f48_self_smoothed_baseline(closeadj, 63)
    base = (sh - lg) * closeadj / closeadj.abs().replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_diff_long_short_504_jerk_v134_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 63)
    lg = _f48_self_smoothed_baseline(closeadj, 504)
    base = (sh - lg)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_baseratio_63v252_jerk_v135_signal(closeadj):
    sh = _f48_self_smoothed_baseline(closeadj, 63)
    lg = _f48_self_smoothed_baseline(closeadj, 252)
    base = sh / lg.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_dualema_252v504_jerk_v136_signal(closeadj):
    ema_s = closeadj.ewm(span=252, adjust=False).mean()
    ema_l = closeadj.ewm(span=504, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 252) + (ema_s - ema_l)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_dualema_5v21_jerk_v137_signal(closeadj):
    ema_s = closeadj.ewm(span=5, adjust=False).mean()
    ema_l = closeadj.ewm(span=21, adjust=False).mean()
    base = _f48_self_smoothed_baseline(closeadj, 5) + (ema_s - ema_l)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_lag_excess_63d_jerk_v138_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = (g - g.shift(63))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvol_z_504d_jerk_v139_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 504) * _z(volume, 504)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_basestd_252d_jerk_v140_signal(closeadj):
    base = _std(_f48_self_smoothed_baseline(closeadj, 21), 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_persdiff_63m252_alt_jerk_v141_signal(closeadj):
    sh = _f48_momentum_persistence(closeadj, 63)
    lg = _f48_momentum_persistence(closeadj, 252)
    base = (sh - lg) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_vw_252d_jerk_v142_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252)
    vw = _mean(closeadj * volume, 63) / _mean(volume, 63).replace(0, np.nan)
    base2 = base + (closeadj - vw)
    result = _jerk(base2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxprice_log_63d_jerk_v143_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 63) * np.log(closeadj.abs().replace(0, np.nan))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_pers_kavg_252d_jerk_v144_signal(closeadj):
    g = _f48_momentum_persistence(closeadj, 252)
    base = (g.rolling(252, min_periods=63).mean() * 0.5 + g * 0.5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excess_smooth_504d_jerk_v145_signal(closeadj):
    g = _f48_self_momentum_excess(closeadj, 63)
    base = (g - _mean(g, 504))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxpers_63d_jerk_v146_signal(closeadj):
    a = _f48_self_momentum_excess(closeadj, 63)
    b = _f48_momentum_persistence(closeadj, 63)
    base = (a + b * closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxvol_dv_252d_jerk_v147_signal(closeadj, volume):
    base = _f48_self_momentum_excess(closeadj, 252) * _z(closeadj * volume, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_excessxlogprice_alt_252d_jerk_v148_signal(closeadj):
    base = _f48_self_momentum_excess(closeadj, 252) * np.log(closeadj.abs().replace(0, np.nan)) * 1.1
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_composite_excess_pers_504d_jerk_v149_signal(closeadj, volume):
    a = _f48_self_momentum_excess(closeadj, 504)
    b = _f48_momentum_persistence(closeadj, 504)
    base = (a + b * closeadj) * _z(volume, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f48srm_f48_sector_relative_momentum_base_84d_jerk_v150_signal(closeadj):
    base = (closeadj - _f48_self_smoothed_baseline(closeadj, 84))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48srm_f48_sector_relative_momentum_base_21d_jerk_v001_signal,
    f48srm_f48_sector_relative_momentum_base_21d_jerk_v002_signal,
    f48srm_f48_sector_relative_momentum_base_63d_jerk_v003_signal,
    f48srm_f48_sector_relative_momentum_base_126d_jerk_v004_signal,
    f48srm_f48_sector_relative_momentum_base_252d_jerk_v005_signal,
    f48srm_f48_sector_relative_momentum_base_504d_jerk_v006_signal,
    f48srm_f48_sector_relative_momentum_base_5d_jerk_v007_signal,
    f48srm_f48_sector_relative_momentum_base_42d_jerk_v008_signal,
    f48srm_f48_sector_relative_momentum_base_189d_jerk_v009_signal,
    f48srm_f48_sector_relative_momentum_base_378d_jerk_v010_signal,
    f48srm_f48_sector_relative_momentum_excess_21d_jerk_v011_signal,
    f48srm_f48_sector_relative_momentum_excess_63d_jerk_v012_signal,
    f48srm_f48_sector_relative_momentum_excess_126d_jerk_v013_signal,
    f48srm_f48_sector_relative_momentum_excess_252d_jerk_v014_signal,
    f48srm_f48_sector_relative_momentum_excess_504d_jerk_v015_signal,
    f48srm_f48_sector_relative_momentum_excess_5d_jerk_v016_signal,
    f48srm_f48_sector_relative_momentum_excess_42d_jerk_v017_signal,
    f48srm_f48_sector_relative_momentum_excess_189d_jerk_v018_signal,
    f48srm_f48_sector_relative_momentum_excess_378d_jerk_v019_signal,
    f48srm_f48_sector_relative_momentum_pers_21d_jerk_v020_signal,
    f48srm_f48_sector_relative_momentum_pers_63d_jerk_v021_signal,
    f48srm_f48_sector_relative_momentum_pers_252d_jerk_v022_signal,
    f48srm_f48_sector_relative_momentum_pers_504d_jerk_v023_signal,
    f48srm_f48_sector_relative_momentum_pers_126d_jerk_v024_signal,
    f48srm_f48_sector_relative_momentum_pers_42d_jerk_v025_signal,
    f48srm_f48_sector_relative_momentum_pers_189d_jerk_v026_signal,
    f48srm_f48_sector_relative_momentum_pers_378d_jerk_v027_signal,
    f48srm_f48_sector_relative_momentum_excessz_63d_jerk_v028_signal,
    f48srm_f48_sector_relative_momentum_excessz_252d_jerk_v029_signal,
    f48srm_f48_sector_relative_momentum_basez_63d_jerk_v030_signal,
    f48srm_f48_sector_relative_momentum_basez_252d_jerk_v031_signal,
    f48srm_f48_sector_relative_momentum_persz_63d_jerk_v032_signal,
    f48srm_f48_sector_relative_momentum_persz_252d_jerk_v033_signal,
    f48srm_f48_sector_relative_momentum_excessstd_63d_jerk_v034_signal,
    f48srm_f48_sector_relative_momentum_excessstd_252d_jerk_v035_signal,
    f48srm_f48_sector_relative_momentum_persstd_252d_jerk_v036_signal,
    f48srm_f48_sector_relative_momentum_basediff_63m252_jerk_v037_signal,
    f48srm_f48_sector_relative_momentum_basediff_21m63_jerk_v038_signal,
    f48srm_f48_sector_relative_momentum_basediff_252m504_jerk_v039_signal,
    f48srm_f48_sector_relative_momentum_excessdiff_63m252_jerk_v040_signal,
    f48srm_f48_sector_relative_momentum_persdiff_63m252_jerk_v041_signal,
    f48srm_f48_sector_relative_momentum_excessema_63d_jerk_v042_signal,
    f48srm_f48_sector_relative_momentum_excessema_252d_jerk_v043_signal,
    f48srm_f48_sector_relative_momentum_persema_63d_jerk_v044_signal,
    f48srm_f48_sector_relative_momentum_persema_252d_jerk_v045_signal,
    f48srm_f48_sector_relative_momentum_excessrank_252d_jerk_v046_signal,
    f48srm_f48_sector_relative_momentum_persrank_252d_jerk_v047_signal,
    f48srm_f48_sector_relative_momentum_excessxvolz_63d_jerk_v048_signal,
    f48srm_f48_sector_relative_momentum_excessxvolz_252d_jerk_v049_signal,
    f48srm_f48_sector_relative_momentum_excessxdv_63d_jerk_v050_signal,
    f48srm_f48_sector_relative_momentum_excessxdv_252d_jerk_v051_signal,
    f48srm_f48_sector_relative_momentum_persxvolz_63d_jerk_v052_signal,
    f48srm_f48_sector_relative_momentum_persxdv_252d_jerk_v053_signal,
    f48srm_f48_sector_relative_momentum_excessskew_252d_jerk_v054_signal,
    f48srm_f48_sector_relative_momentum_excesskurt_252d_jerk_v055_signal,
    f48srm_f48_sector_relative_momentum_sqexcess_252d_jerk_v056_signal,
    f48srm_f48_sector_relative_momentum_sqpers_252d_jerk_v057_signal,
    f48srm_f48_sector_relative_momentum_composite_252d_jerk_v058_signal,
    f48srm_f48_sector_relative_momentum_composite_504d_jerk_v059_signal,
    f48srm_f48_sector_relative_momentum_logexcess_252d_jerk_v060_signal,
    f48srm_f48_sector_relative_momentum_excessxlogvol_63d_jerk_v061_signal,
    f48srm_f48_sector_relative_momentum_persxlogvol_63d_jerk_v062_signal,
    f48srm_f48_sector_relative_momentum_excessmin_63d_jerk_v063_signal,
    f48srm_f48_sector_relative_momentum_excessmax_252d_jerk_v064_signal,
    f48srm_f48_sector_relative_momentum_excessrange_252d_jerk_v065_signal,
    f48srm_f48_sector_relative_momentum_dualema_21v63_jerk_v066_signal,
    f48srm_f48_sector_relative_momentum_dualema_63v252_jerk_v067_signal,
    f48srm_f48_sector_relative_momentum_macdsig_jerk_v068_signal,
    f48srm_f48_sector_relative_momentum_excessrsi_21d_jerk_v069_signal,
    f48srm_f48_sector_relative_momentum_excessvoladj_252d_jerk_v070_signal,
    f48srm_f48_sector_relative_momentum_persvoladj_252d_jerk_v071_signal,
    f48srm_f48_sector_relative_momentum_excess_med_252d_jerk_v072_signal,
    f48srm_f48_sector_relative_momentum_excess_hi_252d_jerk_v073_signal,
    f48srm_f48_sector_relative_momentum_diff_long_short_jerk_v074_signal,
    f48srm_f48_sector_relative_momentum_excess_cumsum_252d_jerk_v075_signal,
    f48srm_f48_sector_relative_momentum_pers_cumsum_252d_jerk_v076_signal,
    f48srm_f48_sector_relative_momentum_lag_excess_252d_jerk_v077_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_growth_252d_jerk_v078_signal,
    f48srm_f48_sector_relative_momentum_persxvol_growth_63d_jerk_v079_signal,
    f48srm_f48_sector_relative_momentum_excess_vw_63d_jerk_v080_signal,
    f48srm_f48_sector_relative_momentum_excessxlogprice_252d_jerk_v081_signal,
    f48srm_f48_sector_relative_momentum_excess_pct_252d_jerk_v082_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_sqrt_63d_jerk_v083_signal,
    f48srm_f48_sector_relative_momentum_excess_kavg_252d_jerk_v084_signal,
    f48srm_f48_sector_relative_momentum_excessxpers_252d_jerk_v085_signal,
    f48srm_f48_sector_relative_momentum_excessxpers_504d_jerk_v086_signal,
    f48srm_f48_sector_relative_momentum_excess_smooth_252d_jerk_v087_signal,
    f48srm_f48_sector_relative_momentum_pers_smooth_252d_jerk_v088_signal,
    f48srm_f48_sector_relative_momentum_excess_dvxprice_252d_jerk_v089_signal,
    f48srm_f48_sector_relative_momentum_excess_volz_long_504d_jerk_v090_signal,
    f48srm_f48_sector_relative_momentum_pers_logprice_252d_jerk_v091_signal,
    f48srm_f48_sector_relative_momentum_basesqrt_252d_jerk_v092_signal,
    f48srm_f48_sector_relative_momentum_excess_logvolxprice_63d_jerk_v093_signal,
    f48srm_f48_sector_relative_momentum_pers_logvol_252d_jerk_v094_signal,
    f48srm_f48_sector_relative_momentum_excessabs_252d_jerk_v095_signal,
    f48srm_f48_sector_relative_momentum_signxexcess_63d_jerk_v096_signal,
    f48srm_f48_sector_relative_momentum_excess_10d_jerk_v097_signal,
    f48srm_f48_sector_relative_momentum_excess_84d_jerk_v098_signal,
    f48srm_f48_sector_relative_momentum_pers_10d_jerk_v099_signal,
    f48srm_f48_sector_relative_momentum_pers_84d_jerk_v100_signal,
    f48srm_f48_sector_relative_momentum_excess_msq_252d_jerk_v101_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_63d_jerk_v102_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_252d_jerk_v103_signal,
    f48srm_f48_sector_relative_momentum_excessrank_504d_jerk_v104_signal,
    f48srm_f48_sector_relative_momentum_baserank_252d_jerk_v105_signal,
    f48srm_f48_sector_relative_momentum_excessz_21d_jerk_v106_signal,
    f48srm_f48_sector_relative_momentum_persz_21d_jerk_v107_signal,
    f48srm_f48_sector_relative_momentum_basediff_252m504_jerk_alt_v108_signal,
    f48srm_f48_sector_relative_momentum_excessstd_504d_jerk_v109_signal,
    f48srm_f48_sector_relative_momentum_basestd_504d_jerk_v110_signal,
    f48srm_f48_sector_relative_momentum_baseema_63d_jerk_v111_signal,
    f48srm_f48_sector_relative_momentum_baseema_252d_jerk_v112_signal,
    f48srm_f48_sector_relative_momentum_excess_lo_252d_jerk_v113_signal,
    f48srm_f48_sector_relative_momentum_pers_hi_252d_jerk_v114_signal,
    f48srm_f48_sector_relative_momentum_excess_logabs_252d_jerk_v115_signal,
    f48srm_f48_sector_relative_momentum_pers_logabs_252d_jerk_v116_signal,
    f48srm_f48_sector_relative_momentum_excess_pct_63d_jerk_v117_signal,
    f48srm_f48_sector_relative_momentum_pers_pct_252d_jerk_v118_signal,
    f48srm_f48_sector_relative_momentum_excess_kavg_63d_jerk_v119_signal,
    f48srm_f48_sector_relative_momentum_excess_long_log_504d_jerk_v120_signal,
    f48srm_f48_sector_relative_momentum_excess_cumprod_252d_jerk_v121_signal,
    f48srm_f48_sector_relative_momentum_excess_cumsum_504d_jerk_v122_signal,
    f48srm_f48_sector_relative_momentum_pers_cumsum_504d_jerk_v123_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_dv_63d_jerk_v124_signal,
    f48srm_f48_sector_relative_momentum_persxvol_dv_252d_jerk_v125_signal,
    f48srm_f48_sector_relative_momentum_basexvol_z_252d_jerk_v126_signal,
    f48srm_f48_sector_relative_momentum_excess_ratiocls_252d_jerk_v127_signal,
    f48srm_f48_sector_relative_momentum_persxprice_sqrt_252d_jerk_v128_signal,
    f48srm_f48_sector_relative_momentum_macdsig_long_jerk_v129_signal,
    f48srm_f48_sector_relative_momentum_excessrsi_63d_jerk_v130_signal,
    f48srm_f48_sector_relative_momentum_excessvoladj_63d_jerk_v131_signal,
    f48srm_f48_sector_relative_momentum_pers_med_252d_jerk_v132_signal,
    f48srm_f48_sector_relative_momentum_basediff_21m63_alt_jerk_v133_signal,
    f48srm_f48_sector_relative_momentum_diff_long_short_504_jerk_v134_signal,
    f48srm_f48_sector_relative_momentum_baseratio_63v252_jerk_v135_signal,
    f48srm_f48_sector_relative_momentum_dualema_252v504_jerk_v136_signal,
    f48srm_f48_sector_relative_momentum_dualema_5v21_jerk_v137_signal,
    f48srm_f48_sector_relative_momentum_lag_excess_63d_jerk_v138_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_z_504d_jerk_v139_signal,
    f48srm_f48_sector_relative_momentum_basestd_252d_jerk_v140_signal,
    f48srm_f48_sector_relative_momentum_persdiff_63m252_alt_jerk_v141_signal,
    f48srm_f48_sector_relative_momentum_excess_vw_252d_jerk_v142_signal,
    f48srm_f48_sector_relative_momentum_excessxprice_log_63d_jerk_v143_signal,
    f48srm_f48_sector_relative_momentum_pers_kavg_252d_jerk_v144_signal,
    f48srm_f48_sector_relative_momentum_excess_smooth_504d_jerk_v145_signal,
    f48srm_f48_sector_relative_momentum_excessxpers_63d_jerk_v146_signal,
    f48srm_f48_sector_relative_momentum_excessxvol_dv_252d_jerk_v147_signal,
    f48srm_f48_sector_relative_momentum_excessxlogprice_alt_252d_jerk_v148_signal,
    f48srm_f48_sector_relative_momentum_composite_excess_pers_504d_jerk_v149_signal,
    f48srm_f48_sector_relative_momentum_base_84d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_SECTOR_RELATIVE_MOMENTUM_REGISTRY_jerk_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f48_sector_relative_momentum_3rd_derivatives_001_150_claude: {n_features} features pass")

