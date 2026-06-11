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


# CV = std/mean of revenue (low CV = stable)
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


# Revenue CV (lower = more stable) × close
def f05urs_f05_utility_revenue_stability_revcv_21d_base_v001_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_63d_base_v002_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_126d_base_v003_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_252d_base_v004_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_504d_base_v005_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Revenue smoothness × close
def f05urs_f05_utility_revenue_stability_revsmooth_21d_base_v006_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revsmooth_63d_base_v007_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revsmooth_126d_base_v008_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revsmooth_252d_base_v009_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revsmooth_504d_base_v010_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stability score × close
def f05urs_f05_utility_revenue_stability_stab_21d_base_v011_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_63d_base_v012_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_126d_base_v013_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_252d_base_v014_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_504d_base_v015_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Z-score
def f05urs_f05_utility_revenue_stability_cvz_252d_base_v016_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothz_252d_base_v017_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabz_252d_base_v018_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Std (of CV)
def f05urs_f05_utility_revenue_stability_cvstd_252d_base_v019_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothstd_252d_base_v020_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EMA
def f05urs_f05_utility_revenue_stability_cvema_252d_base_v021_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothema_252d_base_v022_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabema_252d_base_v023_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Rank
def f05urs_f05_utility_revenue_stability_cvrank_252d_base_v024_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothrank_252d_base_v025_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabrank_252d_base_v026_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Short windows
def f05urs_f05_utility_revenue_stability_revcv_5d_base_v027_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_10d_base_v028_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_42d_base_v029_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_189d_base_v030_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revcv_378d_base_v031_signal(revenue, closeadj):
    result = _f05_revenue_cv(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smoothness short
def f05urs_f05_utility_revenue_stability_revsmooth_5d_base_v032_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revsmooth_42d_base_v033_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revsmooth_189d_base_v034_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_revsmooth_378d_base_v035_signal(revenue, closeadj):
    result = _f05_revenue_smoothness(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stability score short
def f05urs_f05_utility_revenue_stability_stab_5d_base_v036_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_42d_base_v037_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stab_189d_base_v038_signal(revenue, ebitda, closeadj):
    result = _f05_stability_score(revenue, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Volume × CV × close
def f05urs_f05_utility_revenue_stability_cvxvol_63d_base_v039_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 63)
    result = base * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxvol_252d_base_v040_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252)
    result = base * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxvol_252d_base_v041_signal(revenue, closeadj, volume):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxvol_252d_base_v042_signal(revenue, ebitda, closeadj, volume):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV inverse (high = stable) × close
def f05urs_f05_utility_revenue_stability_cvinv_252d_base_v043_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = (1.0 / base.replace(0, np.nan)) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvinv_63d_base_v044_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    result = (1.0 / base.replace(0, np.nan)) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


# ATR × CV × close
def f05urs_f05_utility_revenue_stability_cvxatr_63d_base_v045_signal(revenue, closeadj, high, low):
    base = _f05_revenue_cv(revenue, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxatr_252d_base_v046_signal(revenue, closeadj, high, low):
    base = _f05_revenue_cv(revenue, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxatr_252d_base_v047_signal(revenue, closeadj, high, low):
    base = _f05_revenue_smoothness(revenue, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxatr_252d_base_v048_signal(revenue, ebitda, closeadj, high, low):
    base = _f05_stability_score(revenue, ebitda, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


# CV × close pct change
def f05urs_f05_utility_revenue_stability_cvxret_63d_base_v049_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    result = base * closeadj.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvxret_252d_base_v050_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth × ret
def f05urs_f05_utility_revenue_stability_smoothxret_252d_base_v051_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = base * closeadj.pct_change(63) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × ret
def f05urs_f05_utility_revenue_stability_stabxret_252d_base_v052_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × abs return × close
def f05urs_f05_utility_revenue_stability_cvxabsret_252d_base_v053_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * closeadj.pct_change(63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab × abs return × close
def f05urs_f05_utility_revenue_stability_stabxabsret_252d_base_v054_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * closeadj.pct_change(63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV gap (current vs 504d)
def f05urs_f05_utility_revenue_stability_cvgap_252d_base_v055_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvgap_63d_base_v056_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth gap
def f05urs_f05_utility_revenue_stability_smoothgap_252d_base_v057_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab gap
def f05urs_f05_utility_revenue_stability_stabgap_252d_base_v058_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV cross
def f05urs_f05_utility_revenue_stability_cvcross_21_252_base_v059_signal(revenue, closeadj):
    short = _f05_revenue_cv(revenue, 21)
    long = _f05_revenue_cv(revenue, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_cvcross_63_252_base_v060_signal(revenue, closeadj):
    short = _f05_revenue_cv(revenue, 63)
    long = _f05_revenue_cv(revenue, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Stab cross
def f05urs_f05_utility_revenue_stability_stabcross_21_252_base_v061_signal(revenue, ebitda, closeadj):
    short = _f05_stability_score(revenue, ebitda, 21)
    long = _f05_stability_score(revenue, ebitda, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Smooth cross
def f05urs_f05_utility_revenue_stability_smoothcross_63_252_base_v062_signal(revenue, closeadj):
    short = _f05_revenue_smoothness(revenue, 63)
    long = _f05_revenue_smoothness(revenue, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × revenue size × close
def f05urs_f05_utility_revenue_stability_cvxsize_252d_base_v063_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    s = np.log(revenue.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothxsize_252d_base_v064_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    s = np.log(revenue.abs().replace(0, np.nan))
    result = base * s * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxsize_252d_base_v065_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    s = np.log(revenue.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × close z
def f05urs_f05_utility_revenue_stability_cvxclosez_252d_base_v066_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabxclosez_252d_base_v067_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV × volume z
def f05urs_f05_utility_revenue_stability_cvxvolz_252d_base_v068_signal(revenue, closeadj, volume):
    base = _f05_revenue_cv(revenue, 252)
    result = base * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV log × close
def f05urs_f05_utility_revenue_stability_cvlog_252d_base_v069_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothlog_252d_base_v070_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# CV squared × close
def f05urs_f05_utility_revenue_stability_cvsq_252d_base_v071_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabsq_252d_base_v072_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Acceleration
def f05urs_f05_utility_revenue_stability_cvaccel_252d_base_v073_signal(revenue, closeadj):
    base = _f05_revenue_cv(revenue, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_stabaccel_252d_base_v074_signal(revenue, ebitda, closeadj):
    base = _f05_stability_score(revenue, ebitda, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05urs_f05_utility_revenue_stability_smoothaccel_252d_base_v075_signal(revenue, closeadj):
    base = _f05_revenue_smoothness(revenue, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05urs_f05_utility_revenue_stability_revcv_21d_base_v001_signal,
    f05urs_f05_utility_revenue_stability_revcv_63d_base_v002_signal,
    f05urs_f05_utility_revenue_stability_revcv_126d_base_v003_signal,
    f05urs_f05_utility_revenue_stability_revcv_252d_base_v004_signal,
    f05urs_f05_utility_revenue_stability_revcv_504d_base_v005_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_21d_base_v006_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_63d_base_v007_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_126d_base_v008_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_252d_base_v009_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_504d_base_v010_signal,
    f05urs_f05_utility_revenue_stability_stab_21d_base_v011_signal,
    f05urs_f05_utility_revenue_stability_stab_63d_base_v012_signal,
    f05urs_f05_utility_revenue_stability_stab_126d_base_v013_signal,
    f05urs_f05_utility_revenue_stability_stab_252d_base_v014_signal,
    f05urs_f05_utility_revenue_stability_stab_504d_base_v015_signal,
    f05urs_f05_utility_revenue_stability_cvz_252d_base_v016_signal,
    f05urs_f05_utility_revenue_stability_smoothz_252d_base_v017_signal,
    f05urs_f05_utility_revenue_stability_stabz_252d_base_v018_signal,
    f05urs_f05_utility_revenue_stability_cvstd_252d_base_v019_signal,
    f05urs_f05_utility_revenue_stability_smoothstd_252d_base_v020_signal,
    f05urs_f05_utility_revenue_stability_cvema_252d_base_v021_signal,
    f05urs_f05_utility_revenue_stability_smoothema_252d_base_v022_signal,
    f05urs_f05_utility_revenue_stability_stabema_252d_base_v023_signal,
    f05urs_f05_utility_revenue_stability_cvrank_252d_base_v024_signal,
    f05urs_f05_utility_revenue_stability_smoothrank_252d_base_v025_signal,
    f05urs_f05_utility_revenue_stability_stabrank_252d_base_v026_signal,
    f05urs_f05_utility_revenue_stability_revcv_5d_base_v027_signal,
    f05urs_f05_utility_revenue_stability_revcv_10d_base_v028_signal,
    f05urs_f05_utility_revenue_stability_revcv_42d_base_v029_signal,
    f05urs_f05_utility_revenue_stability_revcv_189d_base_v030_signal,
    f05urs_f05_utility_revenue_stability_revcv_378d_base_v031_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_5d_base_v032_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_42d_base_v033_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_189d_base_v034_signal,
    f05urs_f05_utility_revenue_stability_revsmooth_378d_base_v035_signal,
    f05urs_f05_utility_revenue_stability_stab_5d_base_v036_signal,
    f05urs_f05_utility_revenue_stability_stab_42d_base_v037_signal,
    f05urs_f05_utility_revenue_stability_stab_189d_base_v038_signal,
    f05urs_f05_utility_revenue_stability_cvxvol_63d_base_v039_signal,
    f05urs_f05_utility_revenue_stability_cvxvol_252d_base_v040_signal,
    f05urs_f05_utility_revenue_stability_smoothxvol_252d_base_v041_signal,
    f05urs_f05_utility_revenue_stability_stabxvol_252d_base_v042_signal,
    f05urs_f05_utility_revenue_stability_cvinv_252d_base_v043_signal,
    f05urs_f05_utility_revenue_stability_cvinv_63d_base_v044_signal,
    f05urs_f05_utility_revenue_stability_cvxatr_63d_base_v045_signal,
    f05urs_f05_utility_revenue_stability_cvxatr_252d_base_v046_signal,
    f05urs_f05_utility_revenue_stability_smoothxatr_252d_base_v047_signal,
    f05urs_f05_utility_revenue_stability_stabxatr_252d_base_v048_signal,
    f05urs_f05_utility_revenue_stability_cvxret_63d_base_v049_signal,
    f05urs_f05_utility_revenue_stability_cvxret_252d_base_v050_signal,
    f05urs_f05_utility_revenue_stability_smoothxret_252d_base_v051_signal,
    f05urs_f05_utility_revenue_stability_stabxret_252d_base_v052_signal,
    f05urs_f05_utility_revenue_stability_cvxabsret_252d_base_v053_signal,
    f05urs_f05_utility_revenue_stability_stabxabsret_252d_base_v054_signal,
    f05urs_f05_utility_revenue_stability_cvgap_252d_base_v055_signal,
    f05urs_f05_utility_revenue_stability_cvgap_63d_base_v056_signal,
    f05urs_f05_utility_revenue_stability_smoothgap_252d_base_v057_signal,
    f05urs_f05_utility_revenue_stability_stabgap_252d_base_v058_signal,
    f05urs_f05_utility_revenue_stability_cvcross_21_252_base_v059_signal,
    f05urs_f05_utility_revenue_stability_cvcross_63_252_base_v060_signal,
    f05urs_f05_utility_revenue_stability_stabcross_21_252_base_v061_signal,
    f05urs_f05_utility_revenue_stability_smoothcross_63_252_base_v062_signal,
    f05urs_f05_utility_revenue_stability_cvxsize_252d_base_v063_signal,
    f05urs_f05_utility_revenue_stability_smoothxsize_252d_base_v064_signal,
    f05urs_f05_utility_revenue_stability_stabxsize_252d_base_v065_signal,
    f05urs_f05_utility_revenue_stability_cvxclosez_252d_base_v066_signal,
    f05urs_f05_utility_revenue_stability_stabxclosez_252d_base_v067_signal,
    f05urs_f05_utility_revenue_stability_cvxvolz_252d_base_v068_signal,
    f05urs_f05_utility_revenue_stability_cvlog_252d_base_v069_signal,
    f05urs_f05_utility_revenue_stability_smoothlog_252d_base_v070_signal,
    f05urs_f05_utility_revenue_stability_cvsq_252d_base_v071_signal,
    f05urs_f05_utility_revenue_stability_stabsq_252d_base_v072_signal,
    f05urs_f05_utility_revenue_stability_cvaccel_252d_base_v073_signal,
    f05urs_f05_utility_revenue_stability_stabaccel_252d_base_v074_signal,
    f05urs_f05_utility_revenue_stability_smoothaccel_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_UTILITY_REVENUE_STABILITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f05_utility_revenue_stability_base_001_075_claude: {n_features} features pass")
