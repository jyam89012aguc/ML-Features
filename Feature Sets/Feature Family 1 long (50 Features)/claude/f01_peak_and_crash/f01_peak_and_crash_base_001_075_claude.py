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
def _f01_peak_level(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).max()


def _f01_drawdown_from_peak(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - peak) / peak.replace(0, np.nan).abs()


def _f01_crash_intensity(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    dd = (close - peak) / peak.replace(0, np.nan).abs()
    rng = (close.rolling(w, min_periods=max(1, w // 2)).max()
           - close.rolling(w, min_periods=max(1, w // 2)).min())
    return dd * close / rng.replace(0, np.nan)


# 21d rolling peak level scaled by closeadj
def f01pc_f01_peak_and_crash_peaklevel_21d_base_v001_signal(closeadj):
    result = _f01_peak_level(closeadj, 21) - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling peak level minus closeadj
def f01pc_f01_peak_and_crash_peaklevel_63d_base_v002_signal(closeadj):
    result = _f01_peak_level(closeadj, 63) - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling peak level minus closeadj
def f01pc_f01_peak_and_crash_peaklevel_126d_base_v003_signal(closeadj):
    result = _f01_peak_level(closeadj, 126) - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling peak level minus closeadj
def f01pc_f01_peak_and_crash_peaklevel_252d_base_v004_signal(closeadj):
    result = _f01_peak_level(closeadj, 252) - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling peak level minus closeadj
def f01pc_f01_peak_and_crash_peaklevel_504d_base_v005_signal(closeadj):
    result = _f01_peak_level(closeadj, 504) - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown from peak (event detection)
def f01pc_f01_peak_and_crash_dd_21d_base_v006_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown from peak scaled by close
def f01pc_f01_peak_and_crash_dd_63d_base_v007_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown from peak scaled by close
def f01pc_f01_peak_and_crash_dd_252d_base_v008_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown from peak scaled by close
def f01pc_f01_peak_and_crash_dd_504d_base_v009_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding all-time-high gap scaled by close
def f01pc_f01_peak_and_crash_athgap_base_v010_signal(closeadj):
    ath = closeadj.expanding(min_periods=21).max()
    gap = (closeadj - ath) / ath.replace(0, np.nan).abs()
    result = gap * closeadj + _f01_peak_level(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# days since 252d peak scaled by close (peak age × price)
def f01pc_f01_peak_and_crash_peakage_252d_base_v011_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    result = age * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# days since 63d peak scaled by close
def f01pc_f01_peak_and_crash_peakage_63d_base_v012_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    result = age * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# days since 504d peak scaled by close
def f01pc_f01_peak_and_crash_peakage_504d_base_v013_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    result = age * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d peak erosion (peak today vs peak 21d ago)
def f01pc_f01_peak_and_crash_peakerosion_21d_base_v014_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    result = (peak - peak.shift(21)) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d peak erosion
def f01pc_f01_peak_and_crash_peakerosion_63d_base_v015_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    result = (peak - peak.shift(63)) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak erosion
def f01pc_f01_peak_and_crash_peakerosion_252d_base_v016_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    result = (peak - peak.shift(63)) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d peak erosion
def f01pc_f01_peak_and_crash_peakerosion_504d_base_v017_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    result = (peak - peak.shift(126)) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash intensity (depth weighted by range and price)
def f01pc_f01_peak_and_crash_crashintensity_21d_base_v018_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_63d_base_v019_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_252d_base_v020_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_504d_base_v021_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of new-peak events scaled by closeadj
def f01pc_f01_peak_and_crash_newpeakcount_252d_base_v022_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    new_peak = (closeadj >= peak).astype(float)
    cnt = new_peak.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of new-peak events scaled by closeadj
def f01pc_f01_peak_and_crash_newpeakcount_63d_base_v023_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    new_peak = (closeadj >= peak).astype(float)
    cnt = new_peak.rolling(63, min_periods=21).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of new-peak events scaled by closeadj
def f01pc_f01_peak_and_crash_newpeakcount_504d_base_v024_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    new_peak = (closeadj >= peak).astype(float)
    cnt = new_peak.rolling(504, min_periods=126).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of crash events (drawdown crossing -10%)
def f01pc_f01_peak_and_crash_crashcount_252d_base_v025_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 63)
    cross = ((dd < -0.10) & (dd.shift(1) >= -0.10)).astype(float)
    cnt = cross.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of crash events at -15% threshold
def f01pc_f01_peak_and_crash_crashcount_504d_base_v026_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 252)
    cross = ((dd < -0.15) & (dd.shift(1) >= -0.15)).astype(float)
    cnt = cross.rolling(504, min_periods=126).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of mini-crash events at -5% threshold
def f01pc_f01_peak_and_crash_crashcount_63d_base_v027_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 21)
    cross = ((dd < -0.05) & (dd.shift(1) >= -0.05)).astype(float)
    cnt = cross.rolling(63, min_periods=21).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d post-peak return (5d after peak event)
def f01pc_f01_peak_and_crash_postpeakret_21d_base_v028_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    at_peak = (closeadj >= peak).astype(float)
    fwd = closeadj.shift(-5) / closeadj - 1.0
    result = at_peak * fwd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d post-peak return (21d after peak)
def f01pc_f01_peak_and_crash_postpeakret_63d_base_v029_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    fwd = closeadj.shift(-21) / closeadj - 1.0
    result = at_peak * fwd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d post-peak return (63d after peak)
def f01pc_f01_peak_and_crash_postpeakret_252d_base_v030_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    fwd = closeadj.shift(-63) / closeadj - 1.0
    result = at_peak * fwd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d peak proximity ratio (close / peak) scaled by close
def f01pc_f01_peak_and_crash_peakprox_21d_base_v031_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21).replace(0, np.nan)
    result = (closeadj / peak) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d peak proximity ratio
def f01pc_f01_peak_and_crash_peakprox_63d_base_v032_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63).replace(0, np.nan)
    result = (closeadj / peak) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak proximity ratio
def f01pc_f01_peak_and_crash_peakprox_252d_base_v033_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    result = (closeadj / peak) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d peak proximity ratio
def f01pc_f01_peak_and_crash_peakprox_504d_base_v034_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504).replace(0, np.nan)
    result = (closeadj / peak) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash sharpness: drawdown / days since peak
def f01pc_f01_peak_and_crash_crashsharp_21d_base_v035_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 21).abs()
    peak = _f01_peak_level(closeadj, 21)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    result = (dd / age) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash sharpness
def f01pc_f01_peak_and_crash_crashsharp_63d_base_v036_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 63).abs()
    peak = _f01_peak_level(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    result = (dd / age) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crash sharpness
def f01pc_f01_peak_and_crash_crashsharp_252d_base_v037_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 252).abs()
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    result = (dd / age) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crash sharpness
def f01pc_f01_peak_and_crash_crashsharp_504d_base_v038_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 504).abs()
    peak = _f01_peak_level(closeadj, 504)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    result = (dd / age) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 63d drawdown over 21d
def f01pc_f01_peak_and_crash_ddmean_21d_base_v039_signal(closeadj):
    result = _mean(_f01_drawdown_from_peak(closeadj, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 252d drawdown over 63d
def f01pc_f01_peak_and_crash_ddmean_63d_base_v040_signal(closeadj):
    result = _mean(_f01_drawdown_from_peak(closeadj, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 252d drawdown over 63d
def f01pc_f01_peak_and_crash_ddstd_63d_base_v041_signal(closeadj):
    result = _std(_f01_drawdown_from_peak(closeadj, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 504d drawdown over 126d
def f01pc_f01_peak_and_crash_ddstd_126d_base_v042_signal(closeadj):
    result = _std(_f01_drawdown_from_peak(closeadj, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d zscore of 63d drawdown
def f01pc_f01_peak_and_crash_ddz_21d_base_v043_signal(closeadj):
    result = _z(_f01_drawdown_from_peak(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of 252d drawdown
def f01pc_f01_peak_and_crash_ddz_63d_base_v044_signal(closeadj):
    result = _z(_f01_drawdown_from_peak(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATH gap × volume (event sentiment)
def f01pc_f01_peak_and_crash_athgapxvol_21d_base_v045_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max()
    gap = (closeadj - ath) / ath.replace(0, np.nan).abs()
    result = gap * volume + _f01_drawdown_from_peak(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATH gap × dollar volume
def f01pc_f01_peak_and_crash_athgapxdv_63d_base_v046_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max()
    gap = (closeadj - ath) / ath.replace(0, np.nan).abs()
    dv = closeadj * volume
    result = gap * _mean(dv, 21) + _f01_drawdown_from_peak(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d crash intensity (intraweek)
def f01pc_f01_peak_and_crash_crashintensity_5d_base_v047_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_10d_base_v048_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d crash intensity (2mo)
def f01pc_f01_peak_and_crash_crashintensity_42d_base_v049_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d crash intensity (~9mo)
def f01pc_f01_peak_and_crash_crashintensity_189d_base_v050_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d crash intensity (~1.5y)
def f01pc_f01_peak_and_crash_crashintensity_378d_base_v051_signal(closeadj):
    result = _f01_crash_intensity(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d drawdown × close (intraweek event)
def f01pc_f01_peak_and_crash_dd_5d_base_v052_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d drawdown × close
def f01pc_f01_peak_and_crash_dd_10d_base_v053_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d drawdown × close
def f01pc_f01_peak_and_crash_dd_42d_base_v054_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d drawdown × close
def f01pc_f01_peak_and_crash_dd_189d_base_v055_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d drawdown × close
def f01pc_f01_peak_and_crash_dd_378d_base_v056_signal(closeadj):
    result = _f01_drawdown_from_peak(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d post-crash recovery: close vs trough scaled
def f01pc_f01_peak_and_crash_postcrashrec_21d_base_v057_signal(closeadj):
    trough = closeadj.rolling(21, min_periods=5).min()
    in_crash = (_f01_drawdown_from_peak(closeadj, 21) < -0.05).astype(float)
    rec = (closeadj - trough) / trough.replace(0, np.nan).abs()
    result = rec * in_crash * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d post-crash recovery
def f01pc_f01_peak_and_crash_postcrashrec_63d_base_v058_signal(closeadj):
    trough = closeadj.rolling(63, min_periods=21).min()
    in_crash = (_f01_drawdown_from_peak(closeadj, 63) < -0.10).astype(float)
    rec = (closeadj - trough) / trough.replace(0, np.nan).abs()
    result = rec * in_crash * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d post-crash recovery
def f01pc_f01_peak_and_crash_postcrashrec_252d_base_v059_signal(closeadj):
    trough = closeadj.rolling(252, min_periods=63).min()
    in_crash = (_f01_drawdown_from_peak(closeadj, 252) < -0.15).astype(float)
    rec = (closeadj - trough) / trough.replace(0, np.nan).abs()
    result = rec * in_crash * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding ATH proximity (close / ATH) × close
def f01pc_f01_peak_and_crash_athprox_base_v060_signal(closeadj):
    ath = closeadj.expanding(min_periods=21).max().replace(0, np.nan)
    result = (closeadj / ath) * closeadj + _f01_peak_level(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d peak prominence: peak vs surrounding troughs
def f01pc_f01_peak_and_crash_peakprom_21d_base_v061_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    trough = closeadj.rolling(21, min_periods=5).min()
    result = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d peak prominence
def f01pc_f01_peak_and_crash_peakprom_63d_base_v062_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    trough = closeadj.rolling(63, min_periods=21).min()
    result = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak prominence
def f01pc_f01_peak_and_crash_peakprom_252d_base_v063_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    trough = closeadj.rolling(252, min_periods=63).min()
    result = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d peak prominence
def f01pc_f01_peak_and_crash_peakprom_504d_base_v064_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    trough = closeadj.rolling(504, min_periods=126).min()
    result = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown × volume (event volume)
def f01pc_f01_peak_and_crash_ddxvol_21d_base_v065_signal(closeadj, volume):
    result = _f01_drawdown_from_peak(closeadj, 21) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown × volume
def f01pc_f01_peak_and_crash_ddxvol_63d_base_v066_signal(closeadj, volume):
    result = _f01_drawdown_from_peak(closeadj, 63) * volume
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown × dollar volume
def f01pc_f01_peak_and_crash_ddxdv_252d_base_v067_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f01_drawdown_from_peak(closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown × dollar volume
def f01pc_f01_peak_and_crash_ddxdv_504d_base_v068_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f01_drawdown_from_peak(closeadj, 504) * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d crash intensity × volume
def f01pc_f01_peak_and_crash_intensxvol_21d_base_v069_signal(closeadj, volume):
    result = _f01_crash_intensity(closeadj, 21) * _z(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crash intensity × volume z
def f01pc_f01_peak_and_crash_intensxvol_63d_base_v070_signal(closeadj, volume):
    result = _f01_crash_intensity(closeadj, 63) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown squared (severity emphasis) × close
def f01pc_f01_peak_and_crash_ddsq_252d_base_v071_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown squared × close
def f01pc_f01_peak_and_crash_ddsq_63d_base_v072_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown squared × close
def f01pc_f01_peak_and_crash_ddsq_21d_base_v073_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 21)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d peak level zscore over 504d
def f01pc_f01_peak_and_crash_peakz_252d_base_v074_signal(closeadj):
    result = _z(_f01_peak_level(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown × ATR-style range proxy
def f01pc_f01_peak_and_crash_ddxatr_252d_base_v075_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f01_drawdown_from_peak(closeadj, 252) * closeadj * rng / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01pc_f01_peak_and_crash_peaklevel_21d_base_v001_signal,
    f01pc_f01_peak_and_crash_peaklevel_63d_base_v002_signal,
    f01pc_f01_peak_and_crash_peaklevel_126d_base_v003_signal,
    f01pc_f01_peak_and_crash_peaklevel_252d_base_v004_signal,
    f01pc_f01_peak_and_crash_peaklevel_504d_base_v005_signal,
    f01pc_f01_peak_and_crash_dd_21d_base_v006_signal,
    f01pc_f01_peak_and_crash_dd_63d_base_v007_signal,
    f01pc_f01_peak_and_crash_dd_252d_base_v008_signal,
    f01pc_f01_peak_and_crash_dd_504d_base_v009_signal,
    f01pc_f01_peak_and_crash_athgap_base_v010_signal,
    f01pc_f01_peak_and_crash_peakage_252d_base_v011_signal,
    f01pc_f01_peak_and_crash_peakage_63d_base_v012_signal,
    f01pc_f01_peak_and_crash_peakage_504d_base_v013_signal,
    f01pc_f01_peak_and_crash_peakerosion_21d_base_v014_signal,
    f01pc_f01_peak_and_crash_peakerosion_63d_base_v015_signal,
    f01pc_f01_peak_and_crash_peakerosion_252d_base_v016_signal,
    f01pc_f01_peak_and_crash_peakerosion_504d_base_v017_signal,
    f01pc_f01_peak_and_crash_crashintensity_21d_base_v018_signal,
    f01pc_f01_peak_and_crash_crashintensity_63d_base_v019_signal,
    f01pc_f01_peak_and_crash_crashintensity_252d_base_v020_signal,
    f01pc_f01_peak_and_crash_crashintensity_504d_base_v021_signal,
    f01pc_f01_peak_and_crash_newpeakcount_252d_base_v022_signal,
    f01pc_f01_peak_and_crash_newpeakcount_63d_base_v023_signal,
    f01pc_f01_peak_and_crash_newpeakcount_504d_base_v024_signal,
    f01pc_f01_peak_and_crash_crashcount_252d_base_v025_signal,
    f01pc_f01_peak_and_crash_crashcount_504d_base_v026_signal,
    f01pc_f01_peak_and_crash_crashcount_63d_base_v027_signal,
    f01pc_f01_peak_and_crash_postpeakret_21d_base_v028_signal,
    f01pc_f01_peak_and_crash_postpeakret_63d_base_v029_signal,
    f01pc_f01_peak_and_crash_postpeakret_252d_base_v030_signal,
    f01pc_f01_peak_and_crash_peakprox_21d_base_v031_signal,
    f01pc_f01_peak_and_crash_peakprox_63d_base_v032_signal,
    f01pc_f01_peak_and_crash_peakprox_252d_base_v033_signal,
    f01pc_f01_peak_and_crash_peakprox_504d_base_v034_signal,
    f01pc_f01_peak_and_crash_crashsharp_21d_base_v035_signal,
    f01pc_f01_peak_and_crash_crashsharp_63d_base_v036_signal,
    f01pc_f01_peak_and_crash_crashsharp_252d_base_v037_signal,
    f01pc_f01_peak_and_crash_crashsharp_504d_base_v038_signal,
    f01pc_f01_peak_and_crash_ddmean_21d_base_v039_signal,
    f01pc_f01_peak_and_crash_ddmean_63d_base_v040_signal,
    f01pc_f01_peak_and_crash_ddstd_63d_base_v041_signal,
    f01pc_f01_peak_and_crash_ddstd_126d_base_v042_signal,
    f01pc_f01_peak_and_crash_ddz_21d_base_v043_signal,
    f01pc_f01_peak_and_crash_ddz_63d_base_v044_signal,
    f01pc_f01_peak_and_crash_athgapxvol_21d_base_v045_signal,
    f01pc_f01_peak_and_crash_athgapxdv_63d_base_v046_signal,
    f01pc_f01_peak_and_crash_crashintensity_5d_base_v047_signal,
    f01pc_f01_peak_and_crash_crashintensity_10d_base_v048_signal,
    f01pc_f01_peak_and_crash_crashintensity_42d_base_v049_signal,
    f01pc_f01_peak_and_crash_crashintensity_189d_base_v050_signal,
    f01pc_f01_peak_and_crash_crashintensity_378d_base_v051_signal,
    f01pc_f01_peak_and_crash_dd_5d_base_v052_signal,
    f01pc_f01_peak_and_crash_dd_10d_base_v053_signal,
    f01pc_f01_peak_and_crash_dd_42d_base_v054_signal,
    f01pc_f01_peak_and_crash_dd_189d_base_v055_signal,
    f01pc_f01_peak_and_crash_dd_378d_base_v056_signal,
    f01pc_f01_peak_and_crash_postcrashrec_21d_base_v057_signal,
    f01pc_f01_peak_and_crash_postcrashrec_63d_base_v058_signal,
    f01pc_f01_peak_and_crash_postcrashrec_252d_base_v059_signal,
    f01pc_f01_peak_and_crash_athprox_base_v060_signal,
    f01pc_f01_peak_and_crash_peakprom_21d_base_v061_signal,
    f01pc_f01_peak_and_crash_peakprom_63d_base_v062_signal,
    f01pc_f01_peak_and_crash_peakprom_252d_base_v063_signal,
    f01pc_f01_peak_and_crash_peakprom_504d_base_v064_signal,
    f01pc_f01_peak_and_crash_ddxvol_21d_base_v065_signal,
    f01pc_f01_peak_and_crash_ddxvol_63d_base_v066_signal,
    f01pc_f01_peak_and_crash_ddxdv_252d_base_v067_signal,
    f01pc_f01_peak_and_crash_ddxdv_504d_base_v068_signal,
    f01pc_f01_peak_and_crash_intensxvol_21d_base_v069_signal,
    f01pc_f01_peak_and_crash_intensxvol_63d_base_v070_signal,
    f01pc_f01_peak_and_crash_ddsq_252d_base_v071_signal,
    f01pc_f01_peak_and_crash_ddsq_63d_base_v072_signal,
    f01pc_f01_peak_and_crash_ddsq_21d_base_v073_signal,
    f01pc_f01_peak_and_crash_peakz_252d_base_v074_signal,
    f01pc_f01_peak_and_crash_ddxatr_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_PEAK_AND_CRASH_REGISTRY_001_075 = REGISTRY


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

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f01_peak_level", "_f01_drawdown_from_peak", "_f01_crash_intensity")
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
    print(f"OK f01_peak_and_crash_base_001_075_claude: {n_features} features pass")
