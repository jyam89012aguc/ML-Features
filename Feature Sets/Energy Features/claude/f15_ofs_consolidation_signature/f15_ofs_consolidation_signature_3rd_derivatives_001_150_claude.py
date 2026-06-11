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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f15_intangibles_growth(intangibles, w):
    return intangibles.pct_change(periods=w)


def _f15_consolidation_proxy(intangibles, assets, w):
    base = intangibles / assets.replace(0, np.nan).abs()
    return base.rolling(w, min_periods=max(1, w // 2)).mean()


def _f15_ma_signature(intangibles, capex, w):
    ig = intangibles.pct_change(periods=w)
    cg = capex.pct_change(periods=w)
    return ig - cg


def f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v001_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v002_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v003_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v004_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v005_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v006_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v007_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v008_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v009_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v010_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v011_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v012_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v013_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v014_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v015_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v016_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v017_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v018_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v019_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v020_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v021_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v022_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v023_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v024_signal(intangibles, closeadj):
    base = _f15_intangibles_growth(intangibles, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v025_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v026_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v027_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v028_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v029_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v030_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v031_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v032_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v033_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v034_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v035_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v036_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v037_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v038_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v039_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v040_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v041_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v042_signal(intangibles, closeadj):
    base = _mean(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v043_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v044_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v045_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v046_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v047_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v048_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v049_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v050_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v051_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v052_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v053_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v054_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v055_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v056_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v057_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v058_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v059_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v060_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v061_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v062_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v063_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v064_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v065_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v066_signal(intangibles, assets, closeadj):
    base = _f15_consolidation_proxy(intangibles, assets, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v067_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v068_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v069_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v070_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v071_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v072_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v073_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 252), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v074_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 252), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v075_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 252), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v076_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 252), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v077_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v078_signal(intangibles, assets, closeadj):
    base = _z(_f15_consolidation_proxy(intangibles, assets, 252), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v079_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v080_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v081_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v082_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v083_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v084_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v085_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v086_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v087_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v088_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v089_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v090_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v091_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v092_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v093_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v094_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v095_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v096_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v097_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v098_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v099_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v100_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v101_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v102_signal(intangibles, capex, closeadj):
    base = _f15_ma_signature(intangibles, capex, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v103_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v104_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v105_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v106_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v107_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v108_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v109_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v110_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v111_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v112_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v113_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v114_signal(intangibles, capex, closeadj):
    base = _mean(_f15_ma_signature(intangibles, capex, 21), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v115_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v116_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v117_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v118_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v119_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v120_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v121_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v122_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v123_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v124_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v125_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v126_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v127_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v128_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v129_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v130_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v131_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v132_signal(intangibles, closeadj):
    base = _ema(_f15_intangibles_growth(intangibles, 21), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v133_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v134_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v135_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v136_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v137_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v138_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v139_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v140_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v141_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v142_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v143_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v144_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v145_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v146_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v147_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v148_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v149_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v150_signal(intangibles, assets, closeadj):
    base = _ema(_f15_consolidation_proxy(intangibles, assets, 63), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v001_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v002_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v003_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v004_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v005_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_21d_jerk_v006_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v007_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v008_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v009_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v010_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v011_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_63d_jerk_v012_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v013_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v014_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v015_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v016_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v017_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_126d_jerk_v018_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v019_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v020_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v021_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v022_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v023_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_252d_jerk_v024_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v025_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v026_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v027_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v028_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v029_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_21d_jerk_v030_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v031_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v032_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v033_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v034_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v035_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_63d_jerk_v036_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v037_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v038_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v039_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v040_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v041_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_mean_252d_jerk_v042_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v043_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v044_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v045_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v046_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v047_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_21d_jerk_v048_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v049_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v050_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v051_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v052_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v053_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_63d_jerk_v054_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v055_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v056_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v057_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v058_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v059_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_126d_jerk_v060_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v061_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v062_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v063_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v064_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v065_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_252d_jerk_v066_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v067_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v068_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v069_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v070_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v071_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_63d_jerk_v072_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v073_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v074_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v075_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v076_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v077_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_z_252d_jerk_v078_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v079_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v080_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v081_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v082_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v083_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_21d_jerk_v084_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v085_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v086_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v087_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v088_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v089_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_63d_jerk_v090_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v091_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v092_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v093_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v094_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v095_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_126d_jerk_v096_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v097_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v098_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v099_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v100_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v101_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_252d_jerk_v102_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v103_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v104_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v105_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v106_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v107_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_63d_jerk_v108_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v109_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v110_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v111_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v112_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v113_signal,
    f15ocs_f15_ofs_consolidation_signature_mas_mean_252d_jerk_v114_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v115_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v116_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v117_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v118_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v119_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_21d_jerk_v120_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v121_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v122_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v123_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v124_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v125_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_63d_jerk_v126_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v127_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v128_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v129_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v130_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v131_signal,
    f15ocs_f15_ofs_consolidation_signature_ig_ema_252d_jerk_v132_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v133_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v134_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v135_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v136_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v137_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_21d_jerk_v138_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v139_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v140_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v141_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v142_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v143_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_63d_jerk_v144_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v145_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v146_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v147_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v148_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v149_signal,
    f15ocs_f15_ofs_consolidation_signature_cp_ema_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_OFS_CONSOLIDATION_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f15_intangibles_growth", "_f15_consolidation_proxy", "_f15_ma_signature",)
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
    print(f"OK f15_ofs_consolidation_signature_3rd_derivatives_001_150_claude: {n_features} features pass")
