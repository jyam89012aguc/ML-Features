
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

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v001_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v001_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v002_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v002_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v003_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v003_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v004_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v004_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v005_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v005_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v006_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v006_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v007_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v007_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v008_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v008_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v009_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v009_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v010_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v010_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v011_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v011_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v012_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v012_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v013_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v013_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v014_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v014_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v015_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v015_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v016_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v016_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v017_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v017_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v018_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v018_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v019_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v019_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v020_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v020_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v021_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v021_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v022_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v022_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v023_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v023_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v024_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v024_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v025_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v025_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v026_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v026_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v027_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v027_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v028_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v028_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v029_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v029_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v030_signal(marketcap, gdp_proxy):
    result = _z(_f43_mcap_gdp(marketcap, gdp_proxy), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v030_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v031_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v031_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v032_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v032_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v033_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v033_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v034_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v034_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v035_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v035_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v036_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v036_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v037_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v037_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v038_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v038_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v039_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v039_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v040_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v040_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v041_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v041_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v042_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v042_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v043_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v043_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v044_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v044_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v045_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v045_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v046_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v046_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v047_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v047_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v048_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v048_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v049_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v049_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v050_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v050_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v051_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v051_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v052_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v052_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v053_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v053_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v054_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v054_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v055_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v055_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v056_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v056_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v057_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v057_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v058_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v058_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v059_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v059_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v060_signal(marketcap, revenue):
    result = _rank(_f43_norm_rev(marketcap, revenue), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v060_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v061_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v061_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v062_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v062_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v063_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v063_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v064_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v064_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v065_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v065_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v066_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v066_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v067_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v067_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v068_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v068_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v069_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v069_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v070_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v070_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v071_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v071_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v072_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v072_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v073_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v073_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v074_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v074_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v075_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v075_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v076_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v076_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v077_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v077_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v078_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v078_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v079_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v079_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v080_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v080_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v081_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v081_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v082_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v082_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v083_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v083_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v084_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v084_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v085_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v085_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v086_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v086_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v087_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v087_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v088_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v088_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v089_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v089_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v090_signal(marketcap, assets):
    result = _z(_safe_div(marketcap, assets), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v090_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v091_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v091_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v092_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v092_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v093_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v093_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v094_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v094_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v095_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v095_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v096_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v096_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v097_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v097_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v098_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v098_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v099_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v099_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v100_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v100_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v101_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v101_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v102_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v102_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v103_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v103_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v104_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v104_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v105_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v105_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v106_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v106_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v107_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v107_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v108_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v108_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v109_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v109_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v110_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v110_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v111_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v111_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v112_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v112_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v113_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v113_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v114_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v114_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v115_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v115_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v116_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v116_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v117_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v117_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v118_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v118_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v119_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v119_signal')

def f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v120_signal(marketcap, equity):
    result = _rank(_safe_div(marketcap, equity), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v120_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v121_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v121_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v122_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v122_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v123_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v123_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v124_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v124_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v125_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v125_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v126_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v126_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v127_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v127_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v128_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v128_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v129_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v129_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v130_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v130_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v131_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v131_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v132_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v132_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v133_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v133_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v134_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v134_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v135_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v135_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v136_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v136_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v137_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v137_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v138_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v138_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v139_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v139_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v140_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v140_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v141_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v141_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v142_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v142_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v143_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v143_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v144_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v144_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v145_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v145_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v146_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 21), 21)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v146_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v147_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 63), 63)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v147_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v148_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 126), 126)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v148_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v149_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 252), 252)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v149_signal')

def f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v150_signal(marketcap, gdp_proxy, volume, closeadj):
    ratio = _f43_mcap_gdp(marketcap, gdp_proxy)
    result = _z(ratio * _z(volume * closeadj, 504), 504)
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan).rename('f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v150_signal')

_FEATURES = [f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v001_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v002_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v003_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v004_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v005_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v006_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v007_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v008_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v009_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v010_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v011_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v012_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v013_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v014_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v015_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v016_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v017_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v018_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v019_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v020_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v021_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v022_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v023_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v024_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v025_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_21d_jerk_v026_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_63d_jerk_v027_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_126d_jerk_v028_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_252d_jerk_v029_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdp_504d_jerk_v030_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v031_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v032_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v033_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v034_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v035_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v036_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v037_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v038_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v039_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v040_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v041_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v042_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v043_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v044_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v045_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v046_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v047_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v048_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v049_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v050_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v051_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v052_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v053_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v054_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v055_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_21d_jerk_v056_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_63d_jerk_v057_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_126d_jerk_v058_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_252d_jerk_v059_signal, f43mg_f43_market_cap_to_gdp_proxies_mrev_504d_jerk_v060_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v061_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v062_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v063_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v064_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v065_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v066_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v067_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v068_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v069_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v070_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v071_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v072_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v073_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v074_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v075_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v076_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v077_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v078_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v079_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v080_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v081_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v082_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v083_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v084_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v085_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_21d_jerk_v086_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_63d_jerk_v087_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_126d_jerk_v088_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_252d_jerk_v089_signal, f43mg_f43_market_cap_to_gdp_proxies_mass_504d_jerk_v090_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v091_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v092_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v093_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v094_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v095_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v096_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v097_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v098_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v099_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v100_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v101_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v102_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v103_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v104_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v105_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v106_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v107_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v108_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v109_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v110_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v111_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v112_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v113_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v114_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v115_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_21d_jerk_v116_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_63d_jerk_v117_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_126d_jerk_v118_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_252d_jerk_v119_signal, f43mg_f43_market_cap_to_gdp_proxies_meq_504d_jerk_v120_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v121_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v122_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v123_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v124_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v125_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v126_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v127_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v128_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v129_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v130_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v131_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v132_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v133_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v134_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v135_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v136_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v137_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v138_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v139_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v140_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v141_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v142_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v143_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v144_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v145_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_21d_jerk_v146_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_63d_jerk_v147_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_126d_jerk_v148_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_252d_jerk_v149_signal, f43mg_f43_market_cap_to_gdp_proxies_mgdpv_504d_jerk_v150_signal]
def _inputs_for(fn): return [p.name for p in inspect.signature(fn).parameters.values()]
REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F43MG_REGISTRY_JERKS = REGISTRY

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
    
    revenue = _fund(np.random.randint(0, 10000), allow_neg=True).rename("revenue")
    equity = _fund(np.random.randint(0, 10000), allow_neg=True).rename("equity")
    assets = _fund(np.random.randint(0, 10000), allow_neg=True).rename("assets")
    marketcap = _fund(np.random.randint(0, 10000), allow_neg=True).rename("marketcap")
    gdp_proxy = _fund(np.random.randint(0, 10000), allow_neg=True).rename("gdp_proxy")

    
    _FEATURES = [v for k, v in globals().items() if k.endswith("_signal") and callable(v)]
    for fn in _FEATURES:
        res = fn(**{k: v for k, v in locals().items() if k in inspect.signature(fn).parameters})
        assert res.name.endswith("_signal")
        assert len(res) == n
    print(f"OK: {len(_FEATURES)} features passed")
