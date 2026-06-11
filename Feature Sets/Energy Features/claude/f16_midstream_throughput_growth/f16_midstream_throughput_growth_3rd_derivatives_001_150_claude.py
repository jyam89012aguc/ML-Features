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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f16_revenue_stability(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f16_throughput_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f16_revenue_smoothness(revenue, ppnenet, w):
    r = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    p = ppnenet.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return (r / p) / (1.0 + sd / r.replace(0, np.nan))

def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk5d_jerk_v001_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk10d_jerk_v002_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk21d_jerk_v003_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk42d_jerk_v004_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk63d_jerk_v005_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk126d_jerk_v006_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk5d_jerk_v007_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk10d_jerk_v008_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk21d_jerk_v009_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk42d_jerk_v010_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 5), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk63d_jerk_v011_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk126d_jerk_v012_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk5d_jerk_v013_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk10d_jerk_v014_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk21d_jerk_v015_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk42d_jerk_v016_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk63d_jerk_v017_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk126d_jerk_v018_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk5d_jerk_v019_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk10d_jerk_v020_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk21d_jerk_v021_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk42d_jerk_v022_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk63d_jerk_v023_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk126d_jerk_v024_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk5d_jerk_v025_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk10d_jerk_v026_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk21d_jerk_v027_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk42d_jerk_v028_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk63d_jerk_v029_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk126d_jerk_v030_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk5d_jerk_v031_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk10d_jerk_v032_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk21d_jerk_v033_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk42d_jerk_v034_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk63d_jerk_v035_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk126d_jerk_v036_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * _z(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk5d_jerk_v037_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk10d_jerk_v038_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk21d_jerk_v039_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk42d_jerk_v040_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk63d_jerk_v041_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk126d_jerk_v042_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk5d_jerk_v043_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk10d_jerk_v044_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk21d_jerk_v045_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk42d_jerk_v046_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk63d_jerk_v047_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk126d_jerk_v048_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.pct_change(63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk5d_jerk_v049_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk10d_jerk_v050_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk21d_jerk_v051_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk42d_jerk_v052_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk63d_jerk_v053_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk126d_jerk_v054_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk5d_jerk_v055_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk10d_jerk_v056_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk21d_jerk_v057_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk42d_jerk_v058_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk63d_jerk_v059_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk126d_jerk_v060_signal(revenue, closeadj):
    result = _jerk((_f16_revenue_stability(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk5d_jerk_v061_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk10d_jerk_v062_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk21d_jerk_v063_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk42d_jerk_v064_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk63d_jerk_v065_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk126d_jerk_v066_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk5d_jerk_v067_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk10d_jerk_v068_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk21d_jerk_v069_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk42d_jerk_v070_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 5), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk63d_jerk_v071_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk126d_jerk_v072_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk5d_jerk_v073_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk10d_jerk_v074_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk21d_jerk_v075_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk42d_jerk_v076_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk63d_jerk_v077_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk126d_jerk_v078_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk5d_jerk_v079_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk10d_jerk_v080_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk21d_jerk_v081_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk42d_jerk_v082_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk63d_jerk_v083_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk126d_jerk_v084_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk5d_jerk_v085_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk10d_jerk_v086_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk21d_jerk_v087_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk42d_jerk_v088_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk63d_jerk_v089_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk126d_jerk_v090_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk5d_jerk_v091_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk10d_jerk_v092_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk21d_jerk_v093_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk42d_jerk_v094_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk63d_jerk_v095_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk126d_jerk_v096_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * _z(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk5d_jerk_v097_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk10d_jerk_v098_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk21d_jerk_v099_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk42d_jerk_v100_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk63d_jerk_v101_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk126d_jerk_v102_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk5d_jerk_v103_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk10d_jerk_v104_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk21d_jerk_v105_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk42d_jerk_v106_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk63d_jerk_v107_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk126d_jerk_v108_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.pct_change(63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk5d_jerk_v109_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk10d_jerk_v110_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk21d_jerk_v111_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk42d_jerk_v112_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk63d_jerk_v113_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk126d_jerk_v114_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk5d_jerk_v115_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.ewm(span=21, min_periods=10).mean(), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk10d_jerk_v116_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.ewm(span=21, min_periods=10).mean(), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk21d_jerk_v117_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.ewm(span=21, min_periods=10).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk42d_jerk_v118_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.ewm(span=21, min_periods=10).mean(), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk63d_jerk_v119_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.ewm(span=21, min_periods=10).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk126d_jerk_v120_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 5) * closeadj.ewm(span=21, min_periods=10).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk5d_jerk_v121_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk10d_jerk_v122_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk21d_jerk_v123_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk42d_jerk_v124_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk63d_jerk_v125_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk126d_jerk_v126_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk5d_jerk_v127_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk10d_jerk_v128_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk21d_jerk_v129_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk42d_jerk_v130_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 5), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk63d_jerk_v131_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk126d_jerk_v132_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk5d_jerk_v133_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk10d_jerk_v134_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk21d_jerk_v135_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk42d_jerk_v136_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk63d_jerk_v137_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk126d_jerk_v138_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk5d_jerk_v139_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk10d_jerk_v140_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk21d_jerk_v141_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk42d_jerk_v142_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk63d_jerk_v143_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk126d_jerk_v144_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk5d_jerk_v145_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _z(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk10d_jerk_v146_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _z(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk21d_jerk_v147_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _z(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk42d_jerk_v148_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _z(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk63d_jerk_v149_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _z(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk126d_jerk_v150_signal(revenue, closeadj):
    result = _jerk(_mean(_f16_revenue_stability(revenue, 5), 10) * _z(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk5d_jerk_v001_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk10d_jerk_v002_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk21d_jerk_v003_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk42d_jerk_v004_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk63d_jerk_v005_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl_jerk126d_jerk_v006_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk5d_jerk_v007_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk10d_jerk_v008_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk21d_jerk_v009_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk42d_jerk_v010_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk63d_jerk_v011_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl5_jerk126d_jerk_v012_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk5d_jerk_v013_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk10d_jerk_v014_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk21d_jerk_v015_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk42d_jerk_v016_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk63d_jerk_v017_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl21_jerk126d_jerk_v018_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk5d_jerk_v019_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk10d_jerk_v020_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk21d_jerk_v021_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk42d_jerk_v022_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk63d_jerk_v023_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dcl63_jerk126d_jerk_v024_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk5d_jerk_v025_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk10d_jerk_v026_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk21d_jerk_v027_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk42d_jerk_v028_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk63d_jerk_v029_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz21_jerk126d_jerk_v030_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk5d_jerk_v031_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk10d_jerk_v032_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk21d_jerk_v033_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk42d_jerk_v034_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk63d_jerk_v035_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclz63_jerk126d_jerk_v036_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk5d_jerk_v037_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk10d_jerk_v038_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk21d_jerk_v039_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk42d_jerk_v040_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk63d_jerk_v041_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret21_jerk126d_jerk_v042_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk5d_jerk_v043_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk10d_jerk_v044_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk21d_jerk_v045_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk42d_jerk_v046_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk63d_jerk_v047_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclret63_jerk126d_jerk_v048_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk5d_jerk_v049_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk10d_jerk_v050_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk21d_jerk_v051_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk42d_jerk_v052_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk63d_jerk_v053_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclsqr_jerk126d_jerk_v054_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk5d_jerk_v055_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk10d_jerk_v056_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk21d_jerk_v057_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk42d_jerk_v058_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk63d_jerk_v059_signal,
    f16mtg_f16_midstream_throughput_growth_rsraw_5d5dclema21_jerk126d_jerk_v060_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk5d_jerk_v061_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk10d_jerk_v062_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk21d_jerk_v063_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk42d_jerk_v064_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk63d_jerk_v065_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl_jerk126d_jerk_v066_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk5d_jerk_v067_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk10d_jerk_v068_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk21d_jerk_v069_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk42d_jerk_v070_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk63d_jerk_v071_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl5_jerk126d_jerk_v072_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk5d_jerk_v073_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk10d_jerk_v074_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk21d_jerk_v075_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk42d_jerk_v076_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk63d_jerk_v077_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl21_jerk126d_jerk_v078_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk5d_jerk_v079_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk10d_jerk_v080_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk21d_jerk_v081_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk42d_jerk_v082_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk63d_jerk_v083_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dcl63_jerk126d_jerk_v084_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk5d_jerk_v085_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk10d_jerk_v086_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk21d_jerk_v087_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk42d_jerk_v088_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk63d_jerk_v089_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz21_jerk126d_jerk_v090_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk5d_jerk_v091_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk10d_jerk_v092_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk21d_jerk_v093_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk42d_jerk_v094_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk63d_jerk_v095_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclz63_jerk126d_jerk_v096_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk5d_jerk_v097_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk10d_jerk_v098_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk21d_jerk_v099_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk42d_jerk_v100_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk63d_jerk_v101_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret21_jerk126d_jerk_v102_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk5d_jerk_v103_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk10d_jerk_v104_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk21d_jerk_v105_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk42d_jerk_v106_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk63d_jerk_v107_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclret63_jerk126d_jerk_v108_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk5d_jerk_v109_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk10d_jerk_v110_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk21d_jerk_v111_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk42d_jerk_v112_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk63d_jerk_v113_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclsqr_jerk126d_jerk_v114_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk5d_jerk_v115_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk10d_jerk_v116_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk21d_jerk_v117_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk42d_jerk_v118_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk63d_jerk_v119_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d5dclema21_jerk126d_jerk_v120_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk5d_jerk_v121_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk10d_jerk_v122_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk21d_jerk_v123_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk42d_jerk_v124_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk63d_jerk_v125_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl_jerk126d_jerk_v126_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk5d_jerk_v127_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk10d_jerk_v128_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk21d_jerk_v129_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk42d_jerk_v130_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk63d_jerk_v131_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl5_jerk126d_jerk_v132_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk5d_jerk_v133_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk10d_jerk_v134_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk21d_jerk_v135_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk42d_jerk_v136_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk63d_jerk_v137_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl21_jerk126d_jerk_v138_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk5d_jerk_v139_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk10d_jerk_v140_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk21d_jerk_v141_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk42d_jerk_v142_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk63d_jerk_v143_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dcl63_jerk126d_jerk_v144_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk5d_jerk_v145_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk10d_jerk_v146_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk21d_jerk_v147_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk42d_jerk_v148_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk63d_jerk_v149_signal,
    f16mtg_f16_midstream_throughput_growth_rsmean_5d10dclz21_jerk126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_MIDSTREAM_THROUGHPUT_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "revenue": revenue, "capex": capex,
            "ppnenet": ppnenet, "assets": assets, "deferredrev": deferredrev}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f16_revenue_stability', '_f16_throughput_growth', '_f16_revenue_smoothness',)
    import hashlib
    seen_bodies = set()
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
        body = "\n".join(l.strip() for l in src.splitlines()
                          if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("def "))
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(h)
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f16_midstream_throughput_growth_jerk_001_150_claude: {n_features} features pass")
