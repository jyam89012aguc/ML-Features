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


def _f05_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan)


def _f05_revenue_smoothness(revenue, w):
    pct = revenue.pct_change()
    return 1.0 / (pct.rolling(w, min_periods=max(1, w // 2)).std() + 1e-9)


def _f05_stability_score(revenue, ebitda, w):
    rev_cv = _f05_revenue_cv(revenue, w)
    ebt_cv = _f05_revenue_cv(ebitda, w)
    return (rev_cv + ebt_cv) / 2.0


# CV slopes
def f05urs_f05_utility_revenue_stability_cv_21d_slope_v001_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_21d_slope_v002_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_63d_slope_v003_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_63d_slope_v004_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_63d_slope_v005_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_252d_slope_v006_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_252d_slope_v007_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_252d_slope_v008_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_504d_slope_v009_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cv_504d_slope_v010_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth slopes
def f05urs_f05_utility_revenue_stability_smooth_21d_slope_v011_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_21d_slope_v012_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_63d_slope_v013_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_63d_slope_v014_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_252d_slope_v015_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_252d_slope_v016_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_252d_slope_v017_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_504d_slope_v018_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_504d_slope_v019_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Stab slopes
def f05urs_f05_utility_revenue_stability_stab_21d_slope_v020_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_21d_slope_v021_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_63d_slope_v022_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_63d_slope_v023_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_252d_slope_v024_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_252d_slope_v025_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_252d_slope_v026_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_504d_slope_v027_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_504d_slope_v028_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Volume
def f05urs_f05_utility_revenue_stability_cvxvol_63d_slope_v029_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 63) * _mean(volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxvol_252d_slope_v030_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252) * _mean(volume, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxvol_63d_slope_v031_signal(revenue, closeadj, volume):
    base = _f05_revenue_smoothness(revenue, 63) * _mean(volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxvol_252d_slope_v032_signal(revenue, closeadj, volume):
    base = _f05_revenue_smoothness(revenue, 252) * _mean(volume, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxvol_63d_slope_v033_signal(revenue, ebitda, closeadj, volume):
    base = _f05_stability_score(revenue, ebitda, 63) * _mean(volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxvol_252d_slope_v034_signal(revenue, ebitda, closeadj, volume):
    base = _f05_stability_score(revenue, ebitda, 252) * _mean(volume, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR
def f05urs_f05_utility_revenue_stability_cvxatr_63d_slope_v035_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_revenue_cv(revenue, 63) * atr
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxatr_252d_slope_v036_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f05_revenue_cv(revenue, 252) * atr
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxatr_63d_slope_v037_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_revenue_smoothness(revenue, 63) * atr
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxatr_252d_slope_v038_signal(revenue, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f05_revenue_smoothness(revenue, 252) * atr
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxatr_63d_slope_v039_signal(revenue, ebitda, closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f05_stability_score(revenue, ebitda, 63) * atr
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxatr_252d_slope_v040_signal(revenue, ebitda, closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f05_stability_score(revenue, ebitda, 252) * atr
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA
def f05urs_f05_utility_revenue_stability_cvema_63d_slope_v041_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63).ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvema_252d_slope_v042_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252).ewm(span=63, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothema_63d_slope_v043_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63).ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothema_252d_slope_v044_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252).ewm(span=63, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabema_63d_slope_v045_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63).ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabema_252d_slope_v046_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252).ewm(span=63, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Squared
def f05urs_f05_utility_revenue_stability_cvsq_63d_slope_v047_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = c * c.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvsq_252d_slope_v048_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = c * c.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabsq_63d_slope_v049_signal(revenue, ebitda, closeadj):
    s = _f05_stability_score(revenue, ebitda, 63)
    base = s * s.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabsq_252d_slope_v050_signal(revenue, ebitda, closeadj):
    s = _f05_stability_score(revenue, ebitda, 252)
    base = s * s.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothsq_63d_slope_v051_signal(revenue, closeadj):
    sm = _f05_revenue_smoothness(revenue, 63)
    base = sm * sm * closeadj * 1e-5
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothsq_252d_slope_v052_signal(revenue, closeadj):
    sm = _f05_revenue_smoothness(revenue, 252)
    base = sm * sm * closeadj * 1e-5
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Z-score
def f05urs_f05_utility_revenue_stability_cvz_63d_slope_v053_signal(revenue, closeadj):
    base = _z(_f05_revenue_cv(revenue, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvz_252d_slope_v054_signal(revenue, closeadj):
    base = _z(_f05_revenue_cv(revenue, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothz_63d_slope_v055_signal(revenue, closeadj):
    base = _z(_f05_revenue_smoothness(revenue, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothz_252d_slope_v056_signal(revenue, closeadj):
    base = _z(_f05_revenue_smoothness(revenue, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabz_63d_slope_v057_signal(revenue, ebitda, closeadj):
    base = _z(_f05_stability_score(revenue, ebitda, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabz_252d_slope_v058_signal(revenue, ebitda, closeadj):
    base = _z(_f05_stability_score(revenue, ebitda, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Rank
def f05urs_f05_utility_revenue_stability_cvrank_63d_slope_v059_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvrank_252d_slope_v060_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothrank_63d_slope_v061_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothrank_252d_slope_v062_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabrank_63d_slope_v063_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63).rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabrank_252d_slope_v064_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252).rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Gap
def f05urs_f05_utility_revenue_stability_cvgap_63d_slope_v065_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = (c - _mean(c, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvgap_252d_slope_v066_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = (c - _mean(c, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothgap_63d_slope_v067_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 63)
    base = (s - _mean(s, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothgap_252d_slope_v068_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 252)
    base = (s - _mean(s, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabgap_63d_slope_v069_signal(revenue, ebitda, closeadj):
    s = _f05_stability_score(revenue, ebitda, 63)
    base = (s - _mean(s, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabgap_252d_slope_v070_signal(revenue, ebitda, closeadj):
    s = _f05_stability_score(revenue, ebitda, 252)
    base = (s - _mean(s, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo
def f05urs_f05_utility_revenue_stability_combocvsmooth_63d_slope_v071_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    s = _f05_revenue_smoothness(revenue, 63)
    base = c * s * closeadj * 0.001
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_combocvsmooth_252d_slope_v072_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    s = _f05_revenue_smoothness(revenue, 252)
    base = c * s * closeadj * 0.001
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_combostabsmooth_63d_slope_v073_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 63)
    s = _f05_revenue_smoothness(revenue, 63)
    base = st * s * closeadj * 0.001
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_combostabsmooth_252d_slope_v074_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    s = _f05_revenue_smoothness(revenue, 252)
    base = st * s * closeadj * 0.001
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_combocvstab_63d_slope_v075_signal(revenue, ebitda, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    st = _f05_stability_score(revenue, ebitda, 63)
    base = c * st * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_combocvstab_252d_slope_v076_signal(revenue, ebitda, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    st = _f05_stability_score(revenue, ebitda, 252)
    base = c * st * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Dollar volume
def f05urs_f05_utility_revenue_stability_cvxdv_63d_slope_v077_signal(revenue, closeadj, volume):
    c = _f05_revenue_cv(revenue, 63)
    dv = closeadj * volume
    base = c * _mean(dv, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxdv_252d_slope_v078_signal(revenue, closeadj, volume):
    c = _f05_revenue_cv(revenue, 252)
    dv = closeadj * volume
    base = c * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxdv_63d_slope_v079_signal(revenue, closeadj, volume):
    s = _f05_revenue_smoothness(revenue, 63)
    dv = closeadj * volume
    base = s * _mean(dv, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxdv_252d_slope_v080_signal(revenue, closeadj, volume):
    s = _f05_revenue_smoothness(revenue, 252)
    dv = closeadj * volume
    base = s * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxdv_63d_slope_v081_signal(revenue, ebitda, closeadj, volume):
    st = _f05_stability_score(revenue, ebitda, 63)
    dv = closeadj * volume
    base = st * _mean(dv, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxdv_252d_slope_v082_signal(revenue, ebitda, closeadj, volume):
    st = _f05_stability_score(revenue, ebitda, 252)
    dv = closeadj * volume
    base = st * _mean(dv, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Std
def f05urs_f05_utility_revenue_stability_cvstd_63d_slope_v083_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = _std(c, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvstd_252d_slope_v084_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = _std(c, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothstd_63d_slope_v085_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 63)
    base = _std(s, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothstd_252d_slope_v086_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 252)
    base = _std(s, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabstd_63d_slope_v087_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 63)
    base = _std(st, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabstd_252d_slope_v088_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    base = _std(st, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Size
def f05urs_f05_utility_revenue_stability_cvxsize_63d_slope_v089_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = c * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxsize_252d_slope_v090_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = c * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxsize_63d_slope_v091_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 63)
    base = s * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxsize_252d_slope_v092_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 252)
    base = s * np.log(revenue.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Closez
def f05urs_f05_utility_revenue_stability_cvxclosez_63d_slope_v093_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = c * _z(closeadj, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxclosez_252d_slope_v094_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = c * _z(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxclosez_63d_slope_v095_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 63)
    base = s * _z(closeadj, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxclosez_252d_slope_v096_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 252)
    base = s * _z(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxclosez_63d_slope_v097_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 63)
    base = st * _z(closeadj, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxclosez_252d_slope_v098_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    base = st * _z(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Return
def f05urs_f05_utility_revenue_stability_cvxret_63d_slope_v099_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = c * closeadj.pct_change(21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxret_252d_slope_v100_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = c * closeadj.pct_change(63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxret_63d_slope_v101_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 63)
    base = s * closeadj.pct_change(21) * closeadj * 0.001
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxret_252d_slope_v102_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 252)
    base = s * closeadj.pct_change(63) * closeadj * 0.001
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxret_63d_slope_v103_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 63)
    base = st * closeadj.pct_change(21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxret_252d_slope_v104_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    base = st * closeadj.pct_change(63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Abs return
def f05urs_f05_utility_revenue_stability_cvxabsret_63d_slope_v105_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = c * closeadj.pct_change(21).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxabsret_252d_slope_v106_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = c * closeadj.pct_change(63).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxabsret_63d_slope_v107_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 63)
    base = st * closeadj.pct_change(21).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxabsret_252d_slope_v108_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    base = st * closeadj.pct_change(63).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Acceleration
def f05urs_f05_utility_revenue_stability_cvaccel_63d_slope_v109_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = (c - c.shift(21)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvaccel_252d_slope_v110_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = (c - c.shift(63)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothaccel_63d_slope_v111_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 63)
    base = (s - s.shift(21)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothaccel_252d_slope_v112_signal(revenue, closeadj):
    s = _f05_revenue_smoothness(revenue, 252)
    base = (s - s.shift(63)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabaccel_63d_slope_v113_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 63)
    base = (st - st.shift(21)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabaccel_252d_slope_v114_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    base = (st - st.shift(63)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Inv price
def f05urs_f05_utility_revenue_stability_cvxinv_63d_slope_v115_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = c * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxinv_252d_slope_v116_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = c * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# MA cross
def f05urs_f05_utility_revenue_stability_cvcross_21_252_slope_v117_signal(revenue, closeadj):
    short = _f05_revenue_cv(revenue, 21)
    long = _f05_revenue_cv(revenue, 252)
    base = (short - long) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvcross_63_252_slope_v118_signal(revenue, closeadj):
    short = _f05_revenue_cv(revenue, 63)
    long = _f05_revenue_cv(revenue, 252)
    base = (short - long) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabcross_63_252_slope_v119_signal(revenue, ebitda, closeadj):
    short = _f05_stability_score(revenue, ebitda, 63)
    long = _f05_stability_score(revenue, ebitda, 252)
    base = (short - long) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Spread vs target (utilities CV ~ 0.05)
def f05urs_f05_utility_revenue_stability_cvspread_252d_slope_v120_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = (c - 0.05) * closeadj * _mean(c, 252) / _mean(c, 504).replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabspread_252d_slope_v121_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    base = (st - 0.05) * closeadj * _mean(st, 252) / _mean(st, 504).replace(0, np.nan)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Sum
def f05urs_f05_utility_revenue_stability_cvsum_63d_slope_v122_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = c.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabsum_63d_slope_v123_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 63)
    base = st.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Sign × vol
def f05urs_f05_utility_revenue_stability_cvsignxvol_63d_slope_v124_signal(revenue, closeadj, volume):
    c = _f05_revenue_cv(revenue, 63)
    base = np.sign(c - _mean(c, 252)) * _mean(volume, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvsignxvol_252d_slope_v125_signal(revenue, closeadj, volume):
    c = _f05_revenue_cv(revenue, 252)
    base = np.sign(c - _mean(c, 504)) * _mean(volume, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Diff-norm slopes
def f05urs_f05_utility_revenue_stability_cvdn_63d_slope_v126_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvdn_252d_slope_v127_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothdn_63d_slope_v128_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothdn_252d_slope_v129_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabdn_63d_slope_v130_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabdn_252d_slope_v131_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d
def f05urs_f05_utility_revenue_stability_cv_5d_slope_v132_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_5d_slope_v133_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_5d_slope_v134_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d
def f05urs_f05_utility_revenue_stability_cv_10d_slope_v135_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_10d_slope_v136_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_10d_slope_v137_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d
def f05urs_f05_utility_revenue_stability_cv_42d_slope_v138_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_42d_slope_v139_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_42d_slope_v140_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d
def f05urs_f05_utility_revenue_stability_cv_189d_slope_v141_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252) * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smooth_189d_slope_v142_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252) * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_189d_slope_v143_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252) * closeadj
    result = _slope_pct(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo ATR
def f05urs_f05_utility_revenue_stability_combo_atr_63d_slope_v144_signal(revenue, ebitda, closeadj, high, low):
    c = _f05_revenue_cv(revenue, 63)
    st = _f05_stability_score(revenue, ebitda, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = c * st * atr
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_combo_atr_252d_slope_v145_signal(revenue, ebitda, closeadj, high, low):
    c = _f05_revenue_cv(revenue, 252)
    st = _f05_stability_score(revenue, ebitda, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = c * st * atr
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Combo DV
def f05urs_f05_utility_revenue_stability_combo_dv_63d_slope_v146_signal(revenue, closeadj, volume):
    c = _f05_revenue_cv(revenue, 63)
    s = _f05_revenue_smoothness(revenue, 63)
    dv = closeadj * volume
    base = c * s * _mean(dv, 21) * 0.001
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_combo_dv_252d_slope_v147_signal(revenue, closeadj, volume):
    c = _f05_revenue_cv(revenue, 252)
    s = _f05_revenue_smoothness(revenue, 252)
    dv = closeadj * volume
    base = c * s * _mean(dv, 63) * 0.001
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# CV log
def f05urs_f05_utility_revenue_stability_cvlog_63d_slope_v148_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 63)
    base = np.log(c.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvlog_252d_slope_v149_signal(revenue, closeadj):
    c = _f05_revenue_cv(revenue, 252)
    base = np.log(c.abs().replace(0, np.nan)) * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Stab xmargin
def f05urs_f05_utility_revenue_stability_stabxmargin_252d_slope_v150_signal(revenue, ebitda, closeadj):
    st = _f05_stability_score(revenue, ebitda, 252)
    m = ebitda / revenue.replace(0, np.nan)
    base = st * _mean(m, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05urs_f05_utility_revenue_stability_cv_21d_slope_v001_signal,
    f05urs_f05_utility_revenue_stability_cv_21d_slope_v002_signal,
    f05urs_f05_utility_revenue_stability_cv_63d_slope_v003_signal,
    f05urs_f05_utility_revenue_stability_cv_63d_slope_v004_signal,
    f05urs_f05_utility_revenue_stability_cv_63d_slope_v005_signal,
    f05urs_f05_utility_revenue_stability_cv_252d_slope_v006_signal,
    f05urs_f05_utility_revenue_stability_cv_252d_slope_v007_signal,
    f05urs_f05_utility_revenue_stability_cv_252d_slope_v008_signal,
    f05urs_f05_utility_revenue_stability_cv_504d_slope_v009_signal,
    f05urs_f05_utility_revenue_stability_cv_504d_slope_v010_signal,
    f05urs_f05_utility_revenue_stability_smooth_21d_slope_v011_signal,
    f05urs_f05_utility_revenue_stability_smooth_21d_slope_v012_signal,
    f05urs_f05_utility_revenue_stability_smooth_63d_slope_v013_signal,
    f05urs_f05_utility_revenue_stability_smooth_63d_slope_v014_signal,
    f05urs_f05_utility_revenue_stability_smooth_252d_slope_v015_signal,
    f05urs_f05_utility_revenue_stability_smooth_252d_slope_v016_signal,
    f05urs_f05_utility_revenue_stability_smooth_252d_slope_v017_signal,
    f05urs_f05_utility_revenue_stability_smooth_504d_slope_v018_signal,
    f05urs_f05_utility_revenue_stability_smooth_504d_slope_v019_signal,
    f05urs_f05_utility_revenue_stability_stab_21d_slope_v020_signal,
    f05urs_f05_utility_revenue_stability_stab_21d_slope_v021_signal,
    f05urs_f05_utility_revenue_stability_stab_63d_slope_v022_signal,
    f05urs_f05_utility_revenue_stability_stab_63d_slope_v023_signal,
    f05urs_f05_utility_revenue_stability_stab_252d_slope_v024_signal,
    f05urs_f05_utility_revenue_stability_stab_252d_slope_v025_signal,
    f05urs_f05_utility_revenue_stability_stab_252d_slope_v026_signal,
    f05urs_f05_utility_revenue_stability_stab_504d_slope_v027_signal,
    f05urs_f05_utility_revenue_stability_stab_504d_slope_v028_signal,
    f05urs_f05_utility_revenue_stability_cvxvol_63d_slope_v029_signal,
    f05urs_f05_utility_revenue_stability_cvxvol_252d_slope_v030_signal,
    f05urs_f05_utility_revenue_stability_smoothxvol_63d_slope_v031_signal,
    f05urs_f05_utility_revenue_stability_smoothxvol_252d_slope_v032_signal,
    f05urs_f05_utility_revenue_stability_stabxvol_63d_slope_v033_signal,
    f05urs_f05_utility_revenue_stability_stabxvol_252d_slope_v034_signal,
    f05urs_f05_utility_revenue_stability_cvxatr_63d_slope_v035_signal,
    f05urs_f05_utility_revenue_stability_cvxatr_252d_slope_v036_signal,
    f05urs_f05_utility_revenue_stability_smoothxatr_63d_slope_v037_signal,
    f05urs_f05_utility_revenue_stability_smoothxatr_252d_slope_v038_signal,
    f05urs_f05_utility_revenue_stability_stabxatr_63d_slope_v039_signal,
    f05urs_f05_utility_revenue_stability_stabxatr_252d_slope_v040_signal,
    f05urs_f05_utility_revenue_stability_cvema_63d_slope_v041_signal,
    f05urs_f05_utility_revenue_stability_cvema_252d_slope_v042_signal,
    f05urs_f05_utility_revenue_stability_smoothema_63d_slope_v043_signal,
    f05urs_f05_utility_revenue_stability_smoothema_252d_slope_v044_signal,
    f05urs_f05_utility_revenue_stability_stabema_63d_slope_v045_signal,
    f05urs_f05_utility_revenue_stability_stabema_252d_slope_v046_signal,
    f05urs_f05_utility_revenue_stability_cvsq_63d_slope_v047_signal,
    f05urs_f05_utility_revenue_stability_cvsq_252d_slope_v048_signal,
    f05urs_f05_utility_revenue_stability_stabsq_63d_slope_v049_signal,
    f05urs_f05_utility_revenue_stability_stabsq_252d_slope_v050_signal,
    f05urs_f05_utility_revenue_stability_smoothsq_63d_slope_v051_signal,
    f05urs_f05_utility_revenue_stability_smoothsq_252d_slope_v052_signal,
    f05urs_f05_utility_revenue_stability_cvz_63d_slope_v053_signal,
    f05urs_f05_utility_revenue_stability_cvz_252d_slope_v054_signal,
    f05urs_f05_utility_revenue_stability_smoothz_63d_slope_v055_signal,
    f05urs_f05_utility_revenue_stability_smoothz_252d_slope_v056_signal,
    f05urs_f05_utility_revenue_stability_stabz_63d_slope_v057_signal,
    f05urs_f05_utility_revenue_stability_stabz_252d_slope_v058_signal,
    f05urs_f05_utility_revenue_stability_cvrank_63d_slope_v059_signal,
    f05urs_f05_utility_revenue_stability_cvrank_252d_slope_v060_signal,
    f05urs_f05_utility_revenue_stability_smoothrank_63d_slope_v061_signal,
    f05urs_f05_utility_revenue_stability_smoothrank_252d_slope_v062_signal,
    f05urs_f05_utility_revenue_stability_stabrank_63d_slope_v063_signal,
    f05urs_f05_utility_revenue_stability_stabrank_252d_slope_v064_signal,
    f05urs_f05_utility_revenue_stability_cvgap_63d_slope_v065_signal,
    f05urs_f05_utility_revenue_stability_cvgap_252d_slope_v066_signal,
    f05urs_f05_utility_revenue_stability_smoothgap_63d_slope_v067_signal,
    f05urs_f05_utility_revenue_stability_smoothgap_252d_slope_v068_signal,
    f05urs_f05_utility_revenue_stability_stabgap_63d_slope_v069_signal,
    f05urs_f05_utility_revenue_stability_stabgap_252d_slope_v070_signal,
    f05urs_f05_utility_revenue_stability_combocvsmooth_63d_slope_v071_signal,
    f05urs_f05_utility_revenue_stability_combocvsmooth_252d_slope_v072_signal,
    f05urs_f05_utility_revenue_stability_combostabsmooth_63d_slope_v073_signal,
    f05urs_f05_utility_revenue_stability_combostabsmooth_252d_slope_v074_signal,
    f05urs_f05_utility_revenue_stability_combocvstab_63d_slope_v075_signal,
    f05urs_f05_utility_revenue_stability_combocvstab_252d_slope_v076_signal,
    f05urs_f05_utility_revenue_stability_cvxdv_63d_slope_v077_signal,
    f05urs_f05_utility_revenue_stability_cvxdv_252d_slope_v078_signal,
    f05urs_f05_utility_revenue_stability_smoothxdv_63d_slope_v079_signal,
    f05urs_f05_utility_revenue_stability_smoothxdv_252d_slope_v080_signal,
    f05urs_f05_utility_revenue_stability_stabxdv_63d_slope_v081_signal,
    f05urs_f05_utility_revenue_stability_stabxdv_252d_slope_v082_signal,
    f05urs_f05_utility_revenue_stability_cvstd_63d_slope_v083_signal,
    f05urs_f05_utility_revenue_stability_cvstd_252d_slope_v084_signal,
    f05urs_f05_utility_revenue_stability_smoothstd_63d_slope_v085_signal,
    f05urs_f05_utility_revenue_stability_smoothstd_252d_slope_v086_signal,
    f05urs_f05_utility_revenue_stability_stabstd_63d_slope_v087_signal,
    f05urs_f05_utility_revenue_stability_stabstd_252d_slope_v088_signal,
    f05urs_f05_utility_revenue_stability_cvxsize_63d_slope_v089_signal,
    f05urs_f05_utility_revenue_stability_cvxsize_252d_slope_v090_signal,
    f05urs_f05_utility_revenue_stability_smoothxsize_63d_slope_v091_signal,
    f05urs_f05_utility_revenue_stability_smoothxsize_252d_slope_v092_signal,
    f05urs_f05_utility_revenue_stability_cvxclosez_63d_slope_v093_signal,
    f05urs_f05_utility_revenue_stability_cvxclosez_252d_slope_v094_signal,
    f05urs_f05_utility_revenue_stability_smoothxclosez_63d_slope_v095_signal,
    f05urs_f05_utility_revenue_stability_smoothxclosez_252d_slope_v096_signal,
    f05urs_f05_utility_revenue_stability_stabxclosez_63d_slope_v097_signal,
    f05urs_f05_utility_revenue_stability_stabxclosez_252d_slope_v098_signal,
    f05urs_f05_utility_revenue_stability_cvxret_63d_slope_v099_signal,
    f05urs_f05_utility_revenue_stability_cvxret_252d_slope_v100_signal,
    f05urs_f05_utility_revenue_stability_smoothxret_63d_slope_v101_signal,
    f05urs_f05_utility_revenue_stability_smoothxret_252d_slope_v102_signal,
    f05urs_f05_utility_revenue_stability_stabxret_63d_slope_v103_signal,
    f05urs_f05_utility_revenue_stability_stabxret_252d_slope_v104_signal,
    f05urs_f05_utility_revenue_stability_cvxabsret_63d_slope_v105_signal,
    f05urs_f05_utility_revenue_stability_cvxabsret_252d_slope_v106_signal,
    f05urs_f05_utility_revenue_stability_stabxabsret_63d_slope_v107_signal,
    f05urs_f05_utility_revenue_stability_stabxabsret_252d_slope_v108_signal,
    f05urs_f05_utility_revenue_stability_cvaccel_63d_slope_v109_signal,
    f05urs_f05_utility_revenue_stability_cvaccel_252d_slope_v110_signal,
    f05urs_f05_utility_revenue_stability_smoothaccel_63d_slope_v111_signal,
    f05urs_f05_utility_revenue_stability_smoothaccel_252d_slope_v112_signal,
    f05urs_f05_utility_revenue_stability_stabaccel_63d_slope_v113_signal,
    f05urs_f05_utility_revenue_stability_stabaccel_252d_slope_v114_signal,
    f05urs_f05_utility_revenue_stability_cvxinv_63d_slope_v115_signal,
    f05urs_f05_utility_revenue_stability_cvxinv_252d_slope_v116_signal,
    f05urs_f05_utility_revenue_stability_cvcross_21_252_slope_v117_signal,
    f05urs_f05_utility_revenue_stability_cvcross_63_252_slope_v118_signal,
    f05urs_f05_utility_revenue_stability_stabcross_63_252_slope_v119_signal,
    f05urs_f05_utility_revenue_stability_cvspread_252d_slope_v120_signal,
    f05urs_f05_utility_revenue_stability_stabspread_252d_slope_v121_signal,
    f05urs_f05_utility_revenue_stability_cvsum_63d_slope_v122_signal,
    f05urs_f05_utility_revenue_stability_stabsum_63d_slope_v123_signal,
    f05urs_f05_utility_revenue_stability_cvsignxvol_63d_slope_v124_signal,
    f05urs_f05_utility_revenue_stability_cvsignxvol_252d_slope_v125_signal,
    f05urs_f05_utility_revenue_stability_cvdn_63d_slope_v126_signal,
    f05urs_f05_utility_revenue_stability_cvdn_252d_slope_v127_signal,
    f05urs_f05_utility_revenue_stability_smoothdn_63d_slope_v128_signal,
    f05urs_f05_utility_revenue_stability_smoothdn_252d_slope_v129_signal,
    f05urs_f05_utility_revenue_stability_stabdn_63d_slope_v130_signal,
    f05urs_f05_utility_revenue_stability_stabdn_252d_slope_v131_signal,
    f05urs_f05_utility_revenue_stability_cv_5d_slope_v132_signal,
    f05urs_f05_utility_revenue_stability_smooth_5d_slope_v133_signal,
    f05urs_f05_utility_revenue_stability_stab_5d_slope_v134_signal,
    f05urs_f05_utility_revenue_stability_cv_10d_slope_v135_signal,
    f05urs_f05_utility_revenue_stability_smooth_10d_slope_v136_signal,
    f05urs_f05_utility_revenue_stability_stab_10d_slope_v137_signal,
    f05urs_f05_utility_revenue_stability_cv_42d_slope_v138_signal,
    f05urs_f05_utility_revenue_stability_smooth_42d_slope_v139_signal,
    f05urs_f05_utility_revenue_stability_stab_42d_slope_v140_signal,
    f05urs_f05_utility_revenue_stability_cv_189d_slope_v141_signal,
    f05urs_f05_utility_revenue_stability_smooth_189d_slope_v142_signal,
    f05urs_f05_utility_revenue_stability_stab_189d_slope_v143_signal,
    f05urs_f05_utility_revenue_stability_combo_atr_63d_slope_v144_signal,
    f05urs_f05_utility_revenue_stability_combo_atr_252d_slope_v145_signal,
    f05urs_f05_utility_revenue_stability_combo_dv_63d_slope_v146_signal,
    f05urs_f05_utility_revenue_stability_combo_dv_252d_slope_v147_signal,
    f05urs_f05_utility_revenue_stability_cvlog_63d_slope_v148_signal,
    f05urs_f05_utility_revenue_stability_cvlog_252d_slope_v149_signal,
    f05urs_f05_utility_revenue_stability_stabxmargin_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_UTILITY_REVENUE_STABILITY_REGISTRY_SLOPE_001_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f05_revenue_cv", "_f05_revenue_smoothness", "_f05_stability_score")
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
    print(f"OK f05_utility_revenue_stability_2nd_derivatives_001_150_claude: {n_features} features pass")
