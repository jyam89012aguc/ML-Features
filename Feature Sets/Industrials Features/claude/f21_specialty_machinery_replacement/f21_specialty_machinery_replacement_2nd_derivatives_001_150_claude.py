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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f21_ppe_rejuvenation(capex, ppnenet, depamor):
    return (capex - depamor) / ppnenet.replace(0, np.nan).abs()


def _f21_replacement_intensity(capex, depamor):
    return capex / depamor.replace(0, np.nan).abs()


def _f21_ppe_freshness(ppnenet, depamor, w):
    dep_avg = depamor.rolling(w, min_periods=max(1, w // 2)).mean()
    return ppnenet / dep_avg.replace(0, np.nan).abs()


def _make_slope_repl(window_slope):
    def fn(capex, depamor, closeadj):
        base = _f21_replacement_intensity(capex, depamor) * closeadj
        result = _slope_diff_norm(base, window_slope)
        return result.replace([np.inf, -np.inf], np.nan)
    return fn


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


# v001..v010: replacement intensity * close, slope over varied windows
@_add
def f21smr_f21_specialty_machinery_replacement_repl_5d_slope_v001_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_10d_slope_v002_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_21d_slope_v003_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_42d_slope_v004_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_63d_slope_v005_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_126d_slope_v006_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_252d_slope_v007_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn5_slope_v008_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn21_slope_v009_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn63_slope_v010_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v011..v020: rejuvenation * close slopes
@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_5d_slope_v011_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_10d_slope_v012_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_21d_slope_v013_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_42d_slope_v014_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_63d_slope_v015_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_126d_slope_v016_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_252d_slope_v017_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn21_slope_v018_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn63_slope_v019_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn252_slope_v020_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v021..v030: freshness 252 * close slopes
@_add
def f21smr_f21_specialty_machinery_replacement_freshness_5d_slope_v021_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_10d_slope_v022_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_21d_slope_v023_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_42d_slope_v024_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_63d_slope_v025_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_126d_slope_v026_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_252d_slope_v027_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn21_slope_v028_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn63_slope_v029_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn126_slope_v030_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v031..v045: replacement intensity at various smoothing then slope
@_add
def f21smr_f21_specialty_machinery_replacement_repl_mean21_5d_slope_v031_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_mean21_21d_slope_v032_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_mean63_21d_slope_v033_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_mean63_63d_slope_v034_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_mean252_63d_slope_v035_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_mean252_126d_slope_v036_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema63_21d_slope_v037_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema126_21d_slope_v038_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema252_63d_slope_v039_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_std21_21d_slope_v040_signal(capex, depamor, closeadj):
    base = _std(_f21_replacement_intensity(capex, depamor), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_std63_21d_slope_v041_signal(capex, depamor, closeadj):
    base = _std(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_std252_63d_slope_v042_signal(capex, depamor, closeadj):
    base = _std(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_z252_21d_slope_v043_signal(capex, depamor, closeadj):
    base = _z(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_z252_63d_slope_v044_signal(capex, depamor, closeadj):
    base = _z(_f21_replacement_intensity(capex, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_med63_63d_slope_v045_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.rolling(63, min_periods=21).median() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046..v060: rejuv at various smoothing then slope
@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_mean21_5d_slope_v046_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_mean21_21d_slope_v047_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_mean63_21d_slope_v048_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_mean63_63d_slope_v049_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_mean252_63d_slope_v050_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_mean252_126d_slope_v051_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema63_21d_slope_v052_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema126_21d_slope_v053_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema252_63d_slope_v054_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_std21_21d_slope_v055_signal(capex, ppnenet, depamor, closeadj):
    base = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_std63_21d_slope_v056_signal(capex, ppnenet, depamor, closeadj):
    base = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_std252_63d_slope_v057_signal(capex, ppnenet, depamor, closeadj):
    base = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_z252_21d_slope_v058_signal(capex, ppnenet, depamor, closeadj):
    base = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_z252_63d_slope_v059_signal(capex, ppnenet, depamor, closeadj):
    base = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_med63_63d_slope_v060_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.rolling(63, min_periods=21).median() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061..v075: freshness windows then slopes
@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w63_21d_slope_v061_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w126_21d_slope_v062_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w504_21d_slope_v063_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w63_63d_slope_v064_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w504_63d_slope_v065_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema63_21d_slope_v066_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema126_21d_slope_v067_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema252_63d_slope_v068_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_std21_21d_slope_v069_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _std(base, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_std63_21d_slope_v070_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _std(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_z252_21d_slope_v071_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_z252_63d_slope_v072_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_w504_126d_slope_v073_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_med252_63d_slope_v074_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_med504_126d_slope_v075_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v076..v090: composite slopes
@_add
def f21smr_f21_specialty_machinery_replacement_comp_rj_21d_slope_v076_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r + j) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rj_63d_slope_v077_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r + j) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_21d_slope_v078_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_63d_slope_v079_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_126d_slope_v080_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxj_21d_slope_v081_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r * j) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxj_63d_slope_v082_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r * j) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxjxf_21d_slope_v083_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r * j * f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rxjxf_63d_slope_v084_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r * j * f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_diff_rj_21d_slope_v085_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (j - r) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_diff_rj_63d_slope_v086_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (j - r) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_21d_slope_v087_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (j + f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_63d_slope_v088_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (j + f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rf_21d_slope_v089_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rf_63d_slope_v090_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091..v110: cross-window cross-primitive slope variants
@_add
def f21smr_f21_specialty_machinery_replacement_repl_log_21d_slope_v091_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_log_21d_slope_v092_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() + 1e-6
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_log_21d_slope_v093_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_sqrt_21d_slope_v094_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_sqrt_21d_slope_v095_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs()
    base = np.sqrt(base + 1e-12) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_sqrt_21d_slope_v096_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252).abs()
    base = np.sqrt(base + 1e-9) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_sq_21d_slope_v097_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_sq_21d_slope_v098_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_sq_21d_slope_v099_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_inv_21d_slope_v100_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (1.0 / (base.abs() + 1e-9)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_abs_21d_slope_v101_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_abs_63d_slope_v102_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_above1_21d_slope_v103_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    ind = (base > 1.0).astype(float) * base
    base = ind * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_pos_streak_21d_slope_v104_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    pos = (base > 0).astype(float)
    streak = pos.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_21d_slope_v105_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_63d_slope_v106_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_rank252_21d_slope_v107_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_rank252_21d_slope_v108_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_rank504_21d_slope_v109_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rk = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_rank252_63d_slope_v110_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v111..v130: slope_diff_norm variants
@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn5_slope_v111_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn10_slope_v112_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn42_slope_v113_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_dn126_slope_v114_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn5_slope_v115_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn10_slope_v116_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn42_slope_v117_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_dn126_slope_v118_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn5_slope_v119_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn10_slope_v120_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn42_slope_v121_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_dn252_slope_v122_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_dn21_slope_v123_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_dn63_slope_v124_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rjf_dn126_slope_v125_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (r + j + f) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_ema21_21d_slope_v126_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_ema21_21d_slope_v127_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_ema21_21d_slope_v128_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_w5_21d_slope_v129_signal(capex, depamor, closeadj):
    base = _mean(_f21_replacement_intensity(capex, depamor), 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_w5_21d_slope_v130_signal(capex, ppnenet, depamor, closeadj):
    base = _mean(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v131..v150 more variety
@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_21d_slope2_v131_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 504)
    base = (j + f) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_jf_63d_slope2_v132_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 504)
    base = (j + f) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rj_dn21_slope_v133_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r + j) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_rj_dn63_slope_v134_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (r + j) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_range21_21d_slope_v135_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rng = (base.rolling(21, min_periods=5).max() - base.rolling(21, min_periods=5).min()) * closeadj
    result = _slope_pct(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_range63_21d_slope_v136_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rng = (base.rolling(63, min_periods=21).max() - base.rolling(63, min_periods=21).min()) * closeadj
    result = _slope_pct(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_range252_63d_slope_v137_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_pct(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_dn21_slope_v138_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_comp_w_dn63_slope_v139_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (0.5 * r + 0.3 * j + 0.2 * f) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_med252_21d_slope_v140_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_med252_21d_slope_v141_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_med252_21d_slope_v142_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_max252_63d_slope_v143_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_min252_63d_slope_v144_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = base.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_max252_63d_slope_v145_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_inv_63d_slope_v146_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (1.0 / (base.abs() + 1e-9)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_abs_252d_slope_v147_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_freshness_pulse_63d_slope_v148_signal(ppnenet, depamor, closeadj):
    a = _f21_ppe_freshness(ppnenet, depamor, 63)
    b = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_repl_regime_21d_slope_v149_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    base = (_mean(base, 63) - _mean(base, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f21smr_f21_specialty_machinery_replacement_rejuv_regime_21d_slope_v150_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = (_mean(base, 63) - _mean(base, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_SPECIALTY_MACHINERY_REPLACEMENT_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK f21_specialty_machinery_replacement_2nd_derivatives_001_150_claude: {n_features} features pass")
