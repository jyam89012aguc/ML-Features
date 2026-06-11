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


def f034opd_f034_obv_price_divergence_gap_5d_base_v001_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_10d_base_v002_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_21d_base_v003_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_42d_base_v004_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_63d_base_v005_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_126d_base_v006_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_189d_base_v007_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_252d_base_v008_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_378d_base_v009_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_gap_504d_base_v010_signal(closeadj, volume):
    result = _f034_obv_price_gap(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_5d_base_v011_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 5)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_10d_base_v012_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 10)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_21d_base_v013_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(63, min_periods=5).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_42d_base_v014_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 42)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(63, min_periods=10).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_63d_base_v015_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(63, min_periods=15).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_126d_base_v016_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(126, min_periods=31).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_189d_base_v017_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 189)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(189, min_periods=47).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_252d_base_v018_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_378d_base_v019_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 378)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(378, min_periods=94).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_pslope_504d_base_v020_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 504)
    o = _f034_obv_proxy(closeadj, volume)
    result = p * o.abs() / o.abs().rolling(504, min_periods=126).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_5d_base_v021_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(5) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_10d_base_v022_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(10) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_21d_base_v023_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(21) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_42d_base_v024_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(42) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_63d_base_v025_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(63) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_126d_base_v026_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(126) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_189d_base_v027_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(189) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_252d_base_v028_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(252) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_378d_base_v029_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(378) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_oslope_504d_base_v030_signal(closeadj, volume):
    o = _f034_obv_proxy(closeadj, volume)
    result = o.diff(504) / o.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_5d_base_v031_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    result = _mean(g, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_10d_base_v032_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    result = _mean(g, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_21d_base_v033_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    result = _mean(g, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_42d_base_v034_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    result = _mean(g, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_63d_base_v035_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    result = _mean(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_126d_base_v036_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    result = _mean(g, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_189d_base_v037_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    result = _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_252d_base_v038_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    result = _mean(g, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_378d_base_v039_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    result = _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smgap_504d_base_v040_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    result = _mean(g, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_5d_base_v041_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    result = _z(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_10d_base_v042_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    result = _z(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_21d_base_v043_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    result = _z(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_42d_base_v044_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    result = _z(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_63d_base_v045_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    result = _z(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_126d_base_v046_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    result = _z(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_189d_base_v047_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    result = _z(g, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_252d_base_v048_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    result = _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_378d_base_v049_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    result = _z(g, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_zgap_504d_base_v050_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    result = _z(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_5d_base_v051_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    result = _std(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_10d_base_v052_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    result = _std(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_21d_base_v053_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    result = _std(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_42d_base_v054_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    result = _std(g, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_63d_base_v055_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    result = _std(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_126d_base_v056_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 126)
    result = _std(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_189d_base_v057_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 189)
    result = _std(g, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_252d_base_v058_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 252)
    result = _std(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_378d_base_v059_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 378)
    result = _std(g, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_stdgap_504d_base_v060_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 504)
    result = _std(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_5d_base_v061_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 5)
    result = _mean(p, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_10d_base_v062_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 10)
    result = _mean(p, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_21d_base_v063_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 21)
    result = _mean(p, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_42d_base_v064_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 42)
    result = _mean(p, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_63d_base_v065_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 63)
    result = _mean(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_126d_base_v066_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 126)
    result = _mean(p, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_189d_base_v067_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 189)
    result = _mean(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_252d_base_v068_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 252)
    result = _mean(p, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_378d_base_v069_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 378)
    result = _mean(p, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_smpslope_504d_base_v070_signal(closeadj, volume):
    p = _f034_price_slope(closeadj, 504)
    result = _mean(p, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_5d_base_v071_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 5)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_10d_base_v072_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 10)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_21d_base_v073_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 21)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_42d_base_v074_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 42)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


def f034opd_f034_obv_price_divergence_sqgap_63d_base_v075_signal(closeadj, volume):
    g = _f034_obv_price_gap(closeadj, volume, 63)
    result = (g * g) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f034opd_f034_obv_price_divergence_gap_5d_base_v001_signal,
    f034opd_f034_obv_price_divergence_gap_10d_base_v002_signal,
    f034opd_f034_obv_price_divergence_gap_21d_base_v003_signal,
    f034opd_f034_obv_price_divergence_gap_42d_base_v004_signal,
    f034opd_f034_obv_price_divergence_gap_63d_base_v005_signal,
    f034opd_f034_obv_price_divergence_gap_126d_base_v006_signal,
    f034opd_f034_obv_price_divergence_gap_189d_base_v007_signal,
    f034opd_f034_obv_price_divergence_gap_252d_base_v008_signal,
    f034opd_f034_obv_price_divergence_gap_378d_base_v009_signal,
    f034opd_f034_obv_price_divergence_gap_504d_base_v010_signal,
    f034opd_f034_obv_price_divergence_pslope_5d_base_v011_signal,
    f034opd_f034_obv_price_divergence_pslope_10d_base_v012_signal,
    f034opd_f034_obv_price_divergence_pslope_21d_base_v013_signal,
    f034opd_f034_obv_price_divergence_pslope_42d_base_v014_signal,
    f034opd_f034_obv_price_divergence_pslope_63d_base_v015_signal,
    f034opd_f034_obv_price_divergence_pslope_126d_base_v016_signal,
    f034opd_f034_obv_price_divergence_pslope_189d_base_v017_signal,
    f034opd_f034_obv_price_divergence_pslope_252d_base_v018_signal,
    f034opd_f034_obv_price_divergence_pslope_378d_base_v019_signal,
    f034opd_f034_obv_price_divergence_pslope_504d_base_v020_signal,
    f034opd_f034_obv_price_divergence_oslope_5d_base_v021_signal,
    f034opd_f034_obv_price_divergence_oslope_10d_base_v022_signal,
    f034opd_f034_obv_price_divergence_oslope_21d_base_v023_signal,
    f034opd_f034_obv_price_divergence_oslope_42d_base_v024_signal,
    f034opd_f034_obv_price_divergence_oslope_63d_base_v025_signal,
    f034opd_f034_obv_price_divergence_oslope_126d_base_v026_signal,
    f034opd_f034_obv_price_divergence_oslope_189d_base_v027_signal,
    f034opd_f034_obv_price_divergence_oslope_252d_base_v028_signal,
    f034opd_f034_obv_price_divergence_oslope_378d_base_v029_signal,
    f034opd_f034_obv_price_divergence_oslope_504d_base_v030_signal,
    f034opd_f034_obv_price_divergence_smgap_5d_base_v031_signal,
    f034opd_f034_obv_price_divergence_smgap_10d_base_v032_signal,
    f034opd_f034_obv_price_divergence_smgap_21d_base_v033_signal,
    f034opd_f034_obv_price_divergence_smgap_42d_base_v034_signal,
    f034opd_f034_obv_price_divergence_smgap_63d_base_v035_signal,
    f034opd_f034_obv_price_divergence_smgap_126d_base_v036_signal,
    f034opd_f034_obv_price_divergence_smgap_189d_base_v037_signal,
    f034opd_f034_obv_price_divergence_smgap_252d_base_v038_signal,
    f034opd_f034_obv_price_divergence_smgap_378d_base_v039_signal,
    f034opd_f034_obv_price_divergence_smgap_504d_base_v040_signal,
    f034opd_f034_obv_price_divergence_zgap_5d_base_v041_signal,
    f034opd_f034_obv_price_divergence_zgap_10d_base_v042_signal,
    f034opd_f034_obv_price_divergence_zgap_21d_base_v043_signal,
    f034opd_f034_obv_price_divergence_zgap_42d_base_v044_signal,
    f034opd_f034_obv_price_divergence_zgap_63d_base_v045_signal,
    f034opd_f034_obv_price_divergence_zgap_126d_base_v046_signal,
    f034opd_f034_obv_price_divergence_zgap_189d_base_v047_signal,
    f034opd_f034_obv_price_divergence_zgap_252d_base_v048_signal,
    f034opd_f034_obv_price_divergence_zgap_378d_base_v049_signal,
    f034opd_f034_obv_price_divergence_zgap_504d_base_v050_signal,
    f034opd_f034_obv_price_divergence_stdgap_5d_base_v051_signal,
    f034opd_f034_obv_price_divergence_stdgap_10d_base_v052_signal,
    f034opd_f034_obv_price_divergence_stdgap_21d_base_v053_signal,
    f034opd_f034_obv_price_divergence_stdgap_42d_base_v054_signal,
    f034opd_f034_obv_price_divergence_stdgap_63d_base_v055_signal,
    f034opd_f034_obv_price_divergence_stdgap_126d_base_v056_signal,
    f034opd_f034_obv_price_divergence_stdgap_189d_base_v057_signal,
    f034opd_f034_obv_price_divergence_stdgap_252d_base_v058_signal,
    f034opd_f034_obv_price_divergence_stdgap_378d_base_v059_signal,
    f034opd_f034_obv_price_divergence_stdgap_504d_base_v060_signal,
    f034opd_f034_obv_price_divergence_smpslope_5d_base_v061_signal,
    f034opd_f034_obv_price_divergence_smpslope_10d_base_v062_signal,
    f034opd_f034_obv_price_divergence_smpslope_21d_base_v063_signal,
    f034opd_f034_obv_price_divergence_smpslope_42d_base_v064_signal,
    f034opd_f034_obv_price_divergence_smpslope_63d_base_v065_signal,
    f034opd_f034_obv_price_divergence_smpslope_126d_base_v066_signal,
    f034opd_f034_obv_price_divergence_smpslope_189d_base_v067_signal,
    f034opd_f034_obv_price_divergence_smpslope_252d_base_v068_signal,
    f034opd_f034_obv_price_divergence_smpslope_378d_base_v069_signal,
    f034opd_f034_obv_price_divergence_smpslope_504d_base_v070_signal,
    f034opd_f034_obv_price_divergence_sqgap_5d_base_v071_signal,
    f034opd_f034_obv_price_divergence_sqgap_10d_base_v072_signal,
    f034opd_f034_obv_price_divergence_sqgap_21d_base_v073_signal,
    f034opd_f034_obv_price_divergence_sqgap_42d_base_v074_signal,
    f034opd_f034_obv_price_divergence_sqgap_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F034_OBV_PRICE_DIVERGENCE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f034_obv_price_divergence_base_001_075_claude: {n_features} features pass")
