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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f13_margin_floor(grossmargin, w):
    return grossmargin.rolling(w, min_periods=max(1, w // 2)).min()


def _f13_margin_quality(ebitdamargin, w):
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f13_margin_consistency(grossmargin, ebitdamargin, w):
    gs = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    es = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (1.0 + gs + es)

def f13dmq_f13_diagnostics_margin_quality_floor_5d_slope_v001_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_5d_slope_v002_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_10d_slope_v003_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 10) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_10d_slope_v004_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_21d_slope_v005_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_21d_slope_v006_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_42d_slope_v007_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_42d_slope_v008_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_63d_slope_v009_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_63d_slope_v010_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_126d_slope_v011_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_126d_slope_v012_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_189d_slope_v013_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 189) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_189d_slope_v014_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_252d_slope_v015_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_252d_slope_v016_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_378d_slope_v017_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_378d_slope_v018_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_504d_slope_v019_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floor_504d_slope_v020_signal(grossmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_5d_slope_v021_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_5d_slope_v022_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_10d_slope_v023_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 10) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_10d_slope_v024_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_21d_slope_v025_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_21d_slope_v026_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_42d_slope_v027_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_42d_slope_v028_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_63d_slope_v029_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_63d_slope_v030_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_126d_slope_v031_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_126d_slope_v032_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_189d_slope_v033_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 189) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_189d_slope_v034_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_252d_slope_v035_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_252d_slope_v036_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_378d_slope_v037_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_378d_slope_v038_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_504d_slope_v039_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qual_504d_slope_v040_signal(ebitdamargin, closeadj):
    base = _f13_margin_quality(ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_5d_slope_v041_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_5d_slope_v042_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_10d_slope_v043_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 10) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_10d_slope_v044_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_21d_slope_v045_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_21d_slope_v046_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_42d_slope_v047_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_42d_slope_v048_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_63d_slope_v049_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_63d_slope_v050_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_126d_slope_v051_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_126d_slope_v052_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_189d_slope_v053_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 189) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_189d_slope_v054_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_252d_slope_v055_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_252d_slope_v056_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_378d_slope_v057_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_378d_slope_v058_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_504d_slope_v059_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_cons_504d_slope_v060_signal(grossmargin, ebitdamargin, closeadj):
    base = _f13_margin_consistency(grossmargin, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_5d_slope_v061_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 5), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_5d_slope_v062_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 5), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_10d_slope_v063_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 10), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_10d_slope_v064_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 10), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_21d_slope_v065_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_21d_slope_v066_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 21), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_42d_slope_v067_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 42), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_42d_slope_v068_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 42), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_63d_slope_v069_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 63), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_63d_slope_v070_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_126d_slope_v071_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 126), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_126d_slope_v072_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 126), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_189d_slope_v073_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 189), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_189d_slope_v074_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 189), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_252d_slope_v075_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 252), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_252d_slope_v076_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 252), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_378d_slope_v077_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 378), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_378d_slope_v078_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 378), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_504d_slope_v079_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 504), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floormean_504d_slope_v080_signal(grossmargin, closeadj):
    base = _mean(_f13_margin_floor(grossmargin, 504), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_5d_slope_v081_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 5), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_5d_slope_v082_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 5), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_10d_slope_v083_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 10), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_10d_slope_v084_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 10), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_21d_slope_v085_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_21d_slope_v086_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 21), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_42d_slope_v087_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 42), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_42d_slope_v088_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 42), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_63d_slope_v089_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 63), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_63d_slope_v090_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_126d_slope_v091_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 126), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_126d_slope_v092_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 126), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_189d_slope_v093_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 189), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_189d_slope_v094_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 189), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_252d_slope_v095_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 252), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_252d_slope_v096_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 252), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_378d_slope_v097_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 378), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_378d_slope_v098_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 378), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_504d_slope_v099_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 504), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualema_504d_slope_v100_signal(ebitdamargin, closeadj):
    base = _ema(_f13_margin_quality(ebitdamargin, 504), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_5d_slope_v101_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 5)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_5d_slope_v102_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 5)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_10d_slope_v103_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 10)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_10d_slope_v104_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 10)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_21d_slope_v105_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 21)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_21d_slope_v106_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 21)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_42d_slope_v107_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 42)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_42d_slope_v108_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 42)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_63d_slope_v109_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 63)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_63d_slope_v110_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 63)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_126d_slope_v111_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 126)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_126d_slope_v112_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 126)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_189d_slope_v113_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 189)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_189d_slope_v114_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 189)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_252d_slope_v115_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 252)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_252d_slope_v116_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 252)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_378d_slope_v117_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 378)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_378d_slope_v118_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 378)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_504d_slope_v119_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 504)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorgap_504d_slope_v120_signal(grossmargin, closeadj):
    floor = _f13_margin_floor(grossmargin, 504)
    base = (grossmargin - floor) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_5d_slope_v121_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 5)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 5)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_5d_slope_v122_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 5)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 5)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_10d_slope_v123_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 10)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 10)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_10d_slope_v124_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 10)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 10)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_21d_slope_v125_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 21)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 21)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_21d_slope_v126_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 21)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 21)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_42d_slope_v127_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 42)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 42)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_42d_slope_v128_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 42)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 42)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_63d_slope_v129_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 63)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 63)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_63d_slope_v130_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 63)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 63)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_126d_slope_v131_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 126)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 126)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_126d_slope_v132_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 126)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 126)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_189d_slope_v133_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 189)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 189)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_189d_slope_v134_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 189)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 189)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_252d_slope_v135_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 252)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 252)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_252d_slope_v136_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 252)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 252)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_378d_slope_v137_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 378)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 378)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_378d_slope_v138_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 378)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 378)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_504d_slope_v139_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 504)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 504)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_qualxcons_504d_slope_v140_signal(grossmargin, ebitdamargin, closeadj):
    a = _f13_margin_quality(ebitdamargin, 504)
    b = _f13_margin_consistency(grossmargin, ebitdamargin, 504)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_5d_slope_v141_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 5) * netmargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_5d_slope_v142_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 5) * netmargin * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_10d_slope_v143_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 10) * netmargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_10d_slope_v144_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 10) * netmargin * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_21d_slope_v145_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 21) * netmargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_21d_slope_v146_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 21) * netmargin * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_42d_slope_v147_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 42) * netmargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_42d_slope_v148_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 42) * netmargin * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_63d_slope_v149_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 63) * netmargin * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f13dmq_f13_diagnostics_margin_quality_floorxnm_63d_slope_v150_signal(grossmargin, netmargin, closeadj):
    base = _f13_margin_floor(grossmargin, 63) * netmargin * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13dmq_f13_diagnostics_margin_quality_floor_5d_slope_v001_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_5d_slope_v002_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_10d_slope_v003_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_10d_slope_v004_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_21d_slope_v005_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_21d_slope_v006_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_42d_slope_v007_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_42d_slope_v008_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_63d_slope_v009_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_63d_slope_v010_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_126d_slope_v011_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_126d_slope_v012_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_189d_slope_v013_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_189d_slope_v014_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_252d_slope_v015_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_252d_slope_v016_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_378d_slope_v017_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_378d_slope_v018_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_504d_slope_v019_signal,
    f13dmq_f13_diagnostics_margin_quality_floor_504d_slope_v020_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_5d_slope_v021_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_5d_slope_v022_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_10d_slope_v023_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_10d_slope_v024_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_21d_slope_v025_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_21d_slope_v026_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_42d_slope_v027_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_42d_slope_v028_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_63d_slope_v029_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_63d_slope_v030_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_126d_slope_v031_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_126d_slope_v032_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_189d_slope_v033_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_189d_slope_v034_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_252d_slope_v035_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_252d_slope_v036_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_378d_slope_v037_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_378d_slope_v038_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_504d_slope_v039_signal,
    f13dmq_f13_diagnostics_margin_quality_qual_504d_slope_v040_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_5d_slope_v041_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_5d_slope_v042_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_10d_slope_v043_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_10d_slope_v044_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_21d_slope_v045_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_21d_slope_v046_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_42d_slope_v047_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_42d_slope_v048_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_63d_slope_v049_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_63d_slope_v050_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_126d_slope_v051_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_126d_slope_v052_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_189d_slope_v053_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_189d_slope_v054_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_252d_slope_v055_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_252d_slope_v056_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_378d_slope_v057_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_378d_slope_v058_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_504d_slope_v059_signal,
    f13dmq_f13_diagnostics_margin_quality_cons_504d_slope_v060_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_5d_slope_v061_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_5d_slope_v062_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_10d_slope_v063_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_10d_slope_v064_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_21d_slope_v065_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_21d_slope_v066_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_42d_slope_v067_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_42d_slope_v068_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_63d_slope_v069_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_63d_slope_v070_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_126d_slope_v071_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_126d_slope_v072_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_189d_slope_v073_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_189d_slope_v074_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_252d_slope_v075_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_252d_slope_v076_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_378d_slope_v077_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_378d_slope_v078_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_504d_slope_v079_signal,
    f13dmq_f13_diagnostics_margin_quality_floormean_504d_slope_v080_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_5d_slope_v081_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_5d_slope_v082_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_10d_slope_v083_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_10d_slope_v084_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_21d_slope_v085_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_21d_slope_v086_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_42d_slope_v087_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_42d_slope_v088_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_63d_slope_v089_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_63d_slope_v090_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_126d_slope_v091_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_126d_slope_v092_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_189d_slope_v093_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_189d_slope_v094_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_252d_slope_v095_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_252d_slope_v096_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_378d_slope_v097_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_378d_slope_v098_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_504d_slope_v099_signal,
    f13dmq_f13_diagnostics_margin_quality_qualema_504d_slope_v100_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_5d_slope_v101_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_5d_slope_v102_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_10d_slope_v103_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_10d_slope_v104_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_21d_slope_v105_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_21d_slope_v106_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_42d_slope_v107_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_42d_slope_v108_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_63d_slope_v109_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_63d_slope_v110_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_126d_slope_v111_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_126d_slope_v112_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_189d_slope_v113_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_189d_slope_v114_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_252d_slope_v115_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_252d_slope_v116_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_378d_slope_v117_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_378d_slope_v118_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_504d_slope_v119_signal,
    f13dmq_f13_diagnostics_margin_quality_floorgap_504d_slope_v120_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_5d_slope_v121_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_5d_slope_v122_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_10d_slope_v123_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_10d_slope_v124_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_21d_slope_v125_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_21d_slope_v126_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_42d_slope_v127_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_42d_slope_v128_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_63d_slope_v129_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_63d_slope_v130_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_126d_slope_v131_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_126d_slope_v132_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_189d_slope_v133_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_189d_slope_v134_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_252d_slope_v135_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_252d_slope_v136_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_378d_slope_v137_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_378d_slope_v138_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_504d_slope_v139_signal,
    f13dmq_f13_diagnostics_margin_quality_qualxcons_504d_slope_v140_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_5d_slope_v141_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_5d_slope_v142_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_10d_slope_v143_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_10d_slope_v144_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_21d_slope_v145_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_21d_slope_v146_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_42d_slope_v147_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_42d_slope_v148_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_63d_slope_v149_signal,
    f13dmq_f13_diagnostics_margin_quality_floorxnm_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_DIAGNOSTICS_MARGIN_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


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

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f13_margin_floor", "_f13_margin_quality", "_f13_margin_consistency",)
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
    print(f"OK f13_diagnostics_margin_quality_2nd_derivatives_001_150_claude: {n_features} features pass")
