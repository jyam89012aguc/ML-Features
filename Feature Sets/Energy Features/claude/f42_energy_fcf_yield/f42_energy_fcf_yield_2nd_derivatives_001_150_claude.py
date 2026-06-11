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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# ===== folder domain primitives =====
def _f42_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan).abs()


def _f42_fcf_yield_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan).abs()
    m = y.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = y.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f42_fcf_compound(fcf, marketcap, w):
    yld = fcf / marketcap.replace(0, np.nan).abs()
    return yld.rolling(w, min_periods=max(1, w // 2)).mean()

# ===== features =====
def f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v001_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v002_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v003_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v004_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v005_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v006_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v007_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v008_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v009_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v010_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v011_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v012_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v013_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v014_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v015_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v016_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v017_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v018_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * closeadj * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v019_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v020_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v021_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v022_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v023_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v024_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v025_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v026_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v027_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v028_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v029_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v030_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v031_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v032_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v033_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v034_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v035_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v036_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v037_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v038_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v039_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v040_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v041_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v042_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v043_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v044_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v045_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v046_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v047_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v048_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v049_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v050_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v051_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v052_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v053_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v054_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v055_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v056_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v057_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v058_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v059_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v060_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v061_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v062_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 126) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v063_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v064_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 126) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v065_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v066_signal(fcf, ev, closeadj):
    base = _z((_f42_fcf_yield(fcf, ev)), 126) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v067_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)).abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v068_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)).abs() * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v069_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)).abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v070_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)).abs() * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v071_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)).abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v072_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v073_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev))**2) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v074_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev))**2) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v075_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev))**2) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v076_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev))**2) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v077_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev))**2) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v078_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev))**2) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v079_signal(fcf, ev, closeadj):
    base = _ema(_mean((_f42_fcf_yield(fcf, ev)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v080_signal(fcf, ev, closeadj):
    base = _ema(_mean((_f42_fcf_yield(fcf, ev)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v081_signal(fcf, ev, closeadj):
    base = _ema(_mean((_f42_fcf_yield(fcf, ev)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v082_signal(fcf, ev, closeadj):
    base = _ema(_mean((_f42_fcf_yield(fcf, ev)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v083_signal(fcf, ev, closeadj):
    base = _ema(_mean((_f42_fcf_yield(fcf, ev)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v084_signal(fcf, ev, closeadj):
    base = _ema(_mean((_f42_fcf_yield(fcf, ev)), 21), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v085_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v086_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v087_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v088_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v089_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v090_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield(fcf, ev)) * np.log(closeadj.replace(0, np.nan).abs() + 1.0)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v091_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).max() - (_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v092_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).max() - (_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v093_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).max() - (_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v094_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).max() - (_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v095_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).max() - (_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v096_signal(fcf, ev, closeadj):
    base = ((_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).max() - (_f42_fcf_yield(fcf, ev)).rolling(21, min_periods=10).min()) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v097_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v098_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v099_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v100_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v101_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v102_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v103_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v104_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v105_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v106_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v107_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v108_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v109_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v110_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v111_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v112_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v113_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v114_signal(fcf, ev, closeadj):
    base = (_f42_fcf_yield_stability(fcf, ev, 5)) * closeadj * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v115_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v116_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v117_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v118_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v119_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v120_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v121_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v122_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v123_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v124_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v125_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v126_signal(fcf, ev, closeadj):
    base = _mean((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v127_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v128_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v129_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v130_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v131_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v132_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v133_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v134_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v135_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v136_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v137_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v138_signal(fcf, ev, closeadj):
    base = _ema((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v139_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v140_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v141_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v142_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v143_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v144_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v145_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v146_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v147_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v148_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v149_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v150_signal(fcf, ev, closeadj):
    base = _std((_f42_fcf_yield_stability(fcf, ev, 5)), 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v001_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v002_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v003_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v004_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v005_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_raw_slope_v006_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v007_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v008_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v009_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v010_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v011_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc_slope_v012_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v013_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v014_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v015_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v016_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v017_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_xc2_slope_v018_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v019_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v020_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v021_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v022_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v023_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean21_slope_v024_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v025_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v026_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v027_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v028_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v029_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_mean63_slope_v030_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v031_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v032_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v033_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v034_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v035_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema21_slope_v036_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v037_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v038_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v039_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v040_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v041_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_ema63_slope_v042_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v043_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v044_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v045_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v046_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v047_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std21_slope_v048_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v049_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v050_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v051_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v052_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v053_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_std63_slope_v054_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v055_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v056_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v057_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v058_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v059_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z63_slope_v060_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v061_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v062_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v063_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v064_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v065_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_z126_slope_v066_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v067_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v068_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v069_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v070_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v071_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_abs_xc_slope_v072_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v073_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v074_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v075_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v076_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v077_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_sq_xc_slope_v078_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v079_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v080_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v081_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v082_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v083_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_emamean21_slope_v084_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v085_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v086_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v087_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v088_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v089_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_logc_slope_v090_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v091_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v092_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v093_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v094_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v095_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_x_rngxc_slope_v096_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v097_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v098_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v099_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v100_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v101_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_raw_slope_v102_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v103_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v104_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v105_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v106_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v107_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc_slope_v108_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v109_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v110_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v111_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v112_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v113_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_xc2_slope_v114_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v115_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v116_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v117_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v118_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v119_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean21_slope_v120_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v121_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v122_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v123_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v124_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v125_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_mean63_slope_v126_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v127_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v128_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v129_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v130_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v131_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema21_slope_v132_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v133_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v134_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v135_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v136_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v137_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_ema63_slope_v138_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v139_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v140_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v141_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v142_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v143_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std21_slope_v144_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v145_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v146_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v147_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v148_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v149_signal,
    f42efy_f42_energy_fcf_yield_fcf_yield_stability_5d_std63_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_ENERGY_FCF_YIELD_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor,
        "assets": assets, "liabilities": liabilities, "equity": equity,
        "debt": debt, "cashneq": cashneq, "ppnenet": ppnenet,
        "marketcap": marketcap, "ev": ev,
        "roa": roa, "roe": roe, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f42_fcf_yield", "_f42_fcf_yield_stability", "_f42_fcf_compound")
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
    print(f"OK f42_energy_fcf_yield_2nd_derivatives_001_150_claude: {n_features} features pass")
