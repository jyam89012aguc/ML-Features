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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()

# ===== folder domain primitives =====
def _f20_reinsurance_pulse(revenue, w):
    return revenue.pct_change(periods=w)


def _f20_cycle_position(revenue, netmargin, w):
    rev_g = revenue.pct_change(periods=w)
    nm_sm = netmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rev_g * nm_sm


def _f20_pricing_cycle(revenue, netmargin, w):
    rev_z_m = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    rev_z_s = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).std()
    rev_z = (revenue.pct_change(periods=w) - rev_z_m) / rev_z_s.replace(0, np.nan)
    return rev_z * netmargin

def f20rcy_f20_reinsurance_cycle_pulse_5d_base_v001_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_8d_base_v002_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_10d_base_v003_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_15d_base_v004_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_21d_base_v005_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_30d_base_v006_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_42d_base_v007_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_63d_base_v008_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_90d_base_v009_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_126d_base_v010_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_150d_base_v011_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_189d_base_v012_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_252d_base_v013_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_378d_base_v014_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_504d_base_v015_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    result = p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_5d_base_v016_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    result = _ema(p, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_8d_base_v017_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    result = _ema(p, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_10d_base_v018_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    result = _ema(p, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_15d_base_v019_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    result = _ema(p, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_21d_base_v020_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_30d_base_v021_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    result = _ema(p, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_42d_base_v022_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    result = _ema(p, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_63d_base_v023_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    result = _ema(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_90d_base_v024_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    result = _ema(p, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_126d_base_v025_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    result = _ema(p, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_150d_base_v026_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    result = _ema(p, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_189d_base_v027_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    result = _ema(p, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_252d_base_v028_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    result = _ema(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_378d_base_v029_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    result = _ema(p, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_504d_base_v030_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    result = _ema(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_5d_base_v031_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    result = _z(p, 252) * closeadj * (0.0500)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_8d_base_v032_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    result = _z(p, 252) * closeadj * (0.0800)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_10d_base_v033_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    result = _z(p, 252) * closeadj * (0.1000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_15d_base_v034_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    result = _z(p, 252) * closeadj * (0.1500)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_21d_base_v035_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    result = _z(p, 252) * closeadj * (0.2100)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_30d_base_v036_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    result = _z(p, 252) * closeadj * (0.3000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_42d_base_v037_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    result = _z(p, 252) * closeadj * (0.4200)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_63d_base_v038_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    result = _z(p, 252) * closeadj * (0.6300)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_90d_base_v039_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    result = _z(p, 252) * closeadj * (0.9000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_126d_base_v040_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    result = _z(p, 252) * closeadj * (1.2600)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_150d_base_v041_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    result = _z(p, 252) * closeadj * (1.5000)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_189d_base_v042_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    result = _z(p, 252) * closeadj * (1.8900)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_252d_base_v043_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    result = _z(p, 252) * closeadj * (2.5200)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_378d_base_v044_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    result = _z(p, 252) * closeadj * (3.7800)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_504d_base_v045_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    result = _z(p, 252) * closeadj * (5.0400)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_5d_base_v046_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    result = _std(p, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_8d_base_v047_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    result = _std(p, 8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_10d_base_v048_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    result = _std(p, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_15d_base_v049_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    result = _std(p, 15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_21d_base_v050_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    result = _std(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_30d_base_v051_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    result = _std(p, 30) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_42d_base_v052_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    result = _std(p, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_63d_base_v053_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    result = _std(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_90d_base_v054_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    result = _std(p, 90) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_126d_base_v055_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    result = _std(p, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_150d_base_v056_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    result = _std(p, 150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_189d_base_v057_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    result = _std(p, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_252d_base_v058_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    result = _std(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_378d_base_v059_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    result = _std(p, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_504d_base_v060_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    result = _std(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_5d_base_v061_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 5)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_8d_base_v062_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 8)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_10d_base_v063_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 10)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_15d_base_v064_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 15)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_21d_base_v065_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 21)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_30d_base_v066_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 30)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_42d_base_v067_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 42)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_63d_base_v068_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 63)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_90d_base_v069_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 90)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_126d_base_v070_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 126)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_150d_base_v071_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 150)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_189d_base_v072_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 189)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_252d_base_v073_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 252)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_378d_base_v074_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 378)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_504d_base_v075_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 504)
    result = cp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20rcy_f20_reinsurance_cycle_pulse_5d_base_v001_signal,
    f20rcy_f20_reinsurance_cycle_pulse_8d_base_v002_signal,
    f20rcy_f20_reinsurance_cycle_pulse_10d_base_v003_signal,
    f20rcy_f20_reinsurance_cycle_pulse_15d_base_v004_signal,
    f20rcy_f20_reinsurance_cycle_pulse_21d_base_v005_signal,
    f20rcy_f20_reinsurance_cycle_pulse_30d_base_v006_signal,
    f20rcy_f20_reinsurance_cycle_pulse_42d_base_v007_signal,
    f20rcy_f20_reinsurance_cycle_pulse_63d_base_v008_signal,
    f20rcy_f20_reinsurance_cycle_pulse_90d_base_v009_signal,
    f20rcy_f20_reinsurance_cycle_pulse_126d_base_v010_signal,
    f20rcy_f20_reinsurance_cycle_pulse_150d_base_v011_signal,
    f20rcy_f20_reinsurance_cycle_pulse_189d_base_v012_signal,
    f20rcy_f20_reinsurance_cycle_pulse_252d_base_v013_signal,
    f20rcy_f20_reinsurance_cycle_pulse_378d_base_v014_signal,
    f20rcy_f20_reinsurance_cycle_pulse_504d_base_v015_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_5d_base_v016_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_8d_base_v017_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_10d_base_v018_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_15d_base_v019_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_21d_base_v020_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_30d_base_v021_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_42d_base_v022_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_63d_base_v023_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_90d_base_v024_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_126d_base_v025_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_150d_base_v026_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_189d_base_v027_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_252d_base_v028_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_378d_base_v029_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_504d_base_v030_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_5d_base_v031_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_8d_base_v032_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_10d_base_v033_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_15d_base_v034_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_21d_base_v035_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_30d_base_v036_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_42d_base_v037_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_63d_base_v038_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_90d_base_v039_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_126d_base_v040_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_150d_base_v041_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_189d_base_v042_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_252d_base_v043_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_378d_base_v044_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_504d_base_v045_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_5d_base_v046_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_8d_base_v047_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_10d_base_v048_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_15d_base_v049_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_21d_base_v050_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_30d_base_v051_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_42d_base_v052_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_63d_base_v053_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_90d_base_v054_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_126d_base_v055_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_150d_base_v056_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_189d_base_v057_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_252d_base_v058_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_378d_base_v059_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_504d_base_v060_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_5d_base_v061_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_8d_base_v062_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_10d_base_v063_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_15d_base_v064_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_21d_base_v065_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_30d_base_v066_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_42d_base_v067_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_63d_base_v068_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_90d_base_v069_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_126d_base_v070_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_150d_base_v071_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_189d_base_v072_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_252d_base_v073_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_378d_base_v074_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_REINSURANCE_CYCLE_REGISTRY_001_075 = REGISTRY


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
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "liabilities": liabilities, "equity": equity,
        "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f20_reinsurance_pulse", "_f20_cycle_position", "_f20_pricing_cycle",)
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
    print(f"OK f20_reinsurance_cycle_001_075_claude: {n_features} features pass")
