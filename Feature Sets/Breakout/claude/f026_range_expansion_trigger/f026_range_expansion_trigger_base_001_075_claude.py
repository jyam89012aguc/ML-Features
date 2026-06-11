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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _f026_today_range(high, low, w):
    rng = (high - low).abs()
    return rng.rolling(w, min_periods=max(1, w // 2)).mean()


def _f026_range_expansion(high, low, w):
    rng = (high - low).abs()
    avg = rng.rolling(w, min_periods=max(1, w // 2)).mean()
    return rng / avg.replace(0, np.nan)


def _f026_expansion_after_compress(high, low, w):
    rng = (high - low).abs()
    short_avg = rng.rolling(max(2, w // 4), min_periods=1).mean()
    long_avg = rng.rolling(w, min_periods=max(1, w // 2)).mean()
    return (short_avg - long_avg) / long_avg.replace(0, np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_5d_base_v001_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 5)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_5d_base_v002_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 5)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_5d_base_v003_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_10d_base_v004_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 10)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_10d_base_v005_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 10)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_10d_base_v006_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_21d_base_v007_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 21)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_21d_base_v008_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_21d_base_v009_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_42d_base_v010_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_42d_base_v011_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_42d_base_v012_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_63d_base_v013_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_63d_base_v014_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_63d_base_v015_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_126d_base_v016_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_126d_base_v017_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_126d_base_v018_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_189d_base_v019_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_189d_base_v020_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_189d_base_v021_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_252d_base_v022_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_252d_base_v023_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_252d_base_v024_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_378d_base_v025_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_378d_base_v026_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_378d_base_v027_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrid_504d_base_v028_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexid_504d_base_v029_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacid_504d_base_v030_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_5d_base_v031_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 5)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_5d_base_v032_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 5)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_5d_base_v033_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_10d_base_v034_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 10)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_10d_base_v035_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 10)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_10d_base_v036_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_21d_base_v037_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 21)
    result = _z(base.abs(), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_21d_base_v038_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_21d_base_v039_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_42d_base_v040_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_42d_base_v041_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_42d_base_v042_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_63d_base_v043_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_63d_base_v044_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_63d_base_v045_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_126d_base_v046_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_126d_base_v047_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_126d_base_v048_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_189d_base_v049_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_189d_base_v050_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_189d_base_v051_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_252d_base_v052_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_252d_base_v053_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_252d_base_v054_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_378d_base_v055_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_378d_base_v056_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_378d_base_v057_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrab_504d_base_v058_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexab_504d_base_v059_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacab_504d_base_v060_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrsq_5d_base_v061_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 5)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexsq_5d_base_v062_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 5)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacsq_5d_base_v063_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrsq_10d_base_v064_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 10)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexsq_10d_base_v065_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 10)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacsq_10d_base_v066_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrsq_21d_base_v067_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 21)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexsq_21d_base_v068_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 21)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacsq_21d_base_v069_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrsq_42d_base_v070_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 42)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexsq_42d_base_v071_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 42)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacsq_42d_base_v072_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_tdrsq_63d_base_v073_signal(high, low, closeadj):
    base = _f026_today_range(high, low, 63)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_rexsq_63d_base_v074_signal(high, low, closeadj):
    base = _f026_range_expansion(high, low, 63)
    result = np.tanh(_z(base, 63)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f026ret_f026_range_expansion_trigger_eacsq_63d_base_v075_signal(high, low, closeadj):
    base = _f026_expansion_after_compress(high, low, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f026ret_f026_range_expansion_trigger_tdrid_5d_base_v001_signal,
    f026ret_f026_range_expansion_trigger_rexid_5d_base_v002_signal,
    f026ret_f026_range_expansion_trigger_eacid_5d_base_v003_signal,
    f026ret_f026_range_expansion_trigger_tdrid_10d_base_v004_signal,
    f026ret_f026_range_expansion_trigger_rexid_10d_base_v005_signal,
    f026ret_f026_range_expansion_trigger_eacid_10d_base_v006_signal,
    f026ret_f026_range_expansion_trigger_tdrid_21d_base_v007_signal,
    f026ret_f026_range_expansion_trigger_rexid_21d_base_v008_signal,
    f026ret_f026_range_expansion_trigger_eacid_21d_base_v009_signal,
    f026ret_f026_range_expansion_trigger_tdrid_42d_base_v010_signal,
    f026ret_f026_range_expansion_trigger_rexid_42d_base_v011_signal,
    f026ret_f026_range_expansion_trigger_eacid_42d_base_v012_signal,
    f026ret_f026_range_expansion_trigger_tdrid_63d_base_v013_signal,
    f026ret_f026_range_expansion_trigger_rexid_63d_base_v014_signal,
    f026ret_f026_range_expansion_trigger_eacid_63d_base_v015_signal,
    f026ret_f026_range_expansion_trigger_tdrid_126d_base_v016_signal,
    f026ret_f026_range_expansion_trigger_rexid_126d_base_v017_signal,
    f026ret_f026_range_expansion_trigger_eacid_126d_base_v018_signal,
    f026ret_f026_range_expansion_trigger_tdrid_189d_base_v019_signal,
    f026ret_f026_range_expansion_trigger_rexid_189d_base_v020_signal,
    f026ret_f026_range_expansion_trigger_eacid_189d_base_v021_signal,
    f026ret_f026_range_expansion_trigger_tdrid_252d_base_v022_signal,
    f026ret_f026_range_expansion_trigger_rexid_252d_base_v023_signal,
    f026ret_f026_range_expansion_trigger_eacid_252d_base_v024_signal,
    f026ret_f026_range_expansion_trigger_tdrid_378d_base_v025_signal,
    f026ret_f026_range_expansion_trigger_rexid_378d_base_v026_signal,
    f026ret_f026_range_expansion_trigger_eacid_378d_base_v027_signal,
    f026ret_f026_range_expansion_trigger_tdrid_504d_base_v028_signal,
    f026ret_f026_range_expansion_trigger_rexid_504d_base_v029_signal,
    f026ret_f026_range_expansion_trigger_eacid_504d_base_v030_signal,
    f026ret_f026_range_expansion_trigger_tdrab_5d_base_v031_signal,
    f026ret_f026_range_expansion_trigger_rexab_5d_base_v032_signal,
    f026ret_f026_range_expansion_trigger_eacab_5d_base_v033_signal,
    f026ret_f026_range_expansion_trigger_tdrab_10d_base_v034_signal,
    f026ret_f026_range_expansion_trigger_rexab_10d_base_v035_signal,
    f026ret_f026_range_expansion_trigger_eacab_10d_base_v036_signal,
    f026ret_f026_range_expansion_trigger_tdrab_21d_base_v037_signal,
    f026ret_f026_range_expansion_trigger_rexab_21d_base_v038_signal,
    f026ret_f026_range_expansion_trigger_eacab_21d_base_v039_signal,
    f026ret_f026_range_expansion_trigger_tdrab_42d_base_v040_signal,
    f026ret_f026_range_expansion_trigger_rexab_42d_base_v041_signal,
    f026ret_f026_range_expansion_trigger_eacab_42d_base_v042_signal,
    f026ret_f026_range_expansion_trigger_tdrab_63d_base_v043_signal,
    f026ret_f026_range_expansion_trigger_rexab_63d_base_v044_signal,
    f026ret_f026_range_expansion_trigger_eacab_63d_base_v045_signal,
    f026ret_f026_range_expansion_trigger_tdrab_126d_base_v046_signal,
    f026ret_f026_range_expansion_trigger_rexab_126d_base_v047_signal,
    f026ret_f026_range_expansion_trigger_eacab_126d_base_v048_signal,
    f026ret_f026_range_expansion_trigger_tdrab_189d_base_v049_signal,
    f026ret_f026_range_expansion_trigger_rexab_189d_base_v050_signal,
    f026ret_f026_range_expansion_trigger_eacab_189d_base_v051_signal,
    f026ret_f026_range_expansion_trigger_tdrab_252d_base_v052_signal,
    f026ret_f026_range_expansion_trigger_rexab_252d_base_v053_signal,
    f026ret_f026_range_expansion_trigger_eacab_252d_base_v054_signal,
    f026ret_f026_range_expansion_trigger_tdrab_378d_base_v055_signal,
    f026ret_f026_range_expansion_trigger_rexab_378d_base_v056_signal,
    f026ret_f026_range_expansion_trigger_eacab_378d_base_v057_signal,
    f026ret_f026_range_expansion_trigger_tdrab_504d_base_v058_signal,
    f026ret_f026_range_expansion_trigger_rexab_504d_base_v059_signal,
    f026ret_f026_range_expansion_trigger_eacab_504d_base_v060_signal,
    f026ret_f026_range_expansion_trigger_tdrsq_5d_base_v061_signal,
    f026ret_f026_range_expansion_trigger_rexsq_5d_base_v062_signal,
    f026ret_f026_range_expansion_trigger_eacsq_5d_base_v063_signal,
    f026ret_f026_range_expansion_trigger_tdrsq_10d_base_v064_signal,
    f026ret_f026_range_expansion_trigger_rexsq_10d_base_v065_signal,
    f026ret_f026_range_expansion_trigger_eacsq_10d_base_v066_signal,
    f026ret_f026_range_expansion_trigger_tdrsq_21d_base_v067_signal,
    f026ret_f026_range_expansion_trigger_rexsq_21d_base_v068_signal,
    f026ret_f026_range_expansion_trigger_eacsq_21d_base_v069_signal,
    f026ret_f026_range_expansion_trigger_tdrsq_42d_base_v070_signal,
    f026ret_f026_range_expansion_trigger_rexsq_42d_base_v071_signal,
    f026ret_f026_range_expansion_trigger_eacsq_42d_base_v072_signal,
    f026ret_f026_range_expansion_trigger_tdrsq_63d_base_v073_signal,
    f026ret_f026_range_expansion_trigger_rexsq_63d_base_v074_signal,
    f026ret_f026_range_expansion_trigger_eacsq_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F026_RANGE_EXPANSION_TRIGGER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f026_today_range', '_f026_range_expansion', '_f026_expansion_after_compress')
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
    print(f"OK f026_range_expansion_trigger_base_001_075_claude: {n_features} features pass")
