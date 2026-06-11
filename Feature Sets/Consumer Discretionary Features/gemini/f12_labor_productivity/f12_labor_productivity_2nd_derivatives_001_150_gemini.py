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

def f12_labor_productivity_sgna_slope_pct_5d_v001_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 5d window."""
    res = _slope_pct(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_5d_v002_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 5d window."""
    res = _slope_pct(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_5d_v003_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_5d_v004_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 5d window."""
    res = _slope_pct(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_10d_v005_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 10d window."""
    res = _slope_pct(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_10d_v006_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 10d window."""
    res = _slope_pct(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_10d_v007_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_10d_v008_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 10d window."""
    res = _slope_pct(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_21d_v009_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 21d window."""
    res = _slope_pct(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_21d_v010_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 21d window."""
    res = _slope_pct(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_21d_v011_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_21d_v012_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 21d window."""
    res = _slope_pct(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_42d_v013_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 42d window."""
    res = _slope_pct(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_42d_v014_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 42d window."""
    res = _slope_pct(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_42d_v015_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_42d_v016_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 42d window."""
    res = _slope_pct(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_63d_v017_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 63d window."""
    res = _slope_pct(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_63d_v018_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 63d window."""
    res = _slope_pct(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_63d_v019_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_63d_v020_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 63d window."""
    res = _slope_pct(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_126d_v021_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 126d window."""
    res = _slope_pct(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_126d_v022_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 126d window."""
    res = _slope_pct(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_126d_v023_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_126d_v024_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 126d window."""
    res = _slope_pct(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_252d_v025_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 252d window."""
    res = _slope_pct(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_252d_v026_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 252d window."""
    res = _slope_pct(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_252d_v027_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_252d_v028_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 252d window."""
    res = _slope_pct(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_504d_v029_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 504d window."""
    res = _slope_pct(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_504d_v030_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 504d window."""
    res = _slope_pct(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_504d_v031_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_504d_v032_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 504d window."""
    res = _slope_pct(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_756d_v033_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 756d window."""
    res = _slope_pct(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_756d_v034_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 756d window."""
    res = _slope_pct(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_756d_v035_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_756d_v036_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 756d window."""
    res = _slope_pct(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_1008d_v037_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 1008d window."""
    res = _slope_pct(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_1008d_v038_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 1008d window."""
    res = _slope_pct(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_1008d_v039_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_1008d_v040_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 1008d window."""
    res = _slope_pct(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_pct_1260d_v041_signal(sgna):
    """Percentage slope for momentum for Raw level of sgna over 1260d window."""
    res = _slope_pct(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_pct_1260d_v042_signal(ebit):
    """Percentage slope for momentum for Raw level of ebit over 1260d window."""
    res = _slope_pct(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_pct_1260d_v043_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_pct_1260d_v044_signal(revenue, sgna):
    """Percentage slope for momentum for Sales productivity of the labor/overhead base over 1260d window."""
    res = _slope_pct(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_5d_v045_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 5d window."""
    res = _jerk(sgna, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_5d_v046_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 5d window."""
    res = _jerk(ebit, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_5d_v047_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_5d_v048_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 5d window."""
    res = _jerk(_ratio(revenue, sgna), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_10d_v049_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 10d window."""
    res = _jerk(sgna, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_10d_v050_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 10d window."""
    res = _jerk(ebit, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_10d_v051_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_10d_v052_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 10d window."""
    res = _jerk(_ratio(revenue, sgna), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_21d_v053_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 21d window."""
    res = _jerk(sgna, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_21d_v054_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 21d window."""
    res = _jerk(ebit, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_21d_v055_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_21d_v056_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 21d window."""
    res = _jerk(_ratio(revenue, sgna), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_42d_v057_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 42d window."""
    res = _jerk(sgna, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_42d_v058_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 42d window."""
    res = _jerk(ebit, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_42d_v059_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_42d_v060_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 42d window."""
    res = _jerk(_ratio(revenue, sgna), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_63d_v061_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 63d window."""
    res = _jerk(sgna, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_63d_v062_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 63d window."""
    res = _jerk(ebit, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_63d_v063_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_63d_v064_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 63d window."""
    res = _jerk(_ratio(revenue, sgna), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_126d_v065_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 126d window."""
    res = _jerk(sgna, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_126d_v066_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 126d window."""
    res = _jerk(ebit, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_126d_v067_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_126d_v068_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 126d window."""
    res = _jerk(_ratio(revenue, sgna), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_252d_v069_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 252d window."""
    res = _jerk(sgna, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_252d_v070_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 252d window."""
    res = _jerk(ebit, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_252d_v071_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_252d_v072_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 252d window."""
    res = _jerk(_ratio(revenue, sgna), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_504d_v073_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 504d window."""
    res = _jerk(sgna, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_504d_v074_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 504d window."""
    res = _jerk(ebit, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_504d_v075_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_504d_v076_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 504d window."""
    res = _jerk(_ratio(revenue, sgna), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_756d_v077_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 756d window."""
    res = _jerk(sgna, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_756d_v078_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 756d window."""
    res = _jerk(ebit, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_756d_v079_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_756d_v080_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 756d window."""
    res = _jerk(_ratio(revenue, sgna), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_1008d_v081_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 1008d window."""
    res = _jerk(sgna, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_1008d_v082_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 1008d window."""
    res = _jerk(ebit, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_1008d_v083_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_1008d_v084_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 1008d window."""
    res = _jerk(_ratio(revenue, sgna), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_jerk_1260d_v085_signal(sgna):
    """Acceleration/Jerk for structural shifts for Raw level of sgna over 1260d window."""
    res = _jerk(sgna, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_jerk_1260d_v086_signal(ebit):
    """Acceleration/Jerk for structural shifts for Raw level of ebit over 1260d window."""
    res = _jerk(ebit, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_jerk_1260d_v087_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_jerk_1260d_v088_signal(revenue, sgna):
    """Acceleration/Jerk for structural shifts for Sales productivity of the labor/overhead base over 1260d window."""
    res = _jerk(_ratio(revenue, sgna), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_5d_v089_signal(sgna):
    """Normalized slope change for Raw level of sgna over 5d window."""
    res = (_slope_pct(sgna, 5).diff(5) / _sma(sgna.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_5d_v090_signal(ebit):
    """Normalized slope change for Raw level of ebit over 5d window."""
    res = (_slope_pct(ebit, 5).diff(5) / _sma(ebit.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_5d_v091_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_5d_v092_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 5d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 5).diff(5) / _sma(_ratio(revenue, sgna).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_10d_v093_signal(sgna):
    """Normalized slope change for Raw level of sgna over 10d window."""
    res = (_slope_pct(sgna, 10).diff(10) / _sma(sgna.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_10d_v094_signal(ebit):
    """Normalized slope change for Raw level of ebit over 10d window."""
    res = (_slope_pct(ebit, 10).diff(10) / _sma(ebit.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_10d_v095_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_10d_v096_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 10d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 10).diff(10) / _sma(_ratio(revenue, sgna).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_21d_v097_signal(sgna):
    """Normalized slope change for Raw level of sgna over 21d window."""
    res = (_slope_pct(sgna, 21).diff(21) / _sma(sgna.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_21d_v098_signal(ebit):
    """Normalized slope change for Raw level of ebit over 21d window."""
    res = (_slope_pct(ebit, 21).diff(21) / _sma(ebit.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_21d_v099_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_21d_v100_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 21d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 21).diff(21) / _sma(_ratio(revenue, sgna).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_42d_v101_signal(sgna):
    """Normalized slope change for Raw level of sgna over 42d window."""
    res = (_slope_pct(sgna, 42).diff(42) / _sma(sgna.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_42d_v102_signal(ebit):
    """Normalized slope change for Raw level of ebit over 42d window."""
    res = (_slope_pct(ebit, 42).diff(42) / _sma(ebit.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_42d_v103_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_42d_v104_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 42d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 42).diff(42) / _sma(_ratio(revenue, sgna).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_63d_v105_signal(sgna):
    """Normalized slope change for Raw level of sgna over 63d window."""
    res = (_slope_pct(sgna, 63).diff(63) / _sma(sgna.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_63d_v106_signal(ebit):
    """Normalized slope change for Raw level of ebit over 63d window."""
    res = (_slope_pct(ebit, 63).diff(63) / _sma(ebit.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_63d_v107_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_63d_v108_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 63d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 63).diff(63) / _sma(_ratio(revenue, sgna).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_126d_v109_signal(sgna):
    """Normalized slope change for Raw level of sgna over 126d window."""
    res = (_slope_pct(sgna, 126).diff(126) / _sma(sgna.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_126d_v110_signal(ebit):
    """Normalized slope change for Raw level of ebit over 126d window."""
    res = (_slope_pct(ebit, 126).diff(126) / _sma(ebit.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_126d_v111_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_126d_v112_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 126d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 126).diff(126) / _sma(_ratio(revenue, sgna).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_252d_v113_signal(sgna):
    """Normalized slope change for Raw level of sgna over 252d window."""
    res = (_slope_pct(sgna, 252).diff(252) / _sma(sgna.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_252d_v114_signal(ebit):
    """Normalized slope change for Raw level of ebit over 252d window."""
    res = (_slope_pct(ebit, 252).diff(252) / _sma(ebit.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_252d_v115_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_252d_v116_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 252d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 252).diff(252) / _sma(_ratio(revenue, sgna).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_504d_v117_signal(sgna):
    """Normalized slope change for Raw level of sgna over 504d window."""
    res = (_slope_pct(sgna, 504).diff(504) / _sma(sgna.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_504d_v118_signal(ebit):
    """Normalized slope change for Raw level of ebit over 504d window."""
    res = (_slope_pct(ebit, 504).diff(504) / _sma(ebit.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_504d_v119_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_504d_v120_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 504d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 504).diff(504) / _sma(_ratio(revenue, sgna).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_756d_v121_signal(sgna):
    """Normalized slope change for Raw level of sgna over 756d window."""
    res = (_slope_pct(sgna, 756).diff(756) / _sma(sgna.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_756d_v122_signal(ebit):
    """Normalized slope change for Raw level of ebit over 756d window."""
    res = (_slope_pct(ebit, 756).diff(756) / _sma(ebit.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_756d_v123_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_756d_v124_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 756d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 756).diff(756) / _sma(_ratio(revenue, sgna).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_1008d_v125_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1008d window."""
    res = (_slope_pct(sgna, 1008).diff(1008) / _sma(sgna.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_1008d_v126_signal(ebit):
    """Normalized slope change for Raw level of ebit over 1008d window."""
    res = (_slope_pct(ebit, 1008).diff(1008) / _sma(ebit.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_1008d_v127_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_1008d_v128_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 1008d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 1008).diff(1008) / _sma(_ratio(revenue, sgna).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_slope_diff_norm_1260d_v129_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1260d window."""
    res = (_slope_pct(sgna, 1260).diff(1260) / _sma(sgna.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_slope_diff_norm_1260d_v130_signal(ebit):
    """Normalized slope change for Raw level of ebit over 1260d window."""
    res = (_slope_pct(ebit, 1260).diff(1260) / _sma(ebit.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_slope_diff_norm_1260d_v131_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_slope_diff_norm_1260d_v132_signal(revenue, sgna):
    """Normalized slope change for Sales productivity of the labor/overhead base over 1260d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 1260).diff(1260) / _sma(_ratio(revenue, sgna).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_mom_z_5d_v133_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 5d window."""
    res = _z(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_mom_z_5d_v134_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 5d window."""
    res = _z(_slope_pct(ebit, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_mom_z_5d_v135_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_mom_z_5d_v136_signal(revenue, sgna):
    """Relative momentum strength for Sales productivity of the labor/overhead base over 5d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_mom_z_10d_v137_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 10d window."""
    res = _z(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_mom_z_10d_v138_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 10d window."""
    res = _z(_slope_pct(ebit, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_mom_z_10d_v139_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_mom_z_10d_v140_signal(revenue, sgna):
    """Relative momentum strength for Sales productivity of the labor/overhead base over 10d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_mom_z_21d_v141_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 21d window."""
    res = _z(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_mom_z_21d_v142_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 21d window."""
    res = _z(_slope_pct(ebit, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_mom_z_21d_v143_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_mom_z_21d_v144_signal(revenue, sgna):
    """Relative momentum strength for Sales productivity of the labor/overhead base over 21d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_mom_z_42d_v145_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 42d window."""
    res = _z(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_mom_z_42d_v146_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 42d window."""
    res = _z(_slope_pct(ebit, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_mom_z_42d_v147_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_mom_z_42d_v148_signal(revenue, sgna):
    """Relative momentum strength for Sales productivity of the labor/overhead base over 42d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_mom_z_63d_v149_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 63d window."""
    res = _z(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_mom_z_63d_v150_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 63d window."""
    res = _z(_slope_pct(ebit, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f12_labor_productivity_sgna_slope_pct_5d_v001_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_5d_v001_signal},    "f12_labor_productivity_ebit_slope_pct_5d_v002_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_5d_v002_signal},    "f12_labor_productivity_revenue_slope_pct_5d_v003_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_5d_v003_signal},    "f12_labor_productivity_labor_leverage_slope_pct_5d_v004_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_5d_v004_signal},    "f12_labor_productivity_sgna_slope_pct_10d_v005_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_10d_v005_signal},    "f12_labor_productivity_ebit_slope_pct_10d_v006_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_10d_v006_signal},    "f12_labor_productivity_revenue_slope_pct_10d_v007_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_10d_v007_signal},    "f12_labor_productivity_labor_leverage_slope_pct_10d_v008_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_10d_v008_signal},    "f12_labor_productivity_sgna_slope_pct_21d_v009_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_21d_v009_signal},    "f12_labor_productivity_ebit_slope_pct_21d_v010_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_21d_v010_signal},    "f12_labor_productivity_revenue_slope_pct_21d_v011_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_21d_v011_signal},    "f12_labor_productivity_labor_leverage_slope_pct_21d_v012_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_21d_v012_signal},    "f12_labor_productivity_sgna_slope_pct_42d_v013_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_42d_v013_signal},    "f12_labor_productivity_ebit_slope_pct_42d_v014_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_42d_v014_signal},    "f12_labor_productivity_revenue_slope_pct_42d_v015_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_42d_v015_signal},    "f12_labor_productivity_labor_leverage_slope_pct_42d_v016_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_42d_v016_signal},    "f12_labor_productivity_sgna_slope_pct_63d_v017_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_63d_v017_signal},    "f12_labor_productivity_ebit_slope_pct_63d_v018_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_63d_v018_signal},    "f12_labor_productivity_revenue_slope_pct_63d_v019_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_63d_v019_signal},    "f12_labor_productivity_labor_leverage_slope_pct_63d_v020_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_63d_v020_signal},    "f12_labor_productivity_sgna_slope_pct_126d_v021_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_126d_v021_signal},    "f12_labor_productivity_ebit_slope_pct_126d_v022_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_126d_v022_signal},    "f12_labor_productivity_revenue_slope_pct_126d_v023_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_126d_v023_signal},    "f12_labor_productivity_labor_leverage_slope_pct_126d_v024_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_126d_v024_signal},    "f12_labor_productivity_sgna_slope_pct_252d_v025_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_252d_v025_signal},    "f12_labor_productivity_ebit_slope_pct_252d_v026_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_252d_v026_signal},    "f12_labor_productivity_revenue_slope_pct_252d_v027_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_252d_v027_signal},    "f12_labor_productivity_labor_leverage_slope_pct_252d_v028_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_252d_v028_signal},    "f12_labor_productivity_sgna_slope_pct_504d_v029_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_504d_v029_signal},    "f12_labor_productivity_ebit_slope_pct_504d_v030_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_504d_v030_signal},    "f12_labor_productivity_revenue_slope_pct_504d_v031_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_504d_v031_signal},    "f12_labor_productivity_labor_leverage_slope_pct_504d_v032_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_504d_v032_signal},    "f12_labor_productivity_sgna_slope_pct_756d_v033_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_756d_v033_signal},    "f12_labor_productivity_ebit_slope_pct_756d_v034_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_756d_v034_signal},    "f12_labor_productivity_revenue_slope_pct_756d_v035_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_756d_v035_signal},    "f12_labor_productivity_labor_leverage_slope_pct_756d_v036_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_756d_v036_signal},    "f12_labor_productivity_sgna_slope_pct_1008d_v037_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_1008d_v037_signal},    "f12_labor_productivity_ebit_slope_pct_1008d_v038_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_1008d_v038_signal},    "f12_labor_productivity_revenue_slope_pct_1008d_v039_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_1008d_v039_signal},    "f12_labor_productivity_labor_leverage_slope_pct_1008d_v040_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_1008d_v040_signal},    "f12_labor_productivity_sgna_slope_pct_1260d_v041_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_pct_1260d_v041_signal},    "f12_labor_productivity_ebit_slope_pct_1260d_v042_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_pct_1260d_v042_signal},    "f12_labor_productivity_revenue_slope_pct_1260d_v043_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_pct_1260d_v043_signal},    "f12_labor_productivity_labor_leverage_slope_pct_1260d_v044_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_pct_1260d_v044_signal},    "f12_labor_productivity_sgna_jerk_5d_v045_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_5d_v045_signal},    "f12_labor_productivity_ebit_jerk_5d_v046_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_5d_v046_signal},    "f12_labor_productivity_revenue_jerk_5d_v047_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_5d_v047_signal},    "f12_labor_productivity_labor_leverage_jerk_5d_v048_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_5d_v048_signal},    "f12_labor_productivity_sgna_jerk_10d_v049_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_10d_v049_signal},    "f12_labor_productivity_ebit_jerk_10d_v050_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_10d_v050_signal},    "f12_labor_productivity_revenue_jerk_10d_v051_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_10d_v051_signal},    "f12_labor_productivity_labor_leverage_jerk_10d_v052_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_10d_v052_signal},    "f12_labor_productivity_sgna_jerk_21d_v053_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_21d_v053_signal},    "f12_labor_productivity_ebit_jerk_21d_v054_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_21d_v054_signal},    "f12_labor_productivity_revenue_jerk_21d_v055_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_21d_v055_signal},    "f12_labor_productivity_labor_leverage_jerk_21d_v056_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_21d_v056_signal},    "f12_labor_productivity_sgna_jerk_42d_v057_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_42d_v057_signal},    "f12_labor_productivity_ebit_jerk_42d_v058_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_42d_v058_signal},    "f12_labor_productivity_revenue_jerk_42d_v059_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_42d_v059_signal},    "f12_labor_productivity_labor_leverage_jerk_42d_v060_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_42d_v060_signal},    "f12_labor_productivity_sgna_jerk_63d_v061_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_63d_v061_signal},    "f12_labor_productivity_ebit_jerk_63d_v062_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_63d_v062_signal},    "f12_labor_productivity_revenue_jerk_63d_v063_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_63d_v063_signal},    "f12_labor_productivity_labor_leverage_jerk_63d_v064_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_63d_v064_signal},    "f12_labor_productivity_sgna_jerk_126d_v065_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_126d_v065_signal},    "f12_labor_productivity_ebit_jerk_126d_v066_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_126d_v066_signal},    "f12_labor_productivity_revenue_jerk_126d_v067_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_126d_v067_signal},    "f12_labor_productivity_labor_leverage_jerk_126d_v068_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_126d_v068_signal},    "f12_labor_productivity_sgna_jerk_252d_v069_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_252d_v069_signal},    "f12_labor_productivity_ebit_jerk_252d_v070_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_252d_v070_signal},    "f12_labor_productivity_revenue_jerk_252d_v071_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_252d_v071_signal},    "f12_labor_productivity_labor_leverage_jerk_252d_v072_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_252d_v072_signal},    "f12_labor_productivity_sgna_jerk_504d_v073_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_504d_v073_signal},    "f12_labor_productivity_ebit_jerk_504d_v074_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_504d_v074_signal},    "f12_labor_productivity_revenue_jerk_504d_v075_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_504d_v075_signal},    "f12_labor_productivity_labor_leverage_jerk_504d_v076_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_504d_v076_signal},    "f12_labor_productivity_sgna_jerk_756d_v077_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_756d_v077_signal},    "f12_labor_productivity_ebit_jerk_756d_v078_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_756d_v078_signal},    "f12_labor_productivity_revenue_jerk_756d_v079_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_756d_v079_signal},    "f12_labor_productivity_labor_leverage_jerk_756d_v080_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_756d_v080_signal},    "f12_labor_productivity_sgna_jerk_1008d_v081_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_1008d_v081_signal},    "f12_labor_productivity_ebit_jerk_1008d_v082_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_1008d_v082_signal},    "f12_labor_productivity_revenue_jerk_1008d_v083_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_1008d_v083_signal},    "f12_labor_productivity_labor_leverage_jerk_1008d_v084_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_1008d_v084_signal},    "f12_labor_productivity_sgna_jerk_1260d_v085_signal": {"inputs": [], "func": f12_labor_productivity_sgna_jerk_1260d_v085_signal},    "f12_labor_productivity_ebit_jerk_1260d_v086_signal": {"inputs": [], "func": f12_labor_productivity_ebit_jerk_1260d_v086_signal},    "f12_labor_productivity_revenue_jerk_1260d_v087_signal": {"inputs": [], "func": f12_labor_productivity_revenue_jerk_1260d_v087_signal},    "f12_labor_productivity_labor_leverage_jerk_1260d_v088_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_jerk_1260d_v088_signal},    "f12_labor_productivity_sgna_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_5d_v089_signal},    "f12_labor_productivity_ebit_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_5d_v090_signal},    "f12_labor_productivity_revenue_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_5d_v091_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_5d_v092_signal},    "f12_labor_productivity_sgna_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_10d_v093_signal},    "f12_labor_productivity_ebit_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_10d_v094_signal},    "f12_labor_productivity_revenue_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_10d_v095_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_10d_v096_signal},    "f12_labor_productivity_sgna_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_21d_v097_signal},    "f12_labor_productivity_ebit_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_21d_v098_signal},    "f12_labor_productivity_revenue_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_21d_v099_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_21d_v100_signal},    "f12_labor_productivity_sgna_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_42d_v101_signal},    "f12_labor_productivity_ebit_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_42d_v102_signal},    "f12_labor_productivity_revenue_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_42d_v103_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_42d_v104_signal},    "f12_labor_productivity_sgna_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_63d_v105_signal},    "f12_labor_productivity_ebit_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_63d_v106_signal},    "f12_labor_productivity_revenue_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_63d_v107_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_63d_v108_signal},    "f12_labor_productivity_sgna_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_126d_v109_signal},    "f12_labor_productivity_ebit_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_126d_v110_signal},    "f12_labor_productivity_revenue_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_126d_v111_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_126d_v112_signal},    "f12_labor_productivity_sgna_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_252d_v113_signal},    "f12_labor_productivity_ebit_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_252d_v114_signal},    "f12_labor_productivity_revenue_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_252d_v115_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_252d_v116_signal},    "f12_labor_productivity_sgna_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_504d_v117_signal},    "f12_labor_productivity_ebit_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_504d_v118_signal},    "f12_labor_productivity_revenue_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_504d_v119_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_504d_v120_signal},    "f12_labor_productivity_sgna_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_756d_v121_signal},    "f12_labor_productivity_ebit_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_756d_v122_signal},    "f12_labor_productivity_revenue_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_756d_v123_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_756d_v124_signal},    "f12_labor_productivity_sgna_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_1008d_v125_signal},    "f12_labor_productivity_ebit_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_1008d_v126_signal},    "f12_labor_productivity_revenue_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_1008d_v127_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_1008d_v128_signal},    "f12_labor_productivity_sgna_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f12_labor_productivity_sgna_slope_diff_norm_1260d_v129_signal},    "f12_labor_productivity_ebit_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f12_labor_productivity_ebit_slope_diff_norm_1260d_v130_signal},    "f12_labor_productivity_revenue_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f12_labor_productivity_revenue_slope_diff_norm_1260d_v131_signal},    "f12_labor_productivity_labor_leverage_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_slope_diff_norm_1260d_v132_signal},    "f12_labor_productivity_sgna_mom_z_5d_v133_signal": {"inputs": [], "func": f12_labor_productivity_sgna_mom_z_5d_v133_signal},    "f12_labor_productivity_ebit_mom_z_5d_v134_signal": {"inputs": [], "func": f12_labor_productivity_ebit_mom_z_5d_v134_signal},    "f12_labor_productivity_revenue_mom_z_5d_v135_signal": {"inputs": [], "func": f12_labor_productivity_revenue_mom_z_5d_v135_signal},    "f12_labor_productivity_labor_leverage_mom_z_5d_v136_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_mom_z_5d_v136_signal},    "f12_labor_productivity_sgna_mom_z_10d_v137_signal": {"inputs": [], "func": f12_labor_productivity_sgna_mom_z_10d_v137_signal},    "f12_labor_productivity_ebit_mom_z_10d_v138_signal": {"inputs": [], "func": f12_labor_productivity_ebit_mom_z_10d_v138_signal},    "f12_labor_productivity_revenue_mom_z_10d_v139_signal": {"inputs": [], "func": f12_labor_productivity_revenue_mom_z_10d_v139_signal},    "f12_labor_productivity_labor_leverage_mom_z_10d_v140_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_mom_z_10d_v140_signal},    "f12_labor_productivity_sgna_mom_z_21d_v141_signal": {"inputs": [], "func": f12_labor_productivity_sgna_mom_z_21d_v141_signal},    "f12_labor_productivity_ebit_mom_z_21d_v142_signal": {"inputs": [], "func": f12_labor_productivity_ebit_mom_z_21d_v142_signal},    "f12_labor_productivity_revenue_mom_z_21d_v143_signal": {"inputs": [], "func": f12_labor_productivity_revenue_mom_z_21d_v143_signal},    "f12_labor_productivity_labor_leverage_mom_z_21d_v144_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_mom_z_21d_v144_signal},    "f12_labor_productivity_sgna_mom_z_42d_v145_signal": {"inputs": [], "func": f12_labor_productivity_sgna_mom_z_42d_v145_signal},    "f12_labor_productivity_ebit_mom_z_42d_v146_signal": {"inputs": [], "func": f12_labor_productivity_ebit_mom_z_42d_v146_signal},    "f12_labor_productivity_revenue_mom_z_42d_v147_signal": {"inputs": [], "func": f12_labor_productivity_revenue_mom_z_42d_v147_signal},    "f12_labor_productivity_labor_leverage_mom_z_42d_v148_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_mom_z_42d_v148_signal},    "f12_labor_productivity_sgna_mom_z_63d_v149_signal": {"inputs": [], "func": f12_labor_productivity_sgna_mom_z_63d_v149_signal},    "f12_labor_productivity_ebit_mom_z_63d_v150_signal": {"inputs": [], "func": f12_labor_productivity_ebit_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 12...")
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
