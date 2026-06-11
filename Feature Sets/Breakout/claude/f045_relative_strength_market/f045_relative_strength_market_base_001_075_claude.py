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
def _f045_self_return(closeadj, w):
    return closeadj.pct_change(periods=w)


def _f045_smoothed_return(closeadj, w):
    return closeadj.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()


def _f045_rs_score(closeadj, w):
    r = closeadj.pct_change(periods=w)
    rm = r.rolling(252, min_periods=63).mean()
    rs = r.rolling(252, min_periods=63).std()
    return ((r - rm) / rs.replace(0, np.nan)) * closeadj

def f045rsm_f045_relative_strength_market_sretraw_5d_base_v001_signal(closeadj):
    base = _f045_self_return(closeadj, 5)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_5d_base_v002_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 5)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_5d_base_v003_signal(closeadj):
    base = _f045_rs_score(closeadj, 5)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_10d_base_v004_signal(closeadj):
    base = _f045_self_return(closeadj, 10)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_10d_base_v005_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 10)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_10d_base_v006_signal(closeadj):
    base = _f045_rs_score(closeadj, 10)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_21d_base_v007_signal(closeadj):
    base = _f045_self_return(closeadj, 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_21d_base_v008_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_21d_base_v009_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_42d_base_v010_signal(closeadj):
    base = _f045_self_return(closeadj, 42)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_42d_base_v011_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 42)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_42d_base_v012_signal(closeadj):
    base = _f045_rs_score(closeadj, 42)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_63d_base_v013_signal(closeadj):
    base = _f045_self_return(closeadj, 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_63d_base_v014_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_63d_base_v015_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_126d_base_v016_signal(closeadj):
    base = _f045_self_return(closeadj, 126)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_126d_base_v017_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_126d_base_v018_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_189d_base_v019_signal(closeadj):
    base = _f045_self_return(closeadj, 189)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_189d_base_v020_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 189)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_189d_base_v021_signal(closeadj):
    base = _f045_rs_score(closeadj, 189)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_252d_base_v022_signal(closeadj):
    base = _f045_self_return(closeadj, 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_252d_base_v023_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_252d_base_v024_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_378d_base_v025_signal(closeadj):
    base = _f045_self_return(closeadj, 378)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_378d_base_v026_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 378)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_378d_base_v027_signal(closeadj):
    base = _f045_rs_score(closeadj, 378)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretraw_504d_base_v028_signal(closeadj):
    base = _f045_self_return(closeadj, 504)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretraw_504d_base_v029_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 504)
    result = base * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssraw_504d_base_v030_signal(closeadj):
    base = _f045_rs_score(closeadj, 504)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_5d_base_v031_signal(closeadj):
    base = _f045_self_return(closeadj, 5)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_5d_base_v032_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 5)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_5d_base_v033_signal(closeadj):
    base = _f045_rs_score(closeadj, 5)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_10d_base_v034_signal(closeadj):
    base = _f045_self_return(closeadj, 10)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_10d_base_v035_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 10)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_10d_base_v036_signal(closeadj):
    base = _f045_rs_score(closeadj, 10)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_21d_base_v037_signal(closeadj):
    base = _f045_self_return(closeadj, 21)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_21d_base_v038_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_21d_base_v039_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_42d_base_v040_signal(closeadj):
    base = _f045_self_return(closeadj, 42)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_42d_base_v041_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 42)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_42d_base_v042_signal(closeadj):
    base = _f045_rs_score(closeadj, 42)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_63d_base_v043_signal(closeadj):
    base = _f045_self_return(closeadj, 63)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_63d_base_v044_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_63d_base_v045_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_126d_base_v046_signal(closeadj):
    base = _f045_self_return(closeadj, 126)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_126d_base_v047_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 126)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_126d_base_v048_signal(closeadj):
    base = _f045_rs_score(closeadj, 126)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_189d_base_v049_signal(closeadj):
    base = _f045_self_return(closeadj, 189)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_189d_base_v050_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 189)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_189d_base_v051_signal(closeadj):
    base = _f045_rs_score(closeadj, 189)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_252d_base_v052_signal(closeadj):
    base = _f045_self_return(closeadj, 252)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_252d_base_v053_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 252)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_252d_base_v054_signal(closeadj):
    base = _f045_rs_score(closeadj, 252)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_378d_base_v055_signal(closeadj):
    base = _f045_self_return(closeadj, 378)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_378d_base_v056_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 378)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_378d_base_v057_signal(closeadj):
    base = _f045_rs_score(closeadj, 378)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretabs_504d_base_v058_signal(closeadj):
    base = _f045_self_return(closeadj, 504)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretabs_504d_base_v059_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 504)
    result = base.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rssabs_504d_base_v060_signal(closeadj):
    base = _f045_rs_score(closeadj, 504)
    result = _z(base, 252).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretsqrt_5d_base_v061_signal(closeadj):
    base = _f045_self_return(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretsqrt_5d_base_v062_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rsssqrt_5d_base_v063_signal(closeadj):
    base = _f045_rs_score(closeadj, 5)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretsqrt_10d_base_v064_signal(closeadj):
    base = _f045_self_return(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretsqrt_10d_base_v065_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rsssqrt_10d_base_v066_signal(closeadj):
    base = _f045_rs_score(closeadj, 10)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretsqrt_21d_base_v067_signal(closeadj):
    base = _f045_self_return(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretsqrt_21d_base_v068_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rsssqrt_21d_base_v069_signal(closeadj):
    base = _f045_rs_score(closeadj, 21)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretsqrt_42d_base_v070_signal(closeadj):
    base = _f045_self_return(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretsqrt_42d_base_v071_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rsssqrt_42d_base_v072_signal(closeadj):
    base = _f045_rs_score(closeadj, 42)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_sretsqrt_63d_base_v073_signal(closeadj):
    base = _f045_self_return(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_smretsqrt_63d_base_v074_signal(closeadj):
    base = _f045_smoothed_return(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f045rsm_f045_relative_strength_market_rsssqrt_63d_base_v075_signal(closeadj):
    base = _f045_rs_score(closeadj, 63)
    result = np.sign(_z(base, 252)) * _z(base, 252).abs().pow(0.5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f045rsm_f045_relative_strength_market_sretraw_5d_base_v001_signal,
    f045rsm_f045_relative_strength_market_smretraw_5d_base_v002_signal,
    f045rsm_f045_relative_strength_market_rssraw_5d_base_v003_signal,
    f045rsm_f045_relative_strength_market_sretraw_10d_base_v004_signal,
    f045rsm_f045_relative_strength_market_smretraw_10d_base_v005_signal,
    f045rsm_f045_relative_strength_market_rssraw_10d_base_v006_signal,
    f045rsm_f045_relative_strength_market_sretraw_21d_base_v007_signal,
    f045rsm_f045_relative_strength_market_smretraw_21d_base_v008_signal,
    f045rsm_f045_relative_strength_market_rssraw_21d_base_v009_signal,
    f045rsm_f045_relative_strength_market_sretraw_42d_base_v010_signal,
    f045rsm_f045_relative_strength_market_smretraw_42d_base_v011_signal,
    f045rsm_f045_relative_strength_market_rssraw_42d_base_v012_signal,
    f045rsm_f045_relative_strength_market_sretraw_63d_base_v013_signal,
    f045rsm_f045_relative_strength_market_smretraw_63d_base_v014_signal,
    f045rsm_f045_relative_strength_market_rssraw_63d_base_v015_signal,
    f045rsm_f045_relative_strength_market_sretraw_126d_base_v016_signal,
    f045rsm_f045_relative_strength_market_smretraw_126d_base_v017_signal,
    f045rsm_f045_relative_strength_market_rssraw_126d_base_v018_signal,
    f045rsm_f045_relative_strength_market_sretraw_189d_base_v019_signal,
    f045rsm_f045_relative_strength_market_smretraw_189d_base_v020_signal,
    f045rsm_f045_relative_strength_market_rssraw_189d_base_v021_signal,
    f045rsm_f045_relative_strength_market_sretraw_252d_base_v022_signal,
    f045rsm_f045_relative_strength_market_smretraw_252d_base_v023_signal,
    f045rsm_f045_relative_strength_market_rssraw_252d_base_v024_signal,
    f045rsm_f045_relative_strength_market_sretraw_378d_base_v025_signal,
    f045rsm_f045_relative_strength_market_smretraw_378d_base_v026_signal,
    f045rsm_f045_relative_strength_market_rssraw_378d_base_v027_signal,
    f045rsm_f045_relative_strength_market_sretraw_504d_base_v028_signal,
    f045rsm_f045_relative_strength_market_smretraw_504d_base_v029_signal,
    f045rsm_f045_relative_strength_market_rssraw_504d_base_v030_signal,
    f045rsm_f045_relative_strength_market_sretabs_5d_base_v031_signal,
    f045rsm_f045_relative_strength_market_smretabs_5d_base_v032_signal,
    f045rsm_f045_relative_strength_market_rssabs_5d_base_v033_signal,
    f045rsm_f045_relative_strength_market_sretabs_10d_base_v034_signal,
    f045rsm_f045_relative_strength_market_smretabs_10d_base_v035_signal,
    f045rsm_f045_relative_strength_market_rssabs_10d_base_v036_signal,
    f045rsm_f045_relative_strength_market_sretabs_21d_base_v037_signal,
    f045rsm_f045_relative_strength_market_smretabs_21d_base_v038_signal,
    f045rsm_f045_relative_strength_market_rssabs_21d_base_v039_signal,
    f045rsm_f045_relative_strength_market_sretabs_42d_base_v040_signal,
    f045rsm_f045_relative_strength_market_smretabs_42d_base_v041_signal,
    f045rsm_f045_relative_strength_market_rssabs_42d_base_v042_signal,
    f045rsm_f045_relative_strength_market_sretabs_63d_base_v043_signal,
    f045rsm_f045_relative_strength_market_smretabs_63d_base_v044_signal,
    f045rsm_f045_relative_strength_market_rssabs_63d_base_v045_signal,
    f045rsm_f045_relative_strength_market_sretabs_126d_base_v046_signal,
    f045rsm_f045_relative_strength_market_smretabs_126d_base_v047_signal,
    f045rsm_f045_relative_strength_market_rssabs_126d_base_v048_signal,
    f045rsm_f045_relative_strength_market_sretabs_189d_base_v049_signal,
    f045rsm_f045_relative_strength_market_smretabs_189d_base_v050_signal,
    f045rsm_f045_relative_strength_market_rssabs_189d_base_v051_signal,
    f045rsm_f045_relative_strength_market_sretabs_252d_base_v052_signal,
    f045rsm_f045_relative_strength_market_smretabs_252d_base_v053_signal,
    f045rsm_f045_relative_strength_market_rssabs_252d_base_v054_signal,
    f045rsm_f045_relative_strength_market_sretabs_378d_base_v055_signal,
    f045rsm_f045_relative_strength_market_smretabs_378d_base_v056_signal,
    f045rsm_f045_relative_strength_market_rssabs_378d_base_v057_signal,
    f045rsm_f045_relative_strength_market_sretabs_504d_base_v058_signal,
    f045rsm_f045_relative_strength_market_smretabs_504d_base_v059_signal,
    f045rsm_f045_relative_strength_market_rssabs_504d_base_v060_signal,
    f045rsm_f045_relative_strength_market_sretsqrt_5d_base_v061_signal,
    f045rsm_f045_relative_strength_market_smretsqrt_5d_base_v062_signal,
    f045rsm_f045_relative_strength_market_rsssqrt_5d_base_v063_signal,
    f045rsm_f045_relative_strength_market_sretsqrt_10d_base_v064_signal,
    f045rsm_f045_relative_strength_market_smretsqrt_10d_base_v065_signal,
    f045rsm_f045_relative_strength_market_rsssqrt_10d_base_v066_signal,
    f045rsm_f045_relative_strength_market_sretsqrt_21d_base_v067_signal,
    f045rsm_f045_relative_strength_market_smretsqrt_21d_base_v068_signal,
    f045rsm_f045_relative_strength_market_rsssqrt_21d_base_v069_signal,
    f045rsm_f045_relative_strength_market_sretsqrt_42d_base_v070_signal,
    f045rsm_f045_relative_strength_market_smretsqrt_42d_base_v071_signal,
    f045rsm_f045_relative_strength_market_rsssqrt_42d_base_v072_signal,
    f045rsm_f045_relative_strength_market_sretsqrt_63d_base_v073_signal,
    f045rsm_f045_relative_strength_market_smretsqrt_63d_base_v074_signal,
    f045rsm_f045_relative_strength_market_rsssqrt_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F045_RELATIVE_STRENGTH_MARKET_REGISTRY_001_075 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f045_self_return", "_f045_smoothed_return", "_f045_rs_score")
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
    print(f"OK {__file__}: {n_features} features pass")
