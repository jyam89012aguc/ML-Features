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
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f02_deposit_growth(deposits, w):
    return (deposits - deposits.shift(w)) / deposits.shift(w).abs().replace(0, np.nan)


def _f02_deposit_intensity(deposits, assets):
    return deposits / assets.replace(0, np.nan).abs()


def _f02_franchise_stability(deposits, w):
    m = deposits.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = deposits.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def f02dfg_f02_deposit_franchise_growth_dg_lvl_5d_base_v001_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_mean_5d_base_v002_signal(deposits, closeadj):
    result = _mean(_f02_deposit_growth(deposits, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_std_5d_base_v003_signal(deposits, closeadj):
    result = _std(_f02_deposit_growth(deposits, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_ema_5d_base_v004_signal(deposits, closeadj):
    result = _ema(_f02_deposit_growth(deposits, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_z_5d_base_v005_signal(deposits, closeadj):
    result = _z(_f02_deposit_growth(deposits, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_lvl_5d_base_v006_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_chg_5d_base_v007_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = (base - base.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_z_5d_base_v008_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _z(base, 31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_lvl_5d_base_v009_signal(deposits, closeadj):
    result = _f02_franchise_stability(deposits, 5) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_mean_5d_base_v010_signal(deposits, closeadj):
    result = _mean(_f02_franchise_stability(deposits, 5), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_z_5d_base_v011_signal(deposits, closeadj):
    result = _z(_f02_franchise_stability(deposits, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_5d_base_v012_signal(deposits, assets, closeadj):
    result = _f02_deposit_growth(deposits, 5) * _f02_deposit_intensity(deposits, assets) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxfs_5d_base_v013_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 5) + _f02_franchise_stability(deposits, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_log_5d_base_v014_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 5)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_sq_5d_base_v015_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 5)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_lvl_10d_base_v016_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_mean_10d_base_v017_signal(deposits, closeadj):
    result = _mean(_f02_deposit_growth(deposits, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_std_10d_base_v018_signal(deposits, closeadj):
    result = _std(_f02_deposit_growth(deposits, 10), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_ema_10d_base_v019_signal(deposits, closeadj):
    result = _ema(_f02_deposit_growth(deposits, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_z_10d_base_v020_signal(deposits, closeadj):
    result = _z(_f02_deposit_growth(deposits, 10), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_lvl_10d_base_v021_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_chg_10d_base_v022_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = (base - base.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_z_10d_base_v023_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _z(base, 41) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_lvl_10d_base_v024_signal(deposits, closeadj):
    result = _f02_franchise_stability(deposits, 10) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_mean_10d_base_v025_signal(deposits, closeadj):
    result = _mean(_f02_franchise_stability(deposits, 10), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_z_10d_base_v026_signal(deposits, closeadj):
    result = _z(_f02_franchise_stability(deposits, 10), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_10d_base_v027_signal(deposits, assets, closeadj):
    result = _f02_deposit_growth(deposits, 10) * _f02_deposit_intensity(deposits, assets) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxfs_10d_base_v028_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 10) + _f02_franchise_stability(deposits, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_log_10d_base_v029_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 10)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_sq_10d_base_v030_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 10)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_lvl_21d_base_v031_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_mean_21d_base_v032_signal(deposits, closeadj):
    result = _mean(_f02_deposit_growth(deposits, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_std_21d_base_v033_signal(deposits, closeadj):
    result = _std(_f02_deposit_growth(deposits, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_ema_21d_base_v034_signal(deposits, closeadj):
    result = _ema(_f02_deposit_growth(deposits, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_z_21d_base_v035_signal(deposits, closeadj):
    result = _z(_f02_deposit_growth(deposits, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_lvl_21d_base_v036_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_chg_21d_base_v037_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_z_21d_base_v038_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_lvl_21d_base_v039_signal(deposits, closeadj):
    result = _f02_franchise_stability(deposits, 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_mean_21d_base_v040_signal(deposits, closeadj):
    result = _mean(_f02_franchise_stability(deposits, 21), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_z_21d_base_v041_signal(deposits, closeadj):
    result = _z(_f02_franchise_stability(deposits, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_21d_base_v042_signal(deposits, assets, closeadj):
    result = _f02_deposit_growth(deposits, 21) * _f02_deposit_intensity(deposits, assets) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxfs_21d_base_v043_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 21) + _f02_franchise_stability(deposits, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_log_21d_base_v044_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 21)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_sq_21d_base_v045_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_lvl_42d_base_v046_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_mean_42d_base_v047_signal(deposits, closeadj):
    result = _mean(_f02_deposit_growth(deposits, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_std_42d_base_v048_signal(deposits, closeadj):
    result = _std(_f02_deposit_growth(deposits, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_ema_42d_base_v049_signal(deposits, closeadj):
    result = _ema(_f02_deposit_growth(deposits, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_z_42d_base_v050_signal(deposits, closeadj):
    result = _z(_f02_deposit_growth(deposits, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_lvl_42d_base_v051_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_chg_42d_base_v052_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = (base - base.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_z_42d_base_v053_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _z(base, 105) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_lvl_42d_base_v054_signal(deposits, closeadj):
    result = _f02_franchise_stability(deposits, 42) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_mean_42d_base_v055_signal(deposits, closeadj):
    result = _mean(_f02_franchise_stability(deposits, 42), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_z_42d_base_v056_signal(deposits, closeadj):
    result = _z(_f02_franchise_stability(deposits, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_42d_base_v057_signal(deposits, assets, closeadj):
    result = _f02_deposit_growth(deposits, 42) * _f02_deposit_intensity(deposits, assets) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxfs_42d_base_v058_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 42) + _f02_franchise_stability(deposits, 42) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_log_42d_base_v059_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 42)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_sq_42d_base_v060_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 42)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_lvl_63d_base_v061_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_mean_63d_base_v062_signal(deposits, closeadj):
    result = _mean(_f02_deposit_growth(deposits, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_std_63d_base_v063_signal(deposits, closeadj):
    result = _std(_f02_deposit_growth(deposits, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_ema_63d_base_v064_signal(deposits, closeadj):
    result = _ema(_f02_deposit_growth(deposits, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_z_63d_base_v065_signal(deposits, closeadj):
    result = _z(_f02_deposit_growth(deposits, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_lvl_63d_base_v066_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_chg_63d_base_v067_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_z_63d_base_v068_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets)
    result = _z(base, 147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_lvl_63d_base_v069_signal(deposits, closeadj):
    result = _f02_franchise_stability(deposits, 63) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_mean_63d_base_v070_signal(deposits, closeadj):
    result = _mean(_f02_franchise_stability(deposits, 63), 21) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_z_63d_base_v071_signal(deposits, closeadj):
    result = _z(_f02_franchise_stability(deposits, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_63d_base_v072_signal(deposits, assets, closeadj):
    result = _f02_deposit_growth(deposits, 63) * _f02_deposit_intensity(deposits, assets) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxfs_63d_base_v073_signal(deposits, closeadj):
    result = _f02_deposit_growth(deposits, 63) + _f02_franchise_stability(deposits, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_log_63d_base_v074_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 63)
    result = np.sign(g) * np.log1p(g.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_sq_63d_base_v075_signal(deposits, closeadj):
    g = _f02_deposit_growth(deposits, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02dfg_f02_deposit_franchise_growth_dg_lvl_5d_base_v001_signal,
    f02dfg_f02_deposit_franchise_growth_dg_mean_5d_base_v002_signal,
    f02dfg_f02_deposit_franchise_growth_dg_std_5d_base_v003_signal,
    f02dfg_f02_deposit_franchise_growth_dg_ema_5d_base_v004_signal,
    f02dfg_f02_deposit_franchise_growth_dg_z_5d_base_v005_signal,
    f02dfg_f02_deposit_franchise_growth_di_lvl_5d_base_v006_signal,
    f02dfg_f02_deposit_franchise_growth_di_chg_5d_base_v007_signal,
    f02dfg_f02_deposit_franchise_growth_di_z_5d_base_v008_signal,
    f02dfg_f02_deposit_franchise_growth_fs_lvl_5d_base_v009_signal,
    f02dfg_f02_deposit_franchise_growth_fs_mean_5d_base_v010_signal,
    f02dfg_f02_deposit_franchise_growth_fs_z_5d_base_v011_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_5d_base_v012_signal,
    f02dfg_f02_deposit_franchise_growth_dgxfs_5d_base_v013_signal,
    f02dfg_f02_deposit_franchise_growth_dg_log_5d_base_v014_signal,
    f02dfg_f02_deposit_franchise_growth_dg_sq_5d_base_v015_signal,
    f02dfg_f02_deposit_franchise_growth_dg_lvl_10d_base_v016_signal,
    f02dfg_f02_deposit_franchise_growth_dg_mean_10d_base_v017_signal,
    f02dfg_f02_deposit_franchise_growth_dg_std_10d_base_v018_signal,
    f02dfg_f02_deposit_franchise_growth_dg_ema_10d_base_v019_signal,
    f02dfg_f02_deposit_franchise_growth_dg_z_10d_base_v020_signal,
    f02dfg_f02_deposit_franchise_growth_di_lvl_10d_base_v021_signal,
    f02dfg_f02_deposit_franchise_growth_di_chg_10d_base_v022_signal,
    f02dfg_f02_deposit_franchise_growth_di_z_10d_base_v023_signal,
    f02dfg_f02_deposit_franchise_growth_fs_lvl_10d_base_v024_signal,
    f02dfg_f02_deposit_franchise_growth_fs_mean_10d_base_v025_signal,
    f02dfg_f02_deposit_franchise_growth_fs_z_10d_base_v026_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_10d_base_v027_signal,
    f02dfg_f02_deposit_franchise_growth_dgxfs_10d_base_v028_signal,
    f02dfg_f02_deposit_franchise_growth_dg_log_10d_base_v029_signal,
    f02dfg_f02_deposit_franchise_growth_dg_sq_10d_base_v030_signal,
    f02dfg_f02_deposit_franchise_growth_dg_lvl_21d_base_v031_signal,
    f02dfg_f02_deposit_franchise_growth_dg_mean_21d_base_v032_signal,
    f02dfg_f02_deposit_franchise_growth_dg_std_21d_base_v033_signal,
    f02dfg_f02_deposit_franchise_growth_dg_ema_21d_base_v034_signal,
    f02dfg_f02_deposit_franchise_growth_dg_z_21d_base_v035_signal,
    f02dfg_f02_deposit_franchise_growth_di_lvl_21d_base_v036_signal,
    f02dfg_f02_deposit_franchise_growth_di_chg_21d_base_v037_signal,
    f02dfg_f02_deposit_franchise_growth_di_z_21d_base_v038_signal,
    f02dfg_f02_deposit_franchise_growth_fs_lvl_21d_base_v039_signal,
    f02dfg_f02_deposit_franchise_growth_fs_mean_21d_base_v040_signal,
    f02dfg_f02_deposit_franchise_growth_fs_z_21d_base_v041_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_21d_base_v042_signal,
    f02dfg_f02_deposit_franchise_growth_dgxfs_21d_base_v043_signal,
    f02dfg_f02_deposit_franchise_growth_dg_log_21d_base_v044_signal,
    f02dfg_f02_deposit_franchise_growth_dg_sq_21d_base_v045_signal,
    f02dfg_f02_deposit_franchise_growth_dg_lvl_42d_base_v046_signal,
    f02dfg_f02_deposit_franchise_growth_dg_mean_42d_base_v047_signal,
    f02dfg_f02_deposit_franchise_growth_dg_std_42d_base_v048_signal,
    f02dfg_f02_deposit_franchise_growth_dg_ema_42d_base_v049_signal,
    f02dfg_f02_deposit_franchise_growth_dg_z_42d_base_v050_signal,
    f02dfg_f02_deposit_franchise_growth_di_lvl_42d_base_v051_signal,
    f02dfg_f02_deposit_franchise_growth_di_chg_42d_base_v052_signal,
    f02dfg_f02_deposit_franchise_growth_di_z_42d_base_v053_signal,
    f02dfg_f02_deposit_franchise_growth_fs_lvl_42d_base_v054_signal,
    f02dfg_f02_deposit_franchise_growth_fs_mean_42d_base_v055_signal,
    f02dfg_f02_deposit_franchise_growth_fs_z_42d_base_v056_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_42d_base_v057_signal,
    f02dfg_f02_deposit_franchise_growth_dgxfs_42d_base_v058_signal,
    f02dfg_f02_deposit_franchise_growth_dg_log_42d_base_v059_signal,
    f02dfg_f02_deposit_franchise_growth_dg_sq_42d_base_v060_signal,
    f02dfg_f02_deposit_franchise_growth_dg_lvl_63d_base_v061_signal,
    f02dfg_f02_deposit_franchise_growth_dg_mean_63d_base_v062_signal,
    f02dfg_f02_deposit_franchise_growth_dg_std_63d_base_v063_signal,
    f02dfg_f02_deposit_franchise_growth_dg_ema_63d_base_v064_signal,
    f02dfg_f02_deposit_franchise_growth_dg_z_63d_base_v065_signal,
    f02dfg_f02_deposit_franchise_growth_di_lvl_63d_base_v066_signal,
    f02dfg_f02_deposit_franchise_growth_di_chg_63d_base_v067_signal,
    f02dfg_f02_deposit_franchise_growth_di_z_63d_base_v068_signal,
    f02dfg_f02_deposit_franchise_growth_fs_lvl_63d_base_v069_signal,
    f02dfg_f02_deposit_franchise_growth_fs_mean_63d_base_v070_signal,
    f02dfg_f02_deposit_franchise_growth_fs_z_63d_base_v071_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_63d_base_v072_signal,
    f02dfg_f02_deposit_franchise_growth_dgxfs_63d_base_v073_signal,
    f02dfg_f02_deposit_franchise_growth_dg_log_63d_base_v074_signal,
    f02dfg_f02_deposit_franchise_growth_dg_sq_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_DEPOSIT_FRANCHISE_GROWTH_REGISTRY_001_075 = REGISTRY


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
    deposits     = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="deposits")
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
        "deposits": deposits,
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
    domain_primitives = ("_f02_deposit_growth", "_f02_deposit_intensity", "_f02_franchise_stability",)
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
        # body hash dup check
        body_lines = [ln.strip() for ln in src.splitlines()
                      if ln.strip() and not ln.strip().startswith("#") and not ln.strip().startswith("def ")]
        body_hash = hashlib.sha1("\n".join(body_lines).encode()).hexdigest()
        assert body_hash not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(body_hash)
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f02_deposit_franchise_growth_base_001_075_claude: {n_features} features pass, 0 dup bodies")
