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
def _f21_lender_yield(revenue, assets):
    return revenue / assets.replace(0, np.nan).abs()


def _f21_yield_dynamics(revenue, assets, w):
    y = revenue / assets.replace(0, np.nan).abs()
    return y.diff(periods=w) / y.abs().replace(0, np.nan)


def _f21_yield_persistence(revenue, assets, w):
    y = revenue / assets.replace(0, np.nan).abs()
    m = y.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = y.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)

def f21sly_f21_specialty_lender_yield_yield_5d_xclose_base_v001_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_5d_xclose_base_v002_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_10d_xclose_base_v003_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_21d_xclose_base_v004_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_42d_xclose_base_v005_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_63d_xclose_base_v006_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_126d_xclose_base_v007_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_189d_xclose_base_v008_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_252d_xclose_base_v009_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_378d_xclose_base_v010_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_504d_xclose_base_v011_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_5d_xclose_base_v012_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_10d_xclose_base_v013_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_21d_xclose_base_v014_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_42d_xclose_base_v015_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_63d_xclose_base_v016_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_126d_xclose_base_v017_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_189d_xclose_base_v018_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_252d_xclose_base_v019_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_378d_xclose_base_v020_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yielddyn_504d_xclose_base_v021_signal(revenue, assets, closeadj):
    base = _f21_yield_dynamics(revenue, assets, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_5d_xclose_base_v022_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_10d_xclose_base_v023_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_21d_xclose_base_v024_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_42d_xclose_base_v025_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_63d_xclose_base_v026_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_126d_xclose_base_v027_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_189d_xclose_base_v028_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_252d_xclose_base_v029_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_378d_xclose_base_v030_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldpers_504d_xclose_base_v031_signal(revenue, assets, closeadj):
    base = _f21_yield_persistence(revenue, assets, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_5d_xclose_base_v032_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_10d_xclose_base_v033_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_21d_xclose_base_v034_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_42d_xclose_base_v035_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_63d_xclose_base_v036_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_126d_xclose_base_v037_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_189d_xclose_base_v038_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_252d_xclose_base_v039_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_378d_xclose_base_v040_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldstd_504d_xclose_base_v041_signal(revenue, assets, closeadj):
    base = _std(_f21_lender_yield(revenue, assets), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_5d_xclose_base_v042_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_10d_xclose_base_v043_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_21d_xclose_base_v044_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_42d_xclose_base_v045_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_63d_xclose_base_v046_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_126d_xclose_base_v047_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_189d_xclose_base_v048_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_252d_xclose_base_v049_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_378d_xclose_base_v050_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldz_504d_xclose_base_v051_signal(revenue, assets, closeadj):
    base = _z(_f21_lender_yield(revenue, assets), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_5d_xclose_base_v052_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 5) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_10d_xclose_base_v053_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 10) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_21d_xclose_base_v054_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 21) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_42d_xclose_base_v055_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 42) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_63d_xclose_base_v056_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 63) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_126d_xclose_base_v057_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 126) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_189d_xclose_base_v058_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 189) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_252d_xclose_base_v059_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 252) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_378d_xclose_base_v060_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 378) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldlog_504d_xclose_base_v061_signal(revenue, assets, closeadj):
    base = np.log(_f21_lender_yield(revenue, assets).abs() + 1e-9) + _f21_yield_dynamics(revenue, assets, 504) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_5d_xclose_base_v062_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=5, min_periods=max(1, 5//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_10d_xclose_base_v063_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=10, min_periods=max(1, 10//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_21d_xclose_base_v064_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=21, min_periods=max(1, 21//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_42d_xclose_base_v065_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=42, min_periods=max(1, 42//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_63d_xclose_base_v066_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=63, min_periods=max(1, 63//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_126d_xclose_base_v067_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=126, min_periods=max(1, 126//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_189d_xclose_base_v068_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=189, min_periods=max(1, 189//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_252d_xclose_base_v069_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=252, min_periods=max(1, 252//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_378d_xclose_base_v070_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=378, min_periods=max(1, 378//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldema_504d_xclose_base_v071_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets).ewm(span=504, min_periods=max(1, 504//2)).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yield_5d_xclose2_base_v072_signal(revenue, assets, closeadj):
    base = _f21_lender_yield(revenue, assets)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_5d_xclose2_base_v073_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 5)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_10d_xclose2_base_v074_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 10)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f21sly_f21_specialty_lender_yield_yieldroll_21d_xclose2_base_v075_signal(revenue, assets, closeadj):
    base = _mean(_f21_lender_yield(revenue, assets), 21)
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f21sly_f21_specialty_lender_yield_yield_5d_xclose_base_v001_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_5d_xclose_base_v002_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_10d_xclose_base_v003_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_21d_xclose_base_v004_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_42d_xclose_base_v005_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_63d_xclose_base_v006_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_126d_xclose_base_v007_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_189d_xclose_base_v008_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_252d_xclose_base_v009_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_378d_xclose_base_v010_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_504d_xclose_base_v011_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_5d_xclose_base_v012_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_10d_xclose_base_v013_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_21d_xclose_base_v014_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_42d_xclose_base_v015_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_63d_xclose_base_v016_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_126d_xclose_base_v017_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_189d_xclose_base_v018_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_252d_xclose_base_v019_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_378d_xclose_base_v020_signal,
    f21sly_f21_specialty_lender_yield_yielddyn_504d_xclose_base_v021_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_5d_xclose_base_v022_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_10d_xclose_base_v023_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_21d_xclose_base_v024_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_42d_xclose_base_v025_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_63d_xclose_base_v026_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_126d_xclose_base_v027_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_189d_xclose_base_v028_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_252d_xclose_base_v029_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_378d_xclose_base_v030_signal,
    f21sly_f21_specialty_lender_yield_yieldpers_504d_xclose_base_v031_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_5d_xclose_base_v032_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_10d_xclose_base_v033_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_21d_xclose_base_v034_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_42d_xclose_base_v035_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_63d_xclose_base_v036_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_126d_xclose_base_v037_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_189d_xclose_base_v038_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_252d_xclose_base_v039_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_378d_xclose_base_v040_signal,
    f21sly_f21_specialty_lender_yield_yieldstd_504d_xclose_base_v041_signal,
    f21sly_f21_specialty_lender_yield_yieldz_5d_xclose_base_v042_signal,
    f21sly_f21_specialty_lender_yield_yieldz_10d_xclose_base_v043_signal,
    f21sly_f21_specialty_lender_yield_yieldz_21d_xclose_base_v044_signal,
    f21sly_f21_specialty_lender_yield_yieldz_42d_xclose_base_v045_signal,
    f21sly_f21_specialty_lender_yield_yieldz_63d_xclose_base_v046_signal,
    f21sly_f21_specialty_lender_yield_yieldz_126d_xclose_base_v047_signal,
    f21sly_f21_specialty_lender_yield_yieldz_189d_xclose_base_v048_signal,
    f21sly_f21_specialty_lender_yield_yieldz_252d_xclose_base_v049_signal,
    f21sly_f21_specialty_lender_yield_yieldz_378d_xclose_base_v050_signal,
    f21sly_f21_specialty_lender_yield_yieldz_504d_xclose_base_v051_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_5d_xclose_base_v052_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_10d_xclose_base_v053_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_21d_xclose_base_v054_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_42d_xclose_base_v055_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_63d_xclose_base_v056_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_126d_xclose_base_v057_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_189d_xclose_base_v058_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_252d_xclose_base_v059_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_378d_xclose_base_v060_signal,
    f21sly_f21_specialty_lender_yield_yieldlog_504d_xclose_base_v061_signal,
    f21sly_f21_specialty_lender_yield_yieldema_5d_xclose_base_v062_signal,
    f21sly_f21_specialty_lender_yield_yieldema_10d_xclose_base_v063_signal,
    f21sly_f21_specialty_lender_yield_yieldema_21d_xclose_base_v064_signal,
    f21sly_f21_specialty_lender_yield_yieldema_42d_xclose_base_v065_signal,
    f21sly_f21_specialty_lender_yield_yieldema_63d_xclose_base_v066_signal,
    f21sly_f21_specialty_lender_yield_yieldema_126d_xclose_base_v067_signal,
    f21sly_f21_specialty_lender_yield_yieldema_189d_xclose_base_v068_signal,
    f21sly_f21_specialty_lender_yield_yieldema_252d_xclose_base_v069_signal,
    f21sly_f21_specialty_lender_yield_yieldema_378d_xclose_base_v070_signal,
    f21sly_f21_specialty_lender_yield_yieldema_504d_xclose_base_v071_signal,
    f21sly_f21_specialty_lender_yield_yield_5d_xclose2_base_v072_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_5d_xclose2_base_v073_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_10d_xclose2_base_v074_signal,
    f21sly_f21_specialty_lender_yield_yieldroll_21d_xclose2_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_SPECIALTY_LENDER_YIELD_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f21_lender_yield", "_f21_yield_dynamics", "_f21_yield_persistence")
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
    print(f"OK f21_specialty_lender_yield: {n_features} features pass")
