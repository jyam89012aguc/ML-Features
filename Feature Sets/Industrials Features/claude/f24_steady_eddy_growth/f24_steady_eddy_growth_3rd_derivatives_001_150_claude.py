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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f24_growth_consistency(revenue, w):
    g = revenue.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f24_growth_cv(revenue, w):
    g = revenue.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / (mu.abs() + 1e-9)


def _f24_steady_growth_score(revenue, netinc, w):
    rg = revenue.pct_change(periods=w)
    ig = netinc.pct_change(periods=w)
    rmu = rg.rolling(w, min_periods=max(1, w // 2)).mean()
    imu = ig.rolling(w, min_periods=max(1, w // 2)).mean()
    rsd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    isd = ig.rolling(w, min_periods=max(1, w // 2)).std()
    return (rmu + imu) - (rsd + isd)


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


# Consistency slopes (50)
@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_5d_jerk_v001_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_10d_jerk_v002_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_21d_jerk_v003_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_42d_jerk_v004_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_63d_jerk_v005_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_126d_jerk_v006_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_252d_jerk_v007_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w21_21d_jerk_v008_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w126_21d_jerk_v009_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w252_21d_jerk_v010_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w252_63d_jerk_v011_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w504_63d_jerk_v012_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w42_21d_jerk_v013_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w189_21d_jerk_v014_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w378_42d_jerk_v015_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_dn21_jerk_v016_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_dn63_jerk_v017_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_dn126_jerk_v018_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_ema21_21d_jerk_v019_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_ema63_21d_jerk_v020_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_ema252_63d_jerk_v021_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_z252_21d_jerk_v022_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_std63_21d_jerk_v023_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_log_21d_jerk_v024_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_sq_21d_jerk_v025_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_rank_21d_jerk_v026_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_med_21d_jerk_v027_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_range_21d_jerk_v028_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_demean_21d_jerk_v029_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_xrev_21d_jerk_v030_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * rg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# CV slopes
@_add
def f24seg_f24_steady_eddy_growth_cv_w63_5d_jerk_v031_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_10d_jerk_v032_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_21d_jerk_v033_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_42d_jerk_v034_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_63d_jerk_v035_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_126d_jerk_v036_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_252d_jerk_v037_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w21_21d_jerk_v038_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w126_21d_jerk_v039_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w252_21d_jerk_v040_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w252_63d_jerk_v041_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w504_63d_jerk_v042_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w42_21d_jerk_v043_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_dn21_jerk_v044_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_dn63_jerk_v045_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_ema21_21d_jerk_v046_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_ema63_21d_jerk_v047_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_ema252_63d_jerk_v048_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_z252_21d_jerk_v049_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_std63_21d_jerk_v050_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_log_21d_jerk_v051_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_sq_21d_jerk_v052_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_inv_21d_jerk_v053_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = (1.0 / (base.abs() + 1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_rank_21d_jerk_v054_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_med_21d_jerk_v055_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_range_21d_jerk_v056_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_demean_21d_jerk_v057_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_xrev_21d_jerk_v058_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * rg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Score slopes
@_add
def f24seg_f24_steady_eddy_growth_score_w63_5d_jerk_v059_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_10d_jerk_v060_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_21d_jerk_v061_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_42d_jerk_v062_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_63d_jerk_v063_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_126d_jerk_v064_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w21_21d_jerk_v065_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w126_21d_jerk_v066_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w252_21d_jerk_v067_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w252_63d_jerk_v068_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w504_63d_jerk_v069_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w42_21d_jerk_v070_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w189_21d_jerk_v071_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w378_42d_jerk_v072_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_dn21_jerk_v073_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_dn63_jerk_v074_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_ema21_21d_jerk_v075_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_ema63_21d_jerk_v076_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_ema252_63d_jerk_v077_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_z252_21d_jerk_v078_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_std63_21d_jerk_v079_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = _std(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_log_21d_jerk_v080_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_sq_21d_jerk_v081_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_inv_21d_jerk_v082_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = (1.0 / (base.abs() + 1e-6)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_rank_21d_jerk_v083_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_med_21d_jerk_v084_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_range_21d_jerk_v085_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_demean_21d_jerk_v086_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_xrev_21d_jerk_v087_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * rg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_xnetinc_21d_jerk_v088_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    ng = netinc / (netinc.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * ng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Composites slopes
@_add
def f24seg_f24_steady_eddy_growth_consistency_minus_cv_21d_jerk_v089_signal(revenue, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    base = (c - v) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_times_score_21d_jerk_v090_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    base = c * s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_times_score_21d_jerk_v091_signal(revenue, netinc, closeadj):
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    base = v * s * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_triple_w_21d_jerk_v092_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    base = (0.4 * c + 0.4 * s - 0.2 * v) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_triple_sum_21d_jerk_v093_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    base = (c + s + v) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_triple_sum_63d_jerk_v094_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    base = (c + s + v) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_cross_63_252_jerk_v095_signal(revenue, closeadj):
    a = _f24_growth_consistency(revenue, 63)
    b = _f24_growth_consistency(revenue, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_cross_63_252_jerk_v096_signal(revenue, closeadj):
    a = _f24_growth_cv(revenue, 63)
    b = _f24_growth_cv(revenue, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_cross_63_252_jerk_v097_signal(revenue, netinc, closeadj):
    a = _f24_steady_growth_score(revenue, netinc, 63)
    b = _f24_steady_growth_score(revenue, netinc, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_xebitda_21d_jerk_v098_signal(revenue, ebitda, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * eg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_xebitda_21d_jerk_v099_signal(revenue, ebitda, closeadj):
    base = _f24_growth_cv(revenue, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * eg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_xebitda_21d_jerk_v100_signal(revenue, netinc, ebitda, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * eg * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 50 more slopes with smoothing combos
@_add
def f24seg_f24_steady_eddy_growth_consistency_w252_w42_21d_jerk_v101_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 252), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w252_w42_21d_jerk_v102_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 252), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w252_w42_21d_jerk_v103_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 252), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_w126_63d_jerk_v104_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_w126_63d_jerk_v105_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_w126_63d_jerk_v106_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 63), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w504_w63_21d_jerk_v107_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 504), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w504_w63_21d_jerk_v108_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 504), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w504_w63_21d_jerk_v109_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 504), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_w63_5d_jerk_v110_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_w63_5d_jerk_v111_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_w63_5d_jerk_v112_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_w63_42d_jerk_v113_signal(revenue, closeadj):
    base = _mean(_f24_growth_consistency(revenue, 63), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_w63_42d_jerk_v114_signal(revenue, closeadj):
    base = _mean(_f24_growth_cv(revenue, 63), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_w63_42d_jerk_v115_signal(revenue, netinc, closeadj):
    base = _mean(_f24_steady_growth_score(revenue, netinc, 63), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_dn5_jerk_v116_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_dn5_jerk_v117_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_dn5_jerk_v118_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w63_dn252_jerk_v119_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w63_dn252_jerk_v120_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w63_dn252_jerk_v121_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_z63_21d_jerk_v122_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = _z(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_z63_21d_jerk_v123_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = _z(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_z63_21d_jerk_v124_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = _z(base, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_ema126_63d_jerk_v125_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_ema126_63d_jerk_v126_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_ema126_63d_jerk_v127_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_xclose2_21d_jerk_v128_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_xclose2_21d_jerk_v129_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_xclose2_21d_jerk_v130_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63) * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w42_5d_jerk_v131_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w42_5d_jerk_v132_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w42_5d_jerk_v133_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w189_42d_jerk_v134_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w189_42d_jerk_v135_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w189_42d_jerk_v136_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_w378_63d_jerk_v137_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_w378_63d_jerk_v138_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_w378_63d_jerk_v139_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_streak_pos_21d_jerk_v140_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_streak_low_21d_jerk_v141_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    low = (base < base.rolling(252, min_periods=63).median()).astype(float)
    streak = low.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_streak_pos_21d_jerk_v142_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_pos_above_21d_jerk_v143_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base * closeadj
    result = _jerk(ind, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_above_21d_jerk_v144_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base * closeadj
    result = _jerk(ind, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_above_21d_jerk_v145_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base * closeadj
    result = _jerk(ind, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_sign_21d_jerk_v146_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    sg = np.sign(base) * closeadj
    result = _jerk(sg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_cv_sign_21d_jerk_v147_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    sg = np.sign(base) * closeadj
    result = _jerk(sg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_sign_21d_jerk_v148_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    sg = np.sign(base) * closeadj
    result = _jerk(sg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_consistency_div_cv_21d_jerk_v149_signal(revenue, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    base = _safe_div(c, v.abs() + 1e-6) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f24seg_f24_steady_eddy_growth_score_div_cv_21d_jerk_v150_signal(revenue, netinc, closeadj):
    s = _f24_steady_growth_score(revenue, netinc, 63)
    v = _f24_growth_cv(revenue, 63)
    base = _safe_div(s, v.abs() + 1e-6) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_STEADY_EDDY_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "ebitda": ebitda}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f24_growth_consistency", "_f24_growth_cv", "_f24_steady_growth_score")
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
    print(f"OK f24_steady_eddy_growth_3rd_derivatives_001_150_claude: {n_features} features pass")

