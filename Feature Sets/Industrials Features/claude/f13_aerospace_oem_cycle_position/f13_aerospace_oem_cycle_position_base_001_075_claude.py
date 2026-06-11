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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (f13 aerospace_oem_cycle_position) =====
def _f13_revenue_inflection(revenue, w):
    sm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    short = revenue.rolling(max(1, w // 3), min_periods=max(1, w // 6)).mean()
    return (short - sm) / sm.replace(0, np.nan).abs()


def _f13_cycle_trough_indicator(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - mn) / mn.replace(0, np.nan).abs()


def _f13_recovery_strength(revenue, ebitda, w):
    rg = revenue.pct_change(periods=max(1, w // 2))
    eg = ebitda.pct_change(periods=max(1, w // 2))
    return (rg + eg) * 0.5


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_scaled_v001_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_scaled_v002_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_scaled_v003_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_scaled_v004_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_scaled_v005_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_scaled_v006_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_scaled_v007_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_scaled_v008_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_scaled_v009_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_scaled_v010_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_scaled_v011_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_scaled_v012_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_189d_scaled_v013_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_189d_scaled_v014_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_189d_scaled_v015_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_scaled_v016_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_scaled_v017_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_scaled_v018_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_378d_scaled_v019_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_378d_scaled_v020_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_378d_scaled_v021_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_scaled_v022_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_scaled_v023_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_scaled_v024_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_ema_v025_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 21)
    result = _ema(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_ema_v026_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = _ema(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_ema_v027_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = _ema(base, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_ema_v028_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 42)
    result = _ema(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_ema_v029_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 42)
    result = _ema(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_ema_v030_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 42)
    result = _ema(base, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_ema_v031_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_ema_v032_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_ema_v033_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_ema_v034_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_ema_v035_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_ema_v036_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_189d_ema_v037_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 189)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_189d_ema_v038_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 189)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_189d_ema_v039_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 189)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_ema_v040_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_ema_v041_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_ema_v042_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_378d_ema_v043_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 378)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_378d_ema_v044_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 378)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_378d_ema_v045_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 378)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_ema_v046_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_ema_v047_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_ema_v048_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = _ema(base, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_21d_z_v049_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_21d_z_v050_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_21d_z_v051_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_42d_z_v052_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 42)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_42d_z_v053_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 42)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_42d_z_v054_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 42)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_63d_z_v055_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 63)
    result = _z(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_63d_z_v056_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 63)
    result = _z(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_63d_z_v057_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 63)
    result = _z(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_126d_z_v058_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 126)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_126d_z_v059_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 126)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_126d_z_v060_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 126)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_189d_z_v061_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 189)
    result = _z(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_189d_z_v062_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 189)
    result = _z(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_189d_z_v063_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 189)
    result = _z(base, 94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_252d_z_v064_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_252d_z_v065_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_252d_z_v066_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_378d_z_v067_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 378)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_378d_z_v068_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 378)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_378d_z_v069_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 378)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_504d_z_v070_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_504d_z_v071_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_504d_z_v072_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_revinfl_10d_scaled_v073_signal(closeadj, revenue):
    base = _f13_revenue_inflection(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_trough_10d_ema_v074_signal(closeadj, revenue):
    base = _f13_cycle_trough_indicator(revenue, 10)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def aoc_f13_aerospace_oem_cycle_position_recstr_10d_z_v075_signal(closeadj, ebitda, revenue):
    base = _f13_recovery_strength(revenue, ebitda, 10)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_scaled_v001_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_scaled_v002_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_scaled_v003_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_scaled_v004_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_scaled_v005_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_scaled_v006_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_scaled_v007_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_scaled_v008_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_scaled_v009_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_scaled_v010_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_scaled_v011_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_scaled_v012_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_189d_scaled_v013_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_189d_scaled_v014_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_189d_scaled_v015_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_scaled_v016_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_scaled_v017_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_scaled_v018_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_378d_scaled_v019_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_378d_scaled_v020_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_378d_scaled_v021_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_scaled_v022_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_scaled_v023_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_scaled_v024_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_ema_v025_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_ema_v026_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_ema_v027_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_ema_v028_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_ema_v029_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_ema_v030_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_ema_v031_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_ema_v032_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_ema_v033_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_ema_v034_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_ema_v035_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_ema_v036_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_189d_ema_v037_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_189d_ema_v038_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_189d_ema_v039_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_ema_v040_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_ema_v041_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_ema_v042_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_378d_ema_v043_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_378d_ema_v044_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_378d_ema_v045_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_ema_v046_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_ema_v047_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_ema_v048_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_21d_z_v049_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_21d_z_v050_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_21d_z_v051_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_42d_z_v052_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_42d_z_v053_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_42d_z_v054_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_63d_z_v055_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_63d_z_v056_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_63d_z_v057_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_126d_z_v058_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_126d_z_v059_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_126d_z_v060_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_189d_z_v061_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_189d_z_v062_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_189d_z_v063_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_252d_z_v064_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_252d_z_v065_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_252d_z_v066_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_378d_z_v067_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_378d_z_v068_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_378d_z_v069_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_504d_z_v070_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_504d_z_v071_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_504d_z_v072_signal,
    aoc_f13_aerospace_oem_cycle_position_revinfl_10d_scaled_v073_signal,
    aoc_f13_aerospace_oem_cycle_position_trough_10d_ema_v074_signal,
    aoc_f13_aerospace_oem_cycle_position_recstr_10d_z_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_AEROSPACE_OEM_CYCLE_POSITION_REGISTRY_001_075 = REGISTRY
F13_AEROSPACE_OEM_CYCLE_POSITION_REGISTRY_001_075 = REGISTRY

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
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f13_revenue_inflection", "_f13_cycle_trough_indicator", "_f13_recovery_strength",)
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
    print(f"OK f13_aerospace_oem_cycle_position_base_001_075_claude: {n_features} features pass")
