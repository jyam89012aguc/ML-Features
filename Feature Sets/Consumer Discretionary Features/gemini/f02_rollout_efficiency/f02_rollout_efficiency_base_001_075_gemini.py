import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
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

def f02_rollout_efficiency_capex_base_5d_v001_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 5d window."""
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_5d_v002_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_5d_v003_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_5d_v004_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 5d window."""
    res = _sma(_ratio(netinc, capex + assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_10d_v005_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 10d window."""
    res = _sma(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_10d_v006_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_10d_v007_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_10d_v008_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 10d window."""
    res = _sma(_ratio(netinc, capex + assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_21d_v009_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 21d window."""
    res = _sma(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_21d_v010_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_21d_v011_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_21d_v012_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 21d window."""
    res = _sma(_ratio(netinc, capex + assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_42d_v013_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 42d window."""
    res = _sma(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_42d_v014_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_42d_v015_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_42d_v016_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 42d window."""
    res = _sma(_ratio(netinc, capex + assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_63d_v017_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 63d window."""
    res = _sma(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_63d_v018_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_63d_v019_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_63d_v020_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 63d window."""
    res = _sma(_ratio(netinc, capex + assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_126d_v021_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 126d window."""
    res = _sma(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_126d_v022_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_126d_v023_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_126d_v024_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 126d window."""
    res = _sma(_ratio(netinc, capex + assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_252d_v025_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 252d window."""
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_252d_v026_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_252d_v027_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_252d_v028_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 252d window."""
    res = _sma(_ratio(netinc, capex + assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_504d_v029_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 504d window."""
    res = _sma(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_504d_v030_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_504d_v031_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_504d_v032_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 504d window."""
    res = _sma(_ratio(netinc, capex + assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_756d_v033_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 756d window."""
    res = _sma(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_756d_v034_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_756d_v035_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_756d_v036_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 756d window."""
    res = _sma(_ratio(netinc, capex + assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_1008d_v037_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 1008d window."""
    res = _sma(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_1008d_v038_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_1008d_v039_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_1008d_v040_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 1008d window."""
    res = _sma(_ratio(netinc, capex + assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_base_1260d_v041_signal(capex):
    """Moving average to smooth noise of Raw level of capex over 1260d window."""
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_base_1260d_v042_signal(assets):
    """Moving average to smooth noise of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_base_1260d_v043_signal(netinc):
    """Moving average to smooth noise of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_base_1260d_v044_signal(netinc, capex, assets):
    """Moving average to smooth noise of Earnings return on rollout capital over 1260d window."""
    res = _sma(_ratio(netinc, capex + assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_5d_v045_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 5d window."""
    res = _z(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_5d_v046_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 5d window."""
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_5d_v047_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_z_5d_v048_signal(netinc, capex, assets):
    """Z-score for relative outlier detection of Earnings return on rollout capital over 5d window."""
    res = _z(_ratio(netinc, capex + assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_10d_v049_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 10d window."""
    res = _z(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_10d_v050_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 10d window."""
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_10d_v051_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_z_10d_v052_signal(netinc, capex, assets):
    """Z-score for relative outlier detection of Earnings return on rollout capital over 10d window."""
    res = _z(_ratio(netinc, capex + assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_21d_v053_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 21d window."""
    res = _z(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_21d_v054_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 21d window."""
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_21d_v055_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_z_21d_v056_signal(netinc, capex, assets):
    """Z-score for relative outlier detection of Earnings return on rollout capital over 21d window."""
    res = _z(_ratio(netinc, capex + assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_42d_v057_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 42d window."""
    res = _z(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_42d_v058_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 42d window."""
    res = _z(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_42d_v059_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 42d window."""
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_z_42d_v060_signal(netinc, capex, assets):
    """Z-score for relative outlier detection of Earnings return on rollout capital over 42d window."""
    res = _z(_ratio(netinc, capex + assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_63d_v061_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 63d window."""
    res = _z(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_63d_v062_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 63d window."""
    res = _z(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_63d_v063_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 63d window."""
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_z_63d_v064_signal(netinc, capex, assets):
    """Z-score for relative outlier detection of Earnings return on rollout capital over 63d window."""
    res = _z(_ratio(netinc, capex + assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_126d_v065_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 126d window."""
    res = _z(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_126d_v066_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 126d window."""
    res = _z(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_126d_v067_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 126d window."""
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_z_126d_v068_signal(netinc, capex, assets):
    """Z-score for relative outlier detection of Earnings return on rollout capital over 126d window."""
    res = _z(_ratio(netinc, capex + assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_252d_v069_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 252d window."""
    res = _z(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_252d_v070_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 252d window."""
    res = _z(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_252d_v071_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 252d window."""
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_moat_score_z_252d_v072_signal(netinc, capex, assets):
    """Z-score for relative outlier detection of Earnings return on rollout capital over 252d window."""
    res = _z(_ratio(netinc, capex + assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_capex_z_504d_v073_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 504d window."""
    res = _z(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_assets_z_504d_v074_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 504d window."""
    res = _z(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_rollout_efficiency_netinc_z_504d_v075_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 504d window."""
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f02_rollout_efficiency_capex_base_5d_v001_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_5d_v001_signal},    "f02_rollout_efficiency_assets_base_5d_v002_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_5d_v002_signal},    "f02_rollout_efficiency_netinc_base_5d_v003_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_5d_v003_signal},    "f02_rollout_efficiency_moat_score_base_5d_v004_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_5d_v004_signal},    "f02_rollout_efficiency_capex_base_10d_v005_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_10d_v005_signal},    "f02_rollout_efficiency_assets_base_10d_v006_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_10d_v006_signal},    "f02_rollout_efficiency_netinc_base_10d_v007_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_10d_v007_signal},    "f02_rollout_efficiency_moat_score_base_10d_v008_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_10d_v008_signal},    "f02_rollout_efficiency_capex_base_21d_v009_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_21d_v009_signal},    "f02_rollout_efficiency_assets_base_21d_v010_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_21d_v010_signal},    "f02_rollout_efficiency_netinc_base_21d_v011_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_21d_v011_signal},    "f02_rollout_efficiency_moat_score_base_21d_v012_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_21d_v012_signal},    "f02_rollout_efficiency_capex_base_42d_v013_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_42d_v013_signal},    "f02_rollout_efficiency_assets_base_42d_v014_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_42d_v014_signal},    "f02_rollout_efficiency_netinc_base_42d_v015_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_42d_v015_signal},    "f02_rollout_efficiency_moat_score_base_42d_v016_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_42d_v016_signal},    "f02_rollout_efficiency_capex_base_63d_v017_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_63d_v017_signal},    "f02_rollout_efficiency_assets_base_63d_v018_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_63d_v018_signal},    "f02_rollout_efficiency_netinc_base_63d_v019_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_63d_v019_signal},    "f02_rollout_efficiency_moat_score_base_63d_v020_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_63d_v020_signal},    "f02_rollout_efficiency_capex_base_126d_v021_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_126d_v021_signal},    "f02_rollout_efficiency_assets_base_126d_v022_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_126d_v022_signal},    "f02_rollout_efficiency_netinc_base_126d_v023_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_126d_v023_signal},    "f02_rollout_efficiency_moat_score_base_126d_v024_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_126d_v024_signal},    "f02_rollout_efficiency_capex_base_252d_v025_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_252d_v025_signal},    "f02_rollout_efficiency_assets_base_252d_v026_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_252d_v026_signal},    "f02_rollout_efficiency_netinc_base_252d_v027_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_252d_v027_signal},    "f02_rollout_efficiency_moat_score_base_252d_v028_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_252d_v028_signal},    "f02_rollout_efficiency_capex_base_504d_v029_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_504d_v029_signal},    "f02_rollout_efficiency_assets_base_504d_v030_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_504d_v030_signal},    "f02_rollout_efficiency_netinc_base_504d_v031_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_504d_v031_signal},    "f02_rollout_efficiency_moat_score_base_504d_v032_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_504d_v032_signal},    "f02_rollout_efficiency_capex_base_756d_v033_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_756d_v033_signal},    "f02_rollout_efficiency_assets_base_756d_v034_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_756d_v034_signal},    "f02_rollout_efficiency_netinc_base_756d_v035_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_756d_v035_signal},    "f02_rollout_efficiency_moat_score_base_756d_v036_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_756d_v036_signal},    "f02_rollout_efficiency_capex_base_1008d_v037_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_1008d_v037_signal},    "f02_rollout_efficiency_assets_base_1008d_v038_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_1008d_v038_signal},    "f02_rollout_efficiency_netinc_base_1008d_v039_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_1008d_v039_signal},    "f02_rollout_efficiency_moat_score_base_1008d_v040_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_1008d_v040_signal},    "f02_rollout_efficiency_capex_base_1260d_v041_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_base_1260d_v041_signal},    "f02_rollout_efficiency_assets_base_1260d_v042_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_base_1260d_v042_signal},    "f02_rollout_efficiency_netinc_base_1260d_v043_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_base_1260d_v043_signal},    "f02_rollout_efficiency_moat_score_base_1260d_v044_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_base_1260d_v044_signal},    "f02_rollout_efficiency_capex_z_5d_v045_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_5d_v045_signal},    "f02_rollout_efficiency_assets_z_5d_v046_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_5d_v046_signal},    "f02_rollout_efficiency_netinc_z_5d_v047_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_5d_v047_signal},    "f02_rollout_efficiency_moat_score_z_5d_v048_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_z_5d_v048_signal},    "f02_rollout_efficiency_capex_z_10d_v049_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_10d_v049_signal},    "f02_rollout_efficiency_assets_z_10d_v050_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_10d_v050_signal},    "f02_rollout_efficiency_netinc_z_10d_v051_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_10d_v051_signal},    "f02_rollout_efficiency_moat_score_z_10d_v052_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_z_10d_v052_signal},    "f02_rollout_efficiency_capex_z_21d_v053_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_21d_v053_signal},    "f02_rollout_efficiency_assets_z_21d_v054_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_21d_v054_signal},    "f02_rollout_efficiency_netinc_z_21d_v055_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_21d_v055_signal},    "f02_rollout_efficiency_moat_score_z_21d_v056_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_z_21d_v056_signal},    "f02_rollout_efficiency_capex_z_42d_v057_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_42d_v057_signal},    "f02_rollout_efficiency_assets_z_42d_v058_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_42d_v058_signal},    "f02_rollout_efficiency_netinc_z_42d_v059_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_42d_v059_signal},    "f02_rollout_efficiency_moat_score_z_42d_v060_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_z_42d_v060_signal},    "f02_rollout_efficiency_capex_z_63d_v061_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_63d_v061_signal},    "f02_rollout_efficiency_assets_z_63d_v062_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_63d_v062_signal},    "f02_rollout_efficiency_netinc_z_63d_v063_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_63d_v063_signal},    "f02_rollout_efficiency_moat_score_z_63d_v064_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_z_63d_v064_signal},    "f02_rollout_efficiency_capex_z_126d_v065_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_126d_v065_signal},    "f02_rollout_efficiency_assets_z_126d_v066_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_126d_v066_signal},    "f02_rollout_efficiency_netinc_z_126d_v067_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_126d_v067_signal},    "f02_rollout_efficiency_moat_score_z_126d_v068_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_z_126d_v068_signal},    "f02_rollout_efficiency_capex_z_252d_v069_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_252d_v069_signal},    "f02_rollout_efficiency_assets_z_252d_v070_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_252d_v070_signal},    "f02_rollout_efficiency_netinc_z_252d_v071_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_252d_v071_signal},    "f02_rollout_efficiency_moat_score_z_252d_v072_signal": {"inputs": [], "func": f02_rollout_efficiency_moat_score_z_252d_v072_signal},    "f02_rollout_efficiency_capex_z_504d_v073_signal": {"inputs": [], "func": f02_rollout_efficiency_capex_z_504d_v073_signal},    "f02_rollout_efficiency_assets_z_504d_v074_signal": {"inputs": [], "func": f02_rollout_efficiency_assets_z_504d_v074_signal},    "f02_rollout_efficiency_netinc_z_504d_v075_signal": {"inputs": [], "func": f02_rollout_efficiency_netinc_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 02...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
