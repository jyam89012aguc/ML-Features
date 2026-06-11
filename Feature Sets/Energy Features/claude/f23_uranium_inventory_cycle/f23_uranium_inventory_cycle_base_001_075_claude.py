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
def _f23_inv_to_revenue(inventory, revenue):
    return inventory / revenue.replace(0, np.nan).abs()


def _f23_inv_cycle(inventory, w):
    m = inventory.rolling(w, min_periods=max(1, w // 2)).mean()
    return (inventory - m) / m.replace(0, np.nan).abs()


def _f23_inv_dynamics(inventory, cor, w):
    inv_g = inventory.pct_change(periods=w)
    cor_g = cor.pct_change(periods=w)
    return inv_g - cor_g


def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v001_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v002_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v003_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v004_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v005_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v006_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v007_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v008_signal(inventory, revenue, closeadj):
    result = _f23_inv_to_revenue(inventory, revenue) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v009_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v010_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * (closeadj * closeadj / 100.0))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v011_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * _mean(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v012_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v013_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v014_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0))))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v015_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * (closeadj + _mean(closeadj, 42)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v016_signal(inventory, revenue, closeadj):
    result = (np.log1p(_f23_inv_to_revenue(inventory, revenue).abs()) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v017_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v018_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v019_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v020_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v021_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v022_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v023_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v024_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 5) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v025_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v026_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v027_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v028_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v029_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v030_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v031_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v032_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 10) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v033_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v034_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v035_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v036_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v037_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v038_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v039_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v040_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 21) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v041_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v042_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v043_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v044_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v045_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v046_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v047_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v048_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 42) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v049_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v050_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v051_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v052_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v053_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v054_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v055_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v056_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 63) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v057_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v058_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v059_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v060_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v061_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v062_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v063_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v064_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 126) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v065_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v066_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v067_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v068_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v069_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj * (1.0 + _z(closeadj, 252).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v070_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj * (1.0 + _z(closeadj, 126).fillna(0.0)))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v071_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj + _mean(closeadj, 42))
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v072_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 189) * (closeadj * 0.5 + _mean(closeadj, 21) * 0.5)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v073_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v074_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * (closeadj * closeadj / 100.0)
    return result.replace([np.inf, -np.inf], np.nan)



def f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v075_signal(inventory, revenue, closeadj):
    result = _z(_f23_inv_to_revenue(inventory, revenue), 252) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v001_signal,
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v002_signal,
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v003_signal,
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v004_signal,
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v005_signal,
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v006_signal,
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v007_signal,
    f23uic_f23_uranium_inventory_cycle_invrev_5d_base_v008_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v009_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v010_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v011_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v012_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v013_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v014_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v015_signal,
    f23uic_f23_uranium_inventory_cycle_invrevlog_5d_base_v016_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v017_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v018_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v019_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v020_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v021_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v022_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v023_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_5d_base_v024_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v025_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v026_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v027_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v028_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v029_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v030_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v031_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_10d_base_v032_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v033_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v034_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v035_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v036_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v037_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v038_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v039_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_21d_base_v040_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v041_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v042_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v043_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v044_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v045_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v046_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v047_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_42d_base_v048_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v049_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v050_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v051_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v052_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v053_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v054_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v055_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_63d_base_v056_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v057_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v058_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v059_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v060_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v061_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v062_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v063_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_126d_base_v064_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v065_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v066_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v067_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v068_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v069_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v070_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v071_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_189d_base_v072_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v073_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v074_signal,
    f23uic_f23_uranium_inventory_cycle_invrevz_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_URANIUM_INVENTORY_CYCLE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    inventory = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "capex": capex,
        "depamor": depamor,
        "cor": cor,
        "assets": assets,
        "inventory": inventory,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f23_inv_to_revenue', '_f23_inv_cycle', '_f23_inv_dynamics')
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
    print(f"OK f23_uranium_inventory_cycle_base_001_075_claude: {n_features} features pass")
