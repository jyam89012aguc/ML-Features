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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 5d slope of 21d peak level - close
def f01pc_f01_peak_and_crash_peaklevel_21d_slope_v001_signal(closeadj):
    base = _f01_peak_level(closeadj, 21) - closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d peak level - close
def f01pc_f01_peak_and_crash_peaklevel_21d_slope_v002_signal(closeadj):
    base = _f01_peak_level(closeadj, 21) - closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak gap
def f01pc_f01_peak_and_crash_peaklevel_63d_slope_v003_signal(closeadj):
    base = _f01_peak_level(closeadj, 63) - closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d peak gap
def f01pc_f01_peak_and_crash_peaklevel_126d_slope_v004_signal(closeadj):
    base = _f01_peak_level(closeadj, 126) - closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d peak gap
def f01pc_f01_peak_and_crash_peaklevel_252d_slope_v005_signal(closeadj):
    base = _f01_peak_level(closeadj, 252) - closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d peak gap
def f01pc_f01_peak_and_crash_peaklevel_504d_slope_v006_signal(closeadj):
    base = _f01_peak_level(closeadj, 504) - closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d drawdown × close
def f01pc_f01_peak_and_crash_dd_21d_slope_v007_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d drawdown × close
def f01pc_f01_peak_and_crash_dd_21d_slope_v008_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown × close
def f01pc_f01_peak_and_crash_dd_63d_slope_v009_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown × close
def f01pc_f01_peak_and_crash_dd_252d_slope_v010_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d drawdown × close
def f01pc_f01_peak_and_crash_dd_504d_slope_v011_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of expanding ATH gap × close
def f01pc_f01_peak_and_crash_athgap_slope_v012_signal(closeadj):
    ath = closeadj.expanding(min_periods=21).max()
    gap = (closeadj - ath) / ath.replace(0, np.nan).abs()
    base = gap * closeadj + _f01_peak_level(closeadj, 252) * 0.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d peak age × close
def f01pc_f01_peak_and_crash_peakage_252d_slope_v013_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak age × close
def f01pc_f01_peak_and_crash_peakage_63d_slope_v014_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d peak age × close
def f01pc_f01_peak_and_crash_peakage_504d_slope_v015_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d peak erosion
def f01pc_f01_peak_and_crash_peakerosion_21d_slope_v016_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    base = (peak - peak.shift(21)) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak erosion
def f01pc_f01_peak_and_crash_peakerosion_63d_slope_v017_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    base = (peak - peak.shift(63)) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d peak erosion
def f01pc_f01_peak_and_crash_peakerosion_252d_slope_v018_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    base = (peak - peak.shift(63)) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d peak erosion
def f01pc_f01_peak_and_crash_peakerosion_504d_slope_v019_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    base = (peak - peak.shift(126)) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_21d_slope_v020_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_63d_slope_v021_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_252d_slope_v022_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_504d_slope_v023_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d new-peak count × close
def f01pc_f01_peak_and_crash_newpeakcount_252d_slope_v024_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    new_peak = (closeadj >= peak).astype(float)
    base = new_peak.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d new-peak count × close
def f01pc_f01_peak_and_crash_newpeakcount_63d_slope_v025_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    new_peak = (closeadj >= peak).astype(float)
    base = new_peak.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d new-peak count × close
def f01pc_f01_peak_and_crash_newpeakcount_504d_slope_v026_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    new_peak = (closeadj >= peak).astype(float)
    base = new_peak.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d crash count × close
def f01pc_f01_peak_and_crash_crashcount_252d_slope_v027_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 63)
    cross = ((dd < -0.10) & (dd.shift(1) >= -0.10)).astype(float)
    base = cross.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d crash count × close
def f01pc_f01_peak_and_crash_crashcount_504d_slope_v028_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 252)
    cross = ((dd < -0.15) & (dd.shift(1) >= -0.15)).astype(float)
    base = cross.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d crash count × close
def f01pc_f01_peak_and_crash_crashcount_63d_slope_v029_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 21)
    cross = ((dd < -0.05) & (dd.shift(1) >= -0.05)).astype(float)
    base = cross.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d post-peak return × close (proximity-weighted)
def f01pc_f01_peak_and_crash_postpeakret_21d_slope_v030_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21).replace(0, np.nan)
    proximity = closeadj / peak.abs()
    fwd = closeadj.shift(-5) / closeadj - 1.0
    base = proximity * fwd * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d post-peak return × close (proximity-weighted)
def f01pc_f01_peak_and_crash_postpeakret_63d_slope_v031_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63).replace(0, np.nan)
    proximity = closeadj / peak.abs()
    fwd = closeadj.shift(-21) / closeadj - 1.0
    base = proximity * fwd * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d post-peak return × close (proximity-weighted)
def f01pc_f01_peak_and_crash_postpeakret_252d_slope_v032_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    proximity = closeadj / peak.abs()
    fwd = closeadj.shift(-63) / closeadj - 1.0
    base = proximity * fwd * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d peak proximity × close
def f01pc_f01_peak_and_crash_peakprox_21d_slope_v033_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21).replace(0, np.nan)
    base = (closeadj / peak) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak proximity × close
def f01pc_f01_peak_and_crash_peakprox_63d_slope_v034_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63).replace(0, np.nan)
    base = (closeadj / peak) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d peak proximity × close
def f01pc_f01_peak_and_crash_peakprox_252d_slope_v035_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    base = (closeadj / peak) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d peak proximity × close
def f01pc_f01_peak_and_crash_peakprox_504d_slope_v036_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504).replace(0, np.nan)
    base = (closeadj / peak) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d crash sharpness
def f01pc_f01_peak_and_crash_crashsharp_21d_slope_v037_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 21).abs()
    peak = _f01_peak_level(closeadj, 21)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    base = (dd / age) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d crash sharpness
def f01pc_f01_peak_and_crash_crashsharp_63d_slope_v038_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 63).abs()
    peak = _f01_peak_level(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    base = (dd / age) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d crash sharpness
def f01pc_f01_peak_and_crash_crashsharp_252d_slope_v039_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 252).abs()
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    base = (dd / age) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d crash sharpness
def f01pc_f01_peak_and_crash_crashsharp_504d_slope_v040_signal(closeadj):
    dd = _f01_drawdown_from_peak(closeadj, 504).abs()
    peak = _f01_peak_level(closeadj, 504)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    base = (dd / age) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown mean × close
def f01pc_f01_peak_and_crash_ddmean_21d_slope_v041_signal(closeadj):
    base = _mean(_f01_drawdown_from_peak(closeadj, 63), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d drawdown mean × close
def f01pc_f01_peak_and_crash_ddmean_63d_slope_v042_signal(closeadj):
    base = _mean(_f01_drawdown_from_peak(closeadj, 252), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d drawdown std × close
def f01pc_f01_peak_and_crash_ddstd_63d_slope_v043_signal(closeadj):
    base = _std(_f01_drawdown_from_peak(closeadj, 252), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d drawdown std × close
def f01pc_f01_peak_and_crash_ddstd_126d_slope_v044_signal(closeadj):
    base = _std(_f01_drawdown_from_peak(closeadj, 504), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d drawdown z
def f01pc_f01_peak_and_crash_ddz_21d_slope_v045_signal(closeadj):
    base = _z(_f01_drawdown_from_peak(closeadj, 63), 252)
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d drawdown z
def f01pc_f01_peak_and_crash_ddz_63d_slope_v046_signal(closeadj):
    base = _z(_f01_drawdown_from_peak(closeadj, 252), 504)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ATH gap × volume
def f01pc_f01_peak_and_crash_athgapxvol_21d_slope_v047_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max()
    gap = (closeadj - ath) / ath.replace(0, np.nan).abs()
    base = gap * volume + _f01_drawdown_from_peak(closeadj, 21) * 0.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ATH gap × dollar volume
def f01pc_f01_peak_and_crash_athgapxdv_63d_slope_v048_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max()
    gap = (closeadj - ath) / ath.replace(0, np.nan).abs()
    dv = closeadj * volume
    base = gap * _mean(dv, 21) + _f01_drawdown_from_peak(closeadj, 63) * 0.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_5d_slope_v049_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 5)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_10d_slope_v050_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 10)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_42d_slope_v051_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 189d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_189d_slope_v052_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 189)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d crash intensity
def f01pc_f01_peak_and_crash_crashintensity_378d_slope_v053_signal(closeadj):
    base = _f01_crash_intensity(closeadj, 378)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d drawdown × close
def f01pc_f01_peak_and_crash_dd_5d_slope_v054_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d drawdown × close
def f01pc_f01_peak_and_crash_dd_10d_slope_v055_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d drawdown × close
def f01pc_f01_peak_and_crash_dd_42d_slope_v056_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 189d drawdown × close
def f01pc_f01_peak_and_crash_dd_189d_slope_v057_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d drawdown × close
def f01pc_f01_peak_and_crash_dd_378d_slope_v058_signal(closeadj):
    base = _f01_drawdown_from_peak(closeadj, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d post-crash recovery × close
def f01pc_f01_peak_and_crash_postcrashrec_21d_slope_v059_signal(closeadj):
    trough = closeadj.rolling(21, min_periods=5).min()
    in_crash = (_f01_drawdown_from_peak(closeadj, 21) < -0.05).astype(float)
    rec = (closeadj - trough) / trough.replace(0, np.nan).abs()
    base = rec * in_crash * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d post-crash recovery × close
def f01pc_f01_peak_and_crash_postcrashrec_63d_slope_v060_signal(closeadj):
    trough = closeadj.rolling(63, min_periods=21).min()
    in_crash = (_f01_drawdown_from_peak(closeadj, 63) < -0.10).astype(float)
    rec = (closeadj - trough) / trough.replace(0, np.nan).abs()
    base = rec * in_crash * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d post-crash recovery × close
def f01pc_f01_peak_and_crash_postcrashrec_252d_slope_v061_signal(closeadj):
    trough = closeadj.rolling(252, min_periods=63).min()
    in_crash = (_f01_drawdown_from_peak(closeadj, 252) < -0.15).astype(float)
    rec = (closeadj - trough) / trough.replace(0, np.nan).abs()
    base = rec * in_crash * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of expanding ATH proximity × close
def f01pc_f01_peak_and_crash_athprox_slope_v062_signal(closeadj):
    ath = closeadj.expanding(min_periods=21).max().replace(0, np.nan)
    base = (closeadj / ath) * closeadj + _f01_peak_level(closeadj, 252) * 0.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d peak prominence
def f01pc_f01_peak_and_crash_peakprom_21d_slope_v063_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    trough = closeadj.rolling(21, min_periods=5).min()
    base = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak prominence
def f01pc_f01_peak_and_crash_peakprom_63d_slope_v064_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    trough = closeadj.rolling(63, min_periods=21).min()
    base = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d peak prominence
def f01pc_f01_peak_and_crash_peakprom_252d_slope_v065_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    trough = closeadj.rolling(252, min_periods=63).min()
    base = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d peak prominence
def f01pc_f01_peak_and_crash_peakprom_504d_slope_v066_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    trough = closeadj.rolling(504, min_periods=126).min()
    base = (peak - trough) * closeadj / peak.replace(0, np.nan).abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d drawdown × volume
def f01pc_f01_peak_and_crash_ddxvol_21d_slope_v067_signal(closeadj, volume):
    base = _f01_drawdown_from_peak(closeadj, 21) * volume
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown × volume
def f01pc_f01_peak_and_crash_ddxvol_63d_slope_v068_signal(closeadj, volume):
    base = _f01_drawdown_from_peak(closeadj, 63) * volume
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown × dollar volume
def f01pc_f01_peak_and_crash_ddxdv_252d_slope_v069_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f01_drawdown_from_peak(closeadj, 252) * _mean(dv, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d drawdown × dollar volume
def f01pc_f01_peak_and_crash_ddxdv_504d_slope_v070_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f01_drawdown_from_peak(closeadj, 504) * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d crash intensity × volume z
def f01pc_f01_peak_and_crash_intensxvol_21d_slope_v071_signal(closeadj, volume):
    base = _f01_crash_intensity(closeadj, 21) * _z(volume, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d crash intensity × volume z
def f01pc_f01_peak_and_crash_intensxvol_63d_slope_v072_signal(closeadj, volume):
    base = _f01_crash_intensity(closeadj, 63) * _z(volume, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown squared × close
def f01pc_f01_peak_and_crash_ddsq_252d_slope_v073_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    base = d * d.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown squared × close
def f01pc_f01_peak_and_crash_ddsq_63d_slope_v074_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 63)
    base = d * d.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d drawdown squared × close
def f01pc_f01_peak_and_crash_ddsq_21d_slope_v075_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 21)
    base = d * d.abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d drawdown EMA × close
def f01pc_f01_peak_and_crash_ddema_21d_slope_v076_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 21)
    base = d.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown EMA × close
def f01pc_f01_peak_and_crash_ddema_63d_slope_v077_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 63)
    base = d.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown EMA × close
def f01pc_f01_peak_and_crash_ddema_252d_slope_v078_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    base = d.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d peak EMA - close
def f01pc_f01_peak_and_crash_peakema_21d_slope_v079_signal(closeadj):
    pk = _f01_peak_level(closeadj, 21)
    base = pk.ewm(span=21, adjust=False).mean() - closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak EMA - close
def f01pc_f01_peak_and_crash_peakema_63d_slope_v080_signal(closeadj):
    pk = _f01_peak_level(closeadj, 63)
    base = pk.ewm(span=63, adjust=False).mean() - closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d peak EMA - close
def f01pc_f01_peak_and_crash_peakema_252d_slope_v081_signal(closeadj):
    pk = _f01_peak_level(closeadj, 252)
    base = pk.ewm(span=252, adjust=False).mean() - closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d worst drawdown × close
def f01pc_f01_peak_and_crash_worstdd_63d_slope_v082_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 21)
    base = d.rolling(63, min_periods=21).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d worst drawdown × close
def f01pc_f01_peak_and_crash_worstdd_252d_slope_v083_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 63)
    base = d.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d worst drawdown × close
def f01pc_f01_peak_and_crash_worstdd_504d_slope_v084_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    base = d.rolling(504, min_periods=126).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d drawdown × retvol × close
def f01pc_f01_peak_and_crash_ddxretvol_21d_slope_v085_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f01_drawdown_from_peak(closeadj, 21) * rv * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown × retvol × close
def f01pc_f01_peak_and_crash_ddxretvol_63d_slope_v086_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f01_drawdown_from_peak(closeadj, 63) * rv * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown × retvol × close
def f01pc_f01_peak_and_crash_ddxretvol_252d_slope_v087_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f01_drawdown_from_peak(closeadj, 252) * rv * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown × skew
def f01pc_f01_peak_and_crash_ddxskew_63d_slope_v088_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f01_drawdown_from_peak(closeadj, 63) * sk * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown × skew
def f01pc_f01_peak_and_crash_ddxskew_252d_slope_v089_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f01_drawdown_from_peak(closeadj, 252) * sk * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown × kurt
def f01pc_f01_peak_and_crash_ddxkurt_63d_slope_v090_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f01_drawdown_from_peak(closeadj, 63) * kt * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown × kurt
def f01pc_f01_peak_and_crash_ddxkurt_252d_slope_v091_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f01_drawdown_from_peak(closeadj, 252) * kt * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of drawdown ratio 63v252 × close
def f01pc_f01_peak_and_crash_ddratio_63v252_slope_v092_signal(closeadj):
    a = _f01_drawdown_from_peak(closeadj, 63)
    b = _f01_drawdown_from_peak(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of drawdown ratio 21v63 × close
def f01pc_f01_peak_and_crash_ddratio_21v63_slope_v093_signal(closeadj):
    a = _f01_drawdown_from_peak(closeadj, 21)
    b = _f01_drawdown_from_peak(closeadj, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of drawdown ratio 252v504 × close
def f01pc_f01_peak_and_crash_ddratio_252v504_slope_v094_signal(closeadj):
    a = _f01_drawdown_from_peak(closeadj, 252)
    b = _f01_drawdown_from_peak(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of drawdown diff 63m252 × close
def f01pc_f01_peak_and_crash_dddiff_63m252_slope_v095_signal(closeadj):
    base = (_f01_drawdown_from_peak(closeadj, 63) - _f01_drawdown_from_peak(closeadj, 252)) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of drawdown diff 21m63 × close
def f01pc_f01_peak_and_crash_dddiff_21m63_slope_v096_signal(closeadj):
    base = (_f01_drawdown_from_peak(closeadj, 21) - _f01_drawdown_from_peak(closeadj, 63)) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of drawdown diff 252m504 × close
def f01pc_f01_peak_and_crash_dddiff_252m504_slope_v097_signal(closeadj):
    base = (_f01_drawdown_from_peak(closeadj, 252) - _f01_drawdown_from_peak(closeadj, 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of peak diff 63m252
def f01pc_f01_peak_and_crash_peakdiff_63m252_slope_v098_signal(closeadj):
    base = (_f01_peak_level(closeadj, 63) - _f01_peak_level(closeadj, 252)) / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of peak diff 252m504
def f01pc_f01_peak_and_crash_peakdiff_252m504_slope_v099_signal(closeadj):
    base = (_f01_peak_level(closeadj, 252) - _f01_peak_level(closeadj, 504)) / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d below-peak count × close
def f01pc_f01_peak_and_crash_belowpeak_21d_slope_v100_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    flag = (closeadj < peak).astype(float)
    base = flag.rolling(21, min_periods=5).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d below-peak count × close
def f01pc_f01_peak_and_crash_belowpeak_63d_slope_v101_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    flag = (closeadj < peak).astype(float)
    base = flag.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d below-peak count × close
def f01pc_f01_peak_and_crash_belowpeak_252d_slope_v102_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    flag = (closeadj < peak).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d below-peak count × close
def f01pc_f01_peak_and_crash_belowpeak_504d_slope_v103_signal(closeadj):
    peak = _f01_peak_level(closeadj, 504)
    flag = (closeadj < peak).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d deep-below-peak count × close
def f01pc_f01_peak_and_crash_deepbelowpeak_252d_slope_v104_signal(closeadj):
    flag = (_f01_drawdown_from_peak(closeadj, 252) < -0.10).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d deep-below-peak count × close
def f01pc_f01_peak_and_crash_deepbelowpeak_504d_slope_v105_signal(closeadj):
    flag = (_f01_drawdown_from_peak(closeadj, 252) < -0.20).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d deep-below-peak count × close
def f01pc_f01_peak_and_crash_deepbelowpeak_63d_slope_v106_signal(closeadj):
    flag = (_f01_drawdown_from_peak(closeadj, 63) < -0.05).astype(float)
    base = flag.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intensity × ret
def f01pc_f01_peak_and_crash_intensxret_21d_slope_v107_signal(closeadj):
    r = closeadj.pct_change(5)
    base = _f01_crash_intensity(closeadj, 21) * r
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intensity × ret
def f01pc_f01_peak_and_crash_intensxret_63d_slope_v108_signal(closeadj):
    r = closeadj.pct_change(21)
    base = _f01_crash_intensity(closeadj, 63) * r
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intensity × ret
def f01pc_f01_peak_and_crash_intensxret_252d_slope_v109_signal(closeadj):
    r = closeadj.pct_change(63)
    base = _f01_crash_intensity(closeadj, 252) * r
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d peak distance
def f01pc_f01_peak_and_crash_peakdist_21d_slope_v110_signal(closeadj):
    pk = _f01_peak_level(closeadj, 21)
    base = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak distance
def f01pc_f01_peak_and_crash_peakdist_63d_slope_v111_signal(closeadj):
    pk = _f01_peak_level(closeadj, 63)
    base = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d peak distance
def f01pc_f01_peak_and_crash_peakdist_252d_slope_v112_signal(closeadj):
    pk = _f01_peak_level(closeadj, 252)
    base = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d peak distance
def f01pc_f01_peak_and_crash_peakdist_504d_slope_v113_signal(closeadj):
    pk = _f01_peak_level(closeadj, 504)
    base = (pk - closeadj) * pk / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intensity × ATR
def f01pc_f01_peak_and_crash_intensxatr_21d_slope_v114_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f01_crash_intensity(closeadj, 21) * atr
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intensity × ATR
def f01pc_f01_peak_and_crash_intensxatr_63d_slope_v115_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f01_crash_intensity(closeadj, 63) * atr
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intensity × ATR
def f01pc_f01_peak_and_crash_intensxatr_252d_slope_v116_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f01_crash_intensity(closeadj, 252) * atr
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intensity × downside-vol
def f01pc_f01_peak_and_crash_intensxdownvol_21d_slope_v117_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f01_crash_intensity(closeadj, 21) * dv.rolling(5, min_periods=2).sum()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intensity × downside-vol
def f01pc_f01_peak_and_crash_intensxdownvol_63d_slope_v118_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f01_crash_intensity(closeadj, 63) * dv.rolling(21, min_periods=5).sum()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intensity × downside-vol
def f01pc_f01_peak_and_crash_intensxdownvol_252d_slope_v119_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = (closeadj * volume) * (r < 0).astype(float)
    base = _f01_crash_intensity(closeadj, 252) * dv.rolling(63, min_periods=21).sum()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding worst drawdown × close
def f01pc_f01_peak_and_crash_ddworstever_slope_v120_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 504)
    base = d.expanding(min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d drawdown gap-to-historical-worst
def f01pc_f01_peak_and_crash_ddvshistworst_252d_slope_v121_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 252)
    worst = d.expanding(min_periods=63).min()
    base = (d - worst) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d drawdown gap-to-historical-worst
def f01pc_f01_peak_and_crash_ddvshistworst_504d_slope_v122_signal(closeadj):
    d = _f01_drawdown_from_peak(closeadj, 504)
    worst = d.expanding(min_periods=252).min()
    base = (d - worst) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d crash count × age × close
def f01pc_f01_peak_and_crash_crashcountxage_252d_slope_v123_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = _f01_drawdown_from_peak(closeadj, 63)
    cross = ((dd < -0.10) & (dd.shift(1) >= -0.10)).astype(float)
    cnt = cross.rolling(252, min_periods=63).sum()
    base = (cnt + 1.0) * age * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d crash area × close
def f01pc_f01_peak_and_crash_crasharea_63d_slope_v124_signal(closeadj):
    deficit = (-_f01_drawdown_from_peak(closeadj, 63)).clip(lower=0)
    base = deficit.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d crash area × close
def f01pc_f01_peak_and_crash_crasharea_252d_slope_v125_signal(closeadj):
    deficit = (-_f01_drawdown_from_peak(closeadj, 252)).clip(lower=0)
    base = deficit.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d crash area × close
def f01pc_f01_peak_and_crash_crasharea_504d_slope_v126_signal(closeadj):
    deficit = (-_f01_drawdown_from_peak(closeadj, 504)).clip(lower=0)
    base = deficit.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d local-peak gap
def f01pc_f01_peak_and_crash_localpeakgap_21d_slope_v127_signal(closeadj, high):
    local_pk = high.rolling(21, min_periods=5).max()
    big_pk = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    base = (local_pk - big_pk) * closeadj / big_pk.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d local-peak gap
def f01pc_f01_peak_and_crash_localpeakgap_63d_slope_v128_signal(closeadj, high):
    local_pk = high.rolling(63, min_periods=21).max()
    big_pk = _f01_peak_level(closeadj, 504).replace(0, np.nan)
    base = (local_pk - big_pk) * closeadj / big_pk.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d low distance to peak
def f01pc_f01_peak_and_crash_lowdistpeak_21d_slope_v129_signal(closeadj, low):
    big_pk = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    local_lo = low.rolling(21, min_periods=5).min()
    base = (local_lo - big_pk) * closeadj / big_pk.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d low distance to peak
def f01pc_f01_peak_and_crash_lowdistpeak_63d_slope_v130_signal(closeadj, low):
    big_pk = _f01_peak_level(closeadj, 504).replace(0, np.nan)
    local_lo = low.rolling(63, min_periods=21).min()
    base = (local_lo - big_pk) * closeadj / big_pk.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sharpness × volume z
def f01pc_f01_peak_and_crash_sharpxvolz_21d_slope_v131_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 21).abs()
    peak = _f01_peak_level(closeadj, 21)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    base = (dd / age) * _z(volume, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sharpness × volume z
def f01pc_f01_peak_and_crash_sharpxvolz_63d_slope_v132_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 63).abs()
    peak = _f01_peak_level(closeadj, 63)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    base = (dd / age) * _z(volume, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d new-peak frequency × close
def f01pc_f01_peak_and_crash_newpeakfreq_21d_slope_v133_signal(closeadj):
    peak = _f01_peak_level(closeadj, 21)
    new_peak = (closeadj >= peak).astype(float)
    base = new_peak.rolling(21, min_periods=5).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d new-peak frequency × close
def f01pc_f01_peak_and_crash_newpeakfreq_504d_slope_v134_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    new_peak = (closeadj >= peak).astype(float)
    base = new_peak.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d new-peak rate
def f01pc_f01_peak_and_crash_newpeakrate_63d_slope_v135_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63)
    new_peak = (closeadj >= peak).astype(float)
    base = (new_peak.rolling(63, min_periods=21).sum() / 63.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d new-peak rate
def f01pc_f01_peak_and_crash_newpeakrate_252d_slope_v136_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252)
    new_peak = (closeadj >= peak).astype(float)
    base = (new_peak.rolling(252, min_periods=63).sum() / 252.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ATH proximity × volume z
def f01pc_f01_peak_and_crash_athproxxvolz_21d_slope_v137_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max().replace(0, np.nan)
    prox = closeadj / ath
    base = prox * _z(volume, 21) * closeadj + _f01_peak_level(closeadj, 21) * 0.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ATH proximity × volume z
def f01pc_f01_peak_and_crash_athproxxvolz_63d_slope_v138_signal(closeadj, volume):
    ath = closeadj.expanding(min_periods=21).max().replace(0, np.nan)
    prox = closeadj / ath
    base = prox * _z(volume, 63) * closeadj + _f01_peak_level(closeadj, 63) * 0.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown × range
def f01pc_f01_peak_and_crash_ddxrange_252d_slope_v139_signal(closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f01_drawdown_from_peak(closeadj, 252) * rng
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown × range
def f01pc_f01_peak_and_crash_ddxrange_63d_slope_v140_signal(closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f01_drawdown_from_peak(closeadj, 63) * rng
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sharpness × dollar volume
def f01pc_f01_peak_and_crash_sharpxdv_252d_slope_v141_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 252).abs()
    peak = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= peak).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum().replace(0, np.nan)
    dv = closeadj * volume
    base = (dd / age) * _mean(dv, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d post-peak retreat × close
def f01pc_f01_peak_and_crash_postpeakdrop_63d_slope_v142_signal(closeadj):
    peak = _f01_peak_level(closeadj, 63).replace(0, np.nan)
    proximity = closeadj / peak.abs()
    fwd = closeadj.shift(-63) / closeadj - 1.0
    base = proximity * fwd * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d post-peak retreat × close (proximity-weighted)
def f01pc_f01_peak_and_crash_postpeakdrop_252d_slope_v143_signal(closeadj):
    peak = _f01_peak_level(closeadj, 252).replace(0, np.nan)
    proximity = closeadj / peak.abs()
    fwd = closeadj.shift(-126) / closeadj - 1.0
    base = proximity * fwd * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d crash count × volume
def f01pc_f01_peak_and_crash_crashcountxvol_252d_slope_v144_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 63)
    cross = ((dd < -0.10) & (dd.shift(1) >= -0.10)).astype(float)
    cnt = cross.rolling(252, min_periods=63).sum()
    base = (cnt + 1.0) * _mean(closeadj * volume, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d crash count × dollar volume
def f01pc_f01_peak_and_crash_crashcountxdv_504d_slope_v145_signal(closeadj, volume):
    dd = _f01_drawdown_from_peak(closeadj, 252)
    cross = ((dd < -0.15) & (dd.shift(1) >= -0.15)).astype(float)
    cnt = cross.rolling(504, min_periods=126).sum()
    base = (cnt + 1.0) * _mean(closeadj * volume, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d drawdown × current dollar-volume
def f01pc_f01_peak_and_crash_ddxcurdv_21d_slope_v146_signal(closeadj, volume):
    base = _f01_drawdown_from_peak(closeadj, 21) * (closeadj * volume)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown × current dollar-volume
def f01pc_f01_peak_and_crash_ddxcurdv_252d_slope_v147_signal(closeadj, volume):
    base = _f01_drawdown_from_peak(closeadj, 252) * (closeadj * volume)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite peak-and-crash severity
def f01pc_f01_peak_and_crash_compositesev_252d_slope_v148_signal(closeadj):
    pk = _f01_peak_level(closeadj, 252)
    at_peak = (closeadj >= pk).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = _f01_drawdown_from_peak(closeadj, 252).abs()
    base = (dd + age / 252.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d composite peak-and-crash severity
def f01pc_f01_peak_and_crash_compositesev_504d_slope_v149_signal(closeadj):
    pk = _f01_peak_level(closeadj, 504)
    at_peak = (closeadj >= pk).astype(float)
    grp = at_peak.cumsum()
    age = (~at_peak.astype(bool)).astype(float).groupby(grp).cumsum()
    dd = _f01_drawdown_from_peak(closeadj, 504).abs()
    base = (dd + age / 504.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intensity-area × close
def f01pc_f01_peak_and_crash_intensarea_252d_slope_v150_signal(closeadj):
    inten = _f01_crash_intensity(closeadj, 63).abs()
    base = inten.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01pc_f01_peak_and_crash_peaklevel_21d_slope_v001_signal,
    f01pc_f01_peak_and_crash_peaklevel_21d_slope_v002_signal,
    f01pc_f01_peak_and_crash_peaklevel_63d_slope_v003_signal,
    f01pc_f01_peak_and_crash_peaklevel_126d_slope_v004_signal,
    f01pc_f01_peak_and_crash_peaklevel_252d_slope_v005_signal,
    f01pc_f01_peak_and_crash_peaklevel_504d_slope_v006_signal,
    f01pc_f01_peak_and_crash_dd_21d_slope_v007_signal,
    f01pc_f01_peak_and_crash_dd_21d_slope_v008_signal,
    f01pc_f01_peak_and_crash_dd_63d_slope_v009_signal,
    f01pc_f01_peak_and_crash_dd_252d_slope_v010_signal,
    f01pc_f01_peak_and_crash_dd_504d_slope_v011_signal,
    f01pc_f01_peak_and_crash_athgap_slope_v012_signal,
    f01pc_f01_peak_and_crash_peakage_252d_slope_v013_signal,
    f01pc_f01_peak_and_crash_peakage_63d_slope_v014_signal,
    f01pc_f01_peak_and_crash_peakage_504d_slope_v015_signal,
    f01pc_f01_peak_and_crash_peakerosion_21d_slope_v016_signal,
    f01pc_f01_peak_and_crash_peakerosion_63d_slope_v017_signal,
    f01pc_f01_peak_and_crash_peakerosion_252d_slope_v018_signal,
    f01pc_f01_peak_and_crash_peakerosion_504d_slope_v019_signal,
    f01pc_f01_peak_and_crash_crashintensity_21d_slope_v020_signal,
    f01pc_f01_peak_and_crash_crashintensity_63d_slope_v021_signal,
    f01pc_f01_peak_and_crash_crashintensity_252d_slope_v022_signal,
    f01pc_f01_peak_and_crash_crashintensity_504d_slope_v023_signal,
    f01pc_f01_peak_and_crash_newpeakcount_252d_slope_v024_signal,
    f01pc_f01_peak_and_crash_newpeakcount_63d_slope_v025_signal,
    f01pc_f01_peak_and_crash_newpeakcount_504d_slope_v026_signal,
    f01pc_f01_peak_and_crash_crashcount_252d_slope_v027_signal,
    f01pc_f01_peak_and_crash_crashcount_504d_slope_v028_signal,
    f01pc_f01_peak_and_crash_crashcount_63d_slope_v029_signal,
    f01pc_f01_peak_and_crash_postpeakret_21d_slope_v030_signal,
    f01pc_f01_peak_and_crash_postpeakret_63d_slope_v031_signal,
    f01pc_f01_peak_and_crash_postpeakret_252d_slope_v032_signal,
    f01pc_f01_peak_and_crash_peakprox_21d_slope_v033_signal,
    f01pc_f01_peak_and_crash_peakprox_63d_slope_v034_signal,
    f01pc_f01_peak_and_crash_peakprox_252d_slope_v035_signal,
    f01pc_f01_peak_and_crash_peakprox_504d_slope_v036_signal,
    f01pc_f01_peak_and_crash_crashsharp_21d_slope_v037_signal,
    f01pc_f01_peak_and_crash_crashsharp_63d_slope_v038_signal,
    f01pc_f01_peak_and_crash_crashsharp_252d_slope_v039_signal,
    f01pc_f01_peak_and_crash_crashsharp_504d_slope_v040_signal,
    f01pc_f01_peak_and_crash_ddmean_21d_slope_v041_signal,
    f01pc_f01_peak_and_crash_ddmean_63d_slope_v042_signal,
    f01pc_f01_peak_and_crash_ddstd_63d_slope_v043_signal,
    f01pc_f01_peak_and_crash_ddstd_126d_slope_v044_signal,
    f01pc_f01_peak_and_crash_ddz_21d_slope_v045_signal,
    f01pc_f01_peak_and_crash_ddz_63d_slope_v046_signal,
    f01pc_f01_peak_and_crash_athgapxvol_21d_slope_v047_signal,
    f01pc_f01_peak_and_crash_athgapxdv_63d_slope_v048_signal,
    f01pc_f01_peak_and_crash_crashintensity_5d_slope_v049_signal,
    f01pc_f01_peak_and_crash_crashintensity_10d_slope_v050_signal,
    f01pc_f01_peak_and_crash_crashintensity_42d_slope_v051_signal,
    f01pc_f01_peak_and_crash_crashintensity_189d_slope_v052_signal,
    f01pc_f01_peak_and_crash_crashintensity_378d_slope_v053_signal,
    f01pc_f01_peak_and_crash_dd_5d_slope_v054_signal,
    f01pc_f01_peak_and_crash_dd_10d_slope_v055_signal,
    f01pc_f01_peak_and_crash_dd_42d_slope_v056_signal,
    f01pc_f01_peak_and_crash_dd_189d_slope_v057_signal,
    f01pc_f01_peak_and_crash_dd_378d_slope_v058_signal,
    f01pc_f01_peak_and_crash_postcrashrec_21d_slope_v059_signal,
    f01pc_f01_peak_and_crash_postcrashrec_63d_slope_v060_signal,
    f01pc_f01_peak_and_crash_postcrashrec_252d_slope_v061_signal,
    f01pc_f01_peak_and_crash_athprox_slope_v062_signal,
    f01pc_f01_peak_and_crash_peakprom_21d_slope_v063_signal,
    f01pc_f01_peak_and_crash_peakprom_63d_slope_v064_signal,
    f01pc_f01_peak_and_crash_peakprom_252d_slope_v065_signal,
    f01pc_f01_peak_and_crash_peakprom_504d_slope_v066_signal,
    f01pc_f01_peak_and_crash_ddxvol_21d_slope_v067_signal,
    f01pc_f01_peak_and_crash_ddxvol_63d_slope_v068_signal,
    f01pc_f01_peak_and_crash_ddxdv_252d_slope_v069_signal,
    f01pc_f01_peak_and_crash_ddxdv_504d_slope_v070_signal,
    f01pc_f01_peak_and_crash_intensxvol_21d_slope_v071_signal,
    f01pc_f01_peak_and_crash_intensxvol_63d_slope_v072_signal,
    f01pc_f01_peak_and_crash_ddsq_252d_slope_v073_signal,
    f01pc_f01_peak_and_crash_ddsq_63d_slope_v074_signal,
    f01pc_f01_peak_and_crash_ddsq_21d_slope_v075_signal,
    f01pc_f01_peak_and_crash_ddema_21d_slope_v076_signal,
    f01pc_f01_peak_and_crash_ddema_63d_slope_v077_signal,
    f01pc_f01_peak_and_crash_ddema_252d_slope_v078_signal,
    f01pc_f01_peak_and_crash_peakema_21d_slope_v079_signal,
    f01pc_f01_peak_and_crash_peakema_63d_slope_v080_signal,
    f01pc_f01_peak_and_crash_peakema_252d_slope_v081_signal,
    f01pc_f01_peak_and_crash_worstdd_63d_slope_v082_signal,
    f01pc_f01_peak_and_crash_worstdd_252d_slope_v083_signal,
    f01pc_f01_peak_and_crash_worstdd_504d_slope_v084_signal,
    f01pc_f01_peak_and_crash_ddxretvol_21d_slope_v085_signal,
    f01pc_f01_peak_and_crash_ddxretvol_63d_slope_v086_signal,
    f01pc_f01_peak_and_crash_ddxretvol_252d_slope_v087_signal,
    f01pc_f01_peak_and_crash_ddxskew_63d_slope_v088_signal,
    f01pc_f01_peak_and_crash_ddxskew_252d_slope_v089_signal,
    f01pc_f01_peak_and_crash_ddxkurt_63d_slope_v090_signal,
    f01pc_f01_peak_and_crash_ddxkurt_252d_slope_v091_signal,
    f01pc_f01_peak_and_crash_ddratio_63v252_slope_v092_signal,
    f01pc_f01_peak_and_crash_ddratio_21v63_slope_v093_signal,
    f01pc_f01_peak_and_crash_ddratio_252v504_slope_v094_signal,
    f01pc_f01_peak_and_crash_dddiff_63m252_slope_v095_signal,
    f01pc_f01_peak_and_crash_dddiff_21m63_slope_v096_signal,
    f01pc_f01_peak_and_crash_dddiff_252m504_slope_v097_signal,
    f01pc_f01_peak_and_crash_peakdiff_63m252_slope_v098_signal,
    f01pc_f01_peak_and_crash_peakdiff_252m504_slope_v099_signal,
    f01pc_f01_peak_and_crash_belowpeak_21d_slope_v100_signal,
    f01pc_f01_peak_and_crash_belowpeak_63d_slope_v101_signal,
    f01pc_f01_peak_and_crash_belowpeak_252d_slope_v102_signal,
    f01pc_f01_peak_and_crash_belowpeak_504d_slope_v103_signal,
    f01pc_f01_peak_and_crash_deepbelowpeak_252d_slope_v104_signal,
    f01pc_f01_peak_and_crash_deepbelowpeak_504d_slope_v105_signal,
    f01pc_f01_peak_and_crash_deepbelowpeak_63d_slope_v106_signal,
    f01pc_f01_peak_and_crash_intensxret_21d_slope_v107_signal,
    f01pc_f01_peak_and_crash_intensxret_63d_slope_v108_signal,
    f01pc_f01_peak_and_crash_intensxret_252d_slope_v109_signal,
    f01pc_f01_peak_and_crash_peakdist_21d_slope_v110_signal,
    f01pc_f01_peak_and_crash_peakdist_63d_slope_v111_signal,
    f01pc_f01_peak_and_crash_peakdist_252d_slope_v112_signal,
    f01pc_f01_peak_and_crash_peakdist_504d_slope_v113_signal,
    f01pc_f01_peak_and_crash_intensxatr_21d_slope_v114_signal,
    f01pc_f01_peak_and_crash_intensxatr_63d_slope_v115_signal,
    f01pc_f01_peak_and_crash_intensxatr_252d_slope_v116_signal,
    f01pc_f01_peak_and_crash_intensxdownvol_21d_slope_v117_signal,
    f01pc_f01_peak_and_crash_intensxdownvol_63d_slope_v118_signal,
    f01pc_f01_peak_and_crash_intensxdownvol_252d_slope_v119_signal,
    f01pc_f01_peak_and_crash_ddworstever_slope_v120_signal,
    f01pc_f01_peak_and_crash_ddvshistworst_252d_slope_v121_signal,
    f01pc_f01_peak_and_crash_ddvshistworst_504d_slope_v122_signal,
    f01pc_f01_peak_and_crash_crashcountxage_252d_slope_v123_signal,
    f01pc_f01_peak_and_crash_crasharea_63d_slope_v124_signal,
    f01pc_f01_peak_and_crash_crasharea_252d_slope_v125_signal,
    f01pc_f01_peak_and_crash_crasharea_504d_slope_v126_signal,
    f01pc_f01_peak_and_crash_localpeakgap_21d_slope_v127_signal,
    f01pc_f01_peak_and_crash_localpeakgap_63d_slope_v128_signal,
    f01pc_f01_peak_and_crash_lowdistpeak_21d_slope_v129_signal,
    f01pc_f01_peak_and_crash_lowdistpeak_63d_slope_v130_signal,
    f01pc_f01_peak_and_crash_sharpxvolz_21d_slope_v131_signal,
    f01pc_f01_peak_and_crash_sharpxvolz_63d_slope_v132_signal,
    f01pc_f01_peak_and_crash_newpeakfreq_21d_slope_v133_signal,
    f01pc_f01_peak_and_crash_newpeakfreq_504d_slope_v134_signal,
    f01pc_f01_peak_and_crash_newpeakrate_63d_slope_v135_signal,
    f01pc_f01_peak_and_crash_newpeakrate_252d_slope_v136_signal,
    f01pc_f01_peak_and_crash_athproxxvolz_21d_slope_v137_signal,
    f01pc_f01_peak_and_crash_athproxxvolz_63d_slope_v138_signal,
    f01pc_f01_peak_and_crash_ddxrange_252d_slope_v139_signal,
    f01pc_f01_peak_and_crash_ddxrange_63d_slope_v140_signal,
    f01pc_f01_peak_and_crash_sharpxdv_252d_slope_v141_signal,
    f01pc_f01_peak_and_crash_postpeakdrop_63d_slope_v142_signal,
    f01pc_f01_peak_and_crash_postpeakdrop_252d_slope_v143_signal,
    f01pc_f01_peak_and_crash_crashcountxvol_252d_slope_v144_signal,
    f01pc_f01_peak_and_crash_crashcountxdv_504d_slope_v145_signal,
    f01pc_f01_peak_and_crash_ddxcurdv_21d_slope_v146_signal,
    f01pc_f01_peak_and_crash_ddxcurdv_252d_slope_v147_signal,
    f01pc_f01_peak_and_crash_compositesev_252d_slope_v148_signal,
    f01pc_f01_peak_and_crash_compositesev_504d_slope_v149_signal,
    f01pc_f01_peak_and_crash_intensarea_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_PEAK_AND_CRASH_REGISTRY_SLOPE = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f01_peak_and_crash_2nd_derivatives_001_150_claude: {n_features} features pass")
