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



def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f02_deposit_growth(deposits, w):
    return (deposits - deposits.shift(w)) / deposits.shift(w).abs().replace(0, np.nan)


def _f02_deposit_intensity(deposits, assets):
    return deposits / assets.replace(0, np.nan).abs()


def _f02_franchise_stability(deposits, w):
    m = deposits.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = deposits.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v001_signal(deposits, assets):
    base = _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v002_signal(deposits, assets):
    base = _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v003_signal(deposits, assets):
    base = _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v004_signal(deposits, assets):
    base = _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v005_signal(deposits, assets):
    base = _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v006_signal(deposits, assets):
    base = _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v007_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v008_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v009_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v010_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v011_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v012_signal(deposits, assets, closeadj):
    base = _f02_deposit_intensity(deposits, assets) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v013_signal(deposits):
    base = _f02_deposit_growth(deposits, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v014_signal(deposits):
    base = _f02_deposit_growth(deposits, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v015_signal(deposits):
    base = _f02_deposit_growth(deposits, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v016_signal(deposits):
    base = _f02_deposit_growth(deposits, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v017_signal(deposits):
    base = _f02_deposit_growth(deposits, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v018_signal(deposits):
    base = _f02_deposit_growth(deposits, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v019_signal(deposits):
    base = _f02_franchise_stability(deposits, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v020_signal(deposits):
    base = _f02_franchise_stability(deposits, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v021_signal(deposits):
    base = _f02_franchise_stability(deposits, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v022_signal(deposits):
    base = _f02_franchise_stability(deposits, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v023_signal(deposits):
    base = _f02_franchise_stability(deposits, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v024_signal(deposits):
    base = _f02_franchise_stability(deposits, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v025_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v026_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v027_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v028_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v029_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v030_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v031_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 21) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v032_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 21) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v033_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 21) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v034_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 21) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v035_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 21) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v036_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 21) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v037_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v038_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v039_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v040_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v041_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v042_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v043_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 21) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v044_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 21) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v045_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 21) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v046_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 21) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v047_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 21) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v048_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 21) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v049_signal(deposits):
    base = _f02_deposit_growth(deposits, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v050_signal(deposits):
    base = _f02_deposit_growth(deposits, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v051_signal(deposits):
    base = _f02_deposit_growth(deposits, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v052_signal(deposits):
    base = _f02_deposit_growth(deposits, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v053_signal(deposits):
    base = _f02_deposit_growth(deposits, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v054_signal(deposits):
    base = _f02_deposit_growth(deposits, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v055_signal(deposits):
    base = _f02_franchise_stability(deposits, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v056_signal(deposits):
    base = _f02_franchise_stability(deposits, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v057_signal(deposits):
    base = _f02_franchise_stability(deposits, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v058_signal(deposits):
    base = _f02_franchise_stability(deposits, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v059_signal(deposits):
    base = _f02_franchise_stability(deposits, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v060_signal(deposits):
    base = _f02_franchise_stability(deposits, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v061_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v062_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v063_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v064_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v065_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v066_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v067_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 42) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v068_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 42) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v069_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 42) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v070_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 42) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v071_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 42) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v072_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 42) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v073_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v074_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v075_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v076_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 42) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v077_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v078_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 42) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v079_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 42) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v080_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 42) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v081_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 42) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v082_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 42) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v083_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 42) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v084_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 42) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v085_signal(deposits):
    base = _f02_deposit_growth(deposits, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v086_signal(deposits):
    base = _f02_deposit_growth(deposits, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v087_signal(deposits):
    base = _f02_deposit_growth(deposits, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v088_signal(deposits):
    base = _f02_deposit_growth(deposits, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v089_signal(deposits):
    base = _f02_deposit_growth(deposits, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v090_signal(deposits):
    base = _f02_deposit_growth(deposits, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v091_signal(deposits):
    base = _f02_franchise_stability(deposits, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v092_signal(deposits):
    base = _f02_franchise_stability(deposits, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v093_signal(deposits):
    base = _f02_franchise_stability(deposits, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v094_signal(deposits):
    base = _f02_franchise_stability(deposits, 63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v095_signal(deposits):
    base = _f02_franchise_stability(deposits, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v096_signal(deposits):
    base = _f02_franchise_stability(deposits, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v097_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v098_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v099_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v100_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v101_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v102_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v103_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 63) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v104_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 63) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v105_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 63) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v106_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 63) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v107_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 63) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v108_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 63) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v109_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v110_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v111_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v112_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v113_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v114_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v115_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 63) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v116_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 63) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v117_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 63) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v118_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 63) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v119_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 63) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v120_signal(deposits, assets):
    base = _f02_deposit_growth(deposits, 63) * _f02_deposit_intensity(deposits, assets)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v121_signal(deposits):
    base = _f02_deposit_growth(deposits, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v122_signal(deposits):
    base = _f02_deposit_growth(deposits, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v123_signal(deposits):
    base = _f02_deposit_growth(deposits, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v124_signal(deposits):
    base = _f02_deposit_growth(deposits, 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v125_signal(deposits):
    base = _f02_deposit_growth(deposits, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v126_signal(deposits):
    base = _f02_deposit_growth(deposits, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v127_signal(deposits):
    base = _f02_franchise_stability(deposits, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v128_signal(deposits):
    base = _f02_franchise_stability(deposits, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v129_signal(deposits):
    base = _f02_franchise_stability(deposits, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v130_signal(deposits):
    base = _f02_franchise_stability(deposits, 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v131_signal(deposits):
    base = _f02_franchise_stability(deposits, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v132_signal(deposits):
    base = _f02_franchise_stability(deposits, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v133_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v134_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v135_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v136_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v137_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v138_signal(deposits, closeadj):
    base = _f02_deposit_growth(deposits, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v139_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 126) * closeadj / 100.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v140_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 126) * closeadj / 100.0
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v141_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 126) * closeadj / 100.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v142_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 126) * closeadj / 100.0
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v143_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 126) * closeadj / 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v144_signal(deposits, closeadj):
    base = _f02_franchise_stability(deposits, 126) * closeadj / 100.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v145_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v146_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v147_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v148_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v149_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v150_signal(deposits, assets, closeadj):
    base = _mean(_f02_deposit_intensity(deposits, assets), 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v001_signal,
    f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v002_signal,
    f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v003_signal,
    f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v004_signal,
    f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v005_signal,
    f02dfg_f02_deposit_franchise_growth_di_0d_jerk_v006_signal,
    f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v007_signal,
    f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v008_signal,
    f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v009_signal,
    f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v010_signal,
    f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v011_signal,
    f02dfg_f02_deposit_franchise_growth_dixclose_0d_jerk_v012_signal,
    f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v013_signal,
    f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v014_signal,
    f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v015_signal,
    f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v016_signal,
    f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v017_signal,
    f02dfg_f02_deposit_franchise_growth_dg_21d_jerk_v018_signal,
    f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v019_signal,
    f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v020_signal,
    f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v021_signal,
    f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v022_signal,
    f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v023_signal,
    f02dfg_f02_deposit_franchise_growth_fs_21d_jerk_v024_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v025_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v026_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v027_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v028_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v029_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_21d_jerk_v030_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v031_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v032_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v033_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v034_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v035_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_21d_jerk_v036_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v037_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v038_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v039_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v040_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v041_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_21d_jerk_v042_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v043_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v044_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v045_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v046_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v047_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_21d_jerk_v048_signal,
    f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v049_signal,
    f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v050_signal,
    f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v051_signal,
    f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v052_signal,
    f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v053_signal,
    f02dfg_f02_deposit_franchise_growth_dg_42d_jerk_v054_signal,
    f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v055_signal,
    f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v056_signal,
    f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v057_signal,
    f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v058_signal,
    f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v059_signal,
    f02dfg_f02_deposit_franchise_growth_fs_42d_jerk_v060_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v061_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v062_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v063_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v064_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v065_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_42d_jerk_v066_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v067_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v068_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v069_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v070_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v071_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_42d_jerk_v072_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v073_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v074_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v075_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v076_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v077_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_42d_jerk_v078_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v079_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v080_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v081_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v082_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v083_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_42d_jerk_v084_signal,
    f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v085_signal,
    f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v086_signal,
    f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v087_signal,
    f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v088_signal,
    f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v089_signal,
    f02dfg_f02_deposit_franchise_growth_dg_63d_jerk_v090_signal,
    f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v091_signal,
    f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v092_signal,
    f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v093_signal,
    f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v094_signal,
    f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v095_signal,
    f02dfg_f02_deposit_franchise_growth_fs_63d_jerk_v096_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v097_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v098_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v099_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v100_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v101_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_63d_jerk_v102_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v103_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v104_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v105_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v106_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v107_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_63d_jerk_v108_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v109_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v110_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v111_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v112_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v113_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_63d_jerk_v114_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v115_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v116_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v117_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v118_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v119_signal,
    f02dfg_f02_deposit_franchise_growth_dgxdi_63d_jerk_v120_signal,
    f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v121_signal,
    f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v122_signal,
    f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v123_signal,
    f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v124_signal,
    f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v125_signal,
    f02dfg_f02_deposit_franchise_growth_dg_126d_jerk_v126_signal,
    f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v127_signal,
    f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v128_signal,
    f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v129_signal,
    f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v130_signal,
    f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v131_signal,
    f02dfg_f02_deposit_franchise_growth_fs_126d_jerk_v132_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v133_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v134_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v135_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v136_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v137_signal,
    f02dfg_f02_deposit_franchise_growth_dgxclose_126d_jerk_v138_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v139_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v140_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v141_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v142_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v143_signal,
    f02dfg_f02_deposit_franchise_growth_fsxclose_126d_jerk_v144_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v145_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v146_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v147_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v148_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v149_signal,
    f02dfg_f02_deposit_franchise_growth_dismooth_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_DEPOSIT_FRANCHISE_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f02_deposit_franchise_growth_3rd_derivatives_001_150_claude: {n_features} features pass, 0 dup bodies")
