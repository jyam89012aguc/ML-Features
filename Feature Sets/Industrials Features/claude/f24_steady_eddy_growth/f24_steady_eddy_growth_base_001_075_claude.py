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
def _f24_growth_consistency(revenue, w):
    # mean growth minus std growth (positive when steady and rising)
    g = revenue.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f24_growth_cv(revenue, w):
    # coefficient of variation of growth
    g = revenue.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / (mu.abs() + 1e-9)


def _f24_steady_growth_score(revenue, netinc, w):
    # both revenue and netinc are steady positive
    rg = revenue.pct_change(periods=w)
    ig = netinc.pct_change(periods=w)
    rmu = rg.rolling(w, min_periods=max(1, w // 2)).mean()
    imu = ig.rolling(w, min_periods=max(1, w // 2)).mean()
    rsd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    isd = ig.rolling(w, min_periods=max(1, w // 2)).std()
    return (rmu + imu) - (rsd + isd)


# v001..v025 consistency
def f24seg_f24_steady_eddy_growth_consistency_21d_base_v001_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_63d_base_v002_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_126d_base_v003_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_252d_base_v004_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_504d_base_v005_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_42d_base_v006_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_189d_base_v007_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_378d_base_v008_signal(revenue, closeadj):
    result = _f24_growth_consistency(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_mean_252d_base_v009_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_z_252d_base_v010_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_z_504d_base_v011_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_std_252d_base_v012_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_ema_63d_base_v013_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_sq_base_v014_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_log_base_v015_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_xclose2_base_v016_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_rank252_base_v017_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_cross_63_252_base_v018_signal(revenue, closeadj):
    a = _f24_growth_consistency(revenue, 63)
    b = _f24_growth_consistency(revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_min_252d_base_v019_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_max_252d_base_v020_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_range_252d_base_v021_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_med_252d_base_v022_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_cv_252d_base_v023_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_demean_base_v024_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_abs_base_v025_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026..v050 growth CV
def f24seg_f24_steady_eddy_growth_cv_21d_base_v026_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_63d_base_v027_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_126d_base_v028_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_252d_base_v029_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_504d_base_v030_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_42d_base_v031_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_189d_base_v032_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_378d_base_v033_signal(revenue, closeadj):
    result = _f24_growth_cv(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_mean_252d_base_v034_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_z_252d_base_v035_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_z_504d_base_v036_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_std_252d_base_v037_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_ema_63d_base_v038_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_inv_base_v039_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = (1.0 / (base.abs() + 1e-6)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_log_base_v040_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_sq_base_v041_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_sqrt_base_v042_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_rank252_base_v043_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_cross_63_252_base_v044_signal(revenue, closeadj):
    a = _f24_growth_cv(revenue, 63)
    b = _f24_growth_cv(revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_min_252d_base_v045_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_max_252d_base_v046_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_range_252d_base_v047_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_med_252d_base_v048_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_demean_base_v049_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_xclose2_base_v050_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v051..v075 steady score & combos
def f24seg_f24_steady_eddy_growth_score_21d_base_v051_signal(revenue, netinc, closeadj):
    result = _f24_steady_growth_score(revenue, netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_63d_base_v052_signal(revenue, netinc, closeadj):
    result = _f24_steady_growth_score(revenue, netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_126d_base_v053_signal(revenue, netinc, closeadj):
    result = _f24_steady_growth_score(revenue, netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_252d_base_v054_signal(revenue, netinc, closeadj):
    result = _f24_steady_growth_score(revenue, netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_504d_base_v055_signal(revenue, netinc, closeadj):
    result = _f24_steady_growth_score(revenue, netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_42d_base_v056_signal(revenue, netinc, closeadj):
    result = _f24_steady_growth_score(revenue, netinc, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_189d_base_v057_signal(revenue, netinc, closeadj):
    result = _f24_steady_growth_score(revenue, netinc, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_mean_252d_base_v058_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_z_252d_base_v059_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_std_252d_base_v060_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_ema_63d_base_v061_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_sq_base_v062_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_rank252_base_v063_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_cross_63_252_base_v064_signal(revenue, netinc, closeadj):
    a = _f24_steady_growth_score(revenue, netinc, 63)
    b = _f24_steady_growth_score(revenue, netinc, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_range_252d_base_v065_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_minus_cv_base_v066_signal(revenue, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    result = (c - v) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_times_score_base_v067_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    result = c * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_times_score_base_v068_signal(revenue, netinc, closeadj):
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    result = v * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_triple_w_base_v069_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    result = (0.4 * c + 0.4 * s - 0.2 * v) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_triple_sum_base_v070_signal(revenue, netinc, closeadj):
    c = _f24_growth_consistency(revenue, 63)
    v = _f24_growth_cv(revenue, 63)
    s = _f24_steady_growth_score(revenue, netinc, 63)
    result = (c + s + v) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_xrevenue_base_v071_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_xrevenue_base_v072_signal(revenue, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_cv_xrevenue_base_v073_signal(revenue, closeadj):
    base = _f24_growth_cv(revenue, 63)
    rg = revenue / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_consistency_xnetinc_base_v074_signal(revenue, netinc, closeadj):
    base = _f24_growth_consistency(revenue, 63)
    ng = netinc / (netinc.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f24seg_f24_steady_eddy_growth_score_xnetinc_base_v075_signal(revenue, netinc, closeadj):
    base = _f24_steady_growth_score(revenue, netinc, 63)
    ng = netinc / (netinc.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * ng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24seg_f24_steady_eddy_growth_consistency_21d_base_v001_signal,
    f24seg_f24_steady_eddy_growth_consistency_63d_base_v002_signal,
    f24seg_f24_steady_eddy_growth_consistency_126d_base_v003_signal,
    f24seg_f24_steady_eddy_growth_consistency_252d_base_v004_signal,
    f24seg_f24_steady_eddy_growth_consistency_504d_base_v005_signal,
    f24seg_f24_steady_eddy_growth_consistency_42d_base_v006_signal,
    f24seg_f24_steady_eddy_growth_consistency_189d_base_v007_signal,
    f24seg_f24_steady_eddy_growth_consistency_378d_base_v008_signal,
    f24seg_f24_steady_eddy_growth_consistency_mean_252d_base_v009_signal,
    f24seg_f24_steady_eddy_growth_consistency_z_252d_base_v010_signal,
    f24seg_f24_steady_eddy_growth_consistency_z_504d_base_v011_signal,
    f24seg_f24_steady_eddy_growth_consistency_std_252d_base_v012_signal,
    f24seg_f24_steady_eddy_growth_consistency_ema_63d_base_v013_signal,
    f24seg_f24_steady_eddy_growth_consistency_sq_base_v014_signal,
    f24seg_f24_steady_eddy_growth_consistency_log_base_v015_signal,
    f24seg_f24_steady_eddy_growth_consistency_xclose2_base_v016_signal,
    f24seg_f24_steady_eddy_growth_consistency_rank252_base_v017_signal,
    f24seg_f24_steady_eddy_growth_consistency_cross_63_252_base_v018_signal,
    f24seg_f24_steady_eddy_growth_consistency_min_252d_base_v019_signal,
    f24seg_f24_steady_eddy_growth_consistency_max_252d_base_v020_signal,
    f24seg_f24_steady_eddy_growth_consistency_range_252d_base_v021_signal,
    f24seg_f24_steady_eddy_growth_consistency_med_252d_base_v022_signal,
    f24seg_f24_steady_eddy_growth_consistency_cv_252d_base_v023_signal,
    f24seg_f24_steady_eddy_growth_consistency_demean_base_v024_signal,
    f24seg_f24_steady_eddy_growth_consistency_abs_base_v025_signal,
    f24seg_f24_steady_eddy_growth_cv_21d_base_v026_signal,
    f24seg_f24_steady_eddy_growth_cv_63d_base_v027_signal,
    f24seg_f24_steady_eddy_growth_cv_126d_base_v028_signal,
    f24seg_f24_steady_eddy_growth_cv_252d_base_v029_signal,
    f24seg_f24_steady_eddy_growth_cv_504d_base_v030_signal,
    f24seg_f24_steady_eddy_growth_cv_42d_base_v031_signal,
    f24seg_f24_steady_eddy_growth_cv_189d_base_v032_signal,
    f24seg_f24_steady_eddy_growth_cv_378d_base_v033_signal,
    f24seg_f24_steady_eddy_growth_cv_mean_252d_base_v034_signal,
    f24seg_f24_steady_eddy_growth_cv_z_252d_base_v035_signal,
    f24seg_f24_steady_eddy_growth_cv_z_504d_base_v036_signal,
    f24seg_f24_steady_eddy_growth_cv_std_252d_base_v037_signal,
    f24seg_f24_steady_eddy_growth_cv_ema_63d_base_v038_signal,
    f24seg_f24_steady_eddy_growth_cv_inv_base_v039_signal,
    f24seg_f24_steady_eddy_growth_cv_log_base_v040_signal,
    f24seg_f24_steady_eddy_growth_cv_sq_base_v041_signal,
    f24seg_f24_steady_eddy_growth_cv_sqrt_base_v042_signal,
    f24seg_f24_steady_eddy_growth_cv_rank252_base_v043_signal,
    f24seg_f24_steady_eddy_growth_cv_cross_63_252_base_v044_signal,
    f24seg_f24_steady_eddy_growth_cv_min_252d_base_v045_signal,
    f24seg_f24_steady_eddy_growth_cv_max_252d_base_v046_signal,
    f24seg_f24_steady_eddy_growth_cv_range_252d_base_v047_signal,
    f24seg_f24_steady_eddy_growth_cv_med_252d_base_v048_signal,
    f24seg_f24_steady_eddy_growth_cv_demean_base_v049_signal,
    f24seg_f24_steady_eddy_growth_cv_xclose2_base_v050_signal,
    f24seg_f24_steady_eddy_growth_score_21d_base_v051_signal,
    f24seg_f24_steady_eddy_growth_score_63d_base_v052_signal,
    f24seg_f24_steady_eddy_growth_score_126d_base_v053_signal,
    f24seg_f24_steady_eddy_growth_score_252d_base_v054_signal,
    f24seg_f24_steady_eddy_growth_score_504d_base_v055_signal,
    f24seg_f24_steady_eddy_growth_score_42d_base_v056_signal,
    f24seg_f24_steady_eddy_growth_score_189d_base_v057_signal,
    f24seg_f24_steady_eddy_growth_score_mean_252d_base_v058_signal,
    f24seg_f24_steady_eddy_growth_score_z_252d_base_v059_signal,
    f24seg_f24_steady_eddy_growth_score_std_252d_base_v060_signal,
    f24seg_f24_steady_eddy_growth_score_ema_63d_base_v061_signal,
    f24seg_f24_steady_eddy_growth_score_sq_base_v062_signal,
    f24seg_f24_steady_eddy_growth_score_rank252_base_v063_signal,
    f24seg_f24_steady_eddy_growth_score_cross_63_252_base_v064_signal,
    f24seg_f24_steady_eddy_growth_score_range_252d_base_v065_signal,
    f24seg_f24_steady_eddy_growth_consistency_minus_cv_base_v066_signal,
    f24seg_f24_steady_eddy_growth_consistency_times_score_base_v067_signal,
    f24seg_f24_steady_eddy_growth_cv_times_score_base_v068_signal,
    f24seg_f24_steady_eddy_growth_triple_w_base_v069_signal,
    f24seg_f24_steady_eddy_growth_triple_sum_base_v070_signal,
    f24seg_f24_steady_eddy_growth_score_xrevenue_base_v071_signal,
    f24seg_f24_steady_eddy_growth_consistency_xrevenue_base_v072_signal,
    f24seg_f24_steady_eddy_growth_cv_xrevenue_base_v073_signal,
    f24seg_f24_steady_eddy_growth_consistency_xnetinc_base_v074_signal,
    f24seg_f24_steady_eddy_growth_score_xnetinc_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_STEADY_EDDY_GROWTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")

    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc}

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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f24_steady_eddy_growth_base_001_075_claude: {n_features} features pass")
