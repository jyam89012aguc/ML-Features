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
def _f21_ppe_rejuvenation(capex, ppnenet, depamor):
    # net new ppe added per dollar of depreciation -> higher = rejuvenating
    return (capex - depamor) / ppnenet.replace(0, np.nan).abs()


def _f21_replacement_intensity(capex, depamor):
    # capex over depreciation, classic replacement ratio
    return capex / depamor.replace(0, np.nan).abs()


def _f21_ppe_freshness(ppnenet, depamor, w):
    # implied remaining life of PP&E: net PP&E vs depreciation run-rate
    dep_avg = depamor.rolling(w, min_periods=max(1, w // 2)).mean()
    return ppnenet / dep_avg.replace(0, np.nan).abs()


# v001: replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_base_v001_signal(capex, depamor, closeadj):
    result = _f21_replacement_intensity(capex, depamor) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: 21d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_21d_base_v002_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: 63d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_63d_base_v003_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: 126d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_126d_base_v004_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: 252d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_252d_base_v005_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: 504d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_504d_base_v006_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: 21d std replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintens_std_21d_base_v007_signal(capex, depamor, closeadj):
    result = _std(_f21_replacement_intensity(capex, depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: 63d std replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintens_std_63d_base_v008_signal(capex, depamor, closeadj):
    result = _std(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: 252d std replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintens_std_252d_base_v009_signal(capex, depamor, closeadj):
    result = _std(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: 252d z-score of replacement intensity
def f21smr_f21_specialty_machinery_replacement_replintens_z_252d_base_v010_signal(capex, depamor, closeadj):
    result = _z(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: 504d z-score of replacement intensity
def f21smr_f21_specialty_machinery_replacement_replintens_z_504d_base_v011_signal(capex, depamor, closeadj):
    result = _z(_f21_replacement_intensity(capex, depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: rejuvenation rate * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_base_v012_signal(capex, ppnenet, depamor, closeadj):
    result = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: 21d mean rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_21d_base_v013_signal(capex, ppnenet, depamor, closeadj):
    result = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: 63d mean rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_63d_base_v014_signal(capex, ppnenet, depamor, closeadj):
    result = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: 126d mean rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_126d_base_v015_signal(capex, ppnenet, depamor, closeadj):
    result = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: 252d mean rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_252d_base_v016_signal(capex, ppnenet, depamor, closeadj):
    result = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: 504d mean rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_504d_base_v017_signal(capex, ppnenet, depamor, closeadj):
    result = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: 21d std rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_std_21d_base_v018_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: 63d std rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_std_63d_base_v019_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: 252d std rejuvenation * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_std_252d_base_v020_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021: 252d z-score of rejuvenation
def f21smr_f21_specialty_machinery_replacement_rejuv_z_252d_base_v021_signal(capex, ppnenet, depamor, closeadj):
    result = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: 504d z-score of rejuvenation
def f21smr_f21_specialty_machinery_replacement_rejuv_z_504d_base_v022_signal(capex, ppnenet, depamor, closeadj):
    result = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: ppe freshness 21d * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_21d_base_v023_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: ppe freshness 63d * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_63d_base_v024_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: ppe freshness 126d * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_126d_base_v025_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: ppe freshness 252d * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_252d_base_v026_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: ppe freshness 504d * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_504d_base_v027_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: freshness 252d minus 21d mean (turn signal)
def f21smr_f21_specialty_machinery_replacement_freshness_diff_252_21_base_v028_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (base - _mean(base, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: freshness 504d minus 63d mean
def f21smr_f21_specialty_machinery_replacement_freshness_diff_504_63_base_v029_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504)
    result = (base - _mean(base, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: 252d zscore of freshness 252d
def f21smr_f21_specialty_machinery_replacement_freshness_z_252d_base_v030_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031: 504d zscore of freshness 252d
def f21smr_f21_specialty_machinery_replacement_freshness_z_504d_base_v031_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: rejuvenation vs replacement intensity (orthogonal blend)
def f21smr_f21_specialty_machinery_replacement_rejuv_minus_repl_base_v032_signal(capex, ppnenet, depamor, closeadj):
    a = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    b = _f21_replacement_intensity(capex, depamor)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: rejuvenation times freshness 252
def f21smr_f21_specialty_machinery_replacement_rejuv_x_fresh_252d_base_v033_signal(capex, ppnenet, depamor, closeadj):
    a = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = a * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: replacement intensity / freshness 252 (relative)
def f21smr_f21_specialty_machinery_replacement_repl_div_fresh_252d_base_v034_signal(capex, depamor, ppnenet, closeadj):
    a = _f21_replacement_intensity(capex, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _safe_div(a, f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: 5d mean replacement intensity * closeadj (high freq)
def f21smr_f21_specialty_machinery_replacement_replintensity_5d_base_v035_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036: 10d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_10d_base_v036_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037: 42d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_42d_base_v037_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038: 189d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_189d_base_v038_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: 378d mean replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_replintensity_378d_base_v039_signal(capex, depamor, closeadj):
    result = _mean(_f21_replacement_intensity(capex, depamor), 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: replacement intensity * volume proxy (capex)
def f21smr_f21_specialty_machinery_replacement_replintens_x_capex_base_v040_signal(capex, depamor, closeadj):
    result = _f21_replacement_intensity(capex, depamor) * _mean(capex, 21) / 1e7 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: rejuv * depreciation level
def f21smr_f21_specialty_machinery_replacement_rejuv_x_dep_base_v041_signal(capex, ppnenet, depamor, closeadj):
    result = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * _mean(depamor, 21) / 1e7 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: freshness 252 squared * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_sq_252d_base_v042_signal(ppnenet, depamor, closeadj):
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = f * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: log freshness 252 * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_log_252d_base_v043_signal(ppnenet, depamor, closeadj):
    f = _f21_ppe_freshness(ppnenet, depamor, 252).abs() + 1.0
    result = np.log(f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: rejuvenation cumulative 252 minus 504 (regime shift)
def f21smr_f21_specialty_machinery_replacement_rejuv_regime_base_v044_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = (_mean(base, 252) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: replacement intensity regime (63d vs 252d)
def f21smr_f21_specialty_machinery_replacement_repl_regime_base_v045_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: freshness regime (63 vs 252)
def f21smr_f21_specialty_machinery_replacement_freshness_regime_base_v046_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 63)
    big  = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (base - big) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: replacement intensity above 1 indicator * closeadj
def f21smr_f21_specialty_machinery_replacement_repl_above1_base_v047_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    ind = (base > 1.0).astype(float) * base
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: rejuvenation above 0 streak * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_streak_base_v048_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    pos = (base > 0).astype(float)
    streak = pos.rolling(63, min_periods=21).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: 252d minimum replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_repl_min_252d_base_v049_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: 252d max replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_repl_max_252d_base_v050_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: ema of replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_repl_ema_21d_base_v051_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: ema63 of replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_repl_ema_63d_base_v052_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: rejuv ema 21d
def f21smr_f21_specialty_machinery_replacement_rejuv_ema_21d_base_v053_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: rejuv ema 63d
def f21smr_f21_specialty_machinery_replacement_rejuv_ema_63d_base_v054_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: freshness ema 63d (504 base)
def f21smr_f21_specialty_machinery_replacement_freshness_ema_63d_base_v055_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504)
    result = base.ewm(span=63, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: 21d range of replacement intensity * closeadj
def f21smr_f21_specialty_machinery_replacement_repl_range_21d_base_v056_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rng = base.rolling(21, min_periods=5).max() - base.rolling(21, min_periods=5).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: 63d range of rejuv
def f21smr_f21_specialty_machinery_replacement_rejuv_range_63d_base_v057_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rng = base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: 252d range of freshness
def f21smr_f21_specialty_machinery_replacement_freshness_range_252d_base_v058_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059: rejuvenation rolling quantile (rank) * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_rank_252d_base_v059_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060: replacement rank 252 * closeadj
def f21smr_f21_specialty_machinery_replacement_repl_rank_252d_base_v060_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rk = base.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061: freshness rank 504 * closeadj
def f21smr_f21_specialty_machinery_replacement_freshness_rank_504d_base_v061_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rk = base.rolling(504, min_periods=126).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062: 21d mean rejuv minus 252d mean rejuv (cross)
def f21smr_f21_specialty_machinery_replacement_rejuv_cross_21_252_base_v062_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: 63d std / mean rejuv (CV)
def f21smr_f21_specialty_machinery_replacement_rejuv_cv_63d_base_v063_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    cv = _safe_div(_std(base, 63), _mean(base, 63).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064: replacement intensity CV 252
def f21smr_f21_specialty_machinery_replacement_repl_cv_252d_base_v064_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: freshness CV 252
def f21smr_f21_specialty_machinery_replacement_freshness_cv_252d_base_v065_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: rejuv weighted by capex level
def f21smr_f21_specialty_machinery_replacement_rejuv_capex_weight_base_v066_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    w = capex / (capex.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * w * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: replacement intensity weighted by dep level
def f21smr_f21_specialty_machinery_replacement_repl_dep_weight_base_v067_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    w = depamor / (depamor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * w * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: 5d std rejuv * closeadj (high freq vol)
def f21smr_f21_specialty_machinery_replacement_rejuv_std_5d_base_v068_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: 10d std rejuv * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_std_10d_base_v069_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: 504d std rejuv * closeadj
def f21smr_f21_specialty_machinery_replacement_rejuv_std_504d_base_v070_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: freshness 63 * close (short cycle)
def f21smr_f21_specialty_machinery_replacement_freshness_short_base_v071_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: composite of all three primitives
def f21smr_f21_specialty_machinery_replacement_composite_base_v072_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (r + j + f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: composite weighted average
def f21smr_f21_specialty_machinery_replacement_composite_w_base_v073_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: composite minus 252 mean (decomposed signal)
def f21smr_f21_specialty_machinery_replacement_composite_demean_base_v074_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = r + j + f
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: composite z 252
def f21smr_f21_specialty_machinery_replacement_composite_z_252d_base_v075_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = r + j + f
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21smr_f21_specialty_machinery_replacement_replintensity_base_v001_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_21d_base_v002_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_63d_base_v003_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_126d_base_v004_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_252d_base_v005_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_504d_base_v006_signal,
    f21smr_f21_specialty_machinery_replacement_replintens_std_21d_base_v007_signal,
    f21smr_f21_specialty_machinery_replacement_replintens_std_63d_base_v008_signal,
    f21smr_f21_specialty_machinery_replacement_replintens_std_252d_base_v009_signal,
    f21smr_f21_specialty_machinery_replacement_replintens_z_252d_base_v010_signal,
    f21smr_f21_specialty_machinery_replacement_replintens_z_504d_base_v011_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_base_v012_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_21d_base_v013_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_63d_base_v014_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_126d_base_v015_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_252d_base_v016_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_504d_base_v017_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_21d_base_v018_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_63d_base_v019_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_252d_base_v020_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_z_252d_base_v021_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_z_504d_base_v022_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_21d_base_v023_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_63d_base_v024_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_126d_base_v025_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_252d_base_v026_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_504d_base_v027_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_diff_252_21_base_v028_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_diff_504_63_base_v029_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_z_252d_base_v030_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_z_504d_base_v031_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_minus_repl_base_v032_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_x_fresh_252d_base_v033_signal,
    f21smr_f21_specialty_machinery_replacement_repl_div_fresh_252d_base_v034_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_5d_base_v035_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_10d_base_v036_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_42d_base_v037_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_189d_base_v038_signal,
    f21smr_f21_specialty_machinery_replacement_replintensity_378d_base_v039_signal,
    f21smr_f21_specialty_machinery_replacement_replintens_x_capex_base_v040_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_x_dep_base_v041_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_sq_252d_base_v042_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_log_252d_base_v043_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_regime_base_v044_signal,
    f21smr_f21_specialty_machinery_replacement_repl_regime_base_v045_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_regime_base_v046_signal,
    f21smr_f21_specialty_machinery_replacement_repl_above1_base_v047_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_streak_base_v048_signal,
    f21smr_f21_specialty_machinery_replacement_repl_min_252d_base_v049_signal,
    f21smr_f21_specialty_machinery_replacement_repl_max_252d_base_v050_signal,
    f21smr_f21_specialty_machinery_replacement_repl_ema_21d_base_v051_signal,
    f21smr_f21_specialty_machinery_replacement_repl_ema_63d_base_v052_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_ema_21d_base_v053_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_ema_63d_base_v054_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_ema_63d_base_v055_signal,
    f21smr_f21_specialty_machinery_replacement_repl_range_21d_base_v056_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_range_63d_base_v057_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_range_252d_base_v058_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_rank_252d_base_v059_signal,
    f21smr_f21_specialty_machinery_replacement_repl_rank_252d_base_v060_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_rank_504d_base_v061_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_cross_21_252_base_v062_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_cv_63d_base_v063_signal,
    f21smr_f21_specialty_machinery_replacement_repl_cv_252d_base_v064_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_cv_252d_base_v065_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_capex_weight_base_v066_signal,
    f21smr_f21_specialty_machinery_replacement_repl_dep_weight_base_v067_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_5d_base_v068_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_10d_base_v069_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_504d_base_v070_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_short_base_v071_signal,
    f21smr_f21_specialty_machinery_replacement_composite_base_v072_signal,
    f21smr_f21_specialty_machinery_replacement_composite_w_base_v073_signal,
    f21smr_f21_specialty_machinery_replacement_composite_demean_base_v074_signal,
    f21smr_f21_specialty_machinery_replacement_composite_z_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_SPECIALTY_MACHINERY_REPLACEMENT_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {"closeadj": closeadj, "capex": capex, "depamor": depamor, "ppnenet": ppnenet}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f21_ppe_rejuvenation", "_f21_replacement_intensity", "_f21_ppe_freshness")
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
    print(f"OK f21_specialty_machinery_replacement_base_001_075_claude: {n_features} features pass")
