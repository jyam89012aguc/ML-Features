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
def _f073_asset_growth(assets, w):
    return assets.pct_change(periods=w) * assets


def _f073_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w) * revenue


def _f073_asset_light_gap(revenue, assets, w):
    rev_g = revenue.pct_change(periods=w)
    asset_g = assets.pct_change(periods=w)
    return (rev_g - asset_g) * revenue

def f073als_f073_asset_light_scaling_assetgrowth_5d_base_v001_signal(revenue, assets, closeadj):
    result = _f073_asset_growth(assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_base_v002_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_base_v003_signal(revenue, assets, closeadj):
    result = np.sign(_f073_asset_growth(assets, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_base_v004_signal(revenue, assets, closeadj):
    result = _mean(_f073_asset_growth(assets, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_5d_base_v005_signal(revenue, assets, closeadj):
    result = _std(_f073_asset_growth(assets, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_base_v006_signal(revenue, assets, closeadj):
    result = _z(_f073_asset_growth(assets, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_base_v007_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 21)) * (_f073_asset_growth(assets, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_base_v008_signal(revenue, assets, closeadj):
    result = np.sqrt((_f073_asset_growth(assets, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_base_v009_signal(revenue, assets, closeadj):
    result = np.log1p((_f073_asset_growth(assets, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_21d_base_v010_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_base_v011_signal(revenue, assets, closeadj):
    result = _mean(_f073_asset_growth(assets, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_base_v012_signal(revenue, assets, closeadj):
    result = _std(_f073_asset_growth(assets, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_base_v013_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_base_v014_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_63d_base_v015_signal(revenue, assets, closeadj):
    result = _z(_f073_asset_growth(assets, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_base_v016_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_base_v017_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_base_v018_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_base_v019_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_126d_base_v020_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_base_v021_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_base_v022_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 252)) * (_f073_asset_growth(assets, 252)) * (_f073_asset_growth(assets, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_base_v023_signal(revenue, assets, closeadj):
    result = (_f073_asset_growth(assets, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_base_v024_signal(revenue, assets, closeadj):
    result = ((_f073_asset_growth(assets, 252)) - (_f073_asset_growth(assets, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_assetgrowth_252d_base_v025_signal(revenue, assets, closeadj):
    result = ((_f073_asset_growth(assets, 252)) / (_f073_asset_growth(assets, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_base_v026_signal(revenue, assets, closeadj):
    result = _f073_revenue_growth(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_base_v027_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_base_v028_signal(revenue, assets, closeadj):
    result = np.sign(_f073_revenue_growth(revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_base_v029_signal(revenue, assets, closeadj):
    result = _mean(_f073_revenue_growth(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_5d_base_v030_signal(revenue, assets, closeadj):
    result = _std(_f073_revenue_growth(revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_base_v031_signal(revenue, assets, closeadj):
    result = _z(_f073_revenue_growth(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_base_v032_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 21)) * (_f073_revenue_growth(revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_base_v033_signal(revenue, assets, closeadj):
    result = np.sqrt((_f073_revenue_growth(revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_base_v034_signal(revenue, assets, closeadj):
    result = np.log1p((_f073_revenue_growth(revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_21d_base_v035_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_base_v036_signal(revenue, assets, closeadj):
    result = _mean(_f073_revenue_growth(revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_base_v037_signal(revenue, assets, closeadj):
    result = _std(_f073_revenue_growth(revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_base_v038_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_base_v039_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_63d_base_v040_signal(revenue, assets, closeadj):
    result = _z(_f073_revenue_growth(revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_base_v041_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_base_v042_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_base_v043_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_base_v044_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_126d_base_v045_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_base_v046_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_base_v047_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 252)) * (_f073_revenue_growth(revenue, 252)) * (_f073_revenue_growth(revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_base_v048_signal(revenue, assets, closeadj):
    result = (_f073_revenue_growth(revenue, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_base_v049_signal(revenue, assets, closeadj):
    result = ((_f073_revenue_growth(revenue, 252)) - (_f073_revenue_growth(revenue, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_revgrowth_252d_base_v050_signal(revenue, assets, closeadj):
    result = ((_f073_revenue_growth(revenue, 252)) / (_f073_revenue_growth(revenue, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_base_v051_signal(revenue, assets, closeadj):
    result = _f073_asset_light_gap(revenue, assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_base_v052_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_base_v053_signal(revenue, assets, closeadj):
    result = np.sign(_f073_asset_light_gap(revenue, assets, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_base_v054_signal(revenue, assets, closeadj):
    result = _mean(_f073_asset_light_gap(revenue, assets, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_5d_base_v055_signal(revenue, assets, closeadj):
    result = _std(_f073_asset_light_gap(revenue, assets, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_base_v056_signal(revenue, assets, closeadj):
    result = _z(_f073_asset_light_gap(revenue, assets, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_base_v057_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 21)) * (_f073_asset_light_gap(revenue, assets, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_base_v058_signal(revenue, assets, closeadj):
    result = np.sqrt((_f073_asset_light_gap(revenue, assets, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_base_v059_signal(revenue, assets, closeadj):
    result = np.log1p((_f073_asset_light_gap(revenue, assets, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_21d_base_v060_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_base_v061_signal(revenue, assets, closeadj):
    result = _mean(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_base_v062_signal(revenue, assets, closeadj):
    result = _std(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_base_v063_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_base_v064_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_63d_base_v065_signal(revenue, assets, closeadj):
    result = _z(_f073_asset_light_gap(revenue, assets, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_base_v066_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_base_v067_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_base_v068_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_base_v069_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_126d_base_v070_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_base_v071_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_base_v072_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 252)) * (_f073_asset_light_gap(revenue, assets, 252)) * (_f073_asset_light_gap(revenue, assets, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_base_v073_signal(revenue, assets, closeadj):
    result = (_f073_asset_light_gap(revenue, assets, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_base_v074_signal(revenue, assets, closeadj):
    result = ((_f073_asset_light_gap(revenue, assets, 252)) - (_f073_asset_light_gap(revenue, assets, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f073als_f073_asset_light_scaling_lightgap_252d_base_v075_signal(revenue, assets, closeadj):
    result = ((_f073_asset_light_gap(revenue, assets, 252)) / (_f073_asset_light_gap(revenue, assets, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f073als_f073_asset_light_scaling_assetgrowth_5d_base_v001_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_base_v002_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_base_v003_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_base_v004_signal,
    f073als_f073_asset_light_scaling_assetgrowth_5d_base_v005_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_base_v006_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_base_v007_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_base_v008_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_base_v009_signal,
    f073als_f073_asset_light_scaling_assetgrowth_21d_base_v010_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_base_v011_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_base_v012_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_base_v013_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_base_v014_signal,
    f073als_f073_asset_light_scaling_assetgrowth_63d_base_v015_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_base_v016_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_base_v017_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_base_v018_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_base_v019_signal,
    f073als_f073_asset_light_scaling_assetgrowth_126d_base_v020_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_base_v021_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_base_v022_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_base_v023_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_base_v024_signal,
    f073als_f073_asset_light_scaling_assetgrowth_252d_base_v025_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_base_v026_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_base_v027_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_base_v028_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_base_v029_signal,
    f073als_f073_asset_light_scaling_revgrowth_5d_base_v030_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_base_v031_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_base_v032_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_base_v033_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_base_v034_signal,
    f073als_f073_asset_light_scaling_revgrowth_21d_base_v035_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_base_v036_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_base_v037_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_base_v038_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_base_v039_signal,
    f073als_f073_asset_light_scaling_revgrowth_63d_base_v040_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_base_v041_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_base_v042_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_base_v043_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_base_v044_signal,
    f073als_f073_asset_light_scaling_revgrowth_126d_base_v045_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_base_v046_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_base_v047_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_base_v048_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_base_v049_signal,
    f073als_f073_asset_light_scaling_revgrowth_252d_base_v050_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_base_v051_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_base_v052_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_base_v053_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_base_v054_signal,
    f073als_f073_asset_light_scaling_lightgap_5d_base_v055_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_base_v056_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_base_v057_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_base_v058_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_base_v059_signal,
    f073als_f073_asset_light_scaling_lightgap_21d_base_v060_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_base_v061_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_base_v062_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_base_v063_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_base_v064_signal,
    f073als_f073_asset_light_scaling_lightgap_63d_base_v065_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_base_v066_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_base_v067_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_base_v068_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_base_v069_signal,
    f073als_f073_asset_light_scaling_lightgap_126d_base_v070_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_base_v071_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_base_v072_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_base_v073_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_base_v074_signal,
    f073als_f073_asset_light_scaling_lightgap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F073_ASSET_LIGHT_SCALING_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f073_asset_light_scaling_001_075_claude: {n_features} features pass")
