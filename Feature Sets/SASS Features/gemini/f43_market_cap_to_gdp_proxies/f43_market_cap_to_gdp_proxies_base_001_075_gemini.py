
import numpy as np
import pandas as pd
import inspect

def _safe_div(a, b):
    return a / b.replace(0, np.nan)

def _z(x, w):
    return (x - x.rolling(w, min_periods=w//2).mean()) / x.rolling(w, min_periods=w//2).std().replace(0, np.nan)

def _rank(x, w):
    return x.rolling(w, min_periods=w//2).rank(pct=True) - 0.5

def _slope(x, w):
    return x.diff(w) / x.shift(w).abs().replace(0, np.nan)

def _jerk(x, w):
    s = _slope(x, w)
    return _slope(s, w)

def _f43_mcap_gdp(mcap, gdp):
    return _safe_div(mcap, gdp)

def _f43_norm_rev(mcap, rev):
    return _safe_div(mcap, rev)

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v001_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v001_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v002_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v002_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v003_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v003_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v004_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v004_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v005_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v005_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v006_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v006_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v007_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v007_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v008_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v008_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v009_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v009_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v010_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v010_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v011_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v011_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v012_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v012_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v013_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v013_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v014_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v014_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v015_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v015_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v016_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v016_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v017_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v017_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v018_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v018_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v019_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v019_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v020_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v020_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v021_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v021_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v022_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v022_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v023_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v023_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v024_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v024_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v025_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v025_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v026_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v026_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v027_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v027_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v028_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v028_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v029_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v029_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v030_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v030_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v031_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v031_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v032_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v032_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v033_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v033_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v034_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v034_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v035_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v035_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v036_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v036_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v037_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v037_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v038_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v038_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v039_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v039_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v040_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v040_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v041_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v041_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v042_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v042_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v043_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v043_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v044_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v044_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v045_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v045_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v046_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v046_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v047_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v047_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v048_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v048_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v049_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v049_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v050_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v050_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v051_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v051_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v052_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v052_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v053_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v053_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v054_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v054_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v055_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v055_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v056_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v056_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v057_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v057_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v058_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v058_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v059_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v059_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v060_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v060_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v061_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v061_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v062_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v062_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v063_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v063_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v064_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v064_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v065_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v065_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v066_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v066_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v067_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v067_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v068_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v068_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v069_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v069_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v070_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v070_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v071_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v071_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v072_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v072_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v073_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v073_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v074_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v074_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v075_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v075_signal')

_FEATURES = [f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v001_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v002_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v003_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v004_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v005_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v006_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v007_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v008_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v009_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v010_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v011_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v012_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v013_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v014_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v015_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v016_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v017_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v018_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v019_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v020_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v021_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v022_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v023_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v024_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v025_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_base_v026_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_base_v027_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_base_v028_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_base_v029_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_base_v030_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v031_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v032_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v033_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v034_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v035_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v036_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v037_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v038_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v039_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v040_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v041_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v042_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v043_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v044_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v045_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v046_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v047_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v048_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v049_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v050_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v051_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v052_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v053_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v054_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v055_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_base_v056_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_base_v057_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_base_v058_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_base_v059_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_base_v060_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v061_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v062_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v063_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v064_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v065_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v066_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v067_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v068_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v069_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v070_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_base_v071_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_base_v072_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_base_v073_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_base_v074_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_base_v075_signal]
def _inputs_for(fn): return [p.name for p in inspect.signature(fn).parameters.values()]
REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F43MG_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    import numpy as np, pandas as pd
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0*np.exp(np.cumsum(rets)), name="closeadj")
    close    = pd.Series(closeadj.values, name="close")
    openp    = pd.Series(close.shift(1).fillna(close.iloc[0]).values*(1+np.random.normal(0,0.005,n)), name="open")
    high     = pd.Series(np.maximum(close, openp)*(1+np.abs(np.random.normal(0,0.01,n))), name="high")
    low      = pd.Series(np.minimum(close, openp)*(1-np.abs(np.random.normal(0,0.01,n))), name="low")
    volume   = pd.Series(np.abs(np.random.normal(1e6,3e5,n))+1e5, name="volume")      
    
    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n//63 + 1), 63)[:n]
        s = base*np.exp(np.cumsum(steps/63))
        if allow_neg: s = s - base*0.3
        return pd.Series(s, name=None)
    
    marketcap = _fund(np.random.randint(0, 10000), allow_neg=True).rename("marketcap")
    revenue = _fund(np.random.randint(0, 10000), allow_neg=True).rename("revenue")
    gdp_proxy = _fund(np.random.randint(0, 10000), allow_neg=True).rename("gdp_proxy")
    assets = _fund(np.random.randint(0, 10000), allow_neg=True).rename("assets")

    
    _FEATURES = [v for k, v in globals().items() if k.endswith("_signal") and callable(v)]
    for fn in _FEATURES:
        res = fn(**{k: v for k, v in locals().items() if k in inspect.signature(fn).parameters})
        assert res.name.endswith("_signal")
        assert len(res) == n
    print(f"OK: {len(_FEATURES)} features passed")
