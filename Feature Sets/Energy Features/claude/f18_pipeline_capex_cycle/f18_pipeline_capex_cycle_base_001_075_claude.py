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
def _f18_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f18_capex_cycle(capex, ppnenet, w):
    ci = capex / ppnenet.replace(0, np.nan)
    m = ci.rolling(w, min_periods=max(1, w // 2)).mean()
    return ci - m


def _f18_pipeline_capex_dynamics(capex, revenue, w):
    ci = capex / revenue.replace(0, np.nan)
    return ci.pct_change(periods=w)

def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl_base_v001_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl5_base_v002_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl21_base_v003_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl63_base_v004_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclz21_base_v005_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclz63_base_v006_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclret21_base_v007_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclret63_base_v008_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclsqr_base_v009_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclema21_base_v010_signal(capex, revenue, closeadj):
    result = (_f18_capex_intensity(capex, revenue)) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl_base_v011_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl5_base_v012_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl21_base_v013_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl63_base_v014_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclz21_base_v015_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclz63_base_v016_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclret21_base_v017_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclret63_base_v018_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclsqr_base_v019_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclema21_base_v020_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 5) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl_base_v021_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl5_base_v022_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl21_base_v023_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl63_base_v024_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclz21_base_v025_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclz63_base_v026_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclret21_base_v027_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclret63_base_v028_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclsqr_base_v029_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclema21_base_v030_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 10) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl_base_v031_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl5_base_v032_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl21_base_v033_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl63_base_v034_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclz21_base_v035_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclz63_base_v036_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclret21_base_v037_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclret63_base_v038_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclsqr_base_v039_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclema21_base_v040_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 21) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl_base_v041_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl5_base_v042_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl21_base_v043_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl63_base_v044_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclz21_base_v045_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclz63_base_v046_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclret21_base_v047_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclret63_base_v048_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclsqr_base_v049_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclema21_base_v050_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 42) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl_base_v051_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl5_base_v052_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl21_base_v053_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl63_base_v054_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclz21_base_v055_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclz63_base_v056_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclret21_base_v057_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclret63_base_v058_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclsqr_base_v059_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclema21_base_v060_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 63) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl_base_v061_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl5_base_v062_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl21_base_v063_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl63_base_v064_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclz21_base_v065_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclz63_base_v066_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclret21_base_v067_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclret63_base_v068_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclsqr_base_v069_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclema21_base_v070_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 126) * closeadj.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl_base_v071_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl5_base_v072_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 189) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl21_base_v073_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl63_base_v074_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18pcc_f18_pipeline_capex_cycle_cimean_5d189dclz21_base_v075_signal(capex, revenue, closeadj):
    result = _mean(_f18_capex_intensity(capex, revenue), 189) * _z(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl_base_v001_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl5_base_v002_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl21_base_v003_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dcl63_base_v004_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclz21_base_v005_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclz63_base_v006_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclret21_base_v007_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclret63_base_v008_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclsqr_base_v009_signal,
    f18pcc_f18_pipeline_capex_cycle_ciraw_5d5dclema21_base_v010_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl_base_v011_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl5_base_v012_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl21_base_v013_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dcl63_base_v014_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclz21_base_v015_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclz63_base_v016_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclret21_base_v017_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclret63_base_v018_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclsqr_base_v019_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d5dclema21_base_v020_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl_base_v021_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl5_base_v022_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl21_base_v023_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dcl63_base_v024_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclz21_base_v025_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclz63_base_v026_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclret21_base_v027_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclret63_base_v028_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclsqr_base_v029_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d10dclema21_base_v030_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl_base_v031_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl5_base_v032_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl21_base_v033_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dcl63_base_v034_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclz21_base_v035_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclz63_base_v036_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclret21_base_v037_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclret63_base_v038_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclsqr_base_v039_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d21dclema21_base_v040_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl_base_v041_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl5_base_v042_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl21_base_v043_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dcl63_base_v044_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclz21_base_v045_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclz63_base_v046_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclret21_base_v047_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclret63_base_v048_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclsqr_base_v049_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d42dclema21_base_v050_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl_base_v051_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl5_base_v052_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl21_base_v053_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dcl63_base_v054_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclz21_base_v055_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclz63_base_v056_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclret21_base_v057_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclret63_base_v058_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclsqr_base_v059_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d63dclema21_base_v060_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl_base_v061_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl5_base_v062_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl21_base_v063_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dcl63_base_v064_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclz21_base_v065_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclz63_base_v066_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclret21_base_v067_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclret63_base_v068_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclsqr_base_v069_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d126dclema21_base_v070_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl_base_v071_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl5_base_v072_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl21_base_v073_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d189dcl63_base_v074_signal,
    f18pcc_f18_pipeline_capex_cycle_cimean_5d189dclz21_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_PIPELINE_CAPEX_CYCLE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ('_f18_capex_intensity', '_f18_capex_cycle', '_f18_pipeline_capex_dynamics',)
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f18_pipeline_capex_cycle_001_075_claude: {n_features} features pass")
