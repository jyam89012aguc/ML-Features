import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
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

def f17_credit_resilience_netinc_slope_pct_5d_v001_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_5d_v002_signal(ebt):
    """Percentage slope for Raw level of ebt over 5d window."""
    res = _slope_pct(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_5d_v003_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_5d_v004_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 5d window."""
    res = _slope_pct(_ratio(ebt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_10d_v005_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_10d_v006_signal(ebt):
    """Percentage slope for Raw level of ebt over 10d window."""
    res = _slope_pct(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_10d_v007_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_10d_v008_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 10d window."""
    res = _slope_pct(_ratio(ebt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_21d_v009_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_21d_v010_signal(ebt):
    """Percentage slope for Raw level of ebt over 21d window."""
    res = _slope_pct(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_21d_v011_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_21d_v012_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 21d window."""
    res = _slope_pct(_ratio(ebt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_42d_v013_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_42d_v014_signal(ebt):
    """Percentage slope for Raw level of ebt over 42d window."""
    res = _slope_pct(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_42d_v015_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_42d_v016_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 42d window."""
    res = _slope_pct(_ratio(ebt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_63d_v017_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_63d_v018_signal(ebt):
    """Percentage slope for Raw level of ebt over 63d window."""
    res = _slope_pct(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_63d_v019_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_63d_v020_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 63d window."""
    res = _slope_pct(_ratio(ebt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_126d_v021_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_126d_v022_signal(ebt):
    """Percentage slope for Raw level of ebt over 126d window."""
    res = _slope_pct(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_126d_v023_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_126d_v024_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 126d window."""
    res = _slope_pct(_ratio(ebt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_252d_v025_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_252d_v026_signal(ebt):
    """Percentage slope for Raw level of ebt over 252d window."""
    res = _slope_pct(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_252d_v027_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_252d_v028_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 252d window."""
    res = _slope_pct(_ratio(ebt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_504d_v029_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_504d_v030_signal(ebt):
    """Percentage slope for Raw level of ebt over 504d window."""
    res = _slope_pct(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_504d_v031_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_504d_v032_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 504d window."""
    res = _slope_pct(_ratio(ebt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_756d_v033_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_756d_v034_signal(ebt):
    """Percentage slope for Raw level of ebt over 756d window."""
    res = _slope_pct(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_756d_v035_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_756d_v036_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 756d window."""
    res = _slope_pct(_ratio(ebt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_1008d_v037_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_1008d_v038_signal(ebt):
    """Percentage slope for Raw level of ebt over 1008d window."""
    res = _slope_pct(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_1008d_v039_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_1008d_v040_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 1008d window."""
    res = _slope_pct(_ratio(ebt, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_pct_1260d_v041_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_pct_1260d_v042_signal(ebt):
    """Percentage slope for Raw level of ebt over 1260d window."""
    res = _slope_pct(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_pct_1260d_v043_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_pct_1260d_v044_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 1260d window."""
    res = _slope_pct(_ratio(ebt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_5d_v045_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_5d_v046_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 5d window."""
    res = _jerk(ebt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_5d_v047_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_5d_v048_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 5d window."""
    res = _jerk(_ratio(ebt, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_10d_v049_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_10d_v050_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 10d window."""
    res = _jerk(ebt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_10d_v051_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_10d_v052_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 10d window."""
    res = _jerk(_ratio(ebt, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_21d_v053_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_21d_v054_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 21d window."""
    res = _jerk(ebt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_21d_v055_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_21d_v056_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 21d window."""
    res = _jerk(_ratio(ebt, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_42d_v057_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_42d_v058_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 42d window."""
    res = _jerk(ebt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_42d_v059_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_42d_v060_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 42d window."""
    res = _jerk(_ratio(ebt, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_63d_v061_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_63d_v062_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 63d window."""
    res = _jerk(ebt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_63d_v063_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_63d_v064_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 63d window."""
    res = _jerk(_ratio(ebt, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_126d_v065_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_126d_v066_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 126d window."""
    res = _jerk(ebt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_126d_v067_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_126d_v068_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 126d window."""
    res = _jerk(_ratio(ebt, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_252d_v069_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_252d_v070_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 252d window."""
    res = _jerk(ebt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_252d_v071_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_252d_v072_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 252d window."""
    res = _jerk(_ratio(ebt, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_504d_v073_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_504d_v074_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 504d window."""
    res = _jerk(ebt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_504d_v075_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_504d_v076_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 504d window."""
    res = _jerk(_ratio(ebt, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_756d_v077_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_756d_v078_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 756d window."""
    res = _jerk(ebt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_756d_v079_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_756d_v080_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 756d window."""
    res = _jerk(_ratio(ebt, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_1008d_v081_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_1008d_v082_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 1008d window."""
    res = _jerk(ebt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_1008d_v083_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_1008d_v084_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 1008d window."""
    res = _jerk(_ratio(ebt, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_jerk_1260d_v085_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_jerk_1260d_v086_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 1260d window."""
    res = _jerk(ebt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_jerk_1260d_v087_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_jerk_1260d_v088_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 1260d window."""
    res = _jerk(_ratio(ebt, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_5d_v089_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_5d_v090_signal(ebt):
    """Normalized slope change for Raw level of ebt over 5d window."""
    res = (_slope_pct(ebt, 5).diff(5) / _sma(ebt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_5d_v091_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_5d_v092_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 5d window."""
    res = (_slope_pct(_ratio(ebt, assets), 5).diff(5) / _sma(_ratio(ebt, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_10d_v093_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_10d_v094_signal(ebt):
    """Normalized slope change for Raw level of ebt over 10d window."""
    res = (_slope_pct(ebt, 10).diff(10) / _sma(ebt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_10d_v095_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_10d_v096_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 10d window."""
    res = (_slope_pct(_ratio(ebt, assets), 10).diff(10) / _sma(_ratio(ebt, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_21d_v097_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_21d_v098_signal(ebt):
    """Normalized slope change for Raw level of ebt over 21d window."""
    res = (_slope_pct(ebt, 21).diff(21) / _sma(ebt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_21d_v099_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_21d_v100_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 21d window."""
    res = (_slope_pct(_ratio(ebt, assets), 21).diff(21) / _sma(_ratio(ebt, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_42d_v101_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_42d_v102_signal(ebt):
    """Normalized slope change for Raw level of ebt over 42d window."""
    res = (_slope_pct(ebt, 42).diff(42) / _sma(ebt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_42d_v103_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_42d_v104_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 42d window."""
    res = (_slope_pct(_ratio(ebt, assets), 42).diff(42) / _sma(_ratio(ebt, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_63d_v105_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_63d_v106_signal(ebt):
    """Normalized slope change for Raw level of ebt over 63d window."""
    res = (_slope_pct(ebt, 63).diff(63) / _sma(ebt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_63d_v107_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_63d_v108_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 63d window."""
    res = (_slope_pct(_ratio(ebt, assets), 63).diff(63) / _sma(_ratio(ebt, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_126d_v109_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_126d_v110_signal(ebt):
    """Normalized slope change for Raw level of ebt over 126d window."""
    res = (_slope_pct(ebt, 126).diff(126) / _sma(ebt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_126d_v111_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_126d_v112_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 126d window."""
    res = (_slope_pct(_ratio(ebt, assets), 126).diff(126) / _sma(_ratio(ebt, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_252d_v113_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_252d_v114_signal(ebt):
    """Normalized slope change for Raw level of ebt over 252d window."""
    res = (_slope_pct(ebt, 252).diff(252) / _sma(ebt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_252d_v115_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_252d_v116_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 252d window."""
    res = (_slope_pct(_ratio(ebt, assets), 252).diff(252) / _sma(_ratio(ebt, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_504d_v117_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_504d_v118_signal(ebt):
    """Normalized slope change for Raw level of ebt over 504d window."""
    res = (_slope_pct(ebt, 504).diff(504) / _sma(ebt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_504d_v119_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_504d_v120_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 504d window."""
    res = (_slope_pct(_ratio(ebt, assets), 504).diff(504) / _sma(_ratio(ebt, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_756d_v121_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_756d_v122_signal(ebt):
    """Normalized slope change for Raw level of ebt over 756d window."""
    res = (_slope_pct(ebt, 756).diff(756) / _sma(ebt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_756d_v123_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_756d_v124_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 756d window."""
    res = (_slope_pct(_ratio(ebt, assets), 756).diff(756) / _sma(_ratio(ebt, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_1008d_v125_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_1008d_v126_signal(ebt):
    """Normalized slope change for Raw level of ebt over 1008d window."""
    res = (_slope_pct(ebt, 1008).diff(1008) / _sma(ebt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_1008d_v127_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_1008d_v128_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 1008d window."""
    res = (_slope_pct(_ratio(ebt, assets), 1008).diff(1008) / _sma(_ratio(ebt, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_slope_diff_norm_1260d_v129_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_slope_diff_norm_1260d_v130_signal(ebt):
    """Normalized slope change for Raw level of ebt over 1260d window."""
    res = (_slope_pct(ebt, 1260).diff(1260) / _sma(ebt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_slope_diff_norm_1260d_v131_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_slope_diff_norm_1260d_v132_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 1260d window."""
    res = (_slope_pct(_ratio(ebt, assets), 1260).diff(1260) / _sma(_ratio(ebt, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_mom_z_5d_v133_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_mom_z_5d_v134_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 5d window."""
    res = _z(_slope_pct(ebt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_mom_z_5d_v135_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_mom_z_5d_v136_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 5d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_mom_z_10d_v137_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_mom_z_10d_v138_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 10d window."""
    res = _z(_slope_pct(ebt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_mom_z_10d_v139_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_mom_z_10d_v140_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 10d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_mom_z_21d_v141_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_mom_z_21d_v142_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 21d window."""
    res = _z(_slope_pct(ebt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_mom_z_21d_v143_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_mom_z_21d_v144_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 21d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_mom_z_42d_v145_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_mom_z_42d_v146_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 42d window."""
    res = _z(_slope_pct(ebt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_mom_z_42d_v147_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_mom_z_42d_v148_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 42d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_mom_z_63d_v149_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_mom_z_63d_v150_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 63d window."""
    res = _z(_slope_pct(ebt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f17_credit_resilience_netinc_slope_pct_5d_v001_signal": {"func": f17_credit_resilience_netinc_slope_pct_5d_v001_signal},
    "f17_credit_resilience_ebt_slope_pct_5d_v002_signal": {"func": f17_credit_resilience_ebt_slope_pct_5d_v002_signal},
    "f17_credit_resilience_assets_slope_pct_5d_v003_signal": {"func": f17_credit_resilience_assets_slope_pct_5d_v003_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_5d_v004_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_5d_v004_signal},
    "f17_credit_resilience_netinc_slope_pct_10d_v005_signal": {"func": f17_credit_resilience_netinc_slope_pct_10d_v005_signal},
    "f17_credit_resilience_ebt_slope_pct_10d_v006_signal": {"func": f17_credit_resilience_ebt_slope_pct_10d_v006_signal},
    "f17_credit_resilience_assets_slope_pct_10d_v007_signal": {"func": f17_credit_resilience_assets_slope_pct_10d_v007_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_10d_v008_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_10d_v008_signal},
    "f17_credit_resilience_netinc_slope_pct_21d_v009_signal": {"func": f17_credit_resilience_netinc_slope_pct_21d_v009_signal},
    "f17_credit_resilience_ebt_slope_pct_21d_v010_signal": {"func": f17_credit_resilience_ebt_slope_pct_21d_v010_signal},
    "f17_credit_resilience_assets_slope_pct_21d_v011_signal": {"func": f17_credit_resilience_assets_slope_pct_21d_v011_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_21d_v012_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_21d_v012_signal},
    "f17_credit_resilience_netinc_slope_pct_42d_v013_signal": {"func": f17_credit_resilience_netinc_slope_pct_42d_v013_signal},
    "f17_credit_resilience_ebt_slope_pct_42d_v014_signal": {"func": f17_credit_resilience_ebt_slope_pct_42d_v014_signal},
    "f17_credit_resilience_assets_slope_pct_42d_v015_signal": {"func": f17_credit_resilience_assets_slope_pct_42d_v015_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_42d_v016_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_42d_v016_signal},
    "f17_credit_resilience_netinc_slope_pct_63d_v017_signal": {"func": f17_credit_resilience_netinc_slope_pct_63d_v017_signal},
    "f17_credit_resilience_ebt_slope_pct_63d_v018_signal": {"func": f17_credit_resilience_ebt_slope_pct_63d_v018_signal},
    "f17_credit_resilience_assets_slope_pct_63d_v019_signal": {"func": f17_credit_resilience_assets_slope_pct_63d_v019_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_63d_v020_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_63d_v020_signal},
    "f17_credit_resilience_netinc_slope_pct_126d_v021_signal": {"func": f17_credit_resilience_netinc_slope_pct_126d_v021_signal},
    "f17_credit_resilience_ebt_slope_pct_126d_v022_signal": {"func": f17_credit_resilience_ebt_slope_pct_126d_v022_signal},
    "f17_credit_resilience_assets_slope_pct_126d_v023_signal": {"func": f17_credit_resilience_assets_slope_pct_126d_v023_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_126d_v024_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_126d_v024_signal},
    "f17_credit_resilience_netinc_slope_pct_252d_v025_signal": {"func": f17_credit_resilience_netinc_slope_pct_252d_v025_signal},
    "f17_credit_resilience_ebt_slope_pct_252d_v026_signal": {"func": f17_credit_resilience_ebt_slope_pct_252d_v026_signal},
    "f17_credit_resilience_assets_slope_pct_252d_v027_signal": {"func": f17_credit_resilience_assets_slope_pct_252d_v027_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_252d_v028_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_252d_v028_signal},
    "f17_credit_resilience_netinc_slope_pct_504d_v029_signal": {"func": f17_credit_resilience_netinc_slope_pct_504d_v029_signal},
    "f17_credit_resilience_ebt_slope_pct_504d_v030_signal": {"func": f17_credit_resilience_ebt_slope_pct_504d_v030_signal},
    "f17_credit_resilience_assets_slope_pct_504d_v031_signal": {"func": f17_credit_resilience_assets_slope_pct_504d_v031_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_504d_v032_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_504d_v032_signal},
    "f17_credit_resilience_netinc_slope_pct_756d_v033_signal": {"func": f17_credit_resilience_netinc_slope_pct_756d_v033_signal},
    "f17_credit_resilience_ebt_slope_pct_756d_v034_signal": {"func": f17_credit_resilience_ebt_slope_pct_756d_v034_signal},
    "f17_credit_resilience_assets_slope_pct_756d_v035_signal": {"func": f17_credit_resilience_assets_slope_pct_756d_v035_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_756d_v036_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_756d_v036_signal},
    "f17_credit_resilience_netinc_slope_pct_1008d_v037_signal": {"func": f17_credit_resilience_netinc_slope_pct_1008d_v037_signal},
    "f17_credit_resilience_ebt_slope_pct_1008d_v038_signal": {"func": f17_credit_resilience_ebt_slope_pct_1008d_v038_signal},
    "f17_credit_resilience_assets_slope_pct_1008d_v039_signal": {"func": f17_credit_resilience_assets_slope_pct_1008d_v039_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_1008d_v040_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_1008d_v040_signal},
    "f17_credit_resilience_netinc_slope_pct_1260d_v041_signal": {"func": f17_credit_resilience_netinc_slope_pct_1260d_v041_signal},
    "f17_credit_resilience_ebt_slope_pct_1260d_v042_signal": {"func": f17_credit_resilience_ebt_slope_pct_1260d_v042_signal},
    "f17_credit_resilience_assets_slope_pct_1260d_v043_signal": {"func": f17_credit_resilience_assets_slope_pct_1260d_v043_signal},
    "f17_credit_resilience_pretax_margin_slope_pct_1260d_v044_signal": {"func": f17_credit_resilience_pretax_margin_slope_pct_1260d_v044_signal},
    "f17_credit_resilience_netinc_jerk_5d_v045_signal": {"func": f17_credit_resilience_netinc_jerk_5d_v045_signal},
    "f17_credit_resilience_ebt_jerk_5d_v046_signal": {"func": f17_credit_resilience_ebt_jerk_5d_v046_signal},
    "f17_credit_resilience_assets_jerk_5d_v047_signal": {"func": f17_credit_resilience_assets_jerk_5d_v047_signal},
    "f17_credit_resilience_pretax_margin_jerk_5d_v048_signal": {"func": f17_credit_resilience_pretax_margin_jerk_5d_v048_signal},
    "f17_credit_resilience_netinc_jerk_10d_v049_signal": {"func": f17_credit_resilience_netinc_jerk_10d_v049_signal},
    "f17_credit_resilience_ebt_jerk_10d_v050_signal": {"func": f17_credit_resilience_ebt_jerk_10d_v050_signal},
    "f17_credit_resilience_assets_jerk_10d_v051_signal": {"func": f17_credit_resilience_assets_jerk_10d_v051_signal},
    "f17_credit_resilience_pretax_margin_jerk_10d_v052_signal": {"func": f17_credit_resilience_pretax_margin_jerk_10d_v052_signal},
    "f17_credit_resilience_netinc_jerk_21d_v053_signal": {"func": f17_credit_resilience_netinc_jerk_21d_v053_signal},
    "f17_credit_resilience_ebt_jerk_21d_v054_signal": {"func": f17_credit_resilience_ebt_jerk_21d_v054_signal},
    "f17_credit_resilience_assets_jerk_21d_v055_signal": {"func": f17_credit_resilience_assets_jerk_21d_v055_signal},
    "f17_credit_resilience_pretax_margin_jerk_21d_v056_signal": {"func": f17_credit_resilience_pretax_margin_jerk_21d_v056_signal},
    "f17_credit_resilience_netinc_jerk_42d_v057_signal": {"func": f17_credit_resilience_netinc_jerk_42d_v057_signal},
    "f17_credit_resilience_ebt_jerk_42d_v058_signal": {"func": f17_credit_resilience_ebt_jerk_42d_v058_signal},
    "f17_credit_resilience_assets_jerk_42d_v059_signal": {"func": f17_credit_resilience_assets_jerk_42d_v059_signal},
    "f17_credit_resilience_pretax_margin_jerk_42d_v060_signal": {"func": f17_credit_resilience_pretax_margin_jerk_42d_v060_signal},
    "f17_credit_resilience_netinc_jerk_63d_v061_signal": {"func": f17_credit_resilience_netinc_jerk_63d_v061_signal},
    "f17_credit_resilience_ebt_jerk_63d_v062_signal": {"func": f17_credit_resilience_ebt_jerk_63d_v062_signal},
    "f17_credit_resilience_assets_jerk_63d_v063_signal": {"func": f17_credit_resilience_assets_jerk_63d_v063_signal},
    "f17_credit_resilience_pretax_margin_jerk_63d_v064_signal": {"func": f17_credit_resilience_pretax_margin_jerk_63d_v064_signal},
    "f17_credit_resilience_netinc_jerk_126d_v065_signal": {"func": f17_credit_resilience_netinc_jerk_126d_v065_signal},
    "f17_credit_resilience_ebt_jerk_126d_v066_signal": {"func": f17_credit_resilience_ebt_jerk_126d_v066_signal},
    "f17_credit_resilience_assets_jerk_126d_v067_signal": {"func": f17_credit_resilience_assets_jerk_126d_v067_signal},
    "f17_credit_resilience_pretax_margin_jerk_126d_v068_signal": {"func": f17_credit_resilience_pretax_margin_jerk_126d_v068_signal},
    "f17_credit_resilience_netinc_jerk_252d_v069_signal": {"func": f17_credit_resilience_netinc_jerk_252d_v069_signal},
    "f17_credit_resilience_ebt_jerk_252d_v070_signal": {"func": f17_credit_resilience_ebt_jerk_252d_v070_signal},
    "f17_credit_resilience_assets_jerk_252d_v071_signal": {"func": f17_credit_resilience_assets_jerk_252d_v071_signal},
    "f17_credit_resilience_pretax_margin_jerk_252d_v072_signal": {"func": f17_credit_resilience_pretax_margin_jerk_252d_v072_signal},
    "f17_credit_resilience_netinc_jerk_504d_v073_signal": {"func": f17_credit_resilience_netinc_jerk_504d_v073_signal},
    "f17_credit_resilience_ebt_jerk_504d_v074_signal": {"func": f17_credit_resilience_ebt_jerk_504d_v074_signal},
    "f17_credit_resilience_assets_jerk_504d_v075_signal": {"func": f17_credit_resilience_assets_jerk_504d_v075_signal},
    "f17_credit_resilience_pretax_margin_jerk_504d_v076_signal": {"func": f17_credit_resilience_pretax_margin_jerk_504d_v076_signal},
    "f17_credit_resilience_netinc_jerk_756d_v077_signal": {"func": f17_credit_resilience_netinc_jerk_756d_v077_signal},
    "f17_credit_resilience_ebt_jerk_756d_v078_signal": {"func": f17_credit_resilience_ebt_jerk_756d_v078_signal},
    "f17_credit_resilience_assets_jerk_756d_v079_signal": {"func": f17_credit_resilience_assets_jerk_756d_v079_signal},
    "f17_credit_resilience_pretax_margin_jerk_756d_v080_signal": {"func": f17_credit_resilience_pretax_margin_jerk_756d_v080_signal},
    "f17_credit_resilience_netinc_jerk_1008d_v081_signal": {"func": f17_credit_resilience_netinc_jerk_1008d_v081_signal},
    "f17_credit_resilience_ebt_jerk_1008d_v082_signal": {"func": f17_credit_resilience_ebt_jerk_1008d_v082_signal},
    "f17_credit_resilience_assets_jerk_1008d_v083_signal": {"func": f17_credit_resilience_assets_jerk_1008d_v083_signal},
    "f17_credit_resilience_pretax_margin_jerk_1008d_v084_signal": {"func": f17_credit_resilience_pretax_margin_jerk_1008d_v084_signal},
    "f17_credit_resilience_netinc_jerk_1260d_v085_signal": {"func": f17_credit_resilience_netinc_jerk_1260d_v085_signal},
    "f17_credit_resilience_ebt_jerk_1260d_v086_signal": {"func": f17_credit_resilience_ebt_jerk_1260d_v086_signal},
    "f17_credit_resilience_assets_jerk_1260d_v087_signal": {"func": f17_credit_resilience_assets_jerk_1260d_v087_signal},
    "f17_credit_resilience_pretax_margin_jerk_1260d_v088_signal": {"func": f17_credit_resilience_pretax_margin_jerk_1260d_v088_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_5d_v089_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_5d_v089_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_5d_v090_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_5d_v090_signal},
    "f17_credit_resilience_assets_slope_diff_norm_5d_v091_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_5d_v091_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_5d_v092_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_5d_v092_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_10d_v093_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_10d_v093_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_10d_v094_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_10d_v094_signal},
    "f17_credit_resilience_assets_slope_diff_norm_10d_v095_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_10d_v095_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_10d_v096_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_10d_v096_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_21d_v097_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_21d_v097_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_21d_v098_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_21d_v098_signal},
    "f17_credit_resilience_assets_slope_diff_norm_21d_v099_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_21d_v099_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_21d_v100_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_21d_v100_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_42d_v101_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_42d_v101_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_42d_v102_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_42d_v102_signal},
    "f17_credit_resilience_assets_slope_diff_norm_42d_v103_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_42d_v103_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_42d_v104_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_42d_v104_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_63d_v105_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_63d_v105_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_63d_v106_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_63d_v106_signal},
    "f17_credit_resilience_assets_slope_diff_norm_63d_v107_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_63d_v107_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_63d_v108_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_63d_v108_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_126d_v109_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_126d_v109_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_126d_v110_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_126d_v110_signal},
    "f17_credit_resilience_assets_slope_diff_norm_126d_v111_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_126d_v111_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_126d_v112_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_126d_v112_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_252d_v113_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_252d_v113_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_252d_v114_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_252d_v114_signal},
    "f17_credit_resilience_assets_slope_diff_norm_252d_v115_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_252d_v115_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_252d_v116_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_252d_v116_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_504d_v117_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_504d_v117_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_504d_v118_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_504d_v118_signal},
    "f17_credit_resilience_assets_slope_diff_norm_504d_v119_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_504d_v119_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_504d_v120_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_504d_v120_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_756d_v121_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_756d_v121_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_756d_v122_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_756d_v122_signal},
    "f17_credit_resilience_assets_slope_diff_norm_756d_v123_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_756d_v123_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_756d_v124_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_756d_v124_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_1008d_v125_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_1008d_v125_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_1008d_v126_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_1008d_v126_signal},
    "f17_credit_resilience_assets_slope_diff_norm_1008d_v127_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_1008d_v127_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_1008d_v128_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_1008d_v128_signal},
    "f17_credit_resilience_netinc_slope_diff_norm_1260d_v129_signal": {"func": f17_credit_resilience_netinc_slope_diff_norm_1260d_v129_signal},
    "f17_credit_resilience_ebt_slope_diff_norm_1260d_v130_signal": {"func": f17_credit_resilience_ebt_slope_diff_norm_1260d_v130_signal},
    "f17_credit_resilience_assets_slope_diff_norm_1260d_v131_signal": {"func": f17_credit_resilience_assets_slope_diff_norm_1260d_v131_signal},
    "f17_credit_resilience_pretax_margin_slope_diff_norm_1260d_v132_signal": {"func": f17_credit_resilience_pretax_margin_slope_diff_norm_1260d_v132_signal},
    "f17_credit_resilience_netinc_mom_z_5d_v133_signal": {"func": f17_credit_resilience_netinc_mom_z_5d_v133_signal},
    "f17_credit_resilience_ebt_mom_z_5d_v134_signal": {"func": f17_credit_resilience_ebt_mom_z_5d_v134_signal},
    "f17_credit_resilience_assets_mom_z_5d_v135_signal": {"func": f17_credit_resilience_assets_mom_z_5d_v135_signal},
    "f17_credit_resilience_pretax_margin_mom_z_5d_v136_signal": {"func": f17_credit_resilience_pretax_margin_mom_z_5d_v136_signal},
    "f17_credit_resilience_netinc_mom_z_10d_v137_signal": {"func": f17_credit_resilience_netinc_mom_z_10d_v137_signal},
    "f17_credit_resilience_ebt_mom_z_10d_v138_signal": {"func": f17_credit_resilience_ebt_mom_z_10d_v138_signal},
    "f17_credit_resilience_assets_mom_z_10d_v139_signal": {"func": f17_credit_resilience_assets_mom_z_10d_v139_signal},
    "f17_credit_resilience_pretax_margin_mom_z_10d_v140_signal": {"func": f17_credit_resilience_pretax_margin_mom_z_10d_v140_signal},
    "f17_credit_resilience_netinc_mom_z_21d_v141_signal": {"func": f17_credit_resilience_netinc_mom_z_21d_v141_signal},
    "f17_credit_resilience_ebt_mom_z_21d_v142_signal": {"func": f17_credit_resilience_ebt_mom_z_21d_v142_signal},
    "f17_credit_resilience_assets_mom_z_21d_v143_signal": {"func": f17_credit_resilience_assets_mom_z_21d_v143_signal},
    "f17_credit_resilience_pretax_margin_mom_z_21d_v144_signal": {"func": f17_credit_resilience_pretax_margin_mom_z_21d_v144_signal},
    "f17_credit_resilience_netinc_mom_z_42d_v145_signal": {"func": f17_credit_resilience_netinc_mom_z_42d_v145_signal},
    "f17_credit_resilience_ebt_mom_z_42d_v146_signal": {"func": f17_credit_resilience_ebt_mom_z_42d_v146_signal},
    "f17_credit_resilience_assets_mom_z_42d_v147_signal": {"func": f17_credit_resilience_assets_mom_z_42d_v147_signal},
    "f17_credit_resilience_pretax_margin_mom_z_42d_v148_signal": {"func": f17_credit_resilience_pretax_margin_mom_z_42d_v148_signal},
    "f17_credit_resilience_netinc_mom_z_63d_v149_signal": {"func": f17_credit_resilience_netinc_mom_z_63d_v149_signal},
    "f17_credit_resilience_ebt_mom_z_63d_v150_signal": {"func": f17_credit_resilience_ebt_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 17...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
