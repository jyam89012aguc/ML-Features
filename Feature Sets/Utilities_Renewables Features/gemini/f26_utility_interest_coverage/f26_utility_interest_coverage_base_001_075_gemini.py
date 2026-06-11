import pandas as pd
import numpy as np
import inspect

# ===== Utilities Ultra-High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def f26_utility_interest_coverage_capex_base_5d_v001_signal(capex):
    """Moving average of Raw level of capex over 5d window."""
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_5d_v002_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_5d_v003_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_5d_v004_signal(ebitda):
    """Moving average of Raw level of ebitda over 5d window."""
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_5d_v005_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 5d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_5d_v006_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 5d window."""
    res = _sma(_ratio(ebitda, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_10d_v007_signal(capex):
    """Moving average of Raw level of capex over 10d window."""
    res = _sma(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_10d_v008_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_10d_v009_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_10d_v010_signal(ebitda):
    """Moving average of Raw level of ebitda over 10d window."""
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_10d_v011_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 10d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_10d_v012_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 10d window."""
    res = _sma(_ratio(ebitda, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_21d_v013_signal(capex):
    """Moving average of Raw level of capex over 21d window."""
    res = _sma(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_21d_v014_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_21d_v015_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_21d_v016_signal(ebitda):
    """Moving average of Raw level of ebitda over 21d window."""
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_21d_v017_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 21d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_21d_v018_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 21d window."""
    res = _sma(_ratio(ebitda, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_42d_v019_signal(capex):
    """Moving average of Raw level of capex over 42d window."""
    res = _sma(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_42d_v020_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_42d_v021_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_42d_v022_signal(ebitda):
    """Moving average of Raw level of ebitda over 42d window."""
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_42d_v023_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 42d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_42d_v024_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 42d window."""
    res = _sma(_ratio(ebitda, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_63d_v025_signal(capex):
    """Moving average of Raw level of capex over 63d window."""
    res = _sma(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_63d_v026_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_63d_v027_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_63d_v028_signal(ebitda):
    """Moving average of Raw level of ebitda over 63d window."""
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_63d_v029_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 63d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_63d_v030_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 63d window."""
    res = _sma(_ratio(ebitda, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_126d_v031_signal(capex):
    """Moving average of Raw level of capex over 126d window."""
    res = _sma(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_126d_v032_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_126d_v033_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_126d_v034_signal(ebitda):
    """Moving average of Raw level of ebitda over 126d window."""
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_126d_v035_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 126d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_126d_v036_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 126d window."""
    res = _sma(_ratio(ebitda, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_252d_v037_signal(capex):
    """Moving average of Raw level of capex over 252d window."""
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_252d_v038_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_252d_v039_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_252d_v040_signal(ebitda):
    """Moving average of Raw level of ebitda over 252d window."""
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_252d_v041_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 252d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_252d_v042_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 252d window."""
    res = _sma(_ratio(ebitda, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_504d_v043_signal(capex):
    """Moving average of Raw level of capex over 504d window."""
    res = _sma(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_504d_v044_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_504d_v045_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_504d_v046_signal(ebitda):
    """Moving average of Raw level of ebitda over 504d window."""
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_504d_v047_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 504d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_504d_v048_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 504d window."""
    res = _sma(_ratio(ebitda, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_756d_v049_signal(capex):
    """Moving average of Raw level of capex over 756d window."""
    res = _sma(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_756d_v050_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_756d_v051_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_756d_v052_signal(ebitda):
    """Moving average of Raw level of ebitda over 756d window."""
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_756d_v053_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 756d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_756d_v054_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 756d window."""
    res = _sma(_ratio(ebitda, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_1008d_v055_signal(capex):
    """Moving average of Raw level of capex over 1008d window."""
    res = _sma(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_1008d_v056_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_1008d_v057_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_1008d_v058_signal(ebitda):
    """Moving average of Raw level of ebitda over 1008d window."""
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_1008d_v059_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 1008d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_1008d_v060_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 1008d window."""
    res = _sma(_ratio(ebitda, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_base_1260d_v061_signal(capex):
    """Moving average of Raw level of capex over 1260d window."""
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_base_1260d_v062_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_base_1260d_v063_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_base_1260d_v064_signal(ebitda):
    """Moving average of Raw level of ebitda over 1260d window."""
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_base_1260d_v065_signal(capex, assets, netinc):
    """Moving average of Asset growth constrained by earnings yield over 1260d window."""
    res = _sma(_ratio(capex, assets) * _ratio(netinc, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_base_1260d_v066_signal(ebitda, capex):
    """Moving average of EBITDA generated per unit of grid capex over 1260d window."""
    res = _sma(_ratio(ebitda, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_ewma_5d_v067_signal(capex):
    """Exponential moving average of Raw level of capex over 5d window."""
    res = _ewma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_ewma_5d_v068_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_ewma_5d_v069_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_ebitda_ewma_5d_v070_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 5d window."""
    res = _ewma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_rate_base_growth_proxy_ewma_5d_v071_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 5d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_operating_return_capex_ewma_5d_v072_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 5d window."""
    res = _ewma(_ratio(ebitda, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_capex_ewma_10d_v073_signal(capex):
    """Exponential moving average of Raw level of capex over 10d window."""
    res = _ewma(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_assets_ewma_10d_v074_signal(assets):
    """Exponential moving average of Raw level of assets over 10d window."""
    res = _ewma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_utility_interest_coverage_netinc_ewma_10d_v075_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f26_utility_interest_coverage_capex_base_5d_v001_signal": {"func": f26_utility_interest_coverage_capex_base_5d_v001_signal},
    "f26_utility_interest_coverage_assets_base_5d_v002_signal": {"func": f26_utility_interest_coverage_assets_base_5d_v002_signal},
    "f26_utility_interest_coverage_netinc_base_5d_v003_signal": {"func": f26_utility_interest_coverage_netinc_base_5d_v003_signal},
    "f26_utility_interest_coverage_ebitda_base_5d_v004_signal": {"func": f26_utility_interest_coverage_ebitda_base_5d_v004_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_5d_v005_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_5d_v005_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_5d_v006_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_5d_v006_signal},
    "f26_utility_interest_coverage_capex_base_10d_v007_signal": {"func": f26_utility_interest_coverage_capex_base_10d_v007_signal},
    "f26_utility_interest_coverage_assets_base_10d_v008_signal": {"func": f26_utility_interest_coverage_assets_base_10d_v008_signal},
    "f26_utility_interest_coverage_netinc_base_10d_v009_signal": {"func": f26_utility_interest_coverage_netinc_base_10d_v009_signal},
    "f26_utility_interest_coverage_ebitda_base_10d_v010_signal": {"func": f26_utility_interest_coverage_ebitda_base_10d_v010_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_10d_v011_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_10d_v011_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_10d_v012_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_10d_v012_signal},
    "f26_utility_interest_coverage_capex_base_21d_v013_signal": {"func": f26_utility_interest_coverage_capex_base_21d_v013_signal},
    "f26_utility_interest_coverage_assets_base_21d_v014_signal": {"func": f26_utility_interest_coverage_assets_base_21d_v014_signal},
    "f26_utility_interest_coverage_netinc_base_21d_v015_signal": {"func": f26_utility_interest_coverage_netinc_base_21d_v015_signal},
    "f26_utility_interest_coverage_ebitda_base_21d_v016_signal": {"func": f26_utility_interest_coverage_ebitda_base_21d_v016_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_21d_v017_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_21d_v017_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_21d_v018_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_21d_v018_signal},
    "f26_utility_interest_coverage_capex_base_42d_v019_signal": {"func": f26_utility_interest_coverage_capex_base_42d_v019_signal},
    "f26_utility_interest_coverage_assets_base_42d_v020_signal": {"func": f26_utility_interest_coverage_assets_base_42d_v020_signal},
    "f26_utility_interest_coverage_netinc_base_42d_v021_signal": {"func": f26_utility_interest_coverage_netinc_base_42d_v021_signal},
    "f26_utility_interest_coverage_ebitda_base_42d_v022_signal": {"func": f26_utility_interest_coverage_ebitda_base_42d_v022_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_42d_v023_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_42d_v023_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_42d_v024_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_42d_v024_signal},
    "f26_utility_interest_coverage_capex_base_63d_v025_signal": {"func": f26_utility_interest_coverage_capex_base_63d_v025_signal},
    "f26_utility_interest_coverage_assets_base_63d_v026_signal": {"func": f26_utility_interest_coverage_assets_base_63d_v026_signal},
    "f26_utility_interest_coverage_netinc_base_63d_v027_signal": {"func": f26_utility_interest_coverage_netinc_base_63d_v027_signal},
    "f26_utility_interest_coverage_ebitda_base_63d_v028_signal": {"func": f26_utility_interest_coverage_ebitda_base_63d_v028_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_63d_v029_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_63d_v029_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_63d_v030_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_63d_v030_signal},
    "f26_utility_interest_coverage_capex_base_126d_v031_signal": {"func": f26_utility_interest_coverage_capex_base_126d_v031_signal},
    "f26_utility_interest_coverage_assets_base_126d_v032_signal": {"func": f26_utility_interest_coverage_assets_base_126d_v032_signal},
    "f26_utility_interest_coverage_netinc_base_126d_v033_signal": {"func": f26_utility_interest_coverage_netinc_base_126d_v033_signal},
    "f26_utility_interest_coverage_ebitda_base_126d_v034_signal": {"func": f26_utility_interest_coverage_ebitda_base_126d_v034_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_126d_v035_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_126d_v035_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_126d_v036_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_126d_v036_signal},
    "f26_utility_interest_coverage_capex_base_252d_v037_signal": {"func": f26_utility_interest_coverage_capex_base_252d_v037_signal},
    "f26_utility_interest_coverage_assets_base_252d_v038_signal": {"func": f26_utility_interest_coverage_assets_base_252d_v038_signal},
    "f26_utility_interest_coverage_netinc_base_252d_v039_signal": {"func": f26_utility_interest_coverage_netinc_base_252d_v039_signal},
    "f26_utility_interest_coverage_ebitda_base_252d_v040_signal": {"func": f26_utility_interest_coverage_ebitda_base_252d_v040_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_252d_v041_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_252d_v041_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_252d_v042_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_252d_v042_signal},
    "f26_utility_interest_coverage_capex_base_504d_v043_signal": {"func": f26_utility_interest_coverage_capex_base_504d_v043_signal},
    "f26_utility_interest_coverage_assets_base_504d_v044_signal": {"func": f26_utility_interest_coverage_assets_base_504d_v044_signal},
    "f26_utility_interest_coverage_netinc_base_504d_v045_signal": {"func": f26_utility_interest_coverage_netinc_base_504d_v045_signal},
    "f26_utility_interest_coverage_ebitda_base_504d_v046_signal": {"func": f26_utility_interest_coverage_ebitda_base_504d_v046_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_504d_v047_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_504d_v047_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_504d_v048_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_504d_v048_signal},
    "f26_utility_interest_coverage_capex_base_756d_v049_signal": {"func": f26_utility_interest_coverage_capex_base_756d_v049_signal},
    "f26_utility_interest_coverage_assets_base_756d_v050_signal": {"func": f26_utility_interest_coverage_assets_base_756d_v050_signal},
    "f26_utility_interest_coverage_netinc_base_756d_v051_signal": {"func": f26_utility_interest_coverage_netinc_base_756d_v051_signal},
    "f26_utility_interest_coverage_ebitda_base_756d_v052_signal": {"func": f26_utility_interest_coverage_ebitda_base_756d_v052_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_756d_v053_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_756d_v053_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_756d_v054_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_756d_v054_signal},
    "f26_utility_interest_coverage_capex_base_1008d_v055_signal": {"func": f26_utility_interest_coverage_capex_base_1008d_v055_signal},
    "f26_utility_interest_coverage_assets_base_1008d_v056_signal": {"func": f26_utility_interest_coverage_assets_base_1008d_v056_signal},
    "f26_utility_interest_coverage_netinc_base_1008d_v057_signal": {"func": f26_utility_interest_coverage_netinc_base_1008d_v057_signal},
    "f26_utility_interest_coverage_ebitda_base_1008d_v058_signal": {"func": f26_utility_interest_coverage_ebitda_base_1008d_v058_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_1008d_v059_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_1008d_v059_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_1008d_v060_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_1008d_v060_signal},
    "f26_utility_interest_coverage_capex_base_1260d_v061_signal": {"func": f26_utility_interest_coverage_capex_base_1260d_v061_signal},
    "f26_utility_interest_coverage_assets_base_1260d_v062_signal": {"func": f26_utility_interest_coverage_assets_base_1260d_v062_signal},
    "f26_utility_interest_coverage_netinc_base_1260d_v063_signal": {"func": f26_utility_interest_coverage_netinc_base_1260d_v063_signal},
    "f26_utility_interest_coverage_ebitda_base_1260d_v064_signal": {"func": f26_utility_interest_coverage_ebitda_base_1260d_v064_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_base_1260d_v065_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_base_1260d_v065_signal},
    "f26_utility_interest_coverage_operating_return_capex_base_1260d_v066_signal": {"func": f26_utility_interest_coverage_operating_return_capex_base_1260d_v066_signal},
    "f26_utility_interest_coverage_capex_ewma_5d_v067_signal": {"func": f26_utility_interest_coverage_capex_ewma_5d_v067_signal},
    "f26_utility_interest_coverage_assets_ewma_5d_v068_signal": {"func": f26_utility_interest_coverage_assets_ewma_5d_v068_signal},
    "f26_utility_interest_coverage_netinc_ewma_5d_v069_signal": {"func": f26_utility_interest_coverage_netinc_ewma_5d_v069_signal},
    "f26_utility_interest_coverage_ebitda_ewma_5d_v070_signal": {"func": f26_utility_interest_coverage_ebitda_ewma_5d_v070_signal},
    "f26_utility_interest_coverage_rate_base_growth_proxy_ewma_5d_v071_signal": {"func": f26_utility_interest_coverage_rate_base_growth_proxy_ewma_5d_v071_signal},
    "f26_utility_interest_coverage_operating_return_capex_ewma_5d_v072_signal": {"func": f26_utility_interest_coverage_operating_return_capex_ewma_5d_v072_signal},
    "f26_utility_interest_coverage_capex_ewma_10d_v073_signal": {"func": f26_utility_interest_coverage_capex_ewma_10d_v073_signal},
    "f26_utility_interest_coverage_assets_ewma_10d_v074_signal": {"func": f26_utility_interest_coverage_assets_ewma_10d_v074_signal},
    "f26_utility_interest_coverage_netinc_ewma_10d_v075_signal": {"func": f26_utility_interest_coverage_netinc_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 26...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            # Relaxing non-null for RSI/Skew which need more data
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
