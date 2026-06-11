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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    denom = s.shift(w).abs().replace(0, np.nan)
    return s.diff(periods=w) / denom


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives (f12 long_cycle_visibility) =====
def _f12_multi_year_growth(revenue, w):
    sm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return sm.pct_change(periods=w)


def _f12_smoothed_visibility(revenue, w):
    sm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sm / (sd.replace(0, np.nan) + sm * 0.01)


def _f12_growth_persistence(revenue, w):
    g = revenue.pct_change(periods=max(1, w // 4))
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def lcv_f12_long_cycle_visibility_myg_5d_mean10_closeadj_jerk5_v001_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean10_closeadj_jerk5_v002_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean10_closeadj_jerk5_v003_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean21_closeadj_jerk5_v004_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean21_closeadj_jerk5_v005_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean21_closeadj_jerk5_v006_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean42_closeadj_jerk5_v007_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean42_closeadj_jerk5_v008_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean42_closeadj_jerk5_v009_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean63_closeadj_jerk5_v010_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean63_closeadj_jerk5_v011_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean63_closeadj_jerk5_v012_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean126_closeadj_jerk5_v013_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean126_closeadj_jerk5_v014_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean126_closeadj_jerk5_v015_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean10_closeadj_jerk5_v016_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean10_closeadj_jerk5_v017_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean10_closeadj_jerk5_v018_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean21_closeadj_jerk5_v019_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean21_closeadj_jerk5_v020_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean21_closeadj_jerk5_v021_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean42_closeadj_jerk5_v022_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean42_closeadj_jerk5_v023_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean42_closeadj_jerk5_v024_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean63_closeadj_jerk5_v025_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean63_closeadj_jerk5_v026_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean63_closeadj_jerk5_v027_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean126_closeadj_jerk5_v028_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean126_closeadj_jerk5_v029_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean126_closeadj_jerk5_v030_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean10_closeadj_jerk5_v031_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean10_closeadj_jerk5_v032_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean10_closeadj_jerk5_v033_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean21_closeadj_jerk5_v034_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean21_closeadj_jerk5_v035_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean21_closeadj_jerk5_v036_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean42_closeadj_jerk5_v037_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean42_closeadj_jerk5_v038_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean42_closeadj_jerk5_v039_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean63_closeadj_jerk5_v040_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean63_closeadj_jerk5_v041_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean63_closeadj_jerk5_v042_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean126_closeadj_jerk5_v043_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean126_closeadj_jerk5_v044_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean126_closeadj_jerk5_v045_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_42d_mean10_closeadj_jerk5_v046_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 42)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_42d_mean10_closeadj_jerk5_v047_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 42)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_42d_mean10_closeadj_jerk5_v048_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 42)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_42d_mean21_closeadj_jerk5_v049_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 42)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_42d_mean21_closeadj_jerk5_v050_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 42)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_42d_mean21_closeadj_jerk5_v051_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 42)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_42d_mean42_closeadj_jerk5_v052_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 42)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_42d_mean42_closeadj_jerk5_v053_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 42)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_42d_mean42_closeadj_jerk5_v054_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 42)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_42d_mean63_closeadj_jerk5_v055_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 42)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_42d_mean63_closeadj_jerk5_v056_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 42)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_42d_mean63_closeadj_jerk5_v057_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 42)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_42d_mean126_closeadj_jerk5_v058_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 42)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_42d_mean126_closeadj_jerk5_v059_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 42)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_42d_mean126_closeadj_jerk5_v060_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 42)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_63d_mean10_closeadj_jerk5_v061_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 63)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_63d_mean10_closeadj_jerk5_v062_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 63)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_63d_mean10_closeadj_jerk5_v063_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 63)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_63d_mean21_closeadj_jerk5_v064_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 63)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_63d_mean21_closeadj_jerk5_v065_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 63)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_63d_mean21_closeadj_jerk5_v066_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 63)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_63d_mean42_closeadj_jerk5_v067_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 63)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_63d_mean42_closeadj_jerk5_v068_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 63)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_63d_mean42_closeadj_jerk5_v069_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 63)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_63d_mean63_closeadj_jerk5_v070_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 63)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_63d_mean63_closeadj_jerk5_v071_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 63)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_63d_mean63_closeadj_jerk5_v072_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 63)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_63d_mean126_closeadj_jerk5_v073_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 63)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_63d_mean126_closeadj_jerk5_v074_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 63)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_63d_mean126_closeadj_jerk5_v075_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 63)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_126d_mean10_closeadj_jerk5_v076_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 126)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_126d_mean10_closeadj_jerk5_v077_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 126)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_126d_mean10_closeadj_jerk5_v078_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 126)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_126d_mean21_closeadj_jerk5_v079_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 126)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_126d_mean21_closeadj_jerk5_v080_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 126)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_126d_mean21_closeadj_jerk5_v081_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 126)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_126d_mean42_closeadj_jerk5_v082_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 126)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_126d_mean42_closeadj_jerk5_v083_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 126)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_126d_mean42_closeadj_jerk5_v084_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 126)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_126d_mean63_closeadj_jerk5_v085_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 126)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_126d_mean63_closeadj_jerk5_v086_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 126)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_126d_mean63_closeadj_jerk5_v087_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 126)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_126d_mean126_closeadj_jerk5_v088_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 126)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_126d_mean126_closeadj_jerk5_v089_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 126)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_126d_mean126_closeadj_jerk5_v090_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 126)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_252d_mean10_closeadj_jerk5_v091_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 252)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_252d_mean10_closeadj_jerk5_v092_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 252)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_252d_mean10_closeadj_jerk5_v093_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 252)
    t = _mean(p, 10)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_252d_mean21_closeadj_jerk5_v094_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 252)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_252d_mean21_closeadj_jerk5_v095_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 252)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_252d_mean21_closeadj_jerk5_v096_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 252)
    t = _mean(p, 21)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_252d_mean42_closeadj_jerk5_v097_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 252)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_252d_mean42_closeadj_jerk5_v098_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 252)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_252d_mean42_closeadj_jerk5_v099_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 252)
    t = _mean(p, 42)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_252d_mean63_closeadj_jerk5_v100_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 252)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_252d_mean63_closeadj_jerk5_v101_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 252)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_252d_mean63_closeadj_jerk5_v102_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 252)
    t = _mean(p, 63)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_252d_mean126_closeadj_jerk5_v103_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 252)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_252d_mean126_closeadj_jerk5_v104_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 252)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_252d_mean126_closeadj_jerk5_v105_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 252)
    t = _mean(p, 126)
    base = t * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean10_logclose_jerk5_v106_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean10_logclose_jerk5_v107_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean10_logclose_jerk5_v108_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean21_logclose_jerk5_v109_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean21_logclose_jerk5_v110_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean21_logclose_jerk5_v111_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean42_logclose_jerk5_v112_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean42_logclose_jerk5_v113_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean42_logclose_jerk5_v114_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean63_logclose_jerk5_v115_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean63_logclose_jerk5_v116_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean63_logclose_jerk5_v117_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_5d_mean126_logclose_jerk5_v118_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 5)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_5d_mean126_logclose_jerk5_v119_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 5)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_5d_mean126_logclose_jerk5_v120_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 5)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean10_logclose_jerk5_v121_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean10_logclose_jerk5_v122_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean10_logclose_jerk5_v123_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean21_logclose_jerk5_v124_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean21_logclose_jerk5_v125_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean21_logclose_jerk5_v126_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean42_logclose_jerk5_v127_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean42_logclose_jerk5_v128_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean42_logclose_jerk5_v129_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean63_logclose_jerk5_v130_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean63_logclose_jerk5_v131_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean63_logclose_jerk5_v132_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_10d_mean126_logclose_jerk5_v133_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 10)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_10d_mean126_logclose_jerk5_v134_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 10)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_10d_mean126_logclose_jerk5_v135_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 10)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean10_logclose_jerk5_v136_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean10_logclose_jerk5_v137_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean10_logclose_jerk5_v138_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 10)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean21_logclose_jerk5_v139_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean21_logclose_jerk5_v140_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean21_logclose_jerk5_v141_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 21)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean42_logclose_jerk5_v142_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean42_logclose_jerk5_v143_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean42_logclose_jerk5_v144_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 42)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean63_logclose_jerk5_v145_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean63_logclose_jerk5_v146_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean63_logclose_jerk5_v147_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 63)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_myg_21d_mean126_logclose_jerk5_v148_signal(revenue, closeadj):
    p = _f12_multi_year_growth(revenue, 21)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_smvis_21d_mean126_logclose_jerk5_v149_signal(revenue, closeadj):
    p = _f12_smoothed_visibility(revenue, 21)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def lcv_f12_long_cycle_visibility_grpers_21d_mean126_logclose_jerk5_v150_signal(revenue, closeadj):
    p = _f12_growth_persistence(revenue, 21)
    t = _mean(p, 126)
    base = t * np.log1p(closeadj.abs())
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    lcv_f12_long_cycle_visibility_myg_5d_mean10_closeadj_jerk5_v001_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean10_closeadj_jerk5_v002_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean10_closeadj_jerk5_v003_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean21_closeadj_jerk5_v004_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean21_closeadj_jerk5_v005_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean21_closeadj_jerk5_v006_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean42_closeadj_jerk5_v007_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean42_closeadj_jerk5_v008_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean42_closeadj_jerk5_v009_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean63_closeadj_jerk5_v010_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean63_closeadj_jerk5_v011_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean63_closeadj_jerk5_v012_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean126_closeadj_jerk5_v013_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean126_closeadj_jerk5_v014_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean126_closeadj_jerk5_v015_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean10_closeadj_jerk5_v016_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean10_closeadj_jerk5_v017_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean10_closeadj_jerk5_v018_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean21_closeadj_jerk5_v019_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean21_closeadj_jerk5_v020_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean21_closeadj_jerk5_v021_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean42_closeadj_jerk5_v022_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean42_closeadj_jerk5_v023_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean42_closeadj_jerk5_v024_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean63_closeadj_jerk5_v025_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean63_closeadj_jerk5_v026_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean63_closeadj_jerk5_v027_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean126_closeadj_jerk5_v028_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean126_closeadj_jerk5_v029_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean126_closeadj_jerk5_v030_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean10_closeadj_jerk5_v031_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean10_closeadj_jerk5_v032_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean10_closeadj_jerk5_v033_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean21_closeadj_jerk5_v034_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean21_closeadj_jerk5_v035_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean21_closeadj_jerk5_v036_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean42_closeadj_jerk5_v037_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean42_closeadj_jerk5_v038_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean42_closeadj_jerk5_v039_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean63_closeadj_jerk5_v040_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean63_closeadj_jerk5_v041_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean63_closeadj_jerk5_v042_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean126_closeadj_jerk5_v043_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean126_closeadj_jerk5_v044_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean126_closeadj_jerk5_v045_signal,
    lcv_f12_long_cycle_visibility_myg_42d_mean10_closeadj_jerk5_v046_signal,
    lcv_f12_long_cycle_visibility_smvis_42d_mean10_closeadj_jerk5_v047_signal,
    lcv_f12_long_cycle_visibility_grpers_42d_mean10_closeadj_jerk5_v048_signal,
    lcv_f12_long_cycle_visibility_myg_42d_mean21_closeadj_jerk5_v049_signal,
    lcv_f12_long_cycle_visibility_smvis_42d_mean21_closeadj_jerk5_v050_signal,
    lcv_f12_long_cycle_visibility_grpers_42d_mean21_closeadj_jerk5_v051_signal,
    lcv_f12_long_cycle_visibility_myg_42d_mean42_closeadj_jerk5_v052_signal,
    lcv_f12_long_cycle_visibility_smvis_42d_mean42_closeadj_jerk5_v053_signal,
    lcv_f12_long_cycle_visibility_grpers_42d_mean42_closeadj_jerk5_v054_signal,
    lcv_f12_long_cycle_visibility_myg_42d_mean63_closeadj_jerk5_v055_signal,
    lcv_f12_long_cycle_visibility_smvis_42d_mean63_closeadj_jerk5_v056_signal,
    lcv_f12_long_cycle_visibility_grpers_42d_mean63_closeadj_jerk5_v057_signal,
    lcv_f12_long_cycle_visibility_myg_42d_mean126_closeadj_jerk5_v058_signal,
    lcv_f12_long_cycle_visibility_smvis_42d_mean126_closeadj_jerk5_v059_signal,
    lcv_f12_long_cycle_visibility_grpers_42d_mean126_closeadj_jerk5_v060_signal,
    lcv_f12_long_cycle_visibility_myg_63d_mean10_closeadj_jerk5_v061_signal,
    lcv_f12_long_cycle_visibility_smvis_63d_mean10_closeadj_jerk5_v062_signal,
    lcv_f12_long_cycle_visibility_grpers_63d_mean10_closeadj_jerk5_v063_signal,
    lcv_f12_long_cycle_visibility_myg_63d_mean21_closeadj_jerk5_v064_signal,
    lcv_f12_long_cycle_visibility_smvis_63d_mean21_closeadj_jerk5_v065_signal,
    lcv_f12_long_cycle_visibility_grpers_63d_mean21_closeadj_jerk5_v066_signal,
    lcv_f12_long_cycle_visibility_myg_63d_mean42_closeadj_jerk5_v067_signal,
    lcv_f12_long_cycle_visibility_smvis_63d_mean42_closeadj_jerk5_v068_signal,
    lcv_f12_long_cycle_visibility_grpers_63d_mean42_closeadj_jerk5_v069_signal,
    lcv_f12_long_cycle_visibility_myg_63d_mean63_closeadj_jerk5_v070_signal,
    lcv_f12_long_cycle_visibility_smvis_63d_mean63_closeadj_jerk5_v071_signal,
    lcv_f12_long_cycle_visibility_grpers_63d_mean63_closeadj_jerk5_v072_signal,
    lcv_f12_long_cycle_visibility_myg_63d_mean126_closeadj_jerk5_v073_signal,
    lcv_f12_long_cycle_visibility_smvis_63d_mean126_closeadj_jerk5_v074_signal,
    lcv_f12_long_cycle_visibility_grpers_63d_mean126_closeadj_jerk5_v075_signal,
    lcv_f12_long_cycle_visibility_myg_126d_mean10_closeadj_jerk5_v076_signal,
    lcv_f12_long_cycle_visibility_smvis_126d_mean10_closeadj_jerk5_v077_signal,
    lcv_f12_long_cycle_visibility_grpers_126d_mean10_closeadj_jerk5_v078_signal,
    lcv_f12_long_cycle_visibility_myg_126d_mean21_closeadj_jerk5_v079_signal,
    lcv_f12_long_cycle_visibility_smvis_126d_mean21_closeadj_jerk5_v080_signal,
    lcv_f12_long_cycle_visibility_grpers_126d_mean21_closeadj_jerk5_v081_signal,
    lcv_f12_long_cycle_visibility_myg_126d_mean42_closeadj_jerk5_v082_signal,
    lcv_f12_long_cycle_visibility_smvis_126d_mean42_closeadj_jerk5_v083_signal,
    lcv_f12_long_cycle_visibility_grpers_126d_mean42_closeadj_jerk5_v084_signal,
    lcv_f12_long_cycle_visibility_myg_126d_mean63_closeadj_jerk5_v085_signal,
    lcv_f12_long_cycle_visibility_smvis_126d_mean63_closeadj_jerk5_v086_signal,
    lcv_f12_long_cycle_visibility_grpers_126d_mean63_closeadj_jerk5_v087_signal,
    lcv_f12_long_cycle_visibility_myg_126d_mean126_closeadj_jerk5_v088_signal,
    lcv_f12_long_cycle_visibility_smvis_126d_mean126_closeadj_jerk5_v089_signal,
    lcv_f12_long_cycle_visibility_grpers_126d_mean126_closeadj_jerk5_v090_signal,
    lcv_f12_long_cycle_visibility_myg_252d_mean10_closeadj_jerk5_v091_signal,
    lcv_f12_long_cycle_visibility_smvis_252d_mean10_closeadj_jerk5_v092_signal,
    lcv_f12_long_cycle_visibility_grpers_252d_mean10_closeadj_jerk5_v093_signal,
    lcv_f12_long_cycle_visibility_myg_252d_mean21_closeadj_jerk5_v094_signal,
    lcv_f12_long_cycle_visibility_smvis_252d_mean21_closeadj_jerk5_v095_signal,
    lcv_f12_long_cycle_visibility_grpers_252d_mean21_closeadj_jerk5_v096_signal,
    lcv_f12_long_cycle_visibility_myg_252d_mean42_closeadj_jerk5_v097_signal,
    lcv_f12_long_cycle_visibility_smvis_252d_mean42_closeadj_jerk5_v098_signal,
    lcv_f12_long_cycle_visibility_grpers_252d_mean42_closeadj_jerk5_v099_signal,
    lcv_f12_long_cycle_visibility_myg_252d_mean63_closeadj_jerk5_v100_signal,
    lcv_f12_long_cycle_visibility_smvis_252d_mean63_closeadj_jerk5_v101_signal,
    lcv_f12_long_cycle_visibility_grpers_252d_mean63_closeadj_jerk5_v102_signal,
    lcv_f12_long_cycle_visibility_myg_252d_mean126_closeadj_jerk5_v103_signal,
    lcv_f12_long_cycle_visibility_smvis_252d_mean126_closeadj_jerk5_v104_signal,
    lcv_f12_long_cycle_visibility_grpers_252d_mean126_closeadj_jerk5_v105_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean10_logclose_jerk5_v106_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean10_logclose_jerk5_v107_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean10_logclose_jerk5_v108_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean21_logclose_jerk5_v109_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean21_logclose_jerk5_v110_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean21_logclose_jerk5_v111_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean42_logclose_jerk5_v112_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean42_logclose_jerk5_v113_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean42_logclose_jerk5_v114_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean63_logclose_jerk5_v115_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean63_logclose_jerk5_v116_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean63_logclose_jerk5_v117_signal,
    lcv_f12_long_cycle_visibility_myg_5d_mean126_logclose_jerk5_v118_signal,
    lcv_f12_long_cycle_visibility_smvis_5d_mean126_logclose_jerk5_v119_signal,
    lcv_f12_long_cycle_visibility_grpers_5d_mean126_logclose_jerk5_v120_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean10_logclose_jerk5_v121_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean10_logclose_jerk5_v122_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean10_logclose_jerk5_v123_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean21_logclose_jerk5_v124_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean21_logclose_jerk5_v125_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean21_logclose_jerk5_v126_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean42_logclose_jerk5_v127_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean42_logclose_jerk5_v128_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean42_logclose_jerk5_v129_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean63_logclose_jerk5_v130_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean63_logclose_jerk5_v131_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean63_logclose_jerk5_v132_signal,
    lcv_f12_long_cycle_visibility_myg_10d_mean126_logclose_jerk5_v133_signal,
    lcv_f12_long_cycle_visibility_smvis_10d_mean126_logclose_jerk5_v134_signal,
    lcv_f12_long_cycle_visibility_grpers_10d_mean126_logclose_jerk5_v135_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean10_logclose_jerk5_v136_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean10_logclose_jerk5_v137_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean10_logclose_jerk5_v138_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean21_logclose_jerk5_v139_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean21_logclose_jerk5_v140_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean21_logclose_jerk5_v141_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean42_logclose_jerk5_v142_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean42_logclose_jerk5_v143_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean42_logclose_jerk5_v144_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean63_logclose_jerk5_v145_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean63_logclose_jerk5_v146_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean63_logclose_jerk5_v147_signal,
    lcv_f12_long_cycle_visibility_myg_21d_mean126_logclose_jerk5_v148_signal,
    lcv_f12_long_cycle_visibility_smvis_21d_mean126_logclose_jerk5_v149_signal,
    lcv_f12_long_cycle_visibility_grpers_21d_mean126_logclose_jerk5_v150_signal
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_LONG_CYCLE_VISIBILITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")

    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "netinc": netinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f12_multi_year_growth", "_f12_smoothed_visibility", "_f12_growth_persistence",)
    body_hashes = {}
    import hashlib as _hashlib
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
        # canonical body hash for dup-check (exclude def line / fn name)
        canon = "\n".join(src.splitlines()[1:])
        h = _hashlib.sha256(canon.encode()).hexdigest()
        body_hashes.setdefault(h, []).append(name)
        n_features += 1
    dups = {h: names for h, names in body_hashes.items() if len(names) > 1}
    assert not dups, f"duplicate bodies: {dups}"
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f12_long_cycle_visibility_3rd_derivatives_001_150_claude: {n_features} features pass, 0 duplicate bodies")
