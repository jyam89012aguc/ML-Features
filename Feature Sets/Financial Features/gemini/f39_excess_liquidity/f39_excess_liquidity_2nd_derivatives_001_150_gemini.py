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

def f39_excess_liquidity_cashneq_slope_pct_5d_v001_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 5d window."""
    res = _slope_pct(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_5d_v002_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_5d_v003_signal(deposits):
    """Percentage slope for Raw level of deposits over 5d window."""
    res = _slope_pct(deposits, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_5d_v004_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 5d window."""
    res = _slope_pct(_ratio(cashneq, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_10d_v005_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 10d window."""
    res = _slope_pct(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_10d_v006_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_10d_v007_signal(deposits):
    """Percentage slope for Raw level of deposits over 10d window."""
    res = _slope_pct(deposits, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_10d_v008_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 10d window."""
    res = _slope_pct(_ratio(cashneq, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_21d_v009_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 21d window."""
    res = _slope_pct(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_21d_v010_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_21d_v011_signal(deposits):
    """Percentage slope for Raw level of deposits over 21d window."""
    res = _slope_pct(deposits, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_21d_v012_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 21d window."""
    res = _slope_pct(_ratio(cashneq, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_42d_v013_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 42d window."""
    res = _slope_pct(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_42d_v014_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_42d_v015_signal(deposits):
    """Percentage slope for Raw level of deposits over 42d window."""
    res = _slope_pct(deposits, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_42d_v016_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 42d window."""
    res = _slope_pct(_ratio(cashneq, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_63d_v017_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 63d window."""
    res = _slope_pct(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_63d_v018_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_63d_v019_signal(deposits):
    """Percentage slope for Raw level of deposits over 63d window."""
    res = _slope_pct(deposits, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_63d_v020_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 63d window."""
    res = _slope_pct(_ratio(cashneq, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_126d_v021_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 126d window."""
    res = _slope_pct(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_126d_v022_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_126d_v023_signal(deposits):
    """Percentage slope for Raw level of deposits over 126d window."""
    res = _slope_pct(deposits, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_126d_v024_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 126d window."""
    res = _slope_pct(_ratio(cashneq, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_252d_v025_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 252d window."""
    res = _slope_pct(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_252d_v026_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_252d_v027_signal(deposits):
    """Percentage slope for Raw level of deposits over 252d window."""
    res = _slope_pct(deposits, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_252d_v028_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 252d window."""
    res = _slope_pct(_ratio(cashneq, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_504d_v029_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 504d window."""
    res = _slope_pct(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_504d_v030_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_504d_v031_signal(deposits):
    """Percentage slope for Raw level of deposits over 504d window."""
    res = _slope_pct(deposits, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_504d_v032_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 504d window."""
    res = _slope_pct(_ratio(cashneq, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_756d_v033_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 756d window."""
    res = _slope_pct(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_756d_v034_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_756d_v035_signal(deposits):
    """Percentage slope for Raw level of deposits over 756d window."""
    res = _slope_pct(deposits, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_756d_v036_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 756d window."""
    res = _slope_pct(_ratio(cashneq, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_1008d_v037_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 1008d window."""
    res = _slope_pct(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_1008d_v038_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_1008d_v039_signal(deposits):
    """Percentage slope for Raw level of deposits over 1008d window."""
    res = _slope_pct(deposits, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_1008d_v040_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 1008d window."""
    res = _slope_pct(_ratio(cashneq, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_pct_1260d_v041_signal(cashneq):
    """Percentage slope for Raw level of cashneq over 1260d window."""
    res = _slope_pct(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_pct_1260d_v042_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_pct_1260d_v043_signal(deposits):
    """Percentage slope for Raw level of deposits over 1260d window."""
    res = _slope_pct(deposits, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_pct_1260d_v044_signal(cashneq, assets):
    """Percentage slope for Cash as % of assets over 1260d window."""
    res = _slope_pct(_ratio(cashneq, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_5d_v045_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 5d window."""
    res = _jerk(cashneq, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_5d_v046_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_5d_v047_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 5d window."""
    res = _jerk(deposits, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_5d_v048_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 5d window."""
    res = _jerk(_ratio(cashneq, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_10d_v049_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 10d window."""
    res = _jerk(cashneq, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_10d_v050_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_10d_v051_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 10d window."""
    res = _jerk(deposits, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_10d_v052_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 10d window."""
    res = _jerk(_ratio(cashneq, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_21d_v053_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 21d window."""
    res = _jerk(cashneq, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_21d_v054_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_21d_v055_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 21d window."""
    res = _jerk(deposits, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_21d_v056_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 21d window."""
    res = _jerk(_ratio(cashneq, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_42d_v057_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 42d window."""
    res = _jerk(cashneq, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_42d_v058_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_42d_v059_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 42d window."""
    res = _jerk(deposits, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_42d_v060_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 42d window."""
    res = _jerk(_ratio(cashneq, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_63d_v061_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 63d window."""
    res = _jerk(cashneq, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_63d_v062_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_63d_v063_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 63d window."""
    res = _jerk(deposits, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_63d_v064_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 63d window."""
    res = _jerk(_ratio(cashneq, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_126d_v065_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 126d window."""
    res = _jerk(cashneq, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_126d_v066_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_126d_v067_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 126d window."""
    res = _jerk(deposits, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_126d_v068_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 126d window."""
    res = _jerk(_ratio(cashneq, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_252d_v069_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 252d window."""
    res = _jerk(cashneq, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_252d_v070_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_252d_v071_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 252d window."""
    res = _jerk(deposits, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_252d_v072_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 252d window."""
    res = _jerk(_ratio(cashneq, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_504d_v073_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 504d window."""
    res = _jerk(cashneq, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_504d_v074_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_504d_v075_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 504d window."""
    res = _jerk(deposits, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_504d_v076_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 504d window."""
    res = _jerk(_ratio(cashneq, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_756d_v077_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 756d window."""
    res = _jerk(cashneq, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_756d_v078_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_756d_v079_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 756d window."""
    res = _jerk(deposits, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_756d_v080_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 756d window."""
    res = _jerk(_ratio(cashneq, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_1008d_v081_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 1008d window."""
    res = _jerk(cashneq, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_1008d_v082_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_1008d_v083_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 1008d window."""
    res = _jerk(deposits, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_1008d_v084_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 1008d window."""
    res = _jerk(_ratio(cashneq, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_jerk_1260d_v085_signal(cashneq):
    """Acceleration/Jerk for Raw level of cashneq over 1260d window."""
    res = _jerk(cashneq, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_jerk_1260d_v086_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_jerk_1260d_v087_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 1260d window."""
    res = _jerk(deposits, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_jerk_1260d_v088_signal(cashneq, assets):
    """Acceleration/Jerk for Cash as % of assets over 1260d window."""
    res = _jerk(_ratio(cashneq, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_5d_v089_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 5d window."""
    res = (_slope_pct(cashneq, 5).diff(5) / _sma(cashneq.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_5d_v090_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_5d_v091_signal(deposits):
    """Normalized slope change for Raw level of deposits over 5d window."""
    res = (_slope_pct(deposits, 5).diff(5) / _sma(deposits.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_5d_v092_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 5d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 5).diff(5) / _sma(_ratio(cashneq, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_10d_v093_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 10d window."""
    res = (_slope_pct(cashneq, 10).diff(10) / _sma(cashneq.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_10d_v094_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_10d_v095_signal(deposits):
    """Normalized slope change for Raw level of deposits over 10d window."""
    res = (_slope_pct(deposits, 10).diff(10) / _sma(deposits.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_10d_v096_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 10d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 10).diff(10) / _sma(_ratio(cashneq, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_21d_v097_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 21d window."""
    res = (_slope_pct(cashneq, 21).diff(21) / _sma(cashneq.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_21d_v098_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_21d_v099_signal(deposits):
    """Normalized slope change for Raw level of deposits over 21d window."""
    res = (_slope_pct(deposits, 21).diff(21) / _sma(deposits.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_21d_v100_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 21d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 21).diff(21) / _sma(_ratio(cashneq, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_42d_v101_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 42d window."""
    res = (_slope_pct(cashneq, 42).diff(42) / _sma(cashneq.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_42d_v102_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_42d_v103_signal(deposits):
    """Normalized slope change for Raw level of deposits over 42d window."""
    res = (_slope_pct(deposits, 42).diff(42) / _sma(deposits.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_42d_v104_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 42d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 42).diff(42) / _sma(_ratio(cashneq, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_63d_v105_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 63d window."""
    res = (_slope_pct(cashneq, 63).diff(63) / _sma(cashneq.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_63d_v106_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_63d_v107_signal(deposits):
    """Normalized slope change for Raw level of deposits over 63d window."""
    res = (_slope_pct(deposits, 63).diff(63) / _sma(deposits.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_63d_v108_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 63d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 63).diff(63) / _sma(_ratio(cashneq, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_126d_v109_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 126d window."""
    res = (_slope_pct(cashneq, 126).diff(126) / _sma(cashneq.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_126d_v110_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_126d_v111_signal(deposits):
    """Normalized slope change for Raw level of deposits over 126d window."""
    res = (_slope_pct(deposits, 126).diff(126) / _sma(deposits.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_126d_v112_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 126d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 126).diff(126) / _sma(_ratio(cashneq, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_252d_v113_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 252d window."""
    res = (_slope_pct(cashneq, 252).diff(252) / _sma(cashneq.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_252d_v114_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_252d_v115_signal(deposits):
    """Normalized slope change for Raw level of deposits over 252d window."""
    res = (_slope_pct(deposits, 252).diff(252) / _sma(deposits.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_252d_v116_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 252d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 252).diff(252) / _sma(_ratio(cashneq, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_504d_v117_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 504d window."""
    res = (_slope_pct(cashneq, 504).diff(504) / _sma(cashneq.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_504d_v118_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_504d_v119_signal(deposits):
    """Normalized slope change for Raw level of deposits over 504d window."""
    res = (_slope_pct(deposits, 504).diff(504) / _sma(deposits.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_504d_v120_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 504d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 504).diff(504) / _sma(_ratio(cashneq, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_756d_v121_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 756d window."""
    res = (_slope_pct(cashneq, 756).diff(756) / _sma(cashneq.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_756d_v122_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_756d_v123_signal(deposits):
    """Normalized slope change for Raw level of deposits over 756d window."""
    res = (_slope_pct(deposits, 756).diff(756) / _sma(deposits.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_756d_v124_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 756d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 756).diff(756) / _sma(_ratio(cashneq, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_1008d_v125_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 1008d window."""
    res = (_slope_pct(cashneq, 1008).diff(1008) / _sma(cashneq.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_1008d_v126_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_1008d_v127_signal(deposits):
    """Normalized slope change for Raw level of deposits over 1008d window."""
    res = (_slope_pct(deposits, 1008).diff(1008) / _sma(deposits.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_1008d_v128_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 1008d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 1008).diff(1008) / _sma(_ratio(cashneq, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_slope_diff_norm_1260d_v129_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 1260d window."""
    res = (_slope_pct(cashneq, 1260).diff(1260) / _sma(cashneq.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_slope_diff_norm_1260d_v130_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_slope_diff_norm_1260d_v131_signal(deposits):
    """Normalized slope change for Raw level of deposits over 1260d window."""
    res = (_slope_pct(deposits, 1260).diff(1260) / _sma(deposits.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_slope_diff_norm_1260d_v132_signal(cashneq, assets):
    """Normalized slope change for Cash as % of assets over 1260d window."""
    res = (_slope_pct(_ratio(cashneq, assets), 1260).diff(1260) / _sma(_ratio(cashneq, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_5d_v133_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 5d window."""
    res = _z(_slope_pct(cashneq, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_5d_v134_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_5d_v135_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 5d window."""
    res = _z(_slope_pct(deposits, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_5d_v136_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 5d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_10d_v137_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 10d window."""
    res = _z(_slope_pct(cashneq, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_10d_v138_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_10d_v139_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 10d window."""
    res = _z(_slope_pct(deposits, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_10d_v140_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 10d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_21d_v141_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 21d window."""
    res = _z(_slope_pct(cashneq, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_21d_v142_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_21d_v143_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 21d window."""
    res = _z(_slope_pct(deposits, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_21d_v144_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 21d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_42d_v145_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 42d window."""
    res = _z(_slope_pct(cashneq, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_42d_v146_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_42d_v147_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 42d window."""
    res = _z(_slope_pct(deposits, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_42d_v148_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 42d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_63d_v149_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 63d window."""
    res = _z(_slope_pct(cashneq, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_63d_v150_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f39_excess_liquidity_cashneq_slope_pct_5d_v001_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_5d_v001_signal},
    "f39_excess_liquidity_assets_slope_pct_5d_v002_signal": {"func": f39_excess_liquidity_assets_slope_pct_5d_v002_signal},
    "f39_excess_liquidity_deposits_slope_pct_5d_v003_signal": {"func": f39_excess_liquidity_deposits_slope_pct_5d_v003_signal},
    "f39_excess_liquidity_cash_density_slope_pct_5d_v004_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_5d_v004_signal},
    "f39_excess_liquidity_cashneq_slope_pct_10d_v005_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_10d_v005_signal},
    "f39_excess_liquidity_assets_slope_pct_10d_v006_signal": {"func": f39_excess_liquidity_assets_slope_pct_10d_v006_signal},
    "f39_excess_liquidity_deposits_slope_pct_10d_v007_signal": {"func": f39_excess_liquidity_deposits_slope_pct_10d_v007_signal},
    "f39_excess_liquidity_cash_density_slope_pct_10d_v008_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_10d_v008_signal},
    "f39_excess_liquidity_cashneq_slope_pct_21d_v009_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_21d_v009_signal},
    "f39_excess_liquidity_assets_slope_pct_21d_v010_signal": {"func": f39_excess_liquidity_assets_slope_pct_21d_v010_signal},
    "f39_excess_liquidity_deposits_slope_pct_21d_v011_signal": {"func": f39_excess_liquidity_deposits_slope_pct_21d_v011_signal},
    "f39_excess_liquidity_cash_density_slope_pct_21d_v012_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_21d_v012_signal},
    "f39_excess_liquidity_cashneq_slope_pct_42d_v013_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_42d_v013_signal},
    "f39_excess_liquidity_assets_slope_pct_42d_v014_signal": {"func": f39_excess_liquidity_assets_slope_pct_42d_v014_signal},
    "f39_excess_liquidity_deposits_slope_pct_42d_v015_signal": {"func": f39_excess_liquidity_deposits_slope_pct_42d_v015_signal},
    "f39_excess_liquidity_cash_density_slope_pct_42d_v016_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_42d_v016_signal},
    "f39_excess_liquidity_cashneq_slope_pct_63d_v017_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_63d_v017_signal},
    "f39_excess_liquidity_assets_slope_pct_63d_v018_signal": {"func": f39_excess_liquidity_assets_slope_pct_63d_v018_signal},
    "f39_excess_liquidity_deposits_slope_pct_63d_v019_signal": {"func": f39_excess_liquidity_deposits_slope_pct_63d_v019_signal},
    "f39_excess_liquidity_cash_density_slope_pct_63d_v020_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_63d_v020_signal},
    "f39_excess_liquidity_cashneq_slope_pct_126d_v021_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_126d_v021_signal},
    "f39_excess_liquidity_assets_slope_pct_126d_v022_signal": {"func": f39_excess_liquidity_assets_slope_pct_126d_v022_signal},
    "f39_excess_liquidity_deposits_slope_pct_126d_v023_signal": {"func": f39_excess_liquidity_deposits_slope_pct_126d_v023_signal},
    "f39_excess_liquidity_cash_density_slope_pct_126d_v024_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_126d_v024_signal},
    "f39_excess_liquidity_cashneq_slope_pct_252d_v025_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_252d_v025_signal},
    "f39_excess_liquidity_assets_slope_pct_252d_v026_signal": {"func": f39_excess_liquidity_assets_slope_pct_252d_v026_signal},
    "f39_excess_liquidity_deposits_slope_pct_252d_v027_signal": {"func": f39_excess_liquidity_deposits_slope_pct_252d_v027_signal},
    "f39_excess_liquidity_cash_density_slope_pct_252d_v028_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_252d_v028_signal},
    "f39_excess_liquidity_cashneq_slope_pct_504d_v029_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_504d_v029_signal},
    "f39_excess_liquidity_assets_slope_pct_504d_v030_signal": {"func": f39_excess_liquidity_assets_slope_pct_504d_v030_signal},
    "f39_excess_liquidity_deposits_slope_pct_504d_v031_signal": {"func": f39_excess_liquidity_deposits_slope_pct_504d_v031_signal},
    "f39_excess_liquidity_cash_density_slope_pct_504d_v032_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_504d_v032_signal},
    "f39_excess_liquidity_cashneq_slope_pct_756d_v033_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_756d_v033_signal},
    "f39_excess_liquidity_assets_slope_pct_756d_v034_signal": {"func": f39_excess_liquidity_assets_slope_pct_756d_v034_signal},
    "f39_excess_liquidity_deposits_slope_pct_756d_v035_signal": {"func": f39_excess_liquidity_deposits_slope_pct_756d_v035_signal},
    "f39_excess_liquidity_cash_density_slope_pct_756d_v036_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_756d_v036_signal},
    "f39_excess_liquidity_cashneq_slope_pct_1008d_v037_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_1008d_v037_signal},
    "f39_excess_liquidity_assets_slope_pct_1008d_v038_signal": {"func": f39_excess_liquidity_assets_slope_pct_1008d_v038_signal},
    "f39_excess_liquidity_deposits_slope_pct_1008d_v039_signal": {"func": f39_excess_liquidity_deposits_slope_pct_1008d_v039_signal},
    "f39_excess_liquidity_cash_density_slope_pct_1008d_v040_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_1008d_v040_signal},
    "f39_excess_liquidity_cashneq_slope_pct_1260d_v041_signal": {"func": f39_excess_liquidity_cashneq_slope_pct_1260d_v041_signal},
    "f39_excess_liquidity_assets_slope_pct_1260d_v042_signal": {"func": f39_excess_liquidity_assets_slope_pct_1260d_v042_signal},
    "f39_excess_liquidity_deposits_slope_pct_1260d_v043_signal": {"func": f39_excess_liquidity_deposits_slope_pct_1260d_v043_signal},
    "f39_excess_liquidity_cash_density_slope_pct_1260d_v044_signal": {"func": f39_excess_liquidity_cash_density_slope_pct_1260d_v044_signal},
    "f39_excess_liquidity_cashneq_jerk_5d_v045_signal": {"func": f39_excess_liquidity_cashneq_jerk_5d_v045_signal},
    "f39_excess_liquidity_assets_jerk_5d_v046_signal": {"func": f39_excess_liquidity_assets_jerk_5d_v046_signal},
    "f39_excess_liquidity_deposits_jerk_5d_v047_signal": {"func": f39_excess_liquidity_deposits_jerk_5d_v047_signal},
    "f39_excess_liquidity_cash_density_jerk_5d_v048_signal": {"func": f39_excess_liquidity_cash_density_jerk_5d_v048_signal},
    "f39_excess_liquidity_cashneq_jerk_10d_v049_signal": {"func": f39_excess_liquidity_cashneq_jerk_10d_v049_signal},
    "f39_excess_liquidity_assets_jerk_10d_v050_signal": {"func": f39_excess_liquidity_assets_jerk_10d_v050_signal},
    "f39_excess_liquidity_deposits_jerk_10d_v051_signal": {"func": f39_excess_liquidity_deposits_jerk_10d_v051_signal},
    "f39_excess_liquidity_cash_density_jerk_10d_v052_signal": {"func": f39_excess_liquidity_cash_density_jerk_10d_v052_signal},
    "f39_excess_liquidity_cashneq_jerk_21d_v053_signal": {"func": f39_excess_liquidity_cashneq_jerk_21d_v053_signal},
    "f39_excess_liquidity_assets_jerk_21d_v054_signal": {"func": f39_excess_liquidity_assets_jerk_21d_v054_signal},
    "f39_excess_liquidity_deposits_jerk_21d_v055_signal": {"func": f39_excess_liquidity_deposits_jerk_21d_v055_signal},
    "f39_excess_liquidity_cash_density_jerk_21d_v056_signal": {"func": f39_excess_liquidity_cash_density_jerk_21d_v056_signal},
    "f39_excess_liquidity_cashneq_jerk_42d_v057_signal": {"func": f39_excess_liquidity_cashneq_jerk_42d_v057_signal},
    "f39_excess_liquidity_assets_jerk_42d_v058_signal": {"func": f39_excess_liquidity_assets_jerk_42d_v058_signal},
    "f39_excess_liquidity_deposits_jerk_42d_v059_signal": {"func": f39_excess_liquidity_deposits_jerk_42d_v059_signal},
    "f39_excess_liquidity_cash_density_jerk_42d_v060_signal": {"func": f39_excess_liquidity_cash_density_jerk_42d_v060_signal},
    "f39_excess_liquidity_cashneq_jerk_63d_v061_signal": {"func": f39_excess_liquidity_cashneq_jerk_63d_v061_signal},
    "f39_excess_liquidity_assets_jerk_63d_v062_signal": {"func": f39_excess_liquidity_assets_jerk_63d_v062_signal},
    "f39_excess_liquidity_deposits_jerk_63d_v063_signal": {"func": f39_excess_liquidity_deposits_jerk_63d_v063_signal},
    "f39_excess_liquidity_cash_density_jerk_63d_v064_signal": {"func": f39_excess_liquidity_cash_density_jerk_63d_v064_signal},
    "f39_excess_liquidity_cashneq_jerk_126d_v065_signal": {"func": f39_excess_liquidity_cashneq_jerk_126d_v065_signal},
    "f39_excess_liquidity_assets_jerk_126d_v066_signal": {"func": f39_excess_liquidity_assets_jerk_126d_v066_signal},
    "f39_excess_liquidity_deposits_jerk_126d_v067_signal": {"func": f39_excess_liquidity_deposits_jerk_126d_v067_signal},
    "f39_excess_liquidity_cash_density_jerk_126d_v068_signal": {"func": f39_excess_liquidity_cash_density_jerk_126d_v068_signal},
    "f39_excess_liquidity_cashneq_jerk_252d_v069_signal": {"func": f39_excess_liquidity_cashneq_jerk_252d_v069_signal},
    "f39_excess_liquidity_assets_jerk_252d_v070_signal": {"func": f39_excess_liquidity_assets_jerk_252d_v070_signal},
    "f39_excess_liquidity_deposits_jerk_252d_v071_signal": {"func": f39_excess_liquidity_deposits_jerk_252d_v071_signal},
    "f39_excess_liquidity_cash_density_jerk_252d_v072_signal": {"func": f39_excess_liquidity_cash_density_jerk_252d_v072_signal},
    "f39_excess_liquidity_cashneq_jerk_504d_v073_signal": {"func": f39_excess_liquidity_cashneq_jerk_504d_v073_signal},
    "f39_excess_liquidity_assets_jerk_504d_v074_signal": {"func": f39_excess_liquidity_assets_jerk_504d_v074_signal},
    "f39_excess_liquidity_deposits_jerk_504d_v075_signal": {"func": f39_excess_liquidity_deposits_jerk_504d_v075_signal},
    "f39_excess_liquidity_cash_density_jerk_504d_v076_signal": {"func": f39_excess_liquidity_cash_density_jerk_504d_v076_signal},
    "f39_excess_liquidity_cashneq_jerk_756d_v077_signal": {"func": f39_excess_liquidity_cashneq_jerk_756d_v077_signal},
    "f39_excess_liquidity_assets_jerk_756d_v078_signal": {"func": f39_excess_liquidity_assets_jerk_756d_v078_signal},
    "f39_excess_liquidity_deposits_jerk_756d_v079_signal": {"func": f39_excess_liquidity_deposits_jerk_756d_v079_signal},
    "f39_excess_liquidity_cash_density_jerk_756d_v080_signal": {"func": f39_excess_liquidity_cash_density_jerk_756d_v080_signal},
    "f39_excess_liquidity_cashneq_jerk_1008d_v081_signal": {"func": f39_excess_liquidity_cashneq_jerk_1008d_v081_signal},
    "f39_excess_liquidity_assets_jerk_1008d_v082_signal": {"func": f39_excess_liquidity_assets_jerk_1008d_v082_signal},
    "f39_excess_liquidity_deposits_jerk_1008d_v083_signal": {"func": f39_excess_liquidity_deposits_jerk_1008d_v083_signal},
    "f39_excess_liquidity_cash_density_jerk_1008d_v084_signal": {"func": f39_excess_liquidity_cash_density_jerk_1008d_v084_signal},
    "f39_excess_liquidity_cashneq_jerk_1260d_v085_signal": {"func": f39_excess_liquidity_cashneq_jerk_1260d_v085_signal},
    "f39_excess_liquidity_assets_jerk_1260d_v086_signal": {"func": f39_excess_liquidity_assets_jerk_1260d_v086_signal},
    "f39_excess_liquidity_deposits_jerk_1260d_v087_signal": {"func": f39_excess_liquidity_deposits_jerk_1260d_v087_signal},
    "f39_excess_liquidity_cash_density_jerk_1260d_v088_signal": {"func": f39_excess_liquidity_cash_density_jerk_1260d_v088_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_5d_v089_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_5d_v089_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_5d_v090_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_5d_v090_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_5d_v091_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_5d_v091_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_5d_v092_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_5d_v092_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_10d_v093_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_10d_v093_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_10d_v094_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_10d_v094_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_10d_v095_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_10d_v095_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_10d_v096_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_10d_v096_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_21d_v097_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_21d_v097_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_21d_v098_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_21d_v098_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_21d_v099_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_21d_v099_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_21d_v100_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_21d_v100_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_42d_v101_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_42d_v101_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_42d_v102_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_42d_v102_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_42d_v103_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_42d_v103_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_42d_v104_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_42d_v104_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_63d_v105_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_63d_v105_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_63d_v106_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_63d_v106_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_63d_v107_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_63d_v107_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_63d_v108_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_63d_v108_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_126d_v109_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_126d_v109_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_126d_v110_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_126d_v110_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_126d_v111_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_126d_v111_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_126d_v112_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_126d_v112_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_252d_v113_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_252d_v113_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_252d_v114_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_252d_v114_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_252d_v115_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_252d_v115_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_252d_v116_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_252d_v116_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_504d_v117_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_504d_v117_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_504d_v118_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_504d_v118_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_504d_v119_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_504d_v119_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_504d_v120_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_504d_v120_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_756d_v121_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_756d_v121_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_756d_v122_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_756d_v122_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_756d_v123_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_756d_v123_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_756d_v124_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_756d_v124_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_1008d_v125_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_1008d_v125_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_1008d_v126_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_1008d_v126_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_1008d_v127_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_1008d_v127_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_1008d_v128_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_1008d_v128_signal},
    "f39_excess_liquidity_cashneq_slope_diff_norm_1260d_v129_signal": {"func": f39_excess_liquidity_cashneq_slope_diff_norm_1260d_v129_signal},
    "f39_excess_liquidity_assets_slope_diff_norm_1260d_v130_signal": {"func": f39_excess_liquidity_assets_slope_diff_norm_1260d_v130_signal},
    "f39_excess_liquidity_deposits_slope_diff_norm_1260d_v131_signal": {"func": f39_excess_liquidity_deposits_slope_diff_norm_1260d_v131_signal},
    "f39_excess_liquidity_cash_density_slope_diff_norm_1260d_v132_signal": {"func": f39_excess_liquidity_cash_density_slope_diff_norm_1260d_v132_signal},
    "f39_excess_liquidity_cashneq_mom_z_5d_v133_signal": {"func": f39_excess_liquidity_cashneq_mom_z_5d_v133_signal},
    "f39_excess_liquidity_assets_mom_z_5d_v134_signal": {"func": f39_excess_liquidity_assets_mom_z_5d_v134_signal},
    "f39_excess_liquidity_deposits_mom_z_5d_v135_signal": {"func": f39_excess_liquidity_deposits_mom_z_5d_v135_signal},
    "f39_excess_liquidity_cash_density_mom_z_5d_v136_signal": {"func": f39_excess_liquidity_cash_density_mom_z_5d_v136_signal},
    "f39_excess_liquidity_cashneq_mom_z_10d_v137_signal": {"func": f39_excess_liquidity_cashneq_mom_z_10d_v137_signal},
    "f39_excess_liquidity_assets_mom_z_10d_v138_signal": {"func": f39_excess_liquidity_assets_mom_z_10d_v138_signal},
    "f39_excess_liquidity_deposits_mom_z_10d_v139_signal": {"func": f39_excess_liquidity_deposits_mom_z_10d_v139_signal},
    "f39_excess_liquidity_cash_density_mom_z_10d_v140_signal": {"func": f39_excess_liquidity_cash_density_mom_z_10d_v140_signal},
    "f39_excess_liquidity_cashneq_mom_z_21d_v141_signal": {"func": f39_excess_liquidity_cashneq_mom_z_21d_v141_signal},
    "f39_excess_liquidity_assets_mom_z_21d_v142_signal": {"func": f39_excess_liquidity_assets_mom_z_21d_v142_signal},
    "f39_excess_liquidity_deposits_mom_z_21d_v143_signal": {"func": f39_excess_liquidity_deposits_mom_z_21d_v143_signal},
    "f39_excess_liquidity_cash_density_mom_z_21d_v144_signal": {"func": f39_excess_liquidity_cash_density_mom_z_21d_v144_signal},
    "f39_excess_liquidity_cashneq_mom_z_42d_v145_signal": {"func": f39_excess_liquidity_cashneq_mom_z_42d_v145_signal},
    "f39_excess_liquidity_assets_mom_z_42d_v146_signal": {"func": f39_excess_liquidity_assets_mom_z_42d_v146_signal},
    "f39_excess_liquidity_deposits_mom_z_42d_v147_signal": {"func": f39_excess_liquidity_deposits_mom_z_42d_v147_signal},
    "f39_excess_liquidity_cash_density_mom_z_42d_v148_signal": {"func": f39_excess_liquidity_cash_density_mom_z_42d_v148_signal},
    "f39_excess_liquidity_cashneq_mom_z_63d_v149_signal": {"func": f39_excess_liquidity_cashneq_mom_z_63d_v149_signal},
    "f39_excess_liquidity_assets_mom_z_63d_v150_signal": {"func": f39_excess_liquidity_assets_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 39...")
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
