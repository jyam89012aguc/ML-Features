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
def _f034_obv_proxy(closeadj, volume):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    return (sign * volume).cumsum()


def _f034_price_slope(closeadj, w):
    return closeadj.diff(w) / closeadj.abs().replace(0, np.nan)


def _f034_obv_price_gap(closeadj, volume, w):
    ret = closeadj.diff()
    sign = np.sign(ret).fillna(0.0)
    obv = (sign * volume).cumsum()
    obv_sl = obv.diff(w) / obv.abs().replace(0, np.nan)
    price_sl = closeadj.diff(w) / closeadj.abs().replace(0, np.nan)
    return (obv_sl - price_sl) * closeadj


def f034opd_f034_obv_price_divergence_gap_21d_slope_v001_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_21d_slope_v002_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_63d_slope_v003_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 63)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_63d_slope_v004_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_126d_slope_v005_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_126d_slope_v006_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_252d_slope_v007_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_252d_slope_v008_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 252)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_252d_slope_v009_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_252d_slope_v010_signal(closeadj, volume):
    base = _f034_obv_price_gap(closeadj, volume, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_21d_slope_v011_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_21d_slope_v012_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_63d_slope_v013_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_63d_slope_v014_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_126d_slope_v015_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_126d_slope_v016_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_252d_slope_v017_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_252d_slope_v018_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_252d_slope_v019_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_252d_slope_v020_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    o = _f034_obv_proxy(closeadj, volume)
    base = p * o.abs() / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_21d_slope_v021_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(21) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_21d_slope_v022_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(21) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_63d_slope_v023_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(63) / o.abs().replace(0, np.nan) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_63d_slope_v024_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(63) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_126d_slope_v025_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(126) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_126d_slope_v026_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(126) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_252d_slope_v027_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(252) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_252d_slope_v028_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(252) / o.abs().replace(0, np.nan) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_252d_slope_v029_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(252) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_252d_slope_v030_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    base = o.diff(252) / o.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_21d_slope_v031_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = _mean(g, 7)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_21d_slope_v032_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = _mean(g, 7)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_63d_slope_v033_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = _mean(g, 21)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_63d_slope_v034_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = _mean(g, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_126d_slope_v035_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = _mean(g, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_126d_slope_v036_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = _mean(g, 42)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_252d_slope_v037_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _mean(g, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_252d_slope_v038_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _mean(g, 84)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_252d_slope_v039_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _mean(g, 84)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_252d_slope_v040_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _mean(g, 84)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_21d_slope_v041_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = _z(g, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_21d_slope_v042_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = _z(g, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_63d_slope_v043_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = _z(g, 63)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_63d_slope_v044_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = _z(g, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_126d_slope_v045_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = _z(g, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_126d_slope_v046_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = _z(g, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_252d_slope_v047_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _z(g, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_252d_slope_v048_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _z(g, 252)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_252d_slope_v049_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _z(g, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_252d_slope_v050_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _z(g, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_21d_slope_v051_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = _std(g, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_21d_slope_v052_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = _std(g, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_63d_slope_v053_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = _std(g, 63)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_63d_slope_v054_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = _std(g, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_126d_slope_v055_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = _std(g, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_126d_slope_v056_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = _std(g, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_252d_slope_v057_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _std(g, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_252d_slope_v058_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _std(g, 252)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_252d_slope_v059_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _std(g, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_252d_slope_v060_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = _std(g, 252)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_21d_slope_v061_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    base = _mean(p, 7) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_21d_slope_v062_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    base = _mean(p, 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_63d_slope_v063_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    base = _mean(p, 21) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_63d_slope_v064_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    base = _mean(p, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_126d_slope_v065_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    base = _mean(p, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_126d_slope_v066_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    base = _mean(p, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_252d_slope_v067_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _mean(p, 84) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_252d_slope_v068_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _mean(p, 84) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_252d_slope_v069_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _mean(p, 84) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_252d_slope_v070_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _mean(p, 84) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_21d_slope_v071_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = (g * g) * np.sign(g)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_21d_slope_v072_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = (g * g) * np.sign(g)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_63d_slope_v073_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = (g * g) * np.sign(g)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_63d_slope_v074_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = (g * g) * np.sign(g)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_126d_slope_v075_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = (g * g) * np.sign(g)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_126d_slope_v076_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = (g * g) * np.sign(g)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_252d_slope_v077_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = (g * g) * np.sign(g)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_252d_slope_v078_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = (g * g) * np.sign(g)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_252d_slope_v079_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = (g * g) * np.sign(g)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_252d_slope_v080_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = (g * g) * np.sign(g)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_21d_slope_v081_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    dv = closeadj * volume
    base = g * _mean(dv, 10) / _mean(dv, 21).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_21d_slope_v082_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    dv = closeadj * volume
    base = g * _mean(dv, 10) / _mean(dv, 21).replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_63d_slope_v083_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    dv = closeadj * volume
    base = g * _mean(dv, 31) / _mean(dv, 63).replace(0, np.nan)
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_63d_slope_v084_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    dv = closeadj * volume
    base = g * _mean(dv, 31) / _mean(dv, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_126d_slope_v085_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    dv = closeadj * volume
    base = g * _mean(dv, 63) / _mean(dv, 126).replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_126d_slope_v086_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    dv = closeadj * volume
    base = g * _mean(dv, 63) / _mean(dv, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v087_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    dv = closeadj * volume
    base = g * _mean(dv, 126) / _mean(dv, 252).replace(0, np.nan)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v088_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    dv = closeadj * volume
    base = g * _mean(dv, 126) / _mean(dv, 252).replace(0, np.nan)
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v089_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    dv = closeadj * volume
    base = g * _mean(dv, 126) / _mean(dv, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v090_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    dv = closeadj * volume
    base = g * _mean(dv, 126) / _mean(dv, 252).replace(0, np.nan)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_21d_slope_v091_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    base = _mean(sl, 7) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_21d_slope_v092_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    base = _mean(sl, 7) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_63d_slope_v093_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    base = _mean(sl, 21) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_63d_slope_v094_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    base = _mean(sl, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_126d_slope_v095_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    base = _mean(sl, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_126d_slope_v096_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    base = _mean(sl, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_252d_slope_v097_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _mean(sl, 84) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_252d_slope_v098_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _mean(sl, 84) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_252d_slope_v099_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _mean(sl, 84) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smoslope_252d_slope_v100_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _mean(sl, 84) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_21d_slope_v101_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    base = _z(sl, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_21d_slope_v102_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    base = _z(sl, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_63d_slope_v103_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    base = _z(sl, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_63d_slope_v104_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    base = _z(sl, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_126d_slope_v105_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    base = _z(sl, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_126d_slope_v106_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    base = _z(sl, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_252d_slope_v107_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _z(sl, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_252d_slope_v108_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _z(sl, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_252d_slope_v109_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _z(sl, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zoslope_252d_slope_v110_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = _z(sl, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_21d_slope_v111_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    base = _z(p, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_21d_slope_v112_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    base = _z(p, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_63d_slope_v113_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    base = _z(p, 63) * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_63d_slope_v114_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    base = _z(p, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_126d_slope_v115_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    base = _z(p, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_126d_slope_v116_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    base = _z(p, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_252d_slope_v117_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _z(p, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_252d_slope_v118_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _z(p, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_252d_slope_v119_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _z(p, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zpslope_252d_slope_v120_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    base = _z(p, 252) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_21d_slope_v121_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_21d_slope_v122_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_63d_slope_v123_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_63d_slope_v124_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_126d_slope_v125_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_126d_slope_v126_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_252d_slope_v127_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_252d_slope_v128_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_252d_slope_v129_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absgap_252d_slope_v130_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.abs() * np.sign(closeadj.pct_change(21).fillna(0.0))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_21d_slope_v131_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = g.ewm(span=10, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_21d_slope_v132_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    base = g.ewm(span=10, adjust=False).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_63d_slope_v133_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = g.ewm(span=31, adjust=False).mean()
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_63d_slope_v134_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    base = g.ewm(span=31, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_126d_slope_v135_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = g.ewm(span=63, adjust=False).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_126d_slope_v136_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    base = g.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_252d_slope_v137_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.ewm(span=126, adjust=False).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_252d_slope_v138_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.ewm(span=126, adjust=False).mean()
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_252d_slope_v139_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_emagap_252d_slope_v140_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    base = g.ewm(span=126, adjust=False).mean()
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_21d_slope_v141_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(21, min_periods=5).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_21d_slope_v142_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(21) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_63d_slope_v143_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(63, min_periods=15).mean() * closeadj
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_63d_slope_v144_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(63) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(63, min_periods=15).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_126d_slope_v145_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(126, min_periods=31).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_126d_slope_v146_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(126) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(126, min_periods=31).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_252d_slope_v147_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_252d_slope_v148_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_252d_slope_v149_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_absoslope_252d_slope_v150_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    sl = o.diff(252) / o.abs().replace(0, np.nan)
    base = sl.abs().rolling(252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f034opd_f034_obv_price_divergence_gap_21d_slope_v001_signal,
    f034opd_f034_obv_price_divergence_gap_21d_slope_v002_signal,
    f034opd_f034_obv_price_divergence_gap_63d_slope_v003_signal,
    f034opd_f034_obv_price_divergence_gap_63d_slope_v004_signal,
    f034opd_f034_obv_price_divergence_gap_126d_slope_v005_signal,
    f034opd_f034_obv_price_divergence_gap_126d_slope_v006_signal,
    f034opd_f034_obv_price_divergence_gap_252d_slope_v007_signal,
    f034opd_f034_obv_price_divergence_gap_252d_slope_v008_signal,
    f034opd_f034_obv_price_divergence_gap_252d_slope_v009_signal,
    f034opd_f034_obv_price_divergence_gap_252d_slope_v010_signal,
    f034opd_f034_obv_price_divergence_pslope_21d_slope_v011_signal,
    f034opd_f034_obv_price_divergence_pslope_21d_slope_v012_signal,
    f034opd_f034_obv_price_divergence_pslope_63d_slope_v013_signal,
    f034opd_f034_obv_price_divergence_pslope_63d_slope_v014_signal,
    f034opd_f034_obv_price_divergence_pslope_126d_slope_v015_signal,
    f034opd_f034_obv_price_divergence_pslope_126d_slope_v016_signal,
    f034opd_f034_obv_price_divergence_pslope_252d_slope_v017_signal,
    f034opd_f034_obv_price_divergence_pslope_252d_slope_v018_signal,
    f034opd_f034_obv_price_divergence_pslope_252d_slope_v019_signal,
    f034opd_f034_obv_price_divergence_pslope_252d_slope_v020_signal,
    f034opd_f034_obv_price_divergence_oslope_21d_slope_v021_signal,
    f034opd_f034_obv_price_divergence_oslope_21d_slope_v022_signal,
    f034opd_f034_obv_price_divergence_oslope_63d_slope_v023_signal,
    f034opd_f034_obv_price_divergence_oslope_63d_slope_v024_signal,
    f034opd_f034_obv_price_divergence_oslope_126d_slope_v025_signal,
    f034opd_f034_obv_price_divergence_oslope_126d_slope_v026_signal,
    f034opd_f034_obv_price_divergence_oslope_252d_slope_v027_signal,
    f034opd_f034_obv_price_divergence_oslope_252d_slope_v028_signal,
    f034opd_f034_obv_price_divergence_oslope_252d_slope_v029_signal,
    f034opd_f034_obv_price_divergence_oslope_252d_slope_v030_signal,
    f034opd_f034_obv_price_divergence_smgap_21d_slope_v031_signal,
    f034opd_f034_obv_price_divergence_smgap_21d_slope_v032_signal,
    f034opd_f034_obv_price_divergence_smgap_63d_slope_v033_signal,
    f034opd_f034_obv_price_divergence_smgap_63d_slope_v034_signal,
    f034opd_f034_obv_price_divergence_smgap_126d_slope_v035_signal,
    f034opd_f034_obv_price_divergence_smgap_126d_slope_v036_signal,
    f034opd_f034_obv_price_divergence_smgap_252d_slope_v037_signal,
    f034opd_f034_obv_price_divergence_smgap_252d_slope_v038_signal,
    f034opd_f034_obv_price_divergence_smgap_252d_slope_v039_signal,
    f034opd_f034_obv_price_divergence_smgap_252d_slope_v040_signal,
    f034opd_f034_obv_price_divergence_zgap_21d_slope_v041_signal,
    f034opd_f034_obv_price_divergence_zgap_21d_slope_v042_signal,
    f034opd_f034_obv_price_divergence_zgap_63d_slope_v043_signal,
    f034opd_f034_obv_price_divergence_zgap_63d_slope_v044_signal,
    f034opd_f034_obv_price_divergence_zgap_126d_slope_v045_signal,
    f034opd_f034_obv_price_divergence_zgap_126d_slope_v046_signal,
    f034opd_f034_obv_price_divergence_zgap_252d_slope_v047_signal,
    f034opd_f034_obv_price_divergence_zgap_252d_slope_v048_signal,
    f034opd_f034_obv_price_divergence_zgap_252d_slope_v049_signal,
    f034opd_f034_obv_price_divergence_zgap_252d_slope_v050_signal,
    f034opd_f034_obv_price_divergence_stdgap_21d_slope_v051_signal,
    f034opd_f034_obv_price_divergence_stdgap_21d_slope_v052_signal,
    f034opd_f034_obv_price_divergence_stdgap_63d_slope_v053_signal,
    f034opd_f034_obv_price_divergence_stdgap_63d_slope_v054_signal,
    f034opd_f034_obv_price_divergence_stdgap_126d_slope_v055_signal,
    f034opd_f034_obv_price_divergence_stdgap_126d_slope_v056_signal,
    f034opd_f034_obv_price_divergence_stdgap_252d_slope_v057_signal,
    f034opd_f034_obv_price_divergence_stdgap_252d_slope_v058_signal,
    f034opd_f034_obv_price_divergence_stdgap_252d_slope_v059_signal,
    f034opd_f034_obv_price_divergence_stdgap_252d_slope_v060_signal,
    f034opd_f034_obv_price_divergence_smpslope_21d_slope_v061_signal,
    f034opd_f034_obv_price_divergence_smpslope_21d_slope_v062_signal,
    f034opd_f034_obv_price_divergence_smpslope_63d_slope_v063_signal,
    f034opd_f034_obv_price_divergence_smpslope_63d_slope_v064_signal,
    f034opd_f034_obv_price_divergence_smpslope_126d_slope_v065_signal,
    f034opd_f034_obv_price_divergence_smpslope_126d_slope_v066_signal,
    f034opd_f034_obv_price_divergence_smpslope_252d_slope_v067_signal,
    f034opd_f034_obv_price_divergence_smpslope_252d_slope_v068_signal,
    f034opd_f034_obv_price_divergence_smpslope_252d_slope_v069_signal,
    f034opd_f034_obv_price_divergence_smpslope_252d_slope_v070_signal,
    f034opd_f034_obv_price_divergence_sqgap_21d_slope_v071_signal,
    f034opd_f034_obv_price_divergence_sqgap_21d_slope_v072_signal,
    f034opd_f034_obv_price_divergence_sqgap_63d_slope_v073_signal,
    f034opd_f034_obv_price_divergence_sqgap_63d_slope_v074_signal,
    f034opd_f034_obv_price_divergence_sqgap_126d_slope_v075_signal,
    f034opd_f034_obv_price_divergence_sqgap_126d_slope_v076_signal,
    f034opd_f034_obv_price_divergence_sqgap_252d_slope_v077_signal,
    f034opd_f034_obv_price_divergence_sqgap_252d_slope_v078_signal,
    f034opd_f034_obv_price_divergence_sqgap_252d_slope_v079_signal,
    f034opd_f034_obv_price_divergence_sqgap_252d_slope_v080_signal,
    f034opd_f034_obv_price_divergence_gapxdv_21d_slope_v081_signal,
    f034opd_f034_obv_price_divergence_gapxdv_21d_slope_v082_signal,
    f034opd_f034_obv_price_divergence_gapxdv_63d_slope_v083_signal,
    f034opd_f034_obv_price_divergence_gapxdv_63d_slope_v084_signal,
    f034opd_f034_obv_price_divergence_gapxdv_126d_slope_v085_signal,
    f034opd_f034_obv_price_divergence_gapxdv_126d_slope_v086_signal,
    f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v087_signal,
    f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v088_signal,
    f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v089_signal,
    f034opd_f034_obv_price_divergence_gapxdv_252d_slope_v090_signal,
    f034opd_f034_obv_price_divergence_smoslope_21d_slope_v091_signal,
    f034opd_f034_obv_price_divergence_smoslope_21d_slope_v092_signal,
    f034opd_f034_obv_price_divergence_smoslope_63d_slope_v093_signal,
    f034opd_f034_obv_price_divergence_smoslope_63d_slope_v094_signal,
    f034opd_f034_obv_price_divergence_smoslope_126d_slope_v095_signal,
    f034opd_f034_obv_price_divergence_smoslope_126d_slope_v096_signal,
    f034opd_f034_obv_price_divergence_smoslope_252d_slope_v097_signal,
    f034opd_f034_obv_price_divergence_smoslope_252d_slope_v098_signal,
    f034opd_f034_obv_price_divergence_smoslope_252d_slope_v099_signal,
    f034opd_f034_obv_price_divergence_smoslope_252d_slope_v100_signal,
    f034opd_f034_obv_price_divergence_zoslope_21d_slope_v101_signal,
    f034opd_f034_obv_price_divergence_zoslope_21d_slope_v102_signal,
    f034opd_f034_obv_price_divergence_zoslope_63d_slope_v103_signal,
    f034opd_f034_obv_price_divergence_zoslope_63d_slope_v104_signal,
    f034opd_f034_obv_price_divergence_zoslope_126d_slope_v105_signal,
    f034opd_f034_obv_price_divergence_zoslope_126d_slope_v106_signal,
    f034opd_f034_obv_price_divergence_zoslope_252d_slope_v107_signal,
    f034opd_f034_obv_price_divergence_zoslope_252d_slope_v108_signal,
    f034opd_f034_obv_price_divergence_zoslope_252d_slope_v109_signal,
    f034opd_f034_obv_price_divergence_zoslope_252d_slope_v110_signal,
    f034opd_f034_obv_price_divergence_zpslope_21d_slope_v111_signal,
    f034opd_f034_obv_price_divergence_zpslope_21d_slope_v112_signal,
    f034opd_f034_obv_price_divergence_zpslope_63d_slope_v113_signal,
    f034opd_f034_obv_price_divergence_zpslope_63d_slope_v114_signal,
    f034opd_f034_obv_price_divergence_zpslope_126d_slope_v115_signal,
    f034opd_f034_obv_price_divergence_zpslope_126d_slope_v116_signal,
    f034opd_f034_obv_price_divergence_zpslope_252d_slope_v117_signal,
    f034opd_f034_obv_price_divergence_zpslope_252d_slope_v118_signal,
    f034opd_f034_obv_price_divergence_zpslope_252d_slope_v119_signal,
    f034opd_f034_obv_price_divergence_zpslope_252d_slope_v120_signal,
    f034opd_f034_obv_price_divergence_absgap_21d_slope_v121_signal,
    f034opd_f034_obv_price_divergence_absgap_21d_slope_v122_signal,
    f034opd_f034_obv_price_divergence_absgap_63d_slope_v123_signal,
    f034opd_f034_obv_price_divergence_absgap_63d_slope_v124_signal,
    f034opd_f034_obv_price_divergence_absgap_126d_slope_v125_signal,
    f034opd_f034_obv_price_divergence_absgap_126d_slope_v126_signal,
    f034opd_f034_obv_price_divergence_absgap_252d_slope_v127_signal,
    f034opd_f034_obv_price_divergence_absgap_252d_slope_v128_signal,
    f034opd_f034_obv_price_divergence_absgap_252d_slope_v129_signal,
    f034opd_f034_obv_price_divergence_absgap_252d_slope_v130_signal,
    f034opd_f034_obv_price_divergence_emagap_21d_slope_v131_signal,
    f034opd_f034_obv_price_divergence_emagap_21d_slope_v132_signal,
    f034opd_f034_obv_price_divergence_emagap_63d_slope_v133_signal,
    f034opd_f034_obv_price_divergence_emagap_63d_slope_v134_signal,
    f034opd_f034_obv_price_divergence_emagap_126d_slope_v135_signal,
    f034opd_f034_obv_price_divergence_emagap_126d_slope_v136_signal,
    f034opd_f034_obv_price_divergence_emagap_252d_slope_v137_signal,
    f034opd_f034_obv_price_divergence_emagap_252d_slope_v138_signal,
    f034opd_f034_obv_price_divergence_emagap_252d_slope_v139_signal,
    f034opd_f034_obv_price_divergence_emagap_252d_slope_v140_signal,
    f034opd_f034_obv_price_divergence_absoslope_21d_slope_v141_signal,
    f034opd_f034_obv_price_divergence_absoslope_21d_slope_v142_signal,
    f034opd_f034_obv_price_divergence_absoslope_63d_slope_v143_signal,
    f034opd_f034_obv_price_divergence_absoslope_63d_slope_v144_signal,
    f034opd_f034_obv_price_divergence_absoslope_126d_slope_v145_signal,
    f034opd_f034_obv_price_divergence_absoslope_126d_slope_v146_signal,
    f034opd_f034_obv_price_divergence_absoslope_252d_slope_v147_signal,
    f034opd_f034_obv_price_divergence_absoslope_252d_slope_v148_signal,
    f034opd_f034_obv_price_divergence_absoslope_252d_slope_v149_signal,
    f034opd_f034_obv_price_divergence_absoslope_252d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F034_OBV_PRICE_DIVERGENCE_REGISTRY_SLOPE_001_150 = REGISTRY


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

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f034_obv_proxy', '_f034_price_slope', '_f034_obv_price_gap')
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
    print(f"OK f034_obv_price_divergence_2nd_derivatives_001_150_claude: {n_features} features pass")
