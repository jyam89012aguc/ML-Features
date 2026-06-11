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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

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

def f20rcy_f20_reinsurance_cycle_pulse_5d_slope_5d_slope_v001_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    base = p * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_8d_slope_10d_slope_v002_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    base = p * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_10d_slope_21d_slope_v003_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    base = p * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_15d_slope_42d_slope_v004_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    base = p * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_21d_slope_63d_slope_v005_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    base = p * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_30d_slope_126d_slope_v006_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    base = p * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_42d_slope_5d_slope_v007_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    base = p * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_63d_slope_10d_slope_v008_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    base = p * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_90d_slope_21d_slope_v009_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    base = p * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_126d_slope_42d_slope_v010_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    base = p * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_150d_slope_63d_slope_v011_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    base = p * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_189d_slope_126d_slope_v012_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    base = p * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_252d_slope_5d_slope_v013_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    base = p * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_378d_slope_10d_slope_v014_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    base = p * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulse_504d_slope_21d_slope_v015_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    base = p * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_5d_slope_42d_slope_v016_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    base = _ema(p, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_8d_slope_63d_slope_v017_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    base = _ema(p, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_10d_slope_126d_slope_v018_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    base = _ema(p, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_15d_slope_5d_slope_v019_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    base = _ema(p, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_21d_slope_10d_slope_v020_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    base = _ema(p, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_30d_slope_21d_slope_v021_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    base = _ema(p, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_42d_slope_42d_slope_v022_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    base = _ema(p, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_63d_slope_63d_slope_v023_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    base = _ema(p, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_90d_slope_126d_slope_v024_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    base = _ema(p, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_126d_slope_5d_slope_v025_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    base = _ema(p, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_150d_slope_10d_slope_v026_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    base = _ema(p, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_189d_slope_21d_slope_v027_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    base = _ema(p, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_252d_slope_42d_slope_v028_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    base = _ema(p, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_378d_slope_63d_slope_v029_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    base = _ema(p, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulseema_504d_slope_126d_slope_v030_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    base = _ema(p, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_5d_slope_5d_slope_v031_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    base = _z(p, 252) * closeadj * (0.0500)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_8d_slope_10d_slope_v032_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    base = _z(p, 252) * closeadj * (0.0800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_10d_slope_21d_slope_v033_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    base = _z(p, 252) * closeadj * (0.1000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_15d_slope_42d_slope_v034_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    base = _z(p, 252) * closeadj * (0.1500)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_21d_slope_63d_slope_v035_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    base = _z(p, 252) * closeadj * (0.2100)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_30d_slope_126d_slope_v036_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    base = _z(p, 252) * closeadj * (0.3000)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_42d_slope_5d_slope_v037_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    base = _z(p, 252) * closeadj * (0.4200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_63d_slope_10d_slope_v038_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    base = _z(p, 252) * closeadj * (0.6300)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_90d_slope_21d_slope_v039_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    base = _z(p, 252) * closeadj * (0.9000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_126d_slope_42d_slope_v040_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    base = _z(p, 252) * closeadj * (1.2600)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_150d_slope_63d_slope_v041_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    base = _z(p, 252) * closeadj * (1.5000)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_189d_slope_126d_slope_v042_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    base = _z(p, 252) * closeadj * (1.8900)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_252d_slope_5d_slope_v043_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    base = _z(p, 252) * closeadj * (2.5200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_378d_slope_10d_slope_v044_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    base = _z(p, 252) * closeadj * (3.7800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsez_504d_slope_21d_slope_v045_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    base = _z(p, 252) * closeadj * (5.0400)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_5d_slope_42d_slope_v046_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    base = _std(p, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_8d_slope_63d_slope_v047_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    base = _std(p, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_10d_slope_126d_slope_v048_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    base = _std(p, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_15d_slope_5d_slope_v049_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    base = _std(p, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_21d_slope_10d_slope_v050_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    base = _std(p, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_30d_slope_21d_slope_v051_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    base = _std(p, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_42d_slope_42d_slope_v052_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_63d_slope_63d_slope_v053_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    base = _std(p, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_90d_slope_126d_slope_v054_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    base = _std(p, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_126d_slope_5d_slope_v055_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    base = _std(p, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_150d_slope_10d_slope_v056_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    base = _std(p, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_189d_slope_21d_slope_v057_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    base = _std(p, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_252d_slope_42d_slope_v058_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    base = _std(p, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_378d_slope_63d_slope_v059_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    base = _std(p, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsestd_504d_slope_126d_slope_v060_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    base = _std(p, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_5d_slope_5d_slope_v061_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 5)
    base = cp * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_8d_slope_10d_slope_v062_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 8)
    base = cp * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_10d_slope_21d_slope_v063_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 10)
    base = cp * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_15d_slope_42d_slope_v064_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 15)
    base = cp * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_21d_slope_63d_slope_v065_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 21)
    base = cp * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_30d_slope_126d_slope_v066_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 30)
    base = cp * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_42d_slope_5d_slope_v067_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 42)
    base = cp * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_63d_slope_10d_slope_v068_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 63)
    base = cp * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_90d_slope_21d_slope_v069_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 90)
    base = cp * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_126d_slope_42d_slope_v070_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 126)
    base = cp * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_150d_slope_63d_slope_v071_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 150)
    base = cp * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_189d_slope_126d_slope_v072_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 189)
    base = cp * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_252d_slope_5d_slope_v073_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 252)
    base = cp * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_378d_slope_10d_slope_v074_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 378)
    base = cp * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycpos_504d_slope_21d_slope_v075_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 504)
    base = cp * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_5d_slope_42d_slope_v076_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 5)
    base = _ema(cp, 5) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_8d_slope_63d_slope_v077_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 8)
    base = _ema(cp, 8) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_10d_slope_126d_slope_v078_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 10)
    base = _ema(cp, 10) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_15d_slope_5d_slope_v079_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 15)
    base = _ema(cp, 15) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_21d_slope_10d_slope_v080_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 21)
    base = _ema(cp, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_30d_slope_21d_slope_v081_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 30)
    base = _ema(cp, 30) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_42d_slope_42d_slope_v082_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 42)
    base = _ema(cp, 42) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_63d_slope_63d_slope_v083_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 63)
    base = _ema(cp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_90d_slope_126d_slope_v084_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 90)
    base = _ema(cp, 90) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_126d_slope_5d_slope_v085_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 126)
    base = _ema(cp, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_150d_slope_10d_slope_v086_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 150)
    base = _ema(cp, 150) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_189d_slope_21d_slope_v087_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 189)
    base = _ema(cp, 189) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_252d_slope_42d_slope_v088_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 252)
    base = _ema(cp, 252) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_378d_slope_63d_slope_v089_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 378)
    base = _ema(cp, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposema_504d_slope_126d_slope_v090_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 504)
    base = _ema(cp, 504) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_5d_slope_5d_slope_v091_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 5)
    base = _z(cp, 252) * closeadj * (0.0500)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_8d_slope_10d_slope_v092_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 8)
    base = _z(cp, 252) * closeadj * (0.0800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_10d_slope_21d_slope_v093_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 10)
    base = _z(cp, 252) * closeadj * (0.1000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_15d_slope_42d_slope_v094_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 15)
    base = _z(cp, 252) * closeadj * (0.1500)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_21d_slope_63d_slope_v095_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 21)
    base = _z(cp, 252) * closeadj * (0.2100)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_30d_slope_126d_slope_v096_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 30)
    base = _z(cp, 252) * closeadj * (0.3000)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_42d_slope_5d_slope_v097_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 42)
    base = _z(cp, 252) * closeadj * (0.4200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_63d_slope_10d_slope_v098_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 63)
    base = _z(cp, 252) * closeadj * (0.6300)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_90d_slope_21d_slope_v099_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 90)
    base = _z(cp, 252) * closeadj * (0.9000)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_126d_slope_42d_slope_v100_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 126)
    base = _z(cp, 252) * closeadj * (1.2600)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_150d_slope_63d_slope_v101_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 150)
    base = _z(cp, 252) * closeadj * (1.5000)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_189d_slope_126d_slope_v102_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 189)
    base = _z(cp, 252) * closeadj * (1.8900)
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_252d_slope_5d_slope_v103_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 252)
    base = _z(cp, 252) * closeadj * (2.5200)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_378d_slope_10d_slope_v104_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 378)
    base = _z(cp, 252) * closeadj * (3.7800)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_cycposz_504d_slope_21d_slope_v105_signal(revenue, netmargin, closeadj):
    cp = _f20_cycle_position(revenue, netmargin, 504)
    base = _z(cp, 252) * closeadj * (5.0400)
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_5d_slope_42d_slope_v106_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 5)
    base = pc * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_8d_slope_63d_slope_v107_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 8)
    base = pc * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_10d_slope_126d_slope_v108_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 10)
    base = pc * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_15d_slope_5d_slope_v109_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 15)
    base = pc * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_21d_slope_10d_slope_v110_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 21)
    base = pc * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_30d_slope_21d_slope_v111_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 30)
    base = pc * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_42d_slope_42d_slope_v112_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 42)
    base = pc * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_63d_slope_63d_slope_v113_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 63)
    base = pc * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_90d_slope_126d_slope_v114_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 90)
    base = pc * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_126d_slope_5d_slope_v115_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 126)
    base = pc * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_150d_slope_10d_slope_v116_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 150)
    base = pc * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_189d_slope_21d_slope_v117_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 189)
    base = pc * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_252d_slope_42d_slope_v118_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 252)
    base = pc * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_378d_slope_63d_slope_v119_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 378)
    base = pc * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecyc_504d_slope_126d_slope_v120_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 504)
    base = pc * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_5d_slope_5d_slope_v121_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 5)
    base = _ema(pc, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_8d_slope_10d_slope_v122_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 8)
    base = _ema(pc, 8) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_10d_slope_21d_slope_v123_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 10)
    base = _ema(pc, 10) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_15d_slope_42d_slope_v124_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 15)
    base = _ema(pc, 15) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_21d_slope_63d_slope_v125_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 21)
    base = _ema(pc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_30d_slope_126d_slope_v126_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 30)
    base = _ema(pc, 30) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_42d_slope_5d_slope_v127_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 42)
    base = _ema(pc, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_63d_slope_10d_slope_v128_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 63)
    base = _ema(pc, 63) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_90d_slope_21d_slope_v129_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 90)
    base = _ema(pc, 90) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_126d_slope_42d_slope_v130_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 126)
    base = _ema(pc, 126) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_150d_slope_63d_slope_v131_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 150)
    base = _ema(pc, 150) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_189d_slope_126d_slope_v132_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 189)
    base = _ema(pc, 189) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_252d_slope_5d_slope_v133_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 252)
    base = _ema(pc, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_378d_slope_10d_slope_v134_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 378)
    base = _ema(pc, 378) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pricecycema_504d_slope_21d_slope_v135_signal(revenue, netmargin, closeadj):
    pc = _f20_pricing_cycle(revenue, netmargin, 504)
    base = _ema(pc, 504) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_5d_slope_42d_slope_v136_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 5)
    base = (p - p.shift(5)) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_8d_slope_63d_slope_v137_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 8)
    base = (p - p.shift(8)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_10d_slope_126d_slope_v138_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 10)
    base = (p - p.shift(10)) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_15d_slope_5d_slope_v139_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 15)
    base = (p - p.shift(15)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_21d_slope_10d_slope_v140_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 21)
    base = (p - p.shift(21)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_30d_slope_21d_slope_v141_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 30)
    base = (p - p.shift(30)) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_42d_slope_42d_slope_v142_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 42)
    base = (p - p.shift(42)) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_63d_slope_63d_slope_v143_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 63)
    base = (p - p.shift(63)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_90d_slope_126d_slope_v144_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 90)
    base = (p - p.shift(90)) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_126d_slope_5d_slope_v145_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 126)
    base = (p - p.shift(126)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_150d_slope_10d_slope_v146_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 150)
    base = (p - p.shift(150)) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_189d_slope_21d_slope_v147_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 189)
    base = (p - p.shift(189)) * closeadj
    result = base.diff(periods=21) / base.rolling(21, min_periods=max(1,21//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_252d_slope_42d_slope_v148_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 252)
    base = (p - p.shift(252)) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_378d_slope_63d_slope_v149_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 378)
    base = (p - p.shift(378)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20rcy_f20_reinsurance_cycle_pulsediff_504d_slope_126d_slope_v150_signal(revenue, closeadj):
    p = _f20_reinsurance_pulse(revenue, 504)
    base = (p - p.shift(504)) * closeadj
    result = base.diff(periods=126) / base.rolling(126, min_periods=max(1,126//2)).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20rcy_f20_reinsurance_cycle_pulse_5d_slope_5d_slope_v001_signal,
    f20rcy_f20_reinsurance_cycle_pulse_8d_slope_10d_slope_v002_signal,
    f20rcy_f20_reinsurance_cycle_pulse_10d_slope_21d_slope_v003_signal,
    f20rcy_f20_reinsurance_cycle_pulse_15d_slope_42d_slope_v004_signal,
    f20rcy_f20_reinsurance_cycle_pulse_21d_slope_63d_slope_v005_signal,
    f20rcy_f20_reinsurance_cycle_pulse_30d_slope_126d_slope_v006_signal,
    f20rcy_f20_reinsurance_cycle_pulse_42d_slope_5d_slope_v007_signal,
    f20rcy_f20_reinsurance_cycle_pulse_63d_slope_10d_slope_v008_signal,
    f20rcy_f20_reinsurance_cycle_pulse_90d_slope_21d_slope_v009_signal,
    f20rcy_f20_reinsurance_cycle_pulse_126d_slope_42d_slope_v010_signal,
    f20rcy_f20_reinsurance_cycle_pulse_150d_slope_63d_slope_v011_signal,
    f20rcy_f20_reinsurance_cycle_pulse_189d_slope_126d_slope_v012_signal,
    f20rcy_f20_reinsurance_cycle_pulse_252d_slope_5d_slope_v013_signal,
    f20rcy_f20_reinsurance_cycle_pulse_378d_slope_10d_slope_v014_signal,
    f20rcy_f20_reinsurance_cycle_pulse_504d_slope_21d_slope_v015_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_5d_slope_42d_slope_v016_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_8d_slope_63d_slope_v017_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_10d_slope_126d_slope_v018_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_15d_slope_5d_slope_v019_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_21d_slope_10d_slope_v020_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_30d_slope_21d_slope_v021_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_42d_slope_42d_slope_v022_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_63d_slope_63d_slope_v023_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_90d_slope_126d_slope_v024_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_126d_slope_5d_slope_v025_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_150d_slope_10d_slope_v026_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_189d_slope_21d_slope_v027_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_252d_slope_42d_slope_v028_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_378d_slope_63d_slope_v029_signal,
    f20rcy_f20_reinsurance_cycle_pulseema_504d_slope_126d_slope_v030_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_5d_slope_5d_slope_v031_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_8d_slope_10d_slope_v032_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_10d_slope_21d_slope_v033_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_15d_slope_42d_slope_v034_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_21d_slope_63d_slope_v035_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_30d_slope_126d_slope_v036_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_42d_slope_5d_slope_v037_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_63d_slope_10d_slope_v038_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_90d_slope_21d_slope_v039_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_126d_slope_42d_slope_v040_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_150d_slope_63d_slope_v041_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_189d_slope_126d_slope_v042_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_252d_slope_5d_slope_v043_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_378d_slope_10d_slope_v044_signal,
    f20rcy_f20_reinsurance_cycle_pulsez_504d_slope_21d_slope_v045_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_5d_slope_42d_slope_v046_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_8d_slope_63d_slope_v047_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_10d_slope_126d_slope_v048_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_15d_slope_5d_slope_v049_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_21d_slope_10d_slope_v050_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_30d_slope_21d_slope_v051_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_42d_slope_42d_slope_v052_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_63d_slope_63d_slope_v053_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_90d_slope_126d_slope_v054_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_126d_slope_5d_slope_v055_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_150d_slope_10d_slope_v056_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_189d_slope_21d_slope_v057_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_252d_slope_42d_slope_v058_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_378d_slope_63d_slope_v059_signal,
    f20rcy_f20_reinsurance_cycle_pulsestd_504d_slope_126d_slope_v060_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_5d_slope_5d_slope_v061_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_8d_slope_10d_slope_v062_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_10d_slope_21d_slope_v063_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_15d_slope_42d_slope_v064_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_21d_slope_63d_slope_v065_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_30d_slope_126d_slope_v066_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_42d_slope_5d_slope_v067_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_63d_slope_10d_slope_v068_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_90d_slope_21d_slope_v069_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_126d_slope_42d_slope_v070_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_150d_slope_63d_slope_v071_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_189d_slope_126d_slope_v072_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_252d_slope_5d_slope_v073_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_378d_slope_10d_slope_v074_signal,
    f20rcy_f20_reinsurance_cycle_cycpos_504d_slope_21d_slope_v075_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_5d_slope_42d_slope_v076_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_8d_slope_63d_slope_v077_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_10d_slope_126d_slope_v078_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_15d_slope_5d_slope_v079_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_21d_slope_10d_slope_v080_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_30d_slope_21d_slope_v081_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_42d_slope_42d_slope_v082_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_63d_slope_63d_slope_v083_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_90d_slope_126d_slope_v084_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_126d_slope_5d_slope_v085_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_150d_slope_10d_slope_v086_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_189d_slope_21d_slope_v087_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_252d_slope_42d_slope_v088_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_378d_slope_63d_slope_v089_signal,
    f20rcy_f20_reinsurance_cycle_cycposema_504d_slope_126d_slope_v090_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_5d_slope_5d_slope_v091_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_8d_slope_10d_slope_v092_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_10d_slope_21d_slope_v093_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_15d_slope_42d_slope_v094_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_21d_slope_63d_slope_v095_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_30d_slope_126d_slope_v096_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_42d_slope_5d_slope_v097_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_63d_slope_10d_slope_v098_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_90d_slope_21d_slope_v099_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_126d_slope_42d_slope_v100_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_150d_slope_63d_slope_v101_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_189d_slope_126d_slope_v102_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_252d_slope_5d_slope_v103_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_378d_slope_10d_slope_v104_signal,
    f20rcy_f20_reinsurance_cycle_cycposz_504d_slope_21d_slope_v105_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_5d_slope_42d_slope_v106_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_8d_slope_63d_slope_v107_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_10d_slope_126d_slope_v108_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_15d_slope_5d_slope_v109_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_21d_slope_10d_slope_v110_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_30d_slope_21d_slope_v111_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_42d_slope_42d_slope_v112_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_63d_slope_63d_slope_v113_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_90d_slope_126d_slope_v114_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_126d_slope_5d_slope_v115_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_150d_slope_10d_slope_v116_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_189d_slope_21d_slope_v117_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_252d_slope_42d_slope_v118_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_378d_slope_63d_slope_v119_signal,
    f20rcy_f20_reinsurance_cycle_pricecyc_504d_slope_126d_slope_v120_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_5d_slope_5d_slope_v121_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_8d_slope_10d_slope_v122_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_10d_slope_21d_slope_v123_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_15d_slope_42d_slope_v124_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_21d_slope_63d_slope_v125_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_30d_slope_126d_slope_v126_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_42d_slope_5d_slope_v127_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_63d_slope_10d_slope_v128_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_90d_slope_21d_slope_v129_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_126d_slope_42d_slope_v130_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_150d_slope_63d_slope_v131_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_189d_slope_126d_slope_v132_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_252d_slope_5d_slope_v133_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_378d_slope_10d_slope_v134_signal,
    f20rcy_f20_reinsurance_cycle_pricecycema_504d_slope_21d_slope_v135_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_5d_slope_42d_slope_v136_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_8d_slope_63d_slope_v137_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_10d_slope_126d_slope_v138_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_15d_slope_5d_slope_v139_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_21d_slope_10d_slope_v140_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_30d_slope_21d_slope_v141_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_42d_slope_42d_slope_v142_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_63d_slope_63d_slope_v143_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_90d_slope_126d_slope_v144_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_126d_slope_5d_slope_v145_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_150d_slope_10d_slope_v146_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_189d_slope_21d_slope_v147_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_252d_slope_42d_slope_v148_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_378d_slope_63d_slope_v149_signal,
    f20rcy_f20_reinsurance_cycle_pulsediff_504d_slope_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_REINSURANCE_CYCLE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f20_reinsurance_cycle_slope_001_150_claude: {n_features} features pass")
