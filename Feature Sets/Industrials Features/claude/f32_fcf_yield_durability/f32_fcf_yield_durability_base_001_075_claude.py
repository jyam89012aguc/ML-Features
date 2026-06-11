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
def _f32_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan)


def _f32_fcf_yield_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan)
    return _mean(y, w) / _std(y, w).replace(0, np.nan)


def _f32_fcf_compound_quality(fcf, marketcap, w):
    y = fcf / marketcap.replace(0, np.nan)
    return _mean(y, w) - 0.5 * _std(y, w)


_BWINS_BASE = [5, 10, 21, 42, 63, 126, 189, 252, 378, 504]


def f32fyd_f32_fcf_yield_durability_yield_base_v001_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield(fcf, ev) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_21d_base_v002_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_63d_base_v003_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_126d_base_v004_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_252d_base_v005_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yield_504d_base_v006_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldstd_21d_base_v007_signal(fcf, ev, closeadj):
    result = _std(_f32_fcf_yield(fcf, ev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldstd_63d_base_v008_signal(fcf, ev, closeadj):
    result = _std(_f32_fcf_yield(fcf, ev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldstd_252d_base_v009_signal(fcf, ev, closeadj):
    result = _std(_f32_fcf_yield(fcf, ev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldstd_504d_base_v010_signal(fcf, ev, closeadj):
    result = _std(_f32_fcf_yield(fcf, ev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldz_63d_base_v011_signal(fcf, ev, closeadj):
    result = _z(_f32_fcf_yield(fcf, ev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldz_252d_base_v012_signal(fcf, ev, closeadj):
    result = _z(_f32_fcf_yield(fcf, ev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldz_504d_base_v013_signal(fcf, ev, closeadj):
    result = _z(_f32_fcf_yield(fcf, ev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_21d_base_v014_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_63d_base_v015_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_126d_base_v016_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_252d_base_v017_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stability_504d_base_v018_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_21d_base_v019_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_63d_base_v020_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_126d_base_v021_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_252d_base_v022_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundq_504d_base_v023_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldema_21d_base_v024_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldema_63d_base_v025_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldema_252d_base_v026_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmax_252d_base_v027_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmin_252d_base_v028_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldrange_252d_base_v029_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldrank_63d_base_v030_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rank = base.rolling(63, min_periods=20).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldrank_252d_base_v031_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldrank_504d_base_v032_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddiff_63d_base_v033_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddiff_252d_base_v034_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddiff_504d_base_v035_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilitydiff_63d_base_v036_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilitydiff_252d_base_v037_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield_stability(fcf, ev, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqdiff_63d_base_v038_signal(fcf, marketcap, closeadj):
    base = _f32_fcf_compound_quality(fcf, marketcap, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqdiff_252d_base_v039_signal(fcf, marketcap, closeadj):
    base = _f32_fcf_compound_quality(fcf, marketcap, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldsq_63d_base_v040_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base * base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldsq_252d_base_v041_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base * base.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldsq_504d_base_v042_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base * base.abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmkt_base_v043_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = base * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmkt_63d_base_v044_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _mean(base, 63) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmkt_252d_base_v045_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _mean(base, 252) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmkt_504d_base_v046_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _mean(base, 504) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmktstd_63d_base_v047_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _std(base, 63) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmktstd_252d_base_v048_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _std(base, 252) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmktstd_504d_base_v049_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _std(base, 504) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmktz_63d_base_v050_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _z(base, 252) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldmktz_252d_base_v051_signal(fcf, marketcap, closeadj):
    base = fcf / marketcap.replace(0, np.nan)
    result = _z(base, 504) * closeadj + _f32_fcf_compound_quality(fcf, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxprice_5d_base_v052_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield(fcf, ev) * closeadj * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxprice_21d_base_v053_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 21) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxprice_63d_base_v054_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxprice_252d_base_v055_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityxprice_63d_base_v056_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityxprice_252d_base_v057_signal(fcf, ev, closeadj):
    result = _f32_fcf_yield_stability(fcf, ev, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqxprice_63d_base_v058_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_compoundqxprice_252d_base_v059_signal(fcf, marketcap, closeadj):
    result = _f32_fcf_compound_quality(fcf, marketcap, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldratio_63v252_base_v060_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 63) / _mean(base, 252).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldratio_21v63_base_v061_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 21) / _mean(base, 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldratio_252v504_base_v062_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 252) / _mean(base, 504).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddiff_63m252_base_v063_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yielddiff_252m504_base_v064_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = (_mean(base, 252) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityratio_63v252_base_v065_signal(fcf, ev, closeadj):
    a = _f32_fcf_yield_stability(fcf, ev, 63)
    b = _f32_fcf_yield_stability(fcf, ev, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_stabilityratio_252v504_base_v066_signal(fcf, ev, closeadj):
    a = _f32_fcf_yield_stability(fcf, ev, 252)
    b = _f32_fcf_yield_stability(fcf, ev, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusg_63d_base_v067_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = fcf.pct_change(63)
    result = (_mean(base, 63) - g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldminusg_252d_base_v068_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = fcf.pct_change(252)
    result = (_mean(base, 252) - g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxfcfg_63d_base_v069_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = fcf.pct_change(63)
    result = _mean(base, 63) * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxfcfg_252d_base_v070_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    g = fcf.pct_change(252)
    result = _mean(base, 252) * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldhigh_252d_base_v071_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    med = base.rolling(252, min_periods=63).median()
    hi = (base > med).astype(float)
    result = _mean(hi, 252) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldlow_252d_base_v072_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    med = base.rolling(252, min_periods=63).median()
    lo = (base < med).astype(float)
    result = _mean(lo, 252) * closeadj + base * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxlog_63d_base_v073_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 63) * closeadj * np.log(fcf.abs().replace(0, np.nan)) / 20.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxlog_252d_base_v074_signal(fcf, ev, closeadj):
    result = _mean(_f32_fcf_yield(fcf, ev), 252) * closeadj * np.log(fcf.abs().replace(0, np.nan)) / 20.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32fyd_f32_fcf_yield_durability_yieldxinvev_63d_base_v075_signal(fcf, ev, closeadj):
    base = _f32_fcf_yield(fcf, ev)
    result = _mean(base, 63) * closeadj * 1.0 / ev.replace(0, np.nan).abs() * 1e8
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32fyd_f32_fcf_yield_durability_yield_base_v001_signal,
    f32fyd_f32_fcf_yield_durability_yield_21d_base_v002_signal,
    f32fyd_f32_fcf_yield_durability_yield_63d_base_v003_signal,
    f32fyd_f32_fcf_yield_durability_yield_126d_base_v004_signal,
    f32fyd_f32_fcf_yield_durability_yield_252d_base_v005_signal,
    f32fyd_f32_fcf_yield_durability_yield_504d_base_v006_signal,
    f32fyd_f32_fcf_yield_durability_yieldstd_21d_base_v007_signal,
    f32fyd_f32_fcf_yield_durability_yieldstd_63d_base_v008_signal,
    f32fyd_f32_fcf_yield_durability_yieldstd_252d_base_v009_signal,
    f32fyd_f32_fcf_yield_durability_yieldstd_504d_base_v010_signal,
    f32fyd_f32_fcf_yield_durability_yieldz_63d_base_v011_signal,
    f32fyd_f32_fcf_yield_durability_yieldz_252d_base_v012_signal,
    f32fyd_f32_fcf_yield_durability_yieldz_504d_base_v013_signal,
    f32fyd_f32_fcf_yield_durability_stability_21d_base_v014_signal,
    f32fyd_f32_fcf_yield_durability_stability_63d_base_v015_signal,
    f32fyd_f32_fcf_yield_durability_stability_126d_base_v016_signal,
    f32fyd_f32_fcf_yield_durability_stability_252d_base_v017_signal,
    f32fyd_f32_fcf_yield_durability_stability_504d_base_v018_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_21d_base_v019_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_63d_base_v020_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_126d_base_v021_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_252d_base_v022_signal,
    f32fyd_f32_fcf_yield_durability_compoundq_504d_base_v023_signal,
    f32fyd_f32_fcf_yield_durability_yieldema_21d_base_v024_signal,
    f32fyd_f32_fcf_yield_durability_yieldema_63d_base_v025_signal,
    f32fyd_f32_fcf_yield_durability_yieldema_252d_base_v026_signal,
    f32fyd_f32_fcf_yield_durability_yieldmax_252d_base_v027_signal,
    f32fyd_f32_fcf_yield_durability_yieldmin_252d_base_v028_signal,
    f32fyd_f32_fcf_yield_durability_yieldrange_252d_base_v029_signal,
    f32fyd_f32_fcf_yield_durability_yieldrank_63d_base_v030_signal,
    f32fyd_f32_fcf_yield_durability_yieldrank_252d_base_v031_signal,
    f32fyd_f32_fcf_yield_durability_yieldrank_504d_base_v032_signal,
    f32fyd_f32_fcf_yield_durability_yielddiff_63d_base_v033_signal,
    f32fyd_f32_fcf_yield_durability_yielddiff_252d_base_v034_signal,
    f32fyd_f32_fcf_yield_durability_yielddiff_504d_base_v035_signal,
    f32fyd_f32_fcf_yield_durability_stabilitydiff_63d_base_v036_signal,
    f32fyd_f32_fcf_yield_durability_stabilitydiff_252d_base_v037_signal,
    f32fyd_f32_fcf_yield_durability_compoundqdiff_63d_base_v038_signal,
    f32fyd_f32_fcf_yield_durability_compoundqdiff_252d_base_v039_signal,
    f32fyd_f32_fcf_yield_durability_yieldsq_63d_base_v040_signal,
    f32fyd_f32_fcf_yield_durability_yieldsq_252d_base_v041_signal,
    f32fyd_f32_fcf_yield_durability_yieldsq_504d_base_v042_signal,
    f32fyd_f32_fcf_yield_durability_yieldmkt_base_v043_signal,
    f32fyd_f32_fcf_yield_durability_yieldmkt_63d_base_v044_signal,
    f32fyd_f32_fcf_yield_durability_yieldmkt_252d_base_v045_signal,
    f32fyd_f32_fcf_yield_durability_yieldmkt_504d_base_v046_signal,
    f32fyd_f32_fcf_yield_durability_yieldmktstd_63d_base_v047_signal,
    f32fyd_f32_fcf_yield_durability_yieldmktstd_252d_base_v048_signal,
    f32fyd_f32_fcf_yield_durability_yieldmktstd_504d_base_v049_signal,
    f32fyd_f32_fcf_yield_durability_yieldmktz_63d_base_v050_signal,
    f32fyd_f32_fcf_yield_durability_yieldmktz_252d_base_v051_signal,
    f32fyd_f32_fcf_yield_durability_yieldxprice_5d_base_v052_signal,
    f32fyd_f32_fcf_yield_durability_yieldxprice_21d_base_v053_signal,
    f32fyd_f32_fcf_yield_durability_yieldxprice_63d_base_v054_signal,
    f32fyd_f32_fcf_yield_durability_yieldxprice_252d_base_v055_signal,
    f32fyd_f32_fcf_yield_durability_stabilityxprice_63d_base_v056_signal,
    f32fyd_f32_fcf_yield_durability_stabilityxprice_252d_base_v057_signal,
    f32fyd_f32_fcf_yield_durability_compoundqxprice_63d_base_v058_signal,
    f32fyd_f32_fcf_yield_durability_compoundqxprice_252d_base_v059_signal,
    f32fyd_f32_fcf_yield_durability_yieldratio_63v252_base_v060_signal,
    f32fyd_f32_fcf_yield_durability_yieldratio_21v63_base_v061_signal,
    f32fyd_f32_fcf_yield_durability_yieldratio_252v504_base_v062_signal,
    f32fyd_f32_fcf_yield_durability_yielddiff_63m252_base_v063_signal,
    f32fyd_f32_fcf_yield_durability_yielddiff_252m504_base_v064_signal,
    f32fyd_f32_fcf_yield_durability_stabilityratio_63v252_base_v065_signal,
    f32fyd_f32_fcf_yield_durability_stabilityratio_252v504_base_v066_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusg_63d_base_v067_signal,
    f32fyd_f32_fcf_yield_durability_yieldminusg_252d_base_v068_signal,
    f32fyd_f32_fcf_yield_durability_yieldxfcfg_63d_base_v069_signal,
    f32fyd_f32_fcf_yield_durability_yieldxfcfg_252d_base_v070_signal,
    f32fyd_f32_fcf_yield_durability_yieldhigh_252d_base_v071_signal,
    f32fyd_f32_fcf_yield_durability_yieldlow_252d_base_v072_signal,
    f32fyd_f32_fcf_yield_durability_yieldxlog_63d_base_v073_signal,
    f32fyd_f32_fcf_yield_durability_yieldxlog_252d_base_v074_signal,
    f32fyd_f32_fcf_yield_durability_yieldxinvev_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_FCF_YIELD_DURABILITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf      = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    debt     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    ev = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")

    cols = {
        "closeadj": closeadj, "fcf": fcf, "ev": ev, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_fcf_yield", "_f32_fcf_yield_stability", "_f32_fcf_compound_quality")
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
    print(f"OK f32_fcf_yield_durability_base_001_075_claude: {n_features} features pass")
