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

def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _f073_asset_growth(assets, w):
    return assets.pct_change(periods=w) * assets


def _f073_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w) * revenue


def _f073_asset_light_gap(revenue, assets, w):
    rev_g = revenue.pct_change(periods=w)
    asset_g = assets.pct_change(periods=w)
    return (rev_g - asset_g) * revenue

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v001_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v002_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v003_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v004_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v005_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v006_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v007_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v008_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v009_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v010_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v011_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v012_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v013_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v014_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v015_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v016_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v017_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v018_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v019_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v020_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v021_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v022_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v023_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v024_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v025_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v026_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v027_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v028_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v029_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v030_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v031_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v032_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v033_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v034_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v035_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v036_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v037_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v038_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v039_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v040_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v041_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v042_signal(revenue, assets, closeadj):
    base = _f073_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v043_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v044_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_growth(assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v045_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v046_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_growth(assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v047_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v048_signal(revenue, assets, closeadj):
    base = (_f073_asset_growth(assets, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v049_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v050_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_growth(assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v051_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v052_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v053_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v054_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v055_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v056_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v057_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v058_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v059_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v060_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v061_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v062_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v063_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v064_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v065_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v066_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v067_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v068_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v069_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v070_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v071_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v072_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v073_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v074_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v075_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v076_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v077_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v078_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v079_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v080_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v081_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v082_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v083_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v084_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v085_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v086_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v087_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v088_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v089_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v090_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v091_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v092_signal(revenue, assets, closeadj):
    base = _f073_revenue_growth(revenue, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v093_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v094_signal(revenue, assets, closeadj):
    base = _mean(_f073_revenue_growth(revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v095_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v096_signal(revenue, assets, closeadj):
    base = _std(_f073_revenue_growth(revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v097_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v098_signal(revenue, assets, closeadj):
    base = (_f073_revenue_growth(revenue, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v099_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v100_signal(revenue, assets, closeadj):
    base = _z(_f073_revenue_growth(revenue, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v101_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v102_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v103_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v104_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v105_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v106_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v107_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v108_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v109_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_jerk_v110_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v111_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v112_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v113_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v114_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v115_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v116_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v117_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v118_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v119_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_jerk_v120_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v121_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v122_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v123_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v124_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v125_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v126_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v127_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v128_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v129_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_jerk_v130_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v131_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v132_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v133_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v134_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v135_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v136_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v137_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v138_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v139_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_jerk_v140_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v141_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v142_signal(revenue, assets, closeadj):
    base = _f073_asset_light_gap(revenue, assets, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v143_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v144_signal(revenue, assets, closeadj):
    base = _mean(_f073_asset_light_gap(revenue, assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v145_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v146_signal(revenue, assets, closeadj):
    base = _std(_f073_asset_light_gap(revenue, assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v147_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v148_signal(revenue, assets, closeadj):
    base = (_f073_asset_light_gap(revenue, assets, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v149_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_jerk_v150_signal(revenue, assets, closeadj):
    base = _z(_f073_asset_light_gap(revenue, assets, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v001_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v002_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v003_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v004_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v005_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v006_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v007_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v008_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v009_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_jerk_v010_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v011_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v012_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v013_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v014_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v015_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v016_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v017_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v018_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v019_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_jerk_v020_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v021_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v022_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v023_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v024_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v025_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v026_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v027_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v028_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v029_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_jerk_v030_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v031_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v032_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v033_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v034_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v035_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v036_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v037_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v038_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v039_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_jerk_v040_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v041_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v042_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v043_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v044_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v045_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v046_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v047_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v048_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v049_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_jerk_v050_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v051_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v052_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v053_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v054_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v055_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v056_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v057_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v058_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v059_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_jerk_v060_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v061_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v062_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v063_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v064_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v065_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v066_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v067_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v068_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v069_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_jerk_v070_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v071_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v072_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v073_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v074_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v075_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v076_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v077_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v078_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v079_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_jerk_v080_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v081_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v082_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v083_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v084_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v085_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v086_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v087_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v088_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v089_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_jerk_v090_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v091_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v092_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v093_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v094_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v095_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v096_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v097_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v098_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v099_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_jerk_v100_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v101_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v102_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v103_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v104_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v105_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v106_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v107_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v108_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v109_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_jerk_v110_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v111_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v112_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v113_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v114_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v115_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v116_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v117_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v118_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v119_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_jerk_v120_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v121_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v122_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v123_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v124_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v125_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v126_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v127_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v128_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v129_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_jerk_v130_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v131_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v132_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v133_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v134_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v135_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v136_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v137_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v138_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v139_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_jerk_v140_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v141_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v142_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v143_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v144_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v145_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v146_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v147_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v148_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v149_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F073_ASSET_LIGHT_SCALING_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    cols = {"revenue": revenue, "assets": assets, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f073_asset_growth", "_f073_revenue_growth", "_f073_asset_light_gap")
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
    print(f"OK f073_asset_light_scaling_jerk_001_150_claude: {n_features} features pass")
