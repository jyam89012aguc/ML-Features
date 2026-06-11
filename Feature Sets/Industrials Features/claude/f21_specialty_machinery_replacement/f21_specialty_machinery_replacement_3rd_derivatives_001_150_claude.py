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


# ===== folder domain primitives =====
def _f21_ppe_rejuvenation(capex, ppnenet, depamor):
    return (capex - depamor) / ppnenet.replace(0, np.nan).abs()


def _f21_replacement_intensity(capex, depamor):
    return capex / depamor.replace(0, np.nan).abs()


def _f21_ppe_freshness(ppnenet, depamor, w):
    dep_avg = depamor.rolling(w, min_periods=max(1, w // 2)).mean()
    return ppnenet / dep_avg.replace(0, np.nan).abs()


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


# v001..v010 replacement intensity * close jerk windows
@_add
def f21smr_f21_specialty_machinery_replacement_repl_5d_jerk_v001_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_10d_jerk_v002_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_21d_jerk_v003_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_42d_jerk_v004_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_63d_jerk_v005_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_126d_jerk_v006_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_252d_jerk_v007_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w21_21d_jerk_v008_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w63_21d_jerk_v009_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w252_63d_jerk_v010_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v011..v020 rejuv jerk
@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_5d_jerk_v011_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_10d_jerk_v012_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_21d_jerk_v013_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_42d_jerk_v014_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_63d_jerk_v015_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_126d_jerk_v016_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_252d_jerk_v017_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w21_21d_jerk_v018_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w63_21d_jerk_v019_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w252_63d_jerk_v020_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v021..v030 freshness jerk
@_add
def f21smr_f21_specialty_machinery_replacement_freshness_5d_jerk_v021_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_10d_jerk_v022_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_21d_jerk_v023_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_42d_jerk_v024_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_63d_jerk_v025_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_126d_jerk_v026_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w63_21d_jerk_v027_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w504_21d_jerk_v028_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w504_63d_jerk_v029_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w126_63d_jerk_v030_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031..v045 ema base then jerk
@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema21_21d_jerk_v031_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema63_21d_jerk_v032_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema126_21d_jerk_v033_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema252_63d_jerk_v034_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema21_21d_jerk_v035_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema63_21d_jerk_v036_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema126_21d_jerk_v037_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema252_63d_jerk_v038_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema21_21d_jerk_v039_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema63_21d_jerk_v040_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema126_21d_jerk_v041_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema252_63d_jerk_v042_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_std21_21d_jerk_v043_signal(capex, depamor, closeadj):
    base = _std(_f21_replacement_intensity(capex, depamor), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_std21_21d_jerk_v044_signal(capex, ppnenet, depamor, closeadj):
    base = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_std21_21d_jerk_v045_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _std(base, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v046..v060 z-scored jerk
@_add
def f21smr_f21_specialty_machinery_replacement_repl_z252_21d_jerk_v046_signal(capex, depamor, closeadj):
    base = _z(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_z252_63d_jerk_v047_signal(capex, depamor, closeadj):
    base = _z(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_z252_21d_jerk_v048_signal(capex, ppnenet, depamor, closeadj):
    base = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_z252_63d_jerk_v049_signal(capex, ppnenet, depamor, closeadj):
    base = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_z252_21d_jerk_v050_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_z252_63d_jerk_v051_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _z(base, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_log_21d_jerk_v052_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_log_21d_jerk_v053_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() + 1e-6
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_log_21d_jerk_v054_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_sqrt_21d_jerk_v055_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_sqrt_21d_jerk_v056_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs()
    base = np.sqrt(base + 1e-12) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_sqrt_21d_jerk_v057_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_sq_21d_jerk_v058_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_sq_21d_jerk_v059_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_sq_21d_jerk_v060_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base * base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v061..v080 composite jerks
@_add
def f21smr_f21_specialty_machinery_replacement_comp_rj_21d_jerk_v061_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r + j) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rj_63d_jerk_v062_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r + j) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_21d_jerk_v063_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_63d_jerk_v064_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_126d_jerk_v065_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxj_21d_jerk_v066_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r * j) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxj_63d_jerk_v067_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r * j) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxjxf_21d_jerk_v068_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r * j * f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxjxf_63d_jerk_v069_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r * j * f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_diff_rj_21d_jerk_v070_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (j - r) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_diff_rj_63d_jerk_v071_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (j - r) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_21d_jerk_v072_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (j + f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_63d_jerk_v073_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (j + f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rf_21d_jerk_v074_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rf_63d_jerk_v075_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_21d_jerk_v076_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_63d_jerk_v077_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_126d_jerk_v078_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_rank252_21d_jerk_v079_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_rank252_21d_jerk_v080_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081..v100 small-window jerks and ranges
@_add
def f21smr_f21_specialty_machinery_replacement_freshness_rank504_21d_jerk_v081_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rk = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_rank252_63d_jerk_v082_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(rk, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_range21_21d_jerk_v083_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rng = (base.rolling(21, min_periods=5).max() - base.rolling(21, min_periods=5).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_range63_21d_jerk_v084_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rng = (base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()) * closeadj
    result = _jerk(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_range252_63d_jerk_v085_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _jerk(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_med252_21d_jerk_v086_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_med252_21d_jerk_v087_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_med252_21d_jerk_v088_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_max252_63d_jerk_v089_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_min252_63d_jerk_v090_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_max252_63d_jerk_v091_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_inv_21d_jerk_v092_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (1.0 / (base.abs() + 1e-9)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_abs_21d_jerk_v093_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_abs_63d_jerk_v094_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_pulse_63d_jerk_v095_signal(ppnenet, depamor, closeadj):
    a = _f21_ppe_freshness(ppnenet, depamor, 63)
    b = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_regime_21d_jerk_v096_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (_mean(base, 63) - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_regime_21d_jerk_v097_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (_mean(base, 63) - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_regime_21d_jerk_v098_signal(ppnenet, depamor, closeadj):
    a = _f21_ppe_freshness(ppnenet, depamor, 63)
    b = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (a - b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn21_jerk_v099_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    base = _slope(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn21_jerk_v100_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    base = _slope(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v101..v150 large-window and exotic
@_add
def f21smr_f21_specialty_machinery_replacement_repl_w5_21d_jerk_v101_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w10_21d_jerk_v102_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w42_21d_jerk_v103_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w126_21d_jerk_v104_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w189_21d_jerk_v105_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w378_21d_jerk_v106_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w504_42d_jerk_v107_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w5_21d_jerk_v108_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w10_21d_jerk_v109_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w42_21d_jerk_v110_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w126_21d_jerk_v111_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w189_21d_jerk_v112_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w378_21d_jerk_v113_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w504_42d_jerk_v114_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w42_21d_jerk_v115_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w189_21d_jerk_v116_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w378_21d_jerk_v117_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w63_42d_jerk_v118_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w504_42d_jerk_v119_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w252_42d_jerk_v120_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_21d_jerk2_v121_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 504)
    base = (j + f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_63d_jerk2_v122_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 504)
    base = (j + f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn42_jerk_v123_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    base = _slope(base, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn42_jerk_v124_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    base = _slope(base, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn42_jerk_v125_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    base = _slope(base, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_above1_21d_jerk_v126_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    ind = (base > 1.0).astype(float) * base
    base = ind * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_pos_streak_21d_jerk_v127_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    pos = (base > 0).astype(float)
    streak = pos.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_diff_jf_21d_jerk_v128_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (j - f) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_diff_jf_63d_jerk_v129_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (j - f) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_demean_21d_jerk_v130_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_demean_21d_jerk_v131_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_demean_21d_jerk_v132_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (base - _mean(base, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_demean_63d_jerk_v133_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (base - _mean(base, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_demean_63d_jerk_v134_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (base - _mean(base, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_demean_63d_jerk_v135_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (base - _mean(base, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_dn21_jerk_v136_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    base = _slope(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_dn63_jerk_v137_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    base = _slope(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_xclose2_21d_jerk_v138_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_xclose2_21d_jerk_v139_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_xclose2_21d_jerk_v140_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base * closeadj * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_capex_weight_21d_jerk_v141_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    w = capex / (capex.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * w * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_capex_weight_21d_jerk_v142_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    w = capex / (capex.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * w * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dep_weight_21d_jerk_v143_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    w = depamor / (depamor.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * w * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_w63_21d_jerk_v144_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _mean(r + j + f, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_w252_63d_jerk_v145_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _mean(r + j + f, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_inv_63d_jerk_v146_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (1.0 / (base.abs() + 1e-9)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_med504_63d_jerk_v147_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.rolling(504, min_periods=126).median() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_med504_63d_jerk_v148_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.rolling(504, min_periods=126).median() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_z63_21d_jerk_v149_signal(capex, depamor, closeadj):
    base = _z(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_z63_21d_jerk_v150_signal(capex, ppnenet, depamor, closeadj):
    base = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_SPECIALTY_MACHINERY_REPLACEMENT_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f21_specialty_machinery_replacement_3rd_derivatives_001_150_claude: {n_features} features pass")
