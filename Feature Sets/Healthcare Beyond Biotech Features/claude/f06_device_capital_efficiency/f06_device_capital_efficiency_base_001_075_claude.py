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


# ===== folder domain primitives =====
def _f06_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f06_capital_efficiency(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f06_efficiency_compound(revenue, assets, w):
    ra = revenue / assets.replace(0, np.nan)
    return ra.rolling(w, min_periods=max(1, w // 2)).mean()

def f06dce_f06_device_capital_efficiency_p0raw_5d_base_v001_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 5.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_10d_base_v002_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 10.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_21d_base_v003_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 21.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_42d_base_v004_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 42.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_63d_base_v005_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 63.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_126d_base_v006_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 126.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_189d_base_v007_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 189.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_252d_base_v008_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 252.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_378d_base_v009_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 378.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0raw_504d_base_v010_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base * closeadj * 504.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_5d_base_v011_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_10d_base_v012_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_21d_base_v013_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_42d_base_v014_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_63d_base_v015_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_126d_base_v016_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_189d_base_v017_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_252d_base_v018_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_378d_base_v019_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0mean_504d_base_v020_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_5d_base_v021_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_10d_base_v022_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_21d_base_v023_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_42d_base_v024_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_63d_base_v025_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_126d_base_v026_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_189d_base_v027_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_252d_base_v028_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_378d_base_v029_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0std_504d_base_v030_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_5d_base_v031_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_10d_base_v032_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_21d_base_v033_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_42d_base_v034_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_63d_base_v035_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_126d_base_v036_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_189d_base_v037_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_252d_base_v038_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_378d_base_v039_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0z_504d_base_v040_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_5d_base_v041_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_10d_base_v042_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_21d_base_v043_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_42d_base_v044_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_63d_base_v045_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_126d_base_v046_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_189d_base_v047_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_252d_base_v048_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_378d_base_v049_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0ema_504d_base_v050_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = _ema(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_5d_base_v051_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_10d_base_v052_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_21d_base_v053_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_42d_base_v054_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_63d_base_v055_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_126d_base_v056_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_189d_base_v057_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_252d_base_v058_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_378d_base_v059_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0diff_504d_base_v060_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.diff(periods=504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_5d_base_v061_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_10d_base_v062_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_21d_base_v063_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_42d_base_v064_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_63d_base_v065_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_126d_base_v066_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_189d_base_v067_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_252d_base_v068_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_378d_base_v069_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0pct_504d_base_v070_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = base.pct_change(periods=504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0log_5d_base_v071_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 5.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0log_10d_base_v072_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 10.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0log_21d_base_v073_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 21.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0log_42d_base_v074_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 42.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

def f06dce_f06_device_capital_efficiency_p0log_63d_base_v075_signal(revenue, assets, closeadj):
    base = _f06_revenue_per_asset(revenue, assets)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * 63.0 / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06dce_f06_device_capital_efficiency_p0raw_5d_base_v001_signal,
    f06dce_f06_device_capital_efficiency_p0raw_10d_base_v002_signal,
    f06dce_f06_device_capital_efficiency_p0raw_21d_base_v003_signal,
    f06dce_f06_device_capital_efficiency_p0raw_42d_base_v004_signal,
    f06dce_f06_device_capital_efficiency_p0raw_63d_base_v005_signal,
    f06dce_f06_device_capital_efficiency_p0raw_126d_base_v006_signal,
    f06dce_f06_device_capital_efficiency_p0raw_189d_base_v007_signal,
    f06dce_f06_device_capital_efficiency_p0raw_252d_base_v008_signal,
    f06dce_f06_device_capital_efficiency_p0raw_378d_base_v009_signal,
    f06dce_f06_device_capital_efficiency_p0raw_504d_base_v010_signal,
    f06dce_f06_device_capital_efficiency_p0mean_5d_base_v011_signal,
    f06dce_f06_device_capital_efficiency_p0mean_10d_base_v012_signal,
    f06dce_f06_device_capital_efficiency_p0mean_21d_base_v013_signal,
    f06dce_f06_device_capital_efficiency_p0mean_42d_base_v014_signal,
    f06dce_f06_device_capital_efficiency_p0mean_63d_base_v015_signal,
    f06dce_f06_device_capital_efficiency_p0mean_126d_base_v016_signal,
    f06dce_f06_device_capital_efficiency_p0mean_189d_base_v017_signal,
    f06dce_f06_device_capital_efficiency_p0mean_252d_base_v018_signal,
    f06dce_f06_device_capital_efficiency_p0mean_378d_base_v019_signal,
    f06dce_f06_device_capital_efficiency_p0mean_504d_base_v020_signal,
    f06dce_f06_device_capital_efficiency_p0std_5d_base_v021_signal,
    f06dce_f06_device_capital_efficiency_p0std_10d_base_v022_signal,
    f06dce_f06_device_capital_efficiency_p0std_21d_base_v023_signal,
    f06dce_f06_device_capital_efficiency_p0std_42d_base_v024_signal,
    f06dce_f06_device_capital_efficiency_p0std_63d_base_v025_signal,
    f06dce_f06_device_capital_efficiency_p0std_126d_base_v026_signal,
    f06dce_f06_device_capital_efficiency_p0std_189d_base_v027_signal,
    f06dce_f06_device_capital_efficiency_p0std_252d_base_v028_signal,
    f06dce_f06_device_capital_efficiency_p0std_378d_base_v029_signal,
    f06dce_f06_device_capital_efficiency_p0std_504d_base_v030_signal,
    f06dce_f06_device_capital_efficiency_p0z_5d_base_v031_signal,
    f06dce_f06_device_capital_efficiency_p0z_10d_base_v032_signal,
    f06dce_f06_device_capital_efficiency_p0z_21d_base_v033_signal,
    f06dce_f06_device_capital_efficiency_p0z_42d_base_v034_signal,
    f06dce_f06_device_capital_efficiency_p0z_63d_base_v035_signal,
    f06dce_f06_device_capital_efficiency_p0z_126d_base_v036_signal,
    f06dce_f06_device_capital_efficiency_p0z_189d_base_v037_signal,
    f06dce_f06_device_capital_efficiency_p0z_252d_base_v038_signal,
    f06dce_f06_device_capital_efficiency_p0z_378d_base_v039_signal,
    f06dce_f06_device_capital_efficiency_p0z_504d_base_v040_signal,
    f06dce_f06_device_capital_efficiency_p0ema_5d_base_v041_signal,
    f06dce_f06_device_capital_efficiency_p0ema_10d_base_v042_signal,
    f06dce_f06_device_capital_efficiency_p0ema_21d_base_v043_signal,
    f06dce_f06_device_capital_efficiency_p0ema_42d_base_v044_signal,
    f06dce_f06_device_capital_efficiency_p0ema_63d_base_v045_signal,
    f06dce_f06_device_capital_efficiency_p0ema_126d_base_v046_signal,
    f06dce_f06_device_capital_efficiency_p0ema_189d_base_v047_signal,
    f06dce_f06_device_capital_efficiency_p0ema_252d_base_v048_signal,
    f06dce_f06_device_capital_efficiency_p0ema_378d_base_v049_signal,
    f06dce_f06_device_capital_efficiency_p0ema_504d_base_v050_signal,
    f06dce_f06_device_capital_efficiency_p0diff_5d_base_v051_signal,
    f06dce_f06_device_capital_efficiency_p0diff_10d_base_v052_signal,
    f06dce_f06_device_capital_efficiency_p0diff_21d_base_v053_signal,
    f06dce_f06_device_capital_efficiency_p0diff_42d_base_v054_signal,
    f06dce_f06_device_capital_efficiency_p0diff_63d_base_v055_signal,
    f06dce_f06_device_capital_efficiency_p0diff_126d_base_v056_signal,
    f06dce_f06_device_capital_efficiency_p0diff_189d_base_v057_signal,
    f06dce_f06_device_capital_efficiency_p0diff_252d_base_v058_signal,
    f06dce_f06_device_capital_efficiency_p0diff_378d_base_v059_signal,
    f06dce_f06_device_capital_efficiency_p0diff_504d_base_v060_signal,
    f06dce_f06_device_capital_efficiency_p0pct_5d_base_v061_signal,
    f06dce_f06_device_capital_efficiency_p0pct_10d_base_v062_signal,
    f06dce_f06_device_capital_efficiency_p0pct_21d_base_v063_signal,
    f06dce_f06_device_capital_efficiency_p0pct_42d_base_v064_signal,
    f06dce_f06_device_capital_efficiency_p0pct_63d_base_v065_signal,
    f06dce_f06_device_capital_efficiency_p0pct_126d_base_v066_signal,
    f06dce_f06_device_capital_efficiency_p0pct_189d_base_v067_signal,
    f06dce_f06_device_capital_efficiency_p0pct_252d_base_v068_signal,
    f06dce_f06_device_capital_efficiency_p0pct_378d_base_v069_signal,
    f06dce_f06_device_capital_efficiency_p0pct_504d_base_v070_signal,
    f06dce_f06_device_capital_efficiency_p0log_5d_base_v071_signal,
    f06dce_f06_device_capital_efficiency_p0log_10d_base_v072_signal,
    f06dce_f06_device_capital_efficiency_p0log_21d_base_v073_signal,
    f06dce_f06_device_capital_efficiency_p0log_42d_base_v074_signal,
    f06dce_f06_device_capital_efficiency_p0log_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_DEVICE_CAPITAL_EFFICIENCY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    inventory   = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "assets": assets, "ppnenet": ppnenet, "capex": capex,
        "inventory": inventory, "receivables": receivables, "cor": cor,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_revenue_per_asset", "_f06_capital_efficiency", "_f06_efficiency_compound",)
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
    print(f"OK f06_device_capital_efficiency_base_001_075_claude: {n_features} features pass")
