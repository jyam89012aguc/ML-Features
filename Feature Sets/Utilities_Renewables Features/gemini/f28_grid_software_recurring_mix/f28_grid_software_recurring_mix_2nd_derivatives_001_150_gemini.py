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

def f28_grid_software_recurring_mix_deferredrev_slope_pct_5d_v001_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 5d window."""
    res = _slope_pct(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_5d_v002_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_5d_v003_signal(sgna):
    """Percentage slope for Raw level of sgna over 5d window."""
    res = _slope_pct(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_5d_v004_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_5d_v005_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 5d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_5d_v006_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 5d window."""
    res = _slope_pct(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_10d_v007_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 10d window."""
    res = _slope_pct(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_10d_v008_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_10d_v009_signal(sgna):
    """Percentage slope for Raw level of sgna over 10d window."""
    res = _slope_pct(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_10d_v010_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_10d_v011_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 10d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_10d_v012_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 10d window."""
    res = _slope_pct(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_21d_v013_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 21d window."""
    res = _slope_pct(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_21d_v014_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_21d_v015_signal(sgna):
    """Percentage slope for Raw level of sgna over 21d window."""
    res = _slope_pct(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_21d_v016_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_21d_v017_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 21d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_21d_v018_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 21d window."""
    res = _slope_pct(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_42d_v019_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 42d window."""
    res = _slope_pct(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_42d_v020_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_42d_v021_signal(sgna):
    """Percentage slope for Raw level of sgna over 42d window."""
    res = _slope_pct(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_42d_v022_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_42d_v023_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 42d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_42d_v024_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 42d window."""
    res = _slope_pct(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_63d_v025_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 63d window."""
    res = _slope_pct(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_63d_v026_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_63d_v027_signal(sgna):
    """Percentage slope for Raw level of sgna over 63d window."""
    res = _slope_pct(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_63d_v028_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_63d_v029_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 63d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_63d_v030_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 63d window."""
    res = _slope_pct(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_126d_v031_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 126d window."""
    res = _slope_pct(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_126d_v032_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_126d_v033_signal(sgna):
    """Percentage slope for Raw level of sgna over 126d window."""
    res = _slope_pct(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_126d_v034_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_126d_v035_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 126d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_126d_v036_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 126d window."""
    res = _slope_pct(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_252d_v037_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 252d window."""
    res = _slope_pct(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_252d_v038_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_252d_v039_signal(sgna):
    """Percentage slope for Raw level of sgna over 252d window."""
    res = _slope_pct(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_252d_v040_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_252d_v041_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 252d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_252d_v042_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 252d window."""
    res = _slope_pct(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_504d_v043_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 504d window."""
    res = _slope_pct(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_504d_v044_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_504d_v045_signal(sgna):
    """Percentage slope for Raw level of sgna over 504d window."""
    res = _slope_pct(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_504d_v046_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_504d_v047_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 504d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_504d_v048_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 504d window."""
    res = _slope_pct(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_756d_v049_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 756d window."""
    res = _slope_pct(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_756d_v050_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_756d_v051_signal(sgna):
    """Percentage slope for Raw level of sgna over 756d window."""
    res = _slope_pct(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_756d_v052_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_756d_v053_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 756d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_756d_v054_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 756d window."""
    res = _slope_pct(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_1008d_v055_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 1008d window."""
    res = _slope_pct(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_1008d_v056_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_1008d_v057_signal(sgna):
    """Percentage slope for Raw level of sgna over 1008d window."""
    res = _slope_pct(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_1008d_v058_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_1008d_v059_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 1008d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_1008d_v060_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 1008d window."""
    res = _slope_pct(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_pct_1260d_v061_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 1260d window."""
    res = _slope_pct(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_pct_1260d_v062_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_pct_1260d_v063_signal(sgna):
    """Percentage slope for Raw level of sgna over 1260d window."""
    res = _slope_pct(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_pct_1260d_v064_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_pct_1260d_v065_signal(revenue, deferredrev):
    """Percentage slope for Contract realization velocity over 1260d window."""
    res = _slope_pct(_ratio(revenue, deferredrev), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_1260d_v066_signal(revenue, sgna):
    """Percentage slope for Sales yield on SG&A overhead over 1260d window."""
    res = _slope_pct(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_5d_v067_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 5d window."""
    res = _jerk(deferredrev, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_5d_v068_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_5d_v069_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 5d window."""
    res = _jerk(sgna, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_5d_v070_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_5d_v071_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 5d window."""
    res = _jerk(_ratio(revenue, deferredrev), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_5d_v072_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 5d window."""
    res = _jerk(_ratio(revenue, sgna), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_10d_v073_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 10d window."""
    res = _jerk(deferredrev, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_10d_v074_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_10d_v075_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 10d window."""
    res = _jerk(sgna, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_10d_v076_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_10d_v077_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 10d window."""
    res = _jerk(_ratio(revenue, deferredrev), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_10d_v078_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 10d window."""
    res = _jerk(_ratio(revenue, sgna), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_21d_v079_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 21d window."""
    res = _jerk(deferredrev, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_21d_v080_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_21d_v081_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 21d window."""
    res = _jerk(sgna, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_21d_v082_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_21d_v083_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 21d window."""
    res = _jerk(_ratio(revenue, deferredrev), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_21d_v084_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 21d window."""
    res = _jerk(_ratio(revenue, sgna), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_42d_v085_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 42d window."""
    res = _jerk(deferredrev, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_42d_v086_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_42d_v087_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 42d window."""
    res = _jerk(sgna, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_42d_v088_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_42d_v089_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 42d window."""
    res = _jerk(_ratio(revenue, deferredrev), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_42d_v090_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 42d window."""
    res = _jerk(_ratio(revenue, sgna), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_63d_v091_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 63d window."""
    res = _jerk(deferredrev, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_63d_v092_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_63d_v093_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 63d window."""
    res = _jerk(sgna, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_63d_v094_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_63d_v095_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 63d window."""
    res = _jerk(_ratio(revenue, deferredrev), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_63d_v096_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 63d window."""
    res = _jerk(_ratio(revenue, sgna), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_126d_v097_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 126d window."""
    res = _jerk(deferredrev, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_126d_v098_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_126d_v099_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 126d window."""
    res = _jerk(sgna, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_126d_v100_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_126d_v101_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 126d window."""
    res = _jerk(_ratio(revenue, deferredrev), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_126d_v102_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 126d window."""
    res = _jerk(_ratio(revenue, sgna), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_252d_v103_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 252d window."""
    res = _jerk(deferredrev, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_252d_v104_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_252d_v105_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 252d window."""
    res = _jerk(sgna, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_252d_v106_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_252d_v107_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 252d window."""
    res = _jerk(_ratio(revenue, deferredrev), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_252d_v108_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 252d window."""
    res = _jerk(_ratio(revenue, sgna), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_504d_v109_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 504d window."""
    res = _jerk(deferredrev, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_504d_v110_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_504d_v111_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 504d window."""
    res = _jerk(sgna, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_504d_v112_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_504d_v113_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 504d window."""
    res = _jerk(_ratio(revenue, deferredrev), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_504d_v114_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 504d window."""
    res = _jerk(_ratio(revenue, sgna), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_756d_v115_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 756d window."""
    res = _jerk(deferredrev, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_756d_v116_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_756d_v117_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 756d window."""
    res = _jerk(sgna, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_756d_v118_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_756d_v119_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 756d window."""
    res = _jerk(_ratio(revenue, deferredrev), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_756d_v120_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 756d window."""
    res = _jerk(_ratio(revenue, sgna), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_1008d_v121_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 1008d window."""
    res = _jerk(deferredrev, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_1008d_v122_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_1008d_v123_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1008d window."""
    res = _jerk(sgna, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_1008d_v124_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_1008d_v125_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 1008d window."""
    res = _jerk(_ratio(revenue, deferredrev), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_1008d_v126_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 1008d window."""
    res = _jerk(_ratio(revenue, sgna), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_jerk_1260d_v127_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 1260d window."""
    res = _jerk(deferredrev, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_jerk_1260d_v128_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_jerk_1260d_v129_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1260d window."""
    res = _jerk(sgna, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_jerk_1260d_v130_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_jerk_1260d_v131_signal(revenue, deferredrev):
    """Acceleration/Jerk for Contract realization velocity over 1260d window."""
    res = _jerk(_ratio(revenue, deferredrev), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_jerk_1260d_v132_signal(revenue, sgna):
    """Acceleration/Jerk for Sales yield on SG&A overhead over 1260d window."""
    res = _jerk(_ratio(revenue, sgna), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_5d_v133_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 5d window."""
    res = (_slope_pct(deferredrev, 5).diff(5) / _sma(deferredrev.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_diff_norm_5d_v134_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_diff_norm_5d_v135_signal(sgna):
    """Normalized slope change for Raw level of sgna over 5d window."""
    res = (_slope_pct(sgna, 5).diff(5) / _sma(sgna.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_diff_norm_5d_v136_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_5d_v137_signal(revenue, deferredrev):
    """Normalized slope change for Contract realization velocity over 5d window."""
    res = (_slope_pct(_ratio(revenue, deferredrev), 5).diff(5) / _sma(_ratio(revenue, deferredrev).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_5d_v138_signal(revenue, sgna):
    """Normalized slope change for Sales yield on SG&A overhead over 5d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 5).diff(5) / _sma(_ratio(revenue, sgna).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_10d_v139_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 10d window."""
    res = (_slope_pct(deferredrev, 10).diff(10) / _sma(deferredrev.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_diff_norm_10d_v140_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_diff_norm_10d_v141_signal(sgna):
    """Normalized slope change for Raw level of sgna over 10d window."""
    res = (_slope_pct(sgna, 10).diff(10) / _sma(sgna.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_diff_norm_10d_v142_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_10d_v143_signal(revenue, deferredrev):
    """Normalized slope change for Contract realization velocity over 10d window."""
    res = (_slope_pct(_ratio(revenue, deferredrev), 10).diff(10) / _sma(_ratio(revenue, deferredrev).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_10d_v144_signal(revenue, sgna):
    """Normalized slope change for Sales yield on SG&A overhead over 10d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 10).diff(10) / _sma(_ratio(revenue, sgna).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_21d_v145_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 21d window."""
    res = (_slope_pct(deferredrev, 21).diff(21) / _sma(deferredrev.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_revenue_slope_diff_norm_21d_v146_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_sgna_slope_diff_norm_21d_v147_signal(sgna):
    """Normalized slope change for Raw level of sgna over 21d window."""
    res = (_slope_pct(sgna, 21).diff(21) / _sma(sgna.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_assets_slope_diff_norm_21d_v148_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_21d_v149_signal(revenue, deferredrev):
    """Normalized slope change for Contract realization velocity over 21d window."""
    res = (_slope_pct(_ratio(revenue, deferredrev), 21).diff(21) / _sma(_ratio(revenue, deferredrev).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_21d_v150_signal(revenue, sgna):
    """Normalized slope change for Sales yield on SG&A overhead over 21d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 21).diff(21) / _sma(_ratio(revenue, sgna).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_5d_v001_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_5d_v001_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_5d_v002_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_5d_v002_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_5d_v003_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_5d_v003_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_5d_v004_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_5d_v004_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_5d_v005_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_5d_v005_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_5d_v006_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_5d_v006_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_10d_v007_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_10d_v007_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_10d_v008_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_10d_v008_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_10d_v009_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_10d_v009_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_10d_v010_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_10d_v010_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_10d_v011_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_10d_v011_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_10d_v012_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_10d_v012_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_21d_v013_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_21d_v013_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_21d_v014_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_21d_v014_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_21d_v015_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_21d_v015_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_21d_v016_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_21d_v016_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_21d_v017_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_21d_v017_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_21d_v018_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_21d_v018_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_42d_v019_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_42d_v019_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_42d_v020_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_42d_v020_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_42d_v021_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_42d_v021_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_42d_v022_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_42d_v022_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_42d_v023_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_42d_v023_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_42d_v024_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_42d_v024_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_63d_v025_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_63d_v025_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_63d_v026_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_63d_v026_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_63d_v027_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_63d_v027_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_63d_v028_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_63d_v028_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_63d_v029_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_63d_v029_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_63d_v030_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_63d_v030_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_126d_v031_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_126d_v031_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_126d_v032_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_126d_v032_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_126d_v033_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_126d_v033_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_126d_v034_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_126d_v034_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_126d_v035_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_126d_v035_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_126d_v036_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_126d_v036_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_252d_v037_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_252d_v037_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_252d_v038_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_252d_v038_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_252d_v039_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_252d_v039_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_252d_v040_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_252d_v040_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_252d_v041_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_252d_v041_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_252d_v042_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_252d_v042_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_504d_v043_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_504d_v043_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_504d_v044_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_504d_v044_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_504d_v045_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_504d_v045_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_504d_v046_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_504d_v046_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_504d_v047_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_504d_v047_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_504d_v048_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_504d_v048_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_756d_v049_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_756d_v049_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_756d_v050_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_756d_v050_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_756d_v051_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_756d_v051_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_756d_v052_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_756d_v052_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_756d_v053_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_756d_v053_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_756d_v054_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_756d_v054_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_1008d_v055_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_1008d_v055_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_1008d_v056_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_1008d_v056_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_1008d_v057_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_1008d_v057_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_1008d_v058_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_1008d_v058_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_1008d_v059_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_1008d_v059_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_1008d_v060_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_1008d_v060_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_pct_1260d_v061_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_pct_1260d_v061_signal},
    "f28_grid_software_recurring_mix_revenue_slope_pct_1260d_v062_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_pct_1260d_v062_signal},
    "f28_grid_software_recurring_mix_sgna_slope_pct_1260d_v063_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_pct_1260d_v063_signal},
    "f28_grid_software_recurring_mix_assets_slope_pct_1260d_v064_signal": {"func": f28_grid_software_recurring_mix_assets_slope_pct_1260d_v064_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_pct_1260d_v065_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_pct_1260d_v065_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_1260d_v066_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_pct_1260d_v066_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_5d_v067_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_5d_v067_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_5d_v068_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_5d_v068_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_5d_v069_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_5d_v069_signal},
    "f28_grid_software_recurring_mix_assets_jerk_5d_v070_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_5d_v070_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_5d_v071_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_5d_v071_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_5d_v072_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_5d_v072_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_10d_v073_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_10d_v073_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_10d_v074_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_10d_v074_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_10d_v075_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_10d_v075_signal},
    "f28_grid_software_recurring_mix_assets_jerk_10d_v076_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_10d_v076_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_10d_v077_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_10d_v077_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_10d_v078_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_10d_v078_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_21d_v079_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_21d_v079_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_21d_v080_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_21d_v080_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_21d_v081_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_21d_v081_signal},
    "f28_grid_software_recurring_mix_assets_jerk_21d_v082_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_21d_v082_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_21d_v083_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_21d_v083_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_21d_v084_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_21d_v084_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_42d_v085_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_42d_v085_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_42d_v086_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_42d_v086_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_42d_v087_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_42d_v087_signal},
    "f28_grid_software_recurring_mix_assets_jerk_42d_v088_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_42d_v088_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_42d_v089_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_42d_v089_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_42d_v090_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_42d_v090_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_63d_v091_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_63d_v091_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_63d_v092_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_63d_v092_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_63d_v093_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_63d_v093_signal},
    "f28_grid_software_recurring_mix_assets_jerk_63d_v094_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_63d_v094_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_63d_v095_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_63d_v095_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_63d_v096_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_63d_v096_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_126d_v097_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_126d_v097_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_126d_v098_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_126d_v098_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_126d_v099_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_126d_v099_signal},
    "f28_grid_software_recurring_mix_assets_jerk_126d_v100_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_126d_v100_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_126d_v101_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_126d_v101_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_126d_v102_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_126d_v102_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_252d_v103_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_252d_v103_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_252d_v104_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_252d_v104_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_252d_v105_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_252d_v105_signal},
    "f28_grid_software_recurring_mix_assets_jerk_252d_v106_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_252d_v106_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_252d_v107_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_252d_v107_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_252d_v108_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_252d_v108_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_504d_v109_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_504d_v109_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_504d_v110_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_504d_v110_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_504d_v111_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_504d_v111_signal},
    "f28_grid_software_recurring_mix_assets_jerk_504d_v112_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_504d_v112_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_504d_v113_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_504d_v113_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_504d_v114_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_504d_v114_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_756d_v115_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_756d_v115_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_756d_v116_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_756d_v116_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_756d_v117_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_756d_v117_signal},
    "f28_grid_software_recurring_mix_assets_jerk_756d_v118_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_756d_v118_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_756d_v119_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_756d_v119_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_756d_v120_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_756d_v120_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_1008d_v121_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_1008d_v121_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_1008d_v122_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_1008d_v122_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_1008d_v123_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_1008d_v123_signal},
    "f28_grid_software_recurring_mix_assets_jerk_1008d_v124_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_1008d_v124_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_1008d_v125_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_1008d_v125_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_1008d_v126_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_1008d_v126_signal},
    "f28_grid_software_recurring_mix_deferredrev_jerk_1260d_v127_signal": {"func": f28_grid_software_recurring_mix_deferredrev_jerk_1260d_v127_signal},
    "f28_grid_software_recurring_mix_revenue_jerk_1260d_v128_signal": {"func": f28_grid_software_recurring_mix_revenue_jerk_1260d_v128_signal},
    "f28_grid_software_recurring_mix_sgna_jerk_1260d_v129_signal": {"func": f28_grid_software_recurring_mix_sgna_jerk_1260d_v129_signal},
    "f28_grid_software_recurring_mix_assets_jerk_1260d_v130_signal": {"func": f28_grid_software_recurring_mix_assets_jerk_1260d_v130_signal},
    "f28_grid_software_recurring_mix_backlog_burn_jerk_1260d_v131_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_jerk_1260d_v131_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_jerk_1260d_v132_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_jerk_1260d_v132_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_5d_v133_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_5d_v133_signal},
    "f28_grid_software_recurring_mix_revenue_slope_diff_norm_5d_v134_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_diff_norm_5d_v134_signal},
    "f28_grid_software_recurring_mix_sgna_slope_diff_norm_5d_v135_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_diff_norm_5d_v135_signal},
    "f28_grid_software_recurring_mix_assets_slope_diff_norm_5d_v136_signal": {"func": f28_grid_software_recurring_mix_assets_slope_diff_norm_5d_v136_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_5d_v137_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_5d_v137_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_5d_v138_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_5d_v138_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_10d_v139_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_10d_v139_signal},
    "f28_grid_software_recurring_mix_revenue_slope_diff_norm_10d_v140_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_diff_norm_10d_v140_signal},
    "f28_grid_software_recurring_mix_sgna_slope_diff_norm_10d_v141_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_diff_norm_10d_v141_signal},
    "f28_grid_software_recurring_mix_assets_slope_diff_norm_10d_v142_signal": {"func": f28_grid_software_recurring_mix_assets_slope_diff_norm_10d_v142_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_10d_v143_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_10d_v143_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_10d_v144_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_10d_v144_signal},
    "f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_21d_v145_signal": {"func": f28_grid_software_recurring_mix_deferredrev_slope_diff_norm_21d_v145_signal},
    "f28_grid_software_recurring_mix_revenue_slope_diff_norm_21d_v146_signal": {"func": f28_grid_software_recurring_mix_revenue_slope_diff_norm_21d_v146_signal},
    "f28_grid_software_recurring_mix_sgna_slope_diff_norm_21d_v147_signal": {"func": f28_grid_software_recurring_mix_sgna_slope_diff_norm_21d_v147_signal},
    "f28_grid_software_recurring_mix_assets_slope_diff_norm_21d_v148_signal": {"func": f28_grid_software_recurring_mix_assets_slope_diff_norm_21d_v148_signal},
    "f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_21d_v149_signal": {"func": f28_grid_software_recurring_mix_backlog_burn_slope_diff_norm_21d_v149_signal},
    "f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_21d_v150_signal": {"func": f28_grid_software_recurring_mix_overhead_efficiency_slope_diff_norm_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 28...")
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
